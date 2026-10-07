"""Coverage for `tools/fern-refusals/fern-refusals.py`, which builds `docs/fern-refusals/`.

The script derives the refused-document population from committed records and
writes `documents.tsv`, `unretrievable.tsv` and `classes.tsv`'s `documents`
column. These tests drive the REAL script as a user does. `CommittedTables` runs
`check` over the REAL repository and `build` into a scratch copy of the
registry, which must reproduce the committed tables byte for byte. The drift
cases copy the registry to a scratch directory (`CROZIER_FERN_REFUSALS_REGISTRY`)
and break one thing at a time — a header column, a class id a document carries,
a class count, a row order, a class template the population needs — requiring
the failure to name it: without that half, "check passes" would be
indistinguishable from "check reads nothing". `measure` with the compiled
crozier binary is `tools/fern-refusals-strict/`'s suite, which imports the
helpers defined here.

Run: `just test-fern-refusals` (part of `just check`).
"""

from __future__ import annotations

import contextlib
import gzip
import io
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "fern-refusals" / "fern-refusals.py"
REGISTRY = REPO / "docs" / "fern-refusals"
CONFIRMATIONS = REPO / "docs" / "openapi-surface" / "fern-refusals" / "confirmations.tsv"
TABLES = ("classes.tsv", "documents.tsv", "generated.tsv", "unretrievable.tsv")


def run(*args: str, registry: Path | None = None,
        confirmations: Path | None = None) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env.pop("CROZIER_FERN_REFUSALS_REGISTRY", None)
    env.pop("CROZIER_FERN_REFUSALS_CONFIRMATIONS", None)
    if registry is not None:
        env["CROZIER_FERN_REFUSALS_REGISTRY"] = str(registry)
    if confirmations is not None:
        env["CROZIER_FERN_REFUSALS_CONFIRMATIONS"] = str(confirmations)
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, env=env,
                          cwd=REPO)


def rows(path: Path) -> list[list[str]]:
    return [line.split("\t") for line in path.read_text(encoding="utf-8").splitlines()]


def write_rows(path: Path, table: list[list[str]]) -> None:
    path.write_text("".join("\t".join(row) + "\n" for row in table), encoding="utf-8")


class CommittedTables(unittest.TestCase):
    def test_check_holds_over_the_committed_registry(self) -> None:
        result = run("check")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_build_reproduces_the_committed_tables(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            registry = Path(scratch) / "fern-refusals"
            registry.mkdir()
            for hand_written in ("classes.tsv", "findings.tsv", "documents.tsv"):
                shutil.copy(REGISTRY / hand_written, registry / hand_written)
            result = run("build", registry=registry)
            self.assertEqual(result.returncode, 0, result.stderr)
            for name in TABLES:
                self.assertEqual((registry / name).read_text(encoding="utf-8"),
                                 (REGISTRY / name).read_text(encoding="utf-8"), name)

    def test_rebuild_preserves_strict_measurements_by_digest(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            registry = Path(scratch) / "fern-refusals"
            shutil.copytree(REGISTRY, registry)
            table = rows(registry / "documents.tsv")
            digest = table[1][0]
            table[1][-1] = "1"
            # Identity is the digest, not the row's position in this copy.
            table[1], table[-1] = table[-1], table[1]
            write_rows(registry / "documents.tsv", table)
            result = run("build", registry=registry)
            self.assertEqual(result.returncode, 0, result.stderr)
            measured = next(row for row in rows(registry / "documents.tsv")[1:] if row[0] == digest)
            self.assertEqual(measured[-1], "1")
            result = run("check", registry=registry)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_every_selected_document_is_accounted_for_once(self) -> None:
        result = run("select")
        self.assertEqual(result.returncode, 0, result.stderr)
        selected = [line.split("\t") for line in result.stdout.splitlines()[1:]]
        keys = [row[0] for row in selected]
        self.assertEqual(len(keys), len(set(keys)))
        refused = rows(REGISTRY / "documents.tsv")[1:]
        documents = {row[0] for row in refused} | {row[2] for row in refused}
        generated = {row[4] for row in rows(REGISTRY / "generated.tsv")[1:]} | \
            {row[1] for row in rows(REGISTRY / "generated.tsv")[1:]}
        unretrievable = rows(REGISTRY / "unretrievable.tsv")[1:]
        listed = {row[1] for row in unretrievable}
        self.assertFalse({row[0] for row in refused} & generated, "a document is both refused and generated")
        for name, table in (("documents.tsv", [row[0] for row in refused]),
                            ("generated.tsv", [row[4] for row in rows(REGISTRY / "generated.tsv")[1:]]),
                            ("unretrievable.tsv", [row[1] for row in unretrievable])):
            with self.subTest(table=name):
                self.assertEqual(len(table), len(set(table)), f"{name} lists a document twice")
        for key, _source, locator, *_ in selected:
            with self.subTest(key=key):
                # A document is named by its digest, or by its locator where no
                # record gave a digest; one no record located is named by its key.
                homes = [name for name, names in (("documents.tsv", documents), ("generated.tsv", generated),
                                                  ("unretrievable.tsv", listed))
                         if key in names or locator in names]
                self.assertEqual(1, len(homes), f"{key} is accounted for in {homes or 'none'} of documents.tsv, "
                                                "generated.tsv and unretrievable.tsv, not exactly one")


class Drift(unittest.TestCase):
    def setUp(self) -> None:
        self.scratch = tempfile.TemporaryDirectory()
        self.registry = Path(self.scratch.name) / "fern-refusals"
        shutil.copytree(REGISTRY, self.registry)

    def tearDown(self) -> None:
        self.scratch.cleanup()

    def assert_check_fails_naming(self, *phrases: str) -> None:
        result = run("check", registry=self.registry)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        for phrase in phrases:
            self.assertIn(phrase, result.stderr)

    def test_the_unchanged_copy_holds(self) -> None:
        result = run("check", registry=self.registry)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_a_renamed_header_column_fails(self) -> None:
        for name, column, renamed in (("classes.tsv", "population_strict", "strict_population"),
                                      ("documents.tsv", "crozier_strict_exit", "crozier_strict"),
                                      ("generated.tsv", "findings", "phrases"),
                                      ("unretrievable.tsv", "reason", "why"),
                                      ("findings.tsv", "probe", "document")):
            with self.subTest(table=name):
                original = (self.registry / name).read_text(encoding="utf-8")
                (self.registry / name).write_text(original.replace(column, renamed, 1), encoding="utf-8")
                self.assert_check_fails_naming(f"docs/fern-refusals/{name}: the header must be exactly")
                (self.registry / name).write_text(original, encoding="utf-8")

    def test_a_row_short_of_the_header_fails_naming_its_line(self) -> None:
        table = rows(self.registry / "classes.tsv")
        table[2] = table[2][:-1]
        write_rows(self.registry / "classes.tsv", table)
        result = run("check", registry=self.registry)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn("classes.tsv line 3: 8 column(s) where the header has 9", result.stderr)

    def test_a_document_carrying_an_unknown_class_fails(self) -> None:
        table = rows(self.registry / "documents.tsv")
        table[1][8] = table[1][8] + ",no-such-class"
        write_rows(self.registry / "documents.tsv", table)
        self.assert_check_fails_naming(f"documents.tsv {table[1][0]}: class `no-such-class` is not a classes.tsv row")

    def test_a_miscounted_class_fails(self) -> None:
        table = rows(self.registry / "classes.tsv")
        row = next(row for row in table[1:] if row[5] != "0")
        row[5] = str(int(row[5]) + 1)
        write_rows(self.registry / "classes.tsv", table)
        self.assert_check_fails_naming(f"classes.tsv {row[0]}: documents is {row[5]}")

    def test_unsorted_documents_fail(self) -> None:
        table = rows(self.registry / "documents.tsv")
        table[1], table[2] = table[2], table[1]
        write_rows(self.registry / "documents.tsv", table)
        self.assert_check_fails_naming("documents.tsv: rows are sorted by digest")

    def test_a_template_the_population_needs_fails_the_build(self) -> None:
        table = rows(self.registry / "classes.tsv")
        row = max(table[1:], key=lambda row: int(row[5]))
        row[4] = "A phrase Fern never prints about <…>"
        write_rows(self.registry / "classes.tsv", table)
        self.assert_check_fails_naming("no single class or finding matches")

    def test_the_strict_exit_is_built_only_for_an_evaluated_class(self) -> None:
        table = rows(self.registry / "classes.tsv")
        evaluated = {row[0] for row in table[1:] if row[6] != "unevaluated"}
        committed = rows(REGISTRY / "documents.tsv")[1:]
        # The evaluated class whose withdrawal leaves the most documents with no evaluated class.
        withdrawn = max(sorted(evaluated), key=lambda name: sum(
            set(row[8].split(",")) & evaluated == {name} for row in committed))
        row = next(row for row in table[1:] if row[0] == withdrawn)
        row[6:9] = ["unevaluated", "—", "—"]
        write_rows(self.registry / "classes.tsv", table)
        evaluated.discard(withdrawn)
        result = run("build", registry=self.registry)
        self.assertEqual(result.returncode, 0, result.stderr)
        built = {row[0]: row for row in rows(self.registry / "documents.tsv")[1:]}
        flipped = 0
        for before in committed:
            after = built[before[0]][11]
            with self.subTest(digest=before[0]):
                if set(before[8].split(",")) & evaluated:
                    self.assertEqual(after, before[11])
                else:
                    self.assertEqual(after, "—")
                    flipped += before[11] != "—"
        self.assertGreater(flipped, 0, f"withdrawing {withdrawn} blanked no measured strict exit")

    def test_a_sampled_generation_that_contradicts_its_class_fails(self) -> None:
        confirmations = Path(self.scratch.name) / "confirmations.tsv"
        table = rows(CONFIRMATIONS)
        # The one population document Fern generates from stands in for a
        # confirmation that its class's refusal does not reproduce.
        generated = rows(REGISTRY / "generated.tsv")[1]
        log = next(path for path in (REPO / "docs" / "openapi-surface" / "fern-refusals" / "logs").glob(
            f"{generated[4]}.generate.log"))
        table[1][3:6] = ["0", "40", log.relative_to(REPO).as_posix()]
        write_rows(confirmations, table)
        result = run("check", confirmations=confirmations)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(f"{table[1][0]}: Fern generates from {table[1][1]}", result.stderr)

    def test_a_class_no_sampled_generation_confirms_fails(self) -> None:
        confirmations = Path(self.scratch.name) / "confirmations.tsv"
        table = rows(CONFIRMATIONS)
        dropped = table[1][0]
        write_rows(confirmations, [table[0], *(row for row in table[1:] if row[0] != dropped)])
        result = run("check", confirmations=confirmations)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(f"{dropped}: no real document's generation confirms it", result.stderr)



class MissingInputs(unittest.TestCase):
    """A committed input the population is read from that has gone missing
    fails `select` naming the file and its fix, never with a traceback. The
    script reads its inputs relative to its own checkout, so it runs from a
    scratch one holding only what `select` reads up to the removed file."""

    INPUTS = (
        "tests/fixtures/CORPUS.md",
        "docs/openapi-surface/fern-refusals/dropped-sources.tsv",
        *(f"docs/openapi-surface/golden-reach-witnesses/{source}/enumeration.tsv.gz"
          for source in ("jentic", "apis.guru", "vendor-portals", "github-publisher-trees")),
    )

    def assert_select_names_missing(self, missing: str) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            for relative in ("tools/fern-refusals/fern-refusals.py", *self.INPUTS):
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
                if relative != missing:
                    shutil.copy(REPO / relative, root / relative)
            env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_FERN_REFUSALS")}
            result = subprocess.run([sys.executable, str(root / "tools" / "fern-refusals" / "fern-refusals.py"), "select"],
                                    capture_output=True, text=True, env=env, cwd=root)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn(f"{missing} is missing; restore it from git", result.stderr)

    def test_a_missing_corpus_table_names_it(self) -> None:
        self.assert_select_names_missing("tests/fixtures/CORPUS.md")

    def test_a_missing_enumeration_names_it(self) -> None:
        self.assert_select_names_missing(
            "docs/openapi-surface/golden-reach-witnesses/jentic/enumeration.tsv.gz")

    def test_an_enumeration_without_its_columns_names_them(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            for relative in ("tools/fern-refusals/fern-refusals.py", *self.INPUTS):
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(REPO / relative, root / relative)
            broken = "docs/openapi-surface/golden-reach-witnesses/jentic/enumeration.tsv.gz"
            with gzip.open(root / broken, "wt", encoding="utf-8") as handle:
                handle.write("walk\tdocument\trevision\n")
            env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_FERN_REFUSALS")}
            result = subprocess.run([sys.executable, str(root / "tools" / "fern-refusals" / "fern-refusals.py"), "select"],
                                    capture_output=True, text=True, env=env, cwd=root)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn(f"{broken}: the header lacks sha256", result.stderr)

    def test_missing_search_candidates_name_them(self) -> None:
        # Every input before it is present, so `select` reaches the first search.
        self.assert_select_names_missing(
            "docs/openapi-surface/golden-reach-witnesses/github-code-search/candidates.jsonl")


class MalformedInputs(unittest.TestCase):
    """A committed JSONL record `select` reads that is malformed fails naming
    the file, the line and what it lacks, never with a traceback. Like
    `MissingInputs`, it runs from a scratch checkout of what `select` reads."""

    CANDIDATES = tuple(f"docs/openapi-surface/golden-reach-witnesses/{source}/candidates.jsonl"
                       for source in ("github-code-search", "sourcegraph"))
    SCREENS = "docs/openapi-surface/scratch-search/screens.jsonl"

    def select_over(self, edit: tuple[str, str]) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            for relative in ("tools/fern-refusals/fern-refusals.py", *MissingInputs.INPUTS, *self.CANDIDATES):
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(REPO / relative, root / relative)
            relative, line = edit
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            existing = target.read_text(encoding="utf-8") if target.exists() else ""
            target.write_text(existing + line + "\n", encoding="utf-8")
            numbered = len((existing + line).splitlines())
            env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_FERN_REFUSALS")}
            result = subprocess.run([sys.executable, str(root / "tools" / "fern-refusals" / "fern-refusals.py"), "select"],
                                    capture_output=True, text=True, env=env, cwd=root)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn(f"{relative} line {numbered} ", result.stderr)
        return result

    def test_a_screen_without_its_verdict_names_the_line(self) -> None:
        result = self.select_over((self.SCREENS, '{"source": "scratch"}'))
        self.assertIn("lacks fern; restore it from git", result.stderr)

    def test_a_failed_screen_without_its_location_names_what_it_lacks(self) -> None:
        result = self.select_over((self.SCREENS, '{"fern": "failed: check", "source": "scratch"}'))
        self.assertIn("lacks repository, commit, path; restore it from git", result.stderr)

    def test_a_candidate_without_its_digest_names_the_line(self) -> None:
        result = self.select_over((self.CANDIDATES[0], '{"repository": "o/r", "path": "a.yml", "commit": "c"}'))
        self.assertIn("lacks sha256; restore it from git", result.stderr)

    def test_a_field_that_is_not_a_non_empty_string_names_the_line(self) -> None:
        for edit, field in (
            ((self.SCREENS, '{"fern": 7, "source": "scratch"}'), "fern 7"),
            ((self.SCREENS, '{"fern": "failed: check", "source": "scratch", "repository": ["o/r"], '
                            '"commit": "c", "path": "a.yml"}'), "repository ['o/r']"),
            ((self.CANDIDATES[0], '{"repository": "o/r", "path": "a.yml", "commit": null, "sha256": "d"}'),
             "commit None"),
            ((self.CANDIDATES[0], '{"repository": "", "path": "a.yml", "commit": "c", "sha256": "d"}'),
             "repository ''"),
        ):
            with self.subTest(field=field):
                result = self.select_over(edit)
                self.assertIn(f"has {field}, not a non-empty string; restore it from git", result.stderr)

    def test_a_failed_screens_logs_must_be_a_list_of_paths(self) -> None:
        result = self.select_over((self.SCREENS, '{"fern": "failed: check", "source": "scratch", '
                                                 '"repository": "o/r", "commit": "c", "path": "a.yml", '
                                                 '"fern_logs": "check.log"}'))
        self.assertIn("has fern_logs 'check.log', not a list of log paths; restore it from git", result.stderr)

    def test_a_screen_candidate_that_is_no_name_or_under_no_source_is_refused(self) -> None:
        result = self.select_over((self.SCREENS, '{"fern": "failed: check", "candidate": ["a.yml"]}'))
        self.assertIn("has candidate ['a.yml'], not a candidate name; restore it from git", result.stderr)
        result = self.select_over((self.SCREENS, '{"fern": "failed: check", "candidate": "a.yml"}'))
        self.assertIn("is a screen filed under 'scratch-search', which is neither an enumerated source", result.stderr)

    def test_a_record_that_is_not_json_names_the_line(self) -> None:
        result = self.select_over((self.SCREENS, "{not json"))
        self.assertIn("is not JSON", result.stderr)


class MeasurementsAndArguments(unittest.TestCase):
    """What `measure` reads back and what it is told: a measurement field that is
    not text, and a count or timeout outside its range, are refused up front."""

    def test_a_measurement_field_that_is_not_text_is_refused_naming_its_line(self) -> None:
        spec = importlib.util.spec_from_file_location("fern_refusals_measurements", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as scratch:
            module.EVIDENCE = Path(scratch)
            path = Path(scratch) / "measurements.jsonl"
            path.write_text(json.dumps({"key": "k", "check_exit": 1}) + "\n", encoding="utf-8")
            stderr = io.StringIO()
            with self.assertRaises(SystemExit), contextlib.redirect_stderr(stderr):
                module.read_measurements()
            self.assertIn("measurements.jsonl line 1 has check_exit 1, not a non-empty string", stderr.getvalue())
            path.write_text(json.dumps({"key": "k", "check_exit": "1", "check_log": ""}) + "\n", encoding="utf-8")
            self.assertEqual("1", module.read_measurements()["k"]["check_exit"])

    def test_a_count_or_timeout_out_of_range_is_refused_before_anything_runs(self) -> None:
        for args, message in ((("measure", "--jobs", "0"), "0 is not a positive integer"),
                              (("measure", "--timeout", "-5"), "-5 is not a positive integer"),
                              (("measure", "--limit", "-1"), "-1 is not a non-negative integer"),
                              (("confirm", "--per-class", "-2"), "-2 is not a non-negative integer"),
                              (("probe", "x", "--jobs", "many"), "invalid positive value: 'many'")):
            with self.subTest(args=args):
                refused = run(*args)
                self.assertEqual(2, refused.returncode, refused.stderr)
                self.assertIn(message, refused.stderr)


if __name__ == "__main__":
    unittest.main()
