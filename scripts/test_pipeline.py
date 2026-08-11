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

    def test_target_reaches_new_item(self):
        self.assertIn("--target docs", self.make_n("new", "TAG=x", "TARGET=docs"))

    def test_bare_new_passes_no_target(self):
        self.assertNotIn("--target", self.make_n("new", "TAG=x"))


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


class DocsFixture(PipelineTest):
    ITEM = "2026-08-10-hugo-guide"

    def write_publish_md(self, langs="ko", target="docs", slug="hugo-guide"):
        lang_list = langs.split(",")
        titles = {"ko": "휴고 가이드", "en": "Hugo Guide"}
        block = "\n".join(f'  {l}: "{titles[l]}"' for l in lang_list)
        (self.item_dir(self.ITEM) / "publish.md").write_text(
            "---\n"
            f"target: {target}\n"
            f"slug: {slug}\n"
            f"languages: [{', '.join(lang_list)}]\n"
            "date: 2026-08-10\n"
            "tags: [hugo]\n"
            "title:\n"
            f"{block}\n"
            "---\n",
            encoding="utf-8",
        )

    def write_doc(self, lang, rel, text):
        path = self.item_dir(self.ITEM) / "editing" / lang / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def prepare(self, langs="ko", target="docs", slug="hugo-guide"):
        self.new("hugo-guide", langs=langs)
        self.write_publish_md(langs=langs, target=target, slug=slug)

    def publish(self, *extra):
        return run(PUBLISH, self.ITEM, "--root", self.tmp, *extra)

    def out(self, lang_dir, rel, slug="hugo-guide"):
        return self.tmp / "content" / lang_dir / "docs" / slug / rel


class DocsTargetTest(DocsFixture):
    def test_publishes_a_nested_tree(self):
        self.prepare(langs="ko")
        self.write_doc("ko", "setup.md", '---\ntitle: "설치"\n---\n\n본문\n')
        self.write_doc(
            "ko", "templates/basics.md", '---\ntitle: "기초"\nweight: 10\n---\n\n기초 본문\n'
        )
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)

        setup = self.out("korean", "setup.md").read_text(encoding="utf-8")
        self.assertIn("title: 설치", setup)
        self.assertIn("본문", setup)
        basics = self.out("korean", "templates/basics.md").read_text(encoding="utf-8")
        self.assertIn("weight: 10", basics)

    def test_item_defaults_fill_gaps(self):
        self.prepare(langs="ko")
        self.write_doc("ko", "setup.md", '---\ntitle: "설치"\n---\n\n본문\n')
        self.publish()
        text = self.out("korean", "setup.md").read_text(encoding="utf-8")
        self.assertIn("date: 2026-08-10", text)
        self.assertIn("hugo", text)
        self.assertIn("item: 2026-08-10-hugo-guide", text)

    def test_leaf_front_matter_wins_over_item_defaults(self):
        self.prepare(langs="ko")
        self.write_doc(
            "ko", "setup.md", '---\ntitle: "설치"\ndate: 2020-01-01\n---\n\n본문\n'
        )
        self.publish()
        text = self.out("korean", "setup.md").read_text(encoding="utf-8")
        self.assertIn("date: 2020-01-01", text)

    def test_a_leaf_cannot_override_the_item_marker(self):
        self.prepare(langs="ko")
        self.write_doc(
            "ko", "setup.md", '---\ntitle: "설치"\nitem: forged\n---\n\n본문\n'
        )
        self.publish()
        text = self.out("korean", "setup.md").read_text(encoding="utf-8")
        self.assertIn("item: 2026-08-10-hugo-guide", text)
        self.assertNotIn("forged", text)

    def test_title_falls_back_to_the_h1(self):
        self.prepare(langs="ko")
        self.write_doc("ko", "setup.md", "# 설치 방법\n\n본문\n")
        self.publish()
        text = self.out("korean", "setup.md").read_text(encoding="utf-8")
        self.assertIn("title: 설치 방법", text)

    def test_title_falls_back_to_the_filename_with_a_warning(self):
        self.prepare(langs="ko")
        self.write_doc("ko", "setup.md", "본문만 있음\n")
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("setup", result.stderr)
        text = self.out("korean", "setup.md").read_text(encoding="utf-8")
        self.assertIn("title: setup", text)

    def test_korean_is_not_escaped(self):
        self.prepare(langs="ko")
        self.write_doc("ko", "setup.md", '---\ntitle: "설치"\n---\n\n본문\n')
        self.publish()
        self.assertNotIn("\\u", self.out("korean", "setup.md").read_text(encoding="utf-8"))

    def test_empty_language_tree_names_the_language(self):
        self.prepare(langs="ko,en")
        self.write_doc("ko", "setup.md", '---\ntitle: "설치"\n---\n\n본문\n')
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("'en'", result.stderr)

    def test_partial_failure_writes_nothing(self):
        """A half-publishable tree must not half-publish.

        The returncode assertion matters: without it this test cannot tell a
        correct refusal from a publish.py that silently did nothing, which is
        exactly how the flat-post version of this test was found lacking.
        """
        self.prepare(langs="ko,en")
        self.write_doc("ko", "setup.md", '---\ntitle: "설치"\n---\n\n본문\n')
        result = self.publish()
        self.assertNotEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.out("korean", "setup.md").exists())

    def test_unknown_target_is_rejected(self):
        self.prepare(langs="ko", target="wiki")
        self.write_doc("ko", "setup.md", '---\ntitle: "설치"\n---\n\n본문\n')
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("wiki", result.stderr)
        self.assertIn("docs", result.stderr)

    def test_publishes_both_languages(self):
        self.prepare(langs="ko,en")
        self.write_doc("ko", "templates/basics.md", '---\ntitle: "기초"\n---\n\n본문\n')
        self.write_doc("en", "templates/basics.md", '---\ntitle: "Basics"\n---\n\nBody\n')
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "title: 기초",
            self.out("korean", "templates/basics.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "title: Basics",
            self.out("english", "templates/basics.md").read_text(encoding="utf-8"),
        )

    def test_posts_target_is_unchanged_when_absent(self):
        """The regression guard: no target means today's flat-post behaviour.

        Asserts the exact bytes, not merely that a file appeared — this is the
        only test standing between a refactor and silently changing the output
        of every item published before targets existed.
        """
        self.new("hugo-pipeline", langs="ko")
        item = self.item_dir("2026-08-10-hugo-pipeline")
        (item / "publish.md").write_text(
            '---\nslug: hugo-pipeline\nlanguages: [ko]\ndate: 2026-08-10\n'
            'title:\n  ko: "제목"\n---\n',
            encoding="utf-8",
        )
        (item / "editing" / "ko" / "final.md").write_text("본문\n", encoding="utf-8")
        result = run(PUBLISH, "2026-08-10-hugo-pipeline", "--root", self.tmp)
        self.assertEqual(result.returncode, 0, result.stderr)
        published = self.tmp / "content" / "korean" / "posts" / "hugo-pipeline.md"
        self.assertEqual(
            published.read_text(encoding="utf-8"),
            "---\n"
            "title: 제목\n"
            "date: 2026-08-10\n"
            "item: 2026-08-10-hugo-pipeline\n"
            "---\n"
            "\n"
            "본문\n",
        )


class SectionPageTest(DocsFixture):
    def write_structure(self, text):
        (self.item_dir(self.ITEM) / "structure.md").write_text(text, encoding="utf-8")

    def test_root_section_uses_the_item_title(self):
        self.prepare(langs="ko")
        self.write_doc("ko", "setup.md", '---\ntitle: "설치"\n---\n\n본문\n')
        self.publish()
        text = self.out("korean", "_index.md").read_text(encoding="utf-8")
        self.assertIn("title: 휴고 가이드", text)
        self.assertIn("item: 2026-08-10-hugo-guide", text)

    def test_declared_section_uses_its_override(self):
        self.prepare(langs="ko")
        self.write_doc("ko", "templates/basics.md", '---\ntitle: "기초"\n---\n\n본문\n')
        self.write_structure(
            '---\nsections:\n  templates:\n    title: {ko: "템플릿"}\n'
            "    weight: 20\n    bookCollapseSection: true\n---\n"
        )
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        text = self.out("korean", "templates/_index.md").read_text(encoding="utf-8")
        self.assertIn("title: 템플릿", text)
        self.assertIn("weight: 20", text)
        self.assertIn("bookCollapseSection: true", text)

    def test_undeclared_section_falls_back_and_warns(self):
        self.prepare(langs="ko")
        self.write_doc("ko", "advanced/tips.md", '---\ntitle: "팁"\n---\n\n본문\n')
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("advanced", result.stderr)
        text = self.out("korean", "advanced/_index.md").read_text(encoding="utf-8")
        self.assertIn("title: advanced", text)

    def test_an_editing_index_supplies_the_body(self):
        self.prepare(langs="ko")
        self.write_doc("ko", "setup.md", '---\ntitle: "설치"\n---\n\n본문\n')
        self.write_doc("ko", "_index.md", "이 가이드에 대하여\n")
        self.publish()
        text = self.out("korean", "_index.md").read_text(encoding="utf-8")
        self.assertIn("이 가이드에 대하여", text)
        self.assertIn("title: 휴고 가이드", text)

    def test_declared_section_without_a_directory_is_an_error(self):
        self.prepare(langs="ko")
        self.write_doc("ko", "setup.md", '---\ntitle: "설치"\n---\n\n본문\n')
        self.write_structure('---\nsections:\n  typo:\n    weight: 1\n---\n')
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("typo", result.stderr)

    def test_a_section_present_in_one_language_only_is_valid(self):
        """A half-translated item must still publish.

        Sections validate against the union across declared languages, not
        per language — `advanced/` existing in Korean before English is the
        normal state mid-translation, not an error.
        """
        self.prepare(langs="ko,en")
        self.write_doc("ko", "advanced/tips.md", '---\ntitle: "팁"\n---\n\n본문\n')
        self.write_doc("en", "setup.md", '---\ntitle: "Setup"\n---\n\nBody\n')
        self.write_structure(
            '---\nsections:\n  advanced:\n    title: {ko: "심화", en: "Advanced"}\n---\n'
        )
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("title: 심화", self.out("korean", "advanced/_index.md").read_text(encoding="utf-8"))

    def test_structure_on_a_posts_item_warns_and_is_ignored(self):
        self.prepare(langs="ko", target="posts")
        (self.item_dir(self.ITEM) / "editing" / "ko" / "final.md").write_text(
            "본문\n", encoding="utf-8"
        )
        self.write_structure('---\nsections:\n  t:\n    weight: 1\n---\n')
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("structure.md", result.stderr)
        self.assertIn("ignor", result.stderr.lower())


class TreeOrphanTest(DocsFixture):
    def seed(self, langs="ko"):
        self.prepare(langs=langs)
        for lang in langs.split(","):
            self.write_doc(lang, "setup.md", '---\ntitle: "T"\n---\n\n본문\n')
            self.write_doc(lang, "templates/basics.md", '---\ntitle: "B"\n---\n\n본문\n')
        self.assertEqual(self.publish().returncode, 0)

    def test_deleted_page_becomes_an_orphan(self):
        self.seed()
        (self.item_dir(self.ITEM) / "editing" / "ko" / "templates" / "basics.md").unlink()
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("basics.md", result.stderr)

    def test_renamed_slug_orphans_the_old_subtree(self):
        self.seed()
        self.write_publish_md(langs="ko", slug="renamed-guide")
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("hugo-guide", result.stderr)
        self.assertTrue(self.out("korean", "setup.md", slug="renamed-guide").is_file())

    def test_dropped_language_orphans_its_subtree(self):
        self.seed(langs="ko,en")
        self.write_publish_md(langs="ko")
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("english", result.stderr)

    def test_target_switch_orphans_the_flat_post(self):
        self.prepare(langs="ko", target="posts")
        (self.item_dir(self.ITEM) / "editing" / "ko" / "final.md").write_text(
            "본문\n", encoding="utf-8"
        )
        self.assertEqual(self.publish().returncode, 0)
        self.write_publish_md(langs="ko", target="docs")
        self.write_doc("ko", "setup.md", '---\ntitle: "T"\n---\n\n본문\n')
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("posts", result.stderr)

    def test_generated_sections_are_never_orphans(self):
        """The trap: _index.md comes from directories, not from editing files."""
        self.seed()
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("_index.md", result.stderr)

    def test_selective_publish_warns_about_nothing(self):
        self.seed(langs="ko,en")
        # An override for the generated `templates/` section keeps the
        # unrelated "no title in structure.md" fallback warning (Task 3) out
        # of this assertion; it is not present in either deleted-page test,
        # where the section directory itself may no longer exist.
        (self.item_dir(self.ITEM) / "structure.md").write_text(
            '---\nsections:\n  templates:\n    title: {ko: "템플릿", en: "Templates"}\n---\n',
            encoding="utf-8",
        )
        result = self.publish("--lang", "ko")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")


class TargetScaffoldTest(PipelineTest):
    def new_with_target(self, tag, target):
        return run(
            NEW_ITEM, tag, "--lang", "ko", "--date", "2026-08-10",
            "--target", target, "--root", self.tmp,
        )

    def test_docs_item_declares_its_target(self):
        result = self.new_with_target("hugo-guide", "docs")
        self.assertEqual(result.returncode, 0, result.stderr)
        text = (self.item_dir("2026-08-10-hugo-guide") / "publish.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("target: docs", text)

    def test_docs_item_scaffolds_structure_md(self):
        self.new_with_target("hugo-guide", "docs")
        path = self.item_dir("2026-08-10-hugo-guide") / "structure.md"
        self.assertTrue(path.is_file())
        self.assertIn("sections:", path.read_text(encoding="utf-8"))

    def test_posts_item_has_no_structure_md(self):
        self.new_with_target("hugo-pipeline", "posts")
        item = self.item_dir("2026-08-10-hugo-pipeline")
        self.assertFalse((item / "structure.md").exists())

    def test_default_target_is_posts(self):
        self.new("hugo-pipeline", langs="ko")
        item = self.item_dir("2026-08-10-hugo-pipeline")
        self.assertFalse((item / "structure.md").exists())
        self.assertNotIn("target:", (item / "publish.md").read_text(encoding="utf-8"))

    def test_unknown_target_is_rejected(self):
        result = self.new_with_target("hugo-guide", "wiki")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("wiki", result.stderr)

    def test_no_unrendered_placeholder_in_structure(self):
        self.new_with_target("hugo-guide", "docs")
        text = (self.item_dir("2026-08-10-hugo-guide") / "structure.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("{{", text)

    def test_the_target_token_renders_away_for_a_posts_item(self):
        """{{TARGET_LINE}} must vanish, not linger, on a posts item."""
        self.new_with_target("hugo-pipeline", "posts")
        text = (self.item_dir("2026-08-10-hugo-pipeline") / "publish.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("{{", text)
        self.assertTrue(text.startswith("---\nslug: hugo-pipeline\n"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
