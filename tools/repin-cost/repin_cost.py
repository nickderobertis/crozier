#!/usr/bin/env python3
"""Measure what repinning cost crozier changes in a window.

    python3 tools/repin-cost/repin_cost.py --window runs:<run>[,<run>...] [--until <ISO>] --out <dir>
    python3 tools/repin-cost/repin_cost.py --window base-carries:<sha>[,<sha>...] [--until <ISO>] --out <dir>

`runs:` takes the crozier changes the named runs produced; `base-carries:` scans every
run under the runs root that worked crozier and keeps the changes whose *base* -- the
merge base of the PR's head with crozier's main, so never a commit the branch itself
introduces -- has every named commit as an ancestor. A change is a pull request: a node
branch that never opened one is examined but kept out of every total, and listed in
<out>/excluded.tsv with the reason, as is every change a base-carries window leaves out. Three sources are joined per change (pull request,
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

Exit codes: 0 when the outputs were written; 1 when the measurement stopped on evidence it
could not read or trust (a GitHub answer other than 200, a malformed journal, GitHub record
or output directory, a failed git or results read), naming the cause on stderr; 2 when the
command line is wrong (a bad --window, --until or --runs-root).
"""

# llmlint: ignore-file[modern_domain_modeling] The measurement's rows and totals stay keyed records: every output file's columns are the frozen contract with the committed baseline and serialise by those names, and retyping about 1,000 lines of a method held to the spike's would risk the figures it must reproduce; the journeys pin the outputs instead.
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
from typing import Any

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

import gh  # noqa: E402 -- sibling adapter must follow the runtime script-directory path setup.

IDENTITY = "github.com/nickderobertis/crozier"
ORCH = Path(os.environ.get("ONEPIPELINE_ORCHESTRATOR_ROOT", "/home/whoop/ai-orchestrator"))
# llmlint: ignore[contracts_have_one_source_or_a_drift_gate] The census tier is the spike method's fixed definition, frozen so a re-take stays comparable with the baseline; following a later target rename here would change what is counted, and `comparison.md` states the one target this leaves out.
CENSUS_TASKS = ("surface-census:test-census", "surface-census:test-reach", "surface-census:test-reach-portable")
UNAVAILABLE_OUTCOME = "unavailable (node retired; not in current results)"
KINDS = ("site-anchor", "port-digest", "measured-count", "derived-conflict")


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
DIGEST_RE = re.compile(
    r"re-pin the digest|changed; re-derive|re-derive .* from src/|digest .* (moved|changed)|port digest"
)
COUNT_RE = re.compile(
    r"golden-reach\.tsv|handwritten-reach\.tsv|evidence\.toml|just golden-reach|just handwritten-reach|"
    r"golden-reach-report|reach cell|is stale|out of date|re-?measure|restate-coverage|generated section"
)
# A check outside the census failing because committed data went stale (a repin), as against a content or code defect.
STALE_RE = re.compile(
    r"is stale|not measured|re-?pin|rerun without --check|regenerate|UPDATE_\w+=1|has drifted|drift|re-?bless|"
    r"out of date|run `just [\w-]+(?:-measure|-report|-bless|-update|-refresh)`"
)
DATA_PATH_RE = re.compile(
    r"(?:^|[\s/\\:])((?:docs|tests/fixtures|assets|shots)[/\\][\w./\\-]+\.(?:tsv|json|toml|md|yml))"
)
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
        if re.match(
            r"\s*(E |FAILED |---- .* ----|thread '.*' panicked|AssertionError|assertion|Error:|error:|failures?:)", line
        ):
            keep.extend(lines[i : i + 4])
    return "\n".join(keep)


def classify_failure(log: str) -> dict:
    tasks = failed_tasks(log)
    errors = error_text(log)
    census = any(t in CENSUS_TASKS for t in tasks) or bool(
        re.search(r"FAILED tools/surface-census/tests/surface_census_test\.py", log)
    )
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
    first = next(
        (
            line.strip()
            for line in errors.splitlines()
            if line.strip().startswith(("E ", "E\t")) and len(line.strip()) > 3
        ),
        "",
    )
    return {
        "tasks": tasks,
        "census": census,
        "stale": stale,
        "kinds": kinds,
        "artifacts": sorted(artifacts),
        "excerpt": first[:200],
    }


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


# llmlint: ignore[async_typed_clients_at_boundaries] AGENTS.md keeps this tooling stdlib-only and installless; one short-lived results read per run, one after another, gains nothing from an async client.
def onepipeline_results(run: str) -> dict:
    binary = ORCH / "node_modules" / ".bin" / "onepipeline"
    command = (
        json.loads(os.environ["ONEPIPELINE_RESULTS_COMMAND"])
        if "ONEPIPELINE_RESULTS_COMMAND" in os.environ
        else [str(binary)]
    )
    if not isinstance(command, list) or not command or not all(isinstance(arg, str) and arg for arg in command):
        raise SystemExit("ONEPIPELINE_RESULTS_COMMAND must be a nonempty JSON array of nonempty argv strings")
    done = subprocess.run(
        [*command, "results", run, "--json"],
        capture_output=True,
        text=True,
        check=False,
        cwd=ORCH if ORCH.exists() else REPO_ROOT,
    )
    if done.returncode:
        raise SystemExit(
            f"onepipeline results {run}: exited {done.returncode}: {done.stderr.strip()}; restore the results provider"
        )
    try:
        data = json.loads(done.stdout)
    except json.JSONDecodeError as error:
        raise SystemExit(f"onepipeline results {run}: invalid JSON; restore the results provider") from error
    if (
        not isinstance(data, dict)
        or not isinstance(data.get("nodes"), list)
        or any(
            not isinstance(node, dict)
            or not isinstance(node.get("id"), str)
            or not all(node.get(key) is None or isinstance(node[key], str) for key in ("status", "outcome"))
            for node in data["nodes"]
        )
    ):
        raise SystemExit(
            f"onepipeline results {run}: expected an object containing nodes with string ids and status/outcome values"
        )
    return data


def crozier_runs(root: Path) -> list[str]:
    out = []
    for plan in sorted(root.glob("*/plan.json")):
        try:
            text = plan.read_text(encoding="utf-8", errors="replace")
        except OSError as error:
            raise SystemExit(f"cannot read {plan}: {error}; an unread plan would drop its run's changes") from error
        # llmlint: ignore[boundary_inputs_validated] A run "worked crozier" when its plan names the repository anywhere: the spike's selection rule, kept so this window matches the baseline's; the plan's schema is the orchestrator's.
        if "nickderobertis/crozier" in text:
            out.append(plan.parent.name)
    return out


def record_event(b: dict, kind: str, event: dict, labels: dict, payload: dict, node: str | None) -> None:
    match kind:
        case "change-opened":
            b["pr"] = int(payload["id"])
        case "change-merged":
            b["merged"] = payload.get("sha")
            m = re.search(r"/pull/(\d+)", payload.get("url", ""))
            if m:
                b["pr"] = int(m.group(1))
        case "gate-run":
            key = (labels.get("session"), payload.get("started_at"))
            b["gates"][key] = {
                "start": ts(payload.get("started_at")),
                "end": ts(payload.get("ended_at")),
                "verdict": payload.get("verdict"),
                "failed_checks": [
                    c["name"] for c in payload.get("checks", []) if c.get("conclusion") not in ("success", None)
                ],
                "node": node,
            }
        case "node-dispatched":
            attempt = payload.get("attempt", 1)
            retry = bool(re.search(r"-r\d+$", node or ""))
            if attempt > 1 or retry:
                b["dispatches"].append({"at": ts(event["ts"]), "node": node, "attempt": attempt})
        case "sync-conflict":
            key = (labels.get("session"), event["ts"])
            b["conflicts"][key] = {"at": ts(event["ts"]), "paths": payload.get("paths", []), "node": node}
        case "push" if payload.get("accepted") and payload.get("head"):
            b["pushes"].append((ts(event["ts"]), payload["head"]))
        case "node-settled":
            b["settles"].append(
                {
                    "at": ts(event["ts"]),
                    "node": node,
                    "status": payload.get("status"),
                    "outcome": payload.get("outcome"),
                }
            )


# llmlint: ignore-block[contracts_have_one_source_or_a_drift_gate] The journal's event names and fields belong to the orchestrator, outside this repository, so nothing here can reconcile against them; an event missing a field it needs stops the run instead.
def read_journal(root: Path, run: str, until: dt.datetime) -> dict:
    """Per branch: nodes, PR, gate attempts, dispatches, conflicts, settles."""
    branches: dict[str, dict] = collections.defaultdict(
        lambda: {
            "nodes": set(),
            "runs": set(),
            "pr": None,
            "merged": None,
            "gates": {},
            "dispatches": [],
            "conflicts": {},
            "settles": [],
            "pushes": [],
        }
    )
    session_branch: dict[str, str] = {}
    node_branch: dict[str, str] = {}
    pending: list[dict] = []
    path = root / run / "events.jsonl"
    with path.open(encoding="utf-8", errors="replace") as handle:
        for line in handle:
            try:
                event = json.loads(line)
            # llmlint: ignore[boundary_inputs_validated] An interrupted writer leaves a torn line in a live journal; it records no completed event, and refusing it would make every run that was ever killed unmeasurable.
            except json.JSONDecodeError:
                continue
            if (
                not isinstance(event, dict)
                or not isinstance(event.get("labels", {}), dict)
                or not isinstance(event.get("payload") or {}, dict)
            ):
                raise SystemExit(
                    f"{path}: an event is not an object with object labels and payload; repair the journal"
                )
            when = ts(event.get("ts"))
            if when is None or when > until:
                continue
            labels, payload = event.get("labels", {}), event.get("payload") or {}
            if labels.get("identity") not in (None, IDENTITY):
                continue
            branch = payload.get("branch")
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
        try:
            record_event(b, kind, event, labels, payload, node)
        except (KeyError, TypeError, ValueError, AttributeError) as error:
            raise SystemExit(f"{path}: {kind} event at {event.get('ts')}: {error!r}; repair the journal") from error
    return branches


# llmlint: ignore-end[contracts_have_one_source_or_a_drift_gate]


def ci_runs(hub: gh.GitHub, branch: str, until: dt.datetime) -> list[dict]:
    runs = hub.paged(
        f"/repos/{gh.OWNER_REPO}/actions/runs?branch={branch}",
        "workflow_runs",
        fields=("id", "name", "event", "head_sha", "run_started_at", "updated_at", "conclusion"),
    )
    out = [
        r
        for r in runs
        if r["name"] == "ci"
        and r["event"] == "pull_request"
        and (started := ts(r["run_started_at"])) is not None
        and started <= until
    ]
    return sorted(out, key=lambda r: r["run_started_at"])


def analyse_run(hub: gh.GitHub, run: dict) -> dict:
    jobs = hub.paged(
        f"/repos/{gh.OWNER_REPO}/actions/runs/{run['id']}/jobs?filter=latest",
        "jobs",
        fields=("id", "name", "conclusion"),
    )
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


def fetch_pr(pr: int) -> str | None:
    ref = f"refs/repin-cost/pull/{pr}"
    done = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "fetch", "--quiet", "--no-tags", "origin", f"+refs/pull/{pr}/head:{ref}"],
        capture_output=True,
        text=True,
        check=False,
    )
    if done.returncode != 0:
        return None
    return git("rev-parse", ref).strip()


def is_ancestor(ancestor: str, descendant: str) -> bool:
    if not descendant:
        return False
    return (
        subprocess.run(
            ["git", "-C", str(REPO_ROOT), "merge-base", "--is-ancestor", ancestor, descendant], capture_output=True
        ).returncode
        == 0
    )


def has_commit(sha: str) -> bool:
    return (
        subprocess.run(
            ["git", "-C", str(REPO_ROOT), "cat-file", "-e", f"{sha}^{{commit}}"], capture_output=True
        ).returncode
        == 0
    )


# llmlint: ignore-block[boundary_inputs_validated] A failed read here means an intermediate head was force-pushed away, so its fix attribution is empty: the limit the spike's method states and the baseline carries.
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
        if found and (
            found[0] != "port-digest"
            or re.search(r'^[+-].*"[0-9a-f]{16}"', git("diff", a, b, "--", name, check=False), flags=re.M)
        ):
            out[found[1]] = found[0]
    return out


# llmlint: ignore-end[boundary_inputs_validated]


def parse_window(spec: str, root: Path) -> tuple[list[str], list[str]]:
    """The runs a window reads and the commits it requires; ValueError names what is wrong with it."""
    kind, _, value = spec.partition(":")
    items = [v for v in value.split(",") if v]
    if kind == "runs" and items:
        bad = [v for v in items if v in (".", "..") or "/" in v or "\\" in v]
        if bad:
            raise ValueError(f"--window names run {bad[0]!r}, which is not a directory name under the runs root")
        return items, []
    if kind == "base-carries" and items:
        unknown = [v for v in items if not re.fullmatch(r"[0-9a-f]{40}", v) or not has_commit(v)]
        if unknown:
            raise ValueError(f"--window needs full commit shas this checkout holds; {unknown[0]!r} is not one")
        return crozier_runs(root), items
    raise ValueError(f"--window must be runs:<run>[,...] or base-carries:<sha>[,...], got {spec!r}")


def parse_cutoff(value: str) -> dt.datetime:
    """--until as an aware time, since the journal and CI times it is compared with all are."""
    cutoff = ts(value)
    if cutoff is None or cutoff.tzinfo is None:
        raise ValueError(f"--until must carry a UTC offset or Z, got {value!r}")
    return cutoff


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "compare":
        from comparison import comparison

        parser = argparse.ArgumentParser(description="Compare two repin-cost output directories")
        parser.add_argument("baseline", type=Path)
        parser.add_argument("after", type=Path)
        args = parser.parse_args(sys.argv[2:])
        target = args.after / "comparison.md"
        try:
            rendered = comparison(args.baseline, args.after)
            target.write_text(rendered, encoding="utf-8")
        except (OSError, ValueError, KeyError, TypeError) as error:
            raise SystemExit(f"repin-cost compare: {error}; provide complete measurement output directories") from error
        print(f"repin-cost: comparison -> {target}")
        return 0
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--window", required=True)
    parser.add_argument(
        "--until", default=None, help="ISO time; journal events and CI runs after it are ignored (default: now)"
    )
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--runs-root", type=Path, default=Path(os.environ.get("ONEPIPELINE_RUNS_DIR", ORCH / "runs")))
    args = parser.parse_args()
    if not args.runs_root.is_dir():
        parser.error(f"--runs-root {args.runs_root} is not a directory")
    try:
        until = parse_cutoff(args.until) if args.until else dt.datetime.now(dt.UTC)
        runs, carries = parse_window(args.window, args.runs_root)
    except ValueError as error:
        parser.error(str(error))
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    hub = gh.GitHub(out / "github-evidence")

    branches: dict[str, dict] = {}
    outcomes: dict[str, str] = {}
    for run in runs:
        if not (args.runs_root / run / "events.jsonl").exists():
            raise SystemExit(
                f"no journal for run {run!r} under {args.runs_root}; name a run `onepipeline runs --flat` lists"
            )
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
                prev["pushes"] += data["pushes"]
            else:
                branches[name] = data

    try:
        git("fetch", "--quiet", "--no-tags", "origin", "+refs/heads/main:refs/repin-cost/main")
    except RuntimeError as error:
        raise SystemExit(f"{error}; a base cannot be read without main") from error
    changes, events, excluded = [], [], []
    for name, b in sorted(branches.items(), key=lambda kv: (kv[1]["pr"] or 10**9, kv[0])):
        examined = {
            "pr": b["pr"] or "",
            "branch": name,
            "base": "",
            "head": "",
            "nodes": ";".join(f"{n}={outcomes.get(n, UNAVAILABLE_OUTCOME)}" for n in sorted(b["nodes"])),
            "attempts": len(b["gates"]),
            "redispatches": len(b["dispatches"]),
            "conflicts": len(b["conflicts"]),
        }
        if not b["pr"]:
            excluded.append({**examined, "reason": "no pull request: not a change"})
            continue
        head = fetch_pr(b["pr"])
        if carries:
            # The head as of --until: the last push the journals recorded before it, when git holds it.
            pushed = [h for _, h in sorted(b["pushes"]) if has_commit(h)]
            head = pushed[-1] if pushed else head
            if not head:
                excluded.append({**examined, "reason": f"refs/pull/{b['pr']}/head not fetchable"})
                continue
            base = git("merge-base", "refs/repin-cost/main", head, check=False).strip()
            examined.update(base=base[:12], head=head[:12])
            missing = [c for c in carries if not is_ancestor(c, base)]
            if missing:
                own = [c for c in missing if is_ancestor(c, head)]
                why = f"base {base[:12]} lacks {','.join(m[:12] for m in missing)}"
                if own:
                    why += f" (the branch's own commits carry {','.join(o[:12] for o in own)})"
                excluded.append({**examined, "reason": why})
                continue
        runs_ci = [analyse_run(hub, r) for r in ci_runs(hub, name, until)]
        gates = sorted(b["gates"].values(), key=lambda g: g["start"])
        conflicts = sorted(b["conflicts"].values(), key=lambda c: c["at"])
        dispatches = sorted(b["dispatches"], key=lambda d: d["at"])
        # Any: one TSV row's mixed columns, serialised by name in write_outputs.
        row: dict[str, Any] = {
            "pr": b["pr"],
            "branch": name,
            "runs": sorted(b["runs"]),
            "nodes": [f"{n}={outcomes.get(n, UNAVAILABLE_OUTCOME)}" for n in sorted(b["nodes"])],
            "merged": bool(b["merged"]),
            "ci_runs": len(runs_ci),
            "ci_failed": 0,
            "census_failures": 0,
            "census_runner_min": 0.0,
            "census_elapsed_min": 0.0,
            "census_wait_min": 0.0,
            "other_failures": 0,
            "attempts": len(gates),
            "census_attempts": 0,
            "redispatches": len(dispatches),
            "census_redispatches": 0,
            "conflict_redispatches": 0,
            "derived_conflicts": 0,
            "mixed_conflicts": 0,
            "code_conflicts": 0,
            "conflict_wait_min": 0.0,
            "census_pub_failures": 0,
            "census_pub_wait_min": 0.0,
            "census_pub_unresolved": 0,
            "census_ci_unresolved": 0,
            "census_kinds": [],
            "rewrote": [],
        }
        failure_marks: list[tuple[dt.datetime, str, tuple[str, ...]]] = []
        run_kinds: dict[int, list[str]] = {}
        row["kind_attempts"], row["kind_redispatches"] = collections.Counter(), collections.Counter()
        # --- Journal publication attempts, each matched to the failed CI run that decided it, and the
        # wall clock from its recorded end to the next attempt's recorded start on this branch.
        gate_match: list[tuple[dict, dict | None]] = []
        publication: dict[int, dict] = {}
        for gi, g in enumerate(gates):
            if g["verdict"] == "passed" or "gate" not in g["failed_checks"]:
                continue
            match = [
                r
                for r in runs_ci
                if r["conclusion"] == "failure"
                and g["start"] - dt.timedelta(hours=3) <= r["end"] <= g["end"] + dt.timedelta(minutes=10)
            ]
            decided = match[-1] if match else None
            gate_match.append((g, decided))
            if decided:
                following = [n for n in gates[gi + 1 :] if n["start"] > g["end"]]
                nxt_pub = following[0] if following else None
                publication[decided["id"]] = {
                    "pub_end": g["end"].isoformat(),
                    "next_pub_start": nxt_pub["start"].isoformat() if nxt_pub else "",
                    "pub_wait_min": minutes(g["end"], nxt_pub["start"]) if nxt_pub else None,
                }
        # --- CI failures, each with its fix and the wait to the next CI run on this branch.
        for i, run in enumerate(runs_ci):
            if run["conclusion"] != "failure":
                continue
            row["ci_failed"] += 1
            nxt = runs_ci[i + 1] if i + 1 < len(runs_ci) else None
            ci_resolved = bool(nxt and nxt["start"] > run["end"])
            wait = minutes(run["end"], nxt["start"]) if ci_resolved else 0.0
            fix = {}
            if nxt and has_commit(run["head"]) and has_commit(nxt["head"]):
                fix = worker_pinned(run["head"], nxt["head"])
            kinds = list(run["kinds"])
            artifacts = list(run["artifacts"])
            if run["census"] and not kinds:
                kinds = sorted({k for k in fix.values() if k in KINDS[:3]}) or ["census-unattributed"]
            if not run["census"] and run["stale"]:
                artifacts = artifacts or sorted(a for a, k in fix.items() if k.startswith("other-artifact"))
                artifacts = artifacts or [
                    "task:" + ",".join(t for t in run["tasks"] if not t.startswith("surface-census:")) or "unnamed"
                ]
                kinds = ["other-artifact:" + a for a in artifacts]
            tier = "census" if run["census"] else ("artifact" if run["stale"] else "other")
            if run["census"]:
                row["census_failures"] += 1
                row["census_runner_min"] += run["runner_min"]
                row["census_elapsed_min"] += run["elapsed_min"]
                row["census_wait_min"] += wait
                row["census_ci_unresolved"] += 0 if ci_resolved else 1
                pub = publication.get(run["id"])
                if pub:
                    row["census_pub_failures"] += 1
                    if pub["pub_wait_min"] is None:
                        row["census_pub_unresolved"] += 1
                    else:
                        row["census_pub_wait_min"] += pub["pub_wait_min"]
                row["census_kinds"] = sorted(set(row["census_kinds"]) | set(kinds))
                failure_marks.append((run["end"], "census", tuple(kinds)))
            else:
                row["other_failures"] += 1
                failure_marks.append((run["end"], tier, tuple(kinds) if tier == "artifact" else ()))
            run_kinds[run["id"]] = kinds if tier in ("census", "artifact") else []
            # A failure of a pinned artifact outside the census is a repin event too.
            if tier in ("census", "artifact"):
                pub = publication.get(run["id"])
                if pub is None:
                    pub_fields = {
                        "pub_status": "no-publication",
                        "pub_end": "",
                        "next_pub_start": "",
                        "pub_wait_min": "",
                    }
                elif pub["pub_wait_min"] is None:
                    pub_fields = {
                        "pub_status": "unresolved",
                        "pub_end": pub["pub_end"],
                        "next_pub_start": "",
                        "pub_wait_min": "",
                    }
                else:
                    pub_fields = {
                        "pub_status": "observed",
                        "pub_end": pub["pub_end"],
                        "next_pub_start": pub["next_pub_start"],
                        "pub_wait_min": round(pub["pub_wait_min"] / len(kinds), 1),
                    }
                for k in kinds:
                    events.append(
                        {
                            **pub_fields,
                            "ci_next_run": "observed" if ci_resolved else "unresolved",
                            "pr": b["pr"],
                            "branch": name,
                            "source": "ci",
                            "at": run["end"].isoformat(),
                            "kind": k,
                            "tier": tier,
                            "ci_run": run["id"],
                            "runner_min": round(run["runner_min"] / len(kinds), 1),
                            "elapsed_min": round(run["elapsed_min"] / len(kinds), 1),
                            "wait_min": round(wait / len(kinds), 1),
                            "fix_files": ";".join(sorted(fix)),
                            "tasks": ";".join(run["tasks"]),
                            "excerpt": run["excerpt"],
                        }
                    )
        for _g, decided in gate_match:
            if decided and decided["census"]:
                row["census_attempts"] += 1
            if decided:
                row["kind_attempts"].update(run_kinds.get(decided["id"], []))
        for c in conflicts:
            pinned = {p: artifact_kind(p) for p in c["paths"]}
            derived = sorted(p for p, k in pinned.items() if k)
            later = [g["start"] for g in gates if g["start"] > c["at"]]
            wait = minutes(c["at"], later[0]) if later else 0.0
            if derived:
                row["derived_conflicts"] += 1
                row["conflict_wait_min"] += wait
                failure_marks.append((c["at"], "conflict", ("derived-conflict",)))
                outside = sorted(
                    {value[1] for p in derived if (value := pinned[p]) and value[0].startswith("other-artifact")}
                )
                events.append(
                    {
                        "pr": b["pr"],
                        "branch": name,
                        "source": "journal",
                        "at": c["at"].isoformat(),
                        "kind": "derived-conflict",
                        "tier": "census" if len(outside) < len(derived) else "artifact",
                        "artifact": ";".join(outside),
                        "share": round(len(outside) / len(derived), 3),
                        "runner_min": 0.0,
                        "elapsed_min": 0.0,
                        "wait_min": wait,
                        "fix_files": ";".join(derived),
                        "tasks": "",
                        "excerpt": "",
                    }
                )
            if not derived:
                row["code_conflicts"] += 1
            elif len(derived) < len(c["paths"]):
                row["mixed_conflicts"] += 1
        # --- Re-dispatches, attributed to the latest failure before each.
        previous = None
        for d in dispatches:
            before = [m for m in failure_marks if m[0] <= d["at"] and (previous is None or m[0] > previous)]
            previous = d["at"]
            if before:
                latest = max(before, key=lambda m: m[0])
                last = latest[1]
                row["kind_redispatches"].update(latest[2])
                match last:
                    case "census":
                        row["census_redispatches"] += 1
                    case "conflict":
                        row["conflict_redispatches"] += 1
        # --- What the change rewrote: its squash commit, else its head against main.
        landed = b["merged"] if b["merged"] and has_commit(b["merged"]) else None
        if landed:
            row["rewrote"] = sorted(pinned_changes(None, landed))
        elif head:
            base = git("merge-base", "refs/repin-cost/main", head, check=False).strip() or None
            row["rewrote"] = sorted(pinned_changes(base, head)) if base else []
        for key in (
            "census_runner_min",
            "census_elapsed_min",
            "census_wait_min",
            "conflict_wait_min",
            "census_pub_wait_min",
        ):
            row[key] = round(row[key], 1)
        changes.append(row)

    for ref in git("for-each-ref", "--format=%(refname)", "refs/repin-cost/", check=False).split():
        git("update-ref", "-d", ref, check=False)
    totals = summarise(changes, events)
    totals["window"] = {"spec": args.window, "until": until.isoformat(), "runs": runs, "base_carries": carries}
    totals["github"] = {"uncached_calls": hub.calls, "cache_hits": hub.hits}
    totals["excluded"] = excluded
    write_outputs(out, changes, events, totals)
    xcols = ["pr", "branch", "reason", "base", "head", "attempts", "redispatches", "conflicts", "nodes"]
    with (out / "excluded.tsv").open("w", encoding="utf-8") as handle:
        handle.write("\t".join(xcols) + "\n")
        for x in excluded:
            handle.write("\t".join(str(x[k]) for k in xcols) + "\n")
    print(
        f"repin-cost: {len(changes)} changes ({len(excluded)} examined and excluded), {totals['census']['failures']} census-tier CI failures, "
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
    pub_waits: dict[int, float] = {}
    for e in events:
        if e["source"] == "ci" and e["tier"] == "census" and e.get("pub_status") == "observed":
            pub_waits[e["ci_run"]] = pub_waits.get(e["ci_run"], 0.0) + e["pub_wait_min"]
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
        "ci_retry_unresolved": sum(c["census_ci_unresolved"] for c in changes),
        "publications": sum(c["census_pub_failures"] for c in changes),
        "pub_wait_min": round(sum(c["census_pub_wait_min"] for c in changes), 1),
        "pub_unresolved": sum(c["census_pub_unresolved"] for c in changes),
        "pub_observed": sum(c["census_pub_failures"] - c["census_pub_unresolved"] for c in changes),
        "median_pub_wait_min": median(list(pub_waits.values())),
    }
    conflicts = {
        "derived": sum(c["derived_conflicts"] for c in changes),
        "changes_hit": sum(1 for c in changes if c["derived_conflicts"]),
        "code": sum(c["code_conflicts"] for c in changes),
        "mixed": sum(c["mixed_conflicts"] for c in changes),
        "wait_min": round(sum(c["conflict_wait_min"] for c in changes), 1),
        "redispatches": sum(c["conflict_redispatches"] for c in changes),
        "median_wait_min": median(conflict_waits),
    }
    by_kind: dict[str, dict] = {}
    for e in events:
        k = e["kind"]
        slot = by_kind.setdefault(
            k, {"events": 0, "runner_min": 0.0, "elapsed_min": 0.0, "wait_min": 0.0, "changes": set()}
        )
        slot["events"] += 1
        slot["runner_min"] += e["runner_min"]
        slot["elapsed_min"] += e["elapsed_min"]
        slot["wait_min"] += e["wait_min"]
        match e.get("pub_status"):
            case "observed":
                slot["pub_observed"] = slot.get("pub_observed", 0) + 1
                slot["pub_wait_min"] = slot.get("pub_wait_min", 0.0) + e["pub_wait_min"]
            case "unresolved":
                slot["pub_unresolved"] = slot.get("pub_unresolved", 0) + 1
        slot["changes"].add(e["pr"] or e["branch"])
    for c in changes:
        for field, key in (("kind_attempts", "attempts"), ("kind_redispatches", "redispatches")):
            for kind, count in c[field].items():
                slot = by_kind.setdefault(
                    kind, {"events": 0, "runner_min": 0.0, "elapsed_min": 0.0, "wait_min": 0.0, "changes": set()}
                )
                slot[key] = slot.get(key, 0) + count
    for slot in by_kind.values():
        slot.setdefault("attempts", 0)
        slot.setdefault("pub_observed", 0)
        slot.setdefault("pub_unresolved", 0)
        slot["pub_wait_min"] = round(slot.get("pub_wait_min", 0.0), 1)
        slot.setdefault("redispatches", 0)
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
            slot = artifacts.setdefault(
                artifact, {"ci_failures": 0, "conflicts": 0, "cycle_min": 0.0, "runner_min": 0.0, "changes": set()}
            )
            slot["ci_failures" if e["source"] == "ci" else "conflicts"] += 1
            slot["cycle_min"] += (e["elapsed_min"] + e["wait_min"]) * share
            slot["runner_min"] += e["runner_min"] * share
            slot["changes"].add(e["pr"] or e["branch"])
    ranked = sorted(
        (
            {
                "artifact": a,
                **{
                    k: (len(v) if isinstance(v, set) else round(v, 1) if isinstance(v, float) else v)
                    for k, v in s.items()
                },
            }
            for a, s in artifacts.items()
        ),
        key=lambda r: -float(r["cycle_min"]),
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
        "pr",
        "branch",
        "merged",
        "ci_runs",
        "ci_failed",
        "census_failures",
        "census_runner_min",
        "census_elapsed_min",
        "census_wait_min",
        "census_ci_unresolved",
        "census_pub_failures",
        "census_pub_wait_min",
        "census_pub_unresolved",
        "other_failures",
        "attempts",
        "census_attempts",
        "redispatches",
        "census_redispatches",
        "derived_conflicts",
        "mixed_conflicts",
        "conflict_redispatches",
        "conflict_wait_min",
        "code_conflicts",
        "census_kinds",
        "rewrote",
        "nodes",
        "runs",
    ]
    with (out / "changes.tsv").open("w", encoding="utf-8") as handle:
        handle.write("\t".join(cols) + "\n")
        for c in changes:
            handle.write("\t".join(";".join(v) if isinstance(v := c[k], list) else str(v) for k in cols) + "\n")
    for c in changes:
        c["kind_attempts"], c["kind_redispatches"] = dict(c["kind_attempts"]), dict(c["kind_redispatches"])
    ecols = [
        "pr",
        "branch",
        "source",
        "at",
        "kind",
        "tier",
        "artifact",
        "ci_run",
        "runner_min",
        "elapsed_min",
        "wait_min",
        "ci_next_run",
        "pub_status",
        "pub_end",
        "next_pub_start",
        "pub_wait_min",
        "fix_files",
        "tasks",
        "excerpt",
    ]
    with (out / "events.tsv").open("w", encoding="utf-8") as handle:
        handle.write("\t".join(ecols) + "\n")
        for e in sorted(events, key=lambda e: e["at"]):
            # An unresolved CI retry wait is written blank, never as an observed 0.
            shown = {**e, "wait_min": ""} if e.get("ci_next_run") == "unresolved" else e
            handle.write("\t".join(str(shown.get(k, "")) for k in ecols) + "\n")
    (out / "totals.json").write_text(json.dumps(totals, indent=2, default=str) + "\n", encoding="utf-8")
    c, k = totals["census"], totals["conflicts"]
    n = max(totals["changes"], 1)
    lines = [
        f"# Repin cost — `{totals['window']['spec']}` until {totals['window']['until']}",
        "",
        f"- Changes: {totals['changes']} ({totals['changes_with_pr']} with a PR, {totals['merged']} merged); "
        f"CI runs {totals['ci_runs']}, failed {totals['ci_failed']}.",
        f"- Census-tier CI failures: {c['failures']} ({c['failures'] / n:.2f} per change, {c['changes_hit']} changes hit); "
        f"runner {c['runner_min']} min, elapsed {c['elapsed_min']} min, CI retry wait (failed run's end to the branch's next CI run's start) "
        f"{c['wait_min']} min, {c['ci_retry_unresolved']} with no next CI run by the cutoff (unresolved, not counted) "
        f"(cycle {round(c['elapsed_min'] + c['wait_min'], 1)} min, median {c['median_cycle_min']} per failure).",
        f"- Census-failed journal publications: {c['publications']} (the attempt's recorded end to the branch's next attempt's recorded start): "
        f"{c['pub_observed']} observed, {c['pub_wait_min']} min (median {c['median_pub_wait_min']}); {c['pub_unresolved']} unresolved "
        f"(no next publication by the cutoff); {c['failures'] - c['publications']} census failures had no journal publication.",
        f"- Publication attempts {totals['attempts']} (census-failed {c['attempts']}); re-dispatches {totals['redispatches']} "
        f"(after a census failure {c['redispatches']}, after a derived conflict {k['redispatches']}).",
        f"- Derived-table conflicts: {k['derived']} ({k['changes_hit']} changes), wait to next attempt {k['wait_min']} min "
        f"(median {k['median_wait_min']} per conflict), {k['mixed']} of them also conflicting in code; "
        f"code-only conflicts {k['code']}.",
        "",
        "Per kind (a failure naming several kinds counts once under each; its minutes are split evenly between them):",
        "",
        "| kind | events | changes | runner min | elapsed min | wait min (CI retry; for a conflict, to the next attempt) | cycle min | publication attempts | publication interval min (observed / unresolved) | re-dispatches |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for kind, s in totals["by_kind"].items():
        interval = (
            f"{s['pub_wait_min']} ({s['pub_observed']} / {s['pub_unresolved']})"
            if s["pub_observed"] or s["pub_unresolved"]
            else "n/a"
        )
        lines.append(
            f"| `{kind}` | {s['events']} | {s['changes']} | {s['runner_min']} | {s['elapsed_min']} | {s['wait_min']} | {s['cycle_min']} | {s['attempts']} | {interval} | {s['redispatches']} |"
        )
    lines += [
        "",
        "| artifact outside the census | CI failures | conflicts | changes | cycle min | runner min |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for r in totals["artifacts_outside_census"]:
        lines.append(
            f"| `{r['artifact']}` | {r['ci_failures']} | {r['conflicts']} | {r['changes']} | {r['cycle_min']} | {r['runner_min']} |"
        )

    def category(reason: str) -> str:
        return (
            "without a pull request"
            if reason.startswith("no pull")
            else "whose base lacks a required commit"
            if reason.startswith("base")
            else "with an unfetchable head"
        )

    reasons = collections.Counter(category(x["reason"]) for x in totals["excluded"])
    lines += [
        "",
        f"Examined and excluded from every total: {len(totals['excluded'])} ({'; '.join(f'{v} {k}' for k, v in reasons.items()) or 'none'}); see excluded.tsv.",
    ]
    lines += [
        "",
        f"GitHub: {totals['github']['uncached_calls']} uncached calls, {totals['github']['cache_hits']} cache hits.",
        "",
    ]
    (out / "summary.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, ValueError, KeyError, TypeError, OSError) as failure:
        raise SystemExit(f"repin-cost: {failure!r}; restore the evidence named and re-run") from failure
