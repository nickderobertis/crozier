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
    `<stem>-fern.json` whose stem starts with `<doc>`;
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
import io
import json
import os
import shlex
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

REGISTRY = Path("docs/openapi-surface/output-insensitive.tsv")
COLUMNS = ("key", "context", "search_record", "fern_comparison", "crozier_comparison")
CORPUS_SOURCES = Path("tests/fixtures/corpus-sources")
FERN_TIMEOUT_SECONDS = 1800


class UsageError(ValueError):
    """A record or argument the re-measure cannot act on."""


class GenerationError(RuntimeError):
    """A generator that did not write its tree."""


@dataclass(frozen=True)
class Pair:
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
    generator: str
    before: dict[str, str]
    after: dict[str, str]

    def differing(self) -> list[str]:
        return sorted(
            path for path in set(self.before) | set(self.after) if self.before.get(path) != self.after.get(path)
        )


def certified_pair(root: Path) -> Pair:
    data = json.loads((root / "assets/scaffolding/metadata.json").read_text(encoding="utf-8"))
    return Pair(data["cliVersion"], data["generatorVersion"])


def read_rows(root: Path) -> list[dict[str, str]]:
    with (root / REGISTRY).open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if reader.fieldnames != list(COLUMNS):
            raise UsageError(f"{REGISTRY}: expected columns {COLUMNS}")
        return list(reader)


def write_rows(root: Path, rows: list[dict[str, str]]) -> None:
    out = io.StringIO()
    writer = csv.DictWriter(out, COLUMNS, delimiter="\t", quoting=csv.QUOTE_NONE, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    (root / REGISTRY).write_text(out.getvalue(), encoding="utf-8")


def corpus_source(root: Path, name: str) -> Path | None:
    committed = root / CORPUS_SOURCES / name
    return next(
        (committed / f"openapi.{e}" for e in ("json", "yaml", "yml") if (committed / f"openapi.{e}").is_file()), None
    )


def documents(root: Path, record: str) -> Documents:
    """The two documents a fern record measured, by the rule it was filed under."""
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
        ablated = controls / f"{stem}.json"
        if (controls / f"{doc}.yml").is_file() and ablated.is_file():
            return Documents(controls / f"{doc}.yml", ablated)
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


def fern_tree(fern: list[str], document: Path, pair: Pair, scratch: Path, log: Path) -> dict[str, str]:
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
            timeout=FERN_TIMEOUT_SECONDS,
            check=False,
        )
    tree = preview / "fern-python-sdk"
    if result.returncode != 0 or not (tree / "src").is_dir():
        raise GenerationError(f"fern exited {result.returncode} on {document} without a packaged SDK; see {log}")
    return tree_digests(tree)


def crozier_tree(crozier: Path, document: Path, scratch: Path) -> dict[str, str]:
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
        check=False,
    )
    if result.returncode != 0:
        raise GenerationError(f"crozier exited {result.returncode} on {document}: {result.stderr.strip()}")
    return tree_digests(out)


def record_text(generator: str, pair: Pair, before: dict[str, str], after: dict[str, str]) -> str:
    record = {
        "schema_version": 1,
        "generator": generator,
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
    args = parser.parse_args(argv)
    root = args.root.resolve()
    crozier = args.crozier or root / "target/release/crozier"
    try:
        if not crozier.is_file():
            raise UsageError(f"{crozier} is not built; run `cargo build --release --locked`")
        pair = certified_pair(root)
        rows = read_rows(root)
        records = sorted({(row["fern_comparison"], row["crozier_comparison"]) for row in rows})
        if args.only:
            unknown = set(args.only) - {fern for fern, _ in records}
            if unknown:
                raise UsageError(f"--only names no record of {REGISTRY}: {sorted(unknown)}")
            records = [record for record in records if record[0] in args.only]
        plans = {fern: documents(root, fern) for fern, _ in records}
    except (UsageError, OSError, KeyError, json.JSONDecodeError) as error:
        print(f"output-insensitive-remeasure: {error}", file=sys.stderr)
        return 2
    fern = shlex.split(args.fern)
    logs = (
        Path(os.environ.get("ONEPIPELINE_NODE_SCRATCH_DIR") or tempfile.gettempdir()) / "output-insensitive-remeasure"
    )
    logs.mkdir(parents=True, exist_ok=True)
    measured: dict[tuple[str, Path], dict[str, str]] = {}

    def measure(generator: str, document: Path) -> dict[str, str]:
        key = (generator, document)
        if key not in measured:
            with tempfile.TemporaryDirectory() as scratch:
                if generator == "fern":
                    log = logs / f"{hashlib.sha256(str(document).encode()).hexdigest()[:12]}.fern.log"
                    measured[key] = fern_tree(fern, document, pair, Path(scratch), log)
                else:
                    measured[key] = crozier_tree(crozier, document, Path(scratch))
        return measured[key]

    dropped: set[str] = set()
    failed = False
    for fern_record, crozier_record in records:
        plan = plans[fern_record]
        try:
            outcomes = [
                Outcome(record, generator, measure(generator, plan.before), measure(generator, plan.after))
                for generator, record in (("fern", fern_record), ("crozier", crozier_record))
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
        kept = [row for row in rows if row["fern_comparison"] not in dropped]
        for row in rows:
            if row["fern_comparison"] in dropped:
                print(f"output-insensitive-remeasure: removed {row['key']} at {row['context']}", file=sys.stderr)
        write_rows(root, kept)
    return 1 if failed or dropped else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
