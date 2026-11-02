#!/usr/bin/env python3
"""Measure what repinning cost crozier changes in a window.

    python3 spike/repin-cost/repin_cost.py --window runs:<run>[,<run>...] [--until <ISO>] --out <dir>
    python3 spike/repin-cost/repin_cost.py --window base-carries:<sha>[,<sha>...] [--until <ISO>] --out <dir>

`runs:` takes the crozier changes the named runs produced; `base-carries:` scans every
run under the runs root that worked crozier and keeps the changes whose final head has
every named commit as an ancestor. Three sources are joined per change (pull request,
branch, run nodes):

1. this host's run journals under $ONEPIPELINE_RUNS_DIR (node outcomes through
   `onepipeline results --json`; publication attempts, re-dispatches and sync
   conflicts off each run's events.jsonl, which no view reports);
2. crozier's GitHub CI, read only through tools/witness-search/rate_limit_guard.py
   and its shared response cache (see gh.py) -- a second run over the same window
   makes no uncached request;
3. git: the PRs' head commits (refs/pull/<n>/head, fetched read-only) and squash
   commits, for which pinned or derived files each change and each fix rewrote.

Writes <out>/changes.tsv, <out>/events.tsv, <out>/totals.json and <out>/summary.md;
prints one line. Runs no measurement, no golden test, no generation; never writes to
GitHub.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

import gh  # noqa: E402

IDENTITY = "github.com/nickderobertis/crozier"
ORCH = Path(os.environ.get("ONEPIPELINE_ORCHESTRATOR_ROOT", "/home/whoop/ai-orchestrator"))
CENSUS_TASKS = ("surface-census:test-census", "surface-census:test-reach", "surface-census:test-reach-portable")
KINDS = ("site-anchor", "port-digest", "measured-count", "derived-conflict")

# ---------------------------------------------------------------- classification


def artifact_kind(path: str) -> tuple[str, str] | None:
    """(kind, artifact) for a pinned or derived file; None for authored code or prose."""
    if path == "docs/openapi-surface/golden-reach-sites.tsv":
        return "site-anchor", path
    if path == "tools/surface-census/openapi-surface-census.py":
        return "port-digest", path
    if path == "docs/openapi-surface/scenario-proof-index.tsv":
        return "other-artifact:" + path, path
    if path in (
        "docs/openapi-surface/golden-reach.tsv",
        "docs/openapi-surface/handwritten-reach.tsv",
        "docs/openapi-surface/evidence.toml",
        "docs/openapi-surface-coverage.md",
    ) or (path.startswith("docs/openapi-surface/") and path.count("/") == 2 and path.endswith((".md", ".tsv"))):
        return "measured-count", path
    if path.startswith("docs/openapi-surface/handwritten/"):
        # A hand-written fixture's measured evidence is a reach measurement; its sources and expected trees are authored.
        return ("measured-count", path) if path.endswith("/evidence.toml") else None
    if path.startswith("docs/openapi-surface/") and path.endswith((".tsv", ".json", ".toml")):
        return "other-artifact:" + path, path
    for prefix in ("shots/baseline/", "docs/screenshots/"):
        if path.startswith(prefix):
            return "other-artifact:" + prefix, prefix
    if path in (
        "tests/fixtures/departures-ledger.tsv",
        "tests/fixtures/compared-goldens.json",
        "tests/fixtures/corpus-sources.tsv",
        "tests/fixtures/corpus-remote-ref-pins.tsv",
        "tests/fixtures/CORPUS.md",
        "assets/crozier.schema.json",
        "llmlint-plugins/lock.json",
        "docs/fern-measurements/cases.tsv",
    ) or re.fullmatch(r"docs/fern-(measurements|refusals)/[^/]+\.(tsv|json)", path):
        return "other-artifact:" + path, path
    return None


SITE_RE = re.compile(
    r"site .* matches \d+ (functions|lines)|anchor it|spans no production counter region|cannot bound|"
    r"golden-reach-sites\.tsv (lists no|does not)|names no registered source|correct its selectors"
)
DIGEST_RE = re.compile(r"re-pin the digest|changed; re-derive|re-derive .* from src/|digest .* (moved|changed)|port digest")
COUNT_RE = re.compile(
    r"golden-reach\.tsv|handwritten-reach\.tsv|evidence\.toml|just golden-reach|just handwritten-reach|"
    r"golden-reach-report|reach cell|is stale|out of date|re-?measure|restate-coverage|generated section"
)
# A check outside the census failing because committed data went stale (a repin), as against a content or code defect.
STALE_RE = re.compile(
    r"is stale|not measured|re-?pin|rerun without --check|regenerate|UPDATE_\w+=1|has drifted|drift|re-?bless|"
    r"out of date|run `just [\w-]+(?:-measure|-report|-bless|-update|-refresh)`"
)
DATA_PATH_RE = re.compile(r"(?:^|[\s/\\:])((?:docs|tests/fixtures|assets|shots)[/\\][\w./\\-]+\.(?:tsv|json|toml|md|yml))")
ARTIFACT_RE = re.compile(
    r"(tests/fixtures/departures-ledger\.tsv|departures-ledger|scenario-proof-index\.tsv|crozier\.schema\.json|"
    r"shots/baseline|docs/screenshots|compared-goldens\.json|corpus-sources\.tsv|llmlint-plugins/lock\.json|"
    r"fern-measurements/cases\.tsv)"
)
ARTIFACT_PATH = {
    "departures-ledger": "tests/fixtures/departures-ledger.tsv",
    "tests/fixtures/departures-ledger.tsv": "tests/fixtures/departures-ledger.tsv",
    "scenario-proof-index.tsv": "docs/openapi-surface/scenario-proof-index.tsv",
    "crozier.schema.json": "assets/crozier.schema.json",
    "shots/baseline": "shots/baseline/",
    "docs/screenshots": "docs/screenshots/",
    "compared-goldens.json": "tests/fixtures/compared-goldens.json",
    "corpus-sources.tsv": "tests/fixtures/corpus-sources.tsv",
    "llmlint-plugins/lock.json": "llmlint-plugins/lock.json",
    "fern-measurements/cases.tsv": "docs/fern-measurements/cases.tsv",
}


def clean_log(raw: bytes) -> str:
    text = raw.decode("utf-8", "replace")
    text = re.sub(r"^\S+Z ", "", text, flags=re.M)
    return re.sub(r"\x1b\[[0-9;]*m|\[[0-9;]*m", "", text)


def failed_tasks(log: str) -> list[str]:
    out: list[str] = []
    for block in re.finditer(r"Failed tasks:\s*\n((?:\s*\n|\s*- \S+\n)+)", log):
        out += re.findall(r"- (\S+)", block.group(1))
    return out


def error_text(log: str) -> str:
    """The lines a failure explains itself in: pytest E/FAILED lines, panics, assertion and error lines."""
    keep = []
    lines = log.splitlines()
    for i, line in enumerate(lines):
        if re.match(r"\s*(E |FAILED |---- .* ----|thread '.*' panicked|AssertionError|assertion|Error:|error:|failures?:)", line):
            keep.extend(lines[i : i + 4])
    return "\n".join(keep)


def classify_failure(log: str) -> dict:
    tasks = failed_tasks(log)
    errors = error_text(log)
    census = any(t in CENSUS_TASKS for t in tasks) or bool(re.search(r"FAILED tools/surface-census/tests/surface_census_test\.py", log))
    kinds: list[str] = []
    if census:
        if SITE_RE.search(errors):
            kinds.append("site-anchor")
        if DIGEST_RE.search(errors):
            kinds.append("port-digest")
        if COUNT_RE.search(errors):
            kinds.append("measured-count")
    stale = not census and bool(STALE_RE.search(errors))
    artifacts: set[str] = set()
    if stale:
        artifacts = {ARTIFACT_PATH[m] for m in ARTIFACT_RE.findall(errors)}
        for raw in DATA_PATH_RE.findall(errors):
            found = artifact_kind(raw.replace("\\", "/"))
            if found:
                artifacts.add(found[1])
    first = next((line.strip() for line in errors.splitlines() if line.strip().startswith(("E ", "E\t")) and len(line.strip()) > 3), "")
    return {"tasks": tasks, "census": census, "stale": stale, "kinds": kinds, "artifacts": sorted(artifacts), "excerpt": first[:200]}


# ---------------------------------------------------------------- helpers


def ts(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def minutes(a: dt.datetime | None, b: dt.datetime | None) -> float:
    return round((b - a).total_seconds() / 60, 1) if a and b else 0.0


def git(*args: str, check: bool = True) -> str:
    done = subprocess.run(["git", "-C", str(REPO_ROOT), *args], capture_output=True, text=True, check=False)
    if check and done.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {done.stderr.strip()}")
    return done.stdout


def onepipeline_results(run: str) -> dict:
    binary = ORCH / "node_modules" / ".bin" / "onepipeline"
    done = subprocess.run([str(binary), "results", run, "--json"], capture_output=True, text=True, check=False, cwd=ORCH)
    try:
        return json.loads(done.stdout)
    except json.JSONDecodeError:
        return {"nodes": []}


# ---------------------------------------------------------------- journals


def crozier_runs(root: Path) -> list[str]:
    out = []
    for plan in sorted(root.glob("*/plan.json")):
        try:
            if "nickderobertis/crozier" in plan.read_text(encoding="utf-8", errors="replace"):
                out.append(plan.parent.name)
        except OSError:
            continue
    return out


def read_journal(root: Path, run: str, until: dt.datetime) -> dict:
    """Per branch: nodes, PR, gate attempts, dispatches, conflicts, settles."""
    branches: dict[str, dict] = collections.defaultdict(
        lambda: {"nodes": set(), "runs": set(), "pr": None, "merged": None, "gates": {}, "dispatches": [], "conflicts": {}, "settles": []}
    )
    session_branch: dict[str, str] = {}
    node_branch: dict[str, str] = {}
    pending: list[dict] = []
    path = root / run / "events.jsonl"
    with path.open(encoding="utf-8", errors="replace") as handle:
        for line in handle:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            when = ts(event.get("ts"))
            if when is None or when > until:
                continue
            labels, payload = event.get("labels", {}), event.get("payload") or {}
            if labels.get("identity") not in (None, IDENTITY):
                continue
            branch = payload.get("branch") if isinstance(payload, dict) else None
            if branch and labels.get("session"):
                session_branch[labels["session"]] = branch
            if branch and labels.get("node"):
                node_branch.setdefault(labels["node"], branch)
            pending.append(event)
    for event in pending:
        kind, labels, payload = event["kind"], event.get("labels", {}), event.get("payload") or {}
        node = labels.get("node")
        branch = payload.get("branch") or session_branch.get(labels.get("session", "")) or node_branch.get(node or "")
        if not branch:
            continue
        b = branches[branch]
        b["runs"].add(run)
        if node:
            b["nodes"].add(node)
        if kind == "change-opened":
            b["pr"] = int(payload["id"])
        elif kind == "change-merged":
            b["merged"] = payload.get("sha")
            m = re.search(r"/pull/(\d+)", payload.get("url", ""))
            if m:
                b["pr"] = int(m.group(1))
        elif kind == "gate-run":
            key = (labels.get("session"), payload.get("started_at"))
            b["gates"][key] = {
                "start": ts(payload.get("started_at")),
                "end": ts(payload.get("ended_at")),
                "verdict": payload.get("verdict"),
                "failed_checks": [c["name"] for c in payload.get("checks", []) if c.get("conclusion") not in ("success", None)],
                "node": node,
            }
        elif kind == "node-dispatched":
            attempt = payload.get("attempt", 1)
            retry = bool(re.search(r"-r\d+$", node or ""))
            if attempt > 1 or retry:
                b["dispatches"].append({"at": ts(event["ts"]), "node": node, "attempt": attempt})
        elif kind == "sync-conflict":
            key = (labels.get("session"), event["ts"])
            b["conflicts"][key] = {"at": ts(event["ts"]), "paths": payload.get("paths", []), "node": node}
        elif kind == "node-settled":
            b["settles"].append({"at": ts(event["ts"]), "node": node, "status": payload.get("status"), "outcome": payload.get("outcome")})
    return branches


# ---------------------------------------------------------------- CI


def ci_runs(hub: gh.GitHub, branch: str, until: dt.datetime) -> list[dict]:
    runs = hub.paged(f"/repos/{gh.OWNER_REPO}/actions/runs?branch={branch}", "workflow_runs")
    out = [r for r in runs if r["name"] == "ci" and r["event"] == "pull_request" and ts(r["run_started_at"]) <= until]
    return sorted(out, key=lambda r: r["run_started_at"])


def analyse_run(hub: gh.GitHub, run: dict) -> dict:
    jobs = hub.paged(f"/repos/{gh.OWNER_REPO}/actions/runs/{run['id']}/jobs?filter=latest", "jobs")
    runner = sum(minutes(ts(j.get("started_at")), ts(j.get("completed_at"))) for j in jobs if j.get("completed_at"))
    info = {
        "id": run["id"],
        "head": run["head_sha"],
        "start": ts(run["run_started_at"]),
        "end": ts(run["updated_at"]),
        "conclusion": run["conclusion"],
        "runner_min": round(runner, 1),
        "elapsed_min": minutes(ts(run["run_started_at"]), ts(run["updated_at"])),
        "census": False,
        "stale": False,
        "kinds": [],
        "artifacts": [],
        "tasks": [],
        "failed_jobs": [],
        "excerpt": "",
    }
    if run["conclusion"] != "failure":
        return info
    for job in jobs:
        if job.get("conclusion") != "failure" or job["name"] == "gate":
            continue
        info["failed_jobs"].append(job["name"])
        status, body = hub.get(f"/repos/{gh.OWNER_REPO}/actions/jobs/{job['id']}/logs")
        if status in (404, 410):
            info["logs_missing"] = info.get("logs_missing", 0) + 1
            continue
        if status != 200:
            raise SystemExit(f"GitHub answered {status} for job {job['id']}'s log; re-run the harness")
        found = classify_failure(clean_log(body))
        info["census"] |= found["census"]
        info["stale"] |= found["stale"]
        info["kinds"] = sorted(set(info["kinds"]) | set(found["kinds"]))
        info["artifacts"] = sorted(set(info["artifacts"]) | set(found["artifacts"]))
        info["tasks"] = sorted(set(info["tasks"]) | set(found["tasks"]))
        if (found["census"] or found["stale"]) and not info["excerpt"]:
            info["excerpt"] = found["excerpt"]
    return info


# ---------------------------------------------------------------- git


def fetch_pr(pr: int) -> str | None:
    ref = f"refs/repin-cost/pull/{pr}"
    done = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "fetch", "--quiet", "--no-tags", "origin", f"+refs/pull/{pr}/head:{ref}"],
        capture_output=True, text=True, check=False,
    )
    if done.returncode != 0:
        return None
    return git("rev-parse", ref).strip()


def has_commit(sha: str) -> bool:
    return subprocess.run(["git", "-C", str(REPO_ROOT), "cat-file", "-e", f"{sha}^{{commit}}"], capture_output=True).returncode == 0


def pinned_changes(a: str | None, b: str) -> dict[str, str]:
    """artifact -> kind for each pinned or derived file b rewrote relative to a (a=None: b against its first parent)."""
    names = git("diff", "--name-only", *([a, b] if a else [f"{b}^", b]), check=False).split()
    out: dict[str, str] = {}
    for name in names:
        found = artifact_kind(name)
        if not found:
            continue
        kind, artifact = found
        if kind == "port-digest":
            patch = git("diff", *([a, b] if a else [f"{b}^", b]), "--", name, check=False)
            if not re.search(r'^[+-].*"[0-9a-f]{16}"', patch, flags=re.M):
                continue
        out[artifact] = kind
    return out


def worker_pinned(a: str, b: str) -> dict[str, str]:
    """Pinned files the branch's own commits in a..b rewrote: non-merge commits, plus what each merge
    from main resolved by hand (files differing from every parent); never what main itself brought in."""
    names = set(git("log", "--no-merges", "--format=", "--name-only", f"{a}..{b}", check=False).split())
    for merge in git("rev-list", "--merges", f"{a}..{b}", check=False).split():
        names |= set(git("diff-tree", "--cc", "--no-commit-id", "--name-only", merge, check=False).split())
    out: dict[str, str] = {}
    for name in sorted(names):
        found = artifact_kind(name)
        if found and (found[0] != "port-digest" or re.search(r'^[+-].*"[0-9a-f]{16}"', git("diff", a, b, "--", name, check=False), flags=re.M)):
            out[found[1]] = found[0]
    return out


# ---------------------------------------------------------------- main


def parse_window(spec: str, root: Path) -> tuple[list[str], list[str]]:
    kind, _, value = spec.partition(":")
    items = [v for v in value.split(",") if v]
    if kind == "runs" and items:
        return items, []
    if kind == "base-carries" and items:
        return crozier_runs(root), items
    raise SystemExit(f"--window must be runs:<run>[,...] or base-carries:<sha>[,...], got {spec!r}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--window", required=True)
    parser.add_argument("--until", default=None, help="ISO time; journal events and CI runs after it are ignored (default: now)")
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--runs-root", type=Path, default=Path(os.environ.get("ONEPIPELINE_RUNS_DIR", ORCH / "runs")))
    args = parser.parse_args()
    until = ts(args.until) if args.until else dt.datetime.now(dt.UTC)
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    runs, carries = parse_window(args.window, args.runs_root)
    hub = gh.GitHub(out / "github-evidence")

    branches: dict[str, dict] = {}
    outcomes: dict[str, str] = {}
    for run in runs:
        if not (args.runs_root / run / "events.jsonl").exists():
            raise SystemExit(f"no journal for run {run!r} under {args.runs_root}; name a run `onepipeline runs --flat` lists")
        for node in onepipeline_results(run).get("nodes", []):
            outcomes[node["id"]] = node.get("outcome") or node.get("status") or "?"
        for name, data in read_journal(args.runs_root, run, until).items():
            if name in branches:
                prev = branches[name]
                prev["nodes"] |= data["nodes"]
                prev["runs"] |= data["runs"]
                prev["pr"] = prev["pr"] or data["pr"]
                prev["merged"] = prev["merged"] or data["merged"]
                prev["gates"].update(data["gates"])
                prev["dispatches"] += data["dispatches"]
                prev["conflicts"].update(data["conflicts"])
                prev["settles"] += data["settles"]
            else:
                branches[name] = data

    git("fetch", "--quiet", "--no-tags", "origin", "+refs/heads/main:refs/repin-cost/main", check=False)
    changes, events = [], []
    for name, b in sorted(branches.items(), key=lambda kv: (kv[1]["pr"] or 10**9, kv[0])):
        head = fetch_pr(b["pr"]) if b["pr"] else None
        if carries:
            if not head or not all(
                subprocess.run(["git", "-C", str(REPO_ROOT), "merge-base", "--is-ancestor", c, head], capture_output=True).returncode == 0
                for c in carries
            ):
                continue
        runs_ci = [analyse_run(hub, r) for r in ci_runs(hub, name, until)]
        gates = sorted(b["gates"].values(), key=lambda g: g["start"])
        conflicts = sorted(b["conflicts"].values(), key=lambda c: c["at"])
        dispatches = sorted(b["dispatches"], key=lambda d: d["at"])
        row = {
            "pr": b["pr"], "branch": name, "runs": sorted(b["runs"]),
            "nodes": [f"{n}={outcomes.get(n, '?')}" for n in sorted(b["nodes"])],
            "merged": bool(b["merged"]), "ci_runs": len(runs_ci), "ci_failed": 0, "census_failures": 0,
            "census_runner_min": 0.0, "census_elapsed_min": 0.0, "census_wait_min": 0.0,
            "other_failures": 0, "attempts": len(gates), "census_attempts": 0, "redispatches": len(dispatches),
            "census_redispatches": 0, "conflict_redispatches": 0, "derived_conflicts": 0, "code_conflicts": 0,
            "conflict_wait_min": 0.0, "census_kinds": [], "rewrote": [],
        }
        failure_marks: list[tuple[dt.datetime, str]] = []
        # --- CI failures, each with its fix and the wait to the next CI run on this branch.
        for i, run in enumerate(runs_ci):
            if run["conclusion"] != "failure":
                continue
            row["ci_failed"] += 1
            nxt = runs_ci[i + 1] if i + 1 < len(runs_ci) else None
            wait = minutes(run["end"], nxt["start"]) if nxt and nxt["start"] > run["end"] else 0.0
            fix = {}
            if nxt and has_commit(run["head"]) and has_commit(nxt["head"]):
                fix = worker_pinned(run["head"], nxt["head"])
            kinds = list(run["kinds"])
            artifacts = list(run["artifacts"])
            if run["census"] and not kinds:
                kinds = sorted({k for k in fix.values() if k in KINDS[:3]}) or ["census-unattributed"]
            if not run["census"] and run["stale"]:
                artifacts = artifacts or sorted(a for a, k in fix.items() if k.startswith("other-artifact"))
                artifacts = artifacts or ["task:" + ",".join(t for t in run["tasks"] if not t.startswith("surface-census:")) or "unnamed"]
                kinds = ["other-artifact:" + a for a in artifacts]
            tier = "census" if run["census"] else ("artifact" if run["stale"] else "other")
            if run["census"]:
                row["census_failures"] += 1
                row["census_runner_min"] += run["runner_min"]
                row["census_elapsed_min"] += run["elapsed_min"]
                row["census_wait_min"] += wait
                row["census_kinds"] = sorted(set(row["census_kinds"]) | set(kinds))
                failure_marks.append((run["end"], "census"))
            else:
                row["other_failures"] += 1
                failure_marks.append((run["end"], tier))
            # A failure of a pinned artifact outside the census is a repin event too.
            if tier in ("census", "artifact"):
                for k in kinds:
                    events.append({
                        "pr": b["pr"], "branch": name, "source": "ci", "at": run["end"].isoformat(), "kind": k,
                        "tier": tier, "ci_run": run["id"], "runner_min": round(run["runner_min"] / len(kinds), 1),
                        "elapsed_min": round(run["elapsed_min"] / len(kinds), 1), "wait_min": round(wait / len(kinds), 1),
                        "fix_files": ";".join(sorted(fix)), "tasks": ";".join(run["tasks"]), "excerpt": run["excerpt"],
                    })
        # --- Publication attempts the journal recorded, matched to the CI run that decided them.
        for g in gates:
            if g["verdict"] == "passed" or "gate" not in g["failed_checks"]:
                continue
            match = [r for r in runs_ci if r["conclusion"] == "failure" and g["start"] - dt.timedelta(hours=3) <= r["end"] <= g["end"] + dt.timedelta(minutes=10)]
            if match and match[-1]["census"]:
                row["census_attempts"] += 1
        # --- Conflicts.
        for c in conflicts:
            pinned = {p: artifact_kind(p) for p in c["paths"]}
            derived = sorted(p for p, k in pinned.items() if k)
            later = [g["start"] for g in gates if g["start"] > c["at"]]
            wait = minutes(c["at"], later[0]) if later else 0.0
            if derived:
                row["derived_conflicts"] += 1
                row["conflict_wait_min"] += wait
                failure_marks.append((c["at"], "conflict"))
                outside = sorted({pinned[p][1] for p in derived if pinned[p][0].startswith("other-artifact")})
                events.append({
                    "pr": b["pr"], "branch": name, "source": "journal", "at": c["at"].isoformat(), "kind": "derived-conflict",
                    "tier": "census" if len(outside) < len(derived) else "artifact", "artifact": ";".join(outside),
                    "share": round(len(outside) / len(derived), 3), "runner_min": 0.0, "elapsed_min": 0.0, "wait_min": wait,
                    "fix_files": ";".join(derived), "tasks": "", "excerpt": "",
                })
            if len(derived) < len(c["paths"]):
                row["code_conflicts"] += 1
        # --- Re-dispatches, attributed to the latest failure before each.
        previous = None
        for d in dispatches:
            before = [m for m in failure_marks if m[0] <= d["at"] and (previous is None or m[0] > previous)]
            previous = d["at"]
            if before:
                last = max(before)[1]
                if last == "census":
                    row["census_redispatches"] += 1
                elif last == "conflict":
                    row["conflict_redispatches"] += 1
        # --- What the change rewrote: its squash commit, else its head against main.
        landed = b["merged"] if b["merged"] and has_commit(b["merged"]) else None
        if landed:
            row["rewrote"] = sorted(pinned_changes(None, landed))
        elif head:
            base = git("merge-base", "refs/repin-cost/main", head, check=False).strip() or None
            row["rewrote"] = sorted(pinned_changes(base, head)) if base else []
        for key in ("census_runner_min", "census_elapsed_min", "census_wait_min", "conflict_wait_min"):
            row[key] = round(row[key], 1)
        changes.append(row)

    for ref in git("for-each-ref", "--format=%(refname)", "refs/repin-cost/", check=False).split():
        git("update-ref", "-d", ref, check=False)
    totals = summarise(changes, events)
    totals["window"] = {"spec": args.window, "until": until.isoformat(), "runs": runs, "base_carries": carries}
    totals["github"] = {"uncached_calls": hub.calls, "cache_hits": hub.hits}
    write_outputs(out, changes, events, totals)
    print(
        f"repin-cost: {len(changes)} changes, {totals['census']['failures']} census-tier CI failures, "
        f"{totals['conflicts']['derived']} derived-table conflicts; {hub.calls} uncached GitHub calls -> {out}/summary.md"
    )
    return 0


def median(values: list[float]) -> float:
    ordered = sorted(values)
    if not ordered:
        return 0.0
    mid = len(ordered) // 2
    return round(ordered[mid] if len(ordered) % 2 else (ordered[mid - 1] + ordered[mid]) / 2, 1)


def summarise(changes: list[dict], events: list[dict]) -> dict:
    census_cycles: dict[int, float] = {}
    for e in events:
        if e["source"] == "ci" and e["tier"] == "census":
            census_cycles[e["ci_run"]] = census_cycles.get(e["ci_run"], 0.0) + e["elapsed_min"] + e["wait_min"]
    conflict_waits = [e["wait_min"] for e in events if e["kind"] == "derived-conflict"]
    with_pr = [c for c in changes if c["pr"]]
    census = {
        "failures": sum(c["census_failures"] for c in changes),
        "changes_hit": sum(1 for c in changes if c["census_failures"]),
        "runner_min": round(sum(c["census_runner_min"] for c in changes), 1),
        "elapsed_min": round(sum(c["census_elapsed_min"] for c in changes), 1),
        "wait_min": round(sum(c["census_wait_min"] for c in changes), 1),
        "attempts": sum(c["census_attempts"] for c in changes),
        "redispatches": sum(c["census_redispatches"] for c in changes),
        "median_cycle_min": median(list(census_cycles.values())),
    }
    conflicts = {
        "derived": sum(c["derived_conflicts"] for c in changes),
        "changes_hit": sum(1 for c in changes if c["derived_conflicts"]),
        "code": sum(c["code_conflicts"] for c in changes),
        "wait_min": round(sum(c["conflict_wait_min"] for c in changes), 1),
        "redispatches": sum(c["conflict_redispatches"] for c in changes),
        "median_wait_min": median(conflict_waits),
    }
    by_kind: dict[str, dict] = {}
    for e in events:
        k = e["kind"]
        slot = by_kind.setdefault(k, {"events": 0, "runner_min": 0.0, "elapsed_min": 0.0, "wait_min": 0.0, "changes": set()})
        slot["events"] += 1
        slot["runner_min"] += e["runner_min"]
        slot["elapsed_min"] += e["elapsed_min"]
        slot["wait_min"] += e["wait_min"]
        slot["changes"].add(e["pr"] or e["branch"])
    for slot in by_kind.values():
        slot["changes"] = len(slot["changes"])
        slot["cycle_min"] = round(slot["elapsed_min"] + slot["wait_min"], 1)
        for key in ("runner_min", "elapsed_min", "wait_min"):
            slot[key] = round(slot[key], 1)
    artifacts: dict[str, dict] = {}
    for e in events:
        if e["source"] == "ci":
            names = [e["kind"].split(":", 1)[1]] if e["kind"].startswith("other-artifact:") else []
            share = 1.0
        else:
            names = [a for a in e.get("artifact", "").split(";") if a]
            share = e.get("share", 0.0) / max(len(names), 1)
        for artifact in names:
            slot = artifacts.setdefault(artifact, {"ci_failures": 0, "conflicts": 0, "cycle_min": 0.0, "runner_min": 0.0, "changes": set()})
            slot["ci_failures" if e["source"] == "ci" else "conflicts"] += 1
            slot["cycle_min"] += (e["elapsed_min"] + e["wait_min"]) * share
            slot["runner_min"] += e["runner_min"] * share
            slot["changes"].add(e["pr"] or e["branch"])
    ranked = sorted(
        ({"artifact": a, **{k: (len(v) if isinstance(v, set) else round(v, 1) if isinstance(v, float) else v) for k, v in s.items()}} for a, s in artifacts.items()),
        key=lambda r: -r["cycle_min"],
    )
    rewrote = collections.Counter(p for c in changes for p in c["rewrote"])
    return {
        "changes": len(changes),
        "changes_with_pr": len(with_pr),
        "merged": sum(1 for c in changes if c["merged"]),
        "ci_runs": sum(c["ci_runs"] for c in changes),
        "ci_failed": sum(c["ci_failed"] for c in changes),
        "other_failures": sum(c["other_failures"] for c in changes),
        "attempts": sum(c["attempts"] for c in changes),
        "redispatches": sum(c["redispatches"] for c in changes),
        "census": census,
        "conflicts": conflicts,
        "by_kind": dict(sorted(by_kind.items())),
        "artifacts_outside_census": ranked,
        "rewrote": dict(rewrote.most_common()),
    }


def write_outputs(out: Path, changes: list[dict], events: list[dict], totals: dict) -> None:
    cols = [
        "pr", "branch", "merged", "ci_runs", "ci_failed", "census_failures", "census_runner_min", "census_elapsed_min",
        "census_wait_min", "other_failures", "attempts", "census_attempts", "redispatches", "census_redispatches",
        "derived_conflicts", "conflict_redispatches", "conflict_wait_min", "code_conflicts", "census_kinds", "rewrote", "nodes", "runs",
    ]
    with (out / "changes.tsv").open("w", encoding="utf-8") as handle:
        handle.write("\t".join(cols) + "\n")
        for c in changes:
            handle.write("\t".join(";".join(v) if isinstance(v := c[k], list) else str(v) for k in cols) + "\n")
    ecols = ["pr", "branch", "source", "at", "kind", "tier", "artifact", "ci_run", "runner_min", "elapsed_min", "wait_min", "fix_files", "tasks", "excerpt"]
    with (out / "events.tsv").open("w", encoding="utf-8") as handle:
        handle.write("\t".join(ecols) + "\n")
        for e in sorted(events, key=lambda e: e["at"]):
            handle.write("\t".join(str(e.get(k, "")) for k in ecols) + "\n")
    (out / "totals.json").write_text(json.dumps(totals, indent=2, default=str) + "\n", encoding="utf-8")
    c, k = totals["census"], totals["conflicts"]
    n = max(totals["changes"], 1)
    lines = [
        f"# Repin cost — `{totals['window']['spec']}` until {totals['window']['until']}",
        "",
        f"- Changes: {totals['changes']} ({totals['changes_with_pr']} with a PR, {totals['merged']} merged); "
        f"CI runs {totals['ci_runs']}, failed {totals['ci_failed']}.",
        f"- Census-tier CI failures: {c['failures']} ({c['failures'] / n:.2f} per change, {c['changes_hit']} changes hit); "
        f"runner {c['runner_min']} min, elapsed {c['elapsed_min']} min, wait to next run {c['wait_min']} min "
        f"(cycle {round(c['elapsed_min'] + c['wait_min'], 1)} min, median {c['median_cycle_min']} per failure).",
        f"- Publication attempts {totals['attempts']} (census-failed {c['attempts']}); re-dispatches {totals['redispatches']} "
        f"(after a census failure {c['redispatches']}, after a derived conflict {k['redispatches']}).",
        f"- Derived-table conflicts: {k['derived']} ({k['changes_hit']} changes), wait to next attempt {k['wait_min']} min "
        f"(median {k['median_wait_min']} per conflict); "
        f"code-only conflicts {k['code']}.",
        "",
        "| kind | events | changes | runner min | elapsed min | wait min | cycle min |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for kind, s in totals["by_kind"].items():
        lines.append(f"| `{kind}` | {s['events']} | {s['changes']} | {s['runner_min']} | {s['elapsed_min']} | {s['wait_min']} | {s['cycle_min']} |")
    lines += ["", "| artifact outside the census | CI failures | conflicts | changes | cycle min | runner min |", "| --- | --- | --- | --- | --- | --- |"]
    for r in totals["artifacts_outside_census"]:
        lines.append(f"| `{r['artifact']}` | {r['ci_failures']} | {r['conflicts']} | {r['changes']} | {r['cycle_min']} | {r['runner_min']} |")
    lines += ["", f"GitHub: {totals['github']['uncached_calls']} uncached calls, {totals['github']['cache_hits']} cache hits.", ""]
    (out / "summary.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
