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
                    probe document

Usage:
  fern-references.py list FAMILY
  fern-references.py generate FAMILY [--version V] [--cli-version C] [ITEM...]

`list` prints the family's item names, one per line. `generate` regenerates the
named items, or the whole family when none is named, at the certified pair
unless `--version`/`--cli-version` name another, writing each item where its
committed reference lives. Fern runs once at a time, in a scratch workspace
outside any checkout (so it stamps no `originGitCommit`). Quiet on success
apart from one summary line; a failed item names its log and the rest still run.

Exit status: 0 when every item listed or regenerated; 1 when an item failed
(each named on stderr) or an input it reads is malformed; 2 on a usage error.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import http.server
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from collections.abc import Callable, Generator
from dataclasses import dataclass
from pathlib import Path

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
PINNED_LOG = ".pinned-fern.log"
DOCUMENT_SUFFIXES = (".yml", ".yaml", ".json")
REMOTE_URL = "@REMOTE_URL@"
LOGS = Path(".local/fern-references")
FAMILIES = (
    "corpus",
    "overlays",
    "handwritten",
    "measurements",
    "probes",
    "authored-probes",
    "refusals",
    "departure-evidence",
)
DEPARTURE_EVIDENCE = Path("docs/departures/evidence")
OVERLAY_KINDS = {"expected-literals": ("--enum-type", "literals"), "expected-default-max-retries": None}


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


VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?")


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


def fern(argv: list[str], workspace: Path, env: dict[str, str]) -> tuple[str, str]:
    if shutil.which(argv[0]) is None:
        raise ReferenceError(f"`{argv[0]}` is not on PATH; run `just setup-fern` (it installs the Fern CLI)")
    run = subprocess.run(argv, cwd=workspace, env=env, capture_output=True, text=True, errors="replace", check=False)
    return str(run.returncode), run.stdout + run.stderr


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
    if client_class_name is not None and not (isinstance(client_class_name, str) and client_class_name.isidentifier()):
        raise ReferenceError(f"{rel(path)}: client_class_name {client_class_name!r} is no Python class name")
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


def rewrite_evidence(path: Path, pair: Pair, digest: str) -> None:
    """Restate an `evidence.toml`'s versions and digest, leaving every other line."""
    text = path.read_text(encoding="utf-8")
    for key, value in (("fern_cli_version", pair.cli), ("fern_python_sdk_version", pair.generator), ("digest", digest)):
        text, count = re.subn(rf'(?m)^{key} = "[^"]*"$', f'{key} = "{value}"', text, count=1)
        if count != 1:
            raise ReferenceError(f"{rel(path)} has no `{key}` line to restate")
    path.write_text(text, encoding="utf-8", newline="\n")


def restate_evidence_note(path: Path, pair: Pair, digest: str) -> None:
    """Restate a measurement case's `evidence.md` provenance: the pair that
    generated its tree and the tree's `Canonical tree SHA-256`."""
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"Fern CLI [0-9]+\.[0-9]+\.[0-9]+", f"Fern CLI {pair.cli}", text)
    text = re.sub(r"(fernapi/fern-python-sdk`?:? )[0-9]+\.[0-9]+\.[0-9]+", rf"\g<1>{pair.generator}", text)
    text = re.sub(r"(Canonical tree SHA-256: `)[0-9a-f]{64}(`)", rf"\g<1>{digest}\g<2>", text)
    path.write_text(text, encoding="utf-8", newline="\n")


def read_tsv(path: Path, header: tuple[str, ...]) -> list[dict[str, str]]:
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    if not lines or tuple(lines[0].split("\t")) != header:
        raise SystemExit(f"fern-references: {path} must open with the header {' '.join(header)}")
    return [dict(zip(header, line.split("\t"), strict=True)) for line in lines[1:] if line]


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


def flat_goldens() -> dict[str, str]:
    """`flat-goldens.txt`'s rows: fixture to the fixture whose spec it uses."""
    declared: dict[str, str] = {}
    for line in (ROOT / FIXTURES / "flat-goldens.txt").read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            fixture, _, spec = line.partition("|")
            declared[fixture] = spec or fixture
    return declared


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


def run_script(argv: list[str], log: Path, pair: Pair) -> None:
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
    if result.returncode != 0:
        raise ReferenceError(
            f"`{' '.join(Path(a).name if i == 0 else a for i, a in enumerate(argv))}` exited {result.returncode}; see {rel(log)}"
        )


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


def generate_overlay(item: str, pair: Pair) -> None:
    fixture, _, kind = item.partition("/")
    golden = ROOT / FIXTURES / fixture / kind
    if kind not in OVERLAY_KINDS or not (golden / OVERLAY_MANIFEST).is_file():
        raise ReferenceError(f"{item} is no committed overlay; `list overlays` names the family")
    setting = OVERLAY_KINDS[kind]
    if setting is None:
        manifest = json.loads((golden / OVERLAY_MANIFEST).read_text(encoding="utf-8"))
        retries = manifest.get("default_max_retries") if isinstance(manifest, dict) else None
        if not isinstance(retries, int) or isinstance(retries, bool) or retries < 0:
            raise ReferenceError(
                f"{rel(golden / OVERLAY_MANIFEST)}: default_max_retries must be a non-negative integer, not {retries!r}"
            )
        setting = ("--default-max-retries", str(retries))
    run_script(
        [str(ROOT / "tools/fern-goldens/fern-overlay-goldens.sh"), "--jobs", "1", *setting, fixture],
        ROOT / LOGS / "overlays" / f"{fixture}.{kind}.log",
        pair,
    )


def list_handwritten() -> list[str]:
    return sorted(path.parent.name for path in (ROOT / HANDWRITTEN).glob("*/evidence.toml"))


def generate_handwritten(item: str, pair: Pair) -> None:
    fixture = ROOT / HANDWRITTEN / item
    evidence = fixture / "evidence.toml"
    if not evidence.is_file() or not (fixture / "openapi.yml").is_file():
        raise ReferenceError(f"{item} is no hand-written fixture; `list handwritten` names the family")
    match = re.search(r"(?m)^audiences = \[([^\]]*)\]", evidence.read_text(encoding="utf-8"))
    audiences = tuple(re.findall(r'"([^"]+)"', match.group(1))) if match else ()
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


ENUM_TYPES = ("python-enums", "literals")
LAYOUTS = ("packaged", "flat")


@dataclass(frozen=True)
class MeasurementCase:
    """One `cases.tsv` row: the document a case generates from, its enum mode and
    layout, and the overlay it reduces to (`-` for a complete tree)."""

    name: str
    document: Path
    enum_type: str
    layout: str
    overlay: str


def cases() -> dict[str, MeasurementCase]:
    """`cases.tsv`'s rows, each held to the enum modes and layouts a case may name."""
    found = {}
    for row in read_tsv(CASES, CASES_HEADER):
        if row["enum_type"] not in ENUM_TYPES or row["layout"] not in LAYOUTS:
            raise ReferenceError(
                f"{CASES} row {row['case']}: enum_type is one of {', '.join(ENUM_TYPES)} "
                f"and layout one of {', '.join(LAYOUTS)}"
            )
        found[row["case"]] = MeasurementCase(
            row["case"], ROOT / row["document"], row["enum_type"], row["layout"], row["overlay"]
        )
    return found


PARAMETER_LITERALS = MEASUREMENTS / "parameter-literals"


def parameter_literal_cases() -> list[str]:
    return sorted(json.loads((ROOT / PARAMETER_LITERALS / "certified-trees.json").read_text(encoding="utf-8")))


REFUSAL_LOG = ".fern.log"
PINNED_RUN = "measurement.json"


def refusal_logs() -> dict[str, tuple[Path, Path]]:
    """`<group>/<case>/<stem>` -> (its `<stem>.fern.log`, the `<stem>.openapi.*`
    document beside it): a measurement whose committed reference is Fern's
    refusal of that document, as Fern printed it."""
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
        if document is not None:
            found[rel(log.parent / stem)[len(str(MEASUREMENTS)) + 1 :]] = (log, document)
    return found


@dataclass(frozen=True)
class PinnedRun:
    """A measurement recording one pinned run over its own probe: the case
    directory, its `measurement.json` and the probe that record names."""

    case: Path
    record: dict[str, object]
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
    return PinnedRun(case, record, target)


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
    case, record, probe = run_record.case, dict(run_record.record), run_record.probe
    with run_fern(probe, pair, check=True) as run:
        if run.generate_exit != "0" or run.tree is None:
            raise ReferenceError(f"fern generate exited {run.generate_exit} with no tree")
        (case / "fern.log").write_text(fern_log(pair, run), encoding="utf-8", newline="\n")
        shutil.copyfile(run.tree / "src" / "fern" / "raw_client.py", case / "fern-raw_client.py.txt")
        python_files = sum(1 for path in run.tree.rglob("*.py") if path.is_file())
        record.update(
            {
                "check_diagnostic": first_diagnostic(run.check_log) or "All checks passed",
                "check_exit": run.check_exit,
                "check_log_sha256": hashlib.sha256(run.check_log.encode("utf-8")).hexdigest(),
                "fern_cli": pair.cli,
                "generate_exit": run.generate_exit,
                "generate_log_sha256": hashlib.sha256(run.generate_log.encode("utf-8")).hexdigest(),
                "generate_python_files": python_files,
                "generator": pair.generator,
                "sha256": hashlib.sha256(probe.read_bytes()).hexdigest(),
            }
        )
        record.pop("generate_diagnostic", None)
        record_path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def generate_parameter_literal(case: str, pair: Pair) -> None:
    """Re-measure a parameter-literals claim: Fern's literals tree for a
    hand-written fixture (client `FernApi`, extra fields `allow`) is its
    python-enums tree less `core/enum.py`, with only `.fern/metadata.json`
    differing. Records that metadata and the tree's digest, or fails naming the
    first file the claim no longer holds for."""
    fixture = ROOT / HANDWRITTEN / case
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
        diagnostic = first_diagnostic(run.generate_log)
        if not diagnostic:
            raise ReferenceError(
                f"fern generate exited {run.generate_exit} printing no diagnostic this tool recognises:\n"
                f"{run.generate_log.strip()[-2000:]}"
            )
        write_refusal_record(record, pair, run.generate_exit, diagnostic)


def generate_measurement(item: str, pair: Pair) -> None:
    if item.startswith("parameter-literals/"):
        generate_parameter_literal(item.removeprefix("parameter-literals/"), pair)
        return
    if item in (logs := refusal_logs()):
        remeasure_refusal_log(item, *logs[item], pair)
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
    generated_tree(row.document, destination, pair, enum_type=row.enum_type, layout=row.layout)
    if row.overlay != "-":
        label, _, base = row.overlay.partition(":")
        provenance: dict[str, object] = {
            "fern_python_sdk_version": pair.generator,
            "fern_cli_version": pair.cli,
            "enum_type": row.enum_type,
            "base": label,
        }
        base_tree = None if base == "-" else ROOT / base
        if label == "fern-expected":
            # The digest of the complete tree Fern wrote, which the gate rebuilds
            # from the base and the overlay before comparing.
            provenance["digest"] = contract_digest(destination)
        reduce_overlay(destination, base_tree, provenance)
    evidence = destination.parent / "evidence.toml"
    if evidence.is_file() and "digest = " in evidence.read_text(encoding="utf-8"):
        rewrite_evidence(evidence, pair, contract_digest(destination))
    note = destination.parent / "evidence.md"
    if note.is_file():
        restate_evidence_note(note, pair, contract_digest(destination))


def manifest_rows() -> list[dict[str, str]]:
    return read_tsv(MANIFEST, ("key", "form", "verdict", "artifact", "control", "digest"))


def list_probes() -> list[str]:
    names = set()
    for row in manifest_rows():
        names.add(row["key"])
        if row["control"] != "—":
            names.add(row["control"])
    return sorted(names)


def first_diagnostic(log: str) -> str:
    """The first error Fern itself printed: an `issue:` line of `fern check`'s
    report, the line after `[error]` in the generation's, or the exception a
    crashed generator raised (`KeyError: …`)."""
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


def generate_probe(item: str, pair: Pair) -> None:
    document = ROOT / PROBES / f"{item}.yml"
    if not document.is_file():
        raise ReferenceError(f"no probe document {rel(document)}; `list probes` names the family")
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
            diagnostic = first_diagnostic(run.generate_log)
            if not diagnostic:
                log = ROOT / LOGS / "probes" / f"{item}.generate.log"
                log.parent.mkdir(parents=True, exist_ok=True)
                log.write_text(run.generate_log, encoding="utf-8", newline="\n")
                raise ReferenceError(
                    f"fern generate exited {run.generate_exit} printing no diagnostic this tool recognises; "
                    f"read {rel(log)} and extend first_diagnostic"
                )
            write_refusal_record(record, pair, run.generate_exit, diagnostic)
            if tree.exists():
                shutil.rmtree(tree)
            artifact, digest = record, hashlib.sha256(record.read_bytes()).hexdigest()
    new, old = rel(artifact), rel(tree if artifact == record else record)
    rows = manifest_rows()
    flipped = []
    for row in rows:
        if row["artifact"] == new:
            row["digest"] = digest
        elif row["artifact"] == old or (row["control"] == item and artifact == record):
            flipped.append(row["key"])
            if row["artifact"] == old:
                row["artifact"], row["digest"] = new, digest
    header = ("key", "form", "verdict", "artifact", "control", "digest")
    (ROOT / MANIFEST).write_text(
        "\t".join(header) + "\n" + "".join("\t".join(row[c] for c in header) + "\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )
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
    return sorted(path.parent.name for path in (ROOT / AUTHORED).glob("*/openapi.yml"))


def generate_authored(item: str, pair: Pair) -> None:
    case = ROOT / AUTHORED / item
    if not (case / "openapi.yml").is_file():
        raise ReferenceError(f"{item} is no authored probe; `list authored-probes` names the family")
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
    return [line.split("\t")[index] for line in lines[1:] if line]


def list_refusals() -> list[str]:
    classes = registry_column(REGISTRY / "classes.tsv", "class")
    findings = [f"findings/{name}" for name in registry_column(REGISTRY / "findings.tsv", "finding")]
    evidence = [
        rel(log)[len(str(REGISTRY)) + 1 : -len(PINNED_LOG)]
        for log in sorted((ROOT / REGISTRY).glob(f"*/evidence/*{PINNED_LOG}"))
        if evidence_document(log) is not None
    ]
    return sorted(classes) + findings + evidence


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
        run_script(["python3", tool, "probe", "--jobs", "1", item], logs / f"probe.{item}.log", pair)


def list_departure_evidence() -> list[str]:
    return sorted(path.parent.name for path in (ROOT / DEPARTURE_EVIDENCE).glob("*/fern-reference.json"))


def generate_departure_evidence(item: str, pair: Pair) -> None:
    """A departure's evidence tree: Fern's output for the note's own document,
    under the settings its `fern-reference.json` records."""
    case = ROOT / DEPARTURE_EVIDENCE / item
    settings_path = case / "fern-reference.json"
    if not settings_path.is_file():
        raise ReferenceError(f"{item} has no fern-reference.json; `list departure-evidence` names the family")
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
    with run_fern(case / "openapi.yml", pair, enum_type=enum_type, layout=layout, organization=organization) as run:
        if run.generate_exit != "0" or run.tree is None:
            raise ReferenceError(f"fern generate exited {run.generate_exit} with no tree")
        stage = Path(tempfile.mkdtemp(prefix=".fern-references.", dir=case))
        try:
            strip_into(run.tree, stage / "fern-reference")
            install(stage / "fern-reference", case / "fern-reference")
        finally:
            shutil.rmtree(stage, ignore_errors=True)


FAMILY: dict[str, tuple[Callable[[], list[str]], Callable[[str, Pair], None]]] = {
    "corpus": (list_corpus, generate_corpus),
    "overlays": (list_overlays, generate_overlay),
    "handwritten": (list_handwritten, generate_handwritten),
    "measurements": (list_measurements, generate_measurement),
    "probes": (list_probes, generate_probe),
    "authored-probes": (list_authored, generate_authored),
    "refusals": (list_refusals, generate_refusal),
    "departure-evidence": (list_departure_evidence, generate_departure_evidence),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="fern-references.py", description=__doc__.split("\n", 1)[0])
    commands = parser.add_subparsers(dest="command", required=True)
    listing = commands.add_parser("list", help="print the family's item names")
    listing.add_argument("family", choices=FAMILIES)
    generate = commands.add_parser("generate", help="regenerate the named items, or the whole family")
    generate.add_argument("family", choices=FAMILIES)
    generate.add_argument("--version", help="fern-python-sdk version (default: the certified pair's)")
    generate.add_argument("--cli-version", help="Fern CLI version (default: the certified pair's)")
    generate.add_argument("items", nargs="*")
    args = parser.parse_args(argv)
    lister, generator = FAMILY[args.family]
    known = lister()
    if args.command == "list":
        sys.stdout.write("".join(f"{item}\n" for item in known))
        return 0
    certified = certified_pair()
    pair = Pair(cli=args.cli_version or certified.cli, generator=args.version or certified.generator)
    for value in (pair.cli, pair.generator):
        if not VERSION.fullmatch(value):
            raise SystemExit(f"fern-references: invalid Fern version {value!r}; use an exact semantic version")
    unknown = [item for item in args.items if item not in known]
    if unknown:
        raise SystemExit(
            f"fern-references: no {args.family} item {', '.join(unknown)}; "
            f"`fern-references.py list {args.family}` names the family"
        )
    failures = []
    for item in args.items or known:
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
