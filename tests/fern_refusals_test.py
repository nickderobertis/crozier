"""Coverage for `scripts/fern-refusals.py`, which builds `docs/fern-refusals/`.

The script derives the refused-document population from committed records and
writes `documents.tsv`, `unretrievable.tsv` and `classes.tsv`'s `documents`
column. These tests drive the REAL script as a user does. `CommittedTables` runs
`check` over the REAL repository and `build` into a scratch copy of the
registry, which must reproduce the committed tables byte for byte. The drift
cases copy the registry to a scratch directory (`CROZIER_FERN_REFUSALS_REGISTRY`)
and break one thing at a time — a header column, a class id a document carries,
a class count, a row order, a class template the population needs — requiring
the failure to name it: without that half, "check passes" would be
indistinguishable from "check reads nothing".

Run: `just test-fern-refusals` (part of `just check`).
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "fern-refusals.py"
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
            for hand_written in ("classes.tsv", "findings.tsv"):
                shutil.copy(REGISTRY / hand_written, registry / hand_written)
            result = run("build", registry=registry)
            self.assertEqual(result.returncode, 0, result.stderr)
            for name in TABLES:
                self.assertEqual((registry / name).read_text(encoding="utf-8"),
                                 (REGISTRY / name).read_text(encoding="utf-8"), name)

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
        for key, _source, locator, *_ in selected:
            with self.subTest(key=key):
                # A document is named by its digest, or by its locator where no
                # record gave a digest; one no record located is named by its key.
                self.assertTrue(key in documents | generated or locator in documents | generated | listed
                                or key in listed,
                                f"{key} is in none of documents.tsv, generated.tsv and unretrievable.tsv")


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


if __name__ == "__main__":
    unittest.main()
