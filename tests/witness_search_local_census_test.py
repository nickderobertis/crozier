#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] This Cargo crate has no Nx graph; this subprocess and loopback-server suite is wired into just test-witness-search-acquisition and the deterministic check gate.
"""End-to-end coverage of complete local-tree selector evidence."""

from __future__ import annotations

import csv
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import io
import json
import os
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts/witness-search-local-census.py"
GITHUB_ACQUIRE = REPO / "scripts/witness-acquire-github.py"
KEYS = REPO / "scripts/witness-search-region-keys.py"
TRACKED_KEYS = REPO / "docs/openapi-surface/witness-search-keys.tsv"
POSTMAN = REPO / "scripts/witness-search-postman.py"
PORTAL_TREES = REPO / "scripts/witness-search-portal-trees.py"


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
        )
        (documents / "broken.yaml").write_text(
            "? openapi\n: [unterminated\n", encoding="utf-8"
        )
        contract = root / "keys.md"
        contract.write_text(
            "| key | selector |\n|---|---|\n| `array` | `schema.items` |\n",
            encoding="utf-8",
        )
        completed = subprocess.run(
            [sys.executable, *interpreter_flags, str(SCRIPT),
             "--contract", str(contract),
             "--documents", f"local={documents}", "--all-documents-jsonl"],
            cwd=REPO, capture_output=True, text=True, timeout=30,
        )
        return completed.returncode, {
            row["document"]: row
            for row in map(json.loads, completed.stdout.splitlines())
        }


def pyyaml_importable(interpreter_flags: list[str]) -> bool:
    return subprocess.run(
        [sys.executable, *interpreter_flags, "-c", "import yaml"],
        capture_output=True, timeout=30,
    ).returncode == 0


class LocalCensusTest(unittest.TestCase):
    def test_explicit_yaml_mapping_key_uses_optional_parser(self) -> None:
        if not pyyaml_importable([]):
            self.skipTest("PyYAML is not installed for this interpreter")
        returncode, rows = run_explicit_key_census([])
        self.assertEqual(returncode, 1)
        self.assertGreater(rows["hit.yaml"]["selectors"]["array"], 0)
        self.assertIn("PyYAML", rows["hit.yaml"]["loader"])
        self.assertEqual(rows["broken.yaml"]["classification"], "unreadable")
        self.assertIn("PyYAML parse failure", rows["broken.yaml"]["error"])

    def test_explicit_yaml_mapping_key_without_pyyaml_is_unreadable(self) -> None:
        # `-S` drops site-packages, which is where an installed PyYAML lives;
        # the census scripts themselves are stdlib-only.
        if pyyaml_importable(["-S"]):
            self.skipTest("PyYAML is importable even without site-packages")
        returncode, rows = run_explicit_key_census(["-S"])
        self.assertEqual(returncode, 1)
        for document in ("hit.yaml", "broken.yaml"):
            self.assertEqual(rows[document]["classification"], "unreadable")
            self.assertEqual(rows[document]["loader"], "stdlib-census-yaml")
            self.assertNotIn("selectors", rows[document])
            self.assertNotIn("PyYAML", rows[document]["error"])

    def test_invalid_json_is_recorded_as_a_parse_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "broken.json").write_text(
                '{"openapi":"3.0.0","paths":{},}', encoding="utf-8"
            )
            contract = root / "keys.md"
            contract.write_text(
                "| key | selector |\n|---|---|\n| `array` | `schema.items` |\n",
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--contract", str(contract),
                 "--documents", f"local={root}", "--all-documents-jsonl"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(completed.returncode, 1)
            record = json.loads(completed.stdout)
            self.assertEqual(record["classification"], "unreadable")
            self.assertEqual(record["loader"], "stdlib-json")
            self.assertIn("trailing comma at", record["error"])

    def test_other_json_decode_failure_is_unreadable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "broken.json").write_text('{"openapi":', encoding="utf-8")
            contract = root / "keys.md"
            contract.write_text(
                "| key | selector |\n|---|---|\n| `array` | `schema.items` |\n",
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--contract", str(contract),
                 "--documents", f"local={root}", "--all-documents-jsonl"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
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
            (source / "openapi.json").write_text('{"openapi":"3.0.0"}', encoding="utf-8")
            (source / "notes.txt").write_text("not a spec", encoding="utf-8")
            pin = "a" * 40
            with tarfile.open(archives / "example--api.tar.gz", "w:gz") as archive:
                for path in source.iterdir():
                    archive.add(path, arcname=f"api-{pin}/{path.name}")
            plan = root / "plan.tsv"
            plan.write_text(
                "repository\tpinned_ref\nexample/api\t" + pin +
                "\nmutable/api\tmain\n", encoding="utf-8",
            )
            tree = root / "tree"
            manifest = root / "manifest.tsv"
            completed = subprocess.run(
                [sys.executable, str(PORTAL_TREES), "--plan", str(plan),
                 "--archives", str(archives), "--tree", str(tree),
                 "--manifest", str(manifest)],
                cwd=REPO, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual((tree / "example--api/openapi.json").read_bytes(),
                             (source / "openapi.json").read_bytes())
            self.assertFalse((tree / "example--api/notes.txt").exists())
            self.assertFalse((tree / "mutable--api").exists())
            with manifest.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle, dialect="excel-tab"))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["path"], "openapi.json")
            self.assertEqual(rows[0]["sha256"], hashlib.sha256(
                (source / "openapi.json").read_bytes()).hexdigest())

    def test_portal_archive_refusals_name_a_repair(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            archives = root / "archives"
            archives.mkdir()
            tree = root / "tree"
            manifest = root / "manifest.tsv"
            plan = root / "plan.tsv"
            command = [sys.executable, str(PORTAL_TREES), "--plan", str(plan),
                       "--archives", str(archives), "--tree", str(tree),
                       "--manifest", str(manifest)]
            plan.write_text("wrong\theader\n", encoding="utf-8")
            malformed = subprocess.run(command, cwd=REPO, capture_output=True,
                                       text=True, timeout=30)
            self.assertEqual(malformed.returncode, 1)
            self.assertIn("repository and pinned_ref columns", malformed.stderr)
            plan.write_text("repository\tpinned_ref\nexample/api\t" + "a" * 40 + "\n",
                            encoding="utf-8")
            missing = subprocess.run(command, cwd=REPO, capture_output=True,
                                     text=True, timeout=30)
            self.assertEqual(missing.returncode, 1)
            self.assertIn("missing pinned archive", missing.stderr)
            archive = archives / "example--api.tar.gz"
            with tarfile.open(archive, "w:gz") as handle:
                body = b'{"openapi":"3.0.0"}'
                info = tarfile.TarInfo("api-" + "a" * 40 + "/../escape.json")
                info.size = len(body)
                handle.addfile(info, io.BytesIO(body))
            unsafe = subprocess.run(command, cwd=REPO, capture_output=True,
                                    text=True, timeout=30)
            self.assertEqual(unsafe.returncode, 1)
            self.assertIn("unsafe archive path", unsafe.stderr)
            self.assertFalse(manifest.exists())

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
                    payload = json.dumps({"data": {}, "meta": {"total": {"api": 0}}}).encode()
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, *_args):
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
                "key\tselector\narray-item\tschema.items\n"
                "oauth2-password\tsecurityScheme.flows.password\n", encoding="utf-8",
            )
            evidence = root / "postman"
            completed = subprocess.run(
                [sys.executable, str(POSTMAN), "--keys", str(keys),
                 "--evidence-dir", str(evidence),
                 "--url", f"http://127.0.0.1:{server.server_port}/proxy"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = [json.loads(line) for line in
                    (evidence / "queries.jsonl").read_text().splitlines()]
            self.assertEqual(len(rows), 12)
            self.assertNotEqual(rows[0]["query"], rows[3]["query"])
            self.assertEqual(rows[0]["classification"], "source-refused")
            self.assertEqual(rows[0]["status"], 403)
            self.assertNotIn("totals", rows[0])
            self.assertEqual(rows[1]["classification"], "answered")
            self.assertEqual(rows[1]["totals"]["api"], 0)
            self.assertEqual(rows[9]["query"], "oauth2 password flows")
            self.assertEqual({x["body"]["queryIndices"][0] for x in received}, {
                "apinetwork.team", "runtime.collection", "adp.api"})
            self.assertTrue(all(len(x["body"]["queryIndices"]) == 1 for x in received))
            waits = [json.loads(line) for line in
                     (evidence / "rate-limit-waits.jsonl").read_text().splitlines()]
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
                    payload = json.dumps({"data": {}, "meta": {"total": {
                        "team": count, "collection": 0, "api": 0,
                    }}}).encode()
                    self.send_response(200)
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8")
            evidence = root / "postman"
            completed = subprocess.run(
                [sys.executable, str(POSTMAN), "--keys", str(keys),
                 "--evidence-dir", str(evidence),
                 "--url", f"http://127.0.0.1:{server.server_port}/proxy"],
                cwd=REPO, capture_output=True, text=True, timeout=50,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = [json.loads(line) for line in
                    (evidence / "queries.jsonl").read_text().splitlines()]
            self.assertEqual(rows[0]["classification"], "source-refused")
            self.assertEqual(rows[0]["status"], 429)
            self.assertEqual(rows[1]["classification"], "answered")
            self.assertIn(25, [row["offset"] for row in rows])
            waits = [json.loads(line) for line in
                     (evidence / "rate-limit-waits.jsonl").read_text().splitlines()]
            self.assertTrue(any(row["cause"] == "backoff" for row in waits))

    def test_postman_malformed_answer_is_source_error(self) -> None:
        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):
                self.rfile.read(int(self.headers["Content-Length"]))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"meta":{}}')

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8")
            evidence = root / "postman"
            completed = subprocess.run(
                [sys.executable, str(POSTMAN), "--keys", str(keys),
                 "--evidence-dir", str(evidence),
                 "--url", f"http://127.0.0.1:{server.server_port}/proxy"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = [json.loads(line) for line in
                    (evidence / "queries.jsonl").read_text().splitlines()]
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
                self.wfile.write(json.dumps({"data": {}, "meta": {"total": {
                    "team": 0, "collection": 0, "api": 0,
                }}}).encode())

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8")
            evidence = root / "postman"
            completed = subprocess.run(
                [sys.executable, str(POSTMAN), "--keys", str(keys),
                 "--evidence-dir", str(evidence),
                 "--url", f"http://127.0.0.1:{server.server_port}/proxy"],
                cwd=REPO, capture_output=True, text=True, timeout=40,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = [json.loads(line) for line in
                    (evidence / "queries.jsonl").read_text().splitlines()]
            self.assertEqual(rows[0]["classification"], "source-refused")
            self.assertIsNone(rows[0]["status"])
            self.assertTrue(rows[0]["response"])
            self.assertTrue(all(row["classification"] == "answered" for row in rows[1:]))

    def test_postman_missing_key_derivation_gives_repair_action(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            completed = subprocess.run(
                [sys.executable, str(POSTMAN), "--keys", str(root / "missing.tsv"),
                 "--evidence-dir", str(root / "evidence")],
                cwd=REPO, capture_output=True, text=True, timeout=30,
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

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            keys = root / "keys.tsv"
            keys.write_text("key\tselector\narray-item\tschema.items\n", encoding="utf-8")
            evidence = root / "postman"
            completed = subprocess.run(
                [sys.executable, str(POSTMAN), "--keys", str(keys),
                 "--evidence-dir", str(evidence),
                 "--url", f"http://127.0.0.1:{server.server_port}/proxy"],
                cwd=REPO, capture_output=True, text=True, timeout=180,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(len(received), 5)
            rows = [json.loads(line) for line in
                    (evidence / "queries.jsonl").read_text().splitlines()]
            # The fifth response closes the guard reservation by raising
            # SecondaryLimit, so the consumer records that refusal with its
            # query identity and error instead of a normal HTTP result row.
            self.assertEqual(len([row for row in rows if row.get("status") == 429]), 4)
            self.assertEqual(len([row for row in rows if row.get("error", "").startswith("postman")]), 6)
            self.assertTrue(all(row["classification"] == "source-refused" for row in rows))

    def test_postman_metadata_hits_are_acquired_and_classified_by_census(self) -> None:
        received = []
        throttled = []
        openapi = json.dumps({"openapi": "3.0.0", "info": {"title": "t", "version": "1"},
                              "paths": {}, "components": {"schemas": {
                                  "Shape": {"type": "array", "items": {"type": "string"}}}}}).encode()
        collection = json.dumps({"info": {"_postman_id": "c", "name": "array item",
                                          "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"},
                                 "item": []}).encode()

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

            def log_message(self, *_args):
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
            keys.write_text("key\tselector\nquery-says-nothing\tschema.items\n", encoding="utf-8")
            evidence = root / "postman"
            evidence.mkdir()
            # The query text shares no word with the shape; only the body can declare it.
            (evidence / "queries.jsonl").write_text(json.dumps({
                "key": "query-says-nothing", "query": "unrelated words", "status": 200,
                "data": {
                    "team": [{"document": {"id": 7, "publicHandle": "acme-team"}}],
                    "collection": [{"document": {"id": "1-openapi"}}],
                    "request": [{"document": {"id": "r", "collection": {"id": "2-coll"}}}],
                    "api": [{"document": {"id": "api-9"}}],
                }}) + "\n", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(POSTMAN), "--keys", str(keys), "--evidence-dir", str(evidence),
                 "--acquire-hits", "--web-base", base, "--api-base", base],
                cwd=REPO, capture_output=True, text=True, timeout=120,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            rows = {row["id"]: row for row in (json.loads(line) for line in
                    (evidence / "hit-access.jsonl").read_text().splitlines())}
            self.assertEqual(set(rows), {"7", "1-openapi", "2-coll", "api-9"})
            self.assertEqual(rows["1-openapi"]["classification"], "openapi-3")
            self.assertEqual(rows["1-openapi"]["selectors"], {"query-says-nothing": 1})
            self.assertEqual(rows["1-openapi"]["sha256"], hashlib.sha256(openapi).hexdigest())
            self.assertEqual(received.count("/collections/1-openapi"), 2)
            self.assertEqual(rows["2-coll"]["classification"], "not-openapi-3")
            self.assertEqual(rows["2-coll"]["document_kind"], "postman-collection")
            self.assertNotIn("selectors", rows["2-coll"])
            self.assertEqual(rows["7"]["classification"], "no-document-body")
            self.assertEqual((rows["api-9"]["status"], rows["api-9"]["classification"]),
                             (401, "source-refused"))
            waits = [json.loads(line) for line in
                     (evidence / "rate-limit-waits.jsonl").read_text().splitlines()]
            self.assertTrue(any(row["cause"] == "backoff" for row in waits))
            calls = (evidence / "rate-limit-calls.jsonl").read_text().splitlines()
            self.assertEqual(len(calls), len(received))

    def test_outstanding_items_are_derived_by_key_and_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "witness-search-keys.tsv").write_text(
                "key\tselector\tregion\tcensus_status\n"
                "shape-a\tschema.items\tschemas.md\tsupported\n"
                "scheme-ref\tsecurityScheme:$ref\tsecurity.md\tunsupported-by-census\n",
                encoding="utf-8")
            (root / "witness-search-portal-plan.tsv").write_text(
                "repository\tpinned_ref\tprior_path\tderivation\tacquisition\n"
                "gone/docs\tno-immutable-ref: HTTP 404\tapi.json\tprior\tsource-refused\n"
                "kept/docs\tabc\tapi.json\tprior\tarchive\n", encoding="utf-8")
            portals = root / "witness-search-vendor-portals"
            portals.mkdir()
            (portals / "records.tsv").write_text(
                "source\tkey\tcandidate\trevision\tdigest\tcensus\tlicence_screen\trevision_screen\t"
                "fern_screen\tdisposition\tevidence\n"
                "vendor-portals\tshape-a\tbig.json\tabc\td\t3\tpass\tpass\t"
                "not-run: Fern check timed out after 3600 seconds\toutstanding\tx\n"
                "vendor-portals\tshape-a\tok.json\tabc\td\t1\tpass\tpass\tpass\twitness-found\tx\n",
                encoding="utf-8")
            (portals / "enumeration.tsv").write_text(
                "walk\tdocument\trevision\tsha256\tmatched_keys\tstatus\n"
                "kept/docs\tbad.json\tabc\t" + "0" * 64 + "\t\tunreadable: trailing comma\n"
                "kept/docs\tok.json\tabc\t" + "1" * 64 + "\tshape-a\treadable\n", encoding="utf-8")
            postman = root / "witness-search-postman"
            postman.mkdir()
            (postman / "queries.jsonl").write_text(
                json.dumps({"key": "shape-a", "query": "shape a", "index": "apinetwork.team",
                            "offset": 225, "status": 400, "classification": "source-refused",
                            "taken_utc": "t", "response": "From value: 225"}) + "\n"
                + json.dumps({"key": "shape-a", "query": "shape a", "index": "adp.api",
                              "offset": 0, "status": 200, "classification": "answered",
                              "taken_utc": "t"}) + "\n", encoding="utf-8")
            (postman / "hit-access.jsonl").write_text("".join(json.dumps(row) + "\n" for row in (
                {"hit": "collection", "id": "c1", "keys": ["shape-a"], "status": 404,
                 "classification": "source-refused", "url": "u1",
                 "response": '{"message":"Link does not exist."}'},
                {"hit": "collection", "id": "c2", "keys": ["shape-a"], "status": 200,
                 "classification": "not-openapi-3", "url": "u2"},
                {"hit": "collection", "id": "c3", "keys": ["shape-a"], "status": 200,
                 "classification": "openapi-3", "url": "u3", "selectors": {"shape-a": 2}},
                {"hit": "api", "id": "a1", "keys": ["shape-a"], "status": 401,
                 "classification": "source-refused", "url": "u4", "response": "{}"},
            )), encoding="utf-8")
            (root / "witness-search-registries").mkdir()
            command = [sys.executable, str(REPO / "scripts/witness-search-registries-outstanding.py"),
                       "--root", str(root)]
            stale = subprocess.run([*command, "--check"], capture_output=True, text=True, timeout=30)
            self.assertEqual(stale.returncode, 1)
            self.assertIn("rerun without --check", stale.stderr)
            self.assertEqual(subprocess.run(command, timeout=30).returncode, 0)
            self.assertEqual(subprocess.run([*command, "--check"], timeout=30).returncode, 0)
            with (root / "witness-search-registries/outstanding.tsv").open(newline="") as handle:
                rows = list(csv.DictReader(handle, dialect="excel-tab"))
            found = {(row["key"], row["source"], row["kind"]): row for row in rows}
            self.assertEqual(
                {(source, kind) for key, source, kind in found if key == "scheme-ref"},
                {(source, "selector-unavailable") for source in
                 ("apis.guru", "jentic", "postman", "vendor-portals")})
            self.assertEqual(json.loads(found["shape-a", "vendor-portals", "inconclusive-screen"]["items"]),
                             ["big.json@abc"])
            self.assertIn("3600 seconds", found["shape-a", "vendor-portals", "inconclusive-screen"]["blocker"])
            self.assertEqual(json.loads(found["shape-a", "vendor-portals", "unreadable-document"]["items"]),
                             ["bad.json@abc"])
            self.assertEqual(found["shape-a", "vendor-portals", "portal-unanswered"]["items"], '["gone/docs"]')
            self.assertIn("From value: 225", found["shape-a", "postman", "query-refused"]["blocker"])
            self.assertIn("Link does not exist",
                          found["shape-a", "postman", "collection-body-unacquired"]["blocker"])
            self.assertEqual(found["shape-a", "postman", "collection-body-unacquired"]["items"], '["c1"]')
            self.assertIn("API key", found["shape-a", "postman", "api-body-unacquired"]["blocker"])
            self.assertEqual(found["shape-a", "postman", "unscreened-declarer"]["items"], '["u3"]')
            # A body read and classified by the census, and an answered query, are not outstanding.
            self.assertNotIn("c2", "".join(row["items"] for row in rows))
            self.assertEqual(len(rows), 11)

    def test_committed_outstanding_inventory_matches_its_ledgers(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(REPO / "scripts/witness-search-registries-outstanding.py"), "--check"],
            cwd=REPO, capture_output=True, text=True, timeout=120,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_key_derivation_reads_current_region_tables(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(KEYS)], cwd=REPO,
            capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        rows = list(csv.DictReader(io.StringIO(completed.stdout), dialect="excel-tab"))
        self.assertEqual(len(rows), 32)
        self.assertEqual(len({row["key"] for row in rows}), 32)
        self.assertEqual(
            [row["key"] for row in rows if row["census_status"] == "unsupported-by-census"],
            ["securityscheme-ref"],
        )
        self.assertEqual(completed.stdout, TRACKED_KEYS.read_text(encoding="utf-8"))

    def test_key_derivation_rejects_invalid_region_rows(self) -> None:
        valid = "| `shape-a` | x | x | `gap` | census `schema.items` | x | x | FIXTURE |\n"
        invalid = {
            "no FIXTURE gap rows": "",
            "has no selector": "| `shape-a` | x | x | `gap` | no selector | x | x | FIXTURE |\n",
            "duplicate gap key": valid + valid,
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for region in ("document-paths.md", "parameters.md", "bodies-media.md",
                           "schemas.md", "security.md", "oas31-extensions.md"):
                (root / region).write_text("", encoding="utf-8")
            for expected, contents in invalid.items():
                with self.subTest(expected=expected):
                    (root / "schemas.md").write_text(contents, encoding="utf-8")
                    completed = subprocess.run(
                        [sys.executable, str(KEYS), "--regions-dir", str(root)],
                        cwd=REPO, capture_output=True, text=True, timeout=30,
                    )
                    self.assertEqual(completed.returncode, 1)
                    self.assertIn(expected, completed.stderr)
                    self.assertIn("repair the FIXTURE gap rows", completed.stderr)

    def test_local_census_rejects_incomplete_tsv_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            contract = root / "keys.tsv"
            contract.write_text("key\tselector\nshape-a\tschema.items\n", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--contract", str(contract),
                 "--documents", f"local={root}", "--all-documents-jsonl"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
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
                    body = json.dumps({"resources": {"core": {
                        "limit": 100, "used": used, "remaining": 100 - used,
                        "reset": int(time.time()),
                    }}}).encode()
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

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            url = f"http://127.0.0.1:{server.server_port}"
            env = {**os.environ, "CROZIER_GITHUB_API_URL": url,
                   "GITHUB_TOKEN": "local-test-token"}
            evidence = root / "evidence"
            output = root / "tree.tar.gz"
            completed = subprocess.run(
                [sys.executable, str(GITHUB_ACQUIRE), f"{url}/tree.tar.gz",
                 str(output), "--evidence-dir", str(evidence)],
                cwd=REPO, env=env, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(output.read_bytes(), b"real local tree archive bytes")
            self.assertGreaterEqual(state["reads"], 2)
            self.assertEqual(state["downloads"], 1)
            self.assertTrue(state["authorized"])
            waits = [json.loads(line) for line in
                     (evidence / "rate-limit-waits.jsonl").read_text().splitlines()]
            self.assertTrue(any(row["kind"] == "wait" and row["cause"] == "cap"
                                and row["bucket"] == "core" for row in waits))
            self.assertTrue(any(row["kind"] == "probe" and row["reading"]["used"] == 71
                                for row in waits))
            refused = subprocess.run(
                [sys.executable, str(GITHUB_ACQUIRE), f"{url}/forbidden",
                 str(root / "missing"), "--evidence-dir", str(evidence)],
                cwd=REPO, env=env, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(refused.returncode, 1)
            records = [json.loads(line) for line in
                       (evidence / "acquisitions.jsonl").read_text().splitlines()]
            self.assertEqual([row["status"] for row in records], [200, 403])
            self.assertFalse((root / "missing").exists())
            transport = subprocess.run(
                [sys.executable, str(GITHUB_ACQUIRE), f"{url}/transport",
                 str(root / "missing"), "--evidence-dir", str(evidence)],
                cwd=REPO, env=env, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(transport.returncode, 1)
            self.assertIn("transport error", transport.stderr)
            records = [json.loads(line) for line in
                       (evidence / "acquisitions.jsonl").read_text().splitlines()]
            self.assertNotIn("status", records[-1])
            self.assertTrue(records[-1]["error"])
            invalid_bucket = subprocess.run(
                [sys.executable, str(GITHUB_ACQUIRE), f"{url}/tree.tar.gz",
                 str(root / "invalid"), "--evidence-dir", str(evidence),
                 "--bucket", "graphql"],
                cwd=REPO, env=env, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(invalid_bucket.returncode, 2)
            self.assertIn("invalid choice", invalid_bucket.stderr)
            self.assertFalse((root / "invalid").exists())

            probe_failure = subprocess.run(
                [sys.executable, str(GITHUB_ACQUIRE), f"{url}/tree.tar.gz",
                 str(root / "unprobed"), "--evidence-dir", str(evidence)],
                cwd=REPO, env={**env, "CROZIER_GITHUB_API_URL": f"{url}/missing"},
                capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(probe_failure.returncode, 1)
            self.assertIn("rate-limit guard refused acquisition", probe_failure.stderr)
            self.assertFalse((root / "unprobed").exists())
            self.assertEqual(state["downloads"], 1)

    def test_all_documents_tsv_names_unreadable_document(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            documents = root / "documents"
            documents.mkdir()
            (documents / "broken.json").write_text('{"openapi":', encoding="utf-8")
            contract = root / "keys.md"
            contract.write_text(
                "| key | selector |\n|---|---|\n"
                "| `array` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf` |\n",
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--contract", str(contract),
                 "--documents", f"local={documents}", "--all-documents"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
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
            )
            hit = json.dumps({
                "openapi": "3.0.0", "info": {"title": "hit", "version": "1"},
                "paths": {}, "components": {"schemas": {"Shape": {"oneOf": [
                    {"type": "array", "items": {"anyOf": [{"type": "string"}]}}
                ]}}},
            }).encode()
            miss = json.dumps({
                "openapi": "3.0.0", "info": {"title": "miss", "version": "1"},
                "paths": {}, "components": {"schemas": {"Shape": {"type": "string"}}},
            }).encode()
            (documents / "hit.json").write_bytes(hit)
            (documents / "hit.yaml").write_bytes(hit)
            (documents / "miss.json").write_bytes(miss)
            (documents / "metadata.json").write_text(
                json.dumps({"bundle": json.loads(hit)}), encoding="utf-8"
            )
            (documents / "notes.yaml").write_text(
                "title: no OpenAPI document\n", encoding="utf-8"
            )
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--contract", str(contract),
                 "--documents", f"local={documents}", "--all-documents"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
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
                [sys.executable, str(SCRIPT), "--contract", str(contract),
                 "--documents", f"local={documents}", "--all-documents-jsonl",
                 "--progress-log", str(root / "progress.jsonl")],
                cwd=REPO, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(compact.returncode, 0, compact.stderr)
            objects = [json.loads(line) for line in compact.stdout.splitlines()]
            self.assertEqual(len(objects), 5)
            self.assertEqual({row["document"]: row["loader"] for row in objects}["notes.yaml"], "")
            self.assertEqual({row["document"]: row["selectors"]["array"] for row in objects},
                             {"hit.json": 1, "hit.yaml": 1, "miss.json": 0,
                              "metadata.json": 0,
                              "notes.yaml": 0})
            progress = [json.loads(line) for line in
                        (root / "progress.jsonl").read_text().splitlines()]
            self.assertEqual(len(progress), 10)
            self.assertEqual(
                {name: sum(row["event"] == name for row in progress)
                 for name in ("start", "end")},
                {"start": 5, "end": 5},
            )
            resumed = subprocess.run(
                [sys.executable, str(SCRIPT), "--contract", str(contract),
                 "--documents", f"local={documents}", "--all-documents-jsonl",
                 "--start-after", "miss.json"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
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
            )
            from_regions = subprocess.run(
                [sys.executable, str(SCRIPT), "--contract", str(derived),
                 "--documents", f"local={documents}", "--all-documents-jsonl"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(from_regions.returncode, 0, from_regions.stderr)
            derived_rows = [json.loads(line) for line in from_regions.stdout.splitlines()]
            self.assertEqual({row["document"]: row["selectors"] for row in derived_rows},
                             {"hit.json": {"array": 1}, "hit.yaml": {"array": 1},
                              "miss.json": {"array": 0},
                              "metadata.json": {"array": 0},
                              "notes.yaml": {"array": 0}})


if __name__ == "__main__":
    unittest.main()
