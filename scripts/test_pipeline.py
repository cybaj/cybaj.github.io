#!/usr/bin/env python3
"""End-to-end tests for the writing pipeline scripts."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NEW_ITEM = REPO / "scripts" / "new_item.py"
PUBLISH = REPO / "scripts" / "publish.py"


def run(script, *args):
    """Run a pipeline script, returning the completed process."""
    return subprocess.run(
        [sys.executable, str(script), *map(str, args)],
        capture_output=True,
        text=True,
    )


class PipelineTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        shutil.copytree(
            REPO / "writing" / "TEMPLATES", self.tmp / "writing" / "TEMPLATES"
        )
        for lang_dir in ("korean", "english"):
            (self.tmp / "content" / lang_dir / "posts").mkdir(parents=True)

    def new(self, tag, langs="ko", date="2026-08-10"):
        return run(
            NEW_ITEM, tag, "--lang", langs, "--date", date, "--root", self.tmp
        )

    def item_dir(self, item_id):
        return self.tmp / "writing" / "items" / item_id


class NewItemTest(PipelineTest):
    def test_creates_expected_tree(self):
        result = self.new("hugo-pipeline", langs="ko,en")
        self.assertEqual(result.returncode, 0, result.stderr)

        item = self.item_dir("2026-08-10-hugo-pipeline")
        for name in ("planning.md", "state.md", "publish.md", "manner.md"):
            self.assertTrue((item / name).is_file(), f"missing {name}")
        for lang in ("ko", "en"):
            self.assertTrue((item / "docs" / lang).is_dir())
            self.assertTrue((item / "editing" / lang).is_dir())
        for sub in ("sources", "references"):
            self.assertTrue((item / sub / ".gitkeep").is_file())

    def test_renders_every_placeholder(self):
        self.new("hugo-pipeline", langs="ko,en")
        item = self.item_dir("2026-08-10-hugo-pipeline")
        for name in ("planning.md", "state.md", "publish.md", "manner.md"):
            text = (item / name).read_text(encoding="utf-8")
            self.assertNotIn("{{", text, f"unrendered placeholder in {name}")

    def test_publish_template_declares_languages_and_titles(self):
        self.new("hugo-pipeline", langs="ko,en")
        text = (
            self.item_dir("2026-08-10-hugo-pipeline") / "publish.md"
        ).read_text(encoding="utf-8")
        self.assertIn("slug: hugo-pipeline", text)
        self.assertIn("languages: [ko, en]", text)
        self.assertIn('ko: ""', text)
        self.assertIn('en: ""', text)

    def test_state_template_lists_each_language(self):
        self.new("hugo-pipeline", langs="ko,en")
        text = (
            self.item_dir("2026-08-10-hugo-pipeline") / "state.md"
        ).read_text(encoding="utf-8")
        self.assertIn("  ko: not-started", text)
        self.assertIn("  en: not-started", text)

    def test_refuses_duplicate_item(self):
        self.assertEqual(self.new("hugo-pipeline").returncode, 0)
        result = self.new("hugo-pipeline")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("already exists", result.stderr)

    def test_rejects_invalid_tag(self):
        result = self.new("Hugo Pipeline")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid tag", result.stderr)

    def test_rejects_unknown_language(self):
        result = self.new("hugo-pipeline", langs="ko,fr")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown language", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
