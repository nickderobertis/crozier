#!/usr/bin/env python3
"""Regenerate one family of committed Fern references, one Fern generation at a time.

Every reference crozier is byte-gated against is Fern's own output at the
certified pair `assets/scaffolding/metadata.json` declares (`cliVersion`,
`generatorVersion`). Each family lives where its gate reads it and is written
here through the script that owns one item of it:

  corpus            tests/fixtures/<fixture>/expected/ and expected-flat/ — a
                    CORPUS.md row through `fern-goldens generate`, a vendored
                    fixture through `generate-fern-fixture.sh`
  overlays          tests/fixtures/<fixture>/expected-literals/ and
                    expected-default-max-retries/ through `fern-overlay-goldens.sh`
  handwritten       docs/openapi-surface/handwritten/<fixture>/fern-expected/,
                    with its evidence.toml versions and digest
  measurements      docs/fern-measurements/<group>/<case>/fern-expected/, or
                    the case's Contract A fern-refusal.txt where Fern refuses
                    it, each case's document and setting declared in
                    docs/fern-measurements/cases.tsv; a `<stem>.fern.log`
                    beside its `<stem>.openapi.*` document; and a case's
                    pinned run its measurement.json records
  probes            docs/openapi-surface/probe-expected/<name>/ or its Contract A
                    refusal record, with MANIFEST.tsv's digest
  authored-probes   docs/openapi-surface/authored-probes/<case>/ fern.log and
                    fern-expected/
  departure-evidence  docs/departures/evidence/<id>/fern-reference/, a departure
                    note's own Fern tree, under its fern-reference.json settings
  refusals          docs/fern-refusals/<class>/fern-refusal.txt and
                    findings.tsv through `fern-refusals.py probe|finding --jobs 1`,
                    and each `<class>/evidence/<stem>.pinned-fern.log` beside its
                    probe document; a class whose probe no longer reproduces its
                    record keeps it, and is reported (not failed) through
                    .local/fern-references/refusals/probe.<class>.changes.jsonl

Usage:
  fern-references.py list FAMILY
  fern-references.py check [FAMILY...]
  fern-references.py generate FAMILY [--version V] [--cli-version C] [ITEM...]

`list` prints the family's item names, one per line. `check` validates every
item of every family (or of the named ones) without starting Fern, Docker or
any network request: each input its generation reads exists, and each evidence
file it restates states a restatable pair. It prints one line per broken item,
`<family> <item>: <reason>`, to stderr, and exits 1 when any is broken. `generate` runs
the same per-family validation before it starts Fern, refusing a broken item
with that reason line. `generate` regenerates the
named items, or the whole family when none is named, at the certified pair
unless `--version`/`--cli-version` name another, writing each item where its
committed reference lives. Fern runs once at a time, in a scratch workspace
outside any checkout (so it stamps no `originGitCommit`). Quiet on success
apart from one summary line; a failed item names its log and the rest still run.

Exit status: 0 when every item listed, checked or regenerated; 1 when an item
failed or is broken (each named) or an input it reads is malformed; 2 on a
usage error.
"""

from __future__ import annotations

import argparse
import contextlib
import functools
import hashlib
import http.server
import importlib.util
import json
import keyword
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import tomllib
from collections.abc import Callable, Generator
from dataclasses import asdict, astuple, dataclass, fields
from enum import StrEnum
from pathlib import Path
from typing import NamedTuple, TypeVar, cast

ROOT = Path(os.environ.get("CROZIER_FERN_REFERENCES_ROOT") or Path(__file__).resolve().parents[2]).resolve()
METADATA = Path("assets/scaffolding/metadata.json")
FIXTURES = Path("tests/fixtures")
HANDWRITTEN = Path("docs/openapi-surface/handwritten")
MEASUREMENTS = Path("docs/fern-measurements")
CASES = MEASUREMENTS / "cases.tsv"
CASES_HEADER = ("case", "document", "enum_type", "layout", "overlay")
PROBES = Path("docs/openapi-surface/probes")
PROBE_EXPECTED = Path("docs/openapi-surface/probe-expected")
MANIFEST = PROBE_EXPECTED / "MANIFEST.tsv"
AUTHORED = Path("docs/openapi-surface/authored-probes")
REGISTRY = Path("docs/fern-refusals")
OVERLAY_MANIFEST = ".crozier-overlay.json"
REFUSAL_SUFFIX = ".fern-refusal.txt"
# `fern-refusals.py probe`'s exit when a probe no longer reproduces its recorded refusal.
PROBE_CHANGED_EXIT = 3
PINNED_LOG = ".pinned-fern.log"
DOCUMENT_SUFFIXES = (".yml", ".yaml", ".json")
REMOTE_URL = "@REMOTE_URL@"
LOGS = Path(".local/fern-references")
DEPARTURE_EVIDENCE = Path("docs/departures/evidence")


@dataclass(frozen=True)
class OverlayKind:
    """The setting one overlay golden differs from the python-enums golden by,
    as `fern-overlay-goldens.sh` takes it: a fixed value, or the count the
    golden's own `.crozier-overlay.json` records under `recorded`."""

    flag: str
    value: str | None = None
    recorded: str | None = None


OVERLAY_KINDS = {
    "expected-literals": OverlayKind("--enum-type", value="literals"),
    "expected-default-max-retries": OverlayKind("--default-max-retries", recorded="default_max_retries"),
}


T = TypeVar("T")
# While `check` runs, each whole-tree table below is read once: `check` reads a
# fixed tree, where `generate` may change one between items.
_CHECKING: dict[object, object] | None = None


def read_once(function: Callable[[], T]) -> Callable[[], T]:
    @functools.wraps(function)
    def wrapper() -> T:
        if _CHECKING is None:
            return function()
        if function not in _CHECKING:
            _CHECKING[function] = function()
        # Each entry is keyed by the function that computed it, so it holds
        # exactly that function's return type, T.
        return cast("T", _CHECKING[function])

    return wrapper


class ReferenceError(RuntimeError):
    """An item that could not be regenerated, with the reason and its fix."""


@dataclass(frozen=True)
class Pair:
    cli: str
    generator: str


@dataclass(frozen=True)
class FernRun:
    check_exit: str
    check_log: str
    generate_exit: str
    generate_log: str
    tree: Path | None


# `scripts/lib.sh`'s `valid_fern_version`, which the delegated scripts apply;
# fern_references_test.py holds the two to the same verdicts.
VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?")


def certified_pair(root: Path = ROOT) -> Pair:
    """The pair `assets/scaffolding/metadata.json` certifies: an object whose
    `cliVersion` and `generatorVersion` are exact versions."""
    path = root / METADATA
    fix = "restore it with git checkout -- assets/scaffolding/metadata.json"
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise SystemExit(f"fern-references: cannot read the certified pair from {path} ({error}); {fix}") from None
    cli = record.get("cliVersion") if isinstance(record, dict) else None
    generator = record.get("generatorVersion") if isinstance(record, dict) else None
    if not (
        isinstance(cli, str) and VERSION.fullmatch(cli) and isinstance(generator, str) and VERSION.fullmatch(generator)
    ):
        raise SystemExit(
            f"fern-references: {path} must be an object whose cliVersion and generatorVersion are exact "
            f"versions, not {cli!r} and {generator!r}; {fix}"
        )
    return Pair(cli=cli, generator=generator)


def contract_digest(tree: Path) -> str:
    """Contract A's tree digest: every file sorted by relative path, each
    contributing its path, a NUL, its byte length, a NUL and its bytes."""
    digest = hashlib.sha256()
    for path in sorted((p for p in tree.rglob("*") if p.is_file()), key=lambda p: p.relative_to(tree).as_posix()):
        data = path.read_bytes()
        digest.update(path.relative_to(tree).as_posix().encode("utf-8") + b"\0")
        digest.update(str(len(data)).encode("ascii") + b"\0" + data)
    return digest.hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)


@contextlib.contextmanager
def serve(directory: Path) -> Generator[str]:
    """Serve `directory` on a loopback port for the life of the block."""

    class Quiet(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, directory=str(directory), **kwargs)

        def log_message(self, format: str, *args: object) -> None:
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Quiet)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_address[1]}"
    finally:
        server.shutdown()
        server.server_close()


def scrub(log: str, workspace: Path) -> str:
    """Fern's output with this run's scratch paths made generic."""
    log = log.replace(str(workspace), "<workspace>")
    log = re.sub(r"Generator logs here: \S+", "Generator logs here: <tmp>", log)
    return re.sub(r"/tmp/[\w.-]+", "<tmp>", log)


class FernCommand(NamedTuple):
    """One Fern command's exit status, as text, and its combined output."""

    exit: str
    log: str


# Spellings YAML reads as a boolean or null rather than a string, refused as a
# class or audience name because generators.yml writes both as plain scalars —
# exactly the set `generate-fern-fixture.sh`'s `yaml_keyword` refuses, so the two
# workspaces stay byte-identical (a test reconciles the lists).
YAML_KEYWORDS = frozenset(("true", "false", "yes", "no", "on", "off", "y", "n", "null"))


def plain_yaml_name(name: object, pattern: str) -> bool:
    """Whether `name` is a string matching `pattern` that YAML reads back as that string."""
    return isinstance(name, str) and re.fullmatch(pattern, name) is not None and name.lower() not in YAML_KEYWORDS


def fern(argv: list[str], workspace: Path, env: dict[str, str]) -> FernCommand:
    if shutil.which(argv[0]) is None:
        raise ReferenceError(f"`{argv[0]}` is not on PATH; run `just setup-fern` (it installs the Fern CLI)")
    run = subprocess.run(argv, cwd=workspace, env=env, capture_output=True, text=True, errors="replace", check=False)
    return FernCommand(str(run.returncode), run.stdout + run.stderr)


@contextlib.contextmanager
def run_fern(
    document: Path,
    pair: Pair,
    *,
    enum_type: str = "python-enums",
    layout: str = "packaged",
    audiences: tuple[str, ...] = (),
    check: bool = False,
    client_class_name: str | None = None,
    extra_fields: str | None = None,
    organization: str = "fern",
) -> Generator[FernRun]:
    """`fern generate` (after `fern check` when asked) over one document in the
    workspace `generate-fern-fixture.sh` scaffolds, yielding the raw output tree."""
    with tempfile.TemporaryDirectory(prefix="fern-references-") as scratch:
        base = Path(scratch)
        workspace = base / "fern"
        (workspace / "openapi").mkdir(parents=True)
        text = document.read_text(encoding="utf-8")
        with serve(document.parent) if REMOTE_URL in text else contextlib.nullcontext("") as url:
            (workspace / "openapi" / "openapi.yml").write_text(
                text.replace(REMOTE_URL, url) if url else text, encoding="utf-8"
            )
            (workspace / "fern.config.json").write_text(
                json.dumps({"organization": organization, "version": pair.cli}) + "\n", encoding="utf-8"
            )
            audiences_block = "".join(f"      - {name}\n" for name in audiences)
            pydantic_lines = ("            enum_type: python_enums\n" if enum_type == "python-enums" else "") + (
                f"            extra_fields: {extra_fields}\n" if extra_fields else ""
            )
            pydantic = f"          pydantic_config:\n{pydantic_lines}" if pydantic_lines else ""
            client_class = f"          client_class_name: {client_class_name}\n" if client_class_name else ""
            (workspace / "generators.yml").write_text(
                "api:\n  path: openapi/openapi.yml\ngroups:\n  python-sdk:\n"
                + (f"    audiences:\n{audiences_block}" if audiences else "")
                + "    generators:\n      - name: fernapi/fern-python-sdk\n"
                + f"        version: {pair.generator}\n        config:\n"
                + client_class
                + pydantic
                + "        output:\n          location: local-file-system\n          path: ../generated/python\n",
                encoding="utf-8",
            )
            env = dict(os.environ, CI="true", GITHUB_ACTIONS="true")
            if layout == "packaged":
                env["FERN_TOKEN"] = "preview-only-no-publish"
            else:
                env.pop("FERN_TOKEN", None)
            check_exit, check_log = fern(["fern", "check"], workspace, env) if check else ("", "")
            if layout == "packaged":
                output = base / "preview"
                command = ["fern", "generate", "--group", "python-sdk", "--local", "--preview"]
                command += ["--output", str(output), "--force"]
                tree = output / "fern-python-sdk"
            else:
                command = ["fern", "generate", "--group", "python-sdk", "--local", "--force"]
                tree = base / "generated" / "python"
            generate_exit, generate_log = fern(command, workspace, env)
        produced = tree if tree.is_dir() and any(p.is_file() for p in tree.rglob("*")) else None
        yield FernRun(
            check_exit,
            scrub(check_log, base),
            generate_exit,
            scrub(generate_log, base),
            produced,
        )


def strip_into(source: Path, destination: Path) -> None:
    """Copy Fern's tree, every `.py` through crozier's comment stripper."""
    crozier = ROOT / "target" / "release" / ("crozier.exe" if os.name == "nt" else "crozier")
    if not crozier.is_file():
        raise ReferenceError("build crozier first: cargo build --release (its stripper normalizes the tree)")
    for path in sorted(p for p in source.rglob("*") if p.is_file()):
        target = destination / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == ".py":
            stripped = subprocess.run([str(crozier), "internal-strip", str(path)], capture_output=True, check=False)
            if stripped.returncode != 0:
                raise ReferenceError(f"crozier internal-strip failed on {path.name}: {stripped.stderr.decode()}")
            target.write_bytes(stripped.stdout)
        else:
            shutil.copyfile(path, target)


def install(staged: Path, destination: Path) -> None:
    """Replace `destination` with `staged` (same filesystem), keeping the prior
    tree until the new one is in place."""
    backup = destination.parent / f".{destination.name}.backup.{os.getpid()}"
    if backup.exists():
        raise ReferenceError(f"a stale backup blocks the install: {rel(backup)}; restore or remove it")
    had = destination.exists()
    if had:
        destination.rename(backup)
    try:
        staged.rename(destination)
    except OSError:
        if had:
            backup.rename(destination)
        raise
    if had:
        shutil.rmtree(backup)


EXTRA_FIELDS = ("allow", "ignore", "forbid")


@dataclass(frozen=True)
class GeneratorSettings:
    """The generator settings a committed tree was made under that this family
    regenerates it with: Fern's `client_class_name` and
    `pydantic_config.extra_fields`, each `None` where the tree used the default."""

    client_class_name: str | None = None
    extra_fields: str | None = None


def recorded_generator_config(tree: Path) -> GeneratorSettings:
    """The settings a committed Fern tree's `.fern/metadata.json` records; the
    defaults for a tree that carries none."""
    path = tree / ".fern" / "metadata.json"
    if not path.is_file():
        return GeneratorSettings()
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ReferenceError(f"cannot read {rel(path)} ({error}); restore it from git") from None
    config = record.get("generatorConfig", {}) if isinstance(record, dict) else None
    pydantic = config.get("pydantic_config", {}) if isinstance(config, dict) else None
    if not isinstance(config, dict) or not isinstance(pydantic, dict):
        raise ReferenceError(
            f"{rel(path)}: generatorConfig and its pydantic_config must be objects; restore it from git"
        )
    client_class_name = config.get("client_class_name")
    extra_fields = pydantic.get("extra_fields")
    if client_class_name is not None and not (
        plain_yaml_name(client_class_name, r"[A-Za-z_][A-Za-z0-9_]*") and not keyword.iskeyword(client_class_name)
    ):
        raise ReferenceError(
            f"{rel(path)}: client_class_name {client_class_name!r} is no Python class name YAML reads as a string"
        )
    if extra_fields is not None and extra_fields not in EXTRA_FIELDS:
        raise ReferenceError(f"{rel(path)}: extra_fields {extra_fields!r} is none of {', '.join(EXTRA_FIELDS)}")
    return GeneratorSettings(client_class_name=client_class_name, extra_fields=extra_fields)


def generated_tree(
    document: Path,
    destination: Path,
    pair: Pair,
    *,
    enum_type: str,
    layout: str,
    audiences: tuple[str, ...] = (),
    client_class_name: str | None = None,
    extra_fields: str | None = None,
) -> None:
    """Generate `document` and install Fern's stripped tree at `destination`."""
    with run_fern(
        document,
        pair,
        enum_type=enum_type,
        layout=layout,
        audiences=audiences,
        client_class_name=client_class_name,
        extra_fields=extra_fields,
    ) as run:
        if run.generate_exit != "0" or run.tree is None:
            raise ReferenceError(
                f"fern generate exited {run.generate_exit} with no tree:\n{run.generate_log.strip()[-2000:]}"
            )
        destination.parent.mkdir(parents=True, exist_ok=True)
        stage = Path(tempfile.mkdtemp(prefix=".fern-references.", dir=destination.parent))
        try:
            strip_into(run.tree, stage / destination.name)
            install(stage / destination.name, destination)
        finally:
            shutil.rmtree(stage, ignore_errors=True)


def reduce_overlay(tree: Path, base: Path | None, provenance: dict[str, object]) -> None:
    """Reduce `tree` in place to the files that differ from `base` (all of them
    when there is no base), naming what Fern omits in its manifest."""
    spec = importlib.util.spec_from_file_location("golden_overlay", Path(__file__).with_name("golden_overlay.py"))
    if spec is None or spec.loader is None:
        raise ReferenceError("cannot load tools/fern-goldens/golden_overlay.py; restore it with git checkout")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory() as empty:
        module.reduce(base if base is not None else Path(empty), tree, provenance)


EVIDENCE_KEYS = ("fern_cli_version", "fern_python_sdk_version", "digest")


def check_evidence(path: Path) -> None:
    """Fail before Fern runs unless `evidence.toml` carries each provenance line
    this family restates, once, so a fixture's tree is never replaced under
    evidence it cannot restate."""
    text = path.read_text(encoding="utf-8")
    for key in EVIDENCE_KEYS:
        if len(re.findall(rf'(?m)^{key} = "[^"]*"$', text)) != 1:
            raise ReferenceError(f"{rel(path)} has no single `{key}` line to restate; restore it from git")


def rewrite_evidence(path: Path, pair: Pair, digest: str) -> None:
    """Restate an `evidence.toml`'s versions and digest, leaving every other line."""
    check_evidence(path)
    text = path.read_text(encoding="utf-8")
    for key, value in zip(EVIDENCE_KEYS, (pair.cli, pair.generator, digest), strict=True):
        text = re.sub(rf'(?m)^{key} = "[^"]*"$', f'{key} = "{value}"', text, count=1)
    path.write_text(text, encoding="utf-8", newline="\n")


NOTE_CLI = re.compile(r"Fern CLI [0-9]+\.[0-9]+\.[0-9]+")
NOTE_SDK = re.compile(r"(fernapi/fern-python-sdk`?:? )[0-9]+\.[0-9]+\.[0-9]+")
NOTE_DIGEST = re.compile(r"(Canonical tree SHA-256: `)[0-9a-f]{64}(`)")


def check_evidence_note(path: Path) -> None:
    """Fail before Fern runs unless a case's `evidence.md` states the pair (the
    Fern CLI and the fern-python-sdk version), and a well-formed digest where it
    names one, so a regeneration never leaves its note stating the old ones."""
    text = path.read_text(encoding="utf-8")
    if not NOTE_CLI.search(text) or not NOTE_SDK.search(text):
        raise ReferenceError(f"{rel(path)} states no Fern CLI and fern-python-sdk version to restate")
    if "Canonical tree SHA-256" in text and not NOTE_DIGEST.search(text):
        raise ReferenceError(f"{rel(path)} names a canonical tree SHA-256 that is no 64-digit digest")


def restate_evidence_note(path: Path, pair: Pair, digest: str) -> None:
    """Restate a measurement case's `evidence.md` provenance: the pair that
    generated its tree and the tree's `Canonical tree SHA-256`."""
    check_evidence_note(path)
    text = path.read_text(encoding="utf-8")
    text = NOTE_CLI.sub(f"Fern CLI {pair.cli}", text)
    text = NOTE_SDK.sub(rf"\g<1>{pair.generator}", text)
    text = NOTE_DIGEST.sub(rf"\g<1>{digest}\g<2>", text)
    path.write_text(text, encoding="utf-8", newline="\n")


def read_tsv(path: Path, header: tuple[str, ...]) -> list[dict[str, str]]:
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    if not lines or tuple(lines[0].split("\t")) != header:
        raise SystemExit(f"fern-references: {path} must open with the header {' '.join(header)}")
    return [dict(zip(header, line.split("\t"), strict=True)) for line in lines[1:] if line]


@read_once
def corpus_rows() -> dict[str, str]:
    """CORPUS.md's numbered rows, fixture directory to row name."""
    rows: dict[str, str] = {}
    aliases: dict[str, str] = {}
    alias_file = ROOT / FIXTURES / "corpus-aliases.tsv"
    if alias_file.is_file():
        for line in alias_file.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                name, fixture = line.split("\t")
                aliases[name] = fixture
    for line in (ROOT / FIXTURES / "CORPUS.md").read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\| *\d+ *\| *`([^`]+)` *\|", line)
        if match:
            rows[aliases.get(match.group(1), match.group(1))] = match.group(1)
    return rows


@read_once
def flat_goldens() -> dict[str, str]:
    """`flat-goldens.txt`'s rows: fixture to the fixture whose spec it uses."""
    declared: dict[str, str] = {}
    for line in (ROOT / FIXTURES / "flat-goldens.txt").read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            fixture, _, spec = line.partition("|")
            declared[fixture] = spec or fixture
    return declared


CORPUS_SOURCES = FIXTURES / "corpus-sources.tsv"


@read_once
def corpus_sources() -> dict[str, list[str]]:
    """`corpus-sources.tsv`: each registered row name to the committed files of
    its source document."""
    path = ROOT / CORPUS_SOURCES
    found: dict[str, list[str]] = {}
    lines = path.read_text(encoding="utf-8").splitlines() if path.is_file() else []
    for number, line in enumerate(lines, start=1):
        if line and not line.startswith("#") and not line.startswith("corpus_name\t"):
            cells = line.split("\t")
            if len(cells) < 2 or not cells[0] or not cells[1]:
                raise ReferenceError(
                    f"{CORPUS_SOURCES}:{number} is no `corpus_name<TAB>path…` record; restore it from git"
                )
            found.setdefault(cells[0], []).append(cells[1])
    return found


@read_once
def committed_rows() -> set[str]:
    """The `CORPUS.md` row names whose `decision` is `committed`: every file of
    their source is stored under `corpus-sources/`."""
    names, column = set(), None
    for line in (ROOT / FIXTURES / "CORPUS.md").read_text(encoding="utf-8").splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if "decision" in cells and "name" in cells:
            column = cells.index("decision"), cells.index("name")
        elif column and len(cells) > max(column) and re.fullmatch(r"\d+", cells[0]) and cells[column[0]] == "committed":
            names.add(cells[column[1]].strip("`"))
    return names


def require(path: Path, what: str) -> None:
    """Refuse an item whose generation would read `path`, which is not a file."""
    if not path.is_file():
        raise ReferenceError(f"{what} {rel(path)} does not exist; restore it, or remove the entry that names it")


def require_directory(path: Path, what: str) -> None:
    if not path.is_dir():
        raise ReferenceError(f"{what} {rel(path)} does not exist; restore it, or remove the entry that names it")


def vendored_spec(fixture: str) -> Path:
    """The document `generate-fern-fixture.sh` reads for a fixture's golden: its
    vendored `openapi.yml`, else the committed corpus source of that name."""
    vendored = ROOT / FIXTURES / fixture / "openapi.yml"
    committed = (ROOT / FIXTURES / "corpus-sources" / fixture / f"openapi{suffix}" for suffix in DOCUMENT_SUFFIXES)
    return vendored if vendored.is_file() else next((path for path in committed if path.is_file()), vendored)


def validate_corpus(item: str) -> None:
    """A row's committed source files, or a vendored fixture's document, and the
    document its flat golden is generated from."""
    rows, flats = corpus_rows(), flat_goldens()
    if item in rows:
        name, sources = rows[item], corpus_sources()
        for relative in sources.get(name, []):
            require(ROOT / relative, f"its committed specification ({CORPUS_SOURCES} row {name})")
        if name in committed_rows() and not sources.get(name):
            raise ReferenceError(f"CORPUS.md row {name} is `committed`, but {CORPUS_SOURCES} records no file of it")
        if item in flats and flats[item] != item:
            require(vendored_spec(flats[item]), "the document its flat golden is generated from,")
        return
    require_directory(ROOT / FIXTURES / item, "its fixture directory")
    if (ROOT / FIXTURES / item / "expected").is_dir():
        require(ROOT / FIXTURES / item / "openapi.yml", "its document")
    if item in flats:
        require(vendored_spec(flats[item]), "the document its flat golden is generated from,")


def list_corpus() -> list[str]:
    """Every fixture with a packaged or flat golden, and every row whose golden is
    an exact known Fern failure (retried at each pair, as `fern-goldens` does)."""
    fixtures = ROOT / FIXTURES
    return sorted(
        {
            path.parent.name
            for pattern in ("*/expected", "*/expected-flat", "*/known-fern-failure.json")
            for path in fixtures.glob(pattern)
        }
    )


def run_script(argv: list[str], log: Path, pair: Pair, tolerated: tuple[int, ...] = (0,)) -> int:
    """Run one item's delegate into `log`; an exit outside `tolerated` fails the item."""
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("w", encoding="utf-8", newline="\n") as handle:
        result = subprocess.run(
            argv,
            cwd=ROOT,
            stdout=handle,
            stderr=subprocess.STDOUT,
            env=dict(os.environ, FERN_CLI_VERSION=pair.cli),
            check=False,
        )
    if result.returncode not in tolerated:
        raise ReferenceError(
            f"`{' '.join(Path(a).name if i == 0 else a for i, a in enumerate(argv))}` exited {result.returncode}; see {rel(log)}"
        )
    return result.returncode


def generate_corpus(item: str, pair: Pair) -> None:
    rows, flats = corpus_rows(), flat_goldens()
    logs = ROOT / LOGS / "corpus"
    script = str(ROOT / "tools/fern-goldens/generate-fern-fixture.sh")
    if item in rows:
        if (ROOT / FIXTURES / item / "expected").is_dir() or (
            ROOT / FIXTURES / item / "known-fern-failure.json"
        ).is_file():
            # `fern-goldens` regenerates the packaged golden and a flat one over the row's own spec.
            run_script(
                [
                    str(ROOT / "tools/fern-goldens/fern-goldens"),
                    "generate",
                    "--version",
                    pair.generator,
                    "--fixture",
                    rows[item],
                ],
                logs / f"{item}.log",
                pair,
            )
        if item in flats and (flats[item] != item or not (ROOT / FIXTURES / item / "expected").is_dir()):
            run_script([script, "--layout", "flat", item, pair.generator], logs / f"{item}.flat.log", pair)
        return
    if not (ROOT / FIXTURES / item).is_dir():
        raise ReferenceError(f"no fixture directory tests/fixtures/{item}; `list corpus` names the family")
    if (ROOT / FIXTURES / item / "expected").is_dir():
        run_script([script, item, pair.generator], logs / f"{item}.log", pair)
    if item in flats:
        run_script([script, "--layout", "flat", item, pair.generator], logs / f"{item}.flat.log", pair)


def list_overlays() -> list[str]:
    return sorted(
        f"{path.parent.name}/{path.name}"
        for kind in OVERLAY_KINDS
        for path in (ROOT / FIXTURES).glob(f"*/{kind}")
        if path.is_dir()
    )


def overlay_value(item: str) -> str:
    """The setting an overlay is generated under: its kind's fixed value, or the
    count its golden's `.crozier-overlay.json` records."""
    fixture, _, kind = item.partition("/")
    golden = ROOT / FIXTURES / fixture / kind
    if kind not in OVERLAY_KINDS or not (golden / OVERLAY_MANIFEST).is_file():
        raise ReferenceError(f"{item} is no committed overlay; `list overlays` names the family")
    overlay = OVERLAY_KINDS[kind]
    value = overlay.value
    if overlay.recorded is not None:
        try:
            manifest = json.loads((golden / OVERLAY_MANIFEST).read_text(encoding="utf-8"))
        except ValueError as error:
            raise ReferenceError(
                f"cannot read {rel(golden / OVERLAY_MANIFEST)} ({error}); restore it from git"
            ) from None
        count = manifest.get(overlay.recorded) if isinstance(manifest, dict) else None
        if not isinstance(count, int) or isinstance(count, bool) or count < 0:
            raise ReferenceError(
                f"{rel(golden / OVERLAY_MANIFEST)}: {overlay.recorded} must be a non-negative integer, not {count!r}"
            )
        value = str(count)
    if value is None:
        raise ReferenceError(f"overlay kind {kind} names no value; fix OVERLAY_KINDS")
    return value


def validate_overlay(item: str) -> None:
    """Its manifest's setting, the golden it is reduced against, and a document
    to generate from: the vendored one, a committed source, or a row's fetch."""
    overlay_value(item)
    fixture = item.partition("/")[0]
    require_directory(ROOT / FIXTURES / fixture / "expected", "the golden it is reduced against,")
    if not vendored_spec(fixture).is_file() and fixture not in corpus_rows():
        require(vendored_spec(fixture), "its document")


def generate_overlay(item: str, pair: Pair) -> None:
    fixture, _, kind = item.partition("/")
    overlay = OVERLAY_KINDS[kind]
    value = overlay_value(item)
    run_script(
        [str(ROOT / "tools/fern-goldens/fern-overlay-goldens.sh"), "--jobs", "1", overlay.flag, value, fixture],
        ROOT / LOGS / "overlays" / f"{fixture}.{kind}.log",
        pair,
    )


def list_handwritten() -> list[str]:
    return sorted(path.parent.name for path in (ROOT / HANDWRITTEN).glob("*/evidence.toml"))


def handwritten_audiences(item: str) -> tuple[str, ...]:
    """A hand-written fixture's declared audiences, once its document and the
    evidence it restates are known good."""
    fixture = ROOT / HANDWRITTEN / item
    evidence = fixture / "evidence.toml"
    require(evidence, "its evidence")
    require(fixture / "openapi.yml", "its document")
    try:
        declared = tomllib.loads(evidence.read_text(encoding="utf-8")).get("audiences", [])
    except tomllib.TOMLDecodeError as error:
        raise ReferenceError(f"cannot read {rel(evidence)} ({error}); repair its TOML") from None
    if not isinstance(declared, list) or not all(
        plain_yaml_name(name, r"[A-Za-z][A-Za-z0-9._-]*") for name in declared
    ):
        raise ReferenceError(
            f"{rel(evidence)}: audiences must be a list of audience labels, none of {sorted(YAML_KEYWORDS)}, "
            f"not {declared!r}"
        )
    check_evidence(evidence)
    recorded_generator_config(fixture / "fern-expected")
    return tuple(declared)


def generate_handwritten(item: str, pair: Pair) -> None:
    fixture = ROOT / HANDWRITTEN / item
    evidence = fixture / "evidence.toml"
    audiences = handwritten_audiences(item)
    # A fixture generated under a non-default setting keeps it: the committed
    # tree's own `.fern/metadata.json` records the generator config it was made with.
    config = recorded_generator_config(fixture / "fern-expected")
    generated_tree(
        fixture / "openapi.yml",
        fixture / "fern-expected",
        pair,
        enum_type="python-enums",
        layout="packaged",
        audiences=audiences,
        client_class_name=config.client_class_name,
        extra_fields=config.extra_fields,
    )
    rewrite_evidence(evidence, pair, contract_digest(fixture / "fern-expected"))


class EnumMode(StrEnum):
    """Fern's `pydantic_config.enum_type`, as this family's records spell it."""

    PYTHON_ENUMS = "python-enums"
    LITERALS = "literals"


class Layout(StrEnum):
    """Whether Fern writes the packaged SDK (`--preview`) or the flat module tree."""

    PACKAGED = "packaged"
    FLAT = "flat"


ENUM_TYPES = tuple(EnumMode)
LAYOUTS = tuple(Layout)
OVERLAY_BASES = ("expected", "fern-expected")


@dataclass(frozen=True)
class CaseOverlay:
    """The overlay a case reduces to: the tree kind it is a delta against
    (`expected` or `fern-expected`), and that base tree, or None over no base."""

    label: str
    base: Path | None


@dataclass(frozen=True)
class MeasurementCase:
    """One `cases.tsv` row: the document a case generates from, its enum mode and
    layout, and the overlay it reduces to (None for a complete tree)."""

    name: str
    document: Path
    enum_type: EnumMode
    layout: Layout
    overlay: CaseOverlay | None


def case_row_failure(row: dict[str, str], seen: set[str]) -> str | None:
    """Why one `cases.tsv` row is malformed, or `None`. Whether the document and
    base tree it names exist is the item's own check (`validate_measurement`),
    so one missing input never hides the rest of the table."""
    name, document, overlay = row["case"], row["document"], row["overlay"]
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*(?:/[a-z0-9][a-z0-9._-]*)*", name) or name in seen:
        return "a case is a unique lower-case path under docs/fern-measurements/"
    if row["enum_type"] not in ENUM_TYPES or row["layout"] not in LAYOUTS:
        return f"enum_type is one of {', '.join(ENUM_TYPES)} and layout one of {', '.join(LAYOUTS)}"
    target = (ROOT / document).resolve()
    if not document or not target.is_relative_to(ROOT.resolve()):
        return f"its document {document!r} is no path of this repository"
    label, colon, base = overlay.partition(":")
    base_tree = (ROOT / base).resolve() if base and base != "-" else None
    if overlay != "-" and not (
        colon
        and label in OVERLAY_BASES
        and (base == "-" or (base_tree is not None and base_tree.is_relative_to(ROOT.resolve())))
    ):
        return f"its overlay {overlay!r} is `-` or `<{'|'.join(OVERLAY_BASES)}>:<base tree or ->`"
    return None


@read_once
def cases() -> dict[str, MeasurementCase]:
    """`cases.tsv`'s rows, each a unique case naming a document of this
    repository, an enum mode, a layout and an overlay this family can build."""
    found: dict[str, MeasurementCase] = {}
    for row in read_tsv(CASES, CASES_HEADER):
        failure = case_row_failure(row, set(found))
        if failure:
            raise ReferenceError(f"{CASES} row {row['case']!r}: {failure}")
        label, _, base = row["overlay"].partition(":")
        overlay = None if row["overlay"] == "-" else CaseOverlay(label, None if base == "-" else ROOT / base)
        found[row["case"]] = MeasurementCase(
            row["case"], ROOT / row["document"], EnumMode(row["enum_type"]), Layout(row["layout"]), overlay
        )
    return found


PARAMETER_LITERALS = MEASUREMENTS / "parameter-literals"
# Where a parameter-literals case's document and complete python-enums tree
# live, first match wins: its hand-written fixture, or the parameter-lowering
# measurement a hand-written proof was retired into once a real document
# covered it (crozier-e2e's `parameter_case_dir` reads the same two homes).
PARAMETER_LITERAL_HOMES = (HANDWRITTEN, MEASUREMENTS / "parameter-lowering")


def parameter_literal_fixture(case: str) -> Path:
    """The directory holding `case`'s `openapi.yml` and `fern-expected/`; the
    hand-written one, which then names what is missing, when neither has it."""
    homes = [ROOT / home / case for home in PARAMETER_LITERAL_HOMES]
    return next((home for home in homes if (home / "openapi.yml").is_file()), homes[0])


def parameter_literal_cases() -> list[str]:
    """`certified-trees.json`'s fixtures: an object of hand-written fixture names to digests."""
    path = ROOT / PARAMETER_LITERALS / "certified-trees.json"
    try:
        digests = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ReferenceError(f"cannot read {rel(path)} ({error}); restore it from git") from None
    if not isinstance(digests, dict) or not all(
        isinstance(name, str)
        and re.fullmatch(r"[a-z0-9][a-z0-9-]*", name)
        and isinstance(digest, str)
        and re.fullmatch(r"[0-9a-f]{64}", digest)
        for name, digest in digests.items()
    ):
        raise ReferenceError(f"{rel(path)} must map hand-written fixture names to SHA-256 digests")
    return sorted(digests)


REFUSAL_LOG = ".fern.log"
PINNED_RUN = "measurement.json"


class RefusalLog(NamedTuple):
    """A measurement whose committed reference is Fern's log refusing a document
    (None when no document is beside the log, which its check reports)."""

    log: Path
    document: Path | None


@read_once
def refusal_logs() -> dict[str, RefusalLog]:
    """`<group>/<case>/<stem>` -> (its `<stem>.fern.log`, the `<stem>.openapi.*`
    document beside it): a measurement whose committed reference is Fern's
    refusal of that document, as Fern printed it. A log whose document is gone
    is still an item, so its check names it rather than the item vanishing."""
    found = {}
    for log in sorted((ROOT / MEASUREMENTS).glob(f"*/*/*{REFUSAL_LOG}")):
        stem = log.name[: -len(REFUSAL_LOG)]
        document = next(
            (
                log.with_name(f"{stem}.openapi{suffix}")
                for suffix in DOCUMENT_SUFFIXES
                if log.with_name(f"{stem}.openapi{suffix}").is_file()
            ),
            None,
        )
        found[rel(log.parent / stem)[len(str(MEASUREMENTS)) + 1 :]] = RefusalLog(log, document)
    return found


@dataclass(frozen=True)
class PinnedRecord:
    """A `measurement.json`: the probe a pinned run read, the pair it ran at,
    both exit statuses, the check's diagnostic, each log's digest, the number of
    Python files Fern wrote and the probe's digest."""

    probe: str
    fern_cli: str = ""
    generator: str = ""
    check_exit: str = ""
    check_diagnostic: str = ""
    check_log_sha256: str = ""
    generate_exit: str = ""
    generate_log_sha256: str = ""
    generate_python_files: int = 0
    sha256: str = ""


@dataclass(frozen=True)
class PinnedRun:
    """A measurement recording one pinned run over its own probe: the case
    directory, its `measurement.json` and the probe that record names."""

    case: Path
    record: PinnedRecord
    probe: Path


def pinned_run(record_path: Path) -> PinnedRun:
    """The run a `measurement.json` records, held to an object naming a probe
    file inside its own case directory."""
    case = record_path.parent
    try:
        record = json.loads(record_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ReferenceError(f"cannot read {rel(record_path)} ({error}); restore it from git") from None
    probe = record.get("probe") if isinstance(record, dict) else None
    target = (case / probe).resolve() if isinstance(probe, str) and probe else None
    if (
        not isinstance(record, dict)
        or target is None
        or not target.is_relative_to(case.resolve())
        or not target.is_file()
    ):
        raise ReferenceError(
            f"{rel(record_path)} must be an object whose `probe` names a file in {rel(case)}, not {probe!r}"
        )
    known = {field.name for field in fields(PinnedRecord)}
    return PinnedRun(case, PinnedRecord(**{key: value for key, value in record.items() if key in known}), target)


@read_once
def pinned_runs() -> dict[str, Path]:
    """`<case>` -> its `measurement.json`: a measurement recording one pinned run
    over its own probe, with the run's log and Fern's raw client."""
    return {
        rel(record.parent)[len(str(MEASUREMENTS)) + 1 :]: record
        for record in sorted((ROOT / MEASUREMENTS).glob(f"*/{PINNED_RUN}"))
    }


def list_measurements() -> list[str]:
    extra = (
        [f"parameter-literals/{case}" for case in parameter_literal_cases()]
        if (ROOT / PARAMETER_LITERALS / "certified-trees.json").is_file()
        else []
    )
    return sorted([*cases(), *extra, *refusal_logs(), *pinned_runs()])


def remeasure_refusal_log(item: str, log: Path, document: Path, pair: Pair) -> None:
    """Rewrite a refusal measurement's log at `pair`; fail where Fern now generates."""
    with run_fern(document, pair, check=True) as run:
        log.write_text(fern_log(pair, run), encoding="utf-8", newline="\n")
        if run.generate_exit == "0" and run.tree is not None:
            raise ReferenceError(
                f"Fern now generates {item}; its log is written, so restate the evidence that cites the refusal"
            )


def remeasure_pinned_run(record_path: Path, pair: Pair) -> None:
    """Re-take a pinned run over the case's probe: its log, Fern's raw
    `src/fern/raw_client.py` (kept as text, bytes unedited) and the record of
    both exits and each log's digest."""
    run_record = pinned_run(record_path)
    case, probe = run_record.case, run_record.probe
    with run_fern(probe, pair, check=True) as run:
        if run.generate_exit != "0" or run.tree is None:
            raise ReferenceError(f"fern generate exited {run.generate_exit} with no tree")
        (case / "fern.log").write_text(fern_log(pair, run), encoding="utf-8", newline="\n")
        shutil.copyfile(run.tree / "src" / "fern" / "raw_client.py", case / "fern-raw_client.py.txt")
        python_files = sum(1 for path in run.tree.rglob("*.py") if path.is_file())
        record = PinnedRecord(
            probe=run_record.record.probe,
            fern_cli=pair.cli,
            generator=pair.generator,
            check_exit=run.check_exit,
            check_diagnostic=preferred_diagnostic(run.check_log) or "All checks passed",
            check_log_sha256=hashlib.sha256(run.check_log.encode("utf-8")).hexdigest(),
            generate_exit=run.generate_exit,
            generate_log_sha256=hashlib.sha256(run.generate_log.encode("utf-8")).hexdigest(),
            generate_python_files=python_files,
            sha256=hashlib.sha256(probe.read_bytes()).hexdigest(),
        )
        record_path.write_text(
            json.dumps(asdict(record), indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
        )


def generate_parameter_literal(case: str, pair: Pair) -> None:
    """Re-measure a parameter-literals claim: Fern's literals tree for a
    hand-written fixture (client `FernApi`, extra fields `allow`) is its
    python-enums tree less `core/enum.py`, with only `.fern/metadata.json`
    differing. Records that metadata and the tree's digest, or fails naming the
    first file the claim no longer holds for."""
    fixture = parameter_literal_fixture(case)
    with run_fern(
        fixture / "openapi.yml", pair, enum_type="literals", client_class_name="FernApi", extra_fields="allow"
    ) as run:
        if run.generate_exit != "0" or run.tree is None:
            raise ReferenceError(f"fern generate exited {run.generate_exit} with no tree")
        with tempfile.TemporaryDirectory() as scratch:
            tree = Path(scratch) / "tree"
            strip_into(run.tree, tree)
            base = fixture / "fern-expected"
            ignored = {".fern/metadata.json", ".crozier-fern-golden.json"}
            mine = {p.relative_to(tree).as_posix() for p in tree.rglob("*") if p.is_file()} - ignored
            theirs = {p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file()} - ignored
            theirs.discard("src/fern/core/enum.py")
            differing = sorted(mine ^ theirs) or [
                rel for rel in sorted(mine) if (tree / rel).read_bytes() != (base / rel).read_bytes()
            ]
            if differing:
                raise ReferenceError(
                    f"the literals tree no longer equals the python-enums tree less core/enum.py: {differing[0]}"
                )
            name = (
                f"{case}.metadata.json"
                if (ROOT / PARAMETER_LITERALS / f"{case}.metadata.json").is_file()
                else "metadata.json"
            )
            shutil.copyfile(tree / ".fern" / "metadata.json", ROOT / PARAMETER_LITERALS / name)
            digests_path = ROOT / PARAMETER_LITERALS / "certified-trees.json"
            digests = json.loads(digests_path.read_text(encoding="utf-8"))
            digests[case] = contract_digest(tree)
            digests_path.write_text(json.dumps(digests, indent=2) + "\n", encoding="utf-8", newline="\n")


MEASUREMENT_REFUSAL = "fern-refusal.txt"


def refused_measurement(item: str, row: MeasurementCase, record: Path, pair: Pair) -> None:
    """Re-measure a case whose committed reference is Fern's refusal: rewrite its
    Contract A record, or, where Fern now generates, install the tree in its place
    and fail naming the case, whose evidence then states a refusal Fern no longer
    makes."""
    with run_fern(row.document, pair, enum_type=row.enum_type, layout=row.layout) as run:
        if run.generate_exit == "0" and run.tree is not None:
            destination = record.with_name("fern-expected")
            stage = Path(tempfile.mkdtemp(prefix=".fern-references.", dir=record.parent))
            try:
                strip_into(run.tree, stage / destination.name)
                install(stage / destination.name, destination)
            finally:
                shutil.rmtree(stage, ignore_errors=True)
            record.unlink()
            raise ReferenceError(
                f"Fern now generates {item}; its tree replaces {rel(record)}, so restate the evidence that cites the refusal"
            )
        diagnostic = preferred_diagnostic(run.generate_log)
        if not diagnostic:
            raise ReferenceError(
                f"fern generate exited {run.generate_exit} printing no diagnostic this tool recognises:\n"
                f"{run.generate_log.strip()[-2000:]}"
            )
        write_refusal_record(record, pair, run.generate_exit, diagnostic)


def validate_measurement(item: str) -> None:
    """Every input a measurement's re-measurement reads: a parameter-literals
    claim's document and python-enums tree, a refusal log's document, a pinned
    run's probe, a case's document and overlay base, and the provenance its
    `evidence.toml` and `evidence.md` restate."""
    if item.startswith("parameter-literals/"):
        fixture = parameter_literal_fixture(item.removeprefix("parameter-literals/"))
        require(
            fixture / "openapi.yml", f"its document ({rel(ROOT / PARAMETER_LITERALS)}/certified-trees.json names it)"
        )
        require_directory(fixture / "fern-expected", "the python-enums tree it is compared with,")
        return
    if item in (logs := refusal_logs()):
        if logs[item].document is None:
            stem = logs[item].log.name[: -len(REFUSAL_LOG)]
            raise ReferenceError(
                f"no document {rel(logs[item].log.parent)}/{stem}.openapi.(yml|yaml|json) is beside its log "
                f"{rel(logs[item].log)}; restore it, or remove the log"
            )
        return
    if item in (runs := pinned_runs()):
        pinned_run(runs[item])
        return
    row = cases().get(item)
    if row is None:
        raise ReferenceError(f"{item} is no {CASES} row; `list measurements` names the family")
    require(row.document, f"its document ({CASES} names it)")
    if row.overlay is not None and row.overlay.base is not None:
        require_directory(row.overlay.base, f"its overlay base tree ({CASES} names it)")
    case = ROOT / MEASUREMENTS / item
    if (case / "evidence.toml").is_file() and "digest = " in (case / "evidence.toml").read_text(encoding="utf-8"):
        check_evidence(case / "evidence.toml")
    if (case / "evidence.md").is_file():
        check_evidence_note(case / "evidence.md")


def generate_measurement(item: str, pair: Pair) -> None:
    if item.startswith("parameter-literals/"):
        generate_parameter_literal(item.removeprefix("parameter-literals/"), pair)
        return
    if item in (logs := refusal_logs()):
        document = logs[item].document
        if document is None:
            raise ReferenceError(f"{item} has no `<stem>.openapi.*` document beside its log")
        remeasure_refusal_log(item, logs[item].log, document, pair)
        return
    if item in (runs := pinned_runs()):
        remeasure_pinned_run(runs[item], pair)
        return
    row = cases().get(item)
    if row is None:
        raise ReferenceError(f"{item} is no {CASES} row; `list measurements` names the family")
    destination = ROOT / MEASUREMENTS / item / "fern-expected"
    record = destination.with_name(MEASUREMENT_REFUSAL)
    if record.is_file() and not destination.exists():
        refused_measurement(item, row, record, pair)
        return
    evidence = destination.parent / "evidence.toml"
    # `validate_measurement` held both provenance files before Fern started.
    restates_evidence = evidence.is_file() and "digest = " in evidence.read_text(encoding="utf-8")
    generated_tree(row.document, destination, pair, enum_type=row.enum_type, layout=row.layout)
    if row.overlay is not None:
        provenance: dict[str, object] = {
            "fern_python_sdk_version": pair.generator,
            "fern_cli_version": pair.cli,
            "enum_type": row.enum_type,
            "base": row.overlay.label,
        }
        base_tree = row.overlay.base
        if row.overlay.label == "fern-expected":
            # The digest of the complete tree Fern wrote, which the gate rebuilds
            # from the base and the overlay before comparing.
            provenance["digest"] = contract_digest(destination)
        reduce_overlay(destination, base_tree, provenance)
    if restates_evidence:
        rewrite_evidence(evidence, pair, contract_digest(destination))
    note = destination.parent / "evidence.md"
    if note.is_file():
        restate_evidence_note(note, pair, contract_digest(destination))


@dataclass
class ManifestRow:
    """One `MANIFEST.tsv` row: a probe, its Contract A form and verdict, the
    artifact its gate reads, the control it is measured against, and the
    artifact's digest."""

    key: str
    form: str
    verdict: str
    artifact: str
    control: str
    digest: str


MANIFEST_HEADER = tuple(field.name for field in fields(ManifestRow))


PROBE_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")


def manifest_rows() -> list[ManifestRow]:
    """`MANIFEST.tsv`'s rows, each naming its probe and any control as a plain
    file stem, since both become paths under the probe directories."""
    rows = [ManifestRow(**row) for row in read_tsv(MANIFEST, MANIFEST_HEADER)]
    for row in rows:
        if not PROBE_NAME.fullmatch(row.key) or not (row.control == "—" or PROBE_NAME.fullmatch(row.control)):
            raise SystemExit(
                f"fern-references: {MANIFEST} row {row.key!r} names a probe or control {row.control!r} that is "
                "no plain file stem; restore it from git"
            )
    return rows


def write_manifest(rows: list[ManifestRow]) -> None:
    (ROOT / MANIFEST).write_text(
        "\t".join(MANIFEST_HEADER) + "\n" + "".join("\t".join(astuple(row)) + "\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )


def list_probes() -> list[str]:
    names = set()
    for row in manifest_rows():
        names.add(row.key)
        if row.control != "—":
            names.add(row.control)
    return sorted(names)


def preferred_diagnostic(log: str) -> str:
    """The error Fern printed of the most telling kind, in this order of
    preference: an `issue:` line of `fern check`'s report, the line after
    `[error]` in the generation's, the exception a crashed generator raised
    (`KeyError: …`), an `Error:` line, then a `Failed to …` line; the first of
    that kind in the log."""
    for pattern in (
        r"issue: (.+)",
        r"\[error\] (.+)",
        r"(?m)^\s*([A-Z]\w*Error: .+)$",
        r"(?m)^\s*(?:Error|error): (.+)",
        r"Failed to .+",
    ):
        match = re.search(pattern, log)
        if match:
            return (match.group(1) if match.groups() else match.group(0)).strip()
    return ""


def write_refusal_record(record: Path, pair: Pair, generate_exit: str, diagnostic: str) -> None:
    """A Contract A refusal record: the pair, the exit status and Fern's first diagnostic."""
    record.write_text(
        f"fern_cli_version: {pair.cli}\nfern_python_sdk_version: {pair.generator}\n"
        f"generate_exit: {generate_exit}\ndiagnostic: {diagnostic}\noutput_tree: none\n",
        encoding="utf-8",
        newline="\n",
    )


def validate_probe(item: str) -> None:
    require(ROOT / PROBES / f"{item}.yml", f"its probe document ({MANIFEST} names it)")


def generate_probe(item: str, pair: Pair) -> None:
    document = ROOT / PROBES / f"{item}.yml"
    tree = ROOT / PROBE_EXPECTED / item
    record = ROOT / PROBE_EXPECTED / f"{item}{REFUSAL_SUFFIX}"
    with run_fern(document, pair, enum_type="python-enums", layout="packaged") as run:
        if run.generate_exit == "0" and run.tree is not None:
            stage = Path(tempfile.mkdtemp(prefix=".fern-references.", dir=tree.parent))
            try:
                strip_into(run.tree, stage / item)
                install(stage / item, tree)
            finally:
                shutil.rmtree(stage, ignore_errors=True)
            record.unlink(missing_ok=True)
            artifact, digest = tree, contract_digest(tree)
        else:
            diagnostic = preferred_diagnostic(run.generate_log)
            if not diagnostic:
                log = ROOT / LOGS / "probes" / f"{item}.generate.log"
                log.parent.mkdir(parents=True, exist_ok=True)
                log.write_text(run.generate_log, encoding="utf-8", newline="\n")
                raise ReferenceError(
                    f"fern generate exited {run.generate_exit} printing no diagnostic this tool recognises; "
                    f"read {rel(log)} and extend preferred_diagnostic"
                )
            write_refusal_record(record, pair, run.generate_exit, diagnostic)
            if tree.exists():
                shutil.rmtree(tree)
            artifact, digest = record, hashlib.sha256(record.read_bytes()).hexdigest()
    new, old = rel(artifact), rel(tree if artifact == record else record)
    rows = manifest_rows()
    flipped = []
    for row in rows:
        if row.artifact == new:
            row.digest = digest
        elif row.artifact == old or (row.control == item and artifact == record):
            flipped.append(row.key)
            if row.artifact == old:
                row.artifact, row.digest = new, digest
    write_manifest(rows)
    if flipped:
        raise ReferenceError(
            f"Fern's outcome on {item} changed form ({'refusal' if artifact == record else 'tree'} now); "
            f"the new artifact is written, and {MANIFEST} row(s) {', '.join(sorted(set(flipped)))} need their "
            "form and verdict decided under Contract A"
        )


def fern_log(pair: Pair, run: FernRun) -> str:
    return (
        f"Fern CLI {pair.cli}, python-sdk {pair.generator}\n"
        f"check exit: {run.check_exit}\n{run.check_log.rstrip()}\n\n"
        f"generate exit: {run.generate_exit}\n{run.generate_log.rstrip()}\n"
    )


def list_authored() -> list[str]:
    """Every authored probe: a case directory with its document or the log
    Fern's run over it wrote, so a case whose document is gone is still named."""
    return sorted(
        {path.parent.name for name in ("openapi.yml", "fern.log") for path in (ROOT / AUTHORED).glob(f"*/{name}")}
    )


def validate_authored(item: str) -> None:
    require(ROOT / AUTHORED / item / "openapi.yml", "its document")


def generate_authored(item: str, pair: Pair) -> None:
    case = ROOT / AUTHORED / item
    with run_fern(case / "openapi.yml", pair, check=True) as run:
        (case / "fern.log").write_text(fern_log(pair, run), encoding="utf-8", newline="\n")
        if run.generate_exit != "0" or run.tree is None:
            raise ReferenceError(
                f"Fern now refuses {item} (generate exit {run.generate_exit}); its fern.log is written — a "
                "refused document is no authored probe, so it moves to the refusal registry"
            )
        stage = Path(tempfile.mkdtemp(prefix=".fern-references.", dir=case))
        try:
            strip_into(run.tree, stage / "fern-expected")
            install(stage / "fern-expected", case / "fern-expected")
        finally:
            shutil.rmtree(stage, ignore_errors=True)


def evidence_document(log: Path) -> Path | None:
    stem = log.name[: -len(PINNED_LOG)]
    return next((log.with_name(stem + s) for s in DOCUMENT_SUFFIXES if log.with_name(stem + s).is_file()), None)


def registry_column(path: Path, column: str) -> list[str]:
    """One column of a refusal-registry table, found by its header. The table's
    other columns are `fern-refusals.py`'s to define; this family reads only the
    item names."""
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    header = lines[0].split("\t") if lines else []
    if column not in header:
        raise SystemExit(f"fern-references: {path} has no `{column}` column; restore it from git")
    index = header.index(column)
    names = []
    for number, line in enumerate(lines[1:], start=2):
        cells = line.split("\t")
        if not line:
            continue
        if len(cells) != len(header) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", cells[index]):
            raise SystemExit(
                f"fern-references: {path}:{number} has {len(cells)} cells for {len(header)} columns or a "
                f"`{column}` that is no lower-case name; restore it from git"
            )
        names.append(cells[index])
    return names


def list_refusals() -> list[str]:
    classes = registry_column(REGISTRY / "classes.tsv", "class")
    findings = [f"findings/{name}" for name in registry_column(REGISTRY / "findings.tsv", "finding")]
    evidence = [
        rel(log)[len(str(REGISTRY)) + 1 : -len(PINNED_LOG)]
        for log in sorted((ROOT / REGISTRY).glob(f"*/evidence/*{PINNED_LOG}"))
        if evidence_document(log) is not None
    ]
    return sorted(classes) + findings + evidence


def finding_probe(name: str) -> Path:
    """The probe document `findings.tsv` names for a finding."""
    path = REGISTRY / "findings.tsv"
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    header = lines[0].split("\t") if lines else []
    if "probe" not in header or "finding" not in header:
        raise ReferenceError(f"{path} has no `finding` and `probe` columns; restore it from git")
    for line in lines[1:]:
        cells = line.split("\t")
        if len(cells) == len(header) and cells[header.index("finding")] == name:
            return ROOT / cells[header.index("probe")]
    raise ReferenceError(f"{path} has no row for finding {name}")


def validate_refusal(item: str) -> None:
    """A finding's probe `findings.tsv` names, an evidence log's document, or a
    class's `probe.yml`: the document each one's measurement reads."""
    if item.startswith("findings/"):
        require(finding_probe(item.removeprefix("findings/")), f"its probe document ({REGISTRY}/findings.tsv names it)")
    elif "/evidence/" in item:
        log = ROOT / REGISTRY / f"{item}{PINNED_LOG}"
        if evidence_document(log) is None:
            raise ReferenceError(f"{item} has no pinned log beside a probe document; `list refusals` names the family")
    else:
        require(ROOT / REGISTRY / item / "probe.yml", f"its probe document ({REGISTRY}/classes.tsv names the class)")


def generate_refusal(item: str, pair: Pair) -> None:
    tool = str(ROOT / "tools/fern-refusals/fern-refusals.py")
    logs = ROOT / LOGS / "refusals"
    if item.startswith("findings/"):
        name = item.removeprefix("findings/")
        run_script(["python3", tool, "finding", "--jobs", "1", name], logs / f"finding.{name}.log", pair)
    elif "/evidence/" in item:
        log = ROOT / REGISTRY / f"{item}{PINNED_LOG}"
        document = evidence_document(log) if log.is_file() else None
        if document is None:
            raise ReferenceError(f"{item} has no pinned log beside a probe document; `list refusals` names the family")
        with run_fern(document, pair, check=True) as run:
            log.write_text(fern_log(pair, run), encoding="utf-8", newline="\n")
    else:
        # A class whose probe no longer reproduces its recorded refusal keeps the
        # record and is reported: the weekly run reads this file as its outcome.
        changes = refusal_changes(item)
        changes.unlink(missing_ok=True)
        log = logs / f"probe.{item}.log"
        argv = ["python3", tool, "probe", "--jobs", "1", "--changes", str(changes), item]
        if run_script(argv, log, pair, tolerated=(0, PROBE_CHANGED_EXIT)) == PROBE_CHANGED_EXIT:
            if not reports_class(changes, item):
                raise ReferenceError(
                    f"`fern-refusals.py probe` exited {PROBE_CHANGED_EXIT}, which reports a changed refusal, but "
                    f"{rel(changes)} does not name {item}; see {rel(log)}"
                )
            print(
                f"fern-references: refusals {item}: Fern no longer reproduces the recorded refusal, which is "
                f"kept; {rel(changes)} says how, and {rel(log)} has the run",
                file=sys.stderr,
                flush=True,
            )


def reports_class(changes: Path, item: str) -> bool:
    """Whether a `--changes` report holds a JSON object for class `item`."""
    try:
        lines = changes.read_text(encoding="utf-8").splitlines()
    except OSError:
        return False
    for line in lines:
        with contextlib.suppress(ValueError):
            record = json.loads(line)
            if isinstance(record, dict) and record.get("class") == item:
                return True
    return False


def refusal_changes(item: str) -> Path:
    """Where a refusal class's probe reports an outcome that no longer matches its record."""
    return ROOT / LOGS / "refusals" / f"probe.{item}.changes.jsonl"


def list_departure_evidence() -> list[str]:
    return sorted(path.parent.name for path in (ROOT / DEPARTURE_EVIDENCE).glob("*/fern-reference.json"))


class DepartureSettings(NamedTuple):
    enum_type: str
    layout: str
    organization: str


def departure_settings(item: str) -> DepartureSettings:
    """The settings a departure's `fern-reference.json` records, once it and the
    note's own document are known good."""
    case = ROOT / DEPARTURE_EVIDENCE / item
    settings_path = case / "fern-reference.json"
    require(settings_path, "its settings")
    require(case / "openapi.yml", "its document")
    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
    except ValueError as error:
        raise ReferenceError(f"cannot read {rel(settings_path)} ({error}); restore it from git") from None
    if not isinstance(settings, dict):
        raise ReferenceError(f"{rel(settings_path)} must be an object of generation settings")
    enum_type = settings.get("enum_type", "python-enums")
    layout = settings.get("layout", "packaged")
    organization = settings.get("organization", "fern")
    if (
        enum_type not in ENUM_TYPES
        or layout not in LAYOUTS
        or not (isinstance(organization, str) and re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", organization))
    ):
        raise ReferenceError(
            f"{rel(settings_path)}: enum_type is one of {', '.join(ENUM_TYPES)}, layout one of "
            f"{', '.join(LAYOUTS)} and organization letters and digits starting with a letter, not {enum_type!r}, {layout!r}, {organization!r}"
        )
    return DepartureSettings(enum_type, layout, organization)


def generate_departure_evidence(item: str, pair: Pair) -> None:
    """A departure's evidence tree: Fern's output for the note's own document,
    under the settings its `fern-reference.json` records."""
    case = ROOT / DEPARTURE_EVIDENCE / item
    enum_type, layout, organization = departure_settings(item)
    with run_fern(case / "openapi.yml", pair, enum_type=enum_type, layout=layout, organization=organization) as run:
        if run.generate_exit != "0" or run.tree is None:
            raise ReferenceError(f"fern generate exited {run.generate_exit} with no tree")
        stage = Path(tempfile.mkdtemp(prefix=".fern-references.", dir=case))
        try:
            strip_into(run.tree, stage / "fern-reference")
            install(stage / "fern-reference", case / "fern-reference")
        finally:
            shutil.rmtree(stage, ignore_errors=True)


def validate_handwritten(item: str) -> None:
    handwritten_audiences(item)


def validate_departure_evidence(item: str) -> None:
    departure_settings(item)


@dataclass(frozen=True)
class Family:
    """One reference family: what lists its item names, what validates one's
    inputs (raising `ReferenceError` with the reason, reading files only), and
    what regenerates one. `check` and `generate` both call `validate`, so the
    two never disagree about an input."""

    list: Callable[[], list[str]]
    generate: Callable[[str, Pair], None]
    validate: Callable[[str], None]


FAMILY: dict[str, Family] = {
    "corpus": Family(list_corpus, generate_corpus, validate_corpus),
    "overlays": Family(list_overlays, generate_overlay, validate_overlay),
    "handwritten": Family(list_handwritten, generate_handwritten, validate_handwritten),
    "measurements": Family(list_measurements, generate_measurement, validate_measurement),
    "probes": Family(list_probes, generate_probe, validate_probe),
    "authored-probes": Family(list_authored, generate_authored, validate_authored),
    "refusals": Family(list_refusals, generate_refusal, validate_refusal),
    "departure-evidence": Family(list_departure_evidence, generate_departure_evidence, validate_departure_evidence),
}


def broken(family: str, item: str) -> str | None:
    """The line `check` prints, and `generate` refuses with, for an item whose
    inputs fail its family's validation: `<family> <item>: <reason>`."""
    try:
        FAMILY[family].validate(item)
    except (ReferenceError, OSError, UnicodeDecodeError) as error:
        return f"{family} {item}: {error}"
    return None


def check(families: list[str]) -> int:
    """Validate every item of `families` (every family when empty), printing one
    line per broken item to stderr. Reads the tree only: no Fern, Docker or network."""
    global _CHECKING
    _CHECKING, lines = {}, []
    for family in families or list(FAMILY):
        try:
            items = FAMILY[family].list()
        except (ReferenceError, SystemExit, OSError) as error:
            reason = str(error).removeprefix("fern-references: ")
            lines.append(f"{family} (its listing): {reason}")
            continue
        lines += [line for item in items if (line := broken(family, item)) is not None]
    sys.stderr.write("".join(f"{line}\n" for line in lines))
    if lines:
        print(f"fern-references: check: {len(lines)} broken item(s); repair each input named above", file=sys.stderr)
        return 1
    return 0


# The version overrides a family's delegate cannot honour, and why: an overlay
# is generated at the version its own golden records (run `corpus` first), and
# `fern-refusals.py` reads the certified pair itself.
UNPINNABLE: dict[str, dict[str, str]] = {
    "overlays": {"--version": "each overlay is generated at the version its golden's provenance records"},
    "refusals": {
        "--version": "fern-refusals.py measures at the certified pair metadata.json declares",
        "--cli-version": "fern-refusals.py measures at the certified pair metadata.json declares",
    },
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="fern-references.py", description=__doc__.split("\n", 1)[0])
    commands = parser.add_subparsers(dest="command", required=True)
    listing = commands.add_parser("list", help="print the family's item names")
    listing.add_argument("family", choices=tuple(FAMILY))
    checking = commands.add_parser("check", help="validate every item's inputs without running Fern")
    checking.add_argument("families", nargs="*", choices=tuple(FAMILY), metavar="FAMILY")
    generate = commands.add_parser("generate", help="regenerate the named items, or the whole family")
    generate.add_argument("family", choices=tuple(FAMILY))
    generate.add_argument(
        "--version", help="fern-python-sdk version (default: the certified pair's; not for overlays or refusals)"
    )
    generate.add_argument("--cli-version", help="Fern CLI version (default: the certified pair's; not for refusals)")
    generate.add_argument("items", nargs="*")
    args = parser.parse_args(argv)
    if args.command == "check":
        return check(args.families)
    family = FAMILY[args.family]
    lister, generator = family.list, family.generate
    try:
        known = lister()
    except ReferenceError as error:
        print(f"fern-references: {error}", file=sys.stderr)
        return 1
    if args.command == "list":
        sys.stdout.write("".join(f"{item}\n" for item in known))
        return 0
    for flag, value in (("--version", args.version), ("--cli-version", args.cli_version)):
        if value and flag in UNPINNABLE.get(args.family, ()):
            parser.error(f"{args.family} cannot take {flag}: {UNPINNABLE[args.family][flag]}")
    certified = certified_pair()
    pair = Pair(cli=args.cli_version or certified.cli, generator=args.version or certified.generator)
    for value in (pair.cli, pair.generator):
        if not VERSION.fullmatch(value):
            parser.error(f"invalid Fern version {value!r}; use an exact semantic version")
    unknown = [item for item in args.items if item not in known]
    if unknown:
        parser.error(
            f"no {args.family} item {', '.join(unknown)}; `fern-references.py list {args.family}` names the family"
        )
    failures = []
    for item in args.items or known:
        # The validation `check` runs, before Fern starts, with its reason line.
        if (line := broken(args.family, item)) is not None:
            failures.append(line)
            print(f"fern-references: {line}", file=sys.stderr, flush=True)
            continue
        try:
            generator(item, pair)
        except (ReferenceError, OSError) as error:
            failures.append(f"{item}: {error}")
            print(f"fern-references: {args.family} {item}: {error}", file=sys.stderr, flush=True)
    done = len(args.items or known) - len(failures)
    print(
        f"fern-references: {args.family}: {done} regenerated, {len(failures)} failed at Fern CLI {pair.cli} with fernapi/fern-python-sdk {pair.generator}"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
