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


def split_front_matter(text):
    """Return (metadata, body). Text without front matter yields ({}, text)."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    return yaml.safe_load(parts[1]) or {}, parts[2].lstrip("\n")


def dump_front_matter(meta, body):
    """Render metadata and body as one front-mattered document."""
    front = yaml.safe_dump(
        meta, allow_unicode=True, sort_keys=False, default_flow_style=False
    )
    return f"---\n{front}---\n\n{body}"
