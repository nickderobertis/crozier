#!/usr/bin/env python3
"""Offline tests for tools/witness-search/rate_limit_guard.py against a real local HTTP server.

The server stands in for GitHub's REST API (``/rate_limit`` plus guarded
endpoints that charge a bucket), for Postman's proxy and for Sourcegraph's
search. It serves rate-limit figures and refusals the tests author and records
every request it serves, so each assertion is about what really crossed the
socket. Nothing here mocks the guard or its HTTP client, and nothing asserts a
limit, used count or reset for Postman or Sourcegraph: their fixtures stand in
for transport and refusal behaviour alone.
"""

from __future__ import annotations

import contextlib
import dataclasses
import email.utils
import hashlib
import http.server
import io
import itertools
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

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "witness-search" / "rate_limit_guard.py"
sys.path.insert(0, str(SCRIPT.parent))

import rate_limit_guard as guard_module  # noqa: E402 -- importable only once sys.path names its directory
from rate_limit_guard import (  # noqa: E402 -- importable only once sys.path names its directory
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
        # Units a guarded call spends, per path: another holder's spend folded
        # into this one call, to author a fast burn.
        self.charge: dict[str, int] = {}
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
                    self.buckets[bucket]["used"] += self.charge.get(path, 1)
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
        self.admissions: list[float] = []
        fixture = self.fixture

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self) -> None:
                fixture.handle(self)

            do_POST = do_GET

            def log_message(self, format: str, *args: Any) -> None:
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
        saved = (
            guard_module.RESET_MARGIN_S,
            guard_module.SECONDARY_BACKOFF_BASE_S,
            guard_module.SECONDARY_ATTEMPT_BUDGET,
            dict(guard_module.PACED_LANES),
        )
        guard_module.RESET_MARGIN_S = 0.2
        guard_module.SECONDARY_BACKOFF_BASE_S = 0.3
        guard_module.SECONDARY_ATTEMPT_BUDGET = 3
        for lane in ("postman", "sourcegraph"):
            guard_module.PACED_LANES[lane] = PacedLane(spacing_s=0.4, backoff_base_s=0.3, attempt_budget=4)

        def restore_timings() -> None:
            (
                guard_module.RESET_MARGIN_S,
                guard_module.SECONDARY_BACKOFF_BASE_S,
                guard_module.SECONDARY_ATTEMPT_BUDGET,
                lanes,
            ) = saved
            guard_module.PACED_LANES.clear()
            guard_module.PACED_LANES.update(lanes)

        self.addCleanup(restore_timings)

    def guard(self, host: str = "github") -> RateLimitGuard:
        return RateLimitGuard(host, evidence_dir=self.evidence)

    def call(
        self, guard: RateLimitGuard, bucket: str, path: str, *, cost: int = 1, hold: float = 0.0
    ) -> tuple[float, int]:
        """One guarded call exactly as a consumer makes it; returns (admitted_at, status).

        `admitted_at` is the wall-clock moment the guard released the call, to
        compare with a bucket's reset epoch. The same moment on the monotonic
        clock the guard waits on is appended to `self.admissions`: a wait it
        imposes is measured there, never by wall-clock stamps, which carry any
        step the host makes to its clock (time sync moves it by a tenth of a
        second at a time) and, server-side, the reading thread's scheduling.
        """
        guard.acquire(bucket, cost=cost)
        admitted_at = time.time()
        self.admissions.append(time.monotonic())
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
        self.assertEqual([w["cause"] for w in waits], ["floor"])
        self.assertEqual(waits[0]["bucket"], "code_search")
        self.assertEqual(waits[0]["reading"]["used"], 7)
        self.assertGreater(waits[0]["duration_s"], 0)
        probes = self.kinds(guard, "probe")
        self.assertEqual([p["admitted"] for p in probes], [False, True])

    def test_59_of_100_admits_cost_1_at_the_40_percent_floor_and_waits_on_cost_2(self) -> None:
        self.fixture.set("search", limit=100, used=59, reset_in=3600)
        guard = self.guard()
        guard.acquire("search", cost=1)
        with urllib.request.urlopen(f"{self.url}/search/repositories", timeout=10) as response:
            guard.record(response)
        self.assertEqual(guard.waits(), [])  # exactly 40 of 100 remain after it: admitted, no probe logged

        # One unit more and 39 would remain. A fresh window holds one reading, so
        # no burn rate is measurable and the call waits for the reset.
        self.fixture.set("search", limit=100, used=59, reset_in=1.2)
        reset = self.fixture.buckets["search"]["reset"]
        admitted_at, _ = self.call(guard, "search", "/search/repositories", cost=2)
        self.assertGreaterEqual(admitted_at, reset)
        refusing = self.kinds(guard, "wait")[0]
        self.assertEqual((refusing["cause"], refusing["cost"], refusing["reading"]["used"]), ("floor", 2, 59))
        probes = self.kinds(guard, "probe")
        self.assertEqual([p["admitted"] for p in probes], [False, True])
        self.assertNotIn("burn", probes[0])
        self.assertEqual(probes[1]["admitted_by"], "floor")

    def test_the_floor_is_exact_for_a_limit_whose_share_is_not_a_float(self) -> None:
        # 12 of 30 is exactly 40%; floating point would put it a hair under.
        self.fixture.set("core", limit=30, used=17, reset_in=3600)
        guard = self.guard()
        self.call(guard, "core", "/repos/o/r/contents")
        self.assertEqual(guard.waits(), [])

    def test_a_slow_burn_with_reset_soon_is_admitted_below_the_floor(self) -> None:
        self.fixture.set("core", limit=100, used=58, reset_in=3)
        reset = self.fixture.buckets["core"]["reset"]
        guard = self.guard()
        self.call(guard, "core", "/repos/o/r/contents", hold=0.5)  # 41 remain after it: over the floor
        self.assertEqual(guard.waits(), [])
        # 59 used: a call costing 2 would leave 39, below the floor. The window's
        # two readings show 1 unit burned in at least 0.5 s, so the 39 would
        # last at least 19.5 s against a reset under 3 s away: the window resets
        # first, and the call is admitted now rather than after the reset.
        admitted_at, status = self.call(guard, "core", "/repos/o/r/contents", cost=2)
        self.assertEqual(status, 200)
        self.assertLess(admitted_at, reset)
        self.assertEqual(self.kinds(guard, "wait"), [])
        (probe,) = self.kinds(guard, "probe")
        self.assertEqual((probe["admitted"], probe["admitted_by"], probe["reading"]["used"]), (True, "burn-rate", 59))
        self.assertGreater(probe["burn"]["projected_s"], probe["burn"]["until_reset_s"])
        self.assertGreater(probe["burn"]["rate_per_s"], 0)
        logged = [e for e in self.evidence_lines(guard_module.WAITS_FILE) if e["kind"] == "probe"]
        self.assertEqual([e["admitted_by"] for e in logged], ["burn-rate"])

    def test_a_fast_burn_below_the_floor_waits_for_the_reset(self) -> None:
        self.fixture.set("core", limit=100, used=0, reset_in=2)
        reset = self.fixture.buckets["core"]["reset"]
        self.fixture.charge["/repos/o/r/contents"] = 60
        guard = self.guard()
        self.call(guard, "core", "/repos/o/r/contents")
        self.assertEqual(guard.waits(), [])
        # 60 burned between two readings a fraction of a second apart: the 39
        # left after the next call would be spent long before the reset.
        del self.fixture.charge["/repos/o/r/contents"]
        admitted_at, status = self.call(guard, "core", "/repos/o/r/contents")
        self.assertEqual(status, 200)
        self.assertGreaterEqual(admitted_at, reset)
        self.assertEqual([w["cause"] for w in self.kinds(guard, "wait")], ["floor"])
        probes = self.kinds(guard, "probe")
        self.assertEqual([p["admitted"] for p in probes], [False, True])
        self.assertEqual(probes[0]["reading"]["used"], 60)
        self.assertNotIn("admitted_by", probes[0])
        self.assertEqual(probes[1]["admitted_by"], "floor")

    def test_a_zero_burn_below_the_floor_is_admitted(self) -> None:
        self.fixture.set("search", limit=100, used=59, reset_in=3600)
        self.fixture.charge["/search/repositories"] = 0
        guard = self.guard()
        self.call(guard, "search", "/search/repositories", hold=0.1)  # exactly 40 remain after it
        # Two readings over a measured interval show nothing burning: the 39
        # left after a call costing 2 never run out before the reset.
        self.call(guard, "search", "/search/repositories", cost=2)
        self.assertEqual(self.kinds(guard, "wait"), [])
        (probe,) = self.kinds(guard, "probe")
        self.assertEqual((probe["admitted_by"], probe["burn"]["rate_per_s"]), ("burn-rate", 0))

    def test_the_burn_rate_never_admits_a_call_past_the_remaining_quota(self) -> None:
        self.fixture.set("core", limit=100, used=50, reset_in=1.5)
        reset = self.fixture.buckets["core"]["reset"]
        self.fixture.charge["/repos/o/r/contents"] = 0
        guard = self.guard()
        self.call(guard, "core", "/repos/o/r/contents", hold=0.1)
        # Nothing is burning, but a call costing 60 would take remaining to -10.
        admitted_at, _ = self.call(guard, "core", "/repos/o/r/contents", cost=60)
        self.assertGreaterEqual(admitted_at, reset)
        self.assertEqual([w["cause"] for w in self.kinds(guard, "wait")], ["floor"])
        self.assertFalse(self.kinds(guard, "probe")[0]["admitted"])

    def test_concurrent_acquisitions_are_serialized_against_the_first_reservation(self) -> None:
        # The first call burns 60 units, fast enough that the 39 left after a
        # second would run out before the reset: no burn-rate exception for it.
        self.fixture.set("code_search", limit=100, used=0, reset_in=3)
        self.fixture.charge["/search/code"] = 60
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
        self.assertEqual(refusing["reading"]["used"], 60)
        reads = self.fixture.requests("/rate_limit")
        second_read = next(r for r in reads if r.reading and r.reading["code_search"]["used"] == 60)
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
        self.assertTrue(all(r.reading is not None and r.reading["core"]["used"] == 100 for r in before))
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

        with (
            urllib.request.urlopen(
                urllib.request.Request(f"{self.url}/graphql", data=b"", method="POST"), timeout=10
            ) as response,
            self.assertRaises(UnsupportedBucket),
        ):
            guard.record(response)
        self.assertEqual(guard.waits(), [])

    def test_rejecting_a_graphql_response_releases_the_acquired_bucket(self) -> None:
        guard = self.guard()
        guard.acquire("core")
        request = urllib.request.Request(f"{self.url}/graphql", data=b"", method="POST")
        with urllib.request.urlopen(request, timeout=10) as response, self.assertRaises(UnsupportedBucket):
            guard.record(response)
        # The reservation closed with the refusal: this thread acquires again,
        # and another thread is not left blocked on the bucket's lock.
        self.assertEqual(self.call(guard, "core", "/repos/o/r/contents")[1], 200)
        other: list[int] = []
        thread = threading.Thread(target=lambda: other.append(self.call(guard, "core", "/repos/o/r/contents")[1]))
        thread.start()
        thread.join(timeout=10)
        self.assertEqual(other, [200])

    def test_an_api_root_off_github_https_or_loopback_http_is_refused_before_any_call(self) -> None:
        for root in (
            "http://example.invalid",
            "https://example.invalid",
            "ftp://127.0.0.1:9",
            f"https://127.0.0.1:{self.server.server_address[1]}",
            "not a url",
        ):
            with self.subTest(root=root):
                os.environ["CROZIER_GITHUB_API_URL"] = root
                guard = self.guard()
                with self.assertRaises(ValueError) as raised:
                    guard.acquire("core")
                self.assertIn("CROZIER_GITHUB_API_URL must use https://api.github.com", str(raised.exception))
                self.assertEqual(self.fixture.served, [])
                # The refusal reserved nothing: a valid root still admits.
                os.environ["CROZIER_GITHUB_API_URL"] = self.url
                self.assertEqual(self.call(guard, "core", "/repos/o/r/contents")[1], 200)
                with self.fixture.lock:
                    self.fixture.served.clear()

    def test_rate_limit_figures_that_are_not_nonnegative_integers_are_refused(self) -> None:
        reset = int(time.time()) + 3600
        for figures in (
            {"limit": 100, "used": -1000, "reset": reset},
            {"limit": 100, "used": "5", "reset": reset},
            {"limit": 100, "used": 5.5, "reset": reset},
            {"limit": 100, "used": True, "reset": reset},
            {"limit": -100, "used": 0, "reset": reset},
            {"limit": 100, "used": 0, "remaining": -1, "reset": reset},
            {"limit": 100, "used": 0, "reset": None},
        ):
            with self.subTest(figures=figures):
                self.fixture.rate_limit_body = json.dumps({"resources": {"core": figures}}).encode()
                guard = self.guard()
                with self.assertRaises(RuntimeError) as raised:
                    guard.acquire("core")
                self.assertIn("malformed figures for bucket 'core'", str(raised.exception))
                self.assertEqual(self.fixture.requests("/repos/o/r/contents"), [])
                self.assertEqual(guard.waits(), [])
        # Nothing stays reserved: a well-formed reading admits the next call.
        self.fixture.rate_limit_body = None
        self.assertEqual(self.call(guard, "core", "/repos/o/r/contents")[1], 200)

    def test_record_without_acquire_and_double_acquire_are_loud(self) -> None:
        guard = self.guard()
        with (
            urllib.request.urlopen(f"{self.url}/repos/o/r/contents", timeout=10) as response,
            self.assertRaises(RuntimeError),
        ):
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
        self.assertEqual(len(self.fixture.requests("/search/code")), 2)
        self.assertGreaterEqual(self.admissions[1] - self.admissions[0], 1.0)
        self.assertEqual([w["cause"] for w in self.kinds(guard, "wait")], ["backoff"])

    def test_a_call_that_produced_no_response_still_closes_its_reservation(self) -> None:
        for host, bucket in (("github", "core"), ("postman", "postman")):
            with self.subTest(host=host):
                guard = self.guard(host)
                guard.acquire(bucket)
                with self.assertRaises(urllib.error.URLError) as raised:
                    urllib.request.urlopen("http://127.0.0.1:9/unreachable", timeout=5)
                guard.record(raised.exception)
                path = "/repos/o/r/contents" if host == "github" else "/postman/_api/ws/proxy"
                self.assertEqual(self.call(guard, bucket, path)[1], 200)

    def test_a_reading_without_the_bucket_is_refused_not_waited_on(self) -> None:
        self.fixture.rate_limit_body = json.dumps({"resources": {"core": {"limit": 1, "used": 0, "reset": 0}}}).encode()
        guard = self.guard()
        with self.assertRaises(UnsupportedBucket):
            guard.acquire("code_search")
        self.assertEqual(guard.waits(), [])
        self.fixture.rate_limit_body = b"{}"
        with self.assertRaises(RuntimeError):
            guard.acquire("code_search")
        self.assertEqual([entry.path for entry in self.fixture.served], ["/rate_limit", "/rate_limit"])

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
        at = self.admissions
        self.assertGreaterEqual(at[1] - at[0], 1.0)  # Retry-After over the 0.3 s base
        self.assertGreaterEqual(at[2] - at[1], 0.6)  # base doubled
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
                    (200, {}),
                    (200, {}),
                    (429, {"Retry-After": "1"}),
                    (429, {}),
                    (429, {}),
                    (200, {}),
                    (429, {}),
                    (503, {}),
                    (429, {}),
                    (429, {}),
                ]
                self.admissions.clear()
                statuses = [self.call(guard, lane, path)[1] for _ in range(9)]
                self.assertEqual(statuses, [200, 200, 429, 429, 429, 200, 429, 503, 429])
                with self.assertRaises(SecondaryLimit):
                    self.call(guard, lane, path)
                served = len(self.fixture.requests(path))
                with self.assertRaises(SecondaryLimit):
                    guard.acquire(lane)
                self.assertEqual(len(self.fixture.requests(path)), served)

                at = self.admissions[:9]
                gaps = [later - earlier for earlier, later in itertools.pairwise(at)]
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
        at = self.admissions
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
        threads = [
            threading.Thread(target=self.call, args=(guard, "postman", "/postman/_api/ws/proxy")) for _ in range(3)
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=30)
        self.assertEqual(len(self.fixture.requests("/postman/_api/ws/proxy")), 3)
        at = sorted(self.admissions)
        self.assertEqual(len(at), 3)
        self.assertTrue(all(b - a >= 0.4 for a, b in itertools.pairwise(at)), at)


class EvidenceTests(GuardTestCase):
    def test_waits_are_all_accounted_for_on_disk_without_the_credential(self) -> None:
        self.fixture.set("code_search", limit=10, used=7, reset_in=1.2)
        github = self.guard()
        postman = self.guard("postman")
        self.call(github, "code_search", "/search/code")
        self.call(postman, "postman", "/postman/_api/ws/proxy")
        self.call(postman, "postman", "/postman/_api/ws/proxy")

        on_disk = self.evidence_lines(guard_module.WAITS_FILE)
        self.assertEqual(
            sorted(json.dumps(e, sort_keys=True) for e in on_disk),
            sorted(json.dumps(e, sort_keys=True) for e in github.waits() + postman.waits()),
        )
        self.assertEqual(
            {(e["host"], e["kind"], e.get("cause")) for e in on_disk},
            {("github", "probe", None), ("github", "wait", "floor"), ("postman", "wait", "spacing")},
        )
        for entry in on_disk:
            if entry["kind"] == "wait":
                self.assertGreater(entry["duration_s"], 0)
        self.assertEqual(len(self.evidence_lines(guard_module.CALLS_FILE)), 3)
        for path in self.evidence.iterdir():
            self.assertNotIn(SECRET, path.read_text(encoding="utf-8"))
        self.assertTrue(all(r.authorization == f"Bearer {SECRET}" for r in self.fixture.requests("/rate_limit")))


# One process of the concurrent-cache test: a writer storing its own answer for
# one key over and over, or a reader recording each hit's headers and body.
CONCURRENT_CACHE_CHILD = """
import hashlib, importlib.util, json, sys
spec = importlib.util.spec_from_file_location("guard", sys.argv[1])
guard = importlib.util.module_from_spec(spec)
sys.modules["guard"] = guard
spec.loader.exec_module(guard)
url = "https://api.github.com/repos/o/r/contents/big"
role, letter = sys.argv[2], sys.argv[3]
if role == "write":
    body = letter.encode() * 262144
    for _ in range(40):
        guard.cache_store("GET", url, {}, 200, {"ETag": letter}, body)
else:
    hits = []
    for _ in range(400):
        cached = guard.cache_lookup("GET", url, {})
        if cached is not None:
            body = cached.body()
            hits.append([dict(cached.headers)["ETag"], cached.sha256, hashlib.sha256(body).hexdigest(), body[:1].decode()])
    print(json.dumps(hits))
"""


class ResponseCacheTests(GuardTestCase):
    """The shared GitHub response cache, driven over the loopback server's real responses."""

    def setUp(self) -> None:
        super().setUp()
        self.cache = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.cache)
        saved = {key: os.environ.get(key) for key in (guard_module.CACHE_DIR_ENV, "XDG_CACHE_HOME", "HOME")}
        os.environ[guard_module.CACHE_DIR_ENV] = str(self.cache)

        def restore() -> None:
            for key, value in saved.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value

        self.addCleanup(restore)

    def fetch(self, guard: RateLimitGuard, path: str, headers: dict[str, str]) -> tuple[int, bytes, bool]:
        """One cache-first guarded GET as every GitHub call site makes it; returns (status, body, from_cache)."""
        url = f"{self.url}{path}"
        cached = guard_module.cache_lookup("GET", url, headers)
        if cached is not None:
            return cached.status, cached.body(), True
        guard.acquire(GUARDED[path.split("?", 1)[0]])
        request = urllib.request.Request(url, headers=headers)
        try:
            # llmlint: ignore[async_typed_clients_at_boundaries] This reproduces the witness tooling's own call sites, which AGENTS.md keeps stdlib-only and synchronous so they run installless; an async client here would test a call shape no caller makes.
            response = urllib.request.urlopen(request, timeout=10)
        except urllib.error.HTTPError as refusal:
            response = refusal
        with response:
            body = response.read()
            guard.record(response)
            guard_module.cache_store("GET", url, headers, response.status, response.headers, body)
            return response.status or 0, body, False

    def test_a_repeated_fetch_of_a_cached_key_spends_no_quota(self) -> None:
        headers = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {SECRET}"}
        guard = self.guard()
        first = self.fetch(guard, "/repos/o/r/contents", headers)
        spent = self.fixture.buckets["core"]["used"]
        served = len(self.fixture.served)

        # A fresh guard stands in for another node or worktree: same key, same host cache.
        second = self.fetch(self.guard(), "/repos/o/r/contents", headers)

        self.assertEqual(first[:2], second[:2])
        self.assertEqual((first[2], second[2]), (False, True))
        self.assertEqual(self.fixture.buckets["core"]["used"], spent)
        self.assertEqual(len(self.fixture.served), served)  # no /rate_limit read, no call
        self.assertEqual(len(self.evidence_lines(guard_module.CALLS_FILE)), 1)
        for path in self.cache.rglob("*"):
            if path.is_file():
                self.assertNotIn(SECRET.encode(), path.read_bytes())

        # Accept changes the answer, so it is another key; the credential does not.
        self.assertFalse(self.fetch(guard, "/repos/o/r/contents", {"Accept": "application/vnd.github.raw+json"})[2])
        self.assertTrue(self.fetch(guard, "/repos/o/r/contents", {"Accept": "application/vnd.github+json"})[2])

    def test_refusals_and_transient_failures_are_not_cached(self) -> None:
        path = "/repos/o/r/contents"
        refused = (429, 503, 401, 407, 408)
        self.fixture.scripted[path] = [
            *((status, {}) for status in refused),
            (403, {"Retry-After": "0", "x-ratelimit-remaining": "99"}),
            (403, {"x-ratelimit-remaining": "0"}),
        ]
        guard_module.SECONDARY_ATTEMPT_BUDGET = 10
        guard_module.SECONDARY_BACKOFF_BASE_S = 0.01
        guard = self.guard()
        statuses = [self.fetch(guard, path, {}) for _ in range(len(refused) + 2)]
        self.assertEqual(
            [(status, cached) for status, _, cached in statuses], [(s, False) for s in (*refused, 403, 403)]
        )
        self.assertEqual([p for p in self.cache.rglob("*") if p.is_file()], [])
        # The next ask reaches GitHub, and its answer is the one kept.
        self.assertEqual(self.fetch(guard, path, {})[::2], (200, False))
        self.assertEqual(self.fetch(guard, path, {})[::2], (200, True))

    def test_a_tampered_or_refused_cache_entry_is_a_miss_and_asked_again(self) -> None:
        path = "/repos/o/r/contents"
        guard = self.guard()
        self.assertEqual(self.fetch(guard, path, {})[::2], (200, False))
        [meta] = list(self.cache.rglob("*.json"))
        good = json.loads(meta.read_text(encoding="utf-8"))
        for broken in (
            dict(good, status="200"),
            dict(good, status=True),
            dict(good, status=99),
            dict(good, headers=[["Content-Type", 1]]),
            dict(good, headers=[["Content-Type"]]),
            dict(good, sha256="not-a-digest"),
            dict(good, bytes=-1),
            # A refusal no `cache_store` would keep is no answer.
            dict(good, status=403, headers=[["x-ratelimit-remaining", "0"]]),
            ["not", "an", "object"],
        ):
            with self.subTest(broken=broken):
                meta.write_text(json.dumps(broken), encoding="utf-8")
                served = len(self.fixture.served)
                self.assertEqual(self.fetch(guard, path, {})[::2], (200, False))
                self.assertGreater(len(self.fixture.served), served)
                # The live answer replaced the entry, which serves the next ask.
                self.assertTrue(self.fetch(guard, path, {})[2])

    @unittest.skipIf(os.name == "nt", "a read-only directory mode does not deny writes on Windows")
    def test_a_cache_that_cannot_be_written_costs_the_caller_nothing(self) -> None:
        path = "/repos/o/r/contents"
        self.cache.chmod(0o500)
        self.addCleanup(self.cache.chmod, 0o700)
        guard = self.guard()
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            self.assertEqual(self.fetch(guard, path, {})[::2], (200, False))
        self.assertIn("rate_limit_guard: could not store a GitHub response in", stderr.getvalue())
        self.assertIn(guard_module.CACHE_DIR_ENV, stderr.getvalue())
        # Nothing was stored, so the next ask reaches GitHub again, and is kept once it can be.
        self.cache.chmod(0o700)
        self.assertEqual(self.fetch(guard, path, {})[::2], (200, False))
        self.assertEqual(self.fetch(guard, path, {})[::2], (200, True))

    def test_a_rate_limit_refusal_held_in_a_file_is_not_stored(self) -> None:
        url = f"{self.url}/repos/o/r/tarball"
        body = self.cache.parent / f"{self.cache.name}-download"
        self.addCleanup(body.unlink, missing_ok=True)
        body.write_bytes(b'{"message": "API rate limit exceeded for 127.0.0.1."}')
        self.assertIsNone(guard_module.cache_store("GET", url, {}, 403, {}, body))
        self.assertEqual([p for p in self.cache.rglob("*") if p.is_file()], [])
        # The same file holding an answer is kept, and served back whole.
        body.write_bytes(b"tree archive bytes")
        stored = guard_module.cache_store("GET", url, {}, 200, {}, body)
        self.assertIsNotNone(stored)
        cached = guard_module.cache_lookup("GET", url, {})
        assert cached is not None
        self.assertEqual((cached.status, cached.body()), (200, b"tree archive bytes"))

    def test_a_body_already_published_is_not_replaced_and_a_torn_one_is(self) -> None:
        # A reader may hold the body open, which a replace breaks on Windows, so
        # storing the same bytes again leaves that very file in place.
        url = "https://api.github.com/repos/o/r/contents/same"
        stored = guard_module.cache_store("GET", url, {}, 200, {}, b"same bytes")
        assert stored is not None
        before = stored.body_path.stat()
        again = guard_module.cache_store("GET", url, {}, 200, {}, b"same bytes")
        assert again is not None
        self.assertEqual(again.body_path, stored.body_path)
        after = stored.body_path.stat()
        self.assertEqual((after.st_ino, after.st_mtime_ns), (before.st_ino, before.st_mtime_ns))
        # A body file whose bytes no longer match its name is published again.
        stored.body_path.write_bytes(b"torn")
        self.assertIsNone(guard_module.cache_lookup("GET", url, {}))
        guard_module.cache_store("GET", url, {}, 200, {}, b"same bytes")
        cached = guard_module.cache_lookup("GET", url, {})
        assert cached is not None
        self.assertEqual(cached.body(), b"same bytes")
        self.assertEqual([path.name for path in self.cache.rglob(".*.tmp")], [])

    def test_an_answer_that_is_not_a_success_is_cached(self) -> None:
        self.fixture.scripted["/repos/o/r/contents"] = [(404, {"x-ratelimit-resource": "core"})]
        guard = self.guard()
        self.assertEqual(self.fetch(guard, "/repos/o/r/contents", {})[::2], (404, False))
        self.assertEqual(self.fetch(guard, "/repos/o/r/contents", {})[::2], (404, True))

    def test_the_key_names_method_url_and_answer_changing_headers_only(self) -> None:
        key = guard_module.cache_key
        base = key("GET", "https://api.github.com/x", {"Accept": "a"})
        self.assertEqual(base, key("get", "https://api.github.com/x", {"accept": "a", "Authorization": "Bearer t"}))
        self.assertEqual(base, key("GET", "https://api.github.com/x", {"Accept": "a", "User-Agent": "other"}))
        self.assertNotEqual(base, key("GET", "https://api.github.com/x", {"Accept": "b"}))
        self.assertNotEqual(base, key("GET", "https://api.github.com/y", {"Accept": "a"}))
        self.assertNotEqual(base, key("HEAD", "https://api.github.com/x", {"Accept": "a"}))

    def test_the_root_is_the_host_cache_outside_every_worktree(self) -> None:
        root = guard_module.github_cache_root
        del os.environ[guard_module.CACHE_DIR_ENV]
        os.environ["XDG_CACHE_HOME"] = str(self.cache / "xdg")
        self.assertEqual(root("https://api.github.com/x"), self.cache / "xdg" / "crozier" / "github-responses")
        os.environ["XDG_CACHE_HOME"] = "relative/cache"  # not absolute: ignored, as the XDG spec asks
        self.assertEqual(root("https://api.github.com/x"), Path.home() / ".cache" / "crozier" / "github-responses")
        del os.environ["XDG_CACHE_HOME"]
        self.assertEqual(root("https://raw.githubusercontent.com/o/r"), Path.home() / ".cache/crozier/github-responses")
        # A loopback server stands in for GitHub only in tests: without the override it bypasses the cache.
        self.assertIsNone(root(f"{self.url}/repos/o/r/contents"))
        self.assertIsNone(guard_module.cache_lookup("GET", f"{self.url}/repos/o/r/contents", {}))
        self.assertIsNone(guard_module.cache_store("GET", f"{self.url}/repos/o/r/contents", {}, 200, {}, b"x"))
        self.assertFalse(self.cache.joinpath("xdg").exists())

    def test_a_torn_or_altered_entry_is_a_miss(self) -> None:
        url = "https://api.github.com/repos/o/r"
        stored = guard_module.cache_store("GET", url, {}, 200, {"ETag": "x", "x-ratelimit-used": "5"}, b"body")
        assert stored is not None
        self.assertEqual(stored.headers, (("ETag", "x"),))  # a replayed quota figure is not a reading
        self.assertEqual(guard_module.cache_lookup("GET", url, {}), stored)
        stored.body_path.write_bytes(b"altered")
        self.assertIsNone(guard_module.cache_lookup("GET", url, {}))
        stored.body_path.unlink()
        self.assertIsNone(guard_module.cache_lookup("GET", url, {}))
        self.assertEqual([p.name for p in self.cache.rglob(".*.tmp")], [])

    def test_concurrent_stores_of_one_key_publish_only_whole_answers(self) -> None:
        # Two processes store different answers for one key while two read it: every
        # hit is one writer's whole answer, its headers and its body together.
        url = "https://api.github.com/repos/o/r/contents/big"
        # One answer is on record before the race, so every lookup has an entry to find.
        self.assertIsNotNone(guard_module.cache_store("GET", url, {}, 200, {"ETag": "A"}, b"A" * 262144))
        roles = (("write", "A"), ("write", "B"), ("read", "-"), ("read", "-"))
        children = [
            subprocess.Popen(
                [sys.executable, "-c", CONCURRENT_CACHE_CHILD, str(SCRIPT), role, letter],
                stdout=subprocess.PIPE,
                text=True,
            )
            for role, letter in roles
        ]
        outputs = [child.communicate(timeout=300)[0] for child in children]
        self.assertEqual([child.returncode for child in children], [0, 0, 0, 0])
        hits = [hit for output in outputs[2:] for hit in json.loads(output)]
        self.assertTrue(hits, "no reader saw a stored answer")
        for etag, recorded, read, first in hits:
            self.assertEqual((read, first), (recorded, etag))
        # Both answers were published, each under its own digest, and nothing staged is left.
        bodies = {path.name.split(".")[1] for path in self.cache.rglob("*.body")}
        expected = {hashlib.sha256(letter.encode() * 262144).hexdigest() for letter in "AB"}
        self.assertEqual(bodies, expected)
        self.assertEqual([path.name for path in self.cache.rglob(".*.tmp")], [])
        final = guard_module.cache_lookup("GET", url, {})
        assert final is not None
        self.assertIn(final.sha256, expected)


class QuotaStatusTests(GuardTestCase):
    def status(self, url: str) -> subprocess.CompletedProcess[str]:
        env = {**os.environ, "CROZIER_GITHUB_API_URL": url}
        return subprocess.run(
            [sys.executable, str(SCRIPT), "status"], env=env, capture_output=True, text=True, timeout=30
        )

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
        self.assertIn("BELOW FLOOR", over)
        self.assertNotIn("BELOW FLOOR", core)
        self.assertIn("floor 40% remaining", lines[0])
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

    def test_a_response_without_resources_fails_with_a_next_action(self) -> None:
        for body in (b'{"message": "Not Found"}', b"[]"):
            with self.subTest(body=body):
                self.fixture.rate_limit_body = body
                result = self.status(self.url)
                self.assertEqual(result.returncode, 1)
                self.assertIn("no `resources` object", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_an_api_root_off_github_https_or_loopback_http_fails_with_a_next_action(self) -> None:
        result = self.status("http://example.invalid")
        self.assertEqual(result.returncode, 1)
        self.assertIn("CROZIER_GITHUB_API_URL must use https://api.github.com or a loopback HTTP URL", result.stderr)
        self.assertIn("unset it or point it at the GitHub REST API", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertNotIn(SECRET, result.stdout + result.stderr)

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
