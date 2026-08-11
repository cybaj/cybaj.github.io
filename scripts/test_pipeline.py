#!/usr/bin/env python3
"""End-to-end tests for the writing pipeline scripts."""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NEW_ITEM = REPO / "scripts" / "new_item.py"
PUBLISH = REPO / "scripts" / "publish.py"

sys.path.insert(0, str(REPO / "scripts"))

from frontmatter import FrontMatterError, split_front_matter  # noqa: E402
import hierarchy  # noqa: E402


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

    def test_duplicate_language_does_not_wedge_the_item(self):
        """`--lang ko,ko` used to half-build the item and block every retry."""
        result = self.new("hugo-pipeline", langs="ko,ko")
        self.assertEqual(result.returncode, 0, result.stderr)

        item = self.item_dir("2026-08-10-hugo-pipeline")
        self.assertTrue((item / "docs" / "ko").is_dir())
        self.assertTrue((item / "editing" / "ko").is_dir())
        text = (item / "publish.md").read_text(encoding="utf-8")
        self.assertIn("languages: [ko]", text)
        self.assertEqual(text.count('ko: ""'), 1)
        self.assertEqual(
            (item / "state.md").read_text(encoding="utf-8").count("ko: not-started"), 1
        )

    def test_state_template_carries_the_stage_vocabulary(self):
        self.new("hugo-pipeline")
        text = (self.item_dir("2026-08-10-hugo-pipeline") / "state.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("not-started | drafting | editing | done", text)

    def test_rejects_unknown_language(self):
        result = self.new("hugo-pipeline", langs="ko,fr")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown language", result.stderr)


class PublishFixture(PipelineTest):
    """Helpers shared by the publishing tests. Holds no tests of its own."""

    ITEM = "2026-08-10-hugo-pipeline"

    def write_publish_md(self, langs="ko", slug="hugo-pipeline", titles=None):
        """(Re)write publish.md, the metadata publishing reads."""
        lang_list = langs.split(",")
        titles = titles or {"ko": "한국어 제목", "en": "English Title"}
        title_block = "\n".join(f'  {l}: "{titles[l]}"' for l in lang_list)
        (self.item_dir(self.ITEM) / "publish.md").write_text(
            "---\n"
            f"slug: {slug}\n"
            f"languages: [{', '.join(lang_list)}]\n"
            "date: 2026-08-10\n"
            "tags: [hugo, blogging]\n"
            "title:\n"
            f"{title_block}\n"
            "---\n\n## Publish notes\n",
            encoding="utf-8",
        )

    def prepare(self, langs="ko", titles=None, bodies=None):
        """Scaffold an item and fill in what publishing requires."""
        self.new("hugo-pipeline", langs=langs)
        lang_list = langs.split(",")
        bodies = bodies or {lang: f"# body {lang}\n" for lang in lang_list}
        self.write_publish_md(langs=langs, titles=titles)
        for lang in lang_list:
            if lang in bodies:
                (self.item_dir(self.ITEM) / "editing" / lang / "final.md").write_text(
                    bodies[lang], encoding="utf-8"
                )

    def publish(self, *extra):
        return run(PUBLISH, self.ITEM, "--root", self.tmp, *extra)

    def published(self, lang_dir, slug="hugo-pipeline"):
        return self.tmp / "content" / lang_dir / "posts" / f"{slug}.md"


class PublishTest(PublishFixture):
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
        self.assertIn("no item marker", result.stderr)
        self.assertIn("손으로 쓴 글", self.published("korean").read_text(encoding="utf-8"))

    def test_refusal_distinguishes_another_items_slug(self):
        """A file this pipeline wrote for a different item is not hand-written."""
        self.prepare(langs="ko")
        self.published("korean").write_text(
            "---\ntitle: 다른 항목\nitem: 2026-01-01-other\n---\n\nbody\n",
            encoding="utf-8",
        )
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("belongs to a different item", result.stderr)
        self.assertIn("2026-01-01-other", result.stderr)
        self.assertNotIn("hand-written", result.stderr)

    def test_force_overwrites_handwritten_content(self):
        self.prepare(langs="ko")
        self.published("korean").write_text(
            "---\ntitle: 손으로 쓴 글\n---\n\nbody\n", encoding="utf-8"
        )
        result = self.publish("--force")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("한국어 제목", self.published("korean").read_text(encoding="utf-8"))


class MalformedMetadataTest(PublishFixture):
    """Hand-edited front matter is the likeliest breakage; it must read well."""

    def test_malformed_yaml_reports_the_file_without_a_traceback(self):
        self.prepare(langs="ko")
        path = self.item_dir(self.ITEM) / "publish.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                'ko: "한국어 제목"', 'ko: "한국어 제목'
            ),
            encoding="utf-8",
        )
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("error:", result.stderr)
        self.assertIn("publish.md", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertNotIn("yaml.scanner", result.stderr)
        self.assertFalse(self.published("korean").exists())

    def test_title_as_a_plain_string_fails_cleanly(self):
        self.prepare(langs="ko")
        path = self.item_dir(self.ITEM) / "publish.md"
        path.write_text(
            "---\n"
            "slug: hugo-pipeline\n"
            "languages: [ko]\n"
            "date: 2026-08-10\n"
            'title: "just a string"\n'
            "---\n\n## Publish notes\n",
            encoding="utf-8",
        )
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("error:", result.stderr)
        self.assertIn("title", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertFalse(self.published("korean").exists())


class SelectiveLanguageTest(PublishFixture):
    def test_publishes_one_language_while_the_other_drafts(self):
        """The supported half-finished workflow: ship ko, keep drafting en."""
        self.prepare(langs="ko,en", bodies={"ko": "# body ko\n"})
        result = self.publish("--lang", "ko")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("한국어 제목", self.published("korean").read_text(encoding="utf-8"))
        self.assertFalse(self.published("english").exists())
        self.assertNotIn("warning", result.stderr)


class OrphanWarningTest(PublishFixture):
    def test_renamed_slug_warns_and_still_succeeds(self):
        self.prepare(langs="ko")
        self.assertEqual(self.publish().returncode, 0)

        self.write_publish_md(langs="ko", slug="renamed-pipeline")
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(self.published("korean", "renamed-pipeline").is_file())
        self.assertIn("warning", result.stderr)
        self.assertIn(str(self.published("korean")), result.stderr)
        self.assertIn("renamed-pipeline", result.stderr)

    def test_dropped_language_warns(self):
        self.prepare(langs="ko,en")
        self.assertEqual(self.publish().returncode, 0)

        self.write_publish_md(langs="ko")
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("warning", result.stderr)
        self.assertIn(str(self.published("english")), result.stderr)
        self.assertIn("'en'", result.stderr)
        self.assertTrue(self.published("english").is_file(), "must not delete")

    def test_selective_publish_of_a_published_item_warns_about_nothing(self):
        """The false positive to avoid: `--lang ko` does not orphan English."""
        self.prepare(langs="ko,en")
        self.assertEqual(self.publish().returncode, 0)

        result = self.publish("--lang", "ko")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")

    def test_unrelated_items_are_never_orphans(self):
        self.prepare(langs="ko")
        self.published("korean", "someone-else").write_text(
            "---\ntitle: 남의 글\nitem: 2026-01-01-other\n---\n\nbody\n",
            encoding="utf-8",
        )
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")


class FrontMatterTest(unittest.TestCase):
    def test_body_opening_with_a_horizontal_rule_is_not_metadata(self):
        text = "---\n\nIntro paragraph that matters.\n\n---\n\nRest.\n"
        meta, body = split_front_matter(text)
        self.assertEqual(meta, {})
        self.assertEqual(body, text, "content before the second --- was dropped")

    def test_real_front_matter_still_splits(self):
        meta, body = split_front_matter("---\ntitle: 제목\n---\n\nbody\n")
        self.assertEqual(meta, {"title": "제목"})
        self.assertEqual(body, "body\n")

    def test_malformed_yaml_raises_a_named_error(self):
        with self.assertRaises(FrontMatterError) as caught:
            split_front_matter('---\ntitle: "제목\n---\n\nbody\n', "publish.md")
        message = str(caught.exception)
        self.assertIn("publish.md", message)
        self.assertRegex(message, r"line \d+", "must point at the offending line")
        self.assertEqual(message, message.strip().replace("\n", " "))


class MakefileTest(unittest.TestCase):
    """The Makefile is user interface too: check what it passes through."""

    def make_n(self, *args, env=None):
        make = shutil.which("make")
        if make is None:  # pragma: no cover - depends on the machine
            self.skipTest("make is not installed")
        result = subprocess.run(
            [make, "-n", *args],
            cwd=REPO,
            capture_output=True,
            text=True,
            env={**os.environ, **(env or {})},
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_force_0_does_not_force(self):
        self.assertNotIn("--force", self.make_n("publish", "ITEM=x", "FORCE=0"))
        self.assertNotIn("--force", self.make_n("publish", "ITEM=x", "FORCE=no"))
        self.assertNotIn("--force", self.make_n("publish", "ITEM=x", "FORCE=false"))

    def test_force_1_forces(self):
        self.assertIn("--force", self.make_n("publish", "ITEM=x", "FORCE=1"))

    def test_langs_reaches_new_item(self):
        self.assertIn('--lang "ko,en"', self.make_n("new", "TAG=x", "LANGS=ko,en"))

    def test_bare_new_passes_no_language(self):
        self.assertNotIn("--lang", self.make_n("new", "TAG=x"))

    def test_the_locale_variable_no_longer_leaks_in(self):
        """The rename to LANGS is what makes this safe without a reset."""
        env = {"LANG": "C.UTF-8"}
        self.assertNotIn("--lang", self.make_n("new", "TAG=x", env=env))
        self.assertNotIn("--lang", self.make_n("publish", "ITEM=x", env=env))


class HierarchyTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)

    def tree(self, *rel_paths):
        lang_dir = self.tmp / "editing" / "ko"
        for rel in rel_paths:
            path = lang_dir / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("body\n", encoding="utf-8")
        return lang_dir

    def write_structure(self, text):
        (self.tmp / "structure.md").write_text(text, encoding="utf-8")

    def test_walk_separates_leaves_sections_and_directories(self):
        lang_dir = self.tree(
            "setup.md", "_index.md", "templates/basics.md", "templates/_index.md"
        )
        leaves, bodies, directories = hierarchy.walk_editing_tree(lang_dir)
        self.assertEqual(
            sorted(p.as_posix() for p in leaves),
            ["setup.md", "templates/basics.md"],
        )
        self.assertEqual(sorted(bodies), ["", "templates"])
        self.assertEqual(directories, ["", "templates"])

    def test_walk_records_intermediate_directories(self):
        lang_dir = self.tree("a/b/c/deep.md")
        _, _, directories = hierarchy.walk_editing_tree(lang_dir)
        self.assertEqual(directories, ["", "a", "a/b", "a/b/c"])

    def test_absent_structure_means_no_overrides(self):
        self.assertEqual(hierarchy.load_structure(self.tmp), {})

    def test_structure_loads_section_overrides(self):
        self.write_structure(
            '---\nsections:\n  templates:\n    title: {ko: "템플릿"}\n'
            "    weight: 20\n---\n"
        )
        overrides = hierarchy.load_structure(self.tmp)
        self.assertEqual(overrides["templates"]["weight"], 20)
        self.assertEqual(overrides["templates"]["title"]["ko"], "템플릿")

    def test_structure_rejects_a_non_map_sections(self):
        self.write_structure("---\nsections: nope\n---\n")
        with self.assertRaises(hierarchy.HierarchyError) as caught:
            hierarchy.load_structure(self.tmp)
        self.assertIn("map", str(caught.exception))

    def test_structure_rejects_a_non_map_section_entry(self):
        """`templates: 20` — forgetting to nest weight: — must not crash."""
        self.write_structure("---\nsections:\n  templates: 20\n---\n")
        with self.assertRaises(hierarchy.HierarchyError) as caught:
            hierarchy.load_structure(self.tmp)
        self.assertIn("templates", str(caught.exception))

    def test_declared_section_without_a_directory_is_an_error(self):
        with self.assertRaises(hierarchy.HierarchyError) as caught:
            hierarchy.validate_sections({"typo": {}}, ["", "templates"], "structure.md")
        self.assertIn("typo", str(caught.exception))

    def test_section_title_comes_from_the_override(self):
        overrides = {"templates": {"title": {"ko": "템플릿", "en": "Templates"}}}
        front, fell_back = hierarchy.resolve_section_meta(
            "templates", overrides, "ko", "아이템 제목", "structure.md"
        )
        self.assertEqual(front["title"], "템플릿")
        self.assertFalse(fell_back)

    def test_a_title_omitting_this_language_falls_back(self):
        """A title declared for en only must still fall back for ko."""
        overrides = {"templates": {"title": {"en": "Templates"}}}
        front, fell_back = hierarchy.resolve_section_meta(
            "templates", overrides, "ko", "아이템 제목", "structure.md"
        )
        self.assertEqual(front["title"], "templates")
        self.assertTrue(fell_back)

    def test_root_section_falls_back_to_the_item_title(self):
        front, fell_back = hierarchy.resolve_section_meta(
            "", {}, "ko", "아이템 제목", "structure.md"
        )
        self.assertEqual(front["title"], "아이템 제목")
        self.assertFalse(fell_back)

    def test_undeclared_section_falls_back_to_its_directory_name(self):
        front, fell_back = hierarchy.resolve_section_meta(
            "a/advanced", {}, "ko", "아이템 제목", "structure.md"
        )
        self.assertEqual(front["title"], "advanced")
        self.assertTrue(fell_back)

    def test_unknown_keys_pass_through_to_front_matter(self):
        overrides = {"t": {"title": {"ko": "T"}, "weight": 5, "bookCollapseSection": True}}
        front, _ = hierarchy.resolve_section_meta(
            "t", overrides, "ko", "제목", "structure.md"
        )
        self.assertEqual(front["weight"], 5)
        self.assertTrue(front["bookCollapseSection"])

    def test_a_bare_string_title_is_an_error(self):
        overrides = {"t": {"title": "just a string"}}
        with self.assertRaises(hierarchy.HierarchyError) as caught:
            hierarchy.resolve_section_meta("t", overrides, "ko", "제목", "structure.md")
        self.assertIn("language", str(caught.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)
