# llmlint: ignore-file[new_code_lands_in_a_project] crozier has no Nx workspace; this boundary test sits in tests/ beside the other script tests and runs under `just test-fern-refusals`, part of `check`.
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
indistinguishable from "check reads nothing". `StrictMeasurement` drives
`measure` and `build` from a scratch checkout over one local document with the
compiled crozier binary, the way `just fern-refusals-measure` runs them.

Run: `just test-fern-refusals` (part of `just check`).
"""

from __future__ import annotations

import gzip
import hashlib
import json
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



@unittest.skipIf(os.name == "nt", "`measure` runs `target/release/crozier`, a path with no `.exe`")
class StrictMeasurement(unittest.TestCase):
    """`measure` records crozier's `--fern-strict` exit and `build` writes it
    into `documents.tsv` for a document carrying an evaluated class. Each case
    runs the REAL script from a scratch checkout whose whole population is one
    class's committed probe, screened by its committed `fern check` log (so no
    Fern runs), with the compiled crozier binary where `measure` looks for it."""

    CLASS = "request-property-name-collision"

    @classmethod
    def setUpClass(cls) -> None:
        built = subprocess.run(["cargo", "build", "--locked", "--quiet", "--bin", "crozier",
                                "--message-format=json-render-diagnostics"],
                               capture_output=True, text=True, cwd=REPO)
        if built.returncode != 0:
            raise AssertionError(f"cargo build --bin crozier failed:\n{built.stderr}")
        cls.binary = Path(next(message["executable"] for message in map(json.loads, built.stdout.splitlines())
                               if message.get("reason") == "compiler-artifact" and message.get("executable")))

    def setUp(self) -> None:
        self.scratch = tempfile.TemporaryDirectory()
        self.root = root = Path(self.scratch.name)
        shutil.copytree(REPO / "scripts", root / "scripts")
        binary = root / "target" / "release" / "crozier"
        binary.parent.mkdir(parents=True)
        shutil.copy(self.binary, binary)
        surface = root / "docs" / "openapi-surface"
        (root / "tests" / "fixtures").mkdir(parents=True)
        (root / "tests" / "fixtures" / "CORPUS.md").write_text("", encoding="utf-8")
        # The fetcher's GitHub module reads the census's region rows from this test at import.
        for relative in ("tests/surface_census_test.py", "justfile"):
            shutil.copy(REPO / relative, root / relative)
        (surface / "fern-refusals").mkdir(parents=True)
        (surface / "fern-refusals" / "dropped-sources.tsv").write_text(
            "name\tcorpus_line\tsource\tlocator\trevision\tsha256\tevidence\treason\n", encoding="utf-8")
        for source in ("jentic", "apis.guru", "vendor-portals", "github-publisher-trees"):
            (surface / "golden-reach-witnesses" / source).mkdir(parents=True)
            with gzip.open(surface / "golden-reach-witnesses" / source / "enumeration.tsv.gz", "wt",
                           encoding="utf-8") as handle:
                handle.write("walk\tdocument\trevision\tsha256\n")
        for source in ("github-code-search", "sourcegraph"):
            (surface / "golden-reach-witnesses" / source).mkdir(parents=True)
            (surface / "golden-reach-witnesses" / source / "candidates.jsonl").write_text("", encoding="utf-8")
        # The one screened document: the class's probe, which Fern's committed check refuses.
        (root / "documents").mkdir()
        probe = (REGISTRY / self.CLASS / "probe.yml").read_bytes()
        (root / "documents" / "probe.yml").write_bytes(probe)
        self.digest = hashlib.sha256(probe).hexdigest()
        screens = surface / "scratch"
        screens.mkdir()
        shutil.copy(REPO / "docs" / "openapi-surface" / "fern-refusals" / "probe-logs" / f"{self.CLASS}.check.log",
                    screens / "probe-check.log")
        (screens / "screens.jsonl").write_text(json.dumps({
            "fern": "failed: check exit 1", "source": "scratch", "repository": "scratch/probes",
            "commit": "0" * 40, "path": "probe.yml", "sha256": self.digest,
            "fern_logs": ["probe-check.log"]}) + "\n", encoding="utf-8")
        registry = root / "docs" / "fern-refusals"
        registry.mkdir()
        classes = rows(REGISTRY / "classes.tsv")
        self.classes = [classes[0], next(row for row in classes[1:] if row[0] == self.CLASS)]
        self.assertNotEqual(self.classes[1][6], "unevaluated", f"{self.CLASS} is meant to be an evaluated class")
        write_rows(registry / "classes.tsv", self.classes)
        write_rows(registry / "findings.tsv", rows(REGISTRY / "findings.tsv")[:1])
        self.measurements = surface / "fern-refusals" / "measurements.jsonl"
        self.documents = registry / "documents.tsv"

    def tearDown(self) -> None:
        self.scratch.cleanup()

    def script(self, *args: str) -> subprocess.CompletedProcess[str]:
        env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER")}
        return subprocess.run([sys.executable, str(self.root / "scripts" / "fern-refusals.py"), *args],
                              capture_output=True, text=True, env=env, cwd=self.root)

    def measure(self) -> dict[str, str]:
        result = self.script("measure", "--jobs", "1", "--root", str(self.root / "documents"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        [row] = [json.loads(line) for line in self.measurements.read_text(encoding="utf-8").splitlines()]
        return row

    def built_row(self) -> list[str]:
        result = self.script("build")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        table = rows(self.documents)
        self.assertEqual(table[0][11], "crozier_strict_exit")
        [row] = table[1:]
        self.assertEqual((row[0], row[8]), (self.digest, self.CLASS))
        return row

    def test_measure_records_the_strict_exit_and_build_writes_it(self) -> None:
        measured = self.measure()
        self.assertEqual(measured["digest"], self.digest)
        # crozier refuses the probe's colliding `name` in both modes, writing nothing.
        self.assertEqual((measured["crozier_exit"], measured["crozier_files"]), ("1", "0"))
        self.assertEqual(measured["crozier_strict_exit"], "1")
        self.assertEqual(self.built_row()[9:12], ["1", "0", "1"])

    def test_measure_runs_the_strict_exit_under_fern_strict(self) -> None:
        # Every names class refuses in both modes, so the exits agree; the strict
        # run is told apart by the cause its refusal line names.
        self.measure()
        logs = self.root / ".local" / "fern-refusals" / "crozier-logs"
        default = (logs / f"{self.digest}.default.log").read_text(encoding="utf-8")
        strict = (logs / f"{self.digest}.strict.log").read_text(encoding="utf-8")
        cause = "(fern-strict: Fern refuses this document)"
        self.assertIn(f"{self.CLASS}: ", default)
        self.assertNotIn(cause, default)
        self.assertIn(f"{self.CLASS}: ", strict)
        self.assertIn(cause, strict)

    def test_an_unevaluated_class_builds_no_strict_exit(self) -> None:
        self.measure()
        self.classes[1][6:9] = ["unevaluated", "—", "—"]
        write_rows(self.root / "docs" / "fern-refusals" / "classes.tsv", self.classes)
        self.assertEqual(self.built_row()[11], "—")

    def test_a_missing_strict_measurement_fails_the_build_until_measured(self) -> None:
        measured = self.measure()
        measured["crozier_strict_exit"] = ""
        self.measurements.write_text(json.dumps(measured, sort_keys=True) + "\n", encoding="utf-8")
        result = self.script("build")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn(f"{self.digest}: not measured (crozier-strict); run `just fern-refusals-measure`",
                      result.stderr)
        self.assertFalse(self.documents.exists(), "a failed build wrote documents.tsv")
        # The recovery the message names: `measure` takes only the missing run.
        remeasured = self.measure()
        self.assertEqual(remeasured, dict(measured, crozier_strict_exit="1"))
        self.assertEqual(self.built_row()[11], "1")


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
            for relative in ("scripts/fern-refusals.py", *self.INPUTS):
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
                if relative != missing:
                    shutil.copy(REPO / relative, root / relative)
            env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_FERN_REFUSALS")}
            result = subprocess.run([sys.executable, str(root / "scripts" / "fern-refusals.py"), "select"],
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
            for relative in ("scripts/fern-refusals.py", *self.INPUTS):
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(REPO / relative, root / relative)
            broken = "docs/openapi-surface/golden-reach-witnesses/jentic/enumeration.tsv.gz"
            with gzip.open(root / broken, "wt", encoding="utf-8") as handle:
                handle.write("walk\tdocument\trevision\n")
            env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_FERN_REFUSALS")}
            result = subprocess.run([sys.executable, str(root / "scripts" / "fern-refusals.py"), "select"],
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
            for relative in ("scripts/fern-refusals.py", *MissingInputs.INPUTS, *self.CANDIDATES):
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(REPO / relative, root / relative)
            relative, line = edit
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            existing = target.read_text(encoding="utf-8") if target.exists() else ""
            target.write_text(existing + line + "\n", encoding="utf-8")
            numbered = len((existing + line).splitlines())
            env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_FERN_REFUSALS")}
            result = subprocess.run([sys.executable, str(root / "scripts" / "fern-refusals.py"), "select"],
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

    def test_a_record_that_is_not_json_names_the_line(self) -> None:
        result = self.select_over((self.SCREENS, "{not json"))
        self.assertIn("is not JSON", result.stderr)


if __name__ == "__main__":
    unittest.main()
