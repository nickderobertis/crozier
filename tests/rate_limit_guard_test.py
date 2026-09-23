#!/usr/bin/env python3
"""Offline tests for scripts/rate_limit_guard.py against a real local HTTP server.

The server stands in for GitHub's REST API (``/rate_limit`` plus guarded
endpoints that charge a bucket), for Postman's proxy and for Sourcegraph's
search. It serves rate-limit figures and refusals the tests author and records
every request it serves, so each assertion is about what really crossed the
socket. Nothing here mocks the guard or its HTTP client, and nothing asserts a
limit, used count or reset for Postman or Sourcegraph: their fixtures stand in
for transport and refusal behaviour alone.
"""

from __future__ import annotations

import dataclasses
import email.utils
import http.server
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "rate_limit_guard.py"
sys.path.insert(0, str(SCRIPT.parent))

import rate_limit_guard as guard_module  # noqa: E402 -- importable only once sys.path names scripts/
from rate_limit_guard import (  # noqa: E402 -- importable only once sys.path names scripts/
    PacedLane,
    RateLimitGuard,
    SecondaryLimit,
    UnsupportedBucket,
)

SECRET = "ghp_fixture_secret_never_logged_0123456789"
GUARDED = {"/search/code": "code_search", "/search/repositories": "search", "/repos/o/r/contents": "core"}
PACED = {"/postman/_api/ws/proxy": "postman", "/sourcegraph/.api/search/stream": "sourcegraph"}


@dataclasses.dataclass
class Served:
    path: str
    at: float
    authorization: str | None
    reading: dict[str, Any] | None = None


class Fixture:
    """Rate-limit state the tests author, served over a real socket."""

    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.buckets: dict[str, dict[str, int]] = {}
        self.served: list[Served] = []
        self.scripted: dict[str, list[tuple[int, dict[str, str]]]] = {}
        self.header_override: dict[str, dict[str, str]] = {}
        self.rate_limit_body: bytes | None = None
        for name in ("core", "search", "code_search", "graphql"):
            self.set(name, limit=100, used=0, reset_in=3600)

    def set(self, bucket: str, *, limit: int, used: int, reset_in: float) -> None:
        with self.lock:
            self.buckets[bucket] = {"limit": limit, "used": used, "reset": int(time.time() + reset_in)}

    def roll(self) -> None:
        now = time.time()
        for figures in self.buckets.values():
            if now >= figures["reset"]:
                figures["used"] = 0
                figures["reset"] = int(now + 3600)

    def resources(self) -> dict[str, dict[str, int]]:
        return {
            name: {**figures, "remaining": max(figures["limit"] - figures["used"], 0)}
            for name, figures in self.buckets.items()
        }

    def requests(self, path: str) -> list[Served]:
        with self.lock:
            return [entry for entry in self.served if entry.path == path]

    def handle(self, handler: http.server.BaseHTTPRequestHandler) -> None:
        path = handler.path.split("?", 1)[0]
        length = int(handler.headers.get("Content-Length") or 0)
        if length:
            handler.rfile.read(length)
        with self.lock:
            self.roll()
            entry = Served(path, time.time(), handler.headers.get("Authorization"))
            self.served.append(entry)
            status, headers, body = 200, {}, b"{}"
            if path == "/rate_limit":
                resources = self.resources()
                entry.reading = resources
                body = self.rate_limit_body or json.dumps({"resources": resources, "rate": resources["core"]}).encode()
            elif path == "/graphql":
                headers = {"x-ratelimit-resource": "graphql"}
            elif path in GUARDED:
                bucket = GUARDED[path]
                scripted = self.scripted.get(path)
                if scripted:
                    status, headers = scripted.pop(0)
                else:
                    self.buckets[bucket]["used"] += 1
                    figures = self.buckets[bucket]
                    headers = {
                        "x-ratelimit-limit": str(figures["limit"]),
                        "x-ratelimit-used": str(figures["used"]),
                        "x-ratelimit-remaining": str(figures["limit"] - figures["used"]),
                        "x-ratelimit-reset": str(figures["reset"]),
                        "x-ratelimit-resource": bucket,
                    }
                    headers.update(self.header_override.get(path, {}))
            elif path in PACED:
                scripted = self.scripted.get(path)
                if scripted:
                    status, headers = scripted.pop(0)
            else:
                status = 404
        handler.send_response(status)
        for name, value in headers.items():
            handler.send_header(name, value)
        handler.send_header("Content-Type", "application/json")
        handler.send_header("Content-Length", str(len(body)))
        handler.end_headers()
        handler.wfile.write(body)


class GuardTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = Fixture()
        fixture = self.fixture

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self) -> None:
                fixture.handle(self)

            do_POST = do_GET

            def log_message(self, *args: Any) -> None:
                pass

        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}"
        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)

        self.evidence = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.evidence)

        saved_env = {key: os.environ.get(key) for key in ("CROZIER_GITHUB_API_URL", "GITHUB_TOKEN", "GH_TOKEN")}
        os.environ["CROZIER_GITHUB_API_URL"] = self.url
        os.environ["GITHUB_TOKEN"] = SECRET
        os.environ.pop("GH_TOKEN", None)

        def restore_env() -> None:
            for key, value in saved_env.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value

        self.addCleanup(restore_env)

        # Shorter timings keep the tier fast; the rules they drive are the module's own.
        saved = (guard_module.RESET_MARGIN_S, guard_module.SECONDARY_BACKOFF_BASE_S,
                 guard_module.SECONDARY_ATTEMPT_BUDGET, dict(guard_module.PACED_LANES))
        guard_module.RESET_MARGIN_S = 0.2
        guard_module.SECONDARY_BACKOFF_BASE_S = 0.3
        guard_module.SECONDARY_ATTEMPT_BUDGET = 3
        for lane in ("postman", "sourcegraph"):
            guard_module.PACED_LANES[lane] = PacedLane(spacing_s=0.4, backoff_base_s=0.3, attempt_budget=4)

        def restore_timings() -> None:
            (guard_module.RESET_MARGIN_S, guard_module.SECONDARY_BACKOFF_BASE_S,
             guard_module.SECONDARY_ATTEMPT_BUDGET, lanes) = saved
            guard_module.PACED_LANES.clear()
            guard_module.PACED_LANES.update(lanes)

        self.addCleanup(restore_timings)

    def guard(self, host: str = "github") -> RateLimitGuard:
        return RateLimitGuard(host, evidence_dir=self.evidence)

    def call(self, guard: RateLimitGuard, bucket: str, path: str, *, cost: int = 1,
             hold: float = 0.0) -> tuple[float, int]:
        """One guarded call exactly as a consumer makes it; returns (admitted_at, status)."""
        guard.acquire(bucket, cost=cost)
        admitted_at = time.time()
        time.sleep(hold)
        request = urllib.request.Request(f"{self.url}{path}", headers={"Authorization": f"Bearer {SECRET}"})
        try:
            with urllib.request.urlopen(request, timeout=10) as response:
                guard.record(response)
                return admitted_at, response.status
        except urllib.error.HTTPError as refusal:
            with refusal:
                guard.record(refusal)
            return admitted_at, refusal.code

    def evidence_lines(self, name: str) -> list[dict[str, Any]]:
        path = self.evidence / name
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

    def kinds(self, guard: RateLimitGuard, kind: str) -> list[dict[str, Any]]:
        return [entry for entry in guard.waits() if entry["kind"] == kind]


class GitHubCapTests(GuardTestCase):
    def test_waits_while_over_cap_then_proceeds_after_reset(self) -> None:
        self.fixture.set("code_search", limit=10, used=7, reset_in=1.5)
        reset = self.fixture.buckets["code_search"]["reset"]
        guard = self.guard()

        admitted_at, status = self.call(guard, "code_search", "/search/code")

        self.assertEqual(status, 200)
        self.assertGreaterEqual(admitted_at, reset)
        calls = self.fixture.requests("/search/code")
        self.assertEqual(len(calls), 1)
        self.assertGreaterEqual(calls[0].at, reset)
        waits = self.kinds(guard, "wait")
        self.assertEqual([w["cause"] for w in waits], ["cap"])
        self.assertEqual(waits[0]["bucket"], "code_search")
        self.assertEqual(waits[0]["reading"]["used"], 7)
        self.assertGreater(waits[0]["duration_s"], 0)
        probes = self.kinds(guard, "probe")
        self.assertEqual([p["admitted"] for p in probes], [False, True])

    def test_69_of_100_admits_cost_1_and_waits_on_cost_2(self) -> None:
        self.fixture.set("search", limit=100, used=69, reset_in=3600)
        guard = self.guard()
        guard.acquire("search", cost=1)
        with urllib.request.urlopen(f"{self.url}/search/repositories", timeout=10) as response:
            guard.record(response)
        self.assertEqual(guard.waits(), [])

        self.fixture.set("search", limit=100, used=69, reset_in=1.2)
        reset = self.fixture.buckets["search"]["reset"]
        admitted_at, _ = self.call(guard, "search", "/search/repositories", cost=2)
        self.assertGreaterEqual(admitted_at, reset)
        refusing = self.kinds(guard, "wait")[0]
        self.assertEqual((refusing["cause"], refusing["cost"], refusing["reading"]["used"]), ("cap", 2, 69))

    def test_concurrent_acquisitions_are_serialized_against_the_first_reservation(self) -> None:
        self.fixture.set("code_search", limit=100, used=69, reset_in=2)
        reset = self.fixture.buckets["code_search"]["reset"]
        guard = self.guard()
        admitted: list[float] = []

        def worker() -> None:
            admitted.append(self.call(guard, "code_search", "/search/code", hold=0.4)[0])

        threads = [threading.Thread(target=worker) for _ in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=30)

        calls = self.fixture.requests("/search/code")
        self.assertEqual(len(calls), 2)
        # One reading had room for one call; it did not admit two.
        self.assertLess(calls[0].at, reset)
        self.assertGreaterEqual(calls[1].at, reset)
        self.assertGreaterEqual(max(admitted), reset)
        # The second decided on a reading already holding the first's spend.
        refusing = self.kinds(guard, "probe")[0]
        self.assertFalse(refusing["admitted"])
        self.assertEqual(refusing["reading"]["used"], 70)
        reads = self.fixture.requests("/rate_limit")
        second_read = [r for r in reads if r.reading and r.reading["code_search"]["used"] == 70][0]
        self.assertGreater(second_read.at, calls[0].at)

    def test_first_reading_of_an_over_cap_bucket_is_free_and_repeated_until_reset(self) -> None:
        self.fixture.set("core", limit=100, used=100, reset_in=1.5)
        reset = self.fixture.buckets["core"]["reset"]
        guard = self.guard()  # fresh: no prior knowledge of the bucket

        admitted_at, status = self.call(guard, "core", "/repos/o/r/contents")

        self.assertEqual(status, 200)
        reads = self.fixture.requests("/rate_limit")
        before = [r for r in reads if r.at < reset]
        after = [r for r in reads if r.at >= reset]
        self.assertGreaterEqual(len(before), 1)
        self.assertGreaterEqual(len(after), 1)
        # Reading charged the bucket nothing.
        self.assertTrue(all(r.reading["core"]["used"] == 100 for r in before))
        self.assertTrue(all(r.authorization == f"Bearer {SECRET}" for r in reads))
        calls = self.fixture.requests("/repos/o/r/contents")
        self.assertEqual(len(calls), 1)
        self.assertGreaterEqual(calls[0].at, reset)
        self.assertGreaterEqual(admitted_at, reset)
        self.assertEqual(len(self.kinds(guard, "probe")), len(reads))

    def test_admission_uses_the_live_reading_not_an_earlier_response(self) -> None:
        guard = self.guard()
        self.fixture.set("core", limit=100, used=10, reset_in=1.2)
        self.call(guard, "core", "/repos/o/r/contents")
        self.assertEqual(guard.waits(), [])
        # Another holder of the token spends between that response and the next acquire.
        self.fixture.buckets["core"]["used"] = 75
        reset = self.fixture.buckets["core"]["reset"]
        admitted_at, _ = self.call(guard, "core", "/repos/o/r/contents")
        self.assertGreaterEqual(admitted_at, reset)
        self.assertEqual(self.kinds(guard, "wait")[0]["reading"]["used"], 75)

        # And the reverse: a response claiming the bucket is spent does not block
        # an acquire whose live reading has room.
        guard = self.guard()
        self.fixture.set("search", limit=100, used=5, reset_in=3600)
        self.fixture.header_override["/search/repositories"] = {"x-ratelimit-used": "99", "x-ratelimit-remaining": "1"}
        self.call(guard, "search", "/search/repositories")
        started = time.time()
        self.call(guard, "search", "/search/repositories")
        self.assertLess(time.time() - started, 1.0)
        self.assertEqual(guard.waits(), [])

    def test_graphql_is_refused_before_any_reading_or_wait(self) -> None:
        guard = self.guard()
        for bucket in ("graphql", "not_a_bucket"):
            with self.assertRaises(UnsupportedBucket):
                guard.acquire(bucket)
        self.assertEqual(self.fixture.served, [])
        self.assertEqual(guard.waits(), [])
        # The guard is not wedged: a covered bucket still admits.
        self.call(guard, "core", "/repos/o/r/contents")

        with urllib.request.urlopen(urllib.request.Request(f"{self.url}/graphql", data=b"", method="POST"), timeout=10) as response:
            with self.assertRaises(UnsupportedBucket):
                guard.record(response)
        self.assertEqual(guard.waits(), [])

    def test_record_without_acquire_and_double_acquire_are_loud(self) -> None:
        guard = self.guard()
        with urllib.request.urlopen(f"{self.url}/repos/o/r/contents", timeout=10) as response:
            with self.assertRaises(RuntimeError):
                guard.record(response)
        guard.acquire("core")
        with self.assertRaises(RuntimeError):
            guard.acquire("search")
        with self.assertRaises(ValueError):
            RateLimitGuard("gitlab")


    def test_a_call_spending_in_another_bucket_is_refused_loudly(self) -> None:
        guard = self.guard()
        self.fixture.header_override["/repos/o/r/contents"] = {"x-ratelimit-resource": "integration_manifest"}
        with self.assertRaises(UnsupportedBucket):
            self.call(guard, "core", "/repos/o/r/contents")
        # The reservation is closed, so the bucket is not wedged.
        del self.fixture.header_override["/repos/o/r/contents"]
        self.assertEqual(self.call(guard, "core", "/repos/o/r/contents")[1], 200)

    def test_retry_after_on_a_successful_response_is_honoured(self) -> None:
        guard = self.guard()
        self.fixture.header_override["/search/code"] = {"Retry-After": "1"}
        self.call(guard, "code_search", "/search/code")
        del self.fixture.header_override["/search/code"]
        self.call(guard, "code_search", "/search/code")
        calls = self.fixture.requests("/search/code")
        self.assertGreaterEqual(calls[1].at - calls[0].at, 1.0)
        self.assertEqual([w["cause"] for w in self.kinds(guard, "wait")], ["backoff"])

    def test_cost_must_be_positive(self) -> None:
        guard = self.guard()
        with self.assertRaises(ValueError):
            guard.acquire("core", cost=0)
        self.assertEqual(self.fixture.served, [])

    def test_gh_token_is_the_fallback_credential(self) -> None:
        del os.environ["GITHUB_TOKEN"]
        os.environ["GH_TOKEN"] = SECRET
        self.call(self.guard(), "core", "/repos/o/r/contents")
        self.assertEqual(self.fixture.requests("/rate_limit")[0].authorization, f"Bearer {SECRET}")


class GitHubSecondaryTests(GuardTestCase):
    def test_secondary_refusal_backs_off_then_raises_after_budget(self) -> None:
        self.fixture.set("code_search", limit=100, used=1, reset_in=3600)
        self.fixture.scripted["/search/code"] = [
            (403, {"Retry-After": "1", "x-ratelimit-remaining": "99"}),
            (429, {}),
            (403, {"Retry-After": "0"}),
        ]
        guard = self.guard()

        self.assertEqual(self.call(guard, "code_search", "/search/code")[1], 403)
        self.assertEqual(self.call(guard, "code_search", "/search/code")[1], 429)
        with self.assertRaises(SecondaryLimit):
            self.call(guard, "code_search", "/search/code")
        served = len(self.fixture.served)
        with self.assertRaises(SecondaryLimit):
            guard.acquire("code_search")
        self.assertEqual(len(self.fixture.served), served)

        calls = self.fixture.requests("/search/code")
        self.assertEqual(len(calls), 3)
        self.assertGreaterEqual(calls[1].at - calls[0].at, 1.0)  # Retry-After over the 0.3 s base
        self.assertGreaterEqual(calls[2].at - calls[1].at, 0.6)  # base doubled
        backoffs = [w for w in self.kinds(guard, "wait") if w["cause"] == "backoff"]
        self.assertEqual([w["refusals"] for w in backoffs], [1, 2])
        self.assertTrue(all(p["classifying"] == "secondary" for p in self.kinds(guard, "probe")))

    def test_primary_refusal_waits_for_reset_without_counting_toward_budget(self) -> None:
        guard = self.guard()
        # Admitted on a reading with room, then another holder spends the bucket.
        self.fixture.set("search", limit=100, used=10, reset_in=1.2)
        reset = self.fixture.buckets["search"]["reset"]
        guard.acquire("search")
        self.fixture.buckets["search"]["used"] = 100
        self.fixture.scripted["/search/repositories"] = [(403, {"x-ratelimit-remaining": "0"})]
        try:
            urllib.request.urlopen(f"{self.url}/search/repositories", timeout=10)
        except urllib.error.HTTPError as refusal:
            with refusal:
                guard.record(refusal)
        admitted_at, status = self.call(guard, "search", "/search/repositories")
        self.assertEqual(status, 200)
        self.assertGreaterEqual(admitted_at, reset)
        self.assertEqual(self.kinds(guard, "probe")[0]["classifying"], "primary")


class PacedLaneTests(GuardTestCase):
    def test_each_paced_lane_spaces_waits_out_refusals_and_backs_off(self) -> None:
        for lane, path in (("postman", "/postman/_api/ws/proxy"), ("sourcegraph", "/sourcegraph/.api/search/stream")):
            with self.subTest(lane=lane):
                guard = self.guard(lane)
                self.fixture.scripted[path] = [
                    (200, {}), (200, {}),
                    (429, {"Retry-After": "1"}),
                    (429, {}),
                    (429, {}),
                    (200, {}),
                    (429, {}), (503, {}), (429, {}), (429, {}),
                ]
                statuses = [self.call(guard, lane, path)[1] for _ in range(9)]
                self.assertEqual(statuses, [200, 200, 429, 429, 429, 200, 429, 503, 429])
                with self.assertRaises(SecondaryLimit):
                    self.call(guard, lane, path)
                served = len(self.fixture.requests(path))
                with self.assertRaises(SecondaryLimit):
                    guard.acquire(lane)
                self.assertEqual(len(self.fixture.requests(path)), served)

                at = [entry.at for entry in self.fixture.requests(path)]
                gaps = [later - earlier for earlier, later in zip(at, at[1:])]
                self.assertTrue(all(gap >= 0.4 for gap in gaps), gaps)  # declared spacing
                self.assertGreaterEqual(gaps[2], 1.0)  # Retry-After waited out, not retried into
                self.assertGreaterEqual(gaps[3], 0.6)  # second refusal: base doubled
                self.assertGreaterEqual(gaps[4], 1.2)  # third: doubled again
                self.assertLess(gaps[5], 1.0)  # a success resets the backoff

                waits = self.kinds(guard, "wait")
                self.assertEqual(sum(w["cause"] == "backoff" for w in waits), 6)
                self.assertGreaterEqual(sum(w["cause"] == "spacing" for w in waits), 1)
                self.assertTrue(all(w["lane"] == lane for w in waits))
                self.assertEqual(self.kinds(guard, "probe"), [])
                for entry in guard.waits():
                    self.assertFalse({"limit", "used", "reset", "remaining", "reading"} & entry.keys())

    def test_retry_after_as_an_http_date_and_on_a_success_is_waited_out(self) -> None:
        guard = self.guard("sourcegraph")
        path = "/sourcegraph/.api/search/stream"
        self.fixture.scripted[path] = [
            (429, {"Retry-After": email.utils.formatdate(time.time() + 2, usegmt=True)}),
            (200, {"Retry-After": "1"}),
            (200, {}),
        ]
        for _ in range(3):
            self.call(guard, "sourcegraph", path)
        at = [entry.at for entry in self.fixture.requests(path)]
        self.assertGreaterEqual(at[1] - at[0], 0.9)  # an HTTP date has whole-second resolution
        self.assertGreaterEqual(at[2] - at[1], 1.0)
        self.assertEqual([w["cause"] for w in self.kinds(guard, "wait")], ["backoff", "backoff"])

    def test_a_backoff_on_one_lane_does_not_delay_the_other(self) -> None:
        postman = self.guard("postman")
        sourcegraph = self.guard("sourcegraph")
        self.fixture.scripted["/postman/_api/ws/proxy"] = [(429, {"Retry-After": "3"})]
        self.call(postman, "postman", "/postman/_api/ws/proxy")
        started = time.time()
        self.call(sourcegraph, "sourcegraph", "/sourcegraph/.api/search/stream")
        self.assertLess(time.time() - started, 0.5)
        self.assertEqual(sourcegraph.waits(), [])
        self.call(postman, "postman", "/postman/_api/ws/proxy")
        self.assertGreaterEqual(time.time() - started, 2.5)
        with self.assertRaises(UnsupportedBucket):
            postman.acquire("sourcegraph")

    def test_concurrent_callers_cannot_collapse_one_interval(self) -> None:
        guard = self.guard("postman")
        threads = [threading.Thread(target=self.call, args=(guard, "postman", "/postman/_api/ws/proxy")) for _ in range(3)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=30)
        at = [entry.at for entry in self.fixture.requests("/postman/_api/ws/proxy")]
        self.assertEqual(len(at), 3)
        self.assertTrue(all(b - a >= 0.4 for a, b in zip(at, at[1:])), at)


class EvidenceTests(GuardTestCase):
    def test_waits_are_all_accounted_for_on_disk_without_the_credential(self) -> None:
        self.fixture.set("code_search", limit=10, used=7, reset_in=1.2)
        github = self.guard()
        postman = self.guard("postman")
        self.call(github, "code_search", "/search/code")
        self.call(postman, "postman", "/postman/_api/ws/proxy")
        self.call(postman, "postman", "/postman/_api/ws/proxy")

        on_disk = self.evidence_lines(guard_module.WAITS_FILE)
        self.assertEqual(sorted(json.dumps(e, sort_keys=True) for e in on_disk),
                         sorted(json.dumps(e, sort_keys=True) for e in github.waits() + postman.waits()))
        self.assertEqual({(e["host"], e["kind"], e.get("cause")) for e in on_disk},
                         {("github", "probe", None), ("github", "wait", "cap"), ("postman", "wait", "spacing")})
        for entry in on_disk:
            if entry["kind"] == "wait":
                self.assertGreater(entry["duration_s"], 0)
        self.assertEqual(len(self.evidence_lines(guard_module.CALLS_FILE)), 3)
        for path in self.evidence.iterdir():
            self.assertNotIn(SECRET, path.read_text(encoding="utf-8"))
        self.assertTrue(all(r.authorization == f"Bearer {SECRET}" for r in self.fixture.requests("/rate_limit")))


class QuotaStatusTests(GuardTestCase):
    def status(self, url: str) -> subprocess.CompletedProcess[str]:
        env = {**os.environ, "CROZIER_GITHUB_API_URL": url}
        return subprocess.run([sys.executable, str(SCRIPT), "status"], env=env, capture_output=True,
                              text=True, timeout=30)

    def test_reports_live_figures_in_one_free_read_and_never_waits(self) -> None:
        self.fixture.set("code_search", limit=10, used=9, reset_in=3600)
        self.fixture.set("core", limit=5000, used=1234, reset_in=3600)
        started = time.time()
        result = self.status(self.url)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertLess(time.time() - started, 10)
        self.assertEqual([entry.path for entry in self.fixture.served], ["/rate_limit"])

        lines = result.stdout.splitlines()
        core = next(line for line in lines if line.strip().startswith("core "))
        self.assertIn("limit   5000", core)
        self.assertIn("used   1234", core)
        self.assertIn("24.7%", core)
        self.assertIn("reset 20", core)
        over = next(line for line in lines if line.strip().startswith("code_search "))
        self.assertIn("90.0%", over)
        self.assertIn("OVER CAP", over)
        self.assertTrue(any(line.strip().startswith("search ") for line in lines))
        for lane in ("postman", "sourcegraph"):
            line = next(line for line in lines if line.startswith(f"{lane}:"))
            self.assertIn("no published quota; paced (1 request / 2s", line)
            for word in ("limit", "used", "reset", "%"):
                self.assertNotIn(word, line)
        self.assertNotIn(SECRET, result.stdout + result.stderr)

    def test_unauthenticated_and_uncovered_buckets_are_reported_as_such(self) -> None:
        self.fixture.set("integration_manifest", limit=5000, used=0, reset_in=3600)
        del os.environ["GITHUB_TOKEN"]
        result = self.status(self.url)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("unauthenticated: set GITHUB_TOKEN", result.stdout)
        self.assertIsNone(self.fixture.served[0].authorization)
        lines = result.stdout.splitlines()
        self.assertTrue(next(line for line in lines if "integration_manifest" in line).endswith("not called here"))
        self.assertTrue(next(line for line in lines if line.strip().startswith("core ")).endswith("guarded"))
        graphql = [line for line in lines if "graphql" in line]
        self.assertEqual(graphql, ["  graphql: not covered; this repository makes no GraphQL call"])

    def test_malformed_figures_fail_with_a_next_action(self) -> None:
        self.fixture.rate_limit_body = json.dumps({"resources": {"core": {"limit": 5000}}}).encode()
        result = self.status(self.url)
        self.assertEqual(result.returncode, 1)
        self.assertIn("malformed figures for 'core'", result.stderr)
        self.assertIn("CROZIER_GITHUB_API_URL", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_usage_error_exits_2(self) -> None:
        result = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 2)
        self.assertIn("usage: rate_limit_guard.py status", result.stderr)
        self.assertEqual(self.fixture.served, [])

    def test_unreachable_api_fails_with_a_next_action(self) -> None:
        result = self.status("http://127.0.0.1:9")
        self.assertEqual(result.returncode, 1)
        self.assertIn("could not read", result.stderr)
        self.assertIn("GITHUB_TOKEN", result.stderr)


if __name__ == "__main__":
    unittest.main()
