#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo crate driven by `just`, with no Nx workspace (no nx.json or project.json anywhere); this script sits in scripts/ beside the census scripts whose records it reads, and runs as `just fern-refusals-*` and under `just test-fern-refusals`.
"""Build the refused-document population of `docs/fern-refusals/`.

The registry's population is every document crozier's committed records name as
refused, crashed on, or falsely reported successful by Fern (CLI 5.67.1,
`fernapi/fern-python-sdk` 5.20.0):

* the `DROPPED` rows of `tests/fixtures/CORPUS.md` whose reason is a Fern
  failure — a reason that names Fern; rows dropped for redundancy never do —
  each located by `docs/openapi-surface/fern-refusals/dropped-sources.tsv`;
* every `docs/openapi-surface/**/screens.jsonl` record whose `fern` field is a
  `failed:` or `refused:` verdict, located by its own fields or, for a
  golden-reach witness, by its source's committed enumeration.

Deduplicated by the SHA-256 of the document's bytes.

Subcommands, in the order a refresh runs them:

``select``
    Print the population as TSV (offline).
``measure``
    Fetch each document (through ``scripts/rate_limit_guard.py``'s paced raw
    lane for a GitHub host), run Fern at the pin where no committed log holds
    its complete diagnostic list, and run crozier's release build over it,
    appending one line per document to ``measurements.jsonl``. Needs network,
    Docker, ``fern`` and ``target/release/crozier``.
``build``
    Rewrite ``documents.tsv``, ``unretrievable.tsv`` and ``classes.tsv``'s
    ``documents`` column from the committed inputs alone (offline).
``check``
    Fail when a committed table differs from what ``build`` writes, or when its
    header or cross references drift from the registry contract (offline).

Every class a document carries is found by matching each diagnostic in its Fern
log against ``classes.tsv``'s ``diagnostic`` templates, where ``<…>`` stands for
a document-specific part. A diagnostic no template matches fails ``build``, so a
new phrase becomes a class deliberately rather than silently.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import ModuleType
from typing import Any, Iterable, NamedTuple, TypedDict

REPO = Path(__file__).resolve().parent.parent
# The tests point this at a scratch copy to show `check` failing on drift.
REGISTRY = Path(os.environ.get("CROZIER_FERN_REFUSALS_REGISTRY") or REPO / "docs" / "fern-refusals")
EVIDENCE = REPO / "docs" / "openapi-surface" / "fern-refusals"
SURFACE = REPO / "docs" / "openapi-surface"
CORPUS = REPO / "tests" / "fixtures" / "CORPUS.md"
CACHE = REPO / ".local" / "fern-refusals"

CLASSES_HEADER = ("class", "family", "fern_stage", "fern_exit", "diagnostic", "documents",
                  "status", "crozier_diagnostic", "population_strict")
DOCUMENTS_HEADER = ("digest", "source", "locator", "revision", "recorded_by", "fern_stage", "fern_exit",
                    "fern_log", "classes", "crozier_exit", "crozier_files", "crozier_strict_exit")
UNRETRIEVABLE_HEADER = ("source", "locator", "revision", "recorded_by", "digest", "reason")
GENERATED_HEADER = ("source", "locator", "revision", "recorded_by", "digest", "fern_log", "findings")
CONFIRMATIONS_HEADER = ("class", "digest", "publisher", "generate_exit", "generate_files", "generate_log")
FINDINGS_HEADER = ("finding", "kind", "check_exit", "generate_exit", "diagnostic", "probe")
DROPPED_HEADER = ("name", "corpus_line", "source", "locator", "revision", "sha256", "evidence", "reason")
MEASUREMENT_FIELDS = ("key", "digest", "unretrievable", "check_exit", "check_log", "generate_exit",
                      "generate_files", "generate_log", "crozier_exit", "crozier_files", "crozier_strict_exit")
FERN_CLI = "5.67.1"
FERN_PYTHON_SDK = "5.20.0"
EMPTY = "—"
# Enumerated golden-reach sources name a document by its enumeration subject;
# searched ones by `<repository>:<path>@<commit>` in their `candidates.jsonl`.
ENUMERATED = ("jentic", "apis.guru", "vendor-portals", "github-publisher-trees")
SEARCHED = ("github-code-search", "sourcegraph")
# The enumeration columns a population entry is built from.
ENUMERATION_COLUMNS = ("walk", "document", "revision", "sha256")


def fail(message: str) -> None:
    print(f"fern-refusals: {message}", file=sys.stderr)
    raise SystemExit(1)


def rel(path: Path) -> str:
    """`path` as the repository spells it: relative, POSIX separators."""
    return path.relative_to(REPO).as_posix() if path.is_relative_to(REPO) else path.as_posix()


def require(path: Path) -> Path:
    """`path`, once it is known to exist: a committed input that is gone fails with the fix."""
    if not path.is_file():
        fail(f"{rel(path)} is missing; restore it from git")
    return path


def require_fields(path: Path, number: int, row: dict[str, Any], fields: tuple[str, ...]) -> None:
    """Exit naming line `number` of `path` when its record does not carry every one of `fields`."""
    missing = [field for field in fields if field not in row]
    if missing:
        fail(f"{rel(path)} line {number} lacks {', '.join(missing)}; restore it from git")


def read_jsonl(path: Path, fields: tuple[str, ...]) -> list[tuple[int, dict[str, Any]]]:
    """Each line of a committed JSONL record, numbered, as an object carrying
    `fields`: a malformed line fails naming the file and line, never a traceback."""
    rows = []
    for number, line in enumerate(require(path).read_text(encoding="utf-8").splitlines(), 1):
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            fail(f"{rel(path)} line {number} is not JSON ({error.msg}); restore it from git")
        if not isinstance(row, dict):
            fail(f"{rel(path)} line {number} is not a JSON object; restore it from git")
        require_fields(path, number, row, fields)
        rows.append((number, row))
    return rows


def read_tsv(path: Path, header: tuple[str, ...]) -> list[dict[str, str]]:
    require(path)
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        rows = list(reader)
    if not rows or tuple(rows[0]) != header:
        fail(f"{rel(path)}: the header must be exactly {chr(9).join(header)!r}; restore it from git")
    for number, row in enumerate(rows[1:], 2):
        if len(row) != len(header):
            fail(f"{rel(path)} line {number}: {len(row)} column(s) where the header has {len(header)}; "
                 "restore it from git")
    return [dict(zip(header, row)) for row in rows[1:]]


def tsv_text(header: tuple[str, ...], rows: Iterable[dict[str, str]]) -> str:
    lines = ["\t".join(header)]
    for row in rows:
        cells = [str(row[column]) for column in header]
        for cell in cells:
            if "\t" in cell or "\n" in cell:
                fail(f"a cell holds a tab or newline: {cell!r}; remove it from the record or class row "
                     "it came from, then rerun `build`")
        lines.append("\t".join(cells))
    return "\n".join(lines) + "\n"


def raw_url(repository: str, commit: str, path: str) -> str:
    repository = repository.removeprefix("github.com/")
    return f"https://raw.githubusercontent.com/{repository}/{commit}/{urllib.parse.quote(path)}"


def dropped_rows() -> list[tuple[int, str, str]]:
    """`(line, name, reason)` of every CORPUS.md `DROPPED` row whose reason is a Fern failure."""
    found = []
    for number, line in enumerate(require(CORPUS).read_text(encoding="utf-8").splitlines(), start=1):
        if "DROPPED" not in line or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        status = next((cell for cell in cells if "DROPPED" in cell), "")
        if not re.search(r"\bfern\b", status, re.I):
            continue
        # `letta` at `<ref>` and `count-co` (`<where>`) name one document;
        # `pnp-agents-finder` / `pnp-qna` names two.
        head = re.split(r"\(| at ", cells[0])[0]
        for name in re.findall(r"`([^`]+)`", head):
            found.append((number, name, status))
    return found


def enumeration(source: str) -> dict[str, dict[str, str]]:
    path = SURFACE / "golden-reach-witnesses" / source / "enumeration.tsv.gz"
    with gzip.open(require(path), "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        rows = list(reader)
        missing = [column for column in ENUMERATION_COLUMNS if column not in (reader.fieldnames or [])]
    if missing:
        fail(f"{rel(path)}: the header lacks {', '.join(missing)}; restore it from git, or re-walk the source")
    seen: dict[str, int] = {}
    for row in rows:
        seen[row["document"]] = seen.get(row["document"], 0) + 1
    return {(f"{row['walk']}:{row['document']}" if seen[row["document"]] > 1 else row["document"]): row
            for row in rows}


def enumerated_locator(source: str, row: dict[str, str]) -> str:
    path = row["document"]
    if source == "vendor-portals":
        # A portal clone is laid out as `<owner>--<repo>/<path>`.
        path = path.split("/", 1)[1]
    return raw_url(row["walk"], row["revision"], path)


def searched_candidates(source: str) -> dict[str, dict[str, Any]]:
    # A search's candidate record is free-form JSON; only its repository, path,
    # commit and sha256 are read.
    path = SURFACE / "golden-reach-witnesses" / source / "candidates.jsonl"
    found = {}
    for _number, row in read_jsonl(path, ("repository", "path", "commit", "sha256")):
        found[f"{row['repository']}:{row['path']}@{row['commit']}"] = row
    return found


class Entry(TypedDict, total=False):
    """One selected document: how the committed records locate it and name it."""
    key: str
    digest: str
    source: str
    locator: str
    revision: str
    records: set[str]
    name: str
    reason: str
    verdict: str
    logs: list[str]


def failed(verdict: object) -> bool:
    return str(verdict).startswith(("failed", "refused"))


def population() -> list[Entry]:
    """Every selected document, merged by digest where the digest is known."""
    entries: list[Entry] = []
    corpus = rel(CORPUS)
    located = {row["name"]: row for row in read_tsv(EVIDENCE / "dropped-sources.tsv", DROPPED_HEADER)}
    for line, name, _reason in dropped_rows():
        row = located.get(name)
        if row is None:
            fail(f"CORPUS.md line {line} drops `{name}` for a Fern failure, but "
                 f"{rel(EVIDENCE / 'dropped-sources.tsv')} does not locate it; add its row")
        known = {field: "" if row[field] == EMPTY else row[field] for field in ("sha256", "locator", "revision")}
        entries.append({"digest": known["sha256"], "source": row["source"], "locator": known["locator"],
                        "revision": known["revision"], "records": {corpus}, "name": name,
                        "reason": "" if known["locator"] else row["evidence"]})
    enumerations = {source: enumeration(source) for source in ENUMERATED}
    candidates = {source: searched_candidates(source) for source in SEARCHED}
    for screens in sorted(SURFACE.glob("**/screens.jsonl")):
        source = screens.parent.name
        record = rel(screens)
        for number, row in read_jsonl(screens, ("fern",)):
            if not failed(row["fern"]):
                continue
            if "candidate" not in row:
                require_fields(screens, number, row, ("source", "repository", "commit", "path"))
                logs = [rel(screens.parent / log) for log in row.get("fern_logs", [])]
                entries.append({"digest": row.get("sha256", ""), "source": row["source"],
                                "locator": raw_url(row["repository"], row["commit"], row["path"]),
                                "revision": row["commit"], "records": {record}, "verdict": row["fern"],
                                "logs": logs})
            elif source in enumerations:
                hit = enumerations[source].get(row["candidate"])
                if hit is None:
                    fail(f"{record}: {row['candidate']} is in no {source} enumeration row; restore "
                         f"golden-reach-witnesses/{source}/enumeration.tsv.gz from git, or re-walk the source")
                entries.append({"digest": hit["sha256"], "source": source,
                                "locator": enumerated_locator(source, hit), "revision": hit["revision"],
                                "records": {record}})
            else:
                hit = candidates[source].get(row["candidate"])
                if hit is None:
                    fail(f"{record}: {row['candidate']} is in no {source} candidates.jsonl row; restore "
                         f"golden-reach-witnesses/{source}/candidates.jsonl from git")
                entries.append({"digest": hit["sha256"], "source": source,
                                "locator": raw_url(hit["repository"], hit["commit"], hit["path"]),
                                "revision": hit["commit"], "records": {record}})
    merged: dict[str, Entry] = {}
    for entry in entries:
        key = entry["digest"] or entry["locator"] or f"{corpus}#{entry['name']}"
        if key in merged:
            kept = merged[key]
            kept["records"] |= entry["records"]
            kept.setdefault("logs", [])
            kept["logs"] = sorted(set(kept["logs"]) | set(entry.get("logs", [])))
        else:
            merged[key] = Entry(**entry, key=key)
            merged[key]["logs"] = sorted(entry.get("logs", []))
    return sorted(merged.values(), key=lambda entry: entry["key"])


def select(_args: argparse.Namespace) -> int:
    print("key\tsource\tlocator\trevision\trecorded_by")
    for entry in population():
        print("\t".join([entry["key"], entry["source"], entry["locator"] or EMPTY, entry["revision"] or EMPTY,
                         ";".join(sorted(entry["records"]))]))
    return 0


def _load(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def local_index(roots: list[Path]) -> dict[str, Path]:
    """Every OpenAPI-looking file under `roots`, by the SHA-256 of its bytes."""
    found: dict[str, Path] = {}
    for root in roots:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix in (".json", ".yaml", ".yml"):
                found.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(), path)
    return found


def suffix_of(locator: str) -> str:
    suffix = Path(urllib.parse.urlparse(locator).path).suffix.lower()
    return suffix if suffix in (".json", ".yaml", ".yml") else ".yml"


class Fetcher:
    """Bytes for a locator: a local copy by digest, else one guarded request."""

    def __init__(self, roots: list[Path]) -> None:
        self.index = local_index(roots)
        github = _load("witness_search_github", REPO / "scripts" / "witness-search-github.py")
        self.acquirer = github.Acquirer(CACHE / "evidence", cache=CACHE / "evidence")

    def get(self, entry: Entry) -> tuple[bytes | None, str]:
        digest = entry["digest"]
        if digest and digest in self.index:
            return self.index[digest].read_bytes(), ""
        locator = entry["locator"]
        if not locator:
            return None, entry.get("reason") or "no committed record locates the screened document"
        try:
            if urllib.parse.urlparse(locator).hostname == "raw.githubusercontent.com":
                status, data = self.acquirer.raw_github_get(locator, "fern-refusals", locator)
            else:
                with urllib.request.urlopen(urllib.request.Request(
                        locator, headers={"User-Agent": "crozier-fern-refusals"}), timeout=90) as response:
                    status, data = response.status, response.read()
        except OSError as error:
            return None, f"fetch failed: {error}"
        if status != 200:
            return None, f"{locator} answered HTTP {status}"
        actual = hashlib.sha256(data).hexdigest()
        if digest and actual != digest:
            return None, f"{locator} now serves bytes hashing to {actual}, not the recorded {digest}"
        return data, ""


def fern_workspace(document: Path, workspace: Path) -> None:
    (workspace / "openapi").mkdir(parents=True)
    shutil.copyfile(document, workspace / "openapi" / "openapi.yml")
    (workspace / "fern.config.json").write_text(
        json.dumps({"organization": "fern", "version": FERN_CLI}) + "\n", encoding="utf-8")
    (workspace / "generators.yml").write_text(
        "api:\n  path: openapi/openapi.yml\ngroups:\n  python-sdk:\n    generators:\n"
        f"      - name: fernapi/fern-python-sdk\n        version: {FERN_PYTHON_SDK}\n"
        "        config:\n          pydantic_config:\n            enum_type: python_enums\n"
        "        output:\n          location: local-file-system\n          path: ../generated/python\n",
        encoding="utf-8")


# Node's default heap cannot hold Fern's model of the largest documents (the
# GitHub REST descriptions run out at 4 GB), so a run that would only report
# the host's memory is given room to report Fern's own diagnostics instead.
NODE_HEAP = "--max-old-space-size=16384"


def fern_run(command: list[str], workspace: Path, timeout: int) -> tuple[str, str]:
    if shutil.which(command[0]) is None:
        fail(f"`{command[0]}` is not on PATH; run `just setup-fern` (it installs the Fern CLI and needs Docker "
             "for `fern generate`)")
    env = dict(os.environ, FERN_TOKEN="preview-only-no-publish", CI="true", GITHUB_ACTIONS="true",
               NODE_OPTIONS=NODE_HEAP)
    try:
        run = subprocess.run(command, cwd=workspace, env=env, capture_output=True, text=True,
                             errors="replace", timeout=timeout)
    except subprocess.TimeoutExpired:
        return "timeout", ""
    return str(run.returncode), run.stdout + run.stderr


def fern_check(document: Path, digest: str, timeout: int) -> dict[str, str]:
    """`fern check` over one document, its log kept."""
    with tempfile.TemporaryDirectory(prefix="fern-refusals-") as scratch:
        workspace = Path(scratch) / "fern"
        fern_workspace(document, workspace)
        status, output = fern_run(["fern", "check"], workspace, timeout)
    path = EVIDENCE / "logs" / f"{digest}.check.log"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(scrub(output), encoding="utf-8")
    return {"check_exit": status, "check_log": rel(path)}


def fern_generate(document: Path, digest: str, timeout: int) -> dict[str, str]:
    """`fern generate` over one document whatever the check said — a phrase the
    check refuses may not stop a generation — its log kept and its tree counted."""
    with tempfile.TemporaryDirectory(prefix="fern-refusals-") as scratch:
        workspace = Path(scratch) / "fern"
        fern_workspace(document, workspace)
        preview = Path(scratch) / "preview"
        status, output = fern_run(["fern", "generate", "--group", "python-sdk", "--local", "--preview",
                                   "--output", str(preview), "--force"], workspace, timeout)
        files = sum(1 for path in preview.rglob("*") if path.is_file()) if preview.is_dir() else 0
    path = EVIDENCE / "logs" / f"{digest}.generate.log"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(scrub(output), encoding="utf-8")
    return {"generate_exit": status, "generate_files": str(files), "generate_log": rel(path)}


def scrub(log: str) -> str:
    """Fern's output with this host's paths and scratch names made generic, less
    the lines that only repeat it: the `::error`/`::warning` annotations a CI run
    adds, and each stack frame under an error it already printed."""
    log = "".join(line for line in log.splitlines(keepends=True)
                  if not line.startswith("::") and not re.match(r"\s+at ", line))
    log = re.sub(r"/home/[^/\s]+/\.npm/_npx/[0-9a-f]+/", "<npx>/", log)
    log = re.sub(r"/tmp/[\w.-]+", "<tmp>", log)
    log = re.sub(r"\b\d+(\.\d+)? seconds\b", "<n> seconds", log)
    return log


EXIT = re.compile(r"check(?: exits?| exit) (\d+)")


def committed_check(entry: Entry) -> dict[str, str] | None:
    """A committed screen's `fern check` log, when its record states the exit."""
    exits = EXIT.findall(entry.get("verdict", ""))
    log = next((path for path in entry.get("logs", []) if path.endswith("-check.log")), None)
    if log and exits:
        return {"check_exit": exits[0], "check_log": log}
    return None


def upgraded(row: dict[str, str]) -> dict[str, str]:
    """A measurement in today's fields, each one present. One taken before
    generations were measured carries a single log, the check's or the
    generation's."""
    row = dict({field: "" for field in MEASUREMENT_FIELDS}, **row)
    if "fern_stage" in row:
        stage, status, log = row.pop("fern_stage"), row.pop("fern_exit"), row.pop("fern_log")
        if stage == "check":
            row.update(check_exit=status, check_log=log)
        else:
            row.update(check_exit="0", check_log="", generate_exit=status, generate_log=log)
    return {field: row[field] for field in MEASUREMENT_FIELDS}


def crozier_run(binary: Path, document: Path, timeout: int, *flags: str) -> tuple[str, str]:
    """crozier's exit on `document`, and how many files it wrote."""
    with tempfile.TemporaryDirectory(prefix="fern-refusals-crozier-") as scratch:
        output = Path(scratch) / "sdk"
        try:
            run = subprocess.run([str(binary), "--no-config", "generate", "python", *flags, "--spec",
                                  str(document), "--output", str(output), "--package-name", "fern",
                                  "--project-name", "default_package_name"],
                                 capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return "timeout", "0"
        files = sum(1 for path in output.rglob("*") if path.is_file()) if output.is_dir() else 0
    return str(run.returncode), str(files)


def crozier_measure(binary: Path, document: Path, timeout: int) -> dict[str, str]:
    status, files = crozier_run(binary, document, timeout)
    return {"crozier_exit": status, "crozier_files": files}


def crozier_strict_measure(binary: Path, document: Path, timeout: int) -> dict[str, str]:
    return {"crozier_strict_exit": crozier_run(binary, document, timeout, "--fern-strict")[0]}


def read_measurements() -> dict[str, dict[str, str]]:
    path = EVIDENCE / "measurements.jsonl"
    if not path.is_file():
        return {}
    rows = read_jsonl(path, ("key",))
    for number, row in rows:
        if "fern_stage" in row:
            require_fields(path, number, row, ("fern_exit", "fern_log"))
    return {row["key"]: upgraded(row) for _number, row in rows}


def ran_out_below_the_heap(log: str) -> bool:
    """Whether `log` records Node running out of memory under a heap smaller than
    `NODE_HEAP` grants — its garbage-collection trace names the heap in MB."""
    if "heap out of memory" not in log:
        return False
    sizes = [float(size) for size in re.findall(r"\((\d+(?:\.\d+)?)\) -> ", log)]
    return not sizes or max(sizes) < int(NODE_HEAP.rsplit("=", 1)[1]) * 0.9


def check_blocks(row: dict[str, str]) -> bool:
    """Whether the document's `fern check` names a refusal class. Every class's
    probe shows its phrase stopping `fern generate` too, so such a document's
    generation need not be run to know Fern refuses it."""
    classes = read_tsv(REGISTRY / "classes.tsv", CLASSES_HEADER)
    findings = read_tsv(REGISTRY / "findings.tsv", FINDINGS_HEADER)
    carried, _found, _unmatched = classify(diagnostics(read_log(row.get("check_log", ""))),
                                           class_patterns(classes), finding_patterns(findings))
    return row.get("check_exit") not in ("", "0") and bool(carried)


def missing_measurements(row: dict[str, str]) -> set[str]:
    """Which of `check`, `generate` and `crozier` a retrievable document still needs."""
    if row.get("unretrievable"):
        return set()
    missing = set()
    log = row.get("check_log")
    if not row.get("check_exit") or (log and ran_out_below_the_heap(read_log(log))):
        # A run that ran out of Node's default heap reported the host, not Fern:
        # take it again. One that exhausts `NODE_HEAP` is Fern's own verdict.
        missing.add("check")
    elif not row.get("generate_files") and not check_blocks(row):
        missing.add("generate")
    if not row.get("crozier_exit"):
        missing.add("crozier")
    if not row.get("crozier_strict_exit"):
        # `build` needs it only for a document carrying an evaluated class.
        missing.add("crozier-strict")
    return missing


def measure(args: argparse.Namespace) -> int:
    binary = REPO / "target" / "release" / "crozier"
    if not binary.is_file():
        fail("build crozier's release binary first: run `just fern-refusals-measure`, which builds it and measures")
    done = read_measurements()
    todo = [entry for entry in population()
            if entry["key"] not in done or missing_measurements(done[entry["key"]]) or args.again]
    if args.limit:
        todo = todo[: args.limit]
    fetcher = Fetcher([REPO / ".local", *args.root])
    documents = CACHE / "documents"
    documents.mkdir(parents=True, exist_ok=True)

    def one(entry: Entry, data: bytes) -> dict[str, str]:
        digest = hashlib.sha256(data).hexdigest()
        path = documents / f"{digest}{suffix_of(entry['locator'])}"
        path.write_bytes(data)
        row = {} if args.again else dict(done.get(entry["key"], {}))
        row.update(key=entry["key"], digest=digest, unretrievable="")
        needed = missing_measurements(row) if row.get("check_exit") or row.get("crozier_exit") else \
            {"check", "crozier", "crozier-strict"}
        if "check" in needed:
            row.update(committed_check(entry) if not row.get("check_exit") and committed_check(entry)
                       else fern_check(path, digest, args.timeout))
            if not row.get("generate_files") and not check_blocks(row):
                needed.add("generate")
        if "generate" in needed:
            row.update(fern_generate(path, digest, args.timeout))
        if "crozier" in needed:
            row.update(crozier_measure(binary, path, args.timeout))
        if "crozier-strict" in needed:
            row.update(crozier_strict_measure(binary, path, args.timeout))
        return row

    lock = threading.Lock()

    def record(result: dict[str, str]) -> None:
        with lock:
            done[result["key"]] = {field: result.get(field, "") for field in MEASUREMENT_FIELDS}
            write_measurements(done)

    # Fetches share one paced lane, so they run in this thread, one at a time;
    # Fern and crozier fan out behind them.
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = []
        for entry in todo:
            data, reason = fetcher.get(entry)
            if data is None:
                record({"key": entry["key"], "digest": entry["digest"], "unretrievable": reason})
                continue
            futures.append(pool.submit(one, entry, data))
            futures[-1].add_done_callback(lambda future: record(future.result()))
        for future in futures:
            future.result()
    print(f"fern-refusals: {len(todo)} measured, {len(done)} on record")
    return 0


def write_measurements(done: dict[str, dict[str, str]]) -> None:
    path = EVIDENCE / "measurements.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(done[key], sort_keys=True) + "\n" for key in sorted(done)),
                    encoding="utf-8")


API_LINE = re.compile(r"\[api\]: (?:python-sdk )?(?:fernapi/fern-python-sdk )?(.*)")


def diagnostics(log: str) -> list[str]:
    """Every distinct thing Fern said was wrong, one message each, in first-seen order.

    `fern check` prints each error as an `issue:` line (the lines under it only
    list where);
    a generation prints it after `[error]`; a document Fern never parsed is an
    `[api]:` line naming what it could not resolve or the exception it hit; and
    a generator container that exits non-zero prints, under `Container execution
    failed`, the Python exception or the lint command it died in — the
    `Failed to format …`/`ParseError` lines before a lint failure only say which
    snippet did not parse, and count only when nothing fatal follows them. The
    bare `Failed to parse openapi document <title>` that heads such a failure
    counts only when nothing more specific follows it, and a schema Fern merely
    coerces to `unknown` is a warning, not a refusal.
    """
    found: list[str] = []
    formatting: list[str] = []
    lines = log.splitlines()
    in_container = False
    for line in lines:
        text = line.strip()
        message = ""
        if text.startswith("[api]:"):
            in_container = "Container execution failed" in text
        elif in_container and re.match(r"(Failed to format |ParseError: )", text):
            if text not in formatting:
                formatting.append(text)
        elif in_container and re.match(r"(\w+(Error|Exception): |Failed to run command: )", text):
            message = text
        if text.startswith("issue: "):
            message = text[len("issue: "):]
        elif "JavaScript heap out of memory" in text:
            message = text
        elif "[error] " in text:
            message = text.split("[error] ", 1)[1]
        elif (api := API_LINE.match(text)) and re.match(
                r"Failed to (resolve|parse openapi document)|Unexpected error|Unsupported |Maximum call stack|.* is undefined$|\w*(Error|Exception)\b.*:", api.group(1)):
            message = api.group(1)
        # A name Fern could not form leaves the phrase leading with a space.
        message = message.rstrip()
        if message.strip() and message not in found:
            found.append(message)
    specific = [message for message in found if not message.startswith("Failed to parse openapi document")]
    return specific or found or formatting


class Template(NamedTuple):
    """A class's or finding's `diagnostic` as a matcher, with how much literal
    text it pins down."""
    name: str
    pattern: re.Pattern[str]
    literal: int


def template_pattern(template: str) -> re.Pattern[str]:
    parts = [re.escape(part) for part in template.split("<…>")]
    return re.compile("^" + ".*?".join(parts) + "$", re.S)


def template(name: str, diagnostic: str) -> Template:
    return Template(name, template_pattern(diagnostic), len(diagnostic.replace("<…>", "")))


def most_specific(matching: list[Template]) -> list[str]:
    """Of the templates matching one message, those with the most literal text:
    `Default value <…> is not a valid enum value` over `… is not a valid <…>`."""
    best = max((candidate.literal for candidate in matching), default=0)
    return [candidate.name for candidate in matching if candidate.literal == best]


def class_patterns(classes: list[dict[str, str]]) -> list[Template]:
    return [template(row["class"], row["diagnostic"]) for row in classes]


def finding_patterns(findings: list[dict[str, str]]) -> list[Template]:
    """The phrases `fern check` refuses while `fern generate` still writes an SDK."""
    return [template(row["finding"], row["diagnostic"]) for row in findings if row["kind"] == "check-only"]


def classify(messages: list[str], patterns: list[Template],
             findings: list[Template]) -> tuple[list[str], list[str], list[str]]:
    """The classes and check-only findings `messages` carry, and the messages
    that match no single class or finding."""
    carried: list[str] = []
    found: list[str] = []
    unmatched: list[str] = []
    for message in messages:
        matched = most_specific([candidate for candidate in [*patterns, *findings]
                                 if candidate.pattern.match(message)])
        hits = [candidate.name for candidate in patterns if candidate.name in matched]
        near = [candidate.name for candidate in findings if candidate.name in matched]
        if len(hits) + len(near) != 1:
            unmatched.append(f"{message}  [matches: {', '.join(hits + near) or 'none'}]")
        elif hits and hits[0] not in carried:
            carried.append(hits[0])
        elif near and near[0] not in found:
            found.append(near[0])
    return sorted(carried), sorted(found), unmatched


def read_log(path: str) -> str:
    return (REPO / path).read_text(encoding="utf-8", errors="replace") if path else ""


def verdict(result: dict[str, str], patterns: list[Template],
            findings: list[Template]) -> tuple[dict[str, str] | None, list[str], list[str]]:
    """Whether Fern refuses the measured document, and why.

    Fern refuses when its generation exits non-zero, writes nothing, or reports
    a refusal class over a document it did not parse. Its check's own phrases
    then name the classes when the check carries any; otherwise the generation's
    do. A document Fern generates from returns `None` with the check-only
    phrases it printed. The third value lists every message no class or finding
    matches.
    """
    check_classes, check_found, check_unmatched = classify(diagnostics(read_log(result["check_log"])),
                                                           patterns, findings)
    if check_classes and result["check_exit"] != "0" and not result.get("generate_exit"):
        # The check named a class, which stops the generation too; it was not run.
        return ({"fern_stage": "check", "fern_exit": result["check_exit"], "fern_log": result["check_log"],
                 "classes": ",".join(check_classes)}, check_found, check_unmatched)
    gen_classes, _gen_found, gen_unmatched = classify(diagnostics(read_log(result.get("generate_log", ""))),
                                                      patterns, findings)
    refused = result["generate_exit"] != "0" or result["generate_files"] == "0" or gen_classes
    if not refused:
        return None, check_found, check_unmatched + gen_unmatched
    if check_classes:
        return ({"fern_stage": "check", "fern_exit": result["check_exit"], "fern_log": result["check_log"],
                 "classes": ",".join(check_classes)}, check_found, check_unmatched)
    return ({"fern_stage": "generate", "fern_exit": result["generate_exit"], "fern_log": result["generate_log"],
             "classes": ",".join(gen_classes)}, check_found, gen_unmatched)


def tables() -> tuple[dict[str, str], list[str]]:
    """Every table `build` writes, by file name, and every problem that stops it."""
    problems: list[str] = []
    classes = read_tsv(REGISTRY / "classes.tsv", CLASSES_HEADER)
    findings = read_tsv(REGISTRY / "findings.tsv", FINDINGS_HEADER)
    patterns = class_patterns(classes)
    near = finding_patterns(findings)
    measured = read_measurements()
    documents: dict[str, dict[str, str]] = {}
    generated: dict[str, dict[str, str]] = {}
    unretrievable: list[dict[str, str]] = []
    counts: dict[str, int] = {row["class"]: 0 for row in classes}
    evaluated = {row["class"] for row in classes if row["status"] != "unevaluated"}
    for entry in population():
        records = ";".join(sorted(entry["records"]))
        result = measured.get(entry["key"])
        missing = missing_measurements(result) - {"crozier-strict"} if result is not None else {"any"}
        if missing:
            problems.append(f"{entry['key']}: not measured ({', '.join(sorted(missing))}); "
                            "run `just fern-refusals-measure`")
            continue
        identity = {"source": entry["source"], "locator": entry["locator"] or EMPTY,
                    "revision": entry["revision"] or EMPTY, "recorded_by": records}
        if result["unretrievable"]:
            # A record that never located its document is named by the record itself.
            unretrievable.append(dict(identity, locator=entry["locator"] or entry["key"],
                                      digest=entry["digest"] or EMPTY, reason=result["unretrievable"]))
            continue
        for log in (result["check_log"], result["generate_log"]):
            if log and not (REPO / log).is_file():
                problems.append(f"{entry['key']}: its Fern log {log} is missing; restore it from git, or "
                                "take the document again with `measure --again`")
        refusal, found, unmatched = verdict(result, patterns, near)
        digest = result["digest"]
        problems += [f"{digest}: no single class or finding matches {message}; add a classes.tsv or "
                     "findings.tsv row for the phrase, or narrow the template that overlaps it"
                     for message in unmatched]
        table = documents if refusal else generated
        if digest in table:
            kept = table[digest]
            kept["recorded_by"] = ";".join(sorted(set(kept["recorded_by"].split(";")) | set(entry["records"])))
            continue
        if refusal is None:
            generated[digest] = dict(identity, digest=digest, fern_log=result["check_log"] or result["generate_log"],
                                     findings=",".join(found) or EMPTY)
            continue
        if not refusal["classes"]:
            problems.append(f"{digest}: Fern refuses it, but {refusal['fern_log']} carries no refusal class; "
                            "add a class for the phrase that stopped it")
        names = list(filter(None, refusal["classes"].split(",")))
        for name in names:
            counts[name] += 1
        strict = EMPTY
        if evaluated.intersection(names):
            # `—` until one of the document's classes is evaluated.
            strict = result["crozier_strict_exit"]
            if not strict:
                problems.append(f"{entry['key']}: not measured (crozier-strict); "
                                "run `just fern-refusals-measure`")
                continue
        documents[digest] = dict(identity, digest=digest, **refusal, crozier_exit=result["crozier_exit"],
                                 crozier_files=result["crozier_files"], crozier_strict_exit=strict)
    for row in classes:
        row["documents"] = str(counts[row["class"]])
    return ({"documents.tsv": tsv_text(DOCUMENTS_HEADER, (documents[key] for key in sorted(documents))),
             "generated.tsv": tsv_text(GENERATED_HEADER, (generated[key] for key in sorted(generated))),
             "unretrievable.tsv": tsv_text(UNRETRIEVABLE_HEADER, sorted(unretrievable, key=lambda row: (
                 row["source"], row["locator"], row["recorded_by"]))),
             "classes.tsv": tsv_text(CLASSES_HEADER, classes)}, problems)


def build(_args: argparse.Namespace) -> int:
    written, problems = tables()
    if problems:
        fail("cannot build the tables:\n  " + "\n  ".join(problems))
    for name, text in written.items():
        (REGISTRY / name).write_text(text, encoding="utf-8")
    counts = {name: text.count("\n") - 1 for name, text in written.items()}
    print(f"fern-refusals: {counts['documents.tsv']} refused, {counts['generated.tsv']} generated, "
          f"{counts['unretrievable.tsv']} unretrievable")
    return 0


def cross_reference_problems() -> list[str]:
    """The committed tables against each other and the tree: sort orders, class
    ids, counts, and the logs `documents.tsv` names."""
    problems = []
    classes = read_tsv(REGISTRY / "classes.tsv", CLASSES_HEADER)
    documents = read_tsv(REGISTRY / "documents.tsv", DOCUMENTS_HEADER)
    names = [row["class"] for row in classes]
    if names != sorted(set(names)):
        problems.append("classes.tsv: rows are sorted by class with no class twice")
    digests = [row["digest"] for row in documents]
    if digests != sorted(set(digests)):
        problems.append("documents.tsv: rows are sorted by digest with no digest twice")
    carried: dict[str, int] = {}
    for row in documents:
        ids = [id for id in row["classes"].split(",") if id]
        if not ids:
            problems.append(f"documents.tsv {row['digest']}: carries no class")
        for id in ids:
            if id not in names:
                problems.append(f"documents.tsv {row['digest']}: class `{id}` is not a classes.tsv row")
            carried[id] = carried.get(id, 0) + 1
        if not (REPO / row["fern_log"]).is_file():
            problems.append(f"documents.tsv {row['digest']}: its fern_log {row['fern_log']} is not committed")
    for row in classes:
        if row["documents"] != str(carried.get(row["class"], 0)):
            problems.append(f"classes.tsv {row['class']}: documents is {row['documents']}, but "
                            f"{carried.get(row['class'], 0)} documents.tsv row(s) carry it")
    return problems


def publisher(locator: str) -> str:
    """Who published a document: the API under an aggregation's tree, else the
    repository owner, lower-cased and without a domain suffix (`Adyen` and
    `adyen.com` are one publisher)."""
    return re.sub(r"\.(com|io|org|net|dev|co|de|app|ai)$", "", _publisher(locator).lower())


def _publisher(locator: str) -> str:
    parts = urllib.parse.urlparse(locator).path.strip("/").split("/")
    if parts[:2] in (["APIs-guru", "openapi-directory"], ["jentic", "jentic-public-apis"]):
        tree = parts[3:]
        tree = tree[2:] if tree[:2] == ["apis", "openapi"] else tree[1:]
        return tree[0] if tree else parts[0]
    return parts[1] if urllib.parse.urlparse(locator).hostname == "api.apis.guru" and len(parts) > 3 \
        else parts[0]


def confirmation_holds(row: dict[str, str], pattern: re.Pattern[str]) -> bool:
    """Whether a real document's generation reproduces the refusal its class's probe measured."""
    return row["generate_exit"] != "0" or row["generate_files"] == "0" or any(
        pattern.match(message) for message in diagnostics(read_log(row["generate_log"])))


def confirm(args: argparse.Namespace) -> int:
    """Run `fern generate` on up to `--per-class` real documents carrying each class.

    A document's generation is otherwise not run once its check names a class:
    each class's probe shows the class stopping a generation. This samples the
    population to confirm it — documents carrying only that class first, from
    publishers not yet sampled, smallest first — reusing a generation `measure`
    already took. The results land in `confirmations.tsv`, which `check` holds.
    """
    documents = read_tsv(REGISTRY / "documents.tsv", DOCUMENTS_HEADER)
    classes = read_tsv(REGISTRY / "classes.tsv", CLASSES_HEADER)
    measured = {row["digest"]: row for row in read_measurements().values() if row["digest"]}
    cached = {path.stem: path for path in (CACHE / "documents").glob("*") if path.is_file()}
    path = confirmations_path()
    kept = read_tsv(path, CONFIRMATIONS_HEADER) if path.is_file() else []
    plan: list[tuple[str, dict[str, str]]] = []
    for row in classes:
        name = row["class"]
        done = [confirmed for confirmed in kept if confirmed["class"] == name]
        carrying = [doc for doc in documents if name in doc["classes"].split(",") and doc["digest"] in cached]
        carrying.sort(key=lambda doc: (doc["classes"] != name, doc["digest"] not in measured
                                       or not measured[doc["digest"]]["generate_exit"],
                                       cached[doc["digest"]].stat().st_size))
        publishers = {confirmed["publisher"] for confirmed in done}
        chosen = {confirmed["digest"] for confirmed in done}
        for doc in carrying:
            if len(done) + sum(1 for planned, _ in plan if planned == name) >= args.per_class:
                break
            who = publisher(doc["locator"])
            if who in publishers or doc["digest"] in chosen:
                continue
            publishers.add(who)
            chosen.add(doc["digest"])
            plan.append((name, dict(doc, publisher=who)))

    def one(item: tuple[str, dict[str, str]]) -> dict[str, str]:
        name, doc = item
        digest = doc["digest"]
        previous = measured.get(digest, {})
        result = {key: previous[key] for key in ("generate_exit", "generate_files", "generate_log")} \
            if previous.get("generate_exit") else fern_generate(cached[digest], digest, args.timeout)
        return {"class": name, "digest": digest, "publisher": doc["publisher"], **result}

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        kept += list(pool.map(one, plan))
    kept.sort(key=lambda row: (row["class"], row["digest"]))
    path.write_text(tsv_text(CONFIRMATIONS_HEADER, kept), encoding="utf-8")
    print(f"fern-refusals: {len(plan)} confirmation(s) taken, {len(kept)} on record")
    return 0


def confirmations_path() -> Path:
    # The tests point this at a scratch copy to show `check` failing on a contradiction.
    return Path(os.environ.get("CROZIER_FERN_REFUSALS_CONFIRMATIONS") or EVIDENCE / "confirmations.tsv")


def confirmation_problems() -> list[str]:
    """Every class carried by a document has a sampled real generation, and each reproduces the refusal."""
    path = confirmations_path()
    if not path.is_file():
        return [f"{rel(path)} is missing; run `scripts/fern-refusals.py confirm`"]
    confirmations = read_tsv(path, CONFIRMATIONS_HEADER)
    classes = read_tsv(REGISTRY / "classes.tsv", CLASSES_HEADER)
    documents = {row["digest"]: row for row in read_tsv(REGISTRY / "documents.tsv", DOCUMENTS_HEADER)}
    patterns = {candidate.name: candidate.pattern for candidate in class_patterns(classes)}
    problems = []
    for row in confirmations:
        doc = documents.get(row["digest"])
        if row["class"] not in patterns or doc is None or row["class"] not in doc["classes"].split(","):
            problems.append(f"confirmations.tsv {row['class']} {row['digest']}: names no documents.tsv row "
                            "carrying that class; rerun `confirm` after `build`")
        elif not (REPO / row["generate_log"]).is_file():
            problems.append(f"confirmations.tsv {row['digest']}: its log {row['generate_log']} is not committed")
        elif not confirmation_holds(row, patterns[row["class"]]):
            problems.append(f"{row['class']}: Fern generates from {row['digest']} (exit 0, "
                            f"{row['generate_files']} files), contradicting the class's probe; measure the "
                            "class again, or make the phrase a finding")
    for row in classes:
        if row["documents"] != "0" and not any(confirmed["class"] == row["class"] for confirmed in confirmations):
            problems.append(f"{row['class']}: no real document's generation confirms it; run "
                            "`scripts/fern-refusals.py confirm`")
    return problems


def check(_args: argparse.Namespace) -> int:
    problems = []
    for name, header in (("classes.tsv", CLASSES_HEADER), ("documents.tsv", DOCUMENTS_HEADER),
                         ("generated.tsv", GENERATED_HEADER), ("unretrievable.tsv", UNRETRIEVABLE_HEADER),
                         ("findings.tsv", FINDINGS_HEADER)):
        path = REGISTRY / name
        first = path.read_text(encoding="utf-8").split("\n", 1)[0] if path.is_file() else ""
        if first != "\t".join(header):
            problems.append(f"docs/fern-refusals/{name}: the header must be exactly {chr(9).join(header)!r}")
    if problems:
        fail("\n  ".join(["the registry drifted from its contract:", *problems]))
    problems = cross_reference_problems() + confirmation_problems()
    if problems:
        fail("\n  ".join(["the registry's tables disagree with each other "
                          "(run `scripts/fern-refusals.py build`, or restore the hand-edited one from git):",
                          *problems]))
    written, problems = tables()
    for name, text in written.items():
        if (REGISTRY / name).read_text(encoding="utf-8") != text:
            problems.append(f"docs/fern-refusals/{name} differs from what `build` writes; "
                            "run `scripts/fern-refusals.py build` and commit the result")
    if problems:
        fail("\n  ".join(["the registry drifted from its inputs:", *problems]))
    return 0


def probe(args: argparse.Namespace) -> int:
    """Measure Fern on each named class's `probe.yml` and write its `fern-refusal.txt`.

    `fern check`, then `fern generate` whatever the check said, so the record's
    `generate_exit` is always the generation's own. The class's `fern_stage` and
    `fern_exit` in `classes.tsv` are the stage whose output carries the class's
    phrase and that stage's exit. A probe Fern generates from cleanly is no
    refusal class, and this fails rather than record it.
    """
    classes = read_tsv(REGISTRY / "classes.tsv", CLASSES_HEADER)
    by_name = {row["class"]: row for row in classes}
    patterns = {candidate.name: candidate.pattern for candidate in class_patterns(classes)}
    missing = [name for name in args.cls if name not in by_name]
    if missing:
        fail(f"no classes.tsv row for {', '.join(missing)}; add the row first")

    def one(name: str) -> tuple[str, dict[str, str]]:
        check_exit, check_log, generate_exit, generate_log, tree = fern_probe(
            REGISTRY / name / "probe.yml", name, args.timeout)
        logs = EVIDENCE / "probe-logs"
        pattern = patterns[name]
        stage = next((stage for stage, log in (("check", check_log), ("generate", generate_log))
                      if any(pattern.match(message) for message in diagnostics(log))), "")
        if not stage:
            fail(f"{name}: Fern printed no diagnostic matching its template over the probe "
                 f"(check exit {check_exit}, generate exit {generate_exit}); see {rel(logs)}/{name}.*.log")
        phrase = next(message for message in diagnostics(check_log if stage == "check" else generate_log)
                      if pattern.match(message))
        exit_of_stage = check_exit if stage == "check" else generate_exit
        if exit_of_stage != generate_exit:
            fail(f"{name}: the {stage} stage exits {exit_of_stage} but the generation {generate_exit}, "
                 f"writing {len(tree)} files; a phrase Fern still generates past is a finding "
                 "(findings.tsv), not a class")
        python = [path for path in tree if path.suffix == ".py"]
        # A false success writes a tree from a document Fern never parsed.
        output_tree = f"{len(tree)} files, {len(python)} Python" + (
            ", from a document Fern did not parse" if generate_exit == "0" else "") if tree else "none"
        record = {"fern_cli_version": FERN_CLI, "fern_python_sdk_version": FERN_PYTHON_SDK,
                  "generate_exit": generate_exit, "diagnostic": phrase, "output_tree": output_tree}
        (REGISTRY / name / "fern-refusal.txt").write_text(
            "".join(f"{field}: {value}\n" for field, value in record.items()), encoding="utf-8")
        return name, {"fern_stage": stage, "fern_exit": exit_of_stage}

    results: dict[str, dict[str, str]] = {}
    problems: list[str] = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for name, future in [(name, pool.submit(one, name)) for name in args.cls]:
            try:
                results.update([future.result()])
            except SystemExit:
                problems.append(name)
    for row in classes:
        row.update(results.get(row["class"], {}))
    (REGISTRY / "classes.tsv").write_text(tsv_text(CLASSES_HEADER, classes), encoding="utf-8")
    if problems:
        fail(f"{len(problems)} probe(s) not recorded, each explained above: {', '.join(problems)}")
    print(f"fern-refusals: {len(results)} probe(s) recorded")
    return 0


def fern_probe(document: Path, name: str, timeout: int) -> tuple[str, str, str, str, list[Path]]:
    """`fern check` and `fern generate` over a probe; both logs kept under `probe-logs/`."""
    with tempfile.TemporaryDirectory(prefix="fern-refusals-probe-") as scratch:
        workspace = Path(scratch) / "fern"
        fern_workspace(document, workspace)
        check_exit, check_log = fern_run(["fern", "check"], workspace, timeout)
        preview = Path(scratch) / "preview"
        generate_exit, generate_log = fern_run(
            ["fern", "generate", "--group", "python-sdk", "--local", "--preview", "--output", str(preview),
             "--force"], workspace, timeout)
        tree = sorted(path.relative_to(preview) for path in preview.rglob("*") if path.is_file()) \
            if preview.is_dir() else []
    logs = EVIDENCE / "probe-logs"
    logs.mkdir(parents=True, exist_ok=True)
    (logs / f"{name}.check.log").write_text(scrub(check_log), encoding="utf-8")
    (logs / f"{name}.generate.log").write_text(scrub(generate_log), encoding="utf-8")
    return check_exit, check_log, generate_exit, generate_log, tree


def finding(args: argparse.Namespace) -> int:
    """Measure Fern on each named finding's probe and record its exits in `findings.tsv`.

    A finding is a shape Fern generates from: `check-only` when its check
    refuses a phrase the generation writes an SDK past, `generates` when neither
    stage objects. Either way the generation must exit 0 with a tree, or it is
    no finding.
    """
    findings = read_tsv(REGISTRY / "findings.tsv", FINDINGS_HEADER)
    by_name = {row["finding"]: row for row in findings}
    missing = [name for name in args.name if name not in by_name]
    if missing:
        fail(f"no findings.tsv row for {', '.join(missing)}; add the row first")

    def one(name: str) -> None:
        row = by_name[name]
        check_exit, check_log, generate_exit, _log, tree = fern_probe(REPO / row["probe"], name, args.timeout)
        if generate_exit != "0" or not tree:
            fail(f"{name}: the generation exits {generate_exit} with {len(tree)} files, so Fern refuses the "
                 "probe; a refusal is a class, not a finding")
        if row["kind"] == "check-only" and not any(
                template_pattern(row["diagnostic"]).match(message) for message in diagnostics(check_log)):
            fail(f"{name}: `fern check` printed no diagnostic matching its template; correct the template "
                 f"or the probe, reading {rel(EVIDENCE / 'probe-logs')}/{name}.check.log")
        row.update(check_exit=check_exit, generate_exit=generate_exit)

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        list(pool.map(one, args.name))
    (REGISTRY / "findings.tsv").write_text(tsv_text(FINDINGS_HEADER, findings), encoding="utf-8")
    print(f"fern-refusals: {len(args.name)} finding(s) recorded")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("select", help="print the selected population").set_defaults(run=select)
    m = sub.add_parser("measure", help="fetch, run Fern and crozier, record measurements.jsonl")
    m.add_argument("--jobs", type=int, default=6)
    m.add_argument("--timeout", type=int, default=3600)
    m.add_argument("--limit", type=int, default=0)
    m.add_argument("--again", action="store_true", help="re-measure documents already on record")
    m.add_argument("--root", type=Path, action="append", default=[],
                   help="another directory whose files may supply a document by digest")
    m.set_defaults(run=measure)
    p = sub.add_parser("probe", help="measure Fern on classes' probes and write their fern-refusal.txt")
    p.add_argument("cls", nargs="+", metavar="CLASS")
    p.add_argument("--jobs", type=int, default=6)
    p.add_argument("--timeout", type=int, default=900)
    p.set_defaults(run=probe)
    f = sub.add_parser("finding", help="measure Fern on findings' probes and record their exits")
    f.add_argument("name", nargs="+", metavar="FINDING")
    f.add_argument("--jobs", type=int, default=6)
    f.add_argument("--timeout", type=int, default=900)
    f.set_defaults(run=finding)
    c = sub.add_parser("confirm", help="sample each class's real documents through fern generate")
    c.add_argument("--per-class", type=int, default=3)
    c.add_argument("--jobs", type=int, default=6)
    c.add_argument("--timeout", type=int, default=3600)
    c.set_defaults(run=confirm)
    sub.add_parser("build", help="rewrite the tables from the committed inputs").set_defaults(run=build)
    sub.add_parser("check", help="fail when the tables drift from the inputs").set_defaults(run=check)
    args = parser.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main())
