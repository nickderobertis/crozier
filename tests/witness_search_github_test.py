"""Exercise witness acquisition through real local HTTP responses and the census."""

from __future__ import annotations

import base64
import importlib.util
import json
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
                self.reply(
                    200,
                    {
                        "total_count": 1,
                        "items": [
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
            self.reply(
                200,
                {"encoding": "base64", "content": base64.b64encode(DOCUMENT).decode()},
            )
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
            "contents": 0,
            "sourcegraph": 0,
            "refuse_sourcegraph": False,
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
            self.root, github_url=self.url, sourcegraph_url=self.url
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
        self.assertEqual("does-not-declare", verdict["disposition"])
        self.assertEqual(0, verdict["selector_count"])
        self.assertEqual(1, self.server.state["contents"])

    def test_secondary_refusal_is_outstanding(self) -> None:
        self.server.state["secondary"] = True
        self.assertIsNone(
            self.search.github_search("closed-object", "additionalProperties")
        )
        rows = [
            json.loads(line)
            for line in (self.root / "queries.jsonl").read_text().splitlines()
        ]
        self.assertEqual("refused", rows[-1]["outcome"])
        self.assertEqual(403, rows[-1]["status"])
        self.assertEqual(1, self.server.state["searches"])

    def test_sourcegraph_refusal_then_spacing_are_waited_out(self) -> None:
        self.server.state["refuse_sourcegraph"] = True
        lane = guard_module.PacedLane(
            spacing_s=0.05, backoff_base_s=0.05, attempt_budget=5
        )
        with patch.dict(guard_module.PACED_LANES, {"sourcegraph": lane}):
            self.assertIsNone(self.search.sourcegraph_search("closed-object", "first"))
            self.assertEqual(
                [], self.search.sourcegraph_search("closed-object", "second")
            )
            self.assertEqual(
                [], self.search.sourcegraph_search("closed-object", "third")
            )
        waits = self.search.guards["sourcegraph"].waits()
        self.assertTrue(any(row.get("cause") == "backoff" for row in waits))
        self.assertTrue(any(row.get("cause") == "spacing" for row in waits))
        self.assertEqual(3, self.server.state["sourcegraph"])


if __name__ == "__main__":
    unittest.main()
