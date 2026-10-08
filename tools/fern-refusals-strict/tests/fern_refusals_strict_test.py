"""`fern-refusals.py measure` and `build` with the real, freshly built crozier.

`measure` records crozier's `--fern-strict` exit beside its default one, so
this suite builds crozier and drives the script with that binary from a
scratch checkout: over a document screened by a committed check, and over one
it fetches from a loopback server and runs through a stand-in `fern`. It is the fern-refusals project's one suite that needs the
crate, so it is a project of its own that declares crozier as a dependency;
the offline suites, and the helpers both use, are
`tools/fern-refusals/tests/fern_refusals_test.py`'s.
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
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "fern-refusals" / "tests"))

from fern_refusals_test import REGISTRY, REPO, rows, stub_fern, write_rows  # noqa: E402 - the shared helpers' directory must be on sys.path first


MEASURE_LOADS = (
    "tools/fern-refusals/fern-refusals.py",
    "tools/witness-search/witness-search-github.py",
    "tools/witness-search/witness-search-github-index.py",
    "tools/witness-search/witness_screen.py",
    "tools/witness-search/rate_limit_guard.py",
    "tools/witness-search/witness-search-redo.py",
    "tools/surface-census/openapi-surface-census.py",
    "tools/surface-census/witness-search-region-keys.py",
    "tools/corpus/corpus_remote_ref_pins.py",
)


@unittest.skipIf(os.name == "nt", "`measure` runs `target/release/crozier`, a path with no `.exe`")
class ScratchCheckout(unittest.TestCase):
    """A scratch checkout whose population is one class's committed probe,
    screened by its committed `fern check` log, with the compiled crozier binary
    where `measure` looks for it. The suites below run the REAL script in it."""

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
        # `measure` loads, by their repository paths, the witness-search GitHub
        # acquirer (with the index, screen stage, rate-limit guard and the redo
        # ledger reader it pulls in), the census reader and region keys it reads
        # documents through, and the pin reader the census imports; the scratch
        # checkout carries exactly those (the fern-refusals project's inputs).
        shutil.copytree(REPO / "scripts", root / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
        for relative in MEASURE_LOADS:
            (root / relative).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / relative, root / relative)
        binary = root / "target" / "release" / "crozier"
        binary.parent.mkdir(parents=True)
        shutil.copy(self.binary, binary)
        surface = root / "docs" / "openapi-surface"
        (root / "tests" / "fixtures").mkdir(parents=True)
        (root / "tests" / "fixtures" / "CORPUS.md").write_text("", encoding="utf-8")
        for relative in ("justfile",):
            (root / relative).parent.mkdir(parents=True, exist_ok=True)
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

    def script(self, *args: str, **extra: str) -> subprocess.CompletedProcess[str]:
        env = {key: value for key, value in os.environ.items() if not key.startswith("CROZIER")}
        env.update(extra)
        return subprocess.run([sys.executable, str(self.root / "tools" / "fern-refusals" / "fern-refusals.py"), *args],
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



class StrictMeasurement(ScratchCheckout):
    """`measure` records crozier's `--fern-strict` exit and `build` writes it
    into `documents.tsv` for a document carrying an evaluated class. The probe's
    check is committed, so no Fern runs."""

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


class _Host(ThreadingHTTPServer):
    """A loopback host serving `documents`, by request path."""

    def __init__(self) -> None:
        super().__init__(("127.0.0.1", 0), _Served)
        self.documents: dict[str, bytes] = {}


class _Served(BaseHTTPRequestHandler):
    """Serves the host's document at the request path, or 404 for any other path."""

    server: _Host

    def do_GET(self) -> None:  # noqa: N802 - the name http.server dispatches to
        body = self.server.documents.get(self.path)
        self.send_response(200 if body is not None else 404)
        self.end_headers()
        self.wfile.write(body or b"")

    def log_message(self, *_args: object) -> None:
        pass


class FetchedAndMeasured(ScratchCheckout):
    """A document no committed screen holds and no committed log covers:
    `measure` fetches it from its locator — a loopback server standing in for
    the host — then runs `fern check` and `fern generate` (a stand-in `fern` on
    PATH, `FERN_STUB`) and the real crozier over it, recording every outcome.
    A fetch that fails or serves other bytes records why it is unretrievable."""

    NAME = "served-api"

    def setUp(self) -> None:
        super().setUp()
        self.server = _Host()
        self.addCleanup(self.server.server_close)
        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(thread.join)
        self.addCleanup(self.server.shutdown)
        self.served = (REGISTRY / self.CLASS / "probe.yml").read_bytes() + b"\n# served over loopback\n"
        self.served_digest = hashlib.sha256(self.served).hexdigest()
        self.locator = f"http://127.0.0.1:{self.server.server_address[1]}/{self.NAME}/openapi.yml"
        (self.root / "tests" / "fixtures" / "CORPUS.md").write_text(
            f"| `{self.NAME}` | a document Fern refused | **DROPPED** — Fern golden generation failed |\n",
            encoding="utf-8")
        self.record(self.served_digest)
        self.calls = self.root / "fern-calls.jsonl"
        self.fern = dict(PATH=f"{stub_fern(self.root / 'bin')}{os.pathsep}{os.environ.get('PATH', '')}",
                         FERN_STUB_CALLS=str(self.calls), no_proxy="127.0.0.1", NO_PROXY="127.0.0.1",
                         FERN_STUB_GENERATE_FILES="4")

    def record(self, digest: str) -> None:
        """The CORPUS.md row's committed location: the loopback locator and `digest`."""
        write_rows(self.root / "docs" / "openapi-surface" / "fern-refusals" / "dropped-sources.tsv", [
            ["name", "corpus_line", "source", "locator", "revision", "sha256", "evidence", "reason"],
            [self.NAME, "1", "scratch", self.locator, "0" * 40, digest, "CORPUS.md:1", "Fern failed"]])

    def measured(self, *args: str) -> dict[str, str]:
        result = self.script("measure", "--jobs", "1", "--root", str(self.root / "documents"), *args, **self.fern)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return {row["key"]: row for row in map(json.loads, self.measurements.read_text(encoding="utf-8").splitlines())}

    def test_a_fetched_document_is_checked_generated_and_run_through_crozier(self) -> None:
        self.server.documents[f"/{self.NAME}/openapi.yml"] = self.served
        row = self.measured()[self.served_digest]
        self.assertEqual(row["unretrievable"], "")
        self.assertEqual((row["check_exit"], row["generate_exit"], row["generate_files"]), ("0", "0", "4"))
        # crozier refuses the probe's colliding `name`, as it does the committed one.
        self.assertEqual((row["crozier_exit"], row["crozier_files"], row["crozier_strict_exit"]), ("1", "0", "1"))
        for log in (row["check_log"], row["generate_log"]):
            self.assertTrue((self.root / log).is_file(), log)
        calls = [json.loads(line) for line in self.calls.read_text(encoding="utf-8").splitlines()]
        self.assertEqual([call["argv"][0] for call in calls], ["check", "generate"])
        self.assertTrue(all(call["spec"].encode() == self.served for call in calls))

    def test_a_failed_fetch_is_recorded_unretrievable_and_retaken_with_again(self) -> None:
        row = self.measured()[self.served_digest]
        self.assertEqual(row["unretrievable"], "fetch failed: HTTP Error 404: Not Found")
        self.assertFalse(self.calls.exists(), "Fern ran over a document that was never fetched")
        # Recovery: once the host serves it, `--again` takes it.
        self.server.documents[f"/{self.NAME}/openapi.yml"] = self.served
        row = self.measured("--again")[self.served_digest]
        self.assertEqual((row["unretrievable"], row["check_exit"]), ("", "0"))

    def test_a_host_serving_other_bytes_is_recorded_unretrievable(self) -> None:
        recorded = "f" * 64
        self.record(recorded)
        self.server.documents[f"/{self.NAME}/openapi.yml"] = self.served
        row = self.measured()[recorded]
        self.assertEqual(row["unretrievable"], f"{self.locator} now serves bytes hashing to {self.served_digest}, "
                                               f"not the recorded {recorded}")
        self.assertFalse(self.calls.exists(), "Fern ran over bytes other than the recorded document")


if __name__ == "__main__":
    unittest.main()
