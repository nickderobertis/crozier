#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier's Python maintenance tests live in tests/ and run through just (`test-witness-screen`); no Nx workspace or project boundary exists for them.
"""The measured screening stage, driven through its real CLI and the legacy index that reads it.

`scripts/witness_screen.py screen` runs as a subprocess over a temporary
evidence root, reading the candidate's bytes and licence from a loopback
server standing in for raw.githubusercontent.com (the acquirer's exact-commit
raw route, `CROZIER_RAW_GITHUB_URL`) and running a stub `fern` on PATH, since
the pinned CLI resolves its version over the network and generates in Docker.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import textwrap
import threading
import unittest
import unittest.mock
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "witness_screen.py"
COMMIT = "c" * 40
DOCUMENT = b"openapi: 3.0.3\ninfo: {title: shop, version: '1'}\npaths: {}\n"
PROPRIETARY = b"openapi: 3.0.3\ninfo: {title: shop, version: '1', license: {name: Shop EULA}}\npaths: {}\n"
SECRET = "ghp_offlinesecretvalue0123456789"
FERN = """\
    import os, pathlib, sys, time
    print("token in use: " + os.environ.get("GITHUB_TOKEN", ""))
    if os.environ["FERN_STUB"] == "hang":
        time.sleep(30)
    if os.environ["FERN_STUB"] == "refuse":
        print("Found 1 error in 0.42 seconds.")
        print("issue: the `x-fern-enum` extension is missing; add it")
        sys.exit(1)
    if sys.argv[1] == "generate":
        package = pathlib.Path(sys.argv[sys.argv.index("--output") + 1]) / "fern-python-sdk"
        package.mkdir(parents=True)
        (package / "client.py").write_text("class Client: ...\\n")
    """


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SCREEN = load("witness_screen_under_test", SCRIPT)
INDEX = load("witness_search_github_index_under_test", REPO / "scripts" / "witness-search-github-index.py")


class _Raw(BaseHTTPRequestHandler):
    """raw.githubusercontent.com's exact-commit route for two repositories."""

    def log_message(self, *args: object) -> None:
        pass

    def do_GET(self) -> None:
        files = {
            f"/acme/shop/{COMMIT}/openapi.yaml": DOCUMENT,
            f"/acme/shop/{COMMIT}/LICENSE": b"MIT License\n\nCopyright (c) acme\n",
            f"/acme/eula/{COMMIT}/openapi.yaml": PROPRIETARY,
            f"/acme/eula/{COMMIT}/LICENSE": b"MIT License\n",
        }
        body = files.get(self.path)
        self.send_response(200 if body is not None else 404)
        body = body if body is not None else b"404: Not Found"
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


@unittest.skipIf(os.name == "nt", "a bare `fern` resolves only as fern.exe on Windows, which a script cannot stand in for")
class LegacyScreenCliTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory(prefix="witness-screen-")
        self.addCleanup(scratch.cleanup)
        self.scratch = Path(scratch.name)
        self.root = self.scratch / "surface"
        self.evidence = self.root / "witness-search-sourcegraph"
        self.evidence.mkdir(parents=True)
        server = ThreadingHTTPServer(("127.0.0.1", 0), _Raw)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        fake_bin = self.scratch / "bin"
        fake_bin.mkdir()
        (fake_bin / "fern").write_text(f"#!{sys.executable}\n" + textwrap.dedent(FERN), encoding="utf-8")
        os.chmod(fake_bin / "fern", 0o755)
        self.env = {**os.environ, "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}", "FERN_STUB": "pass",
                    "GITHUB_TOKEN": SECRET, "CROZIER_RAW_GITHUB_URL": f"http://127.0.0.1:{server.server_port}"}

    def screen(self, *args: str, repository: str = "acme/shop", **env: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "screen", "--source", "sourcegraph", "--key", "sample-shape",
             "--repository", repository, "--commit", COMMIT, "--path", "openapi.yaml",
             "--evidence-root", str(self.root), "--timeout", "60", *args],
            env={**self.env, **env}, capture_output=True, text=True, cwd=REPO, timeout=300)

    def rows(self) -> list[dict[str, object]]:
        path = self.evidence / "screens.jsonl"
        if not path.is_file():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

    def test_a_candidate_passing_every_screen_is_filed_with_its_measured_record(self) -> None:
        # Passing every screen owes a disposition; nothing is filed without one.
        refused = self.screen()
        self.assertEqual(1, refused.returncode)
        self.assertIn("every screen passed; say what becomes of the candidate with --disposition", refused.stderr)
        self.assertEqual([], self.rows())

        done = self.screen("--disposition", "witness-found", "--sha256", hashlib.sha256(DOCUMENT).hexdigest())
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertIn("licence passed, ref passed, fern passed; witness-found", done.stdout)
        [row] = self.rows()
        record = row["measured"]
        self.assertEqual([], SCREEN.measured_failures(record, self.evidence))
        self.assertEqual(("passed", "passed"), (row["fern"], record["fern"]["outcome"]))
        self.assertEqual("passed: no info.license, LICENSE at the pinned commit reads as MIT, which the corpus "
                         "rule admits", row["license"])
        self.assertEqual(("200", "LICENSE:200", "check 0, generate 0"),
                         (record["ref"]["exit"], record["licence"]["exit"], record["fern"]["exit"]))
        self.assertEqual(hashlib.sha256(DOCUMENT).hexdigest(), row["sha256"])
        # Every log is committed under `screens/`, carries its recorded digest, and
        # holds no credential the run could see.
        for name in ("licence", "ref", "fern"):
            log = self.evidence / record[name]["log"]
            self.assertTrue(record[name]["log"].startswith("screens/"))
            self.assertEqual(record[name]["log_sha256"], hashlib.sha256(log.read_bytes()).hexdigest())
            self.assertNotIn(SECRET, log.read_text(encoding="utf-8"))
        self.assertIn("token in use: [GITHUB_TOKEN redacted]", (self.evidence / record["fern"]["log"]).read_text())
        # The reads went through the acquirer's raw lane, which logs each call.
        calls = [json.loads(line) for line in
                 (self.evidence / "raw-github-calls.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(["openapi.yaml", "LICENSE"] * 2, [call["url"].rsplit("/", 1)[1] for call in calls])
        # The refused first run left no log behind: only the filed record's three remain.
        self.assertEqual(sorted(record[name]["log"] for name in ("licence", "ref", "fern")),
                         sorted(path.relative_to(self.evidence).as_posix()
                                for path in (self.evidence / "screens").iterdir()))
        # The legacy index reads the row as measured, and labels it nothing else.
        self.assertEqual([], SCREEN.row_failures(row, self.evidence, INDEX.SCREEN_FIELDS))
        self.assertEqual(1, len(INDEX.jsonl(self.evidence / "screens.jsonl")))
        screened = INDEX.screens(self.evidence)
        result = INDEX.classify("sourcegraph", "sample-shape", {
            "repository": "acme/shop", "path": "openapi.yaml", "commit": COMMIT, "sha256": row["sha256"],
            "disposition": "declares", "selector_count": 1}, "candidates.jsonl:1", screened)
        self.assertEqual(("pass", "witness-found", "candidates.jsonl:1"),
                         (result["fern_screen"], result["disposition"], result["evidence"]))

    def test_a_ref_the_read_cannot_pin_fails_and_the_later_screens_do_not_run(self) -> None:
        for args, ref in (
            (["--commit", "main"], "failed: 'main' is no full commit SHA, so the ref is mutable"),
            (["--path", "gone.yaml"], f"failed: HTTP 404 reading gone.yaml at acme/shop@{COMMIT}"),
            (["--sha256", "0" * 64], f"failed: the bytes at acme/shop@{COMMIT} carry sha256 "
                                     f"{hashlib.sha256(DOCUMENT).hexdigest()}, not the pinned {'0' * 64}"),
        ):
            with self.subTest(args=args):
                (self.evidence / "screens.jsonl").unlink(missing_ok=True)
                command = [sys.executable, str(SCRIPT), "screen", "--source", "sourcegraph", "--key", "sample-shape",
                           "--repository", "acme/shop", "--commit", COMMIT, "--path", "openapi.yaml",
                           "--evidence-root", str(self.root)]
                for flag, value in zip(args[::2], args[1::2]):
                    if flag in command:
                        command[command.index(flag) + 1] = value
                    else:
                        command += [flag, value]
                done = subprocess.run(command, env=self.env, capture_output=True, text=True, cwd=REPO, timeout=300)
                self.assertEqual(0, done.returncode, done.stderr)
                [row] = self.rows()
                self.assertEqual(ref, row["ref"])
                self.assertEqual("rejected", row["disposition"])
                self.assertEqual("not-run: the ref screen failed", row["fern"])
                if args[0] == "--path":
                    self.assertEqual("not-run: the ref screen failed, so no bytes were read", row["license"])

    def test_a_fern_run_cut_off_by_its_timeout_files_nothing(self) -> None:
        refused = self.screen("--disposition", "witness-found", "--timeout", "1", FERN_STUB="hang")
        self.assertEqual(1, refused.returncode)
        self.assertIn("Fern timed out after 1s on acme/shop:openapi.yaml; nothing was filed", refused.stderr)
        self.assertEqual([], self.rows())
        self.assertEqual([], sorted((self.evidence / "screens").iterdir()), "a log outlived its unfiled screen")

    def test_fern_text_is_refused_as_a_measurement(self) -> None:
        refused = self.screen("--fern", "passed", "--disposition", "witness-found")
        self.assertEqual(1, refused.returncode)
        self.assertIn("`--fern` is no longer a measurement", refused.stderr)
        self.assertEqual([], self.rows())

    def test_a_measured_refusal_is_filed_rejected_and_a_success_claim_over_it_is_refused(self) -> None:
        claimed = self.screen("--disposition", "witness-found", FERN_STUB="refuse")
        self.assertEqual(1, claimed.returncode)
        self.assertIn("`witness-found` claims a candidate that passed every screen", claimed.stderr)
        self.assertEqual([], self.rows())
        done = self.screen(FERN_STUB="refuse")
        self.assertEqual(0, done.returncode, done.stderr)
        [row] = self.rows()
        self.assertEqual("rejected", row["disposition"])
        self.assertEqual(f"failed: {SCREEN.fern_label()} fern check exit 1: Found 1 error. First: the "
                         "'x-fern-enum' extension is missing, add it", row["fern"])

    def test_a_licence_the_reading_cannot_recognise_is_refused_and_fern_is_not_run(self) -> None:
        done = self.screen(repository="acme/eula")
        self.assertEqual(0, done.returncode, done.stderr)
        [row] = self.rows()
        self.assertEqual("failed: info.license 'Shop EULA' names no grant the corpus rule admits", row["license"])
        self.assertEqual("not-run: the licence screen failed", row["fern"])
        self.assertEqual("rejected", row["disposition"])

    def test_a_judgement_refuses_a_licence_the_reading_passes_and_is_recorded_beside_it(self) -> None:
        done = self.screen("--licence-refusal", "a third-party copy; the publisher grants nothing")
        self.assertEqual(0, done.returncode, done.stderr)
        [row] = self.rows()
        self.assertEqual("failed: a third-party copy, the publisher grants nothing", row["license"])
        pins = row["measured"]["licence"]["pins"]
        self.assertEqual(("MIT", "a third-party copy; the publisher grants nothing"),
                         (pins["licence_file_family"], pins["judgement"]))

    def test_a_record_missing_its_measurement_is_refused_naming_what_is_missing(self) -> None:
        self.assertEqual(0, self.screen("--disposition", "witness-found").returncode)
        record = self.rows()[0]["measured"]
        (self.evidence / "screens.jsonl").unlink()
        for mutate, missing in (
            (lambda r: r["fern"].pop("log_sha256"), "the fern screen's redacted log and its sha256"),
            (lambda r: r["licence"].pop("exit"), "the licence screen's exit status"),
            (lambda r: r["fern"]["run"].update(generate_exit="1"),
             "a fern outcome its run measured: it reads 'passed'"),
            (lambda r: r.pop("stage"), "the stage that measured it"),
        ):
            broken = json.loads(json.dumps(record))
            mutate(broken)
            path = self.scratch / "broken.json"
            path.write_text(json.dumps(broken), encoding="utf-8")
            with self.subTest(missing=missing):
                refused = self.screen("--measured", str(path), "--disposition", "witness-found")
                self.assertEqual(1, refused.returncode)
                self.assertIn("a screen is filed only with its measured record; it lacks", refused.stderr)
                self.assertIn(missing, refused.stderr)
        self.assertEqual([], self.rows())


    def test_an_unreadable_measured_file_or_timeout_is_refused_with_its_remedy(self) -> None:
        missing = self.screen("--measured", str(self.scratch / "absent.json"))
        self.assertEqual(1, missing.returncode)
        self.assertIn("pass the JSON file a measurement wrote, or drop --measured", missing.stderr)
        garbled = self.scratch / "garbled.json"
        garbled.write_text("{not json", encoding="utf-8")
        refused = self.screen("--measured", str(garbled))
        self.assertEqual(1, refused.returncode)
        self.assertIn("is not JSON", refused.stderr)
        zero = subprocess.run([sys.executable, str(SCRIPT), "screen", "--source", "sourcegraph", "--key", "k",
                               "--repository", "acme/shop", "--commit", COMMIT, "--path", "openapi.yaml",
                               "--timeout", "0"], capture_output=True, text=True, cwd=REPO)
        self.assertEqual(2, zero.returncode)
        self.assertIn("0 is not a positive number of seconds", zero.stderr)
        self.assertEqual([], self.rows())


class WindowsNewlineTests(unittest.TestCase):
    """A committed log carries the digest recorded for it under Windows' text-mode newlines."""

    def test_a_log_written_under_crlf_translation_still_carries_its_recorded_digest(self) -> None:
        opened = Path.open

        def windows_open(path: Path, mode: str = "r", buffering: int = -1, encoding: str | None = None,
                         errors: str | None = None, newline: str | None = None):
            # Windows' text mode: an unset `newline` writes each `\n` as `\r\n`.
            if "b" not in mode and newline is None:
                newline = "\r\n"
            return opened(path, mode, buffering, encoding, errors, newline)

        with tempfile.TemporaryDirectory(prefix="witness-screen-") as directory:
            base = Path(directory)
            with unittest.mock.patch.object(Path, "open", windows_open):
                # A 404 fails the ref screen, so its log is written and no later screen runs.
                record = SCREEN.measure(repository="acme/shop", commit=COMMIT, path="openapi.yaml",
                                        fetch=lambda _url, _subject: (404, b""), raw_base="http://127.0.0.1:9",
                                        logs=base / "screens", base=base, timeout=30)
            self.assertTrue(record["ref"]["outcome"].startswith("failed: HTTP 404"))
            self.assertIn(b"\n", (base / record["ref"]["log"]).read_bytes())
            self.assertEqual([], SCREEN.measured_failures(record, base))


class HistoricalRowTests(unittest.TestCase):
    """What the legacy index reads a screen row filed before the stage as."""

    ROW = {"source": "sourcegraph", "repository": "acme/shop", "path": "openapi.yaml", "commit": COMMIT,
           "keys": ["sample-shape"], "license": "passed", "ref": "passed", "fern": "passed",
           "disposition": "witness-found"}

    def write(self, row: dict[str, object]) -> Path:
        scratch = tempfile.TemporaryDirectory(prefix="witness-screen-history-")
        self.addCleanup(scratch.cleanup)
        path = Path(scratch.name) / "screens.jsonl"
        path.write_text(json.dumps(row) + "\n", encoding="utf-8")
        return path

    def test_a_row_predating_the_stage_is_read_and_labelled_historical(self) -> None:
        path = self.write({**self.ROW, "sha256": "a" * 64, "screened_at": "2026-09-29T12:54:27+00:00"})
        self.assertEqual(1, len(INDEX.jsonl(path)))
        result = INDEX.classify("sourcegraph", "sample-shape", {
            "repository": "acme/shop", "path": "openapi.yaml", "commit": COMMIT, "sha256": "a" * 64,
            "disposition": "declares", "selector_count": 1}, "candidates.jsonl:7", INDEX.screens(path.parent))
        self.assertEqual(f"candidates.jsonl:7; {INDEX.HISTORICAL_SCREEN}", result["evidence"])

    def test_a_row_filed_after_the_stage_without_its_record_is_refused(self) -> None:
        path = self.write({**self.ROW, "screened_at": "2026-10-03T09:00:00+00:00"})
        with self.assertRaises(ValueError) as refused:
            INDEX.jsonl(path)
        self.assertIn("a screen is filed only with its measured record", str(refused.exception))
        self.assertIn("after the measured stage landed", str(refused.exception))


class CommittedScreenTests(unittest.TestCase):
    """Every screen row the tree commits, read the way the two families read it."""

    def test_every_committed_screen_is_measured_whole_or_historical(self) -> None:
        surface = REPO / "docs" / "openapi-surface"
        measured = []
        for screens in sorted(surface.glob("**/screens.jsonl")):
            legacy = screens.parent.name.startswith("witness-search-")
            fields = INDEX.SCREEN_FIELDS if legacy else {name: name for name in SCREEN.SCREENS}
            for number, line in enumerate(screens.read_text(encoding="utf-8").splitlines(), 1):
                row = json.loads(line)
                with self.subTest(screens=screens.relative_to(REPO).as_posix(), line=number):
                    self.assertEqual([], SCREEN.row_failures(row, screens.parent, fields))
                if not SCREEN.is_historical(row):
                    measured.append(row["measured"])
        # At least one real candidate's Fern outcome is one pinned Fern produced
        # when the stage ran: its run's exit statuses, at the corpus pins.
        cli, generator, version, _config = SCREEN.corpus_fern_pins()
        ran = [record for record in measured if isinstance(record["fern"].get("run"), dict)]
        self.assertTrue(ran, "no committed screen carries a pinned Fern run")
        for record in ran:
            self.assertEqual((cli, generator, version), (record["fern"]["pins"]["fern_cli"],
                             record["fern"]["pins"]["generator"], record["fern"]["pins"]["generator_version"]))
            self.assertEqual(record["fern"]["outcome"], SCREEN.fern_verdict(record["fern"]["run"]))


class LicenceReadingTests(unittest.TestCase):
    """The licence reading against the rule's own enumeration, which it parses rather than copies."""

    def test_the_admissible_set_is_read_off_the_rule(self) -> None:
        families = SCREEN.admissible_families()
        rule = (REPO / "docs" / "corpus-licensing.md").read_text(encoding="utf-8")
        for family in families:
            self.assertIn(family, rule)
        self.assertIn("Apache-2.0", families)
        self.assertNotIn("other grants of that kind", " ".join(families))

    def test_every_family_the_rule_admits_is_one_the_reading_recognises(self) -> None:
        """The drift gate between the rule's enumeration and the spellings the reading knows."""
        self.assertEqual(set(SCREEN.admissible_families()), {family for family, _ in SCREEN.RECOGNISED})

    def test_each_reading(self) -> None:
        centred = "                                 Apache License\n                           Version 2.0, January 2004"
        for text, family in (("Apache 2.0", "Apache-2.0"), ("Apache License\nVersion 2.0", "Apache-2.0"),
                             (centred, "Apache-2.0"),
                             ("GNU LESSER GENERAL PUBLIC LICENSE", "LGPL"), ("AGPL-3.0", "AGPL"),
                             ("CC-BY-SA-4.0", "CC-BY-SA"), ("CC-BY-4.0", "CC-BY"), ("NOASSERTION", None),
                             ("CC-BY-NC-4.0", None), ("AppVeyor End User License Agreement (EULA)", None),
                             ("Proprietary", None)):
            with self.subTest(text=text):
                self.assertEqual(family, SCREEN.recognise(text))


if __name__ == "__main__":
    unittest.main()
