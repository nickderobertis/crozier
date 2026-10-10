#!/usr/bin/env python3
"""End-to-end coverage of the witness-search acquisition, census and ledger scripts."""

from __future__ import annotations

import csv
import gzip
import hashlib
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

# Every child these tests start has its output decoded as UTF-8, so a Python
# child writes UTF-8 too, whatever the platform locale (cp1252 on Windows).
os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools/witness-search/witness-search-local-census.py"
GITHUB_ACQUIRE = REPO / "tools/witness-search/witness-acquire-github.py"
KEYS = REPO / "tools/surface-census/witness-search-region-keys.py"
TRACKED_KEYS = REPO / "docs/openapi-surface/witness-search-keys.tsv"
POSTMAN = REPO / "tools/witness-search/witness-search-postman.py"
PORTAL_TREES = REPO / "tools/witness-search/witness-search-portal-trees.py"
# The hit kinds each Postman index's answer counts, as the real API reports them.
POSTMAN_KINDS = ("team", "collection", "api", "apiDefinition", "specification")


def run_explicit_key_census(interpreter_flags: list[str]) -> tuple[int, dict]:
    """Census a YAML tree only PyYAML reads, under the given interpreter flags."""
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        documents = root / "documents"
        documents.mkdir()
        (documents / "hit.yaml").write_text(
            "? openapi\n: 3.0.0\npaths: {}\ncomponents:\n  schemas:\n"
            "    Shape:\n      type: array\n      items: {type: string}\n",
            encoding="utf-8",
            newline="\n",
        )
        (documents / "broken.yaml").write_text("? openapi\n: [unterminated\n", encoding="utf-8", newline="\n")
        contract = root / "keys.md"
        contract.write_text(
            "| key | selector |\n|---|---|\n| `array` | `schema.items` |\n",
            encoding="utf-8",
            newline="\n",
        )
        completed = subprocess.run(
            [
                sys.executable,
                *interpreter_flags,
                str(SCRIPT),
                "--contract",
                str(contract),
                "--documents",
                f"local={documents}",
                "--all-documents-jsonl",
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=30,
            encoding="utf-8",
        )
        return completed.returncode, {row["document"]: row for row in map(json.loads, completed.stdout.splitlines())}


def pyyaml_importable(interpreter_flags: list[str]) -> bool:
    return (
        subprocess.run(
            [sys.executable, *interpreter_flags, "-c", "import yaml"],
            capture_output=True,
            timeout=30,
        ).returncode
        == 0
    )


def load_rate_limit_guard():
    """The guard module the acquisition CLI loads, read from the same file."""
    spec = importlib.util.spec_from_file_location(
        "acquisition_test_guard", REPO / "tools/witness-search/rate_limit_guard.py"
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class WitnessSearchAcquisitionTest(unittest.TestCase):
    """Registry, portal, Postman and local-tree acquisition driven through the real CLIs."""

    def test_explicit_yaml_mapping_key_is_read_by_the_stdlib_reader(self) -> None:
        # crozier#363: the census's own YAML subset reads `?` keys, so a valid
        # document never needs PyYAML; only a malformed one reaches the fallback.
        if not pyyaml_importable([]):
            self.skipTest("PyYAML is not installed for this interpreter")
        returncode, rows = run_explicit_key_census([])
        self.assertEqual(returncode, 1)
        self.assertEqual(rows["hit.yaml"]["classification"], "openapi-3")
        self.assertEqual(rows["hit.yaml"]["loader"], "stdlib-census-yaml")
        self.assertGreater(rows["hit.yaml"]["selectors"]["array"], 0)
        self.assertEqual(rows["broken.yaml"]["classification"], "unreadable")
        self.assertIn("PyYAML parse failure", rows["broken.yaml"]["error"])

    def test_explicit_yaml_mapping_key_without_pyyaml_is_still_read(self) -> None:
        # `-S` drops site-packages, which is where an installed PyYAML lives;
        # the census scripts themselves are stdlib-only.
        if pyyaml_importable(["-S"]):
            self.skipTest("PyYAML is importable even without site-packages")
        returncode, rows = run_explicit_key_census(["-S"])
        self.assertEqual(returncode, 1)
        self.assertEqual(rows["hit.yaml"]["classification"], "openapi-3")
        self.assertEqual(rows["hit.yaml"]["loader"], "stdlib-census-yaml")
        self.assertGreater(rows["hit.yaml"]["selectors"]["array"], 0)
        self.assertEqual(rows["broken.yaml"]["classification"], "unreadable")
        self.assertEqual(rows["broken.yaml"]["loader"], "stdlib-census-yaml")
        self.assertNotIn("selectors", rows["broken.yaml"])
        self.assertIn("never closed", rows["broken.yaml"]["error"])

    def test_invalid_json_is_recorded_as_a_parse_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "broken.json").write_text('{"openapi":"3.0.0","paths":{},}', encoding="utf-8", newline="\n")
            contract = root / "keys.md"
            contract.write_text(
                "| key | selector |\n|---|---|\n| `array` | `schema.items` |\n",
                encoding="utf-8",
                newline="\n",
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--contract",
                    str(contract),
                    "--documents",
                    f"local={root}",
                    "--all-documents-jsonl",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 1)
            record = json.loads(completed.stdout)
            self.assertEqual(record["classification"], "unreadable")
            self.assertEqual(record["loader"], "stdlib-json")
            self.assertIn("trailing comma at", record["error"])

    def test_other_json_decode_failure_is_unreadable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "broken.json").write_text('{"openapi":', encoding="utf-8", newline="\n")
            contract = root / "keys.md"
            contract.write_text(
                "| key | selector |\n|---|---|\n| `array` | `schema.items` |\n",
                encoding="utf-8",
                newline="\n",
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--contract",
                    str(contract),
                    "--documents",
                    f"local={root}",
                    "--all-documents-jsonl",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 1)
            record = json.loads(completed.stdout)
            self.assertEqual(record["classification"], "unreadable")
            self.assertIn("Expecting value", record["error"])

    def test_portal_archive_inventory_uses_real_tree_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            archives = root / "archives"
            archives.mkdir()
            source = root / "source"
            source.mkdir()
            (source / "openapi.json").write_text('{"openapi":"3.0.0"}', encoding="utf-8", newline="\n")
            (source / "notes.txt").write_text("not a spec", encoding="utf-8", newline="\n")
            pin = "a" * 40
            with tarfile.open(archives / "example--api.tar.gz", "w:gz") as archive:
                for path in source.iterdir():
                    archive.add(path, arcname=f"api-{pin}/{path.name}")
            plan = root / "plan.tsv"
            plan.write_text(
                "repository\tpinned_ref\nexample/api\t" + pin + "\nmutable/api\tmain\n",
                encoding="utf-8",
                newline="\n",
            )
            tree = root / "tree"
            manifest = root / "manifest.tsv"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(PORTAL_TREES),
                    "--plan",
                    str(plan),
                    "--archives",
                    str(archives),
                    "--tree",
                    str(tree),
                    "--manifest",
                    str(manifest),
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual((tree / "example--api/openapi.json").read_bytes(), (source / "openapi.json").read_bytes())
            self.assertFalse((tree / "example--api/notes.txt").exists())
            self.assertFalse((tree / "mutable--api").exists())
            with manifest.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle, dialect="excel-tab"))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["path"], "openapi.json")
            self.assertEqual(rows[0]["sha256"], hashlib.sha256((source / "openapi.json").read_bytes()).hexdigest())

    def test_portal_archive_refusals_name_a_repair(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            archives = root / "archives"
            archives.mkdir()
            tree = root / "tree"
            manifest = root / "manifest.tsv"
            plan = root / "plan.tsv"
            command = [
                sys.executable,
                str(PORTAL_TREES),
                "--plan",
                str(plan),
                "--archives",
                str(archives),
                "--tree",
                str(tree),
                "--manifest",
                str(manifest),
            ]
            plan.write_text("wrong\theader\n", encoding="utf-8", newline="\n")
            malformed = subprocess.run(command, cwd=REPO, capture_output=True, text=True, timeout=30, encoding="utf-8")
            self.assertEqual(malformed.returncode, 1)
            self.assertIn("repository and pinned_ref columns", malformed.stderr)
            plan.write_text("repository\tpinned_ref\nexample/api\t" + "a" * 40 + "\n", encoding="utf-8", newline="\n")
            missing = subprocess.run(command, cwd=REPO, capture_output=True, text=True, timeout=30, encoding="utf-8")
            self.assertEqual(missing.returncode, 1)
            self.assertIn("missing pinned archive", missing.stderr)
            archive = archives / "example--api.tar.gz"
            with tarfile.open(archive, "w:gz") as handle:
                body = b'{"openapi":"3.0.0"}'
                info = tarfile.TarInfo("api-" + "a" * 40 + "/../escape.json")
                info.size = len(body)
                handle.addfile(info, io.BytesIO(body))
            unsafe = subprocess.run(command, cwd=REPO, capture_output=True, text=True, timeout=30, encoding="utf-8")
            self.assertEqual(unsafe.returncode, 1)
            self.assertIn("unsafe archive path", unsafe.stderr)
            self.assertFalse(manifest.exists())

    def test_portal_archive_names_and_plan_identities_cannot_escape_the_tree(self) -> None:
        pin = "a" * 40
        body = b'{"openapi":"3.0.0"}'
        # Each escapes the extraction root on some host of the release matrix:
        # an absolute name, a Windows drive, or backslash traversal.
        for name in (
            "/abs-root/escape.json",
            f"api-{pin}/C:/escape.json",
            f"api-{pin}/..\\..\\escape.json",
            f"api-{pin}\\..\\escape.json",
            f"../api-{pin}/escape.json",
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                archives = root / "archives"
                archives.mkdir()
                with tarfile.open(archives / "example--api.tar.gz", "w:gz") as handle:
                    info = tarfile.TarInfo(name)
                    info.size = len(body)
                    handle.addfile(info, io.BytesIO(body))
                plan = root / "plan.tsv"
                plan.write_text(f"repository\tpinned_ref\nexample/api\t{pin}\n", encoding="utf-8")
                completed = subprocess.run(
                    [
                        sys.executable,
                        str(PORTAL_TREES),
                        "--plan",
                        str(plan),
                        "--archives",
                        str(archives),
                        "--tree",
                        str(root / "tree"),
                        "--manifest",
                        str(root / "manifest.tsv"),
                    ],
                    cwd=REPO,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=30,
                )
                self.assertEqual(completed.returncode, 1, completed.stderr)
                self.assertIn("unsafe archive path", completed.stderr)
                self.assertIn("check the plan and pinned archives before retrying", completed.stderr)
                self.assertFalse((root / "tree").exists())
                self.assertFalse((root / "manifest.tsv").exists())

        # A pinned row names a GitHub owner/name at a full hexadecimal commit;
        # a repository of `..` would otherwise write beside the tree.
        for repository, revision, message in (
            ("..", pin, "is not a GitHub owner/name"),
            ("example/..", pin, "is not a GitHub owner/name"),
            ("example", pin, "is not a GitHub owner/name"),
            ("example/api/extra", pin, "is not a GitHub owner/name"),
            ("example/a pi", pin, "is not a GitHub owner/name"),
            ("example/api", "g" * 40, "is not a full lowercase hexadecimal commit SHA"),
            ("example/api", "A" * 40, "is not a full lowercase hexadecimal commit SHA"),
        ):
            with self.subTest(repository=repository, revision=revision), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                archives = root / "archives"
                archives.mkdir()
                with tarfile.open(archives / f"{repository.replace('/', '--')}.tar.gz", "w:gz") as handle:
                    info = tarfile.TarInfo(f"api-{pin}/escape.json")
                    info.size = len(body)
                    handle.addfile(info, io.BytesIO(body))
                plan = root / "plan.tsv"
                plan.write_text(f"repository\tpinned_ref\n{repository}\t{revision}\n", encoding="utf-8")
                tree = root / "work" / "tree"
                completed = subprocess.run(
                    [
                        sys.executable,
                        str(PORTAL_TREES),
                        "--plan",
                        str(plan),
                        "--archives",
                        str(archives),
                        "--tree",
                        str(tree),
                        "--manifest",
                        str(root / "manifest.tsv"),
                    ],
                    cwd=REPO,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=30,
                )
                self.assertEqual(completed.returncode, 1, completed.stderr)
                self.assertIn(message, completed.stderr)
                self.assertFalse((root / "work").exists())
                self.assertFalse((root / "manifest.tsv").exists())

        with tempfile.TemporaryDirectory() as temporary:
            plan = Path(temporary) / "plan.tsv"
            plan.write_text("repository\tpinned_ref\nexample/api\n", encoding="utf-8")
            short = subprocess.run(
                [
                    sys.executable,
                    str(PORTAL_TREES),
                    "--plan",
                    str(plan),
                    "--archives",
                    temporary,
                    "--tree",
                    str(Path(temporary) / "tree"),
                    "--manifest",
                    str(Path(temporary) / "m.tsv"),
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(short.returncode, 1, short.stderr)
            self.assertIn("lacks a repository or pinned_ref cell", short.stderr)
            self.assertNotIn("Traceback", short.stderr)

        # Every row of the committed plan still reads: pinned rows validate, and
        # the rows recording why no immutable ref exists are skipped as before.
        spec = importlib.util.spec_from_file_location("portal_trees_plan", PORTAL_TREES)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with (REPO / "docs/openapi-surface/witness-search-portal-plan.tsv").open(
            encoding="utf-8", newline=""
        ) as handle:
            committed = list(csv.DictReader(handle, dialect="excel-tab"))
        self.assertEqual(sum(map(module.pinned, committed)), len(committed) - 3)

    def test_postman_search_records_queries_and_refusal_without_zero(self) -> None:
        received = []

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                received.append(body)
                if len(received) == 1:
                    self.send_response(403)
                    payload = b"Forbidden"
                else:
                    self.send_response(200)
                    payload = json.dumps({"data": {}, "meta": {"total": dict.fromkeys(POSTMAN_KINDS, 0)}}).encode(
                        "utf-8"
                    )
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text(
                "key\tselector\narray-item\tschema.items\noauth2-password\tsecurityScheme.flows.password\n",
                encoding="utf-8",
                newline="\n",
            )
            evidence = root / "postman"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(POSTMAN),
                    "--keys",
                    str(keys),
                    "--evidence-dir",
                    str(evidence),
                    "--url",
                    f"http://127.0.0.1:{server.server_port}/proxy",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = [json.loads(line) for line in (evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(len(rows), 12)
            self.assertNotEqual(rows[0]["query"], rows[3]["query"])
            self.assertEqual(rows[0]["classification"], "source-refused")
            self.assertEqual(rows[0]["status"], 403)
            self.assertNotIn("totals", rows[0])
            self.assertEqual(rows[1]["classification"], "answered")
            self.assertEqual(rows[1]["totals"]["api"], 0)
            self.assertEqual(rows[9]["query"], "oauth2 password flows")
            self.assertEqual(
                {x["body"]["queryIndices"][0] for x in received}, {"apinetwork.team", "runtime.collection", "adp.api"}
            )
            self.assertTrue(all(len(x["body"]["queryIndices"]) == 1 for x in received))
            waits = [
                json.loads(line)
                for line in (evidence / "rate-limit-waits.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertTrue(any(row["cause"] == "spacing" for row in waits))

    def test_postman_refusal_waits_then_paginates_answer(self) -> None:
        received = []

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                received.append(body)
                if len(received) == 1:
                    self.send_response(429)
                    self.send_header("Retry-After", "0")
                    payload = b"paced refusal"
                else:
                    index = body["body"]["queryIndices"][0]
                    count = 26 if index == "apinetwork.team" else 0
                    payload = json.dumps(
                        {
                            "data": {},
                            "meta": {
                                "total": {
                                    **dict.fromkeys(POSTMAN_KINDS, 0),
                                    "team": count,
                                }
                            },
                        }
                    ).encode("utf-8")
                    self.send_response(200)
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8", newline="\n")
            evidence = root / "postman"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(POSTMAN),
                    "--keys",
                    str(keys),
                    "--evidence-dir",
                    str(evidence),
                    "--url",
                    f"http://127.0.0.1:{server.server_port}/proxy",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=50,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = [json.loads(line) for line in (evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(rows[0]["classification"], "source-refused")
            self.assertEqual(rows[0]["status"], 429)
            self.assertEqual(rows[1]["classification"], "answered")
            self.assertIn(25, [row["offset"] for row in rows])
            waits = [
                json.loads(line)
                for line in (evidence / "rate-limit-waits.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertTrue(any(row["cause"] == "backoff" for row in waits))

    def test_postman_malformed_answer_is_source_error(self) -> None:
        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                self.rfile.read(int(self.headers["Content-Length"]))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"meta":{}}')

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8", newline="\n")
            evidence = root / "postman"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(POSTMAN),
                    "--keys",
                    str(keys),
                    "--evidence-dir",
                    str(evidence),
                    "--url",
                    f"http://127.0.0.1:{server.server_port}/proxy",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = [json.loads(line) for line in (evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(len(rows), 6)
            self.assertTrue(all(row["classification"] == "source-error" for row in rows))
            self.assertTrue(all("total" in row["error"] for row in rows))

    def test_postman_transport_refusal_records_unknown_status(self) -> None:
        received = []

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                self.rfile.read(int(self.headers["Content-Length"]))
                received.append(self.path)
                if len(received) == 1:
                    self.connection.close()
                    return
                self.send_response(200)
                self.end_headers()
                self.wfile.write(
                    json.dumps({"data": {}, "meta": {"total": dict.fromkeys(POSTMAN_KINDS, 0)}}).encode("utf-8")
                )

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8", newline="\n")
            evidence = root / "postman"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(POSTMAN),
                    "--keys",
                    str(keys),
                    "--evidence-dir",
                    str(evidence),
                    "--url",
                    f"http://127.0.0.1:{server.server_port}/proxy",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=40,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = [json.loads(line) for line in (evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(rows[0]["classification"], "source-refused")
            self.assertIsNone(rows[0]["status"])
            self.assertTrue(rows[0]["response"])
            self.assertTrue(all(row["classification"] == "answered" for row in rows[1:]))

    def test_postman_totals_must_be_reported_nonnegative_integer_counts(self) -> None:
        answers: list[dict] = []

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                index = body["body"]["queryIndices"][0]
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps({"data": {}, "meta": {"total": answers[0][index]}}).encode())

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        counted = dict.fromkeys(POSTMAN_KINDS, 0)
        for totals, error in (
            ({**counted, "team": "40"}, "meta.total.team is '40', not a nonnegative integer count"),
            ({**counted, "collection": 30.5}, "meta.total.collection is 30.5, not a nonnegative integer count"),
            ({**counted, "api": -1}, "meta.total.api is -1, not a nonnegative integer count"),
            ({**counted, "specification": True}, "meta.total.specification is True"),
            ({key: 0 for key in counted if key != "team"}, "meta.total has no count for team"),
            ({key: 0 for key in counted if key != "apiDefinition"}, "meta.total has no count for apiDefinition"),
        ):
            # Every index answers the same malformed totals; the one it counts
            # is what refuses the answer.
            bad = next(kind for kind in POSTMAN_KINDS if kind not in totals or totals[kind] != 0)
            index = {"team": "apinetwork.team", "collection": "runtime.collection"}.get(bad, "adp.api")
            answers[:] = [
                {
                    name: totals if name == index else counted
                    for name in ("apinetwork.team", "runtime.collection", "adp.api")
                }
            ]
            with self.subTest(totals=totals), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                keys = root / "keys.tsv"
                keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8")
                evidence = root / "postman"
                completed = subprocess.run(
                    [
                        sys.executable,
                        str(POSTMAN),
                        "--keys",
                        str(keys),
                        "--evidence-dir",
                        str(evidence),
                        "--url",
                        f"http://127.0.0.1:{server.server_port}/proxy",
                    ],
                    cwd=REPO,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=60,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                rows = [json.loads(line) for line in (evidence / "queries.jsonl").read_text().splitlines()]
                self.assertEqual(len(rows), 6)
                refused = [row for row in rows if row["index"] == index]
                self.assertEqual([row["classification"] for row in refused], ["source-error"] * 2)
                self.assertTrue(all(error in row["error"] for row in refused), refused)
                self.assertTrue(all("totals" not in row for row in refused))
                self.assertTrue(all(row["classification"] == "answered" for row in rows if row["index"] != index))

    def test_postman_key_derivation_rows_are_validated_before_any_request(self) -> None:
        received = []

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                received.append(self.path)
                self.send_response(500)
                self.end_headers()

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        header = "key\tselector\tregion\tcensus_status\n"
        good = "array-item\tschema.items\tschemas.md\tsupported\n"
        for text, error in (
            (header + good + "\tschema.items\tschemas.md\tsupported\n", "line 3 has an empty key or selector"),
            (header + good + "empty-selector\t\tschemas.md\tsupported\n", "line 3 has an empty key or selector"),
            (header + good + "short\tschema.items\n", "line 3 does not have the header's 4 cells"),
            (
                header + good + "long\tschema.items\tschemas.md\tsupported\textra\n",
                "line 3 does not have the header's 4 cells",
            ),
            (header + good + good, "line 3 repeats key 'array-item'"),
            (
                header + good + "array-item\tsecurityScheme:$ref\tsecurity.md\tunsupported-by-census\n",
                "line 3 repeats key 'array-item'",
            ),
            (
                header + good + "typo\tschema.items\tschemas.md\tsuported\n",
                "line 3 has census_status 'suported', not supported or unsupported-by-census",
            ),
            (
                header + good + "\tsecurityScheme:$ref\tsecurity.md\tunsupported-by-census\n",
                "line 3 has an empty key or selector",
            ),
            ("key\tselector\tkey\tcensus_status\n" + good, "its header names key more than once"),
            (
                header + good + "invented\tschema.bogus:nope\tschemas.md\tsupported\n",
                "line 3 (invented): 'schema.bogus:nope' is not one of the predicate selectors",
            ),
            (
                header + "unsupported\tsecurityScheme:$ref\tsecurity.md\tunsupported-by-census\n",
                "it has no supported key rows",
            ),
            ("name\tvalue\narray-item\tschema.items\n", "it has no key and selector columns"),
        ):
            with self.subTest(error=error), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                keys = root / "keys.tsv"
                keys.write_text(text, encoding="utf-8")
                completed = subprocess.run(
                    [
                        sys.executable,
                        str(POSTMAN),
                        "--keys",
                        str(keys),
                        "--evidence-dir",
                        str(root / "postman"),
                        "--url",
                        f"http://127.0.0.1:{server.server_port}/proxy",
                    ],
                    cwd=REPO,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=30,
                )
                self.assertEqual(completed.returncode, 2, completed.stderr)
                self.assertIn("--keys must be the region-key derivation TSV", completed.stderr)
                self.assertIn(error, completed.stderr)
                self.assertIn("regenerate the region-key derivation", completed.stderr)
                self.assertFalse((root / "postman").exists())
        self.assertEqual(received, [])
        # A row the derivation marks unsupported is skipped, not refused, and the
        # committed derivation reads.
        spec = importlib.util.spec_from_file_location("postman_keys", POSTMAN)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        census = module.load_census()
        with tempfile.TemporaryDirectory() as temporary:
            keys = Path(temporary) / "keys.tsv"
            keys.write_text(
                header + good + "unsupported\tsecurityScheme:$ref\tsecurity.md\tunsupported-by-census\n",
                encoding="utf-8",
                newline="\n",
            )
            self.assertEqual([row["key"] for row in module.read_keys(keys, census)], ["array-item"])
        self.assertTrue(module.read_keys(TRACKED_KEYS, census))

    def test_postman_missing_key_derivation_gives_repair_action(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            completed = subprocess.run(
                [
                    sys.executable,
                    str(POSTMAN),
                    "--keys",
                    str(root / "missing.tsv"),
                    "--evidence-dir",
                    str(root / "evidence"),
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 2)
            self.assertIn("regenerate the region-key derivation", completed.stderr)

    def test_postman_repeated_refusals_stop_at_guard_budget(self) -> None:
        received = []

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                self.rfile.read(int(self.headers["Content-Length"]))
                received.append(self.path)
                self.send_response(429)
                self.send_header("Retry-After", "0")
                self.end_headers()
                self.wfile.write(b"refused")

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8", newline="\n")
            evidence = root / "postman"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(POSTMAN),
                    "--keys",
                    str(keys),
                    "--evidence-dir",
                    str(evidence),
                    "--url",
                    f"http://127.0.0.1:{server.server_port}/proxy",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=180,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(len(received), 5)
            rows = [json.loads(line) for line in (evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()]
            # The fifth response closes the guard reservation by raising
            # SecondaryLimit, so the consumer records that refusal with its
            # query identity and error instead of a normal HTTP result row.
            self.assertEqual(len([row for row in rows if row.get("status") == 429]), 4)
            self.assertEqual(len([row for row in rows if row.get("error", "").startswith("postman")]), 6)
            self.assertTrue(all(row["classification"] == "source-refused" for row in rows))

    def test_postman_metadata_hits_are_acquired_and_classified_by_census(self) -> None:
        received = []
        throttled = []
        openapi = json.dumps(
            {
                "openapi": "3.0.0",
                "info": {"title": "t", "version": "1"},
                "paths": {},
                "components": {"schemas": {"Shape": {"type": "array", "items": {"type": "string"}}}},
            }
        ).encode("utf-8")
        collection = json.dumps(
            {
                "info": {
                    "_postman_id": "c",
                    "name": "array item",
                    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
                },
                "item": [],
            }
        ).encode("utf-8")

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                received.append(self.path)
                if self.path == "/collections/1-openapi" and not throttled:
                    throttled.append(self.path)
                    status, kind, body = 429, "text/plain", b"slow down"
                elif self.path == "/collections/1-openapi":
                    status, kind, body = 200, "application/json", openapi
                elif self.path == "/collections/2-coll":
                    status, kind, body = 200, "application/json; charset=utf-8", collection
                elif self.path == "/collections/3-bad":
                    status, kind, body = 200, "application/json", b"{not json"
                elif self.path == "/acme-team":
                    status, kind, body = 200, "text/html", b"<!doctype html><title>Postman</title>"
                else:
                    status, kind, body = 401, "application/problem+json", b'{"status":401}'
                self.send_response(status)
                self.send_header("Content-Type", kind)
                if status == 429:
                    self.send_header("Retry-After", "0")
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        base = f"http://127.0.0.1:{server.server_port}"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\nquery-says-nothing\tschema.items\n", encoding="utf-8", newline="\n")
            evidence = root / "postman"
            evidence.mkdir()
            # The query text shares no word with the shape; only the body can declare it.
            (evidence / "queries.jsonl").write_text(
                json.dumps(
                    {
                        "key": "query-says-nothing",
                        "query": "unrelated words",
                        "status": 200,
                        "data": {
                            "team": [{"document": {"id": 7, "publicHandle": "acme-team"}}],
                            "collection": [{"document": {"id": "1-openapi"}}, {"document": {"id": "3-bad"}}],
                            "request": [
                                {"document": {"id": "r", "collection": {"id": "2-coll"}}},
                                {"document": {"id": "r2", "collection": {"id": "1-openapi"}}},
                                "not-a-hit",
                            ],
                            "api": [{"document": {"id": "api-9"}}, {"document": {"id": "../x?y"}}],
                        },
                    }
                )
                + "\n",
                encoding="utf-8",
                newline="\n",
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    str(POSTMAN),
                    "--keys",
                    str(keys),
                    "--evidence-dir",
                    str(evidence),
                    "--acquire-hits",
                    "--web-base",
                    base,
                    "--api-base",
                    base,
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=120,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = {
                row["id"]: row
                for row in (
                    json.loads(line)
                    for line in (evidence / "hit-access.jsonl").read_text(encoding="utf-8").splitlines()
                )
            }
            self.assertEqual(set(rows), {"7", "1-openapi", "2-coll", "3-bad", "api-9", "../x?y"})
            self.assertEqual(rows["3-bad"]["classification"], "parse-failure")
            self.assertIn("/apis/..%2Fx%3Fy", received)
            # Each request hit is read through its own parent collection, never by its own id.
            self.assertFalse({"/collections/r", "/collections/r2"} & set(received))
            self.assertEqual(rows["1-openapi"]["classification"], "openapi-3")
            self.assertEqual(rows["1-openapi"]["selectors"], {"query-says-nothing": 1})
            self.assertEqual(rows["1-openapi"]["sha256"], hashlib.sha256(openapi).hexdigest())
            self.assertEqual(received.count("/collections/1-openapi"), 2)
            self.assertEqual(rows["2-coll"]["classification"], "not-openapi-3")
            self.assertEqual(rows["2-coll"]["document_kind"], "postman-collection")
            self.assertNotIn("selectors", rows["2-coll"])
            self.assertEqual(rows["7"]["classification"], "no-document-body")
            self.assertEqual((rows["api-9"]["status"], rows["api-9"]["classification"]), (401, "source-refused"))
            waits = [
                json.loads(line)
                for line in (evidence / "rate-limit-waits.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertTrue(any(row["cause"] == "backoff" for row in waits))
            calls = (evidence / "rate-limit-calls.jsonl").read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(calls), len(received))

    def test_outstanding_items_are_derived_by_key_and_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "witness-search-keys.tsv").write_text(
                "key\tselector\tregion\tcensus_status\n"
                "shape-a\tschema.items\tschemas.md\tsupported\n"
                "scheme-ref\tsecurityScheme:$ref\tsecurity.md\tunsupported-by-census\n",
                encoding="utf-8",
                newline="\n",
            )
            (root / "witness-search-portal-plan.tsv").write_text(
                "repository\tpinned_ref\tprior_path\tderivation\tacquisition\n"
                "gone/docs\tno-immutable-ref: HTTP 404\tapi.json\tprior\tsource-refused\n"
                "kept/docs\tabc\tapi.json\tprior\tacquired\n",
                encoding="utf-8",
                newline="\n",
            )
            portals = root / "witness-search-vendor-portals"
            portals.mkdir()
            (portals / "records.tsv").write_text(
                "source\tkey\tcandidate\trevision\tdigest\tcensus\tlicence_screen\trevision_screen\t"
                "fern_screen\tdisposition\tevidence\n"
                "vendor-portals\tshape-a\tbig.json\tabc\td\t3\tpass\tpass\t"
                "not-run: Fern check timed out after 3600 seconds\toutstanding\tx\n"
                "vendor-portals\tshape-a\tok.json\tabc\td\t1\tpass\tpass\tpass\twitness-found\tx\n",
                encoding="utf-8",
                newline="\n",
            )
            (portals / "enumeration.tsv").write_text(
                "walk\tdocument\trevision\tsha256\tmatched_keys\tstatus\n"
                "kept/docs\tbad.json\tabc\t" + "0" * 64 + "\t\tunreadable: trailing comma\n"
                "kept/docs\tok.json\tabc\t" + "1" * 64 + "\tshape-a\treadable\n",
                encoding="utf-8",
                newline="\n",
            )
            header = (
                "source\tkey\tcandidate\trevision\tdigest\tcensus\tlicence_screen\t"
                "revision_screen\tfern_screen\tdisposition\tevidence\n"
            )
            for source in ("apis.guru", "jentic"):
                (root / f"witness-search-{source}").mkdir(exist_ok=True)
                (root / f"witness-search-{source}/records.tsv").write_text(header, encoding="utf-8", newline="\n")
            (root / "witness-search-registries").mkdir()
            command = [
                sys.executable,
                str(REPO / "tools/witness-search/witness-search-registries-index.py"),
                "--root",
                str(root),
            ]
            stale = subprocess.run([*command, "--check"], capture_output=True, text=True, timeout=30, encoding="utf-8")
            self.assertEqual(stale.returncode, 1)
            self.assertIn("rerun without --check", stale.stderr)
            registries = root / "witness-search-registries"
            if os.name != "nt" and os.geteuid() != 0:
                # A directory it cannot write, then an index it cannot read: each named with its fix.
                registries.chmod(0o555)
                try:
                    unwritable = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=30)
                finally:
                    registries.chmod(0o755)
                self.assertEqual(unwritable.returncode, 1, unwritable.stderr)
                self.assertNotIn("Traceback", unwritable.stderr)
                self.assertIn(
                    f"cannot write {registries / 'candidates.tsv'} (Permission denied); make "
                    f"{registries} a writable directory, then rerun",
                    unwritable.stderr,
                )
            self.assertEqual(subprocess.run(command, timeout=30).returncode, 0)
            self.assertEqual(subprocess.run([*command, "--check"], timeout=30).returncode, 0)
            if os.name != "nt" and os.geteuid() != 0:
                (registries / "candidates.tsv").chmod(0)
                try:
                    unreadable = subprocess.run(
                        [*command, "--check"], capture_output=True, text=True, encoding="utf-8", timeout=30
                    )
                finally:
                    (registries / "candidates.tsv").chmod(0o644)
                self.assertEqual(unreadable.returncode, 1, unreadable.stderr)
                self.assertNotIn("Traceback", unreadable.stderr)
                self.assertIn(
                    f"cannot read {registries / 'candidates.tsv'} (Permission denied); make "
                    f"{registries / 'candidates.tsv'} readable, then rerun",
                    unreadable.stderr,
                )
            with (root / "witness-search-registries/outstanding.tsv").open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle, dialect="excel-tab"))
            with (root / "witness-search-registries/candidates.tsv").open(newline="", encoding="utf-8") as handle:
                ledger = list(csv.DictReader(handle, dialect="excel-tab"))
            self.assertEqual(
                [(row["candidate"], row["record"]) for row in ledger],
                [
                    ("big.json", "witness-search-vendor-portals/records.tsv:2"),
                    ("ok.json", "witness-search-vendor-portals/records.tsv:3"),
                ],
            )
            found = {(row["key"], row["source"], row["kind"]): row for row in rows}
            self.assertEqual(
                {(source, kind) for key, source, kind in found if key == "scheme-ref"},
                {(source, "selector-unavailable") for source in ("apis.guru", "jentic", "vendor-portals")},
            )
            self.assertEqual(
                json.loads(found["shape-a", "vendor-portals", "inconclusive-screen"]["items"]), ["big.json@abc"]
            )
            self.assertIn("3600 seconds", found["shape-a", "vendor-portals", "inconclusive-screen"]["blocker"])
            self.assertEqual(
                json.loads(found["shape-a", "vendor-portals", "unreadable-document"]["items"]), ["bad.json@abc"]
            )
            self.assertEqual(found["shape-a", "vendor-portals", "portal-unanswered"]["items"], '["gone/docs"]')
            self.assertEqual(len(rows), 6)
            (root / "witness-search-jentic/records.tsv").write_text("source\tkey\n", encoding="utf-8", newline="\n")
            broken = subprocess.run(command, capture_output=True, text=True, timeout=30, encoding="utf-8")
            self.assertEqual(broken.returncode, 1)
            self.assertIn("does not have the candidate-record header", broken.stderr)
            self.assertIn("repair the ledger it names", broken.stderr)
            (root / "witness-search-jentic/records.tsv").write_text(
                header + "jentic\tshape-a\tall-pass.json\tabc\td\t1\tpass\tpass\tpass\toutstanding\tx\n",
                encoding="utf-8",
                newline="\n",
            )
            passing = subprocess.run(command, capture_output=True, text=True, timeout=30, encoding="utf-8")
            self.assertEqual(passing.returncode, 1)
            self.assertIn("records.tsv:2 is outstanding but every screen reads pass", passing.stderr)
            self.assertIn("repair the ledger it names", passing.stderr)
            good = "jentic\tshape-a\tc.json\tabc\td\t1\tpass\tpass\tpass\twitness-found\tx"
            for label, row, message in (
                ("short", "jentic\tshape-a\tc.json", "records.tsv:2 has another number of cells than its header names"),
                ("long", good + "\tsurplus", "records.tsv:2 has another number of cells than its header names"),
                ("no candidate", good.replace("c.json", ""), "records.tsv:2 has no candidate"),
                (
                    "another source",
                    good.replace("jentic", "apis.guru", 1),
                    "is filed under jentic but names source 'apis.guru'",
                ),
                (
                    "unknown screen",
                    good.replace("\tpass\tpass\tpass", "\tpass\tok\tpass"),
                    "has revision_screen 'ok', not pass, failed: <reason> or not-run: <reason>",
                ),
                (
                    "screen without its reason",
                    good.replace("\tpass\tpass\tpass", "\tpass\tfailed: \tpass"),
                    "has revision_screen 'failed: ', not pass, failed: <reason> or not-run: <reason>",
                ),
                (
                    "unknown disposition",
                    good.replace("witness-found", "approved"),
                    "has disposition 'approved', which the index grammar does not read",
                ),
                (
                    "witness over a failed screen",
                    good.replace("\tpass\tpass\tpass", "\tfailed: refused\tpass\tpass"),
                    "settles the candidate as 'witness-found' but its licence_screen reads 'failed: refused'",
                ),
                (
                    "corpus copy over an unrun screen",
                    good.replace(
                        "\tpass\twitness-found",
                        "\tnot-run: no fern\tbyte-identical to CORPUS row 1, sha256 " + "0" * 64,
                    ),
                    "but its fern_screen reads 'not-run: no fern'",
                ),
                (
                    "pending registration over a failed screen",
                    good.replace(
                        "\tpass\tpass\tpass\twitness-found", "\tpass\tfailed: moved\tpass\tpending-registration"
                    ),
                    "settles the candidate as 'pending-registration' but its revision_screen reads 'failed: moved'",
                ),
            ):
                with self.subTest(label):
                    (root / "witness-search-jentic/records.tsv").write_text(header + row + "\n", encoding="utf-8")
                    refused = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=30)
                    self.assertEqual(refused.returncode, 1, refused.stderr)
                    self.assertIn(message, refused.stderr)
                    self.assertIn("repair the ledger it names", refused.stderr)
            (root / "witness-search-jentic/records.tsv").write_text(header, encoding="utf-8", newline="\n")
            for label, path, text, message in (
                (
                    "repeated column",
                    root / "witness-search-keys.tsv",
                    "key\tselector\tregion\tcensus_status\tkey\nshape-a\tx\ts.md\tsupported\tother\n",
                    "witness-search-keys.tsv names column(s) key twice",
                ),
                (
                    "census status",
                    root / "witness-search-keys.tsv",
                    "key\tselector\tregion\tcensus_status\nshape-a\tx\ts.md\tmaybe\n",
                    "witness-search-keys.tsv:2 has census_status 'maybe', not one of supported, unsupported-by-census",
                ),
                # A repeated key would count its documents twice, or under two statuses at once.
                (
                    "repeated key",
                    root / "witness-search-keys.tsv",
                    "key\tselector\tregion\tcensus_status\nshape-a\tx\ts.md\tsupported\n"
                    "shape-a\tsecurityScheme:$ref\ts.md\tunsupported-by-census\n",
                    "witness-search-keys.tsv:3 repeats key 'shape-a' (first at line 2)",
                ),
                (
                    "unreadable without its reason",
                    portals / "enumeration.tsv",
                    "walk\tdocument\trevision\tsha256\tmatched_keys\tstatus\nk\tx.json\tabc\t-\t\tunreadable: \n",
                    "enumeration.tsv:2 has status 'unreadable: ', not readable or unreadable: <reason>",
                ),
                (
                    "enumeration status",
                    portals / "enumeration.tsv",
                    "walk\tdocument\trevision\tsha256\tmatched_keys\tstatus\nk\tx.json\tabc\t-\t\tskipped\n",
                    "enumeration.tsv:2 has status 'skipped', not readable or unreadable: <reason>",
                ),
                (
                    "acquisition",
                    root / "witness-search-portal-plan.tsv",
                    "repository\tpinned_ref\tprior_path\tderivation\tacquisition\nkept/docs\tabc\ta\tp\tpending\n",
                    "witness-search-portal-plan.tsv:2 has acquisition 'pending', not source-refused, acquired",
                ),
                (
                    "acquired spelled otherwise",
                    root / "witness-search-portal-plan.tsv",
                    "repository\tpinned_ref\tprior_path\tderivation\tacquisition\nkept/docs\tabc\ta\tp\tacquired-invalid\n",
                    "witness-search-portal-plan.tsv:2 has acquisition 'acquired-invalid', not source-refused",
                ),
            ):
                with self.subTest(label):
                    kept = path.read_text(encoding="utf-8")
                    path.write_text(text, encoding="utf-8")
                    refused = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=30)
                    path.write_text(kept, encoding="utf-8")
                    self.assertEqual(refused.returncode, 1, refused.stderr)
                    self.assertIn(message, refused.stderr)
            (root / "witness-search-keys.tsv").write_text("key\tselector\nshape-a\tx\n", encoding="utf-8", newline="\n")
            unnamed = subprocess.run(command, capture_output=True, text=True, timeout=30, encoding="utf-8")
            self.assertEqual(unnamed.returncode, 1)
            self.assertIn("witness-search-keys.tsv lacks column(s) census_status", unnamed.stderr)

    def test_postman_hit_refused_past_the_guard_budget_is_recorded_not_retried(self) -> None:
        received = []

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                received.append(self.path)
                self.send_response(429)
                self.send_header("Retry-After", "0")
                self.end_headers()
                self.wfile.write(b"refused")

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        base = f"http://127.0.0.1:{server.server_port}"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8", newline="\n")
            evidence = root / "postman"
            evidence.mkdir()
            (evidence / "queries.jsonl").write_text(
                json.dumps(
                    {
                        "key": "array-item",
                        "data": {"collection": [{"document": {"id": "c"}}]},
                    }
                )
                + "\n",
                encoding="utf-8",
                newline="\n",
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    str(POSTMAN),
                    "--keys",
                    str(keys),
                    "--evidence-dir",
                    str(evidence),
                    "--acquire-hits",
                    "--web-base",
                    base,
                    "--api-base",
                    base,
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=240,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(len(received), 5)
            [row] = [
                json.loads(line) for line in (evidence / "hit-access.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual((row["status"], row["classification"]), (None, "source-refused"))
            self.assertIn("postman", row["response"])
            waits = [
                json.loads(line)
                for line in (evidence / "rate-limit-waits.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual(len([w for w in waits if w["cause"] == "backoff"]), 4)

    def test_postman_hit_acquisition_without_a_search_gives_repair_action(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8", newline="\n")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(POSTMAN),
                    "--keys",
                    str(keys),
                    "--evidence-dir",
                    str(root / "postman"),
                    "--acquire-hits",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 1)
            self.assertIn("run the search stage first", completed.stderr)
            self.assertFalse((root / "postman" / "hit-access.jsonl").exists())

    def test_the_registries_are_the_declared_sources_the_github_index_does_not_hold(self) -> None:
        """The two indexes partition the arm search's declared sources between them."""

        def load(name: str, path: Path):
            spec = importlib.util.spec_from_file_location(name, path)
            assert spec and spec.loader
            module = importlib.util.module_from_spec(spec)
            sys.modules[name] = module
            spec.loader.exec_module(module)
            return module

        registries = load("registries_index_sources", REPO / "tools/witness-search/witness-search-registries-index.py")
        github = load("github_index_sources", REPO / "tools/witness-search/witness-search-github-index.py")
        search = load("golden_reach_search_sources", REPO / "tools/surface-census/golden-reach-search.py")
        self.assertEqual(
            tuple(source for source in search.DECLARED_SOURCES if source not in github.SOURCES),
            registries.SOURCES,
        )
        self.assertEqual(set(search.DECLARED_SOURCES), set(registries.SOURCES) | set(github.SOURCES))
        self.assertFalse(set(registries.SOURCES) & set(github.SOURCES))
        for source in registries.SOURCES:
            self.assertTrue((REPO / f"docs/openapi-surface/witness-search-{source}/records.tsv").is_file(), source)

    def test_committed_outstanding_inventory_matches_its_ledgers(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(REPO / "tools/witness-search/witness-search-registries-index.py"), "--check"],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=120,
            encoding="utf-8",
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        spec = importlib.util.spec_from_file_location(
            "registries_index", REPO / "tools/witness-search/witness-search-registries-index.py"
        )
        assert spec is not None and spec.loader is not None
        index = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(index)
        readme = (REPO / "docs/openapi-surface/witness-search-registries/README.md").read_text(encoding="utf-8")
        section = readme.partition("## Outstanding items")[2].partition("\n## ")[0]
        self.assertEqual(tuple(re.findall(r"^- `([a-z-]+)`:", section, re.MULTILINE)), index.KINDS)

    def test_key_derivation_reads_current_region_tables(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(KEYS)],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=30,
            encoding="utf-8",
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        rows = list(csv.DictReader(io.StringIO(completed.stdout), dialect="excel-tab"))
        self.assertEqual(len(rows), 68)
        self.assertEqual(len({row["key"] for row in rows}), 68)
        self.assertNotIn("request-body-string-map", {row["key"] for row in rows})
        self.assertEqual(
            [row["key"] for row in rows if row["census_status"] == "unsupported-by-census"],
            [],
        )
        self.assertEqual(completed.stdout, TRACKED_KEYS.read_text(encoding="utf-8"))

    def test_key_derivation_rejects_invalid_region_rows(self) -> None:
        valid = "| `shape-a` | x | x | `gap` | census `schema.items` | x | x | FIXTURE |\n"
        invalid = {
            "no FIXTURE gap rows": "",
            "has no selector": "| `shape-a` | x | x | `gap` | no selector | x | x | FIXTURE |\n",
            "duplicate gap key": valid + valid,
            "handwritten shape-b has no selector in witness-search-keys.tsv": valid
            + "| `shape-b` | x | x | `handwritten` | handwritten: shape-b-fixture; search: exhausted"
            " ([record](schemas.md#witness-search-exhaustive)) |  |  |  |\n",
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for region in (
                "document-paths.md",
                "parameters.md",
                "bodies-media.md",
                "schemas.md",
                "security.md",
                "oas31-extensions.md",
            ):
                (root / region).write_text("", encoding="utf-8", newline="\n")
            for expected, contents in invalid.items():
                with self.subTest(expected=expected):
                    (root / "schemas.md").write_text(contents, encoding="utf-8", newline="\n")
                    completed = subprocess.run(
                        [sys.executable, str(KEYS), "--regions-dir", str(root)],
                        cwd=REPO,
                        capture_output=True,
                        text=True,
                        timeout=30,
                        encoding="utf-8",
                    )
                    self.assertEqual(completed.returncode, 1)
                    self.assertIn(expected, completed.stderr)
                    self.assertIn("repair the FIXTURE gap rows", completed.stderr)

    def test_key_derivation_keeps_a_handwritten_row_with_its_tracked_selector(self) -> None:
        """A row a hand-written fixture moved out of `gap` stays in the searched key set.

        Its evidence cell names fixtures and a search rather than a selector, so
        the selector is the one the tracked file already records for the key.
        """
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for region in (
                "document-paths.md",
                "parameters.md",
                "bodies-media.md",
                "security.md",
                "oas31-extensions.md",
            ):
                (root / region).write_text("", encoding="utf-8", newline="\n")
            (root / "schemas.md").write_text(
                "| `shape-a` | x | x | `gap` | census `schema.items` | x | x | FIXTURE |\n"
                "| `shape-b` | x | x | `handwritten` | handwritten: shape-b-fixture; search: exhausted"
                " ([record](schemas.md#witness-search-exhaustive)) |  |  |  |\n"
                "| `shape-c` | x | x | `golden` | census `schema.oneOf` | x |  |  |\n",
                encoding="utf-8",
                newline="\n",
            )
            (root / "witness-search-keys.tsv").write_text(
                "key\tselector\tregion\tcensus_status\n"
                "shape-a\tschema.items\tschemas.md\tsupported\n"
                "shape-b\tschema.items>schema.discriminator:inheritance-union\tschemas.md\tsupported\n",
                encoding="utf-8",
                newline="\n",
            )
            completed = subprocess.run(
                [sys.executable, str(KEYS), "--regions-dir", str(root)],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(
                completed.stdout,
                (root / "witness-search-keys.tsv").read_text(encoding="utf-8"),
                "the derivation dropped the handwritten row or changed its selector",
            )
            (root / "witness-search-keys.tsv").write_text(
                "name\tshape\nshape-b\tschema.items\n", encoding="utf-8", newline="\n"
            )
            refused = subprocess.run(
                [sys.executable, str(KEYS), "--regions-dir", str(root)],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(refused.returncode, 1)
            self.assertIn("has no `key` and `selector` columns", refused.stderr)

    def test_local_census_rejects_incomplete_tsv_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            contract = root / "keys.tsv"
            contract.write_text("key\tselector\nshape-a\tschema.items\n", encoding="utf-8", newline="\n")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--contract",
                    str(contract),
                    "--documents",
                    f"local={root}",
                    "--all-documents-jsonl",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 2)
            self.assertIn("requires key, selector, and census_status", completed.stderr)
            self.assertIn("pass a readable key/selector contract", completed.stderr)

    def test_guarded_acquisition_waits_for_cap_and_records_refusal(self) -> None:
        state = {"reads": 0, "downloads": 0, "authorized": False}

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == "/rate_limit":
                    state["reads"] += 1
                    used = 71 if state["reads"] == 1 else 0
                    body = json.dumps(
                        {
                            "resources": {
                                "core": {
                                    "limit": 100,
                                    "used": used,
                                    "remaining": 100 - used,
                                    "reset": int(time.time()),
                                }
                            }
                        }
                    ).encode("utf-8")
                    self.send_response(200)
                elif self.path == "/tree.tar.gz":
                    state["downloads"] += 1
                    state["authorized"] = self.headers.get("Authorization") == "Bearer local-test-token"
                    body = b"real local tree archive bytes"
                    self.send_response(200)
                    self.send_header("x-ratelimit-resource", "core")
                elif self.path == "/transport":
                    self.connection.close()
                    return
                else:
                    body = b"Forbidden"
                    self.send_response(403)
                    self.send_header("x-ratelimit-resource", "core")
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            url = f"http://127.0.0.1:{server.server_port}"
            env = {**os.environ, "CROZIER_GITHUB_API_URL": url, "GITHUB_TOKEN": "local-test-token"}
            evidence = root / "evidence"
            output = root / "tree.tar.gz"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(GITHUB_ACQUIRE),
                    f"{url}/tree.tar.gz",
                    str(output),
                    "--evidence-dir",
                    str(evidence),
                ],
                cwd=REPO,
                env=env,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(output.read_bytes(), b"real local tree archive bytes")
            self.assertGreaterEqual(state["reads"], 2)
            self.assertEqual(state["downloads"], 1)
            self.assertTrue(state["authorized"])
            waits = [
                json.loads(line)
                for line in (evidence / "rate-limit-waits.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertTrue(
                any(row["kind"] == "wait" and row["cause"] == "cap" and row["bucket"] == "core" for row in waits)
            )
            self.assertTrue(any(row["kind"] == "probe" and row["reading"]["used"] == 71 for row in waits))
            refused = subprocess.run(
                [
                    sys.executable,
                    str(GITHUB_ACQUIRE),
                    f"{url}/forbidden",
                    str(root / "missing"),
                    "--evidence-dir",
                    str(evidence),
                ],
                cwd=REPO,
                env=env,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(refused.returncode, 1)
            records = [
                json.loads(line) for line in (evidence / "acquisitions.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual([row["status"] for row in records], [200, 403])
            self.assertFalse((root / "missing").exists())
            transport = subprocess.run(
                [
                    sys.executable,
                    str(GITHUB_ACQUIRE),
                    f"{url}/transport",
                    str(root / "missing"),
                    "--evidence-dir",
                    str(evidence),
                ],
                cwd=REPO,
                env=env,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(transport.returncode, 1)
            self.assertIn("transport error", transport.stderr)
            records = [
                json.loads(line) for line in (evidence / "acquisitions.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertNotIn("status", records[-1])
            self.assertTrue(records[-1]["error"])
            invalid_bucket = subprocess.run(
                [
                    sys.executable,
                    str(GITHUB_ACQUIRE),
                    f"{url}/tree.tar.gz",
                    str(root / "invalid"),
                    "--evidence-dir",
                    str(evidence),
                    "--bucket",
                    "graphql",
                ],
                cwd=REPO,
                env=env,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(invalid_bucket.returncode, 2)
            self.assertIn("invalid choice", invalid_bucket.stderr)
            # The CLI's choices are the guard's covered buckets, not a copy of them.
            offered = re.search(r"choose from (.*?)\)", invalid_bucket.stderr)
            assert offered is not None, invalid_bucket.stderr
            self.assertEqual(set(re.findall(r"'?([a-z_]+)'?", offered[1])), set(load_rate_limit_guard().GITHUB_BUCKETS))
            self.assertFalse((root / "invalid").exists())

            probe_failure = subprocess.run(
                [
                    sys.executable,
                    str(GITHUB_ACQUIRE),
                    f"{url}/tree.tar.gz",
                    str(root / "unprobed"),
                    "--evidence-dir",
                    str(evidence),
                ],
                cwd=REPO,
                env={**env, "CROZIER_GITHUB_API_URL": f"{url}/missing"},
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(probe_failure.returncode, 1)
            self.assertIn("rate-limit guard refused acquisition", probe_failure.stderr)
            self.assertFalse((root / "unprobed").exists())
            self.assertEqual(state["downloads"], 1)

    def test_a_redirect_is_followed_only_to_an_allowed_url_and_never_carries_the_token_across_hosts(self) -> None:
        landed: list[str | None] = []
        redirect_rate_limit = threading.Event()

        class Handler(BaseHTTPRequestHandler):
            server: ThreadingHTTPServer

            def do_GET(self):
                port = self.server.server_port
                if self.path == "/rate_limit" and redirect_rate_limit.is_set():
                    self.redirect("http://example.invalid/rate_limit")
                elif self.path == "/rate_limit":
                    self.reply(
                        json.dumps(
                            {
                                "resources": {
                                    "core": {
                                        "limit": 100,
                                        "used": 0,
                                        "remaining": 100,
                                        "reset": int(time.time()) + 60,
                                    }
                                }
                            }
                        ).encode()
                    )
                elif self.path == "/away.tar.gz":
                    self.redirect("http://example.invalid/tree.tar.gz")
                elif self.path == "/same-host.tar.gz":
                    self.redirect("/landing.tar.gz")
                elif self.path == "/other-host.tar.gz":
                    self.redirect(f"http://localhost:{port}/landing.tar.gz")
                elif self.path == "/landing.tar.gz":
                    landed.append(self.headers.get("Authorization"))
                    self.reply(b"tree bytes")

            def redirect(self, location: str) -> None:
                self.send_response(302)
                self.send_header("Location", location)
                self.send_header("Content-Length", "0")
                self.end_headers()

            def reply(self, body: bytes) -> None:
                self.send_response(200)
                self.send_header("x-ratelimit-resource", "core")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        env = {**os.environ, "CROZIER_GITHUB_API_URL": url, "GITHUB_TOKEN": "local-test-token"}

        def acquire(root: Path, path: str) -> subprocess.CompletedProcess[str]:
            return subprocess.run(
                [
                    sys.executable,
                    str(GITHUB_ACQUIRE),
                    f"{url}{path}",
                    str(root / "tree.tar.gz"),
                    "--evidence-dir",
                    str(root / "evidence"),
                ],
                cwd=REPO,
                env=env,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            # A redirect within the API host keeps the token; one to another host drops it.
            for path, token in (("/same-host.tar.gz", "Bearer local-test-token"), ("/other-host.tar.gz", None)):
                with self.subTest(path):
                    landed.clear()
                    completed = acquire(root, path)
                    self.assertEqual(completed.returncode, 0, completed.stderr)
                    self.assertEqual(b"tree bytes", (root / "tree.tar.gz").read_bytes())
                    self.assertEqual(landed, [token])
            # A redirect to a host no download may reach is refused, and nothing is saved.
            (root / "tree.tar.gz").unlink()
            refused = acquire(root, "/away.tar.gz")
            self.assertEqual(refused.returncode, 1, refused.stderr)
            self.assertIn("redirect to http://example.invalid/tree.tar.gz refused", refused.stderr)
            self.assertIn("retry the recorded source when available", refused.stderr)
            self.assertFalse((root / "tree.tar.gz").exists())
            # The guard's own rate-limit read is held to the API host the same way.
            redirect_rate_limit.set()
            guarded = acquire(root, "/same-host.tar.gz")
            self.assertEqual(guarded.returncode, 1, guarded.stderr)
            self.assertIn("redirect to http://example.invalid/rate_limit refused", guarded.stderr)
            self.assertFalse((root / "tree.tar.gz").exists())

    def test_guarded_acquisition_succeeds_only_once_the_transfer_completes(self) -> None:
        served: list[str] = []

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                served.append(self.path)
                if self.path == "/rate_limit":
                    body = json.dumps(
                        {
                            "resources": {
                                "core": {
                                    "limit": 100,
                                    "used": 0,
                                    "remaining": 100,
                                    "reset": int(time.time()) + 60,
                                }
                            }
                        }
                    ).encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                    return
                self.send_response(200)
                if self.path == "/truncated.tar.gz":
                    # The status line and headers promise 1000 bytes; the
                    # connection drops after 10.
                    self.send_header("x-ratelimit-resource", "core")
                    self.send_header("Content-Length", "1000")
                    self.end_headers()
                    self.wfile.write(b"0123456789")
                    self.wfile.flush()
                    self.close_connection = True
                    return
                body = b"real local tree archive bytes"
                # A 200 the guard refuses after the body is written: it was
                # spent in a bucket other than the one acquired.
                bucket = "search" if self.path == "/other-bucket.tar.gz" else "core"
                self.send_header("x-ratelimit-resource", bucket)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format: str, *_args: Any) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        env = {**os.environ, "CROZIER_GITHUB_API_URL": url, "GITHUB_TOKEN": "local-test-token"}

        def acquire(root: Path, path: str, output: Path, **overrides: str) -> subprocess.CompletedProcess[str]:
            return subprocess.run(
                [
                    sys.executable,
                    str(GITHUB_ACQUIRE),
                    path if "://" in path else f"{url}{path}",
                    str(output),
                    "--evidence-dir",
                    str(root / "evidence"),
                ],
                cwd=REPO,
                env={**env, **overrides},
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=30,
            )

        def records(root: Path, name: str) -> list[dict]:
            return [json.loads(line) for line in (root / "evidence" / name).read_text().splitlines()]

        cases = [
            ("interrupted transfer", "/truncated.tar.gz", "IncompleteRead"),
            ("bucket refused after the body", "/other-bucket.tar.gz", "spent in 'search'"),
            ("publication fails", "/tree.tar.gz", "could not publish"),
        ]
        if Path("/dev/full").exists():
            cases.append(("destination write fails", "/tree.tar.gz", "No space left on device"))
        for name, path, error in cases:
            with self.subTest(name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                output = root / "tree.tar.gz"
                partial = root / "tree.tar.gz.part"
                if name == "destination write fails":
                    # Every write to the staging file fails as a full disk does.
                    partial.symlink_to("/dev/full")
                if name == "publication fails":
                    # A directory where the file is published: every byte arrives, the rename cannot land.
                    output.mkdir()
                    (output / "occupied").write_text("", encoding="utf-8")
                completed = acquire(root, path, output)
                self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
                self.assertNotIn("Traceback", completed.stderr)
                self.assertNotIn("saved", completed.stdout)
                self.assertIn(error, completed.stderr)
                self.assertIn("retry the recorded source when available", completed.stderr)
                # Nothing is published: the destination is as it was before the run.
                self.assertTrue(output.is_dir() if name == "publication fails" else not os.path.lexists(output))
                self.assertFalse(os.path.lexists(partial))
                [record] = records(root, "acquisitions.jsonl")
                self.assertEqual(record["status"], 200)
                self.assertIn(error, record["error"])
                self.assertNotIn("bytes", record)
                self.assertNotIn("sha256", record)
                # The reservation was closed: the next acquisition on the same
                # evidence runs, and a complete transfer still succeeds.
                again = acquire(root, "/tree.tar.gz", root / "again.tar.gz")
                self.assertEqual(again.returncode, 0, again.stderr)
                self.assertEqual((root / "again.tar.gz").read_bytes(), b"real local tree archive bytes")

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            served.clear()
            for target, overrides, message in (
                (
                    "http://example.invalid/tree.tar.gz",
                    {},
                    "must be an https:// URL on api.github.com, codeload.github.com, raw.githubusercontent.com",
                ),
                ("https://example.invalid/tree.tar.gz", {}, "must be an https:// URL on"),
                ("file:///etc/passwd", {}, "must be an https:// URL on"),
                (
                    "/tree.tar.gz",
                    {"CROZIER_GITHUB_API_URL": "http://example.invalid"},
                    "CROZIER_GITHUB_API_URL must use https://api.github.com or a loopback HTTP URL",
                ),
                # A port that names no TCP port is refused here, not by the HTTP client later.
                ("http://127.0.0.1:bogus/tree.tar.gz", {}, "must be an https:// URL on"),
                ("http://127.0.0.1:99999/tree.tar.gz", {}, "must be an https:// URL on"),
                (
                    "/tree.tar.gz",
                    {"CROZIER_GITHUB_API_URL": "http://127.0.0.1:0"},
                    "CROZIER_GITHUB_API_URL must use https://api.github.com or a loopback HTTP URL",
                ),
            ):
                with self.subTest(target=target, overrides=overrides):
                    refused = acquire(root, target, root / "refused", **overrides)
                    self.assertEqual(refused.returncode, 2, refused.stdout + refused.stderr)
                    self.assertIn(message, refused.stderr)
                    self.assertNotIn("local-test-token", refused.stdout + refused.stderr)
                    self.assertFalse((root / "refused").exists())
            # Refused before the guard read a bucket or anything was fetched.
            self.assertEqual(served, [])
            self.assertFalse((root / "evidence").exists())

    def test_all_documents_tsv_names_unreadable_document(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            documents = root / "documents"
            documents.mkdir()
            (documents / "broken.json").write_text('{"openapi":', encoding="utf-8", newline="\n")
            contract = root / "keys.md"
            contract.write_text(
                "| key | selector |\n|---|---|\n"
                "| `array` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf` |\n",
                encoding="utf-8",
                newline="\n",
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--contract",
                    str(contract),
                    "--documents",
                    f"local={documents}",
                    "--all-documents",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 1)
            rows = list(csv.DictReader(io.StringIO(completed.stdout), dialect="excel-tab"))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["document"], "broken.json")
            self.assertTrue(rows[0]["count"].startswith("parse-failure: "))
            self.assertIn("broken.json", completed.stderr)

    def test_real_tree_reports_zeroes_and_declarations_per_document(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            documents = root / "documents"
            documents.mkdir()
            contract = root / "keys.md"
            contract.write_text(
                "| key | selector |\n|---|---|\n"
                "| `array` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf` |\n",
                encoding="utf-8",
                newline="\n",
            )
            hit = json.dumps(
                {
                    "openapi": "3.0.0",
                    "info": {"title": "hit", "version": "1"},
                    "paths": {},
                    "components": {
                        "schemas": {"Shape": {"oneOf": [{"type": "array", "items": {"anyOf": [{"type": "string"}]}}]}}
                    },
                }
            ).encode("utf-8")
            miss = json.dumps(
                {
                    "openapi": "3.0.0",
                    "info": {"title": "miss", "version": "1"},
                    "paths": {},
                    "components": {"schemas": {"Shape": {"type": "string"}}},
                }
            ).encode("utf-8")
            (documents / "hit.json").write_bytes(hit)
            (documents / "hit.yaml").write_bytes(hit)
            (documents / "miss.json").write_bytes(miss)
            (documents / "metadata.json").write_text(
                json.dumps({"bundle": json.loads(hit)}), encoding="utf-8", newline="\n"
            )
            (documents / "notes.yaml").write_text("title: no OpenAPI document\n", encoding="utf-8", newline="\n")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--contract",
                    str(contract),
                    "--documents",
                    f"local={documents}",
                    "--all-documents",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = list(csv.DictReader(io.StringIO(completed.stdout), dialect="excel-tab"))
            self.assertEqual(len(rows), 5)
            by_name = {row["document"]: row for row in rows}
            self.assertEqual(by_name["hit.json"]["count"], "1")
            self.assertEqual(by_name["hit.yaml"]["count"], "1")
            self.assertEqual(by_name["miss.json"]["count"], "0")
            self.assertEqual(by_name["metadata.json"]["count"], "0")
            self.assertEqual(by_name["metadata.json"]["openapi_version"], "")
            self.assertEqual(by_name["notes.yaml"]["count"], "0")
            self.assertEqual(by_name["hit.json"]["sha256"], hashlib.sha256(hit).hexdigest())
            self.assertEqual(by_name["miss.json"]["sha256"], hashlib.sha256(miss).hexdigest())
            compact = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--contract",
                    str(contract),
                    "--documents",
                    f"local={documents}",
                    "--all-documents-jsonl",
                    "--progress-log",
                    str(root / "progress.jsonl"),
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(compact.returncode, 0, compact.stderr)
            objects = [json.loads(line) for line in compact.stdout.splitlines()]
            self.assertEqual(len(objects), 5)
            self.assertEqual({row["document"]: row["loader"] for row in objects}["notes.yaml"], "")
            self.assertEqual(
                {row["document"]: row["selectors"]["array"] for row in objects},
                {"hit.json": 1, "hit.yaml": 1, "miss.json": 0, "metadata.json": 0, "notes.yaml": 0},
            )
            progress = [json.loads(line) for line in (root / "progress.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(len(progress), 10)
            self.assertEqual(
                {name: sum(row["event"] == name for row in progress) for name in ("start", "end")},
                {"start": 5, "end": 5},
            )
            resumed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--contract",
                    str(contract),
                    "--documents",
                    f"local={documents}",
                    "--all-documents-jsonl",
                    "--start-after",
                    "miss.json",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(resumed.returncode, 0, resumed.stderr)
            self.assertEqual(
                [json.loads(line)["document"] for line in resumed.stdout.splitlines()],
                ["notes.yaml"],
            )

            derived = root / "region-keys.tsv"
            derived.write_text(
                "key\tselector\tregion\tcensus_status\n"
                "array\tschema.oneOf>schema.type:primary=array&schema.items>schema.anyOf\t"
                "schemas.md\tsupported\n"
                "pending\tsecurityScheme:$ref\tsecurity.md\tunsupported-by-census\n",
                encoding="utf-8",
                newline="\n",
            )
            from_regions = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--contract",
                    str(derived),
                    "--documents",
                    f"local={documents}",
                    "--all-documents-jsonl",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(from_regions.returncode, 0, from_regions.stderr)
            derived_rows = [json.loads(line) for line in from_regions.stdout.splitlines()]
            self.assertEqual(
                {row["document"]: row["selectors"] for row in derived_rows},
                {
                    "hit.json": {"array": 1},
                    "hit.yaml": {"array": 1},
                    "miss.json": {"array": 0},
                    "metadata.json": {"array": 0},
                    "notes.yaml": {"array": 0},
                },
            )

    def test_predicate_selector_counts_once_per_declaration_site(self) -> None:
        """A predicate is recorded by the walk alone, never again as a conjunction."""
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            documents = root / "documents"
            documents.mkdir()
            contract = root / "keys.tsv"
            contract.write_text(
                "key\tselector\tregion\tcensus_status\n"
                "securityscheme-ref\tsecurityScheme:$ref\tsecurity.md\tsupported\n",
                encoding="utf-8",
                newline="\n",
            )
            scheme = {"type": "http", "scheme": "bearer"}
            (documents / "two.json").write_text(
                json.dumps(
                    {
                        "openapi": "3.0.3",
                        "info": {"title": "two", "version": "1"},
                        "paths": {},
                        "components": {
                            "securitySchemes": {
                                "real": scheme,
                                "a": {"$ref": "#/components/securitySchemes/real"},
                                "b": {"$ref": "#/components/securitySchemes/real"},
                            }
                        },
                    }
                ),
                encoding="utf-8",
                newline="\n",
            )
            (documents / "inline.json").write_text(
                json.dumps(
                    {
                        "openapi": "3.0.3",
                        "info": {"title": "inline", "version": "1"},
                        "paths": {},
                        "components": {"securitySchemes": {"real": scheme}},
                    }
                ),
                encoding="utf-8",
                newline="\n",
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--contract",
                    str(contract),
                    "--documents",
                    f"local={documents}",
                    "--all-documents-jsonl",
                ],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=30,
                encoding="utf-8",
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(
                {
                    row["document"]: row["selectors"]["securityscheme-ref"]
                    for row in map(json.loads, completed.stdout.splitlines())
                },
                {"two.json": 2, "inline.json": 0},
            )


class SecuritySchemeRefCensusReadmeTest(unittest.TestCase):
    """The registries README's securityscheme-ref counts are the census archives' own."""

    SOURCES = (("apis.guru", "APIs.guru"), ("jentic", "jentic"), ("vendor-portals", "the vendor portals"))

    def test_readme_counts_are_derived_from_each_sources_census(self) -> None:
        root = REPO / "docs/openapi-surface"
        readme = " ".join((root / "witness-search-registries/README.md").read_text(encoding="utf-8").split())
        rows, parsed, unreadable = {}, {}, {}
        for source, _ in self.SOURCES:
            with gzip.open(
                root / f"witness-search-{source}/securityscheme-ref-census.tsv.gz", "rt", encoding="utf-8", newline=""
            ) as stream:
                census = list(csv.DictReader(stream, delimiter="\t"))
            with (root / f"witness-search-{source}/enumeration.tsv").open(encoding="utf-8", newline="") as stream:
                enumerated = list(csv.DictReader(stream, delimiter="\t"))
            with self.subTest(source=source):
                self.assertEqual(
                    sorted(row["sha256"] for row in enumerated),
                    sorted(row["sha256"] for row in census),
                )
                declared = [
                    row for row in census if row["classification"] == "openapi-3" and row["securityscheme-ref"] != "0"
                ]
                self.assertEqual([], declared)
                self.assertEqual(
                    sorted(row["sha256"] for row in census if row["classification"] == "unreadable"),
                    sorted(row["sha256"] for row in enumerated if row["status"].startswith("unreadable")),
                )
            rows[source] = len(census)
            parsed[source] = sum(row["classification"] == "openapi-3" for row in census)
            unreadable[source] = sum(row["classification"] == "unreadable" for row in census)
        (first, first_name), (second, second_name), (third, third_name) = self.SOURCES
        self.assertIn(
            f"The counts are {rows[first]:,} rows for {first_name}, {rows[second]:,} for"
            f" {second_name} and {rows[third]:,} for {third_name}.",
            readme,
        )
        self.assertIn(
            f"That covers {parsed[first]:,} OpenAPI 3 documents in {first_name},"
            f" {parsed[second]:,} in {second_name} and {parsed[third]:,} in {third_name}.",
            readme,
        )
        self.assertEqual(0, unreadable[first] + unreadable[second])
        self.assertIn(
            f"The {unreadable[third]} portal files whose `enumeration.tsv` status is already `unreadable`", readme
        )


if __name__ == "__main__":
    unittest.main()
