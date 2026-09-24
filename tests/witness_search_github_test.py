"""Exercise witness acquisition through real local HTTP responses and the census."""

from __future__ import annotations

import base64
import importlib.util
import json
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
import rate_limit_guard as guard_module  # noqa: E402

SPEC = importlib.util.spec_from_file_location(
    "witness_search_github", REPO / "scripts/witness-search-github.py"
)
assert SPEC and SPEC.loader
SEARCH = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SEARCH
SPEC.loader.exec_module(SEARCH)

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
            if state["secondary"]:
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
        elif self.path.startswith("/repos/example/api/contents/openapi.yaml"):
            state["contents"] += 1
            if (
                state["large"]
                and self.headers.get("Accept") == "application/vnd.github.raw+json"
            ):
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
            if state["raw_refuse"] and state["raw_hits"] == 1:
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
            if state["refuse_sourcegraph"] and state["sourcegraph"] == 1:
                self.reply(429, {"message": "wait"}, {"Retry-After": "0.1"})
            else:
                body = (
                    b"event: matches\ndata: []\n\n"
                    b'event: progress\ndata: {"done":true,"matchCount":0}\n\n'
                )
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
            "partition": False,
            "early_empty": False,
            "contents": 0,
            "sourcegraph": 0,
            "refuse_sourcegraph": False,
            "raw_hits": 0,
            "raw_refuse": False,
            "raw_document": DOCUMENT,
            "raw_incomplete_remaining": 0,
            "trees": 0,
            "large": False,
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
        self.assertIn("annotated-ref-target-closed-object", keys)
        self.assertIn("securityscheme-ref", keys)
        queries = SEARCH.query_plan(
            keys["annotated-ref-target-closed-object"]["selector"]
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
        pointer_queries = SEARCH.query_plan(
            keys["ref-pointer-unnamed-segment"]["selector"]
        )
        self.assertTrue(
            all(
                "/$defs/" in q or "/definitions/" in q
                for q in pointer_queries["github-code-search"]
            )
        )

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
            for line in (self.root / "queries.jsonl").read_text().splitlines()
        ]
        self.assertEqual("refused", rows[-1]["outcome"])
        self.assertEqual(403, rows[-1]["status"])
        self.assertEqual(1, self.server.state["searches"])

    def test_index_truncation_remains_outstanding_on_resume(self) -> None:
        self.server.state["early_empty"] = True
        self.assertIsNone(
            self.search.github_search("closed-object", "additionalProperties")
        )
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text().splitlines()
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
            "".join(json.dumps(row) + "\n" for row in records)
        )
        self.assertIsNone(self.search.github_search("closed-object", query))
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text().splitlines()
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
            for line in (self.root / "queries.jsonl").read_text().splitlines()
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
            for line in (self.root / "queries.jsonl").read_text().splitlines()
        ]
        self.assertEqual("partitioned", rows[0]["outcome"])
        self.assertEqual(2, sum(row["outcome"] == "answered" for row in rows))
        self.assertEqual(3, self.server.state["searches"])

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
            json.loads(x) for x in (self.root / "trees.jsonl").read_text().splitlines()
        ]
        documents = [
            json.loads(x)
            for x in (self.root / "documents.jsonl").read_text().splitlines()
        ]
        self.assertEqual(1, trees[0]["candidate_document_count"])
        self.assertEqual("openapi.yaml", documents[0]["path"])
        self.assertEqual(0, documents[0]["selector_counts"]["closed-object"])
        self.assertEqual(1, self.server.state["trees"])
        self.assertEqual(1, self.server.state["raw_hits"])
        self.assertEqual(0, self.server.state["contents"])

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
        tree = json.loads((self.root / "trees.jsonl").read_text().splitlines()[0])
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

    def test_sourcegraph_refusal_then_spacing_are_waited_out(self) -> None:
        self.server.state["refuse_sourcegraph"] = True
        lane = guard_module.PacedLane(
            spacing_s=0.05, backoff_base_s=0.05, attempt_budget=5
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
            .read_text()
            .splitlines()
        ]
        self.assertTrue(any(row["cause"] == "refusal-cooldown" for row in index_waits))
        self.assertEqual(
            1, len((self.root / "refusals.jsonl").read_text().splitlines())
        )

    def test_sourcegraph_github_match_uses_pinned_raw_route_and_waits(self) -> None:
        self.server.state["raw_refuse"] = True
        item = {
            "repository": "github.com/example/api",
            "path": "openapi.yaml",
            "commit": "c" * 40,
        }
        with patch.object(SEARCH, "RAW_SPACING_S", 0.05), patch.object(
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
            for x in (self.root / "raw-github-waits.jsonl").read_text().splitlines()
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
            for line in (self.root / "raw-github-calls.jsonl").read_text().splitlines()
        ]
        self.assertEqual(2, sum(row["status"] == "IncompleteRead" for row in calls))

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
            (self.root / "documents.jsonl").read_text().splitlines()[0]
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

    def test_consolidated_index_tracks_each_source_record_and_screen(self) -> None:
        root = self.root / "index"
        code = root / "witness-search-github-code-search"
        trees = root / "witness-search-github-publisher-trees"
        sourcegraph = root / "witness-search-sourcegraph"
        for directory in (code, trees, sourcegraph):
            directory.mkdir(parents=True)
        identity = {
            "repository": "example/api",
            "path": "openapi.yaml",
            "commit": "c" * 40,
            "sha256": "d" * 64,
        }
        (code / "candidates.jsonl").write_text(
            json.dumps({**identity, "key": "shape", "disposition": "declares"}) + "\n"
        )
        (trees / "documents.jsonl").write_text(
            json.dumps(
                {**identity, "status": "readable", "selector_counts": {"shape": 1}}
            )
            + "\n"
        )
        (sourcegraph / "candidates.jsonl").write_text(
            json.dumps({**identity, "key": "shape", "disposition": "declares"}) + "\n"
        )
        (sourcegraph / "screens.jsonl").write_text(
            json.dumps(
                {
                    **identity,
                    "license": "passed: publisher grant",
                    "ref": "passed: immutable",
                    "fern": "passed: generated SDK",
                    "disposition": "witness-found",
                }
            )
            + "\n"
        )
        command = [
            sys.executable,
            str(REPO / "scripts/witness-search-github-index.py"),
            "--evidence-root",
            str(root),
        ]
        subprocess.run(command, check=True, capture_output=True, text=True)
        index = (root / "witness-search-github/candidates.tsv").read_text()
        self.assertEqual(2, len(index.splitlines()))
        self.assertIn("github-code-search,github-publisher-trees,sourcegraph", index)
        self.assertIn("witness-found", index)
        subprocess.run([*command, "--check"], check=True, capture_output=True)
        (code / "candidates.jsonl").write_text(
            (code / "candidates.jsonl").read_text()
            + json.dumps(
                {
                    **identity,
                    "path": "new.yaml",
                    "key": "other",
                    "disposition": "declares",
                }
            )
            + "\n"
        )
        failed = subprocess.run([*command, "--check"], capture_output=True, text=True)
        self.assertEqual(1, failed.returncode)

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
