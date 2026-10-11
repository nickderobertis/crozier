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

Three subcommands: ``check`` prints every failure to stderr (nothing on success)
and exits 1 when there is one; ``summary`` prints the counts the coverage report
quotes, read off both tables; ``hunks DIFF`` prints the hunks of one comparison
diff in the form `residuals.tsv` cites them.
"""

from __future__ import annotations

import argparse
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
from typing import Any, NamedTuple

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
INVENTORY = Path("tests/fixtures/compared-goldens.json")
LEDGER = Path("tests/fixtures/departures-ledger.tsv")
LEDGER_HEADER = ("golden", "file", "line", "departure")
CATALOG = Path("assets/departures.yml")
# The plan this index closes owns exactly these many scenario shapes; a row
# removed or added changes the count, so the closure cannot shrink silently.
SHAPES = 160
PIN = ("5.67.1", "5.20.0")
NONE = "—"
UNOWNED = "unowned"
REFUSAL_SETTINGS = "default;fern-strict"
SHAPE_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
E2E_SOURCES = ("crates/crozier-e2e/tests/e2e.rs", "crates/crozier-e2e/tests/e2e")
HANDWRITTEN = "docs/openapi-surface/handwritten/"
E2E_COVERS = "docs/openapi-surface/handwritten-e2e.toml"
MEASUREMENTS = "docs/fern-measurements/"


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
    def outcome(self) -> str:
        default = "refuse" if self is RefusalStatus.REFUSE else "generate"
        return f"default={default};strict=refuse"


class WitnessStatus(StrEnum):
    REGISTERED = "registered"
    DIFFERS = "differs"


def values(kind: type[StrEnum]) -> frozenset[str]:
    """The spellings a cell may hold for `kind`."""
    return frozenset(member.value for member in kind)


def split(cell: str) -> tuple[str, ...]:
    return () if cell == NONE else tuple(part.strip() for part in cell.split(";"))


@dataclass(frozen=True)
class Proof:
    """One row of the scenario proof index."""

    shape: str
    owner: Owner
    kind: Kind
    source: tuple[str, ...]
    goldens: tuple[str, ...]
    settings: str
    tests: tuple[str, ...]
    outcome: str
    ids: str
    evidence: tuple[str, ...]

    @property
    def where(self) -> str:
        return f"{INDEX} {self.shape}"


@dataclass(frozen=True)
class Witness:
    """One handed-off publisher specification."""

    name: str
    status: WitnessStatus
    corpus: str
    diff: str
    evidence: str

    @property
    def where(self) -> str:
        return f"{WITNESSES} {self.name}"

    @property
    def corpus_name(self) -> str:
        """The corpus fixture a registered witness's `corpus` cell (`<row> \\`<name>\\``) names."""
        return self.corpus.partition(" ")[2].strip("`")


@dataclass(frozen=True)
class Residual:
    """One `residuals.tsv` row: hunks of one witness file and the shape that owns them."""

    witness: str
    file: str
    hunks: tuple[str, ...]
    owner: str


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
        proofs.append(
            Proof(
                shape=row["shape"],
                owner=Owner(row["owner"]),
                kind=Kind(row["kind"]),
                source=split(row["source"]),
                goldens=split(row["goldens"]),
                settings=row["settings"],
                tests=split(row["tests"]),
                outcome=row["outcome"],
                ids=row["ids"],
                evidence=split(row["evidence"]),
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
        witnesses.append(
            Witness(row["witness"], WitnessStatus(row["status"]), row["corpus"], row["diff"], row["evidence"])
        )
    residual_rows, residual_failures = read_tsv(root / RESIDUALS, RESIDUAL_HEADER)
    residuals = [Residual(row["witness"], row["file"], split(row["hunks"]), row["owner"]) for row in residual_rows]
    return witnesses, residuals, failures + residual_failures


class Catalogs(NamedTuple):
    inventory: frozenset[str]
    defects: frozenset[str]
    ledger: dict[str, set[str]]
    classes: dict[str, RefusalStatus]
    tests: frozenset[str]
    corpus: frozenset[str]


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


def read_defects(root: Path) -> tuple[frozenset[str], list[str]]:
    """The ids of the departure catalog's `fern-defect` entries."""
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
    return frozenset(entry["id"] for entry in entries if entry["kind"] == "fern-defect"), []


def read_ledger(root: Path) -> tuple[dict[str, set[str]], list[str]]:
    """Each golden's departures, from the line-pinned ledger."""
    rows, failures = read_tsv(root / LEDGER, LEDGER_HEADER)
    ledger: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        ledger[row["golden"]].add(row["departure"])
    return ledger, failures


def read_classes(root: Path) -> tuple[dict[str, RefusalStatus], list[str]]:
    """Each decided refusal class's status; an `unevaluated` class decides no outcome."""
    rows, failures = read_tsv(root / CLASSES, CLASSES_HEADER)
    return {
        row["class"]: RefusalStatus(row["status"]) for row in rows if row["status"] in values(RefusalStatus)
    }, failures


def read_tests(root: Path) -> frozenset[str]:
    """Every e2e test name: a `fn`, or a name a `flat_goldens!`-style macro invocation expands."""
    sources: list[Path] = []
    for entry in E2E_SOURCES:
        path = root / entry
        sources += [path] if path.is_file() else sorted(path.glob("*.rs"))
    pattern = re.compile(r"(?m)^\s*(?:pub )?fn (\w+)\(|^\s*(\w+) =>")
    return frozenset(
        name
        for path in sources
        for found in pattern.findall(path.read_text(encoding="utf-8"))
        for name in found
        if name
    )


def catalogs(root: Path) -> tuple[Catalogs, list[str]]:
    """The authoritative catalogs every row is reconciled with."""
    inventory, failures = read_inventory(root)
    defects, defect_failures = read_defects(root)
    ledger, ledger_failures = read_ledger(root)
    classes, class_failures = read_classes(root)
    corpus = frozenset(_handwritten().corpus_rows(root))
    known = Catalogs(inventory, defects, ledger, classes, read_tests(root), corpus)
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
    failures = []
    if (record.get("cliVersion"), record.get("generatorVersion")) != PIN:
        failures.append(f"golden {golden} is not output of Fern CLI {PIN[0]} with fern-python-sdk {PIN[1]}")
    parts = [str(pydantic.get("enum_type", "literals"))]
    if golden.endswith("-flat") or "-flat/" in golden:
        parts.append("flat")
    for key, value in sorted(config.items()):
        if key == "pydantic_config":
            parts += [f"{name}={setting}" for name, setting in sorted(pydantic.items()) if name != "enum_type"]
        else:
            parts.append(f"{key}={value}")
    return "+".join(parts), failures


def path_failures(root: Path, where: str, references: tuple[str, ...]) -> list[str]:
    failures = []
    for reference in references:
        relative, _, anchor = reference.partition("#")
        path = root / relative
        if not path.exists():
            failures.append(f"{where}: {relative} does not exist")
        elif anchor and anchor not in _handwritten().heading_anchors(path.read_text(encoding="utf-8")):
            failures.append(f"{where}: {relative} has no heading #{anchor}")
    return failures


def refusal_failures(root: Path, proof: Proof, known: Catalogs) -> list[str]:
    name, where = proof.ids, proof.where
    status = known.classes.get(name)
    if status is None:
        return [f"{where}: {name} is no decided docs/fern-refusals/classes.tsv class"]
    failures = []
    if proof.goldens or proof.settings != REFUSAL_SETTINGS:
        failures.append(f"{where}: a refusal cites no golden and records `{REFUSAL_SETTINGS}`")
    if proof.outcome != status.outcome:
        failures.append(f"{where}: outcome {proof.outcome} disagrees with {name}'s registry status {status}")
    note = root / "docs" / "fern-refusals" / name / "evaluation.md"
    if not note.is_file():
        return [*failures, f"{where}: {name} has no evaluation note"]
    if status is RefusalStatus.GENERATE and not (note.parent / "wire_test.py").is_file():
        failures.append(f"{where}: {name} claims default generation without its wire evaluation")
    text = note.read_text(encoding="utf-8")
    for probe in proof.source:
        if Path(probe).name not in text:
            failures.append(f"{where}: {name}'s evaluation note does not name the probe {probe}")
    return failures


def generated_failures(root: Path, proof: Proof, known: Catalogs) -> list[str]:
    where = proof.where
    if not proof.goldens:
        return [f"{where}: a {proof.kind} proof cites at least one golden"]
    failures, settings, defects = [], [], set()
    for golden in proof.goldens:
        if golden not in known.inventory:
            failures.append(f"{where}: golden {golden} is not in {INVENTORY}")
        setting, problems = golden_settings(root, golden)
        failures += [f"{where}: {problem}" for problem in problems]
        settings.append(setting or "?")
        defects |= known.ledger.get(golden, set()) & known.defects
    if proof.settings != ";".join(settings):
        failures.append(f"{where}: settings {proof.settings} disagree with the goldens' metadata {';'.join(settings)}")
    outcome = "departure" if defects else "match"
    ids = ";".join(sorted(defects)) if defects else NONE
    if (proof.outcome, proof.ids) != (outcome, ids):
        failures.append(f"{where}: outcome {proof.outcome} {proof.ids} disagrees with the ledger's {outcome} {ids}")
    match proof.kind:
        case Kind.REAL if not any(
            golden.startswith("tests/fixtures/") and golden.split("/")[2] in known.corpus for golden in proof.goldens
        ):
            failures.append(f"{where}: a real proof cites a registered corpus row's golden")
        case Kind.HANDWRITTEN if not any(source.startswith((HANDWRITTEN, MEASUREMENTS)) for source in proof.source):
            failures.append(f"{where}: a hand-written proof's source is a hand-written fixture")
        case Kind.HANDWRITTEN if any(source.startswith(MEASUREMENTS) for source in proof.source):
            covers = (root / E2E_COVERS).read_text(encoding="utf-8")
            if not any(f'fixture = "{source}"' in covers for source in proof.source):
                failures.append(f"{where}: a multi-file hand-written source is a {E2E_COVERS} cover")
        case Kind.MEASUREMENT if not all(golden.startswith(MEASUREMENTS) for golden in proof.goldens):
            failures.append(f"{where}: a measurement proof's goldens are under {MEASUREMENTS}")
    return failures


def index_failures(root: Path, proofs: list[Proof], known: Catalogs) -> list[str]:
    """Every way the scenario proof index disagrees with the catalogs it cites."""
    failures = []
    counts = Counter(proof.shape for proof in proofs)
    failures += [f"{INDEX}: {shape} is indexed {count} times" for shape, count in counts.items() if count > 1]
    if len(counts) != SHAPES:
        failures.append(f"{INDEX}: indexes {len(counts)} shapes, not the plan's {SHAPES}")
    if [proof.shape for proof in proofs] != sorted(proof.shape for proof in proofs):
        failures.append(f"{INDEX}: rows are sorted by shape")
    for proof in proofs:
        if not SHAPE_NAME.match(proof.shape):
            failures.append(f"{proof.where}: a shape id is lower-kebab")
        failures += path_failures(root, proof.where, proof.source)
        failures += path_failures(root, proof.where, proof.evidence)
        failures += [f"{proof.where}: no e2e test is named {test}" for test in proof.tests if test not in known.tests]
        if proof.kind is Kind.REFUSAL:
            failures += refusal_failures(root, proof, known)
        else:
            failures += generated_failures(root, proof, known)
    return failures


def diff_hunks(text: str) -> list[Hunk]:
    """Each change of a `crozier compare` diff, as `-start,count +start,count` or a one-sided file."""
    hunks: list[Hunk] = []
    current: str | None = None
    reference = crozier = 0
    run: _Run | None = None
    for line in [*text.splitlines(), None]:
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


def witness_failures(root: Path, shapes: set[str], witnesses: list[Witness], residuals: list[Residual]) -> list[str]:
    """Every way the handed-off witnesses disagree with the corpus, their diffs and the index."""
    failures: list[str] = []
    corpus = _handwritten().corpus_rows(root)
    claimed: dict[str, Counter[Hunk]] = defaultdict(Counter)
    for residual in residuals:
        if residual.owner != UNOWNED and residual.owner not in shapes:
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
                golden = root / "tests" / "fixtures" / witness.corpus_name / "expected"
                if witness.corpus_name not in corpus or not golden.is_dir():
                    failures.append(f"{where}: registered as {witness.corpus}, which is no corpus row with a golden")
                if witness.diff != NONE or found:
                    failures.append(f"{where}: a registered witness has no comparison diff or residual")
            case WitnessStatus.DIFFERS:
                diff = root / WITNESSES.parent / witness.diff
                if not diff.is_file():
                    failures.append(f"{where}: comparison diff {witness.diff} is missing")
                    continue
                expected = Counter(diff_hunks(diff.read_text(encoding="utf-8")))
                for hunk in sorted((expected - found).elements()):
                    failures.append(f"{where}: {hunk.file} {hunk.spelling} is in the diff but attributed to no shape")
                for hunk in sorted((found - expected).elements()):
                    failures.append(
                        f"{where}: {hunk.file} {hunk.spelling} is attributed but not in the diff (or twice)"
                    )
    failures += [f"{RESIDUALS}: {name} is no differing witness" for name in sorted(claimed)]
    return failures


def check(root: Path) -> list[str]:
    proofs, failures = read_proofs(root)
    witnesses, residuals, witness_read_failures = read_witnesses(root)
    known, catalog_failures = catalogs(root)
    failures += witness_read_failures + catalog_failures
    failures += index_failures(root, proofs, known)
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
        hunks[residual.owner] += len(residual.hunks)

    def spelled(counts: Counter[str]) -> str:
        return ", ".join(f"{name} {count}" for name, count in sorted(counts.items()))

    return [
        f"shapes: {len(proofs)}",
        f"by kind: {spelled(Counter(str(proof.kind) for proof in proofs))}",
        f"by owner: {spelled(Counter(str(proof.owner) for proof in proofs))}",
        f"by outcome: {spelled(Counter(proof.outcome for proof in proofs))}",
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
                text = args.diff.read_text(encoding="utf-8")
            except OSError as error:
                print(
                    f"scenario-proof-index: cannot read {args.diff} ({error}) — pass a committed diff", file=sys.stderr
                )
                return 1
            for hunk in diff_hunks(text):
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
