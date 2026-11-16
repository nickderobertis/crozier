#!/usr/bin/env python3
"""Keep Fern's untouched output reusable: the host's shared certified-tree store.

A certified generation is expensive and deterministic in its inputs, so the tree
Fern wrote — before any comment stripping, overlay reduction or install — is kept
under one key every reader can compute:

    ${XDG_CACHE_HOME:-$HOME/.cache}/crozier/certified-trees/
        fern-<cli>_python-<generator>/<document sha256>/<python_enums|literals>/
            tree/            Fern's output exactly as it wrote it
            document.sha256  the digest of the document Fern read
            exit-code        `fern generate`'s exit status (always 0 here)
            fern.log         its scrubbed output (empty when the caller kept none)
            screen.json      a witness screen's record, when a screen published it

That is the layout the entries already on this host use, so an entry written
before this module stays readable. This module is its one writer and reader:
`fern-references.py`, the witness screen (`tools/witness-search/witness_screen.py`)
and the overlay generation (`fern-overlay-goldens.sh`, through
`generate-fern-fixture.sh`) publish through `publish`, and `find` answers where an
entry is.

Only a tree that describes itself as that key is published: its
`.fern/metadata.json` must record the pair and the enum mode, and no other
generator setting (a client class name, extra fields, retries), because the key
names nothing else. A caller generating with a setting the metadata does not
record — audiences, a non-default organization, the flat layout, a document whose
remote refs were served from a scratch port — does not publish at all.

Publication is atomic (the entry is assembled beside its final name and renamed
into place) and first-wins: an existing entry is kept. It takes no lock of its
own: it runs inside a generation, which already holds the host's
`fern-generation.lock`, and a second hold of that lock from the same caller would
deadlock.

Usage: certified_tree.py publish DOCUMENT TREE --enum-type python-enums|literals [--log FILE]
       certified_tree.py find DOCUMENT --enum-type python-enums|literals [--cli V --generator V]

Exit status: `publish` 0 when the entry is in place (printing its path), 1 when the
tree is refused (the reason on stderr); `find` 0 printing the entry's path, 1 when
there is none; 2 on a usage error.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

# `scripts/lib.sh`'s `valid_fern_version` (fern_references_test holds this copy to
# it); it also keeps a recorded version from naming any path but one directory.
VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?")
# The one generator the store's `python-<generator>` key names.
GENERATOR = "fernapi/fern-python-sdk"
REMEDY = "regenerate with the certified pair and no setting the key does not name, then re-run"
METADATA = Path("assets/scaffolding/metadata.json")
RECORD_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")


class EnumMode(StrEnum):
    """The enum mode as this repository's commands spell it; `directory` is the store's (Fern's) spelling."""

    PYTHON_ENUMS = "python-enums"
    LITERALS = "literals"

    @property
    def directory(self) -> str:
        return self.value.replace("-", "_")


# The one generatorConfig each mode's untouched tree records, and nothing else.
RECORDED_CONFIG = {
    EnumMode.PYTHON_ENUMS: {"pydantic_config": {"enum_type": "python_enums"}},
    EnumMode.LITERALS: {},
}


class RefusedTree(ValueError):
    """A tree that does not describe itself as the key it would be published under."""


@dataclass(frozen=True)
class Key:
    cli: str
    generator: str
    document_sha256: str
    mode: EnumMode

    def entry(self, root: Path) -> Path:
        return root / f"fern-{self.cli}_python-{self.generator}" / self.document_sha256 / self.mode.directory


def store_root() -> Path:
    """`${XDG_CACHE_HOME:-$HOME/.cache}/crozier/certified-trees`; a relative XDG_CACHE_HOME is ignored, as XDG asks."""
    base = os.environ.get("XDG_CACHE_HOME") or ""
    cache = Path(base) if os.path.isabs(base) else Path.home() / ".cache"
    return cache / "crozier" / "certified-trees"


def document_digest(document: Path) -> str:
    return hashlib.sha256(document.read_bytes()).hexdigest()


def tree_key(document: Path, tree: Path, mode: EnumMode) -> Key:
    """The key `tree` describes itself as, refused unless it is a complete Fern tree of `mode`."""
    path = tree / ".fern" / "metadata.json"
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise RefusedTree(f"{path} is no Fern metadata record ({error})") from None
    if not isinstance(record, dict):
        raise RefusedTree(f"{path} is no JSON object")
    if record.get("generatorName") != GENERATOR:
        raise RefusedTree(f"{path} records generator {record.get('generatorName')!r}, not {GENERATOR}")
    cli, generator = record.get("cliVersion"), record.get("generatorVersion")
    if not (
        isinstance(cli, str) and VERSION.fullmatch(cli) and isinstance(generator, str) and VERSION.fullmatch(generator)
    ):
        raise RefusedTree(f"{path} records no exact cliVersion and generatorVersion ({cli!r}, {generator!r})")
    config = record.get("generatorConfig", {})
    if config != RECORDED_CONFIG[mode]:
        raise RefusedTree(
            f"{path} records generatorConfig {json.dumps(config, sort_keys=True)}, not {mode}'s "
            f"{json.dumps(RECORDED_CONFIG[mode])}: the store keys a tree by its pair and enum mode alone"
        )
    return Key(cli, generator, document_digest(document), mode)


def publish(
    document: Path,
    tree: Path,
    mode: EnumMode,
    log: str = "",
    records: Mapping[str, str] | None = None,
    root: Path | None = None,
) -> Path:
    """Copy `tree`, Fern's untouched output for `document`, into the store; the entry's path.

    `records` are further files the caller keeps beside the tree, by name (the
    witness screen keeps its `screen.json`). First wins: an entry already there is
    kept as it is.
    """
    records = dict(records or {})
    reserved = {"tree", "document.sha256", "exit-code", "fern.log"}
    if any(not RECORD_NAME.fullmatch(name) or name in reserved for name in records):
        raise ValueError(f"record names {sorted(records)} must be plain file names other than {sorted(reserved)}")
    entry = tree_key(document, tree, mode).entry(root or store_root())
    if entry.is_dir():
        incomplete = entry_failure(entry)
        if incomplete:
            raise RefusedTree(
                f"the entry already at {entry} is incomplete ({incomplete}); remove that directory so this "
                "generation can publish it, then re-run"
            )
        return entry
    entry.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=f".{entry.name}.", dir=entry.parent))
    try:
        shutil.copytree(tree, stage / "tree", symlinks=True)
        (stage / "document.sha256").write_text(f"{entry.parent.name}\n", encoding="utf-8", newline="\n")
        (stage / "exit-code").write_text("0\n", encoding="utf-8", newline="\n")
        (stage / "fern.log").write_text(log, encoding="utf-8", newline="\n")
        for name, text in records.items():
            (stage / name).write_text(text, encoding="utf-8", newline="\n")
        try:
            stage.rename(entry)
        except OSError:
            # Another publisher renamed its entry in first; theirs is the same tree.
            if not entry.is_dir():
                raise
    finally:
        shutil.rmtree(stage, ignore_errors=True)
    return entry


def entry_failure(entry: Path) -> str | None:
    """Why `entry` is not a whole entry of its key's layout, or None when it is.

    A whole entry holds `tree/`, the `document.sha256` its directory names and an
    integer `exit-code` (a refused generation is recorded too, with its status).
    """
    if not (entry / "tree").is_dir():
        return "it holds no tree/"
    try:
        digest = (entry / "document.sha256").read_text(encoding="utf-8").strip()
        status = (entry / "exit-code").read_text(encoding="utf-8").strip()
    except OSError as error:
        return f"its records cannot be read: {error}"
    if digest != entry.parent.name:
        return f"its document.sha256 reads {digest!r}, not the {entry.parent.name} it is filed under"
    if not re.fullmatch(r"[0-9]+", status):
        return f"its exit-code reads {status!r}, no exit status"
    return None


def find(document: Path, cli: str, generator: str, mode: EnumMode, root: Path | None = None) -> Path | None:
    """The whole published entry for `document` at the pair and mode, or None."""
    entry = Key(cli, generator, document_digest(document), mode).entry(root or store_root())
    return entry if entry.is_dir() and entry_failure(entry) is None else None


def certified_pair(repo: Path) -> tuple[str, str]:
    """The pair `assets/scaffolding/metadata.json` certifies."""
    path = repo / METADATA
    record = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(record, dict):
        raise ValueError(f"{path} is no JSON object")
    cli, generator = record.get("cliVersion"), record.get("generatorVersion")
    if not (
        isinstance(cli, str) and VERSION.fullmatch(cli) and isinstance(generator, str) and VERSION.fullmatch(generator)
    ):
        raise ValueError(f"{path} records no exact cliVersion and generatorVersion")
    return cli, generator


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="certified_tree.py", description=__doc__.split("\n", 1)[0])
    commands = parser.add_subparsers(dest="command", required=True)
    publishing = commands.add_parser("publish", help="keep Fern's untouched tree for DOCUMENT in the store")
    publishing.add_argument("document", type=Path)
    publishing.add_argument("tree", type=Path)
    publishing.add_argument("--enum-type", required=True, choices=tuple(EnumMode))
    publishing.add_argument("--log", type=Path, help="Fern's scrubbed output, kept as the entry's fern.log")
    finding = commands.add_parser("find", help="print the store entry for DOCUMENT, if one is published")
    finding.add_argument("document", type=Path)
    finding.add_argument("--enum-type", required=True, choices=tuple(EnumMode))
    finding.add_argument("--cli", help="the Fern CLI version (default: the certified pair's)")
    finding.add_argument("--generator", help="the fern-python-sdk version (default: the certified pair's)")
    args = parser.parse_args(argv)
    mode = EnumMode(args.enum_type)
    try:
        if args.command == "publish":
            log = args.log.read_text(encoding="utf-8") if args.log else ""
            print(publish(args.document, args.tree, mode, log))
            return 0
        if (args.cli is None) != (args.generator is None):
            parser.error("--cli and --generator name one pair: pass both, or neither for the certified pair")
        repo = Path(__file__).resolve().parents[2]
        cli, generator = (args.cli, args.generator) if args.cli else certified_pair(repo)
        if not (VERSION.fullmatch(cli) and VERSION.fullmatch(generator)):
            parser.error("--cli and --generator are exact versions")
        entry = find(args.document, cli, generator, mode)
    except RefusedTree as error:
        print(f"certified-tree: not published: {error}; {REMEDY}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as error:
        print(f"certified-tree: {error}; check the path named, then re-run", file=sys.stderr)
        return 1
    if entry is None:
        print(
            f"certified-tree: no entry for {args.document} at Fern CLI {cli} / python-sdk {generator} ({mode})",
            file=sys.stderr,
        )
        return 1
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
