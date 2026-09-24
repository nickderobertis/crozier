# llmlint: ignore-file[new_code_lands_in_a_project] crozier's Python maintenance tests live in tests/ and run through just; no Nx workspace or project boundary exists for this offline HTTP tier.
"""Exercise witness acquisition through real local HTTP responses and the census."""

from __future__ import annotations

import base64
import csv
import importlib.util
import json
import os
import shutil
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
                            json.loads, evidence.read_text().splitlines()
                        )
                    ),
                    row,
                )


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
        security_queries = SEARCH.query_plan(keys["securityscheme-ref"]["selector"])
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
            for line in (self.root / "queries.jsonl").read_text().splitlines()
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
            json.loads((self.root / "queries.jsonl").read_text().splitlines()[-1])[
                "outcome"
            ],
        )
        self.server.state["malformed_sourcegraph"] = True
        with self.assertRaises(SEARCH.SearchStopped):
            self.search.sourcegraph_search("closed-object", "additionalProperties")
        self.assertEqual(
            "outstanding-malformed-response",
            json.loads((self.root / "queries.jsonl").read_text().splitlines()[-1])[
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
            for line in (self.root / "queries.jsonl").read_text().splitlines()
        ]
        self.assertEqual("outstanding-incomplete-results", rows[-1]["outcome"])
        self.server.state["incomplete_sourcegraph"] = True
        self.assertIsNone(
            self.search.sourcegraph_search("closed-object", "additionalProperties")
        )
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text().splitlines()
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
        records = [json.loads(line) for line in (self.root / "documents.jsonl").read_text().splitlines()]
        self.assertEqual("acquisition-failure", records[-1]["status"])
        self.assertEqual(403, records[-1]["http_status"])

    def test_sourcegraph_http_error_stops_search(self) -> None:
        self.server.state["sourcegraph_status"] = 404
        with self.assertRaisesRegex(SEARCH.SearchStopped, "HTTP 404"):
            self.search.sourcegraph_search("closed-object", "additionalProperties")
        record = json.loads((self.root / "queries.jsonl").read_text().splitlines()[-1])
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
        waits = [json.loads(line) for line in (self.root / "raw-github-waits.jsonl").read_text().splitlines()]
        self.assertEqual(4, len(waits))

    def test_cli_search_evaluate_walk_resume_and_failure_exits(self) -> None:
        script = REPO / "scripts/witness-search-github.py"
        evidence = self.root / "cli"
        derived = subprocess.run(
            [sys.executable, str(script), "--evidence", str(evidence), "--derive-only"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, derived.returncode, derived.stderr)
        self.assertIn("FIXTURE gap keys", derived.stdout)
        self.assertIn(
            "annotated-ref-target-closed-object",
            json.loads((evidence / "keys.json").read_text())["keys"],
        )
        invalid = subprocess.run(
            [sys.executable, str(script), "--evidence", str(evidence)],
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
                "--evidence",
                str(evidence),
                "--source",
                "github-code-search",
                "--stage",
                "search",
                "--key",
                "annotated-ref-target-closed-object",
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
            for line in (evidence / "queries.jsonl").read_text().splitlines()
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
                    "key": "annotated-ref-target-closed-object",
                    "query": "local API witness",
                    "outcome": "answered",
                    "results": [item],
                }
            )
            + "\n"
        )
        before = self.server.state["contents"]
        command = [
            sys.executable,
            str(script),
            "--evidence",
            str(evaluation),
            "--source",
            "github-code-search",
            "--stage",
            "evaluate",
            "--key",
            "annotated-ref-target-closed-object",
        ]
        evaluated = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(0, evaluated.returncode, evaluated.stderr)
        candidate = json.loads(
            (evaluation / "candidates.jsonl").read_text().splitlines()[0]
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
        ]}))
        walked = subprocess.run(
            [sys.executable, str(script), "--evidence", str(walk_evidence),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-file", str(publisher_file)],
            env={**env, "CROZIER_RAW_GITHUB_URL": self.url},
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, walked.returncode, walked.stderr)
        self.assertEqual(1, len(json.loads((walk_evidence / "publisher-set.json").read_text())["publishers"]))
        document = json.loads((walk_evidence / "documents.jsonl").read_text().splitlines()[0])
        self.assertEqual("readable", document["status"])
        self.assertEqual(64, len(document["sha256"]))

        invalid_key = subprocess.run(
            [sys.executable, str(script), "--evidence", str(self.root / "cli-key"),
             "--source", "github-code-search", "--stage", "search", "--key", "no-such-key"],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(2, invalid_key.returncode)
        self.assertIn("unknown key", invalid_key.stderr)
        invalid_regions = subprocess.run(
            [sys.executable, str(script), "--evidence", str(self.root / "cli-no-regions"),
             "--regions", str(self.root / "missing-regions"), "--derive-only"],
            capture_output=True, text=True,
        )
        self.assertEqual(1, invalid_regions.returncode)
        self.assertIn("repair the region file and rerun", invalid_regions.stderr)
        evidence_file = self.root / "evidence-is-a-file"
        evidence_file.write_text("occupied")
        unwritable_evidence = subprocess.run(
            [sys.executable, str(script), "--evidence", str(evidence_file), "--derive-only"],
            capture_output=True, text=True,
        )
        self.assertEqual(1, unwritable_evidence.returncode)
        self.assertIn("make --evidence and --cache writable", unwritable_evidence.stderr)
        if os.name != "nt":
            git_failure = self.root / "git-failure"
            git_failure.mkdir()
            fake_git = git_failure / "git"
            fake_git.write_text("#!/bin/sh\nexit 1\n")
            fake_git.chmod(0o755)
            no_commit = subprocess.run(
                [sys.executable, str(script), "--evidence", str(self.root / "cli-no-commit"),
                 "--derive-only"],
                env={**env, "PATH": str(git_failure)}, capture_output=True, text=True,
            )
            self.assertEqual(1, no_commit.returncode)
            self.assertIn("fetch origin/main and rerun", no_commit.stderr)
            git_only = self.root / "git-only"
            git_only.mkdir()
            git_binary = shutil.which("git")
            self.assertIsNotNone(git_binary)
            (git_only / "git").symlink_to(git_binary)
            no_credential_env = {**env, "PATH": str(git_only), "GITHUB_TOKEN": "", "GH_TOKEN": ""}
            no_credential = subprocess.run(
                [sys.executable, str(script), "--evidence", str(self.root / "cli-no-credential"),
                 "--source", "github-code-search", "--stage", "search",
                 "--key", "annotated-ref-target-closed-object"],
                env=no_credential_env, capture_output=True, text=True,
            )
            self.assertEqual(1, no_credential.returncode)
            self.assertIn("set GITHUB_TOKEN or run gh auth login", no_credential.stderr)
        bad_publishers = self.root / "bad-publishers.json"
        bad_publishers.write_text('{"publishers": [{}]}')
        invalid_file = subprocess.run(
            [sys.executable, str(script), "--evidence", str(self.root / "cli-bad-publishers"),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-file", str(bad_publishers)],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(2, invalid_file.returncode)
        self.assertIn("invalid publisher repository", invalid_file.stderr)
        bad_publishers.write_text('{"publishers": [{"repository": "publisher/api", "commit": "main", "scope": ""}]}')
        mutable_ref = subprocess.run(
            [sys.executable, str(script), "--evidence", str(self.root / "cli-mutable-publisher"),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-file", str(bad_publishers)],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(2, mutable_ref.returncode)
        self.assertIn("publisher commit must be a 40-hex SHA", mutable_ref.stderr)
        bad_publishers.write_text("{broken json}")
        invalid_json_file = subprocess.run(
            [sys.executable, str(script), "--evidence", str(self.root / "cli-bad-json-publishers"),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-file", str(bad_publishers)],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(2, invalid_json_file.returncode)
        self.assertIn("--publisher-file cannot be read", invalid_json_file.stderr)
        missing_catalog = subprocess.run(
            [sys.executable, str(script), "--evidence", str(self.root / "cli-missing-catalog"),
             "--source", "github-publisher-trees", "--stage", "walk",
             "--publisher-root", str(self.root / "missing-catalog")],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(1, missing_catalog.returncode)
        self.assertIn("repair the publisher manifests and rerun", missing_catalog.stderr)
        for override in ("CROZIER_GITHUB_API_URL", "CROZIER_SOURCEGRAPH_URL", "CROZIER_RAW_GITHUB_URL"):
            with self.subTest(override=override):
                invalid_url = subprocess.run(
                    [sys.executable, str(script), "--evidence", str(self.root / f"cli-{override}"),
                     "--source", "sourcegraph", "--stage", "search",
                     "--key", "annotated-ref-target-closed-object"],
                    env={**env, override: "file:///etc/passwd"},
                    capture_output=True, text=True,
                )
                self.assertEqual(2, invalid_url.returncode)
                self.assertIn(override, invalid_url.stderr)
                self.assertEqual("", invalid_url.stdout)

        self.server.state["malformed_tree"] = True
        walk_stopped = subprocess.run(
            [sys.executable, str(script), "--evidence", str(self.root / "cli-walk-stop"),
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
        (evaluation_stop / "queries.jsonl").write_text((evaluation / "queries.jsonl").read_text())
        stopped_evaluation = subprocess.run(
            [sys.executable, str(script), "--evidence", str(evaluation_stop),
             "--source", "github-code-search", "--stage", "evaluate",
             "--key", "annotated-ref-target-closed-object"],
            env=env, capture_output=True, text=True,
        )
        self.assertEqual(1, stopped_evaluation.returncode)
        self.assertIn("--stage evaluate", stopped_evaluation.stderr)

        self.server.state["sourcegraph_status"] = 404
        sourcegraph_stop = subprocess.run(
            [sys.executable, str(script), "--evidence", str(self.root / "cli-sourcegraph-stop"),
             "--source", "sourcegraph", "--stage", "search",
             "--key", "annotated-ref-target-closed-object"],
            env={**env, "CROZIER_SOURCEGRAPH_URL": self.url}, capture_output=True, text=True,
        )
        self.assertEqual(1, sourcegraph_stop.returncode)
        self.assertIn("--stage search", sourcegraph_stop.stderr)

    def test_cli_rejects_corrupt_acquisition_ledgers(self) -> None:
        script = REPO / "scripts/witness-search-github.py"
        evidence = self.root / "bad-ledger"
        evidence.mkdir()
        command = [sys.executable, str(script), "--evidence", str(evidence),
                   "--source", "github-code-search", "--stage", "evaluate",
                   "--key", "annotated-ref-target-closed-object"]
        env = {**os.environ, "CROZIER_GITHUB_API_URL": self.url, "GITHUB_TOKEN": "offline-test-token"}
        (evidence / "queries.jsonl").write_text("{bad json}\n")
        malformed = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(1, malformed.returncode)
        self.assertIn("queries.jsonl:1", malformed.stderr)
        self.assertIn("repair the named evidence file", malformed.stderr)
        (evidence / "queries.jsonl").write_text(json.dumps({
            "source": "github-code-search", "key": "annotated-ref-target-closed-object",
            "query": "test", "outcome": "answered",
        }) + "\n")
        missing_results = subprocess.run(command, env=env, capture_output=True, text=True)
        self.assertEqual(1, missing_results.returncode)
        self.assertIn("answered query lacks result identities", missing_results.stderr)
        (evidence / "queries.jsonl").write_text(json.dumps({
            "source": "github-code-search", "key": "annotated-ref-target-closed-object",
            "query": "test", "outcome": "answered", "results": [],
        }) + "\n")
        (evidence / "candidates.jsonl").write_text(json.dumps({
            "source": "github-code-search", "key": "annotated-ref-target-closed-object",
            "repository": "example/api", "disposition": "does-not-declare",
        }) + "\n")
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
        rows = [json.loads(line) for line in (self.root / "transport/queries.jsonl").read_text().splitlines()]
        self.assertEqual(["acquisition-failure", "acquisition-failure"], [row["outcome"] for row in rows])

    def test_parsed_reference_object_is_counted_from_document(self) -> None:
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
                tree_record = json.loads((self.root / label / "documents.jsonl").read_text().splitlines()[0])
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

    def test_unsplittable_index_window_stays_outstanding(self) -> None:
        self.assertIsNone(self.search._partition_window("closed-object", "additionalProperties size:1..1", 1, 1, 1001))
        record = json.loads((self.root / "queries.jsonl").read_text().splitlines()[-1])
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
        self.search.publisher_walk(publisher, keys)
        self.assertEqual(1, self.server.state["trees"])
        self.assertEqual(1, self.server.state["raw_hits"])
        self.assertEqual(1, len((self.root / "documents.jsonl").read_text().splitlines()))

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

    def test_consolidated_index_tracks_source_verdicts_and_unfetched_results(
        self,
    ) -> None:
        root = self.root / "index"
        code = root / "witness-search-github-code-search"
        trees = root / "witness-search-github-publisher-trees"
        sourcegraph = root / "witness-search-sourcegraph"
        for directory in (code, trees, sourcegraph):
            directory.mkdir(parents=True)
            (directory / "keys.json").write_text(json.dumps({"keys": {"shape": {}}}))
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
            + "\n"
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
            + "\n"
        )
        (trees / "documents.jsonl").write_text(
            json.dumps(
                {**identity, "source": "github-publisher-trees", "status": "readable", "selector_counts": {"shape": 1}}
            )
            + "\n"
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
            + "\n"
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
            + "\n"
        )
        command = [
            sys.executable,
            str(REPO / "scripts/witness-search-github-index.py"),
            "--evidence-root",
            str(root),
        ]
        first_index = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(0, first_index.returncode, first_index.stderr)
        with (root / "witness-search-github/candidates.tsv").open() as stream:
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
        (code / "closure-shape.json").write_text(json.dumps({"witness": "example/api"}))
        subprocess.run(command, check=True, capture_output=True, text=True)
        with (root / "witness-search-github/candidates.tsv").open() as stream:
            closed_rows = list(csv.DictReader(stream, delimiter="\t"))
        closed = next(row for row in closed_rows if row["candidate"] == "example/other:openapi.yaml")
        self.assertEqual("not-owed", closed["disposition"])
        with (code / "candidates.jsonl").open("a") as stream:
            stream.write(json.dumps({**identity, "repository": "example/unavailable",
                                     "source": "github-code-search", "key": "shape", "disposition": "selector-unavailable",
                                     "diagnostic": "selector unavailable"}) + "\n")
        subprocess.run(command, check=True, capture_output=True, text=True)
        with (root / "witness-search-github/candidates.tsv").open() as stream:
            unavailable = next(row for row in csv.DictReader(stream, delimiter="\t")
                               if row["candidate"] == "example/unavailable:openapi.yaml")
        self.assertEqual("outstanding", unavailable["disposition"])
        (trees / "trees.jsonl").write_text(json.dumps({
            "repository": "example/api", "commit": "c" * 40,
            "paths": [{"path": "unfetched.yaml", "blob": "f" * 40}],
        }) + "\n")
        subprocess.run(command, check=True, capture_output=True, text=True)
        with (root / "witness-search-github/candidates.tsv").open() as stream:
            walked = next(row for row in csv.DictReader(stream, delimiter="\t")
                          if row["candidate"] == "example/api:unfetched.yaml")
        self.assertEqual("outstanding", walked["disposition"])
        self.assertEqual("not-fetched", walked["digest"])
        (sourcegraph / "screens.jsonl").write_text(
            (sourcegraph / "screens.jsonl")
            .read_text()
            .replace("witness-found", "fern-rejected")
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
        (code / "keys.json").write_text(json.dumps({"keys": "shape"}))
        malformed_keys = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, malformed_keys.returncode)
        self.assertIn("keys must be a mapping", malformed_keys.stderr)
        (code / "keys.json").write_text(json.dumps({"keys": {"shape": {}}}))
        valid_candidates = (code / "candidates.jsonl").read_text()
        (code / "candidates.jsonl").write_text('"not an object"\n')
        invalid_record = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, invalid_record.returncode)
        self.assertIn("candidates.jsonl:1: expected a JSON object", invalid_record.stderr)
        (code / "candidates.jsonl").write_text(valid_candidates)
        screens_path = sourcegraph / "screens.jsonl"
        valid_screen = json.loads(screens_path.read_text().splitlines()[0])
        screens_path.write_text(json.dumps({**valid_screen, "license": 7}) + "\n")
        bad_screen = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, bad_screen.returncode)
        self.assertIn("screens.jsonl:1: missing or invalid license", bad_screen.stderr)
        screens_path.write_text(json.dumps(valid_screen) + "\n")
        documents_path = trees / "documents.jsonl"
        valid_document = json.loads(documents_path.read_text().splitlines()[0])
        documents_path.write_text(json.dumps({**valid_document, "selector_counts": []}) + "\n")
        bad_counts = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, bad_counts.returncode)
        self.assertIn("documents.jsonl:1: invalid selector_counts", bad_counts.stderr)
        documents_path.write_text(json.dumps(valid_document) + "\n")
        (trees / "trees.jsonl").write_text(json.dumps({
            "repository": "example/api", "commit": "c" * 40,
            "paths": [{"path": "openapi.yaml"}],
        }) + "\n")
        bad_tree = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, bad_tree.returncode)
        self.assertIn("trees.jsonl:1: invalid publisher tree paths", bad_tree.stderr)

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
