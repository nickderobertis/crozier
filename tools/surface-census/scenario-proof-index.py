#!/usr/bin/env python3
"""Reconcile the scenario proof index and the handed-off witnesses with the catalogs they cite.

`docs/openapi-surface/scenario-plan.tsv` is the parity plan's closure: every
scenario shape it owns and the node that owns it. `scenario-proof-index.tsv`
beside it names, once per planned shape, the committed proof that closes it: a
registered corpus golden, a hand-written fixture, a measurement, or a refusal
class. Every fact a row repeats from another catalog is re-derived here from
that catalog and compared, so a row cannot drift from what it cites:

* the index holds exactly the plan's shapes, each under the plan's owner;
* a golden must be a complete certified tree (`.fern/metadata.json` naming the
  pinned Fern pair) that `tests/fixtures/compared-goldens.json` inventories, its
  `settings` cell is read off that metadata, and its `outcome`/`ids` cells are
  the `fern-defect` entries of `assets/departures.yml` that
  `tests/fixtures/departures-ledger.tsv` applies to it;
* the row's sources are exactly the documents its goldens were generated from,
  in golden order;
* each golden, and each refusal probe, is reached by one of the row's tests: a
  `#[test]` of the e2e crate whose corpus binding, overlay or flat registration
  or hand-written walk covers it, or whose body (or a callee's) names a path
  containing it;
* a refusal names a `docs/fern-refusals/classes.tsv` class whose `status` fixes
  both mode outcomes, and whose evaluation note names every probe the row cites;
* every source, evidence document and anchor exists;
* the `open` cell names exactly the residuals still open on the shape's own
  trigger: each handed-off witness whose `residuals.tsv` hunks the shape owns,
  and `python_enums` when a `python_enums` residual diff of the shape is
  committed. A shape is closed with no residual only when that cell is empty.

`docs/fern-measurements/blocked-witnesses/witnesses.tsv` lists every real
publisher specification handed off for registration. A registered one names its
committed corpus row by number and name; one that still differs names its
committed comparison diff, and `residuals.tsv` attributes every hunk of that
diff, exactly once, to a scenario of the index or to `unowned`. Hunks are read
from the diff itself, which must be well formed.

Three subcommands: ``check`` prints every failure to stderr (nothing on success)
and exits 1 when there is one; ``summary`` prints the counts the coverage report
quotes, read off both tables; ``hunks DIFF`` prints the hunks of one comparison
diff in the form `residuals.tsv` cites them.
"""

from __future__ import annotations

import argparse
import ast
import functools
import importlib.util
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from types import ModuleType
from typing import Any, NamedTuple, NewType

REPO = Path(__file__).resolve().parents[2]
PLAN = Path("docs/openapi-surface/scenario-plan.tsv")
PLAN_HEADER = ("shape", "owner")
INDEX = Path("docs/openapi-surface/scenario-proof-index.tsv")
INDEX_HEADER = (
    "shape",
    "owner",
    "kind",
    "source",
    "goldens",
    "settings",
    "tests",
    "outcome",
    "ids",
    "evidence",
    "open",
)
# A literals-proven shape whose `python_enums` output still differs keeps that diff here, by shape.
PYTHON_ENUMS_RESIDUALS = Path("docs/fern-measurements/python-enums-residuals")
PYTHON_ENUMS = "python_enums"
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
INVENTORY = Path("tests/fixtures/compared-goldens.json")
LEDGER = Path("tests/fixtures/departures-ledger.tsv")
LEDGER_HEADER = ("golden", "file", "line", "departure")
CATALOG = Path("assets/departures.yml")
CORPUS = Path("tests/fixtures/CORPUS.md")
NONE = "—"
UNOWNED = "unowned"
UNEVALUATED = "unevaluated"
REFUSAL_SETTINGS = "default;fern-strict"
SHAPE_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
E2E_SOURCES = ("crates/crozier-e2e/tests/e2e.rs", "crates/crozier-e2e/tests/e2e")
HANDWRITTEN = "docs/openapi-surface/handwritten/"
HANDWRITTEN_TEST = "handwritten_fixtures_match_fern_goldens"
E2E_COVERS = "docs/openapi-surface/handwritten-e2e.toml"
MEASUREMENTS = "docs/fern-measurements/"
# How corpus tests bind their fixtures, as `every_registered_corpus_is_wired_into_the_gate` reads them.
CORPUS_DRIVERS = ("assert_corpus_matches(&", "assert_committed_corpus_matches(&", "known_fern_failure(&")
SETTING_VALUE = (str, int, float, bool)
DOCUMENTS = ("openapi.yml", "openapi.yaml", "openapi.json")

ShapeId = NewType("ShapeId", str)
WitnessName = NewType("WitnessName", str)
DepartureId = NewType("DepartureId", str)
RefusalClass = NewType("RefusalClass", str)
TestName = NewType("TestName", str)


class FernPair(NamedTuple):
    """The certified Fern CLI and fern-python-sdk versions every golden is output of."""

    cli: str
    generator: str


PIN = FernPair(cli="5.67.1", generator="5.20.0")


class EnumType(StrEnum):
    """The fern-python-sdk `enum_type` settings a golden may be generated under."""

    LITERALS = "literals"
    PYTHON_ENUMS = "python_enums"


class Outcome(StrEnum):
    """What a proof shows: a byte match, a catalogued departure, or each mode's refusal outcome."""

    MATCH = "match"
    DEPARTURE = "departure"
    REFUSED = "default=refuse;strict=refuse"
    GENERATED = "default=generate;strict=refuse"


class Owner(StrEnum):
    """The scenario node that settled a shape."""

    BODIES_RESPONSES = "bodies-responses"
    CLIENTS_EXTENSIONS = "clients-extensions"
    EXAMPLES_DOCS = "examples-docs"
    MODELS_REFS = "models-refs"
    PARAMETERS = "parameters"
    PROVE_MATCHES = "prove-matches"
    STREAMING = "streaming"
    UNIONS = "unions"


class Kind(StrEnum):
    """What a shape's proof is: a real golden, a hand-written one, a measurement, or a refusal."""

    REAL = "real"
    HANDWRITTEN = "handwritten"
    MEASUREMENT = "measurement"
    REFUSAL = "refusal"


class RefusalStatus(StrEnum):
    """A refusal class's registry decision, which fixes crozier's outcome in each mode."""

    REFUSE = "refuse"
    GENERATE = "generate"

    @property
    def outcome(self) -> Outcome:
        return Outcome.REFUSED if self is RefusalStatus.REFUSE else Outcome.GENERATED


class WitnessStatus(StrEnum):
    REGISTERED = "registered"
    DIFFERS = "differs"


def values(kind: type[StrEnum]) -> frozenset[str]:
    """The spellings a cell may hold for `kind`."""
    return frozenset(member.value for member in kind)


def split(cell: str) -> tuple[str, ...]:
    """A `;`-separated cell's members; `—` is the empty list, and a blank member is kept for `blank_members`."""
    return () if cell == NONE else tuple(part.strip() for part in cell.split(";"))


LIST_COLUMNS = ("source", "goldens", "tests", "ids", "evidence", "open")


def blank_members(row: dict[str, str], columns: tuple[str, ...]) -> list[str]:
    """The list columns of `row` holding an empty member, which would name the repository root as a path."""
    return [column for column in columns if "" in split(row[column])]


@dataclass(frozen=True)
class Proof:
    """One row of the scenario proof index."""

    shape: ShapeId
    owner: Owner
    kind: Kind
    source: tuple[str, ...]
    goldens: tuple[str, ...]
    settings: str
    tests: tuple[TestName, ...]
    outcome: Outcome
    departures: tuple[DepartureId, ...]
    refusal: RefusalClass | None
    evidence: tuple[str, ...]
    open: tuple[str, ...]

    @property
    def where(self) -> str:
        return f"{INDEX} {self.shape}"

    @property
    def fully_closed(self) -> bool:
        """Closed by its proof with no residual left open on its own trigger."""
        return not self.open


class CorpusRef(NamedTuple):
    """A numbered `CORPUS.md` row and the fixture it registers."""

    number: str
    fixture: str


@dataclass(frozen=True)
class Witness:
    """One handed-off publisher specification."""

    name: WitnessName
    status: WitnessStatus
    corpus: str
    diff: str
    evidence: str

    @property
    def where(self) -> str:
        return f"{WITNESSES} {self.name}"

    @property
    def corpus_row(self) -> CorpusRef:
        """The corpus row a registered witness's `corpus` cell (`<row> \\`<name>\\``) names."""
        number, _, name = self.corpus.partition(" ")
        return CorpusRef(number=number, fixture=name.strip("`"))


@dataclass(frozen=True)
class Residual:
    """One `residuals.tsv` row: hunks of one witness file and the shape that owns them, if any."""

    witness: WitnessName
    file: str
    hunks: tuple[str, ...]
    owner: ShapeId | None


class Hunk(NamedTuple):
    file: str
    spelling: str


@dataclass
class _Run:
    """The open run of changed lines a diff is being read through."""

    file: str
    reference_start: int
    crozier_start: int
    removed: int = 0
    added: int = 0

    @property
    def hunk(self) -> Hunk:
        return Hunk(self.file, f"-{self.reference_start},{self.removed} +{self.crozier_start},{self.added}")


def corpus_fixture(golden: str) -> str | None:
    """The corpus fixture of a `tests/fixtures/<fixture>/<tree>` golden, or None for any other path."""
    parts = golden.split("/")
    return parts[2] if len(parts) == 4 and parts[:2] == ["tests", "fixtures"] and all(parts[2:]) else None


class MalformedDiff(ValueError):
    """A comparison diff that is not `crozier compare`'s normalized diff."""


@functools.cache
def _handwritten() -> ModuleType:
    """The hand-written fixture gate, whose anchor reader this reuses."""
    path = REPO / "tools" / "surface-census" / "handwritten-fixtures.py"
    spec = importlib.util.spec_from_file_location("scenario_proof_index_handwritten", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_tsv(path: Path, header: tuple[str, ...]) -> tuple[list[dict[str, str]], list[str]]:
    """Rows of a tab-separated file whose first line must be `header`, each cell non-empty."""
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


def read_plan(root: Path) -> tuple[dict[ShapeId, Owner], list[str]]:
    rows, failures = read_tsv(root / PLAN, PLAN_HEADER)
    plan: dict[ShapeId, Owner] = {}
    for row in rows:
        if row["owner"] not in values(Owner):
            failures.append(f"{PLAN} {row['shape']}: owner {row['owner']} is none of {', '.join(Owner)}")
        elif row["shape"] in plan:
            failures.append(f"{PLAN}: {row['shape']} is planned twice")
        else:
            plan[ShapeId(row["shape"])] = Owner(row["owner"])
    return plan, failures


def read_proofs(root: Path) -> tuple[list[Proof], list[str]]:
    rows, failures = read_tsv(root / INDEX, INDEX_HEADER)
    proofs = []
    for row in rows:
        where = f"{INDEX} {row['shape']}"
        if row["owner"] not in values(Owner):
            failures.append(f"{where}: owner {row['owner']} is none of {', '.join(Owner)}")
            continue
        if row["kind"] not in values(Kind):
            failures.append(f"{where}: kind {row['kind']} is none of {', '.join(Kind)}")
            continue
        if row["outcome"] not in values(Outcome):
            failures.append(f"{where}: outcome {row['outcome']} is none of {', '.join(Outcome)}")
            continue
        if blank := blank_members(row, LIST_COLUMNS):
            failures.append(f"{where}: {', '.join(blank)} hold an empty `;`-separated member")
            continue
        kind = Kind(row["kind"])
        refusal = kind is Kind.REFUSAL
        proofs.append(
            Proof(
                shape=ShapeId(row["shape"]),
                owner=Owner(row["owner"]),
                kind=kind,
                source=split(row["source"]),
                goldens=split(row["goldens"]),
                settings=row["settings"],
                tests=tuple(TestName(test) for test in split(row["tests"])),
                outcome=Outcome(row["outcome"]),
                departures=() if refusal else tuple(DepartureId(name) for name in split(row["ids"])),
                refusal=RefusalClass(row["ids"]) if refusal else None,
                evidence=split(row["evidence"]),
                open=split(row["open"]),
            )
        )
    return proofs, failures


def read_witnesses(root: Path) -> tuple[list[Witness], list[Residual], list[str]]:
    rows, failures = read_tsv(root / WITNESSES, WITNESS_HEADER)
    witnesses = []
    for row in rows:
        if row["status"] not in values(WitnessStatus):
            failures.append(f"{WITNESSES} {row['witness']}: status {row['status']} is neither registered nor differs")
            continue
        status = WitnessStatus(row["status"])
        witnesses.append(Witness(WitnessName(row["witness"]), status, row["corpus"], row["diff"], row["evidence"]))
    residual_rows, residual_failures = read_tsv(root / RESIDUALS, RESIDUAL_HEADER)
    for row in residual_rows:
        if blank_members(row, ("hunks",)):
            residual_failures.append(f"{RESIDUALS} {row['witness']} {row['file']}: hunks hold an empty member")
    residuals = [
        Residual(
            WitnessName(row["witness"]),
            row["file"],
            split(row["hunks"]),
            None if row["owner"] == UNOWNED else ShapeId(row["owner"]),
        )
        for row in residual_rows
    ]
    return witnesses, residuals, failures + residual_failures


@dataclass(frozen=True)
class E2e:
    """The e2e crate's tests, and how each reaches the goldens it compares."""

    tests: frozenset[TestName]
    bodies: dict[str, str]
    constants: dict[str, str]
    corpus_tests: dict[str, TestName]
    flat_tests: dict[TestName, str]
    overlay_test: TestName | None

    def paths(self, name: str, depth: int = 2, seen: frozenset[str] = frozenset()) -> set[str]:
        """Path-like strings a function's body names, directly, through its constants, or through its callees."""
        body = self.bodies.get(name)
        if body is None or name in seen:
            return set()
        found = set(re.findall(r'"([^"\n]*[/-][^"\n]*)"', body))
        named = re.findall(r"\b[A-Z][A-Z0-9_]+\b", body)
        found |= {self.constants[constant] for constant in named if constant in self.constants}
        if depth:
            for callee in set(re.findall(r"\b([a-z_][a-z0-9_]+)\(", body)) - {name}:
                found |= self.paths(callee, depth - 1, seen | {name})
        return found

    def reaches(self, target: str, tests: tuple[TestName, ...]) -> bool:
        """Whether one of `tests` reaches `target`, a golden tree or a probe.

        A corpus golden is reached by the test bound to its fixture's `Corpus`
        (`expected/`), by the flat test registered for it (`expected-flat/`), or
        by the overlay gate (any other `expected-*/`). A hand-written golden,
        `handwritten/<fixture>/fern-expected`, is reached by the gate that walks
        every such tree. Anything else is reached when a test's body, or a
        callee's, names a path that contains it.
        """
        parts = target.split("/")
        if fixture := corpus_fixture(target):
            match parts[3]:
                case "expected":
                    return self.corpus_tests.get(fixture) in tests
                case "expected-flat":
                    return any(self.flat_tests.get(test) == fixture for test in tests)
                case _:
                    return self.overlay_test in tests
        if target.startswith(HANDWRITTEN) and len(parts) == 5 and parts[4] == "fern-expected":
            return HANDWRITTEN_TEST in tests
        return any(path in target for test in tests for path in self.paths(test) if len(path) > 3)


def read_e2e(root: Path) -> E2e:
    sources: list[Path] = []
    for entry in E2E_SOURCES:
        path = root / entry
        sources += [path] if path.is_file() else sorted(path.glob("*.rs"))
    tests: set[TestName] = set()
    bodies: dict[str, str] = {}
    constants: dict[str, str] = {}
    corpus_constants: dict[str, str] = {}
    flat_tests: dict[TestName, str] = {}
    for path in sources:
        text = path.read_text(encoding="utf-8")
        constants |= dict(re.findall(r'(?m)^\s*(?:pub(?:\(super\))? )?const (\w+): &str = "([^"]*)";', text))
        lines = text.splitlines()
        attributed, pending_corpus, flat = False, None, False
        for index, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("#[test]"):
                attributed = True
            elif found := re.match(r"^(\s*)(?:pub(?:\(super\))? )?fn (\w+)\(", line):
                indent, name = found.group(1), found.group(2)
                end = next(
                    (later for later in range(index + 1, len(lines)) if lines[later].rstrip() == f"{indent}}}"),
                    len(lines) - 1,
                )
                bodies[name] = "\n".join(lines[index : end + 1])
                if attributed:
                    tests.add(TestName(name))
                attributed = False
            elif not stripped.startswith(("#[", "//")):
                attributed = False
            if found := re.match(r"^const (\w+): Corpus = Corpus \{", line):
                pending_corpus = found.group(1)
            elif pending_corpus and (found := re.match(r'^\s*api: "([^"]+)"', line)):
                corpus_constants[pending_corpus], pending_corpus = found.group(1), None
            if stripped.startswith("flat_goldens! {"):
                flat = True
            elif flat and stripped == "}":
                flat = False
            elif flat and (found := re.match(r'^(\w+) => "([^"]+)"', stripped)):
                flat_tests[TestName(found.group(1))] = found.group(2)
    tests |= set(flat_tests)
    corpus_tests: dict[str, TestName] = {}
    for name, body in bodies.items():
        for constant, fixture in corpus_constants.items():
            if name in tests and any(f"{driver}{constant})" in body for driver in CORPUS_DRIVERS):
                corpus_tests.setdefault(fixture, TestName(name))
    overlay = constants.get("CORPUS_TEST")
    return E2e(
        frozenset(tests),
        bodies,
        constants,
        corpus_tests,
        flat_tests,
        TestName(overlay) if overlay and overlay in tests else None,
    )


class Catalogs(NamedTuple):
    inventory: frozenset[str]
    defects: frozenset[DepartureId]
    ledger: dict[str, set[str]]
    classes: dict[RefusalClass, RefusalStatus]
    e2e: E2e
    corpus: dict[str, frozenset[str]]


def read_inventory(root: Path) -> tuple[frozenset[str], list[str]]:
    """The goldens the gate compares: the keys of the inventory's `goldens` object."""
    try:
        data = json.loads((root / INVENTORY).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return frozenset(), [f"{INVENTORY}: unreadable ({error})"]
    goldens = data.get("goldens") if isinstance(data, dict) else None
    if not isinstance(goldens, dict):
        return frozenset(), [f"{INVENTORY}: holds no `goldens` object"]
    return frozenset(goldens), []


def _yaml() -> ModuleType:
    """PyYAML, imported only where a YAML document is read, so `hunks` runs on a bare interpreter."""
    import yaml

    return yaml


def read_defects(root: Path) -> tuple[frozenset[DepartureId], list[str]]:
    """The ids of the departure catalog's `fern-defect` entries."""
    yaml = _yaml()
    try:
        catalog = yaml.safe_load((root / CATALOG).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        return frozenset(), [f"{CATALOG}: unreadable ({error})"]
    entries = catalog if isinstance(catalog, list) else None
    if entries is None or not all(
        isinstance(entry, dict) and isinstance(entry.get("id"), str) and isinstance(entry.get("kind"), str)
        for entry in entries
    ):
        return frozenset(), [f"{CATALOG}: is not a list of entries each with a string `id` and `kind`"]
    return frozenset(DepartureId(entry["id"]) for entry in entries if entry["kind"] == "fern-defect"), []


def read_ledger(root: Path) -> tuple[dict[str, set[str]], list[str]]:
    """Each golden's departures, from the line-pinned ledger."""
    rows, failures = read_tsv(root / LEDGER, LEDGER_HEADER)
    ledger: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        ledger[row["golden"]].add(row["departure"])
    return ledger, failures


def read_classes(root: Path) -> tuple[dict[RefusalClass, RefusalStatus], list[str]]:
    """Each decided refusal class's status; an `unevaluated` class decides no outcome."""
    rows, failures = read_tsv(root / CLASSES, CLASSES_HEADER)
    statuses = values(RefusalStatus)
    decided = {}
    for row in rows:
        if row["status"] in statuses:
            decided[RefusalClass(row["class"])] = RefusalStatus(row["status"])
        elif row["status"] != UNEVALUATED:
            failures.append(
                f"{CLASSES} {row['class']}: status {row['status']} is none of {', '.join(statuses)}, {UNEVALUATED}"
            )
    return decided, failures


def read_corpus(root: Path) -> dict[str, frozenset[str]]:
    """Each numbered `CORPUS.md` row's fixture name -> the row numbers it is listed under."""
    path = root / CORPUS
    rows: dict[str, set[str]] = defaultdict(set)
    if path.is_file():
        for found in re.finditer(r"(?m)^\| (\d+) \| `([^`]+)` \|", path.read_text(encoding="utf-8")):
            rows[found.group(2)].add(found.group(1))
    return {name: frozenset(numbers) for name, numbers in rows.items()}


def catalogs(root: Path) -> tuple[Catalogs, list[str]]:
    """The authoritative catalogs every row is reconciled with."""
    inventory, failures = read_inventory(root)
    defects, defect_failures = read_defects(root)
    ledger, ledger_failures = read_ledger(root)
    classes, class_failures = read_classes(root)
    known = Catalogs(inventory, defects, ledger, classes, read_e2e(root), read_corpus(root))
    return known, failures + defect_failures + ledger_failures + class_failures


def golden_settings(root: Path, golden: str) -> tuple[str | None, list[str]]:
    """A golden's generator settings as the index spells them, read off its metadata."""
    metadata = root / golden / ".fern" / "metadata.json"
    if not metadata.is_file():
        return None, [f"golden {golden} is not a complete certified tree (no .fern/metadata.json)"]
    try:
        record: Any = json.loads(metadata.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return None, [f"golden {golden}'s metadata is not JSON ({error})"]
    config = record.get("generatorConfig", {}) if isinstance(record, dict) else None
    pydantic = config.get("pydantic_config", {}) if isinstance(config, dict) else None
    if not isinstance(config, dict) or not isinstance(pydantic, dict):
        return None, [f"golden {golden}'s metadata holds no generatorConfig object"]
    settings = {**{key: value for key, value in config.items() if key != "pydantic_config"}, **pydantic}
    if not all(isinstance(value, SETTING_VALUE) for value in settings.values()):
        return None, [f"golden {golden}'s generatorConfig holds a setting that is not a scalar"]
    failures = []
    if (record.get("cliVersion"), record.get("generatorVersion")) != PIN:
        failures.append(f"golden {golden} is not output of Fern CLI {PIN.cli} with fern-python-sdk {PIN.generator}")
    enum_type = pydantic.get("enum_type", EnumType.LITERALS)
    if enum_type not in values(EnumType):
        return None, [f"golden {golden}'s enum_type {enum_type!r} is none of {', '.join(EnumType)}"]
    parts = [enum_type]
    if golden.endswith("-flat") or "-flat/" in golden:
        parts.append("flat")
    for key, value in sorted(config.items()):
        if key == "pydantic_config":
            parts += [f"{name}={setting}" for name, setting in sorted(pydantic.items()) if name != "enum_type"]
        else:
            parts.append(f"{key}={value}")
    return "+".join(parts), failures


def _document(directory: Path, root: Path) -> str | None:
    for name in DOCUMENTS:
        if (directory / name).is_file():
            return (directory / name).relative_to(root).as_posix()
    documents = directory / "documents"
    return documents.relative_to(root).as_posix() if documents.is_dir() else None


def golden_source(root: Path, golden: str) -> str | None:
    """The committed document a golden was generated from.

    A corpus golden's is its fixture's one committed corpus source. A
    measurement or hand-written golden's is its case directory's document (or
    multi-file `documents/`); a case without one is an overlay of the fixture or
    case of the same name, less a `-literals` or `-flat` suffix.
    """
    parts = golden.split("/")
    if golden.startswith("tests/fixtures/"):
        fixture = corpus_fixture(golden)
        if fixture is None:
            return None
        sources = root / "tests" / "fixtures" / "corpus-sources" / fixture
        files = sorted(path for path in sources.glob("*") if path.is_file()) if sources.is_dir() else []
        return files[0].relative_to(root).as_posix() if len(files) == 1 else None
    case = root.joinpath(*parts[:-1])
    if found := _document(case, root):
        return found
    name = re.sub(r"-(?:literals|flat)$", "", case.name)
    candidates = [root / HANDWRITTEN / name, *sorted((root / MEASUREMENTS).glob(f"*/{name}"))]
    return next((found for candidate in candidates if (found := _document(candidate, root))), None)


def path_failures(root: Path, where: str, references: tuple[str, ...]) -> list[str]:
    failures = []
    for reference in references:
        relative, _, anchor = reference.partition("#")
        path = root / relative
        if not path.exists():
            failures.append(f"{where}: {relative} does not exist")
        elif anchor and not path.is_file():
            failures.append(f"{where}: {relative} is no document to hold heading #{anchor}")
        elif anchor and anchor not in _handwritten().heading_anchors(path.read_text(encoding="utf-8")):
            failures.append(f"{where}: {relative} has no heading #{anchor}")
    return failures


def _declared_defaults(document: Any) -> tuple[list[str], str | None]:
    """Every scalar `default` a probe's operation (or path) parameters declare, or why it cannot be read."""
    paths = document.get("paths") if isinstance(document, dict) else None
    if not isinstance(paths, dict) or not paths:
        return [], "declares no `paths` object"
    found: list[str] = []
    for route, item in paths.items():
        if not isinstance(item, dict):
            return [], f"path {route} is not an object"
        operations = [("", item), *((key, value) for key, value in item.items() if isinstance(value, dict))]
        for method, operation in operations:
            parameters = operation.get("parameters", [])
            if not isinstance(parameters, list) or not all(isinstance(parameter, dict) for parameter in parameters):
                return [], f"{route} {method} parameters are not a list of objects".replace("  ", " ")
            for parameter in parameters:
                schema = parameter.get("schema")
                default = schema.get("default") if isinstance(schema, dict) else None
                if isinstance(default, SETTING_VALUE) and str(default) not in found:
                    found.append(str(default))
    return found, None


def _wire_assertions(source: str) -> tuple[list[set[str]], str | None]:
    """The literal values each wire assertion compares a sent request against, or why it cannot be parsed.

    Only an `assert` inside a pytest `test_*` function counts, and only when its
    expression reads a runtime value (a name, attribute, call or subscript) rather
    than constants alone: `assert True`, or a default named only in a comment, a
    docstring or a constant-only comparison, asserts nothing about the request.
    """
    try:
        module = ast.parse(source)
    except SyntaxError as error:
        return [], f"line {error.lineno}: {error.msg}"
    asserted = []
    for function in ast.walk(module):
        if not isinstance(function, ast.FunctionDef | ast.AsyncFunctionDef) or not function.name.startswith("test"):
            continue
        for statement in ast.walk(function):
            if not isinstance(statement, ast.Assert):
                continue
            nodes = list(ast.walk(statement.test))
            if any(isinstance(node, ast.Name | ast.Attribute | ast.Call | ast.Subscript) for node in nodes):
                asserted.append(
                    {
                        str(node.value)
                        for node in nodes
                        if isinstance(node, ast.Constant) and isinstance(node.value, SETTING_VALUE)
                    }
                )
    return asserted, None


# How the registry's evaluation notes state a class's decision: a heading
# ending in it, "is `refuse`", "`refuse` in both" / "`refuse` status", or
# "Decision: **refuse**".
DECISION_PATTERNS = (
    re.compile(r"(?m)^# .*:\s*(refuse|generate)\s*$"),
    re.compile(r"\bis `(refuse|generate)`"),
    re.compile(r"`(refuse|generate)` (?:in both|status)"),
    re.compile(r"Decision: \*\*(refuse|generate)\*\*"),
)


def note_decisions(note: str) -> set[RefusalStatus]:
    """Every decision an evaluation note states for its class."""
    return {RefusalStatus(found) for pattern in DECISION_PATTERNS for found in pattern.findall(note)}


def exception_failures(directory: Path, note: str) -> list[str]:
    """Why a `generate` class's committed evaluation does not establish default generation.

    The registry contract (`docs/fern-refusals/README.md`) has default
    generation rest on the class's own evidence, so each finding is read from
    it (the note's own `generate` decision is reconciled for every class by
    `note_decisions`): a log it links shows the probe is valid OpenAPI, which with Fern's recorded
    refusal (`fern-refusal.txt`) makes the refusal a Fern limitation; a linked
    `mypy` log shows the SDK imports and type-checks clean; a linked wire log
    shows the wire evaluation passing; and `wire_test.py` holds, in executable
    test assertions over the request the SDK sends, every default the probe's
    operations declare (see `_wire_assertions`).
    """
    problems = []
    logs = {}
    for target in re.findall(r"\]\(([^)\s#]+)\)", note):
        path = directory / target
        if path.is_file() and path.suffix == ".log":
            logs[target] = path.read_text(encoding="utf-8", errors="replace")
    if not any(re.search(r"validation: passed", text) for text in logs.values()):
        problems.append("links no log establishing that its probe is valid OpenAPI")
    refusal = directory / "fern-refusal.txt"
    record = refusal.read_text(encoding="utf-8") if refusal.is_file() else ""
    if not re.search(r"(?m)^generate_exit: [1-9]", record) or f"fern_cli_version: {PIN.cli}" not in record:
        problems.append("has no pinned Fern refusal record, so no Fern limitation is established")
    if not any("Success: no issues found" in text for text in logs.values()):
        problems.append("links no mypy log showing its SDK imports and type-checks clean")
    wire_logs = [text for target, text in logs.items() if "wire" in Path(target).name]
    # A pytest run's own summary is the positive evidence; anything failing beside it disqualifies the log.
    passing = [text for text in wire_logs if re.search(r"\b[1-9]\d* passed\b", text)]
    if not passing or any(
        re.search(r"Traceback|AssertionError|\b\d+ (?:failed|errors?)\b", text) for text in wire_logs
    ):
        problems.append("links no passing wire-evaluation log")
    wire = directory / "wire_test.py"
    asserted, unparsable = _wire_assertions(wire.read_text(encoding="utf-8") if wire.is_file() else "")
    if unparsable:
        problems.append(f"has a wire_test.py that is not valid Python ({unparsable})")
    if not asserted:
        problems.append("has no wire_test.py asserting the generated SDK's wire behaviour")
    yaml = _yaml()
    try:
        probe = yaml.safe_load((directory / "probe.yml").read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        return [*problems, f"has no readable probe.yml ({error})"]
    defaults, malformed = _declared_defaults(probe)
    if malformed:
        problems.append(f"has a probe.yml whose operations cannot be read: it {malformed}")
    for default in defaults:
        if not any(default in values for values in asserted):
            problems.append(f"has a wire_test.py that never asserts the declared default {default!r}")
    return problems


def refusal_failures(root: Path, proof: Proof, known: Catalogs) -> list[str]:
    name, where = proof.refusal, proof.where
    status = known.classes.get(name) if name else None
    if name is None or status is None:
        return [f"{where}: {name} is no decided {CLASSES} class"]
    failures = []
    if proof.goldens or proof.settings != REFUSAL_SETTINGS:
        failures.append(f"{where}: a refusal cites no golden and records `{REFUSAL_SETTINGS}`")
    if proof.outcome != status.outcome:
        failures.append(f"{where}: outcome {proof.outcome} disagrees with {name}'s registry status {status}")
    note = root / "docs" / "fern-refusals" / name / "evaluation.md"
    if not note.is_file():
        return [*failures, f"{where}: {name} has no evaluation note"]
    text = note.read_text(encoding="utf-8")
    decisions = note_decisions(text)
    if not decisions:
        failures.append(f"{where}: {name}'s evaluation note states no `refuse` or `generate` decision")
    elif decisions != {status}:
        stated = ", ".join(f"`{decision}`" for decision in sorted(decisions))
        failures.append(f"{where}: {name}'s evaluation note decides {stated}, not its registry status `{status}`")
    for decision in sorted(decisions):
        if proof.outcome != decision.outcome:
            failures.append(
                f"{where}: outcome {proof.outcome} disagrees with its evaluation note's `{decision}` decision"
            )
    if status is RefusalStatus.GENERATE:
        failures += [f"{where}: {name} {problem}" for problem in exception_failures(note.parent, text)]
    for probe in proof.source:
        if Path(probe).name not in text:
            failures.append(f"{where}: {name}'s evaluation note does not name the probe {probe}")
        if not known.e2e.reaches(probe, proof.tests):
            failures.append(f"{where}: none of its tests reaches the probe {probe}")
    return failures


def generated_failures(root: Path, proof: Proof, known: Catalogs) -> list[str]:
    where = proof.where
    if not proof.goldens:
        return [f"{where}: a {proof.kind} proof cites at least one golden"]
    failures, settings, defects = [], [], set()
    for golden in proof.goldens:
        if golden not in known.inventory:
            failures.append(f"{where}: golden {golden} is not in {INVENTORY}")
        if not known.e2e.reaches(golden, proof.tests):
            failures.append(f"{where}: none of its tests reaches golden {golden}")
        setting, problems = golden_settings(root, golden)
        failures += [f"{where}: {problem}" for problem in problems]
        settings.append(setting or "?")
        defects |= known.ledger.get(golden, set()) & known.defects
    sources: list[str] = []
    for golden in proof.goldens:
        source = golden_source(root, golden)
        if source is None:
            failures.append(f"{where}: golden {golden} has no committed document it was generated from")
        elif source not in sources:
            sources.append(source)
    if list(proof.source) != sources:
        failures.append(f"{where}: sources {';'.join(proof.source)} are not its goldens' documents {';'.join(sources)}")
    if proof.settings != ";".join(settings):
        failures.append(f"{where}: settings {proof.settings} disagree with the goldens' metadata {';'.join(settings)}")
    outcome = Outcome.DEPARTURE if defects else Outcome.MATCH
    if (proof.outcome, set(proof.departures)) != (outcome, defects):
        failures.append(
            f"{where}: outcome {proof.outcome} {';'.join(proof.departures) or NONE} disagrees with the ledger's "
            f"{outcome} {';'.join(sorted(defects)) or NONE}"
        )
    elif list(proof.departures) != sorted(proof.departures):
        failures.append(f"{where}: departure ids are sorted")
    match proof.kind:
        case Kind.REAL if not any(corpus_fixture(golden) in known.corpus for golden in proof.goldens):
            failures.append(f"{where}: a real proof cites a registered corpus row's golden")
        case Kind.HANDWRITTEN if not any(source.startswith((HANDWRITTEN, MEASUREMENTS)) for source in proof.source):
            failures.append(f"{where}: a hand-written proof's source is a hand-written fixture")
        case Kind.HANDWRITTEN if not any(source.startswith(HANDWRITTEN) for source in proof.source):
            covers = (root / E2E_COVERS).read_text(encoding="utf-8")
            if not any(f'fixture = "{source}"' in covers for source in proof.source):
                failures.append(f"{where}: a multi-file hand-written source is a {E2E_COVERS} cover")
        case Kind.MEASUREMENT if not all(golden.startswith(MEASUREMENTS) for golden in proof.goldens):
            failures.append(f"{where}: a measurement proof's goldens are under {MEASUREMENTS}")
    return failures


def index_failures(root: Path, plan: dict[ShapeId, Owner], proofs: list[Proof], known: Catalogs) -> list[str]:
    """Every way the scenario proof index disagrees with the plan and the catalogs it cites."""
    failures = []
    counts = Counter(proof.shape for proof in proofs)
    failures += [f"{INDEX}: {shape} is indexed {count} times" for shape, count in counts.items() if count > 1]
    failures += [f"{INDEX}: {shape} is planned but not indexed" for shape in sorted(set(plan) - set(counts))]
    failures += [f"{INDEX}: {shape} is indexed but not planned" for shape in sorted(set(counts) - set(plan))]
    if [proof.shape for proof in proofs] != sorted(proof.shape for proof in proofs):
        failures.append(f"{INDEX}: rows are sorted by shape")
    for proof in proofs:
        if not SHAPE_NAME.match(proof.shape):
            failures.append(f"{proof.where}: a shape id is lower-kebab")
        if proof.shape in plan and plan[proof.shape] is not proof.owner:
            failures.append(f"{proof.where}: owner {proof.owner} is not the plan's {plan[proof.shape]}")
        for cell, cited in (("source", proof.source), ("tests", proof.tests), ("evidence", proof.evidence)):
            if not cited:
                failures.append(f"{proof.where}: its {cell} cell cites nothing")
        failures += path_failures(root, proof.where, proof.source)
        failures += path_failures(root, proof.where, proof.evidence)
        unknown = [test for test in proof.tests if test not in known.e2e.tests]
        failures += [f"{proof.where}: no e2e #[test] is named {test}" for test in unknown]
        if proof.kind is Kind.REFUSAL:
            failures += refusal_failures(root, proof, known)
        else:
            failures += generated_failures(root, proof, known)
    return failures


def diff_hunks(text: str) -> list[Hunk]:
    """Each change of a `crozier compare` diff, as `-start,count +start,count` or a one-sided file.

    Raises MalformedDiff on any line that is not the normalized diff's: a file
    header pair, a one-sided file, a context, change or elision line, a `#`
    comment or a blank line; and on a diff with no difference at all.
    """
    hunks: list[Hunk] = []
    current: str | None = None
    reference = crozier = 0
    run: _Run | None = None
    awaiting: str | None = None
    for number, line in enumerate([*text.splitlines(), None], start=1):
        if awaiting is not None:
            if line != f"+++ crozier/{awaiting}":
                raise MalformedDiff(f"line {number}: `--- reference/{awaiting}` is not followed by its `+++` header")
            current, awaiting, reference, crozier = awaiting, None, 0, 0
            continue
        changed = current is not None and line is not None and (line[:2] in ("- ", "+ ") or line in ("-", "+"))
        if run is not None and not changed:
            hunks.append(run.hunk)
            run = None
        if line is None:
            break
        if changed and current is not None:
            if run is None:
                run = _Run(current, reference + 1, crozier + 1)
            if line.startswith("-"):
                reference, run.removed = reference + 1, run.removed + 1
            else:
                crozier, run.added = crozier + 1, run.added + 1
        elif line.startswith("--- reference/"):
            awaiting, current = line.removeprefix("--- reference/"), None
        elif found := re.match(r"^Only in (reference|crozier): (.+)$", line):
            current = None
            hunks.append(Hunk(found.group(2), f"only in {found.group(1)}"))
        elif current is None:
            if line and not line.startswith("#"):
                raise MalformedDiff(f"line {number}: `{line[:60]}` is outside any file of the diff")
        elif found := re.match(r"^\s+⋮ \((\d+) unchanged line\(s\)\)$", line):
            reference += int(found.group(1))
            crozier += int(found.group(1))
        elif line == "" or line.startswith("  "):
            reference += 1
            crozier += 1
        else:
            raise MalformedDiff(f"line {number}: `{line[:60]}` is no context, change or elision line")
    if not hunks:
        raise MalformedDiff("it holds no difference")
    return hunks


def open_failures(root: Path, proofs: list[Proof], residuals: list[Residual]) -> list[str]:
    """Every shape whose `open` cell disagrees with the residuals committed against it."""
    owned: dict[ShapeId, set[str]] = defaultdict(set)
    for residual in residuals:
        if residual.owner is not None:
            owned[residual.owner].add(residual.witness)
    failures = []
    for proof in proofs:
        expected = sorted(owned.get(proof.shape, set()))
        diff = root / PYTHON_ENUMS_RESIDUALS / f"{proof.shape}.diff"
        if diff.is_file():
            try:
                diff_hunks(diff.read_text(encoding="utf-8"))
            except MalformedDiff as error:
                failures.append(f"{proof.where}: its python_enums residual diff is malformed: {error}")
            expected.append(PYTHON_ENUMS)
        if list(proof.open) != expected:
            failures.append(
                f"{proof.where}: open {';'.join(proof.open) or NONE} disagrees with its committed residuals "
                f"{';'.join(expected) or NONE}"
            )
    return failures


def witness_failures(
    root: Path, shapes: set[ShapeId], witnesses: list[Witness], residuals: list[Residual]
) -> list[str]:
    """Every way the handed-off witnesses disagree with the corpus, their diffs and the index."""
    failures: list[str] = []
    corpus = read_corpus(root)
    claimed: dict[WitnessName, Counter[Hunk]] = defaultdict(Counter)
    for residual in residuals:
        if residual.owner is not None and residual.owner not in shapes:
            where = f"{RESIDUALS} {residual.witness} {residual.file}"
            failures.append(f"{where}: owner {residual.owner} is no indexed shape nor {UNOWNED}")
        claimed[residual.witness].update(Hunk(residual.file, spelling) for spelling in residual.hunks)
    names = Counter(witness.name for witness in witnesses)
    failures += [f"{WITNESSES}: {name} is listed {count} times" for name, count in names.items() if count > 1]
    for witness in witnesses:
        where = witness.where
        failures += path_failures(root, where, (witness.evidence,))
        found = claimed.pop(witness.name, Counter())
        match witness.status:
            case WitnessStatus.REGISTERED:
                number, fixture = witness.corpus_row
                golden = root / "tests" / "fixtures" / fixture / "expected"
                if number not in corpus.get(fixture, frozenset()) or not golden.is_dir():
                    failures.append(f"{where}: registered as {witness.corpus}, which is no corpus row with a golden")
                if witness.diff != NONE or found:
                    failures.append(f"{where}: a registered witness has no comparison diff or residual")
            case WitnessStatus.DIFFERS:
                diff = root / WITNESSES.parent / witness.diff
                if not diff.is_file():
                    failures.append(f"{where}: comparison diff {witness.diff} is missing")
                    continue
                try:
                    expected = Counter(diff_hunks(diff.read_text(encoding="utf-8")))
                except MalformedDiff as error:
                    failures.append(f"{where}: comparison diff {witness.diff} is malformed: {error}")
                    continue
                for hunk in sorted((expected - found).elements()):
                    failures.append(f"{where}: {hunk.file} {hunk.spelling} is in the diff but attributed to no shape")
                for hunk in sorted((found - expected).elements()):
                    failures.append(
                        f"{where}: {hunk.file} {hunk.spelling} is attributed but not in the diff (or twice)"
                    )
    failures += [f"{RESIDUALS}: {name} is no differing witness" for name in sorted(claimed)]
    return failures


def check(root: Path) -> list[str]:
    plan, failures = read_plan(root)
    proofs, proof_failures = read_proofs(root)
    witnesses, residuals, witness_read_failures = read_witnesses(root)
    known, catalog_failures = catalogs(root)
    failures += proof_failures + witness_read_failures + catalog_failures
    failures += index_failures(root, plan, proofs, known)
    failures += open_failures(root, proofs, residuals)
    return failures + witness_failures(root, {proof.shape for proof in proofs}, witnesses, residuals)


def summary(root: Path) -> tuple[list[str], list[str]]:
    """The index's shapes by kind, owner and outcome, and the witnesses' hunks by owner; or why not."""
    proofs, failures = read_proofs(root)
    witnesses, residuals, witness_read_failures = read_witnesses(root)
    failures += witness_read_failures
    if failures:
        return [], failures
    hunks: Counter[str] = Counter()
    for residual in residuals:
        hunks[residual.owner or UNOWNED] += len(residual.hunks)

    def spelled(counts: Counter[str]) -> str:
        return ", ".join(f"{name} {count}" for name, count in sorted(counts.items()))

    return [
        f"shapes: {len(proofs)}",
        f"by kind: {spelled(Counter(str(proof.kind) for proof in proofs))}",
        f"by owner: {spelled(Counter(str(proof.owner) for proof in proofs))}",
        f"by outcome: {spelled(Counter(proof.outcome for proof in proofs))}",
        f"closed with no open residual: {sum(proof.fully_closed for proof in proofs)}",
        "closed on their proof with a residual open: "
        + (", ".join(f"{proof.shape} ({';'.join(proof.open)})" for proof in proofs if not proof.fully_closed) or NONE),
        f"witnesses: {spelled(Counter(str(witness.status) for witness in witnesses))}",
        f"witness hunks by owner: {spelled(hunks)}",
    ], []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--repo-root", type=Path, default=REPO)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="reconcile the index and witnesses; print each failure to stderr")
    sub.add_parser("summary", help="print the index's and the witnesses' counts")
    hunks = sub.add_parser("hunks", help="print a comparison diff's hunks as residuals.tsv cites them")
    hunks.add_argument("diff", type=Path)
    args = parser.parse_args(argv)
    match args.command:
        case "hunks":
            try:
                found = diff_hunks(args.diff.read_text(encoding="utf-8"))
            except (OSError, MalformedDiff) as error:
                print(
                    f"scenario-proof-index: cannot read {args.diff} ({error}) — pass a committed diff", file=sys.stderr
                )
                return 1
            for hunk in found:
                print(f"{hunk.file}\t{hunk.spelling}")
            return 0
        case "summary":
            lines, failures = summary(args.repo_root)
            print("\n".join(lines or failures), file=sys.stdout if lines else sys.stderr)
            return 1 if failures else 0
        case _:
            failures = check(args.repo_root)
            for failure in failures:
                print(failure, file=sys.stderr)
            if failures:
                print(f"{len(failures)} failure(s): fix the row or the proof it cites, then re-run", file=sys.stderr)
            return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
