#!/usr/bin/env python3
"""The measured screening stage, driven through its real CLI and the legacy index that reads it.

`tools/witness-search/witness_screen.py screen` runs as a subprocess over a temporary
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
from typing import Any, ClassVar

# Every child these tests start has its output decoded as UTF-8, so a Python
# child writes UTF-8 too, whatever the platform locale (cp1252 on Windows).
os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "witness-search" / "witness_screen.py"
COMMIT = "c" * 40
DOCUMENT = b"openapi: 3.0.3\ninfo: {title: shop, version: '1'}\npaths: {}\n"
PROPRIETARY = b"openapi: 3.0.3\ninfo: {title: shop, version: '1', license: {name: Shop EULA}}\npaths: {}\n"
DECLARED = b"openapi: 3.0.3\ninfo: {title: shop, version: '1', license: {name: Apache 2.0}}\npaths: {}\n"
SECRET = "ghp_offlinesecretvalue0123456789"
FERN = """\
    import os, pathlib, sys, time
    mode = os.environ["FERN_STUB"]
    print("token in use: " + os.environ.get("GITHUB_TOKEN", ""))
    print("\\x1b[31mcoloured\\x1b[0m in " + os.getcwd() + " under " + os.path.expanduser("~"))
    if mode == "hang" or (mode == "generate-hang" and sys.argv[1] == "generate"):
        time.sleep(30)
    if mode == "refuse":
        print("Found 1 error in 0.42 seconds.")
        print("issue: the `x-fern-enum` extension is missing; add it")
        sys.exit(1)
    if sys.argv[1] == "generate":
        if mode == "generate-fail":
            print("error: the generator container exited 3")
            sys.exit(2)
        if mode == "generate-unparsed":
            print("Failed to parse the API definition; generated nothing")
            sys.exit(0)
        if mode == "generate-empty":
            sys.exit(0)
        package = pathlib.Path(sys.argv[sys.argv.index("--output") + 1]) / "fern-python-sdk"
        package.mkdir(parents=True)
        (package / "client.py").write_text("class Client: ...\\n", encoding="utf-8", newline="\\n")
    """


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SCREEN = load("witness_screen_under_test", SCRIPT)
INDEX = load(
    "witness_search_github_index_under_test", REPO / "tools" / "witness-search" / "witness-search-github-index.py"
)


class _RawServer(ThreadingHTTPServer):
    requests: list[str]


class _Raw(BaseHTTPRequestHandler):
    """raw.githubusercontent.com's exact-commit route, serving each candidate repository's file below."""

    server: _RawServer

    def log_message(self, format: str, *args: Any) -> None:
        pass

    def do_GET(self) -> None:
        self.server.requests.append(self.path)
        files = {
            f"/acme/shop/{COMMIT}/openapi.yaml": DOCUMENT,
            f"/acme/shop/{COMMIT}/LICENSE": b"MIT License\n\nCopyright (c) acme\n",
            f"/acme/eula/{COMMIT}/openapi.yaml": PROPRIETARY,
            f"/acme/eula/{COMMIT}/LICENSE": b"MIT License\n",
            # Declares an admissible grant itself; its repository's licence file is fetched and
            # recorded, but never decides it.
            f"/acme/declared/{COMMIT}/openapi.yaml": DECLARED,
            f"/acme/declared/{COMMIT}/LICENSE": b"All rights reserved.\n",
            f"/acme/garbled/{COMMIT}/openapi.yaml": b"openapi: [3.0.3\ninfo: {title\n",
            # Declares a grant, but not as a License Object; the MIT file must not stand in for it.
            f"/acme/malformed/{COMMIT}/openapi.yaml": b"openapi: 3.0.3\ninfo: {title: shop, version: '1', license: MIT}\npaths: {}\n",
            f"/acme/malformed/{COMMIT}/LICENSE": b"MIT License\n",
            f"/acme/custom/{COMMIT}/openapi.yaml": DOCUMENT,
            f"/acme/custom/{COMMIT}/LICENSE": b"The Acme Community Licence\n\nUse it as Acme says.\n",
            f"/acme/bare/{COMMIT}/openapi.yaml": DOCUMENT,
            # Only the last spelling the stage tries is there.
            f"/acme/copying/{COMMIT}/openapi.yaml": DOCUMENT,
            f"/acme/copying/{COMMIT}/COPYING": b"Apache License\nVersion 2.0, January 2004\n",
        }
        body = files.get(self.path)
        self.send_response(200 if body is not None else 404)
        body = body if body is not None else b"404: Not Found"
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


@unittest.skipIf(
    os.name == "nt", "a bare `fern` resolves only as fern.exe on Windows, which a script cannot stand in for"
)
class LegacyScreenCliTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory(prefix="witness-screen-")
        self.addCleanup(scratch.cleanup)
        self.scratch = Path(scratch.name)
        self.root = self.scratch / "surface"
        self.evidence = self.root / "witness-search-sourcegraph"
        self.evidence.mkdir(parents=True)
        (self.root / "witness-search-keys.tsv").write_text(
            "key\tselector\tregion\tcensus_status\nsample-shape\tschema:x\tschemas.md\tsupported\n", encoding="utf-8"
        )
        server = _RawServer(("127.0.0.1", 0), _Raw)
        server.requests = []
        self.server = server
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        fake_bin = self.scratch / "bin"
        fake_bin.mkdir()
        (fake_bin / "fern").write_text(f"#!{sys.executable}\n" + textwrap.dedent(FERN), encoding="utf-8", newline="\n")
        os.chmod(fake_bin / "fern", 0o755)
        self.env = {
            **os.environ,
            "PATH": f"{fake_bin}{os.pathsep}{os.environ['PATH']}",
            "FERN_STUB": "pass",
            "GITHUB_TOKEN": SECRET,
            "CROZIER_RAW_GITHUB_URL": f"http://127.0.0.1:{server.server_port}",
        }

    def screen(self, *args: str, repository: str = "acme/shop", **env: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "screen",
                "--source",
                "sourcegraph",
                "--key",
                "sample-shape",
                "--repository",
                repository,
                "--commit",
                COMMIT,
                "--path",
                "openapi.yaml",
                "--evidence-root",
                str(self.root),
                "--timeout",
                "60",
                *args,
            ],
            env={**self.env, **env},
            capture_output=True,
            text=True,
            cwd=REPO,
            timeout=300,
            encoding="utf-8",
        )

    def rows(self) -> list[dict[str, Any]]:
        path = self.evidence / "screens.jsonl"
        if not path.is_file():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

    def test_excluded_repositories_fail_before_fetching_or_filing(self) -> None:
        for repository in sorted(INDEX.EXCLUDED_REPOSITORIES):
            with self.subTest(repository=repository):
                rejected = self.screen(repository=repository)
                self.assertNotEqual(0, rejected.returncode)
                self.assertIn("excluded by the repository rule", rejected.stderr)
                self.assertIn("specification publisher's repository", rejected.stderr)
                self.assertEqual([], self.server.requests)
                self.assertEqual([], list(self.evidence.iterdir()))
        recovered = self.screen("--disposition", "witness-found")
        self.assertEqual(0, recovered.returncode, recovered.stderr)
        self.assertTrue(self.server.requests)
        self.assertEqual(1, len(self.rows()))

    def test_measure_refuses_opaque_history_before_its_real_fetch_boundary(self) -> None:
        load("rate_limit_guard", REPO / "tools/witness-search/rate_limit_guard.py")
        github = load("witness_screen_acquirer_for_test", REPO / "tools/witness-search/witness-search-github.py")
        acquirer = github.Acquirer(
            self.evidence, cache=self.scratch / "cache", raw_github_url=self.env["CROZIER_RAW_GITHUB_URL"]
        )
        token = INDEX.make_opaque_identity("d" * 32, 1)
        logs = self.evidence / "measurement-logs"
        with self.assertRaisesRegex(SystemExit, "opaque history cannot be measured again"):
            SCREEN.measure(
                repository="example/copied-input",
                commit=token,
                path=token,
                expected_sha256=token,
                fetch=lambda url, subject: acquirer.raw_github_get(url, "sample-shape", subject),
                raw_base=acquirer.raw_github_url,
                logs=logs,
                base=self.evidence,
            )
        self.assertEqual([], self.server.requests)
        self.assertFalse(logs.exists())
        self.assertEqual([], self.rows())

    def test_opaque_history_is_skipped_and_unknown_versions_fail_without_writes(self) -> None:
        def token(number: int) -> str:
            return INDEX.make_opaque_identity("b" * 32, number)

        arguments = ["--path", token(1), "--commit", token(2), "--sha256", token(3)]
        skipped = self.screen(*arguments, repository="example/copied-input")
        self.assertEqual(0, skipped.returncode, skipped.stderr)
        self.assertIn("screened by repository rule", skipped.stdout)
        self.assertEqual(1, len(skipped.stdout.splitlines()))
        self.assertEqual([], self.server.requests)
        self.assertEqual([], list(self.evidence.iterdir()))
        invalid = [arg.replace(":v2:", ":v3:") for arg in arguments]
        rejected = self.screen(*invalid, repository="example/copied-input")
        self.assertNotEqual(0, rejected.returncode)
        self.assertIn("unsupported opaque identity version v3", rejected.stderr)
        self.assertIn("restore valid v2 evidence", rejected.stderr)
        self.assertEqual([], self.server.requests)
        self.assertEqual([], list(self.evidence.iterdir()))
        recovered = self.screen(*arguments, repository="example/copied-input")
        self.assertEqual(0, recovered.returncode, recovered.stderr)
        self.assertEqual([], self.server.requests)
        self.assertEqual([], list(self.evidence.iterdir()))

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
        self.assertEqual(
            "passed: no info.license, LICENSE at the pinned commit reads as MIT, which the corpus rule admits",
            row["license"],
        )
        self.assertEqual(
            ("200", "LICENSE:200", "check 0, generate 0"),
            (record["ref"]["exit"], record["licence"]["exit"], record["fern"]["exit"]),
        )
        self.assertEqual(hashlib.sha256(DOCUMENT).hexdigest(), row["sha256"])
        # Every log is committed under `screens/`, carries its recorded digest, and
        # holds no credential the run could see.
        for name in ("licence", "ref", "fern"):
            log = self.evidence / record[name]["log"]
            self.assertTrue(record[name]["log"].startswith("screens/"))
            self.assertEqual(record[name]["log_sha256"], hashlib.sha256(log.read_bytes()).hexdigest())
            self.assertNotIn(SECRET, log.read_text(encoding="utf-8"))
        self.assertIn(
            "token in use: [GITHUB_TOKEN redacted]", (self.evidence / record["fern"]["log"]).read_text(encoding="utf-8")
        )
        # The reads went through the acquirer's raw lane, which logs each call.
        calls = [
            json.loads(line)
            for line in (self.evidence / "raw-github-calls.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual(["openapi.yaml", "LICENSE"] * 2, [call["url"].rsplit("/", 1)[1] for call in calls])
        # The refused first run left no log behind: only the filed record's three remain.
        self.assertEqual(
            sorted(record[name]["log"] for name in ("licence", "ref", "fern")),
            sorted(path.relative_to(self.evidence).as_posix() for path in (self.evidence / "screens").iterdir()),
        )
        # The legacy index reads the row as measured, and labels it nothing else.
        self.assertEqual([], SCREEN.row_failures(row, self.evidence, INDEX.SCREEN_FIELDS))
        self.assertEqual(1, len(INDEX.jsonl(self.evidence / "screens.jsonl")))
        screened = INDEX.screens(self.evidence)
        result = INDEX.classify(
            "sourcegraph",
            "sample-shape",
            {
                "repository": "acme/shop",
                "path": "openapi.yaml",
                "commit": COMMIT,
                "sha256": row["sha256"],
                "disposition": "declares",
                "selector_count": 1,
            },
            "candidates.jsonl:1",
            screened,
        )
        self.assertEqual(
            ("pass", "witness-found", "candidates.jsonl:1"),
            (result["fern_screen"], result["disposition"], result["evidence"]),
        )

    def test_a_ref_the_read_cannot_pin_fails_and_the_later_screens_do_not_run(self) -> None:
        for args, ref in (
            (["--commit", "main"], "failed: 'main' is no full commit SHA, so the ref is mutable"),
            (["--path", "gone.yaml"], f"failed: HTTP 404 reading gone.yaml at acme/shop@{COMMIT}"),
            (
                ["--sha256", "0" * 64],
                f"failed: the bytes at acme/shop@{COMMIT} carry sha256 "
                f"{hashlib.sha256(DOCUMENT).hexdigest()}, not the pinned {'0' * 64}",
            ),
        ):
            with self.subTest(args=args):
                (self.evidence / "screens.jsonl").unlink(missing_ok=True)
                command = [
                    sys.executable,
                    str(SCRIPT),
                    "screen",
                    "--source",
                    "sourcegraph",
                    "--key",
                    "sample-shape",
                    "--repository",
                    "acme/shop",
                    "--commit",
                    COMMIT,
                    "--path",
                    "openapi.yaml",
                    "--evidence-root",
                    str(self.root),
                ]
                for flag, value in zip(args[::2], args[1::2], strict=False):
                    if flag in command:
                        command[command.index(flag) + 1] = value
                    else:
                        command += [flag, value]
                done = subprocess.run(
                    command, env=self.env, capture_output=True, text=True, cwd=REPO, timeout=300, encoding="utf-8"
                )
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
        self.assertEqual(
            f"failed: {SCREEN.fern_label()} fern check exit 1: Found 1 error. First: the "
            "'x-fern-enum' extension is missing, add it",
            row["fern"],
        )

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
        self.assertEqual(
            ("MIT", "a third-party copy; the publisher grants nothing"),
            (pins["licence_file_family"], pins["judgement"]),
        )

    def test_a_record_missing_its_measurement_is_refused_naming_what_is_missing(self) -> None:
        self.assertEqual(0, self.screen("--disposition", "witness-found").returncode)
        record = self.rows()[0]["measured"]
        (self.evidence / "screens.jsonl").unlink()
        for mutate, missing in (
            (lambda r: r["fern"].pop("log_sha256"), "the fern screen's redacted log and its sha256"),
            (lambda r: r["licence"].pop("exit"), "the licence screen's exit status"),
            (
                lambda r: r["fern"]["run"].update(generate_exit="1"),
                "a fern outcome its run measured: it reads 'passed'",
            ),
            (lambda r: r.pop("stage"), "the stage that measured it"),
        ):
            broken = json.loads(json.dumps(record))
            mutate(broken)
            path = self.scratch / "broken.json"
            path.write_text(json.dumps(broken), encoding="utf-8", newline="\n")
            with self.subTest(missing=missing):
                refused = self.screen("--measured", str(path), "--disposition", "witness-found")
                self.assertEqual(1, refused.returncode)
                self.assertIn("a screen is filed only with its measured record; it lacks", refused.stderr)
                self.assertIn(missing, refused.stderr)
        self.assertEqual([], self.rows())

    def test_a_measured_log_outside_the_evidence_directory_is_refused(self) -> None:
        self.assertEqual(0, self.screen("--disposition", "witness-found").returncode)
        record = self.rows()[0]["measured"]
        (self.evidence / "screens.jsonl").unlink()
        # The same bytes, so each recorded digest still matches: only where the
        # log lives is wrong.
        data = (self.evidence / record["fern"]["log"]).read_bytes()
        outside = self.scratch / "outside.log"
        outside.write_bytes(data)
        (self.root / "outside.log").write_bytes(data)
        link = self.evidence / "screens" / "linked.log"
        link.symlink_to(outside)
        for log in (
            str(outside),
            "../outside.log",
            "screens/../../outside.log",
            "screens/linked.log",
            "screens\\..\\..\\outside.log",
            "C:/outside.log",
        ):
            broken = json.loads(json.dumps(record))
            broken["fern"]["log"] = log
            path = self.scratch / "outside.json"
            path.write_text(json.dumps(broken), encoding="utf-8", newline="\n")
            with self.subTest(log=log):
                refused = self.screen("--measured", str(path), "--disposition", "witness-found")
                self.assertEqual(1, refused.returncode, refused.stderr)
                self.assertIn(
                    f"the fern screen's log {log} inside the evidence directory, not outside it", refused.stderr
                )
                self.assertEqual([], self.rows())
                self.assertFalse(SCREEN.inside(self.evidence, log))
        self.assertEqual(data, outside.read_bytes())
        # The record as measured, its logs under the evidence directory, files.
        path.write_text(json.dumps(record), encoding="utf-8")
        self.assertEqual(0, self.screen("--measured", str(path), "--disposition", "witness-found").returncode)
        self.assertEqual(1, len(self.rows()))

    def test_a_disposition_the_index_cannot_read_is_refused_before_measuring(self) -> None:
        for disposition in (
            "approved",
            "witness-found-ish",
            "pending-registration; owner Bad Node",
            "pending-registration; owner -node",
            "outstanding",
            "byte-identical to CORPUS row x, sha256 abc",
        ):
            with self.subTest(disposition=disposition):
                refused = self.screen("--disposition", disposition)
                self.assertEqual(2, refused.returncode, refused.stderr)
                self.assertIn(f"{disposition!r} is not a disposition: use rejected, witness-found", refused.stderr)
                self.assertEqual([], self.rows())
                self.assertFalse((self.evidence / "screens").exists(), "a refused argument measured something")
        # Every spelling the index reads is filed as given.
        for disposition in ("rejected", "pending-registration; owner node-7"):
            with self.subTest(disposition=disposition):
                filed = self.screen("--disposition", disposition)
                self.assertEqual(0, filed.returncode, filed.stderr)
                self.assertEqual(disposition, self.rows()[-1]["disposition"])

    def test_an_unreadable_measured_file_or_timeout_is_refused_with_its_remedy(self) -> None:
        missing = self.screen("--measured", str(self.scratch / "absent.json"))
        self.assertEqual(1, missing.returncode)
        self.assertIn("pass the JSON file a measurement wrote, or drop --measured", missing.stderr)
        garbled = self.scratch / "garbled.json"
        garbled.write_text("{not json", encoding="utf-8", newline="\n")
        refused = self.screen("--measured", str(garbled))
        self.assertEqual(1, refused.returncode)
        self.assertIn("is not JSON", refused.stderr)
        zero = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "screen",
                "--source",
                "sourcegraph",
                "--key",
                "k",
                "--repository",
                "acme/shop",
                "--commit",
                COMMIT,
                "--path",
                "openapi.yaml",
                "--timeout",
                "0",
            ],
            capture_output=True,
            text=True,
            cwd=REPO,
            encoding="utf-8",
        )
        self.assertEqual(2, zero.returncode)
        self.assertIn("0 is not a positive number of seconds", zero.stderr)
        self.assertEqual([], self.rows())

    def raw_calls(self) -> list[str]:
        path = self.evidence / "raw-github-calls.jsonl"
        if not path.is_file():
            return []
        return [json.loads(line)["url"] for line in path.read_text(encoding="utf-8").splitlines()]

    def test_the_committed_logs_and_diagnostics_hold_no_escape_scratch_path_or_home(self) -> None:
        for mode, args in (("pass", ("--disposition", "witness-found")), ("generate-empty", ())):
            with self.subTest(mode=mode):
                (self.evidence / "screens.jsonl").unlink(missing_ok=True)
                done = self.screen(*args, FERN_STUB=mode)
                self.assertEqual(0, done.returncode, done.stderr)
                record = self.rows()[-1]["measured"]
                committed = [
                    (self.evidence / record["fern"]["log"]).read_text(encoding="utf-8"),
                    json.dumps(record["fern"]["run"]),
                ]
                home = os.path.expanduser("~")
                for text in committed:
                    self.assertNotIn("\x1b[", text)
                    self.assertNotIn("\\u001b", text)
                    self.assertNotIn(tempfile.gettempdir() + os.sep + "witness-screen-", text)
                    self.assertNotIn(home + os.sep, text)
                self.assertIn("coloured in <scratch>/", committed[0])
                self.assertIn(" under ~", committed[0])

    def test_each_way_generation_can_fail_after_check_passes_is_filed_as_measured(self) -> None:
        label = SCREEN.fern_label()
        for mode, fern in (
            (
                "generate-fail",
                f"failed: {label} fern generate exit 2 after fern check exit 0: "
                "error: the generator container exited 3",
            ),
            (
                "generate-unparsed",
                f"failed: {label} fern generate exit 0 over an unparsed document, 0 Python "
                "files: Failed to parse the API definition, generated nothing",
            ),
            ("generate-empty", f"failed: {label} fern generate exit 0 over an unparsed document, 0 Python files: "),
        ):
            with self.subTest(mode=mode):
                claimed = self.screen("--disposition", "witness-found", FERN_STUB=mode)
                self.assertEqual(1, claimed.returncode, claimed.stderr)
                self.assertIn("`witness-found` claims a candidate that passed every screen", claimed.stderr)
                done = self.screen(FERN_STUB=mode)
                self.assertEqual(0, done.returncode, done.stderr)
                row = self.rows()[-1]
                self.assertTrue(row["fern"].startswith(fern), row["fern"])
                self.assertEqual("rejected", row["disposition"])
                self.assertEqual([], SCREEN.measured_failures(row["measured"], self.evidence))
        hung = self.screen("--disposition", "witness-found", "--timeout", "1", FERN_STUB="generate-hang")
        self.assertEqual(1, hung.returncode)
        self.assertIn("Fern timed out after 1s on acme/shop:openapi.yaml; nothing was filed", hung.stderr)
        self.assertEqual(3, len(self.rows()), "a generation cut off by its timeout filed a row")

    def test_each_licence_reading_is_the_one_the_rule_gives(self) -> None:
        tried = [f"{name}" for name in SCREEN.LICENCE_FILES]
        for repository, args, licence, reads in (
            (
                "acme/declared",
                ("--disposition", "witness-found"),
                "passed: info.license 'Apache 2.0' reads as Apache-2.0, which the corpus rule admits",
                ["openapi.yaml", "LICENSE"],
            ),
            (
                "acme/garbled",
                (),
                "failed: the document could not be read for its info.license",
                ["openapi.yaml", *tried],
            ),
            (
                "acme/malformed",
                (),
                "failed: info.license is there but is no License Object (a mapping naming "
                "the grant in a string identifier, name or url)",
                ["openapi.yaml", "LICENSE"],
            ),
            (
                "acme/custom",
                (),
                "failed: no info.license, and LICENSE at the pinned commit names no grant the corpus rule admits",
                ["openapi.yaml", "LICENSE"],
            ),
            (
                "acme/bare",
                (),
                "failed: grants nothing — no info.license and no licence file at the pinned commit",
                ["openapi.yaml", *tried],
            ),
            (
                "acme/copying",
                ("--disposition", "witness-found"),
                "passed: no info.license, COPYING at the pinned commit reads as Apache-2.0, which the corpus rule "
                "admits",
                ["openapi.yaml", *tried],
            ),
        ):
            with self.subTest(repository=repository):
                (self.evidence / "raw-github-calls.jsonl").unlink(missing_ok=True)
                done = self.screen(*args, repository=repository)
                self.assertEqual(0, done.returncode, done.stderr)
                row = self.rows()[-1]
                self.assertEqual(licence, row["license"])
                self.assertEqual(reads, [url.rsplit("/", 1)[1] for url in self.raw_calls()])
                self.assertEqual([], SCREEN.measured_failures(row["measured"], self.evidence))
                if licence.startswith("failed: "):
                    self.assertEqual(
                        ("rejected", "not-run: the licence screen failed"), (row["disposition"], row["fern"])
                    )

    def test_a_path_outside_the_repository_or_a_mutable_ref_is_never_fetched(self) -> None:
        for path in ("../openapi.yaml", "/openapi.yaml", "specs/./openapi.yaml", "specs\\openapi.yaml", ""):
            with self.subTest(path=path):
                refused = subprocess.run(
                    [
                        sys.executable,
                        str(SCRIPT),
                        "screen",
                        "--source",
                        "sourcegraph",
                        "--key",
                        "sample-shape",
                        "--repository",
                        "acme/shop",
                        "--commit",
                        COMMIT,
                        "--path",
                        path,
                        "--evidence-root",
                        str(self.root),
                    ],
                    env=self.env,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    cwd=REPO,
                )
                self.assertEqual(1, refused.returncode, refused.stderr)
                self.assertIn(f"{path!r} is no path inside a repository", refused.stderr)
        for repository in ("../acme", "acme/..", "./shop"):
            with self.subTest(repository=repository):
                refused = self.screen(repository=repository)
                self.assertEqual(1, refused.returncode, refused.stderr)
                self.assertIn(f"{repository!r} is no `<owner>/<name>` repository", refused.stderr)
        mutable = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "screen",
                "--source",
                "sourcegraph",
                "--key",
                "sample-shape",
                "--repository",
                "acme/shop",
                "--commit",
                "main",
                "--path",
                "openapi.yaml",
                "--evidence-root",
                str(self.root),
            ],
            env=self.env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=REPO,
        )
        self.assertEqual(0, mutable.returncode, mutable.stderr)
        self.assertEqual("failed: 'main' is no full commit SHA, so the ref is mutable", self.rows()[-1]["ref"])
        self.assertEqual("not-fetched", self.rows()[-1]["measured"]["ref"]["exit"])
        self.assertEqual([], self.raw_calls(), "a mutable ref or a refused path was fetched")
        self.assertEqual(1, len(self.rows()))

    def test_a_key_no_witness_search_names_is_refused_before_measuring(self) -> None:
        unknown = self.screen("--key", "no-such-shape", "--disposition", "witness-found")
        self.assertEqual(1, unknown.returncode, unknown.stderr)
        self.assertIn("--key 'no-such-shape' is no witness-search key in", unknown.stderr)
        empty = self.screen("--key", " ")
        self.assertEqual(2, empty.returncode, empty.stderr)
        self.assertIn("a key is a non-empty witness-search key", empty.stderr)
        self.assertEqual([], self.rows())
        self.assertEqual([], self.raw_calls())

    def test_a_whole_record_of_another_document_is_refused(self) -> None:
        self.assertEqual(0, self.screen("--disposition", "witness-found").returncode)
        record = self.rows()[0]["measured"]
        (self.evidence / "screens.jsonl").unlink()
        path = self.scratch / "measured.json"
        path.write_text(json.dumps(record), encoding="utf-8")
        refused = self.screen("--measured", str(path), "--disposition", "witness-found", repository="acme/eula")
        self.assertEqual(1, refused.returncode, refused.stderr)
        self.assertIn("the measured record names another document than --repository/--commit/--path", refused.stderr)
        self.assertEqual([], self.rows())
        pinned = self.screen("--measured", str(path), "--disposition", "witness-found", "--sha256", "0" * 64)
        self.assertEqual(1, pinned.returncode, pinned.stderr)
        self.assertIn(f"not the --sha256 {'0' * 64} the acquisition pinned", pinned.stderr)
        self.assertEqual([], self.rows())
        self.assertEqual(0, self.screen("--measured", str(path), "--disposition", "witness-found").returncode)

    def test_a_keys_file_that_is_not_the_derivation_is_refused(self) -> None:
        keys = self.root / "witness-search-keys.tsv"
        for text, message in (
            ("selector\tregion\nschema:x\ts.md\n", "has no header naming a `key` column once"),
            ("key\tkey\nsample-shape\tother\n", "has no header naming a `key` column once"),
            ("key\tselector\nsample-shape\n", "witness-search-keys.tsv:2 is not 2 cells with a key"),
            ("key\tselector\n\tschema:x\n", "witness-search-keys.tsv:2 is not 2 cells with a key"),
        ):
            with self.subTest(text=text):
                keys.write_text(text, encoding="utf-8")
                refused = self.screen("--disposition", "witness-found")
                self.assertEqual(1, refused.returncode, refused.stderr)
                self.assertIn(message, refused.stderr)
                self.assertIn("witness-search-region-keys.py", refused.stderr)
        self.assertEqual([], self.rows())
        self.assertEqual([], self.raw_calls())

    def test_a_measured_record_whose_parts_disagree_is_refused_naming_the_part(self) -> None:
        self.assertEqual(0, self.screen("--disposition", "witness-found").returncode)
        record = self.rows()[0]["measured"]
        (self.evidence / "screens.jsonl").unlink()

        def licence_pins(**pins: object):
            return lambda r: r["licence"]["pins"].update(pins)

        for mutate, missing in (
            (lambda r: r.update(screened_at="yesterday"), "when it was measured (`screened_at`"),
            (lambda r: r.update(screened_at="2026-10-05T10:00:00"), "when it was measured (`screened_at`"),
            (lambda r: r["document"].update(path=""), "the document it read (['path'] of `document`)"),
            (lambda r: r["document"].update(path="../escape.yaml"), "the document it read (['path'] of `document`)"),
            (
                lambda r: r["document"].update(repository="../acme"),
                "the document it read (['repository'] of `document`)",
            ),
            (lambda r: r["ref"].update(outcome="passed-invalid"), "a ref outcome reading `passed` or `failed: "),
            (lambda r: r["ref"].update(outcome="passed: "), "a ref outcome reading `passed` or `failed: "),
            (lambda r: r["ref"].update(outcome="passed:    "), "a ref outcome reading `passed` or `failed: "),
            (lambda r: r["fern"].update(outcome="failed: "), "the fern screen's reason: 'failed: ' says what happened"),
            (lambda r: r["ref"]["pins"].update(path="other.yaml"), "its repository, commit and path pins"),
            (lambda r: r["ref"]["pins"].update(expected_sha256="0" * 64), "the bytes its pin names"),
            (licence_pins(judgement="a third-party copy"), "a judgement can only refuse"),
            (
                licence_pins(document_licence="Apache 2.0", document_family=None),
                "the licence screen's reading of its document's info.license",
            ),
            (licence_pins(licence_file_sha256=""), "the licence screen's licence file and its sha256"),
            (licence_pins(rule="docs/elsewhere.md"), "the licence screen's rule (docs/corpus-licensing.md"),
            (lambda r: r["fern"]["run"].update(generate_python_files="3"), "`run.generate_python_files` as a count"),
            (lambda r: r["fern"]["run"].update(check_diagnostic=7), "`run.check_diagnostic` as a string"),
            (
                lambda r: r["fern"]["run"].update(generate_exit="maybe"),
                "`run.generate_exit` as an exit status or `timeout`",
            ),
            (lambda r: r["fern"]["run"].update(generate_diagnostic=["no"]), "`run.generate_diagnostic` as a string"),
            (licence_pins(admissible="MIT"), "the licence screen's admissible set as the rule it read listed it"),
            (licence_pins(admissible=["MIT", 7]), "the licence screen's admissible set as the rule it read listed it"),
            (licence_pins(document_licence=None), "a pass needs `document_licence` read"),
            (
                licence_pins(document_licence="Apache 2.0", document_family="MIT"),
                "family for info.license 'Apache 2.0' as the reading gives it ('Apache-2.0', not 'MIT')",
            ),
            (lambda r: r["fern"]["run"].update(sha256="0" * 64), "run over the document the record names"),
            (lambda r: r["fern"].update(exit="check 0"), "exit as its run records it ('check 0, generate 0'"),
            (lambda r: r["fern"]["run"].update(check_exit="maybe"), "`run.check_exit` as an exit status or `timeout`"),
            (lambda r: r["fern"]["run"].update(check_exit="1"), "a generation exactly when `fern check` exited 0"),
            (
                lambda r: r["licence"].update(outcome="failed: a third-party copy"),
                "it runs only after the ref and licence screens pass",
            ),
        ):
            broken = json.loads(json.dumps(record))
            mutate(broken)
            path = self.scratch / "broken.json"
            path.write_text(json.dumps(broken), encoding="utf-8", newline="\n")
            with self.subTest(missing=missing):
                refused = self.screen("--measured", str(path), "--disposition", "witness-found")
                self.assertEqual(1, refused.returncode, refused.stderr)
                self.assertIn("a screen is filed only with its measured record; it lacks", refused.stderr)
                self.assertIn(missing, refused.stderr)
                self.assertNotIn("Traceback", refused.stderr)
        self.assertEqual([], self.rows())


class GoldenFernPinsTests(unittest.TestCase):
    """The Fern pins a screen runs at come off the goldens' own metadata; a golden
    whose record is not one stops the stage, naming the file, before anything is
    filed. Driven through the real CLI over a synthetic root holding the stage."""

    def test_a_golden_metadata_record_that_is_no_pin_set_is_refused(self) -> None:
        good = {
            "cliVersion": "5.20.0",
            "generatorName": "fernapi/fern-python-sdk",
            "generatorVersion": "4.3.17",
            "generatorConfig": {"enum_type": "python_enums"},
        }
        for label, text, message in (
            ("not JSON", "{not json", "is not JSON"),
            ("not an object", "[]", "is not a JSON object"),
            ("no CLI version", json.dumps({**good, "cliVersion": ""}), "lacks a non-empty cliVersion"),
            (
                "config no mapping",
                json.dumps({**good, "generatorConfig": "python_enums"}),
                "carries a generatorConfig that is no mapping",
            ),
            ("no golden at all", None, "no golden records its Fern pins"),
        ):
            with self.subTest(label), tempfile.TemporaryDirectory(prefix="witness-screen-pins-") as scratch:
                root = Path(scratch)
                for relative in (
                    "tools/witness-search/witness_screen.py",
                    "tools/witness-search/witness-search-github-index.py",
                    "docs/corpus-licensing.md",
                ):
                    (root / relative).parent.mkdir(parents=True, exist_ok=True)
                    (root / relative).write_bytes((REPO / relative).read_bytes())
                if text is not None:
                    metadata = root / "tests/fixtures/alpha/expected/.fern/metadata.json"
                    metadata.parent.mkdir(parents=True)
                    metadata.write_text(text, encoding="utf-8")
                surface = root / "docs/openapi-surface"
                (surface / "witness-search-sourcegraph").mkdir(parents=True)
                (surface / "witness-search-keys.tsv").write_text(
                    "key\tselector\nsample-shape\tschema:x\n", encoding="utf-8"
                )
                # Whole enough for the stage to reach the Fern screen, which is what reads the pins.
                section = {"exit": "200", "pins": {}, "log": "screens/x.log", "log_sha256": "0" * 64}
                record = {
                    "stage": SCREEN.STAGE,
                    "screened_at": "2026-10-05T10:00:00+00:00",
                    "document": {
                        "repository": "acme/shop",
                        "commit": COMMIT,
                        "path": "openapi.yaml",
                        "sha256": "a" * 64,
                    },
                    "ref": {**section, "outcome": "failed: HTTP 404"},
                    "licence": {"outcome": "not-run: the ref screen failed"},
                    "fern": {**section, "outcome": "passed", "exit": "check 0, generate 0"},
                }
                measured = root / "record.json"
                measured.write_text(json.dumps(record), encoding="utf-8")
                refused = subprocess.run(
                    [
                        sys.executable,
                        str(root / "tools/witness-search/witness_screen.py"),
                        "screen",
                        "--source",
                        "sourcegraph",
                        "--key",
                        "sample-shape",
                        "--repository",
                        "acme/shop",
                        "--commit",
                        COMMIT,
                        "--path",
                        "openapi.yaml",
                        "--evidence-root",
                        str(surface),
                        "--measured",
                        str(measured),
                        "--disposition",
                        "witness-found",
                    ],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=120,
                )
                self.assertEqual(1, refused.returncode, refused.stderr)
                self.assertIn(message, refused.stderr)
                self.assertNotIn("Traceback", refused.stderr)
                if text is not None:
                    self.assertIn("tests/fixtures/alpha/expected/.fern/metadata.json", refused.stderr)
                self.assertFalse((surface / "witness-search-sourcegraph" / "screens.jsonl").exists())


class WindowsNewlineTests(unittest.TestCase):
    """A committed log carries the digest recorded for it under Windows' text-mode newlines."""

    def test_a_log_written_under_crlf_translation_still_carries_its_recorded_digest(self) -> None:
        opened = Path.open

        def windows_open(
            path: Path,
            mode: str = "r",
            buffering: int = -1,
            encoding: str | None = None,
            errors: str | None = None,
            newline: str | None = None,
        ):
            # Windows' text mode: an unset `newline` writes each `\n` as `\r\n`.
            if "b" not in mode and newline is None:
                newline = "\r\n"
            return opened(path, mode, buffering, encoding, errors, newline)

        with tempfile.TemporaryDirectory(prefix="witness-screen-") as directory:
            base = Path(directory)
            with unittest.mock.patch.object(Path, "open", windows_open):
                # A 404 fails the ref screen, so its log is written and no later screen runs.
                record = SCREEN.measure(
                    repository="acme/shop",
                    commit=COMMIT,
                    path="openapi.yaml",
                    fetch=lambda _url, _subject: (404, b""),
                    raw_base="http://127.0.0.1:9",
                    logs=base / "screens",
                    base=base,
                    timeout=30,
                )
            self.assertTrue(record["ref"]["outcome"].startswith("failed: HTTP 404"))
            self.assertIn(b"\n", (base / record["ref"]["log"]).read_bytes())
            self.assertEqual([], SCREEN.measured_failures(record, base))


class HistoricalRowTests(unittest.TestCase):
    """What the legacy index reads a screen row filed before the stage as."""

    ROW: ClassVar = {
        "source": "sourcegraph",
        "repository": "acme/shop",
        "path": "openapi.yaml",
        "commit": COMMIT,
        "keys": ["sample-shape"],
        "license": "passed",
        "ref": "passed",
        "fern": "passed",
        "disposition": "witness-found",
    }

    def write(self, row: dict[str, object]) -> Path:
        scratch = tempfile.TemporaryDirectory(prefix="witness-screen-history-")
        self.addCleanup(scratch.cleanup)
        path = Path(scratch.name) / "screens.jsonl"
        path.write_text(json.dumps(row) + "\n", encoding="utf-8", newline="\n")
        return path

    def test_a_row_predating_the_stage_is_read_and_labelled_historical(self) -> None:
        path = self.write({**self.ROW, "sha256": "a" * 64, "screened_at": "2026-09-29T12:54:27+00:00"})
        self.assertEqual(1, len(INDEX.jsonl(path)))
        result = INDEX.classify(
            "sourcegraph",
            "sample-shape",
            {
                "repository": "acme/shop",
                "path": "openapi.yaml",
                "commit": COMMIT,
                "sha256": "a" * 64,
                "disposition": "declares",
                "selector_count": 1,
            },
            "candidates.jsonl:7",
            INDEX.screens(path.parent),
        )
        self.assertEqual(f"candidates.jsonl:7; {INDEX.HISTORICAL_SCREEN}", result["evidence"])

    def test_an_unmeasured_row_stands_as_historical_only_when_its_date_predates_the_stage(self) -> None:
        for label, dates, refusal in (
            ("no date: the shape filed before the stage", {}, None),
            ("Z offset, before", {"screened_at": "2026-09-30T23:59:59Z"}, None),
            ("recorded_at, before", {"recorded_at": "2026-09-01T00:00:00+00:00"}, None),
            ("another offset, before in UTC", {"screened_at": "2026-10-02T01:00:00+02:00"}, None),
            ("exactly the cutover", {"screened_at": "2026-10-02T00:00:00Z"}, "after the measured stage landed"),
            ("after", {"recorded_at": "2026-10-05T00:00:00+00:00"}, "after the measured stage landed"),
            ("no offset", {"screened_at": "2026-09-01T00:00:00"}, "is no ISO 8601 instant with its offset"),
            ("malformed", {"screened_at": "last week"}, "is no ISO 8601 instant with its offset"),
            ("empty", {"screened_at": ""}, "is no ISO 8601 instant with its offset"),
        ):
            with self.subTest(label):
                path = self.write({**self.ROW, "sha256": "a" * 64, **dates})
                if refusal is None:
                    self.assertEqual(1, len(INDEX.jsonl(path)))
                    continue
                with self.assertRaises(ValueError) as refused:
                    INDEX.jsonl(path)
                self.assertIn("a screen is filed only with its measured record", str(refused.exception))
                self.assertIn(refusal, str(refused.exception))

    def test_a_row_filed_after_the_stage_without_its_record_is_refused(self) -> None:
        path = self.write({**self.ROW, "screened_at": "2026-10-03T09:00:00+00:00"})
        with self.assertRaises(ValueError) as refused:
            INDEX.jsonl(path)
        self.assertIn("a screen is filed only with its measured record", str(refused.exception))
        self.assertIn("after the measured stage landed", str(refused.exception))

    def test_the_index_cli_names_where_a_late_row_is_filed_today(self) -> None:
        root = Path(self.write({**self.ROW, "screened_at": "2026-10-03T09:00:00+00:00"}).parent)
        source = root / "witness-search-github-code-search"
        source.mkdir()
        (root / "screens.jsonl").rename(source / "screens.jsonl")
        refused = subprocess.run(
            [
                sys.executable,
                str(REPO / "tools" / "witness-search" / "witness-search-github-index.py"),
                "--check",
                "--evidence-root",
                str(root),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=REPO,
            timeout=60,
        )
        self.assertEqual(1, refused.returncode, refused.stderr)
        self.assertIn("file it through `tools/witness-search/witness_screen.py`", refused.stderr)
        self.assertTrue((REPO / "tools" / "witness-search" / "witness_screen.py").is_file())


class CommittedScreenTests(unittest.TestCase):
    """Every screen row the tree commits, read the way the two families read it."""

    def test_the_legacy_sources_are_the_ledgers_that_carry_screens(self) -> None:
        surface = REPO / "docs" / "openapi-surface"
        ledgers = {
            screens.parent.name.removeprefix("witness-search-")
            for screens in surface.glob("witness-search-*/screens.jsonl")
        }
        self.assertEqual(
            ledgers,
            set(SCREEN.LEGACY_SOURCES),
            "`screen --source` must offer exactly the legacy ledgers that file screens",
        )

    def test_every_committed_screen_is_measured_whole_or_historical(self) -> None:
        surface = REPO / "docs" / "openapi-surface"
        measured = []
        for screens in sorted(surface.glob("**/screens.jsonl")):
            # A key-scoped search files its legacy rows one level down, under
            # `witness-search-<key>/<source>/`, in the same row shape.
            legacy = screens.relative_to(surface).parts[0].startswith("witness-search-")
            fields = INDEX.SCREEN_FIELDS if legacy else {name: name for name in SCREEN.SCREENS}
            for number, line in enumerate(screens.read_text(encoding="utf-8").splitlines(), 1):
                row = json.loads(line)
                with self.subTest(screens=screens.relative_to(REPO).as_posix(), line=number):
                    self.assertEqual([], SCREEN.row_failures(row, screens.parent, fields))
                if not SCREEN.unmeasured(row):
                    measured.append(row["measured"])
        # At least one real candidate's Fern outcome is one pinned Fern produced
        # when the stage ran: its run's exit statuses, at the corpus pins.
        cli, generator, version, _config = SCREEN.corpus_fern_pins()
        ran = [record for record in measured if isinstance(record["fern"].get("run"), dict)]
        self.assertTrue(ran, "no committed screen carries a pinned Fern run")
        for record in ran:
            self.assertEqual(
                (cli, generator, version),
                (
                    record["fern"]["pins"]["fern_cli"],
                    record["fern"]["pins"]["generator"],
                    record["fern"]["pins"]["generator_version"],
                ),
            )
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
        centred = (
            "                                 Apache License\n                           Version 2.0, January 2004"
        )
        for text, family in (
            ("Apache 2.0", "Apache-2.0"),
            ("Apache License\nVersion 2.0", "Apache-2.0"),
            (centred, "Apache-2.0"),
            ("GNU LESSER GENERAL PUBLIC LICENSE", "LGPL"),
            ("AGPL-3.0", "AGPL"),
            ("CC-BY-SA-4.0", "CC-BY-SA"),
            ("CC-BY-4.0", "CC-BY"),
            ("NOASSERTION", None),
            ("CC-BY-NC-4.0", None),
            ("AppVeyor End User License Agreement (EULA)", None),
            ("Proprietary", None),
        ):
            with self.subTest(text=text):
                self.assertEqual(family, SCREEN.recognise(text))


if __name__ == "__main__":
    unittest.main()
