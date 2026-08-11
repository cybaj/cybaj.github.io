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


def check_ownership(target, item_id, force):
    """Refuse to overwrite a published file this item does not own.

    Every planned write passes through here — flat post, leaf and generated
    section page alike. A section page is published content like any other;
    exempting it let publishing destroy a hand-written `_index.md`, and let two
    `docs` items sharing a slug take over each other's sections, in silence.
    """
    if force or not target.exists():
        return
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


def read_source(source):
    """One editing file's (own front matter, body); ({}, "") for no file."""
    if source is None:
        return {}, ""
    return split_front_matter(source.read_text(encoding="utf-8"), source)


def plan_posts(item_dir, item_id, meta, langs, content_root):
    """Plan the flat post each language publishes.

    Planning reads and parses every source, so that a missing draft or a
    malformed one fails before the first file is written. A two-language item
    with one unfinished draft must fail without half-publishing the other.
    """
    writes = []
    for lang in langs:
        final = item_dir / "editing" / lang / "final.md"
        if not final.is_file():
            raise PublishError(
                f"no finished draft for language {lang!r}: expected {final}"
            )
        found, body = read_source(final)
        if found:
            print(
                f"warning: ignoring front matter in {final}; "
                "publish.md is the source of truth",
                file=sys.stderr,
            )
        writes.append(Write(
            source=final,
            target=content_root / LANG_DIRS[lang] / "posts" / f"{meta['slug']}.md",
            front=build_front_matter(meta, lang, item_id),
            body=body,
        ))
    return writes


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


def merge_section_front_matter(resolved, own, meta, item_id):
    """Front matter for one section page: resolved metadata over its own keys.

    `structure.md` outranks a hand-written `_index.md`: the section page's own
    front matter fills gaps only, since one place must decide the sidebar.
    """
    front = dict(resolved)
    for key, value in own.items():
        if key not in ("item", "title"):
            front.setdefault(key, value)
    front["date"] = front.get("date", meta["date"])
    front["item"] = item_id
    return front


def plan_docs(item_dir, item_id, meta, langs, content_root):
    """Plan every leaf and generated section page across the given languages.

    Planning reads and parses every source, so a malformed document fails
    before the first file is written — the `docs` path is the one that asks
    for hand-authored per-file front matter, so a YAML typo is routine.
    """
    overrides = hierarchy.load_structure(item_dir)
    structure_path = item_dir / "structure.md"
    hierarchy.validate_sections(
        overrides, section_union(item_dir, meta), structure_path
    )

    writes = []
    fallbacks = []
    for lang in langs:
        lang_dir = item_dir / "editing" / lang
        leaves, bodies, directories = (
            hierarchy.walk_editing_tree(lang_dir)
            if lang_dir.is_dir()
            else ([], {}, [""])
        )
        if not leaves:
            raise PublishError(
                f"no documents for language {lang!r}: expected at least one "
                f"document (a `.md` file other than `{SECTION_FILE}`) under "
                f"{lang_dir}"
            )
        root = docs_root(content_root, lang, meta["slug"])

        for rel in leaves:
            source = lang_dir / rel
            own, body = read_source(source)
            front, fell_back = merge_leaf_front_matter(
                meta, item_id, own, body, source
            )
            if fell_back:
                print(
                    f"warning: {source} has no title and no H1; using "
                    f"{front['title']!r} from the filename",
                    file=sys.stderr,
                )
            writes.append(
                Write(source=source, target=root / rel, front=front, body=body)
            )

        for section in directories:
            resolved, fell_back = hierarchy.resolve_section_meta(
                section, overrides, lang, meta["title"][lang], structure_path
            )
            if fell_back:
                fallbacks.append(section)
            body_rel = bodies.get(section)
            source = (lang_dir / body_rel) if body_rel else None
            own, body = read_source(source)
            writes.append(Write(
                source=source,
                target=(root / section / SECTION_FILE) if section else root / SECTION_FILE,
                front=merge_section_front_matter(resolved, own, meta, item_id),
                body=body,
            ))

    for section in sorted(set(fallbacks)):
        print(
            f"warning: section {section!r} has no title in structure.md; "
            f"using the directory name. On a bilingual site this shows "
            f"the same name in every language.",
            file=sys.stderr,
        )
    return writes


def write_all(planned):
    """Write every planned file. Formatting only — nothing here can fail.

    Every source has already been parsed and every target checked for
    ownership, so this loop cannot stop halfway and leave a partial publish.
    """
    for write in planned:
        write.target.parent.mkdir(parents=True, exist_ok=True)
        write.target.write_text(
            dump_front_matter(write.front, write.body), encoding="utf-8"
        )
    return [write.target for write in planned]


def expected_targets(item_dir, meta, content_root):
    """Every path this item would write, per language, regardless of --lang.

    Computed from `editing/`, not from what a run wrote, so publishing one
    language never makes the other language's files look orphaned.

    Generated section pages MUST be included. They derive from directories
    rather than from editing files, so collecting only `editing/**/*.md` would
    omit every `_index.md` and flag each one as an orphan on the next publish.
    """
    expected = {lang: set() for lang in LANG_DIRS}
    if item_target(meta) != "docs":
        for lang in meta["languages"]:
            expected[lang].add(
                content_root / LANG_DIRS[lang] / "posts" / f"{meta['slug']}.md"
            )
        return expected

    for lang in meta["languages"]:
        lang_dir = item_dir / "editing" / lang
        if not lang_dir.is_dir():
            continue
        leaves, _, directories = hierarchy.walk_editing_tree(lang_dir)
        root = docs_root(content_root, lang, meta["slug"])
        for rel in leaves:
            expected[lang].add(root / rel)
        for section in directories:
            expected[lang].add(
                (root / section / SECTION_FILE) if section else root / SECTION_FILE
            )
    return expected


def find_orphans(item_id, item_dir, meta, content_root):
    """Published files still marked as this item's that no longer belong.

    Renaming an item's slug, dropping a language from `languages`, deleting a
    page from a tree, or switching `target` all leave previously published
    files in `content/` where they keep deploying.

    Both `posts/` and `docs/` are scanned regardless of the item's current
    target, since an item that switched target is exactly the case a
    target-only scan would miss. A file counts as current whenever its
    language is still declared and its path is one this item would write —
    whether or not this run rewrote it. Publishing one language of a
    multi-language item is a supported workflow, so "not written this run"
    must never mean "orphan".
    """
    declared = set(meta["languages"])
    expected = expected_targets(item_dir, meta, content_root)
    orphans = []
    for lang, dir_name in LANG_DIRS.items():
        for area in ("posts", "docs"):
            root = content_root / dir_name / area
            if not root.is_dir():
                continue
            for path in sorted(root.rglob("*.md")):
                try:
                    existing, _ = split_front_matter(
                        path.read_text(encoding="utf-8"), path
                    )
                except (FrontMatterError, UnicodeDecodeError):
                    continue  # not ours to judge; publishing already succeeded
                if existing.get("item") != item_id:
                    continue
                if lang not in declared:
                    orphans.append(
                        (path, f"language {lang!r} is no longer declared")
                    )
                elif path not in expected[lang]:
                    # Preserve the original, more specific posts-target
                    # message (it names the new slug) for the case that
                    # already shipped in Task 1-3's regression tests; trees,
                    # and an item that switched target away from posts, get
                    # the general reason since no single field explains them.
                    if area == "posts" and item_target(meta) != "docs":
                        reason = f"the slug is now {meta['slug']!r}"
                    else:
                        reason = "this item no longer publishes that path"
                    orphans.append((path, reason))
    return orphans


def warn_orphans(item_id, item_dir, meta, content_root):
    """Report orphaned published files on stderr. Never fails the publish."""
    for path, reason in find_orphans(item_id, item_dir, meta, content_root):
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
            planned = plan_docs(item_dir, args.item_id, meta, langs, content_root)
        else:
            if (item_dir / "structure.md").is_file():
                print(
                    f"warning: {item_dir / 'structure.md'} is ignored because "
                    "this item's target is posts, not docs",
                    file=sys.stderr,
                )
            planned = plan_posts(item_dir, args.item_id, meta, langs, content_root)
        # One gate over every planned target, leaf and section alike, after
        # both planners and before any write.
        for write in planned:
            check_ownership(write.target, args.item_id, args.force)
        written = write_all(planned)
    except (PublishError, FrontMatterError, HierarchyError) as exc:
        sys.exit(f"error: {exc}")

    for target in written:
        print(f"published {target}")
    warn_orphans(args.item_id, item_dir, meta, content_root)
    print("next: set stage to published in state.md, then commit and push")
    return 0


if __name__ == "__main__":
    sys.exit(main())
