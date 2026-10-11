#!/usr/bin/env python3
"""Reconcile the scenario proof index and the handed-off witnesses with the catalogs they cite.

`docs/openapi-surface/scenario-proof-index.tsv` names, once per parity scenario
shape, the committed proof that closes it: a registered corpus golden, a
hand-written fixture, a measurement, or a refusal class. Every fact a row
repeats from another catalog is re-derived here from that catalog and compared,
so a row cannot drift from what it cites:

* a golden must be a complete certified tree (`.fern/metadata.json` naming the
  pinned Fern pair) that `tests/fixtures/compared-goldens.json` inventories, its
  `settings` cell is read off that metadata, and its `outcome`/`ids` cells are
  the `fern-defect` entries of `assets/departures.yml` that
  `tests/fixtures/departures-ledger.tsv` applies to it;
* a refusal names a `docs/fern-refusals/classes.tsv` class whose `status` fixes
  both mode outcomes, and whose evaluation note names every probe the row cites;
* every source, evidence document and anchor exists, and every test is a
  `#[test]` of the e2e crate.

`docs/fern-measurements/blocked-witnesses/witnesses.tsv` lists every real
publisher specification handed off for registration. A registered one names its
committed corpus row; one that still differs names its committed comparison
diff, and `residuals.tsv` attributes every hunk of that diff, exactly once, to a
scenario of the index or to `unowned`. Hunks are read from the diff itself.

Two subcommands: ``check`` prints every failure (nothing on success) and exits 1
when there is one; ``hunks DIFF`` prints the hunks of one comparison diff in the
form `residuals.tsv` cites them.
"""

from __future__ import annotations

import argparse
import functools
import importlib.util
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from types import ModuleType
from typing import NamedTuple

import yaml

REPO = Path(__file__).resolve().parents[2]
INDEX = Path("docs/openapi-surface/scenario-proof-index.tsv")
INDEX_HEADER = ("shape", "owner", "kind", "source", "goldens", "settings", "tests", "outcome", "ids", "evidence")
WITNESSES = Path("docs/fern-measurements/blocked-witnesses/witnesses.tsv")
WITNESS_HEADER = ("witness", "source", "revision", "sha256", "status", "corpus", "diff", "evidence")
RESIDUALS = Path("docs/fern-measurements/blocked-witnesses/residuals.tsv")
RESIDUAL_HEADER = ("witness", "file", "hunks", "owner", "shape")
CLASSES = Path("docs/fern-refusals/classes.tsv")
CLASSES_HEADER = (
    "class",
    "family",
    "fern_stage",
    "fern_exit",
    "diagnostic",
    "documents",
    "status",
    "crozier_diagnostic",
    "population_strict",
)
# The plan this index closes owns exactly these many scenario shapes; a row
# removed or added changes the count, so the closure cannot shrink silently.
SHAPES = 160
OWNERS = (
    "bodies-responses",
    "clients-extensions",
    "examples-docs",
    "models-refs",
    "parameters",
    "prove-matches",
    "streaming",
    "unions",
)
KINDS = ("real", "handwritten", "measurement", "refusal")
PIN = ("5.67.1", "5.20.0")
NONE = "—"
UNOWNED = "unowned"
# A refusal class's registry status fixes what crozier does in each mode.
MODE_OUTCOMES = {"refuse": "default=refuse;strict=refuse", "generate": "default=generate;strict=refuse"}
REFUSAL_SETTINGS = "default;fern-strict"
SHAPE_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
E2E_SOURCES = ("crates/crozier-e2e/tests/e2e.rs", "crates/crozier-e2e/tests/e2e")
HANDWRITTEN = "docs/openapi-surface/handwritten/"
E2E_COVERS = "docs/openapi-surface/handwritten-e2e.toml"
MEASUREMENTS = "docs/fern-measurements/"


@functools.cache
def _handwritten() -> ModuleType:
    """The hand-written fixture gate, whose anchor and corpus readers this reuses."""
    path = REPO / "tools" / "surface-census" / "handwritten-fixtures.py"
    spec = importlib.util.spec_from_file_location("scenario_proof_index_handwritten", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_tsv(path: Path, header: tuple[str, ...]) -> tuple[list[dict[str, str]], list[str]]:
    """Rows of a tab-separated file whose first line must be `header`."""
    if not path.is_file():
        return [], [f"{path}: missing"]
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or tuple(lines[0].split("\t")) != header:
        return [], [f"{path}: header must be the tab-separated {', '.join(header)}"]
    rows, failures = [], []
    for number, line in enumerate(lines[1:], start=2):
        cells = line.split("\t")
        if len(cells) != len(header) or any(not cell.strip() for cell in cells):
            failures.append(f"{path}:{number}: needs {len(header)} non-empty cells")
            continue
        rows.append(dict(zip(header, cells, strict=True)))
    return rows, failures


def split(cell: str) -> list[str]:
    return [] if cell == NONE else [part.strip() for part in cell.split(";")]


class Catalogs(NamedTuple):
    inventory: set[str]
    defects: set[str]
    ledger: dict[str, set[str]]
    classes: dict[str, str]
    tests: set[str]
    corpus: set[str]


def catalogs(root: Path) -> tuple[Catalogs, list[str]]:
    """The authoritative catalogs every row is reconciled with."""
    failures: list[str] = []
    inventory_path = root / "tests" / "fixtures" / "compared-goldens.json"
    inventory = set(json.loads(inventory_path.read_text(encoding="utf-8"))["goldens"])
    catalog = yaml.safe_load((root / "assets" / "departures.yml").read_text(encoding="utf-8"))
    defects = {entry["id"] for entry in catalog if entry["kind"] == "fern-defect"}
    ledger: dict[str, set[str]] = defaultdict(set)
    ledger_lines = (root / "tests" / "fixtures" / "departures-ledger.tsv").read_text(encoding="utf-8").splitlines()
    for line in ledger_lines[1:]:
        golden, _file, _line, departure = line.split("\t")
        ledger[golden].add(departure)
    classes_rows, class_failures = read_tsv(
        root / CLASSES,
        CLASSES_HEADER,
    )
    failures += class_failures
    classes = {row["class"]: row["status"] for row in classes_rows}
    sources = []
    for entry_path in E2E_SOURCES:
        path = root / entry_path
        sources += [path] if path.is_file() else sorted(path.glob("*.rs"))
    # A test is a `fn` of the e2e crate, or a name a `flat_goldens!`-style macro
    # invocation (`name => "fixture"`) expands into one.
    tests = {
        name
        for path in sources
        for found in re.findall(r"(?m)^\s*(?:pub )?fn (\w+)\(|^\s*(\w+) =>", path.read_text(encoding="utf-8"))
        for name in found
        if name
    }
    return Catalogs(inventory, defects, ledger, classes, tests, _handwritten().corpus_rows(root)), failures


def golden_settings(root: Path, golden: str) -> tuple[str | None, list[str]]:
    """A golden's generator settings as the index spells them, read off its metadata."""
    metadata = root / golden / ".fern" / "metadata.json"
    if not metadata.is_file():
        return None, [f"golden {golden} is not a complete certified tree (no .fern/metadata.json)"]
    record = json.loads(metadata.read_text(encoding="utf-8"))
    failures = []
    if (record.get("cliVersion"), record.get("generatorVersion")) != PIN:
        failures.append(f"golden {golden} is not output of Fern CLI {PIN[0]} with fern-python-sdk {PIN[1]}")
    config = record.get("generatorConfig") or {}
    parts = [(config.get("pydantic_config") or {}).get("enum_type", "literals")]
    if golden.endswith("-flat") or "-flat/" in golden:
        parts.append("flat")
    for key, value in sorted(config.items()):
        if key == "pydantic_config":
            parts += [f"{name}={setting}" for name, setting in sorted(value.items()) if name != "enum_type"]
        else:
            parts.append(f"{key}={value}")
    return "+".join(parts), failures


def path_failures(root: Path, where: str, cell: str) -> list[str]:
    failures = []
    for reference in split(cell):
        relative, _, anchor = reference.partition("#")
        path = root / relative
        if not path.exists():
            failures.append(f"{where}: {relative} does not exist")
        elif anchor and anchor not in _handwritten().heading_anchors(path.read_text(encoding="utf-8")):
            failures.append(f"{where}: {relative} has no heading #{anchor}")
    return failures


def test_failures(where: str, cell: str, tests: set[str]) -> list[str]:
    return [f"{where}: no e2e test is named {test}" for test in split(cell) if test not in tests]


def refusal_failures(root: Path, where: str, row: dict[str, str], known: Catalogs) -> list[str]:
    failures = []
    name = row["ids"]
    status = known.classes.get(name)
    if status is None:
        return [f"{where}: {name} is no docs/fern-refusals/classes.tsv class"]
    if row["goldens"] != NONE or row["settings"] != REFUSAL_SETTINGS:
        failures.append(f"{where}: a refusal cites no golden and records `{REFUSAL_SETTINGS}`")
    expected = MODE_OUTCOMES.get(status)
    if row["outcome"] != expected:
        failures.append(f"{where}: outcome {row['outcome']} disagrees with {name}'s registry status {status}")
    note = root / "docs" / "fern-refusals" / name / "evaluation.md"
    if not note.is_file():
        return [*failures, f"{where}: {name} has no evaluation note"]
    if status == "generate" and not (note.parent / "wire_test.py").is_file():
        failures.append(f"{where}: {name} claims default generation without its wire evaluation")
    text = note.read_text(encoding="utf-8")
    for probe in split(row["source"]):
        if Path(probe).name not in text:
            failures.append(f"{where}: {name}'s evaluation note does not name the probe {probe}")
    return failures


def generated_failures(root: Path, where: str, row: dict[str, str], known: Catalogs) -> list[str]:
    goldens = split(row["goldens"])
    if not goldens:
        return [f"{where}: a {row['kind']} proof cites at least one golden"]
    failures, settings, defects = [], [], set()
    for golden in goldens:
        if golden not in known.inventory:
            failures.append(f"{where}: golden {golden} is not in tests/fixtures/compared-goldens.json")
        setting, problems = golden_settings(root, golden)
        failures += [f"{where}: {problem}" for problem in problems]
        settings.append(setting or "?")
        defects |= known.ledger.get(golden, set()) & known.defects
    if row["settings"] != ";".join(settings):
        failures.append(f"{where}: settings {row['settings']} disagree with the goldens' metadata {';'.join(settings)}")
    outcome = "departure" if defects else "match"
    ids = ";".join(sorted(defects)) if defects else NONE
    if (row["outcome"], row["ids"]) != (outcome, ids):
        failures.append(f"{where}: outcome {row['outcome']} {row['ids']} disagrees with the ledger's {outcome} {ids}")
    sources = split(row["source"])
    if row["kind"] == "real" and not any(
        golden.startswith("tests/fixtures/") and golden.split("/")[2] in known.corpus for golden in goldens
    ):
        failures.append(f"{where}: a real proof cites a registered corpus row's golden")
    if row["kind"] == "handwritten" and not any(source.startswith((HANDWRITTEN, MEASUREMENTS)) for source in sources):
        failures.append(f"{where}: a hand-written proof's source is a hand-written fixture")
    if row["kind"] == "handwritten" and any(source.startswith(MEASUREMENTS) for source in sources):
        covers = (root / E2E_COVERS).read_text(encoding="utf-8")
        if not any(f'fixture = "{source}"' in covers for source in sources):
            failures.append(f"{where}: a multi-file hand-written source is a {E2E_COVERS} cover")
    if row["kind"] == "measurement" and not all(golden.startswith(MEASUREMENTS) for golden in goldens):
        failures.append(f"{where}: a measurement proof's goldens are under {MEASUREMENTS}")
    return failures


def index_failures(root: Path) -> list[str]:
    """Every way the scenario proof index disagrees with the catalogs it cites."""
    rows, failures = read_tsv(root / INDEX, INDEX_HEADER)
    known, catalog_failures = catalogs(root)
    failures += catalog_failures
    counts = Counter(row["shape"] for row in rows)
    failures += [f"{INDEX}: {shape} is indexed {count} times" for shape, count in counts.items() if count > 1]
    if len(counts) != SHAPES:
        failures.append(f"{INDEX}: indexes {len(counts)} shapes, not the plan's {SHAPES}")
    if [row["shape"] for row in rows] != sorted(row["shape"] for row in rows):
        failures.append(f"{INDEX}: rows are sorted by shape")
    for row in rows:
        where = f"{INDEX} {row['shape']}"
        if not SHAPE_NAME.match(row["shape"]):
            failures.append(f"{where}: a shape id is lower-kebab")
        if row["owner"] not in OWNERS:
            failures.append(f"{where}: owner {row['owner']} is none of {', '.join(OWNERS)}")
        if row["kind"] not in KINDS:
            failures.append(f"{where}: kind {row['kind']} is none of {', '.join(KINDS)}")
            continue
        failures += path_failures(root, where, row["source"])
        failures += path_failures(root, where, row["evidence"])
        failures += test_failures(where, row["tests"], known.tests)
        if row["kind"] == "refusal":
            failures += refusal_failures(root, where, row, known)
        else:
            failures += generated_failures(root, where, row, known)
    return failures


class Hunk(NamedTuple):
    file: str
    spelling: str


def diff_hunks(text: str) -> list[Hunk]:
    """Each change of a `crozier compare` diff, as `-start,count +start,count` or a one-sided file."""
    hunks: list[Hunk] = []
    current: str | None = None
    reference = crozier = 0
    # The open run of changed lines: its file, its first line on each side, and its length on each.
    run: tuple[str, int, int] | None = None
    removed = added = 0
    for line in [*text.splitlines(), None]:
        changed = current is not None and line is not None and (line[:2] in ("- ", "+ ") or line in ("-", "+"))
        if run is not None and not changed:
            hunks.append(Hunk(run[0], f"-{run[1]},{removed} +{run[2]},{added}"))
            run = None
        if line is None:
            break
        if changed and current is not None:
            if run is None:
                run, removed, added = (current, reference + 1, crozier + 1), 0, 0
            if line.startswith("-"):
                reference, removed = reference + 1, removed + 1
            else:
                crozier, added = crozier + 1, added + 1
        elif line.startswith("--- reference/"):
            current, reference, crozier = line.removeprefix("--- reference/"), 0, 0
        elif line.startswith("+++ crozier/"):
            continue
        elif found := re.match(r"^Only in (reference|crozier): (.+)$", line):
            current = None
            hunks.append(Hunk(found.group(2), f"only in {found.group(1)}"))
        elif current is None:
            continue
        elif found := re.match(r"^\s+⋮ \((\d+) unchanged line\(s\)\)$", line):
            reference += int(found.group(1))
            crozier += int(found.group(1))
        else:
            reference += 1
            crozier += 1
    return hunks


def witness_failures(root: Path, shapes: set[str]) -> list[str]:
    """Every way the handed-off witnesses disagree with the corpus, their diffs and the index."""
    witnesses, failures = read_tsv(root / WITNESSES, WITNESS_HEADER)
    residuals, residual_failures = read_tsv(root / RESIDUALS, RESIDUAL_HEADER)
    failures += residual_failures
    corpus = _handwritten().corpus_rows(root)
    claimed: dict[str, Counter[Hunk]] = defaultdict(Counter)
    for row in residuals:
        where = f"{RESIDUALS} {row['witness']} {row['file']}"
        if row["owner"] != UNOWNED and row["owner"] not in shapes:
            failures.append(f"{where}: owner {row['owner']} is no indexed shape nor {UNOWNED}")
        for spelling in split(row["hunks"]):
            claimed[row["witness"]][Hunk(row["file"], spelling)] += 1
    names = Counter(row["witness"] for row in witnesses)
    failures += [f"{WITNESSES}: {name} is listed {count} times" for name, count in names.items() if count > 1]
    for row in witnesses:
        where = f"{WITNESSES} {row['witness']}"
        failures += path_failures(root, where, row["evidence"])
        if row["status"] == "registered":
            name = row["corpus"].partition(" ")[2].strip("`")
            if name not in corpus or not (root / "tests" / "fixtures" / name / "expected").is_dir():
                failures.append(f"{where}: registered as {row['corpus']}, which is no corpus row with a golden")
            if row["diff"] != NONE or claimed.pop(row["witness"], None):
                failures.append(f"{where}: a registered witness has no comparison diff or residual")
            continue
        if row["status"] != "differs":
            failures.append(f"{where}: status {row['status']} is neither registered nor differs")
            continue
        diff = root / WITNESSES.parent / row["diff"]
        if not diff.is_file():
            failures.append(f"{where}: comparison diff {row['diff']} is missing")
            continue
        expected = Counter(diff_hunks(diff.read_text(encoding="utf-8")))
        found = claimed.pop(row["witness"], Counter())
        for hunk in sorted((expected - found).elements()):
            failures.append(f"{where}: {hunk.file} {hunk.spelling} is in the diff but attributed to no shape")
        for hunk in sorted((found - expected).elements()):
            failures.append(f"{where}: {hunk.file} {hunk.spelling} is attributed but not in the diff (or twice)")
    failures += [f"{RESIDUALS}: {name} is no differing witness" for name in sorted(claimed)]
    return failures


def check(root: Path) -> list[str]:
    rows, _ = read_tsv(root / INDEX, INDEX_HEADER)
    return index_failures(root) + witness_failures(root, {row["shape"] for row in rows})


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--repo-root", type=Path, default=REPO)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="reconcile the index and witnesses; print each failure")
    hunks = sub.add_parser("hunks", help="print a comparison diff's hunks as residuals.tsv cites them")
    hunks.add_argument("diff", type=Path)
    args = parser.parse_args(argv)
    if args.command == "hunks":
        for hunk in diff_hunks(args.diff.read_text(encoding="utf-8")):
            print(f"{hunk.file}\t{hunk.spelling}")
        return 0
    failures = check(args.repo_root)
    for failure in failures:
        print(failure)
    if failures:
        print(f"{len(failures)} failure(s): fix the row or the proof it cites, then re-run", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
