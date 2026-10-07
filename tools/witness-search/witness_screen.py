#!/usr/bin/env python3
"""The one measured screening stage a witness candidate's three screens come from.

A candidate owes three screens before it can stand as a witness: its licence
(the corpus licence rule, `docs/corpus-licensing.md`), its ref (bytes read at an
immutable commit) and Fern (the pinned CLI and generator accepting it). Both
witness-search families take them here — `tools/surface-census/golden-reach-search.py
screen` for an arm search and this script's own `screen` for the legacy
`witness-search-<source>/` ledgers — and nowhere else, so every outcome comes
from a run rather than from a caller's sentence:

* **ref** — the document is fetched at ``<repository>@<commit>`` through the
  guarded acquirer's exact-commit raw route (`tools/witness-search/witness-search-github.py`,
  under `tools/witness-search/rate_limit_guard.py`'s pacing); it passes when the commit is a
  full 40-hex SHA, the fetch answers 200, and, where the caller's pin names one,
  the bytes carry that SHA-256.
* **licence** — the fetched document's own ``info.license`` and the repository's
  licence file at the same commit, read against the admissible set the rule's
  canonical enumeration names. A grant the reading cannot recognise is refused,
  never guessed; a caller may refuse a candidate the reading would pass (a
  third-party copy, say) with ``--licence-refusal``, which is recorded as that
  judgement beside the reading, and may never pass one the reading refuses.
* **fern** — `fern check` at the corpus's pinned CLI, then the generation
  `tools/fern-goldens/generate-fern-fixture.sh` runs where that exits 0. It runs only once
  the licence and ref screens pass: an earlier refusal records it ``not-run``.

Each screen is filed as ``{outcome, exit, pins, log, log_sha256}``: the exit
status of what it ran, the pins it ran at, and its redacted log, committed
under the evidence directory's ``screens/`` and named by its digest.
[`measured_failures`] is the one check of that record; a success claim missing
any part of it is refused, naming the part, and a Fern outcome that is not what
its own recorded run yields is refused as unmeasured.

A screen row filed before this stage landed carries no such record. It stays
readable and is **historical**: no live completeness decision reads it as a
measurement. A row dated at or after [`MEASURED_SINCE`] without one is refused.

`screen` exits 0 when it filed the row — a rejected candidate is filed too, so
0 says the screens were taken and recorded, not that they passed; 1 when it
refused to file (an unknown key, a path outside the repository, a record that
is not whole, a success claim the outcomes do not support, a Fern timeout); 2
on a usage error.
"""

from __future__ import annotations

import argparse
import datetime
import functools
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.parse
from collections import Counter
from collections.abc import Callable
from pathlib import Path, PurePosixPath
from types import ModuleType
from typing import Any

REPO = Path(__file__).resolve().parents[2]
RULE = REPO / "docs" / "corpus-licensing.md"
RULE_MARKER = "corpus-licence-set:"
# The stage's identity as every committed screen records it: the path it was
# run from when those screens were measured. It names the stage; the file now
# lives in tools/witness-search/.
STAGE = "scripts/witness_screen.py"
SCREENS = ("licence", "ref", "fern")
# A screen row dated at or after this instant was filed after the measured stage
# landed, so it owes the measured record; one before it is historical.
MEASURED_SINCE = "2026-10-02T00:00:00+00:00"
LOG_DIR = "screens"
LICENCE_FILES = ("LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md", "COPYING")
# How much of a licence file is read for its grant: its title and opening
# paragraph, never a later mention of some other licence.
LICENCE_HEAD_LINES = 30
SHA = re.compile(r"[0-9a-f]{64}")
COMMIT = re.compile(r"[0-9a-f]{40}")
REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")
# The legacy witness-search ledgers this stage files screens into: every
# `witness-search-<source>/` that carries a `screens.jsonl`, which
# `tools/witness-search/tests/witness_screen_test.py` reconciles against the committed tree.
LEGACY_SOURCES = ("apis.guru", "jentic", "github-code-search", "github-publisher-trees", "sourcegraph")

Fetch = Callable[[str, str], tuple[int, bytes]]


def fail(message: str) -> None:
    raise SystemExit(f"witness-screen: {message}")


def _load(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(f"cannot load {path.relative_to(REPO)}; restore it from git (`git checkout -- {path.relative_to(REPO)}`)")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@functools.lru_cache(maxsize=1)
def corpus_fern_pins() -> tuple[str, str, str, dict[str, Any]]:
    """The Fern CLI, generator, generator version and config the registered goldens were generated at.

    Read off each golden's own `.fern/metadata.json`, the corpus's provenance, so
    a screen is taken at the corpus's pins without restating them; the pair most
    goldens record is the pin (a synthetic fixture may record another).
    """
    counts: Counter[str] = Counter()
    for path in sorted((REPO / "tests" / "fixtures").glob("*/expected/.fern/metadata.json")):
        remedy = f"restore {path.relative_to(REPO)} from git (it is the golden's Fern provenance)"
        try:
            meta = json.loads(path.read_text(encoding="utf-8"))
        except ValueError as error:
            fail(f"{path.relative_to(REPO)} is not JSON ({error}); {remedy}")
        if not isinstance(meta, dict):
            fail(f"{path.relative_to(REPO)} is not a JSON object; {remedy}")
        pins = [meta.get("cliVersion"), meta.get("generatorName"), meta.get("generatorVersion")]
        # A synthetic fixture's record may carry no generatorConfig; one that is
        # there is the mapping generators.yml is written from.
        config = meta.get("generatorConfig", {})
        if not all(isinstance(pin, str) and pin for pin in pins) or not isinstance(config, dict):
            fail(f"{path.relative_to(REPO)} lacks a non-empty cliVersion, generatorName and generatorVersion, "
                 f"or carries a generatorConfig that is no mapping; {remedy}")
        counts[json.dumps([*pins, config], sort_keys=True)] += 1
    if not counts:
        fail("no golden records its Fern pins in tests/fixtures/*/expected/.fern/metadata.json; "
             "restore the corpus goldens from git")
    cli, name, version, config = json.loads(counts.most_common(1)[0][0])
    return cli, name, version, config


def _yaml_block(value: Any, indent: int) -> list[str]:
    """A generator config mapping as the block YAML generate-fern-fixture.sh writes."""
    lines = []
    for key, item in value.items():
        if isinstance(item, dict):
            lines += [" " * indent + f"{key}:"] + _yaml_block(item, indent + 2)
        else:
            lines.append(" " * indent + f"{key}: {item}")
    return lines


def fern_workspace_files() -> tuple[str, str]:
    """`fern.config.json` and `generators.yml` as generate-fern-fixture.sh scaffolds them for a document.

    Its install into `tests/fixtures/` is left out: a screen reads Fern's verdict
    and never writes a golden. `tools/surface-census/tests/golden_reach_test.py` holds the YAML to
    that script's own heredoc.
    """
    cli, name, version, config = corpus_fern_pins()
    generators = [
        "api:", "  path: openapi/openapi.yml", "groups:", "  python-sdk:", "    generators:",
        f"      - name: {name}", f"        version: {version}", "        config:",
        *_yaml_block(config, 10),
        "        output:", "          location: local-file-system", "          path: ../generated/python",
    ]
    return json.dumps({"organization": "fern", "version": cli}) + "\n", "\n".join(generators) + "\n"


def fern_label() -> str:
    cli, _name, version, _config = corpus_fern_pins()
    return f"Fern CLI {cli} / python-sdk {version}"


UNPARSED = re.compile(r"Unexpected error|Failed to (resolve|parse)", re.I)
ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")
SECRET_NAME = re.compile(r"TOKEN|SECRET|PASSWORD|API_KEY|AUTH", re.I)


def redact(text: str, *paths: Path) -> str:
    """A log fit to commit: no terminal escapes, no secret's value, no host path.

    Every environment value named like a credential is replaced wherever it
    appears, as are the scratch paths a run worked in and the home directory.
    """
    text = ANSI.sub("", text)
    for name, value in os.environ.items():
        if SECRET_NAME.search(name) and len(value) >= 8:
            text = text.replace(value, f"[{name} redacted]")
    for path in paths:
        text = text.replace(str(path), "<scratch>")
    home = os.path.expanduser("~")
    if len(home) > 1:
        text = text.replace(home, "~")
    return text


def _fern_run(command: list[str], workspace: Path, timeout: int) -> tuple[str, str]:
    """One Fern command in a scratch workspace: its exit status (or `timeout`) and its output."""
    env = dict(os.environ, FERN_TOKEN=os.environ.get("FERN_TOKEN", "preview-only-no-publish"),
               CI="true", GITHUB_ACTIONS="true")
    try:
        run = subprocess.run(command, cwd=workspace, env=env, capture_output=True, text=True,
                             errors="replace", timeout=timeout)
    except subprocess.TimeoutExpired as expired:
        out = expired.stdout or ""
        return "timeout", out if isinstance(out, str) else out.decode("utf-8", "replace")
    return str(run.returncode), run.stdout + run.stderr


def fern_diagnostic(output: str) -> str:
    """The first thing Fern said was wrong, as it printed it, on one line and without `; `."""
    lines = [line.strip() for line in output.splitlines() if line.strip() and not line.startswith("::")]
    summary = next((re.sub(r" in [\d.]+ seconds\.?$", ".", line)
                    for line in lines if re.match(r"Found \d+ errors?", line)), "")
    first = next((line[len("issue: "):] for line in lines if line.startswith("issue: ")), "")
    if not first:
        first = next((line for line in lines if UNPARSED.search(line) or re.search(r"\berror\b", line, re.I)
                      and "deprecated" not in line), lines[-1] if lines else "no output")
    text = f"{summary} First: {first}" if summary else first
    # A screen cell quotes each result in backticks and joins them with `; `.
    return text.replace("; ", ", ").replace("`", "'")[:400]


def fern_screen_document(document: Path, scratch: Path, timeout: int) -> dict[str, Any]:
    """Fern's measured verdict on one document: `fern check`, then a generation where it passes.

    Each log digest is taken over the redacted log; the logs themselves ride
    along under `logs` for a caller that commits them, and are no part of the row.
    """
    digest = hashlib.sha256(document.read_bytes()).hexdigest()
    workspace = scratch / digest / "fern"
    (workspace / "openapi").mkdir(parents=True, exist_ok=True)
    (workspace / "openapi" / "openapi.yml").write_bytes(document.read_bytes())
    config, generators = fern_workspace_files()
    (workspace / "fern.config.json").write_text(config, encoding="utf-8")
    (workspace / "generators.yml").write_text(generators, encoding="utf-8")
    cli, _name, version, _config = corpus_fern_pins()
    row: dict[str, Any] = {"sha256": digest, "fern_cli": cli, "generator": version}
    status, output = _fern_run(["fern", "check"], workspace, timeout)
    check_log = redact(output, scratch)
    # Diagnostics are read off the redacted log: they are committed in the row too.
    row.update(check_exit=status, check_log_sha256=hashlib.sha256(check_log.encode()).hexdigest(),
               check_diagnostic=fern_diagnostic(check_log))
    logs = {"check": check_log}
    if status == "0":
        preview = scratch / digest / "preview"
        status, output = _fern_run(["fern", "generate", "--group", "python-sdk", "--local", "--preview",
                                    "--output", str(preview), "--force"], workspace, timeout)
        package = preview / "fern-python-sdk"
        files = sum(1 for path in package.rglob("*.py")) if package.is_dir() else 0
        logs["generate"] = redact(output, scratch)
        unparsed = next((line.strip() for line in logs["generate"].splitlines() if UNPARSED.search(line)), "")
        row.update(generate_exit=status, generate_log_sha256=hashlib.sha256(logs["generate"].encode()).hexdigest(),
                   generate_python_files=files,
                   generate_diagnostic=(unparsed or fern_diagnostic(logs["generate"])).replace("; ", ", ")
                   .replace("`", "'")[:400])
    row["logs"] = logs
    return row


def fern_verdict(row: dict[str, Any]) -> str | None:
    """A screen's `fern` result from a measured run, or None when the run did not finish."""
    check = row["check_exit"]
    if check == "timeout" or row.get("generate_exit") == "timeout":
        return None
    if check != "0":
        return f"failed: {fern_label()} fern check exit {check}: {row['check_diagnostic']}"
    generated = row["generate_exit"]
    if generated != "0":
        return f"failed: {fern_label()} fern generate exit {generated} after fern check exit 0: " \
               f"{row['generate_diagnostic']}"
    if UNPARSED.search(row["generate_diagnostic"]) or row["generate_python_files"] == 0:
        return (f"failed: {fern_label()} fern generate exit 0 over an unparsed document, "
                f"{row['generate_python_files']} Python files: {row['generate_diagnostic']}")
    return "passed"


@functools.lru_cache(maxsize=None)
def admissible_families(rule: Path = RULE) -> tuple[str, ...]:
    """The licence names the rule's canonical enumeration admits, in its own order.

    `docs/corpus-licensing.md` is the only statement of the rule, so its marked
    `Admissible` sentence is parsed here rather than copied: a licence it stops
    naming stops passing.
    """
    text = rule.read_text(encoding="utf-8")
    if RULE_MARKER not in text:
        fail(f"{rule.relative_to(REPO)} carries no `{RULE_MARKER}` marker; restore the rule from git")
    sentence = text.split(RULE_MARKER, 1)[1].split("**Not admissible", 1)[0]
    listed = sentence.split(":", 1)[1].split("and other grants", 1)[0] if ":" in sentence else ""
    families = tuple(re.sub(r"^the | family$", "", name.strip()) for name in listed.replace("\n", " ").split(",")
                     if name.strip())
    if not families:
        fail(f"{rule.relative_to(REPO)}'s admissible sentence names no licence; restore the rule from git")
    return families


# Each family the rule names, as an SPDX identifier, a licence's name, or the
# opening words of its text spell it. Most specific first, so `LGPL` is not read
# as `GPL` and `CC-BY-SA` not as `CC-BY`.
RECOGNISED = (
    ("AGPL", r"\bAGPL|AFFERO GENERAL PUBLIC"),
    ("LGPL", r"\bLGPL|LESSER GENERAL PUBLIC|LIBRARY GENERAL PUBLIC"),
    ("GPL", r"\bGPL|GNU GENERAL PUBLIC"),
    ("Apache-2.0", r"\bAPACHE\b.{0,40}?\b2(?:\.0)?\b"),
    ("MIT", r"\bMIT\b|PERMISSION IS HEREBY GRANTED, FREE OF CHARGE"),
    ("BSD", r"\bBSD\b|REDISTRIBUTION AND USE IN SOURCE AND BINARY FORMS"),
    ("CC0", r"\bCC0\b|CC-ZERO|CREATIVE COMMONS ZERO|CC0 1\.0 UNIVERSAL"),
    ("MPL", r"\bMPL\b|MOZILLA PUBLIC LICEN[CS]E"),
    ("EPL", r"\bEPL\b|ECLIPSE PUBLIC LICEN[CS]E"),
    ("CC-BY-SA", r"\bCC[- ]BY[- ]SA\b|ATTRIBUTION[- ]SHAREALIKE"),
    ("CC-BY-ND", r"\bCC[- ]BY[- ]ND\b|ATTRIBUTION[- ]NODERIVATIVES"),
    ("CC-BY", r"\bCC[- ]BY\b|CREATIVE COMMONS ATTRIBUTION"),
)
# What the rule refuses whatever else the text says: no assertion at all, or a
# grant whose redistribution is conditioned on terms the repository cannot meet.
WITHHELD = re.compile(r"NOASSERTION|NON-?COMMERCIAL|\bCC[- ]BY(?:[- ]SA|[- ]ND)?[- ]NC\b|PROPRIETARY|ALL RIGHTS RESERVED")


def clean(outcome: str) -> str:
    """An outcome fit for a records cell: one line, no backtick, no `; ` (the cell's own separators)."""
    return " ".join(outcome.split()).replace("`", "'").replace("; ", ", ")


def recognise(text: str) -> str | None:
    """The admissible family `text` names, or None when it names none the rule lists."""
    # A licence file's title is often centred: compare words, not layout.
    upper = " ".join(text.upper().split())
    if WITHHELD.search(upper):
        return None
    for family, pattern in RECOGNISED:
        if re.search(pattern, upper):
            return family
    return None


# What `document_licence` answers for an `info.license` that is there but is no
# License Object: a refusal of its own, never a fallback to the licence file.
MALFORMED = object()
LICENCE_FIELDS = ("identifier", "name", "url")


def document_licence(data: bytes, scratch: Path) -> str | None | object:
    """The document's own `info.license` as one line, `""` when it declares none, None when
    unreadable, and `MALFORMED` when it declares one that is no License Object."""
    path = scratch / "licence-read" / f"{hashlib.sha256(data).hexdigest()}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    census = _load("openapi_surface_census_screen", REPO / "tools" / "surface-census" / "openapi-surface-census.py")
    try:
        document = census.load_document(path)
    except Exception:  # the census's own parse refusal, whatever its type
        return None
    info = document.get("info") if isinstance(document, dict) else None
    if not isinstance(info, dict) or "license" not in info:
        return ""
    licence = info["license"]
    if (not isinstance(licence, dict)
            or any(field in licence and not isinstance(licence[field], str) for field in LICENCE_FIELDS)
            or not any(isinstance(licence.get(field), str) and licence[field].strip() for field in LICENCE_FIELDS)):
        return MALFORMED
    return " / ".join(licence[field] for field in LICENCE_FIELDS
                      if isinstance(licence.get(field), str) and licence[field].strip())


def licence_screen(document_text: str | None | object, files: list[tuple[str, int, bytes]],
                   refusal: str = "") -> tuple[str, dict[str, Any], str]:
    """The licence outcome, its pins and its log, from the two readings the rule names."""
    malformed = document_text is MALFORMED
    if malformed:
        document_text = None
    families = admissible_families()
    file_name, file_status, file_bytes = next(((n, s, b) for n, s, b in files if s == 200), ("", 0, b""))
    head = "\n".join(line for line in file_bytes.decode("utf-8", "replace").splitlines() if line.strip())
    head = "\n".join(head.splitlines()[:LICENCE_HEAD_LINES])
    doc_family = recognise(document_text) if document_text else None
    file_family = recognise(head) if file_name else None
    if malformed:
        outcome = ("failed: info.license is there but is no License Object (a mapping naming the grant "
                   "in a string identifier, name or url)")
    elif document_text is None:
        outcome = "failed: the document could not be read for its info.license"
    elif document_text:
        outcome = (f"passed: info.license '{document_text}' reads as {doc_family}, which the corpus rule admits"
                   if doc_family in families else
                   f"failed: info.license '{document_text}' names no grant the corpus rule admits")
    elif file_name:
        outcome = (f"passed: no info.license; {file_name} at the pinned commit reads as {file_family}, "
                   "which the corpus rule admits" if file_family in families else
                   f"failed: no info.license, and {file_name} at the pinned commit names no grant "
                   "the corpus rule admits")
    else:
        outcome = "failed: grants nothing — no info.license and no licence file at the pinned commit"
    judgement = ""
    if refusal:
        judgement = refusal
        outcome = f"failed: {refusal}"
    outcome = clean(outcome)
    pins = {
        "rule": RULE.relative_to(REPO).as_posix(),
        "rule_sha256": hashlib.sha256(RULE.read_bytes()).hexdigest(),
        "admissible": list(families),
        "document_licence": document_text,
        "document_family": doc_family,
        "licence_file": file_name,
        "licence_file_sha256": hashlib.sha256(file_bytes).hexdigest() if file_name else "",
        "licence_file_family": file_family,
    }
    if judgement:
        pins["judgement"] = judgement
    log = "\n".join([
        f"rule {pins['rule']} sha256 {pins['rule_sha256']}: admits {', '.join(families)}",
        f"info.license: {'(malformed)' if malformed else repr(document_text)} -> {doc_family}",
        *(f"GET {name}: HTTP {status}" for name, status, _data in files),
        f"licence file {file_name or '(none)'} -> {file_family}",
        *([f"--- {file_name} (first {LICENCE_HEAD_LINES} non-blank lines) ---", head] if file_name else []),
        *([f"caller judgement: {judgement}"] if judgement else []),
        f"outcome: {outcome}",
    ]) + "\n"
    exit_status = " ".join(f"{name}:{status}" for name, status, _data in files) or "none"
    return outcome, {"exit": exit_status, "pins": pins}, log


def repository_path(path: str) -> bool:
    """Whether `path` names a file inside a repository: relative, `/`-separated, no `..`."""
    parts = PurePosixPath(path).parts
    return bool(parts) and not PurePosixPath(path).is_absolute() and "\\" not in path \
        and ".." not in parts and "." not in path.split("/")


def passed(outcome: str) -> bool:
    """Whether a screen outcome reads as a pass: exactly `passed`, or `passed: <reason>`."""
    return outcome == "passed" or outcome.startswith("passed: ")


def timestamp(value: Any) -> datetime.datetime | None:
    """An ISO 8601 instant carrying its offset (`Z` included), or None when `value` is not one."""
    if not isinstance(value, str) or not value:
        return None
    try:
        stamp = datetime.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return stamp if stamp.tzinfo is not None else None


def raw_url(base: str, repository: str, commit: str, path: str) -> str:
    return f"{base.rstrip('/')}/{repository}/{commit}/{urllib.parse.quote(path)}"


def write_log(logs: Path, base: Path, sha256: str, screen: str, text: str) -> tuple[str, str]:
    """Commit one redacted log by its own digest; its path relative to `base` and that digest."""
    data = text.encode()
    digest = hashlib.sha256(data).hexdigest()
    path = logs / f"{sha256[:12]}.{screen}.{digest[:12]}.log"
    logs.mkdir(parents=True, exist_ok=True)
    # Bytes, not text: a text write turns `\n` into `\r\n` on Windows, and the
    # committed log would then no longer carry the digest recorded for it.
    path.write_bytes(data)
    return path.relative_to(base).as_posix(), digest


def measure(*, repository: str, commit: str, path: str, fetch: Fetch, raw_base: str,
            logs: Path, base: Path, expected_sha256: str = "", licence_refusal: str = "",
            timeout: int = 1800, now: str | None = None) -> dict[str, Any]:
    """Take one candidate's three screens and return the measured record.

    `fetch(url, subject)` is the guarded acquirer's exact-commit raw route; it
    answers `(status, bytes)`. Logs land in `logs`, recorded relative to `base`.
    """
    if not REPOSITORY.fullmatch(repository):
        fail(f"{repository!r} is no `<owner>/<name>` repository; pass the one the candidate was acquired from")
    if not repository_path(path):
        fail(f"{path!r} is no path inside a repository (relative, `/`-separated, no `..`); pass the "
             "document's path as the acquisition recorded it")
    url = raw_url(raw_base, repository, commit, path)
    # A ref that is no full commit SHA is mutable: the screen fails on that alone,
    # so nothing is fetched at it.
    status, data = fetch(url, f"{repository}:{path}") if COMMIT.fullmatch(commit) else (0, b"")
    sha256 = hashlib.sha256(data).hexdigest() if status == 200 else ""
    record: dict[str, Any] = {
        "stage": STAGE,
        "screened_at": now or datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
        "document": {"repository": repository, "commit": commit, "path": path,
                     "sha256": sha256, "bytes": len(data) if status == 200 else 0},
    }
    if not COMMIT.fullmatch(commit):
        ref = f"failed: '{commit}' is no full commit SHA, so the ref is mutable"
    elif status != 200:
        ref = f"failed: HTTP {status} reading {path} at {repository}@{commit}"
    elif expected_sha256 and sha256 != expected_sha256:
        ref = f"failed: the bytes at {repository}@{commit} carry sha256 {sha256}, not the pinned {expected_sha256}"
    else:
        ref = f"passed: {len(data)} bytes read at the immutable commit {commit}, sha256 {sha256}"
    ref = clean(ref)
    request = f"GET {url}\nHTTP {status}" if COMMIT.fullmatch(commit) else f"not fetched: {commit!r} is no commit SHA"
    ref_log = redact(f"{request}\n{len(data)} bytes, sha256 {sha256 or '-'}\n"
                     f"pinned sha256 {expected_sha256 or '(none)'}\noutcome: {ref}\n")
    key = sha256 or hashlib.sha256(url.encode()).hexdigest()
    log, digest = write_log(logs, base, key, "ref", ref_log)
    record["ref"] = {"outcome": ref, "exit": str(status) if COMMIT.fullmatch(commit) else "not-fetched",
                     "pins": {"repository": repository, "commit": commit, "path": path, "url": url,
                              "sha256": sha256, "expected_sha256": expected_sha256},
                     "log": log, "log_sha256": digest}
    with tempfile.TemporaryDirectory(prefix="witness-screen-") as scratch_dir:
        scratch = Path(scratch_dir)
        if status == 200:
            files = []
            for name in LICENCE_FILES:
                file_status, file_bytes = fetch(raw_url(raw_base, repository, commit, name), f"{repository}:{name}")
                files.append((name, file_status, file_bytes))
                if file_status == 200:
                    break
            outcome, section, licence_log = licence_screen(document_licence(data, scratch), files, licence_refusal)
            log, digest = write_log(logs, base, key, "licence", redact(licence_log, scratch))
            record["licence"] = {"outcome": outcome, **section, "log": log, "log_sha256": digest}
        else:
            record["licence"] = {"outcome": "not-run: the ref screen failed, so no bytes were read"}
        # The screen that refused it: the ref is read first, and a licence not run never failed.
        failed = [name for name in ("ref", "licence") if record[name]["outcome"].startswith("failed: ")]
        if failed:
            record["fern"] = {"outcome": f"not-run: the {failed[0]} screen failed"}
            return record
        document = scratch / "document"
        document.write_bytes(data)
        run = fern_screen_document(document, scratch / "fern", timeout)
    logs_text = run.pop("logs")
    verdict = fern_verdict(run)
    if verdict is None:
        discard_logs(record, base)
        fail(f"Fern timed out after {timeout}s on {repository}:{path}; nothing was filed — "
             "re-run with a longer --timeout")
    text = "".join(f"--- fern {name} (exit {run.get(f'{name}_exit')}) ---\n{body}\n" for name, body in logs_text.items())
    log, digest = write_log(logs, base, key, "fern", text)
    cli, generator, version, _config = corpus_fern_pins()
    exit_status = f"check {run['check_exit']}" + (f", generate {run['generate_exit']}" if "generate_exit" in run else "")
    record["fern"] = {"outcome": verdict, "exit": exit_status,
                      "pins": {"fern_cli": cli, "generator": generator, "generator_version": version},
                      "run": {k: v for k, v in run.items() if k not in ("fern_cli", "generator")},
                      "log": log, "log_sha256": digest}
    return record


REQUIRED_PINS = {
    "licence": ("rule", "rule_sha256", "admissible", "document_licence", "licence_file", "licence_file_sha256"),
    "ref": ("repository", "commit", "path", "sha256"),
    "fern": ("fern_cli", "generator", "generator_version"),
}


def measured_failures(record: Any, base: Path | None = None) -> list[str]:
    """Every part of a measured record that is missing or does not hold; empty means it is whole.

    Each screen that ran owes its outcome, the exit status of what it ran, its
    pins, and its redacted log's path and digest; where `base` is given the log
    must be there and carry that digest. A screen that did not run says
    `not-run: <why>`, and only after an earlier screen failed. A Fern outcome
    must be the one its own recorded run yields, at the corpus's pins.
    """
    if not isinstance(record, dict):
        return ["no measured record"]
    missing = []
    if record.get("stage") != STAGE:
        missing.append(f"the stage that measured it (`stage: {STAGE}`)")
    if timestamp(record.get("screened_at")) is None:
        missing.append("when it was measured (`screened_at`, an ISO 8601 instant with its offset)")
    document = record.get("document") if isinstance(record.get("document"), dict) else {}
    absent = [field for field in ("repository", "commit", "path") if not isinstance(document.get(field), str)
              or not document[field]]
    if not isinstance(document.get("sha256"), str) or (document["sha256"] and not SHA.fullmatch(document["sha256"])):
        absent.append("sha256")
    if absent:
        missing.append(f"the document it read ({absent} of `document`)")
    for name in SCREENS:
        section = record.get(name)
        if not isinstance(section, dict) or not isinstance(section.get("outcome"), str):
            missing.append(f"the {name} screen's outcome")
            continue
        outcome = section["outcome"]
        if outcome.startswith("not-run: "):
            earlier = SCREENS[:SCREENS.index(name)] if name != "licence" else ("ref",)
            if not any(isinstance(record.get(e), dict)
                       and str(record[e].get("outcome", "")).startswith("failed: ") for e in earlier):
                missing.append(f"the {name} screen's run: it reads `not-run` with no earlier screen failed")
            continue
        if not (passed(outcome) or outcome.startswith("failed: ")):
            missing.append(f"a {name} outcome reading `passed` or `failed: <reason>`, not {outcome!r}")
        if not isinstance(section.get("exit"), str) or not section["exit"]:
            missing.append(f"the {name} screen's exit status")
        pins = section.get("pins") if isinstance(section.get("pins"), dict) else {}
        absent = [pin for pin in REQUIRED_PINS[name] if pin not in pins]
        if absent:
            missing.append(f"the {name} screen's pins {absent}")
        log, digest = section.get("log"), section.get("log_sha256")
        if not isinstance(log, str) or not log or not isinstance(digest, str) or not SHA.fullmatch(digest):
            missing.append(f"the {name} screen's redacted log and its sha256")
        elif base is not None and not inside(base, log):
            missing.append(f"the {name} screen's log {log} inside the evidence directory, not outside it")
        elif base is not None:
            path = base / log
            if not path.is_file():
                missing.append(f"the {name} screen's log {log}, which is not committed")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                missing.append(f"the {name} screen's log {log} as recorded: its sha256 differs")
        if name == "ref" and passed(outcome):
            if section.get("exit") != "200" or not COMMIT.fullmatch(str(pins.get("commit", ""))):
                missing.append("the ref screen's HTTP 200 read at a full commit SHA")
            if not SHA.fullmatch(str(pins.get("sha256", ""))) or pins.get("sha256") != document.get("sha256"):
                missing.append("the ref screen's sha256 of the bytes it read")
            if any(pins.get(field) != document.get(field) for field in ("repository", "commit", "path")):
                missing.append("the ref screen's read of the document the record names (its repository, "
                               "commit and path pins)")
            if pins.get("expected_sha256") and pins.get("expected_sha256") != pins.get("sha256"):
                missing.append("the ref screen's read of the bytes its pin names (`expected_sha256`)")
        if name == "licence" and passed(outcome):
            missing += licence_pass_failures(pins)
        if name == "fern":
            run = section.get("run") if isinstance(section.get("run"), dict) else None
            cli, generator, version, _config = corpus_fern_pins()
            if (pins.get("fern_cli"), pins.get("generator"), pins.get("generator_version")) != (cli, generator, version):
                missing.append(f"the fern screen's run at the corpus pins ({cli}, {generator} {version})")
            if run is None or "check_exit" not in run:
                missing.append("the fern screen's measured run (`run.check_exit` and what followed)")
            elif wrong := fern_run_failures(run, document):
                missing += wrong
            else:
                if not all(isinstance(record.get(e), dict) and passed(str(record[e].get("outcome", "")))
                           for e in ("ref", "licence")):
                    missing.append("the fern screen's turn: it runs only after the ref and licence screens pass")
                expected = f"check {run['check_exit']}" + (
                    f", generate {run['generate_exit']}" if "generate_exit" in run else "")
                if section.get("exit") != expected:
                    missing.append(f"the fern screen's exit as its run records it ({expected!r}, not "
                                   f"{section.get('exit')!r})")
                try:
                    measured = fern_verdict(run)
                except KeyError as error:
                    measured = f"an incomplete run lacking {error}"
                if measured != outcome:
                    missing.append(f"a fern outcome its run measured: it reads {outcome!r}, and its "
                                   f"recorded run yields {measured!r}")
    return missing


def licence_pass_failures(pins: dict[str, Any]) -> list[str]:
    """Why a `passed` licence screen's pins do not show the pass the rule gives, or nothing.

    The document's own `info.license` decides where it says anything; the
    licence file decides only where it says nothing; a caller's judgement can
    only refuse. So a pass names the rule it read, a family that rule admits,
    and that family where precedence puts it.
    """
    families = pins.get("admissible")
    wrong = []
    if pins.get("rule") != RULE.relative_to(REPO).as_posix() or not SHA.fullmatch(str(pins.get("rule_sha256", ""))):
        wrong.append(f"the licence screen's rule ({RULE.relative_to(REPO).as_posix()} and its sha256)")
    if not isinstance(families, list) or not all(isinstance(family, str) for family in families):
        return [*wrong, "the licence screen's admissible set as the rule it read listed it"]
    declared = pins.get("document_licence")
    if not isinstance(declared, str):
        return [*wrong, "the licence screen's reading of the document (a pass needs `document_licence` read, "
                        "if only as empty)"]
    if declared:
        family, source = pins.get("document_family"), "its document's info.license"
        if family != recognise(declared):
            wrong.append(f"the licence screen's family for info.license {declared!r} as the reading gives it "
                         f"({recognise(declared)!r}, not {family!r})")
    else:
        family, source = pins.get("licence_file_family"), "its licence file"
        if not pins.get("licence_file") or not SHA.fullmatch(str(pins.get("licence_file_sha256", ""))):
            wrong.append("the licence screen's licence file and its sha256, which a pass without "
                         "info.license rests on")
    if family not in families or family not in admissible_families():
        wrong.append(f"the licence screen's reading of {source} as a grant the corpus rule admits")
    if pins.get("judgement"):
        wrong.append("a licence pass with no caller refusal: a judgement can only refuse")
    return wrong


EXIT = re.compile(r"\d+|timeout")


def fern_run_failures(run: dict[str, Any], document: dict[str, Any]) -> list[str]:
    """Why a recorded Fern run is not one `fern_screen_document` could have written over
    `document`, or nothing: its digest, exit statuses and the step order it ran in."""
    wrong = []
    if run.get("sha256") != document.get("sha256") or not SHA.fullmatch(str(run.get("sha256", ""))):
        wrong.append("the fern screen's run over the document the record names (`run.sha256`)")
    if not isinstance(run.get("check_exit"), str) or not EXIT.fullmatch(run["check_exit"]):
        wrong.append("the fern screen's `run.check_exit` as an exit status or `timeout`")
    if not isinstance(run.get("check_diagnostic"), str):
        wrong.append("the fern screen's `run.check_diagnostic` as a string")
    if ("generate_exit" in run) != (run.get("check_exit") == "0"):
        wrong.append("the fern screen's step order: a generation exactly when `fern check` exited 0")
    if "generate_exit" in run:
        if not isinstance(run.get("generate_exit"), str) or not EXIT.fullmatch(run["generate_exit"]):
            wrong.append("the fern screen's `run.generate_exit` as an exit status or `timeout`")
        if not isinstance(run.get("generate_diagnostic"), str):
            wrong.append("the fern screen's `run.generate_diagnostic` as a string")
        files = run.get("generate_python_files")
        if type(files) is not int or files < 0:
            wrong.append("the fern screen's `run.generate_python_files` as a count")
    return wrong


def inside(base: Path, log: str) -> bool:
    """Whether a recorded log path names a file under the evidence directory `base`.

    It is read as the POSIX path it is written as, on every host: relative, with
    no `..`, backslash or drive, and still under `base` once links resolve."""
    relative = PurePosixPath(log)
    if relative.is_absolute() or "\\" in log or ":" in log or ".." in relative.parts:
        return False
    return (base / Path(*relative.parts)).resolve().is_relative_to(base.resolve())


def discard_logs(record: dict[str, Any], base: Path) -> None:
    """Remove the logs a measurement wrote when its record is refused, so no log outlives its row."""
    for name in SCREENS:
        section = record.get(name)
        if isinstance(section, dict) and isinstance(section.get("log"), str) and inside(base, section["log"]):
            (base / section["log"]).unlink(missing_ok=True)


def read_measured(path: Path) -> Any:
    """A record this stage measured earlier, read from `path`, or a refusal saying how to get one."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as error:
        fail(f"--measured {path}: {error.strerror}; pass the JSON file a measurement wrote, or drop "
             "--measured to measure now")
    except ValueError as error:
        fail(f"--measured {path} is not JSON ({error}); pass the record a measurement wrote, unedited")
    raise AssertionError  # unreachable: `fail` exits


KEYS_FILE = "witness-search-keys.tsv"


def witness_keys(root: Path) -> set[str]:
    """The keys the region tables' derived key set names, read from `root`'s keys file."""
    path = root / KEYS_FILE
    remedy = "regenerate it with `tools/surface-census/witness-search-region-keys.py`"
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        fail(f"cannot read {path}: {error.strerror}; {remedy}")
    header = lines[0].split("\t") if lines else []
    if "key" not in header or len(set(header)) != len(header):
        fail(f"{path} has no header naming a `key` column once; {remedy}")
    column = header.index("key")
    keys = set()
    for number, line in enumerate(lines[1:], 2):
        cells = line.split("\t")
        if len(cells) != len(header) or not cells[column]:
            fail(f"{path}:{number} is not {len(header)} cells with a key; {remedy}")
        keys.add(cells[column])
    return keys


def nonempty(text: str) -> str:
    if not text.strip():
        raise argparse.ArgumentTypeError("a key is a non-empty witness-search key")
    return text


def positive_int(text: str) -> int:
    value = int(text)
    if value <= 0:
        raise argparse.ArgumentTypeError(f"{text} is not a positive number of seconds")
    return value


def outcomes(record: dict[str, Any]) -> dict[str, str]:
    return {name: record[name]["outcome"] for name in SCREENS}


def unmeasured(row: dict[str, Any]) -> bool:
    """A screen row carrying no measured record. Whether one may stand as historical is
    `row_failures`'s decision, which reads its date."""
    return "measured" not in row


def unmeasured_date_failure(row: dict[str, Any]) -> str | None:
    """Why an unmeasured row cannot stand as historical, or None when it can.

    `screen` dates every row it files, so a row with no date at all is one of
    the shapes filed before the stage existed. A date that is there must be an
    instant with its offset, and before [`MEASURED_SINCE`]: a malformed or
    offset-less one says nothing about when the row was filed, and one at or
    after the cutover owes the measured record.
    """
    field = next((name for name in ("screened_at", "recorded_at") if name in row), None)
    if field is None:
        return None
    stamp = timestamp(row[field])
    if stamp is None:
        return (f"its `{field}` {row[field]!r} is no ISO 8601 instant with its offset, so nothing shows it "
                f"predates the measured stage ({MEASURED_SINCE}) — restore the row from git, or file it "
                f"through `{STAGE}`")
    if stamp >= datetime.datetime.fromisoformat(MEASURED_SINCE):
        return (f"it is dated {row[field]}, after the measured stage landed ({MEASURED_SINCE}), and carries "
                f"no measured record — file it through `{STAGE}`")
    return None


def row_failures(row: dict[str, Any], base: Path, fields: dict[str, str]) -> list[str]:
    """One screen row against its measured record: refused unless it is whole or historical.

    `fields` maps each screen to the row field that states its outcome. A row
    carrying a record must state exactly the outcomes it records; one without
    is historical only if it predates the stage (`unmeasured_date_failure`).
    """
    if unmeasured(row):
        failure = unmeasured_date_failure(row)
        return [failure] if failure else []
    failures = measured_failures(row["measured"], base)
    if not failures:
        for name, field in fields.items():
            if row.get(field) != row["measured"][name]["outcome"]:
                failures.append(f"its {field} {row.get(field)!r} is not the measured {name} outcome")
    return failures


# A filed screen is `rejected` or a success the index reads: its own grammar,
# `known_disposition`, less the two that settle nothing about a candidate.
REJECTED = "rejected"
UNSETTLED = (REJECTED, "outstanding")


@functools.lru_cache(maxsize=1)
def disposition_index() -> ModuleType:
    """`witness-search-github-index.py`, the one statement of the disposition grammar."""
    return _load("witness_screen_disposition_index", Path(__file__).with_name("witness-search-github-index.py"))


def success_disposition(text: str) -> bool:
    """Whether `text` is a disposition claiming a candidate, as the index reads one."""
    return text not in UNSETTLED and disposition_index().known_disposition(text)


def disposition_arg(text: str) -> str:
    if text and text != REJECTED and not success_disposition(text):
        raise argparse.ArgumentTypeError(
            f"{text!r} is not a disposition: use {REJECTED}, witness-found, not-owed, "
            "pending-registration[; owner <node>], or byte-identical to CORPUS row <n>, sha256 <digest>")
    return text


def legacy_screen(args: argparse.Namespace) -> int:
    """Take one candidate's screens and append them to its legacy `screens.jsonl`."""
    if args.fern is not None:
        fail("`--fern` is no longer a measurement: this stage runs pinned Fern itself and records its exit "
             "status and log — drop `--fern`")
    directory = args.evidence_root / f"witness-search-{args.source}"
    if not directory.is_dir():
        fail(f"{directory} does not exist; acquire {args.source} through its witness-search script first")
    known = witness_keys(args.evidence_root)
    unknown = [key for key in args.key if key not in known]
    if unknown:
        fail(f"--key {', '.join(map(repr, unknown))} is no witness-search key in "
             f"{args.evidence_root / KEYS_FILE}; pass a key that file lists (regenerate it with "
             "`tools/surface-census/witness-search-region-keys.py` if the regions moved)")
    if args.measured:
        record = read_measured(args.measured)
    else:
        github = _load("witness_search_github_screen", REPO / "tools" / "witness-search" / "witness-search-github.py")
        acquirer = github.Acquirer(directory, cache=REPO / ".local" / "witness-screen" / args.source,
                                   raw_github_url=github.checked_service_url(
                                       os.environ.get("CROZIER_RAW_GITHUB_URL", github.RAW_GITHUB_URL),
                                       "CROZIER_RAW_GITHUB_URL", "raw.githubusercontent.com"))
        record = measure(repository=args.repository, commit=args.commit, path=args.path,
                         fetch=lambda url, subject: acquirer.raw_github_get(url, args.key[0], subject),
                         raw_base=acquirer.raw_github_url, logs=directory / LOG_DIR, base=directory,
                         expected_sha256=args.sha256, licence_refusal=args.licence_refusal,
                         timeout=args.timeout)
    missing = measured_failures(record, directory)
    all_passed = isinstance(record, dict) and all(
        isinstance(record.get(name), dict) and passed(str(record[name].get("outcome", ""))) for name in SCREENS)
    disposition = args.disposition or ("" if all_passed else REJECTED)
    refusal = ""
    if missing:
        refusal = ("a screen is filed only with its measured record; it lacks " + "; ".join(missing)
                   + " — measure it again: run `screen` without --measured")
    elif disposition and success_disposition(disposition) and not all_passed:
        refusal = (f"`{disposition}` claims a candidate that passed every screen, and this one's measured "
                   f"outcomes read {outcomes(record)}; drop --disposition to file it `rejected`")
    elif not disposition:
        refusal = ("every screen passed; say what becomes of the candidate with --disposition "
                   "(witness-found, pending-registration, …)")
    elif (record["document"]["repository"], record["document"]["commit"], record["document"]["path"]) \
            != (args.repository, args.commit, args.path):
        refusal = ("the measured record names another document than --repository/--commit/--path; pass "
                   "the record's own document, or drop --measured to measure this one")
    elif args.measured and args.sha256 and record["document"]["sha256"] != args.sha256:
        # A fresh measurement checks the pin itself, as its ref screen; an
        # imported one was measured elsewhere, so the pin is checked here.
        refusal = (f"the measured record read bytes with sha256 {record['document']['sha256'] or '(none)'}, "
                   f"not the --sha256 {args.sha256} the acquisition pinned; pass the record measured over "
                   "those bytes, or drop --measured to measure them now")
    if refusal:
        if not args.measured and isinstance(record, dict):
            discard_logs(record, directory)
        fail(refusal)
    document = record["document"]
    row = {"source": args.source, "repository": args.repository, "path": args.path, "commit": args.commit,
           "sha256": document["sha256"], "keys": args.key, "license": record["licence"]["outcome"],
           "ref": record["ref"]["outcome"], "fern": record["fern"]["outcome"], "disposition": disposition,
           "screened_at": record["screened_at"], "measured": record}
    with (directory / "screens.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True) + "\n")
    print(f"witness-screen: {args.source}: {args.repository}:{args.path} — licence "
          f"{row['license'].split(':', 1)[0]}, ref {row['ref'].split(':', 1)[0]}, "
          f"fern {row['fern'].split(':', 1)[0]}; {disposition}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)
    s = sub.add_parser("screen", help="screen one legacy witness-search candidate")
    s.add_argument("--source", required=True, choices=LEGACY_SOURCES)
    s.add_argument("--key", action="append", required=True, type=nonempty)
    s.add_argument("--repository", required=True, help="owner/name")
    s.add_argument("--commit", required=True)
    s.add_argument("--path", required=True)
    s.add_argument("--sha256", default="", help="the digest the acquisition pinned, checked against what is read")
    s.add_argument("--licence-refusal", default="", help="refuse a licence the reading would pass, and why")
    s.add_argument("--disposition", default="", type=disposition_arg,
                   help="what becomes of a candidate passing every screen")
    s.add_argument("--measured", type=Path, help="a record this stage measured earlier, filed as it stands")
    s.add_argument("--timeout", type=positive_int, default=1800)
    s.add_argument("--evidence-root", type=Path, default=REPO / "docs" / "openapi-surface")
    s.add_argument("--fern", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    return legacy_screen(args)


if __name__ == "__main__":
    sys.exit(main())
