"""Render two committed measurements without reading journals, git or GitHub."""

# llmlint: ignore-file[modern_domain_modeling] The totals are a persisted JSON record whose fields `load_totals` checks one by one and whose figures render by key path; a second typed copy of that record could only drift from the producer the journeys feed it from.
from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Any

# Any: parsed JSON, whose shape `load_totals` checks field by field.
Totals = dict[str, Any]
LIVE_RUN = "Close-crozier-s-remaining-Fern-departures-and-unproven-features-and-combinations"
TOP_FIELDS = {
    "changes",
    "changes_with_pr",
    "merged",
    "ci_runs",
    "ci_failed",
    "other_failures",
    "attempts",
    "redispatches",
}
CENSUS_FIELDS = {
    "failures",
    "changes_hit",
    "runner_min",
    "elapsed_min",
    "wait_min",
    "attempts",
    "redispatches",
    "median_cycle_min",
    "ci_retry_unresolved",
    "publications",
    "pub_wait_min",
    "pub_unresolved",
    "pub_observed",
    "median_pub_wait_min",
}
CONFLICT_FIELDS = {"derived", "changes_hit", "wait_min", "median_wait_min", "redispatches", "mixed", "code"}
GITHUB_FIELDS = {"uncached_calls", "cache_hits"}
KIND_FIELDS = {
    "events",
    "changes",
    "runner_min",
    "elapsed_min",
    "wait_min",
    "cycle_min",
    "attempts",
    "redispatches",
    "pub_observed",
    "pub_unresolved",
    "pub_wait_min",
}
ARTIFACT_FIELDS = {"ci_failures", "conflicts", "changes", "cycle_min", "runner_min"}


def numeric_rows(data: Totals, prefix: str = "") -> dict[str, float]:
    rows: dict[str, float] = {}
    for key, value in data.items():
        label = f"{prefix}.{key}" if prefix else key
        match value:
            case bool():
                continue
            case int() | float():
                rows[label] = value
            case dict():
                rows.update(numeric_rows(value, label))
    return rows


def load_totals(path: Path) -> Totals:
    """Reject incomplete or nonnumeric evidence instead of reporting missing cost as zero."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: totals must be an object")
    for group, fields in (("census", CENSUS_FIELDS), ("conflicts", CONFLICT_FIELDS), ("github", GITHUB_FIELDS)):
        if not isinstance(data.get(group), dict) or not fields <= data[group].keys():
            raise ValueError(f"{path}: {group} must hold {sorted(fields)}")
        numbers(path, {field: data[group][field] for field in fields}, group)
    if not data.keys() >= TOP_FIELDS:
        raise ValueError(f"{path}: totals must hold {sorted(TOP_FIELDS)}")
    numbers(path, {field: data[field] for field in TOP_FIELDS}, "totals")
    if not isinstance(data["changes"], int):
        raise ValueError(f"{path}: changes must be an integer")
    if max(data["merged"], data["changes_with_pr"]) > data["changes"]:
        raise ValueError(f"{path}: merged and changes_with_pr cannot exceed changes")
    if not isinstance(data.get("by_kind"), dict):
        raise ValueError(f"{path}: by_kind must be an object")
    for kind, values in data["by_kind"].items():
        if not isinstance(values, dict) or not values.keys() >= KIND_FIELDS:
            raise ValueError(f"{path}: kind {kind!r} must hold {sorted(KIND_FIELDS)}")
        numbers(path, values, kind)
    artifacts = data.get("artifacts_outside_census")
    if not isinstance(artifacts, list):
        raise ValueError(f"{path}: artifacts_outside_census must be a list")
    for artifact in artifacts:
        if not isinstance(artifact, dict) or not isinstance(artifact.get("artifact"), str):
            raise ValueError(f"{path}: malformed artifact record")
        if not artifact.keys() >= ARTIFACT_FIELDS:
            raise ValueError(f"{path}: artifact {artifact['artifact']!r} must hold {sorted(ARTIFACT_FIELDS)}")
        numbers(path, {k: v for k, v in artifact.items() if k != "artifact"}, artifact["artifact"])
    window = data.get("window")
    if (
        not isinstance(window, dict)
        or not all(isinstance(window.get(key), str) and window[key] for key in ("spec", "until"))
        or not isinstance(window.get("base_carries"), list)
        or not all(isinstance(sha, str) and sha for sha in window["base_carries"])
    ):
        raise ValueError(f"{path}: malformed window metadata")
    return data


def numbers(path: Path, values: dict[str, object], label: str) -> None:
    for key, value in values.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
            raise ValueError(f"{path}: {label}.{key} must be a finite nonnegative number")


def reference_rates(baseline: Path, totals: Totals) -> list[tuple[str, float | None]]:
    """Census failures per change the after sample is read against, both from the baseline given."""
    with (baseline / "changes.tsv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if any("census_failures" not in row or "runs" not in row for row in rows):
        raise ValueError(f"{baseline}/changes.tsv: needs census_failures and runs columns")
    live = [row for row in rows if LIVE_RUN in row["runs"].split(";")]
    return [
        ("pooled baseline", totals["census"]["failures"] / totals["changes"] if totals["changes"] else None),
        ("live run baseline", sum(int(row["census_failures"]) for row in live) / len(live) if live else None),
    ]


def comparison(baseline: Path, after: Path) -> str:
    before = load_totals(baseline / "totals.json")
    current = load_totals(after / "totals.json")
    with (after / "changes.tsv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if not reader.fieldnames or "pr" not in reader.fieldnames:
            raise ValueError(f"{after}/changes.tsv: missing pr column")
        records = list(reader)
        if len(records) != current["changes"] or any(
            not row["pr"] or not row["pr"].isdigit() or int(row["pr"]) < 1 for row in records
        ):
            raise ValueError(f"{after}/changes.tsv: PR rows must match totals.changes and contain positive PR numbers")
        prs = [f"#{row['pr']}" for row in records]
    n, m = before["changes"], current["changes"]
    window = current["window"]
    lines = [
        "# Repin cost after the incremental census tooling",
        "",
        f"{'Provisional' if m < 5 else 'Measured'} comparison: {m} after-sample changes; {n} baseline changes.",
        "No reduction can be inferred from an empty sample."
        if not m
        else "Cycle intervals include other work and queueing; they do not establish causation.",
        "",
        f"After-sample PRs: {', '.join(prs) or 'none'}.",
        f"Landing commits: {', '.join(window['base_carries']) or 'not a base-carries window'}.",
        f"Cutoff: {window['until']}.",
        "",
        "```sh",
        f'python3 tools/repin-cost/repin_cost.py --window {window["spec"]} --runs-root "$ONEPIPELINE_RUNS_DIR" --until {window["until"]} --out tools/repin-cost/after',
        "python3 tools/repin-cost/repin_cost.py compare tools/repin-cost/baseline tools/repin-cost/after",
        "```",
        "",
        "Differences are after minus baseline. Per-change denominators are all eligible changes, including those with no repin.",
        "An empty sample has undefined per-change rates (n/a). Unresolved intervals remain excluded from minute sums and medians.",
        "Kind counts overlap when a failure names several kinds; its minutes are split evenly, as in the baseline.",
        "Medians and changes-hit counts are also shown per eligible change for completeness; median totals retain their original meaning.",
        "",
        "| figure | baseline total | baseline / change | after total | after / change | difference total | difference / change |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    excluded = {"window", "github", "excluded", "by_kind", "rewrote", "artifacts_outside_census"}

    def figures(data: Totals) -> dict[str, float]:
        rows = numeric_rows({k: v for k, v in data.items() if k not in excluded})
        rows["census.cycle_min"] = data["census"]["elapsed_min"] + data["census"]["wait_min"]
        rows["census_and_conflict_redispatches"] = data["census"]["redispatches"] + data["conflicts"]["redispatches"]
        rows.update(numeric_rows(data["by_kind"], "kind"))
        for artifact in data["artifacts_outside_census"]:
            rows.update(
                numeric_rows({k: v for k, v in artifact.items() if k != "artifact"}, "artifact." + artifact["artifact"])
            )
        return rows

    left, right = figures(before), figures(current)
    for label in sorted(left.keys() | right.keys()):
        a, b = left.get(label, 0), right.get(label, 0)
        ar, br = f"{a / n:.2f}" if n else "n/a", f"{b / m:.2f}" if m else "n/a"
        delta = f"{b / m - a / n:+.2f}" if n and m else "n/a"
        lines.append(f"| `{label}` | {a:.2f} | {ar} | {b:.2f} | {br} | {b - a:+.2f} | {delta} |")
    rate = current["census"]["failures"] / m if m else None
    references = reference_rates(baseline, before)
    lines += [
        "",
        "| census failures / change reference | reference | after | difference |",
        "| --- | ---: | ---: | ---: |",
    ]
    for label, reference in references:
        shown = f"{rate:.2f}" if rate is not None else "n/a"
        known = f"{reference:.2f}" if reference is not None else "n/a"
        delta = f"{rate - reference:+.2f}" if rate is not None and reference is not None else "n/a"
        lines.append(f"| {label} | {known} | {shown} | {delta} |")
    lines += [
        "",
        f"After measurement GitHub quota: {current['github']['uncached_calls']} uncached core REST calls; {current['github']['cache_hits']} cache hits.",
        "The dispatch-wide quota and baseline-cache verification are recorded in the hand-counted evidence below.",
        "",
    ]
    return "\n".join(lines) + "\n"
