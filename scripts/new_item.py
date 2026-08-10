#!/usr/bin/env python3
"""Scaffold a new writing item from writing/TEMPLATES/."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
KNOWN_LANGS = ("ko", "en")
TEMPLATE_FILES = ("planning.md", "state.md", "publish.md", "manner.md")


class ItemError(Exception):
    """A problem the author can fix, reported without a traceback."""


def render(text, item_id, date, tag, langs):
    """Substitute the six template placeholders.

    The slug defaults to the tag, so `{{SLUG}}` covers both; there is no
    separate `{{TAG}}` token.
    """
    language_states = "\n".join(f"  {lang}: not-started" for lang in langs)
    title_entries = "\n".join(f'  {lang}: ""' for lang in langs)
    return (
        text.replace("{{ITEM_ID}}", item_id)
        .replace("{{DATE}}", date)
        .replace("{{SLUG}}", tag)
        .replace("{{LANGUAGES}}", ", ".join(langs))
        .replace("{{LANGUAGE_STATES}}", language_states)
        .replace("{{TITLE_ENTRIES}}", title_entries)
    )


def create_item(root, tag, date, langs):
    if not SLUG_RE.match(tag):
        raise ItemError(
            f"invalid tag {tag!r}: must match {SLUG_RE.pattern} "
            "(it is also the default publish slug)"
        )
    unknown = [lang for lang in langs if lang not in KNOWN_LANGS]
    if unknown:
        raise ItemError(
            f"unknown language(s): {', '.join(unknown)}; "
            f"known: {', '.join(KNOWN_LANGS)}"
        )

    item_id = f"{date}-{tag}"
    item_dir = root / "writing" / "items" / item_id
    if item_dir.exists():
        raise ItemError(f"item already exists: {item_dir}")

    templates = root / "writing" / "TEMPLATES"
    rendered = {}
    for name in TEMPLATE_FILES:
        src = templates / name
        if not src.is_file():
            raise ItemError(f"missing template: {src}")
        rendered[name] = render(
            src.read_text(encoding="utf-8"), item_id, date, tag, langs
        )

    for lang in langs:
        (item_dir / "docs" / lang).mkdir(parents=True)
        (item_dir / "editing" / lang).mkdir(parents=True)
    for sub in ("sources", "references"):
        (item_dir / sub).mkdir(parents=True)
        (item_dir / sub / ".gitkeep").touch()
    for name, text in rendered.items():
        (item_dir / name).write_text(text, encoding="utf-8")

    return item_dir


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Scaffold a new writing item from writing/TEMPLATES/."
    )
    parser.add_argument("tag", help="short kebab-case topic tag, also the default slug")
    parser.add_argument(
        "--lang",
        default="ko",
        help="comma-separated languages this item targets (default: ko)",
    )
    parser.add_argument(
        "--date", default=None, help="item date, YYYY-MM-DD (default: today)"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="repository root (default: parent of scripts/)",
    )
    args = parser.parse_args(argv)

    date = args.date or dt.date.today().isoformat()
    try:
        dt.date.fromisoformat(date)
    except ValueError:
        sys.exit(f"error: invalid date {date!r}: expected YYYY-MM-DD")

    langs = [lang.strip() for lang in args.lang.split(",") if lang.strip()]
    if not langs:
        sys.exit("error: --lang must name at least one language")

    try:
        item_dir = create_item(args.root, args.tag, date, langs)
    except ItemError as exc:
        sys.exit(f"error: {exc}")

    print(f"created {item_dir}")
    print("next: fill in planning.md and manner.md, then set stage in state.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
