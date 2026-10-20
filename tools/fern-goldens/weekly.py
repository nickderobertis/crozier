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
            into as few shards as fit the weekly budget with a margin, each
            predicted from `generation-seconds.tsv`
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
summary). Every artifact one phase hands the next is a typed record, validated
when it is read. Exit status: 0 when the phase finished (a diff is a finished
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
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass, field, replace
from enum import StrEnum
from pathlib import Path, PurePosixPath
from types import ModuleType
from typing import TypeVar

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
# The shard job's `timeout-minutes`, which the workflow test holds the YAML to;
# GitHub stops a job at 6 hours, and no shard is planned past this.
SHARD_TIMEOUT_MINUTES = 300.0
# A free-plan public repository runs at most 20 jobs at once.
CONCURRENT_JOBS = 20
# The same run generated 222 trees (218 packaged + 4 flat) in 3,590 seconds of
# its generation step: the rate an item no run has timed yet is planned at,
# until the table holds corpus timings of its own.
SEED_SECONDS_PER_GENERATION = 3590.0 / 222

VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+")
NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]*")
REPORT_LIMIT = 6000
BODY_LIMIT = 60000


class WeeklyError(RuntimeError):
    """A failure this phase names, with what to do about it."""


class Status(StrEnum):
    """How one item's regeneration ended."""

    OK = "ok"
    KNOWN = "known-upstream-failure"
    UNFETCHABLE = "spec-unfetchable"
    FAILED = "failed"


class Verdict(StrEnum):
    """How one of crozier's comparisons ended."""

    PASS = "pass"
    REJECT = "reject"
    CANNOT_RUN = "cannot-run"


class Outcome(StrEnum):
    """The run's decision: crozier matches every reference, differs from one,
    or a comparison could not be made."""

    MATCH = "match"
    DIFF = "diff"
    FAILURE = "failure"


T = TypeVar("T")


def field_of(record: object, key: str, kind: type[T], where: str) -> T:
    """`record[key]` when `record` is an object and the value is a `kind`."""
    value = record.get(key) if isinstance(record, dict) else None
    if not isinstance(value, kind) or (kind is int and isinstance(value, bool)):
        raise WeeklyError(f"{where}: `{key}` must be {kind.__name__}, not {value!r}; re-run the phase that wrote it")
    return value


def seconds_of(record: object, key: str, where: str) -> float:
    value = record.get(key) if isinstance(record, dict) else None
    if isinstance(value, bool) or not isinstance(value, int | float) or not math.isfinite(value) or value < 0:
        raise WeeklyError(f"{where}: `{key}` must be a non-negative number, not {value!r}")
    return float(value)


def base_of(record: object, where: str) -> str | None:
    """The commit an artifact was made over: a full hex object name, or null
    when it records none (a plan made outside a checkout)."""
    value = record.get("base") if isinstance(record, dict) else None
    if value is not None and not (isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", value)):
        raise WeeklyError(f"{where}: `base` must be a commit's full name or null, not {value!r}")
    return value


def name_of(record: object, key: str, where: str) -> str:
    """A family or item name: path segments of letters, digits, `.`, `_` and
    `-`, never `..`, so it can name a log or a path under the checkout."""
    value = field_of(record, key, str, where)
    if not NAME.fullmatch(value) or ".." in value.split("/"):
        raise WeeklyError(f"{where}: `{key}` {value!r} is no family or item name")
    return value


def stable(version: object) -> bool:
    return isinstance(version, str) and VERSION.fullmatch(version) is not None


def safe_path(value: object, where: str) -> str:
    """A repository-relative POSIX path that stays inside the checkout."""
    path = PurePosixPath(value) if isinstance(value, str) and value and "\\" not in value else None
    if path is None or path.is_absolute() or ".." in path.parts or path.parts[:1] == (".git",):
        raise WeeklyError(f"{where}: {value!r} is no path inside the repository")
    return path.as_posix()


def inside(root: Path, relative: str, where: str) -> Path:
    """`root / relative`, refused unless it resolves inside `root`: a lexically
    safe path whose components are symbolic links leading out is no path of
    the checkout either."""
    target = root / safe_path(relative, where)
    if not target.resolve().is_relative_to(root.resolve()):
        raise WeeklyError(f"{where}: {relative!r} resolves outside {root} through a symbolic link")
    return target


def regular_files(directory: Path, where: str) -> list[Path]:
    """Every file under an artifact directory, refused if any is a symbolic link."""
    found = []
    for path in sorted(directory.rglob("*")) if directory.is_dir() else []:
        if path.is_symlink():
            raise WeeklyError(
                f"{where}: {path.relative_to(directory).as_posix()} is a symbolic link; re-run the job that wrote it"
            )
        if path.is_file():
            found.append(path)
    return found


def safe_name(item: str) -> str:
    return item.replace("/", "__")


@dataclass(frozen=True)
class Pair:
    cli: str
    generator: str

    def label(self) -> str:
        return f"Fern CLI {self.cli} / fern-python-sdk {self.generator}"

    def to_json(self) -> dict[str, str]:
        return {"cli": self.cli, "generator": self.generator}

    @classmethod
    def from_json(cls, record: object, where: str) -> Pair:
        cli, generator = field_of(record, "cli", str, where), field_of(record, "generator", str, where)
        if not (stable(cli) and stable(generator)):
            raise WeeklyError(f"{where}: the pair must name exact stable versions, not {cli!r} and {generator!r}")
        return cls(cli, generator)


@dataclass(frozen=True)
class Selector:
    """One part of a dispatch's subset: a whole family, or one item of it."""

    family: str
    item: str | None = None


@dataclass(frozen=True)
class PlannedItem:
    family: str
    item: str
    seconds: float

    def key(self) -> tuple[str, str]:
        return self.family, self.item


@dataclass(frozen=True)
class PlannedShard:
    index: int
    seconds: float
    minutes: float
    items: tuple[PlannedItem, ...]


@dataclass(frozen=True)
class FamilyTotal:
    items: int
    seconds: float


@dataclass(frozen=True)
class Estimate:
    """The run's predicted minutes, start to pull request, and their parts."""

    minutes: float
    stages: dict[str, float]
    waves: int
    setup_minutes_per_job: float
    assembly_minutes: float
    longest_shard_minutes: float


@dataclass(frozen=True)
class Plan:
    """What the run generates, in which shards, at which pair and base."""

    complete: bool
    items: str
    base: str | None
    pair: Pair | None
    budget_minutes: float
    shard_limit_minutes: float
    default_seconds: float
    families: dict[str, FamilyTotal]
    units: int
    shards: tuple[PlannedShard, ...]
    estimate: Estimate

    def to_json(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "complete": self.complete,
            "items": self.items,
            "base": self.base,
            "pair": self.pair.to_json() if self.pair else None,
            "budget_minutes": self.budget_minutes,
            "shard_limit_minutes": self.shard_limit_minutes,
            "default_seconds": self.default_seconds,
            "families": {name: vars(total) for name, total in self.families.items()},
            "units": self.units,
            "shards": [
                {
                    "index": shard.index,
                    "seconds": shard.seconds,
                    "minutes": shard.minutes,
                    "items": [vars(entry) for entry in shard.items],
                }
                for shard in self.shards
            ],
            "estimate": vars(self.estimate),
        }

    @classmethod
    def from_json(cls, record: object, where: str) -> Plan:
        if field_of(record, "schema_version", int, where) != SCHEMA_VERSION:
            raise WeeklyError(f"{where} is no plan of this tool's schema; re-run the plan job")
        assert isinstance(record, dict)
        shards = []
        for index, shard in enumerate(field_of(record, "shards", list, where)):
            at = f"{where} shard {index}"
            if field_of(shard, "index", int, at) != index:
                raise WeeklyError(f"{at}: shards must be numbered from 0 in order")
            items = tuple(
                PlannedItem(name_of(entry, "family", at), name_of(entry, "item", at), seconds_of(entry, "seconds", at))
                for entry in field_of(shard, "items", list, at)
            )
            shards.append(
                PlannedShard(index, seconds_of(shard, "seconds", at), seconds_of(shard, "minutes", at), items)
            )
        keys = [entry.key() for shard in shards for entry in shard.items]
        if len(keys) != len(set(keys)):
            raise WeeklyError(f"{where} plans an item twice; re-run the plan job")
        families = {
            name_of({"family": name}, "family", where): FamilyTotal(
                field_of(total, "items", int, where), seconds_of(total, "seconds", where)
            )
            for name, total in field_of(record, "families", dict, where).items()
        }
        for name, total in families.items():
            if total.items < 1 or sum(family == name for family, _item in keys) != total.items:
                raise WeeklyError(f"{where}: its shards do not hold the {total.items} {name} item(s) it counts")
        if {family for family, _item in keys} - set(families):
            raise WeeklyError(f"{where}: a shard holds an item of no family it counts")
        complete = field_of(record, "complete", bool, where)
        if complete != (not parse_selectors(field_of(record, "items", str, where))) or (complete and not keys):
            raise WeeklyError(
                f"{where}: `complete` must say whether it plans the whole inventory, which is never empty"
            )
        estimate = field_of(record, "estimate", dict, where)
        stages = field_of(estimate, "stages", dict, where)
        pair = record.get("pair")
        return cls(
            complete=complete,
            items=field_of(record, "items", str, where),
            base=base_of(record, where),
            pair=Pair.from_json(pair, where) if pair is not None else None,
            budget_minutes=seconds_of(record, "budget_minutes", where),
            shard_limit_minutes=seconds_of(record, "shard_limit_minutes", where),
            default_seconds=seconds_of(record, "default_seconds", where),
            families=families,
            units=field_of(record, "units", int, where),
            shards=tuple(shards),
            estimate=Estimate(
                minutes=seconds_of(estimate, "minutes", where),
                stages={name: seconds_of(stages, name, where) for name in stages},
                waves=field_of(estimate, "waves", int, where),
                setup_minutes_per_job=seconds_of(estimate, "setup_minutes_per_job", where),
                assembly_minutes=seconds_of(estimate, "assembly_minutes", where),
                longest_shard_minutes=seconds_of(estimate, "longest_shard_minutes", where),
            ),
        )

    def candidate(self) -> Pair:
        if self.pair is None:
            raise WeeklyError("the plan names no pair to generate at; re-run the plan job with --cli and --generator")
        return self.pair


@dataclass(frozen=True)
class ItemResult:
    """How one item regenerated: its outcome, seconds, log and files written."""

    family: str
    item: str
    status: Status
    detail: str
    seconds: float
    changed: tuple[str, ...]
    log: str
    shard: int | None = None

    def to_json(self) -> dict[str, object]:
        record: dict[str, object] = {
            "family": self.family,
            "item": self.item,
            "status": self.status.value,
            "detail": self.detail,
            "seconds": self.seconds,
            "changed": list(self.changed),
            "log": self.log,
        }
        if self.shard is not None:
            record["shard"] = self.shard
        return record

    @classmethod
    def from_json(cls, record: object, where: str) -> ItemResult:
        status = field_of(record, "status", str, where)
        if status not in set(Status):
            raise WeeklyError(f"{where}: status {status!r} is none of {', '.join(Status)}")
        shard = record.get("shard") if isinstance(record, dict) else None
        return cls(
            family=name_of(record, "family", where),
            item=name_of(record, "item", where),
            status=Status(status),
            detail=field_of(record, "detail", str, where),
            seconds=seconds_of(record, "seconds", where),
            changed=tuple(safe_path(path, where) for path in field_of(record, "changed", list, where)),
            log=field_of(record, "log", str, where),
            shard=shard if isinstance(shard, int) and not isinstance(shard, bool) else None,
        )


@dataclass(frozen=True)
class ShardResult:
    """One shard's artifact record: what each item did, and the files it carries."""

    index: int
    pair: Pair
    base: str | None
    items: tuple[ItemResult, ...]
    written: tuple[str, ...]
    deleted: tuple[str, ...]

    def to_json(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "index": self.index,
            "pair": self.pair.to_json(),
            "base": self.base,
            "items": [item.to_json() for item in self.items],
            "written": list(self.written),
            "deleted": list(self.deleted),
        }

    @classmethod
    def from_json(cls, record: object, where: str) -> ShardResult:
        if field_of(record, "schema_version", int, where) != SCHEMA_VERSION:
            raise WeeklyError(f"{where} is no shard result of this tool's schema")
        return cls(
            index=field_of(record, "index", int, where),
            pair=Pair.from_json(record.get("pair") if isinstance(record, dict) else None, where),
            base=base_of(record, where),
            items=tuple(ItemResult.from_json(item, where) for item in field_of(record, "items", list, where)),
            written=tuple(safe_path(path, where) for path in field_of(record, "written", list, where)),
            deleted=tuple(safe_path(path, where) for path in field_of(record, "deleted", list, where)),
        )


@dataclass(frozen=True)
class Bundle:
    """Every shard combined: the one tree a decision and a pull request read."""

    pair: Pair
    base: str | None
    complete: bool
    items: tuple[ItemResult, ...]
    deleted: tuple[str, ...]
    failures: tuple[str, ...]

    def to_json(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "pair": self.pair.to_json(),
            "base": self.base,
            "complete": self.complete,
            "items": [item.to_json() for item in self.items],
            "deleted": list(self.deleted),
            "failures": list(self.failures),
        }

    @classmethod
    def from_json(cls, record: object, where: str) -> Bundle:
        if field_of(record, "schema_version", int, where) != SCHEMA_VERSION:
            raise WeeklyError(f"{where} holds no bundle of this tool's schema; re-run the assembly job")
        return cls(
            pair=Pair.from_json(record.get("pair") if isinstance(record, dict) else None, where),
            base=base_of(record, where),
            complete=field_of(record, "complete", bool, where),
            items=tuple(ItemResult.from_json(item, where) for item in field_of(record, "items", list, where)),
            deleted=tuple(safe_path(path, where) for path in field_of(record, "deleted", list, where)),
            failures=tuple(str(failure) for failure in field_of(record, "failures", list, where)),
        )


@dataclass(frozen=True)
class FailingItem:
    """An item crozier's comparison rejected, with the comparison's own report."""

    item: str
    report: str


@dataclass(frozen=True)
class Unfetchable:
    """A reference whose pinned upstream specification could not be fetched."""

    item: str
    detail: str


@dataclass(frozen=True)
class GateRun:
    """One comparison the decision ran, and the file its report is saved in."""

    command: str
    family: str
    item: str | None
    verdict: Verdict
    exit: int | None
    report: str


@dataclass
class Decision:
    pair: Pair
    complete: bool
    bundle: str
    failing: dict[str, list[FailingItem]] = field(default_factory=dict)
    unfetchable: list[Unfetchable] = field(default_factory=list)
    cannot_run: list[str] = field(default_factory=list)
    gates: list[GateRun] = field(default_factory=list)

    @property
    def outcome(self) -> Outcome:
        if self.cannot_run:
            return Outcome.FAILURE
        return Outcome.DIFF if self.failing or self.unfetchable else Outcome.MATCH

    def title(self) -> str:
        return f"test(fern-goldens): regenerate at Fern CLI {self.pair.cli} / fern-python-sdk {self.pair.generator}"

    def to_json(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "outcome": self.outcome.value,
            "complete": self.complete,
            "pair": self.pair.to_json(),
            "bundle": self.bundle,
            "failing": {family: [vars(entry) for entry in entries] for family, entries in self.failing.items()},
            "unfetchable": [vars(entry) for entry in self.unfetchable],
            "cannot_run": self.cannot_run,
            "gates": [{**vars(run_), "verdict": run_.verdict.value} for run_ in self.gates],
            "title": self.title(),
        }


@dataclass(frozen=True)
class RecordedDecision:
    """A decision as the publication job reads it back."""

    outcome: Outcome
    complete: bool
    pair: Pair
    bundle: str
    title: str

    @classmethod
    def from_json(cls, record: object, where: str) -> RecordedDecision:
        if field_of(record, "schema_version", int, where) != SCHEMA_VERSION:
            raise WeeklyError(f"{where} is no decision of this tool's schema; re-run the decision job")
        outcome = field_of(record, "outcome", str, where)
        if outcome not in set(Outcome):
            raise WeeklyError(f"{where}: outcome {outcome!r} is none of {', '.join(Outcome)}")
        return cls(
            Outcome(outcome),
            field_of(record, "complete", bool, where),
            Pair.from_json(record.get("pair") if isinstance(record, dict) else None, where),
            field_of(record, "bundle", str, where),
            field_of(record, "title", str, where),
        )


@dataclass(frozen=True)
class Step:
    """One publication step and how it ended."""

    name: str
    outcome: str


def root() -> Path:
    return Path(os.environ.get(ROOT_ENV) or Path(__file__).resolve().parents[2]).resolve()


def run(
    argv: Sequence[str],
    cwd: Path,
    env: dict[str, str] | None = None,
    *,
    check: bool = False,
) -> subprocess.CompletedProcess[str]:
    environment = {**(os.environ if env is None else env), "PYTHONUTF8": "1"}
    try:
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
        raise WeeklyError(f"`{' '.join(argv)}` exited {result.returncode}: {result.stderr.strip()[-2000:]}")
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


def load_references(base: Path) -> ModuleType:
    """`fern-references.py` over `base`: the per-family recipe whose item lists
    and case tables the planner calls rather than re-parses. The module reads
    its root from `CROZIER_FERN_REFERENCES_ROOT` as it loads, so that is set for
    the load and restored after it."""
    previous = os.environ.get("CROZIER_FERN_REFERENCES_ROOT")
    os.environ["CROZIER_FERN_REFERENCES_ROOT"] = str(base)
    try:
        return load_module("fern_references", base / "tools/fern-goldens/fern-references.py")
    finally:
        if previous is None:
            del os.environ["CROZIER_FERN_REFERENCES_ROOT"]
        else:
            os.environ["CROZIER_FERN_REFERENCES_ROOT"] = previous


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


def read_json(path: Path, what: str) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise WeeklyError(f"cannot read the {what} {path} ({error})") from error


def write_json(path: Path, record: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8", newline="\n")


def metadata_record(text: str, where: str) -> dict[str, object]:
    try:
        record = json.loads(text)
    except ValueError as error:
        raise WeeklyError(f"cannot read {where} ({error}); restore it with git checkout -- {METADATA}") from error
    if not isinstance(record, dict):
        raise WeeklyError(f"{where} must be an object; restore it with git checkout -- {METADATA}")
    return record


def certified(base: Path) -> Pair:
    """The pair `metadata.json` declares."""
    try:
        text = (base / METADATA).read_text(encoding="utf-8")
    except OSError as error:
        raise WeeklyError(f"cannot read {METADATA} ({error}); restore it with git checkout -- {METADATA}") from error
    record = metadata_record(text, str(METADATA))
    return Pair.from_json({"cli": record.get("cliVersion"), "generator": record.get("generatorVersion")}, str(METADATA))


def certified_at_base(base: Path) -> Pair:
    """The pair HEAD certifies, whatever the working tree now declares."""
    shown = subprocess.run(
        ["git", "-C", str(base), "cat-file", "blob", f"HEAD:{METADATA.as_posix()}"], capture_output=True, check=False
    )
    if shown.returncode != 0:
        return certified(base)
    record = metadata_record(shown.stdout.decode("utf-8"), f"HEAD:{METADATA}")
    return Pair.from_json(
        {"cli": record.get("cliVersion"), "generator": record.get("generatorVersion")}, f"HEAD:{METADATA}"
    )


def set_pair(base: Path, pair: Pair) -> None:
    """Move `metadata.json`, the pair's one declaration, to `pair`."""
    path = base / METADATA
    record = metadata_record(path.read_text(encoding="utf-8"), str(METADATA))
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


def semantic(version: str) -> tuple[int, int, int]:
    major, minor, patch = version.split(".")
    return int(major), int(minor), int(patch)


# llmlint: ignore-block[async_typed_clients_at_boundaries] Each phase is one CI job that makes these few remote calls one after another: npm and Docker Hub are read once through `curl` (as `fern-goldens` already resolves its tags), and `git` and `gh` are the CLIs the runner authenticates with the workflow's token. The repository's Python tooling stays stdlib-only (AGENTS.md's Python departures), so a typed async client would add a dependency and buy no concurrency.
def newest_cli(base: Path) -> str:
    """The newest stable `fern-api` version npm publishes."""
    fetched = run(["curl", "-fsSL", NPM_URL], base)
    if fetched.returncode != 0:
        raise WeeklyError(f"could not read {NPM_URL}: {fetched.stderr.strip() or fetched.returncode}; re-run later")
    try:
        document = json.loads(fetched.stdout)
    except ValueError as error:
        raise WeeklyError(f"{NPM_URL} returned no package document ({error}); re-run later") from error
    versions = document.get("versions") if isinstance(document, dict) else None
    if not isinstance(versions, dict):
        raise WeeklyError(f"{NPM_URL} returned no `versions` object; re-run later")
    found = [version for version in versions if stable(version)]
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


def gh(repo: str, *args: str) -> subprocess.CompletedProcess[str]:
    return run(["gh", *args, "--repo", repo], Path.cwd())


def gh_objects(listed: subprocess.CompletedProcess[str], what: str) -> list[dict[str, object]]:
    try:
        found = json.loads(listed.stdout or "[]")
    except ValueError as error:
        raise WeeklyError(f"gh printed no JSON listing {what} ({error})") from error
    if not isinstance(found, list) or not all(isinstance(entry, dict) for entry in found):
        raise WeeklyError(f"gh listed {what} as no list of objects")
    return found


@dataclass(frozen=True)
class OpenPull:
    """The open pull request on `fern-goldens/update`, as gh lists it."""

    number: int
    auto_merge: bool


def open_pull(repo: str) -> OpenPull | None:
    listed = gh(repo, "pr", "list", "--head", BRANCH, "--state", "open", "--json", "number,url,autoMergeRequest,labels")
    if listed.returncode != 0:
        raise WeeklyError(f"could not list pull requests: {listed.stderr.strip()}")
    pulls = gh_objects(listed, "pull requests")
    if not pulls:
        return None
    request = pulls[0].get("autoMergeRequest")
    if request is not None and not isinstance(request, dict):
        raise WeeklyError(f"gh listed autoMergeRequest as {request!r}, neither null nor an auto-merge request")
    return OpenPull(field_of(pulls[0], "number", int, "gh pr list"), request is not None)


def ensure_label(repo: str) -> str:
    listed = gh(repo, "label", "list", "--search", LABEL, "--json", "name", "--limit", "100")
    if listed.returncode != 0:
        raise WeeklyError(f"could not list labels: {listed.stderr.strip()}")
    if any(label.get("name") == LABEL for label in gh_objects(listed, "labels")):
        return "present"
    created = gh(repo, "label", "create", LABEL, "--color", "0E8A16", "--description", "Weekly Fern goldens run")
    if created.returncode != 0:
        raise WeeklyError(f"could not create the {LABEL} label: {created.stderr.strip()}")
    return "created"


def push(base: Path, steps: list[Step]) -> None:
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
            mark(steps, f"push {BRANCH}", f"already on the remote at {remote[:12]}")
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
    mark(steps, f"push {BRANCH}", "pushed")


# llmlint: ignore-end[async_typed_clients_at_boundaries]


def parse_selectors(spec: str) -> list[Selector]:
    """A dispatch's subset: comma-separated `family` or `family:item`."""
    selectors = []
    for part in (part.strip() for part in spec.split(",")):
        if not part:
            continue
        family, colon, item = part.partition(":")
        if not NAME.fullmatch(family) or (colon and not NAME.fullmatch(item)):
            raise WeeklyError(f"items selector {part!r} is no `family` or `family:item`")
        selectors.append(Selector(family, item if colon else None))
    return selectors


def checked_pairs(base: Path) -> dict[Pair, str]:
    """The pairs a run recorded crozier as matching, each to the day it checked."""
    path = base / CHECKS
    if not path.is_file():
        return {}
    found = {}
    for row in read_tsv(path, CHECKS_HEADER):
        where = f"{CHECKS} row {row['fern_cli_version']} {row['fern_python_sdk_version']}"
        pair = Pair.from_json({"cli": row["fern_cli_version"], "generator": row["fern_python_sdk_version"]}, where)
        try:
            datetime.date.fromisoformat(row["checked_on"])
        except ValueError as error:
            raise WeeklyError(f"{where}: checked_on {row['checked_on']!r} is no YYYY-MM-DD date") from error
        if row["outcome"] != Outcome.MATCH:
            raise WeeklyError(f"{where}: outcome {row['outcome']!r} is not `match`, the only outcome a run records")
        found[pair] = row["checked_on"]
    return found


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


def inventory(base: Path) -> dict[str, list[str]]:
    """Every family's items, as `fern-references.py list` names them: the same
    listing functions, called in this process rather than once per family."""
    module = load_references(base)
    found = {}
    for family, entry in module.FAMILY.items():
        try:
            found[family] = list(entry.list())
        except (SystemExit, module.ReferenceError, OSError) as error:
            raise WeeklyError(f"`fern-references.py list {family}` failed: {error}") from error
    return found


def select(found: dict[str, list[str]], selectors: list[Selector]) -> dict[str, list[str]]:
    if not selectors:
        return found
    chosen: dict[str, list[str]] = {}
    for selector in selectors:
        family, item = selector.family, selector.item
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
    table: dict[tuple[str, str], float] = {}
    for row in read_tsv(path, TIMINGS_HEADER) if path.is_file() else []:
        key = (row["family"], row["item"])
        where = f"{TIMINGS} row {row['family']} {row['item']}"
        try:
            seconds = float(row["seconds"])
        except ValueError as error:
            raise WeeklyError(f"{where}: seconds is no number") from error
        if not math.isfinite(seconds) or seconds < 0:
            raise WeeklyError(f"{where}: seconds must be a finite, non-negative number")
        if key in table:
            raise WeeklyError(f"{where}: the item has two rows; keep one")
        table[key] = seconds
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
    module = load_references(base)
    keys = [f"{family}\t{item}" for family, items in chosen.items() for item in items]
    grouped = Units(keys)
    for family in SHARED_TABLE_FAMILIES:
        items = chosen.get(family, [])
        for item in items[1:]:
            grouped.join(f"{family}\t{items[0]}", f"{family}\t{item}")
    # llmlint: ignore[changed_behavior_has_e2e] An overlay is generated by fern-overlay-goldens.sh against its corpus golden and decided by crozier-e2e's overlay gate, which rebuilds the full tree from both; the weekly journeys carry every other family end to end, and weekly_test.py holds each real overlay to its golden's shard and order.
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
    """How many bins the units take: from the fewest the total allows under
    `limit` (its lower bound), one more each time longest-processing-time
    packing overflows a bin, and one bin per unit at most (a unit alone past the
    limit cannot be split). It is the minimum whenever the packing reaches the
    lower bound, which the test over the real inventory holds it to."""
    if not weights:
        return 0, []
    count = max(1, math.ceil(sum(weights) / limit))
    while True:
        bins = pack(weights, count)
        if max(sum(weights[i] for i in group) for group in bins) <= limit or count >= len(weights):
            return len(bins), bins
        count += 1


def wall_clock(shard_seconds: list[float]) -> Estimate:
    """The run's predicted minutes, start to pull request: the plan job, the
    shards in waves of the concurrent-job allowance, then assembly, decision
    and publication, each with its job setup."""
    minutes = sorted((JOB_SETUP_MINUTES + seconds / 60 for seconds in shard_seconds), reverse=True)
    waves = [minutes[start : start + CONCURRENT_JOBS] for start in range(0, len(minutes), CONCURRENT_JOBS)]
    stages = {
        "plan": JOB_SETUP_MINUTES + PLAN_MINUTES,
        "shards": sum(wave[0] for wave in waves),
        "assembly": JOB_SETUP_MINUTES + ASSEMBLY_MINUTES,
        "decision": JOB_SETUP_MINUTES + DECISION_MINUTES,
        "publication": JOB_SETUP_MINUTES + PUBLISH_MINUTES,
    }
    return Estimate(
        minutes=round(sum(stages.values()), 2),
        stages={name: round(value, 2) for name, value in stages.items()},
        waves=len(waves),
        setup_minutes_per_job=JOB_SETUP_MINUTES,
        assembly_minutes=round(stages["assembly"], 2),
        longest_shard_minutes=round(minutes[0], 2) if minutes else 0.0,
    )


def make_plan(base: Path, items: str, pair: Pair | None, commit: str | None = None) -> Plan:
    """The plan of `items` (the whole inventory when blank) over `base`'s
    reference inventory and timing table, at `pair`, generated over `commit`."""
    selectors = parse_selectors(items)
    chosen = {family: entries for family, entries in select(inventory(base), selectors).items() if entries}
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
    for index, group in enumerate(bins):
        members = [key for unit in (grouped[i] for i in group) for key in unit]
        seconds = sum(weights[key] for key in members)
        shards.append(
            PlannedShard(
                index=index,
                seconds=round(seconds, 1),
                minutes=round(JOB_SETUP_MINUTES + seconds / 60, 2),
                items=tuple(
                    PlannedItem(key.partition("\t")[0], key.partition("\t")[2], round(weights[key], 1))
                    for key in members
                ),
            )
        )
    return Plan(
        complete=not selectors,
        items=items,
        base=commit,
        pair=pair,
        budget_minutes=BUDGET_MINUTES,
        shard_limit_minutes=round(limit / 60, 2),
        default_seconds=round(default, 2),
        families={
            family: FamilyTotal(len(entries), round(sum(weights[f"{family}\t{item}"] for item in entries), 1))
            for family, entries in chosen.items()
        },
        units=len(grouped),
        shards=tuple(shards),
        estimate=wall_clock(
            [sum(weights[f"{entry.family}\t{entry.item}"] for entry in shard.items) for shard in shards]
        ),
    )


def plan(args: argparse.Namespace) -> int:
    base = root()
    if bool(args.cli) != bool(args.generator):
        raise WeeklyError("--cli and --generator name the pair together; pass both or neither")
    pair = Pair.from_json({"cli": args.cli, "generator": args.generator}, "--cli/--generator") if args.cli else None
    commit = base_of({"base": args.base or None}, "--base")
    made = make_plan(base, args.items, pair, commit)
    for destination in (args.output, args.telemetry):
        if destination:
            write_json(Path(destination), made.to_json())
    count = len(made.shards)
    write_outputs(args.github_output, {"matrix": json.dumps({"shard": list(range(count))}), "shards": str(count)})
    total = sum(family.items for family in made.families.values())
    summarize(
        args.summary,
        [
            "## Fern goldens: plan",
            "",
            f"{total} item(s) in {made.units} unit(s), {count} shard(s) of at most "
            f"{made.shard_limit_minutes} generation minutes; predicted {made.estimate.minutes} minutes "
            f"start to pull request (budget {BUDGET_MINUTES:g}).",
            "",
            "| family | items | predicted seconds |",
            "|---|---:|---:|",
            *(f"| {name} | {family.items} | {family.seconds} |" for name, family in made.families.items()),
        ],
    )
    print(
        f"fern-goldens-weekly: planned {total} item(s) in {count} shard(s), {made.estimate.minutes} minutes predicted"
    )
    return 0


def read_plan(path: Path) -> Plan:
    return Plan.from_json(read_json(path, "plan"), str(path))


def committed_digest(base: Path, path: str) -> str | None:
    """The digest of `path`'s committed bytes, or None when HEAD has no such file."""
    shown = subprocess.run(
        ["git", "-C", str(base), "cat-file", "blob", f"HEAD:{path}"], capture_output=True, check=False
    )
    return hashlib.sha256(shown.stdout).hexdigest() if shown.returncode == 0 else None


def digest_of(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def dirty(base: Path) -> dict[str, str | None]:
    """Every path that differs from HEAD — modified, deleted, or new and not
    ignored — to its content digest (None when deleted). `ls-files -z` prints
    bare paths, so nothing is parsed off a status prefix."""
    listed = run(
        ["git", "-C", str(base), "ls-files", "-z", "--modified", "--deleted", "--others", "--exclude-standard"],
        base,
        check=True,
    )
    return {path: digest_of(base / path) for path in listed.stdout.split("\0") if path}


def changed_between(base: Path, before: dict[str, str | None], after: dict[str, str | None]) -> list[str]:
    paths = []
    for path in sorted({*before, *after}):
        was = before[path] if path in before else committed_digest(base, path)
        if was != digest_of(base / path):
            paths.append(path)
    return paths


def listed_fixtures(path: Path) -> dict[str, str]:
    """A `fern-goldens` report's fixtures, each to the detail after its tab."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return {}
    return {line.split("\t")[0]: line.partition("\t")[2] for line in lines if line}


def delegate_logs(base: Path, since: float) -> list[Path]:
    """The logs the recipe and its delegates wrote while one item generated."""
    found = []
    for directory in (base / FERN_REFERENCES_LOGS, base / FERN_GOLDENS_REPORT / "generation-logs"):
        if directory.is_dir():
            found += [path for path in directory.rglob("*") if path.is_file() and path.stat().st_mtime >= since]
    return sorted(found)


def generate_item(base: Path, entry: PlannedItem, logs: Path) -> ItemResult:
    family, item = entry.family, entry.item
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
    status, detail = Status.OK, ""
    if result.returncode != 0:
        unfetchable = listed_fixtures(base / FERN_GOLDENS_REPORT / "fetch-failures.txt") if family == "corpus" else {}
        if item in unfetchable:
            status, detail = Status.UNFETCHABLE, unfetchable[item]
        else:
            status = Status.FAILED
            detail = (result.stderr.strip() or result.stdout.strip() or f"exit {result.returncode}").splitlines()[-1]
    elif family == "corpus" and item in listed_fixtures(base / FERN_GOLDENS_REPORT / "known-upstream-failures.txt"):
        status, detail = Status.KNOWN, "the exact known upstream Fern failure, reproduced"
    return ItemResult(
        family=family,
        item=item,
        status=status,
        detail=detail,
        seconds=round(seconds, 1),
        changed=tuple(changed_between(base, before, dirty(base))),
        log=log.relative_to(logs.parent).as_posix(),
    )


def shard(args: argparse.Namespace) -> int:
    base = root()
    made = read_plan(Path(args.plan))
    if not 0 <= args.index < len(made.shards):
        raise WeeklyError(f"the plan has {len(made.shards)} shard(s), not index {args.index}")
    pair = made.candidate()
    head = git(base, "rev-parse", "HEAD")
    if made.base and head != made.base:
        raise WeeklyError(
            f"the plan was made over {made.base}, but this checkout is at {head}; check out the plan's commit"
        )
    output = Path(args.output).resolve()
    if output.exists():
        shutil.rmtree(output)
    (output / "files").mkdir(parents=True)
    set_pair(base, pair)
    results = [generate_item(base, entry, output / "logs") for entry in made.shards[args.index].items]
    written, deleted = [], []
    for path in sorted({path for result in results for path in result.changed}):
        source = base / path
        if source.is_file():
            target = output / "files" / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            written.append(path)
        else:
            deleted.append(path)
    record = ShardResult(args.index, pair, made.base, tuple(results), tuple(written), tuple(deleted))
    write_json(output / "result.json", record.to_json())
    failed = [result for result in results if result.status == Status.FAILED]
    counts = {status: sum(result.status == status for result in results) for status in Status}
    summarize(
        args.summary,
        [
            f"## Fern goldens: shard {args.index}",
            "",
            f"{len(results)} item(s) at {pair.label()}: "
            + ", ".join(f"{count} {status.value}" for status, count in counts.items()),
            *(
                f"- {result.family} `{result.item}`: {result.status.value}: {result.detail}"
                for result in results
                if result.status != Status.OK
            ),
        ],
    )
    print(f"fern-goldens-weekly: shard {args.index}: {len(results)} item(s), {len(failed)} failed")
    for result in failed:
        print(f"{result.family} {result.item}: {result.detail} (log {result.log})", file=sys.stderr)
    return 1 if failed else 0


def uploaded_results(shards_dir: Path, failures: list[str]) -> dict[int, tuple[Path, ShardResult]]:
    """Every shard result under the downloaded artifacts, by its index."""
    uploaded: dict[int, tuple[Path, ShardResult]] = {}
    for path in sorted(shards_dir.rglob("result.json")):
        try:
            record = ShardResult.from_json(read_json(path, "shard result"), str(path))
        except WeeklyError as error:
            failures.append(str(error))
            continue
        if record.index in uploaded:
            failures.append(f"shard {record.index} uploaded two results ({uploaded[record.index][0]} and {path})")
        uploaded[record.index] = (path.parent, record)
    return uploaded


def unplanned(uploaded: dict[int, tuple[Path, ShardResult]], made: Plan) -> list[str]:
    """A failure for every uploaded result no planned shard accounts for."""
    planned = {shard.index for shard in made.shards}
    return [f"shard {index} uploaded a result the plan has no shard for" for index in sorted(set(uploaded) - planned)]


def assemble(args: argparse.Namespace) -> int:
    base = root()
    made = read_plan(Path(args.plan))
    pair = made.candidate()
    output = Path(args.output).resolve()
    if output.exists():
        shutil.rmtree(output)
    (output / "files").mkdir(parents=True)
    failures: list[str] = []
    results: list[ItemResult] = []
    owners: dict[str, int] = {}
    deleted: list[str] = []
    uploaded = uploaded_results(Path(args.shards), failures)
    failures += unplanned(uploaded, made)
    for planned in made.shards:
        index = planned.index
        if index not in uploaded:
            failures.append(f"shard {index} uploaded no result; its job failed or was cancelled before uploading")
            continue
        shard_dir, record = uploaded[index]
        expected = [entry.key() for entry in planned.items]
        reported = [(entry.family, entry.item) for entry in record.items]
        if record.pair != pair or record.base != made.base:
            failures.append(f"shard {index} generated at another pair or base than the plan")
            continue
        if reported != expected:
            missing = [f"{family} {item}" for family, item in expected if (family, item) not in reported]
            failures.append(
                f"shard {index} does not account for its planned items"
                + (f": missing {', '.join(missing)}" if missing else ": its items differ from the plan")
            )
            continue
        for path in (*record.written, *record.deleted):
            if path in owners and owners[path] != index:
                failures.append(f"{path} was written by shards {owners[path]} and {index}; plan their items together")
            owners[path] = index
        carried = {
            source.relative_to(shard_dir / "files").as_posix()
            for source in regular_files(shard_dir / "files", f"shard {index}")
        }
        changed = {path for entry in record.items for path in entry.changed}
        inventory = set(record.written) | set(record.deleted)
        if set(record.written) & set(record.deleted) or changed != inventory or carried - set(record.written):
            failures.append(
                f"shard {index}'s files disagree with what its items wrote: written {sorted(record.written)}, "
                f"deleted {sorted(record.deleted)}, changed {sorted(changed)}, carried {sorted(carried)}"
            )
            continue
        for path in record.written:
            if path not in carried:
                failures.append(f"shard {index} lists {path} but its artifact does not carry it")
                continue
            target = inside(output / "files", path, f"shard {index}")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(shard_dir / "files" / path, target)
        deleted += record.deleted
        if (shard_dir / "logs").is_dir():
            shutil.copytree(shard_dir / "logs", output / "logs", dirs_exist_ok=True)
        for entry in record.items:
            results.append(replace(entry, shard=index))
            if entry.status == Status.FAILED:
                failures.append(f"{entry.family} {entry.item}: generation failed: {entry.detail} (log {entry.log})")
    write_timings(base, made, results, output / "files" / TIMINGS)
    metadata = output / "files" / METADATA
    metadata.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(base / METADATA, metadata)
    set_pair(output / "files", pair)
    unfetchable = [entry for entry in results if entry.status == Status.UNFETCHABLE]
    bundle = Bundle(pair, made.base, made.complete, tuple(results), tuple(sorted(set(deleted))), tuple(failures))
    write_json(output / "bundle.json", bundle.to_json())
    summarize(
        args.summary,
        [
            "## Fern goldens: assembly",
            "",
            f"{len(results)} item(s) from {len(made.shards)} shard(s) at {pair.label()}; "
            f"{len(unfetchable)} with an unfetchable upstream specification; {len(failures)} failure(s).",
            *(f"- **failure**: {failure}" for failure in failures),
            *(f"- not regenerated: corpus `{entry.item}`: {entry.detail}" for entry in unfetchable),
        ],
    )
    if failures:
        print("fern-goldens-weekly: assembly failed:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1
    print(f"fern-goldens-weekly: assembled {len(results)} item(s) from {len(made.shards)} shard(s)")
    return 0


def write_timings(base: Path, made: Plan, results: list[ItemResult], destination: Path) -> None:
    """The timing table with every measured item's seconds in place of its
    row; an item that did not run keeps its row, and a complete run drops the
    rows of items no longer in the inventory."""
    table, _default = timings(base)
    for entry in results:
        if entry.status in (Status.OK, Status.KNOWN):
            table[(entry.family, entry.item)] = entry.seconds
    if made.complete:
        planned = {entry.key() for shard_plan in made.shards for entry in shard_plan.items}
        table = {key: value for key, value in table.items() if key in planned}
    families = list(made.families)

    def order(key: tuple[str, str]) -> tuple[int, str]:
        return (families.index(key[0]) if key[0] in families else len(families), key[1])

    write_tsv(
        destination,
        TIMINGS_HEADER,
        ([family, item, f"{table[(family, item)]:.1f}"] for family, item in sorted(table, key=order)),
        TIMINGS_NOTE,
    )


def bundle_digest(path: Path) -> str:
    """The digest of a bundle — its record and every file it carries, each by
    path and content — which a decision names to bind itself to the one tree it
    decided."""
    digest = hashlib.sha256()
    try:
        digest.update((path / "bundle.json").read_bytes())
        files = path / "files"
        for source in sorted(p for p in files.rglob("*") if p.is_file()) if files.is_dir() else []:
            content = source.read_bytes()
            digest.update(f"\0{source.relative_to(files).as_posix()}\0{len(content)}\0".encode())
            digest.update(content)
    except OSError as error:
        raise WeeklyError(f"cannot read the bundle {path} ({error}); re-run the assembly job") from error
    return digest.hexdigest()


def read_bundle(path: Path) -> Bundle:
    bundle = Bundle.from_json(read_json(path / "bundle.json", "assembled bundle"), str(path / "bundle.json"))
    if bundle.failures:
        raise WeeklyError(f"{path} is a failed assembly; nothing from it may be decided or published")
    return bundle


def apply_bundle(base: Path, path: Path) -> Bundle:
    bundle = read_bundle(path)
    head = git(base, "rev-parse", "HEAD")
    if bundle.base and head != bundle.base:
        raise WeeklyError(f"the bundle was generated over {bundle.base}, but this checkout is at {head}")
    files = path / "files"
    for source in regular_files(files, str(path)):
        target = inside(base, source.relative_to(files).as_posix(), str(path))
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    for relative in bundle.deleted:
        target = inside(base, relative, str(path))
        if target.is_file():
            target.unlink()
    restated = run([sys.executable, str(base / "tools/fern-goldens/certified_pair.py"), "restate", str(base)], base)
    if restated.returncode != 0:
        raise WeeklyError(f"restating the pair failed: {restated.stderr.strip()}")
    return bundle


def verify_applied(base: Path, path: Path, bundle: Bundle) -> None:
    """Refuse to decide over a checkout the bundle was not laid over: every file
    it carries must be there byte for byte, every file it deletes gone, and the
    declared pair its own."""
    files = path / "files"
    for source in regular_files(files, str(path)):
        relative = source.relative_to(files).as_posix()
        target = inside(base, relative, str(path))
        if not target.is_file() or target.read_bytes() != source.read_bytes():
            raise WeeklyError(f"this checkout does not carry the bundle's {relative}; run `apply` before `decide`")
    for relative in bundle.deleted:
        if inside(base, relative, str(path)).exists():
            raise WeeklyError(
                f"this checkout still has {relative}, which the bundle deletes; run `apply` before `decide`"
            )
    if certified(base) != bundle.pair:
        raise WeeklyError(f"this checkout declares {certified(base).label()}, not the bundle's {bundle.pair.label()}")


def apply(args: argparse.Namespace) -> int:
    bundle = apply_bundle(root(), Path(args.bundle))
    print(f"fern-goldens-weekly: applied {len(bundle.items)} item(s) at {bundle.pair.label()}")
    return 0


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


def gates(base: Path, families: Iterable[str] | None = None) -> list[Gate]:
    known = set(families) if families is not None else None
    found = []
    for row in read_tsv(base / GATES, GATES_HEADER):
        where = f"{GATES}: {row['family']} `{row['command']}`"
        named = tuple(name for name in row["family"].split(",") if name)
        if row["scope"] not in ("item", "family") or not named:
            raise WeeklyError(f"{where}: scope is item or family, and a family is named")
        if known is not None and not set(named) <= known:
            raise WeeklyError(f"{where}: {', '.join(sorted(set(named) - known))} is no reference family")
        try:
            words = shlex.split(row["command"])
        except ValueError as error:
            raise WeeklyError(f"{where}: the command does not parse ({error})") from error
        if not [word for word in words if not re.fullmatch(r"[A-Z_][A-Z0-9_]*=.*", word)]:
            raise WeeklyError(f"{where}: the command names nothing to run")
        passes: tuple[int, ...] = ()
        rejects: tuple[int, ...] = ()
        if row["verdict"] != "fixtures-report":
            match = re.fullmatch(r"exit:([0-9,]+)/([0-9,]+)", row["verdict"])
            if match is None:
                raise WeeklyError(f"{where}: verdict {row['verdict']!r} is fixtures-report or exit:PASS/REJECT")
            passes = tuple(int(code) for code in match.group(1).split(",") if code)
            rejects = tuple(int(code) for code in match.group(2).split(",") if code)
            if set(passes) & set(rejects) or not passes or not rejects:
                raise WeeklyError(f"{where}: verdict {row['verdict']!r} names each exit once, as a pass or a rejection")
        found.append(Gate(named, row["scope"] == "item", row["verdict"], passes, rejects, row["command"]))
    return found


@dataclass(frozen=True)
class GateResult:
    verdict: Verdict
    report: str
    exit: int | None = None


DIFFS = re.compile(r"(?m)^(\d+) differing file\(s\) across the reported corpora\.$")
GENERATION = re.compile(r"(?m)^(\d+) comparison generation failure\(s\) across the reported corpora\.$")
PROCESSING = re.compile(r"(?m)^(\d+) comparison processing failure\(s\) across the reported corpora\.$")
REGRESSION = re.compile(r"(?m)^--- .* \[REGRESSION")
SETUP = re.compile(r"(?m)^  Comparison setup failed: ")


# llmlint: ignore[changed_behavior_has_e2e] `report_fixture_diffs` is crozier-e2e's ignored reporter over a committed corpus golden, so driving it needs the whole fixture tree and the e2e build; tools/fern-goldens/tests/weekly_test.py drives this reader over the reporter's own report shapes, and tools/fern-goldens-git/tests/weekly_git_test.py holds those shapes to the strings the reporter prints.
def read_report(code: int, output: str) -> Verdict:
    """The verdict `report_fixture_diffs` (`just fixtures-diff`) states for its
    corpus, read off its own summary: a difference its corpus does not list in
    `unmatched`, a Crozier generation failure or a comparison it could not
    process is a rejection; a setup failure or a report without its summaries
    is a comparison that could not run."""
    summaries = [pattern.search(output) for pattern in (DIFFS, GENERATION, PROCESSING)]
    if code != 0 or any(match is None for match in summaries) or SETUP.search(output):
        return Verdict.CANNOT_RUN
    _diffs, generation, processing = (int(match.group(1)) for match in summaries if match is not None)
    return Verdict.REJECT if REGRESSION.search(output) or generation or processing else Verdict.PASS


def run_gate(base: Path, gate: Gate, item: str | None) -> GateResult:
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
            return GateResult(Verdict.CANNOT_RUN, str(error))
    output = (result.stdout or "") + (result.stderr or "")
    if gate.verdict == "fixtures-report":
        return GateResult(read_report(result.returncode, output), output, result.returncode)
    if result.returncode in gate.passes:
        return GateResult(Verdict.PASS, output, result.returncode)
    if result.returncode in gate.rejects:
        return GateResult(Verdict.REJECT, output, result.returncode)
    return GateResult(Verdict.CANNOT_RUN, output, result.returncode)


def excerpt(report: str, tokens: Iterable[str], context: int = 4, limit: int = 80) -> str:
    """The lines of a family gate's own report that name an item, with the
    lines after each, which is how the report attributes a failure. A token
    names the item only standing alone: `lantern` in `handwritten/lantern/` or
    `lantern: …`, never inside `types/lantern.py` or `alpha_lanterns`."""
    edge = r"[A-Za-z0-9_.-]"
    wanted = [re.compile(rf"(?<!{edge}){re.escape(token)}(?!{edge})") for token in tokens if token]
    lines = report.splitlines()
    keep: set[int] = set()
    for number, line in enumerate(lines):
        if any(pattern.search(line) for pattern in wanted):
            keep.update(range(number, min(number + context + 1, len(lines))))
    return "\n".join(lines[number] for number in sorted(keep)[:limit])


def record_gate(
    decision: Decision, reports: Path, gate: Gate, family: str, item: str | None, result: GateResult
) -> None:
    name = f"{len(decision.gates):04d}-{safe_name(family)}{'-' + safe_name(item) if item else ''}.log"
    (reports / name).write_text(result.report, encoding="utf-8", newline="\n")
    decision.gates.append(GateRun(gate.command, family, item, result.verdict, result.exit, name))
    if result.verdict == Verdict.CANNOT_RUN:
        decision.cannot_run.append(
            f"`{gate.command}`{f' for {family} `{item}`' if item else ''} could not run "
            f"(exit {result.exit}); see {name}"
        )


def attribute(
    decision: Decision, gate: Gate, families: list[str], items: dict[str, list[ItemResult]], report: str
) -> None:
    """A rejecting family gate's report, split over the items it names: each
    item whose name or regenerated files appear in it, with those lines; the
    report's tail under the first family when it names none."""
    named = False
    for family in families:
        for entry in items[family]:
            part = excerpt(report, [entry.item, *entry.changed])
            if not part:
                continue
            named = True
            listed = decision.failing.setdefault(family, [])
            if not any(existing.item == entry.item for existing in listed):
                listed.append(FailingItem(entry.item, f"`{gate.command}`:\n{part}"))
    if not named:
        tail = "\n".join(report.splitlines()[-80:])
        decision.failing.setdefault(families[0], []).append(
            FailingItem("(the gate's report names no item)", f"`{gate.command}`:\n{tail}")
        )


def decide_bundle(base: Path, bundle: Bundle, digest: str, reports: Path, families: Iterable[str]) -> Decision:
    decision = Decision(bundle.pair, bundle.complete, digest)
    items: dict[str, list[ItemResult]] = {}
    for entry in bundle.items:
        if entry.status == Status.UNFETCHABLE:
            decision.unfetchable.append(Unfetchable(entry.item, entry.detail))
        else:
            items.setdefault(entry.family, []).append(entry)
    reports.mkdir(parents=True, exist_ok=True)
    # A command several family rows name runs once, and its report is split over
    # every family those rows name.
    shared: dict[str, tuple[Gate, list[str]]] = {}
    table = gates(base, families)
    undecided = sorted(set(items) - {family for gate in table for family in gate.families})
    if undecided:
        raise WeeklyError(f"{GATES} names no comparison for {', '.join(undecided)}; add the gate that decides it")
    for gate in table:
        decided = [family for family in gate.families if family in items]
        if not decided:
            continue
        if not gate.per_item:
            _first, named = shared.setdefault(gate.command, (gate, []))
            named.extend(family for family in decided if family not in named)
            continue
        for family in decided:
            for entry in items[family]:
                result = run_gate(base, gate, entry.item)
                record_gate(decision, reports, gate, family, entry.item, result)
                if result.verdict == Verdict.REJECT:
                    decision.failing.setdefault(family, []).append(FailingItem(entry.item, result.report.strip()))
    for gate, named in shared.values():
        result = run_gate(base, gate, None)
        record_gate(decision, reports, gate, ",".join(named), None, result)
        if result.verdict == Verdict.REJECT:
            attribute(decision, gate, named, items, result.report)
    return decision


def fenced(text: str) -> str:
    longest = max((len(ticks) for ticks in re.findall(r"`+", text)), default=0)
    fence = "`" * max(3, longest + 1)
    return f"{fence}text\n{text}\n{fence}"


def body(decision: Decision, bundle: Bundle, current: Pair) -> str:
    run_url = ""
    if os.environ.get("GITHUB_RUN_ID") and os.environ.get("GITHUB_REPOSITORY"):
        server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
        run_url = f"{server}/{os.environ['GITHUB_REPOSITORY']}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
    families: dict[str, int] = {}
    for entry in bundle.items:
        families[entry.family] = families.get(entry.family, 0) + 1
    lines = [
        "## What",
        "",
        f"The weekly Fern goldens run regenerated every committed Fern reference at {decision.pair.label()} "
        f"(certified: {current.label()}) and compared crozier's output with each through crozier's own comparison.",
        "",
    ]
    if decision.outcome == Outcome.MATCH:
        lines.append(
            "**No diff**: crozier's output matches every regenerated reference, so this adopts the pair: "
            "`assets/scaffolding/metadata.json`, every statement of the pair, the regenerated references, the "
            "measured generation seconds and a `tests/fixtures/fern-pair-checks.tsv` row. It merges itself once "
            "crozier's required checks pass."
        )
    else:
        failing = sum(len(entries) for entries in decision.failing.values())
        unfetchable = (
            f", and {len(decision.unfetchable)} reference(s) could not be regenerated" if decision.unfetchable else ""
        )
        lines.append(
            f"**Diff**: crozier's comparison fails for {failing} item(s){unfetchable}. This carries the regenerated "
            "references and the new pair; crozier's checks on it show what crozier must change. It is not auto-merged."
        )
    lines += ["", "## Why", "", "Fern released a new version; crozier promises to match the Fern its users run.", ""]
    if decision.failing:
        lines += ["## Failing items", ""]
        budget = BODY_LIMIT // max(1, sum(len(entries) for entries in decision.failing.values()))
        limit = min(REPORT_LIMIT, max(400, budget))
        for family, entries in decision.failing.items():
            lines += [f"### {family} ({len(entries)})", ""]
            for entry in entries:
                report = entry.report
                if len(report) > limit:
                    report = report[:limit] + "\n… (truncated; the decision artifact holds the whole report)"
                lines += [f"- `{entry.item}`", "", "<details><summary>report</summary>", "", fenced(report), ""]
                lines += ["</details>", ""]
    if decision.unfetchable:
        lines += ["## Not regenerated: upstream specification unavailable", ""]
        lines += [f"- corpus `{entry.item}`: {entry.detail}" for entry in decision.unfetchable]
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
    verify_applied(base, Path(args.bundle), bundle)
    current = certified_at_base(base)
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    decision = decide_bundle(
        base, bundle, bundle_digest(Path(args.bundle)), output / "reports", load_references(base).FAMILY
    )
    write_json(output / "decision.json", decision.to_json())
    (output / "body.md").write_text(body(decision, bundle, current), encoding="utf-8", newline="\n")
    failing = [f"{family} `{entry.item}`" for family, entries in decision.failing.items() for entry in entries]
    summarize(
        args.summary,
        [
            "## Fern goldens: decision",
            "",
            f"**{decision.outcome.value}** at {decision.pair.label()}"
            + ("" if decision.complete else " (a diagnostic subset: nothing is published)"),
            *(f"- **cannot run**: {line}" for line in decision.cannot_run),
            *(f"- differs: {line}" for line in failing),
            *(f"- not regenerated: corpus `{entry.item}`: {entry.detail}" for entry in decision.unfetchable),
        ],
    )
    print(f"fern-goldens-weekly: decision {decision.outcome.value}: {len(failing)} failing item(s)")
    if decision.cannot_run:
        for line in decision.cannot_run:
            print(f"  cannot run: {line}", file=sys.stderr)
        return 1
    return 0


def mark(steps: list[Step], name: str, outcome: str) -> None:
    steps.append(Step(name, outcome))
    print(f"fern-goldens-weekly: publish: {name}: {outcome}")


def commit_tree(base: Path, bundle_path: Path, decision: RecordedDecision, checked_on: str) -> None:
    """The one commit the pull request carries, on the planned base."""
    apply_bundle(base, bundle_path)
    if decision.outcome == Outcome.MATCH:
        path = base / CHECKS
        rows = read_tsv(path, CHECKS_HEADER) if path.is_file() else []
        rows.append(
            dict(zip(CHECKS_HEADER, (decision.pair.cli, decision.pair.generator, checked_on, "match"), strict=True))
        )
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
        decision.title,
    )


def open_or_update(repo: str, decision: RecordedDecision, body_file: str, steps: list[Step]) -> OpenPull:
    pull = open_pull(repo)
    if pull is None:
        created = gh(
            repo,
            "pr",
            "create",
            "--base",
            BASE,
            "--head",
            BRANCH,
            "--title",
            decision.title,
            "--body-file",
            body_file,
            "--label",
            LABEL,
        )
        if created.returncode != 0:
            raise WeeklyError(f"opening the pull request failed: {created.stderr.strip()}")
        pull = open_pull(repo)
        if pull is None:
            raise WeeklyError("the pull request gh reported opened is not listed open")
        mark(steps, "pull request", f"opened #{pull.number}")
        return pull
    edited = gh(
        repo,
        "pr",
        "edit",
        str(pull.number),
        "--title",
        decision.title,
        "--body-file",
        body_file,
        "--add-label",
        LABEL,
    )
    if edited.returncode != 0:
        raise WeeklyError(f"updating pull request #{pull.number} failed: {edited.stderr.strip()}")
    mark(steps, "pull request", f"updated #{pull.number}")
    return pull


def settle_auto_merge(repo: str, decision: RecordedDecision, pull: OpenPull, steps: list[Step]) -> None:
    """Auto-merge on for a match, off for a diff, each only when not already so."""
    number = str(pull.number)
    if decision.outcome == Outcome.MATCH:
        if pull.auto_merge:
            mark(steps, "auto-merge", "already enabled")
            return
        merged = gh(repo, "pr", "merge", number, "--auto", "--squash")
        if merged.returncode != 0:
            raise WeeklyError(f"enabling auto-merge on #{number} failed: {merged.stderr.strip()}")
        mark(steps, "auto-merge", "enabled")
    elif pull.auto_merge:
        disabled = gh(repo, "pr", "merge", number, "--disable-auto")
        if disabled.returncode != 0:
            raise WeeklyError(f"turning off auto-merge on #{number} failed: {disabled.stderr.strip()}")
        mark(steps, "auto-merge", "turned off: a diff waits for a person")
    else:
        mark(steps, "auto-merge", "off: a diff waits for a person")


def publish(args: argparse.Namespace) -> int:
    base = root()
    steps: list[Step] = []
    try:
        decision = RecordedDecision.from_json(
            read_json(Path(args.decision) / "decision.json", "decision"), str(Path(args.decision) / "decision.json")
        )
        bundle = read_bundle(Path(args.bundle))
        if decision.outcome not in (Outcome.MATCH, Outcome.DIFF):
            raise WeeklyError(f"the decision is {decision.outcome.value!r}; only a match or a diff is published")
        if not decision.complete or not bundle.complete:
            raise WeeklyError("a diagnostic subset run never publishes, adopts or records a pair")
        if decision.pair != bundle.pair:
            raise WeeklyError(f"the decision is at {decision.pair.label()}, the bundle at {bundle.pair.label()}")
        if decision.bundle != bundle_digest(Path(args.bundle)):
            raise WeeklyError("the decision was made over another bundle than this one; re-run the decision job")
        if not os.environ.get("GH_TOKEN"):
            raise WeeklyError(
                "GH_TOKEN (the workflow's RELEASE_PLZ_TOKEN) is not set; add the secret, then re-run. Nothing was pushed."
            )
        checked_on = args.checked_on or datetime.datetime.now(datetime.UTC).date().isoformat()
        try:
            datetime.date.fromisoformat(checked_on)
        except ValueError as error:
            raise WeeklyError(f"--checked-on {checked_on!r} is no YYYY-MM-DD date") from error
        commit_tree(base, Path(args.bundle), decision, checked_on)
        mark(steps, "commit", git(base, "rev-parse", "--short=12", "HEAD"))
        push(base, steps)
        # Every write reads the remote first: a branch already holding this tree,
        # a present label and auto-merge already as wanted are left alone, and an
        # open pull request is updated rather than duplicated, so a run after a
        # failure or a lost response finishes the rest. A write that fails ends the
        # run red, whatever the remote may since have applied.
        mark(steps, f"label {LABEL}", ensure_label(args.repo))
        pull = open_or_update(args.repo, decision, str(Path(args.decision) / "body.md"), steps)
        settle_auto_merge(args.repo, decision, pull, steps)
    except WeeklyError as error:
        completed = [f"- {step.name}: {step.outcome}" for step in steps] or ["- none"]
        summarize(
            args.summary,
            [
                "## Fern goldens: publication failed",
                "",
                f"**{error}**",
                "",
                "Steps completed before it:",
                *completed,
                "",
                "The next run reconciles from the remote: it reuses the branch and pull request and finishes the rest.",
            ],
        )
        print(f"fern-goldens-weekly: publication failed: {error}", file=sys.stderr)
        return 1
    summarize(args.summary, ["## Fern goldens: publication", "", *(f"- {step.name}: {step.outcome}" for step in steps)])
    return 0


PHASES: dict[str, Callable[[argparse.Namespace], int]] = {
    "resolve": resolve,
    "plan": plan,
    "shard": shard,
    "assemble": assemble,
    "apply": apply,
    "decide": decide,
    "publish": publish,
}


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
    phase.add_argument("--base", default="", help="the commit every shard checks out (the workflow's github.sha)")
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
        return PHASES[args.command](args)
    except WeeklyError as error:
        summarize(args.summary, [f"## Fern goldens: {args.command} failed", "", f"**{error}**"])
        print(f"fern-goldens-weekly: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
