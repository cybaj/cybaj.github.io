#!/usr/bin/env python3
"""Publish an item's finished drafts into the Hugo content tree."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from frontmatter import (  # noqa: E402
    FrontMatterError,
    dump_front_matter,
    split_front_matter,
)
import hierarchy  # noqa: E402
from hierarchy import HierarchyError, SECTION_FILE, Write  # noqa: E402

# SLUG_RE and the language table are deliberately duplicated in new_item.py:
# that script must run without PyYAML, so it cannot import from frontmatter.py
# or from here. Do not "fix" the duplication by extracting a shared module.
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LANG_DIRS = {"ko": "korean", "en": "english"}
REQUIRED = ("slug", "languages", "date", "title")
OPTIONAL = ("tags", "categories", "author", "draft")
TARGETS = ("posts", "docs")


class PublishError(Exception):
    """A problem the author can fix, reported without a traceback."""


def load_item(item_dir):
    """Read and validate an item's publish.md."""
    if not item_dir.is_dir():
        raise PublishError(f"item not found: {item_dir}")
    publish_md = item_dir / "publish.md"
    if not publish_md.is_file():
        raise PublishError(f"missing publish.md: {publish_md}")

    meta, _ = split_front_matter(publish_md.read_text(encoding="utf-8"), publish_md)
    missing = [field for field in REQUIRED if field not in meta]
    if missing:
        raise PublishError(
            f"publish.md is missing required field(s): {', '.join(missing)}"
        )
    if not SLUG_RE.match(str(meta["slug"])):
        raise PublishError(
            f"invalid slug {meta['slug']!r}: must match {SLUG_RE.pattern}"
        )

    langs = list(meta["languages"] or [])
    if not langs:
        raise PublishError("publish.md declares no languages")
    unknown = [lang for lang in langs if lang not in LANG_DIRS]
    if unknown:
        raise PublishError(
            f"unknown language(s): {', '.join(unknown)}; "
            f"known: {', '.join(LANG_DIRS)}"
        )
    titles = meta["title"] or {}
    if not isinstance(titles, dict):
        raise PublishError(
            "publish.md title must map each declared language to a title "
            '(title:, then an indented `ko: "..."` line per language), '
            f"not a bare {type(titles).__name__}"
        )
    for lang in langs:
        if not titles.get(lang):
            raise PublishError(
                f"publish.md title has no non-empty entry for declared "
                f"language {lang!r}"
            )
    target = meta.get("target", "posts")
    if target not in TARGETS:
        raise PublishError(
            f"unknown target {target!r}: expected one of {', '.join(TARGETS)}"
        )
    return meta


def item_target(meta):
    """The publish destination kind for this item; `posts` when unset."""
    return meta.get("target", "posts")


def docs_root(content_root, lang, slug):
    """The subtree root for one language, e.g. content/korean/docs/{slug}."""
    return content_root / LANG_DIRS[lang] / "docs" / slug


def build_front_matter(meta, lang, item_id):
    """Assemble the Hugo front matter for one language."""
    front = {"title": meta["title"][lang], "date": meta["date"]}
    for field in OPTIONAL:
        if field in meta:
            front[field] = meta[field]
    front["item"] = item_id
    return front


def leaf_title(own, body, source):
    """A leaf's title: its own, else the first H1, else the filename stem.

    Deriving from the H1 matches hugo-book itself — several pages in the
    archived demo carry no front matter and take their title from the heading.
    Returns (title, fell_back_to_filename).
    """
    if own.get("title"):
        return own["title"], False
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip(), False
    return source.stem, True


def merge_leaf_front_matter(meta, item_id, own, body, source):
    """Front matter for one leaf: its own, over item defaults, plus the marker.

    Returns (front, fell_back_to_filename). The leaf wins over item defaults —
    publish.md supplies item-wide values, not every field — and the item marker
    always wins over the leaf, because the orphan check depends on it.
    """
    title, fell_back = leaf_title(own, body, source)
    # title and date lead so the generated front matter reads in a stable
    # order; sort_keys=False preserves insertion order.
    front = {"title": title, "date": meta["date"]}
    for field in OPTIONAL:
        if field in meta:
            front[field] = meta[field]
    for key, value in own.items():
        if key != "item":
            front[key] = value
    # Re-assert both after the leaf's own keys: `title` because leaf_title has
    # already resolved it, and `item` because a leaf must never forge it.
    front["title"] = title
    front["item"] = item_id
    return front, fell_back


def resolve_language(item_dir, item_id, meta, lang, content_root, force):
    """Validate one language, returning the (source, target) pair to write.

    Validation is separated from writing so that every language can be checked
    before any file is written. A two-language item with one unfinished draft
    must fail without half-publishing the other.
    """
    final = item_dir / "editing" / lang / "final.md"
    if not final.is_file():
        raise PublishError(
            f"no finished draft for language {lang!r}: expected {final}"
        )

    target = content_root / LANG_DIRS[lang] / "posts" / f"{meta['slug']}.md"
    if target.exists() and not force:
        existing, _ = split_front_matter(target.read_text(encoding="utf-8"), target)
        owner = existing.get("item")
        if owner is None:
            raise PublishError(
                f"{target} was not produced by this pipeline "
                "(it carries no item marker, so it is hand-written content); "
                "refusing to overwrite. Pass --force to replace it."
            )
        if owner != item_id:
            raise PublishError(
                f"{target} already belongs to a different item ({owner!r}); "
                "refusing to overwrite. Change this item's slug, or pass "
                "--force to take the slug over."
            )
    return final, target


def write_language(meta, lang, item_id, final, target):
    """Write one validated language into the content tree."""
    found, body = split_front_matter(final.read_text(encoding="utf-8"), final)
    if found:
        print(
            f"warning: ignoring front matter in {final}; "
            "publish.md is the source of truth",
            file=sys.stderr,
        )

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        dump_front_matter(build_front_matter(meta, lang, item_id), body),
        encoding="utf-8",
    )
    return target


def section_union(item_dir, meta):
    """Every section path across all declared languages.

    Sections are validated against the union, never per language: an item
    mid-translation legitimately has `advanced/` in Korean before English, and
    a per-language check would reject a section that is perfectly valid. All
    declared languages are walked even when --lang narrows the publish, so the
    union does not shrink with the selection.
    """
    union = set()
    for lang in meta["languages"]:
        lang_dir = item_dir / "editing" / lang
        if lang_dir.is_dir():
            _, _, directories = hierarchy.walk_editing_tree(lang_dir)
            union.update(directories)
    return sorted(union)


def resolve_docs_language(item_dir, item_id, meta, lang, content_root, force):
    """Validate one language's subtree, returning the writes it implies.

    Section pages are added by `plan_sections`; this returns leaves only.
    """
    lang_dir = item_dir / "editing" / lang
    leaves, _, _ = (
        hierarchy.walk_editing_tree(lang_dir) if lang_dir.is_dir() else ([], {}, [""])
    )
    if not leaves:
        raise PublishError(
            f"no documents for language {lang!r}: expected at least one .md "
            f"file under {lang_dir}"
        )

    root = docs_root(content_root, lang, meta["slug"])
    writes = []
    for rel in leaves:
        target = root / rel
        if target.exists() and not force:
            existing, _ = split_front_matter(
                target.read_text(encoding="utf-8"), target
            )
            owner = existing.get("item")
            if owner is None:
                raise PublishError(
                    f"{target} was not produced by this pipeline "
                    "(it carries no item marker, so it is hand-written content); "
                    "refusing to overwrite. Pass --force to replace it."
                )
            if owner != item_id:
                raise PublishError(
                    f"{target} already belongs to a different item ({owner!r}); "
                    "refusing to overwrite. Change this item's slug, or pass "
                    "--force to take the slug over."
                )
        writes.append(Write(source=lang_dir / rel, target=target, front=None))
    return writes


def plan_sections(item_dir, meta, lang, content_root, overrides):
    """Generated section pages for one language, and which titles fell back."""
    lang_dir = item_dir / "editing" / lang
    _, bodies, directories = hierarchy.walk_editing_tree(lang_dir)
    root = docs_root(content_root, lang, meta["slug"])
    structure_path = item_dir / "structure.md"

    writes = []
    fallbacks = []
    for section in directories:
        front, fell_back = hierarchy.resolve_section_meta(
            section, overrides, lang, meta["title"][lang], structure_path
        )
        if fell_back:
            fallbacks.append(section)
        body_rel = bodies.get(section)
        writes.append(Write(
            source=(lang_dir / body_rel) if body_rel else None,
            target=(root / section / SECTION_FILE) if section else root / SECTION_FILE,
            front=front,
        ))
    return writes, fallbacks


def write_docs(meta, item_id, write):
    """Write one planned file — leaf or generated section — into content/."""
    body = ""
    own = {}
    if write.source is not None:
        own, body = split_front_matter(
            write.source.read_text(encoding="utf-8"), write.source
        )
    if write.front is None:
        front, fell_back = merge_leaf_front_matter(
            meta, item_id, own, body, write.source
        )
        if fell_back:
            print(
                f"warning: {write.source} has no title and no H1; using "
                f"{front['title']!r} from the filename",
                file=sys.stderr,
            )
    else:
        front = dict(write.front)
        for key, value in own.items():
            if key not in ("item", "title"):
                front.setdefault(key, value)
        front["date"] = front.get("date", meta["date"])
        front["item"] = item_id

    write.target.parent.mkdir(parents=True, exist_ok=True)
    write.target.write_text(dump_front_matter(front, body), encoding="utf-8")
    return write.target


def find_orphans(item_id, meta, content_root):
    """Published files still marked as this item's that no longer belong.

    Renaming an item's slug, or dropping a language from `languages`, leaves
    the previously published file in `content/` where it keeps deploying.

    Both language directories are scanned regardless of what the item declares
    now, since a dropped language is exactly the case a declared-only scan
    would miss. A file counts as current whenever its language is still
    declared and its path is the one the current slug maps to — whether or not
    this run rewrote it. Publishing one language of a two-language item is a
    supported workflow, so "not written this run" must never mean "orphan".
    """
    declared = set(meta["languages"])
    orphans = []
    for lang, dir_name in LANG_DIRS.items():
        posts = content_root / dir_name / "posts"
        if not posts.is_dir():
            continue
        expected = posts / f"{meta['slug']}.md"
        for path in sorted(posts.glob("*.md")):
            try:
                existing, _ = split_front_matter(
                    path.read_text(encoding="utf-8"), path
                )
            except (FrontMatterError, UnicodeDecodeError):
                continue  # not ours to judge; publishing already succeeded
            if existing.get("item") != item_id:
                continue
            if lang not in declared:
                orphans.append((path, f"language {lang!r} is no longer declared"))
            elif path != expected:
                orphans.append((path, f"the slug is now {meta['slug']!r}"))
    return orphans


def warn_orphans(item_id, meta, content_root):
    """Report orphaned published files on stderr. Never fails the publish."""
    for path, reason in find_orphans(item_id, meta, content_root):
        print(
            f"warning: {path} still carries this item's marker but "
            f"{reason}; publish no longer writes it. Delete it by hand if it "
            "should no longer be on the site.",
            file=sys.stderr,
        )


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Publish an item's finished drafts into the Hugo content tree."
    )
    parser.add_argument("item_id", help="item directory name, e.g. 2026-08-10-hugo-pipeline")
    parser.add_argument("--lang", help="publish only this language")
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite content not produced by this pipeline",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="repository root (default: parent of scripts/)",
    )
    args = parser.parse_args(argv)

    item_dir = args.root / "writing" / "items" / args.item_id
    try:
        meta = load_item(item_dir)
        langs = list(meta["languages"])
        if args.lang:
            if args.lang not in langs:
                raise PublishError(
                    f"language {args.lang!r} is not declared by this item; "
                    f"declared: {', '.join(langs)}"
                )
            langs = [args.lang]
        content_root = args.root / "content"
        if item_target(meta) == "docs":
            overrides = hierarchy.load_structure(item_dir)
            hierarchy.validate_sections(
                overrides, section_union(item_dir, meta), item_dir / "structure.md"
            )
            planned = []
            fallbacks = []
            for lang in langs:
                planned.extend(resolve_docs_language(
                    item_dir, args.item_id, meta, lang, content_root, args.force,
                ))
                section_writes, fell_back = plan_sections(
                    item_dir, meta, lang, content_root, overrides
                )
                planned.extend(section_writes)
                fallbacks.extend(fell_back)
            written = [write_docs(meta, args.item_id, w) for w in planned]
            for section in sorted(set(fallbacks)):
                print(
                    f"warning: section {section!r} has no title in structure.md; "
                    f"using the directory name. On a bilingual site this shows "
                    f"the same name in every language.",
                    file=sys.stderr,
                )
        else:
            if (item_dir / "structure.md").is_file():
                print(
                    f"warning: {item_dir / 'structure.md'} is ignored because "
                    "this item's target is posts, not docs",
                    file=sys.stderr,
                )
            posts_planned = [
                (lang, *resolve_language(
                    item_dir, args.item_id, meta, lang, content_root, args.force
                ))
                for lang in langs
            ]
            written = [
                write_language(meta, lang, args.item_id, final, target)
                for lang, final, target in posts_planned
            ]
    except (PublishError, FrontMatterError, HierarchyError) as exc:
        sys.exit(f"error: {exc}")

    for target in written:
        print(f"published {target}")
    warn_orphans(args.item_id, meta, content_root)
    print("next: set stage to published in state.md, then commit and push")
    return 0


if __name__ == "__main__":
    sys.exit(main())
