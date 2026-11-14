#!/usr/bin/env python3
"""Re-measure the output-insensitive comparison records at the certified pair.

`docs/openapi-surface/output-insensitive.tsv` decides a key output-insensitive
on a fern and a crozier comparison record. Each record holds the complete
before/after relative-file SHA-256 maps of one generator over two documents.
`output-insensitive.py` refuses a record that is not at the certified pair, so
moving the pair stales every record. This regenerates them.

Each record's documents are found beside it, by the rule its search filed it
under:
  - `<dir>/before.json` and `<dir>/after.json`, for a record in its own folder;
  - `removal-controls/<doc>.yml`, then `removal-controls/<stem>.json`, for
    `<stem>-fern.json` whose stem starts with `<doc>`; where that JSON is an edit
    record rather than a document, the after document is `<doc>.yml` with each
    pointer it names deleted;
  - the committed corpus source of `<doc>`, then `removal-controls/<doc>-after.yml`.
A record none of these resolves is refused: nothing is guessed.

Fern's tree is its raw packaged output (`fern generate --local --preview`),
from the workspace `tools/fern-goldens/generate-fern-fixture.sh` scaffolds:
`python_enums`, the `fern` organization, CI's invocation identity. crozier's is
the raw tree `crozier --no-config generate python` writes, as `fern`/
`default_package_name`. Fern runs one document at a time, each document once.

A record is rewritten only where its before and after trees are identical.
Where either generator's trees differ, no record is written: the rows citing
the record leave the table, and each differing path is printed. Nothing is
restated that was not measured.

Usage: output-insensitive-remeasure.py [--root DIR] [--fern CMD] [--crozier BIN] [--only RECORD]...
Exit status: 0 when every record was rewritten; 1 when a record's trees differ
(its rows were removed, each path printed) or a generation failed; 2 on a usage
error or a record whose documents do not resolve.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
from dataclasses import astuple, dataclass, fields
from enum import StrEnum
from pathlib import Path
from types import ModuleType

import yaml

CORPUS_SOURCES = Path("tests/fixtures/corpus-sources")
GENERATION_TIMEOUT_SECONDS = 1800
LIST_INDEX = re.compile(r"0|[1-9][0-9]*")


def load_reader() -> ModuleType:
    """`output-insensitive.py`, whose columns, pair and evidence-path rules this
    re-measure writes to, so neither file restates them."""
    spec = importlib.util.spec_from_file_location(
        "output_insensitive", Path(__file__).with_name("output-insensitive.py")
    )
    if spec is None or spec.loader is None:
        raise ImportError("cannot load output-insensitive.py beside this script")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


READER = load_reader()
REGISTRY: Path = READER.REGISTRY
COLUMNS: tuple[str, ...] = READER.COLUMNS


class UsageError(ValueError):
    """A record or argument the re-measure cannot act on."""


class GenerationError(RuntimeError):
    """A generator that did not write its tree."""


class Generator(StrEnum):
    FERN = "fern"
    CROZIER = "crozier"


@dataclass(frozen=True)
class Row:
    """One disposition of the shared table, in its column order."""

    key: str
    context: str
    search_record: str
    fern_comparison: str
    crozier_comparison: str

    def record(self, generator: Generator) -> str:
        return self.fern_comparison if generator is Generator.FERN else self.crozier_comparison


if tuple(field.name for field in fields(Row)) != COLUMNS:
    raise ImportError(f"Row's fields are not {REGISTRY}'s columns {COLUMNS}, in order")


@dataclass(frozen=True)
class Pair:
    """The certified Fern CLI and fern-python-sdk versions."""

    cli: str
    generator: str


@dataclass(frozen=True)
class Documents:
    before: Path
    after: Path


@dataclass(frozen=True)
class Outcome:
    """One record's re-measure: the trees, and the paths that differ."""

    record: str
    generator: Generator
    before: dict[str, str]
    after: dict[str, str]

    def differing(self) -> list[str]:
        return sorted(
            path for path in set(self.before) | set(self.after) if self.before.get(path) != self.after.get(path)
        )


def certified_pair(root: Path) -> Pair:
    """The pair `output-insensitive.py` holds every record to (it validates the declaration)."""
    try:
        cli, generator = READER.certified_pair(root)
        return Pair(cli, generator)
    except (OSError, ValueError, KeyError, TypeError) as error:
        raise UsageError(f"assets/scaffolding/metadata.json: {error}") from error


def read_rows(root: Path) -> list[Row]:
    """Every row, each complete and naming evidence inside the documentation
    tree, as `output-insensitive.py` requires before any file is read or written."""
    with (root / REGISTRY).open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if reader.fieldnames != list(COLUMNS):
            raise UsageError(f"{REGISTRY}: expected columns {COLUMNS}")
        rows = []
        for number, cells in enumerate(reader, 2):
            if set(cells) != set(COLUMNS) or not all(isinstance(v, str) and v for v in cells.values()):
                raise UsageError(f"{REGISTRY} line {number}: a row fills every column")
            row = Row(**{column: cells[column] for column in COLUMNS})
            for path in (row.search_record, row.fern_comparison, row.crozier_comparison):
                try:
                    READER.local_file(root, path)
                except ValueError as error:
                    raise UsageError(f"{REGISTRY} line {number}: {error}") from error
            rows.append(row)
        return rows


def write_rows(root: Path, rows: list[Row]) -> None:
    out = io.StringIO()
    writer = csv.writer(out, delimiter="\t", quoting=csv.QUOTE_NONE, lineterminator="\n")
    writer.writerow(COLUMNS)
    writer.writerows(astuple(row) for row in rows)
    (root / REGISTRY).write_text(out.getvalue(), encoding="utf-8")


def corpus_source(root: Path, name: str) -> Path | None:
    committed = root / CORPUS_SOURCES / name
    return next(
        (committed / f"openapi.{e}" for e in ("json", "yaml", "yml") if (committed / f"openapi.{e}").is_file()), None
    )


def pointer_parts(pointer: object) -> list[str] | None:
    """The unescaped tokens of a JSON pointer, or None when it is not one."""
    match pointer:
        case str() if pointer.startswith("/"):
            return [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
        case _:
            return None


def child(node: object, part: str) -> object:
    """The member `part` names in `node`, or None: a list index is a JSON
    pointer's decimal, within bounds."""
    match node:
        case dict() if part in node:
            return node[part]
        case list() if LIST_INDEX.fullmatch(part) and int(part) < len(node):
            return node[int(part)]
        case _:
            return None


def ablated(before: Path, edits_record: Path, doc: str, scratch: Path) -> Path:
    """The after document an edit record describes: `before` with each pointer it
    names deleted. A record whose fixture is not `doc`, an edit that is not a
    deletion, or a pointer that names nothing is refused rather than approximated."""
    record = json.loads(edits_record.read_text(encoding="utf-8"))
    match record:
        case {"fixture": str(fixture), "edits": [*edits]} if fixture == doc and edits:
            pass
        case _:
            raise UsageError(f"{edits_record}: an edit record names its fixture {doc!r} and at least one edit")
    document = yaml.safe_load(before.read_text(encoding="utf-8"))
    for edit in edits:
        match edit:
            case {"pointer": pointer, "edit": str(text)} if text.startswith("deleted"):
                parts = pointer_parts(pointer)
            case _:
                parts = None
        if not parts:
            raise UsageError(f"{edits_record}: {edit!r} is not a deletion at a JSON pointer")
        *parents, last = parts
        node: object = document
        for part in parents:
            node = child(node, part)
        match node:
            case dict() if last in node:
                del node[last]
            case list() if LIST_INDEX.fullmatch(last) and int(last) < len(node):
                del node[int(last)]
            case _:
                raise UsageError(f"{edits_record}: {edit['pointer']} names nothing in {before}")
    after = scratch / f"{edits_record.stem}.after.json"
    after.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
    return after


def documents(root: Path, record: str, scratch: Path) -> Documents:
    """The two documents a fern record measured, by the rule it was filed under.
    An edit record's after document is written into `scratch`."""
    path = root / record
    folder = path.parent
    if (folder / "before.json").is_file() and (folder / "after.json").is_file():
        return Documents(folder / "before.json", folder / "after.json")
    controls = folder / "removal-controls"
    stem = path.name.removesuffix("-fern.json")
    if stem == path.name:
        raise UsageError(f"{record}: a fern record is named `*-fern.json`")
    parts = stem.split("-")
    for cut in range(len(parts) - 1, 0, -1):
        doc = "-".join(parts[:cut])
        ablated_path = controls / f"{stem}.json"
        if (controls / f"{doc}.yml").is_file() and ablated_path.is_file():
            before = controls / f"{doc}.yml"
            control = json.loads(ablated_path.read_text(encoding="utf-8"))
            if isinstance(control, dict) and "openapi" in control:
                return Documents(before, ablated_path)
            return Documents(before, ablated(before, ablated_path, doc, scratch))
        source = corpus_source(root, doc)
        if source is not None and (controls / f"{doc}-after.yml").is_file():
            return Documents(source, controls / f"{doc}-after.yml")
    raise UsageError(f"{record}: no before/after documents resolve beside it")


def tree_digests(tree: Path) -> dict[str, str]:
    files = {
        path.relative_to(tree).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(tree.rglob("*"))
        if path.is_file()
    }
    if not files:
        raise GenerationError(f"{tree} holds no generated file")
    return files


GENERATORS_YML = """\
api:
  path: openapi/{name}
groups:
  python-sdk:
    generators:
      - name: fernapi/fern-python-sdk
        version: {version}
        config:
          pydantic_config:
            enum_type: python_enums
        output:
          location: local-file-system
          path: ../generated/python
"""


def fern_tree(
    fern: list[str], document: Path, pair: Pair, scratch: Path, log: Path, timeout: int = GENERATION_TIMEOUT_SECONDS
) -> dict[str, str]:
    """Fern's raw packaged tree for `document`, from the fixture recipe's workspace."""
    workspace = scratch / "fern"
    (workspace / "openapi").mkdir(parents=True)
    name = "openapi.json" if document.suffix == ".json" else "openapi.yml"
    (workspace / "openapi" / name).write_bytes(document.read_bytes())
    (workspace / "fern.config.json").write_text(
        json.dumps({"organization": "fern", "version": pair.cli}) + "\n", encoding="utf-8"
    )
    (workspace / "generators.yml").write_text(
        GENERATORS_YML.format(name=name, version=pair.generator), encoding="utf-8"
    )
    preview = scratch / "preview"
    preview.mkdir()
    environment = {
        **os.environ,
        "FERN_TOKEN": os.environ.get("FERN_TOKEN", "preview-only-no-publish"),
        "CI": os.environ.get("CI", "true"),
        "GITHUB_ACTIONS": os.environ.get("GITHUB_ACTIONS", "true"),
    }
    command = [*fern, "generate", "--group", "python-sdk", "--local", "--preview", "--output", str(preview), "--force"]
    with log.open("w", encoding="utf-8") as handle:
        result = subprocess.run(
            command,
            cwd=workspace,
            env=environment,
            stdout=handle,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
    tree = preview / "fern-python-sdk"
    if result.returncode != 0 or not (tree / "src").is_dir():
        raise GenerationError(f"fern exited {result.returncode} on {document} without a packaged SDK; see {log}")
    return tree_digests(tree)


def crozier_tree(
    crozier: Path, document: Path, scratch: Path, timeout: int = GENERATION_TIMEOUT_SECONDS
) -> dict[str, str]:
    out = scratch / "crozier"
    result = subprocess.run(
        [
            str(crozier),
            "--no-config",
            "generate",
            "python",
            "--spec",
            str(document),
            "--output",
            str(out),
            "--package-name",
            "fern",
            "--project-name",
            "default_package_name",
        ],
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    if result.returncode != 0:
        raise GenerationError(f"crozier exited {result.returncode} on {document}: {result.stderr.strip()}")
    return tree_digests(out)


def record_text(generator: Generator, pair: Pair, before: dict[str, str], after: dict[str, str]) -> str:
    record = {
        "schema_version": 1,
        "generator": str(generator),
        "fern_cli_version": pair.cli,
        "fern_python_sdk_version": pair.generator,
        "before": before,
        "after": after,
    }
    return json.dumps(record, indent=2) + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--fern", default="fern", help="the Fern CLI command (default: fern)")
    parser.add_argument("--crozier", type=Path, help="the crozier binary (default: ROOT/target/release/crozier)")
    parser.add_argument("--only", action="append", default=[], help="re-measure only this fern record")
    parser.add_argument(
        "--timeout",
        type=int,
        default=GENERATION_TIMEOUT_SECONDS,
        help="seconds one generation may run before its record is left unmeasured (default: 1800)",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    crozier = args.crozier or root / "target/release/crozier"
    logs = (
        Path(os.environ.get("ONEPIPELINE_NODE_SCRATCH_DIR") or tempfile.gettempdir()) / "output-insensitive-remeasure"
    )
    logs.mkdir(parents=True, exist_ok=True)
    try:
        if args.timeout <= 0:
            raise UsageError("--timeout is a positive number of seconds")
        try:
            fern = shlex.split(args.fern)
        except ValueError as error:
            raise UsageError(f"--fern {args.fern!r} is no command: {error}") from error
        if not fern:
            raise UsageError("--fern names no command")
        if not crozier.is_file():
            raise UsageError(f"{crozier} is not built; run `cargo build --release --locked`")
        pair = certified_pair(root)
        rows = read_rows(root)
        records = sorted({(row.fern_comparison, row.crozier_comparison) for row in rows})
        if args.only:
            unknown = set(args.only) - {fern for fern, _ in records}
            if unknown:
                raise UsageError(f"--only names no record of {REGISTRY}: {sorted(unknown)}")
            records = [record for record in records if record[0] in args.only]
        derived = logs / "ablations"
        derived.mkdir(exist_ok=True)
        plans = {fern: documents(root, fern, derived) for fern, _ in records}
    except (UsageError, OSError, json.JSONDecodeError, yaml.YAMLError) as error:
        print(f"output-insensitive-remeasure: {error}", file=sys.stderr)
        return 2
    measured: dict[tuple[Generator, Path], dict[str, str]] = {}

    def measure(generator: Generator, document: Path) -> dict[str, str]:
        key = (generator, document)
        if key not in measured:
            with tempfile.TemporaryDirectory() as scratch:
                if generator is Generator.FERN:
                    log = logs / f"{hashlib.sha256(str(document).encode()).hexdigest()[:12]}.fern.log"
                    measured[key] = fern_tree(fern, document, pair, Path(scratch), log, args.timeout)
                else:
                    measured[key] = crozier_tree(crozier, document, Path(scratch), args.timeout)
        return measured[key]

    dropped: set[str] = set()
    failed = False
    for fern_record, crozier_record in records:
        plan = plans[fern_record]
        try:
            outcomes = [
                Outcome(record, generator, measure(generator, plan.before), measure(generator, plan.after))
                for generator, record in ((Generator.FERN, fern_record), (Generator.CROZIER, crozier_record))
            ]
        except (GenerationError, OSError, subprocess.TimeoutExpired) as error:
            print(f"output-insensitive-remeasure: {fern_record}: {error}", file=sys.stderr)
            failed = True
            continue
        differing = [(outcome, outcome.differing()) for outcome in outcomes]
        if any(paths for _, paths in differing):
            dropped.add(fern_record)
            for outcome, paths in differing:
                for path in paths:
                    print(
                        f"output-insensitive-remeasure: {fern_record}: {outcome.generator} moves {path}",
                        file=sys.stderr,
                    )
            continue
        for outcome in outcomes:
            (root / outcome.record).write_text(
                record_text(outcome.generator, pair, outcome.before, outcome.after), encoding="utf-8"
            )
    if dropped:
        kept = [row for row in rows if row.fern_comparison not in dropped]
        for row in rows:
            if row.fern_comparison in dropped:
                print(f"output-insensitive-remeasure: removed {row.key} at {row.context}", file=sys.stderr)
        write_rows(root, kept)
    return 1 if failed or dropped else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
