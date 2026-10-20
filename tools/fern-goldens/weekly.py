#!/usr/bin/env python3
"""The weekly Fern goldens run: check the newest Fern against every committed
Fern reference crozier byte-matches against, and propose what changed.

`.github/workflows/fern-goldens.yml` is a thin sequence of these phases, each a
job of its own, so every decision lives here where the tests drive it:

  resolve   the pair to check: the newest stable Fern CLI (npm `fern-api`) and
            `fernapi/fern-python-sdk` tag, or the exact versions a dispatch
            pins; a complete run of a pair already checked, or of the certified
            pair, ends green here and changes nothing
  plan      every family `fern-references.py list` names (or a dispatch's
            subset), grouped into units that must generate together and packed
            into the fewest shards whose predicted generation time fits the
            weekly budget with a margin, from `generation-seconds.tsv`
  shard     one shard's items, each through `fern-references.py generate`, with
            `metadata.json` at the candidate pair; per item its seconds, its log,
            its outcome and the files it wrote
  assemble  every shard's result combined into one bundle, or red when a shard is
            missing, an item is unaccounted for, failed, or two shards wrote one
            file
  apply     the bundle laid over a checkout of the planned commit, with every
            statement of the pair restated, so the tree is the one a pull request
            would carry
  decide    crozier's own comparison over that tree, through the gates
            `decision-gates.tsv` names, and nothing else: match, diff, or red when
            a comparison cannot run
  publish   the one pull request on `fern-goldens/update`, reconciled with what
            the remote already holds: a diff stays open for a person; a match
            records the pair in `tests/fixtures/fern-pair-checks.tsv` and is
            auto-merged

Each phase prints one line and appends its Markdown to `--summary` (the step
summary). Exit status: 0 when the phase finished (a diff is a finished
decision), 1 when it found a failure (each named on stderr and in the summary),
2 on a usage error. See docs/fern-goldens.md.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import importlib.machinery
import importlib.util
import json
import math
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from collections.abc import Iterable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType
from typing import Any

ROOT_ENV = "CROZIER_FERN_WEEKLY_ROOT"
METADATA = Path("assets/scaffolding/metadata.json")
TIMINGS = Path("tools/fern-goldens/generation-seconds.tsv")
TIMINGS_HEADER = ("family", "item", "seconds")
TIMINGS_NOTE = (
    "# Seconds each Fern reference took to regenerate, per family and item, as the weekly\n"
    "# Fern goldens run last measured them (tools/fern-goldens/weekly.py `assemble` writes\n"
    "# it back). Seeded from run 38208782203 (2026-10-12), which recorded no per-item time:\n"
    "# its 3,590-second generation step over 222 trees, so 16.2 s a tree. The planner gives\n"
    "# an item with no row the mean of the corpus rows.\n"
)
GATES = Path("tools/fern-goldens/decision-gates.tsv")
GATES_HEADER = ("family", "scope", "verdict", "command")
CHECKS = Path("tests/fixtures/fern-pair-checks.tsv")
CHECKS_HEADER = ("fern_cli_version", "fern_python_sdk_version", "checked_on", "outcome")
FERN_GOLDENS_REPORT = Path(".local/fern-goldens")
FERN_REFERENCES_LOGS = Path(".local/fern-references")
NPM_URL = "https://registry.npmjs.org/fern-api"
BRANCH = "fern-goldens/update"
LABEL = "fern-goldens"
BASE = "main"
SCHEMA_VERSION = 1

# The budget the planner sizes shards against: `crozier-fern-goldens-weekly-minutes`
# in `.github/budgets.yaml`, whose test holds the two equal.
BUDGET_MINUTES = 180.0
# The share of what the budget leaves for generation that a shard may predict
# to use, so a slower week than the timing table records still fits.
SHARD_MARGIN = 0.25
# Run 38208782203 (2026-10-12): job start to its generation step took 3.6
# minutes (checkout, toolchains, a release crozier build); every job pays it.
JOB_SETUP_MINUTES = 4.0
PLAN_MINUTES = 1.0
ASSEMBLY_MINUTES = 2.0
# Estimated, not measured: a crozier build and its golden gates over the tree.
DECISION_MINUTES = 30.0
PUBLISH_MINUTES = 1.0
# GitHub-hosted runners stop a job at 6 hours; a shard's timeout-minutes sits
# inside it, and no shard is planned past the timeout.
SHARD_TIMEOUT_MINUTES = 300.0
# A free-plan public repository runs at most 20 jobs at once.
CONCURRENT_JOBS = 20
# The same run generated 222 trees (218 packaged + 4 flat) in 3,590 seconds of
# its generation step: the rate an item no run has timed yet is planned at,
# until the table holds corpus timings of its own.
SEED_SECONDS_PER_GENERATION = 3590.0 / 222

VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+")
NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]*")
STATUS_OK = "ok"
STATUS_KNOWN = "known-upstream-failure"
STATUS_UNFETCHABLE = "spec-unfetchable"
STATUS_FAILED = "failed"
REPORT_LIMIT = 6000
BODY_LIMIT = 60000


class WeeklyError(RuntimeError):
    """A failure this phase names, with what to do about it."""


@dataclass(frozen=True)
class Pair:
    cli: str
    generator: str

    def label(self) -> str:
        return f"Fern CLI {self.cli} / fern-python-sdk {self.generator}"


def root() -> Path:
    return Path(os.environ.get(ROOT_ENV) or Path(__file__).resolve().parents[2]).resolve()


def run(
    argv: Sequence[str],
    cwd: Path,
    env: dict[str, str] | None = None,
    *,
    check: bool = False,
    binary: bool = False,
) -> subprocess.CompletedProcess[Any]:
    environment = {**(os.environ if env is None else env), "PYTHONUTF8": "1"}
    try:
        if binary:
            result = subprocess.run(list(argv), cwd=cwd, env=environment, capture_output=True, check=False)
        else:
            result = subprocess.run(
                list(argv),
                cwd=cwd,
                env=environment,
                capture_output=True,
                check=False,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
    except OSError as error:
        raise WeeklyError(f"could not run {argv[0]!r}: {error}; install it, then re-run") from error
    if check and result.returncode != 0:
        detail = result.stderr if isinstance(result.stderr, str) else result.stderr.decode("utf-8", "replace")
        raise WeeklyError(f"`{' '.join(argv)}` exited {result.returncode}: {detail.strip()[-2000:]}")
    return result


def git(base: Path, *args: str, check: bool = True) -> str:
    return run(["git", "-C", str(base), *args], base, check=check).stdout.strip()


def load_module(name: str, path: Path) -> ModuleType:
    loader = importlib.machinery.SourceFileLoader(name, str(path))
    spec = importlib.util.spec_from_loader(name, loader)
    if spec is None:
        raise WeeklyError(f"cannot load {path}; restore it with git checkout")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    loader.exec_module(module)
    return module


def references(base: Path) -> ModuleType:
    """`fern-references.py` over `base`: the per-family recipe whose item lists
    and case tables the planner reads rather than re-parses."""
    os.environ["CROZIER_FERN_REFERENCES_ROOT"] = str(base)
    return load_module("fern_references", base / "tools/fern-goldens/fern-references.py")


def read_tsv(path: Path, header: tuple[str, ...]) -> list[dict[str, str]]:
    try:
        lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line and not line.startswith("#")]
    except OSError as error:
        raise WeeklyError(f"cannot read {path} ({error}); restore it with git checkout") from error
    if not lines or tuple(lines[0].split("\t")) != header:
        raise WeeklyError(f"{path} must open with the header {' '.join(header)}; restore it with git checkout")
    rows = []
    for number, line in enumerate(lines[1:], start=2):
        cells = line.split("\t")
        if len(cells) != len(header):
            raise WeeklyError(f"{path} row {number} has {len(cells)} cells for {len(header)} columns")
        rows.append(dict(zip(header, cells, strict=True)))
    return rows


def write_tsv(path: Path, header: tuple[str, ...], rows: Iterable[Sequence[str]], note: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        note + "\t".join(header) + "\n" + "".join("\t".join(row) + "\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )


def certified(base: Path) -> Pair:
    try:
        record = json.loads((base / METADATA).read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise WeeklyError(f"cannot read {METADATA} ({error}); restore it with git checkout -- {METADATA}") from error
    cli, generator = record.get("cliVersion"), record.get("generatorVersion")
    if not (isinstance(cli, str) and isinstance(generator, str)):
        raise WeeklyError(f"{METADATA} names no cliVersion and generatorVersion; restore it with git checkout")
    return Pair(cli, generator)


def set_pair(base: Path, pair: Pair) -> None:
    """Move `metadata.json`, the pair's one declaration, to `pair`."""
    path = base / METADATA
    record = json.loads(path.read_text(encoding="utf-8"))
    record["cliVersion"], record["generatorVersion"] = pair.cli, pair.generator
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8", newline="\n")


def summarize(path: str | None, lines: Iterable[str]) -> None:
    if path:
        with open(path, "a", encoding="utf-8", newline="\n") as handle:
            handle.write("\n".join(lines) + "\n\n")


def write_outputs(path: str | None, values: dict[str, str]) -> None:
    if path:
        with open(path, "a", encoding="utf-8", newline="\n") as handle:
            handle.write("".join(f"{key}={value}\n" for key, value in values.items()))


# ---------------------------------------------------------------- resolve


def stable(version: str) -> bool:
    return VERSION.fullmatch(version) is not None


def semantic(version: str) -> tuple[int, int, int]:
    major, minor, patch = version.split(".")
    return int(major), int(minor), int(patch)


def newest_cli(base: Path) -> str:
    """The newest stable `fern-api` version npm publishes."""
    fetched = run(["curl", "-fsSL", NPM_URL], base)
    if fetched.returncode != 0:
        raise WeeklyError(f"could not read {NPM_URL}: {fetched.stderr.strip() or fetched.returncode}; re-run later")
    try:
        versions = json.loads(fetched.stdout).get("versions", {})
    except (ValueError, AttributeError) as error:
        raise WeeklyError(f"{NPM_URL} returned no package document ({error}); re-run later") from error
    found = [version for version in versions if isinstance(version, str) and stable(version)]
    if not found:
        raise WeeklyError(f"{NPM_URL} lists no stable fern-api version")
    return max(found, key=semantic)


def newest_generator(base: Path) -> str:
    """The newest stable `fernapi/fern-python-sdk` tag, as `fern-goldens` resolves it."""
    tool = load_module("fern_goldens", base / "tools/fern-goldens/fern-goldens")
    try:
        return tool.resolve_latest_version(base)
    except tool.GoldensError as error:
        raise WeeklyError(str(error)) from error


def checked_pairs(base: Path) -> dict[Pair, str]:
    path = base / CHECKS
    if not path.is_file():
        return {}
    return {
        Pair(row["fern_cli_version"], row["fern_python_sdk_version"]): row["checked_on"]
        for row in read_tsv(path, CHECKS_HEADER)
    }


def parse_selectors(spec: str) -> list[tuple[str, str | None]]:
    """A dispatch's subset: comma-separated `family` or `family:item`."""
    selectors: list[tuple[str, str | None]] = []
    for part in (part.strip() for part in spec.split(",")):
        if not part:
            continue
        family, colon, item = part.partition(":")
        if not NAME.fullmatch(family) or (colon and not NAME.fullmatch(item)):
            raise WeeklyError(f"items selector {part!r} is no `family` or `family:item`")
        selectors.append((family, item if colon else None))
    return selectors


def resolve(args: argparse.Namespace) -> int:
    base = root()
    selectors = parse_selectors(args.items)
    complete = not selectors
    if complete and args.ref != f"refs/heads/{BASE}":
        raise WeeklyError(
            f"a run over the whole inventory publishes, so it runs from refs/heads/{BASE}, not {args.ref}; "
            "pass `items` for a diagnostic run on a branch"
        )
    for name, value in (("--cli-version", args.cli_version), ("--generator-version", args.generator_version)):
        if value and not stable(value):
            raise WeeklyError(f"{name} {value!r} is no exact stable version (MAJOR.MINOR.PATCH)")
    pair = Pair(args.cli_version or newest_cli(base), args.generator_version or newest_generator(base))
    current = certified(base)
    checked = checked_pairs(base)
    reason = ""
    if complete and pair == current:
        reason = f"{pair.label()} is the certified pair already; nothing to check"
    elif complete and pair in checked:
        reason = f"{pair.label()} was checked on {checked[pair]} and crozier matched it; nothing to check"
    if complete and not reason and not args.token_present:
        raise WeeklyError(
            "RELEASE_PLZ_TOKEN is not set, so no pull request could be opened from this run; add the secret "
            "(a PAT whose pull requests trigger crozier's required checks; see docs/fern-goldens.md), then re-run"
        )
    write_outputs(
        args.github_output,
        {
            "run": "false" if reason else "true",
            "complete": "true" if complete else "false",
            "cli": pair.cli,
            "generator": pair.generator,
            "items": args.items,
        },
    )
    scope = "the whole reference inventory" if complete else f"the diagnostic subset `{args.items}`"
    line = reason or f"Checking {pair.label()} over {scope} (certified: {current.label()})."
    summarize(args.summary, ["## Fern goldens: pair", "", line])
    print(f"fern-goldens-weekly: {line}")
    return 0


# ---------------------------------------------------------------- plan


@dataclass
class Item:
    family: str
    item: str
    seconds: float

    def key(self) -> str:
        return f"{self.family}\t{self.item}"


def inventory(base: Path) -> dict[str, list[str]]:
    """Every family's items, as `fern-references.py list` names them: the same
    listing functions, called in this process rather than once per family."""
    module = references(base)
    found = {}
    for family, entry in module.FAMILY.items():
        try:
            found[family] = list(entry.list())
        except (SystemExit, module.ReferenceError, OSError) as error:
            raise WeeklyError(f"`fern-references.py list {family}` failed: {error}") from error
    return found


def select(found: dict[str, list[str]], selectors: list[tuple[str, str | None]]) -> dict[str, list[str]]:
    if not selectors:
        return found
    chosen: dict[str, list[str]] = {}
    for family, item in selectors:
        if family not in found:
            raise WeeklyError(f"no reference family {family!r}; the families are {', '.join(found)}")
        if item is not None and item not in found[family]:
            raise WeeklyError(f"no {family} item {item!r}; `fern-references.py list {family}` names the family")
        wanted = found[family] if item is None else [item]
        chosen[family] = sorted({*chosen.get(family, []), *wanted}, key=found[family].index)
    return {family: chosen[family] for family in found if family in chosen}


def timings(base: Path) -> tuple[dict[tuple[str, str], float], float]:
    """The recorded seconds per item, and the corpus rate an untimed item gets."""
    path = base / TIMINGS
    rows = read_tsv(path, TIMINGS_HEADER) if path.is_file() else []
    table: dict[tuple[str, str], float] = {}
    for row in rows:
        try:
            seconds = float(row["seconds"])
        except ValueError as error:
            raise WeeklyError(f"{TIMINGS} row {row['family']} {row['item']}: seconds is no number") from error
        if seconds < 0:
            raise WeeklyError(f"{TIMINGS} row {row['family']} {row['item']}: seconds is negative")
        table[(row["family"], row["item"])] = seconds
    corpus = [seconds for (family, _item), seconds in table.items() if family == "corpus"]
    return table, (sum(corpus) / len(corpus) if corpus else SEED_SECONDS_PER_GENERATION)


class Units:
    """Items that must generate in one shard, in order: an overlay after the
    golden it is reduced against, a measurement after the hand-written tree it
    overlays, and every item of a family that rewrites one shared table."""

    def __init__(self, keys: Iterable[str]) -> None:
        self.parent = {key: key for key in keys}

    def find(self, key: str) -> str:
        while self.parent[key] != key:
            self.parent[key] = self.parent[self.parent[key]]
            key = self.parent[key]
        return key

    def join(self, first: str, second: str) -> None:
        if first in self.parent and second in self.parent:
            self.parent[self.find(second)] = self.find(first)


# Families every item of which rewrites one table: `probes` the probe
# MANIFEST.tsv, `refusals` classes.tsv and findings.tsv.
SHARED_TABLE_FAMILIES = ("probes", "refusals")


def units(base: Path, chosen: dict[str, list[str]]) -> list[list[str]]:
    module = references(base)
    keys = [f"{family}\t{item}" for family, items in chosen.items() for item in items]
    grouped = Units(keys)
    for family in SHARED_TABLE_FAMILIES:
        items = chosen.get(family, [])
        for item in items[1:]:
            grouped.join(f"{family}\t{items[0]}", f"{family}\t{item}")
    for item in chosen.get("overlays", []):
        grouped.join(f"corpus\t{item.partition('/')[0]}", f"overlays\t{item}")
    measurements = chosen.get("measurements", [])
    if measurements:
        handwritten = (base / module.HANDWRITTEN).resolve()
        measured = (base / module.MEASUREMENTS).resolve()
        try:
            rows = module.cases()
        except module.ReferenceError as error:
            raise WeeklyError(str(error)) from error
        literals = [item for item in measurements if item.startswith("parameter-literals/")]
        for item in literals:
            # One shared certified-trees.json, and each case reads its hand-written tree.
            grouped.join(f"measurements\t{literals[0]}", f"measurements\t{item}")
            grouped.join(f"handwritten\t{item.removeprefix('parameter-literals/')}", f"measurements\t{item}")
        for item in measurements:
            row = rows.get(item)
            overlay = row.overlay.base.resolve() if row is not None and row.overlay and row.overlay.base else None
            if overlay is None:
                continue
            if overlay.is_relative_to(handwritten):
                grouped.join(f"handwritten\t{overlay.relative_to(handwritten).parts[0]}", f"measurements\t{item}")
            elif overlay.is_relative_to(measured):
                inner = overlay.relative_to(measured).as_posix()
                owner = max((case for case in rows if inner.startswith(f"{case}/")), key=len, default=None)
                if owner is not None:
                    grouped.join(f"measurements\t{owner}", f"measurements\t{item}")
    order = {key: index for index, key in enumerate(keys)}
    members: dict[str, list[str]] = {}
    for key in keys:
        members.setdefault(grouped.find(key), []).append(key)
    return sorted((sorted(group, key=order.__getitem__) for group in members.values()), key=lambda g: order[g[0]])


def overhead_minutes() -> float:
    """Every minute of a run that is not a shard's generation: each job's
    setup, the plan, a shard's own setup, the assembly, decision and publication."""
    jobs = 4  # plan, assemble, decide, publish
    return (
        jobs * JOB_SETUP_MINUTES + PLAN_MINUTES + ASSEMBLY_MINUTES + DECISION_MINUTES + PUBLISH_MINUTES
    ) + JOB_SETUP_MINUTES


def shard_limit_seconds() -> float:
    """The most generation one shard may predict: what the budget leaves after
    the overhead, less the margin, and inside the shard's job timeout."""
    budgeted = (BUDGET_MINUTES - overhead_minutes()) * (1 - SHARD_MARGIN)
    return 60 * min(budgeted, SHARD_TIMEOUT_MINUTES - JOB_SETUP_MINUTES)


def pack(weights: list[float], count: int) -> list[list[int]]:
    """Longest-processing-time packing of `weights` into `count` bins."""
    bins: list[list[int]] = [[] for _ in range(count)]
    loads = [0.0] * count
    for index in sorted(range(len(weights)), key=lambda i: (-weights[i], i)):
        target = min(range(count), key=lambda b: (loads[b], b))
        bins[target].append(index)
        loads[target] += weights[index]
    return [sorted(group) for group in bins if group]


def shard_count(weights: list[float], limit: float) -> tuple[int, list[list[int]]]:
    """The fewest bins whose every load fits `limit`: never fewer than the
    total over the limit allows, one more each time the packing overflows, and
    one bin per unit at most (a unit alone past the limit cannot be split)."""
    if not weights:
        return 0, []
    count = max(1, math.ceil(sum(weights) / limit))
    while True:
        bins = pack(weights, count)
        if max(sum(weights[i] for i in group) for group in bins) <= limit or count >= len(weights):
            return len(bins), bins
        count += 1


def wall_clock(shard_seconds: list[float]) -> dict[str, Any]:
    """The run's predicted minutes, start to pull request: the plan job, the
    shards in waves of the concurrent-job allowance, then assembly, decision
    and publication, each with its job setup."""
    minutes = sorted((JOB_SETUP_MINUTES + seconds / 60 for seconds in shard_seconds), reverse=True)
    waves = [minutes[start : start + CONCURRENT_JOBS] for start in range(0, len(minutes), CONCURRENT_JOBS)]
    shards = sum(wave[0] for wave in waves)
    stages = {
        "plan": JOB_SETUP_MINUTES + PLAN_MINUTES,
        "shards": shards,
        "assembly": JOB_SETUP_MINUTES + ASSEMBLY_MINUTES,
        "decision": JOB_SETUP_MINUTES + DECISION_MINUTES,
        "publication": JOB_SETUP_MINUTES + PUBLISH_MINUTES,
    }
    return {
        "minutes": round(sum(stages.values()), 2),
        "stages": {name: round(value, 2) for name, value in stages.items()},
        "waves": len(waves),
        "setup_minutes_per_job": JOB_SETUP_MINUTES,
        "assembly_minutes": round(stages["assembly"], 2),
        "longest_shard_minutes": round(minutes[0], 2) if minutes else 0.0,
    }


def make_plan(base: Path, items: str, pair: Pair | None) -> dict[str, Any]:
    chosen = select(inventory(base), parse_selectors(items))
    table, default = timings(base)
    weights = {
        f"{family}\t{item}": table.get((family, item), default)
        for family, entries in chosen.items()
        for item in entries
    }
    grouped = units(base, chosen)
    limit = shard_limit_seconds()
    _, bins = shard_count([sum(weights[key] for key in unit) for unit in grouped], limit)
    shards = []
    shard_seconds: list[float] = []
    for index, group in enumerate(bins):
        members = [key for unit in (grouped[i] for i in group) for key in unit]
        seconds = sum(weights[key] for key in members)
        shard_seconds.append(seconds)
        shards.append(
            {
                "index": index,
                "seconds": round(seconds, 1),
                "minutes": round(JOB_SETUP_MINUTES + seconds / 60, 2),
                "items": [
                    {"family": key.split("\t")[0], "item": key.split("\t")[1], "seconds": round(weights[key], 1)}
                    for key in members
                ],
            }
        )
    families = {
        family: {
            "items": len(entries),
            "seconds": round(sum(weights[f"{family}\t{item}"] for item in entries), 1),
        }
        for family, entries in chosen.items()
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "complete": not parse_selectors(items),
        "items": items,
        "base": git(base, "rev-parse", "HEAD", check=False) or None,
        "pair": {"cli": pair.cli, "generator": pair.generator} if pair else None,
        "budget_minutes": BUDGET_MINUTES,
        "shard_limit_minutes": round(limit / 60, 2),
        "default_seconds": round(default, 2),
        "families": families,
        "units": len(grouped),
        "shards": shards,
        "estimate": wall_clock(shard_seconds),
    }


def plan(args: argparse.Namespace) -> int:
    base = root()
    pair = Pair(args.cli, args.generator) if args.cli and args.generator else None
    made = make_plan(base, args.items, pair)
    text = json.dumps(made, indent=2) + "\n"
    for destination in (args.output, args.telemetry):
        if destination:
            Path(destination).parent.mkdir(parents=True, exist_ok=True)
            Path(destination).write_text(text, encoding="utf-8", newline="\n")
    count = len(made["shards"])
    write_outputs(args.github_output, {"matrix": json.dumps({"shard": list(range(count))}), "shards": str(count)})
    total = sum(family["items"] for family in made["families"].values())
    estimate = made["estimate"]
    summarize(
        args.summary,
        [
            "## Fern goldens: plan",
            "",
            f"{total} item(s) in {made['units']} unit(s), {count} shard(s) of at most "
            f"{made['shard_limit_minutes']} generation minutes; predicted {estimate['minutes']} minutes "
            f"start to pull request (budget {BUDGET_MINUTES:g}).",
            "",
            "| family | items | predicted seconds |",
            "|---|---:|---:|",
            *(f"| {name} | {family['items']} | {family['seconds']} |" for name, family in made["families"].items()),
        ],
    )
    print(f"fern-goldens-weekly: planned {total} item(s) in {count} shard(s), {estimate['minutes']} minutes predicted")
    return 0


def read_json(path: Path, what: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise WeeklyError(f"cannot read the {what} {path} ({error})") from error


def read_plan(path: Path) -> dict[str, Any]:
    made = read_json(path, "plan")
    if not isinstance(made, dict) or made.get("schema_version") != SCHEMA_VERSION or not made.get("pair"):
        raise WeeklyError(f"{path} is no plan of this tool's schema naming a pair; re-run the plan job")
    return made


def plan_pair(made: dict[str, Any]) -> Pair:
    return Pair(made["pair"]["cli"], made["pair"]["generator"])


# ---------------------------------------------------------------- shard


def blob(base: Path, path: str) -> bytes | None:
    """`path`'s committed bytes, or None when HEAD has no such file."""
    shown = run(["git", "-C", str(base), "cat-file", "blob", f"HEAD:{path}"], base, binary=True)
    return shown.stdout if shown.returncode == 0 else None


def dirty(base: Path) -> dict[str, str | None]:
    """Every path that differs from HEAD, to its content digest (None when deleted)."""
    listed = run(["git", "-C", str(base), "status", "--porcelain=v1", "-z", "--untracked-files=all"], base, check=True)
    found: dict[str, str | None] = {}
    for entry in listed.stdout.split("\0"):
        if len(entry) > 3:
            path = entry[3:]
            target = base / path
            found[path] = digest(target.read_bytes()) if target.is_file() else None
    return found


def digest(data: bytes | None) -> str | None:
    return None if data is None else hashlib.sha256(data).hexdigest()


def changed_between(base: Path, before: dict[str, str | None], after: dict[str, str | None]) -> list[str]:
    paths = []
    for path in sorted({*before, *after}):
        was = before[path] if path in before else digest(blob(base, path))
        target = base / path
        now = digest(target.read_bytes()) if target.is_file() else None
        if was != now:
            paths.append(path)
    return paths


def listed_fixtures(path: Path) -> list[str]:
    try:
        return [line.split("\t")[0] for line in path.read_text(encoding="utf-8").splitlines() if line]
    except OSError:
        return []


def delegate_logs(base: Path, since: float) -> list[Path]:
    """The logs the recipe and its delegates wrote while one item generated."""
    found = []
    for directory in (base / FERN_REFERENCES_LOGS, base / FERN_GOLDENS_REPORT / "generation-logs"):
        if directory.is_dir():
            found += [path for path in directory.rglob("*") if path.is_file() and path.stat().st_mtime >= since]
    return sorted(found)


def safe_name(item: str) -> str:
    return item.replace("/", "__")


def generate_item(base: Path, family: str, item: str, logs: Path) -> dict[str, Any]:
    environment = dict(os.environ, CROZIER_FERN_REFERENCES_ROOT=str(base), CROZIER_FERN_GOLDENS_ROOT=str(base))
    before = dirty(base)
    started_wall, started = time.time() - 1, time.monotonic()
    result = run(
        [sys.executable, str(base / "tools/fern-goldens/fern-references.py"), "generate", family, item],
        base,
        environment,
    )
    seconds = time.monotonic() - started
    log = logs / family / f"{safe_name(item)}.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    parts = [f"$ fern-references.py generate {family} {item}\nexit {result.returncode}\n{result.stdout}{result.stderr}"]
    for path in delegate_logs(base, started_wall):
        parts.append(
            f"\n=== {path.relative_to(base).as_posix()} ===\n{path.read_text(encoding='utf-8', errors='replace')}"
        )
    log.write_text("".join(parts), encoding="utf-8", newline="\n")
    status, detail = STATUS_OK, ""
    known = listed_fixtures(base / FERN_GOLDENS_REPORT / "known-upstream-failures.txt")
    if result.returncode != 0:
        fetch = base / FERN_GOLDENS_REPORT / "fetch-failures.txt"
        unfetchable = (
            {
                line.split("\t")[0]: line.partition("\t")[2]
                for line in fetch.read_text(encoding="utf-8").splitlines()
                if line
            }
            if family == "corpus" and fetch.is_file()
            else {}
        )
        if item in unfetchable:
            status, detail = STATUS_UNFETCHABLE, unfetchable[item]
        else:
            status = STATUS_FAILED
            detail = (result.stderr.strip() or result.stdout.strip() or f"exit {result.returncode}").splitlines()[-1]
    elif family == "corpus" and item in known:
        status, detail = STATUS_KNOWN, "the exact known upstream Fern failure, reproduced"
    return {
        "family": family,
        "item": item,
        "status": status,
        "detail": detail,
        "seconds": round(seconds, 1),
        "changed": changed_between(base, before, dirty(base)),
        "log": log.relative_to(logs.parent).as_posix(),
    }


def shard(args: argparse.Namespace) -> int:
    base = root()
    made = read_plan(Path(args.plan))
    shards = made["shards"]
    if not 0 <= args.index < len(shards):
        raise WeeklyError(f"the plan has {len(shards)} shard(s), not index {args.index}")
    pair = plan_pair(made)
    output = Path(args.output).resolve()
    if output.exists():
        shutil.rmtree(output)
    (output / "files").mkdir(parents=True)
    set_pair(base, pair)
    results = [
        generate_item(base, entry["family"], entry["item"], output / "logs") for entry in shards[args.index]["items"]
    ]
    written = sorted({path for result in results for path in result["changed"]})
    deleted = []
    for path in written:
        source = base / path
        if source.is_file():
            target = output / "files" / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        else:
            deleted.append(path)
    record = {
        "schema_version": SCHEMA_VERSION,
        "index": args.index,
        "pair": made["pair"],
        "base": made["base"],
        "items": results,
        "written": [path for path in written if path not in deleted],
        "deleted": deleted,
    }
    (output / "result.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8", newline="\n")
    failed = [result for result in results if result["status"] == STATUS_FAILED]
    counts = {
        status: sum(r["status"] == status for r in results)
        for status in (STATUS_OK, STATUS_KNOWN, STATUS_UNFETCHABLE, STATUS_FAILED)
    }
    summarize(
        args.summary,
        [
            f"## Fern goldens: shard {args.index}",
            "",
            f"{len(results)} item(s) at {pair.label()}: "
            + ", ".join(f"{count} {status}" for status, count in counts.items()),
            *(
                f"- {r['family']} `{r['item']}`: {r['status']}: {r['detail']}"
                for r in results
                if r["status"] != STATUS_OK
            ),
        ],
    )
    print(f"fern-goldens-weekly: shard {args.index}: {len(results)} item(s), {len(failed)} failed")
    for result in failed:
        print(f"{result['family']} {result['item']}: {result['detail']} (log {result['log']})", file=sys.stderr)
    return 1 if failed else 0


# ---------------------------------------------------------------- assemble


def assemble(args: argparse.Namespace) -> int:
    base = root()
    made = read_plan(Path(args.plan))
    pair = plan_pair(made)
    shards_dir = Path(args.shards)
    output = Path(args.output).resolve()
    if output.exists():
        shutil.rmtree(output)
    (output / "files").mkdir(parents=True)
    failures: list[str] = []
    results: list[dict[str, Any]] = []
    owners: dict[str, int] = {}
    deleted: list[str] = []
    uploaded: dict[int, Path] = {}
    for path in sorted(shards_dir.rglob("result.json")):
        record = read_json(path, "shard result")
        index = record.get("index") if isinstance(record, dict) else None
        if isinstance(index, int):
            if index in uploaded:
                failures.append(f"shard {index} uploaded two results ({uploaded[index]} and {path})")
            uploaded[index] = path
    for planned in made["shards"]:
        index = planned["index"]
        if index not in uploaded:
            failures.append(f"shard {index} uploaded no result; its job failed or was cancelled before uploading")
            continue
        record = read_json(uploaded[index], f"shard {index} result")
        shard_dir = uploaded[index].parent
        expected = [(entry["family"], entry["item"]) for entry in planned["items"]]
        reported = [(entry["family"], entry["item"]) for entry in record.get("items", [])]
        if record.get("pair") != made["pair"] or record.get("base") != made["base"]:
            failures.append(f"shard {index} generated at another pair or base than the plan")
            continue
        if reported != expected:
            missing = [f"{family} {item}" for family, item in expected if (family, item) not in reported]
            failures.append(
                f"shard {index} does not account for its planned items"
                + (f": missing {', '.join(missing)}" if missing else ": its items differ from the plan")
            )
            continue
        for path in [*record["written"], *record["deleted"]]:
            if path in owners and owners[path] != index:
                failures.append(f"{path} was written by shards {owners[path]} and {index}; plan their items together")
            owners[path] = index
        for path in record["written"]:
            source = shard_dir / "files" / path
            if not source.is_file():
                failures.append(f"shard {index} lists {path} but its artifact does not carry it")
                continue
            target = output / "files" / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        deleted += record["deleted"]
        logs = shard_dir / "logs"
        if logs.is_dir():
            shutil.copytree(logs, output / "logs", dirs_exist_ok=True)
        for entry in record["items"]:
            entry["shard"] = index
            results.append(entry)
            if entry["status"] == STATUS_FAILED:
                failures.append(
                    f"{entry['family']} {entry['item']}: generation failed: {entry['detail']} (log {entry['log']})"
                )
    # The measured seconds replace the recorded ones; an item that did not run keeps its row.
    table, _default = timings(base)
    for entry in results:
        if entry["status"] in (STATUS_OK, STATUS_KNOWN):
            table[(entry["family"], entry["item"])] = entry["seconds"]
    if made["complete"]:
        planned_keys = {
            (entry["family"], entry["item"]) for shard_plan in made["shards"] for entry in shard_plan["items"]
        }
        table = {key: value for key, value in table.items() if key in planned_keys}
    families = list(made["families"])
    rows = sorted(
        table.items(), key=lambda kv: (families.index(kv[0][0]) if kv[0][0] in families else len(families), kv[0][1])
    )
    write_tsv(
        output / "files" / TIMINGS,
        TIMINGS_HEADER,
        ([family, item, f"{seconds:.1f}"] for (family, item), seconds in rows),
        TIMINGS_NOTE,
    )
    metadata = output / "files" / METADATA
    metadata.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(base / METADATA, metadata)
    record = json.loads(metadata.read_text(encoding="utf-8"))
    record["cliVersion"], record["generatorVersion"] = pair.cli, pair.generator
    metadata.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8", newline="\n")
    unfetchable = [entry for entry in results if entry["status"] == STATUS_UNFETCHABLE]
    bundle = {
        "schema_version": SCHEMA_VERSION,
        "pair": made["pair"],
        "base": made["base"],
        "complete": made["complete"],
        "items": results,
        "deleted": sorted(set(deleted)),
        "failures": failures,
    }
    (output / "bundle.json").write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8", newline="\n")
    summarize(
        args.summary,
        [
            "## Fern goldens: assembly",
            "",
            f"{len(results)} item(s) from {len(made['shards'])} shard(s) at {pair.label()}; "
            f"{len(unfetchable)} with an unfetchable upstream specification; {len(failures)} failure(s).",
            *(f"- **failure**: {failure}" for failure in failures),
            *(f"- not regenerated: corpus `{entry['item']}`: {entry['detail']}" for entry in unfetchable),
        ],
    )
    if failures:
        print("fern-goldens-weekly: assembly failed:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1
    print(f"fern-goldens-weekly: assembled {len(results)} item(s) from {len(made['shards'])} shard(s)")
    return 0


# ---------------------------------------------------------------- apply


def read_bundle(path: Path) -> dict[str, Any]:
    bundle = read_json(path / "bundle.json", "assembled bundle")
    if not isinstance(bundle, dict) or bundle.get("schema_version") != SCHEMA_VERSION:
        raise WeeklyError(f"{path} holds no bundle of this tool's schema; re-run the assembly job")
    if bundle.get("failures"):
        raise WeeklyError(f"{path} is a failed assembly; nothing from it may be decided or published")
    return bundle


def apply_bundle(base: Path, path: Path) -> dict[str, Any]:
    bundle = read_bundle(path)
    head = git(base, "rev-parse", "HEAD")
    if bundle["base"] and head != bundle["base"]:
        raise WeeklyError(f"the bundle was generated over {bundle['base']}, but this checkout is at {head}")
    files = path / "files"
    for source in sorted(p for p in files.rglob("*") if p.is_file()):
        target = base / source.relative_to(files)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    for relative in bundle["deleted"]:
        target = base / relative
        if target.is_file():
            target.unlink()
    restated = run([sys.executable, str(base / "tools/fern-goldens/certified_pair.py"), "restate", str(base)], base)
    if restated.returncode != 0:
        raise WeeklyError(f"restating the pair failed: {restated.stderr.strip()}")
    return bundle


def apply(args: argparse.Namespace) -> int:
    base = root()
    bundle = apply_bundle(base, Path(args.bundle))
    print(f"fern-goldens-weekly: applied {len(bundle['items'])} item(s) at {Pair(**bundle['pair']).label()}")
    return 0


# ---------------------------------------------------------------- decide


@dataclass(frozen=True)
class Gate:
    """One `decision-gates.tsv` row: the families it decides, whether it runs
    once per item or once for its families, how its exit is read, and the
    command (crozier's own comparison, never logic of this tool's)."""

    families: tuple[str, ...]
    per_item: bool
    verdict: str
    passes: tuple[int, ...]
    rejects: tuple[int, ...]
    command: str


def gates(base: Path) -> list[Gate]:
    found = []
    for row in read_tsv(base / GATES, GATES_HEADER):
        families = tuple(name for name in row["family"].split(",") if name)
        if row["scope"] not in ("item", "family") or not families:
            raise WeeklyError(f"{GATES}: {row['family']}: scope is item or family, and a family is named")
        passes: tuple[int, ...] = ()
        rejects: tuple[int, ...] = ()
        if row["verdict"] != "fixtures-report":
            match = re.fullmatch(r"exit:([0-9,]+)/([0-9,]+)", row["verdict"])
            if match is None:
                raise WeeklyError(f"{GATES}: verdict {row['verdict']!r} is fixtures-report or exit:PASS/REJECT")
            passes = tuple(int(code) for code in match.group(1).split(","))
            rejects = tuple(int(code) for code in match.group(2).split(","))
        found.append(Gate(families, row["scope"] == "item", row["verdict"], passes, rejects, row["command"]))
    return found


@dataclass
class Verdict:
    status: str  # pass, reject, cannot-run
    report: str
    exit: int | None = None


DIFFS = re.compile(r"(?m)^(\d+) differing file\(s\) across the reported corpora\.$")
GENERATION = re.compile(r"(?m)^(\d+) comparison generation failure\(s\) across the reported corpora\.$")
PROCESSING = re.compile(r"(?m)^(\d+) comparison processing failure\(s\) across the reported corpora\.$")
REGRESSION = re.compile(r"(?m)^--- .* \[REGRESSION")
SETUP = re.compile(r"(?m)^  Comparison setup failed: ")


def read_report(code: int, output: str) -> str:
    """The verdict `report_fixture_diffs` (`just fixtures-diff`) states for its
    corpus, read off its own summary: a difference its corpus does not list in
    `unmatched`, a Crozier generation failure or a comparison it could not
    process is a rejection; a setup failure or a report without its summaries
    is a comparison that could not run."""
    summaries = [pattern.search(output) for pattern in (DIFFS, GENERATION, PROCESSING)]
    if code != 0 or any(match is None for match in summaries) or SETUP.search(output):
        return "cannot-run"
    _diffs, generation, processing = (int(match.group(1)) for match in summaries if match is not None)
    return "reject" if REGRESSION.search(output) or generation or processing else "pass"


def run_gate(base: Path, gate: Gate, item: str | None) -> Verdict:
    with tempfile.TemporaryDirectory(prefix="fern-goldens-gate-") as scratch:
        words = [
            word.replace("{root}", str(base)).replace("{scratch}", scratch).replace("{item}", item or "")
            for word in shlex.split(gate.command)
        ]
        environment = dict(os.environ)
        while words and re.fullmatch(r"[A-Z_][A-Z0-9_]*=.*", words[0]):
            name, _, value = words.pop(0).partition("=")
            environment[name] = value
        try:
            result = run(words, base, environment)
        except WeeklyError as error:
            return Verdict("cannot-run", str(error))
    output = (result.stdout or "") + (result.stderr or "")
    if gate.verdict == "fixtures-report":
        return Verdict(read_report(result.returncode, output), output, result.returncode)
    if result.returncode in gate.passes:
        return Verdict("pass", output, result.returncode)
    if result.returncode in gate.rejects:
        return Verdict("reject", output, result.returncode)
    return Verdict("cannot-run", output, result.returncode)


def excerpt(report: str, tokens: Iterable[str], context: int = 4, limit: int = 80) -> str:
    """The lines of a family gate's own report that name an item, with the
    lines after each, which is how the report attributes a failure."""
    wanted = [token for token in tokens if token]
    lines = report.splitlines()
    keep: set[int] = set()
    for number, line in enumerate(lines):
        if any(token in line for token in wanted):
            keep.update(range(number, min(number + context + 1, len(lines))))
    return "\n".join(lines[number] for number in sorted(keep)[:limit])


@dataclass
class Decision:
    pair: Pair
    complete: bool
    failing: dict[str, list[dict[str, str]]] = field(default_factory=dict)
    unfetchable: list[dict[str, str]] = field(default_factory=list)
    cannot_run: list[str] = field(default_factory=list)
    gates: list[dict[str, Any]] = field(default_factory=list)

    @property
    def outcome(self) -> str:
        if self.cannot_run:
            return "failure"
        return "diff" if self.failing or self.unfetchable else "match"


def decide_bundle(base: Path, bundle: dict[str, Any], reports: Path) -> Decision:
    decision = Decision(Pair(**bundle["pair"]), bool(bundle["complete"]))
    items: dict[str, list[dict[str, Any]]] = {}
    for entry in bundle["items"]:
        if entry["status"] == STATUS_UNFETCHABLE:
            decision.unfetchable.append({"item": entry["item"], "detail": entry["detail"]})
        else:
            items.setdefault(entry["family"], []).append(entry)
    reports.mkdir(parents=True, exist_ok=True)
    seen: dict[str, Verdict] = {}
    for gate in gates(base):
        decided = [family for family in gate.families if family in items]
        if not decided:
            continue
        if gate.per_item:
            for family in decided:
                for entry in items[family]:
                    verdict = run_gate(base, gate, entry["item"])
                    record_gate(decision, reports, gate, family, entry["item"], verdict)
                    if verdict.status == "reject":
                        decision.failing.setdefault(family, []).append(
                            {"item": entry["item"], "report": verdict.report.strip()}
                        )
            continue
        verdict = seen.get(gate.command) or run_gate(base, gate, None)
        first = gate.command not in seen
        seen[gate.command] = verdict
        if first:
            record_gate(decision, reports, gate, ",".join(gate.families), None, verdict)
        if verdict.status != "reject":
            continue
        for family in decided:
            named = False
            for entry in items[family]:
                part = excerpt(verdict.report, [entry["item"], *entry["changed"]])
                if part:
                    named = True
                    listed = decision.failing.setdefault(family, [])
                    if not any(existing["item"] == entry["item"] for existing in listed):
                        listed.append({"item": entry["item"], "report": f"`{gate.command}`:\n{part}"})
            if not named and family == decided[0]:
                tail = "\n".join(verdict.report.splitlines()[-80:])
                decision.failing.setdefault(family, []).append(
                    {"item": "(the gate's report names no item)", "report": f"`{gate.command}`:\n{tail}"}
                )
    return decision


def record_gate(decision: Decision, reports: Path, gate: Gate, family: str, item: str | None, verdict: Verdict) -> None:
    name = f"{len(decision.gates):04d}-{safe_name(family)}{'-' + safe_name(item) if item else ''}.log"
    (reports / name).write_text(verdict.report, encoding="utf-8", newline="\n")
    decision.gates.append(
        {
            "command": gate.command,
            "family": family,
            "item": item,
            "status": verdict.status,
            "exit": verdict.exit,
            "report": name,
        }
    )
    if verdict.status == "cannot-run":
        decision.cannot_run.append(
            f"`{gate.command}`{f' for {family} `{item}`' if item else ''} could not run "
            f"(exit {verdict.exit}); see {name}"
        )


def fenced(text: str) -> str:
    longest = max((len(run_) for run_ in re.findall(r"`+", text)), default=0)
    fence = "`" * max(3, longest + 1)
    return f"{fence}text\n{text}\n{fence}"


def title(pair: Pair) -> str:
    return f"test(fern-goldens): regenerate at Fern CLI {pair.cli} / fern-python-sdk {pair.generator}"


def body(decision: Decision, bundle: dict[str, Any], current: Pair) -> str:
    run_url = ""
    if os.environ.get("GITHUB_RUN_ID") and os.environ.get("GITHUB_REPOSITORY"):
        server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
        run_url = f"{server}/{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
    families: dict[str, int] = {}
    for entry in bundle["items"]:
        families[entry["family"]] = families.get(entry["family"], 0) + 1
    lines = [
        "## What",
        "",
        f"The weekly Fern goldens run regenerated every committed Fern reference at {decision.pair.label()} "
        f"(certified: {current.label()}) and compared crozier's output with each through crozier's own comparison.",
        "",
    ]
    if decision.outcome == "match":
        lines += [
            "**No diff**: crozier's output matches every regenerated reference, so this adopts the pair: "
            "`assets/scaffolding/metadata.json`, every statement of the pair, the regenerated references, the "
            "measured generation seconds and a `tests/fixtures/fern-pair-checks.tsv` row. It merges itself once "
            "crozier's required checks pass.",
        ]
    else:
        failing = sum(len(entries) for entries in decision.failing.values())
        lines += [
            f"**Diff**: crozier's comparison fails for {failing} item(s)"
            + (
                f", and {len(decision.unfetchable)} reference(s) could not be regenerated"
                if decision.unfetchable
                else ""
            )
            + ". This carries the regenerated references and the new pair; crozier's checks on it show what "
            "crozier must change. It is not auto-merged.",
        ]
    lines += ["", "## Why", "", "Fern released a new version; crozier promises to match the Fern its users run.", ""]
    if decision.failing:
        lines += ["## Failing items", ""]
        budget = BODY_LIMIT // max(1, sum(len(entries) for entries in decision.failing.values()))
        for family, entries in decision.failing.items():
            lines += [f"### {family} ({len(entries)})", ""]
            for entry in entries:
                report = entry["report"]
                limit = min(REPORT_LIMIT, max(400, budget))
                if len(report) > limit:
                    report = report[:limit] + "\n… (truncated; the decision artifact holds the whole report)"
                lines += [
                    f"- `{entry['item']}`",
                    "",
                    "<details><summary>report</summary>",
                    "",
                    fenced(report),
                    "",
                    "</details>",
                    "",
                ]
    if decision.unfetchable:
        lines += ["## Not regenerated: upstream specification unavailable", ""]
        lines += [f"- corpus `{entry['item']}`: {entry['detail']}" for entry in decision.unfetchable]
        lines += [""]
    lines += ["## Inventory", "", "| family | items |", "|---|---:|"]
    lines += [f"| {family} | {count} |" for family, count in families.items()]
    if run_url:
        lines += ["", f"Run: {run_url}"]
    lines += ["", "🤖 Generated by the Fern goldens workflow."]
    text = "\n".join(lines) + "\n"
    return text if len(text) <= BODY_LIMIT + 5000 else text[:BODY_LIMIT] + "\n… (truncated)\n"


def decide(args: argparse.Namespace) -> int:
    base = root()
    bundle = read_bundle(Path(args.bundle))
    current = certified_at_base(base)
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    decision = decide_bundle(base, bundle, output / "reports")
    record = {
        "schema_version": SCHEMA_VERSION,
        "outcome": decision.outcome,
        "complete": decision.complete,
        "pair": bundle["pair"],
        "failing": decision.failing,
        "unfetchable": decision.unfetchable,
        "cannot_run": decision.cannot_run,
        "gates": decision.gates,
        "title": title(decision.pair),
    }
    (output / "decision.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8", newline="\n")
    (output / "body.md").write_text(body(decision, bundle, current), encoding="utf-8", newline="\n")
    failing = [f"{family} `{entry['item']}`" for family, entries in decision.failing.items() for entry in entries]
    summarize(
        args.summary,
        [
            "## Fern goldens: decision",
            "",
            f"**{decision.outcome}** at {decision.pair.label()}"
            + ("" if decision.complete else " (a diagnostic subset: nothing is published)"),
            *(f"- **cannot run**: {line}" for line in decision.cannot_run),
            *(f"- differs: {line}" for line in failing),
            *(f"- not regenerated: corpus `{entry['item']}`: {entry['detail']}" for entry in decision.unfetchable),
        ],
    )
    print(f"fern-goldens-weekly: decision {decision.outcome}: {len(failing)} failing item(s)")
    if decision.cannot_run:
        for line in decision.cannot_run:
            print(f"  cannot run: {line}", file=sys.stderr)
        return 1
    return 0


def certified_at_base(base: Path) -> Pair:
    """The pair HEAD certifies, whatever the working tree now declares."""
    shown = blob(base, METADATA.as_posix())
    if shown is None:
        return certified(base)
    record = json.loads(shown.decode("utf-8"))
    return Pair(record["cliVersion"], record["generatorVersion"])


# ---------------------------------------------------------------- publish


class Steps:
    """The publication steps and how each ended, for the summary a failure
    leaves: the next run reconciles from the remote, not from this record."""

    def __init__(self) -> None:
        self.done: list[tuple[str, str]] = []

    def mark(self, step: str, outcome: str) -> None:
        self.done.append((step, outcome))
        print(f"fern-goldens-weekly: publish: {step}: {outcome}")

    def lines(self) -> list[str]:
        return [f"- {step}: {outcome}" for step, outcome in self.done]


def gh(repo: str, *args: str) -> subprocess.CompletedProcess[Any]:
    return run(["gh", *args, "--repo", repo], Path.cwd())


def open_pull(repo: str) -> dict[str, Any] | None:
    listed = gh(repo, "pr", "list", "--head", BRANCH, "--state", "open", "--json", "number,url,autoMergeRequest,labels")
    if listed.returncode != 0:
        raise WeeklyError(f"could not list pull requests: {listed.stderr.strip()}")
    try:
        pulls = json.loads(listed.stdout or "[]")
    except ValueError as error:
        raise WeeklyError(f"gh pr list printed no JSON ({error})") from error
    return pulls[0] if pulls else None


def ensure_label(repo: str) -> str:
    listed = gh(repo, "label", "list", "--search", LABEL, "--json", "name", "--limit", "100")
    if listed.returncode != 0:
        raise WeeklyError(f"could not list labels: {listed.stderr.strip()}")
    if any(label.get("name") == LABEL for label in json.loads(listed.stdout or "[]")):
        return "present"
    created = gh(repo, "label", "create", LABEL, "--color", "0E8A16", "--description", "Weekly Fern goldens run")
    if created.returncode != 0:
        raise WeeklyError(f"could not create the {LABEL} label: {created.stderr.strip()}")
    return "created"


def commit_tree(base: Path, bundle_path: Path, decision: dict[str, Any], checked_on: str) -> str:
    """The one commit the pull request carries, on the planned base."""
    apply_bundle(base, bundle_path)
    pair = Pair(**decision["pair"])
    if decision["outcome"] == "match":
        path = base / CHECKS
        rows = read_tsv(path, CHECKS_HEADER) if path.is_file() else []
        rows.append(dict(zip(CHECKS_HEADER, (pair.cli, pair.generator, checked_on, "match"), strict=True)))
        write_tsv(path, CHECKS_HEADER, ([row[key] for key in CHECKS_HEADER] for row in rows))
    git(base, "checkout", "-B", BRANCH)
    git(base, "add", "-A")
    git(
        base,
        "-c",
        "user.name=github-actions[bot]",
        "-c",
        "user.email=41898282+github-actions[bot]@users.noreply.github.com",
        "commit",
        "-q",
        "--allow-empty",
        "-m",
        decision["title"],
    )
    return git(base, "rev-parse", "HEAD")


def push(base: Path, steps: Steps) -> None:
    """Push the branch unless the remote already holds this tree on this base;
    a lease on what the remote held keeps the push from overwriting a change
    made since it was read. Never `main`."""
    remote = git(base, "ls-remote", "origin", f"refs/heads/{BRANCH}").split("\t")[0]
    if remote:
        git(base, "fetch", "--no-tags", "origin", f"refs/heads/{BRANCH}")
        same_tree = git(base, "rev-parse", f"{remote}^{{tree}}") == git(base, "rev-parse", "HEAD^{tree}")
        same_base = git(base, "rev-parse", f"{remote}^", check=False) == git(base, "rev-parse", "HEAD^")
        if same_tree and same_base:
            git(base, "reset", "-q", "--hard", remote)
            steps.mark(f"push {BRANCH}", f"already on the remote at {remote[:12]}")
            return
    pushed = run(
        [
            "git",
            "-C",
            str(base),
            "push",
            f"--force-with-lease=refs/heads/{BRANCH}:{remote}",
            "origin",
            f"HEAD:refs/heads/{BRANCH}",
        ],
        base,
    )
    if pushed.returncode != 0:
        raise WeeklyError(f"pushing {BRANCH} failed: {pushed.stderr.strip()}")
    steps.mark(f"push {BRANCH}", "pushed")


def publish(args: argparse.Namespace) -> int:
    base = root()
    steps = Steps()
    decision = read_json(Path(args.decision) / "decision.json", "decision")
    try:
        if decision.get("outcome") not in ("match", "diff"):
            raise WeeklyError(f"the decision is {decision.get('outcome')!r}; only a match or a diff is published")
        if not decision.get("complete"):
            raise WeeklyError("a diagnostic subset run never publishes, adopts or records a pair")
        if not os.environ.get("GH_TOKEN"):
            raise WeeklyError(
                "GH_TOKEN (the workflow's RELEASE_PLZ_TOKEN) is not set; add the secret, then re-run. Nothing was pushed."
            )
        checked_on = args.checked_on or datetime.datetime.now(datetime.UTC).date().isoformat()
        commit_tree(base, Path(args.bundle), decision, checked_on)
        steps.mark("commit", git(base, "rev-parse", "--short=12", "HEAD"))
        push(base, steps)
        steps.mark(f"label {LABEL}", ensure_label(args.repo))
        body_file = str(Path(args.decision) / "body.md")
        # Every write reads the remote first and is skipped when already done, so
        # a run after a failure or a lost response finishes the rest; a write that
        # fails ends the run red, whatever the remote may since have applied.
        pull = open_pull(args.repo)
        if pull is None:
            created = gh(
                args.repo,
                "pr",
                "create",
                "--base",
                BASE,
                "--head",
                BRANCH,
                "--title",
                decision["title"],
                "--body-file",
                body_file,
                "--label",
                LABEL,
            )
            if created.returncode != 0:
                raise WeeklyError(f"opening the pull request failed: {created.stderr.strip()}")
            pull = open_pull(args.repo)
            if pull is None:
                raise WeeklyError("the pull request gh reported opened is not listed open")
            steps.mark("pull request", f"opened #{pull['number']}")
        else:
            edited = gh(
                args.repo,
                "pr",
                "edit",
                str(pull["number"]),
                "--title",
                decision["title"],
                "--body-file",
                body_file,
                "--add-label",
                LABEL,
            )
            if edited.returncode != 0:
                raise WeeklyError(f"updating pull request #{pull['number']} failed: {edited.stderr.strip()}")
            steps.mark("pull request", f"updated #{pull['number']}")
        number = str(pull["number"])
        if decision["outcome"] == "match":
            if pull.get("autoMergeRequest"):
                steps.mark("auto-merge", "already enabled")
            else:
                merged = gh(args.repo, "pr", "merge", number, "--auto", "--squash")
                if merged.returncode != 0:
                    raise WeeklyError(f"enabling auto-merge on #{number} failed: {merged.stderr.strip()}")
                steps.mark("auto-merge", "enabled")
        elif pull.get("autoMergeRequest"):
            disabled = gh(args.repo, "pr", "merge", number, "--disable-auto")
            if disabled.returncode != 0:
                raise WeeklyError(f"turning off auto-merge on #{number} failed: {disabled.stderr.strip()}")
            steps.mark("auto-merge", "turned off: a diff waits for a person")
        else:
            steps.mark("auto-merge", "off: a diff waits for a person")
    except WeeklyError as error:
        summarize(
            args.summary,
            [
                "## Fern goldens: publication failed",
                "",
                f"**{error}**",
                "",
                "Steps completed before it:",
                *(steps.lines() or ["- none"]),
                "",
                "The next run reconciles from the remote: it reuses the branch and pull request and finishes the rest.",
            ],
        )
        print(f"fern-goldens-weekly: publication failed: {error}", file=sys.stderr)
        return 1
    summarize(args.summary, ["## Fern goldens: publication", "", *steps.lines()])
    return 0


# ---------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="weekly.py", description=__doc__.split("\n", 1)[0])
    commands = parser.add_subparsers(dest="command", required=True)
    phase = commands.add_parser("resolve", help="the pair to check, or why there is none")
    phase.add_argument("--ref", required=True)
    phase.add_argument("--cli-version", default="")
    phase.add_argument("--generator-version", default="")
    phase.add_argument("--items", default="")
    phase.add_argument("--token-present", action="store_true")
    phase = commands.add_parser("plan", help="the shards every planned item generates in")
    phase.add_argument("--items", default="")
    phase.add_argument("--cli", default="")
    phase.add_argument("--generator", default="")
    phase.add_argument("--output")
    phase.add_argument("--telemetry", help="also write the plan where the weekly budget reads it")
    phase = commands.add_parser("shard", help="generate one shard's items")
    phase.add_argument("--plan", required=True)
    phase.add_argument("--index", type=int, required=True)
    phase.add_argument("--output", required=True)
    phase = commands.add_parser("assemble", help="combine every shard's result into one bundle")
    phase.add_argument("--plan", required=True)
    phase.add_argument("--shards", required=True)
    phase.add_argument("--output", required=True)
    phase = commands.add_parser("apply", help="lay a bundle over this checkout")
    phase.add_argument("--bundle", required=True)
    phase = commands.add_parser("decide", help="crozier's comparison over the applied tree")
    phase.add_argument("--bundle", required=True)
    phase.add_argument("--output", required=True)
    phase = commands.add_parser("publish", help="open, update or finish the one pull request")
    phase.add_argument("--bundle", required=True)
    phase.add_argument("--decision", required=True)
    phase.add_argument("--repo", required=True)
    phase.add_argument("--checked-on", default="")
    for sub in commands.choices.values():
        sub.add_argument("--summary", help="append this phase's Markdown here (the step summary)")
        sub.add_argument("--github-output", help="append this phase's outputs here")
    args = parser.parse_args(argv)
    try:
        return {
            "resolve": resolve,
            "plan": plan,
            "shard": shard,
            "assemble": assemble,
            "apply": apply,
            "decide": decide,
            "publish": publish,
        }[args.command](args)
    except WeeklyError as error:
        summarize(getattr(args, "summary", None), [f"## Fern goldens: {args.command} failed", "", f"**{error}**"])
        print(f"fern-goldens-weekly: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
