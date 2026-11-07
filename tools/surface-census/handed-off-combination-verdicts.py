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
from pathlib import Path
from typing import Any, NamedTuple

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
RECORD = Path("docs/openapi-surface/witness-search-operation-combinations")
HANDED_OFF = Path("docs/fern-measurements/handed-off")
VIEWS = Path(".local/golden-reach")
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
OUTSTANDING_VERDICTS = {"declared-no-exclusive-arm", "declared-pooled-arm-executed"}
REASONS = {
    "not-declared": "fresh exact-byte source census does not declare this combination",
    "declared-arm-not-executed": "registered byte-matching golden declares it, and its instrumented run never executes the arm",
    "witness": "registered byte-matching golden declares it and its instrumented run executes the exclusive arm",
    "declared-no-exclusive-arm": (
        "registered byte-matching golden declares it, but crozier has no exclusive counter region "
        "for its run to execute, so the meeting point cannot be screened"
    ),
    "declared-pooled-arm-executed": (
        "registered byte-matching golden declares it and executes the declared region, "
        "which is pooled with other cases, so the execution does not imply both features"
    ),
}


class Document(NamedTuple):
    document: str
    sha256: str
    fixture: str


def _load(name: str, file: str) -> Any:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    if spec is None or spec.loader is None:
        raise SystemExit(f"handed-off-combination-verdicts: cannot load tools/surface-census/{file}; restore it from git")
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
        for row in csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE):
            if row["status"] != "registered":
                continue
            named = re.fullmatch(r"\d+ \((.+)\)", row["corpus_row"])
            if not named:
                raise ValueError(f"{row['document']}: a registered row must name its fixture: {row['corpus_row']!r}")
            found[row["document"]] = Document(row["document"], row["sha256"], named.group(1))
    readme = (root / HANDED_OFF / "README.md").read_text(encoding="utf-8")
    admitted = readme.partition("## Newly admitted documents")[2].split("\n## ", 1)[0]
    for document, sha256 in re.findall(r"^- `([^`]+)` \| `([0-9a-f]{64})`", admitted, re.M):
        if document not in found or found[document].sha256 != sha256:
            raise ValueError(f"{document}: newly admitted, but not the same `registered` row of documents.tsv")
    return sorted(found.values())


def contract(root: Path) -> dict[str, str]:
    with (root / RECORD / "contract.tsv").open(encoding="utf-8", newline="") as handle:
        return {row["key"]: row["selector"] for row in csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)}


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


def verdict(proof_class: str | None, cooccurrence: bool, declared: int, executed: str) -> str:
    if declared == 0:
        return "not-declared"
    if cooccurrence:
        return "declared-no-exclusive-arm"
    if int(executed) == 0:
        return "declared-arm-not-executed"
    return "witness" if proof_class != "open" else "declared-pooled-arm-executed"


def classes(root: Path) -> tuple[dict[str, str | None], dict[str, Any]]:
    audit, failures = REACH.read_cooccurrence(root / "docs/openapi-surface/combination-cooccurrence.tsv")
    if failures:
        raise ValueError("; ".join(failures))
    return {key: row.proof_class for key, row in audit.items()}, REACH.read_sites_table(
        root / "docs/openapi-surface/golden-reach-sites.tsv"
    )


def measure(root: Path) -> list[dict[str, str]]:
    documents = population(root)
    selectors = contract(root)
    counts = declared_sites(root, documents, selectors)
    registrations = CENSUS.golden_registrations(root / "crates/crozier-e2e/tests/e2e.rs")
    proof, table = classes(root)
    universe = json.loads((root / VIEWS / "universe.json").read_text(encoding="utf-8"))
    rows = []
    for document in documents:
        registration = registrations[document.fixture]
        hit = json.loads((root / VIEWS / "tests" / f"{registration.test}.json").read_text(encoding="utf-8"))
        for key in sorted(selectors):
            declared = counts[document.document, key]
            cooccurrence = key not in table or table[key].cooccurrence
            executed = total = NOT_MEASURED
            if not cooccurrence:
                site = REACH.resolve_site(table[key].sites[0], root)
                regions = {tuple(r) for r in universe.get(site.file, []) if site.holds(tuple(r))}
                executed = str(len(regions & {tuple(r) for r in hit.get(site.file, [])}))
                total = str(len(regions))
            rows.append(
                dict(
                    zip(
                        COLUMNS,
                        (
                            key,
                            document.document,
                            document.sha256,
                            document.fixture,
                            registration.test,
                            str(len(registration.unmatched)),
                            str(declared),
                            executed,
                            total,
                            verdict(proof.get(key), cooccurrence, declared, executed),
                        ),
                        strict=True,
                    )
                )
            )
    return rows


def read_rows(root: Path) -> list[dict[str, str]]:
    with (root / RECORD / "handed-off-verdicts.tsv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if tuple(reader.fieldnames or ()) != COLUMNS:
            raise ValueError(f"handed-off-verdicts.tsv columns must be {COLUMNS}")
        return list(reader)


def outcome(row: dict[str, str]) -> str:
    state = "outstanding" if row["verdict"] in OUTSTANDING_VERDICTS else "decided"
    return f"{state}: {row['verdict']}: {REASONS[row['verdict']]}"


def read_census(root: Path) -> tuple[list[str], list[dict[str, str]]]:
    text = gzip.decompress((root / RECORD / "census.tsv.gz").read_bytes()).decode("utf-8")
    reader = csv.DictReader(io.StringIO(text, newline=""), delimiter="\t")
    return list(reader.fieldnames or ()), list(reader)


def rendered_census(columns: list[str], rows: list[dict[str, str]]) -> str:
    """The one canonical serialization `canonical_census_failures` holds: sorted over every column."""
    written = io.StringIO(newline="")
    writer = csv.writer(written, delimiter="\t", lineterminator="\n")
    writer.writerow(columns)
    writer.writerows(sorted([row[column] for column in columns] for row in rows))
    return written.getvalue()


def restated_census(root: Path, verdicts: list[dict[str, str]]) -> tuple[list[str], list[dict[str, str]]]:
    columns, rows = read_census(root)
    by_cell = {(row["key"], row["document"]): row for row in verdicts}
    seen = set()
    for row in rows:
        verdict_row = by_cell.get((row["key"], row["document"]))
        if verdict_row is not None:
            seen.add((row["key"], row["document"]))
            row["sites"] = verdict_row["declared_sites"]
            row["outcome"] = outcome(verdict_row)
    for cell, verdict_row in sorted(by_cell.items()):
        if cell not in seen:
            added = dict.fromkeys(columns, "-")
            added.update(
                key=cell[0],
                document=cell[1],
                sha256=verdict_row["sha256"],
                kind="combination",
                sites=verdict_row["declared_sites"],
                licence="not-reassessed",
                outcome=outcome(verdict_row),
            )
            rows.append(added)
    return columns, rows


def proven_keys(root: Path) -> set[str]:
    return {key for key, kind in classes(root)[0].items() if kind == "interaction"}


def restated_index(root: Path, rows: list[dict[str, str]]) -> str:
    """`outstanding-candidates.tsv`: each open key's outstanding candidates, one reason per document."""
    proven = proven_keys(root)
    open_rows: dict[tuple[str, str], tuple[list[str], list[str]]] = {}
    for row in rows:
        state, _, reason = row["outcome"].partition(":")
        if state != "outstanding" or row["key"] in proven:
            continue
        keys, reasons = open_rows.setdefault((row["document"], row["sha256"]), ([], []))
        keys.append(row["key"])
        if reason.strip() not in reasons:
            reasons.append(reason.strip())
    written = io.StringIO(newline="")
    writer = csv.writer(written, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE)
    writer.writerow(("document", "sha256", "combinations", "why_not_screened"))
    for (document, sha256), (keys, reasons) in sorted(open_rows.items()):
        writer.writerow((document, sha256, ",".join(sorted(keys)), "; ".join(sorted(reasons))))
    return written.getvalue()


def restated_readme(root: Path, rows: list[dict[str, str]]) -> str:
    text = (root / RECORD / "README.md").read_text(encoding="utf-8")
    proven = proven_keys(root)
    candidates: dict[str, int] = {}
    outstanding: dict[str, int] = {}
    for row in rows:
        candidates[row["key"]] = candidates.get(row["key"], 0) + 1
        outstanding[row["key"]] = outstanding.get(row["key"], 0) + row["outcome"].startswith("outstanding:")

    def restate(match: re.Match[str]) -> str:
        key = match.group(1)
        if key in proven:
            return f"| `{key}` | `interaction-proven` | {candidates[key]} | 0 |"
        return f"| `{key}` | `search-incomplete` | {candidates[key]} | {outstanding[key]} |"

    return re.sub(r"^\| `(combo-[^`]+)` \| `(?:search-incomplete|interaction-proven)` \| \d+ \| \d+ \|$", restate, text, flags=re.M)


def write(root: Path) -> None:
    rows = measure(root)
    written = io.StringIO(newline="")
    writer = csv.DictWriter(written, COLUMNS, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE)
    writer.writeheader()
    writer.writerows(rows)
    (root / RECORD / "handed-off-verdicts.tsv").write_text(written.getvalue(), encoding="utf-8", newline="\n")
    columns, census = restated_census(root, rows)
    (root / RECORD / "census.tsv.gz").write_bytes(
        gzip.compress(rendered_census(columns, census).encode("utf-8"), compresslevel=9, mtime=0)
    )
    (root / RECORD / "outstanding-candidates.tsv").write_text(restated_index(root, census), encoding="utf-8", newline="\n")
    (root / RECORD / "README.md").write_text(restated_readme(root, census), encoding="utf-8", newline="\n")


def failures(root: Path) -> list[str]:
    """Every way the committed verdicts differ from the committed bytes, audit and record."""
    try:
        rows = read_rows(root)
        documents = population(root)
        selectors = contract(root)
        counts = declared_sites(root, documents, selectors)
        proof, table = classes(root)
        registrations = CENSUS.golden_registrations(root / "crates/crozier-e2e/tests/e2e.rs")
    except (OSError, ValueError, KeyError) as error:
        return [f"handed-off-verdicts.tsv: {error}"]
    found = []
    expected = {(document.document, key) for document in documents for key in selectors}
    cells = {(row["document"], row["key"]): row for row in rows}
    if len(cells) != len(rows):
        found.append("handed-off-verdicts.tsv repeats a document and combination")
    found += [f"{key}: no verdict on {document}" for document, key in sorted(expected - set(cells))]
    found += [f"{key}: a verdict on {document}, outside the population" for document, key in sorted(set(cells) - expected)]
    for (document, key), row in sorted(cells.items()):
        if (document, key) not in expected:
            continue
        where = f"{key} on {document}"
        if row["declared_sites"] != str(counts[document, key]):
            found.append(f"{where}: records {row['declared_sites']} declarations; the bytes declare {counts[document, key]}")
        registered = registrations.get(row["fixture"])
        if registered is None or registered.test != row["golden_test"]:
            found.append(f"{where}: `{row['golden_test']}` is not {row['fixture']}'s golden test")
        elif str(len(registered.unmatched)) != row["unmatched_files"]:
            found.append(f"{where}: records {row['unmatched_files']} unmatched files; it registers {len(registered.unmatched)}")
        cooccurrence = key not in table or table[key].cooccurrence
        if cooccurrence != (row["arm_regions_executed"] == NOT_MEASURED):
            found.append(f"{where}: its arm measurement disagrees with the site table")
            continue
        if row["verdict"] != verdict(proof.get(key), cooccurrence, int(row["declared_sites"]), row["arm_regions_executed"]):
            found.append(f"{where}: verdict `{row['verdict']}` does not follow from its measurements")
        if row["verdict"] == "witness" and row["unmatched_files"] != "0":
            found.append(f"{where}: a witness must byte-match whole; it leaves {row['unmatched_files']} files unmatched")
    _columns, census = read_census(root)
    named = {(row["document"], row["key"]): row for row in census}
    for cell, row in sorted(cells.items()):
        if cell in named and named[cell]["outcome"] != outcome(row):
            found.append(f"{cell[1]} on {cell[0]}: census.tsv.gz does not state its verdict `{row['verdict']}`")
        if cell not in named:
            found.append(f"{cell[1]} on {cell[0]}: census.tsv.gz does not name it")
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
        write(args.repo_root.resolve())
        return 0
    problems = failures(args.repo_root.resolve())
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        print("run `just census-repin`, then this script's `write`", file=sys.stderr)
    return int(bool(problems))


if __name__ == "__main__":
    raise SystemExit(main())
