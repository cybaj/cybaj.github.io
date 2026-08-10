#!/usr/bin/env python3
"""Publish an item's finished drafts into the Hugo content tree."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from frontmatter import dump_front_matter, split_front_matter  # noqa: E402

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LANG_DIRS = {"ko": "korean", "en": "english"}
REQUIRED = ("slug", "languages", "date", "title")
OPTIONAL = ("tags", "categories", "author", "draft")


class PublishError(Exception):
    """A problem the author can fix, reported without a traceback."""


def load_item(item_dir):
    """Read and validate an item's publish.md."""
    if not item_dir.is_dir():
        raise PublishError(f"item not found: {item_dir}")
    publish_md = item_dir / "publish.md"
    if not publish_md.is_file():
        raise PublishError(f"missing publish.md: {publish_md}")

    meta, _ = split_front_matter(publish_md.read_text(encoding="utf-8"))
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
    for lang in langs:
        if not titles.get(lang):
            raise PublishError(
                f"publish.md title has no non-empty entry for declared "
                f"language {lang!r}"
            )
    return meta


def build_front_matter(meta, lang, item_id):
    """Assemble the Hugo front matter for one language."""
    front = {"title": meta["title"][lang], "date": meta["date"]}
    for field in OPTIONAL:
        if field in meta:
            front[field] = meta[field]
    front["item"] = item_id
    return front


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
        existing, _ = split_front_matter(target.read_text(encoding="utf-8"))
        if existing.get("item") != item_id:
            raise PublishError(
                f"{target} was not produced by this pipeline "
                f"(item marker: {existing.get('item')!r}); "
                "refusing to overwrite. Pass --force to replace it."
            )
    return final, target


def write_language(meta, lang, item_id, final, target):
    """Write one validated language into the content tree."""
    found, body = split_front_matter(final.read_text(encoding="utf-8"))
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
        planned = [
            (lang, *resolve_language(
                item_dir, args.item_id, meta, lang, content_root, args.force
            ))
            for lang in langs
        ]
        written = [
            write_language(meta, lang, args.item_id, final, target)
            for lang, final, target in planned
        ]
    except PublishError as exc:
        sys.exit(f"error: {exc}")

    for target in written:
        print(f"published {target}")
    print("next: set stage to published in state.md, then commit and push")
    return 0


if __name__ == "__main__":
    sys.exit(main())
