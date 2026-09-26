#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier has no Nx workspace; this boundary test sits in tests/ beside fixtures_coverage_test.py and runs under `just test-fixtures-coverage`.
"""Boundary tests for `just golden-reach` (run by `just test-fixtures-coverage`).

`scripts/golden-reach.py` turns the golden-only coverage tier into a per-row
reach cell. Its `measure` half needs an instrumented corpus run and the network,
so it stays outside `just check` exactly as `just fixtures-coverage` does. What
these cases drive instead is everything that decides what a cell *says*:

* the site resolver, over the real `src/` — a declared arm must bound the code
  the arm runs and nothing beside it, or a reached `else` reads as a reached
  `if`;
* the `report` subcommand as a subprocess, over a small repository laid out
  the way this one is (a region file, a site table, `tests/e2e.rs`, a census and
  a measurement directory), so the ledger and the rewritten region cells are the
  CLI's own output rather than a function's return value;
* `scripts/golden-reach-search.py`'s offline readings — the predicate a
  `fixture=` row is searched with, the git blob a publisher-tree pin is checked
  against, and a result URL's quoting — over real bytes. Its network stages go
  through the guarded acquirer and are checked, once committed, by
  `RankedBacklogTests`' reconciliation of every arm-search record.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "golden-reach.py"

_spec = importlib.util.spec_from_file_location("golden_reach", SCRIPT)
assert _spec and _spec.loader
golden_reach = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(golden_reach)


def recipe_body(name: str) -> str:
    """The command lines of one justfile recipe, so a rewiring fails here."""
    lines = (REPO / "justfile").read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if re.match(rf"^{re.escape(name)}( +[\w*\"=]+)*:", line):
            body = []
            for follower in lines[index + 1 :]:
                if not follower.startswith((" ", "\t")):
                    break
                body.append(follower.strip())
            return "\n".join(body)
    raise AssertionError(f"the justfile has no `{name}` recipe")


class SiteResolutionTests(unittest.TestCase):
    """Declared sites resolve against the real `src/`, at the grain of an arm."""

    def resolve(self, spec: str):
        return golden_reach.resolve_site(spec, REPO)

    def line_of(self, file: str, number: int) -> str:
        return (REPO / file).read_text(encoding="utf-8").splitlines()[number - 1]

    def test_a_function_site_spans_its_whole_item(self) -> None:
        site = self.resolve("src/openapi.rs::filter_ignored")
        self.assertIn("pub fn filter_ignored", self.line_of(site.file, site.start))
        self.assertEqual("}", self.line_of(site.file, site.end))
        self.assertTrue(site.holds((site.start, 1, site.start, 9)))

    def test_a_method_site_is_named_through_its_impl(self) -> None:
        operation = self.resolve("src/openapi.rs::Operation::ignored")
        schema = self.resolve("src/openapi.rs::Schema::ignored")
        self.assertNotEqual(operation.start, schema.start)
        for site in (operation, schema):
            self.assertIn("pub fn ignored", self.line_of(site.file, site.start))

    def test_an_arm_starts_at_its_brace_and_stops_before_the_next_arm(self) -> None:
        taken = self.resolve(r"src/openapi.rs::filter_by_audience[if labels\.is_empty\(\) \{]")
        other = self.resolve(r"src/openapi.rs::filter_by_audience[\} else \{]")
        # The `} else {` line closes one arm and opens the other: a region
        # starting at the `else` body belongs to the second arm only, and the
        # condition before the first arm's brace belongs to neither.
        else_body = (other.start, other.start_col, other.start, other.start_col + 1)
        self.assertTrue(other.holds(else_body))
        self.assertFalse(taken.holds(else_body))
        condition = (taken.start, taken.start_col - 5, taken.start, taken.start_col - 1)
        self.assertFalse(taken.holds(condition))
        self.assertEqual(taken.end, other.start)

    def test_a_multi_line_condition_opens_its_arm_on_a_later_line(self) -> None:
        site = self.resolve(r"src/ir.rs::InlineHoister::hoist_union_variant[^ {8}\{$]")
        self.assertEqual("{", self.line_of(site.file, site.start).strip())
        self.assertIn("return TypeRef::Named(name);", self.line_of(site.file, site.end - 1))

    def test_a_line_only_arm_holds_regions_from_its_match_onward(self) -> None:
        site = self.resolve(r"src/ir.rs::auth_model[=_ => Auth::Bearer \{ required: false \}]")
        self.assertEqual(site.start, site.end)
        self.assertTrue(site.holds((site.start, site.start_col, site.start, site.start_col + 5)))
        self.assertFalse(site.holds((site.start, 1, site.start, 2)))

    def test_a_regex_may_hold_a_comma(self) -> None:
        cell = r"src/ir.rs::resolve_request_body[\.find\(\x7c\(media_type, media\)\x7c \{],src/ir.rs::is_binary_response"
        parts = golden_reach._split_sites(cell)
        self.assertEqual(2, len(parts))
        self.assertTrue(parts[0].endswith(r"\{]"))
        self.resolve(parts[0])

    def test_an_unqualified_method_or_a_missing_site_is_refused_with_its_name(self) -> None:
        for spec, message in (
            # `ignored` is a method of two types; a bare name means a free function.
            ("src/openapi.rs::ignored", "qualify a method as `Type::name`"),
            ("src/openapi.rs::no_such_function", "matches 0 functions"),
            ("src/nowhere.rs::load", "does not exist"),
            (r"src/openapi.rs::filter_ignored[no such text]", "matches 0 lines"),
            ("src/openapi.rs::filter_by_audience[keep = |op]", "write `\\x7c`"),
        ):
            with self.subTest(spec=spec), self.assertRaises(SystemExit) as refused:
                self.resolve(spec)
            self.assertIn(message, str(refused.exception))
            self.assertIn(spec, str(refused.exception))


DEMO_SOURCE = textwrap.dedent(
    """\
    pub fn handles(flag: bool) -> u8 {
        if flag {
            1
        } else {
            2
        }
    }

    pub fn unrelated() -> u8 {
        3
    }
    """
)

# Counter regions as llvm-cov reports them: [line_start, col_start, line_end, col_end].
UNIVERSE = [
    [1, 1, 1, 35],   # `handles` entry
    [2, 8, 2, 12],   # the condition
    [3, 9, 3, 10],   # the `if` arm
    [4, 12, 6, 6],   # the `else` arm
    [9, 1, 10, 6],   # `unrelated`
]

REGION_FILE = textwrap.dedent(
    """\
    # demo

    ## Entries

    | key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |
    |---|---|---|---|---|---|---|---|
    | `flag-set` | both | Demo Object.flag | golden | census `demo.flag`: `demo-a` (1) |  |  |  |
    | `flag-orphan` | both | Demo Object.orphan | golden | census `demo.orphan`: `dropped-doc` (1) |  |  |  |
    | `flag-unread` | both | Demo Object.unread | golden | census `demo.unread`: `demo-b` (1) |  |  |  |
    | `flag-gap` | both | Demo Object.gap | gap | census `demo.gap`: 0 | none | nothing | `UNREACHABLE` nothing to settle |
    """
)

SITES = textwrap.dedent(
    """\
    key\tselectors\tsites\tnote
    flag-set\tdemo.flag\tsrc/demo.rs::handles[if flag \\{],src/demo.rs::handles[\\} else \\{]\t
    flag-orphan\tdemo.orphan\tsrc/demo.rs::unrelated\t
    flag-unread\tdemo.unread\tnone\tno arm of `src/demo.rs` reads it
    """
)

E2E = textwrap.dedent(
    """\
    const DEMO_A: Corpus = Corpus {
        api: "demo-a",
    };

    const DEMO_B: Corpus = Corpus {
        api: "demo-b",
    };

    #[test]
    fn demo_a_matches_fern_output() {
        assert_link_ok_corpus_matches(&DEMO_A);
    }

    #[test]
    fn demo_b_matches_fern_output() {
        assert_link_ok_corpus_matches(&DEMO_B);
    }
    """
)

CENSUS = {
    "sources": [
        {"fixture": "demo-a", "origin": "corpus", "path": None},
        {"fixture": "demo-b", "origin": "corpus", "path": None},
        {"fixture": "dropped-doc", "origin": "corpus", "path": None},
    ],
    "rows": [
        {"selector": "demo.flag", "fixture": "demo-a", "count": 1},
        {"selector": "demo.orphan", "fixture": "dropped-doc", "count": 1},
        {"selector": "demo.unread", "fixture": "demo-b", "count": 1},
    ],
    "absent_selectors": [],
}


class ReportTests(unittest.TestCase):
    """`golden-reach.py report` over a repository laid out like this one."""

    def setUp(self) -> None:
        self.scratch = tempfile.TemporaryDirectory(prefix="golden-reach-test-")
        root = Path(self.scratch.name)
        self.repo = root / "repo"
        self.measurement = root / "measurement"
        (self.repo / "src").mkdir(parents=True)
        (self.repo / "src" / "demo.rs").write_text(DEMO_SOURCE, encoding="utf-8")
        regions = self.repo / "docs" / "openapi-surface"
        regions.mkdir(parents=True)
        (regions / "demo.md").write_text(REGION_FILE, encoding="utf-8")
        (regions / "golden-reach-sites.tsv").write_text(SITES, encoding="utf-8")
        (self.repo / "tests" / "fixtures").mkdir(parents=True)
        (self.repo / "tests" / "e2e.rs").write_text(E2E, encoding="utf-8")
        (self.measurement / "tests").mkdir(parents=True)
        (self.measurement / "universe.json").write_text(
            json.dumps({"src/demo.rs": UNIVERSE}), encoding="utf-8"
        )
        # `demo-a` takes the `if` arm and never the `else` one.
        (self.measurement / "tests" / "demo_a_matches_fern_output.json").write_text(
            json.dumps({"src/demo.rs": UNIVERSE[:3]}), encoding="utf-8"
        )
        (self.measurement / "tests" / "demo_b_matches_fern_output.json").write_text(
            json.dumps({"src/demo.rs": [UNIVERSE[4]]}), encoding="utf-8"
        )
        (self.measurement / "provenance.json").write_text(
            json.dumps({"commit": "0123456789abcdef", "tests": 2}), encoding="utf-8"
        )
        (self.measurement / "census.json").write_text(json.dumps(CENSUS), encoding="utf-8")

    def tearDown(self) -> None:
        self.scratch.cleanup()

    def run_report(self, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable, str(SCRIPT), "--repo-root", str(self.repo),
                "--out", str(self.measurement), "report", *extra,
            ],
            capture_output=True, text=True,
        )

    def cells(self) -> dict[str, list[str]]:
        text = (self.repo / "docs" / "openapi-surface" / "demo.md").read_text(encoding="utf-8")
        return {cells[0].strip("`"): cells for cells in golden_reach.region_rows(text)}

    def test_report_writes_the_ranked_ledger_and_every_golden_rows_reach_cell(self) -> None:
        run = self.run_report("--write")
        self.assertEqual(0, run.returncode, run.stderr)
        ledger = golden_reach.read_ledger(self.repo / "docs" / "openapi-surface" / "golden-reach.tsv")
        self.assertEqual(
            ["flag-orphan", "flag-set", "flag-unread"],
            [reach.key for _rank, reach in ledger],
            "a row with an unreached site ranks above a row reaching all of its own",
        )
        rank, flag_set = ledger[1]
        self.assertEqual(("demo-a",), flag_set.witnesses)
        self.assertEqual(1, flag_set.unreached_sites)
        cells = self.cells()
        self.assertTrue(cells["flag-set"][5].startswith("reach: **1** of **2** handling sites"))
        self.assertIn("its **one** golden-only witness `demo-a`", cells["flag-set"][5])
        self.assertIn(r"unreached `src/demo.rs::handles[\} else \{]` 0/1", cells["flag-set"][5])
        self.assertIn(f"rank {rank})", cells["flag-set"][5])
        self.assertIn("no handling site", cells["flag-unread"][5])
        self.assertIn("not counted: no arm of `src/demo.rs` reads it", cells["flag-unread"][5])
        self.assertEqual("none", cells["flag-gap"][5], "a gap row's cells are not the reach cell's")

    def test_a_searched_row_links_its_arm_search_record_and_no_other_row_does(self) -> None:
        records = self.repo / "docs" / "openapi-surface" / "golden-reach-witnesses" / "searches"
        records.mkdir(parents=True)
        (records / "flag-set.md").write_text("# Arm search: `flag-set`\n", encoding="utf-8")
        self.assertEqual(0, self.run_report("--write").returncode)
        cells = self.cells()
        self.assertIn(
            "; arm search [record](golden-reach-witnesses/searches/flag-set.md)", cells["flag-set"][5]
        )
        self.assertNotIn("arm search", cells["flag-orphan"][5])

    def test_a_row_declared_only_by_a_source_without_a_golden_says_so(self) -> None:
        self.assertEqual(0, self.run_report("--write").returncode)
        cell = self.cells()["flag-orphan"][5]
        self.assertIn("**no** golden-only witness", cell)
        self.assertIn("`dropped-doc`, which carries no committed golden", cell)

    def test_report_is_idempotent_over_its_own_output(self) -> None:
        self.assertEqual(0, self.run_report("--write").returncode)
        first = (self.repo / "docs" / "openapi-surface" / "demo.md").read_text(encoding="utf-8")
        again = self.run_report("--write")
        self.assertIn("wrote the ledger and 0 reach cell(s)", again.stdout)
        self.assertEqual(first, (self.repo / "docs" / "openapi-surface" / "demo.md").read_text(encoding="utf-8"))

    def test_a_site_table_missing_a_golden_row_is_refused(self) -> None:
        table = self.repo / "docs" / "openapi-surface" / "golden-reach-sites.tsv"
        table.write_text("\n".join(SITES.splitlines()[:-1]) + "\n", encoding="utf-8")
        run = self.run_report()
        self.assertNotEqual(0, run.returncode)
        self.assertIn("missing ['flag-unread']", run.stderr)

    def test_a_missing_measurement_names_the_recipe_that_takes_it(self) -> None:
        (self.measurement / "universe.json").unlink()
        run = self.run_report()
        self.assertNotEqual(0, run.returncode)
        self.assertIn("just golden-reach", run.stderr)

    def test_a_profile_llvm_cannot_read_fails_with_its_stderr_and_the_rebuild(self) -> None:
        profdata = golden_reach._llvm_tool("llvm-profdata")
        with tempfile.TemporaryDirectory() as scratch:
            raw = Path(scratch) / "stale.profraw"
            raw.write_bytes(b"not a profile")
            with self.assertRaises(SystemExit) as refused:
                golden_reach.run_llvm(
                    [profdata, "merge", "-sparse", str(raw), "-o", str(Path(scratch) / "m.profdata")]
                )
        message = str(refused.exception)
        self.assertIn("`llvm-profdata merge` exited", message)
        self.assertIn("stale.profraw", message)
        self.assertIn("just golden-reach", message)


_search_spec = importlib.util.spec_from_file_location(
    "golden_reach_search", REPO / "scripts" / "golden-reach-search.py"
)
assert _search_spec and _search_spec.loader
golden_reach_search = importlib.util.module_from_spec(_search_spec)
sys.modules["golden_reach_search"] = golden_reach_search
_search_spec.loader.exec_module(golden_reach_search)


class ArmSearchTests(unittest.TestCase):
    """What `golden-reach-search.py` decides without a network: its readings of bytes."""

    def document(self, text: str, suffix: str = ".yaml") -> Path:
        directory = tempfile.TemporaryDirectory(prefix="golden-reach-search-test-")
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / f"openapi{suffix}"
        path.write_text(textwrap.dedent(text), encoding="utf-8")
        return path

    def test_a_parameterized_media_key_is_counted_and_a_malformed_one_is_not(self) -> None:
        """The `media-type-key-parameters` reading, over a real document on disk."""
        path = self.document(
            """\
            openapi: 3.0.3
            info: {title: demo, version: "1"}
            paths:
              /a:
                get:
                  responses:
                    "200":
                      description: ok
                      content:
                        application/json; charset=utf-8: {schema: {type: string}}
                        text/plain; utf-8: {schema: {type: string}}
                        application/json: {schema: {type: string}}
            """
        )
        self.assertEqual(1, golden_reach_search.predicate_count("media-type-key-parameters", path))

    def test_a_swagger_2_document_declares_nothing_a_search_can_use(self) -> None:
        path = self.document(
            """\
            swagger: "2.0"
            info: {title: demo, version: "1"}
            paths:
              /a:
                get:
                  produces: [application/json; charset=utf-8]
                  responses:
                    "200":
                      description: ok
                      content:
                        application/json; charset=utf-8: {schema: {type: string}}
            """
        )
        self.assertEqual(0, golden_reach_search.predicate_count("media-type-key-parameters", path))

    def test_a_pin_s_blob_is_the_hash_git_itself_computes(self) -> None:
        path = self.document('{"openapi": "3.1.0"}\n', ".json")
        git = subprocess.run(["git", "hash-object", str(path)], capture_output=True, text=True, check=True)
        self.assertEqual(git.stdout.strip(), golden_reach_search.git_blob(path.read_bytes()))

    def test_a_result_path_holding_a_space_is_quoted_once(self) -> None:
        url = "https://api.github.com/repositories/1/contents/REST Bindings/openapi.yaml?ref=abc"
        quoted = golden_reach_search._quoted(url)
        self.assertEqual(
            "https://api.github.com/repositories/1/contents/REST%20Bindings/openapi.yaml?ref=abc", quoted
        )
        self.assertEqual(quoted, golden_reach_search._quoted(quoted))

    def test_filing_a_source_s_records_again_never_repeats_a_row(self) -> None:
        """The records a probe files on top of a walk's, read back from disk once each."""
        directory = tempfile.TemporaryDirectory(prefix="golden-reach-search-evidence-")
        self.addCleanup(directory.cleanup)
        original = golden_reach_search.EVIDENCE
        golden_reach_search.EVIDENCE = Path(directory.name)
        self.addCleanup(setattr, golden_reach_search, "EVIDENCE", original)
        walk = [
            {"key": "k", "kind": "walk", "subject": "t@" + "0" * 40, "result": "2", "file": "enumeration.tsv.gz"},
            {"key": "k", "kind": "document", "subject": "a.yaml", "result": "census 1", "file": "enumeration.tsv.gz"},
        ]
        golden_reach_search.write_records("jentic", {"k"}, walk)
        golden_reach_search.file_probes(
            "jentic", "k", [{"key": "k", "candidate": "a.yaml", "status": "generated", "reached": ["site"]}]
        )
        golden_reach_search.file_probes(
            "jentic", "k", [{"key": "k", "candidate": "a.yaml", "status": "generated", "reached": ["site"]}]
        )
        rows = golden_reach_search.read_records("jentic")
        self.assertEqual(2, len(rows), "probing names no candidate; screening does")
        screen = argparse.Namespace(
            source="jentic", key="k", candidate="a.yaml", licence="passed", ref="passed",
            fern="failed: Fern check reports 1 error", gap_keys="", evidence="", declined="",
        )
        golden_reach_search.screen(screen)
        golden_reach_search.screen(screen)
        rows = golden_reach_search.read_records("jentic")
        self.assertEqual(6, len(rows), rows)
        self.assertEqual(
            [("candidate", "census 1")], [(r["kind"], r["result"]) for r in rows if r["kind"] == "candidate"]
        )

    def test_a_row_naming_its_witness_by_fixture_is_read_with_its_predicate(self) -> None:
        self.assertEqual(
            ("predicate:media-type-key-parameters",),
            golden_reach_search.selectors_of("media-type-key-parameters"),
        )
        self.assertEqual(("schema.anyOf>schema.oneOf",), golden_reach_search.selectors_of("anyof-oneof-variant"))


class UnreadableReasonTests(unittest.TestCase):
    """An unreadable document's status names it and keeps the census's whole reason."""

    def test_a_parse_refusal_names_the_document_and_its_line_not_the_local_copy(self) -> None:
        import hashlib
        with tempfile.TemporaryDirectory() as scratch:
            local = Path(scratch) / ("deep/" * 12) / "openapi.yaml"
            local.parent.mkdir(parents=True)
            local.write_text("openapi: 3.0.0\ninfo:\n  ? explicit\n  : key\n", encoding="utf-8")
            digest = hashlib.sha256(local.read_bytes()).hexdigest()
            result = golden_reach_search._census_one(
                (str(local), digest, "yaml/Pinned-v1.yaml", (("k", ("schema.oneOf",)),)))
        status = result["status"]
        self.assertTrue(status.startswith("unreadable: DocumentError: yaml/Pinned-v1.yaml: line 3: "), status)
        self.assertIn("explicit `? ` mapping keys are not supported", status)
        self.assertNotIn(scratch, status)


class MeasurementInputTests(unittest.TestCase):
    """A missing or malformed measurement or record names the step that makes it."""

    def test_a_measurement_with_no_provenance_names_the_recipe(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            with self.assertRaises(SystemExit) as refused:
                golden_reach.measured_commit(Path(scratch))
            self.assertIn("just golden-reach", str(refused.exception))
            (Path(scratch) / "provenance.json").write_text('{"commit": "main"}', encoding="utf-8")
            with self.assertRaises(SystemExit) as refused:
                golden_reach.measured_commit(Path(scratch))
            self.assertIn("not a commit", str(refused.exception))
            commit = "a" * 40
            (Path(scratch) / "provenance.json").write_text(json.dumps({"commit": commit}), encoding="utf-8")
            self.assertEqual(commit, golden_reach.measured_commit(Path(scratch)))

    def test_a_tree_that_differs_from_head_is_not_measured(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            git = ["git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", scratch]
            subprocess.run([*git, "init", "-q"], check=True)
            (root / "ir.rs").write_text("fn a() {}\n", encoding="utf-8")
            subprocess.run([*git, "add", "ir.rs"], check=True)
            subprocess.run([*git, "commit", "-q", "-m", "base"], check=True)
            (root / "ir.rs").write_text("fn b() {}\n", encoding="utf-8")
            with self.assertRaises(SystemExit) as refused:
                golden_reach.measure(argparse.Namespace(repo_root=root, out=root / "out"))
            self.assertIn("ir.rs", str(refused.exception))
            self.assertIn("commit them first", str(refused.exception))
            self.assertFalse((root / "out").exists())

    def test_a_records_file_with_another_header_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            evidence = golden_reach_search.EVIDENCE
            golden_reach_search.EVIDENCE = Path(scratch)
            self.addCleanup(setattr, golden_reach_search, "EVIDENCE", evidence)
            (Path(scratch) / "jentic").mkdir()
            (Path(scratch) / "jentic" / "records.tsv").write_text("key\tsubject\nk\tx\n", encoding="utf-8")
            with self.assertRaises(SystemExit) as refused:
                golden_reach_search.read_records("jentic")
            self.assertIn("not ['key', 'kind', 'subject', 'result', 'file']", str(refused.exception))


class ArmSearchOutcomeTests(unittest.TestCase):
    """A search reads `exhausted` only when nothing is outstanding on a build `src/` still matches."""

    SETTLED = {"declarers": 3, "unreadable": 0, "probed": 3, "timeouts": 0, "unprofiled": 0,
               "failed": 0, "reaching": 0, "screened": 0, "passing": 0}

    def test_a_settled_search_on_an_unmoved_src_is_exhausted(self) -> None:
        self.assertEqual("exhausted", golden_reach_search._outcome({"jentic": dict(self.SETTLED)}))

    def test_every_kind_of_outstanding_declarer_keeps_the_search_incomplete(self) -> None:
        for field, value in (("probed", 2), ("timeouts", 1), ("unprofiled", 1), ("unreadable", 1)):
            with self.subTest(field=field):
                tally = dict(self.SETTLED, **{field: value})
                self.assertEqual(1, golden_reach_search._outstanding(tally))
                self.assertEqual("search-incomplete", golden_reach_search._outcome({"jentic": tally}))

    def test_a_moved_src_keeps_even_a_settled_search_incomplete(self) -> None:
        self.assertEqual(
            "search-incomplete",
            golden_reach_search._outcome({"jentic": dict(self.SETTLED)}, src_moved=True),
        )

    def test_the_commits_since_a_build_are_read_off_git(self) -> None:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True,
                              text=True, check=True).stdout.strip()
        self.assertEqual([], golden_reach_search.src_commits_since(head))
        with self.assertRaises(SystemExit) as refused:
            golden_reach_search.src_commits_since("0" * 40)
        self.assertIn("just golden-reach", str(refused.exception))


class RecipeTests(unittest.TestCase):
    def test_the_recipes_drive_this_script_and_write_the_census_it_reads(self) -> None:
        body = recipe_body("golden-reach")
        self.assertIn("scripts/golden-reach.py measure", body)
        self.assertIn("openapi-surface-census.py --json > .local/golden-reach/census.json", body)
        self.assertIn("scripts/golden-reach.py report --write", body)
        self.assertIn("scripts/golden-reach.py report --write", recipe_body("golden-reach-report"))
        self.assertEqual(REPO / ".local" / "golden-reach", golden_reach.DEFAULT_OUT)


if __name__ == "__main__":
    unittest.main()
