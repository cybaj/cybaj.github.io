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


class PublishTest(PipelineTest):
    ITEM = "2026-08-10-hugo-pipeline"

    def prepare(self, langs="ko", titles=None, bodies=None):
        """Scaffold an item and fill in what publishing requires."""
        self.new("hugo-pipeline", langs=langs)
        lang_list = langs.split(",")
        titles = titles or {"ko": "한국어 제목", "en": "English Title"}
        bodies = bodies or {lang: f"# body {lang}\n" for lang in lang_list}

        title_block = "\n".join(f'  {l}: "{titles[l]}"' for l in lang_list)
        (self.item_dir(self.ITEM) / "publish.md").write_text(
            "---\n"
            "slug: hugo-pipeline\n"
            f"languages: [{', '.join(lang_list)}]\n"
            "date: 2026-08-10\n"
            "tags: [hugo, blogging]\n"
            "title:\n"
            f"{title_block}\n"
            "---\n\n## Publish notes\n",
            encoding="utf-8",
        )
        for lang in lang_list:
            if lang in bodies:
                (self.item_dir(self.ITEM) / "editing" / lang / "final.md").write_text(
                    bodies[lang], encoding="utf-8"
                )

    def publish(self, *extra):
        return run(PUBLISH, self.ITEM, "--root", self.tmp, *extra)

    def published(self, lang_dir):
        return self.tmp / "content" / lang_dir / "posts" / "hugo-pipeline.md"

    def test_publishes_single_language(self):
        self.prepare(langs="ko")
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)

        text = self.published("korean").read_text(encoding="utf-8")
        self.assertIn("한국어 제목", text)
        self.assertIn("item: 2026-08-10-hugo-pipeline", text)
        self.assertIn("# body ko", text)
        self.assertFalse(self.published("english").exists())

    def test_does_not_escape_korean(self):
        self.prepare(langs="ko")
        self.publish()
        text = self.published("korean").read_text(encoding="utf-8")
        self.assertNotIn("\\u", text)

    def test_publishes_both_languages(self):
        self.prepare(langs="ko,en")
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("한국어 제목", self.published("korean").read_text(encoding="utf-8"))
        self.assertIn("English Title", self.published("english").read_text(encoding="utf-8"))

    def test_is_idempotent(self):
        self.prepare(langs="ko")
        self.publish()
        first = self.published("korean").read_text(encoding="utf-8")
        self.publish()
        self.assertEqual(first, self.published("korean").read_text(encoding="utf-8"))

    def test_missing_final_names_the_language(self):
        self.prepare(langs="ko,en", bodies={"ko": "# body ko\n"})
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("'en'", result.stderr)

    def test_partial_failure_writes_nothing(self):
        """A half-publishable item must not half-publish.

        The returncode assertion matters: without it this test cannot tell
        a correct refusal from a publish.py that silently did nothing.
        """
        self.prepare(langs="ko,en", bodies={"ko": "# body ko\n"})
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.published("korean").exists())
        self.assertFalse(self.published("english").exists())

    def test_missing_required_field_fails(self):
        self.prepare(langs="ko")
        (self.item_dir(self.ITEM) / "publish.md").write_text(
            "---\nlanguages: [ko]\ndate: 2026-08-10\ntitle:\n  ko: \"제목\"\n---\n",
            encoding="utf-8",
        )
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("slug", result.stderr)

    def test_unfilled_title_fails(self):
        self.prepare(langs="ko", titles={"ko": ""})
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("title", result.stderr)

    def test_invalid_slug_fails(self):
        self.prepare(langs="ko")
        path = self.item_dir(self.ITEM) / "publish.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "slug: hugo-pipeline", "slug: Hugo Pipeline"
            ),
            encoding="utf-8",
        )
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("slug", result.stderr)

    def test_undeclared_language_fails(self):
        self.prepare(langs="ko")
        result = self.publish("--lang", "en")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not declared", result.stderr)

    def test_missing_item_fails(self):
        result = run(PUBLISH, "2026-01-01-nope", "--root", self.tmp)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("item not found", result.stderr)

    def test_refuses_to_clobber_handwritten_content(self):
        self.prepare(langs="ko")
        self.published("korean").write_text(
            "---\ntitle: 손으로 쓴 글\n---\n\nbody\n", encoding="utf-8"
        )
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not produced by this pipeline", result.stderr)
        self.assertIn("손으로 쓴 글", self.published("korean").read_text(encoding="utf-8"))

    def test_force_overwrites_handwritten_content(self):
        self.prepare(langs="ko")
        self.published("korean").write_text(
            "---\ntitle: 손으로 쓴 글\n---\n\nbody\n", encoding="utf-8"
        )
        result = self.publish("--force")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("한국어 제목", self.published("korean").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
