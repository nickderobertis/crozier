"""Render two committed measurements without reading journals, git or GitHub."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Any


def numeric_rows(data: dict[str, Any], prefix: str = "") -> dict[str, float]:
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


def load_totals(path: Path) -> dict[str, Any]:
    """Reject incomplete or nonnumeric evidence instead of reporting missing cost as zero."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: totals must be an object")
    required = {
        "census": {"failures", "elapsed_min", "wait_min", "redispatches"},
        "conflicts": {"redispatches"},
        "github": {"uncached_calls", "cache_hits"},
        "window": {"spec", "until", "base_carries"},
        "by_kind": set(),
    }
    for group, keys in required.items():
        if not isinstance(data.get(group), dict) or not keys <= data[group].keys():
            raise ValueError(f"{path}: missing or malformed {group} fields: {sorted(keys)}")

    def numbers(values: dict, label: str) -> None:
        for key, value in values.items():
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                raise ValueError(f"{path}: {label}.{key} must be a finite nonnegative number")

    if not isinstance(data.get("changes"), int) or isinstance(data["changes"], bool) or data["changes"] < 0:
        raise ValueError(f"{path}: changes must be a nonnegative integer")
    for group in ("census", "conflicts", "github"):
        numbers(data[group], group)
    ignored = {"census", "conflicts", "github", "window", "by_kind", "artifacts_outside_census", "excluded", "rewrote"}
    numbers({k: v for k, v in data.items() if k not in ignored}, "totals")
    for kind, values in data["by_kind"].items():
        if not isinstance(kind, str) or not isinstance(values, dict):
            raise ValueError(f"{path}: malformed repin kind")
        numbers(values, kind)
    artifacts = data.get("artifacts_outside_census")
    if not isinstance(artifacts, list):
        raise ValueError(f"{path}: artifacts_outside_census must be a list")
    for artifact in artifacts:
        if not isinstance(artifact, dict) or not isinstance(artifact.get("artifact"), str):
            raise ValueError(f"{path}: malformed artifact record")
        numbers({k: v for k, v in artifact.items() if k != "artifact"}, artifact["artifact"])
    window = data["window"]
    if (
        not all(isinstance(window[key], str) and window[key] for key in ("spec", "until"))
        or not isinstance(window["base_carries"], list)
        or not all(isinstance(sha, str) and sha for sha in window["base_carries"])
    ):
        raise ValueError(f"{path}: malformed window metadata")
    return data


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

    def figures(data: dict[str, Any]) -> dict[str, float]:
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
    lines += [
        "",
        "| census failures / change reference | reference | after | difference |",
        "| --- | ---: | ---: | ---: |",
    ]
    for label, reference in (("pooled baseline", 0.58), ("live run baseline", 1.86)):
        shown = f"{rate:.2f}" if rate is not None else "n/a"
        delta = f"{rate - reference:+.2f}" if rate is not None else "n/a"
        lines.append(f"| {label} | {reference:.2f} | {shown} | {delta} |")
    lines += [
        "",
        f"After measurement GitHub quota: {current['github']['uncached_calls']} uncached core REST calls; {current['github']['cache_hits']} cache hits.",
        "The dispatch-wide quota and baseline-cache verification are recorded in the hand-counted evidence below.",
        "",
    ]
    return "\n".join(lines) + "\n"
