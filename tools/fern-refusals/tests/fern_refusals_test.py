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
indistinguishable from "check reads nothing". `FernRuns` drives `probe`,
`finding` and `confirm` with a stand-in `fern` on PATH. `measure` with the
compiled crozier binary is `tools/fern-refusals-strict/`'s suite, which imports
the helpers defined here.

Run: `just test-fern-refusals` (part of `just check`).
"""

from __future__ import annotations

import contextlib
import gzip
import hashlib
import importlib.util
import io
import json
import os
import shlex
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from types import ModuleType
from typing import Any

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "fern-refusals" / "fern-refusals.py"
# The script and the record it reads the certified pair from, as a scratch root mirrors them.
SCRIPT_LOADS = (
    "tools/fern-refusals/fern-refusals.py",
    "tools/fern-refusals/sdk_evaluation.py",
    "tools/fern-refusals/sdk_evaluation_runtime.py",
    "assets/scaffolding/metadata.json",
)
REGISTRY = REPO / "docs" / "fern-refusals"
CONFIRMATIONS = REPO / "docs" / "openapi-surface" / "fern-refusals" / "confirmations.tsv"
# The certified Fern pair, from its one declaration.
CERTIFIED = json.loads((REPO / "assets" / "scaffolding" / "metadata.json").read_text(encoding="utf-8"))
TABLES = ("classes.tsv", "documents.tsv", "generated.tsv", "unretrievable.tsv")
# `dispositions.tsv`'s columns, as `reduce` writes them.
DISPOSITIONS_HEADER = (
    "document",
    "crozier_class",
    "disposition",
    "representative",
    "reduction",
    "reduced_digest",
    "check_exit",
    "generate_exit",
    "classes",
    "log",
)
# The first line of every log `measure` and `confirm` write, naming the pair.
PAIR_LINE = (
    f"fern-refusals: Fern CLI {CERTIFIED['cliVersion']}, fernapi/fern-python-sdk {CERTIFIED['generatorVersion']}\n"
)


def run(
    *args: str, registry: Path | None = None, confirmations: Path | None = None
) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env.pop("CROZIER_FERN_REFUSALS_REGISTRY", None)
    env.pop("CROZIER_FERN_REFUSALS_CONFIRMATIONS", None)
    if registry is not None:
        env["CROZIER_FERN_REFUSALS_REGISTRY"] = str(registry)
    if confirmations is not None:
        env["CROZIER_FERN_REFUSALS_CONFIRMATIONS"] = str(confirmations)
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, env=env, cwd=REPO)


# A stand-in for the Fern CLI, which these suites never run: it answers
# `fern check` and `fern generate` as the FERN_STUB_* variables say, writing
# FERN_STUB_GENERATE_FILES files under `--output`, and appends what it was run
# with (its arguments, the workspace's pinned CLI and generator versions, and
# the environment `fern_run` sets) to FERN_STUB_CALLS. With FERN_STUB_HANG it
# starts a child and never ends, writing both process ids to that file; with
# FERN_STUB_HANG_STAGE too, only that stage hangs.
FERN_STUB = """\
import json, os, sys
from pathlib import Path
stage = sys.argv[1]
calls = os.environ.get("FERN_STUB_CALLS")
if calls:
    with open(calls, "a", encoding="utf-8") as handle:
        handle.write(json.dumps({"argv": sys.argv[1:],
                                 "cli": json.loads(Path("fern.config.json").read_text())["version"],
                                 "generators": Path("generators.yml").read_text(),
                                 "spec": Path("openapi/openapi.yml").read_text(),
                                 "node_options": os.environ.get("NODE_OPTIONS")}) + "\\n")
hang = os.environ.get("FERN_STUB_HANG")
if hang and os.environ.get("FERN_STUB_HANG_STAGE", stage) == stage:
    # A run that never ends, as Fern's `npx` tree does: a child of its own, then a wait.
    import subprocess, time
    child = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(600)"])
    Path(hang).write_text(f"{os.getpid()} {child.pid}", encoding="utf-8")
    time.sleep(600)
prefix = "FERN_STUB_" + stage.upper()
print(os.environ.get(prefix + "_OUTPUT", ""))
if stage == "generate":
    output = Path(sys.argv[sys.argv.index("--output") + 1])
    for number in range(int(os.environ.get("FERN_STUB_GENERATE_FILES", "0"))):
        (output / "src").mkdir(parents=True, exist_ok=True)
        (output / "src" / f"module_{number}.py").write_text("", encoding="utf-8")
sys.exit(int(os.environ.get(prefix + "_EXIT", "0")))
"""


def stub_fern(directory: Path) -> Path:
    """`directory` holding an executable `fern` that runs FERN_STUB under this interpreter."""
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "fern-stub.py").write_text(FERN_STUB, encoding="utf-8")
    fern = directory / "fern"
    fern.write_text(
        f'#!/bin/sh\nexec {shlex.quote(sys.executable)} {shlex.quote(str(directory / "fern-stub.py"))} "$@"\n',
        encoding="utf-8",
    )
    fern.chmod(0o755)
    return directory


def load_script(name: str) -> ModuleType:
    """The REAL script as a module, for the readers its subcommands share."""
    spec = importlib.util.spec_from_file_location(name, SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def phrase(template: str) -> str:
    """A message a class's or finding's `diagnostic` template matches."""
    return template.replace("<…>", "widget")


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
            for hand_written in ("classes.tsv", "findings.tsv", "documents.tsv", "dispositions.tsv"):
                shutil.copy(REGISTRY / hand_written, registry / hand_written)
            result = run("build", registry=registry)
            self.assertEqual(result.returncode, 0, result.stderr)
            for name in TABLES:
                self.assertEqual(
                    (registry / name).read_text(encoding="utf-8"), (REGISTRY / name).read_text(encoding="utf-8"), name
                )

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
        generated = {row[4] for row in rows(REGISTRY / "generated.tsv")[1:]} | {
            row[1] for row in rows(REGISTRY / "generated.tsv")[1:]
        }
        unretrievable = rows(REGISTRY / "unretrievable.tsv")[1:]
        listed = {row[1] for row in unretrievable}
        self.assertFalse({row[0] for row in refused} & generated, "a document is both refused and generated")
        for name, table in (
            ("documents.tsv", [row[0] for row in refused]),
            ("generated.tsv", [row[4] for row in rows(REGISTRY / "generated.tsv")[1:]]),
            ("unretrievable.tsv", [row[1] for row in unretrievable]),
        ):
            with self.subTest(table=name):
                self.assertEqual(len(table), len(set(table)), f"{name} lists a document twice")
        for key, _source, locator, *_ in selected:
            with self.subTest(key=key):
                # A document is named by its digest, or by its locator where no
                # record gave a digest; one no record located is named by its key.
                homes = [
                    name
                    for name, names in (
                        ("documents.tsv", documents),
                        ("generated.tsv", generated),
                        ("unretrievable.tsv", listed),
                    )
                    if key in names or locator in names
                ]
                self.assertEqual(
                    1,
                    len(homes),
                    f"{key} is accounted for in {homes or 'none'} of documents.tsv, "
                    "generated.tsv and unretrievable.tsv, not exactly one",
                )


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
        for name, column, renamed in (
            ("classes.tsv", "population_strict", "strict_population"),
            ("documents.tsv", "crozier_strict_exit", "crozier_strict"),
            ("generated.tsv", "findings", "phrases"),
            ("unretrievable.tsv", "reason", "why"),
            ("findings.tsv", "probe", "document"),
        ):
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

    def test_a_finding_naming_a_class_probe_holds_and_one_naming_no_class_fails(self) -> None:
        # A `generates` finding whose probe is a class's own probe.yml retires
        # that class; the class's rows stay until the population is re-measured.
        table = rows(self.registry / "findings.tsv")
        classes = [row[0] for row in rows(self.registry / "classes.tsv")[1:]]
        retiring = [row for row in table[1:] if row[5] == f"docs/fern-refusals/{classes[0]}/probe.yml"]
        if not retiring:
            table.append(
                [f"{classes[0]}-generates", "generates", "0", "0", "—", f"docs/fern-refusals/{classes[0]}/probe.yml"]
            )
            write_rows(self.registry / "findings.tsv", table)
        result = run("check", registry=self.registry)
        self.assertEqual(result.returncode, 0, result.stderr)
        table.append(["stray-generates", "generates", "0", "0", "—", "docs/fern-refusals/no-such-class/probe.yml"])
        write_rows(self.registry / "findings.tsv", table)
        self.assert_check_fails_naming(
            "findings.tsv stray-generates: its probe docs/fern-refusals/no-such-class/probe.yml is inside the "
            "registry but is no classes.tsv row's probe.yml"
        )

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

    def test_the_strict_exit_is_built_for_evaluated_classes_and_generating_exceptions(self) -> None:
        table = rows(self.registry / "classes.tsv")
        evaluated = {row[0] for row in table[1:] if row[6] != "unevaluated"}
        committed = rows(REGISTRY / "documents.tsv")[1:]
        exceptions = {row[0] for row in rows(REGISTRY / "dispositions.tsv")[1:] if row[2] == "fern-limitation"}
        # The evaluated class whose withdrawal leaves the most documents with no evaluated class.
        withdrawn = max(
            sorted(evaluated), key=lambda name: sum(set(row[8].split(",")) & evaluated == {name} for row in committed)
        )
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
                if set(before[8].split(",")) & evaluated or before[0] in exceptions:
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
        log = next(
            path
            for path in (REPO / "docs" / "openapi-surface" / "fern-refusals" / "logs").glob(
                f"{generated[4]}.generate.log"
            )
        )
        table[1][3:6] = ["0", "40", log.relative_to(REPO).as_posix()]
        write_rows(confirmations, table)
        result = run("check", confirmations=confirmations)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(f"{table[1][0]}: Fern generates from {table[1][1]}", result.stderr)

    def test_a_generation_that_wrote_nothing_or_printed_the_phrase_confirms(self) -> None:
        confirmations = Path(self.scratch.name) / "confirmations.tsv"
        table = rows(CONFIRMATIONS)
        patterns = load_script("fern_refusals_confirming")
        classes = {row["class"]: row for row in patterns.read_tsv(REGISTRY / "classes.tsv", patterns.CLASSES_HEADER)}
        generated = rows(REGISTRY / "generated.tsv")[1]
        silent = f"docs/openapi-surface/fern-refusals/logs/{generated[4]}.generate.log"
        # A refused row whose own log carries its class's phrase, made to exit 0 with a tree.
        phrased = next(
            number
            for number, row in enumerate(table[1:], 1)
            if row[3] == "1"
            and any(
                patterns.template_pattern(classes[row[0]]["diagnostic"]).match(message)
                for message in patterns.diagnostics(patterns.read_log(row[5]))
            )
        )
        for name, number, outcome in (
            ("exit 0, no files", 1, ["0", "0", silent]),
            ("exit 0, a tree, the phrase", phrased, ["0", "40", table[phrased][5]]),
        ):
            with self.subTest(name):
                edited = [list(row) for row in table]
                edited[number][3:6] = outcome
                write_rows(confirmations, edited)
                result = run("check", confirmations=confirmations)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        # The same tree with neither is the contradiction `check` exists for.
        edited = [list(row) for row in table]
        edited[1][3:6] = ["0", "40", silent]
        write_rows(confirmations, edited)
        self.assertEqual(run("check", confirmations=confirmations).returncode, 1)

    def test_a_timed_out_or_malformed_confirmation_fails(self) -> None:
        confirmations = Path(self.scratch.name) / "confirmations.tsv"
        for outcome, phrase_ in (
            (["timeout", "0"], "timed out, which confirms nothing; rerun `confirm` with a longer `--timeout`"),
            (
                ["1", "many"],
                "generate_exit '1' and generate_files 'many' must be an exit status or `timeout`, and a file count",
            ),
            (["00", "40"], "generate_exit '00' and generate_files '40' must be an exit"),
            (["", "0"], "must be an exit status"),
        ):
            with self.subTest(outcome=outcome):
                table = rows(CONFIRMATIONS)
                table[1][3:5] = outcome
                write_rows(confirmations, table)
                result = run("check", confirmations=confirmations)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(phrase_, result.stderr)

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
        *(
            f"docs/openapi-surface/golden-reach-witnesses/{source}/enumeration.tsv.gz"
            for source in ("jentic", "apis.guru", "vendor-portals", "github-publisher-trees")
        ),
    )

    def assert_select_names_missing(self, missing: str) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            for relative in (*SCRIPT_LOADS, *self.INPUTS):
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
                if relative != missing:
                    shutil.copy(REPO / relative, root / relative)
            env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_FERN_REFUSALS")}
            result = subprocess.run(
                [sys.executable, str(root / "tools" / "fern-refusals" / "fern-refusals.py"), "select"],
                capture_output=True,
                text=True,
                env=env,
                cwd=root,
            )
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn(f"{missing} is missing; restore it from git", result.stderr)

    def test_a_missing_corpus_table_names_it(self) -> None:
        self.assert_select_names_missing("tests/fixtures/CORPUS.md")

    def test_a_missing_enumeration_names_it(self) -> None:
        self.assert_select_names_missing("docs/openapi-surface/golden-reach-witnesses/jentic/enumeration.tsv.gz")

    def select_over_enumeration(self, source: str, text: str) -> subprocess.CompletedProcess[str]:
        """`select` from a scratch checkout whose `source` enumeration is `text`."""
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            for relative in (*SCRIPT_LOADS, *self.INPUTS):
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(REPO / relative, root / relative)
            with gzip.open(root / self.enumeration(source), "wt", encoding="utf-8") as handle:
                handle.write(text)
            env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_FERN_REFUSALS")}
            result = subprocess.run(
                [sys.executable, str(root / "tools" / "fern-refusals" / "fern-refusals.py"), "select"],
                capture_output=True,
                text=True,
                env=env,
                cwd=root,
            )
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        return result

    @staticmethod
    def enumeration(source: str) -> str:
        return f"docs/openapi-surface/golden-reach-witnesses/{source}/enumeration.tsv.gz"

    def test_an_enumeration_without_its_columns_names_them(self) -> None:
        result = self.select_over_enumeration("jentic", "walk\tdocument\trevision\n")
        self.assertIn(f"{self.enumeration('jentic')}: the header lacks sha256", result.stderr)

    def test_an_enumeration_row_short_or_long_of_its_header_names_the_line(self) -> None:
        header = "walk\tdocument\trevision\tsha256\n"
        for row in ("o/r\ta.yml\tc\n", "o/r\ta.yml\tc\td\tsurplus\n"):
            with self.subTest(row=row):
                result = self.select_over_enumeration("jentic", header + "o/r\tb.yml\tc\td\n" + row)
                self.assertIn(
                    f"{self.enumeration('jentic')} line 3 is not one cell per column of its header", result.stderr
                )

    def test_a_vendor_portal_document_outside_its_clone_names_the_line(self) -> None:
        result = self.select_over_enumeration(
            "vendor-portals", "walk\tdocument\trevision\tsha256\no/r\topenapi.yml\tc\td\n"
        )
        self.assertIn(
            f"{self.enumeration('vendor-portals')} line 2: vendor-portals document 'openapi.yml' is not "
            "`<owner>--<repo>/<path>`",
            result.stderr,
        )

    def test_missing_search_candidates_name_them(self) -> None:
        # Every input before it is present, so `select` reaches the first search.
        self.assert_select_names_missing(
            "docs/openapi-surface/golden-reach-witnesses/github-code-search/candidates.jsonl"
        )


class MalformedInputs(unittest.TestCase):
    """A committed JSONL record `select` reads that is malformed fails naming
    the file, the line and what it lacks, never with a traceback. Like
    `MissingInputs`, it runs from a scratch checkout of what `select` reads."""

    CANDIDATES = tuple(
        f"docs/openapi-surface/golden-reach-witnesses/{source}/candidates.jsonl"
        for source in ("github-code-search", "sourcegraph")
    )
    SCREENS = "docs/openapi-surface/scratch-search/screens.jsonl"

    def select_over(self, edit: tuple[str, str]) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            for relative in (*SCRIPT_LOADS, *MissingInputs.INPUTS, *self.CANDIDATES):
                (root / relative).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(REPO / relative, root / relative)
            relative, line = edit
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            existing = target.read_text(encoding="utf-8") if target.exists() else ""
            target.write_text(existing + line + "\n", encoding="utf-8")
            numbered = len((existing + line).splitlines())
            env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER_FERN_REFUSALS")}
            result = subprocess.run(
                [sys.executable, str(root / "tools" / "fern-refusals" / "fern-refusals.py"), "select"],
                capture_output=True,
                text=True,
                env=env,
                cwd=root,
            )
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
            (
                (
                    self.SCREENS,
                    '{"fern": "failed: check", "source": "scratch", "repository": ["o/r"], '
                    '"commit": "c", "path": "a.yml"}',
                ),
                "repository ['o/r']",
            ),
            (
                (self.CANDIDATES[0], '{"repository": "o/r", "path": "a.yml", "commit": null, "sha256": "d"}'),
                "commit None",
            ),
            (
                (self.CANDIDATES[0], '{"repository": "", "path": "a.yml", "commit": "c", "sha256": "d"}'),
                "repository ''",
            ),
        ):
            with self.subTest(field=field):
                result = self.select_over(edit)
                self.assertIn(f"has {field}, not a non-empty string; restore it from git", result.stderr)

    def test_a_failed_screens_digest_must_be_text(self) -> None:
        result = self.select_over(
            (
                self.SCREENS,
                '{"fern": "failed: check", "source": "scratch", '
                '"repository": "o/r", "commit": "c", "path": "a.yml", '
                '"sha256": 7}',
            )
        )
        self.assertIn("has sha256 7, not a digest string; restore it from git", result.stderr)

    def test_a_failed_screens_logs_must_be_a_list_of_paths(self) -> None:
        result = self.select_over(
            (
                self.SCREENS,
                '{"fern": "failed: check", "source": "scratch", '
                '"repository": "o/r", "commit": "c", "path": "a.yml", '
                '"fern_logs": "check.log"}',
            )
        )
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
        assert spec is not None and spec.loader is not None
        # `Any`, not `ModuleType`: the case rebinds the script's `EVIDENCE`, an
        # assignment ty refuses on a plain module.
        module: Any = importlib.util.module_from_spec(spec)
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

    def test_a_measured_value_outside_its_grammar_is_refused_naming_its_line(self) -> None:
        # `Any` for the same reason: the case rebinds the script's `EVIDENCE`.
        module: Any = load_script("fern_refusals_grammar")
        with tempfile.TemporaryDirectory() as scratch:
            module.EVIDENCE = Path(scratch)
            path = Path(scratch) / "measurements.jsonl"
            for row, message in (
                ({"check_exit": "failed"}, "has check_exit 'failed', not an exit status or `timeout`"),
                ({"generate_files": "-1"}, "has generate_files '-1', not a file count"),
                # A spelling a comparison with "0" would misread: exit 00 is a success.
                ({"generate_exit": "00"}, "has generate_exit '00', not an exit status"),
                ({"generate_files": "00"}, "has generate_files '00', not a file count"),
                ({"crozier_exit": "\u0661"}, "has crozier_exit '\u0661', not an exit status"),
                ({"crozier_files": "3 files"}, "has crozier_files '3 files', not a file count"),
                ({"digest": "abc"}, "has digest 'abc', not a SHA-256 digest"),
                (
                    {"fern_stage": "lint", "fern_exit": "1", "fern_log": ""},
                    "has fern_stage 'lint', not check or generate",
                ),
                ({"fern_stage": "check", "fern_exit": "x", "fern_log": ""}, "has fern_exit 'x', not an exit status"),
            ):
                with self.subTest(row=row):
                    path.write_text(json.dumps({"key": "k", **row}) + "\n", encoding="utf-8")
                    stderr = io.StringIO()
                    with self.assertRaises(SystemExit), contextlib.redirect_stderr(stderr):
                        module.read_measurements()
                    self.assertIn(f"measurements.jsonl line 1 {message}", stderr.getvalue())
            # What `measure` writes is read back: a signal's negative status, a
            # timeout, and a legacy single-stage record.
            path.write_text(
                "".join(
                    json.dumps(row) + "\n"
                    for row in (
                        {
                            "key": "a",
                            "digest": "0" * 64,
                            "check_exit": "-9",
                            "crozier_exit": "timeout",
                            "crozier_files": "0",
                        },
                        {
                            "key": "b",
                            "fern_stage": "generate",
                            "fern_exit": "1",
                            "fern_log": "",
                            "generate_files": "12",
                        },
                    )
                ),
                encoding="utf-8",
            )
            read = module.read_measurements()
            self.assertEqual((read["a"]["check_exit"], read["a"]["crozier_exit"]), ("-9", "timeout"))
            self.assertEqual((read["b"]["check_exit"], read["b"]["generate_exit"]), ("0", "1"))

    def test_a_log_a_record_names_that_is_gone_is_refused(self) -> None:
        module = load_script("fern_refusals_logs")
        stderr = io.StringIO()
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(stderr):
            module.read_log("docs/openapi-surface/fern-refusals/logs/gone.check.log")
        self.assertIn(
            "docs/openapi-surface/fern-refusals/logs/gone.check.log is missing; restore it from git, "
            "or rerun `measure --again` to retake it",
            stderr.getvalue(),
        )
        self.assertEqual("", module.read_log(""))

    def test_a_count_or_timeout_out_of_range_is_refused_before_anything_runs(self) -> None:
        for args, message in (
            (("measure", "--jobs", "0"), "0 is not a positive integer"),
            (("measure", "--timeout", "-5"), "-5 is not a positive integer"),
            (("measure", "--limit", "-1"), "-1 is not a non-negative integer"),
            (("confirm", "--per-class", "-2"), "-2 is not a non-negative integer"),
            (("probe", "x", "--jobs", "many"), "invalid positive value: 'many'"),
        ):
            with self.subTest(args=args):
                refused = run(*args)
                self.assertEqual(2, refused.returncode, refused.stderr)
                self.assertIn(message, refused.stderr)


@unittest.skipIf(os.name == "nt", "the stand-in `fern` is a POSIX shell script")
class FernRuns(unittest.TestCase):
    """`probe`, `finding` and `confirm` run Fern and record what it said. Each
    case runs the REAL script from a scratch checkout with a stand-in `fern`
    first on PATH (`FERN_STUB`), so no Fern, Docker or network is reached, and
    reads back the tables and logs the script wrote there."""

    CLASS = "request-property-name-collision"
    FINDING = "exploded-property-not-list"

    def setUp(self) -> None:
        self.scratch = tempfile.TemporaryDirectory()
        self.root = root = Path(self.scratch.name)
        (root / "tools" / "fern-refusals").mkdir(parents=True)
        for relative in SCRIPT_LOADS:
            (root / relative).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(REPO / relative, root / relative)
        self.registry = root / "docs" / "fern-refusals"
        self.evidence = root / "docs" / "openapi-surface" / "fern-refusals"
        (self.registry / self.CLASS).mkdir(parents=True)
        self.evidence.mkdir(parents=True)
        shutil.copy(REGISTRY / self.CLASS / "probe.yml", self.registry / self.CLASS / "probe.yml")
        classes = rows(REGISTRY / "classes.tsv")
        self.class_row = next(row for row in classes[1:] if row[0] == self.CLASS)
        write_rows(self.registry / "classes.tsv", [classes[0], self.class_row])
        findings = rows(REGISTRY / "findings.tsv")
        self.finding_row = next(row for row in findings[1:] if row[0] == self.FINDING)
        write_rows(self.registry / "findings.tsv", [findings[0], self.finding_row])
        probe = root / self.finding_row[5]
        probe.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(REPO / self.finding_row[5], probe)
        self.calls = root / "fern-calls.jsonl"
        self.env = {key: value for key, value in os.environ.items() if not key.startswith(("CROZIER", "FERN_STUB"))}
        self.env.update(
            PATH=f"{stub_fern(root / 'bin')}{os.pathsep}{self.env.get('PATH', '')}", FERN_STUB_CALLS=str(self.calls)
        )

    def tearDown(self) -> None:
        self.scratch.cleanup()

    def script(self, *args: str, **fern: str) -> subprocess.CompletedProcess[str]:
        env = dict(self.env, **{f"FERN_STUB_{key.upper()}": value for key, value in fern.items()})
        return subprocess.run(
            [sys.executable, str(self.root / "tools" / "fern-refusals" / "fern-refusals.py"), *args],
            capture_output=True,
            text=True,
            env=env,
            cwd=self.root,
        )

    def calls_made(self) -> list[dict[str, str]]:
        if not self.calls.exists():
            return []
        return [json.loads(line) for line in self.calls.read_text(encoding="utf-8").splitlines()]

    def test_probe_records_the_stage_whose_output_carries_the_phrase(self) -> None:
        said = phrase(self.class_row[4])
        result = self.script(
            "probe",
            self.CLASS,
            check_exit="1",
            check_output=f"issue: {said}",
            generate_exit="1",
            generate_output=f"[error] {said}",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual("fern-refusals: 1 probe(s) recorded\n", result.stdout)
        [row] = rows(self.registry / "classes.tsv")[1:]
        self.assertEqual(row[2:4], ["check", "1"])
        refusal = (self.registry / self.CLASS / "fern-refusal.txt").read_text(encoding="utf-8")
        self.assertIn("generate_exit: 1\n", refusal)
        self.assertIn(f"diagnostic: {said}\n", refusal)
        self.assertIn("output_tree: none\n", refusal)
        self.assertIn(said, (self.evidence / "probe-logs" / f"{self.CLASS}.check.log").read_text(encoding="utf-8"))
        # Both stages ran, in a workspace pinning the CLI and generator, over the probe.
        calls = self.calls_made()
        self.assertEqual([call["argv"][0] for call in calls], ["check", "generate"])
        self.assertTrue(
            all(
                call["cli"] == CERTIFIED["cliVersion"]
                and f"version: {CERTIFIED['generatorVersion']}" in call["generators"]
                and call["node_options"] == "--max-old-space-size=16384"
                for call in calls
            )
        )
        self.assertEqual(calls[0]["spec"], (REGISTRY / self.CLASS / "probe.yml").read_text(encoding="utf-8"))

    def test_a_probe_fern_generates_past_is_refused_as_a_finding(self) -> None:
        said = phrase(self.class_row[4])
        result = self.script(
            "probe", self.CLASS, check_exit="1", check_output=f"issue: {said}", generate_exit="0", generate_files="3"
        )
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn(
            f"{self.CLASS}: the check stage exits 1 but the generation 0, writing 3 files; a phrase "
            "Fern still generates past is a finding",
            result.stderr,
        )
        self.assertIn("1 probe(s) not recorded, each explained above", result.stderr)
        self.assertFalse((self.registry / self.CLASS / "fern-refusal.txt").exists())
        self.assertEqual(rows(self.registry / "classes.tsv")[1], self.class_row)

    def test_a_probe_without_the_class_phrase_names_its_logs(self) -> None:
        result = self.script(
            "probe", self.CLASS, check_exit="1", check_output="issue: something else", generate_exit="1"
        )
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(
            f"{self.CLASS}: Fern printed no diagnostic matching its template over the probe "
            "(check exit 1, generate exit 1); see docs/openapi-surface/fern-refusals/probe-logs/"
            f"{self.CLASS}.*.log",
            result.stderr,
        )

    def record_refusal(self) -> str:
        """The class's committed refusal, as `probe` wrote it at an older pair."""
        said = phrase(self.class_row[4])
        record = (
            "fern_cli_version: 0.1.0\nfern_python_sdk_version: 0.2.0\n"  # certified-pair: stand-in (an older pair)
            f"generate_exit: 1\ndiagnostic: {said}\noutput_tree: none\n"
        )
        (self.registry / self.CLASS / "fern-refusal.txt").write_text(record, encoding="utf-8")
        self.class_row[2:4] = ["check", "1"]
        write_rows(self.registry / "classes.tsv", [rows(self.registry / "classes.tsv")[0], self.class_row])
        return record

    def changes(self) -> list[dict[str, str]]:
        return [json.loads(line) for line in (self.root / "changes.jsonl").read_text(encoding="utf-8").splitlines()]

    def test_a_probe_reproducing_its_recorded_refusal_rewrites_it_at_the_pair(self) -> None:
        self.record_refusal()
        said = phrase(self.class_row[4])
        result = self.script(
            "probe",
            self.CLASS,
            "--changes",
            str(self.root / "changes.jsonl"),
            check_exit="1",
            check_output=f"issue: {said}",
            generate_exit="1",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual("fern-refusals: 1 probe(s) recorded\n", result.stdout)
        self.assertEqual([], self.changes())
        refusal = (self.registry / self.CLASS / "fern-refusal.txt").read_text(encoding="utf-8")
        self.assertIn(f"fern_cli_version: {CERTIFIED['cliVersion']}\n", refusal)

    def test_a_probe_no_longer_reproducing_its_recorded_refusal_is_reported_and_keeps_the_record(self) -> None:
        recorded = (
            f"the check stage exits 1 and the generation 1, with `{phrase(self.class_row[4])}`, "
            "at Fern CLI 0.1.0 / fern-python-sdk 0.2.0"
        )
        said = phrase(self.class_row[4])
        cases = [
            (
                "generates",
                {"generate_exit": "0", "generate_files": "3"},
                "Fern generates from the probe (check exit 0, generate exit 0, writing 3 files)",
            ),
            (
                "generates",
                {"check_exit": "1", "check_output": f"issue: {said}", "generate_exit": "0", "generate_files": "2"},
                "Fern generates from the probe (check exit 1, generate exit 0, writing 2 files); the check stage "
                "still prints the class's phrase",
            ),
            (
                "refuses-otherwise",
                {"check_exit": "1", "check_output": f"issue: {said}", "generate_exit": "2"},
                f"Fern refuses the probe otherwise (check exit 1, generate exit 2), printing `{said}`; the check "
                "stage still prints the class's phrase",
            ),
            (
                "refuses-otherwise",
                {"check_exit": "1", "check_output": "issue: something else", "generate_exit": "1"},
                "Fern refuses the probe otherwise (check exit 1, generate exit 1), printing `something else`",
            ),
            (
                "refuses-otherwise",
                {"check_exit": "2", "check_output": f"issue: {said}", "generate_exit": "2"},
                f"Fern refuses the probe otherwise (check exit 2, generate exit 2), printing `{said}`; the check "
                "stage still prints the class's phrase",
            ),
            (
                "unsettled",
                {
                    "check_exit": "1",
                    "check_output": f"issue: {said}",
                    "hang": str(self.root / "fern-pids"),
                    "hang_stage": "generate",
                },
                "unsettled: `fern generate` ran past the probe's 3-second bound (check exit 1, generate exit "
                "timeout); the check stage still prints the class's phrase; a run cut short says nothing about "
                "whether Fern refuses given more time or memory",
            ),
            (
                "unsettled",
                {"hang": str(self.root / "fern-pids")},
                "unsettled: `fern check` and `fern generate` ran past the probe's 3-second bound (check exit "
                "timeout, generate exit timeout), printing no diagnostic matching the template; a run cut short "
                "says nothing about whether Fern refuses given more time or memory",
            ),
        ]
        for outcome, fern, now in cases:
            with self.subTest(outcome=outcome, now=now):
                record = self.record_refusal()
                # The bound is the probe's own, or the override the weekly run's harness sets.
                self.env["CROZIER_FERN_REFUSALS_PROBE_TIMEOUT"] = "3"
                result = self.script("probe", self.CLASS, "--changes", str(self.root / "changes.jsonl"), **fern)
                self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual(
                    [{"class": self.CLASS, "outcome": outcome, "recorded": recorded, "now": now}], self.changes()
                )
                self.assertIn(
                    f"{self.CLASS}: Fern no longer reproduces the recorded refusal ({outcome})", result.stderr
                )
                self.assertEqual(
                    "fern-refusals: 0 probe(s) recorded, 1 no longer reproducing the recorded refusal\n", result.stdout
                )
                self.assertEqual(record, (self.registry / self.CLASS / "fern-refusal.txt").read_text(encoding="utf-8"))
                self.assertEqual(rows(self.registry / "classes.tsv")[1], self.class_row)

    def test_a_probe_with_no_record_cut_short_after_its_phrase_records_nothing(self) -> None:
        said = phrase(self.class_row[4])
        result = self.script(
            "probe",
            self.CLASS,
            "--timeout",
            "3",
            check_exit="1",
            check_output=f"issue: {said}",
            hang=str(self.root / "fern-pids"),
            hang_stage="generate",
        )
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(
            f"{self.CLASS}: Fern ran past the probe's 3-second bound (check exit 1, generate exit timeout), "
            "which settles no refusal; rerun with a longer --timeout",
            result.stderr,
        )
        self.assertFalse((self.registry / self.CLASS / "fern-refusal.txt").exists())

    def test_a_malformed_recorded_refusal_fails_rather_than_support_a_change(self) -> None:
        self.record_refusal()
        record = self.registry / self.CLASS / "fern-refusal.txt"
        for text in ("generate_exit: 1\n", "fern_cli_version: 0.1.0\nnot a field\n"):
            with self.subTest(text=text):
                record.write_text(text, encoding="utf-8")
                result = self.script("probe", self.CLASS, "--changes", str(self.root / "changes.jsonl"))
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(
                    f"{self.CLASS}: docs/fern-refusals/{self.CLASS}/fern-refusal.txt is no refusal record",
                    result.stderr,
                )
                self.assertEqual([], self.changes())
                self.assertEqual(text, record.read_text(encoding="utf-8"))

    def test_a_probe_without_its_document_fails_and_reports_no_change(self) -> None:
        self.record_refusal()
        (self.registry / self.CLASS / "probe.yml").unlink()
        result = self.script("probe", self.CLASS, "--changes", str(self.root / "changes.jsonl"))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn(
            f"{self.CLASS}: no probe document docs/fern-refusals/{self.CLASS}/probe.yml; restore it from git",
            result.stderr,
        )
        self.assertEqual([], self.changes())
        self.assertEqual([], self.calls_made())

    def test_a_run_past_its_timeout_is_ended_with_every_process_it_started(self) -> None:
        pids = self.root / "fern-pids"
        result = self.script("probe", self.CLASS, "--timeout", "3", hang=str(pids))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("(check exit timeout, generate exit timeout)", result.stderr)
        for pid in map(int, pids.read_text(encoding="utf-8").split()):
            # Ended and reaped, or at most a zombie of an exited parent: never still running.
            with self.subTest(pid=pid), contextlib.suppress(ProcessLookupError):
                os.kill(pid, 0)
                state = Path(f"/proc/{pid}/stat")
                if state.exists():
                    self.assertIn(state.read_text().split(") ", 1)[1][0], "ZX", f"process {pid} still runs")
                else:
                    self.fail(f"process {pid} still runs")

    def test_a_terminated_run_ends_the_fern_session_it_started(self) -> None:
        pids = self.root / "fern-pids"
        env = dict(self.env, FERN_STUB_HANG=str(pids))
        script = self.root / "tools" / "fern-refusals" / "fern-refusals.py"
        with subprocess.Popen(
            [sys.executable, str(script), "probe", self.CLASS], env=env, cwd=self.root, stderr=subprocess.PIPE
        ) as run:
            deadline = time.monotonic() + 60
            while not pids.exists() and time.monotonic() < deadline:
                time.sleep(0.1)
            run.terminate()
            run.wait(timeout=30)
        self.assertEqual(run.returncode, 128 + signal.SIGTERM)
        started = list(map(int, pids.read_text(encoding="utf-8").split()))
        time.sleep(0.5)
        for pid in started:
            with self.subTest(pid=pid), contextlib.suppress(ProcessLookupError):
                os.kill(pid, 0)
                state = Path(f"/proc/{pid}/stat")
                if not state.exists() or state.read_text().split(") ", 1)[1][0] not in "ZX":
                    self.fail(f"process {pid} still runs")

    def test_without_fern_on_path_the_setup_recipe_is_named(self) -> None:
        self.env["PATH"] = str(self.root / "no-fern")
        result = self.script("probe", self.CLASS)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("`fern` is not on PATH; run `just setup-fern`", result.stderr)

    def test_finding_records_the_exits_of_a_check_only_phrase(self) -> None:
        self.finding_row[2:4] = ["7", "7"]
        write_rows(self.registry / "findings.tsv", [rows(self.registry / "findings.tsv")[0], self.finding_row])
        result = self.script(
            "finding",
            self.FINDING,
            check_exit="1",
            check_output=f"issue: {phrase(self.finding_row[4])}",
            generate_files="4",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual("fern-refusals: 1 finding(s) recorded\n", result.stdout)
        [row] = rows(self.registry / "findings.tsv")[1:]
        self.assertEqual(row[2:4], ["1", "0"])

    def test_finding_measures_a_class_probe_fern_now_generates_from(self) -> None:
        # The retiring case: a `generates` finding whose probe is the class's own.
        retiring = [f"{self.CLASS}-generates", "generates", "", "", "—", f"docs/fern-refusals/{self.CLASS}/probe.yml"]
        header = rows(self.registry / "findings.tsv")[0]
        write_rows(self.registry / "findings.tsv", [header, self.finding_row, retiring])
        result = self.script("finding", retiring[0], generate_files="3")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(rows(self.registry / "findings.tsv")[2][2:4], ["0", "0"])
        calls = self.calls_made()
        probe = (self.registry / self.CLASS / "probe.yml").read_text(encoding="utf-8")
        self.assertTrue(calls and all(call["spec"] == probe for call in calls), calls)

    def test_a_finding_fern_refuses_is_refused_as_a_class(self) -> None:
        result = self.script("finding", self.FINDING, check_exit="1", generate_exit="1")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(
            f"{self.FINDING}: the generation exits 1 with 0 files, so Fern refuses the probe; "
            "a refusal is a class, not a finding",
            result.stderr,
        )
        self.assertEqual(rows(self.registry / "findings.tsv")[1], self.finding_row)

    def test_a_check_only_finding_whose_check_is_silent_names_its_log(self) -> None:
        result = self.script("finding", self.FINDING, check_exit="1", generate_files="2")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(
            f"{self.FINDING}: `fern check` printed no diagnostic matching its template; correct the "
            f"template or the probe, reading docs/openapi-surface/fern-refusals/probe-logs/"
            f"{self.FINDING}.check.log",
            result.stderr,
        )

    def carrying_document(self) -> str:
        """A documents.tsv row carrying the class, its bytes in the cache `confirm` samples from."""
        document = (REGISTRY / self.CLASS / "probe.yml").read_bytes()
        digest = hashlib.sha256(document).hexdigest()
        cache = self.root / ".local" / "fern-refusals" / "documents"
        cache.mkdir(parents=True)
        (cache / f"{digest}.yml").write_bytes(document)
        header = rows(REGISTRY / "documents.tsv")[0]
        row = dict.fromkeys(header, "—")
        row.update(
            digest=digest,
            source="scratch",
            classes=self.CLASS,
            locator="https://raw.githubusercontent.com/acme/api/0/openapi.yml",
        )
        write_rows(self.registry / "documents.tsv", [header, [row[column] for column in header]])
        return digest

    def test_confirm_runs_a_carrying_documents_generation_and_records_it(self) -> None:
        digest = self.carrying_document()
        result = self.script(
            "confirm", check_output="unused", generate_exit="1", generate_output=f"[error] {phrase(self.class_row[4])}"
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual("fern-refusals: 1 confirmation(s) taken, 1 on record\n", result.stdout)
        log = f"docs/openapi-surface/fern-refusals/logs/{digest}.generate.log"
        self.assertEqual(
            rows(self.evidence / "confirmations.tsv"),
            [
                ["class", "digest", "publisher", "generate_exit", "generate_files", "generate_log"],
                [self.CLASS, digest, "acme", "1", "0", log],
            ],
        )
        self.assertIn(phrase(self.class_row[4]), (self.root / log).read_text(encoding="utf-8"))
        self.assertEqual([call["argv"][0] for call in self.calls_made()], ["generate"])
        # A class already sampled `--per-class` times is not run again.
        again = self.script("confirm", "--per-class", "1")
        self.assertEqual(again.returncode, 0, again.stdout + again.stderr)
        self.assertEqual("fern-refusals: 0 confirmation(s) taken, 1 on record\n", again.stdout)
        self.assertEqual(len(self.calls_made()), 1)

    def test_confirm_reuses_a_generation_measure_took_at_the_pair(self) -> None:
        digest = self.carrying_document()
        log = f"docs/openapi-surface/fern-refusals/logs/{digest}.generate.log"
        (self.root / log).parent.mkdir(parents=True)
        (self.root / log).write_text(PAIR_LINE + f"[error] {phrase(self.class_row[4])}\n", encoding="utf-8")
        measured = {
            "key": digest,
            "digest": digest,
            "check_exit": "0",
            "generate_exit": "1",
            "generate_files": "0",
            "generate_log": log,
        }
        pair = {"fern_cli": CERTIFIED["cliVersion"], "fern_python_sdk": CERTIFIED["generatorVersion"]}
        (self.evidence / "measurements.jsonl").write_text(json.dumps(dict(measured, **pair)) + "\n", encoding="utf-8")
        result = self.script("confirm")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.calls_made(), [])
        self.assertEqual(rows(self.evidence / "confirmations.tsv")[1], [self.CLASS, digest, "acme", "1", "0", log])
        # A generation an older pair took is no confirmation: `confirm` runs Fern again.
        (self.evidence / "confirmations.tsv").unlink()
        (self.evidence / "measurements.jsonl").write_text(json.dumps(measured) + "\n", encoding="utf-8")
        result = self.script("confirm", generate_exit="1")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual([call["argv"][0] for call in self.calls_made()], ["generate"])

    def test_confirm_retakes_a_confirmation_another_pair_took(self) -> None:
        digest = self.carrying_document()
        log = f"docs/openapi-surface/fern-refusals/logs/{digest}.generate.log"
        (self.root / log).parent.mkdir(parents=True)
        (self.root / log).write_text(f"[error] {phrase(self.class_row[4])}\n", encoding="utf-8")
        write_rows(
            self.evidence / "confirmations.tsv",
            [
                ["class", "digest", "publisher", "generate_exit", "generate_files", "generate_log"],
                [self.CLASS, digest, "acme", "1", "0", log],
            ],
        )
        result = self.script("confirm", generate_exit="1", generate_output=f"[error] {phrase(self.class_row[4])}")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual("fern-refusals: 1 confirmation(s) taken, 1 on record\n", result.stdout)
        self.assertEqual([call["argv"][0] for call in self.calls_made()], ["generate"])
        self.assertTrue((self.root / log).read_text(encoding="utf-8").startswith(PAIR_LINE))

    def test_confirm_drops_a_confirmation_of_a_document_that_no_longer_carries_the_class(self) -> None:
        carrying = self.carrying_document()
        log = f"docs/openapi-surface/fern-refusals/logs/{carrying}.generate.log"
        (self.root / log).parent.mkdir(parents=True)
        (self.root / log).write_text(PAIR_LINE + f"[error] {phrase(self.class_row[4])}\n", encoding="utf-8")
        # Taken at the pair, but of a document a later measurement no longer files under the class.
        gone = "0" * 64
        header = ["class", "digest", "publisher", "generate_exit", "generate_files", "generate_log"]
        write_rows(self.evidence / "confirmations.tsv", [header, [self.CLASS, gone, "other", "1", "0", log]])
        result = self.script("confirm", generate_exit="1", generate_output=f"[error] {phrase(self.class_row[4])}")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual("fern-refusals: 1 confirmation(s) taken, 1 on record\n", result.stdout)
        self.assertEqual(
            rows(self.evidence / "confirmations.tsv"), [header, [self.CLASS, carrying, "acme", "1", "0", log]]
        )

    def shape(self, name: str, marker: str) -> Path:
        """A shape file in the scratch class directory: the class probe's bytes plus `marker`."""
        path = self.registry / self.CLASS / name
        path.write_text((REGISTRY / self.CLASS / "probe.yml").read_text(encoding="utf-8") + f"# {marker}\n")
        return path

    def shape_rows(self) -> dict[str, dict[str, str]]:
        table = rows(self.evidence / "shapes.tsv")
        return {row[1]: dict(zip(table[0], row, strict=True)) for row in table[1:]}

    def shape_problems(self) -> list[str]:
        """`check`'s verdict on the scratch shapes, from the REAL script loaded at the scratch root."""
        spec = importlib.util.spec_from_file_location(
            "fern_refusals_scratch", self.root / "tools" / "fern-refusals" / "fern-refusals.py"
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        problems: list[str] = module.shape_problems()
        return problems

    def test_shapes_records_a_refused_probe_and_a_generated_control_and_keeps_each_at_the_pair(self) -> None:
        said = phrase(self.class_row[4])
        self.shape("alpha-probe.yml", "alpha")
        result = self.script("shapes", self.CLASS, check_exit="1", check_output=f"issue: {said}")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual("fern-refusals: 1 shape(s) measured, 1 on record\n", result.stdout)
        alpha = self.shape_rows()["alpha-probe.yml"]
        log = f"docs/fern-refusals/{self.CLASS}/evaluation-logs/fern-alpha.log"
        self.assertEqual(
            [alpha[key] for key in ("role", "check_exit", "generate_exit", "classes", "verdict", "log")],
            ["probe", "1", "—", self.CLASS, "refused", log],
        )
        written = (self.root / log).read_text(encoding="utf-8")
        self.assertTrue(written.startswith(PAIR_LINE + "check exit: 1\n"), written)
        self.assertIn(said, written)
        # The check named the class, which stops the generation: it was not run.
        self.assertEqual([call["argv"][0] for call in self.calls_made()], ["check"])
        # A near miss Fern generates from; the probe, measured at the pair over these bytes, is kept.
        self.shape("beta-control.yml", "beta")
        result = self.script("shapes", generate_files="3")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual("fern-refusals: 1 shape(s) measured, 2 on record\n", result.stdout)
        beta = self.shape_rows()["beta-control.yml"]
        self.assertEqual(
            [beta[key] for key in ("role", "check_exit", "generate_exit", "generate_files", "classes", "verdict")],
            ["control", "0", "0", "3", "—", "generates"],
        )
        self.assertIn("generate exit: 0\nfiles: 3\n", (self.root / beta["log"]).read_text(encoding="utf-8"))
        self.assertEqual([call["argv"][0] for call in self.calls_made()], ["check", "check", "generate"])
        self.assertEqual(self.shape_problems(), [])

    def test_check_names_a_probe_fern_generates_from_and_a_log_another_pair_took(self) -> None:
        probe = self.shape("alpha-probe.yml", "alpha")
        self.assertEqual(
            self.shape_problems(),
            [
                "docs/openapi-surface/fern-refusals/shapes.tsv is missing; run `tools/fern-refusals/fern-refusals.py shapes`"
            ],
        )
        result = self.script("shapes", generate_files="2")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.shape_rows()["alpha-probe.yml"]["verdict"], "generates")
        self.assertEqual(
            self.shape_problems(),
            [
                f"docs/fern-refusals/{self.CLASS}/alpha-probe.yml: Fern generates from the probe; make it a "
                "control and narrow crozier's detector to match"
            ],
        )
        # A log an older pair took says nothing of this one: `check` names it and `shapes` takes it again.
        log = self.root / self.shape_rows()["alpha-probe.yml"]["log"]
        older = "Fern CLI 5.67.1, python-sdk 5.20.0"  # certified-pair: stand-in (a pair before the certified one)
        log.write_text(f"{older}\ncheck exit: 1\n", encoding="utf-8")
        self.assertIn("is not one `shapes` wrote at Fern CLI", self.shape_problems()[0])
        said = phrase(self.class_row[4])
        result = self.script("shapes", check_exit="1", check_output=f"issue: {said}")
        self.assertEqual("fern-refusals: 1 shape(s) measured, 1 on record\n", result.stdout)
        self.assertEqual(self.shape_problems(), [])
        # Other bytes than were measured are unmeasured, and so is a control Fern refuses.
        probe.write_text(probe.read_text(encoding="utf-8") + "# edited\n", encoding="utf-8")
        probe.rename(probe.with_name("alpha-control.yml"))
        self.assertEqual(
            self.shape_problems(),
            [
                f"docs/fern-refusals/{self.CLASS}/alpha-control.yml: not measured over these bytes; "
                f"run `tools/fern-refusals/fern-refusals.py shapes {self.CLASS}`",
                f"docs/openapi-surface/fern-refusals/shapes.tsv names alpha-probe.yml of {self.CLASS}, which is "
                "not committed; rerun `shapes`",
            ],
        )
        result = self.script("shapes", check_exit="1", check_output=f"issue: {said}")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(list(self.shape_rows()), ["alpha-control.yml"])
        calls = len(self.calls_made())
        # Renamed back to a probe over the same bytes, it keeps the measurement it has.
        probe.with_name("alpha-control.yml").rename(probe)
        result = self.script("shapes")
        self.assertEqual("fern-refusals: 0 shape(s) measured, 1 on record\n", result.stdout)
        self.assertEqual(len(self.calls_made()), calls)
        self.assertEqual(self.shape_rows()["alpha-probe.yml"]["role"], "probe")
        self.assertEqual(self.shape_problems(), [])
        probe.rename(probe.with_name("alpha-control.yml"))
        result = self.script("shapes")
        self.assertEqual(list(self.shape_rows()), ["alpha-control.yml"])
        self.assertEqual(
            self.shape_problems(),
            [
                f"docs/fern-refusals/{self.CLASS}/alpha-control.yml: Fern refuses the control with {self.CLASS}; "
                "make it a probe of the class that names it"
            ],
        )

    def test_a_name_both_roles_share_keeps_a_log_per_role(self) -> None:
        said = phrase(self.class_row[4])
        self.shape("alpha-probe.yml", "probe")
        self.shape("alpha-control.yml", "control")
        self.assertEqual(self.script("shapes", check_exit="1", check_output=f"issue: {said}").returncode, 0)
        logs = {name: row["log"] for name, row in self.shape_rows().items()}
        self.assertEqual(
            logs,
            {
                "alpha-control.yml": f"docs/fern-refusals/{self.CLASS}/evaluation-logs/fern-alpha-control.log",
                "alpha-probe.yml": f"docs/fern-refusals/{self.CLASS}/evaluation-logs/fern-alpha-probe.log",
            },
        )
        for log in logs.values():
            self.assertIn(said, (self.root / log).read_text(encoding="utf-8"))

    def test_check_names_a_row_its_log_does_not_derive(self) -> None:
        said = phrase(self.class_row[4])
        self.shape("alpha-probe.yml", "alpha")
        self.assertEqual(self.script("shapes", check_exit="1", check_output=f"issue: {said}").returncode, 0)
        self.assertEqual(self.shape_problems(), [])
        table = rows(self.evidence / "shapes.tsv")
        table[1][table[0].index("check_exit")] = "0"
        write_rows(self.evidence / "shapes.tsv", table)
        log = f"docs/fern-refusals/{self.CLASS}/evaluation-logs/fern-alpha.log"
        self.assertEqual(
            self.shape_problems(),
            [
                f"docs/fern-refusals/{self.CLASS}/alpha-probe.yml: shapes.tsv disagrees with its log {log}; "
                f"run `tools/fern-refusals/fern-refusals.py shapes {self.CLASS}`"
            ],
        )
        # `shapes` re-derives the row from its log, with no Fern run.
        calls = len(self.calls_made())
        self.assertEqual(self.script("shapes").returncode, 0)
        self.assertEqual(len(self.calls_made()), calls)
        self.assertEqual(self.shape_problems(), [])
        # A log whose exit is no exit status is no measurement at all.
        written = (self.root / log).read_text(encoding="utf-8")
        (self.root / log).write_text(written.replace("check exit: 1\n", "check exit: maybe\n"), encoding="utf-8")
        self.assertEqual(
            self.shape_problems(),
            [
                f"docs/fern-refusals/{self.CLASS}/alpha-probe.yml: its log {log} is not one `shapes` wrote at Fern "
                f"CLI {CERTIFIED['cliVersion']} with fernapi/fern-python-sdk {CERTIFIED['generatorVersion']}; "
                f"run `tools/fern-refusals/fern-refusals.py shapes {self.CLASS}`"
            ],
        )

    def test_shapes_measures_only_the_named_class_and_again_runs_fern_anew(self) -> None:
        other = "named-type-default"
        classes = rows(REGISTRY / "classes.tsv")
        write_rows(
            self.registry / "classes.tsv",
            [classes[0], *sorted([self.class_row, next(row for row in classes[1:] if row[0] == other)])],
        )
        (self.registry / other).mkdir()
        shutil.copy(REGISTRY / other / "probe.yml", self.registry / other / "beta-control.yml")
        self.shape("alpha-control.yml", "alpha")
        self.assertEqual(self.script("shapes", generate_files="2").returncode, 0)
        before = self.shape_rows()
        self.assertEqual(sorted(before), ["alpha-control.yml", "beta-control.yml"])
        calls = len(self.calls_made())
        # Named, one class is measured again from scratch; the other's row is untouched.
        result = self.script("shapes", self.CLASS, "--again", generate_files="3")
        self.assertEqual("fern-refusals: 1 shape(s) measured, 2 on record\n", result.stdout)
        after = self.shape_rows()
        self.assertEqual([call["argv"][0] for call in self.calls_made()[calls:]], ["check", "generate"])
        self.assertEqual(after["alpha-control.yml"]["generate_files"], "3")
        self.assertEqual(after["beta-control.yml"], before["beta-control.yml"])

    def test_a_shape_past_the_bound_is_unmeasured_never_a_verdict(self) -> None:
        self.shape("alpha-control.yml", "alpha")
        result = self.script("shapes", "--timeout", "3", hang=str(self.root / "fern-pids"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        alpha = self.shape_rows()["alpha-control.yml"]
        self.assertEqual(
            [alpha[key] for key in ("check_exit", "generate_exit", "verdict")], ["timeout", "—", "unmeasured"]
        )
        self.assertEqual([call["argv"][0] for call in self.calls_made()], ["check"])
        self.assertEqual(self.shape_problems(), [])

    def test_a_shape_whose_generation_runs_past_the_bound_is_unmeasured(self) -> None:
        self.shape("alpha-control.yml", "alpha")
        result = self.script(
            "shapes", "--timeout", "3", hang=str(self.root / "fern-pids"), hang_stage="generate", generate_files="3"
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        alpha = self.shape_rows()["alpha-control.yml"]
        self.assertEqual(
            [alpha[key] for key in ("check_exit", "generate_exit", "generate_files", "verdict")],
            ["0", "timeout", "0", "unmeasured"],
        )
        # The check finished and named no class, so the generation ran, and was ended.
        self.assertEqual([call["argv"][0] for call in self.calls_made()], ["check", "generate"])
        self.assertEqual(self.shape_problems(), [])

    def test_a_shape_recorded_twice_is_refused_rather_than_one_row_kept(self) -> None:
        said = phrase(self.class_row[4])
        self.shape("alpha-probe.yml", "alpha")
        result = self.script("shapes", self.CLASS, check_exit="1", check_output=f"issue: {said}")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.shape_problems(), [])
        # A second, contradictory row for the same shape: neither is believed.
        table = rows(self.evidence / "shapes.tsv")
        twice = [*table[1][:8], "generates", *table[1][9:]]
        write_rows(self.evidence / "shapes.tsv", [*table, twice])
        refusal = f"records alpha-probe.yml of {self.CLASS} twice; delete both rows and rerun `shapes`"
        # `check`'s shape verdict refuses the table...
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit):
            self.shape_problems()
        self.assertIn(refusal, stderr.getvalue())
        # ...and so does `shapes`, which measures nothing over it.
        result = self.script("shapes", self.CLASS)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(refusal, result.stderr)
        self.assertEqual(len(rows(self.evidence / "shapes.tsv")), 3, "a refused table was rewritten anyway")

    def test_shapes_refuses_a_class_the_registry_does_not_name(self) -> None:
        result = self.script("shapes", "no-such-class")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("no classes.tsv row for no-such-class; add the row first", result.stderr)


# What `measure` loads by repository path besides the script: the witness-search
# GitHub acquirer its fetcher runs (with the modules that pulls in), the census
# reader and region keys, and the pin reader the census imports.
MEASURE_LOADS = (
    *SCRIPT_LOADS,
    "tools/witness-search/witness-search-github.py",
    "tools/witness-search/witness-search-github-index.py",
    "tools/witness-search/witness_screen.py",
    "tools/witness-search/rate_limit_guard.py",
    "tools/witness-search/witness-search-redo.py",
    "tools/surface-census/openapi-surface-census.py",
    "tools/surface-census/witness-search-region-keys.py",
    "tools/corpus/corpus_remote_ref_pins.py",
)


@unittest.skipIf(os.name == "nt", "the stand-in `fern` and `crozier` are POSIX shell scripts")
class MeasuredAtThePair(unittest.TestCase):
    """`measure` takes every Fern verdict at the certified pair. It runs the REAL
    script from a scratch checkout over committed records of two kinds — screens
    whose `fern check` log the screen took, and `measurements.jsonl` rows — one
    of each taken at an older pair and one at the current pair, with a stand-in
    `fern` (`FERN_STUB`) and a stand-in `crozier` that count their runs. What was
    taken at the older pair is measured afresh; what was taken at the current
    pair is reused, and no Fern runs over it."""

    CLASS = "type-name-collision"
    OLD = "CLI 5.67.1 with fernapi/fern-python-sdk:5.20.0"  # certified-pair: stand-in (a screen's older pair)
    CURRENT = f"CLI {CERTIFIED['cliVersion']} with fernapi/fern-python-sdk:{CERTIFIED['generatorVersion']}"

    def setUp(self) -> None:
        self.scratch = tempfile.TemporaryDirectory()
        self.root = root = Path(self.scratch.name)
        shutil.copytree(REPO / "scripts", root / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
        for relative in MEASURE_LOADS:
            (root / relative).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / relative, root / relative)
        (root / "tests" / "fixtures").mkdir(parents=True)
        (root / "tests" / "fixtures" / "CORPUS.md").write_text("", encoding="utf-8")
        surface = root / "docs" / "openapi-surface"
        self.evidence = surface / "fern-refusals"
        self.evidence.mkdir(parents=True)
        (self.evidence / "dropped-sources.tsv").write_text(
            "name\tcorpus_line\tsource\tlocator\trevision\tsha256\tevidence\treason\n", encoding="utf-8"
        )
        for source in ("jentic", "apis.guru", "vendor-portals", "github-publisher-trees"):
            (surface / "golden-reach-witnesses" / source).mkdir(parents=True)
            with gzip.open(
                surface / "golden-reach-witnesses" / source / "enumeration.tsv.gz", "wt", encoding="utf-8"
            ) as handle:
                handle.write("walk\tdocument\trevision\tsha256\n")
        for source in ("github-code-search", "sourcegraph"):
            (surface / "golden-reach-witnesses" / source).mkdir(parents=True)
            (surface / "golden-reach-witnesses" / source / "candidates.jsonl").write_text("", encoding="utf-8")
        registry = root / "docs" / "fern-refusals"
        registry.mkdir()
        classes = rows(REGISTRY / "classes.tsv")
        self.class_row = next(row for row in classes[1:] if row[0] == self.CLASS)
        write_rows(registry / "classes.tsv", [classes[0], self.class_row])
        write_rows(registry / "findings.tsv", rows(REGISTRY / "findings.tsv")[:1])
        # Four documents, each its own bytes, supplied by digest from `--root`.
        (root / "documents").mkdir()
        probe = (REGISTRY / self.CLASS / "probe.yml").read_bytes()
        self.documents = {}
        for name in ("screened-old", "screened-current", "measured-old", "measured-current"):
            data = probe + f"\n# {name}\n".encode()
            (root / "documents" / f"{name}.yml").write_bytes(data)
            self.documents[name] = hashlib.sha256(data).hexdigest()
        # Two screens whose check logs refuse the document with the class's phrase.
        screens = surface / "scratch"
        screens.mkdir()
        said = f"issue: {phrase(self.class_row[4])}\n"
        records = []
        for name, pair in (("screened-old", self.OLD), ("screened-current", self.CURRENT)):
            (screens / f"{name}-check.log").write_text(said, encoding="utf-8")
            records.append(
                {
                    "fern": f"failed: `fern check` exit 1 at {pair}",
                    "source": "scratch",
                    "repository": "scratch/apis",
                    "commit": "0" * 40,
                    "path": f"{name}.yml",
                    "sha256": self.documents[name],
                    "fern_logs": [f"{name}-check.log"],
                }
            )
        # Two more screens with no log of their own, measured already: one at an
        # older pair (no pair recorded), one at the current pair.
        logs = self.evidence / "logs"
        logs.mkdir()
        measured = []
        for name, pair in (("measured-old", None), ("measured-current", CERTIFIED)):
            digest = self.documents[name]
            log = logs / f"{digest}.check.log"
            log.write_text((PAIR_LINE if pair else "") + said, encoding="utf-8")
            records.append(
                {
                    "fern": "failed: `fern check` refused it",
                    "source": "scratch",
                    "repository": "scratch/apis",
                    "commit": "0" * 40,
                    "path": f"{name}.yml",
                    "sha256": digest,
                }
            )
            strict = self.evidence / "crozier-logs" / f"{digest}.strict.log"
            strict.parent.mkdir(exist_ok=True)
            strict.write_text(self.stand_in_log(), encoding="utf-8")
            row = {
                "key": digest,
                "digest": digest,
                "unretrievable": "",
                "check_exit": "1",
                "check_log": log.relative_to(root).as_posix(),
                "crozier_exit": "1",
                "crozier_files": "0",
                "crozier_strict_exit": "1",
                "crozier_strict_log": strict.relative_to(root).as_posix(),
            }
            if pair:
                row.update(fern_cli=pair["cliVersion"], fern_python_sdk=pair["generatorVersion"])
            measured.append(row)
        (screens / "screens.jsonl").write_text("".join(json.dumps(record) + "\n" for record in records), "utf-8")
        self.measurements = self.evidence / "measurements.jsonl"
        self.measurements.write_text("".join(json.dumps(row) + "\n" for row in measured), encoding="utf-8")
        # A stand-in crozier that refuses every document with the class's
        # diagnostic, as the real one prints it, and counts its runs.
        self.crozier_calls = root / "crozier-calls"
        crozier = root / "target" / "release" / "crozier"
        crozier.parent.mkdir(parents=True)
        crozier.write_text(
            "#!/bin/sh\n"
            f'echo "$*" >> {shlex.quote(str(self.crozier_calls))}\n'
            'while [ $# -gt 0 ]; do case "$1" in --spec) spec=$2;; --output) output=$2;; esac; shift; done\n'
            f'printf %s "{self.refusal("$spec")}" >&2\n'
            'printf "wrote nothing into %s\\n" "$output" >&2\n'
            "exit 1\n",
            "utf-8",
        )
        crozier.chmod(0o755)
        self.calls = root / "fern-calls.jsonl"
        self.env = {key: value for key, value in os.environ.items() if not key.startswith(("CROZIER", "FERN_STUB"))}
        self.env.update(
            PATH=f"{stub_fern(root / 'bin')}{os.pathsep}{self.env.get('PATH', '')}",
            FERN_STUB_CALLS=str(self.calls),
            FERN_STUB_CHECK_EXIT="1",
            FERN_STUB_CHECK_OUTPUT=said.strip(),
        )

    def tearDown(self) -> None:
        self.scratch.cleanup()

    def refusal(self, document: str) -> str:
        """What crozier's `--fern-strict` run prints refusing `document` with the class."""
        return f"crozier: invalid OpenAPI document {document}: {self.CLASS}: type Widget (fern-strict refusal)\n"

    def stand_in_log(self) -> str:
        """The strict log `measure` commits from the stand-in crozier's stderr: both scratch paths made generic."""
        return self.refusal("<document>") + "wrote nothing into <output>\n"

    def script(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.root / "tools" / "fern-refusals" / "fern-refusals.py"), *args],
            capture_output=True,
            text=True,
            env=self.env,
            cwd=self.root,
        )

    def measure(self, *args: str) -> dict[str, dict[str, str]]:
        result = self.script("measure", "--jobs", "1", "--root", str(self.root / "documents"), *args)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return {row["key"]: row for row in map(json.loads, self.measurements.read_text(encoding="utf-8").splitlines())}

    def checked(self) -> list[str]:
        """The documents `fern check` ran over, by name."""
        if not self.calls.exists():
            return []
        names = {self.documents[name]: name for name in self.documents}
        return [
            names[hashlib.sha256(call["spec"].encode()).hexdigest()]
            for call in map(json.loads, self.calls.read_text(encoding="utf-8").splitlines())
            if call["argv"][0] == "check"
        ]

    def test_a_verdict_taken_at_an_older_pair_is_measured_afresh_and_one_at_the_pair_reused(self) -> None:
        measured = self.measure()
        # Fern ran exactly over the two documents whose verdicts an older pair took.
        self.assertEqual(sorted(self.checked()), ["measured-old", "screened-old"])
        pair = (CERTIFIED["cliVersion"], CERTIFIED["generatorVersion"])
        for name, row in ((name, measured[digest]) for name, digest in self.documents.items()):
            with self.subTest(document=name):
                self.assertEqual((row["fern_cli"], row["fern_python_sdk"]), pair)
                self.assertEqual(row["check_exit"], "1")
        # The fresh logs are written at the pair, and say so on their first line.
        for name in ("screened-old", "measured-old"):
            digest = self.documents[name]
            log = f"docs/openapi-surface/fern-refusals/logs/{digest}.check.log"
            self.assertEqual(measured[digest]["check_log"], log)
            first = (self.root / log).read_text(encoding="utf-8").splitlines()[0]
            self.assertEqual(first, f"fern-refusals: Fern CLI {pair[0]}, fernapi/fern-python-sdk {pair[1]}", name)
        # The screen taken at the pair keeps its own log; Fern never ran over it.
        current = self.documents["screened-current"]
        self.assertEqual(measured[current]["check_log"], "docs/openapi-surface/scratch/screened-current-check.log")
        # crozier ran only where no verdict was on record — the two screened documents — and only
        # its `--fern-strict` run, the verdict the registry reads; no default-mode generation.
        runs = self.crozier_calls.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(runs), 2, runs)
        self.assertTrue(all("--fern-strict" in run for run in runs), runs)
        for name in ("screened-old", "screened-current"):
            row = measured[self.documents[name]]
            self.assertEqual((row["crozier_strict_exit"], row["crozier_exit"], row["crozier_files"]), ("1", "", ""))
        # Everything is now at the pair, so a second run measures nothing.
        self.calls.unlink()
        self.assertEqual(self.measure(), measured)
        self.assertEqual(self.checked(), [])

    def test_crozier_s_strict_diagnostic_is_committed_and_holds_each_refused_record(self) -> None:
        measured = self.measure()
        # Each strict run's stderr is committed beside Fern's logs, the scratch
        # path of the document made generic, and the record names it.
        for name, digest in self.documents.items():
            with self.subTest(document=name):
                log = f"docs/openapi-surface/fern-refusals/crozier-logs/{digest}.strict.log"
                self.assertEqual(measured[digest]["crozier_strict_log"], log)
                self.assertEqual((self.root / log).read_text(encoding="utf-8"), self.stand_in_log())
        built = self.script("build")
        self.assertEqual(built.returncode, 0, built.stdout + built.stderr)
        [row] = rows(self.root / "docs" / "fern-refusals" / "classes.tsv")[1:]
        self.assertEqual(row[8], "4/4")

        # A refusal at the parser, before any class detector, is no refusal by the class.
        stopped = self.documents["measured-current"]
        log = self.root / measured[stopped]["crozier_strict_log"]
        parser = "crozier: could not parse OpenAPI document <document>: alias replay limit exceeded\n"
        log.write_text(parser, encoding="utf-8")
        built = self.script("build")
        self.assertNotEqual(built.returncode, 0, built.stdout)
        self.assertIn(f"{stopped}: crozier --fern-strict stops at `{parser.strip()}`", built.stderr)
        self.assertIn(f"not with a diagnostic of its classes {self.CLASS}", built.stderr)

        # Nor is a refusal by a class the document does not carry.
        log.write_text(self.refusal("<document>").replace(self.CLASS, "type-name-not-letter-led"), encoding="utf-8")
        self.assertIn(f"{stopped}: crozier --fern-strict stops at", self.script("build").stderr)

        # A recorded exit the log does not bear out is named too.
        log.write_text("", encoding="utf-8")
        self.assertIn(f"{stopped}: crozier_strict_exit 1 disagrees with", self.script("build").stderr)

        # A record whose log is gone is taken again, with no Fern run.
        log.unlink()
        self.calls.unlink()
        self.crozier_calls.unlink()
        self.measure()
        self.assertEqual(len(self.crozier_calls.read_text(encoding="utf-8").splitlines()), 1)
        self.assertFalse(self.calls.exists(), "Fern ran again over a verdict already at the pair")
        self.assertEqual(self.script("build").returncode, 0)

    def test_crozier_runs_in_lanes_of_its_own_beside_one_fern_lane(self) -> None:
        # A stand-in crozier that holds each run open long enough for lanes to overlap.
        spans = self.root / "crozier-spans"
        (self.root / "target" / "release" / "crozier").write_text(
            "#!/bin/sh\n"
            f'echo "start $(date +%s.%N)" >> {shlex.quote(str(spans))}\n'
            "sleep 0.5\n"
            f'echo "end $(date +%s.%N)" >> {shlex.quote(str(spans))}\n'
            "exit 1\n",
            encoding="utf-8",
        )

        def widest(lanes: str) -> int:
            spans.unlink(missing_ok=True)
            self.measure("--crozier-jobs", lanes, "--crozier-again")
            open_runs, most = 0, 0
            events = sorted(
                (float(at), kind) for kind, at in (line.split() for line in spans.read_text("utf-8").splitlines())
            )
            for _at, kind in events:
                open_runs += 1 if kind == "start" else -1
                most = max(most, open_runs)
            self.assertEqual(sum(kind == "start" for _at, kind in events), len(self.documents))
            return most

        # Fern keeps its one `--jobs` lane while crozier takes `--crozier-jobs` of its own.
        self.assertEqual(widest("2"), 2)
        self.assertEqual(widest("1"), 1)

    def test_a_check_past_the_time_bound_is_recorded_unmeasured_and_not_generated(self) -> None:
        self.env["FERN_STUB_HANG"] = str(self.root / "fern-pids")
        measured = self.measure("--timeout", "2")
        for name in ("screened-old", "measured-old"):
            with self.subTest(document=name):
                row = measured[self.documents[name]]
                self.assertEqual((row["check_exit"], row["generate_exit"]), ("timeout", ""))
        # Only the two checks ran: a check that never finished is not followed by a generation.
        self.assertEqual(sorted(self.checked()), ["measured-old", "screened-old"])
        self.assertEqual(len(self.calls.read_text(encoding="utf-8").splitlines()), 2)
        built = self.script("build")
        self.assertEqual(built.returncode, 0, built.stdout + built.stderr)
        self.assertEqual("fern-refusals: 2 refused, 0 generated, 2 unretrievable\n", built.stdout)
        # The class counts, and how many of them crozier's strict run refuses, come from the same rows.
        [row] = rows(self.root / "docs" / "fern-refusals" / "classes.tsv")[1:]
        self.assertEqual((row[5], row[8]), ("2", "2/2"))
        unretrievable = rows(self.root / "docs" / "fern-refusals" / "unretrievable.tsv")[1:]
        self.assertEqual(
            sorted((row[4], row[5]) for row in unretrievable),
            sorted(
                (
                    self.documents[name],
                    f"unmeasured: `fern check` ran past `measure`'s time bound at Fern CLI "
                    f"{CERTIFIED['cliVersion']} with fernapi/fern-python-sdk {CERTIFIED['generatorVersion']}",
                )
                for name in ("screened-old", "measured-old")
            ),
        )

    def test_a_generation_past_the_time_bound_is_recorded_unmeasured(self) -> None:
        self.env.update(
            FERN_STUB_CHECK_EXIT="0",
            FERN_STUB_CHECK_OUTPUT="",
            FERN_STUB_HANG=str(self.root / "fern-pids"),
            FERN_STUB_HANG_STAGE="generate",
        )
        measured = self.measure("--timeout", "2")
        for name in ("screened-old", "measured-old"):
            with self.subTest(document=name):
                row = measured[self.documents[name]]
                self.assertEqual((row["check_exit"], row["generate_exit"]), ("0", "timeout"))
        # Each check named no class, so each was followed by a generation that never finished.
        stages = [json.loads(line)["argv"][0] for line in self.calls.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(stages, ["check", "generate", "check", "generate"])
        built = self.script("build")
        self.assertEqual(built.returncode, 0, built.stdout + built.stderr)
        self.assertEqual("fern-refusals: 2 refused, 0 generated, 2 unretrievable\n", built.stdout)
        unretrievable = rows(self.root / "docs" / "fern-refusals" / "unretrievable.tsv")[1:]
        self.assertEqual(
            sorted((row[4], row[5]) for row in unretrievable),
            sorted(
                (
                    self.documents[name],
                    f"unmeasured: `fern generate` ran past `measure`'s time bound at Fern CLI "
                    f"{CERTIFIED['cliVersion']} with fernapi/fern-python-sdk {CERTIFIED['generatorVersion']}",
                )
                for name in ("screened-old", "measured-old")
            ),
        )

    def rewrite_measurement(self, name: str, **fields: str) -> None:
        """The measurements.jsonl row of document `name`, with `fields` replaced."""
        digest = self.documents[name]
        table = [json.loads(line) for line in self.measurements.read_text(encoding="utf-8").splitlines()]
        for row in table:
            if row["key"] == digest:
                row.update(fields)
        self.measurements.write_text("".join(json.dumps(row) + "\n" for row in table), encoding="utf-8")

    def test_a_record_of_other_bytes_is_measured_afresh(self) -> None:
        self.measure()
        self.calls.unlink()
        # The record says it measured other bytes than the document now holds.
        self.rewrite_measurement("measured-current", digest="f" * 64)
        measured = self.measure()
        self.assertEqual(self.checked(), ["measured-current"])
        row = measured[self.documents["measured-current"]]
        self.assertEqual(row["digest"], self.documents["measured-current"])
        self.assertTrue((self.root / row["check_log"]).read_text(encoding="utf-8").startswith(PAIR_LINE))

    def test_an_unretrievable_record_another_pair_took_is_fetched_again(self) -> None:
        self.measure()
        self.calls.unlink()
        reason = "fetch failed: the host was down"
        self.rewrite_measurement("measured-old", unretrievable=reason, fern_cli="5.67.1", fern_python_sdk="5.20.0")
        self.rewrite_measurement("measured-current", unretrievable=reason)
        measured = self.measure()
        # The older pair's failed fetch is tried again and measured; this pair's is kept as it stands.
        self.assertEqual(self.checked(), ["measured-old"])
        self.assertEqual(measured[self.documents["measured-old"]]["unretrievable"], "")
        self.assertEqual(measured[self.documents["measured-current"]]["unretrievable"], reason)

    def test_crozier_again_retakes_only_the_strict_verdict(self) -> None:
        self.measure()
        self.crozier_calls.unlink()
        self.calls.unlink()
        self.measure("--crozier-again")
        runs = self.crozier_calls.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(runs), 4, runs)
        self.assertTrue(all("--fern-strict" in run for run in runs), runs)
        self.assertFalse(self.calls.exists(), "Fern ran again over verdicts already at the pair")

    def add_classes(self, *names: str) -> dict[str, list[str]]:
        """The registry's rows for `names`, added to the scratch class's."""
        classes = rows(REGISTRY / "classes.tsv")
        others = {row[0]: row for row in classes[1:] if row[0] in names}
        table = [classes[0], *sorted([self.class_row, *others.values()])]
        write_rows(self.root / "docs" / "fern-refusals" / "classes.tsv", table)
        return others

    def add_document(self, name: str, data: bytes) -> str:
        """A population document Fern's check refuses with the scratch class, supplied by `--root`; its digest."""
        digest = hashlib.sha256(data).hexdigest()
        (self.root / "documents" / name).write_bytes(data)
        screens = self.root / "docs" / "openapi-surface" / "scratch" / "screens.jsonl"
        record = {
            "fern": "failed: `fern check` refused it",
            "source": "scratch",
            "repository": "scratch/apis",
            "commit": "0" * 40,
            "path": name,
            "sha256": digest,
        }
        screens.write_text(screens.read_text(encoding="utf-8") + json.dumps(record) + "\n", encoding="utf-8")
        return digest

    def dispose(self, digest: str, **cells: str) -> None:
        """`dispositions.tsv` holding one row, for `digest`."""
        row = dict.fromkeys(DISPOSITIONS_HEADER, "—")
        row.update(document=digest, **cells)
        table = [list(DISPOSITIONS_HEADER), [row[key] for key in DISPOSITIONS_HEADER]]
        write_rows(self.root / "docs" / "fern-refusals" / "dispositions.tsv", table)

    def test_a_generating_fern_limitation_requires_sdk_evaluation_and_ledger_entry(self) -> None:
        measured = self.measure()
        digest = self.documents["measured-current"]
        entry = measured[digest]
        entry.update(crozier_exit="0", crozier_files="3", crozier_strict_exit="0")
        (self.root / entry["crozier_strict_log"]).write_text("", encoding="utf-8")
        self.measurements.write_text("".join(json.dumps(row) + "\n" for row in measured.values()), encoding="utf-8")
        relative = f"docs/openapi-surface/fern-refusals/limitations/{digest}.json"
        self.dispose(digest, disposition="fern-limitation", representative=digest, log=relative)
        evidence_path = self.root / relative
        evidence_path.parent.mkdir()
        stages = ("validation", "default_generation", "strict_generation", "build", "installation", "imports")
        # This tests metadata admission, not SDK execution: the promoted
        # sdk_env_native_refusal_evaluation test drives the native producer.
        # Raw JSON is deliberately mutated to invalid field types below.
        evidence: dict[str, Any] = json.loads(
            (
                REPO
                / "docs/openapi-surface/fern-refusals/limitations/0ceee3870e41b0bfb0d72172b352d6a12e5dfdfc8dd4e3f2ec28a380d3e33470.json"
            ).read_text()
        )
        evidence["document_sha256"] = digest
        evidence["validation"]["input_sha256"] = digest
        evidence["validation"]["output_sha256"] = digest
        for stage in ("default_generation", "strict_generation"):
            evidence[stage]["input_sha256"] = digest
        ledger = self.root / "docs/fern-limitations.md"
        ledger_text = (
            "## New limitations at the certified pair\n\n"
            f"| `{digest}` | Valid document; Fern refuses its type name. | [SDK evidence](openapi-surface/fern-refusals/limitations/{digest}.json) |\n"
        )

        def write_evidence() -> None:
            evidence_path.write_text(json.dumps(evidence), encoding="utf-8")

        write_evidence()
        ledger.write_text(ledger_text, encoding="utf-8")
        accepted = self.script("build")
        self.assertEqual(accepted.returncode, 0, accepted.stdout + accepted.stderr)
        reduced = self.script("reduce", "--root", str(self.root / "documents"))
        self.assertEqual(reduced.returncode, 0, reduced.stdout + reduced.stderr)
        self.assertEqual(rows(self.root / "docs/fern-refusals/dispositions.tsv")[1][2], "fern-limitation")
        schema = self.script("sdk-evaluation-schema")
        self.assertEqual(schema.returncode, 0, schema.stderr)
        derived = json.loads(schema.stdout)
        self.assertEqual(set(derived["properties"]), set(evidence))
        self.assertEqual(set(derived["required"]), set(evidence))
        self.assertFalse(derived["additionalProperties"])
        self.assertEqual(derived["properties"]["schema_version"]["enum"], [2])
        for stage in stages:
            with self.subTest(stage=stage):
                evidence[stage]["exit"] = 1
                write_evidence()
                failed = self.script("build")
                self.assertNotEqual(failed.returncode, 0)
                self.assertIn(f"{stage}.exit", failed.stderr)
                evidence[stage]["exit"] = 0
        original = evidence["build"]["input_sha256"]
        evidence["build"]["input_sha256"] = "f" * 64
        write_evidence()
        self.assertIn("build input digest", self.script("build").stderr)
        evidence["build"]["input_sha256"] = original
        imports = evidence.pop("imports")
        write_evidence()
        self.assertIn("missing fields ['imports']", self.script("build").stderr)
        evidence["imports"] = imports
        original_command = evidence["validation"]["command"]
        evidence["validation"]["command"] = "not-an-array"
        write_evidence()
        self.assertIn("validation.command: expected an array", self.script("build").stderr)
        evidence["validation"]["command"] = original_command
        write_evidence()
        ledger.write_text("## Historical measurements\n", encoding="utf-8")
        failed = self.script("build")
        self.assertNotEqual(failed.returncode, 0)
        self.assertIn("matching new-limitations ledger entry", failed.stderr)
        ledger.write_text(ledger_text, encoding="utf-8")
        evidence_path.unlink()
        self.assertIn("cannot read SDK evidence", self.script("build").stderr)
        write_evidence()
        evidence["document_sha256"] = "c" * 64
        write_evidence()
        self.assertIn("wrong document or certified pair", self.script("build").stderr)
        evidence["document_sha256"] = digest
        write_evidence()
        entry["crozier_exit"] = "1"
        self.measurements.write_text("".join(json.dumps(row) + "\n" for row in measured.values()), encoding="utf-8")
        self.assertIn("requires generation in both modes", self.script("build").stderr)
        entry["crozier_exit"] = "0"
        self.measurements.write_text("".join(json.dumps(row) + "\n" for row in measured.values()), encoding="utf-8")
        self.assertEqual(self.script("build").returncode, 0)

    def test_both_refuse_relation_requires_a_fern_generation_refusal(self) -> None:
        self.add_classes("generator-lint-failure", "path-parameter-unreferenced")
        document = {
            "openapi": "3.0.3",
            "info": {"title": "Reading relation", "version": "1"},
            "paths": {
                "/readings": {
                    "put": {
                        "parameters": [{"in": "path", "name": "id", "required": True, "schema": {"type": "string"}}],
                        "responses": {"200": {"description": "OK"}},
                    }
                }
            },
        }
        digest = self.add_document("both-refuse.json", json.dumps(document).encode())
        measured = self.measure()
        entry = measured[digest]
        log = self.evidence / "logs" / f"{digest}.generate.log"
        said = "Failed to run command: ruff check generated.py"
        log.write_text(PAIR_LINE + "[error] " + said + "\n", encoding="utf-8")
        entry.update(
            check_exit="0", generate_exit="1", generate_files="0", generate_log=log.relative_to(self.root).as_posix()
        )
        (self.root / entry["check_log"]).write_text(PAIR_LINE, encoding="utf-8")
        strict = self.root / entry["crozier_strict_log"]
        strict.write_text(
            "crozier: invalid OpenAPI document <document>: path-parameter-unreferenced: PUT /readings parameter id\n",
            encoding="utf-8",
        )
        self.measurements.write_text("".join(json.dumps(row) + "\n" for row in measured.values()), encoding="utf-8")
        self.dispose(
            digest, crozier_class="path-parameter-unreferenced", disposition="both-refuse", representative=digest
        )
        self.env.update(
            FERN_STUB_CHECK_EXIT="0",
            FERN_STUB_CHECK_OUTPUT="",
            FERN_STUB_GENERATE_EXIT="1",
            FERN_STUB_GENERATE_OUTPUT="[error] " + said,
        )
        reduced = self.script("reduce", "--root", str(self.root / "documents"))
        self.assertEqual(reduced.returncode, 0, reduced.stdout + reduced.stderr)
        result = self.script("build")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(rows(self.root / "docs/fern-refusals/dispositions.tsv")[1][2], "both-refuse")
        entry.update(generate_exit="0", generate_files="1")
        log.write_text(PAIR_LINE, encoding="utf-8")
        self.measurements.write_text("".join(json.dumps(row) + "\n" for row in measured.values()), encoding="utf-8")
        result = self.script("build")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Fern generates it, but crozier --fern-strict stops", result.stderr)

    def test_a_refusal_by_a_class_fern_does_not_report_is_held_to_its_recorded_disposition(self) -> None:
        registry = self.root / "docs" / "fern-refusals"
        # Two more classes: one only `fern generate` reports, one its check does.
        others = self.add_classes("generator-lint-failure", "object-extends-non-object")
        # A JSON document Fern refuses with the scratch class, its own representative.
        document = {"openapi": "3.0.3", "info": {"title": "t", "version": "1"}, "paths": {}, "x-note": "reduce me"}
        digest = self.add_document("json-current.json", json.dumps(document).encode())
        measured = self.measure()
        strict = self.root / measured[digest]["crozier_strict_log"]

        def built() -> subprocess.CompletedProcess[str]:
            return self.script("build")

        def refused_with(cls: str) -> None:
            strict.write_text(self.refusal("<document>").replace(self.CLASS, cls), encoding="utf-8")

        def dispose(**cells: str) -> None:
            self.dispose(digest, **cells)

        self.assertEqual(built().returncode, 0, built().stderr)
        # A check-stage class Fern's log does not carry fails the build until disposed.
        refused_with("object-extends-non-object")
        result = built()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(f"{digest}: crozier --fern-strict stops at", result.stderr)
        self.assertIn("dispositions.tsv", result.stderr)
        # Reduced until the scratch class is gone, Fern reports crozier's class: masked.
        dispose(
            crozier_class="object-extends-non-object", disposition="masked", representative=digest, reduction="/x-note"
        )
        objects = others["object-extends-non-object"][4]
        self.env.update(FERN_STUB_CHECK_OUTPUT=f"issue: {phrase(objects)}", FERN_STUB_CHECK_EXIT="1")
        self.calls.unlink()
        reduced = self.script("reduce", "--root", str(self.root / "documents"))
        self.assertEqual(reduced.returncode, 0, reduced.stdout + reduced.stderr)
        [row] = [
            dict(zip(DISPOSITIONS_HEADER, cells, strict=True)) for cells in rows(registry / "dispositions.tsv")[1:]
        ]
        without = {key: value for key, value in document.items() if key != "x-note"}
        reduced_digest = hashlib.sha256((json.dumps(without) + "\n").encode()).hexdigest()
        self.assertEqual(
            (row["disposition"], row["reduced_digest"], row["check_exit"], row["generate_exit"], row["classes"]),
            ("masked", reduced_digest, "1", "—", "object-extends-non-object"),
        )
        # Fern ran once, over the reduced bytes, and the log names its inputs, then the pair.
        [call] = [json.loads(line) for line in self.calls.read_text(encoding="utf-8").splitlines()]
        self.assertEqual((call["argv"], json.loads(call["spec"])), (["check"], without))
        provenance, pair = (self.root / row["log"]).read_text(encoding="utf-8").splitlines(keepends=True)[:2]
        self.assertEqual((provenance, pair), (f"fern-refusals: reduction of {digest}: /x-note\n", PAIR_LINE))
        # Reduced again without --again, the recorded run is reused and Fern does not run.
        self.calls.unlink()
        reused = self.script("reduce", "--root", str(self.root / "documents"))
        self.assertEqual(reused.returncode, 0, reused.stdout + reused.stderr)
        self.assertIn("0 reduction(s) measured", reused.stdout)
        self.assertFalse(self.calls.exists(), "Fern ran over a reduction already on record")
        self.assertEqual(built().returncode, 0, built().stderr)
        # A second row whose other reduction yields the same bytes cannot share that
        # one log: `check` names the pair, and `reduce` refuses before any Fern run.
        kept = [row[key] for key in DISPOSITIONS_HEADER]
        alias = dict(row, crozier_class="generator-lint-failure", reduction="/*-openapi,info,paths")
        write_rows(
            registry / "dispositions.tsv",
            [list(DISPOSITIONS_HEADER), [alias[key] for key in DISPOSITIONS_HEADER], kept],
        )
        shared = (
            f"reduced document {reduced_digest} comes from representative {digest} reduced by "
            f"'/*-openapi,info,paths' and from {digest} reduced by '/x-note'"
        )
        self.assertIn(shared, self.script("check").stderr)
        refused = self.script("reduce", "--again", "--root", str(self.root / "documents"))
        self.assertEqual(refused.returncode, 1, refused.stdout + refused.stderr)
        self.assertIn(shared, refused.stderr)
        self.assertFalse(self.calls.exists(), "Fern ran over a reduction whose provenance is shared")
        write_rows(registry / "dispositions.tsv", [list(DISPOSITIONS_HEADER), kept])
        # A row its log does not derive is named by `check`.
        edited = dict(row, disposition="reported-other")
        write_rows(
            registry / "dispositions.tsv", [list(DISPOSITIONS_HEADER), [edited[key] for key in DISPOSITIONS_HEADER]]
        )
        self.assertIn(f"dispositions.tsv {digest}: the row disagrees with its log", self.script("check").stderr)
        # A reduction's log no row names is named too.
        stray = self.evidence / "reductions" / f"{'0' * 64}.log"
        stray.write_text(PAIR_LINE, encoding="utf-8")
        self.assertIn(
            f"{stray.relative_to(self.root).as_posix()}: no dispositions.tsv row", self.script("check").stderr
        )
        stray.unlink()
        # Fern generating from the reduction shows crozier's detector over-broad: refused.
        self.env.update(FERN_STUB_CHECK_OUTPUT="", FERN_STUB_CHECK_EXIT="0", FERN_STUB_GENERATE_FILES="3")
        reduced = self.script("reduce", "--again", "--root", str(self.root / "documents"))
        self.assertEqual(reduced.returncode, 0, reduced.stdout + reduced.stderr)
        self.assertEqual(rows(registry / "dispositions.tsv")[1][2], "over-broad")
        self.assertIn(f"{digest}: crozier --fern-strict stops at", built().stderr)
        # Fern naming another class there instead is recorded as reported, and vouches.
        self.env.update(
            FERN_STUB_CHECK_OUTPUT=f"issue: {phrase(self.class_row[4])}",
            FERN_STUB_CHECK_EXIT="1",
            FERN_STUB_GENERATE_FILES="0",
        )
        reduced = self.script("reduce", "--again", "--root", str(self.root / "documents"))
        self.assertEqual(reduced.returncode, 0, reduced.stdout + reduced.stderr)
        table = rows(registry / "dispositions.tsv")
        self.assertEqual((table[1][2], table[1][8]), ("reported-other", self.CLASS))
        self.assertEqual(built().returncode, 0, built().stderr)
        # A row whose inputs are not the ones its log was taken from is named.
        table[1][4] = "/info"
        write_rows(registry / "dispositions.tsv", table)
        self.assertIn(f"dispositions.tsv {digest}: its log", self.script("check").stderr)
        self.assertIn("was taken from representative", self.script("check").stderr)
        table[1][4] = "/x-note"
        write_rows(registry / "dispositions.tsv", table)
        # A reduction Fern does not finish within the bound is unmeasured, and vouches for nothing.
        self.env["FERN_STUB_HANG"] = str(self.root / "fern-pids")
        reduced = self.script("reduce", "--again", "--timeout", "2", "--root", str(self.root / "documents"))
        self.assertEqual(reduced.returncode, 0, reduced.stdout + reduced.stderr)
        table = rows(registry / "dispositions.tsv")
        self.assertEqual((table[1][2], table[1][6], table[1][8]), ("unmeasured", "timeout", "—"))
        self.assertIn(f"{digest}: crozier --fern-strict stops at", built().stderr)
        # So is one whose check names nothing and whose generation does not finish.
        self.env.update(FERN_STUB_CHECK_OUTPUT="", FERN_STUB_CHECK_EXIT="0", FERN_STUB_HANG_STAGE="generate")
        reduced = self.script("reduce", "--again", "--timeout", "2", "--root", str(self.root / "documents"))
        self.assertEqual(reduced.returncode, 0, reduced.stdout + reduced.stderr)
        table = rows(registry / "dispositions.tsv")
        self.assertEqual((table[1][2], table[1][6], table[1][7], table[1][8]), ("unmeasured", "0", "timeout", "—"))
        self.assertIn(f"{digest}: crozier --fern-strict stops at", built().stderr)
        del self.env["FERN_STUB_HANG"], self.env["FERN_STUB_HANG_STAGE"]
        # A class only `fern generate` reports, on a document Fern's check stopped, agrees by rule.
        refused_with("generator-lint-failure")
        dispose(crozier_class="generator-lint-failure", disposition="generate-stage")
        self.assertEqual(built().returncode, 0, built().stderr)
        # That rule is for a generate-stage class alone.
        dispose(crozier_class="object-extends-non-object", disposition="generate-stage")
        self.assertIn(f"dispositions.tsv {digest}: with no representative", self.script("check").stderr)
        # `build` holds a disposition before letting it vouch for a refusal.
        refused_with("object-extends-non-object")
        result = built()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(f"dispositions.tsv {digest}: with no representative", result.stderr)
        dispose(crozier_class="object-extends-non-object", disposition="agreed")
        self.assertIn(f"dispositions.tsv {digest}: disposition 'agreed' is not one of", built().stderr)
        dispose(crozier_class="object-extends-non-object", disposition="masked", reduced_digest="../../escape")
        self.assertIn(f"dispositions.tsv {digest}: reduced_digest '../../escape' is not a SHA-256", built().stderr)
        # Two rows sharing one reduction take one Fern run between them, and one log.
        other = self.documents["measured-current"]
        shared = [digest, "object-extends-non-object", "masked", digest, "/x-note", "—", "—", "—", "—", "—"]
        table = [list(DISPOSITIONS_HEADER), *sorted([shared, [other, *shared[1:]]])]
        write_rows(registry / "dispositions.tsv", table)
        self.env.update(FERN_STUB_CHECK_OUTPUT=f"issue: {phrase(objects)}", FERN_STUB_CHECK_EXIT="1")
        self.calls.unlink(missing_ok=True)
        reduced = self.script("reduce", "--again", "--root", str(self.root / "documents"))
        self.assertEqual(reduced.returncode, 0, reduced.stdout + reduced.stderr)
        self.assertEqual(len(self.calls.read_text(encoding="utf-8").splitlines()), 1)
        self.assertIn("1 reduction(s) measured, 2 disposition(s)", reduced.stdout)
        self.assertEqual(len({row[9] for row in rows(registry / "dispositions.tsv")[1:]}), 1)

    def test_reduce_keeps_a_yaml_representative_yaml_and_refuses_a_pointer_that_names_nothing(self) -> None:
        self.add_classes("object-extends-non-object")
        source = (
            "openapi: 3.0.3\n"
            "info: {title: t, version: '1'}\n"
            "paths:\n"
            "  /kept: {get: {responses: {'204': {description: ok}}}}\n"
            "  /dropped: {get: {responses: {'204': {description: ok}}}}\n"
            "tags: [{name: first}, {name: second}]\n"
            "components:\n"
            "  schemas:\n"
            "    Flag:\n"
            "      type: object\n"
            "      properties:\n"
            "        on: {type: boolean, default: yes}\n"
            "        when: {type: string, format: date, example: 2006-01-02T15:04:05Z}\n"
            "        op: {type: string, enum: [=, '~']}\n"
        )
        digest = self.add_document("yaml-current.yml", source.encode())
        self.measure()
        documents = str(self.root / "documents")

        def reduced_by(reduction: str) -> subprocess.CompletedProcess[str]:
            self.dispose(
                digest,
                crozier_class="object-extends-non-object",
                disposition="masked",
                representative=digest,
                reduction=reduction,
            )
            self.calls.unlink(missing_ok=True)
            return self.script("reduce", "--root", documents)

        # A keep-set, a list item, an enum member and a mapping member, in turn.
        result = reduced_by("/paths/*-~1kept;/tags/0;/components/schemas/Flag/properties/op/enum/1")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        [call] = [json.loads(line) for line in self.calls.read_text(encoding="utf-8").splitlines()]
        spec = call["spec"]
        # Still YAML: `on` and `yes` stay the strings Fern's YAML 1.2 reads, the
        # timestamp stays plain, and `=` stays a string.
        self.assertFalse(spec.lstrip().startswith("{"), spec)
        self.assertIn("'on':", spec)
        self.assertIn("default: 'yes'", spec)
        self.assertIn("example: 2006-01-02 15:04:05+00:00\n", spec)
        self.assertIn("- '='\n", spec)
        for gone in ("/dropped", "first", "'~'"):
            self.assertNotIn(gone, spec)
        self.assertIn("/kept", spec)
        # A pointer naming nothing fails, naming itself, before any Fern run.
        for pointer in (
            "/tags/2",
            "/tags/-1",
            "/tags/01",
            "/paths/~1absent/get",
            "/paths/*-~1absent",
            "tags",
            "/paths/~2kept",
            "/paths/~",
        ):
            with self.subTest(pointer=pointer):
                result = reduced_by(pointer)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(pointer, result.stderr)
                self.assertFalse(self.calls.exists(), "Fern ran over a reduction that names nothing")
        # Without PyYAML a YAML representative cannot be reduced: say how to get it.
        withheld = self.root / "no-yaml" / "yaml"
        withheld.mkdir(parents=True)
        (withheld / "__init__.py").write_text("raise ImportError('PyYAML withheld')\n", encoding="utf-8")
        self.env["PYTHONPATH"] = str(withheld.parent)
        result = reduced_by("/tags/0")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("reducing a YAML document needs PyYAML", result.stderr)

    def test_a_document_fern_generates_from_is_one_crozier_generates(self) -> None:
        # Fern's check and generation both pass over every document, and the
        # screen taken at the pair names no class either.
        self.env.update(FERN_STUB_CHECK_EXIT="0", FERN_STUB_CHECK_OUTPUT="", FERN_STUB_GENERATE_FILES="3")
        (self.root / "docs" / "openapi-surface" / "scratch" / "screened-current-check.log").write_text("", "utf-8")
        self.measure("--again")
        built = self.script("build")
        self.assertNotEqual(built.returncode, 0)
        self.assertIn("Fern generates it, but crozier --fern-strict stops at `crozier: invalid", built.stderr)
        # A crozier that generates them too holds.
        (self.root / "target" / "release" / "crozier").write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        self.measure("--crozier-again")
        built = self.script("build")
        self.assertEqual(built.returncode, 0, built.stderr)
        self.assertEqual(built.stdout, "fern-refusals: 0 refused, 4 generated, 0 unretrievable\n")
        # A generated document's strict log gone is no measurement to hold it to.
        log = self.root / "docs" / "openapi-surface" / "fern-refusals" / "crozier-logs"
        gone = log / f"{self.documents['measured-old']}.strict.log"
        gone.unlink()
        built = self.script("build")
        self.assertNotEqual(built.returncode, 0)
        self.assertIn(f"{self.documents['measured-old']}: its crozier log", built.stderr)
        self.assertIn("is missing", built.stderr)

    def test_a_screen_naming_another_generator_is_not_reused(self) -> None:
        screens = self.root / "docs" / "openapi-surface" / "scratch" / "screens.jsonl"
        records = [json.loads(line) for line in screens.read_text(encoding="utf-8").splitlines()]
        other = "fern-python-sdk:5.20.0"  # certified-pair: stand-in (a generator other than the certified one)
        records[1]["fern"] = f"failed: `fern check` exit 1 at CLI {CERTIFIED['cliVersion']}, {other}"
        screens.write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")
        self.measure()
        self.assertEqual(sorted(self.checked()), ["measured-old", "screened-current", "screened-old"])


# A run that never ends on its own, on any platform: it starts a child that
# inherits its pipes and beats a heartbeat file, then waits.
HANGING_TREE = """\
import subprocess, sys, time
beat = sys.argv[1]
child = subprocess.Popen([sys.executable, "-c", (
    "import sys, time\\n"
    "while True:\\n"
    "    open(sys.argv[1], 'a').write('.'); time.sleep(0.1)\\n"
), beat])
time.sleep(600)
"""


class FernRunTree(unittest.TestCase):
    """`fern_run` ends a run past its bound with every process it started, on every platform."""

    def test_a_run_past_its_bound_returns_with_its_descendants_ended(self) -> None:
        module = load_script("fern_refusals_run_tree")
        with tempfile.TemporaryDirectory() as scratch:
            beat = Path(scratch) / "beat"
            results: list[tuple[str, str]] = []
            run = threading.Thread(
                target=lambda: results.append(
                    module.fern_run([sys.executable, "-c", HANGING_TREE, str(beat)], Path(scratch), 3)
                ),
                daemon=True,
            )
            run.start()
            run.join(60)
            # The descendant held the run's pipes; returning at all shows it was ended.
            self.assertFalse(run.is_alive(), "fern_run never returned: a descendant kept its pipes open")
            self.assertEqual(results, [("timeout", "")])
            self.assertTrue(beat.exists(), "the descendant never started, so nothing was proven")
            # No heartbeat after the run returned: the descendant is gone.
            time.sleep(0.5)
            last = beat.stat().st_size
            time.sleep(1)
            self.assertEqual(beat.stat().st_size, last)


class DiagnosticExtraction(unittest.TestCase):
    """What `diagnostics` reads off a Fern log, over the generator's own lines."""

    module: ModuleType

    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_script("fern_refusals_diagnostics")

    def test_the_generators_response_object_refusal_is_its_diagnostic(self) -> None:
        log = "\n".join(
            [
                "[api]: python-sdk fernapi/fern-python-sdk Started.",
                "[api]: python-sdk ✓ All checks passed",
                "[api]: python-sdk fernapi/fern-python-sdk Response must be an object in order to "
                "return property next as a response.",
                "[api]: python-sdk fernapi/fern-python-sdk Failed.",
            ]
        )
        self.assertEqual(
            ["Response must be an object in order to return property next as a response."],
            self.module.diagnostics(log),
        )

    def test_the_generators_type_error_over_a_value_is_its_diagnostic(self) -> None:
        log = "\n".join(
            [
                "[api]: python-sdk ✓ All checks passed",
                "[api]: python-sdk fernapi/fern-python-sdk Cannot use 'in' operator to search for 'wireValue' in 1",
                "[api]: python-sdk fernapi/fern-python-sdk Failed.",
            ]
        )
        self.assertEqual(["Cannot use 'in' operator to search for 'wireValue' in 1"], self.module.diagnostics(log))

    def test_the_generators_progress_lines_are_no_diagnostic(self) -> None:
        log = "\n".join(
            [
                "[api]: python-sdk fernapi/fern-python-sdk Started.",
                "[api]: python-sdk fernapi/fern-python-sdk Wrote files to <tmp>/preview/fern-python-sdk",
                "[api]: python-sdk fernapi/fern-python-sdk Finished.",
            ]
        )
        self.assertEqual([], self.module.diagnostics(log))


class ProbeRecording(unittest.TestCase):
    """`probe` reads a class's diagnostic off Fern's own output and records it.

    `fern` is the script's subprocess boundary; a stand-in on `PATH` replays the
    committed logs of the measured run with that run's exits, so the real
    `probe` subcommand classifies them and writes the class's `fern-refusal.txt`
    into a scratch registry, which must be the committed record. Replaying the
    committed logs leaves the probe logs `probe` rewrites byte-identical.
    """

    NAME = "paginated-nullable-response"

    @unittest.skipIf(os.name == "nt", "the stand-in `fern` is a POSIX shell script")
    def test_probe_records_the_generators_response_object_refusal(self) -> None:
        logs = REPO / "docs" / "openapi-surface" / "fern-refusals" / "probe-logs"
        with tempfile.TemporaryDirectory() as scratch:
            registry = Path(scratch) / "fern-refusals"
            shutil.copytree(REGISTRY, registry)
            (registry / self.NAME / "fern-refusal.txt").unlink()
            bin_dir = Path(scratch) / "bin"
            bin_dir.mkdir()
            fern = bin_dir / "fern"
            check_log = logs / f"{self.NAME}.check.log"
            generate_log = logs / f"{self.NAME}.generate.log"
            fern.write_text(
                f'#!/bin/sh\nif [ "$1" = check ]; then cat "{check_log}"; exit 0; fi\ncat "{generate_log}"; exit 1\n',
                encoding="utf-8",
            )
            fern.chmod(0o755)
            env = dict(
                os.environ,
                CROZIER_FERN_REFUSALS_REGISTRY=str(registry),
                PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
            )
            before = {path.name: path.read_bytes() for path in logs.glob(f"{self.NAME}.*.log")}
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "probe", self.NAME], capture_output=True, text=True, env=env, cwd=REPO
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(
                (REGISTRY / self.NAME / "fern-refusal.txt").read_text(encoding="utf-8"),
                (registry / self.NAME / "fern-refusal.txt").read_text(encoding="utf-8"),
            )
            self.assertEqual(before, {path.name: path.read_bytes() for path in logs.glob(f"{self.NAME}.*.log")})


# Seconds the compiler-timeout case allows the whole evaluation: enough for the
# real venv setup on a loaded host, so the timeout lands on the compiler.
COMPILER_TIMEOUT_BUDGET = 30
# Seconds past its budget an evaluation may take to stop an overrunning stage,
# report, and exit before the test fails it as never having stopped.
DRIVER_STOP_GRACE = 60


@unittest.skipIf(os.name == "nt", "the package-tool and compiler doubles are POSIX shell scripts")
class SdkEvaluationDriverTests(unittest.TestCase):
    """The native driver sequences real child processes and installed-file inspection offline."""

    def setUp(self) -> None:
        from sdk_evaluation_doubles import install

        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.compiler, self.env = install(self.root / "bin")
        self.source = self.root / "source.yml"
        self.source.write_text(
            "openapi: 3.1.0\ninfo: {title: Offline Chain, version: '1'}\npaths: {}\n", encoding="utf-8"
        )
        self.calls = self.root / "calls.txt"
        self.env["SDK_EVAL_CALLS"] = str(self.calls)
        # The runtime inspector runs in a genuinely separate venv. Copying the
        # already-installed tracer there lets the tooling coverage tier see it.
        try:
            import coverage
        except ImportError:
            pass
        else:
            if coverage.Coverage.current() is not None:
                self.env["SDK_EVAL_COVERAGE"] = "1"
                self.env["COVERAGE_PROCESS_START"] = str(REPO / "pyproject.toml")
                self.env["COVERAGE_FILE"] = str(Path(os.environ.get("COVERAGE_FILE", ".coverage")).resolve())

    def evaluate(
        self, mode: str = "", name: str = "run", destination: Path | None = None, timeout: int = 120
    ) -> tuple[subprocess.CompletedProcess[str], Path]:
        env = {**self.env, "SDK_EVAL_MODE": mode}
        receipt = destination or self.root / f"{name}.json"
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "evaluate-sdk",
                "--document",
                str(self.source),
                "--crozier",
                str(self.compiler),
                "--work-dir",
                str(self.root / name),
                "--output",
                str(receipt),
                "--timeout",
                str(timeout),
            ],
            capture_output=True,
            text=True,
            env=env,
            check=False,
            # The driver's budget covers every stage; a driver that leaves an
            # overrunning stage running fails here instead of hanging the suite.
            timeout=timeout + DRIVER_STOP_GRACE,
        )
        return result, receipt

    def test_driver_records_each_actual_artifact_and_import_environment_in_order(self) -> None:
        result, receipt = self.evaluate()
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(receipt.read_text())
        self.assertEqual(
            self.calls.read_text().splitlines(),
            [
                "uv:venv",
                "uv:venv",
                "uv:pip",
                "validation",
                "default_generation",
                "strict_generation",
                "build",
                "uv:pip",
                "imports",
            ],
        )
        digest = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.assertEqual(data["validation"]["input_sha256"], digest)
        self.assertEqual(data["validation"]["output_sha256"], digest)
        wheel = next((self.root / "run/dist").glob("*.whl"))
        self.assertEqual(data["build"]["output_sha256"], hashlib.sha256(wheel.read_bytes()).hexdigest())
        self.assertEqual(data["installation"]["input_sha256"], data["build"]["output_sha256"])
        self.assertEqual(data["imports"]["input_sha256"], data["installation"]["output_sha256"])
        self.assertEqual(data["imports"]["environment"], data["installation"]["environment"])
        self.assertEqual(data["imports"]["modules"], ["limitation_sdk", "limitation_sdk.reading"])
        answer = subprocess.run(
            [sys.executable, str(SCRIPT), "check-sdk-evaluation", str(receipt), "--document", str(self.source)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(answer.returncode, 0, answer.stderr)

    def test_driver_refuses_failed_stages_without_replacing_a_receipt(self) -> None:
        for stage in ("validation", "default_generation", "strict_generation", "build", "installation", "imports"):
            with self.subTest(stage=stage):
                name = "failed-" + stage
                receipt = self.root / f"{name}.json"
                receipt.write_text("prior receipt\n")
                result, receipt = self.evaluate(stage + "-fails", name)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("failed with exit", result.stderr)
                self.assertEqual(receipt.read_text(), "prior receipt\n")

    def test_driver_refuses_missing_outputs_and_mismatching_artifact_digests(self) -> None:
        for mode, reason in (
            ("missing-sdk", "nonempty"),
            ("missing-wheel", "exactly one wheel"),
            ("mutated-tree", "building mutated"),
            ("different-trees", "default/strict generated tree digest"),
        ):
            with self.subTest(mode=mode):
                result, receipt = self.evaluate(mode, mode)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(reason, result.stderr)
                self.assertFalse(receipt.exists())

    def test_driver_protects_inputs_and_rejects_symlinks_and_invalid_runtime_provenance(self) -> None:
        for index, target in enumerate((self.source, self.compiler)):
            with self.subTest(overwrite=target.name):
                before = target.read_bytes()
                result, _receipt = self.evaluate(name=f"overwrite-{index}", destination=target)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("overwrite an input", result.stderr)
                self.assertEqual(before, target.read_bytes())
                self.assertFalse((self.root / f"overwrite-{index}").exists())
        for mode, reason in (
            ("symlink-sdk", "contains a symlink"),
            ("outside-env", "did not come from the fresh installation"),
            ("discovery-fails", "could not discover SDK package"),
            ("mutating-import", "imports changed the installed distribution"),
        ):
            with self.subTest(mode=mode):
                result, receipt = self.evaluate(mode, mode)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(reason, result.stderr)
                self.assertFalse(receipt.exists())

    def assert_receipt_recovery(self, receipt: Path, name: str) -> None:
        result, _ = self.evaluate(name=name, destination=receipt)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(2, json.loads(receipt.read_text())["schema_version"])

    def test_process_start_and_timeout_preserve_receipts_and_recover(self) -> None:
        for mode in ("compiler-unexecutable", "compiler-timeout"):
            with self.subTest(mode=mode):
                receipt = self.root / f"{mode}.json"
                receipt.write_text("previous receipt\n")
                if mode == "compiler-unexecutable":
                    self.compiler.chmod(0o644)
                try:
                    # The budget covers every stage, so it must outlast the venv setup
                    # before the compiler; the compiler double then blocks until killed.
                    result, _ = self.evaluate(mode, mode, receipt, timeout=COMPILER_TIMEOUT_BUDGET)
                finally:
                    self.compiler.chmod(0o755)
                self.assertEqual(1, result.returncode)
                self.assertIn("default_generation could not run", result.stderr)
                self.assertIn("timed out" if mode == "compiler-timeout" else "Permission denied", result.stderr)
                if mode == "compiler-timeout":
                    self.assertEqual("default_generation", self.calls.read_text().splitlines()[-1])
                self.assertEqual("previous receipt\n", receipt.read_text())
                self.assert_receipt_recovery(receipt, mode + "-recovered")

    def test_malformed_inspector_output_preserves_receipts_and_recovers(self) -> None:
        for mode, diagnostic in (
            ("inspector-json", "runtime inspection did not produce JSON"),
            ("inspector-structure", "distribution_sha256"),
        ):
            with self.subTest(mode=mode):
                receipt = self.root / f"{mode}.json"
                receipt.write_text("previous receipt\n")
                result, _ = self.evaluate(mode, mode, receipt)
                self.assertEqual(1, result.returncode)
                self.assertIn(diagnostic, result.stderr)
                self.assertEqual("previous receipt\n", receipt.read_text())
                self.assert_receipt_recovery(receipt, mode + "-recovered")

    def test_missing_prerequisites_preserve_receipts_and_recover(self) -> None:
        for mode, diagnostic in (
            ("compiler", "crozier executable missing"),
            ("work-directory", "evaluation work directory already exists"),
            ("uv", "uv is missing from PATH"),
        ):
            with self.subTest(mode=mode):
                receipt = self.root / f"missing-{mode}.json"
                receipt.write_text("previous receipt\n")
                original_compiler = self.compiler
                original_path = self.env["PATH"]
                name = "missing-" + mode
                match mode:
                    case "compiler":
                        self.compiler = self.root / "absent-compiler"
                    case "work-directory":
                        (self.root / name).mkdir()
                    case "uv":
                        self.env["PATH"] = str(self.root / "absent-tools")
                try:
                    result, _ = self.evaluate(name=name, destination=receipt)
                finally:
                    self.compiler = original_compiler
                    self.env["PATH"] = original_path
                self.assertEqual(1, result.returncode)
                self.assertIn(diagnostic, result.stderr)
                self.assertEqual("previous receipt\n", receipt.read_text())
                self.assertFalse(self.calls.exists(), "prerequisites must fail before starting a tool")
                self.assert_receipt_recovery(receipt, name + "-recovered")
                self.calls.unlink()

    def test_receipt_replacement_failure_cleans_temporary_file_and_recovers(self) -> None:
        receipt = self.root / "receipt.json"
        receipt.mkdir()
        previous = receipt / "previous.json"
        previous.write_text("previous receipt\n")
        result, _ = self.evaluate(destination=receipt)
        self.assertEqual(1, result.returncode)
        self.assertIn("SDK evaluation:", result.stderr)
        self.assertIn("receipt.json", result.stderr)
        self.assertEqual("previous receipt\n", previous.read_text())
        self.assertEqual([], list(self.root.glob(".sdk-evaluation-*")))
        self.assertTrue((self.root / "run/imports.log").is_file(), "failure must happen after SDK evaluation")
        previous.unlink()
        receipt.rmdir()
        self.assert_receipt_recovery(receipt, "replacement-recovered")
        self.assertEqual([], list(self.root.glob(".sdk-evaluation-*")))

    def test_receipt_integrity_rejects_each_invalid_environment_and_import_description(self) -> None:
        result, receipt = self.evaluate()
        self.assertEqual(result.returncode, 0, result.stderr)
        original = receipt.read_text()

        def refresh_environment(data: dict) -> None:
            for label in ("installation", "imports"):
                environment = data[label]["environment"]
                data[label]["environment_sha256"] = hashlib.sha256(
                    json.dumps(environment, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
                ).hexdigest()

        for case, reason in (
            ("environment-digest", "environment digest does not match"),
            ("duplicates", "not unique and sorted"),
            ("unsorted", "not unique and sorted"),
            ("missing-sdk", "does not identify the installed SDK"),
            ("wrong-sdk", "does not identify the installed SDK"),
            ("missing-interpreter", "omits its interpreter"),
            ("module-digest", "imported module list digest"),
            ("wrong-modules", "every discovered module"),
            ("unsorted-modules", "every discovered module"),
            ("empty-command", "no recorded command"),
        ):
            with self.subTest(case=case):
                data = json.loads(original)
                match case:
                    case "environment-digest":
                        data["imports"]["environment"]["prefix"] = "changed prefix"
                    case "duplicates" | "unsorted" | "missing-sdk" | "wrong-sdk" | "missing-interpreter":
                        environment = data["installation"]["environment"]
                        entries = environment["distributions"]
                        sdk = next(item for item in entries if item["name"] == "limitation-sdk")
                        match case:
                            case "duplicates":
                                entries.append(dict(sdk))
                            case "unsorted":
                                environment["distributions"] = [
                                    sdk,
                                    {"name": "aaa", "version": "1", "sha256": "a" * 64},
                                ]
                            case "missing-sdk":
                                environment["distributions"] = [
                                    item for item in entries if item["name"] != "limitation-sdk"
                                ]
                            case "wrong-sdk":
                                sdk["sha256"] = "f" * 64
                            case "missing-interpreter":
                                environment["executable"] = ""
                        data["imports"]["environment"] = json.loads(json.dumps(environment))
                        refresh_environment(data)
                    case "module-digest":
                        data["imports"]["output_sha256"] = "f" * 64
                    case "wrong-modules" | "unsorted-modules":
                        data["imports"]["modules"] = (
                            ["unrelated_package"]
                            if case == "wrong-modules"
                            else list(reversed(data["imports"]["modules"]))
                        )
                        data["imports"]["output_sha256"] = hashlib.sha256(
                            json.dumps(data["imports"]["modules"], separators=(",", ":")).encode()
                        ).hexdigest()
                    case "empty-command":
                        data["imports"]["command"] = []
                receipt.write_text(json.dumps(data), encoding="utf-8")
                checked = subprocess.run(
                    [sys.executable, str(SCRIPT), "check-sdk-evaluation", str(receipt), "--document", str(self.source)],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertNotEqual(checked.returncode, 0)
                self.assertIn(reason, checked.stderr)
        receipt.write_text(original, encoding="utf-8")


class SdkArtifactDigestTests(unittest.TestCase):
    def test_binary_contents_cannot_be_confused_with_another_file_boundary(self) -> None:
        evaluator = load_script("sdk_digest_boundary").sdk_evaluator()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first, second = root / "one-file", root / "two-files"
            first.mkdir()
            second.mkdir()
            (first / "a").write_bytes(b"x\0b\0y")
            (second / "a").write_bytes(b"x")
            (second / "b").write_bytes(b"y")
            self.assertNotEqual(evaluator.tree_digest(first), evaluator.tree_digest(second))


if __name__ == "__main__":
    unittest.main()
