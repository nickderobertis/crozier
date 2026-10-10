#!/usr/bin/env python3
"""Read and measure the hand-written generation fixtures.

A hand-written fixture is generation evidence of a lower level than a real
specification: a document written for the purpose, admitted only where the
real-specification search for its shape failed, with the tree Fern generated
from it. The contract — directory layout, `evidence.toml`, the `handwritten`
category and its ledger — is stated once, in
`docs/openapi-surface/handwritten/AGENTS.md`. Two subcommands:

* ``gate`` checks every fixture directory against that contract as far as the
  committed documents can say: its layout, its `evidence.toml`, each cover
  against the region rows, the site table, both reach ledgers and the search
  record it cites, both directions between the fixtures and the `handwritten`
  rows and reach ledger, and that nothing a fixture holds is a corpus row, a
  corpus golden or a census source. It prints one JSON object, the parsed pins
  and digest of each fixture and every failure, for
  `handwritten_fixtures_match_fern_goldens` in `crates/crozier-e2e/tests/e2e.rs`, which adds the
  checks only Rust can make: Contract A's digest, the pin, and crozier's
  byte-match against `fern-expected/`. It exits 0 when that list is empty and
  1 when it is not (the JSON is printed either way), so the exit status alone
  says whether the gate passed.
* ``measure`` runs an instrumented crozier over each fixture's `openapi.yml`
  alone — one run per fixture, the way `golden-reach.py measure` scopes one
  golden test — and writes `docs/openapi-surface/handwritten-reach.tsv`, one row
  per arm-level cover. `just handwritten-reach` runs it.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path
from typing import Any, Final, Literal, NamedTuple, NewType

REPO = Path(__file__).resolve().parents[2]
REGIONS = Path("docs") / "openapi-surface"
HANDWRITTEN = REGIONS / "handwritten"
REACH_LEDGER = REGIONS / "handwritten-reach.tsv"
REACH_HEADER = ("fixture", "key", "site", "regions_executed", "regions")
# The measured configuration gate: for each arm-level cover of a fixture that
# declares a generation setting, the arm's reach with that setting and without it.
GATE_LEDGER = REGIONS / "handwritten-config-gates.tsv"
GATE_HEADER = ("fixture", "key", "site", "setting", "regions_executed", "regions")
UNSET = "-"
CATEGORIES = ("golden", "limitations", "handwritten", "gap")
LAYOUT = ("evidence.toml", "fern-expected", "openapi.yml")
TOP_LEVEL = ("covers", "digest", "fern_cli_version", "fern_python_sdk_version")
# Optional generation settings: absent, crozier and Fern generate the whole API.
OPTIONAL_TOP_LEVEL = ("audiences",)
COVER_FIELDS = ("arm", "key", "renewed", "search", "verdict")
SearchVerdict = Literal["exhausted", "search-incomplete", "config-gated"]
VERDICTS: tuple[SearchVerdict, ...] = ("exhausted", "search-incomplete", "config-gated")
# A verdict only an arm-search record states, beside the settlement rule's
# outcomes: the arm runs only under a generation setting no search probe sets.
ARM_VERDICTS = ("config-gated",)
# Every word a search record states as an outcome, so a key row stating a
# different one than the cover cites is read as a disagreement, and the
# non-generation verdicts that make a row `limitations`. RankedBacklogTests holds
# both to the vocabularies the census suite gates.
OUTCOMES = ("witness-found", "witness-blocked", "fern-rejected", "none-found", "search-incomplete", "exhausted")
NON_GENERATION = ("discards", "ignores", "refuses", "crashes", "coincidence")
FIXTURE_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EVIDENCE_CELL = re.compile(
    r"^handwritten: (?P<fixtures>[a-z0-9-]+(?:, [a-z0-9-]+)*); "
    r"search: (?P<verdict>[a-z-]+) \(\[record\]\((?P<link>[^)\s]+)\)\)$"
)
E2E_COVERS = REGIONS / "handwritten-e2e.toml"
E2E_EVIDENCE_CELL = re.compile(
    r"^handwritten-e2e: (?P<fixture>docs/fern-measurements/[a-z0-9/-]+); "
    r"test: (?P<test>[a-z0-9_]+); evidence: \[note\]\((?P<evidence>[^)\s]+)\); "
    r"search: (?P<verdict>[a-z-]+) \(\[record\]\((?P<link>[^)\s]+)\)\)$"
)
_CORPUS_ROW = re.compile(r"^\s*\|\s*\d+\s*\|")


def _load(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, module)
    spec.loader.exec_module(module)
    return module


def golden_reach() -> Any:
    return _load("handwritten_golden_reach", REPO / "tools" / "surface-census" / "golden-reach.py")


def region_keys() -> Any:
    """The one reader of `witness-search-keys.tsv`, the searched key set."""
    return _load("handwritten_region_keys", REPO / "tools" / "surface-census" / "witness-search-region-keys.py")


def census() -> Any:
    return _load("handwritten_census", REPO / "tools" / "surface-census" / "openapi-surface-census.py")


class Cover(NamedTuple):
    key: str
    arm: str | None
    search: str
    verdict: str
    renewed: str | None


class Fixture(NamedTuple):
    name: str
    fern_cli_version: str
    fern_python_sdk_version: str
    digest: str
    covers: tuple[Cover, ...]
    audiences: tuple[str, ...]


# The census key of the shape a cover proves, shared with the region row it settles.
ShapeKey = NewType("ShapeKey", str)
E2E_KIND: Final = "handwritten-e2e"


class E2ECover(NamedTuple):
    """One validated `handwritten-e2e.toml` cover: a multi-document loopback journey."""

    kind: Literal["handwritten-e2e"]
    key: ShapeKey
    fixture: str
    test: str
    evidence: str
    golden: str
    search: str
    verdict: SearchVerdict
    renewed: str


E2E_FIELDS = set(E2ECover._fields)


def table_cells(line: str) -> list[str]:
    """One markdown table line's cells; `\\|` inside a cell is an escaped pipe."""
    if not line.startswith("|"):
        return []
    return [cell.replace("\x00", "\\|").strip() for cell in line.replace("\\|", "\x00").strip().strip("|").split("|")]


def region_rows(root: Path) -> dict[str, tuple[str, list[str]]]:
    """Every entry-table row of the region files: key -> (region file name, its eight cells)."""
    rows: dict[str, tuple[str, list[str]]] = {}
    for path in sorted((root / REGIONS).glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            cells = table_cells(line)
            if len(cells) == 8 and cells[3].strip("`") in CATEGORIES:
                rows[cells[0].strip("`")] = (path.name, cells)
    return rows


def read_evidence(directory: Path) -> tuple[Fixture | None, list[str]]:
    """`evidence.toml`, held to exactly the keys and types the contract names."""
    name = directory.name
    path = directory / "evidence.toml"
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError) as error:
        return None, [f"{name}: evidence.toml cannot be read ({error}); write it as the contract states"]
    except tomllib.TOMLDecodeError as error:
        return None, [f"{name}: evidence.toml is not TOML ({error}); repair its syntax"]
    failures = []
    if not set(TOP_LEVEL) <= set(data) <= set(TOP_LEVEL) | set(OPTIONAL_TOP_LEVEL):
        failures.append(
            f"{name}: evidence.toml carries keys {sorted(data)}; the contract admits exactly "
            f"{sorted(TOP_LEVEL)}, and optionally {sorted(OPTIONAL_TOP_LEVEL)} — remove or add keys "
            "until they match"
        )
    for field in ("fern_cli_version", "fern_python_sdk_version", "digest"):
        if field in data and not isinstance(data[field], str):
            failures.append(f"{name}: evidence.toml `{field}` is not a string")
    audiences = data.get("audiences", [])
    if "audiences" in data and (
        not isinstance(audiences, list)
        or not audiences
        or not all(isinstance(audience, str) and audience.strip() == audience and audience for audience in audiences)
    ):
        failures.append(
            f"{name}: evidence.toml `audiences` is {audiences!r}; it is a non-empty list of audience "
            "names, the same list Fern's generator group was given — or remove it to generate the whole API"
        )
        audiences = []
    covers: list[Cover] = []
    raw = data.get("covers", [])
    if not isinstance(raw, list) or not raw:
        failures.append(
            f"{name}: evidence.toml has no cover — a fixture admitted as evidence names at "
            "least one `[[covers]]` table, each citing its failed search"
        )
        raw = []
    for index, table in enumerate(raw, start=1):
        where = f"{name}: cover {index}"
        if not isinstance(table, dict):
            failures.append(f"{where} is not a `[[covers]]` table")
            continue
        extra = sorted(set(table) - set(COVER_FIELDS))
        missing = sorted({"key", "search", "verdict"} - set(table))
        if extra or missing:
            failures.append(
                f"{where} carries unknown field(s) {extra} and lacks {missing}; a cover has "
                "`key`, `search`, `verdict`, and optionally `arm` and `renewed`"
            )
            continue
        if not all(isinstance(value, str) and value for value in table.values()):
            failures.append(f"{where}: every field is a non-empty string")
            continue
        verdict = table["verdict"]
        if verdict not in VERDICTS:
            failures.append(
                f"{where} (`{table['key']}`): verdict `{verdict}` is not `exhausted`, "
                "`search-incomplete` or `config-gated`; only a failed search, or an arm no search "
                "can reach, admits a hand-written fixture"
            )
        if verdict == "search-incomplete" and "renewed" not in table:
            failures.append(
                f"{where} (`{table['key']}`): verdict `search-incomplete` without a `renewed` "
                "record — cite the renewed search that found the key `none-registrable`"
            )
        if verdict != "search-incomplete" and "renewed" in table:
            failures.append(
                f"{where} (`{table['key']}`): `renewed` is required exactly when the verdict "
                "is `search-incomplete`; remove it"
            )
        covers.append(Cover(table["key"], table.get("arm"), table["search"], verdict, table.get("renewed")))
    fixture = Fixture(
        name,
        str(data.get("fern_cli_version", "")),
        str(data.get("fern_python_sdk_version", "")),
        str(data.get("digest", "")),
        tuple(covers),
        tuple(audiences),
    )
    return fixture, failures


def heading_anchors(text: str) -> dict[str, tuple[int, int]]:
    """GitHub's anchor for each heading -> (its line index, its level)."""
    anchors: dict[str, tuple[int, int]] = {}
    fenced = False
    for index, line in enumerate(text.splitlines()):
        if line.startswith("```"):
            fenced = not fenced
            continue
        heading = re.match(r"^(#{1,6}) (.+?)\s*#*\s*$", line)
        if fenced or not heading:
            continue
        title = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading.group(2)).lower()
        slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        candidate, suffix = slug, 1
        while candidate in anchors:
            candidate, suffix = f"{slug}-{suffix}", suffix + 1
        anchors[candidate] = (index, len(heading.group(1)))
    return anchors


def record_section(root: Path, reference: str) -> tuple[str | None, str | None]:
    """The text a `path#anchor` reference names, or why it names none."""
    path, _, anchor = reference.partition("#")
    if not path or not anchor:
        return None, f"`{reference}` is not `<repo-relative path>#<anchor>`"
    target = root / path
    if not target.is_file():
        return None, f"`{path}` does not exist"
    text = target.read_text(encoding="utf-8")
    anchors = heading_anchors(text)
    if anchor not in anchors:
        return None, f"no heading of `{path}` has the anchor `#{anchor}`"
    start, level = anchors[anchor]
    lines = text.splitlines()
    end = len(lines)
    for index in range(start + 1, len(lines)):
        heading = re.match(r"^(#{1,6}) ", lines[index])
        if heading and len(heading.group(1)) <= level:
            end = index
            break
    return "\n".join(lines[start:end]), None


def key_rows(section: str, key: str) -> list[list[str]]:
    return [cells for cells in map(table_cells, section.splitlines()) if cells and cells[0].strip("`") == key]


def verdict_failures(base: Path, reference: str, key: str, verdict: str) -> list[str]:
    """`reference` (`<path>#<anchor>`, relative to `base`) resolves, and the record
    it names states `verdict` — and no other outcome — on every line of `key`."""
    section, error = record_section(base, reference)
    if section is None:
        return [f"its search anchor does not resolve: {error}"]
    rows = key_rows(section, key)
    stated = {cell.strip("`") for cells in rows for cell in cells if cell.strip("`") in (*OUTCOMES, *ARM_VERDICTS)}
    if not rows or stated != {verdict}:
        return [
            f"the record `{reference}` states {sorted(stated) or 'no verdict'} for `{key}`, "
            f"not `{verdict}` — cite the verdict the record states"
        ]
    return []


def evidence_cell_failures(region: Path, key: str, cell: str) -> list[str]:
    """A `handwritten` row's evidence cell: its form, and the record its link names
    stating the verdict it states. The link is relative to the region file."""
    parsed = EVIDENCE_CELL.match(cell) or E2E_EVIDENCE_CELL.match(cell)
    if parsed is None:
        return [
            f"{key}: its evidence cell must read `handwritten: <fixture>[, <fixture>…]; search: "
            "<verdict> ([record](<link>))`"
        ]
    return [
        f"{key}: {failure}"
        for failure in verdict_failures(region.parent, parsed.group("link"), key, parsed.group("verdict"))
    ]


def search_failures(root: Path, where: str, cover: Cover) -> list[str]:
    """The cited record resolves, states the cover's verdict for its key (and arm)."""
    failures = [f"{where}: {failure}" for failure in verdict_failures(root, cover.search, cover.key, cover.verdict)]
    if failures and "does not resolve" in failures[0]:
        return failures
    if cover.arm is not None:
        record = (root / cover.search.partition("#")[0]).read_text(encoding="utf-8")
        if f"`{cover.arm}`" not in record:
            failures.append(
                f"{where}: the record `{cover.search}` does not name the arm `{cover.arm}` — "
                "cite the arm search that searched for it"
            )
    if cover.renewed is not None:
        renewed = root / cover.renewed
        if not renewed.is_file():
            failures.append(f"{where}: its `renewed` record `{cover.renewed}` does not exist")
        elif not any(
            "none-registrable" in {cell.strip("`") for cell in cells}
            for cells in key_rows(renewed.read_text(encoding="utf-8"), cover.key)
        ):
            failures.append(
                f"{where}: its `renewed` record `{cover.renewed}` does not name `{cover.key}` "
                "with the outcome `none-registrable`"
            )
    return failures


def read_reach_ledger(path: Path) -> tuple[list[tuple[str, str, str, int, int]], list[str]]:
    """`handwritten-reach.tsv`: its header, its rows and their order."""
    name = path.name
    if not path.is_file():
        return [], [
            f"{name}: missing — restore it (`git checkout -- {path.as_posix()}`) or run `just handwritten-reach`"
        ]
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or tuple(lines[0].split("\t")) != REACH_HEADER:
        return [], [
            f"{name}: the header line must be exactly {'<TAB>'.join(REACH_HEADER)}; run `just handwritten-reach`"
        ]
    rows, failures = [], []
    for number, line in enumerate(lines[1:], start=2):
        fields = line.split("\t")
        if len(fields) != len(REACH_HEADER) or not fields[3].isdigit() or not fields[4].isdigit():
            failures.append(
                f"{name} line {number}: not five tab-separated fields ending in two counts; run `just handwritten-reach`"
            )
            continue
        rows.append((fields[0], fields[1], fields[2], int(fields[3]), int(fields[4])))
    keys = [row[:3] for row in rows]
    if keys != sorted(keys) or len(keys) != len(set(keys)):
        failures.append(
            f"{name}: rows are not sorted by fixture, key and site with none twice; run `just handwritten-reach`"
        )
    return rows, failures


def setting_of(fixture: Fixture) -> str:
    """The generation setting a fixture declares, as the gate ledger spells it."""
    return f"audiences={','.join(fixture.audiences)}" if fixture.audiences else UNSET


def read_gate_ledger(path: Path) -> tuple[list[tuple[str, str, str, str, int, int]], list[str]]:
    """`handwritten-config-gates.tsv`: its header, its rows and their order."""
    name = path.name
    if not path.is_file():
        return [], [
            f"{name}: missing — restore it (`git checkout -- {path.as_posix()}`) or run `just handwritten-reach`"
        ]
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or tuple(lines[0].split("\t")) != GATE_HEADER:
        return [], [
            f"{name}: the header line must be exactly {'<TAB>'.join(GATE_HEADER)}; run `just handwritten-reach`"
        ]
    rows, failures = [], []
    for number, line in enumerate(lines[1:], start=2):
        fields = line.split("\t")
        if len(fields) != len(GATE_HEADER) or not fields[4].isdigit() or not fields[5].isdigit():
            failures.append(
                f"{name} line {number}: not six tab-separated fields ending in two counts; run `just handwritten-reach`"
            )
            continue
        rows.append((fields[0], fields[1], fields[2], fields[3], int(fields[4]), int(fields[5])))
    keys = [row[:4] for row in rows]
    if keys != sorted(keys) or len(keys) != len(set(keys)):
        failures.append(
            f"{name}: rows are not sorted by fixture, key, site and setting with none twice; run `just handwritten-reach`"
        )
    return rows, failures


def gate_ledger_failures(fixtures: dict[str, Fixture], rows: list[tuple[str, str, str, str, int, int]]) -> list[str]:
    """Each arm-level cover of a fixture declaring a setting is measured with and without it.

    A `config-gated` cover's fixture must declare the setting its record says
    gates the arm, so the pair shows the arm run with it and not without it.
    """
    failures = []
    expected = set()
    for name, fixture in sorted(fixtures.items()):
        for cover in fixture.covers:
            where = f"{name}: cover `{cover.key}`" + (f" arm `{cover.arm}`" if cover.arm else "")
            if cover.verdict == "config-gated" and (cover.arm is None or not fixture.audiences):
                failures.append(
                    f"{where}: a `config-gated` cover is arm-level and its fixture declares the setting "
                    "that gates the arm — add `arm` and the setting, or cite a search verdict"
                )
            if cover.arm is not None and fixture.audiences:
                expected |= {(name, cover.key, cover.arm, setting_of(fixture)), (name, cover.key, cover.arm, UNSET)}
    measured = {row[:4] for row in rows}
    for missing in sorted(expected - measured):
        failures.append(
            f"handwritten-config-gates.tsv: no row for `{missing[0]}` `{missing[1]}` `{missing[2]}` with setting "
            f"`{missing[3]}` — run `just handwritten-reach`"
        )
    for extra in sorted(measured - expected):
        failures.append(
            f"handwritten-config-gates.tsv: the row `{extra[0]}` `{extra[1]}` `{extra[2]}` `{extra[3]}` names no "
            "live arm-level cover of a fixture declaring that setting — run `just handwritten-reach`"
        )
    return failures


def corpus_rows(root: Path) -> set[str]:
    """Every numbered `CORPUS.md` row's name, whatever its decision."""
    manifest = root / "tests" / "fixtures" / "CORPUS.md"
    if not manifest.is_file():
        return set()
    names = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if _CORPUS_ROW.match(line):
            cells = [cell.strip().strip("`").strip() for cell in line.split("|")]
            if len(cells) > 2 and cells[2]:
                names.add(cells[2])
    return names


def e2e_cover_failures(root: Path, rows: dict[str, tuple[str, list[str]]]) -> tuple[set[str], list[str]]:
    """Strict additive covers for committed multi-document loopback journeys.

    Ordinary three-entry fixtures and their cover rules are unchanged. This
    separate versioned record never supplies an ordinary fixture's cover.
    """
    path = root / E2E_COVERS
    if not path.exists():
        return set(), []
    failures: list[str] = []
    keys: set[str] = set()
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        return keys, [
            f"{E2E_COVERS}: cannot read cover records: {error} — restore the registry or repair its TOML syntax"
        ]
    if (
        set(data) != {"version", "covers"}
        or type(data.get("version")) is not int
        or data.get("version") != 1
        or not isinstance(data.get("covers"), list)
    ):
        return keys, [
            f"{E2E_COVERS}: invalid registry fields {sorted(data)}, version {data.get('version')!r} or covers type {type(data.get('covers')).__name__} — expected version = 1 and covers tables; repair the registry to contain only those fields"
        ]

    def committed_path(value: str) -> Path | None:
        candidate = root / value
        relative = Path(value)
        return candidate if not relative.is_absolute() and ".." not in relative.parts else None

    test_path = root / "crates" / "crozier-e2e" / "tests" / "e2e.rs"
    test_source = test_path.read_text(encoding="utf-8") if test_path.is_file() else ""
    for table in data["covers"]:
        if (
            not isinstance(table, dict)
            or set(table) != E2E_FIELDS
            or not all(isinstance(v, str) and v for v in table.values())
        ):
            failures.append(
                f"{E2E_COVERS}: a cover must have exactly {sorted(E2E_FIELDS)}, all nonempty strings — repair this cover table to contain those fields and supply a nonempty string for each"
            )
            continue
        where = f"handwritten-e2e `{table['key']}`"
        if table["kind"] != E2E_KIND:
            failures.append(f"{where}: invalid kind `{table['kind']}` — set kind to handwritten-e2e")
            continue
        verdict = next((known for known in VERDICTS if known == table["verdict"]), None)
        if verdict is None:
            failures.append(f"{where}: invalid real-specification search verdict — cite one of {', '.join(VERDICTS)}")
            continue
        cover = E2ECover(
            kind=E2E_KIND,
            key=ShapeKey(table["key"]),
            fixture=table["fixture"],
            test=table["test"],
            evidence=table["evidence"],
            golden=table["golden"],
            search=table["search"],
            verdict=verdict,
            renewed=table["renewed"],
        )
        key = cover.key
        if key in keys:
            failures.append(f"{where}: duplicate key — keep exactly one registry cover for this shape")
            continue
        keys.add(key)
        fixture = committed_path(cover.fixture)
        if fixture is None or not fixture.is_dir() or len(list(fixture.glob("*.yml"))) < 2:
            failures.append(f"{where}: commit the named multi-file fixture directory")
        evidence = committed_path(cover.evidence)
        if evidence is None or not evidence.is_file():
            failures.append(f"{where}: commit the named evidence note")
        golden = committed_path(cover.golden)
        if golden is None or not golden.is_dir() or not (golden / ".fern" / "metadata.json").is_file():
            failures.append(f"{where}: commit the complete certified golden")
        test = re.search(
            r"#\[test\]\s*fn " + re.escape(cover.test) + r"\(\)\s*\{([\s\S]*?)(?=\n#\[test\]|\Z)", test_source
        )
        body = test.group(1) if test else ""
        required = (
            "LocalDocumentServer::start",
            "probe_command",
            "golden_tree_failures",
            "assert!(failures.is_empty()",
        )
        fixture_include = cover.fixture + "/"
        if not body or any(token not in body for token in required) or fixture_include not in body:
            failures.append(
                f"{where}: name a gated real-binary test serving this fixture over loopback and comparing its complete tree"
            )
        golden_prefix, _, golden_suffix = cover.golden.rpartition("/")
        golden_prefix, _, fixture_name = golden_prefix.rpartition("/")
        constants = re.findall(r'const ([A-Z_]+): &str = "([^"]+)";', test_source)
        names_prefix = any(name in body and value == golden_prefix for name, value in constants)
        if cover.golden not in body and not (names_prefix and f"{fixture_name}/{golden_suffix}" in body):
            failures.append(f"{where}: the gated test must name this certified golden")
        if committed_path(cover.search.partition("#")[0]) is None or committed_path(cover.renewed) is None:
            failures.append(
                f"{where}: invalid search {cover.search!r} or renewed {cover.renewed!r} — replace it with a repository-relative path without parent traversal"
            )
        else:
            failures += search_failures(root, where, Cover(key, None, cover.search, cover.verdict, cover.renewed))
        row = rows.get(key)
        evidence_link = os.path.relpath(root / cover.evidence, root / REGIONS).replace(os.sep, "/")
        search_path, _, anchor = cover.search.partition("#")
        search_link = os.path.relpath(root / search_path, root / REGIONS).replace(os.sep, "/") + "#" + anchor
        expected = (
            f"handwritten-e2e: {cover.fixture}; test: {cover.test}; "
            f"evidence: [note]({evidence_link}); search: {cover.verdict} ([record]({search_link}))"
        )
        if row is None or row[1][3] != "handwritten" or row[1][4] != expected or any(row[1][5:8]):
            failures.append(
                f"{where}: its handwritten row must name exactly this fixture, test, evidence and search, with empty remaining cells"
            )
    for key, (_region, cells) in rows.items():
        if cells[4].startswith("handwritten-e2e:") and key not in keys:
            failures.append(
                f"{key}: handwritten-e2e row has no cover record — add its registry cover or remove the unsupported row"
            )
    return keys, failures


def gate(root: Path) -> dict[str, Any]:
    """Every contract failure the committed documents show, and each fixture's pins and digest."""
    failures: list[str] = []
    base = root / HANDWRITTEN
    if not base.is_dir():
        return {
            "fixtures": {},
            "failures": [f"{HANDWRITTEN.as_posix()}: missing — the fixture directory must exist, with its AGENTS.md"],
        }
    fixtures: dict[str, Fixture] = {}
    for entry in sorted(base.iterdir()):
        if entry.is_file() and entry.name == "AGENTS.md":
            continue
        if not entry.is_dir():
            failures.append(
                f"{entry.name}: is under {HANDWRITTEN.as_posix()}/ but is not a fixture directory — move or remove it"
            )
            continue
        name = entry.name
        if not FIXTURE_NAME.match(name):
            failures.append(f"{name}: a fixture name is lower-kebab; rename the directory")
        present = sorted(child.name for child in entry.iterdir())
        for missing in sorted(set(LAYOUT) - set(present)):
            reason = {
                "fern-expected": "the complete comment-stripped tree Fern generated from openapi.yml; a document Fern refuses cannot be a fixture",
                "openapi.yml": "the hand-written OpenAPI document",
                "evidence.toml": "the cover record",
            }[missing]
            failures.append(f"{name}: {missing} is missing — commit {reason}")
        for extra in sorted(set(present) - set(LAYOUT)):
            failures.append(f"{name}: {extra} is not part of a fixture; it holds exactly {', '.join(LAYOUT)}")
        if (entry / "fern-expected").exists() and not (entry / "fern-expected").is_dir():
            failures.append(f"{name}: fern-expected is not a directory — replace it with the tree Fern generated")
        if not (entry / "evidence.toml").is_file():
            continue
        fixture, found = read_evidence(entry)
        failures += found
        if fixture is not None:
            fixtures[name] = fixture

    rows = region_rows(root)
    e2e_keys, found = e2e_cover_failures(root, rows)
    failures += found
    reach = golden_reach()
    try:
        sites = reach.read_sites_table(root / REGIONS / "golden-reach-sites.tsv")
    except SystemExit as error:
        sites = {}
        failures.append(str(error))
    try:
        ledger = {r.key: r for _rank, r in reach.read_ledger(root / REGIONS / "golden-reach.tsv")}
    except (SystemExit, OSError) as error:
        ledger = {}
        failures.append(f"golden-reach.tsv: {error}")
    try:
        selectors = region_keys().tracked_selectors(root / REGIONS)
    except ValueError as error:
        selectors = {}
        failures.append(f"witness-search-keys.tsv: {error}")
    reach_rows, found = read_reach_ledger(root / REACH_LEDGER)
    failures += found
    measured = {(f, k, s): (executed, total) for f, k, s, executed, total in reach_rows}
    gate_rows, found = read_gate_ledger(root / GATE_LEDGER)
    failures += found + gate_ledger_failures(fixtures, gate_rows)
    engine = census()

    feature_covers: dict[str, list[tuple[str, Cover]]] = {}
    arm_covers: set[tuple[str, str, str]] = set()
    for name, fixture in sorted(fixtures.items()):
        document = None
        for cover in fixture.covers:
            where = f"{name}: cover `{cover.key}`" + (f" arm `{cover.arm}`" if cover.arm else "")
            failures += search_failures(root, where, cover)
            if cover.key not in rows:
                failures.append(f"{where}: no region row carries this key — spell it as its region file does")
                continue
            category = rows[cover.key][1][3].strip("`")
            if cover.arm is None:
                feature_covers.setdefault(cover.key, []).append((name, cover))
                if category != "handwritten":
                    failures.append(
                        f"{where}: a feature-level cover's row must read `handwritten`, and it reads "
                        f"`{category}` — reclassify the row, or make the cover arm-level"
                    )
                selector = selectors.get(cover.key)
                if selector is None:
                    failures.append(
                        f"{where}: witness-search-keys.tsv records no selector for this key — a feature-level "
                        "cover needs a key its real-specification search ran on; re-derive the file with "
                        "`tools/surface-census/witness-search-region-keys.py`, or cover a searched key"
                    )
                    continue
                spec = root / HANDWRITTEN / name / "openapi.yml"
                if not spec.is_file():
                    continue
                if document is None:
                    try:
                        document = engine.census_document(engine.load_document(spec))
                    except (SystemExit, ValueError, engine.DocumentError) as error:
                        failures.append(f"{name}: the census cannot read openapi.yml ({error})")
                        break
                if not document.get(selector):
                    failures.append(
                        f"{where}: openapi.yml declares no site of `{selector}`, the key's census "
                        "selector — the fixture must declare the shape it covers"
                    )
                continue
            arm_covers.add((name, cover.key, cover.arm))
            if category != "golden":
                failures.append(f"{where}: an arm-level cover's row must read `golden`, and it reads `{category}`")
            if cover.key not in sites or cover.arm not in sites[cover.key].sites:
                failures.append(
                    f"{where}: golden-reach-sites.tsv lists no such site for this key — spell the arm "
                    "exactly as the site table does"
                )
            executed = measured.get((name, cover.key, cover.arm))
            if executed is None:
                failures.append(f"{where}: handwritten-reach.tsv has no row for it — run `just handwritten-reach`")
            elif executed[0] < 1:
                failures.append(
                    f"{where}: handwritten-reach.tsv measures 0 of its {executed[1]} regions executed, "
                    "so the fixture does not reach the arm it covers"
                )
            golden = ledger.get(cover.key)
            spec_counts = {spec: hit for spec, hit, _total in golden.sites} if golden else {}
            if cover.arm not in spec_counts:
                failures.append(
                    f"{where}: golden-reach.tsv measures no such site for this key — re-run "
                    "`just golden-reach-report` if the site table changed, or spell the arm as it does"
                )
            elif spec_counts[cover.arm] > 0:
                failures.append(
                    f"{where}: golden-reach.tsv now reports the arm reached by a real specification, "
                    "which supersedes the fixture — remove this cover"
                )

    for fixture, key, site in sorted(set(measured) - arm_covers):
        failures.append(
            f"handwritten-reach.tsv: the row `{fixture}` `{key}` `{site}` names no live arm-level "
            "cover — run `just handwritten-reach`"
        )

    manifest = root / REGIONS / "probe-expected" / "MANIFEST.tsv"
    proofs = {}
    if manifest.is_file():
        for line in manifest.read_text(encoding="utf-8").splitlines()[1:]:
            fields = line.split("\t")
            if len(fields) == 6:
                proofs[fields[0]] = fields[2]
    for key, (_region, cells) in sorted(rows.items()):
        if cells[3].strip("`") != "handwritten":
            continue
        if key in e2e_keys and cells[4].startswith("handwritten-e2e:"):
            continue
        failures += handwritten_row_failures(key, cells, feature_covers.get(key, []))
        if proofs.get(key) in NON_GENERATION:
            failures.append(
                f"{key}: a committed non-generation proof settles it, so it is `limitations`, not `handwritten`"
            )
        if key in sites:
            failures.append(
                f"{key}: golden-reach-sites.tsv lists it, so a golden source declares it and it is not `handwritten`"
            )

    failures += isolation_failures(root, sorted(e.name for e in base.iterdir() if e.is_dir()), ledger)
    return {
        "fixtures": {
            name: {
                "fern_cli_version": fixture.fern_cli_version,
                "fern_python_sdk_version": fixture.fern_python_sdk_version,
                "digest": fixture.digest,
                "audiences": list(fixture.audiences),
            }
            for name, fixture in fixtures.items()
        },
        "failures": failures,
    }


def handwritten_row_failures(key: str, cells: list[str], covers: list[tuple[str, Cover]]) -> list[str]:
    """A `handwritten` row: a feature-level cover names it, and its cells say so."""
    if not covers:
        return [
            f"{key}: the row reads `handwritten`, but no fixture's feature-level cover names it — "
            "add the cover, or return the row to the category its evidence supports"
        ]
    failures = []
    if any(cells[5:8]):
        failures.append(
            f"{key}: a `handwritten` row's `crozier sites`, `why bytes could move` and `settlement` cells are empty"
        )
    parsed = EVIDENCE_CELL.match(cells[4])
    if parsed is None:
        return [
            *failures,
            f"{key}: its evidence cell must read `handwritten: <fixture>[, <fixture>…]; search: "
            "<verdict> ([record](<link>))`",
        ]
    named = parsed.group("fixtures").split(", ")
    if named != sorted({name for name, _cover in covers}):
        failures.append(
            f"{key}: its evidence cell names {named}, but the fixtures whose feature-level covers "
            f"name it are {sorted({name for name, _cover in covers})} (sorted)"
        )
    link = parsed.group("link")
    path, _, anchor = link.partition("#")
    target = os.path.normpath((REGIONS / path).as_posix()).replace(os.sep, "/")
    cited = {(cover.search, cover.verdict) for _name, cover in covers}
    if cited != {(f"{target}#{anchor}", parsed.group("verdict"))}:
        failures.append(
            f"{key}: its evidence cell cites `{parsed.group('verdict')}` at `{target}#{anchor}`, but its "
            f"covers cite {sorted(cited)}"
        )
    return failures


def isolation_failures(root: Path, names: list[str], ledger: dict[str, Any]) -> list[str]:
    """Nothing under the fixture directory enters a real-specification count."""
    failures = []
    corpus = corpus_rows(root)
    manifest = root / "tests" / "fixtures" / "CORPUS.md"
    if manifest.is_file() and HANDWRITTEN.as_posix() in manifest.read_text(encoding="utf-8"):
        failures.append(f"CORPUS.md: names {HANDWRITTEN.as_posix()}/; a hand-written fixture is never a corpus row")
    witnesses = {w for reach in ledger.values() for w in (*reach.witnesses, *reach.outside)}
    base = (root / HANDWRITTEN).resolve()
    engine = census()
    fixtures_root = root / "tests" / "fixtures"
    sources = (
        engine.registered_sources(fixtures_root, root / ".local" / "corpus", True) if fixtures_root.is_dir() else []
    )
    for source in sources:
        if source.path is not None and source.path.resolve().is_relative_to(base):
            failures.append(
                f"{source.fixture}: the census reads it from {HANDWRITTEN.as_posix()}/; a hand-written "
                "fixture is never a census source"
            )
    for name in names:
        if name in corpus:
            failures.append(
                f"{name}: is also a CORPUS.md row; a hand-written fixture is never a corpus row — rename it"
            )
        if (fixtures_root / name).exists():
            failures.append(
                f"{name}: tests/fixtures/{name} exists; a hand-written fixture is never a corpus golden — rename it"
            )
        if name in witnesses:
            failures.append(
                f"{name}: golden-reach.tsv counts it as a witness; the golden-only tier never reads a hand-written fixture"
            )
    return failures


def measure(args: argparse.Namespace) -> int:
    """One instrumented crozier run per fixture with an arm-level cover; write the ledger."""
    repo_root: Path = args.repo_root
    base: Path = args.handwritten_dir or repo_root / HANDWRITTEN
    ledger: Path = args.ledger or repo_root / REACH_LEDGER
    gates: Path = args.gates or repo_root / GATE_LEDGER
    if not base.is_dir():
        raise SystemExit(f"handwritten-reach: {base} is not a directory; pass --handwritten-dir or restore it")
    reach = golden_reach()
    sites = reach.read_sites_table(repo_root / REGIONS / "golden-reach-sites.tsv")
    planned: list[tuple[str, Cover]] = []
    declared: dict[str, Fixture] = {}
    for entry in sorted(p for p in base.iterdir() if p.is_dir()):
        fixture, failures = read_evidence(entry)
        if failures or fixture is None:
            raise SystemExit("handwritten-reach: " + "; ".join(failures))
        declared[entry.name] = fixture
        for cover in fixture.covers:
            if cover.arm is None:
                continue
            if cover.key not in sites or cover.arm not in sites[cover.key].sites:
                raise SystemExit(
                    f"handwritten-reach: {entry.name}: cover `{cover.key}` arm `{cover.arm}` is not a site "
                    "golden-reach-sites.tsv lists for that key; spell it as the site table does"
                )
            reach.resolve_site(cover.arm, repo_root)
            planned.append((entry.name, cover))
    rows: list[tuple[str, str, str, int, int]] = []
    gate_rows: list[tuple[str, str, str, str, int, int]] = []
    if planned:
        crozier = instrumented_crozier(repo_root, reach)
        profdata, llvm_cov = reach._llvm_tool("llvm-profdata"), reach._llvm_tool("llvm-cov")
        runs: dict[str, tuple[dict, dict]] = {}
        for name in sorted({name for name, _cover in planned}):
            runs[name] = scoped_run(
                base / name / "openapi.yml", declared[name].audiences, crozier, profdata, llvm_cov, repo_root, reach
            )
        # A fixture declaring a setting is measured without it too: the control
        # half of the configuration gate its covers' records rest on.
        controls = {
            name: scoped_run(base / name / "openapi.yml", (), crozier, profdata, llvm_cov, repo_root, reach)
            for name in sorted({name for name, _cover in planned if declared[name].audiences})
        }

        def reached(run: tuple[dict, dict], arm: str) -> tuple[int, int]:
            universe, hit = run
            site = reach.resolve_site(arm, repo_root)
            regions = {tuple(r) for r in universe.get(site.file, []) if site.holds(r)}
            return len(regions & {tuple(r) for r in hit.get(site.file, [])}), len(regions)

        for name, cover in planned:
            # `planned` holds the arm-level covers alone.
            assert cover.arm is not None
            rows.append((name, cover.key, cover.arm, *reached(runs[name], cover.arm)))
            if name in controls:
                gate_rows.append(
                    (name, cover.key, cover.arm, setting_of(declared[name]), *reached(runs[name], cover.arm))
                )
                gate_rows.append((name, cover.key, cover.arm, UNSET, *reached(controls[name], cover.arm)))
    rows.sort(key=lambda row: row[:3])
    gate_rows.sort(key=lambda row: row[:4])
    for path, header, lines in ((ledger, REACH_HEADER, rows), (gates, GATE_HEADER, gate_rows)):
        path.write_text(
            "\n".join(["\t".join(header)] + ["\t".join(map(str, row)) for row in lines]) + "\n",
            encoding="utf-8",
        )
    print(
        f"handwritten-reach: measured {len(rows)} arm-level cover(s) into {ledger}, "
        f"{len(gate_rows) // 2} configuration gate(s) into {gates}"
    )
    return 0


def instrumented_crozier(repo_root: Path, reach: Any) -> Path:
    """Build the instrumented crozier `just golden-reach` measures with, and return it."""
    build = subprocess.run(
        [
            "cargo",
            "llvm-cov",
            "--locked",
            "--no-report",
            "nextest",
            "--workspace",
            "-E",
            "binary(e2e) and test(=every_feature_target_has_its_own_golden_test)",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if build.returncode != 0:
        sys.stderr.write(build.stdout[-4000:] + build.stderr[-4000:])
        raise SystemExit(
            "handwritten-reach: the instrumented build failed (its output is above); fix what it names and re-run"
        )
    _e2e, crozier = reach._instrumented_binaries(repo_root)
    return crozier


def scoped_run(
    spec: Path, audiences: tuple[str, ...], crozier: Path, profdata: str, llvm_cov: str, repo_root: Path, reach: Any
) -> tuple[dict, dict]:
    """(every production region, the executed ones) of one crozier run over `spec` alone,
    filtered to the fixture's `audiences` as the gate generates it."""
    with tempfile.TemporaryDirectory(prefix="handwritten-reach-") as scratch:
        raw = Path(scratch)
        run = subprocess.run(
            [
                str(crozier),
                "generate",
                "python",
                "--spec",
                str(spec),
                "--output",
                str(raw / "sdk"),
                "--package-name",
                "fern",
                "--project-name",
                "default_package_name",
                *(argument for audience in audiences for argument in ("--audience", audience)),
            ],
            cwd=repo_root,
            capture_output=True,
            text=True,
            env=dict(os.environ, LLVM_PROFILE_FILE=str(raw / "%p-%m.profraw")),
        )
        if run.returncode != 0:
            raise SystemExit(
                f"handwritten-reach: crozier failed over {spec} ({run.stderr.strip()[-600:]}); a fixture "
                "crozier cannot generate measures nothing — repair crozier and re-run"
            )
        merged = raw / "merged.profdata"
        reach.run_llvm(
            [profdata, "merge", "-sparse", *sorted(str(p) for p in raw.glob("*.profraw")), "-o", str(merged)]
        )
        export = raw / "export.json"
        with export.open("w", encoding="utf-8") as sink:
            reach.run_llvm([llvm_cov, "export", "-format=text", f"-instr-profile={merged}", str(crozier)], stdout=sink)
        return reach._covered(export, repo_root)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--repo-root", type=Path, default=REPO)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("gate", help="check every fixture against the contract; print JSON")
    m = sub.add_parser("measure", help="instrumented crozier per fixture; write handwritten-reach.tsv")
    m.add_argument("--handwritten-dir", type=Path, help="fixture directory (default: the committed one)")
    m.add_argument("--ledger", type=Path, help="ledger to write (default: the committed one)")
    m.add_argument("--gates", type=Path, help="configuration-gate ledger to write (default: the committed one)")
    args = parser.parse_args(argv)
    if args.command == "gate":
        result = gate(args.repo_root)
        json.dump(result, sys.stdout, indent=1)
        sys.stdout.write("\n")
        return 1 if result["failures"] else 0
    return measure(args)


if __name__ == "__main__":
    sys.exit(main())
