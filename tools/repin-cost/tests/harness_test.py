"""Drive the public CLI through real journals, git and guarded HTTP."""

# llmlint: ignore-file[modern_domain_modeling] These dictionaries are the wire shapes the harness reads, written as a journal line or a GitHub response would be; a typed model of them would hide the JSON the journeys exist to serve.
# llmlint: ignore-file[shell_test_tiers_stay_split] This suite drives only git, python3 and loopback servers on 127.0.0.1, which every leg carries and which reach no network; it installs nothing and runs in one to two minutes (see `metadata.description` on the target in project.json).
from __future__ import annotations

import csv
import hashlib
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

PYTHON = str(Path(sys.executable).resolve())
SOURCE = Path(__file__).resolve().parents[1]
GUARD = SOURCE.parent / "witness-search/rate_limit_guard.py"
UNTIL = "2026-01-02T00:00:00Z"
OUTSTANDING = "docs/openapi-surface/witness-search-registries/outstanding.tsv"
# An invented stand-in for a private repository's name; no real one belongs in this suite.
STAND_IN = "Zephyrquill"
LIVE_RUN = "Close-crozier-s-remaining-Fern-departures-and-unproven-features-and-combinations"


def digest(identifier):
    """The published form of a host identifier, spelled out here so a change to it fails."""
    return "id-" + hashlib.sha256(identifier.encode()).hexdigest()[:12]


class HarnessTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=os.environ.get("ONEPIPELINE_NODE_SCRATCH_DIR"))
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        tool = self.repo / "tools/repin-cost"
        tool.mkdir(parents=True)
        for name in ("repin_cost.py", "gh.py", "comparison.py", "public_id.py"):
            shutil.copyfile(SOURCE / name, tool / name)
        guard = self.repo / "tools/witness-search/rate_limit_guard.py"
        guard.parent.mkdir()
        shutil.copyfile(GUARD, guard)
        self.cli = tool / "repin_cost.py"
        self.git("init", "-b", "main")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Repin test")
        self.git("config", "commit.gpgsign", "false")
        self.initial = self.commit("initial")
        self.git("checkout", "-b", "first")
        self.first = self.commit("first")
        self.git("checkout", "-b", "both")
        self.second = self.commit("second")
        self.git("checkout", "main")
        self.git("checkout", "-b", "second-only")
        self.git("cherry-pick", self.second)
        self.only_second = self.git("rev-parse", "HEAD").strip()
        # The two named commits must be independent ancestors to exercise each missing half.
        self.second = self.only_second
        self.git("checkout", "main")
        self.git("merge", "--no-ff", "first", "-m", "first landing")
        self.git("merge", "--no-ff", "second-only", "-m", "second landing")
        self.main = self.git("rev-parse", "HEAD").strip()
        self.git("remote", "add", "origin", str(self.repo))
        self.runs = self.root / "runs"
        self.run_dir = self.runs / "sample"
        self.run_dir.mkdir(parents=True)
        (self.run_dir / "plan.json").write_text('"nickderobertis/crozier"', encoding="utf-8")
        self.journal = []
        self.results = self.root / "results.py"
        self.results.write_text(
            'import json\nprint(json.dumps({"nodes": [{"id": "node", "status": "done", "outcome": "merged"}]}))\n',
            encoding="utf-8",
        )
        self.requests = []
        self.responses = {}
        self.redirects = {}
        self.dropped = set()
        self.auth = {}
        self.quota = "ok"
        owner = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, format, *args):
                pass

            def do_GET(self):
                owner.requests.append(self.path)
                owner.auth[self.path] = self.headers.get("Authorization")
                if self.path in owner.dropped:
                    self.close_connection = True
                    return
                if self.path in owner.redirects:
                    self.send_response(302)
                    self.send_header("Location", owner.redirects[self.path])
                    self.end_headers()
                    return
                if self.path == "/rate_limit":
                    status = 503 if owner.quota == "refuse" else 200
                    used = 99 if owner.quota == "wait" else 1
                    payload = {
                        "resources": {
                            "core": {
                                "limit": 100,
                                "used": used,
                                "remaining": 100 - used,
                                "reset": int(time.time()) + 3600,
                            }
                        }
                    }
                    body = json.dumps(payload).encode()
                else:
                    status, payload = owner.responses.get(self.path, (200, {"workflow_runs": []}))
                    body = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(body)

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.env = {
            **os.environ,
            "GITHUB_TOKEN": "test-token",
            "GH_TOKEN": "test-token",
            "CROZIER_GITHUB_API_URL": f"http://127.0.0.1:{self.server.server_port}",
            "CROZIER_GITHUB_CACHE_DIR": str(self.root / "cache"),
            "ONEPIPELINE_RESULTS_COMMAND": json.dumps([PYTHON, str(self.results)]),
        }

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.repo), *args], check=True, capture_output=True, text=True).stdout

    def commit(self, name):
        # Separate files let the independent landing branches merge without conflicts.
        (self.repo / (name + ".txt")).write_text(name, encoding="utf-8")
        self.git("add", "--all")
        self.git("commit", "-m", name)
        return self.git("rev-parse", "HEAD").strip()

    def event(self, kind, branch, payload, when="2026-01-01T01:00:00Z"):
        self.journal.append(
            {
                "ts": when,
                "kind": kind,
                "labels": {"node": "node", "session": branch, "identity": "github.com/nickderobertis/crozier"},
                "payload": {"branch": branch, **payload},
            }
        )

    def change(self, pr, base, own=False):
        branch = f"change-{pr}"
        self.git("checkout", "-b", branch, base)
        if own:
            self.git("merge", "--no-ff", "first", "-m", "own first")
            self.git("merge", "--no-ff", "second-only", "-m", "own second")
        head = self.commit(branch)
        self.git("update-ref", f"refs/pull/{pr}/head", head)
        self.event("node-dispatched", branch, {"attempt": 1})
        self.event("change-opened", branch, {"id": pr})
        self.event("push", branch, {"accepted": True, "head": head})
        self.git("checkout", "main")
        return branch, head

    def command(self, window=None, out="out"):
        (self.run_dir / "events.jsonl").write_text(
            "".join(json.dumps(e) + "\n" for e in self.journal), encoding="utf-8"
        )
        return [
            PYTHON,
            str(self.cli),
            "--window",
            window or f"base-carries:{self.first},{self.second}",
            "--runs-root",
            str(self.runs),
            "--until",
            UNTIL,
            "--out",
            str(self.root / out),
        ]

    def invoke(self, **kwargs):
        result = subprocess.run(self.command(**kwargs), env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        return self.root / kwargs.get("out", "out")

    def rows(self, out, name):
        with (out / name).open(encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle, delimiter="\t"))

    def test_selection_and_cache(self):
        self.change(1, self.main)
        self.change(2, self.first)
        self.change(3, self.second)
        self.change(4, self.initial)
        self.journal[-1]["labels"]["node"] = "retired"
        self.change(5, self.initial, own=True)
        # Today's fetched head carries both, but the cutoff's pushed head does not.
        branch, _ = self.change(6, self.initial)
        self.git("update-ref", "refs/pull/6/head", self.main)
        self.event("push", branch, {"accepted": True, "head": self.main}, "2026-01-03T00:00:00Z")
        out = self.invoke()
        self.assertEqual([r["pr"] for r in self.rows(out, "changes.tsv")], ["1"])
        self.assertEqual(self.rows(out, "changes.tsv")[0]["nodes"], f"{digest('node')}=merged")
        excluded = {r["pr"]: r["reason"] for r in self.rows(out, "excluded.tsv")}
        self.assertEqual(set(excluded), {"2", "3", "4", "5", "6"})
        self.assertIn(self.second[:12], excluded["2"])
        self.assertIn(self.first[:12], excluded["3"])
        self.assertIn("own commits carry", excluded["5"])
        self.assertIn("base", excluded["6"])
        retired = next(r for r in self.rows(out, "excluded.tsv") if r["pr"] == "4")
        self.assertIn(f"{digest('retired')}=unavailable (node retired; not in current results)", retired["nodes"])
        before = list(self.requests)
        self.invoke(out="repeat")
        self.assertEqual(self.requests, before)
        totals = json.loads((self.root / "repeat/totals.json").read_text())
        self.assertEqual(totals["github"], {"uncached_calls": 0, "cache_hits": 1})

    def test_failures_conflicts_and_intervals(self):
        branch, head = self.change(1, self.main)
        logs = [
            b"E AssertionError: site abc matches 0 functions; anchor it\nFailed tasks:\n - surface-census:test-census\n",
            b"E AssertionError: re-pin the digest; port digest changed\nFailed tasks:\n - surface-census:test-census\n",
            f"E AssertionError: {OUTSTANDING} is stale\nFailed tasks:\n - witness-search:test-index\n".encode(),
        ]
        runs = []
        for i, log in enumerate(logs, 1):
            start, end = f"2026-01-01T0{i}:00:00Z", f"2026-01-01T0{i}:10:00Z"
            runs.append(
                {
                    "id": i,
                    "name": "ci",
                    "event": "pull_request",
                    "run_started_at": start,
                    "updated_at": end,
                    "conclusion": "failure",
                    "head_sha": head,
                }
            )
            self.responses[f"/repos/nickderobertis/crozier/actions/runs/{i}/jobs?filter=latest&per_page=100&page=1"] = (
                200,
                {
                    "jobs": [
                        {"id": i, "name": "check", "conclusion": "failure", "started_at": start, "completed_at": end}
                    ]
                },
            )
            self.responses[f"/repos/nickderobertis/crozier/actions/jobs/{i}/logs"] = (200, log)
            self.event(
                "gate-run",
                branch,
                {
                    "started_at": start,
                    "ended_at": end,
                    "verdict": "failed",
                    "checks": [{"name": "gate", "conclusion": "failure"}],
                },
                end,
            )
            self.event("node-dispatched", branch, {"attempt": i + 1}, f"2026-01-01T0{i}:15:00Z")
        self.responses[f"/repos/nickderobertis/crozier/actions/runs?branch={branch}&per_page=100&page=1"] = (
            200,
            {"workflow_runs": runs},
        )
        self.event(
            "sync-conflict", branch, {"paths": ["docs/openapi-surface/golden-reach.tsv"]}, "2026-01-01T03:20:00Z"
        )
        self.event("sync-conflict", branch, {"paths": ["src/lib.rs"]}, "2026-01-01T03:25:00Z")
        self.event(
            "change-merged",
            branch,
            {"sha": head, "url": "https://github.com/nickderobertis/crozier/pull/1"},
            "2026-01-01T04:00:00Z",
        )
        out = self.invoke(window="runs:sample")
        events = self.rows(out, "events.tsv")
        self.assertEqual(
            [r["kind"] for r in events],
            ["site-anchor", "port-digest", "other-artifact:" + OUTSTANDING, "derived-conflict"],
        )
        totals = json.loads((out / "totals.json").read_text())
        self.assertEqual(totals["census"]["failures"], 2)
        self.assertEqual(totals["conflicts"]["derived"], 1)
        self.assertEqual(totals["conflicts"]["code"], 1)
        self.assertEqual(totals["census"]["runner_min"], 20)
        self.assertEqual(totals["census"]["pub_observed"], 2)
        self.assertEqual(events[2]["pub_status"], "unresolved")
        self.assertEqual(events[2]["wait_min"], "")
        self.assertEqual(events[2]["pub_wait_min"], "")

    def test_non_200_and_recovery(self):
        branch, _ = self.change(1, self.main)
        path = f"/repos/nickderobertis/crozier/actions/runs?branch={branch}&per_page=100&page=1"
        self.responses[path] = (503, {"message": "unavailable"})
        done = subprocess.run(self.command(), env=self.env, capture_output=True, text=True, timeout=20)
        self.assertNotEqual(done.returncode, 0)
        self.assertIn("GitHub answered 503", done.stderr)
        self.assertFalse((self.root / "out/totals.json").exists())
        self.responses[path] = (200, {"workflow_runs": []})
        self.invoke(out="recovered")

    def test_missing_job_log_stops(self):
        branch, head = self.change(1, self.main)
        run = {
            "id": 1,
            "name": "ci",
            "event": "pull_request",
            "run_started_at": "2026-01-01T01:00:00Z",
            "updated_at": "2026-01-01T01:10:00Z",
            "conclusion": "failure",
            "head_sha": head,
        }
        self.responses[f"/repos/nickderobertis/crozier/actions/runs?branch={branch}&per_page=100&page=1"] = (
            200,
            {"workflow_runs": [run]},
        )
        self.responses["/repos/nickderobertis/crozier/actions/runs/1/jobs?filter=latest&per_page=100&page=1"] = (
            200,
            {
                "jobs": [
                    {
                        "id": 1,
                        "name": "check",
                        "conclusion": "failure",
                        "started_at": run["run_started_at"],
                        "completed_at": run["updated_at"],
                    }
                ]
            },
        )
        self.responses["/repos/nickderobertis/crozier/actions/jobs/1/logs"] = (404, {"message": "expired log"})
        done = subprocess.run(self.command(), env=self.env, capture_output=True, text=True, timeout=20)
        self.assertNotEqual(done.returncode, 0)
        self.assertIn("GitHub answered 404", done.stderr)
        self.assertFalse((self.root / "out/totals.json").exists())

    def serve_runs(self, branch, runs, logs):
        """Answer the branch's run list and each run's one failed job, whose log is `logs[run id]`."""
        self.responses[f"/repos/nickderobertis/crozier/actions/runs?branch={branch}&per_page=100&page=1"] = (
            200,
            {"workflow_runs": runs},
        )
        for run in runs:
            job = {
                "id": run["id"],
                "name": "check",
                "conclusion": run["conclusion"],
                "started_at": run["run_started_at"],
                "completed_at": run["updated_at"],
            }
            self.responses[
                f"/repos/nickderobertis/crozier/actions/runs/{run['id']}/jobs?filter=latest&per_page=100&page=1"
            ] = (200, {"jobs": [job]})
            if run["id"] in logs:
                self.responses[f"/repos/nickderobertis/crozier/actions/jobs/{run['id']}/logs"] = (
                    200,
                    logs[run["id"]],
                )

    def ci_run(self, run_id, hour, head, conclusion="failure"):
        return {
            "id": run_id,
            "name": "ci",
            "event": "pull_request",
            "run_started_at": f"2026-01-01T{hour:02}:00:00Z",
            "updated_at": f"2026-01-01T{hour:02}:10:00Z",
            "conclusion": conclusion,
            "head_sha": head,
        }

    def test_kinds_fixes_intervals_and_summary(self):
        branch, head1 = self.change(1, self.main)
        self.git("checkout", branch)
        (self.repo / "docs/openapi-surface").mkdir(parents=True)
        (self.repo / "tools/surface-census").mkdir(parents=True)
        sites = self.repo / "docs/openapi-surface/golden-reach-sites.tsv"
        census = self.repo / "tools/surface-census/openapi-surface-census.py"
        sites.write_text("moved\n", encoding="utf-8")
        census.write_text("# no digest in this change\n", encoding="utf-8")
        head2 = self.commit("re-anchor")
        census.write_text('DIGEST = "0123456789abcdef"\n', encoding="utf-8")
        (self.repo / "docs/openapi-surface/golden-reach.tsv").write_text("row\n", encoding="utf-8")
        head3 = self.commit("remeasure")
        self.git("update-ref", "refs/pull/1/head", head3)
        self.git("checkout", "main")
        runs = [
            self.ci_run(1, 1, head1),
            self.ci_run(2, 2, head2),
            self.ci_run(3, 3, head3),
            self.ci_run(4, 4, head3, "success"),
        ]
        self.serve_runs(
            branch,
            runs,
            {
                1: b"E AssertionError: unrelated words\nFAILED tools/surface-census/tests/surface_census_test.py::x\n",
                2: b"E AssertionError: site s matches 0 lines; anchor it; re-pin the digest\n"
                b"Failed tasks:\n - surface-census:test-census\n",
                3: b"E AssertionError: docs/openapi-surface/golden-reach.tsv is stale\n"
                b"Failed tasks:\n - surface-census:test-reach\n",
            },
        )
        failed = [{"name": "gate", "conclusion": "failure"}]
        self.event(
            "gate-run",
            branch,
            {
                "started_at": "2026-01-01T02:00:00Z",
                "ended_at": "2026-01-01T02:10:00Z",
                "verdict": "failed",
                "checks": failed,
            },
            "2026-01-01T02:10:00Z",
        )
        self.event(
            "gate-run",
            branch,
            {
                "started_at": "2026-01-01T04:00:00Z",
                "ended_at": "2026-01-01T04:10:00Z",
                "verdict": "passed",
                "checks": [],
            },
            "2026-01-01T04:10:00Z",
        )
        self.event("node-dispatched", branch, {"attempt": 1}, "2026-01-01T02:20:00Z")
        self.journal[-1]["labels"]["node"] = "node-r1"
        self.event(
            "sync-conflict",
            branch,
            {"paths": ["tests/fixtures/departures-ledger.tsv", "src/lib.rs"]},
            "2026-01-01T03:20:00Z",
        )
        self.event("node-dispatched", "never-opened", {"attempt": 2})
        # One branch across two runs is one change.
        other = self.runs / "other-run"
        other.mkdir()
        (other / "plan.json").write_text('"nickderobertis/crozier"', encoding="utf-8")
        retry = {
            "ts": "2026-01-01T02:30:00Z",
            "kind": "node-dispatched",
            "labels": {"node": "elsewhere"},
            "payload": {"branch": branch, "attempt": 2},
        }
        (other / "events.jsonl").write_text(json.dumps(retry) + "\n", encoding="utf-8")

        out = self.invoke(window="runs:sample,other-run")

        rows = self.rows(out, "changes.tsv")
        self.assertEqual([r["pr"] for r in rows], ["1"])
        self.assertEqual(rows[0]["runs"], f"{digest('other-run')};{digest('sample')}")
        self.assertEqual(
            rows[0]["rewrote"],
            ";".join(
                sorted(
                    [
                        "docs/openapi-surface/golden-reach-sites.tsv",
                        "docs/openapi-surface/golden-reach.tsv",
                        "tools/surface-census/openapi-surface-census.py",
                    ]
                )
            ),
        )
        events = self.rows(out, "events.tsv")
        by_run = {r["ci_run"]: r for r in events if r["ci_run"] == "1"}
        # The text names no kind, so the fix decides it; a census script change with no digest is no port repin.
        self.assertEqual(by_run["1"]["kind"], "site-anchor")
        self.assertEqual(by_run["1"]["fix_files"], "docs/openapi-surface/golden-reach-sites.tsv")
        self.assertEqual(
            [(r["kind"], r["runner_min"]) for r in events if r["ci_run"] == "2"],
            [("port-digest", "5.0"), ("site-anchor", "5.0")],
        )
        self.assertEqual([r["kind"] for r in events if r["ci_run"] == "3"], ["measured-count"])
        self.assertEqual(
            [r["pub_wait_min"] for r in events if r["ci_run"] == "2"],
            ["55.0", "55.0"],
        )
        totals = json.loads((out / "totals.json").read_text())
        census = totals["census"]
        self.assertEqual(census["failures"], 3)
        self.assertEqual(census["wait_min"], 150)
        self.assertEqual(census["median_cycle_min"], 60)
        self.assertEqual((census["pub_observed"], census["pub_wait_min"], census["pub_unresolved"]), (1, 110, 0))
        # Two re-dispatches follow the failure; only the first is charged to it, per the method.
        self.assertEqual((totals["redispatches"], census["redispatches"]), (2, 1))
        self.assertEqual((totals["conflicts"]["derived"], totals["conflicts"]["mixed"]), (1, 1))
        self.assertEqual(totals["conflicts"]["wait_min"], 40)
        self.assertEqual(totals["by_kind"]["site-anchor"]["events"], 2)
        self.assertEqual(totals["by_kind"]["site-anchor"]["runner_min"], 15)
        self.assertEqual(totals["artifacts_outside_census"][0]["artifact"], "tests/fixtures/departures-ledger.tsv")
        self.assertEqual(self.rows(out, "excluded.tsv")[0]["reason"], "no pull request: not a change")
        summary = (out / "summary.md").read_text()
        self.assertIn("Census-tier CI failures: 3 (3.00 per change, 1 changes hit)", summary)
        self.assertIn("Examined and excluded from every total: 1 (1 without a pull request)", summary)

        # What the harness writes is what `compare` reads, so the two cannot drift apart unseen.
        done = subprocess.run(
            [PYTHON, str(self.cli), "compare", str(out), str(out)], capture_output=True, text=True, timeout=20
        )
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertIn(
            "| `census.failures` | 3.00 | 3.00 | 3.00 | 3.00 | +0.00 | +0.00 |", (out / "comparison.md").read_text()
        )

    def test_log_redirect_drops_the_credential_and_later_pages_are_read(self):
        branch, head = self.change(1, self.main)
        filler = [dict(self.ci_run(100 + i, 1, head, "success"), name="other") for i in range(100)]
        run = self.ci_run(7, 1, head)
        self.serve_runs(branch, [], {})
        self.serve_runs(branch, filler, {})
        page2 = f"/repos/nickderobertis/crozier/actions/runs?branch={branch}&per_page=100&page=2"
        self.responses[page2] = (200, {"workflow_runs": [run]})
        self.serve_jobs_for(run)
        log = "/repos/nickderobertis/crozier/actions/jobs/7/logs"
        self.redirects[log] = f"http://127.0.0.1:{self.server.server_port}/blob/7"
        self.responses["/blob/7"] = (200, b"E AssertionError: x\nFailed tasks:\n - surface-census:test-census\n")
        out = self.invoke()
        totals = json.loads((out / "totals.json").read_text())
        self.assertEqual((totals["ci_runs"], totals["census"]["failures"]), (1, 1))
        self.assertEqual(self.auth[log], "Bearer test-token")
        self.assertIsNone(self.auth["/blob/7"])

    def serve_jobs_for(self, run):
        self.responses[
            f"/repos/nickderobertis/crozier/actions/runs/{run['id']}/jobs?filter=latest&per_page=100&page=1"
        ] = (
            200,
            {
                "jobs": [
                    {
                        "id": run["id"],
                        "name": "check",
                        "conclusion": run["conclusion"],
                        "started_at": run["run_started_at"],
                        "completed_at": run["updated_at"],
                    }
                ]
            },
        )

    def test_ordinary_failure_artifact_kinds_merges_and_temporary_refs(self):
        branch, head1 = self.change(1, self.main)
        self.git("checkout", branch)
        paths = {
            "docs/openapi-surface/handwritten/orchard/evidence.toml": True,
            "docs/openapi-surface/handwritten/orchard/spec.yml": False,
            "shots/baseline/run.png": True,
            "assets/crozier.schema.json": True,
            "tests/fixtures/CORPUS.md": True,
            "docs/fern-refusals/classes.tsv": True,
            "src/lib.rs": False,
            "docs/openapi-surface/scenario-proof-index.tsv": True,
            "docs/screenshots/run.png": True,
            "tests/fixtures/corpus-remote-ref-pins.tsv": True,
            "llmlint-plugins/lock.json": True,
            "docs/fern-measurements/cases.tsv": True,
            "docs/fern-measurements/runs.json": True,
            "docs/openapi-surface/witness-search-x/census.tsv": True,
            "docs/openapi-surface/parameters.md": True,
            "docs/openapi-surface/witness-search-x/README.md": False,
        }
        for name in paths:
            target = self.repo / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("v1\n", encoding="utf-8")
        head2 = self.commit("artifacts")
        # Main moves the same table and a second one; the worker resolves the first by hand.
        self.git("checkout", "main")
        sites = self.repo / "docs/openapi-surface/golden-reach-sites.tsv"
        sites.parent.mkdir(parents=True, exist_ok=True)
        sites.write_text("main\n", encoding="utf-8")
        (self.repo / "docs/openapi-surface/golden-reach.tsv").write_text("main\n", encoding="utf-8")
        self.commit("main-tables")
        self.git("checkout", branch)
        sites.write_text("branch\n", encoding="utf-8")
        self.commit("branch-table")
        subprocess.run(["git", "-C", str(self.repo), "merge", "main", "--no-edit"], capture_output=True, check=False)
        sites.write_text("resolved\n", encoding="utf-8")
        self.git("add", "--all")
        self.git("commit", "--no-edit")
        head3 = self.git("rev-parse", "HEAD").strip()
        self.git("update-ref", "refs/pull/1/head", head3)
        self.git("checkout", "main")
        self.serve_runs(
            branch,
            [self.ci_run(1, 1, head1), self.ci_run(2, 2, head2), self.ci_run(3, 3, head3, "success")],
            {
                1: b"E AssertionError: formatting differs\nFailed tasks:\n - crozier:test\n",
                2: b"E AssertionError: unrelated words\nFailed tasks:\n - surface-census:test-census\n",
            },
        )
        out = self.invoke(window="runs:sample")
        row = self.rows(out, "changes.tsv")[0]
        self.assertEqual((row["ci_failed"], row["other_failures"], row["census_failures"]), ("2", "1", "1"))
        events = self.rows(out, "events.tsv")
        self.assertEqual([e["ci_run"] for e in events], ["2", "2"])
        # The fix range holds the hand-resolved merge and the commits it imported from main.
        self.assertEqual(
            events[0]["fix_files"], "docs/openapi-surface/golden-reach-sites.tsv;docs/openapi-surface/golden-reach.tsv"
        )
        self.assertEqual([e["kind"] for e in events], ["measured-count", "site-anchor"])
        rewrote = set(row["rewrote"].split(";"))
        for name, pinned in paths.items():
            shown = "shots/baseline/" if name.startswith("shots/") else name
            shown = "docs/screenshots/" if name.startswith("docs/screenshots/") else shown
            self.assertEqual(shown in rewrote, pinned, name)
        self.assertEqual(self.git("for-each-ref", "refs/repin-cost/"), "")

    def test_logs_jobs_fallbacks_and_conflict_shares(self):
        branch, head1 = self.change(1, self.main)
        self.git("checkout", branch)
        ledger = self.repo / "tests/fixtures/departures-ledger.tsv"
        ledger.parent.mkdir(parents=True, exist_ok=True)
        ledger.write_text("v1\n", encoding="utf-8")
        head2 = self.commit("ledger")
        self.git("checkout", "main")
        run1 = self.ci_run(1, 1, head1)
        run2 = self.ci_run(2, 2, head1)
        run3 = self.ci_run(3, 3, head2)
        run4 = self.ci_run(4, 4, head2, "success")
        run5 = self.ci_run(5, 5, head2)
        self.serve_runs(branch, [run1, run2, run3, run4, run5], {})

        def jobs(run, count):
            return (
                200,
                {
                    "jobs": [
                        {
                            "id": run["id"] * 10 + i,
                            "name": "gate" if count > 1 and i == count else f"check-{i}",
                            "conclusion": "failure",
                            "started_at": run["run_started_at"],
                            "completed_at": run["updated_at"],
                        }
                        for i in range(1, count + 1)
                    ]
                },
            )

        for run, count in ((run1, 3), (run2, 1), (run3, 1), (run5, 1)):
            self.responses[
                f"/repos/nickderobertis/crozier/actions/runs/{run['id']}/jobs?filter=latest&per_page=100&page=1"
            ] = jobs(run, count)
        logs = {
            # Timestamped, coloured lines across two failed jobs; the gate job's log is never read.
            11: b"2026-01-01T01:05:00.0000000Z \x1b[31mE AssertionError: site s matches 0 lines; anchor it\x1b[0m\n"
            b"2026-01-01T01:05:00.0000000Z Failed tasks:\n2026-01-01T01:05:00.0000000Z  - surface-census:test-census\n",
            12: b"E AssertionError: re-pin the digest\nFailed tasks:\n - surface-census:test-reach\n",
            # Stale with nothing named: the fix names the artifact.
            21: b"E AssertionError: the table is stale\nFailed tasks:\n - witness-search:test-index\n",
            # Stale with nothing named and no fix: the task names it.
            31: b"E AssertionError: the table is stale\nFailed tasks:\n - corpus:test-sources\n",
            51: b"E AssertionError: the table is stale\nFailed tasks:\n - corpus:test-sources\n",
        }
        for job, body in logs.items():
            self.responses[f"/repos/nickderobertis/crozier/actions/jobs/{job}/logs"] = (200, body)
        self.event(
            "sync-conflict",
            branch,
            {
                "paths": [
                    "docs/openapi-surface/golden-reach.tsv",
                    "tests/fixtures/CORPUS.md",
                    "tests/fixtures/compared-goldens.json",
                ]
            },
            "2026-01-01T01:20:00Z",
        )
        self.event(
            "gate-run",
            branch,
            {
                "started_at": "2026-01-01T01:30:00Z",
                "ended_at": "2026-01-01T01:40:00Z",
                "verdict": "passed",
                "checks": [],
            },
            "2026-01-01T01:40:00Z",
        )
        out = self.invoke(window="runs:sample")
        events = self.rows(out, "events.tsv")
        first = [e for e in events if e["ci_run"] == "1"]
        self.assertEqual(
            [(e["kind"], e["runner_min"]) for e in first], [("port-digest", "15.0"), ("site-anchor", "15.0")]
        )
        self.assertEqual(first[0]["excerpt"], "E AssertionError: site s matches 0 lines; anchor it")
        self.assertNotIn("/repos/nickderobertis/crozier/actions/jobs/13/logs", self.requests)
        self.assertEqual(
            [e["kind"] for e in events if e["ci_run"] == "2"], ["other-artifact:tests/fixtures/departures-ledger.tsv"]
        )
        self.assertEqual([e["kind"] for e in events if e["ci_run"] == "5"], ["other-artifact:task:corpus:test-sources"])
        totals = json.loads((out / "totals.json").read_text())
        # A 10-minute conflict wait, two of whose three derived files sit outside the census.
        shares = {r["artifact"]: r["cycle_min"] for r in totals["artifacts_outside_census"]}
        conflict = next(e for e in events if e["source"] == "journal")
        self.assertEqual(
            (conflict["kind"], conflict["tier"], conflict["wait_min"]), ("derived-conflict", "census", "10.0")
        )
        self.assertEqual(shares["tests/fixtures/CORPUS.md"], 3.3)
        self.assertEqual(shares["tests/fixtures/compared-goldens.json"], 3.3)

    def test_journal_identity_ci_filters_and_overlapping_runs(self):
        branch, head = self.change(1, self.main)
        session = "session-1"
        self.journal[0]["labels"]["session"] = session
        # Carries no branch: the session's earlier event names it.
        self.journal.append(
            {
                "ts": "2026-01-01T02:00:00Z",
                "kind": "node-dispatched",
                "labels": {"session": session, "node": "by-session"},
                "payload": {"attempt": 2},
            }
        )
        # Carries neither: the node's earlier event names it.
        self.journal.append(
            {
                "ts": "2026-01-01T02:10:00Z",
                "kind": "node-dispatched",
                "labels": {"node": "node"},
                "payload": {"attempt": 3},
            }
        )
        # Another repository's event on a branch of the same name is not this change's.
        self.event("node-dispatched", branch, {"attempt": 9})
        self.journal[-1]["labels"]["identity"] = "github.com/someone/else"
        self.event("node-dispatched", branch, {"attempt": 10}, "2026-01-03T00:00:00Z")
        overlapped = self.ci_run(1, 1, head)
        overlapped["updated_at"] = "2026-01-01T02:30:00Z"
        next_run = self.ci_run(2, 2, head, "success")
        push_event = dict(self.ci_run(3, 3, head), event="push")
        after_cutoff = dict(self.ci_run(4, 4, head), run_started_at="2026-01-03T00:00:00Z")
        self.serve_runs(
            branch,
            [overlapped, next_run, push_event, after_cutoff],
            {1: b"E AssertionError: x\nFailed tasks:\n - surface-census:test-census\n"},
        )
        out = self.invoke(window="runs:sample")
        row = self.rows(out, "changes.tsv")[0]
        self.assertEqual((row["ci_runs"], row["redispatches"]), ("2", "2"))
        self.assertIn(digest("by-session"), row["nodes"])
        self.assertEqual(
            (row["census_failures"], row["census_wait_min"], row["census_ci_unresolved"]), ("1", "0.0", "1")
        )
        event = self.rows(out, "events.tsv")[0]
        self.assertEqual((event["ci_next_run"], event["wait_min"]), ("unresolved", ""))

    @unittest.skipIf(os.name == "nt", "the stand-in gh is a POSIX script")
    def test_with_no_token_in_the_environment_gh_supplies_it(self):
        self.change(1, self.main)
        fake = self.root / "bin"
        fake.mkdir()
        gh = fake / "gh"
        gh.write_text("#!/bin/sh\necho from-gh\n", encoding="utf-8")
        gh.chmod(0o755)
        env = {k: v for k, v in self.env.items() if k not in ("GITHUB_TOKEN", "GH_TOKEN")}
        env["PATH"] = f"{fake}{os.pathsep}{env['PATH']}"
        done = subprocess.run(self.command(), env=env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(
            self.auth["/repos/nickderobertis/crozier/actions/runs?branch=change-1&per_page=100&page=1"],
            "Bearer from-gh",
        )

    def test_a_branch_name_is_quoted_in_the_run_query(self):
        self.change(1, self.main)
        odd = "odd&name#1"
        for event in self.journal:
            event["payload"]["branch"] = odd
        self.invoke()
        self.assertIn(
            "/repos/nickderobertis/crozier/actions/runs?branch=odd%26name%231&per_page=100&page=1", self.requests
        )

    def test_a_missing_journal_and_a_bad_results_command_stop_and_recover(self):
        self.change(1, self.main)
        command = self.command(window="runs:absent")
        done = subprocess.run(command, env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertIn("no journal for run 'absent'", done.stderr)
        (self.runs / "absent").mkdir()
        (self.runs / "absent" / "events.jsonl").write_text("", encoding="utf-8")
        done = subprocess.run(command, env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 0, done.stderr)
        for value in ("[]", '"results"', '[""]'):
            env = {**self.env, "ONEPIPELINE_RESULTS_COMMAND": value}
            done = subprocess.run(self.command(), env=env, capture_output=True, text=True, timeout=20)
            self.assertEqual(done.returncode, 1, done.stderr)
            self.assertIn("ONEPIPELINE_RESULTS_COMMAND must be", done.stderr)

    def test_a_ci_time_or_head_that_cannot_be_trusted_stops(self):
        branch, head = self.change(1, self.main)
        run = self.ci_run(7, 1, head)
        good = {"id": 7, "name": "check", "conclusion": "failure", "started_at": run["run_started_at"]}
        jobs = "/repos/nickderobertis/crozier/actions/runs/7/jobs?filter=latest&per_page=100&page=1"
        cases = (
            (run, dict(good, completed_at=None), "None"),
            (run, dict(good, completed_at="2026-01-01T01:10:00"), "with an offset"),
            (dict(run, head_sha="not-a-sha"), dict(good, completed_at=run["updated_at"]), "not a commit sha"),
            (dict(run, run_started_at=""), dict(good, completed_at=run["updated_at"]), "with an offset"),
        )
        for i, (served, job, expected) in enumerate(cases):
            self.serve_runs(branch, [served], {})
            self.responses[jobs] = (200, {"jobs": [job]})
            env = {**self.env, "CROZIER_GITHUB_CACHE_DIR": str(self.root / f"times-{i}")}
            done = subprocess.run(self.command(out=f"times-{i}"), env=env, capture_output=True, text=True, timeout=20)
            self.assertEqual(done.returncode, 1, done.stderr)
            self.assertIn(expected, done.stderr)
            self.assertNotIn("Traceback", done.stderr)

    def test_a_redirect_off_the_api_and_a_wrong_identifier_stop(self):
        branch, head = self.change(1, self.main)
        run = self.ci_run(7, 1, head)
        self.serve_runs(branch, [run], {})
        log = "/repos/nickderobertis/crozier/actions/jobs/7/logs"
        self.redirects[log] = "http://elsewhere.invalid/blob"
        done = subprocess.run(self.command(), env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertIn("refusing to follow", done.stderr)
        self.assertNotIn("Traceback", done.stderr)
        self.responses[f"/repos/nickderobertis/crozier/actions/runs?branch={branch}&per_page=100&page=1"] = (
            200,
            {"workflow_runs": [dict(run, id=True)]},
        )
        env = {**self.env, "CROZIER_GITHUB_CACHE_DIR": str(self.root / "fresh")}
        done = subprocess.run(self.command(out="flagged"), env=env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertIn("malformed workflow_runs", done.stderr)

    def test_an_even_population_takes_the_mean_of_its_middle_pair(self):
        branch, head = self.change(1, self.main)
        log = b"E AssertionError: x\nFailed tasks:\n - surface-census:test-census\n"
        self.serve_runs(
            branch,
            [self.ci_run(1, 1, head), self.ci_run(2, 2, head), self.ci_run(3, 4, head, "success")],
            {1: log, 2: log},
        )
        totals = json.loads((self.invoke(window="runs:sample") / "totals.json").read_text())
        # Cycles of 60 and 120 minutes: each 10 elapsed plus its wait to the next run.
        self.assertEqual(totals["census"]["median_cycle_min"], 90)

    def test_an_unwritable_destination_stops_and_recovers(self):
        self.change(1, self.main)
        blocked = self.root / "blocked"
        blocked.write_text("a file where the output directory belongs", encoding="utf-8")
        done = subprocess.run(self.command(out="blocked"), env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertNotIn("Traceback", done.stderr)
        blocked.unlink()
        out = self.invoke(out="blocked")
        self.assertTrue((out / "totals.json").exists())

    def test_a_merged_change_reports_its_squash_commit_and_an_empty_sample_says_so(self):
        branch, _ = self.change(1, self.main)
        table = self.repo / "docs/openapi-surface/golden-reach.tsv"
        table.parent.mkdir(parents=True)
        table.write_text("landed\n", encoding="utf-8")
        squash = self.commit("squash")
        self.event("change-merged", branch, {"sha": squash, "url": "https://github.com/nickderobertis/crozier/pull/1"})
        out = self.invoke(window="runs:sample")
        row = self.rows(out, "changes.tsv")[0]
        self.assertEqual((row["merged"], row["rewrote"]), ("True", "docs/openapi-surface/golden-reach.tsv"))

        # The change's base lacks a commit made after it, so nothing qualifies.
        out = self.invoke(window=f"base-carries:{squash}", out="empty")
        self.assertEqual(self.rows(out, "changes.tsv"), [])
        summary = (out / "summary.md").read_text()
        self.assertIn("- Changes: 0 (0 with a PR, 0 merged); CI runs 0, failed 0.", summary)
        self.assertIn("Census-tier CI failures: 0 (0.00 per change, 0 changes hit)", summary)
        self.assertIn("Derived-table conflicts: 0 (0 changes)", summary)
        self.assertIn("1 whose base lacks a required commit", summary)

    def test_a_dropped_connection_and_invalid_json_stop_and_recover(self):
        branch, _ = self.change(1, self.main)
        path = f"/repos/nickderobertis/crozier/actions/runs?branch={branch}&per_page=100&page=1"
        self.dropped.add(path)
        done = subprocess.run(self.command(out="dropped"), env=self.env, capture_output=True, text=True, timeout=60)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertNotIn("Traceback", done.stderr)
        self.assertFalse((self.root / "dropped/totals.json").exists())
        self.dropped.clear()
        self.responses[path] = (200, b"<html>not json</html>")
        done = subprocess.run(self.command(out="garbled"), env=self.env, capture_output=True, text=True, timeout=60)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertIn("invalid JSON", done.stderr)
        self.assertFalse((self.root / "garbled/totals.json").exists())
        self.responses[path] = (200, {"workflow_runs": []})
        self.invoke(out="recovered")

    def test_a_failed_run_with_no_jobs_stops(self):
        branch, head = self.change(1, self.main)
        self.serve_runs(branch, [self.ci_run(7, 1, head)], {})
        self.responses["/repos/nickderobertis/crozier/actions/runs/7/jobs?filter=latest&per_page=100&page=1"] = (
            200,
            {"jobs": []},
        )
        done = subprocess.run(self.command(), env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertIn("no jobs to classify", done.stderr)

    def test_an_unknown_conclusion_and_an_unreadable_base_stop(self):
        branch, head = self.change(1, self.main)
        self.serve_runs(branch, [self.ci_run(7, 1, head, "mystery")], {})
        done = subprocess.run(self.command(out="odd"), env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertIn("conclusion 'mystery'", done.stderr)
        self.assertNotIn("Traceback", done.stderr)
        self.serve_runs(branch, [], {})
        # A head with no history in common with main has no base to judge it by.
        self.git("checkout", "--orphan", "unrelated")
        unrelated = self.commit("unrelated")
        self.git("checkout", "main")
        self.git("update-ref", "refs/pull/2/head", unrelated)
        self.event("change-opened", "elsewhere", {"id": 2})
        self.event("push", "elsewhere", {"accepted": True, "head": unrelated})
        env = {**self.env, "CROZIER_GITHUB_CACHE_DIR": str(self.root / "fresh")}
        done = subprocess.run(self.command(out="orphan"), env=env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertIn("merge-base", done.stderr)

    def test_an_unnamed_census_failure_and_a_redispatch_after_a_conflict(self):
        branch, head = self.change(1, self.main)
        self.serve_runs(
            branch,
            [self.ci_run(1, 1, head)],
            {1: b"E AssertionError: unrelated words\nFailed tasks:\n - surface-census:test-census\n"},
        )
        self.event(
            "sync-conflict", branch, {"paths": ["docs/openapi-surface/golden-reach.tsv"]}, "2026-01-01T02:00:00Z"
        )
        self.event("node-dispatched", branch, {"attempt": 2}, "2026-01-01T02:10:00Z")
        out = self.invoke(window="runs:sample")
        self.assertEqual([e["kind"] for e in self.rows(out, "events.tsv")], ["census-unattributed", "derived-conflict"])
        totals = json.loads((out / "totals.json").read_text())
        self.assertEqual(totals["by_kind"]["census-unattributed"]["events"], 1)
        self.assertEqual(totals["by_kind"]["derived-conflict"]["redispatches"], 1)
        self.assertEqual((totals["conflicts"]["redispatches"], totals["census"]["redispatches"]), (1, 0))

    def test_a_collection_longer_than_the_page_limit_stops(self):
        branch, head = self.change(1, self.main)
        page = [dict(self.ci_run(100, 1, head, "success"), name="other") for _ in range(100)]
        for number in range(1, 21):
            self.responses[f"/repos/nickderobertis/crozier/actions/runs?branch={branch}&per_page=100&page={number}"] = (
                200,
                {"workflow_runs": page},
            )
        done = subprocess.run(self.command(), env=self.env, capture_output=True, text=True, timeout=60)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertIn("more than 20 pages", done.stderr)

    def test_malformed_github_collection_stops(self):
        branch, head = self.change(1, self.main)
        path = f"/repos/nickderobertis/crozier/actions/runs?branch={branch}&per_page=100&page=1"
        wrong_id = dict(self.ci_run(1, 1, head), id="one")
        for i, payload in enumerate(
            ({}, {"workflow_runs": 3}, {"workflow_runs": [{"id": 1}]}, {"workflow_runs": [wrong_id]})
        ):
            self.responses[path] = (200, payload)
            env = {**self.env, "CROZIER_GITHUB_CACHE_DIR": str(self.root / f"cache-{i}")}
            done = subprocess.run(self.command(out=f"bad-{i}"), env=env, capture_output=True, text=True, timeout=20)
            self.assertEqual(done.returncode, 1, done.stderr)
            self.assertIn("malformed workflow_runs", done.stderr)
            self.assertFalse((self.root / f"bad-{i}/totals.json").exists())

    def test_unread_heads_and_main_are_named(self):
        branch, _ = self.change(1, self.main)
        self.git("update-ref", "-d", "refs/pull/1/head")
        self.journal = [e for e in self.journal if e["kind"] != "push"]
        out = self.invoke()
        self.assertIn("refs/pull/1/head not fetchable", self.rows(out, "excluded.tsv")[0]["reason"])
        self.assertIn("1 with an unfetchable head", (out / "summary.md").read_text())
        # A pushed head git no longer holds falls back to the pull request's head.
        self.git("update-ref", "refs/pull/1/head", self.git("rev-parse", "main").strip())
        self.event("push", branch, {"accepted": True, "head": "f" * 40})
        out = self.invoke(out="fallback")
        self.assertEqual([r["pr"] for r in self.rows(out, "changes.tsv")], ["1"])
        self.git("remote", "remove", "origin")
        done = subprocess.run(self.command(out="no-main"), env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertIn("a base cannot be read without main", done.stderr)

    def test_an_accepted_push_with_no_head_falls_back_to_the_pull_requests_head(self):
        branch, head = self.change(1, self.main)
        self.journal = [e for e in self.journal if e["kind"] != "push"]
        self.event("push", branch, {"accepted": True})
        self.assertEqual([r["pr"] for r in self.rows(self.invoke(), "changes.tsv")], ["1"])
        # The fallback decides the base: the same journal with a pull request head lacking the second commit is out.
        self.git("update-ref", "refs/pull/1/head", self.first)
        excluded = self.rows(self.invoke(out="older-head"), "excluded.tsv")
        self.assertEqual([(r["pr"], r["head"]) for r in excluded], [("1", self.first[:12])])
        self.assertNotEqual(head[:12], excluded[0]["head"])

    def test_a_job_completed_before_it_started_keeps_its_negative_minutes(self):
        branch, head = self.change(1, self.main)
        run = self.ci_run(1, 1, head)
        log = b"E AssertionError: unrelated words\nFailed tasks:\n - surface-census:test-census\n"
        self.serve_runs(branch, [run], {1: log})
        reversed_job = {
            "id": 1,
            "name": "check",
            "conclusion": "failure",
            "started_at": "2026-01-01T01:10:00Z",
            "completed_at": "2026-01-01T01:00:00Z",
        }
        forward_job = {
            "id": 2,
            "name": "other",
            "conclusion": "success",
            "started_at": "2026-01-01T01:00:00Z",
            "completed_at": "2026-01-01T01:30:00Z",
        }
        self.responses["/repos/nickderobertis/crozier/actions/runs/1/jobs?filter=latest&per_page=100&page=1"] = (
            200,
            {"jobs": [reversed_job, forward_job]},
        )
        out = self.invoke(window="runs:sample")
        self.assertEqual(self.rows(out, "events.tsv")[0]["runner_min"], "20.0")
        self.assertEqual(json.loads((out / "totals.json").read_text())["census"]["runner_min"], 20.0)

    def test_a_wrong_command_line_exits_2_and_writes_nothing(self):
        self.change(1, self.main)
        cases = [
            (["--window", "base-carries:" + self.first[:12]], "full commit shas"),
            (["--window", "base-carries:" + "f" * 40], "full commit shas"),
            (["--window", "base-carries:main"], "full commit shas"),
            (["--window", "runs:../escape"], "not a directory name"),
            (["--window", "commits:" + self.first], "--window must be"),
            (["--window", "runs:sample,"], "--window must be"),
            (["--window", "runs:,sample"], "--window must be"),
            (["--window", "runs:"], "--window must be"),
            (["--window", f"base-carries:{self.first},"], "--window must be"),
            (["--window", "runs:sample,sample"], "names something twice"),
            (["--window", f"base-carries:{self.first},{self.first}"], "names something twice"),
            (["--until", "2026-01-02T00:00:00"], "UTC offset"),
            (["--until", "not-a-time"], "--until"),
            (["--runs-root", str(self.root / "absent")], "not a directory"),
        ]
        for extra, expected in cases:
            with self.subTest(extra=extra):
                done = subprocess.run(
                    [*self.command(out="wrong"), *extra], env=self.env, capture_output=True, text=True, timeout=20
                )
                self.assertEqual(done.returncode, 2, done.stderr)
                self.assertIn(expected, done.stderr)
                self.assertFalse((self.root / "wrong").exists())

    def test_journal_and_results_failures_stop_and_a_torn_line_does_not(self):
        self.change(1, self.main)
        path = self.run_dir / "events.jsonl"
        good = self.command()
        lines = path.read_text(encoding="utf-8")
        path.write_text(lines + '{"ts": "2026-01-01T0', encoding="utf-8")
        done = subprocess.run(good, env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 0, done.stderr)
        for bad, expected in (
            ("[1]\n", "not an object"),
            ('{"kind": "push", "labels": {}, "payload": {}}\n', "no usable time"),
            ('{"ts": 3, "kind": "push", "labels": {}, "payload": {}}\n', "no usable time"),
            (
                json.dumps(
                    {
                        "ts": "2026-01-01T02:00:00Z",
                        "kind": "push",
                        "labels": {"session": "change-1", "identity": "github.com/nickderobertis/crozier"},
                        "payload": {"branch": "change-1", "accepted": True, "head": int("1" * 40)},
                    }
                )
                + "\n",
                "head",
            ),
            (
                json.dumps(
                    {
                        "ts": "2026-01-01T02:00:00Z",
                        "kind": "change-merged",
                        "labels": {"session": "change-1", "identity": "github.com/nickderobertis/crozier"},
                        "payload": {"branch": "change-1", "sha": int("1" * 40)},
                    }
                )
                + "\n",
                "a merge's sha",
            ),
            ('{"ts": "2026-01-01T02:00:00Z", "kind": 3, "labels": {}, "payload": {}}\n', "string kind"),
            (
                '{"ts": "2026-01-01T02:00:00Z", "kind": "push", "labels": {"node": 3}, "payload": {}}\n',
                "string identities",
            ),
        ):
            path.write_text(lines + bad, encoding="utf-8")
            done = subprocess.run(good, env=self.env, capture_output=True, text=True, timeout=20)
            self.assertEqual(done.returncode, 1, done.stderr)
            self.assertIn(expected, done.stderr)
        opened = {
            "ts": "2026-01-01T02:00:00Z",
            "kind": "change-opened",
            "labels": {"node": "node"},
            "payload": {"branch": "x"},
        }
        path.write_text(lines + json.dumps(opened) + "\n", encoding="utf-8")
        done = subprocess.run(good, env=self.env, capture_output=True, text=True, timeout=20)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertIn("change-opened event", done.stderr)
        self.assertNotIn("Traceback", done.stderr)
        for kind, payload in (
            ("gate-run", {"started_at": "2026-01-01T02:00:00Z"}),
            (
                "gate-run",
                {
                    "started_at": "2026-01-01T03:00:00Z",
                    "ended_at": "2026-01-01T02:00:00Z",
                    "verdict": "failed",
                    "checks": [],
                },
            ),
            ("change-opened", {"id": True}),
            ("change-merged", {"sha": "not-a-sha"}),
            ("change-merged", {"sha": "a" * 40, "url": "https://github.com/o/r/pull/0"}),
            ("push", {"accepted": True, "head": "not-a-sha"}),
            ("push", {"accepted": "true", "head": "a" * 40}),
            ("sync-conflict", {"paths": [3]}),
            (
                "gate-run",
                {
                    "started_at": "2026-01-01T02:00:00Z",
                    "ended_at": "2026-01-01T02:10:00Z",
                    "verdict": "failed",
                    "checks": [{"name": "gate", "conclusion": "odd"}],
                },
            ),
            (
                "gate-run",
                {
                    "started_at": "2026-01-01T02:00:00Z",
                    "ended_at": "2026-01-01T02:10:00Z",
                    "verdict": "odd",
                    "checks": [],
                },
            ),
            ("change-opened", {"id": -3}),
            ("node-dispatched", {"attempt": 1.5}),
        ):
            bad = dict(opened, kind=kind, payload={"branch": "x", **payload})
            path.write_text(lines + json.dumps(bad) + "\n", encoding="utf-8")
            done = subprocess.run(good, env=self.env, capture_output=True, text=True, timeout=20)
            self.assertEqual(done.returncode, 1, done.stderr)
            self.assertIn(f"{kind} event", done.stderr)
        path.write_text(lines, encoding="utf-8")
        for provider, expected in (
            ("import sys\nsys.exit(3)\n", "exited 3"),
            ("print('not json')\n", "invalid JSON"),
            ("print('{\"nodes\": [{}]}')\n", "string ids"),
        ):
            self.results.write_text(provider, encoding="utf-8")
            done = subprocess.run(good, env=self.env, capture_output=True, text=True, timeout=20)
            self.assertEqual(done.returncode, 1, done.stderr)
            self.assertIn(expected, done.stderr)

    def test_guard_refusal_and_wait_send_no_api_request(self):
        self.change(1, self.main)
        self.quota = "refuse"
        done = subprocess.run(self.command(), env=self.env, capture_output=True, text=True, timeout=20)
        self.assertNotEqual(done.returncode, 0)
        self.assertEqual(self.requests, ["/rate_limit"])
        self.requests.clear()
        self.quota = "wait"
        process = subprocess.Popen(
            self.command(out="waiting"), env=self.env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        try:
            deadline = time.monotonic() + 10
            while not self.requests and time.monotonic() < deadline:
                time.sleep(0.02)
            self.assertEqual(self.requests, ["/rate_limit"])
            self.assertIsNone(process.poll())
            # The guard logs its refusal probe before sleeping; the wait row follows sleep.
            evidence = self.root / "waiting/github-evidence/rate-limit-waits.jsonl"
            deadline = time.monotonic() + 5
            while not evidence.exists() and time.monotonic() < deadline:
                time.sleep(0.02)
            probes = [json.loads(line) for line in evidence.read_text().splitlines()]
            self.assertTrue(any(p["kind"] == "probe" and p["admitted"] is False for p in probes))
            time.sleep(0.25)
            self.assertIsNone(process.poll())
            self.assertEqual(self.requests, ["/rate_limit"])
        finally:
            process.terminate()
            process.communicate(timeout=10)

    # Every file a measurement writes may be committed, so a host's names must not reach one.
    BRANCH = f"nick/Generate-{STAND_IN}-s-Python-SDKs"
    NODE = f"{STAND_IN.lower()}-parity-gaps"
    RUN = f"Generate-{STAND_IN}-s-Python-SDKs"

    def run_records(self, run=RUN):
        """A run, as a host records it, whose run, branch and node names all hold the stand-in."""
        shutil.rmtree(self.run_dir)
        self.run_dir = self.runs / run
        self.run_dir.mkdir()
        (self.run_dir / "plan.json").write_text('"nickderobertis/crozier"', encoding="utf-8")
        self.results.write_text(
            "import json\nprint(json.dumps("
            + repr({"nodes": [{"id": self.NODE, "status": "done", "outcome": "merged"}]})
            + "))\n",
            encoding="utf-8",
        )
        _, kept = self.change(1, self.main)
        self.change(2, self.initial)
        for event in self.journal:
            pr = "1" if event["payload"]["branch"] == "change-1" else "2"
            event["labels"].update(node=f"{self.NODE}-{pr}", session=f"{self.BRANCH}-{pr}")
            event["payload"]["branch"] = f"{self.BRANCH}-{pr}"
        self.journal.append(
            {
                "ts": "2026-01-01T01:00:00Z",
                "kind": "node-dispatched",
                "labels": {"node": self.NODE, "session": self.BRANCH, "identity": "github.com/nickderobertis/crozier"},
                "payload": {"branch": self.BRANCH, "attempt": 1},
            }
        )
        return kept

    def assert_stand_in_absent(self, *roots):
        written = [path for root in roots for path in sorted(root.rglob("*")) if path.is_file()]
        self.assertTrue(written, "nothing was written, so nothing was checked")
        for path in written:
            self.assertNotIn(STAND_IN.lower(), path.relative_to(self.root).as_posix().lower())
            self.assertNotIn(STAND_IN.lower().encode(), path.read_bytes().lower(), f"{path} carries the stand-in")

    def test_no_file_written_carries_a_host_identifier(self):
        kept = self.run_records()
        log = b"E AssertionError: golden-reach.tsv is stale\nFailed tasks:\n - surface-census:test-census\n"
        self.serve_runs(f"{self.BRANCH}-1", [self.ci_run(1, 2, kept)], {1: log})
        carries = f"base-carries:{self.first},{self.second}"
        for window, out in ((carries, "carries"), (f"runs:{self.RUN}", "named")):
            done = subprocess.run(
                self.command(window=window, out=out), env=self.env, capture_output=True, text=True, timeout=20
            )
            self.assertEqual(done.returncode, 0, done.stderr)
            self.assertNotIn(STAND_IN.lower(), done.stdout.lower())
        carried, named = self.root / "carries", self.root / "named"
        # `compare` writes into the measurement it reads, so it is scanned with the rest.
        baseline = self.root / "fixture-baseline"
        shutil.copytree(SOURCE / "tests/fixtures/baseline", baseline)
        done = subprocess.run(
            [PYTHON, str(self.cli), "compare", str(baseline), str(named)], capture_output=True, text=True, timeout=20
        )
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assert_stand_in_absent(carried, named, self.root / "cache")

        # Absence alone would pass on empty files: the figures and the rows they belong to are still there.
        change = self.rows(carried, "changes.tsv")[0]
        self.assertEqual(
            (change["pr"], change["branch"], change["census_failures"], change["ci_runs"]),
            ("1", digest(f"{self.BRANCH}-1"), "1", "1"),
        )
        self.assertEqual(
            change["nodes"], f"{digest(self.NODE + '-1')}=unavailable (node retired; not in current results)"
        )
        self.assertEqual(change["runs"], digest(self.RUN))
        self.assertEqual(self.rows(carried, "events.tsv")[0]["branch"], digest(f"{self.BRANCH}-1"))
        excluded = {row["pr"]: row for row in self.rows(carried, "excluded.tsv")}
        self.assertEqual(set(excluded), {"", "2"})
        self.assertEqual(excluded[""]["branch"], digest(self.BRANCH))
        self.assertEqual(excluded[""]["nodes"], f"{digest(self.NODE)}=merged")
        totals = json.loads((named / "totals.json").read_text())
        self.assertEqual(totals["window"]["spec"], f"runs:{digest(self.RUN)}")
        self.assertEqual(totals["window"]["runs"], [digest(self.RUN)])
        self.assertEqual(totals["census"]["failures"], 1)
        self.assertIn(f"`runs:{digest(self.RUN)}`", (named / "summary.md").read_text())
        ledger = (carried / "github-evidence/repin-cost-requests.jsonl").read_text()
        self.assertIn(f"branch={digest(self.BRANCH + '-1')}", ledger)

    def test_a_ci_log_line_naming_a_host_identifier_is_published_redacted(self):
        kept = self.run_records()
        # Long enough that the 200-character cut falls inside the name, keeping only its first half if cut first.
        prefix = "E AssertionError: golden-reach.tsv is stale at " + "x" * 135 + " "
        name = f"{self.BRANCH}-1"
        self.assertLess(len(prefix) + name.index(STAND_IN), 200)
        self.assertGreater(len(prefix) + len(name), 200)
        for line, out in (
            (f"{prefix}{name}", "whole-branch"),
            (f"E AssertionError: golden-reach.tsv is stale under /runs/{self.RUN}/{self.NODE}-1/x", "run-and-node"),
        ):
            log = f"{line}\nFailed tasks:\n - surface-census:test-census\n".encode()
            self.env["CROZIER_GITHUB_CACHE_DIR"] = str(self.root / f"cache-{out}")
            self.serve_runs(name, [self.ci_run(1, 2, kept)], {1: log})
            result = self.invoke(window=f"runs:{self.RUN}", out=out)
            # Only the measurement's own directory: the host's response cache keeps GitHub's answer as it came.
            self.assert_stand_in_absent(result)
            excerpt = self.rows(result, "events.tsv")[0]["excerpt"]
            self.assertTrue(excerpt.startswith("E AssertionError: golden-reach.tsv is stale"), excerpt)
            self.assertLessEqual(len(excerpt), 200)
            self.assertIn(digest(name)[:6] if out == "whole-branch" else digest(self.RUN), excerpt)

    def test_a_run_named_by_digest_is_still_the_live_run_baseline(self):
        kept = self.run_records(run=LIVE_RUN)
        log = b"E AssertionError: golden-reach.tsv is stale\nFailed tasks:\n - surface-census:test-census\n"
        self.serve_runs(f"{self.BRANCH}-1", [self.ci_run(1, 2, kept)], {1: log})
        measured = self.invoke(window=f"runs:{LIVE_RUN}")
        after = self.root / "fixture-after"
        shutil.copytree(SOURCE / "tests/fixtures/after", after)
        done = subprocess.run(
            [PYTHON, str(self.cli), "compare", str(measured), str(after)], capture_output=True, text=True, timeout=20
        )
        self.assertEqual(done.returncode, 0, done.stderr)
        # One census failure over the run's two changes; a run not recognised by its digest reads n/a.
        self.assertIn("| live run baseline | 0.50 |", (after / "comparison.md").read_text())


class ComparisonTest(unittest.TestCase):
    def test_compare_every_figure(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get("ONEPIPELINE_NODE_SCRATCH_DIR")) as scratch:
            root = Path(scratch)
            for name in ("baseline", "after"):
                shutil.copytree(SOURCE / "tests/fixtures" / name, root / name)
            result = subprocess.run(
                [PYTHON, str(SOURCE / "repin_cost.py"), "compare", str(root / "baseline"), str(root / "after")],
                capture_output=True,
                text=True,
                timeout=20,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            text = (root / "after/comparison.md").read_text()
            before = json.loads((root / "baseline/totals.json").read_text())
            expected = {}

            def flatten(data, prefix=""):
                for key, value in data.items():
                    label = f"{prefix}.{key}" if prefix else key
                    match value:
                        case dict():
                            flatten(value, label)
                        case int() | float():
                            expected[label] = value

            flatten(
                {
                    k: v
                    for k, v in before.items()
                    if k not in {"window", "github", "by_kind", "artifacts_outside_census"}
                }
            )
            flatten(before["by_kind"], "kind")
            for artifact in before["artifacts_outside_census"]:
                flatten({k: v for k, v in artifact.items() if k != "artifact"}, "artifact." + artifact["artifact"])
            expected["census.cycle_min"] = 60
            expected["census_and_conflict_redispatches"] = 3
            for label, value in expected.items():
                after = 8 if label == "changes" else value * 3
                row = f"| `{label}` | {value:.2f} | {value / 4:.2f} | {after:.2f} | {after / 8:.2f} | {after - value:+.2f} | {after / 8 - value / 4:+.2f} |"
                self.assertIn(row, text, label)
            self.assertIn("| pooled baseline | 0.50 | 0.75 | +0.25 |", text)
            self.assertIn("| live run baseline | 2.00 | 0.75 | -1.25 |", text)
            self.assertIn("#8", text)
            missing = subprocess.run(
                [PYTHON, str(SOURCE / "repin_cost.py"), "compare", str(root / "missing"), str(root / "after")],
                capture_output=True,
                text=True,
                timeout=20,
            )
            self.assertNotEqual(missing.returncode, 0)
            self.assertIn("totals.json", missing.stderr)
            # An empty after sample must not assert a zero rate or an improvement.
            after_path = root / "after/totals.json"
            current = json.loads(after_path.read_text())
            current.update(changes=0, changes_with_pr=0, merged=0)
            current["census"].update(failures=0, changes_hit=0)
            current["conflicts"].update(derived=0, changes_hit=0)
            after_path.write_text(json.dumps(current))
            (root / "after/changes.tsv").write_text("pr\n")
            result = subprocess.run(
                [PYTHON, str(SOURCE / "repin_cost.py"), "compare", str(root / "baseline"), str(root / "after")],
                capture_output=True,
                text=True,
                timeout=20,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            text = (root / "after/comparison.md").read_text()
            self.assertIn("Provisional comparison: 0 after-sample changes", text)
            self.assertIn("| live run baseline | 2.00 | n/a | n/a |", text)

    def test_compare_refuses_incomplete_evidence_and_shows_one_sided_kinds(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get("ONEPIPELINE_NODE_SCRATCH_DIR")) as scratch:
            root = Path(scratch)
            for name in ("baseline", "after"):
                shutil.copytree(SOURCE / "tests/fixtures" / name, root / name)
            path = root / "after/totals.json"
            good = json.loads(path.read_text())
            tsv = root / "after/changes.tsv"
            rows = tsv.read_text()

            def compare():
                return subprocess.run(
                    [PYTHON, str(SOURCE / "repin_cost.py"), "compare", str(root / "baseline"), str(root / "after")],
                    capture_output=True,
                    text=True,
                    timeout=20,
                )

            def mutated(change):
                data = json.loads(json.dumps(good))
                change(data)
                return data

            cases = {
                "census.wait_min": lambda d: d["census"].pop("wait_min"),
                "must be a finite": lambda d: d["census"].update(failures=True),
                "conflicts must hold": lambda d: d["conflicts"].pop("mixed"),
                "cannot exceed": lambda d: d.update(merged=d["changes"] + 1),
                "every count": lambda d: d["census"].update(attempts=1.5),
                "contradict": lambda d: d.update(ci_failed=d["ci_runs"] + 1),
                "census.extra": lambda d: d["census"].update(extra=-1),
                "totals.extra": lambda d: d.update(extra=float("inf")),
                "counts must be integers": lambda d: next(iter(d["by_kind"].values())).update(events=0.5),
                "listed twice": lambda d: d["artifacts_outside_census"].extend(
                    [d["artifacts_outside_census"][0], d["artifacts_outside_census"][0]]
                ),
                "empty sample": lambda d: (
                    d.update(changes=0, changes_with_pr=0, merged=0)
                    or d["census"].update(changes_hit=0)
                    or d["conflicts"].update(changes_hit=0)
                ),
                "kind 'x' must hold": lambda d: d["by_kind"].update(x={"events": 1}),
                "malformed artifact": lambda d: d["artifacts_outside_census"].append({}),
                "malformed artifact record": lambda d: d["artifacts_outside_census"].append({"artifact": ["a"]}),
                "window metadata": lambda d: d["window"].update(spec=""),
                "metadata": lambda d: d["window"].update(until="not-a-time"),
                "malformed window": lambda d: d["window"].update(base_carries=["short"]),
            }
            for expected, change in cases.items():
                with self.subTest(expected=expected):
                    path.write_text(json.dumps(mutated(change)))
                    done = compare()
                    self.assertEqual(done.returncode, 1, done.stderr)
                    self.assertIn("wait_min" if expected == "census.wait_min" else expected, done.stderr)
            for window in (
                {"spec": "base-carries:"},
                {"spec": "base-carries:" + "b" * 40},
                {"spec": "runs:earlier", "base_carries": ["a" * 40]},
            ):
                with self.subTest(window=window):
                    path.write_text(json.dumps(mutated(lambda d, update=window: d["window"].update(update))))
                    done = compare()
                    self.assertEqual(done.returncode, 1, done.stderr)
                    self.assertIn("malformed window metadata", done.stderr)
            path.write_text(json.dumps(good))
            tsv.write_text("pr\tcensus_failures\truns\nnot-a-number\t0\tr\n")
            done = compare()
            self.assertEqual(done.returncode, 1)
            self.assertIn("a positive pr", done.stderr)
            tsv.write_text(rows.replace("\n1\t1\t", "\n1\t2\t"))
            self.assertIn("disagree with totals.json", compare().stderr)
            tsv.write_text(rows)
            tsv.write_text(rows)
            target = root / "after/comparison.md"
            target.unlink(missing_ok=True)
            target.mkdir()
            done = compare()
            self.assertEqual(done.returncode, 1, done.stderr)
            self.assertIn("provide complete measurement output directories", done.stderr)
            target.rmdir()
            self.assertEqual(compare().returncode, 0)
            self.assertTrue(target.is_file())
            tsv.write_text(rows.replace("\n2\t1\t", "\n1\t1\t"))
            self.assertIn("appears twice", compare().stderr)
            tsv.write_text(rows)

            only_after = dict(next(iter(good["by_kind"].values())), events=2)
            path.write_text(json.dumps(mutated(lambda d: d["by_kind"].update(fresh=only_after))))
            self.assertEqual(compare().returncode, 0)
            text = (root / "after/comparison.md").read_text()
            self.assertIn("| `kind.fresh.events` | 0.00 | 0.00 | 2.00 | 0.25 | +2.00 | +0.25 |", text)

            before = root / "baseline/totals.json"
            data = json.loads(before.read_text())
            data.update(changes=0, changes_with_pr=0, merged=0)
            data["census"].update(failures=0, changes_hit=0)
            data["conflicts"].update(derived=0, changes_hit=0)
            before.write_text(json.dumps(data))
            base_rows = (root / "baseline/changes.tsv").read_text()
            self.assertIn("disagree with totals.json", compare().stderr)
            (root / "baseline/changes.tsv").write_text(base_rows.splitlines()[0] + "\n")
            path.write_text(json.dumps(good))
            self.assertEqual(compare().returncode, 0)
            text = (root / "after/comparison.md").read_text()
            self.assertIn("| `changes` | 0.00 | n/a | 8.00 | 1.00 | +8.00 | n/a |", text)
            self.assertIn("| pooled baseline | n/a | 0.75 | n/a |", text)
            self.assertIn("| live run baseline | n/a | 0.75 | n/a |", text)


if __name__ == "__main__":
    unittest.main()
