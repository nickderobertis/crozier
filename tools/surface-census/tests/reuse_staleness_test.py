#!/usr/bin/env python3
"""What the census suites keep between cases answers for the content it was read from.

`golden-reach.py`, `scenario-proof-index.py` and the census suite's own loaders
keep what they read by file content, so a table, source or script that changes is
read again. These warm each reading first, then change the input the way a later
commit would, through the same real functions the suite calls; a stale reading
fails here. They live apart from `surface_census_test.py` because that suite's
collected cases are pinned (`tools/ci/suite-cases/`).
"""

from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType
from unittest import mock

REPO = Path(__file__).resolve().parents[3]


def load(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


reach = load(REPO / "tools/surface-census/golden-reach.py", "reuse_golden_reach")
index = load(REPO / "tools/surface-census/scenario-proof-index.py", "reuse_scenario_index")
suite = load(REPO / "tools/surface-census/tests/surface_census_test.py", "reuse_census_suite")

SOURCE = """\
struct Lantern;

impl Lantern {
    fn light(&self) -> u8 {
        1
    }
}

fn light() -> u8 {
    2
}
"""


class SiteResolutionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        (self.root / "src").mkdir()
        self.source = self.root / "src/lantern.rs"
        self.source.write_text(SOURCE, encoding="utf-8")

    def span(self, spec: str) -> tuple[int, int]:
        site = reach.resolve_site(spec, self.root)
        return site.start, site.end

    def test_free_functions_and_methods_keep_their_own_spans(self) -> None:
        self.assertEqual((4, 6), self.span("src/lantern.rs::Lantern::light"))
        self.assertEqual((9, 11), self.span("src/lantern.rs::light"))

    def test_a_moved_function_resolves_where_it_now_is(self) -> None:
        self.assertEqual((9, 11), self.span("src/lantern.rs::light"))
        self.source.write_text("// moved\n\n" + SOURCE, encoding="utf-8")
        self.assertEqual((11, 13), self.span("src/lantern.rs::light"))

    def test_a_removed_function_is_refused_after_it_resolved(self) -> None:
        self.assertEqual((4, 6), self.span("src/lantern.rs::Lantern::light"))
        self.source.write_text("struct Lantern;\n", encoding="utf-8")
        with self.assertRaisesRegex(SystemExit, "matches 0 functions"):
            self.span("src/lantern.rs::Lantern::light")

    def test_a_returned_function_resolves_again(self) -> None:
        self.assertEqual((9, 11), self.span("src/lantern.rs::light"))
        self.source.write_text("struct Lantern;\n", encoding="utf-8")
        with self.assertRaises(SystemExit):
            self.span("src/lantern.rs::light")
        self.source.write_text(SOURCE, encoding="utf-8")
        self.assertEqual((9, 11), self.span("src/lantern.rs::light"))


class E2eReadingTests(unittest.TestCase):
    def test_a_changed_e2e_source_is_read_again(self) -> None:
        root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        for entry in index.E2E_SOURCES:
            (root / entry).parent.mkdir(parents=True, exist_ok=True)
        source = root / "crates/crozier-e2e/tests/e2e.rs"
        source.write_text("#[test]\nfn lantern() {\n}\n", encoding="utf-8")
        self.assertEqual({"lantern"}, set(index.read_e2e(root).tests))
        source.write_text("#[test]\nfn harbour() {\n}\n", encoding="utf-8")
        self.assertEqual({"harbour"}, set(index.read_e2e(root).tests))

    def test_a_body_ends_at_its_own_indent_and_an_unclosed_one_at_the_file_end(self) -> None:
        root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        for entry in index.E2E_SOURCES:
            (root / entry).parent.mkdir(parents=True, exist_ok=True)
        (root / "crates/crozier-e2e/tests/e2e.rs").write_text(
            "fn outer() {\n    fn inner() {\n    }\n    tail();\n}\nfn unclosed() {\n    open();\n", encoding="utf-8"
        )
        bodies = index.read_e2e(root).bodies
        self.assertEqual("    fn inner() {\n    }", bodies["inner"])
        self.assertTrue(bodies["outer"].endswith("    tail();\n}"))
        self.assertEqual("fn unclosed() {\n    open();", bodies["unclosed"])


class ScriptLoadingTests(unittest.TestCase):
    def test_a_changed_script_is_executed_again_and_an_unchanged_one_is_not(self) -> None:
        root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        script = root / "tool.py"
        script.write_text("ANSWER = 1\n", encoding="utf-8")
        with mock.patch.object(suite, "REPO", root):
            first = suite.load_script("tool.py")
            self.assertIs(first, suite.load_script("tool.py"))
            script.write_text("ANSWER = 22\n", encoding="utf-8")
            self.assertEqual(22, suite.load_script("tool.py").ANSWER)
        self.assertEqual(1, first.ANSWER)

    def test_a_script_a_case_rebinds_is_its_own_copy(self) -> None:
        path = "tools/surface-census/port_pins.py"
        fresh = suite.fresh_script(path)
        self.assertIsNot(fresh, suite.load_script(path))


class FinishedStateTests(unittest.TestCase):
    """The gate's own copy of the committed ledgers, warmed, then made stale."""

    def setUp(self) -> None:
        case = suite.FinishedStateGateTests("test_the_committed_ledgers_are_in_their_finished_state")
        case.setUp()
        self.addCleanup(case.doCleanups)
        self.root = case.root
        self.assertEqual([], suite.finished_state_failures(self.root))

    def test_a_stale_expected_table_is_rejected_then_accepted_once_repaired(self) -> None:
        table = self.root / "docs/openapi-surface/handwritten-reach.tsv"
        committed = table.read_text(encoding="utf-8")
        table.write_text(committed.replace("\t", "  ", 1), encoding="utf-8")
        self.assertNotEqual([], suite.finished_state_failures(self.root))
        table.write_text(committed, encoding="utf-8")
        self.assertEqual([], suite.finished_state_failures(self.root))

    def test_a_changed_witness_document_is_parsed_again(self) -> None:
        engine = suite.load_script("tools/surface-census/openapi-surface-census.py")
        document = self.root / "lantern.yml"
        document.write_text("openapi: 3.0.3\npaths: {}\n", encoding="utf-8")
        self.assertEqual({}, suite.committed_document(engine, document)["paths"])
        document.write_text("openapi: 3.0.3\npaths: {/lanterns: {}}\n", encoding="utf-8")
        self.assertEqual({"/lanterns": {}}, suite.committed_document(engine, document)["paths"])
        shutil.rmtree(self.root / "docs")
        document.write_text("openapi: [unterminated\n", encoding="utf-8")
        with self.assertRaises((engine.DocumentError, ValueError)):
            suite.committed_document(engine, document)


class EvidenceDirectoryTests(unittest.TestCase):
    def test_a_fresh_reading_sees_what_a_shared_one_kept(self) -> None:
        directory = Path(self.enterContext(tempfile.TemporaryDirectory()))
        (directory / "records.tsv").write_text("key\tkind\tfile\n", encoding="utf-8")
        (directory / "stray.txt").write_text("unaccounted\n", encoding="utf-8")
        shared = suite.EvidenceDirectory(directory)
        self.assertEqual(shared.layout_failures(()), shared.layout_failures(()))
        self.assertIn("stray.txt", shared.layout_failures(())[0])
        self.assertEqual(shared.layout_failures(("stray.txt",)), [])
        (directory / "stray.txt").unlink()
        self.assertEqual([], suite.EvidenceDirectory(directory).layout_failures(()))


if __name__ == "__main__":
    unittest.main()
