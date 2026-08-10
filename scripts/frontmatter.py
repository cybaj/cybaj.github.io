#!/usr/bin/env python3
"""Read and write YAML front matter."""

from __future__ import annotations

import sys

try:
    import yaml
except ImportError:  # pragma: no cover - environment problem, not logic
    sys.exit(
        "error: PyYAML is required. Install it with: python3 -m pip install pyyaml"
    )


class FrontMatterError(Exception):
    """Front matter the author can fix, reported without a traceback."""


def split_front_matter(text, source=None):
    """Return (metadata, body). Text without front matter yields ({}, text).

    `source` is the path the text came from, used only to name the file in the
    error message when the YAML is malformed — hand-editing front matter is the
    most likely way to break an item, and a raw ScannerError helps nobody.
    """
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        where = f" in {source}" if source else ""
        said = [
            part
            for part in (getattr(exc, "context", None), getattr(exc, "problem", None))
            if part
        ]
        detail = ", ".join(said) or " ".join(str(exc).split())
        mark = getattr(exc, "problem_mark", None)
        if mark is not None:
            # parts[1] starts with the newline that ended the opening `---`, so
            # PyYAML's line numbers already match the file's.
            detail += f" (line {mark.line + 1}, column {mark.column + 1})"
        raise FrontMatterError(
            f"malformed YAML front matter{where}: {detail}"
        ) from None
    if not isinstance(meta, dict):
        # A scalar or list parse means those dashes were not front matter at
        # all — a body opening with a horizontal rule, say. Treating it as
        # metadata would silently discard everything before the second `---`.
        return {}, text
    return meta, parts[2].lstrip("\n")


def dump_front_matter(meta, body):
    """Render metadata and body as one front-mattered document."""
    front = yaml.safe_dump(
        meta, allow_unicode=True, sort_keys=False, default_flow_style=False
    )
    return f"---\n{front}---\n\n{body}"
