#!/usr/bin/env python3
"""Per-combination verdicts over the handed-off documents the operation search must screen.

`docs/fern-measurements/handed-off/` names a population of registered real
documents: its `registered` rows and its `## Newly admitted documents` list. Each
already has committed source bytes and a golden test, so each combination's verdict
on each document is measured rather than inferred from a name appearing in a list:
the census selector over the exact bytes, and the interaction arm's regions in that
golden test's instrumented run.

    handed-off-combination-verdicts.py write   needs `just census-repin`'s views
    handed-off-combination-verdicts.py check   offline: recomputes all but the reach

`write` restates `handed-off-verdicts.tsv`, then the search's `census.tsv.gz` cells,
`outstanding-candidates.tsv` and verdict table from it. `check` holds all of them to
the committed bytes and audit.

Exit status: 0 when the command succeeded; 1 when `check` found drift or an input
could not be read or validated, each reason on stderr; 2 for a usage error. Nothing
is written unless every input validates.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import importlib.util
import io
import json
import re
import sys
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any, NamedTuple, NewType, Protocol

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
RECORD = Path("docs/openapi-surface/witness-search-operation-combinations")
HANDED_OFF = Path("docs/fern-measurements/handed-off")
VIEWS = Path(".local/golden-reach")
DOCUMENT_COLUMNS = ("document", "sha256", "source", "root_causes", "status", "corpus_row", "note")
CONTRACT_COLUMNS = ("key", "selector", "census_status")
CENSUS_COLUMNS = {"key", "document", "sha256", "kind", "sites", "licence", "outcome"}
COLUMNS = (
    "key",
    "document",
    "sha256",
    "fixture",
    "golden_test",
    "unmatched_files",
    "declared_sites",
    "arm_regions_executed",
    "arm_regions_total",
    "verdict",
)
# The combinations resting on a hand-written fixture when this search began.
FORMER_HANDWRITTEN = (
    "combo-body-property-named-as-header-param",
    "combo-body-property-named-as-path-param",
    "combo-inline-body-read-only-property",
    "combo-success-anyof-nullable",
    "combo-success-oneof-nullable",
)
NOT_MEASURED = "-"
# Every `status` documents.tsv may carry; the census suite holds this set to its own record type.
HANDED_OFF_STATUSES = frozenset(
    {
        "registered",
        "byte-matches-not-admissible",
        "refused-by-ruling",
        "differs",
        "could-not-check",
        "registration-incomplete",
    }
)
CombinationKey = NewType("CombinationKey", str)
Sha256 = NewType("Sha256", str)
SHA256 = re.compile(r"[0-9a-f]{64}")
FIXTURE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")


class Verdict(StrEnum):
    NOT_DECLARED = "not-declared"
    ARM_NOT_EXECUTED = "declared-arm-not-executed"
    WITNESS = "witness"
    NO_EXCLUSIVE_ARM = "declared-no-exclusive-arm"
    POOLED_ARM_EXECUTED = "declared-pooled-arm-executed"


OUTSTANDING_VERDICTS = {Verdict.NO_EXCLUSIVE_ARM, Verdict.POOLED_ARM_EXECUTED}
REASONS = {
    Verdict.NOT_DECLARED: "fresh exact-byte source census does not declare this combination",
    Verdict.ARM_NOT_EXECUTED: "registered byte-matching golden declares it, and its instrumented run never executes the arm",
    Verdict.WITNESS: "registered byte-matching golden declares it and its instrumented run executes the exclusive arm",
    Verdict.NO_EXCLUSIVE_ARM: (
        "registered byte-matching golden declares it, but crozier has no exclusive counter region "
        "for its run to execute, so the meeting point cannot be screened"
    ),
    Verdict.POOLED_ARM_EXECUTED: (
        "registered byte-matching golden declares it and executes the declared region, "
        "which is pooled with other cases, so the execution does not imply both features"
    ),
}


class Document(NamedTuple):
    document: str
    sha256: Sha256
    fixture: str


class Region(NamedTuple):
    """One llvm-cov counter region: where it starts and ends in its source file, 1-based."""

    start_line: int
    start_column: int
    end_line: int
    end_column: int


class ArmCount(NamedTuple):
    executed: int
    total: int


def _count(text: str, what: str) -> int:
    if not text.isascii() or not text.isdigit():
        raise ValueError(f"{what} must be a non-negative integer, not {text!r}")
    return int(text)


@dataclass(frozen=True)
class VerdictRow:
    """One combination on one document, as `handed-off-verdicts.tsv` holds it."""

    key: CombinationKey
    document: str
    sha256: Sha256
    fixture: str
    golden_test: str
    unmatched_files: int
    declared_sites: int
    arm: ArmCount | None
    verdict: Verdict

    @classmethod
    def parse(cls, cells: dict[str, str]) -> VerdictRow:
        where = f"{cells['key']} on {cells['document']}"
        if not all(cells.values()):
            raise ValueError(f"{where}: an empty cell")
        if not SHA256.fullmatch(cells["sha256"]):
            raise ValueError(f"{where}: {cells['sha256']!r} is no SHA-256")
        executed, total = cells["arm_regions_executed"], cells["arm_regions_total"]
        arm = None
        if (executed, total) != (NOT_MEASURED, NOT_MEASURED):
            arm = ArmCount(_count(executed, f"{where}: executed regions"), _count(total, f"{where}: total regions"))
            if arm.executed > arm.total:
                raise ValueError(f"{where}: executes {arm.executed} of only {arm.total} regions")
        try:
            verdict = Verdict(cells["verdict"])
        except ValueError as error:
            raise ValueError(f"{where}: unknown verdict {cells['verdict']!r}") from error
        return cls(
            CombinationKey(cells["key"]),
            cells["document"],
            Sha256(cells["sha256"]),
            cells["fixture"],
            cells["golden_test"],
            _count(cells["unmatched_files"], f"{where}: unmatched files"),
            _count(cells["declared_sites"], f"{where}: declared sites"),
            arm,
            verdict,
        )

    def cells(self) -> tuple[str, ...]:
        executed, total = (str(self.arm.executed), str(self.arm.total)) if self.arm else (NOT_MEASURED, NOT_MEASURED)
        return (
            self.key,
            self.document,
            self.sha256,
            self.fixture,
            self.golden_test,
            str(self.unmatched_files),
            str(self.declared_sites),
            executed,
            total,
            str(self.verdict),
        )

    def outcome(self) -> Outcome:
        state = CandidateState.OUTSTANDING if self.verdict in OUTSTANDING_VERDICTS else CandidateState.DECIDED
        return Outcome(state, f"{self.verdict}: {REASONS[self.verdict]}")


class SiteRow(Protocol):
    """What this tool reads of a `golden-reach-sites.tsv` row."""

    cooccurrence: bool
    sites: tuple[str, ...]


def _load(name: str, file: str) -> Any:
    """A sibling script by path: its hyphenated name is no importable module, so it is typed `Any`."""
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    if spec is None or spec.loader is None:
        raise SystemExit(
            f"handed-off-combination-verdicts: cannot load tools/surface-census/{file}; restore it from git"
        )
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CENSUS = _load("handed_off_verdicts_census", "openapi-surface-census.py")
REACH = _load("handed_off_verdicts_reach", "golden-reach.py")


def population(root: Path) -> list[Document]:
    """The `registered` rows and the newly admitted list, which must agree on digest and fixture."""
    found: dict[str, Document] = {}
    with (root / HANDED_OFF / "documents.tsv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if tuple(reader.fieldnames or ()) != DOCUMENT_COLUMNS:
            raise ValueError(f"documents.tsv columns must be {DOCUMENT_COLUMNS}")
        for row in reader:
            if None in row or None in row.values():
                raise ValueError(f"documents.tsv line {reader.line_num}: extra or missing cells")
            if row["status"] not in HANDED_OFF_STATUSES:
                raise ValueError(f"{row['document']}: unknown status {row['status']!r} in documents.tsv")
            if row["status"] != "registered":
                continue
            named = re.fullmatch(r"\d+ \((.+)\)", row["corpus_row"])
            if not named or not FIXTURE.fullmatch(named.group(1)):
                raise ValueError(f"{row['document']}: a registered row must name its fixture: {row['corpus_row']!r}")
            if not SHA256.fullmatch(row["sha256"]):
                raise ValueError(f"{row['document']}: {row['sha256']!r} is no SHA-256")
            if row["document"] in found:
                raise ValueError(f"{row['document']}: registered twice in documents.tsv")
            found[row["document"]] = Document(row["document"], Sha256(row["sha256"]), named.group(1))
    readme = (root / HANDED_OFF / "README.md").read_text(encoding="utf-8")
    _before, heading, admitted = readme.partition("## Newly admitted documents")
    if not heading:
        raise ValueError("the handed-off README has no `## Newly admitted documents` section")
    entries = [line for line in admitted.split("\n## ", 1)[0].splitlines() if line.startswith("- ")]
    for entry in entries:
        listed = re.match(r"- `([^`]+)` \| `([0-9a-f]{64})`", entry)
        if not listed:
            raise ValueError(f"the handed-off README's newly admitted entry is malformed: {entry[:120]!r}")
        document, sha256 = listed.groups()
        if document not in found or found[document].sha256 != sha256:
            raise ValueError(f"{document}: newly admitted, but not the same `registered` row of documents.tsv")
    return sorted(found.values())


def contract(root: Path) -> dict[str, str]:
    selectors: dict[str, str] = {}
    with (root / RECORD / "contract.tsv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if tuple(reader.fieldnames or ()) != CONTRACT_COLUMNS:
            raise ValueError(f"contract.tsv columns must be {CONTRACT_COLUMNS}")
        for row in reader:
            key, selector = row["key"], row["selector"]
            if None in row or not key or not selector or key in selectors:
                raise ValueError(f"contract.tsv line {reader.line_num}: a key must appear once, with a selector")
            problem = CENSUS.selector_error(selector)
            if problem:
                raise ValueError(f"contract.tsv line {reader.line_num}: {problem}")
            selectors[key] = selector
    if not selectors:
        raise ValueError("contract.tsv declares no combination")
    return selectors


def declared_sites(root: Path, documents: list[Document], selectors: dict[str, str]) -> dict[tuple[str, str], int]:
    """(document, key) -> declarations in the exact committed bytes, whose digest must be the pinned one."""
    conjunctions = {s: CENSUS.compile_conjunction(s) for s in selectors.values() if CENSUS.is_conjunction(s)}
    counts: dict[tuple[str, str], int] = {}
    for document in documents:
        path = CENSUS.spec_in(root / "tests" / "fixtures" / "corpus-sources" / document.fixture)
        if path is None:
            raise ValueError(f"{document.fixture}: no committed source; restore it from git")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != document.sha256:
            raise ValueError(f"{document.fixture}: committed source is {digest}, not the handed-off {document.sha256}")
        found = CENSUS.census_document(CENSUS.load_document(path), conjunctions=conjunctions, root_path=path)
        for key, selector in selectors.items():
            counts[document.document, key] = found.get(selector, 0)
    return counts


# llmlint: ignore[modern_domain_modeling] `CombinationProofClass` lives in golden-reach.py, a hyphenated script loaded by path and so typed `Any` here; the body converts the value to that enum, refusing any other.
def verdict_of(proof_class: str | None, cooccurrence: bool, declared: int, arm: ArmCount | None) -> Verdict:
    """The verdict its measurements imply; `proof_class` is a `CombinationProofClass` value, or None unaudited."""
    if proof_class is not None:
        REACH.CombinationProofClass(proof_class)  # An unknown class raises ValueError, never reads as a witness.
    if declared == 0:
        return Verdict.NOT_DECLARED
    if cooccurrence or arm is None:
        return Verdict.NO_EXCLUSIVE_ARM
    if arm.executed == 0:
        return Verdict.ARM_NOT_EXECUTED
    return Verdict.POOLED_ARM_EXECUTED if proof_class == REACH.CombinationProofClass.OPEN else Verdict.WITNESS


def classes(root: Path) -> tuple[dict[str, Any], dict[str, SiteRow]]:
    """Each audit row (its class and witness), and the site table; the census scripts own both types."""
    audit, failures = REACH.read_cooccurrence(root / "docs/openapi-surface/combination-cooccurrence.tsv")
    if failures:
        raise ValueError("; ".join(failures))
    return audit, REACH.read_sites_table(root / "docs/openapi-surface/golden-reach-sites.tsv")


def _view(path: Path) -> dict[str, set[Region]]:
    """A measurement view's `file -> regions`, refusing anything but ordered four-integer spans."""
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ValueError(f"cannot read {path}: {error}; run `just census-repin`") from error
    if not isinstance(loaded, dict):
        raise ValueError(f"{path} is not a file-to-regions map; run `just census-repin`")
    regions: dict[str, set[Region]] = {}
    for file, spans in loaded.items():
        if not isinstance(spans, list) or not all(
            isinstance(span, list) and len(span) == 4 and all(type(cell) is int for cell in span) for span in spans
        ):
            raise ValueError(f"{path}: {file}'s regions are not four integers each; run `just census-repin`")
        parsed = {Region(*span) for span in spans}
        for region in parsed:
            if min(region) < 1 or (region.start_line, region.start_column) > (region.end_line, region.end_column):
                raise ValueError(
                    f"{path}: {file}'s region {list(region)} is not an ordered source span; run `just census-repin`"
                )
        regions[file] = parsed
    return regions


def measure(root: Path) -> list[VerdictRow]:
    documents = population(root)
    selectors = contract(root)
    counts = declared_sites(root, documents, selectors)
    registrations = CENSUS.golden_registrations(root / "crates/crozier-e2e/tests/e2e.rs")
    audit, table = classes(root)
    universe = _view(root / VIEWS / "universe.json")
    rows = []
    for document in documents:
        registration = registrations.get(document.fixture)
        if registration is None:
            raise ValueError(f"{document.fixture}: no golden test registers it")
        hit = _view(root / VIEWS / "tests" / f"{registration.test}.json")
        for key in sorted(selectors):
            declared = counts[document.document, key]
            cooccurrence = key not in table or table[key].cooccurrence
            arm = None
            if not cooccurrence:
                site = REACH.resolve_site(table[key].sites[0], root)
                if site.file not in universe or site.file not in hit:
                    raise ValueError(f"{registration.test}: no measurement of {site.file}; run `just census-repin`")
                regions = {region for region in universe[site.file] if site.holds(region)}
                arm = ArmCount(len(regions & hit[site.file]), len(regions))
            proof = audit[key].proof_class if key in audit else None
            rows.append(
                VerdictRow(
                    CombinationKey(key),
                    document.document,
                    document.sha256,
                    document.fixture,
                    registration.test,
                    len(registration.unmatched),
                    declared,
                    arm,
                    verdict_of(proof, cooccurrence, declared, arm),
                )
            )
    return rows


def read_rows(root: Path) -> list[VerdictRow]:
    with (root / RECORD / "handed-off-verdicts.tsv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if tuple(reader.fieldnames or ()) != COLUMNS:
            raise ValueError(f"handed-off-verdicts.tsv columns must be {COLUMNS}")
        rows = []
        for row in reader:
            if None in row or None in row.values():
                raise ValueError(f"handed-off-verdicts.tsv line {reader.line_num}: extra or missing cells")
            rows.append(VerdictRow.parse(row))
    return rows


class CandidateState(StrEnum):
    DECIDED = "decided"
    OUTSTANDING = "outstanding"


class Outcome(NamedTuple):
    """A census `outcome` cell: its state, and the reason after the first colon."""

    state: CandidateState
    reason: str

    @classmethod
    def parse(cls, text: str, where: str) -> Outcome:
        state, separator, reason = text.partition(":")
        try:
            parsed = CandidateState(state)
        except ValueError as error:
            raise ValueError(f"{where}: unknown candidate state {state!r}") from error
        if not separator or not reason.strip():
            raise ValueError(f"{where}: a candidate outcome needs a reason")
        return cls(parsed, reason.strip())

    def __str__(self) -> str:
        return f"{self.state}: {self.reason}"


@dataclass
class CensusRow:
    """One candidate of `census.tsv.gz`; columns this tool does not read travel in `other`."""

    key: CombinationKey
    document: str
    sha256: Sha256
    # None where the census recorded no count, because the source bytes were unavailable.
    sites: int | None
    outcome: Outcome
    other: dict[str, str]

    @classmethod
    def parse(cls, cells: dict[str, str], where: str) -> CensusRow:
        if not cells["key"] or not cells["document"]:
            raise ValueError(f"{where}: an empty key or document")
        # An unavailable document has no recorded digest; any other cell must be one.
        if cells["sha256"] != NOT_MEASURED and not SHA256.fullmatch(cells["sha256"]):
            raise ValueError(f"{where}: {cells['sha256']!r} is no SHA-256")
        sites = None if cells["sites"] == NOT_MEASURED else _count(cells["sites"], f"{where}: sites")
        known = {"key", "document", "sha256", "sites", "outcome"}
        return cls(
            CombinationKey(cells["key"]),
            cells["document"],
            Sha256(cells["sha256"]),
            sites,
            Outcome.parse(cells["outcome"], where),
            {name: value for name, value in cells.items() if name not in known},
        )

    def cell(self, column: str) -> str:
        if column == "sites":
            return NOT_MEASURED if self.sites is None else str(self.sites)
        return self.other[column] if column in self.other else str(getattr(self, column))


def read_census(root: Path) -> tuple[list[str], list[CensusRow]]:
    text = gzip.decompress((root / RECORD / "census.tsv.gz").read_bytes()).decode("utf-8")
    reader = csv.DictReader(io.StringIO(text, newline=""), delimiter="\t")
    columns = list(reader.fieldnames or ())
    if len(columns) != len(set(columns)):
        raise ValueError("census.tsv.gz repeats a column name")
    if not set(columns) >= CENSUS_COLUMNS:
        raise ValueError(f"census.tsv.gz lacks {sorted(CENSUS_COLUMNS - set(columns))}")
    rows = []
    for number, row in enumerate(reader, start=2):
        if None in row or None in row.values():
            raise ValueError(f"census.tsv.gz line {number}: extra or missing cells")
        rows.append(CensusRow.parse(row, f"census.tsv.gz line {number}"))
    return columns, rows


def rendered_census(columns: list[str], rows: list[CensusRow]) -> str:
    """The one canonical serialization `canonical_census_failures` holds: sorted over every column."""
    written = io.StringIO(newline="")
    writer = csv.writer(written, delimiter="\t", lineterminator="\n")
    writer.writerow(columns)
    writer.writerows(sorted([row.cell(column) for column in columns] for row in rows))
    return written.getvalue()


def restated_census(root: Path, verdicts: list[VerdictRow]) -> tuple[list[str], list[CensusRow]]:
    columns, rows = read_census(root)
    by_cell = {(row.key, row.document): row for row in verdicts}
    seen = set()
    for row in rows:
        verdict_row = by_cell.get((row.key, row.document))
        if verdict_row is not None:
            seen.add((row.key, row.document))
            if row.sha256 not in {NOT_MEASURED, verdict_row.sha256}:
                raise ValueError(
                    f"{row.key} on {row.document}: census.tsv.gz pins {row.sha256}, not {verdict_row.sha256}"
                )
            row.sha256 = verdict_row.sha256
            row.sites = verdict_row.declared_sites
            row.outcome = verdict_row.outcome()
    for cell, verdict_row in sorted(by_cell.items()):
        if cell not in seen:
            other = dict.fromkeys(set(columns) - {"key", "document", "sha256", "sites", "outcome"}, "-")
            other.update(kind="combination", licence="not-reassessed")
            rows.append(
                CensusRow(
                    cell[0],
                    cell[1],
                    verdict_row.sha256,
                    verdict_row.declared_sites,
                    verdict_row.outcome(),
                    other,
                )
            )
    return columns, rows


def proven_keys(root: Path) -> set[str]:
    audit, _table = classes(root)
    return {key for key, row in audit.items() if row.proof_class == REACH.CombinationProofClass.INTERACTION}


class Outstanding(NamedTuple):
    """One document's open combinations, and each distinct reason they stay open."""

    keys: list[str]
    reasons: list[str]


def restated_index(root: Path, rows: list[CensusRow]) -> str:
    """`outstanding-candidates.tsv`: each open key's outstanding candidates, with the reasons."""
    proven = proven_keys(root)
    open_rows: dict[tuple[str, str], Outstanding] = {}
    for row in rows:
        if row.outcome.state is not CandidateState.OUTSTANDING or row.key in proven:
            continue
        entry = open_rows.setdefault((row.document, row.sha256), Outstanding([], []))
        entry.keys.append(row.key)
        if row.outcome.reason not in entry.reasons:
            entry.reasons.append(row.outcome.reason)
    written = io.StringIO(newline="")
    writer = csv.writer(written, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE)
    writer.writerow(("document", "sha256", "combinations", "why_not_screened"))
    for (document, sha256), entry in sorted(open_rows.items()):
        writer.writerow((document, sha256, ",".join(sorted(entry.keys)), "; ".join(sorted(entry.reasons))))
    return written.getvalue()


def restated_readme(root: Path, rows: list[CensusRow]) -> str:
    text = (root / RECORD / "README.md").read_text(encoding="utf-8")
    proven = proven_keys(root)
    candidates: dict[str, int] = {}
    outstanding: dict[str, int] = {}
    for row in rows:
        candidates[row.key] = candidates.get(row.key, 0) + 1
        outstanding[row.key] = outstanding.get(row.key, 0) + (row.outcome.state is CandidateState.OUTSTANDING)

    def restate(match: re.Match[str]) -> str:
        key = match.group(1)
        if key in proven:
            return f"| `{key}` | `interaction-proven` | {candidates[key]} | 0 |"
        return f"| `{key}` | `search-incomplete` | {candidates[key]} | {outstanding[key]} |"

    return re.sub(
        r"^\| `(combo-[^`]+)` \| `(?:search-incomplete|interaction-proven)` \| \d+ \| \d+ \|$",
        restate,
        text,
        flags=re.M,
    )


def write(root: Path) -> None:
    """Render all four artifacts from validated inputs, then write them: nothing changes on a refusal."""
    rows = measure(root)
    columns, census = restated_census(root, rows)
    written = io.StringIO(newline="")
    writer = csv.writer(written, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE)
    writer.writerow(COLUMNS)
    writer.writerows(row.cells() for row in rows)
    compressed = gzip.compress(rendered_census(columns, census).encode("utf-8"), compresslevel=9, mtime=0)
    index = restated_index(root, census)
    readme = restated_readme(root, census)
    (root / RECORD / "handed-off-verdicts.tsv").write_text(written.getvalue(), encoding="utf-8", newline="\n")
    (root / RECORD / "census.tsv.gz").write_bytes(compressed)
    (root / RECORD / "outstanding-candidates.tsv").write_text(index, encoding="utf-8", newline="\n")
    (root / RECORD / "README.md").write_text(readme, encoding="utf-8", newline="\n")


def failures(root: Path, counts: dict[tuple[str, str], int] | None = None) -> list[str]:
    """Every way the committed verdicts differ from the committed bytes, audit and record.

    `counts` is `declared_sites`' answer, for a caller that already censused these bytes.
    """
    try:
        rows = read_rows(root)
        documents = population(root)
        selectors = contract(root)
        counts = declared_sites(root, documents, selectors) if counts is None else counts
        audit, table = classes(root)
        registrations = CENSUS.golden_registrations(root / "crates/crozier-e2e/tests/e2e.rs")
        _columns, census = read_census(root)
    except (OSError, ValueError, KeyError, EOFError) as error:
        return [f"handed-off-verdicts.tsv: {error}"]
    found = []
    by_document = {document.document: document for document in documents}
    expected = {(document.document, key) for document in documents for key in selectors}
    cells = {(row.document, row.key): row for row in rows}
    if len(cells) != len(rows):
        found.append("handed-off-verdicts.tsv repeats a document and combination")
    found += [f"{key}: no verdict on {document}" for document, key in sorted(expected - set(cells))]
    found += [
        f"{key}: a verdict on {document}, outside the population" for document, key in sorted(set(cells) - expected)
    ]
    for (document, key), row in sorted(cells.items()):
        if (document, key) not in expected:
            continue
        where = f"{key} on {document}"
        pinned = by_document[document]
        if (row.sha256, row.fixture) != (pinned.sha256, pinned.fixture):
            found.append(
                f"{where}: records {row.fixture} at {row.sha256}, not the handed-off {pinned.fixture} at {pinned.sha256}"
            )
        if row.declared_sites != counts[document, key]:
            found.append(
                f"{where}: records {row.declared_sites} declarations; the bytes declare {counts[document, key]}"
            )
        registered = registrations.get(row.fixture)
        if registered is None or registered.test != row.golden_test:
            found.append(f"{where}: `{row.golden_test}` is not {row.fixture}'s golden test")
        elif len(registered.unmatched) != row.unmatched_files:
            found.append(
                f"{where}: records {row.unmatched_files} unmatched files; it registers {len(registered.unmatched)}"
            )
        cooccurrence = key not in table or table[key].cooccurrence
        if cooccurrence != (row.arm is None):
            found.append(f"{where}: its arm measurement disagrees with the site table")
            continue
        proof = audit[key].proof_class if key in audit else None
        if row.verdict != verdict_of(proof, cooccurrence, row.declared_sites, row.arm):
            found.append(f"{where}: verdict `{row.verdict}` does not follow from its measurements")
        if row.verdict is Verdict.WITNESS and row.unmatched_files:
            found.append(f"{where}: a witness must byte-match whole; it leaves {row.unmatched_files} files unmatched")
    populated = {document.fixture for document in documents}
    for key in FORMER_HANDWRITTEN:
        if key not in audit or audit[key].proof_class != REACH.CombinationProofClass.INTERACTION:
            continue
        witness = audit[key].witness
        if witness in populated and not any(
            row.key == key and row.fixture == witness and row.verdict is Verdict.WITNESS for row in rows
        ):
            found.append(
                f"{key}: its audit names {witness} as its witness, but no verdict says that run executes the arm"
            )
    named: dict[tuple[str, str], CensusRow] = {}
    for row in census:
        identity = (row.document, row.key)
        if identity in cells and identity in named:
            found.append(f"{row.key} on {row.document}: census.tsv.gz names it twice")
        named[identity] = row
    for cell, row in sorted(cells.items()):
        stated = named.get(cell)
        if stated is None:
            found.append(f"{cell[1]} on {cell[0]}: census.tsv.gz does not name it")
        elif stated.sha256 != row.sha256:
            found.append(f"{cell[1]} on {cell[0]}: census.tsv.gz pins {stated.sha256}, not {row.sha256}")
        elif stated.outcome != row.outcome():
            found.append(f"{cell[1]} on {cell[0]}: census.tsv.gz does not state its verdict `{row.verdict}`")
        elif stated.sites != row.declared_sites:
            found.append(
                f"{cell[1]} on {cell[0]}: census.tsv.gz counts {stated.sites} declarations, not {row.declared_sites}"
            )
    index = (root / RECORD / "outstanding-candidates.tsv").read_text(encoding="utf-8")
    if index != restated_index(root, census):
        found.append("outstanding-candidates.tsv does not restate census.tsv.gz; run this script's `write`")
    if (root / RECORD / "README.md").read_text(encoding="utf-8") != restated_readme(root, census):
        found.append("the record's verdict table does not restate census.tsv.gz; run this script's `write`")
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("mode", choices=("write", "check"))
    parser.add_argument("--repo-root", type=Path, default=REPO)
    args = parser.parse_args()
    if args.mode == "write":
        try:
            write(args.repo_root.resolve())
        except (OSError, ValueError, KeyError, EOFError) as error:
            print(f"handed-off-combination-verdicts: wrote nothing \u2014 {error}", file=sys.stderr)
            return 1
        return 0
    problems = failures(args.repo_root.resolve())
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        print("the verdicts are stale \u2014 run `just census-repin`, then this script's `write`", file=sys.stderr)
    return int(bool(problems))


if __name__ == "__main__":
    # The CLI emits UTF-8 even when a Windows pipe defaults to a legacy codec.
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main())
