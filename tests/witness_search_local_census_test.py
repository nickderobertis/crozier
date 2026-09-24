#!/usr/bin/env python3
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
POSTMAN = REPO / "scripts/witness-search-postman.py"
PORTAL_TREES = REPO / "scripts/witness-search-portal-trees.py"


class LocalCensusTest(unittest.TestCase):
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
                "repository\tpinned_ref\nexample/api\t" + pin + "\n", encoding="utf-8",
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
            with manifest.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle, dialect="excel-tab"))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["path"], "openapi.json")
            self.assertEqual(rows[0]["sha256"], hashlib.sha256(
                (source / "openapi.json").read_bytes()).hexdigest())

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
            self.assertEqual(len(rows), 4)
            by_name = {row["document"]: row for row in rows}
            self.assertEqual(by_name["hit.json"]["count"], "1")
            self.assertEqual(by_name["miss.json"]["count"], "0")
            self.assertEqual(by_name["metadata.json"]["count"], "0")
            self.assertEqual(by_name["metadata.json"]["openapi_version"], "")
            self.assertEqual(by_name["notes.yaml"]["count"], "0")
            self.assertEqual(by_name["hit.json"]["sha256"], hashlib.sha256(hit).hexdigest())
            self.assertEqual(by_name["miss.json"]["sha256"], hashlib.sha256(miss).hexdigest())
            compact = subprocess.run(
                [sys.executable, str(SCRIPT), "--contract", str(contract),
                 "--documents", f"local={documents}", "--all-documents-jsonl"],
                cwd=REPO, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(compact.returncode, 0, compact.stderr)
            objects = [json.loads(line) for line in compact.stdout.splitlines()]
            self.assertEqual(len(objects), 4)
            self.assertEqual({row["document"]: row["selectors"]["array"] for row in objects},
                             {"hit.json": 1, "miss.json": 0, "metadata.json": 0,
                              "notes.yaml": 0})
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
                             {"hit.json": {"array": 1}, "miss.json": {"array": 0},
                              "metadata.json": {"array": 0},
                              "notes.yaml": {"array": 0}})


if __name__ == "__main__":
    unittest.main()
