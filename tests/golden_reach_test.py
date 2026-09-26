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
  against, and a result URL's quoting — over real bytes, and its `walk`, `screen`
  and `render` stages through `main` over real documents. Its `query` and
  `fetch-pins` stages run the real guarded acquirer against a loopback server.
  Its `probe` stage runs the instrumented build `measure` makes, so it stays
  outside `just check` as `measure` does; only its refusal of a stale build is
  driven here. What the stages commit is checked by `RankedBacklogTests`'
  reconciliation of every arm-search record.
"""

from __future__ import annotations

import argparse
import base64
import contextlib
import csv
import gzip
import hashlib
import importlib.util
import io
import os
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from unittest import mock
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

    def run_sites(self, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--repo-root", str(self.repo), "sites", *extra],
            capture_output=True, text=True,
        )

    def test_sites_resolves_every_declared_site_and_names_its_span(self) -> None:
        run = self.run_sites("--verbose", "--census", str(self.measurement / "census.json"))
        self.assertEqual(0, run.returncode, run.stderr)
        lines = run.stdout.splitlines()
        self.assertEqual("golden-reach: 3 site(s) across 3 row(s) resolve", lines[-1])
        self.assertTrue(any(line.startswith("src/demo.rs::unrelated\tsrc/demo.rs:") for line in lines), lines)

    def test_sites_refuses_a_row_no_registered_source_declares(self) -> None:
        census = dict(CENSUS, rows=[r for r in CENSUS["rows"] if r["selector"] != "demo.orphan"])
        (self.measurement / "census.json").write_text(json.dumps(census), encoding="utf-8")
        run = self.run_sites("--census", str(self.measurement / "census.json"))
        self.assertNotEqual(0, run.returncode)
        self.assertIn("flag-orphan: no registered source declares any of demo.orphan", run.stderr)

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

    def test_a_tool_is_named_without_the_windows_exe_suffix(self) -> None:
        """Windows' tool path ends `.exe`; the message names the tool as POSIX does."""
        with tempfile.TemporaryDirectory() as scratch:
            if os.name == "nt":
                tool = golden_reach._llvm_tool("llvm-profdata")
            else:
                tool = str(Path(scratch) / "llvm-profdata.exe")
                Path(tool).write_text('#!/bin/sh\necho "$3: truncated profile data" >&2\nexit 1\n', encoding="utf-8")
                os.chmod(tool, 0o755)
            self.assertTrue(tool.lower().endswith(".exe"), tool)
            with self.assertRaises(SystemExit) as refused:
                golden_reach.run_llvm([tool, "merge", "-sparse", str(Path(scratch) / "stale.profraw")])
        self.assertIn("`llvm-profdata merge` exited 1", str(refused.exception))
        self.assertEqual("llvm-profdata", golden_reach.tool_name(r"C:\rustlib\bin\llvm-profdata.EXE"))
        self.assertEqual("llvm-cov", golden_reach.tool_name("/rustlib/bin/llvm-cov"))


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
        """Over the bytes as they are: `--no-filters`, so no host's line-ending setting intervenes."""
        path = self.document("", ".json")
        path.write_bytes(b'{\r\n"openapi": "3.1.0"}\n')
        git = subprocess.run(["git", "hash-object", "--no-filters", str(path)],
                             capture_output=True, text=True, check=True)
        self.assertEqual(git.stdout.strip(), golden_reach_search.git_blob(path.read_bytes()))

    def test_a_checkout_s_converted_line_endings_keep_the_committed_blob(self) -> None:
        """A Windows checkout writes CRLF over a blob committed with LF; the pin names the blob."""
        directory = tempfile.TemporaryDirectory(prefix="golden-reach-search-checkout-")
        self.addCleanup(directory.cleanup)
        repo = Path(directory.name)

        def git(*argv: str) -> str:
            return subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@t",
                                   "-c", "commit.gpgsign=false", *argv],
                                  capture_output=True, text=True, check=True).stdout.strip()

        git("init", "-q")
        git("config", "core.autocrlf", "false")
        committed = b'{\n"openapi": "3.1.0"}\n'
        path = repo / "openapi.json"
        path.write_bytes(committed)
        git("add", "openapi.json")
        git("commit", "-q", "-m", "pin")
        git("config", "core.autocrlf", "true")
        path.unlink()
        git("checkout", "--", "openapi.json")
        self.assertEqual(committed.replace(b"\n", b"\r\n"), path.read_bytes(), "the checkout converted it")
        self.assertEqual("", git("status", "--porcelain"), "git reads the converted copy as unmodified")
        pinned = git("rev-parse", "HEAD:openapi.json")
        self.assertNotEqual(pinned, golden_reach_search.git_blob(path.read_bytes()))
        self.assertEqual(committed, golden_reach_search.committed_bytes(path))
        self.assertEqual(pinned, golden_reach_search.git_blob(golden_reach_search.committed_bytes(path)))
        untracked = repo / "other.json"
        untracked.write_bytes(b"{}\r\n")
        self.assertEqual(b"{}\r\n", golden_reach_search.committed_bytes(untracked))

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
            fern="failed: Fern check reports 1 error", gap_keys="", evidence="", declined="", registered="",
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
                golden_reach.measure(argparse.Namespace(repo_root=root, out=root / "out", tests=None))
            self.assertIn("ir.rs", str(refused.exception))
            self.assertIn("commit them first", str(refused.exception))
            self.assertFalse((root / "out").exists())

    def test_a_tests_filter_that_is_no_regex_is_refused_before_anything_builds(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            with self.assertRaises(SystemExit) as refused:
                golden_reach.main(["--repo-root", scratch, "--out", str(Path(scratch) / "out"),
                                   "measure", "--tests", "golden_(("])
            self.assertIn("--tests 'golden_((' is not a regex", str(refused.exception))
            self.assertFalse((Path(scratch) / "out").exists())

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


    def test_a_ledger_row_with_a_field_missing_or_a_count_garbled_is_refused(self) -> None:
        committed = golden_reach.LEDGER.read_text(encoding="utf-8").splitlines()
        row = committed[2].split("\t")
        for label, broken in (("short", "\t".join(row[:-1])), ("garbled", "\t".join(["first", *row[1:]]))):
            with self.subTest(label), tempfile.TemporaryDirectory() as scratch:
                ledger = Path(scratch) / "golden-reach.tsv"
                ledger.write_text("\n".join([*committed[:2], broken]) + "\n", encoding="utf-8")
                with self.assertRaises(SystemExit) as refused:
                    golden_reach.read_ledger(ledger)
                self.assertIn(f"{ledger}:3", str(refused.exception))
                self.assertIn("just golden-reach-report", str(refused.exception))

    def test_a_measurement_or_census_of_another_shape_is_refused_with_the_recipe(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            regions = Path(scratch) / "universe.json"
            census = Path(scratch) / "census.json"
            for path, text, load in (
                (regions, '{"src/ir.rs": [[1, 2, 3]]}', golden_reach.load_regions),
                (regions, "[]", golden_reach.load_regions),
                (census, '{"sources": []}', golden_reach.load_census),
                (census, '{"sources": [], "rows": [{"selector": "schema.oneOf"}]}', golden_reach.load_census),
            ):
                with self.subTest(text):
                    path.write_text(text, encoding="utf-8")
                    with self.assertRaises(SystemExit) as refused:
                        load(path)
                    self.assertIn(str(path), str(refused.exception))
                    self.assertIn("re-run `just golden-reach`", str(refused.exception))
            regions.write_text('{"src/ir.rs": [[1, 2, 3, 4]]}', encoding="utf-8")
            self.assertEqual({"src/ir.rs": {(1, 2, 3, 4)}}, golden_reach.load_regions(regions))

    def test_a_hand_off_file_missing_a_column_is_refused_by_name(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            handoff = Path(scratch) / "handoff.tsv"
            handoff.write_text("golden_key\tcandidate_url\nk\thttps://example.test/a.json\n", encoding="utf-8")
            with self.assertRaises(SystemExit) as refused:
                golden_reach_search.read_tsv(handoff, golden_reach_search.HANDOFF_FIELDS, "restore it from git")
            self.assertIn("'unreached_site'", str(refused.exception))
            self.assertIn("restore it from git", str(refused.exception))


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


class _StageScratch(unittest.TestCase):
    """A scratch evidence tree for the arm search's stages, and three pinned documents.

    The evidence directories are redirected to it; the site table, the reach
    ledger and the census engine are the repository's own.
    """

    KEY = "anyof-oneof-variant"
    DECLARING = """\
        openapi: 3.0.3
        info: {title: declaring, version: "1"}
        paths: {}
        components:
          schemas:
            Pet:
              anyOf:
                - oneOf: [{type: string}, {type: integer}]
                - type: boolean
        """
    PLAIN = """\
        openapi: 3.0.3
        info: {title: plain, version: "1"}
        paths: {}
        components: {schemas: {Pet: {type: string}}}
        """
    UNREADABLE = "openapi: 3.0.0\ninfo:\n  ? explicit\n  : key\n"
    REVISION = "e" * 40

    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory(prefix="golden-reach-search-stage-")
        self.addCleanup(scratch.cleanup)
        self.scratch = Path(scratch.name)
        self.head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True,
                                   text=True, check=True).stdout.strip()
        measurement = self.scratch / "measurement"
        measurement.mkdir()
        (measurement / "provenance.json").write_text(json.dumps({"commit": self.head}), encoding="utf-8")
        surface = self.scratch / "surface"
        for module, name, value in (
            (golden_reach_search, "SURFACE", surface),
            (golden_reach_search, "EVIDENCE", surface / "golden-reach-witnesses"),
            (golden_reach_search, "CACHE", self.scratch / "cache"),
            (golden_reach_search.REACH, "DEFAULT_OUT", measurement),
        ):
            self.addCleanup(setattr, module, name, getattr(module, name))
            setattr(module, name, value)
        self.root = self.scratch / "jentic"
        manifest = ["walk\tdocument\trevision\tsha256"]
        for name, text in (("a.yaml", self.DECLARING), ("b.yaml", self.PLAIN), ("c.yaml", self.UNREADABLE)):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(textwrap.dedent(text), encoding="utf-8")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            manifest.append(f"jentic-public-apis\t{name}\t{self.REVISION}\t{digest}")
        shared = surface / "witness-search-jentic"
        shared.mkdir(parents=True)
        (shared / "acquisition-manifest.tsv").write_text("\n".join(manifest) + "\n", encoding="utf-8")


class ArmSearchStageTests(_StageScratch):
    """The `walk`, `screen`, `render` and `probe` stages driven through `main`."""

    def walk(self) -> None:
        with contextlib.redirect_stdout(io.StringIO()) as printed:
            code = golden_reach_search.main(
                ["walk", "--source", "jentic", "--root", str(self.root), "--key", self.KEY, "--jobs", "1"]
            )
        self.assertEqual(0, code)
        self.assertEqual("golden-reach-search: jentic: 3 documents walked, 1 unreadable\n", printed.getvalue())

    def test_a_walk_records_every_pinned_document_and_the_one_that_declares_the_row(self) -> None:
        self.walk()
        evidence = golden_reach_search.EVIDENCE / "jentic"
        with gzip.open(evidence / "enumeration.tsv.gz", "rt", encoding="utf-8") as handle:
            enumeration = {row["document"]: row for row in csv.DictReader(handle, delimiter="\t")}
        self.assertEqual(self.KEY, enumeration["a.yaml"]["matched_keys"])
        self.assertEqual(("readable", ""), (enumeration["b.yaml"]["status"], enumeration["b.yaml"]["matched_keys"]))
        self.assertTrue(enumeration["c.yaml"]["status"].startswith("unreadable: DocumentError: c.yaml: line 3"))
        records = golden_reach_search.read_records("jentic")
        self.assertEqual(
            [("walk", f"jentic-public-apis@{self.REVISION}", "3"), ("document", "a.yaml", "census 1")],
            sorted(((r["kind"], r["subject"], r["result"]) for r in records), reverse=True),
        )

    def test_a_walk_reads_a_precomputed_census_and_refuses_one_of_another_shape(self) -> None:
        census = self.scratch / "census.jsonl.gz"
        lines = [
            {"document": "a.yaml", "sha256_ok": True, "openapi": "3.0.3", "census": {"schema.anyOf>schema.oneOf": 2}},
            {"document": "b.yaml", "sha256_ok": True, "openapi": "3.0.3", "census": None},
            {"document": "c.yaml", "sha256_ok": True, "error": "TimeoutError after 60s"},
        ]
        with gzip.open(census, "wt", encoding="utf-8") as handle:
            handle.writelines(json.dumps(line) + "\n" for line in lines)
        argv = ["walk", "--source", "jentic", "--root", str(self.root), "--key", self.KEY, "--jobs", "1",
                "--census", str(census)]
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(0, golden_reach_search.main(argv))
        records = {(r["kind"], r["subject"]): r["result"] for r in golden_reach_search.read_records("jentic")}
        self.assertEqual("census 2", records[("document", "a.yaml")])
        with gzip.open(census, "wt", encoding="utf-8") as handle:
            handle.write(json.dumps({"document": "a.yaml", "census": {"schema.anyOf>schema.oneOf": "two"}}) + "\n")
        with self.assertRaises(SystemExit) as refused:
            golden_reach_search.main(argv)
        self.assertIn(f"{census}:1", str(refused.exception))
        self.assertIn("take the walk census again", str(refused.exception))

    def test_render_writes_one_line_per_declared_source_and_counts_what_is_outstanding(self) -> None:
        self.walk()
        golden_reach_search.file_probes("jentic", self.KEY, [
            {"key": self.KEY, "candidate": "a.yaml", "status": "generated", "build": self.head[:12],
             "reached": list(golden_reach_search.unreached_sites(self.KEY))},
        ])
        golden_reach_search.main([
            "screen", "--source", "jentic", "--key", self.KEY, "--candidate", "a.yaml",
            "--licence", "passed", "--ref", "passed", "--fern", "failed: Fern check reports 1 error",
        ])
        self.assertEqual(0, golden_reach_search.main(["render", "--key", self.KEY]))
        record = (golden_reach_search.EVIDENCE / "searches" / f"{self.KEY}.md").read_text(encoding="utf-8")
        lines = [line for line in record.splitlines() if line.startswith(f"| `{self.KEY}` |")]
        self.assertEqual(list(golden_reach_search.DECLARED_SOURCES),
                         [line.split(" | ")[1].strip("`") for line in lines])
        jentic = next(line for line in lines if "| `jentic` |" in line)
        self.assertIn("`search-incomplete`", jentic)
        self.assertIn(f"`jentic-public-apis` at `{self.REVISION}` → 3 documents", jentic)
        self.assertIn("`a.yaml` licence `passed` ref `passed` fern `failed: Fern check reports 1 error`", jentic)
        # One declarer, probed and reaching the arm and screened; the unreadable
        # document is the one outstanding item.
        self.assertIn("| `jentic` | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 |", record)
        self.assertIn(f"build `{self.head[:12]}` only", record)
        self.assertNotIn("had moved since that build", record)

    def test_a_screened_candidate_filed_as_registered_renders_as_its_disposition(self) -> None:
        self.walk()
        screen = ["screen", "--source", "jentic", "--key", self.KEY, "--candidate", "a.yaml",
                  "--licence", "passed", "--ref", "passed", "--fern", "passed"]
        with self.assertRaises(SystemExit) as refused:
            golden_reach_search.main(screen + ["--registered", "corpus row 1", "--declined", "a duplicate"])
        self.assertIn("registered or declined, not both", str(refused.exception))
        self.assertEqual(0, golden_reach_search.main(screen + ["--registered", "corpus row 1 (`a`)"]))
        self.assertEqual(0, golden_reach_search.main(["render", "--key", self.KEY]))
        record = (golden_reach_search.EVIDENCE / "searches" / f"{self.KEY}.md").read_text(encoding="utf-8")
        self.assertIn("- **Registered** (`jentic`): `a.yaml` — corpus row 1 (`a`)", record.splitlines())

    def test_render_as_of_an_earlier_build_keeps_the_searched_arm_and_counts_that_builds_probes(self) -> None:
        touched = subprocess.run(["git", "log", "-1", "--format=%H", "--", "src/"], cwd=REPO,
                                 capture_output=True, text=True, check=True).stdout.strip()
        before = subprocess.run(["git", "rev-parse", "--verify", "-q", f"{touched}^"], cwd=REPO,
                                capture_output=True, text=True)
        if before.returncode != 0:
            self.skipTest("a shallow clone holds no commit before src/'s latest change")
        earlier = before.stdout.strip()[:12]
        self.walk()
        self.assertEqual(0, golden_reach_search.main(["render", "--key", self.KEY]))
        path = golden_reach_search.EVIDENCE / "searches" / f"{self.KEY}.md"
        # The arm this record searched for, since reached by a registered witness:
        # the ledger no longer names it, and the re-render must keep it.
        searched = "The unreached handling site(s) searched for: `src/ir.rs::since_reached`."
        path.write_text(re.sub(r"(?m)^The unreached handling site\(s\) searched for: .*$", searched,
                               path.read_text(encoding="utf-8")), encoding="utf-8")
        golden_reach_search.file_probes("jentic", self.KEY, [
            {"key": self.KEY, "candidate": "a.yaml", "status": "generated", "build": earlier, "reached": []},
        ])
        self.assertEqual(0, golden_reach_search.main(["render", "--key", self.KEY, "--build", earlier]))
        record = path.read_text(encoding="utf-8")
        self.assertIn(searched, record.splitlines())
        self.assertIn(f"build of commit `{earlier}`, the one the reach ledger was measured on when these probes ran,",
                      " ".join(record.split()))
        # The earlier build's probe counts; only the unreadable document is outstanding.
        self.assertIn("| `jentic` | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |", record)
        self.assertIn("had moved since that build", record)
        self.assertNotIn("The arm this search looked for is now reached", record)
        # A witness registered since reaches every site: the ledger, re-read from a
        # copy whose row is fully reached, and the record says the arm is closed.
        ledger = self.scratch / "golden-reach.tsv"
        rows = golden_reach_search.REACH.LEDGER.read_text(encoding="utf-8").splitlines()
        for number, row in enumerate(rows):
            cells = row.split("\t")
            if len(cells) > 8 and cells[1] == self.KEY:
                cells[3] = "0"
                cells[8] = re.sub(r"=(\d+)/(\d+)", r"=\2/\2", cells[8])
                rows[number] = "\t".join(cells)
        ledger.write_text("\n".join(rows) + "\n", encoding="utf-8")
        original = golden_reach_search.REACH.read_ledger
        self.addCleanup(setattr, golden_reach_search.REACH, "read_ledger", original)
        golden_reach_search.REACH.read_ledger = lambda: original(ledger)
        self.assertEqual((), golden_reach_search.ledger_unreached(self.KEY))
        self.assertEqual(0, golden_reach_search.main(["render", "--key", self.KEY, "--build", earlier]))
        record = path.read_text(encoding="utf-8")
        self.assertIn(searched, record.splitlines())
        self.assertIn("The arm this search looked for is now reached", record)
        with self.assertRaises(SystemExit) as refused:
            golden_reach_search.main(["render", "--key", self.KEY, "--build", "0" * 40])
        self.assertIn("names no commit in this checkout", str(refused.exception))
        path.unlink()
        with self.assertRaises(SystemExit) as refused:
            golden_reach_search.main(["render", "--key", self.KEY, "--build", earlier])
        self.assertIn("states no arm it searched for", str(refused.exception))

    def test_a_probe_refuses_a_build_src_has_moved_from(self) -> None:
        touched = subprocess.run(["git", "log", "-1", "--format=%H", "--", "src/"], cwd=REPO,
                                 capture_output=True, text=True, check=True).stdout.strip()
        before = subprocess.run(["git", "rev-parse", "--verify", "-q", f"{touched}^"], cwd=REPO,
                                capture_output=True, text=True)
        if before.returncode != 0:
            self.skipTest("a shallow clone holds no commit before src/'s latest change")
        (golden_reach_search.REACH.DEFAULT_OUT / "provenance.json").write_text(
            json.dumps({"commit": before.stdout.strip()}), encoding="utf-8")
        with self.assertRaises(SystemExit) as refused:
            golden_reach_search.main(["probe", "--source", "jentic", "--key", self.KEY, "--root", str(self.root)])
        self.assertIn("re-run `just golden-reach`", str(refused.exception))


class _Loopback(BaseHTTPRequestHandler):
    """GitHub's REST search, contents and rate-limit routes, and its exact-commit raw route."""

    COMMIT = "b" * 40

    def log_message(self, *args: object) -> None:
        pass

    def do_GET(self) -> None:
        base = f"http://127.0.0.1:{self.server.server_port}"
        declaring = textwrap.dedent(_StageScratch.DECLARING).encode()
        if self.path == "/rate_limit":
            bucket = {"limit": 100, "used": 0, "remaining": 100, "reset": int(time.time()) + 60}
            self.reply(200, {"resources": {"code_search": bucket, "core": bucket}})
        elif self.path.startswith("/search/code"):
            if "refused" in urllib.parse.unquote_plus(self.path):
                self.reply(422, {"message": "Validation Failed"})
            else:
                self.reply(200, {"total_count": 2, "items": [{
                    "repository": {"full_name": "example/api"}, "path": "openapi.yaml",
                    "sha": golden_reach_search.git_blob(declaring),
                    "url": f"{base}/repos/example/api/contents/openapi.yaml?ref={self.COMMIT}",
                }]})
        elif self.path.startswith("/repos/example/api/contents/openapi.yaml"):
            self.reply(200, {"encoding": "base64", "content": base64.b64encode(declaring).decode()})
        elif self.path == f"/example/api/{self.COMMIT}/fetched.yaml":
            fetched = declaring + b"# no local copy holds these bytes\n"
            self.send_response(200)
            self.send_header("Content-Length", str(len(fetched)))
            self.end_headers()
            self.wfile.write(fetched)
        else:
            self.reply(404, {"message": "Not Found"})

    def reply(self, status: int, body: object) -> None:
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("X-Ratelimit-Resource", "code_search" if self.path.startswith("/search/") else "core")
        self.end_headers()
        self.wfile.write(data)


class ArmSearchNetworkStageTests(_StageScratch):
    """`query` and `fetch-pins` through the real guarded acquirer, against a loopback server."""

    def setUp(self) -> None:
        super().setUp()
        server = ThreadingHTTPServer(("127.0.0.1", 0), _Loopback)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        environment = mock.patch.dict(os.environ, {"CROZIER_GITHUB_API_URL": url, "GITHUB_TOKEN": "offline-test-token"})
        environment.start()
        self.addCleanup(environment.stop)
        options = {"github_url": url, "sourcegraph_url": url, "raw_github_url": url,
                   "code_search_spacing_s": 0.01, "code_search_refusal_cooldown_s": 0.01}
        self.addCleanup(setattr, golden_reach_search, "ACQUIRER_OPTIONS", golden_reach_search.ACQUIRER_OPTIONS)
        golden_reach_search.ACQUIRER_OPTIONS = options

    def test_a_query_records_each_phrasing_s_answer_and_censuses_what_it_fetched(self) -> None:
        queries = self.scratch / "queries.tsv"
        queries.write_text(
            f"key\tsource\tphrasing\n{self.KEY}\tgithub-code-search\tanyOf oneOf\n"
            f"{self.KEY}\tgithub-code-search\trefused anyOf\n", encoding="utf-8")
        self.addCleanup(setattr, golden_reach_search, "QUERIES", golden_reach_search.QUERIES)
        golden_reach_search.QUERIES = queries
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(0, golden_reach_search.main(["query", "--source", "github-code-search", "--key", self.KEY]))
        rows = {(r["kind"], r["subject"]): r["result"] for r in golden_reach_search.read_records("github-code-search")}
        self.assertEqual("2", rows[("query", "anyOf oneOf")])
        self.assertEqual("unanswered: HTTP 422 refused", rows[("query", "refused anyOf")])
        self.assertEqual("census 1", rows[("document", f"example/api:openapi.yaml@{_Loopback.COMMIT}")])
        self.assertIn(("wait", "github-code-search guard log rate-limit-calls.jsonl"), rows)

    def test_fetch_pins_resolves_a_local_copy_fetches_a_missing_one_and_leaves_a_wrong_blob_unresolved(self) -> None:
        fetched = textwrap.dedent(self.DECLARING).encode() + b"# no local copy holds these bytes\n"
        pins = [
            {"repository": "example/api", "path": "a.yaml", "commit": _Loopback.COMMIT,
             "blob": golden_reach_search.git_blob((self.root / "a.yaml").read_bytes())},
            {"repository": "example/api", "path": "fetched.yaml", "commit": _Loopback.COMMIT,
             "blob": golden_reach_search.git_blob(fetched)},
            {"repository": "example/api", "path": "gone.yaml", "commit": _Loopback.COMMIT, "blob": "0" * 40},
        ]
        shared = golden_reach_search.SURFACE / "witness-search-github-publisher-trees"
        shared.mkdir(parents=True)
        (shared / "documents.jsonl").write_text("".join(json.dumps(p) + "\n" for p in pins), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()) as printed:
            self.assertEqual(0, golden_reach_search.main(["fetch-pins", "--root", str(self.root)]))
        self.assertEqual("golden-reach-search: github-publisher-trees: 3 pins, 1 fetched, 1 unresolved\n",
                         printed.getvalue())
        listing = {row["document"]: row["sha256"] for row in golden_reach_search.pinned_listing("github-publisher-trees")}
        self.assertEqual(hashlib.sha256((self.root / "a.yaml").read_bytes()).hexdigest(), listing["a.yaml"])
        self.assertEqual(hashlib.sha256(fetched).hexdigest(), listing["fetched.yaml"])
        self.assertEqual("", listing["gone.yaml"])


WITHOUT_POSIX = REPO / "tests" / "without-posix-modules"
# The maintenance scripts `check` drives on every OS, Windows included, so each must
# import without the POSIX-only modules; the rate-limit guard comes in through the
# ones that search.
PORTABLE_SCRIPTS = (
    "golden-reach.py",
    "golden-reach-search.py",
    "llmlint-diff.py",
    "openapi-surface-census.py",
    "witness-scrape-wide.py",
    "witness-search-github.py",
)
LOCK_HOLDER = """\
import importlib.util, os, sys, time
from pathlib import Path
spec = importlib.util.spec_from_file_location("golden_reach_search", sys.argv[1])
search = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = search
spec.loader.exec_module(search)
scratch, key = Path(sys.argv[2]), sys.argv[3]
search.CACHE, search.EVIDENCE = scratch / "cache", scratch / "evidence"
search.CACHE.mkdir(parents=True, exist_ok=True)
log = os.open(scratch / "held.log", os.O_WRONLY | os.O_APPEND | os.O_CREAT)
with search.exclusive_lock(search.CACHE / "jentic.probe.lock"):
    os.write(log, f"enter {key}\\n".encode())
    time.sleep(0.3)
    os.write(log, f"leave {key}\\n".encode())
search.file_probes("jentic", key, [{"key": key, "candidate": "a.yaml", "status": "generated", "reached": []}])
print("fcntl" if search.fcntl else "msvcrt" if search.msvcrt else "exclusive-create")
"""


def python_env(*, posix_modules: bool) -> dict[str, str]:
    """This environment with the POSIX-only modules importable or, as on Windows, not."""
    kept = [p for p in os.environ.get("PYTHONPATH", "").split(os.pathsep)
            if p and Path(p).resolve() != WITHOUT_POSIX]
    return dict(os.environ, PYTHONPATH=os.pathsep.join(kept if posix_modules else [str(WITHOUT_POSIX), *kept]))


class WithoutPosixModulesTests(unittest.TestCase):
    """The scripts run where `fcntl` and the other POSIX-only modules do not exist.

    Windows has none of them; the `check (windows-latest)` leg is where this
    used to fail, at import. `just test-fixtures-coverage` also runs this whole
    suite under the same condition.
    """

    def test_the_shadow_makes_every_posix_only_module_unimportable(self) -> None:
        for name in ("fcntl", "grp", "pwd", "resource", "termios"):
            with self.subTest(name):
                run = subprocess.run([sys.executable, "-c", f"import {name}"], capture_output=True, text=True,
                                     env=python_env(posix_modules=False))
                self.assertNotEqual(0, run.returncode)
                self.assertIn(f"import of {name} halted", run.stderr)

    def test_every_script_runs_its_command_line_without_them(self) -> None:
        for script in PORTABLE_SCRIPTS:
            with self.subTest(script):
                run = subprocess.run([sys.executable, str(REPO / "scripts" / script), "--help"],
                                     capture_output=True, text=True, env=python_env(posix_modules=False))
                self.assertEqual(0, run.returncode, run.stderr)
                self.assertIn("usage:", run.stdout)

    def test_the_probe_lock_admits_one_process_at_a_time_with_or_without_them(self) -> None:
        for posix_modules in (True, False):
            with self.subTest(posix_modules=posix_modules), tempfile.TemporaryDirectory() as scratch:
                keys = ("k1", "k2", "k3")
                holders = [
                    subprocess.Popen(
                        [sys.executable, "-c", LOCK_HOLDER, str(REPO / "scripts" / "golden-reach-search.py"),
                         scratch, key],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                        env=python_env(posix_modules=posix_modules),
                    )
                    for key in keys
                ]
                mechanisms = set()
                for holder in holders:
                    out, err = holder.communicate(timeout=120)
                    self.assertEqual(0, holder.returncode, err)
                    mechanisms.add(out.strip())
                if not posix_modules:
                    self.assertNotIn("fcntl", mechanisms)
                elif os.name != "nt":
                    self.assertEqual({"fcntl"}, mechanisms)
                held = (Path(scratch) / "held.log").read_text(encoding="utf-8").split()
                spans = [held[i:i + 4] for i in range(0, len(held), 4)]
                self.assertEqual(len(keys), len(spans), held)
                for enter, key, leave, same in spans:
                    self.assertEqual(("enter", "leave", key), (enter, leave, same), f"two holders overlapped: {held}")
                self.assertEqual(set(keys), {row["key"] for row in golden_reach_search.read_jsonl(
                    Path(scratch) / "evidence" / "jentic" / "probe.jsonl", ("key",), "")})
                self.assertFalse(any(Path(scratch, "cache").glob("*.held")), "a released lock left its marker")


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
