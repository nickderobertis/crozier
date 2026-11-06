"""Drive the public CLI through real journals, git and guarded HTTP."""

from __future__ import annotations

import csv
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


class HarnessTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=os.environ.get("ONEPIPELINE_NODE_SCRATCH_DIR"))
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        tool = self.repo / "tools/repin-cost"
        tool.mkdir(parents=True)
        for name in ("repin_cost.py", "gh.py", "comparison.py"):
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
        self.quota = "ok"
        owner = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, format, *args):
                pass

            def do_GET(self):
                owner.requests.append(self.path)
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
        self.assertEqual(self.rows(out, "changes.tsv")[0]["nodes"], "node=merged")
        excluded = {r["pr"]: r["reason"] for r in self.rows(out, "excluded.tsv")}
        self.assertEqual(set(excluded), {"2", "3", "4", "5", "6"})
        self.assertIn(self.second[:12], excluded["2"])
        self.assertIn(self.first[:12], excluded["3"])
        self.assertIn("own commits carry", excluded["5"])
        self.assertIn("base", excluded["6"])
        retired = next(r for r in self.rows(out, "excluded.tsv") if r["pr"] == "4")
        self.assertIn("retired=unavailable (node retired; not in current results)", retired["nodes"])
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
                    if isinstance(value, dict):
                        flatten(value, label)
                    elif isinstance(value, (int, float)):
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
            self.assertIn("| pooled baseline | 0.58 | 0.75 | +0.17 |", text)
            self.assertIn("| live run baseline | 1.86 | 0.75 | -1.11 |", text)
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
            current["changes"] = 0
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
            self.assertIn("| live run baseline | 1.86 | n/a | n/a |", text)


if __name__ == "__main__":
    unittest.main()
