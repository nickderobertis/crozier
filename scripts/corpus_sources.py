#!/usr/bin/env python3
"""The committed source documents of every registered corpus row.

Every numbered `tests/fixtures/CORPUS.md` row's source document is committed
under `tests/fixtures/corpus-sources/<name>/`, laid out exactly as
`scripts/fetch-corpus.sh` publishes a fetch: `openapi.<suffix>` for a single
document, the pinned tree's own paths for a multi-document row, and
`remote/<host>/<path>` for each document an absolute-URL `$ref` names (the
pinned URLs of `tests/fixtures/corpus-remote-ref-pins.tsv`). The gate, the
census and every routine recipe read those copies; nothing routine fetches a
corpus document. The pinned URL in CORPUS.md is provenance, used only when a
Fern golden is deliberately rebuilt or a source re-audited.

`tests/fixtures/corpus-sources.tsv` records, per committed file, the row, the
path, the URL it was fetched from and the SHA-256 of the bytes fetched at that
pinned revision. For a row whose document carries absolute-URL `$ref`s the
recorded root bytes are the fetch as published — the remote-ref pins already
substituted, since that is the document Fern and crozier read.

Commands
--------
`check`
    The offline gate (`just lint-corpus-sources`). Opens no socket. Every
    canonical row is `committed` and recorded; every recorded file is present
    with its recorded digest; no unrecorded file sits under the root; a tree
    row's records are exactly its pinned members and a remote-ref row's include
    every pinned document, at the pin manifest's digests.
`vendor [--fixture NAME]... [--from DIR]`
    Fetch the selected rows (default: every canonical row) through
    `scripts/fetch-corpus.sh`, fetch each pinned remote document, then replace
    their committed copies and records. `--from` reuses a completed fetch in DIR
    instead. Rebuild-only: run it when a row is added or its pin moves.
`audit [--fixture NAME]... [--from DIR]`
    The same fetch, compared with the committed copies instead of written:
    exits 1 naming every file whose upstream bytes no longer match.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_remote_ref_pins as pins  # noqa: E402

ROOT_RELATIVE = PurePosixPath("tests/fixtures/corpus-sources")
MANIFEST_RELATIVE = PurePosixPath("tests/fixtures/corpus-sources.tsv")
CORPUS_RELATIVE = PurePosixPath("tests/fixtures/CORPUS.md")
COLUMNS = ("corpus_name", "path", "source_url", "sha256")
SPEC_SUFFIXES = (".json", ".yaml", ".yml")
REMOTE_DIR = "remote"
DIGEST_RE = re.compile(r"[0-9a-f]{64}")
HEADER = f"""\
# The committed source document of every registered corpus row, one record per
# file. `scripts/corpus_sources.py` is the validator (`check`, offline) and the
# only writer (`vendor`, which fetches); see its docstring.
#
# {chr(9).join(COLUMNS)}
#
#   corpus_name  a canonical CORPUS.md numbered row name (its third cell)
#   path         the committed copy, repository-relative
#   source_url   the pinned URL its bytes were fetched from
#   sha256       lowercase hex SHA-256 of those bytes; for a row with remote-ref
#                pins, of its root as published with the pins substituted
"""


class SourcesError(RuntimeError):
    """An actionable command-boundary error."""


@dataclass(frozen=True)
class Record:
    corpus_name: str
    path: str
    source_url: str
    sha256: str


@dataclass(frozen=True)
class Row:
    name: str
    url: str
    decision: str


def default_root() -> Path:
    return Path(__file__).resolve().parent.parent


def corpus_rows(root: Path) -> list[Row]:
    """The canonical numbered CORPUS.md rows, as `scripts/corpus-lib.sh` reads them.

    A withdrawn row keeps its number in a later table whose `decision` is
    `withdrawn`; only `committed` and `link-ok` rows are registered.
    """
    path = root / CORPUS_RELATIVE
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise SourcesError(f"could not read corpus manifest {path}: {error}") from error
    rows: list[Row] = []
    for line in lines:
        cells = [cell.strip() for cell in line.split("|")]
        if len(cells) < 9 or not cells[1].isdigit():
            continue
        name, url, decision = cells[2].strip("` "), cells[4], cells[7]
        if name and decision in {"committed", "link-ok"}:
            rows.append(Row(name, url, decision))
    if not rows:
        raise SourcesError(f"no numbered corpus rows found in {path}")
    return rows


def spec_filename(url: str) -> str:
    """`openapi.<suffix>`, the canonical name `scripts/corpus-lib.sh` publishes."""
    suffix = PurePosixPath(urlsplit(url).path).suffix
    if suffix not in SPEC_SUFFIXES:
        raise SourcesError(f"{url} has no supported OpenAPI suffix ({', '.join(SPEC_SUFFIXES)})")
    return f"openapi{suffix}"


def remote_path(url: str) -> str:
    """Where a pinned remote document lives under its row's directory."""
    parts = urlsplit(url)
    return f"{REMOTE_DIR}/{parts.netloc}{unquote(parts.path)}"


def expected_files(root: Path, row: Row) -> dict[str, tuple[str, str | None]]:
    """`row-relative path -> (source_url, pinned digest or None)` for one row."""
    tree = pins.tree_records_for(row.name, root)
    if tree:
        return {record.path: (record.pinned_url, record.sha256) for record in tree}
    files: dict[str, tuple[str, str | None]] = {spec_filename(row.url): (row.url, None)}
    for record in pins.records_for(row.name, root):
        files[remote_path(record.pinned_url)] = (record.pinned_url, record.sha256)
    return files


def load_manifest(root: Path) -> list[Record]:
    path = root / MANIFEST_RELATIVE
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise SourcesError(f"could not read {path}: {error}; run `just corpus-sources vendor`") from error
    records: list[Record] = []
    for number, line in enumerate(lines, 1):
        if not line.strip() or line.startswith("#"):
            continue
        cells = line.split("\t")
        site = f"{MANIFEST_RELATIVE}:{number}"
        if len(cells) != len(COLUMNS):
            raise SourcesError(f"{site}: expected {len(COLUMNS)} tab-separated cells ({', '.join(COLUMNS)})")
        record = Record(*cells)
        if not DIGEST_RE.fullmatch(record.sha256):
            raise SourcesError(f"{site}: sha256 {record.sha256!r} is not 64 lowercase hexadecimal characters")
        relative = PurePosixPath(record.path)
        prefix = ROOT_RELATIVE / record.corpus_name
        if ".." in relative.parts or not relative.is_relative_to(prefix) or relative == prefix:
            raise SourcesError(f"{site}: path {record.path!r} is not a file under {prefix}/")
        records.append(record)
    keys = [(record.corpus_name, record.path) for record in records]
    if keys != sorted(keys):
        raise SourcesError(f"{MANIFEST_RELATIVE}: records must sort by (corpus_name, path); rewrite it with `vendor`")
    if len(set(keys)) != len(keys):
        raise SourcesError(f"{MANIFEST_RELATIVE}: a path is recorded twice")
    return records


def write_manifest(root: Path, records: list[Record]) -> None:
    ordered = sorted(records, key=lambda record: (record.corpus_name, record.path))
    body = "".join(
        "\t".join((record.corpus_name, record.path, record.source_url, record.sha256)) + "\n"
        for record in ordered
    )
    (root / MANIFEST_RELATIVE).write_text(HEADER + "\n" + body, encoding="utf-8", newline="\n")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(root: Path) -> int:
    """Validate the committed sources offline; return how many files were verified."""
    rows = corpus_rows(root)
    records = load_manifest(root)
    problems: list[str] = []
    by_row: dict[str, dict[str, Record]] = {}
    for record in records:
        relative = PurePosixPath(record.path).relative_to(ROOT_RELATIVE / record.corpus_name)
        by_row.setdefault(record.corpus_name, {})[relative.as_posix()] = record
    names = {row.name for row in rows}
    for name in sorted(set(by_row) - names):
        problems.append(f"{name}: recorded in {MANIFEST_RELATIVE} but is no canonical CORPUS.md row; delete its records and {ROOT_RELATIVE / name}/")
    for row in rows:
        if row.decision != "committed":
            problems.append(
                f"{row.name}: CORPUS.md decision is `{row.decision}`, but every registered row's source is "
                f"committed; run `just corpus-sources vendor --fixture {row.name}` and mark the row `committed`"
            )
        recorded = by_row.get(row.name, {})
        expected = expected_files(root, row)
        for missing in sorted(set(expected) - set(recorded)):
            problems.append(f"{row.name}: {missing} is not committed; run `just corpus-sources vendor --fixture {row.name}`")
        for extra in sorted(set(recorded) - set(expected)):
            problems.append(f"{row.name}: {extra} is recorded but the row does not resolve it; run `just corpus-sources vendor --fixture {row.name}`")
        for relative, record in sorted(recorded.items()):
            if relative not in expected:
                continue
            url, pinned = expected[relative]
            if record.source_url != url:
                problems.append(f"{row.name}: {relative} records source {record.source_url}, but the row resolves {url}")
            if pinned is not None and record.sha256 != pinned:
                problems.append(
                    f"{row.name}: {relative} records sha256 {record.sha256}, but "
                    f"tests/fixtures/corpus-remote-ref-pins.tsv pins {pinned}"
                )
    verified = 0
    for record in records:
        path = root / record.path
        if not path.is_file():
            problems.append(f"{record.path} is recorded but missing; restore it from git or re-run `vendor`")
            continue
        measured = sha256(path)
        if measured != record.sha256:
            problems.append(
                f"{record.path} has sha256 {measured}, but the bytes fetched at its pinned revision "
                f"have {record.sha256}; restore it from git (a committed source is never edited)"
            )
            continue
        verified += 1
    recorded_paths = {record.path for record in records}
    base = root / ROOT_RELATIVE
    if base.is_dir():
        for path in sorted(base.rglob("*")):
            if path.is_symlink() or (path.is_file() and path.relative_to(root).as_posix() not in recorded_paths):
                problems.append(f"{path.relative_to(root).as_posix()} is not recorded in {MANIFEST_RELATIVE}; delete it or vendor its row")
    if problems:
        raise SourcesError("\n".join(problems))
    return verified


def fetch(root: Path, names: list[str], destination: Path) -> None:
    """Fetch each selected row through the real `scripts/fetch-corpus.sh`."""
    script = root / "scripts" / "fetch-corpus.sh"
    for name in names:
        result = subprocess.run(
            ["bash", str(script), "--fixture", name, str(destination)],
            cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True,
        )
        if result.returncode != 0:
            raise SourcesError(f"{name}: scripts/fetch-corpus.sh failed: {result.stderr.strip()}")


def fetched_bytes(root: Path, row: Row, fetched: Path) -> dict[str, tuple[str, bytes]]:
    """`row-relative path -> (source_url, bytes)` for one row's completed fetch."""
    files: dict[str, tuple[str, bytes]] = {}
    override = pins.origin_override()
    for relative, (url, pinned) in expected_files(root, row).items():
        if relative.startswith(f"{REMOTE_DIR}/"):
            try:
                body = pins.fetch_bytes(url, override)
            except pins.PinError as error:
                raise SourcesError(f"{row.name}: {error}") from error
        else:
            path = fetched / row.name / relative
            if not path.is_file():
                raise SourcesError(f"{row.name}: the fetch left no {relative} under {fetched / row.name}")
            body = path.read_bytes()
        if pinned is not None and hashlib.sha256(body).hexdigest() != pinned:
            raise SourcesError(f"{row.name}: {url} no longer serves its pinned sha256 {pinned}")
        files[relative] = (url, body)
    return files


def selected_rows(root: Path, fixtures: list[str]) -> list[Row]:
    rows = corpus_rows(root)
    if not fixtures:
        return rows
    known = {row.name: row for row in rows}
    unknown = [name for name in fixtures if name not in known]
    if unknown:
        raise SourcesError(f"{unknown[0]!r} is not a canonical CORPUS.md row")
    return [known[name] for name in fixtures]


def refetch(root: Path, fixtures: list[str], source: Path | None, *, write: bool) -> list[str]:
    rows = selected_rows(root, fixtures)
    with tempfile.TemporaryDirectory(prefix="crozier-corpus-sources-") as scratch:
        fetched = source or Path(scratch)
        if source is None:
            fetch(root, [row.name for row in rows], fetched)
        try:
            records = load_manifest(root)
        except SourcesError:
            if not write:
                raise
            records = []
        recorded = {record.path: record for record in records}
        drifted: list[str] = []
        replaced = {row.name for row in rows}
        kept = [record for record in records if record.corpus_name not in replaced]
        staged: list[tuple[Path, bytes]] = []
        for row in rows:
            for relative, (url, body) in sorted(fetched_bytes(root, row, fetched).items()):
                path = (ROOT_RELATIVE / row.name / relative).as_posix()
                digest = hashlib.sha256(body).hexdigest()
                kept.append(Record(row.name, path, url, digest))
                staged.append((root / path, body))
                previous = recorded.get(path)
                if previous is None or previous.sha256 != digest:
                    drifted.append(f"{path}: committed {previous.sha256 if previous else 'nothing'}, upstream {digest}")
        if write:
            for name in replaced:
                directory = root / ROOT_RELATIVE / name
                if directory.exists():
                    shutil.rmtree(directory)
            for path, body in staged:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(body)
            write_manifest(root, kept)
        return drifted


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=None, help="repository root (defaults to this script's own)")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="validate the committed sources offline")
    for name, help_text in (
        ("vendor", "fetch rows and replace their committed copies"),
        ("audit", "fetch rows and compare them with their committed copies"),
    ):
        command = commands.add_parser(name, help=help_text)
        command.add_argument("--fixture", action="append", default=[], metavar="NAME")
        command.add_argument("--from", dest="source", type=Path, default=None, metavar="DIR",
                             help="reuse a completed scripts/fetch-corpus.sh fetch in DIR")
    args = parser.parse_args(argv)
    root = (args.root or default_root()).resolve()
    try:
        if args.command == "check":
            check(root)
        elif args.command == "vendor":
            refetch(root, args.fixture, args.source, write=True)
            check(root)
        else:
            drifted = refetch(root, args.fixture, args.source, write=False)
            if drifted:
                print("corpus-sources: upstream no longer serves the committed bytes:", file=sys.stderr)
                print("\n".join(f"  {line}" for line in drifted), file=sys.stderr)
                return 1
    except (SourcesError, pins.PinError) as error:
        print(f"corpus-sources: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
