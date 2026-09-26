# llmlint: ignore-file[new_code_lands_in_a_project] crozier's Python maintenance tests live in tests/ and run through just; no Nx workspace or project boundary exists for this offline HTTP tier.
"""Exercise witness acquisition through real local HTTP responses and the census."""

from __future__ import annotations

import base64
import csv
import hashlib
import importlib.util
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import rate_limit_guard as guard_module  # noqa: E402 - scripts must enter sys.path first

SPEC = importlib.util.spec_from_file_location(
    "witness_search_github", REPO / "scripts/witness-search-github.py"
)
assert SPEC and SPEC.loader
SEARCH = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SEARCH
SPEC.loader.exec_module(SEARCH)

# CI checks out without origin/main, so every CLI run but the fallback test names
# the branch point explicitly rather than deriving it with git merge-base.
SOURCE_COMMIT = ["--source-commit", "a" * 40]

DOCUMENT = b"""openapi: 3.0.3
info:
  title: Search result
  version: 1.0.0
paths: {}
components:
  schemas:
    A:
      type: object
      properties:
        field:
          type: string
"""


class PublisherSelectionTests(unittest.TestCase):
    def test_widened_publishers_are_confirmed_declarer_repositories(self) -> None:
        selected = {row["repository"]: row for row in SEARCH.publisher_set()}
        manifest = (
            REPO
            / "docs/openapi-surface/witness-search-github-publisher-trees/publisher-declarers.tsv"
        )
        with manifest.open(encoding="utf-8", newline="") as stream:
            declarers = list(csv.DictReader(stream, delimiter="\t"))
        self.assertGreater(len(declarers), 5)
        for row in declarers:
            with self.subTest(repository=row["repository"]):
                self.assertEqual(row["commit"], selected[row["repository"]]["commit"])
                evidence = (
                    REPO
                    / f"docs/openapi-surface/witness-search-{row['source']}/candidates.jsonl"
                )
                self.assertTrue(
                    any(
                        candidate.get("disposition") == "declares"
                        and candidate.get("repository", "").removeprefix("github.com/")
                        == row["repository"]
                        and candidate.get("commit") == row["commit"]
                        for candidate in map(
                            json.loads, SEARCH.INDEX.read_ledger(evidence).splitlines()
                        )
                    ),
                    row,
                )



class LedgerShardTests(unittest.TestCase):
    """A ledger past GitHub's blob limit is kept as line-aligned parts."""

    GITHUB_BLOB_LIMIT = 100 * 1000 * 1000
    GITHUB_WARNING_SIZE = 50 * 1000 * 1000

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def test_committed_evidence_fits_under_githubs_blob_limit(self) -> None:
        evidence = REPO / "docs/openapi-surface"
        oversized = [
            str(path.relative_to(REPO))
            for path in evidence.rglob("*")
            if path.is_file() and path.stat().st_size >= self.GITHUB_BLOB_LIMIT
        ]
        self.assertEqual([], oversized, "GitHub refuses a push carrying these blobs")

    def test_split_ledgers_stay_under_githubs_warning_size(self) -> None:
        evidence = REPO / "docs/openapi-surface"
        ledgers = [evidence / "witness-search-github/candidates.tsv"] + [
            evidence / f"witness-search-{source}" / name
            for source in ("github-code-search", "github-publisher-trees", "sourcegraph")
            for name in ("records.tsv", "candidates.jsonl", "queries.jsonl", "documents.jsonl")
        ]
        oversized = [
            str(part.relative_to(REPO))
            for ledger in ledgers
            for part in SEARCH.INDEX.ledger_parts(ledger)
            if part.is_file() and part.stat().st_size >= self.GITHUB_WARNING_SIZE
        ]
        self.assertEqual([], oversized, "rewrite these through INDEX.write_ledger")

    def test_readme_states_the_shard_threshold_and_part_names_the_index_writes(self) -> None:
        readme = " ".join(
            (REPO / "docs/openapi-surface/witness-search-github/README.md").read_text(encoding="utf-8").split()
        )
        ledger = self.root / "candidates.tsv"
        SEARCH.INDEX.write_ledger(ledger, "header\nrow\nrow\n", len("header\n"))
        names = [part.name for part in SEARCH.INDEX.ledger_parts(ledger)]
        self.assertEqual(["candidates.tsv", "candidates.001.tsv", "candidates.002.tsv"], names)
        for stated in (
            f"over {self.GITHUB_BLOB_LIMIT // 1_000_000} MB",
            f"larger than {SEARCH.INDEX.SHARD_BYTES // 1_000_000} MB",
            *(f"`{name}`" for name in names),
        ):
            self.assertIn(stated, readme)

    def test_acquirer_appends_into_numbered_parts_read_back_in_order(self) -> None:
        evidence = self.root / "evidence"
        acquirer = SEARCH.Acquirer(evidence, cache=self.root / "cache")
        rows = [
            {"source": "github-code-search", "key": "shape", "repository": f"example/api{n}",
             "path": "openapi.yaml", "disposition": "does-not-declare"}
            for n in range(12)
        ]
        with patch.object(SEARCH.INDEX, "SHARD_BYTES", 400):
            for row in rows:
                acquirer.write("candidates.jsonl", row)
        parts = SEARCH.INDEX.ledger_parts(evidence / "candidates.jsonl")
        self.assertGreater(len(parts), 2)
        self.assertEqual(evidence / "candidates.001.jsonl", parts[1])
        for part in parts:
            self.assertLessEqual(part.stat().st_size, 400)
            self.assertTrue(part.read_text(encoding="utf-8").endswith("\n"))
        read = SEARCH.jsonl(evidence / "candidates.jsonl")
        self.assertEqual([row["repository"] for row in rows], [row["repository"] for row in read])

    def test_index_writes_parts_and_checks_them_as_one_ledger(self) -> None:
        root = self.root / "index"
        for source in ("github-code-search", "github-publisher-trees", "sourcegraph"):
            directory = root / f"witness-search-{source}"
            directory.mkdir(parents=True)
            (directory / "keys.json").write_text(json.dumps(
                {"keys": {"shape": {"selector": "schema.additionalProperties=false"}}}
            ), encoding="utf-8")
        (root / "witness-search-github-publisher-trees/publisher-set.json").write_text(
            json.dumps({"publishers": []}), encoding="utf-8"
        )
        SEARCH.INDEX.write_ledger(
            root / "witness-search-github-code-search/candidates.jsonl",
            "".join(
                json.dumps({"source": "github-code-search", "key": "shape",
                            "repository": f"example/api{n}", "path": "openapi.yaml",
                            "commit": f"{n:x}" * 40, "sha256": "d" * 64,
                            "disposition": "does-not-declare", "selector_count": 0}) + "\n"
                for n in range(8)
            ),
            300,
        )
        command = [sys.executable, str(REPO / "scripts/witness-search-github-index.py"),
                   "--evidence-root", str(root)]
        central = root / "witness-search-github/candidates.tsv"
        sharded = subprocess.run([*command, "--shard-bytes", "500"], capture_output=True, text=True)
        self.assertEqual(0, sharded.returncode, sharded.stderr)
        parts = SEARCH.INDEX.ledger_parts(central)
        self.assertGreater(len(parts), 1)
        self.assertTrue(all(part.stat().st_size <= 500 for part in parts))
        indexed = list(csv.DictReader(
            SEARCH.INDEX.read_ledger(central).splitlines(), delimiter="\t"
        ))
        self.assertEqual(8, len(indexed))
        self.assertEqual({"github-code-search"}, {row["source"] for row in indexed})
        records = root / "witness-search-github-code-search/records.tsv"
        self.assertGreater(len(SEARCH.INDEX.ledger_parts(records)), 1)
        self.assertEqual(
            [row["candidate"] for row in indexed],
            [row["candidate"] for row in csv.DictReader(
                SEARCH.INDEX.read_ledger(records).splitlines(), delimiter="\t"
            )],
        )
        subprocess.run([*command, "--check"], check=True, capture_output=True)
        parts[-1].write_text("", encoding="utf-8")
        stale = subprocess.run([*command, "--check"], capture_output=True, text=True)
        self.assertEqual(1, stale.returncode)
        self.assertIn("candidates.tsv", stale.stderr)
        subprocess.run(command, check=True, capture_output=True)
        self.assertEqual([central], SEARCH.INDEX.ledger_parts(central))
        self.assertEqual([records], SEARCH.INDEX.ledger_parts(records))
        subprocess.run([*command, "--check"], check=True, capture_output=True)
        search_index = root / "witness-search-github-code-search/search-index.tsv"
        indexed_text = search_index.read_text(encoding="utf-8")
        search_index.write_text(indexed_text + "shape\tquery\tnever issued\t0 results\tqueries.jsonl\n", encoding="utf-8")
        drifted = subprocess.run([*command, "--check"], capture_output=True, text=True)
        self.assertEqual(1, drifted.returncode)
        self.assertIn(str(search_index), drifted.stderr)
        self.assertIn("indexed query 'never issued' was never issued", drifted.stderr)
        search_index.write_text(indexed_text, encoding="utf-8")
        subprocess.run([*command, "--check"], check=True, capture_output=True)
        refused = subprocess.run([*command, "--shard-bytes", "0"], capture_output=True, text=True)
        self.assertEqual(2, refused.returncode)
        self.assertIn("--shard-bytes must be positive", refused.stderr)

class LocalServer(BaseHTTPRequestHandler):
    def log_message(self, *args: object) -> None:
        pass

    def do_GET(self) -> None:
        state = self.server.state
        if self.path == "/rate_limit":
            state["reads"] += 1
            used = 7 if state["reads"] == 1 and state["cap"] else 0
            self.reply(
                200,
                {
                    "resources": {
                        "code_search": {
                            "limit": 10,
                            "used": used,
                            "remaining": 10 - used,
                            "reset": int(time.time())
                            if used
                            else int(time.time()) + 60,
                        },
                        "core": {
                            "limit": 10,
                            "used": 0,
                            "remaining": 10,
                            "reset": int(time.time()) + 60,
                        },
                    }
                },
            )
        elif self.path.startswith("/search/code"):
            state["searches"] += 1
            if state["malformed_github"]:
                self.reply(200, {"total_count": 1, "items": [{"path": "openapi.yaml"}]})
            elif state["secondary"]:
                self.reply(
                    403,
                    {"message": "secondary rate limit"},
                    {"X-Ratelimit-Remaining": "9", "Retry-After": "1"},
                )
            else:
                early_empty = state["early_empty"] and "page=2" in self.path
                self.reply(
                    200,
                    {
                        "total_count": 1001
                        if state["partition"] and "size%3A" not in self.path
                        else 2
                        if state["early_empty"]
                        else 1,
                        "incomplete_results": state["incomplete_github"],
                        "items": []
                        if early_empty
                        else [
                            {
                                "repository": {"full_name": "example/api"},
                                "path": "openapi.yaml",
                                "sha": "a" * 40,
                                "url": f"http://127.0.0.1:{self.server.server_port}/repos/example/api/contents/openapi.yaml?ref={'b' * 40}",
                            }
                        ],
                    },
                )
        elif self.path.startswith("/repos/example/api/contents/open%20api.yaml"):
            state["contents"] += 1
            self.reply(200, {"encoding": "base64", "content": base64.b64encode(DOCUMENT).decode()})
        elif self.path.startswith("/repos/example/api/contents/openapi.yaml"):
            state["contents"] += 1
            if state["contents_status"]:
                self.reply(state["contents_status"], {"message": "unavailable"})
            elif state["contents_payload"] is not None:
                self.reply(200, state["contents_payload"])
            elif (
                state["large"]
                and self.headers.get("Accept") == "application/vnd.github.raw+json"
            ):
                if state["raw_metadata"]:
                    self.reply(200, {"encoding": "none", "download_url": "unused"})
                else:
                    self.send_response(200)
                    self.send_header("Content-Type", "application/yaml")
                    self.send_header("X-Ratelimit-Resource", "core")
                    self.send_header("Content-Length", str(len(DOCUMENT)))
                    self.end_headers()
                    self.wfile.write(DOCUMENT)
            elif state["large"]:
                self.reply(200, {"encoding": "none", "download_url": "unused"})
            else:
                self.reply(
                    200,
                    {
                        "encoding": "base64",
                        "content": base64.b64encode(DOCUMENT).decode(),
                    },
                )
        elif self.path.startswith("/repos/example/api/git/trees/"):
            state["trees"] += 1
            if state["malformed_tree"]:
                self.reply(200, {"tree": [{"path": "openapi.yaml"}]})
            elif state["truncated_tree"]:
                if "/" + "d" * 40 in self.path:
                    self.reply(200, {"truncated": False, "tree": [
                        {"type": "blob", "path": "openapi.yaml", "sha": "a" * 40}
                    ]})
                else:
                    self.reply(200, {"truncated": "recursive=1" in self.path, "tree": [
                        {"type": "tree", "path": "sub", "sha": "d" * 40}
                    ]})
            else:
                self.reply(
                    200,
                    {
                        "truncated": False,
                        "tree": [
                            {"type": "blob", "path": "openapi.yaml", "sha": "a" * 40},
                            {"type": "blob", "path": "README.md", "sha": "b" * 40},
                        ],
                    },
                )
        elif self.path.startswith("/example/api/"):
            state["raw_hits"] += 1
            if state["raw_status"]:
                self.reply(state["raw_status"], {"message": "wait"}, {"Retry-After": "invalid-date"})
            elif state["raw_refuse"] and state["raw_hits"] == 1:
                self.reply(429, {"message": "wait"}, {"Retry-After": "0.1"})
            else:
                document = state["raw_document"]
                self.send_response(200)
                incomplete = state["raw_incomplete_remaining"] > 0
                if incomplete:
                    state["raw_incomplete_remaining"] -= 1
                self.send_header(
                    "Content-Length", str(len(document) + (5 if incomplete else 0))
                )
                self.end_headers()
                self.wfile.write(document)
        elif self.path.startswith("/.api/search/stream"):
            state["sourcegraph"] += 1
            if state["sourcegraph_status"]:
                self.reply(state["sourcegraph_status"], {"message": "unavailable"})
            elif state["refuse_sourcegraph"] and state["sourcegraph"] == 1:
                self.reply(429, {"message": "wait"}, {"Retry-After": "0.1"})
            else:
                matches = (
                    b"event: matches\ndata: [\n\n"
                    if state["malformed_sourcegraph"]
                    else b"event: matches\ndata: []\n\n"
                )
                progress = (
                    b'event: progress\ndata: {"done":false,"matchCount":0}\n\n'
                    if state["incomplete_sourcegraph"]
                    else b'event: progress\ndata: {"done":true,"matchCount":0}\n\n'
                )
                body = matches + progress
                self.send_response(200)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
        else:
            self.reply(404, {"message": "missing"})

    def reply(
        self, status: int, body: object, headers: dict[str, str] | None = None
    ) -> None:
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header(
            "X-Ratelimit-Resource",
            "code_search" if self.path.startswith("/search/") else "core",
        )
        for name, value in (headers or {}).items():
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(data)


class WitnessSearchGithubTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), LocalServer)
        self.server.state = {
            "reads": 0,
            "cap": False,
            "searches": 0,
            "secondary": False,
            "malformed_github": False,
            "malformed_sourcegraph": False,
            "incomplete_github": False,
            "incomplete_sourcegraph": False,
            "partition": False,
            "early_empty": False,
            "contents": 0,
            "sourcegraph": 0,
            "refuse_sourcegraph": False,
            "raw_hits": 0,
            "raw_refuse": False,
            "raw_status": 0,
            "contents_status": 0,
            "contents_payload": None,
            "malformed_tree": False,
            "truncated_tree": False,
            "sourcegraph_status": 0,
            "raw_document": DOCUMENT,
            "raw_incomplete_remaining": 0,
            "trees": 0,
            "large": False,
            "raw_metadata": False,
        }
        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.root = Path(self.temporary.name)
        self.url = f"http://127.0.0.1:{self.server.server_port}"
        self.rate_url = patch.object(
            guard_module, "github_api_url", return_value=self.url
        )
        self.rate_url.start()
        self.addCleanup(self.rate_url.stop)
        self.search = SEARCH.Acquirer(
            self.root,
            github_url=self.url,
            sourcegraph_url=self.url,
            raw_github_url=self.url,
            code_search_spacing_s=0.01,
            code_search_refusal_cooldown_s=0.05,
            sourcegraph_spacing_s=0.01,
            sourcegraph_refusal_cooldown_s=0.05,
        )

    def test_key_derivation_and_both_serialization_query_plan(self) -> None:
        keys = SEARCH.derive_keys(REPO / "docs/openapi-surface")
        self.assertIn("annotated-ref-target-string-const", keys)
        # A row a registered witness settled leaves the key set: corpus rows 178
        # and 179 made `securityscheme-ref` `golden`.
        self.assertNotIn("securityscheme-ref", keys)
        queries = SEARCH.query_plan(
            keys["annotated-ref-target-string-const"]["selector"]
        )
        self.assertEqual(7, len(queries["github-code-search"]))
        self.assertEqual(2, len(queries["sourcegraph"]))
        self.assertTrue(
            any("filename:openapi.json" in q for q in queries["github-code-search"])
        )
        self.assertTrue(
            any("filename:swagger.yaml" in q for q in queries["github-code-search"])
        )
        self.assertTrue(
            any("language:YAML" in q for q in queries["github-code-search"])
        )
        self.assertTrue(any(".json" in q for q in queries["sourcegraph"]))
        # `ref-pointer-unnamed-segment` is `golden` now, so no longer a derived
        # key; its selector still exercises the pointer phrasing.
        pointer_queries = SEARCH.query_plan("schema.$ref:unnamed-segment")
        self.assertTrue(
            all(
                "/$defs/" in q or "/definitions/" in q
                for q in pointer_queries["github-code-search"]
            )
        )
        security_queries = SEARCH.query_plan("securityScheme:$ref")
        self.assertEqual(7, len(security_queries["github-code-search"]))
        self.assertEqual(2, len(security_queries["sourcegraph"]))
        self.assertTrue(all("$ref" in q for q in security_queries["sourcegraph"]))

    def test_registered_publishers_are_prioritized_without_dropping_results(
        self,
    ) -> None:
        items = [
            (
                (
                    "shape",
                    "github.com/APIs-guru/openapi-directory",
                    "APIs/a/openapi.yaml",
                    "a",
                ),
                {},
            ),
            (("shape", "github.com/livepeer/ai-runner", "openapi.yaml", "b"), {}),
        ]
        self.assertEqual(
            "github.com/livepeer/ai-runner",
            sorted(items, key=SEARCH.candidate_priority)[0][0][1],
        )

    def test_cap_waits_and_census_overrides_query_ingredients(self) -> None:
        self.server.state["cap"] = True
        items = self.search.github_search(
            "closed-object", '"additionalProperties" filename:openapi.yaml'
        )
        self.assertEqual(1, len(items))
        self.assertEqual(1, self.server.state["searches"])
        waits = self.search.guards["github"].waits()
        self.assertTrue(any(row.get("cause") == "cap" for row in waits))
        item = {**items[0], "selector": "schema.additionalProperties=false"}
        verdict = self.search.github_document("closed-object", item)
        self.assertEqual("b" * 40, verdict["commit"])
        self.assertEqual("does-not-declare", verdict["disposition"])
        self.assertEqual(0, verdict["selector_count"])
        self.assertEqual(1, self.server.state["contents"])

    def test_secondary_refusal_is_outstanding(self) -> None:
        self.server.state["secondary"] = True
        with self.assertRaises(SEARCH.SearchStopped):
            self.search.github_search("closed-object", "additionalProperties")
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual("refused", rows[-1]["outcome"])
        self.assertEqual(403, rows[-1]["status"])

        self.assertEqual(1, self.server.state["searches"])

    def test_malformed_search_results_are_recorded_as_outstanding(self) -> None:
        self.server.state["malformed_github"] = True
        with self.assertRaises(SEARCH.SearchStopped):
            self.search.github_search("closed-object", "additionalProperties")
        self.assertEqual(
            "outstanding-malformed-response",
            json.loads((self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()[-1])[
                "outcome"
            ],
        )
        self.server.state["malformed_sourcegraph"] = True
        with self.assertRaises(SEARCH.SearchStopped):
            self.search.sourcegraph_search("closed-object", "additionalProperties")
        self.assertEqual(
            "outstanding-malformed-response",
            json.loads((self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()[-1])[
                "outcome"
            ],
        )

    def test_incomplete_search_results_remain_outstanding(self) -> None:
        self.server.state["incomplete_github"] = True
        self.assertIsNone(
            self.search.github_search("closed-object", "additionalProperties")
        )
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual("outstanding-incomplete-results", rows[-1]["outcome"])
        self.server.state["incomplete_sourcegraph"] = True
        self.assertIsNone(
            self.search.sourcegraph_search("closed-object", "additionalProperties")
        )
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual("incomplete-stream", rows[-1]["outcome"])

    def test_untrusted_content_url_is_recorded_without_a_request(self) -> None:
        before = self.server.state["contents"]
        record = self.search.github_document(
            "closed-object",
            {
                "selector": "schema.additionalProperties=false",
                "repository": "example/api",
                "path": "openapi.yaml",
                "sha": "a" * 40,
                "url": "https://example.invalid/openapi.yaml",
            },
        )
        self.assertEqual("acquisition-failure", record["disposition"])
        self.assertIn("untrusted", record["diagnostic"])
        self.assertEqual(before, self.server.state["contents"])

    def test_malformed_contents_and_tree_are_outstanding(self) -> None:
        item = {
            "selector": "schema.additionalProperties=false",
            "repository": "example/api", "path": "openapi.yaml", "sha": "a" * 40,
            "url": f"{self.url}/repos/example/api/contents/openapi.yaml?ref={'b' * 40}",
        }
        self.server.state["contents_payload"] = {"encoding": "base64", "content": "!invalid!"}
        record = self.search.github_document("closed-object", item)
        self.assertEqual("acquisition-failure", record["disposition"])
        self.assertIn("invalid GitHub base64", str(record["diagnostic"]))
        self.server.state["malformed_tree"] = True
        publisher = {"repository": "example/api", "commit": "c" * 40,
                     "scope": "", "derivation": "local API publisher"}
        with self.assertRaisesRegex(SEARCH.SearchStopped, "malformed entries"):
            self.search.publisher_walk(publisher, {"closed-object": {"selector": "schema.additionalProperties=false"}})
        self.assertEqual(1, self.server.state["trees"])

    def test_publisher_raw_refusal_stays_outstanding(self) -> None:
        self.server.state["raw_status"] = 403
        publisher = {"repository": "example/api", "commit": "c" * 40,
                     "scope": "", "derivation": "local API publisher"}
        with self.assertRaisesRegex(SEARCH.SearchStopped, "publisher contents"):
            self.search.publisher_walk(publisher, {"closed-object": {"selector": "schema.additionalProperties=false"}})
        records = [json.loads(line) for line in (self.root / "documents.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual("acquisition-failure", records[-1]["status"])
        self.assertEqual(403, records[-1]["http_status"])

    def test_sourcegraph_http_error_stops_search(self) -> None:
        self.server.state["sourcegraph_status"] = 404
        with self.assertRaisesRegex(SEARCH.SearchStopped, "HTTP 404"):
            self.search.sourcegraph_search("closed-object", "additionalProperties")
        record = json.loads((self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()[-1])
        self.assertEqual("refused", record["outcome"])
        self.assertEqual(404, record["status"])

    def test_sourcegraph_paced_document_and_missing_identity(self) -> None:
        result = self.search.sourcegraph_document(
            "closed-object", "schema.additionalProperties=false",
            {"repository": "example/api", "path": "openapi.yaml", "commit": "c" * 40},
        )
        self.assertEqual("sourcegraph-paced", result["acquisition_route"])
        self.assertEqual("does-not-declare", result["disposition"])
        self.assertEqual(1, self.server.state["raw_hits"])
        missing = self.search.sourcegraph_document(
            "closed-object", "schema.additionalProperties=false",
            {"repository": "example/api", "path": "openapi.yaml"},
        )
        self.assertEqual("acquisition-failure", missing["disposition"])
        self.assertIn("lacks a repository", missing["diagnostic"])
        self.assertEqual(1, self.server.state["raw_hits"])
        self.server.state["raw_status"] = 404
        refused = self.search.sourcegraph_document(
            "closed-object", "schema.additionalProperties=false",
            {"repository": "example/api", "path": "openapi.yaml", "commit": "d" * 40},
        )
        self.assertEqual("acquisition-failure", refused["disposition"])
        self.assertEqual(404, refused["status"])

    def test_truncated_publisher_tree_descends_into_subtree(self) -> None:
        self.server.state["truncated_tree"] = True
        paths = self.search.scope_files("example/api", "c" * 40, "")
        self.assertEqual([{"path": "sub/openapi.yaml", "blob": "a" * 40}], paths)
        self.assertEqual(3, self.server.state["trees"])

    def test_raw_refusals_observe_retry_budget_with_invalid_retry_after(self) -> None:
        self.server.state["raw_status"] = 429
        with patch.object(SEARCH, "RAW_BACKOFF_BASE_S", 0.001), patch.object(SEARCH, "RAW_SPACING_S", 0):
            with self.assertRaisesRegex(SEARCH.SearchStopped, "five times"):
                self.search.raw_github_get(f"{self.url}/example/api/{'c' * 40}/openapi.yaml", "closed-object", "example/api/openapi.yaml")
        self.assertEqual(5, self.server.state["raw_hits"])
        waits = [json.loads(line) for line in (self.root / "raw-github-waits.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(4, len(waits))

    def test_cli_search_evaluate_walk_resume_and_failure_exits(self) -> None:
        script = REPO / "scripts/witness-search-github.py"
        evidence = self.root / "cli"
        derived = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evidence), "--derive-only"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, derived.returncode, derived.stderr)
        self.assertIn("FIXTURE gap keys", derived.stdout)
        recorded = json.loads((evidence / "keys.json").read_text(encoding="utf-8"))
        self.assertIn("annotated-ref-target-string-const", recorded["keys"])
        self.assertEqual("a" * 40, recorded["source_commit"])
        short_commit = subprocess.run(
            [sys.executable, str(script), "--source-commit", "abc123", "--evidence",
             str(self.root / "cli-short-commit"), "--derive-only"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(2, short_commit.returncode)
        self.assertIn("--source-commit must be a full 40-character", short_commit.stderr)
        invalid = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evidence)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(2, invalid.returncode)
        self.assertIn("--source and --stage", invalid.stderr)
        self.server.state["secondary"] = True
        env = {
            **os.environ,
            "CROZIER_GITHUB_API_URL": self.url,
            "GITHUB_TOKEN": "offline-test-token",
        }
        stopped = subprocess.run(
            [
                sys.executable,
                str(script),
                *SOURCE_COMMIT,
                "--evidence",
                str(evidence),
                "--source",
                "github-code-search",
                "--stage",
                "search",
                "--key",
                "annotated-ref-target-string-const",
            ],
            env=env,
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, stopped.returncode, stopped.stderr)
        self.assertIn("backoff before resuming", stopped.stderr)
        self.assertEqual(1, self.server.state["searches"])
        rows = [
            json.loads(line)
            for line in (evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual("refused", rows[-1]["outcome"])
        self.assertEqual(403, rows[-1]["status"])

        evaluation = self.root / "cli-evaluate"
        evaluation.mkdir()
        item = {
            "repository": "example/api",
            "path": "openapi.yaml",
            "sha": "a" * 40,
            "url": f"{self.url}/repos/example/api/contents/openapi.yaml?ref={'b' * 40}",
        }
        (evaluation / "queries.jsonl").write_text(
            json.dumps(
                {
                    "source": "github-code-search",
                    "key": "annotated-ref-target-string-const",
                    "query": "local API witness",
                    "outcome": "answered",
                    "results": [item],
                }
            )
            + "\n", encoding="utf-8"
        )
        before = self.server.state["contents"]
        command = [
            sys.executable,
            str(script),
            *SOURCE_COMMIT,
            "--evidence",
            str(evaluation),
            "--source",
            "github-code-search",
            "--stage",
            "evaluate",
            "--key",
            "annotated-ref-target-string-const",
        ]
        evaluated = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(0, evaluated.returncode, evaluated.stderr)
        candidate = json.loads(
            (evaluation / "candidates.jsonl").read_text(encoding="utf-8").splitlines()[0]
        )
        self.assertEqual("does-not-declare", candidate["disposition"])
        self.assertEqual(before + 1, self.server.state["contents"])
        resumed = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(0, resumed.returncode, resumed.stderr)
        self.assertEqual(before + 1, self.server.state["contents"])

        walk_evidence = self.root / "cli-walk"
        publisher_file = self.root / "publisher-set.json"
        publisher_file.write_text(json.dumps({"publishers": [
            {"repository": "example/api", "commit": "c" * 40,
             "scope": "", "derivation": "local API publisher"}
        ]}), encoding="utf-8")
        walked = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(walk_evidence),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-file", str(publisher_file)],
            env={**env, "CROZIER_RAW_GITHUB_URL": self.url},
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, walked.returncode, walked.stderr)
        self.assertEqual(1, len(json.loads((walk_evidence / "publisher-set.json").read_text(encoding="utf-8"))["publishers"]))
        document = json.loads((walk_evidence / "documents.jsonl").read_text(encoding="utf-8").splitlines()[0])
        self.assertEqual("readable", document["status"])
        self.assertEqual(64, len(document["sha256"]))

        invalid_key = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(self.root / "cli-key"),
             "--source", "github-code-search", "--stage", "search", "--key", "no-such-key"],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(2, invalid_key.returncode)
        self.assertIn("unknown key", invalid_key.stderr)
        invalid_regions = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(self.root / "cli-no-regions"),
             "--regions", str(self.root / "missing-regions"), "--derive-only"],
            capture_output=True, text=True,
        )
        self.assertEqual(1, invalid_regions.returncode)
        self.assertIn("repair the region file and rerun", invalid_regions.stderr)
        evidence_file = self.root / "evidence-is-a-file"
        evidence_file.write_text("occupied", encoding="utf-8")
        unwritable_evidence = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evidence_file), "--derive-only"],
            capture_output=True, text=True,
        )
        self.assertEqual(1, unwritable_evidence.returncode)
        self.assertIn("make --evidence and --cache writable", unwritable_evidence.stderr)
        if os.name != "nt":
            git_failure = self.root / "git-failure"
            git_failure.mkdir()
            fake_git = git_failure / "git"
            fake_git.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
            fake_git.chmod(0o755)
            no_commit = subprocess.run(
                [sys.executable, str(script), "--evidence", str(self.root / "cli-no-commit"),
                 "--derive-only"],
                env={**env, "PATH": str(git_failure)}, capture_output=True, text=True,
            )
            self.assertEqual(1, no_commit.returncode)
            self.assertIn("fetch origin/main or pass --source-commit", no_commit.stderr)
            git_only = self.root / "git-only"
            git_only.mkdir()
            git_binary = shutil.which("git")
            self.assertIsNotNone(git_binary)
            (git_only / "git").symlink_to(git_binary)
            no_credential_env = {**env, "PATH": str(git_only), "GITHUB_TOKEN": "", "GH_TOKEN": ""}
            no_credential = subprocess.run(
                [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(self.root / "cli-no-credential"),
                 "--source", "github-code-search", "--stage", "search",
                 "--key", "annotated-ref-target-string-const"],
                env=no_credential_env, capture_output=True, text=True,
            )
            self.assertEqual(1, no_credential.returncode)
            self.assertIn("set GITHUB_TOKEN or run gh auth login", no_credential.stderr)
        bad_publishers = self.root / "bad-publishers.json"
        bad_publishers.write_text('{"publishers": [{}]}', encoding="utf-8")
        invalid_file = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(self.root / "cli-bad-publishers"),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-file", str(bad_publishers)],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(2, invalid_file.returncode)
        self.assertIn("invalid publisher repository", invalid_file.stderr)
        bad_publishers.write_text('{"publishers": [{"repository": "publisher/api", "commit": "main", "scope": ""}]}', encoding="utf-8")
        mutable_ref = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(self.root / "cli-mutable-publisher"),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-file", str(bad_publishers)],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(2, mutable_ref.returncode)
        self.assertIn("publisher commit must be a 40-hex SHA", mutable_ref.stderr)
        bad_publishers.write_text("{broken json}", encoding="utf-8")
        invalid_json_file = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(self.root / "cli-bad-json-publishers"),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-file", str(bad_publishers)],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(2, invalid_json_file.returncode)
        self.assertIn("--publisher-file cannot be read", invalid_json_file.stderr)
        missing_catalog = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(self.root / "cli-missing-catalog"),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-root", str(self.root / "missing-catalog")],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(1, missing_catalog.returncode)
        self.assertIn("repair the publisher manifests and rerun", missing_catalog.stderr)
        for override in ("CROZIER_GITHUB_API_URL", "CROZIER_SOURCEGRAPH_URL", "CROZIER_RAW_GITHUB_URL"):
            with self.subTest(override=override):
                invalid_url = subprocess.run(
                    [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(self.root / f"cli-{override}"),
                     "--source", "sourcegraph", "--stage", "search",
                     "--key", "annotated-ref-target-string-const"],
                    env={**env, override: "file:///etc/passwd"},
                    capture_output=True, text=True,
                )
                self.assertEqual(2, invalid_url.returncode)
                self.assertIn(override, invalid_url.stderr)
                self.assertEqual("", invalid_url.stdout)

        self.server.state["malformed_tree"] = True
        walk_stopped = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(self.root / "cli-walk-stop"),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-file", str(publisher_file)],
            env={**env, "CROZIER_RAW_GITHUB_URL": self.url}, capture_output=True, text=True,
        )
        self.assertEqual(1, walk_stopped.returncode)
        self.assertIn("rerun --source github-publisher-trees --stage walk", walk_stopped.stderr)
        self.server.state["malformed_tree"] = False

        self.server.state["contents_status"] = 403
        evaluation_stop = self.root / "cli-evaluate-stop"
        evaluation_stop.mkdir()
        (evaluation_stop / "queries.jsonl").write_text((evaluation / "queries.jsonl").read_text(encoding="utf-8"), encoding="utf-8")
        stopped_evaluation = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evaluation_stop),
             "--source", "github-code-search", "--stage", "evaluate",
             "--key", "annotated-ref-target-string-const"],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(1, stopped_evaluation.returncode)
        self.assertIn("--stage evaluate", stopped_evaluation.stderr)

        self.server.state["sourcegraph_status"] = 404
        sourcegraph_stop = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(self.root / "cli-sourcegraph-stop"),
             "--source", "sourcegraph", "--stage", "search",
             "--key", "annotated-ref-target-string-const"],
            env={**env, "CROZIER_SOURCEGRAPH_URL": self.url}, capture_output=True, text=True,
        )
        self.assertEqual(1, sourcegraph_stop.returncode)
        self.assertIn("--stage search", sourcegraph_stop.stderr)

    def test_cli_evaluate_fetches_a_document_once_for_every_key_reaching_it(self) -> None:
        """Deduplication by repository, path and revision: one read, one row per key."""
        script = REPO / "scripts/witness-search-github.py"
        evaluation = self.root / "cli-shared"
        evaluation.mkdir()
        item = {
            "repository": "example/api",
            "path": "openapi.yaml",
            "sha": "a" * 40,
            "url": f"{self.url}/repos/example/api/contents/openapi.yaml?ref={'b' * 40}",
        }
        keys = tuple(sorted(SEARCH.derive_keys(REPO / "docs/openapi-surface"))[:2])
        (evaluation / "queries.jsonl").write_text("".join(
            json.dumps({"source": "github-code-search", "key": key, "query": f"q {key}",
                        "outcome": "answered", "results": [item]}) + "\n"
            for key in keys
        ), encoding="utf-8")
        env = {**os.environ, "CROZIER_GITHUB_API_URL": self.url, "GITHUB_TOKEN": "offline-test-token"}
        evaluated = subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evaluation),
             "--cache", str(self.root / "cli-shared-cache"), "--source", "github-code-search",
             "--stage", "evaluate", *(arg for key in keys for arg in ("--key", key))],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(0, evaluated.returncode, evaluated.stderr)
        self.assertEqual(1, self.server.state["contents"])
        rows = [json.loads(line) for line in (evaluation / "candidates.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(set(keys), {row["key"] for row in rows})
        self.assertEqual({"does-not-declare"}, {row["disposition"] for row in rows})
        self.assertEqual(1, len({row["sha256"] for row in rows}))
        self.assertEqual(1, sum("shared_with_key" in row for row in rows))
        self.assertFalse((evaluation / "documents").exists())

    def test_cli_evaluate_raw_route_downloads_at_the_commit_off_the_rest_buckets(self) -> None:
        """Exact-commit raw download: no contents read, paced lane, sharded identities."""
        script = REPO / "scripts/witness-search-github.py"
        evaluation = self.root / "cli-raw"
        evaluation.mkdir()
        items = [
            {"repository": "example/api", "path": path, "sha": "a" * 40,
             "url": f"{self.url}/repos/example/api/contents/{path}?ref={'b' * 40}"}
            for path in ("openapi.yaml", "v2/openapi.yaml", "v3/openapi.yaml", "v4/openapi.yaml")
        ]
        key = min(SEARCH.derive_keys(REPO / "docs/openapi-surface"))
        (evaluation / "queries.jsonl").write_text(json.dumps({
            "source": "github-code-search", "key": key,
            "query": "q", "outcome": "answered", "results": items}) + "\n", encoding="utf-8")
        env = {**os.environ, "CROZIER_GITHUB_API_URL": self.url, "CROZIER_RAW_GITHUB_URL": self.url,
               "GITHUB_TOKEN": "offline-test-token"}
        def run(*extra: str) -> subprocess.CompletedProcess:
            return subprocess.run(
                [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evaluation),
                 "--cache", str(self.root / "cli-raw-cache"), "--source", "github-code-search",
                 "--stage", "evaluate", "--key", key,
                 "--route", "raw", *extra],
                env=env, capture_output=True, text=True,
            )
        first = run("--shard", "0/2")
        self.assertEqual(0, first.returncode, first.stderr)
        second = run("--shard", "1/2")
        self.assertEqual(0, second.returncode, second.stderr)
        rows = [json.loads(line) for line in (evaluation / "candidates.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(sorted(item["path"] for item in items), sorted(row["path"] for row in rows))
        self.assertEqual({"pinned-raw-github"}, {row["acquisition_route"] for row in rows})
        self.assertTrue(all(row["raw_url"].endswith(f"/example/api/{'b' * 40}/{row['path']}") for row in rows))
        self.assertEqual(0, self.server.state["contents"])
        self.assertEqual(4, self.server.state["raw_hits"])
        again = run("--shard", "0/1")
        self.assertEqual(0, again.returncode, again.stderr)
        self.assertEqual(4, self.server.state["raw_hits"])
        refused = run("--shard", "2/2")
        self.assertEqual(2, refused.returncode)
        self.assertIn("--shard must be I/N", refused.stderr)

    def test_raw_route_refusal_waits_and_missing_commit_is_recorded(self) -> None:
        self.server.state["raw_refuse"] = True
        item = {"repository": "example/api", "path": "openapi.yaml", "sha": "a" * 40,
                "url": f"{self.url}/repos/example/api/contents/openapi.yaml?ref={'b' * 40}",
                "selector": "schema.additionalProperties=false"}
        record = self.search.github_document("closed-object", item, route="raw")
        self.assertNotEqual("acquisition-failure", record["disposition"])
        self.assertEqual(2, self.server.state["raw_hits"])
        waits = [json.loads(line) for line in (self.root / "raw-github-waits.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertTrue(any(row["cause"].startswith("HTTP 429") for row in waits))
        unpinned = self.search.github_document(
            "closed-object", {**item, "url": f"{self.url}/repos/example/api/contents/openapi.yaml"}, route="raw")
        self.assertEqual("acquisition-failure", unpinned["disposition"])
        self.assertIn("no commit SHA", unpinned["diagnostic"])

    def test_reused_acquisition_failure_is_recorded_for_each_key(self) -> None:
        failed = {"source": "sourcegraph", "key": "first", "repository": "example/api",
                  "path": "openapi.yaml", "commit": "c" * 40, "disposition": "acquisition-failure",
                  "status": 404, "diagnostic": "missing"}
        record = self.search.reuse(failed, "second", "schema.additionalProperties=false")
        self.assertEqual(("second", "acquisition-failure", 404, "first"),
                         (record["key"], record["disposition"], record["status"], record["shared_with_key"]))

    def test_cli_split_truncated_splits_through_the_guard_and_refuses_bad_bounds(self) -> None:
        script = REPO / "scripts/witness-search-github.py"
        evidence = self.root / "cli-split"
        key = min(SEARCH.derive_keys(REPO / "docs/openapi-surface"))
        env = {**os.environ, "CROZIER_GITHUB_API_URL": self.url, "GITHUB_TOKEN": "offline-test-token",
               "CROZIER_TEST_CODE_SEARCH_SPACING_S": "0.01"}
        run = lambda *extra: subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evidence),
             "--source", "github-code-search", "--stage", "search", "--key", key, *extra],
            env=env, capture_output=True, text=True)
        for flags, message in ((("--split-truncated-floor", "0"), "--split-truncated-floor must be a positive"),
                               (("--split-budget", "-1"), "--split-budget must not be negative")):
            with self.subTest(flags=flags):
                refused = run(*flags)
                self.assertEqual(2, refused.returncode)
                self.assertIn(message, refused.stderr)
        for bad in ("-1", "nan", "soon"):
            with self.subTest(spacing=bad):
                refused = subprocess.run(
                    [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evidence),
                     "--source", "github-code-search", "--stage", "search", "--key", key],
                    env={**env, "CROZIER_TEST_CODE_SEARCH_SPACING_S": bad}, capture_output=True, text=True)
                self.assertEqual(2, refused.returncode)
                self.assertIn("must be a non-negative number of seconds", refused.stderr)
        self.server.state["early_empty"] = True
        split = run("--split-truncated-floor", "400000", "--split-budget", "1")
        self.assertEqual(0, split.returncode, split.stderr)
        rows = [json.loads(line) for line in (evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()]
        outcomes = {row["outcome"] for row in rows}
        self.assertIn("partitioned", outcomes)
        self.assertIn("outstanding-index-truncation-floor", outcomes)
        self.assertFalse(any(row["outcome"] == "answered"
                             and row["retrieved_total"] >= row["result_count"] for row in rows))
        calls = [json.loads(line) for line in (evidence / "rate-limit-calls.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(self.server.state["searches"], sum(row.get("bucket") == "code_search" for row in calls))

    def test_cli_keeps_the_recorded_key_set_until_derive_only(self) -> None:
        """A stage run searches the key set it recorded, not today's gap rows."""
        script = REPO / "scripts/witness-search-github.py"
        evidence = self.root / "recorded-keys"
        evidence.mkdir()
        recorded = {"source_commit": "a" * 40, "derivation": "earlier branch point",
                    "keys": {"registered-since": {"region": "schemas", "selector": "schema.additionalProperties=false"}}}
        (evidence / "keys.json").write_text(json.dumps(recorded), encoding="utf-8")
        (evidence / "queries.jsonl").write_text("", encoding="utf-8")
        env = {**os.environ, "CROZIER_GITHUB_API_URL": self.url, "GITHUB_TOKEN": "offline-test-token"}
        run = lambda *extra: subprocess.run(
            [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evidence), *extra],
            env=env, capture_output=True, text=True)
        kept = run("--source", "github-code-search", "--stage", "evaluate", "--key", "registered-since")
        self.assertEqual(0, kept.returncode, kept.stderr)
        self.assertEqual(recorded, json.loads((evidence / "keys.json").read_text(encoding="utf-8")))
        (evidence / "keys.json").write_text(json.dumps({"keys": {"broken": {}}}), encoding="utf-8")
        broken = run("--source", "github-code-search", "--stage", "evaluate")
        self.assertEqual(1, broken.returncode)
        self.assertIn("rerun with --derive-only", broken.stderr)
        derived = run("--derive-only")
        self.assertEqual(0, derived.returncode, derived.stderr)
        self.assertEqual(set(SEARCH.derive_keys(REPO / "docs/openapi-surface")),
                         set(json.loads((evidence / "keys.json").read_text(encoding="utf-8"))["keys"]))

    def test_cli_rejects_corrupt_acquisition_ledgers(self) -> None:
        script = REPO / "scripts/witness-search-github.py"
        evidence = self.root / "bad-ledger"
        evidence.mkdir()
        command = [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evidence),
                   "--source", "github-code-search", "--stage", "evaluate",
                   "--key", "annotated-ref-target-string-const"]
        env = {**os.environ, "CROZIER_GITHUB_API_URL": self.url, "GITHUB_TOKEN": "offline-test-token"}
        (evidence / "queries.jsonl").write_text("{bad json}\n", encoding="utf-8")
        malformed = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(1, malformed.returncode)
        self.assertIn("queries.jsonl:1", malformed.stderr)
        self.assertIn("repair the named evidence file", malformed.stderr)
        (evidence / "queries.jsonl").write_text(json.dumps({
            "source": "github-code-search", "key": "annotated-ref-target-string-const",
            "query": "test", "outcome": "answered",
        }) + "\n", encoding="utf-8")
        missing_results = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(1, missing_results.returncode)
        self.assertIn("answered query lacks result identities", missing_results.stderr)
        (evidence / "queries.jsonl").write_text(json.dumps({
            "source": "github-code-search", "key": "annotated-ref-target-string-const",
            "query": "test", "outcome": "answered", "results": [],
        }) + "\n", encoding="utf-8")
        (evidence / "candidates.jsonl").write_text(json.dumps({
            "source": "github-code-search", "key": "annotated-ref-target-string-const",
            "repository": "example/api", "disposition": "does-not-declare",
        }) + "\n", encoding="utf-8")
        missing_identity = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(1, missing_identity.returncode)
        self.assertIn("candidates.jsonl:1: missing or invalid path", missing_identity.stderr)

    def test_search_transport_errors_leave_a_record(self) -> None:
        unavailable = "http://127.0.0.1:1"
        search = SEARCH.Acquirer(
            self.root / "transport", github_url=unavailable,
            sourcegraph_url=unavailable, code_search_spacing_s=0,
            sourcegraph_spacing_s=0,
        )
        with self.assertRaises(SEARCH.SearchStopped):
            search.github_search("closed-object", "additionalProperties")
        with self.assertRaises(SEARCH.SearchStopped):
            search.sourcegraph_search("closed-object", "additionalProperties")
        rows = [json.loads(line) for line in (self.root / "transport/queries.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(["acquisition-failure", "acquisition-failure"], [row["outcome"] for row in rows])

    def test_security_scheme_reference_is_counted_by_the_census_engine(self) -> None:
        document = b"""openapi: 3.0.3
info: {title: Security, version: 1.0.0}
paths: {}
components:
  securitySchemes:
    Alias: {$ref: '#/components/securitySchemes/Real'}
    Real: {type: http, scheme: bearer}
"""
        result = self.search.classify_and_record(
            {
                "source": "sourcegraph",
                "key": "securityscheme-ref",
                "selector": "securityScheme:$ref",
                "repository": "example/api",
                "path": "openapi.yaml",
                "commit": "a" * 40,
            },
            document,
        )
        self.assertEqual("declares", result["disposition"])
        self.assertEqual(1, result["selector_count"])
        self.assertNotIn("selector_method", result)
        self.assertIsNone(SEARCH.CENSUS.selector_error("securityScheme:$ref"))
        self.assertTrue((self.root / "documents" / result["document"]).is_file())

    def test_document_failures_keep_their_census_dispositions(self) -> None:
        publisher = {"repository": "example/api", "commit": "c" * 40,
                     "scope": "", "derivation": "local API publisher"}
        keys = {"closed-object": {"selector": "schema.additionalProperties=false"}}
        for label, document, expected in (
            ("old-version", b"swagger: '2.0'\npaths: {}\n", "excluded-non-openapi-3"),
            ("broken-yaml", b"openapi: 3.0.3\ninfo: [\n", "parse-failure"),
        ):
            with self.subTest(label=label):
                self.server.state["raw_document"] = document
                acquirer = SEARCH.Acquirer(
                    self.root / label, github_url=self.url, sourcegraph_url=self.url,
                    raw_github_url=self.url, code_search_spacing_s=0.01,
                    sourcegraph_spacing_s=0.01,
                )
                acquirer.publisher_walk(publisher, keys)
                tree_record = json.loads((self.root / label / "documents.jsonl").read_text(encoding="utf-8").splitlines()[0])
                self.assertEqual(expected, tree_record["status"])
                candidate = acquirer.sourcegraph_document(
                    "closed-object", "schema.additionalProperties=false",
                    {"repository": "example/api", "path": "openapi.yaml", "commit": "c" * 40},
                )
                self.assertEqual(expected, candidate["disposition"])
        self.server.state["raw_document"] = DOCUMENT
        unavailable = self.search.sourcegraph_document(
            "invalid-selector", "schema.not-a-selector",
            {"repository": "example/api", "path": "openapi.yaml", "commit": "c" * 40},
        )
        self.assertEqual("selector-unavailable", unavailable["disposition"])

    def test_index_truncation_remains_outstanding_on_resume(self) -> None:
        self.server.state["early_empty"] = True
        self.assertIsNone(
            self.search.github_search("closed-object", "additionalProperties")
        )
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual("outstanding-index-truncation", rows[-1]["outcome"])
        self.assertEqual(2, rows[-1]["reported"])
        self.assertEqual(1, rows[-1]["retrieved"])
        self.assertIsNone(
            self.search.github_search("closed-object", "additionalProperties")
        )
        self.assertEqual(2, self.server.state["searches"])

    def test_old_empty_page_is_marked_outstanding_on_resume(self) -> None:
        query = "additionalProperties"
        records = [
            {
                "source": "github-code-search",
                "key": "closed-object",
                "query": query,
                "outcome": "answered",
                "page": page,
                "page_count": count,
                "result_count": 2,
                "retrieved_total": 1,
                "results": [],
            }
            for page, count in ((1, 1), (2, 0))
        ]
        (self.root / "queries.jsonl").write_text(
            "".join(json.dumps(row) + "\n" for row in records), encoding="utf-8"
        )
        self.assertIsNone(self.search.github_search("closed-object", query))
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual("outstanding-index-truncation", rows[-1]["outcome"])
        self.assertEqual(0, self.server.state["searches"])

    def test_partition_walk_records_both_incomplete_children(self) -> None:
        self.server.state["partition"] = True
        self.server.state["early_empty"] = True
        self.assertIsNone(
            self.search.github_search("closed-object", "additionalProperties")
        )
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual(
            2, sum(row["outcome"] == "outstanding-index-truncation" for row in rows)
        )
        self.assertEqual(5, self.server.state["searches"])

    def test_large_code_search_is_partitioned_before_paging(self) -> None:
        self.server.state["partition"] = True
        results = self.search.github_search("closed-object", "additionalProperties")
        self.assertEqual(2, len(results))
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual("partitioned", rows[0]["outcome"])
        self.assertEqual(2, sum(row["outcome"] == "answered" for row in rows))
        self.assertEqual(3, self.server.state["searches"])

    def test_first_page_only_records_every_count_then_resumes_depth(self) -> None:
        """Breadth first: a count per query now, partitions and pages on resume."""
        self.server.state["partition"] = True
        breadth = SEARCH.Acquirer(
            self.root, github_url=self.url, sourcegraph_url=self.url,
            raw_github_url=self.url, code_search_spacing_s=0.01,
            sourcegraph_spacing_s=0.01, first_page_only=True,
        )
        self.assertIsNone(breadth.github_search("closed-object", "additionalProperties"))
        self.assertIsNone(breadth.github_search("closed-object", "additionalProperties"))
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual(["partitioned"], [row["outcome"] for row in rows])
        self.assertEqual(1001, rows[0]["reported"])
        self.assertEqual(1, self.server.state["searches"])
        results = self.search.github_search("closed-object", "additionalProperties")
        self.assertEqual(2, len(results))
        self.assertEqual(3, self.server.state["searches"])

    def test_first_page_only_stops_a_small_query_after_page_one(self) -> None:
        self.server.state["early_empty"] = True
        breadth = SEARCH.Acquirer(
            self.root, github_url=self.url, sourcegraph_url=self.url,
            raw_github_url=self.url, code_search_spacing_s=0.01,
            sourcegraph_spacing_s=0.01, first_page_only=True,
        )
        self.assertIsNone(breadth.github_search("closed-object", "additionalProperties"))
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual([("answered", 2, 1)], [
            (row["outcome"], row["result_count"], row["retrieved_total"]) for row in rows
        ])
        self.assertEqual(1, self.server.state["searches"])

    def test_contents_url_with_an_unescaped_space_is_read(self) -> None:
        item = {
            "repository": "example/api",
            "path": "open api.yaml",
            "sha": "a" * 40,
            "url": f"{self.url}/repos/example/api/contents/open api.yaml?ref={'b' * 40}",
            "selector": "schema.additionalProperties=false",
        }
        record = self.search.github_document("closed-object", item)
        self.assertNotEqual("acquisition-failure", record["disposition"])
        self.assertEqual(1, self.server.state["contents"])

    def test_truncated_window_is_split_until_its_floor_within_budget(self) -> None:
        """An empty page before the reported count splits the window by size."""
        self.server.state["early_empty"] = True
        split = SEARCH.Acquirer(
            self.root, github_url=self.url, sourcegraph_url=self.url, raw_github_url=self.url,
            code_search_spacing_s=0.01, sourcegraph_spacing_s=0.01,
            split_truncated_floor=100001, split_budget=1,
        )
        self.assertIsNone(split._github_window("closed-object", "q size:0..199999", 0, 199999))
        rows = [json.loads(line) for line in (self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()]
        outcomes = [(row["query"], row["outcome"]) for row in rows]
        self.assertIn(("q size:0..199999", "outstanding-index-truncation"), outcomes)
        self.assertIn(("q size:0..199999", "partitioned"), outcomes)
        partition = next(row for row in rows if row["outcome"] == "partitioned")
        self.assertEqual(2, partition["reported"])
        self.assertEqual(["q size:0..99998", "q size:99999..199999"], [w["query"] for w in partition["windows"]])
        # Both halves truncate again; each is no wider than the floor, so each is
        # recorded at the floor and neither is split nor marked answered.
        floors = [row for row in rows if row["outcome"] == "outstanding-index-truncation-floor"]
        self.assertEqual({"q size:0..99998", "q size:99999..199999"}, {row["query"] for row in floors})
        self.assertEqual({(2, 1)}, {(row["reported"], row["retrieved"]) for row in floors})
        # Every index-limit row written carries the fields the index reads its reason from.
        for row in rows:
            for field in SEARCH.INDEX_LIMIT_FIELDS.get(row["outcome"], ()):
                self.assertIsInstance(row[field], int, (row["outcome"], field))
        self.assertLessEqual(set(SEARCH.INDEX_LIMIT_FIELDS), set(SEARCH.ANSWER_OUTCOMES))
        spent = SEARCH.Acquirer(
            self.root / "spent", github_url=self.url, sourcegraph_url=self.url, raw_github_url=self.url,
            code_search_spacing_s=0.01, sourcegraph_spacing_s=0.01,
            split_truncated_floor=1, split_budget=0,
        )
        self.assertIsNone(spent._github_window("closed-object", "q", 0, None))
        rows = [json.loads(line) for line in (self.root / "spent/queries.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual("outstanding-index-truncation", rows[-1]["outcome"])
        self.assertFalse(any(row["outcome"] == "partitioned" for row in rows))

    def test_unsplittable_index_window_stays_outstanding(self) -> None:
        self.assertIsNone(self.search._partition_window("closed-object", "additionalProperties size:1..1", 1, 1, 1001))
        record = json.loads((self.root / "queries.jsonl").read_text(encoding="utf-8").splitlines()[-1])
        self.assertEqual("outstanding-index-cap", record["outcome"])
        self.assertEqual(1, record["size"])
        self.assertEqual(0, self.server.state["searches"])

    def test_publisher_tree_lists_and_censuses_every_spec_path(self) -> None:
        publisher = {
            "repository": "example/api",
            "commit": "c" * 40,
            "scope": "",
            "derivation": "local API publisher",
        }
        keys = {"closed-object": {"selector": "schema.additionalProperties=false"}}
        self.search.publisher_walk(publisher, keys)
        trees = [
            json.loads(x) for x in (self.root / "trees.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        documents = [
            json.loads(x)
            for x in (self.root / "documents.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual(1, trees[0]["candidate_document_count"])
        self.assertEqual("openapi.yaml", documents[0]["path"])
        self.assertEqual(0, documents[0]["selector_counts"]["closed-object"])
        self.assertEqual(1, self.server.state["trees"])
        self.assertEqual(1, self.server.state["raw_hits"])
        self.assertEqual(0, self.server.state["contents"])
        self.search.publisher_walk(publisher, keys)
        self.assertEqual(1, self.server.state["trees"])
        self.assertEqual(1, self.server.state["raw_hits"])
        self.assertEqual(1, len((self.root / "documents.jsonl").read_text(encoding="utf-8").splitlines()))

    def test_missing_named_publisher_scope_is_measured_without_losing_siblings(
        self,
    ) -> None:
        publisher = {
            "repository": "example/api",
            "commit": "c" * 40,
            "scope": ["", "missing"],
            "derivation": "local API publisher",
        }
        self.search.publisher_walk(publisher, {})
        tree = json.loads((self.root / "trees.jsonl").read_text(encoding="utf-8").splitlines()[0])
        self.assertEqual(1, tree["candidate_document_count"])
        self.assertIn("missing", tree["missing_scopes"][0])

    def test_large_contents_use_the_same_guarded_contents_endpoint(self) -> None:
        self.server.state["large"] = True
        path = "/repos/example/api/contents/openapi.yaml?ref=" + "c" * 40
        status, data, evidence = self.search.github_contents(path)
        self.assertEqual(200, status)
        self.assertEqual(DOCUMENT, data)
        self.assertEqual("application/vnd.github.raw+json", evidence["raw_media_type"])
        self.assertEqual(2, self.server.state["contents"])

    def test_large_contents_metadata_fallback_is_an_acquisition_failure(self) -> None:
        self.server.state["large"] = True
        self.server.state["raw_metadata"] = True
        item = {
            "selector": "schema.additionalProperties=false",
            "repository": "example/api", "path": "openapi.yaml", "sha": "a" * 40,
            "url": f"{self.url}/repos/example/api/contents/openapi.yaml?ref={'b' * 40}",
        }
        result = self.search.github_document("closed-object", item)
        self.assertEqual("acquisition-failure", result["disposition"])
        self.assertIn("raw_media_type_response", result["diagnostic"])
        self.assertEqual(2, self.server.state["contents"])

    def test_sourcegraph_refusal_then_spacing_are_waited_out(self) -> None:
        self.server.state["refuse_sourcegraph"] = True
        # Windows wide enough that a slow runner still reaches the next
        # acquire inside them; at 0.05s a macOS runner outlasted both.
        lane = guard_module.PacedLane(
            spacing_s=1.0, backoff_base_s=1.0, attempt_budget=5
        )
        with patch.dict(guard_module.PACED_LANES, {"sourcegraph": lane}):
            self.assertEqual(
                [], self.search.sourcegraph_search("closed-object", "first")
            )
            self.assertEqual(
                [], self.search.sourcegraph_search("closed-object", "second")
            )
        waits = self.search.guards["sourcegraph"].waits()
        self.assertTrue(any(row.get("cause") == "backoff" for row in waits))
        self.assertTrue(any(row.get("cause") == "spacing" for row in waits))
        self.assertEqual(3, self.server.state["sourcegraph"])
        index_waits = [
            json.loads(line)
            for line in (self.root / "index-pacing-waits.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
        ]
        self.assertTrue(any(row["cause"] == "refusal-cooldown" for row in index_waits))
        self.assertEqual(
            1, len((self.root / "refusals.jsonl").read_text(encoding="utf-8").splitlines())
        )

    def test_sourcegraph_github_match_uses_pinned_raw_route_and_waits(self) -> None:
        self.server.state["raw_refuse"] = True
        item = {
            "repository": "github.com/example/api",
            "path": "openapi.yaml",
            "commit": "c" * 40,
        }
        # Spacing wide enough that parsing the first document still ends
        # inside it; at 0.05s a Windows runner outlasted the window.
        with patch.object(SEARCH, "RAW_SPACING_S", 1.0), patch.object(
            SEARCH, "RAW_BACKOFF_BASE_S", 0.05
        ):
            result = self.search.sourcegraph_document(
                "closed-object", "schema.additionalProperties=false", item
            )
            self.search.sourcegraph_document(
                "closed-object", "schema.additionalProperties=false", item
            )
        self.assertEqual("pinned-raw-github", result["acquisition_route"])
        self.assertEqual("does-not-declare", result["disposition"])
        self.assertEqual(3, self.server.state["raw_hits"])
        waits = [
            json.loads(x)
            for x in (self.root / "raw-github-waits.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertTrue(any("backoff" in row["cause"] for row in waits))
        self.assertTrue(any(row["cause"] == "spacing" for row in waits))

    def test_exact_commit_raw_download_retries_incomplete_transfer(self) -> None:
        self.server.state["raw_incomplete_remaining"] = 2
        url = self.url + "/example/api/" + "c" * 40 + "/openapi.yaml"
        with patch.object(SEARCH, "RAW_SPACING_S", 0.01), patch.object(
            SEARCH, "RAW_BACKOFF_BASE_S", 0.01
        ):
            status, document = self.search.raw_github_get(
                url, "publisher-trees", "example/api/openapi.yaml"
            )
        self.assertEqual(200, status)
        self.assertEqual(DOCUMENT, document)
        self.assertEqual(3, self.server.state["raw_hits"])
        calls = [
            json.loads(line)
            for line in (self.root / "raw-github-calls.jsonl").read_text(encoding="utf-8").splitlines()
        ]
        self.assertEqual(2, sum(row["status"] == "IncompleteRead" for row in calls))
        completed = [row for row in calls if row["status"] == 200]
        self.assertEqual(1, len(completed))
        self.assertEqual("c" * 40, completed[0]["commit"])
        self.assertEqual(hashlib.sha256(DOCUMENT).hexdigest(), completed[0]["sha256"])

    def test_publisher_transfer_failure_stays_outstanding_after_retry_budget(
        self,
    ) -> None:
        self.server.state["raw_incomplete_remaining"] = 3
        publisher = {
            "repository": "example/api",
            "commit": "c" * 40,
            "scope": "",
            "derivation": "local API publisher",
        }
        with patch.object(SEARCH, "RAW_SPACING_S", 0.01), patch.object(
            SEARCH, "RAW_BACKOFF_BASE_S", 0.01
        ):
            self.search.publisher_walk(publisher, {})
        document = json.loads(
            (self.root / "documents.jsonl").read_text(encoding="utf-8").splitlines()[0]
        )
        self.assertEqual("acquisition-failure", document["status"])
        self.assertIn("IncompleteRead after 3 attempts", document["diagnostic"])
        self.assertEqual(3, self.server.state["raw_hits"])

    def test_newer_openapi_three_document_is_censused(self) -> None:
        self.server.state["raw_document"] = DOCUMENT.replace(
            b"openapi: 3.0.3", b"openapi: 3.2.0"
        ).replace(
            b"type: string", b"type: object\n          additionalProperties: false"
        )
        result = self.search.sourcegraph_document(
            "closed-object",
            "schema.additionalProperties=false",
            {
                "repository": "github.com/example/api",
                "path": "openapi.yaml",
                "commit": "c" * 40,
            },
        )
        self.assertEqual("declares", result["disposition"])
        self.assertEqual(1, result["selector_count"])

    def test_outstanding_inventory_is_derived_from_the_ledgers(self) -> None:
        """Unissued, partly paged and refused queries and unwalked trees stay owed."""
        root = self.root / "inventory"
        code = root / "witness-search-github-code-search"
        trees = root / "witness-search-github-publisher-trees"
        sourcegraph = root / "witness-search-sourcegraph"
        selector = "schema.additionalProperties=false"
        for directory in (code, trees, sourcegraph):
            directory.mkdir(parents=True)
            (directory / "keys.json").write_text(json.dumps({"keys": {"shape": {"selector": selector}}}), encoding="utf-8")
        (trees / "publisher-set.json").write_text(json.dumps({"publishers": [
            {"repository": "example/api", "commit": "c" * 40},
            {"repository": "example/unlisted", "commit": "d" * 40},
        ]}), encoding="utf-8")
        (trees / "trees.jsonl").write_text(json.dumps({
            "repository": "example/api", "commit": "c" * 40,
            "paths": [{"path": "openapi.yaml", "blob": "f" * 40}],
        }) + "\n", encoding="utf-8")
        plan = SEARCH.query_plan(selector)
        first, second = plan["github-code-search"][:2]
        (code / "queries.jsonl").write_text("".join(json.dumps(row) + "\n" for row in (
            {"source": "github-code-search", "key": "shape", "query": first, "outcome": "answered",
             "page": 1, "result_count": 150, "retrieved_total": 100, "results": []},
            {"source": "github-code-search", "key": "shape", "query": second, "outcome": "refused",
             "page": 1, "status": 403, "diagnostic": "secondary rate limit"},
        )), encoding="utf-8")
        sg_first = plan["sourcegraph"][0]
        (sourcegraph / "queries.jsonl").write_text(json.dumps(
            {"source": "sourcegraph", "key": "shape", "query": sg_first, "outcome": "answered",
             "result_count": 0, "results": []}) + "\n", encoding="utf-8")
        command = [sys.executable, str(REPO / "scripts/witness-search-github-index.py"),
                   "--evidence-root", str(root)]
        subprocess.run(command, check=True, capture_output=True, text=True)
        with (root / "witness-search-github/outstanding.tsv").open(encoding="utf-8") as stream:
            rows = {row["source"]: row for row in csv.DictReader(stream, delimiter="\t")}
        code_row = rows["github-code-search"]
        self.assertEqual("search-incomplete", code_row["outcome"])
        self.assertEqual(str(len(plan["github-code-search"])), code_row["planned_queries"])
        self.assertEqual("0", code_row["answered_queries"])
        self.assertEqual(plan["github-code-search"][2:], json.loads(code_row["unissued_queries"]))
        self.assertEqual([first, second], [q["query"] for q in json.loads(code_row["issued_incomplete"])])
        refusal = json.loads(code_row["refusals"])
        self.assertEqual([(second, "refused", 403)], [(r["query"], r["outcome"], r["status"]) for r in refusal])
        self.assertEqual(
            ["example/api@" + "c" * 40 + ": 1 documents outstanding",
             "example/unlisted@" + "d" * 40 + ": tree not listed"],
            json.loads(rows["github-publisher-trees"]["unwalked_trees"]),
        )
        index = {
            (row[1], row[2]): row[3]
            for row in (line.split("\t") for line in
                        (code / "search-index.tsv").read_text(encoding="utf-8").splitlines()[1:])
        }
        self.assertEqual("150 (100 retrieved)", index[("query", first)])
        self.assertTrue(index[("query", second)].startswith("no answer yet: refused HTTP 403"))
        walks = [line.split("\t") for line in (trees / "search-index.tsv").read_text(encoding="utf-8").splitlines()[1:]]
        self.assertIn(["shape", "walk", "example/api@" + "c" * 40, "1 (0 censused)", "documents.jsonl"], walks)
        self.assertEqual("1", rows["sourcegraph"]["answered_queries"])
        self.assertEqual([plan["sourcegraph"][1]], json.loads(rows["sourcegraph"]["unissued_queries"]))
        subprocess.run([*command, "--check"], check=True, capture_output=True)
        (sourcegraph / "queries.jsonl").write_text("".join(json.dumps(
            {"source": "sourcegraph", "key": "shape", "query": query, "outcome": "answered",
             "result_count": 0, "results": []}) + "\n" for query in plan["sourcegraph"]), encoding="utf-8")
        subprocess.run(command, check=True, capture_output=True, text=True)
        with (root / "witness-search-github/outstanding.tsv").open(encoding="utf-8") as stream:
            rows = {row["source"]: row for row in csv.DictReader(stream, delimiter="\t")}
        self.assertEqual("none-found", rows["sourcegraph"]["outcome"])
        self.assertEqual("[]", rows["sourcegraph"]["refusals"])
        fresh = subprocess.run([*command, "--check"], capture_output=True, text=True)
        self.assertEqual(0, fresh.returncode, fresh.stderr)
        (code / "queries.jsonl").write_text("", encoding="utf-8")
        drifted = subprocess.run([*command, "--check"], capture_output=True, text=True)
        self.assertEqual(1, drifted.returncode)
        self.assertIn("outstanding.tsv", drifted.stderr)

    def test_consolidated_index_tracks_source_verdicts_and_unfetched_results(
        self,
    ) -> None:
        root = self.root / "index"
        code = root / "witness-search-github-code-search"
        trees = root / "witness-search-github-publisher-trees"
        sourcegraph = root / "witness-search-sourcegraph"
        for directory in (code, trees, sourcegraph):
            directory.mkdir(parents=True)
            (directory / "keys.json").write_text(json.dumps(
                {"keys": {"shape": {"selector": "schema.additionalProperties=false"}}}
            ), encoding="utf-8")
        (trees / "publisher-set.json").write_text(json.dumps({"publishers": []}), encoding="utf-8")
        identity = {
            "repository": "example/api",
            "path": "openapi.yaml",
            "commit": "c" * 40,
            "sha256": "d" * 64,
        }
        (code / "candidates.jsonl").write_text(
            json.dumps(
                {
                    **identity,
                    "source": "github-code-search",
                    "key": "shape",
                    "blob": "e" * 40,
                    "disposition": "declares",
                    "selector_count": 1,
                }
            )
            + "\n", encoding="utf-8"
        )
        (code / "queries.jsonl").write_text(
            json.dumps(
                {
                    "source": "github-code-search",
                    "key": "shape",
                    "query": "local index witness",
                    "outcome": "answered",
                    "results": [
                        {
                            "repository": "example/api",
                            "path": "openapi.yaml",
                            "sha": "e" * 40,
                        },
                        {
                            "repository": "example/other",
                            "path": "openapi.yaml",
                            "sha": "e" * 40,
                        }
                    ],
                }
            )
            + "\n", encoding="utf-8"
        )
        (trees / "documents.jsonl").write_text(
            json.dumps(
                {**identity, "source": "github-publisher-trees", "status": "readable", "selector_counts": {"shape": 1}}
            )
            + "\n", encoding="utf-8"
        )
        (sourcegraph / "candidates.jsonl").write_text(
            json.dumps(
                {
                    **identity,
                    "source": "sourcegraph",
                    "key": "shape",
                    "disposition": "declares",
                    "selector_count": 1,
                }
            )
            + "\n", encoding="utf-8"
        )
        (sourcegraph / "screens.jsonl").write_text(
            json.dumps(
                {
                    **identity,
                    "source": "sourcegraph",
                    "keys": ["shape"],
                    "license": "passed: publisher grant",
                    "ref": "passed: immutable",
                    "fern": "passed: generated SDK",
                    "disposition": "witness-found",
                }
            )
            + "\n", encoding="utf-8"
        )
        command = [
            sys.executable,
            str(REPO / "scripts/witness-search-github-index.py"),
            "--evidence-root",
            str(root),
        ]
        first_index = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(0, first_index.returncode, first_index.stderr)
        with (root / "witness-search-github/candidates.tsv").open(encoding="utf-8") as stream:
            indexed = list(csv.DictReader(stream, delimiter="\t"))
        self.assertEqual(4, len(indexed))
        self.assertEqual(
            {"github-code-search", "github-publisher-trees", "sourcegraph"},
            {row["source"] for row in indexed},
        )
        witness = next(row for row in indexed if row["source"] == "sourcegraph")
        self.assertEqual("witness-found", witness["disposition"])
        self.assertEqual("pass", witness["fern_screen"])
        pending = next(
            row for row in indexed if row["candidate"] == "example/other:openapi.yaml"
        )
        self.assertEqual("outstanding", pending["disposition"])
        self.assertEqual("not-fetched", pending["digest"])
        subprocess.run([*command, "--check"], check=True, capture_output=True)
        (code / "closure-shape.json").write_text(json.dumps({"witness": "example/api"}), encoding="utf-8")
        subprocess.run(command, check=True, capture_output=True, text=True)
        with (root / "witness-search-github/candidates.tsv").open(encoding="utf-8") as stream:
            closed_rows = list(csv.DictReader(stream, delimiter="\t"))
        closed = next(row for row in closed_rows if row["candidate"] == "example/other:openapi.yaml")
        self.assertEqual("not-owed", closed["disposition"])
        with (code / "candidates.jsonl").open("a", encoding="utf-8") as stream:
            stream.write(json.dumps({**identity, "repository": "example/unavailable",
                                     "source": "github-code-search", "key": "shape", "disposition": "selector-unavailable",
                                     "diagnostic": "selector unavailable"}) + "\n")
        subprocess.run(command, check=True, capture_output=True, text=True)
        with (root / "witness-search-github/candidates.tsv").open(encoding="utf-8") as stream:
            unavailable = next(row for row in csv.DictReader(stream, delimiter="\t")
                               if row["candidate"] == "example/unavailable:openapi.yaml")
        self.assertEqual("outstanding", unavailable["disposition"])
        (trees / "trees.jsonl").write_text(json.dumps({
            "repository": "example/api", "commit": "c" * 40,
            "paths": [{"path": "unfetched.yaml", "blob": "f" * 40}],
        }) + "\n", encoding="utf-8")
        subprocess.run(command, check=True, capture_output=True, text=True)
        with (root / "witness-search-github/candidates.tsv").open(encoding="utf-8") as stream:
            walked = next(row for row in csv.DictReader(stream, delimiter="\t")
                          if row["candidate"] == "example/api:unfetched.yaml")
        self.assertEqual("outstanding", walked["disposition"])
        self.assertEqual("not-fetched", walked["digest"])
        (sourcegraph / "screens.jsonl").write_text(
            (sourcegraph / "screens.jsonl")
            .read_text(encoding="utf-8")
            .replace("witness-found", "fern-rejected"), encoding="utf-8"
        )
        failed = subprocess.run([*command, "--check"], capture_output=True, text=True)
        self.assertEqual(1, failed.returncode)
        self.assertEqual("", failed.stdout)
        self.assertIn(
            "rerun scripts/witness-search-github-index.py without --check",
            failed.stderr,
        )
        (code / "keys.json").unlink()
        missing_keys = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, missing_keys.returncode)
        self.assertIn("inspect the source evidence and rerun", missing_keys.stderr)
        (code / "keys.json").write_text(json.dumps({"keys": "shape"}), encoding="utf-8")
        malformed_keys = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, malformed_keys.returncode)
        self.assertIn("keys must be a mapping", malformed_keys.stderr)
        (code / "keys.json").write_text(json.dumps(
            {"keys": {"shape": {"selector": "schema.additionalProperties=false"}}}
        ), encoding="utf-8")
        valid_candidates = (code / "candidates.jsonl").read_text(encoding="utf-8")
        (code / "candidates.jsonl").write_text('"not an object"\n', encoding="utf-8")
        invalid_record = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, invalid_record.returncode)
        self.assertIn("candidates.jsonl:1: expected a JSON object", invalid_record.stderr)
        (code / "candidates.jsonl").write_text(valid_candidates, encoding="utf-8")
        screens_path = sourcegraph / "screens.jsonl"
        valid_screen = json.loads(screens_path.read_text(encoding="utf-8").splitlines()[0])
        screens_path.write_text(json.dumps({**valid_screen, "license": 7}) + "\n", encoding="utf-8")
        bad_screen = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, bad_screen.returncode)
        self.assertIn("screens.jsonl:1: missing or invalid license", bad_screen.stderr)
        screens_path.write_text(json.dumps(valid_screen) + "\n", encoding="utf-8")
        documents_path = trees / "documents.jsonl"
        valid_document = json.loads(documents_path.read_text(encoding="utf-8").splitlines()[0])
        documents_path.write_text(json.dumps({**valid_document, "selector_counts": []}) + "\n", encoding="utf-8")
        bad_counts = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, bad_counts.returncode)
        self.assertIn("documents.jsonl:1: invalid selector_counts", bad_counts.stderr)
        documents_path.write_text(json.dumps(valid_document) + "\n", encoding="utf-8")
        (trees / "trees.jsonl").write_text(json.dumps({
            "repository": "example/api", "commit": "c" * 40,
            "paths": [{"path": "openapi.yaml"}],
        }) + "\n", encoding="utf-8")
        bad_tree = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, bad_tree.returncode)
        self.assertIn("trees.jsonl:1: invalid publisher tree paths", bad_tree.stderr)

    def test_an_oversized_parser_diagnostic_is_cited_not_copied(self) -> None:
        row = {"repository": "example/api", "path": "openapi.yaml", "commit": "c" * 40,
               "sha256": "d" * 64, "disposition": "parse-failure", "diagnostic": "x" * 200000}
        record = SEARCH.INDEX.classify("sourcegraph", "shape", row, "candidates.jsonl:1", {})
        self.assertLess(len(record["census"]), 3000)
        self.assertIn("200000 characters; whole text in the ledger row", record["census"])
        self.assertEqual("outstanding", record["disposition"])

    def test_partition_windows_decide_completeness_and_report_their_refusals(self) -> None:
        """A partitioned query is complete only when every window is; a refused window is named."""
        root = self.root / "windows"
        selector = "schema.additionalProperties=false"
        for source in ("github-code-search", "github-publisher-trees", "sourcegraph"):
            (root / f"witness-search-{source}").mkdir(parents=True)
            (root / f"witness-search-{source}/keys.json").write_text(json.dumps({"keys": {"shape": {"selector": selector}}}), encoding="utf-8")
        (root / "witness-search-github-publisher-trees/publisher-set.json").write_text(json.dumps({"publishers": []}), encoding="utf-8")
        query = SEARCH.query_plan(selector)["github-code-search"][0]
        low, high = f"{query} size:0..99", f"{query} size:>=100"
        partition = {"source": "github-code-search", "key": "shape", "query": query, "outcome": "partitioned",
                     "reported": 1500, "windows": [{"query": low, "lower": 0, "upper": 99},
                                                   {"query": high, "lower": 100, "upper": None}]}
        answered = lambda q: {"source": "github-code-search", "key": "shape", "query": q, "outcome": "answered",
                              "page": 1, "result_count": 1, "retrieved_total": 1, "results": []}
        refused = {"source": "github-code-search", "key": "shape", "query": high, "outcome": "refused",
                   "page": 1, "status": 403, "at": "2026-09-25T00:00:00+00:00", "diagnostic": "secondary"}
        ledger = root / "witness-search-github-code-search/queries.jsonl"
        command = [sys.executable, str(REPO / "scripts/witness-search-github-index.py"), "--evidence-root", str(root)]

        def row() -> dict[str, str]:
            subprocess.run(command, check=True, capture_output=True, text=True)
            with (root / "witness-search-github/outstanding.tsv").open(encoding="utf-8") as stream:
                return next(r for r in csv.DictReader(stream, delimiter="\t") if r["source"] == "github-code-search")

        ledger.write_text("".join(json.dumps(r) + "\n" for r in (partition, answered(low), refused)), encoding="utf-8")
        pending = row()
        self.assertEqual(["partitioned"], [q["outcome"] for q in json.loads(pending["issued_incomplete"])])
        self.assertEqual([(high, "refused", 403)], [(r["query"], r["outcome"], r["status"]) for r in json.loads(pending["refusals"])])
        self.assertEqual("0", pending["answered_queries"])
        ledger.write_text("".join(json.dumps(r) + "\n" for r in (partition, answered(low), refused, answered(high))), encoding="utf-8")
        settled = row()
        self.assertEqual("1", settled["answered_queries"])
        self.assertEqual("[]", settled["refusals"])
        self.assertEqual("[]", settled["issued_incomplete"])
        index = {tuple(line.split("\t")[1:3]): line.split("\t")[3] for line in
                 (root / "witness-search-github-code-search/search-index.tsv").read_text(encoding="utf-8").splitlines()[1:]}
        self.assertEqual("1500 (partitioned by size)", index[("query", query)])

    def test_retained_windows_carry_their_concrete_index_limit(self) -> None:
        """A truncated, floored or capped window stays incomplete and says why."""
        root = self.root / "limits"
        selector = "schema.additionalProperties=false"
        for source in ("github-code-search", "github-publisher-trees", "sourcegraph"):
            (root / f"witness-search-{source}").mkdir(parents=True)
            (root / f"witness-search-{source}/keys.json").write_text(json.dumps({"keys": {"shape": {"selector": selector}}}), encoding="utf-8")
        (root / "witness-search-github-publisher-trees/publisher-set.json").write_text(json.dumps({"publishers": []}), encoding="utf-8")
        plan = SEARCH.query_plan(selector)["github-code-search"]
        base = {"source": "github-code-search", "key": "shape"}
        answered = lambda q, n: {**base, "query": q, "outcome": "answered", "page": 1,
                                 "result_count": n, "retrieved_total": n - 1, "results": []}
        rows = [
            answered(plan[0], 10),
            {**base, "query": plan[0], "outcome": "outstanding-index-truncation", "reported": 10, "retrieved": 9, "page": 2},
            answered(plan[1], 10),
            {**base, "query": plan[1], "outcome": "outstanding-index-truncation", "reported": 10, "retrieved": 9, "page": 2},
            {**base, "query": plan[1], "outcome": "outstanding-index-truncation-floor", "reported": 10,
             "retrieved": 9, "lower": 0, "upper": 199, "floor": 256},
            {**base, "query": plan[2], "outcome": "partitioned", "reported": 5000,
             "windows": [{"query": plan[2] + " size:7..7", "lower": 7, "upper": 7}]},
            {**base, "query": plan[2] + " size:7..7", "outcome": "outstanding-index-cap", "reported": 1200, "size": 7},
            answered(plan[3], 10),
            {**base, "query": plan[3], "outcome": "outstanding-incomplete-results"},
        ]
        (root / "witness-search-github-code-search/queries.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
        subprocess.run([sys.executable, str(REPO / "scripts/witness-search-github-index.py"), "--evidence-root", str(root)],
                       check=True, capture_output=True, text=True)
        with (root / "witness-search-github/outstanding.tsv").open(encoding="utf-8") as stream:
            line = next(r for r in csv.DictReader(stream, delimiter="\t") if r["source"] == "github-code-search")
        self.assertEqual("0", line["answered_queries"])
        reasons = {q["query"]: [w["reason"] for w in q["windows"]] for q in json.loads(line["issued_incomplete"])}
        self.assertEqual(["GitHub reported 10 and served 9 before an empty page 2; not yet split by size"], reasons[plan[0]])
        self.assertEqual(["GitHub reported 10 and served 9 in a 200-byte window, at or under the 256-byte split floor"], reasons[plan[1]])
        self.assertEqual(["a window of files of 7 bytes still reports 1200 results, over the 1,000 GitHub pages"], reasons[plan[2]])
        self.assertEqual(["GitHub flagged the response incomplete_results"], reasons[plan[3]])
        self.assertEqual("[]", line["refusals"])

    def test_unread_windows_and_pages_state_why_they_stayed_unread(self) -> None:
        """An unissued window or an unrequested page is outstanding with its cause, never silent."""
        root = self.root / "unread"
        selector = "schema.additionalProperties=false"
        for source in ("github-code-search", "github-publisher-trees", "sourcegraph"):
            (root / f"witness-search-{source}").mkdir(parents=True)
            (root / f"witness-search-{source}/keys.json").write_text(json.dumps({"keys": {"shape": {"selector": selector}}}), encoding="utf-8")
        (root / "witness-search-github-publisher-trees/publisher-set.json").write_text(json.dumps({"publishers": []}), encoding="utf-8")
        plan = SEARCH.query_plan(selector)["github-code-search"]
        base = {"source": "github-code-search", "key": "shape"}
        rows = [
            {**base, "query": plan[0], "outcome": "partitioned", "reported": 5000,
             "windows": [{"query": plan[0] + " size:0..99", "lower": 0, "upper": 99}]},
            {**base, "query": plan[1], "outcome": "answered", "page": 1, "page_count": 100,
             "result_count": 250, "retrieved_total": 100, "results": []},
            {**base, "query": plan[2], "outcome": "answered", "page": 3, "page_count": 0,
             "result_count": 230, "retrieved_total": 228, "results": []},
        ]
        (root / "witness-search-github-code-search/queries.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
        command = [sys.executable, str(REPO / "scripts/witness-search-github-index.py"), "--evidence-root", str(root)]

        def reasons() -> dict[str, list[str]]:
            subprocess.run(command, check=True, capture_output=True, text=True)
            with (root / "witness-search-github/outstanding.tsv").open(encoding="utf-8") as stream:
                line = next(r for r in csv.DictReader(stream, delimiter="\t") if r["source"] == "github-code-search")
            return {q["query"]: [w["reason"] for w in q["windows"]] for q in json.loads(line["issued_incomplete"])}

        budget = "; the turn budget ran out before it was read"
        self.assertEqual({
            plan[0]: ["this size window was never issued" + budget],
            plan[1]: ["100 of 250 reported results read; page 2 onward never requested" + budget],
            plan[2]: ["GitHub reported 230 and served 228 before an empty page 3"],
        }, reasons())
        (root / "witness-search-github-code-search/closure-shape.json").write_text("{}", encoding="utf-8")
        closed = reasons()
        self.assertTrue(closed[plan[1]][0].endswith("closure-shape.json closed it on a witness, and the turn budget went to the open keys"))
        self.assertEqual(["GitHub reported 230 and served 228 before an empty page 3"], closed[plan[2]])

    def test_search_index_accounts_for_each_lane_calls_and_waits(self) -> None:
        root = self.root / "lanes"
        for source in ("github-code-search", "github-publisher-trees", "sourcegraph"):
            (root / f"witness-search-{source}").mkdir(parents=True)
            (root / f"witness-search-{source}/keys.json").write_text(json.dumps(
                {"keys": {"shape": {"selector": "schema.additionalProperties=false"}}}), encoding="utf-8")
        (root / "witness-search-github-publisher-trees/publisher-set.json").write_text(json.dumps({"publishers": []}), encoding="utf-8")
        code = root / "witness-search-github-code-search"
        write = lambda name, rows: (code / name).write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
        write("rate-limit-calls.jsonl", [{"at": "2026-09-25T00:00:00+00:00", "bucket": "code_search", "status": 200}] * 2
              + [{"at": "2026-09-25T00:00:00+00:00", "bucket": "core", "status": 200}])
        write("index-pacing-waits.jsonl", [{"bucket": "code_search", "cause": "spacing", "duration_s": 1.5},
                                           {"bucket": "code_search", "cause": "refusal-cooldown", "duration_s": 2.5}])
        write("raw-github-calls.jsonl", [{"key": "shape", "status": 429, "subject": "s", "url": "u"}])
        write("raw-github-waits.jsonl", [{"key": "shape", "cause": "HTTP 429 backoff", "duration_s": 3.0, "subject": "s"}])
        subprocess.run([sys.executable, str(REPO / "scripts/witness-search-github-index.py"), "--evidence-root", str(root)],
                       check=True, capture_output=True, text=True)
        waits = {line.split("\t")[2]: (line.split("\t")[3], line.split("\t")[4])
                 for line in (code / "search-index.tsv").read_text(encoding="utf-8").splitlines()[1:] if "\twait\t" in line}
        self.assertEqual({
            "code_search": ("2 calls; 2 waits 4 s in index-pacing-waits.jsonl", "rate-limit-calls.jsonl"),
            "core": ("1 calls; 0 waits", "rate-limit-calls.jsonl"),
            "raw.githubusercontent.com": ("1 calls; 1 waits 3 s in raw-github-waits.jsonl", "raw-github-calls.jsonl"),
        }, waits)

    def test_index_refuses_ledger_fields_it_would_misread(self) -> None:
        """A malformed window list, count or publisher entry names its file and line."""
        root = self.root / "malformed"
        for source in ("github-code-search", "github-publisher-trees", "sourcegraph"):
            (root / f"witness-search-{source}").mkdir(parents=True)
            (root / f"witness-search-{source}/keys.json").write_text(json.dumps(
                {"keys": {"shape": {"selector": "schema.additionalProperties=false"}}}), encoding="utf-8")
        trees = root / "witness-search-github-publisher-trees"
        queries = root / "witness-search-github-code-search/queries.jsonl"
        command = [sys.executable, str(REPO / "scripts/witness-search-github-index.py"),
                   "--evidence-root", str(root)]
        cases = {
            "partitioned query lacks its size windows": (
                {"source": "github-code-search", "key": "shape", "query": "q",
                 "outcome": "partitioned", "windows": [{"lower": 0}]}, {"publishers": []}),
            "result_count is not an integer": (
                {"source": "github-code-search", "key": "shape", "query": "q",
                 "outcome": "answered", "result_count": "12", "results": []}, {"publishers": []}),
            "page is not an integer": (
                {"source": "github-code-search", "key": "shape", "query": "q",
                 "outcome": "answered", "result_count": 12, "page": "1", "results": []},
                {"publishers": []}),
            "partitioned query lacks its reported count": (
                {"source": "github-code-search", "key": "shape", "query": "q",
                 "outcome": "partitioned", "windows": [{"query": "q size:0..9"}]}, {"publishers": []}),
            "outstanding-index-truncation lacks an integer retrieved": (
                {"source": "github-code-search", "key": "shape", "query": "q",
                 "outcome": "outstanding-index-truncation", "reported": 3, "page": 2}, {"publishers": []}),
            "publishers must be objects naming a repository and a commit": (
                {"source": "github-code-search", "key": "shape", "query": "q",
                 "outcome": "answered", "result_count": 0, "results": []},
                {"publishers": [{"repository": "example/api"}]}),
        }
        for expected, (query, publishers) in cases.items():
            with self.subTest(expected=expected):
                queries.write_text(json.dumps(query) + "\n", encoding="utf-8")
                (trees / "publisher-set.json").write_text(json.dumps(publishers), encoding="utf-8")
                refused = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(1, refused.returncode)
                self.assertIn(expected, refused.stderr)
                self.assertIn("inspect the source evidence and rerun", refused.stderr)
        queries.write_text("", encoding="utf-8")
        (trees / "publisher-set.json").write_text(json.dumps({"publishers": []}), encoding="utf-8")
        waits = root / "witness-search-github-code-search/index-pacing-waits.jsonl"
        waits.write_text(json.dumps({"bucket": "code_search", "duration_s": "30"}) + "\n", encoding="utf-8")
        refused = subprocess.run(command, capture_output=True, text=True)
        self.assertIn("index-pacing-waits.jsonl:1: duration_s is not a number", refused.stderr)
        waits.unlink()
        (root / "witness-search-sourcegraph/keys.json").write_text(json.dumps({"keys": {"shape": {}}}), encoding="utf-8")
        refused = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, refused.returncode)
        self.assertIn("every key must map to an object carrying its selector", refused.stderr)

    def test_every_written_query_outcome_is_on_one_side_of_the_split(self) -> None:
        """The index reads answered-versus-not from the writer; nothing written escapes it."""
        source = (REPO / "scripts/witness-search-github.py").read_text(encoding="utf-8")
        written = set(re.findall(r'"outcome": "([a-z-]+)"', source))
        written |= set(re.findall(r'"outcome": "answered" if [^\n]+ else "([a-z-]+)"', source))
        written -= {"waiting-on-guard"}  # a refusals.jsonl row, not a query outcome
        self.assertIn("incomplete-stream", written)
        split = set(SEARCH.ANSWER_OUTCOMES) | set(SEARCH.NON_ANSWER_OUTCOMES)
        self.assertEqual(set(), set(SEARCH.ANSWER_OUTCOMES) & set(SEARCH.NON_ANSWER_OUTCOMES))
        self.assertEqual(split, written)

    def test_raw_route_failures_are_recorded_as_acquisition_failures(self) -> None:
        item = {"repository": "example/api", "path": "openapi.yaml", "sha": "a" * 40,
                "url": f"{self.url}/repos/example/api/contents/openapi.yaml?ref={'b' * 40}",
                "selector": "schema.additionalProperties=false"}
        self.server.state["raw_status"] = 404
        missing = self.search.github_document("closed-object", item, route="raw")
        self.assertEqual(("acquisition-failure", 404), (missing["disposition"], missing["status"]))
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            closed_port = probe.getsockname()[1]
        unreachable = SEARCH.Acquirer(
            self.root / "unreachable", github_url=self.url, sourcegraph_url=self.url,
            raw_github_url=f"http://127.0.0.1:{closed_port}",
        )
        failed = unreachable.github_document("closed-object", item, route="raw")
        self.assertEqual("acquisition-failure", failed["disposition"])
        self.assertIn("URLError", failed["diagnostic"])

    def test_cli_first_page_only_does_not_reissue_an_answered_or_partitioned_query(self) -> None:
        script = REPO / "scripts/witness-search-github.py"
        evidence = self.root / "cli-breadth"
        key = min(SEARCH.derive_keys(REPO / "docs/openapi-surface"))
        self.server.state["partition"] = True
        env = {**os.environ, "CROZIER_GITHUB_API_URL": self.url, "GITHUB_TOKEN": "offline-test-token"}
        command = [sys.executable, str(script), *SOURCE_COMMIT, "--evidence", str(evidence),
                   "--source", "github-code-search", "--stage", "search", "--key", key,
                   "--first-page-only"]
        first = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stderr)
        planned = len(SEARCH.query_plan(SEARCH.derive_keys(REPO / "docs/openapi-surface")[key]["selector"])["github-code-search"])
        self.assertEqual(planned, self.server.state["searches"])
        rows = [json.loads(line) for line in (evidence / "queries.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual({"partitioned"}, {row["outcome"] for row in rows})
        again = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(0, again.returncode, again.stderr)
        self.assertEqual(planned, self.server.state["searches"])

    def test_csv_field_size_limits_fit_a_32_bit_c_long(self) -> None:
        """Windows' C long is 32 bits, so a limit past 2**31 - 1 overflows there."""
        c_long_max = 2**31 - 1
        real_limit = csv.field_size_limit

        def thirty_two_bit_limit(*limit: int) -> int:
            if limit and not -c_long_max - 1 <= limit[0] <= c_long_max:
                raise OverflowError("Python int too large to convert to C long")
            return real_limit(*limit)

        previous = real_limit()
        self.addCleanup(real_limit, previous)
        with patch.object(csv, "field_size_limit", thirty_two_bit_limit):
            for source in SEARCH.INDEX.SOURCES:
                with self.subTest(source=source):
                    SEARCH.INDEX.search_index_failures(REPO / "docs/openapi-surface" / f"witness-search-{source}")
        self.assertLessEqual(SEARCH.INDEX.CSV_FIELD_SIZE_LIMIT, c_long_max)
        for script in sorted((REPO / "scripts").glob("witness-search*.py")):
            for line in script.read_text(encoding="utf-8").splitlines():
                if "csv.field_size_limit(" in line:
                    with self.subTest(script=script.name, line=line.strip()):
                        self.assertIn("csv.field_size_limit(CSV_FIELD_SIZE_LIMIT)", line)

    def test_search_index_reconciles_with_records_in_both_directions(self) -> None:
        """A dropped or an invented index row is named, and so is a stale query."""
        root = REPO / "docs/openapi-surface"
        for source in SEARCH.INDEX.SOURCES:
            with self.subTest(source=source):
                self.assertEqual([], SEARCH.INDEX.search_index_failures(root / f"witness-search-{source}"))
        work = self.root / "reconcile"
        shutil.copytree(root / "witness-search-sourcegraph", work, ignore=shutil.ignore_patterns("documents", "screens", "licences"))
        lines = (work / "search-index.tsv").read_text(encoding="utf-8").splitlines()
        candidate = next(line for line in lines if "\tcandidate\t" in line)
        query = next(line for line in lines if "\tquery\t" in line)
        kept = [line for line in lines if line not in (candidate, query)]
        (work / "search-index.tsv").write_text("\n".join([*kept, candidate.replace("census", "census 9") + "x"]) + "\n", encoding="utf-8")
        failures = "\n".join(SEARCH.INDEX.search_index_failures(work))
        self.assertIn("is not indexed", failures)
        self.assertIn("has no records.tsv row", failures)
        self.assertIn(f"issued query {query.split(chr(9))[2]!r} is not indexed", failures)
        (work / "search-index.tsv").write_text("\n".join([*lines, "k\tquery\tnever asked\t0\tqueries.jsonl"]) + "\n", encoding="utf-8")
        self.assertIn("indexed query 'never asked' was never issued", "\n".join(SEARCH.INDEX.search_index_failures(work)))
        (work / "search-index.tsv").write_text("\n".join([*lines, query]) + "\n", encoding="utf-8")
        self.assertIn("a query is indexed twice", "\n".join(SEARCH.INDEX.search_index_failures(work)))

    def test_the_readme_states_the_search_index_columns_the_index_writes(self) -> None:
        readme = (REPO / "docs/openapi-surface/witness-search-github/README.md").read_text(encoding="utf-8")
        stated = re.search(r"as `(key kind subject result file|[a-z ]+)` rows", readme.replace("\n", " "))
        self.assertIsNotNone(stated, "the README no longer states the search-index.tsv columns")
        self.assertEqual(" ".join(SEARCH.INDEX.SEARCH_INDEX_FIELDS), stated.group(1))

    def test_committed_index_matches_per_source_evidence(self) -> None:
        command = [
            sys.executable,
            str(REPO / "scripts/witness-search-github-index.py"),
            "--evidence-root",
            str(REPO / "docs/openapi-surface"),
            "--check",
        ]
        subprocess.run(command, check=True, capture_output=True, text=True)


if __name__ == "__main__":
    unittest.main()
