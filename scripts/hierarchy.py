#!/usr/bin/env python3
"""Tree shape for document-hierarchy items.

Directories under `editing/{lang}/` are the source of truth for the shape of a
published subtree — nothing enumerates documents a second time. This module
turns that directory tree into the paths publish.py writes, and resolves the
metadata for each generated section page.
"""

from __future__ import annotations

import sys
from collections import namedtuple
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from frontmatter import split_front_matter  # noqa: E402

SECTION_FILE = "_index.md"

# One file publish.py will write. `source` is the editing file to take a body
# from, or None for a generated section page with no body. `front` carries
# resolved section metadata for section pages, and is None for leaves, whose
# front matter is merged from the file itself at write time.
Write = namedtuple("Write", "source target front")


class HierarchyError(Exception):
    """A problem the author can fix, reported without a traceback."""


def load_structure(item_dir):
    """Read structure.md's section overrides. An absent file means none."""
    path = item_dir / "structure.md"
    if not path.is_file():
        return {}
    meta, _ = split_front_matter(path.read_text(encoding="utf-8"), path)
    sections = meta.get("sections") or {}
    if not isinstance(sections, dict):
        raise HierarchyError(
            f"{path}: sections must be a map of section path to its settings, "
            f"not a bare {type(sections).__name__}"
        )
    resolved = {}
    for key, value in sections.items():
        section = str(key)
        value = value or {}
        if not isinstance(value, dict):
            raise HierarchyError(
                f"{path}: section {section!r} must be a map of settings "
                f"(title, weight, or a theme flag), not a bare "
                f"{type(value).__name__}"
            )
        resolved[section] = value
    return resolved


def walk_editing_tree(lang_dir):
    """Split one language's editing tree into leaves, section bodies, sections.

    Returns (leaves, section_bodies, directories):
      leaves         — relative paths of documents, excluding _index.md
      section_bodies — {section path: relative path of that section's _index.md}
      directories    — every section path, sorted, with "" for the root
    """
    leaves = []
    section_bodies = {}
    directories = {""}
    for path in sorted(lang_dir.rglob("*.md")):
        rel = path.relative_to(lang_dir)
        parts = rel.parent.parts
        section = "/".join(parts)
        directories.add(section)
        for depth in range(1, len(parts)):
            directories.add("/".join(parts[:depth]))
        if rel.name == SECTION_FILE:
            section_bodies[section] = rel
        else:
            leaves.append(rel)
    return leaves, section_bodies, sorted(directories)


def validate_sections(overrides, directories, structure_path):
    """Every declared section must correspond to a real directory."""
    known = set(directories)
    unknown = sorted(section for section in overrides if section not in known)
    if unknown:
        listed = ", ".join(repr(section) for section in unknown)
        available = ", ".join(repr(section) for section in sorted(known))
        raise HierarchyError(
            f"{structure_path}: section(s) {listed} have no matching directory "
            f"under editing/; directories present: {available}"
        )


def resolve_section_meta(section, overrides, lang, item_title, structure_path):
    """Front matter for one generated section page, and whether it fell back.

    Title resolution: the override, then the item title for the root, then the
    directory's own name. The last case sets the fallback flag so publish can
    warn — on a bilingual site an undeclared section would otherwise appear in
    the sidebar under an English directory name, silently.
    """
    entry = overrides.get(section, {})
    declared = entry.get("title")
    title = None
    if isinstance(declared, dict):
        title = declared.get(lang)
    elif declared is not None:
        raise HierarchyError(
            f"{structure_path}: section {section or '(root)'!r} title must map "
            f"each language to a string (title:, then an indented `ko: \"...\"` "
            f"line), not a bare {type(declared).__name__}"
        )

    fell_back = False
    if not title:
        if section == "":
            title = item_title
        else:
            title = section.rsplit("/", 1)[-1]
            fell_back = True

    front = {"title": title}
    if "weight" in entry:
        front["weight"] = entry["weight"]
    for key, value in entry.items():
        if key not in ("title", "weight"):
            front[key] = value
    return front, fell_back
