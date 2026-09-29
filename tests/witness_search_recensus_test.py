#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier has no Nx workspace; this test sits in tests/ beside the other witness-search suites and runs under `just test-census-fallback`, which CI's live-e2e leg runs.
"""`scripts/witness-search-recensus.py`, driven through its real CLI.

`full-yaml` over a temporary ledger whose parse failures name real documents in
a temporary cache: one only the full YAML parser reads, one only its lenient
reading reads, one no reading reads, and one that is YAML but no OpenAPI
description. Each ledger row it appends, and the `records.tsv` row
`witness-search-github-index.py` derives from it, says what was read and how.

`reacquire-head` against a loopback server standing in for api.github.com,
raw.githubusercontent.com and Sourcegraph: a file the head still holds, a
deleted repository whose blob Sourcegraph's mirror still serves, and one
nothing serves. Every REST call is logged by the rate-limit guard.

It needs the search's pinned ruamel.yaml: run it as `just test-census-fallback`.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "witness-search-recensus.py"
KEY = "property-sole-anyof-composed-member"
SELECTOR = "schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf"

# The census's stdlib loader refuses the explicit `? ` key; YAML 1.2 reads it.
DECLARER = b"""openapi: 3.0.3
info: {title: Pets, version: '1'}
paths:
  ? /pets
  : get:
      responses:
        '200': {description: ok}
components:
  schemas:
    Base:
      type: object
      properties:
        id: {type: string}
    Pet:
      type: object
      properties:
        owner:
          anyOf:
            - allOf:
                - $ref: '#/components/schemas/Base'
"""
# A duplicate key the strict construction refuses and the lenient reading keeps last.
DUPLICATE = b"""openapi: 3.0.3
info: {title: First, version: '1'}
info: {title: Second, version: '1'}
paths: {}
"""
TEMPLATE = b"{{- if .Values.enabled }}\nopenapi: 3.0.0\n{{- end }}\n"
NOT_OPENAPI = b"name: chart\nversion: 1.0.0\n"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


INDEX = _load("witness_search_github_index", REPO / "scripts" / "witness-search-github-index.py")


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


OTHER = "oneof-anyof-variant"


def keys_file(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "keys.json").write_text(json.dumps({"keys": {
        KEY: {"region": "schemas", "selector": SELECTOR, "selector_status": "available"},
        OTHER: {"region": "schemas", "selector": "schema.oneOf>schema.anyOf", "selector_status": "available"},
    }}), encoding="utf-8")


def run(*args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True,
                          env={**os.environ, **(env or {})}, timeout=300)


class FullYamlTest(unittest.TestCase):
    def test_each_parse_failure_is_read_again_and_recorded_with_its_reading(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            rows = []
            for name, data in (("declarer", DECLARER), ("duplicate", DUPLICATE), ("template", TEMPLATE),
                               ("chart", NOT_OPENAPI)):
                digest = hashlib.sha256(data).hexdigest()
                (cache / "documents" / f"{digest}.yaml").write_bytes(data)
                rows.append({"source": "sourcegraph", "key": KEY, "selector": SELECTOR,
                             "repository": f"github.com/example/{name}", "path": "openapi.yaml",
                             "commit": "c" * 40, "sha256": digest, "document": f"{digest}.yaml",
                             "disposition": "parse-failure", "diagnostic": "the stdlib loader refused it"})
            other = {**rows[0], "key": OTHER, "selector": "schema.oneOf>schema.anyOf"}
            (evidence / "candidates.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in [*rows, other]), encoding="utf-8")

            completed = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                            "--cache", str(cache), "--jobs", "2", "--key", KEY)
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("4 parse-failure row(s) over 4 document(s) read again", completed.stdout)

            appended = {row["repository"].rsplit("/", 1)[1]: row
                        for _, row in INDEX.jsonl(evidence / "candidates.jsonl") if row.get("loader")}
            self.assertEqual("declares", appended["declarer"]["disposition"])
            self.assertEqual(1, appended["declarer"]["selector_count"])
            self.assertEqual("ruamel.yaml 0.19.1 (YAML 1.2)", appended["declarer"]["loader"])
            self.assertEqual("does-not-declare", appended["duplicate"]["disposition"])
            self.assertIn("duplicate keys last-wins", appended["duplicate"]["loader"])
            self.assertEqual("census-refused", appended["template"]["disposition"])
            self.assertIn("ruamel.yaml 0.19.1", appended["template"]["diagnostic"])
            self.assertIn(f"sha256 {rows[2]['sha256']}", appended["template"]["diagnostic"])
            self.assertEqual("excluded-non-openapi-3", appended["chart"]["disposition"])

            records = {row["candidate"].split("/", 1)[1].split(":")[0]: row
                       for row in INDEX.source_rows(root, "sourcegraph")}
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records["declarer"]["census"])
            self.assertEqual("outstanding", records["declarer"]["disposition"])  # its screens are owed
            self.assertTrue(records["duplicate"]["census"].startswith("census 0; read by ruamel.yaml"))
            self.assertEqual("rejected", records["duplicate"]["disposition"])
            self.assertTrue(records["template"]["census"].startswith("census-refused: ruamel.yaml 0.19.1"))
            self.assertEqual("rejected", records["template"]["disposition"])
            self.assertEqual("rejected", records["chart"]["disposition"])

            # The key filter left the other key's row to a later run, which reads it and no more.
            self.assertEqual("outstanding", next(r for r in INDEX.source_rows(root, "sourcegraph")
                                                 if r["key"] == OTHER)["disposition"])
            again = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", "--cache", str(cache))
            self.assertEqual(0, again.returncode, again.stderr)
            self.assertIn("1 parse-failure row(s) over 1 document(s) read again: 1 does-not-declare", again.stdout)

    def test_a_document_past_the_time_bound_is_refused_with_the_bound(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            # Large enough that the pure-Python parser cannot finish it inside one second.
            data = b"openapi: 3.0.3\nx:\n" + b"".join(b"  k%d: [a, {b: c}]\n" % n for n in range(400_000))
            digest = hashlib.sha256(data).hexdigest()
            (cache / "documents" / f"{digest}.yaml").write_bytes(data)
            row = {"source": "sourcegraph", "key": KEY, "repository": "github.com/example/huge", "path": "a.yaml",
                   "commit": "c" * 40, "sha256": digest, "disposition": "parse-failure"}
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
            completed = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                            "--cache", str(cache), "--timeout", "1")
            self.assertEqual(0, completed.returncode, completed.stderr)
            refused = [r for _, r in INDEX.jsonl(evidence / "candidates.jsonl") if r.get("loader")]
            self.assertEqual("census-refused", refused[0]["disposition"])
            self.assertIn("parse exceeded 1 s", refused[0]["diagnostic"])
            self.assertIn(f"sha256 {digest}", refused[0]["diagnostic"])

    def test_an_absent_copy_and_a_bad_bound_name_their_repair(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            row = {"source": "sourcegraph", "key": KEY, "repository": "github.com/example/api", "path": "a.yaml",
                   "commit": "c" * 40, "sha256": "a" * 64, "disposition": "parse-failure"}
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
            missing = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                          "--cache", str(Path(tmp) / "empty"))
            self.assertEqual(1, missing.returncode)
            self.assertIn(f"no cached copy of sha256 {'a' * 64}", missing.stderr)
            self.assertIn("pass the cache it was acquired into with --cache", missing.stderr)
            bound = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph",
                        "--cache", str(Path(tmp) / "empty"), "--jobs", "0")
            self.assertEqual(2, bound.returncode)
            self.assertIn("--jobs and --timeout must be positive", bound.stderr)

    def test_a_copy_that_does_not_hash_to_its_pin_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-sourcegraph"
            keys_file(evidence)
            cache = Path(tmp) / "cache"
            (cache / "documents").mkdir(parents=True)
            digest = hashlib.sha256(DECLARER).hexdigest()
            (cache / "documents" / f"{digest}.yaml").write_bytes(DUPLICATE)
            row = {"source": "sourcegraph", "key": KEY, "repository": "github.com/example/api", "path": "a.yaml",
                   "commit": "c" * 40, "sha256": digest, "disposition": "parse-failure"}
            (evidence / "candidates.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
            completed = run("--evidence-root", str(root), "full-yaml", "--source", "sourcegraph", "--cache", str(cache))
            self.assertEqual(1, completed.returncode)
            self.assertIn("does not hash to the pinned sha256", completed.stderr)
            self.assertIn("re-acquire it at its commit", completed.stderr)


HEAD = "d" * 40
PINNED = "e" * 40
OLDER = "f" * 40


class Upstream(BaseHTTPRequestHandler):
    def log_message(self, *args: object) -> None:
        pass

    def reply(self, status: int, body: bytes | dict) -> None:
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        self.server.paths.append(self.path)
        reset = int(time.time()) + 60
        if self.path == "/rate_limit":
            self.reply(200, {"resources": {"core": {"limit": 5000, "used": 0, "remaining": 5000, "reset": reset}}})
        elif self.path == "/repos/example/kept":
            self.reply(200, {"default_branch": "main"})
        elif self.path == "/repos/example/kept/commits/main":
            self.reply(200, {"sha": HEAD})
        elif self.path == f"/example/kept/{HEAD}/openapi.yaml":
            self.reply(200, DECLARER)
        elif self.path in ("/repos/example/moved", "/repos/example/dropped", "/repos/example/headless",
                           "/repos/example/unlisted"):
            self.reply(200, {"default_branch": "main"})
        elif self.path == "/repos/example/unlisted/commits/main":
            self.reply(200, {"sha": HEAD})
        elif self.path.startswith("/repos/example/unlisted/commits?path="):
            self.reply(500, {"message": "Server Error"})
        elif self.path in ("/repos/example/moved/commits/main", "/repos/example/dropped/commits/main"):
            self.reply(200, {"sha": HEAD})
        elif self.path == f"/repos/example/moved/commits?path=openapi.yaml&sha={HEAD}&per_page=100":
            self.reply(200, [{"sha": HEAD}, {"sha": OLDER}])  # removed at head, present before it
        elif self.path == f"/repos/example/dropped/commits?path=openapi.yaml&sha={HEAD}&per_page=100":
            self.reply(200, [])
        elif self.path == f"/example/moved/{OLDER}/openapi.yaml":
            self.reply(200, DECLARER)
        elif self.path.startswith("/repos/"):
            self.reply(404, {"message": "Not Found"})
        elif self.path == f"/github.com/example/mirrored/-/raw/openapi.yaml?rev={PINNED}":
            self.reply(200, DECLARER)
        else:
            self.reply(404, b"Not Found")


class ReacquireHeadTest(unittest.TestCase):
    def test_each_404_is_requested_at_head_then_at_the_mirror(self) -> None:
        server = ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
        server.paths = []
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        url = f"http://127.0.0.1:{server.server_port}"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "evidence"
            evidence = root / "witness-search-github-code-search"
            keys_file(evidence)
            rows = [{"source": "github-code-search", "key": KEY, "selector": SELECTOR,
                     "repository": f"example/{name}", "path": "openapi.yaml", "commit": PINNED,
                     "blob": git_blob(DECLARER), "disposition": "acquisition-failure", "status": 404,
                     "diagnostic": "404: Not Found"}
                    for name in ("kept", "mirrored", "gone", "moved", "dropped", "headless", "unlisted")]
            (evidence / "candidates.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")

            completed = run("--evidence-root", str(root), "reacquire-head", "--cache-dir", str(Path(tmp) / "cache"),
                            env={"CROZIER_GITHUB_API_URL": url, "CROZIER_RAW_GITHUB_URL": url,
                                 "CROZIER_SOURCEGRAPH_URL": url, "GITHUB_TOKEN": "offline-test-token"})
            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertIn("7 404 candidate(s) requested at head: 4 acquisition-failure, 3 declares", completed.stdout)

            records = {row["candidate"].split(":")[0].split("/")[1]: row
                       for row in INDEX.source_rows(root, "github-code-search")}
            self.assertEqual(7, len(records), records)  # a read at another commit supersedes its pinned 404
            self.assertEqual(HEAD, records["kept"]["revision"])
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records["kept"]["census"])
            self.assertEqual(PINNED, records["mirrored"]["revision"])
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records["mirrored"]["census"])
            self.assertEqual("outstanding", records["gone"]["disposition"])
            self.assertIn("GET /repos/example/gone answered HTTP 404 at", records["gone"]["census"])
            self.assertIn(f"Sourcegraph's mirror at {PINNED} served HTTP 404 at", records["gone"]["census"])

            # Head served, file gone from it: the path's history reaches the pinned blob.
            self.assertEqual(OLDER, records["moved"]["revision"])
            self.assertEqual("census 1; read by ruamel.yaml 0.19.1 (YAML 1.2)", records["moved"]["census"])
            # Head served, and neither its history nor the mirror holds the blob: refused, at its pin.
            self.assertEqual(PINNED, records["dropped"]["revision"])
            self.assertEqual("outstanding", records["dropped"]["disposition"])
            self.assertIn(f"openapi.yaml at {HEAD} (head of main) answered HTTP 404 at", records["dropped"]["census"])
            self.assertIn(f"the path's history at {HEAD} lists 0 commit(s), none serving blob", records["dropped"]["census"])
            self.assertIn(f"Sourcegraph's mirror at {PINNED} served HTTP 404 at", records["dropped"]["census"])
            # A head commit GitHub will not name, and a history GitHub will not list.
            self.assertIn("GET /repos/example/headless/commits/main answered HTTP 404 at", records["headless"]["census"])
            self.assertIn(f"the path's history at {HEAD} answered HTTP 500 at", records["unlisted"]["census"])
            self.assertEqual({"outstanding"}, {records[name]["disposition"] for name in ("headless", "unlisted")})

            ledger = {row["repository"].split("/")[1]: row for _, row in INDEX.jsonl(evidence / "candidates.jsonl")}
            self.assertEqual("sourcegraph-mirror", ledger["mirrored"]["acquisition_route"])
            guarded = [row for _, row in INDEX.jsonl(evidence / "rate-limit-calls.jsonl") if row.get("bucket") == "core"]
            rest = [path for path in server.paths if path.startswith("/repos/")]
            self.assertEqual(len(rest), len(guarded))
            # seven repositories, five head commits asked for, and three histories of the path
            self.assertEqual(15, len(rest))
            sourcegraph = [row for _, row in INDEX.jsonl(evidence / "rate-limit-calls.jsonl")
                           if row.get("host") == "sourcegraph"]
            self.assertEqual(5, len(sourcegraph))

            # A second run leaves what the first decided; `--again` requests only what is still refused.
            env = {"CROZIER_GITHUB_API_URL": url, "CROZIER_RAW_GITHUB_URL": url,
                   "CROZIER_SOURCEGRAPH_URL": url, "GITHUB_TOKEN": "offline-test-token"}
            second = run("--evidence-root", str(root), "reacquire-head", "--cache-dir", str(Path(tmp) / "cache"), env=env)
            self.assertIn("0 404 candidate(s) requested at head", second.stdout)
            again = run("--evidence-root", str(root), "reacquire-head", "--again",
                        "--cache-dir", str(Path(tmp) / "cache"), env=env)
            self.assertEqual(0, again.returncode, again.stderr)
            self.assertIn("4 404 candidate(s) requested at head: 4 acquisition-failure", again.stdout)
            self.assertEqual(7, len(INDEX.source_rows(root, "github-code-search")))

            misspelt = run("--evidence-root", str(root), "reacquire-head", "--key", "no-such-key",
                           "--cache-dir", str(Path(tmp) / "cache"))
            self.assertEqual(2, misspelt.returncode)
            self.assertIn("--key ['no-such-key'] names no key of witness-search-github-code-search/keys.json",
                          misspelt.stderr)

            invalid = run("--evidence-root", str(root), "reacquire-head", "--again",
                          "--cache-dir", str(Path(tmp) / "cache"),
                          env={"CROZIER_GITHUB_API_URL": url, "CROZIER_SOURCEGRAPH_URL": "file:///etc/passwd"})
            self.assertEqual(1, invalid.returncode)
            self.assertIn("CROZIER_SOURCEGRAPH_URL must use https://sourcegraph.com", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
