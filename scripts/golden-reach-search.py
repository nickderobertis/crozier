#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo crate driven by `just`, with no Nx workspace; this arm-search script sits in scripts/ beside golden-reach.py, whose ledger it reads, and the witness-search scripts whose acquirer it drives.
"""Search the six declared sources for a real-world witness of a golden row's unreached arm.

A `golden` row whose reach cell names an unreached handling site is missing an
arm: its witnesses declare the feature and never send crozier down that site. A
witness for the arm is a real-world document that declares the row's census
selector **and** executes the site. The census decides the first half, exactly as
Contract B requires; the second half is not a selector, so it is decided the same
way the reach cell was: by running the instrumented `crozier` over the document
and reading which of the row's unreached sites executed.

Each subcommand does one stage and writes its evidence under
`docs/openapi-surface/golden-reach-witnesses/<source>/`, in Contract B's
`records.tsv` form (`key kind subject result file`):

* ``walk`` — an enumerable source (``apis.guru``, ``jentic``, ``vendor-portals``,
  ``github-publisher-trees``). The documents are the source's committed pinned
  listing, read from a local copy whose every byte is checked against the
  listing's SHA-256 before the census reads it. Every document goes into
  ``enumeration.tsv.gz`` — Contract B's enumeration columns — with the requested
  keys it declares, or the measured reason it could not be read. The publisher
  trees' pins name documents rather than archives, so ``fetch-pins`` first
  fetches each one with no local copy at its pinned commit.
* ``query`` — a source that takes a text query (``github-code-search``,
  ``sourcegraph``), through the existing guarded acquirer in
  `scripts/witness-search-github.py`: each phrasing in
  ``golden-reach-witnesses/queries.tsv`` is issued once, its reported count
  recorded, and its first page of results fetched at their indexed commits and
  censused. A fetched result is a ``document`` row, as a walked one is.
* ``probe`` — every declarer the two stages found, run through the instrumented
  build `just golden-reach` measures with (so, like that measurement, it runs
  outside `just check`); the row's unreached sites it executes
  go to ``probe.jsonl``. A declarer that executes one is the row's ``candidate``,
  and only a candidate owes the three screens: a declarer that never reaches the
  arm is no witness for it, however it screens.
* ``render`` — the row's search record,
  ``golden-reach-witnesses/searches/<key>.md``: one line per declared source.
  ``--build`` re-renders a committed record as of the build its probes ran on,
  keeping the arm it searched for, when its evidence moves after `src/` has.
* ``outstanding`` — every item the committed records' ``outstanding`` columns
  count, one line each with its blocker, into
  ``golden-reach-witnesses/outstanding.tsv``: the continuation's work list.

Screens are recorded by ``screen``, which takes the outcome, the evidence it
rests on and a passing candidate's disposition (``--registered`` or
``--declined``) from the caller: a licence, an immutable ref and Fern's acceptance are
each a measurement taken elsewhere (the corpus licence rule, the source's pin,
`scripts/generate-fern-fixture.sh`), and this script only files them.

Every GitHub and Sourcegraph call goes through `scripts/rate_limit_guard.py`, by
way of the acquirer; this script opens no socket of its own.
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import gzip
import hashlib
import http.client
import importlib.util
import itertools
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.parse
from collections import defaultdict
from collections.abc import Callable, Iterator
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from pathlib import Path
from types import ModuleType
from typing import Any

try:
    import fcntl
except ImportError:  # Windows: no POSIX advisory locks; see `exclusive_lock`
    fcntl = None  # type: ignore[assignment]
try:
    import msvcrt
except ImportError:
    msvcrt = None  # type: ignore[assignment]  # POSIX: no Windows locking; see `exclusive_lock`

REPO = Path(__file__).resolve().parent.parent
SURFACE = REPO / "docs" / "openapi-surface"
EVIDENCE = SURFACE / "golden-reach-witnesses"
QUERIES = EVIDENCE / "queries.tsv"
CACHE = REPO / ".local" / "golden-reach-search"
DECLARED_SOURCES = (
    "apis.guru",
    "jentic",
    "github-code-search",
    "github-publisher-trees",
    "sourcegraph",
    "vendor-portals",
)
WALKS = ("apis.guru", "jentic", "vendor-portals", "github-publisher-trees")
QUERY_SOURCES = ("github-code-search", "sourcegraph")
RECORD_FIELDS = ("key", "kind", "subject", "result", "file")
WALK_FIELDS = ("walk", "document", "revision", "sha256", "matched_keys", "status")
FIRST_PAGE = 100
# Keyword arguments every acquirer this script builds is given. A real search
# leaves them empty; the offline tests point them at a loopback server.
ACQUIRER_OPTIONS: dict[str, Any] = {}
# Probe results are filed this many declarers at a time, so a stopped run keeps them;
# some catalogue documents take minutes each under an instrumented build.
PROBE_CHUNK = 8


def _load(name: str, path: Path) -> ModuleType:
    """A sibling script imported by path: its hyphenated file name is no module name."""
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


REACH = _load("golden_reach", REPO / "scripts" / "golden-reach.py")
CENSUS = _load("openapi_surface_census", REPO / "scripts" / "openapi-surface-census.py")


def fail(message: str) -> None:
    raise SystemExit(f"golden-reach-search: {message}")


def read_tsv(path: Path, required: tuple[str, ...], remedy: str) -> list[dict[str, str]]:
    """A tab-separated file's rows, refused unless its header names every `required` column."""
    if not path.is_file():
        fail(f"{path} is missing; {remedy}")
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        missing = [column for column in required if column not in (reader.fieldnames or ())]
        if missing:
            fail(f"{path} has no {missing} column(s) (header {reader.fieldnames}); {remedy}")
        return list(reader)


def read_jsonl(path: Path, required: tuple[str, ...], remedy: str) -> list[dict[str, Any]]:
    """A JSON-lines file's objects, refused at the first line that is not one carrying `required`."""
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            fail(f"{path}:{number} is not JSON ({error.msg}); {remedy}")
        if not isinstance(row, dict) or any(field not in row for field in required):
            fail(f"{path}:{number} lacks one of {list(required)}; {remedy}")
        rows.append(row)
    return rows




def _parameterized_media_keys(document: Any) -> int:
    """Content-map keys whose every `;`-delimited segment after the type is `name=value`.

    The reading `bodies-media.md`'s `media-type-key-parameters` row states: an
    RFC 7231 media type carrying parameters, which the census names no selector
    for, so its site-table row names its witness with `fixture=` instead.
    """
    found = 0
    stack = [document]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            content = node.get("content")
            if isinstance(content, dict):
                for media in content:
                    head, _, rest = str(media).partition(";")
                    segments = [s.strip() for s in rest.split(";")] if rest else []
                    if "/" in head and segments and all(
                        "=" in s and s.split("=", 1)[0].strip() and s.split("=", 1)[1].strip()
                        for s in segments
                    ):
                        found += 1
            stack.extend(node.values())
        elif isinstance(node, list):
            stack.extend(node)
    return found


# Rows whose site table names their witnesses by `fixture=` because no census
# selector reads the shape: the search reads them with a predicate of its own,
# prefiltered on the raw bytes so a walk parses only the documents that could hold one.
PREDICATE_ROWS: dict[str, tuple[str, Callable[[Any], int]]] = {
    "media-type-key-parameters": (r"/[A-Za-z0-9.+-]+\s*;\s*[A-Za-z0-9_-]+\s*=", _parameterized_media_keys),
}


def selectors_of(key: str) -> tuple[str, ...]:
    """The census selectors a row's witnesses are read off (its site-table row)."""
    table = REACH.read_sites_table()
    if key not in table:
        fail(f"{key} is not a golden row of the site table; check the key against {REACH.SITES_TABLE.name}")
    if key in PREDICATE_ROWS:
        return (f"predicate:{key}",)
    selectors = tuple(s for s in table[key].selectors if not s.startswith("fixture="))
    if not selectors:
        fail(f"{key} names its witnesses directly; no census selector can search for it. Add it to PREDICATE_ROWS with a predicate, or give its site-table row a census selector")
    return selectors


def predicate_count(key: str, path: Path) -> int:
    """A predicate row's count over one document, 0 where its bytes cannot hold one."""
    import re

    pattern, reader = PREDICATE_ROWS[key]
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return 0
    if not re.search(pattern, text):
        return 0
    try:
        document = CENSUS.load_document(path)
    except Exception:  # a document the census cannot parse declares nothing it can read
        return 0
    if not isinstance(document, dict) or not str(document.get("openapi", "")).startswith("3"):
        return 0
    return reader(document)


def _predicate_one(args: tuple[str, str, tuple[str, ...]]) -> dict[str, int]:
    path, sha256, keys = args
    try:
        data = Path(path).read_bytes()
    except OSError:
        return {}
    if hashlib.sha256(data).hexdigest() != sha256:
        return {}
    return {key: n for key in keys for n in [predicate_count(key, Path(path))] if n}


def ledger_unreached(key: str) -> tuple[str, ...]:
    """The row's unreached handling sites in the committed ledger, none where it reaches every one."""
    for _rank, reach in REACH.read_ledger():
        if reach.key == key:
            return tuple(spec for spec, hit, _total in reach.sites if not hit)
    fail(f"{key} is not in the ledger; check the key against docs/openapi-surface/golden-reach.tsv, or re-run `just golden-reach-report`")
    raise AssertionError


def unreached_sites(key: str) -> tuple[str, ...]:
    """The row's unreached handling sites in the committed ledger — the arm searched for."""
    sites = ledger_unreached(key)
    if not sites:
        fail(f"{key} reaches every handling site; there is no arm to search for. Drop it from this search")
    return sites


def declared(counts: dict[str, int], selectors: tuple[str, ...]) -> int:
    return sum(counts.get(selector, 0) for selector in selectors)




def source_dir(source: str) -> Path:
    if source not in DECLARED_SOURCES:
        fail(f"{source} is not a declared source; it is one of {', '.join(DECLARED_SOURCES)}")
    path = EVIDENCE / source
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_records(source: str) -> list[dict[str, str]]:
    path = source_dir(source) / "records.tsv"
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if tuple(reader.fieldnames or ()) != RECORD_FIELDS:
            fail(f"{path} has header {reader.fieldnames}, not {list(RECORD_FIELDS)}; restore it from git "
                 f"(`git checkout -- {path}`) or re-file the source's stages")
        return list(reader)


def write_records(source: str, keys: set[str], rows: list[dict[str, str]]) -> None:
    """Replace `keys`' rows of one source's records.tsv, keeping every other key's."""
    replace_records(source, [row for row in read_records(source) if row["key"] not in keys] + rows)


def replace_records(source: str, rows: list[dict[str, str]]) -> None:
    """Write exactly `rows` as one source's records.tsv, one line per distinct row."""
    path = source_dir(source) / "records.tsv"
    unique = {tuple(row[f] for f in RECORD_FIELDS): row for row in rows}
    with path.open("w", encoding="utf-8", newline="") as handle:
        # Contract B's reader splits on tabs and nothing else, so a quote is text.
        writer = csv.DictWriter(
            handle, RECORD_FIELDS, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None
        )
        writer.writeheader()
        for row in sorted(unique.values(), key=lambda r: (r["key"], r["kind"], r["subject"], r["result"])):
            writer.writerow(row)


def record_guard_logs(source: str) -> None:
    """The guard's own logs: every call and wait this source's searches made.

    Contract B names each evidence file from a records row, so each log is
    filed as a `wait` row under the pseudo-key `*` it answers for. The names are
    the acquirer's, which writes them.
    """
    github = _load("witness_search_github", REPO / "scripts" / "witness-search-github.py")
    directory = source_dir(source)
    rows = []
    for name in github.GUARD_LOGS:
        path = directory / name
        if path.is_file():
            calls = sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
            rows.append({"key": "*", "kind": "wait", "subject": f"{source} guard log {name}",
                         "result": f"{calls} entries", "file": name})
    write_records(source, {"*"}, rows)




PIN_FIELDS = ("walk", "document", "revision", "blob", "sha256")
HANDOFF_FIELDS = ("golden_key", "unreached_site", "candidate_url", "immutable_ref", "sha256",
                  "licence_spdx", "fern_screen", "gap_keys")


def git_blob(data: bytes) -> str:
    """Git's own content hash of a file, which every publisher-tree pin records."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def committed_bytes(path: Path) -> bytes:
    """The bytes git committed for `path`, which is what a pin's blob hashes.

    A checkout may have converted a tracked file's line endings on the way out
    (Windows' `core.autocrlf`), so its working-tree bytes are not the blob the
    pin names. A tracked file git reads as unmodified is therefore read back from
    its own repository's index; any other file is its own bytes.
    """
    data = path.read_bytes()
    if b"\r\n" not in data:
        return data
    git = ["git", "-C", str(path.parent)]
    literal = {**os.environ, "GIT_LITERAL_PATHSPECS": "1"}
    staged = subprocess.run([*git, "ls-files", "--stage", "--", path.name],
                            capture_output=True, text=True, env=literal)
    fields = staged.stdout.split() if staged.returncode == 0 else []
    if len(fields) < 2 or fields[1] == git_blob(data):
        return data
    if subprocess.run([*git, "diff", "--quiet", "--", path.name], capture_output=True, env=literal).returncode:
        return data
    return subprocess.run([*git, "cat-file", "blob", fields[1]], capture_output=True, check=True).stdout


def pinned_listing(source: str) -> list[dict[str, str]]:
    """The source's committed pinned document listing: walk, document, revision, sha256.

    The publisher trees pin each document by commit, path and git blob; eleven of
    the shared pins carry no SHA-256 because their own read failed. `fetch-pins`
    resolves every pin to its bytes — verified against the SHA-256 where the pin
    has one and against the blob where it does not — into this directory's
    `pins.tsv`, which the walk then reads.
    """
    shared = SURFACE / f"witness-search-{source}"
    if source == "github-publisher-trees":
        resolved = source_dir(source) / "pins.tsv"
        if not resolved.is_file():
            fail("the publisher trees' pins are unresolved; run `fetch-pins` first")
        return read_tsv(resolved, PIN_FIELDS, "re-run `fetch-pins` to rewrite it")
    rows = read_tsv(shared / "acquisition-manifest.tsv", ("walk", "document", "revision", "sha256"),
                    f"restore it from git, or re-acquire {source} through its witness-search script")
    immutable = [row for row in rows if len(row["revision"]) == 40]
    if not immutable:
        fail(f"{source}'s acquisition manifest names no document at an immutable ref; re-acquire the source through its witness-search script before walking it")
    return immutable


def unreadable_reason(error: BaseException, document: str) -> str:
    """Why the census could not read a document, naming it rather than the local copy.

    The census's message leads with the absolute path of the scratch copy it read,
    which means nothing in the tree, so the pinned document's name replaces it and
    the census's reason is kept whole.
    """
    message = str(error)
    if isinstance(error, CENSUS.DocumentError):
        message = f"line {error.line}: {message.split(f'{error.path}:{error.line}: ', 1)[-1]}"
    return f"unreadable: {type(error).__name__}: {document}: {message}"


def _census_one(args: tuple[str, str, str, tuple[tuple[str, tuple[str, ...]], ...]]) -> dict[str, str]:
    path, sha256, document, keys = args
    try:
        data = Path(path).read_bytes()
    except OSError as error:
        return {"status": f"unreadable: no local copy ({error.strerror})", "matched_keys": ""}
    if hashlib.sha256(data).hexdigest() != sha256:
        return {"status": "unreadable: local bytes differ from the pinned SHA-256", "matched_keys": ""}
    try:
        parsed = CENSUS.load_document(Path(path))
    except Exception as error:  # the census's own parse refusal, whatever its type
        return {"status": unreadable_reason(error, document), "matched_keys": ""}
    if not isinstance(parsed, dict) or not str(parsed.get("openapi", "")).startswith("3"):
        return {"status": "readable", "matched_keys": "", "counts": "{}"}
    try:
        counts = CENSUS.census_document(parsed, root_path=Path(path))
    except Exception as error:
        return {"status": unreadable_reason(error, document), "matched_keys": ""}
    matched = {key: declared(counts, selectors) for key, selectors in keys}
    return {
        "status": "readable",
        "matched_keys": ",".join(key for key, n in matched.items() if n),
        "counts": json.dumps({key: n for key, n in matched.items() if n}),
    }


def _precomputed(
    path: Path, listing: list[dict[str, str]], keys: tuple[tuple[str, tuple[str, ...]], ...]
) -> list[dict[str, str]]:
    """Results from a census already taken over this listing's pinned bytes.

    Each line is `{document, sha256_ok, status, census}` as the walk census writes
    it: `sha256_ok` is the local copy's digest checked against the listing, and
    `census` the engine's nonzero selector counts over the parsed document.
    """
    taken = {}
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            try:
                row = json.loads(line)
            except json.JSONDecodeError as error:
                fail(f"{path}:{number} is not JSON ({error.msg}); take the walk census again, or walk without --census")
            census = (row.get("census") or {}) if isinstance(row, dict) else None
            if (
                not isinstance(row, dict)
                or not isinstance(row.get("document"), str)
                or not isinstance(row.get("error", ""), str)
                or not isinstance(census, dict)
                or not all(isinstance(n, int) for n in census.values())
            ):
                fail(f"{path}:{number} is not `{{document, sha256_ok, status, census}}` with a string `error` "
                     "and a selector-count `census`; take the walk census again, or walk without --census")
            taken[row["document"]] = row
    out = []
    for row in listing:
        found = taken.get(row["document"])
        if found is None or found.get("local") == "missing":
            out.append({"status": "unreadable: no local copy", "matched_keys": ""})
        elif found.get("sha256_ok") is False:
            out.append({"status": "unreadable: local bytes differ from the pinned SHA-256", "matched_keys": ""})
        elif "error" in found:
            # A parse refusal (`DocumentError: …`) is worth reading again for its
            # whole reason; a census that ran out of time is not.
            refusal = bool(re.match(r"\w+: ", found["error"]))
            out.append({"status": f"unreadable: {found['error']}", "matched_keys": "",
                        "census_error": "1" if refusal else ""})
        else:
            # Only an OpenAPI 3 document is one crozier generates from; a Swagger 2
            # one is read, and declares nothing this search can use.
            counts = (found.get("census") or {}) if str(found.get("openapi", "")).startswith("3") else {}
            matched = {key: declared(counts, selectors) for key, selectors in keys}
            out.append({
                "status": "readable",
                "matched_keys": ",".join(key for key, n in matched.items() if n),
                "counts": json.dumps({key: n for key, n in matched.items() if n}),
            })
    return out


def locate(source: str, root: Path, row: dict[str, str], by_digest: dict[str, Path]) -> Path:
    if source == "github-publisher-trees":
        return by_digest.get(row["sha256"], root / "missing")
    return root / row["document"]


def walk(args: argparse.Namespace) -> int:
    source = args.source
    if source not in WALKS:
        fail(f"{source} is not enumerable; `query` it instead")
    keys = tuple((key, selectors_of(key)) for key in args.key)
    listing = pinned_listing(source)
    by_digest: dict[str, Path] = {}
    if source == "github-publisher-trees":
        for path in args.root.rglob("*"):
            if path.is_file() and path.suffix in (".json", ".yaml", ".yml"):
                by_digest.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(), path)
    jobs = [
        (str(locate(source, args.root, row, by_digest)), row["sha256"], row["document"], keys)
        for row in listing
    ]
    if args.census:
        results = _precomputed(args.census, listing, keys)
        # A precomputed census keeps only the head of a parse error; the document
        # it could not read is read again here for the whole reason.
        again = [index for index, result in enumerate(results) if result.get("census_error")]
        with ProcessPoolExecutor(max_workers=args.jobs) as pool:
            for index, result in zip(again, pool.map(_census_one, [jobs[i] for i in again])):
                results[index] = result
    else:
        with ProcessPoolExecutor(max_workers=args.jobs) as pool:
            results = list(pool.map(_census_one, jobs, chunksize=16))
    predicate_keys = tuple(key for key, _ in keys if key in PREDICATE_ROWS)
    if predicate_keys:
        jobs = [(str(locate(source, args.root, row, by_digest)), row["sha256"], predicate_keys) for row in listing]
        with ProcessPoolExecutor(max_workers=args.jobs) as pool:
            extra = list(pool.map(_predicate_one, jobs, chunksize=64))
        for result, found in zip(results, extra):
            if not found or result["status"] != "readable":
                continue
            counts = {**json.loads(result.get("counts") or "{}"), **found}
            result["counts"] = json.dumps(counts)
            result["matched_keys"] = ",".join(counts)
    out = source_dir(source) / "enumeration.tsv.gz"
    records: list[dict[str, str]] = []
    walks: dict[tuple[str, str], int] = defaultdict(int)
    with gzip.open(out, "wt", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, WALK_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row, result in zip(listing, results):
            walks[(row["walk"], row["revision"])] += 1
            writer.writerow({**{f: row[f] for f in ("walk", "document", "revision", "sha256")},
                             "matched_keys": result["matched_keys"], "status": result["status"]})
            counts = json.loads(result.get("counts") or "{}")
            for key, count in counts.items():
                records.append({"key": key, "kind": "document", "subject": row["document"],
                                "result": f"census {count}", "file": out.name})
    listing_file = "pins.tsv" if source == "github-publisher-trees" else out.name
    for key, _selectors in keys:
        for (tree, revision), count in sorted(walks.items()):
            records.append({"key": key, "kind": "walk", "subject": f"{tree}@{revision}",
                            "result": str(count), "file": listing_file})
    requested = {key for key, _ in keys}
    kept = [r for r in read_records(source) if r["key"] in requested and r["kind"] not in ("walk", "document")]
    write_records(source, requested, kept + records)
    unreadable = sum(1 for r in results if r["status"] != "readable")
    print(f"golden-reach-search: {source}: {len(listing)} documents walked, {unreadable} unreadable")
    return 0



def fetch_pins(args: argparse.Namespace) -> int:
    """Resolve every publisher-tree pin to bytes read at its pinned commit.

    A pin with a local copy under `--root` is matched by its SHA-256, or by its
    git blob where the pin has no SHA-256, each taken over the copy's committed
    bytes; any other is fetched through the acquirer's exact-commit raw route,
    whose calls land in this source's evidence directory, and kept only if it is
    the pinned blob. A copy whose checkout converted its line endings has its
    committed bytes written beside the fetched ones, where a walk finds them by
    digest. The result is `pins.tsv`.
    """
    source = "github-publisher-trees"
    github = _load("witness_search_github", REPO / "scripts" / "witness-search-github.py")
    acquirer = github.Acquirer(source_dir(source), cache=CACHE / source, **ACQUIRER_OPTIONS)
    by_sha: dict[str, tuple[Path, bytes]] = {}
    by_blob: dict[str, tuple[Path, bytes]] = {}
    for path in args.root.rglob("*"):
        if path.is_file() and path.suffix in (".json", ".yaml", ".yml"):
            data = committed_bytes(path)
            by_sha.setdefault(hashlib.sha256(data).hexdigest(), (path, data))
            by_blob.setdefault(git_blob(data), (path, data))
    target = args.root / "fetched"
    target.mkdir(parents=True, exist_ok=True)
    shared = SURFACE / f"witness-search-{source}" / "documents.jsonl"
    resolved, fetched, missing = [], 0, 0
    seen: set[tuple[str, str, str]] = set()
    pins = read_jsonl(shared, ("repository", "path", "commit", "blob"),
                      "restore it from git; it is the publisher trees' committed pin list")
    for pin in pins:
        # The shared pin lists a few documents twice over, word for word; a walk
        # reads each document once.
        identity = (pin["repository"], pin["path"], pin["commit"])
        if identity in seen:
            continue
        seen.add(identity)
        found = by_sha.get(pin.get("sha256", "")) or by_blob.get(pin["blob"])
        local, data = found if found else (None, b"")
        if local is not None and data != local.read_bytes():
            local = target / (pin["blob"] + Path(pin["path"]).suffix)
            local.write_bytes(data)
        if local is None:
            url = f"{acquirer.raw_github_url}/{pin['repository']}/{pin['commit']}/{urllib.parse.quote(pin['path'])}"
            status, data = acquirer.raw_github_get(url, "*", f"{pin['repository']}:{pin['path']}")
            if status == 200 and git_blob(data) == pin["blob"]:
                local = target / (pin["blob"] + Path(pin["path"]).suffix)
                local.write_bytes(data)
                fetched += 1
        sha256 = hashlib.sha256(data).hexdigest() if local else ""
        if pin.get("sha256") and sha256 and sha256 != pin["sha256"]:
            fail(f"{pin['path']}: the blob matches but the SHA-256 differs from the pin; delete {local} and re-run `fetch-pins`")
        missing += not sha256
        resolved.append({"walk": pin["repository"], "document": pin["path"], "revision": pin["commit"],
                         "blob": pin["blob"], "sha256": sha256})
    with (source_dir(source) / "pins.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, PIN_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(resolved)
    record_guard_logs(source)
    print(f"golden-reach-search: {source}: {len(resolved)} pins, {fetched} fetched, {missing} unresolved")
    return 0




def phrasings(key: str, source: str) -> list[str]:
    rows = [
        r for r in read_tsv(QUERIES, ("key", "source", "phrasing"), "restore it from git")
        if r["key"] == key and r["source"] == source
    ]
    found = [r["phrasing"] for r in rows]
    if len(found) < 2 or len(set(found)) != len(found):
        fail(f"{QUERIES.name} owes {key} two distinct phrasings for {source}; add them there before querying")
    return found


def _quoted(url: str) -> str:
    """A contents URL with its path percent-encoded: result paths may hold a space."""
    parts = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit(parts._replace(path=urllib.parse.quote(urllib.parse.unquote(parts.path))))


def _fetch(read: Callable[..., dict[str, Any]], *args: Any) -> dict[str, Any]:
    """One result's acquisition, a failure to read it recorded rather than raised."""
    try:
        return read(*args)
    except (OSError, ValueError, http.client.HTTPException) as error:
        item = args[-1]
        return {"disposition": "acquisition-failure", "diagnostic": f"{type(error).__name__}: {error}",
                "repository": (item.get("repository") or {}).get("full_name")
                if isinstance(item.get("repository"), dict) else item.get("repository"),
                "path": item.get("path"), "commit": item.get("commit")}


# `acquirer` is `scripts/witness-search-github.py`'s `Acquirer`, loaded from a
# hyphenated file by path, so there is no importable name to annotate it with.
def _one_query(acquirer: Any, source: str, key: str, phrasing: str, selectors: tuple[str, ...],
               new: list[dict[str, str]]) -> tuple[list[dict[str, Any]] | None, int]:
    """Issue one phrasing; its reported count and its first page's documents, or None if refused."""
    if source == "github-code-search":
        path = "/search/code?" + urllib.parse.urlencode(
            {"q": phrasing, "per_page": FIRST_PAGE, "page": 1}
        )
        status, payload, _ = acquirer.github_json("code_search", path)
        if status != 200:
            new.append({"key": key, "kind": "query", "subject": phrasing,
                        "result": f"unanswered: HTTP {status} refused", "file": "queries.jsonl"})
            acquirer.write("queries.jsonl", {"source": source, "key": key, "query": phrasing,
                                             "outcome": "refused", "status": status})
            return None, 0
        total = payload.get("total_count") if isinstance(payload, dict) else None
        items = payload.get("items") if isinstance(payload, dict) else None
        if not isinstance(total, int) or not isinstance(items, list) or not all(
            isinstance(item, dict) and isinstance(item.get("url"), str) for item in items
        ):
            new.append({"key": key, "kind": "query", "subject": phrasing,
                        "result": "unanswered: HTTP 200 carried no `total_count` and `items` list", "file": "queries.jsonl"})
            acquirer.write("queries.jsonl", {"source": source, "key": key, "query": phrasing,
                                             "outcome": "malformed", "status": status})
            return None, 0
        items = items[:FIRST_PAGE]
        acquirer.write("queries.jsonl", {"source": source, "key": key, "query": phrasing,
                                         "outcome": "answered", "result_count": total,
                                         "retrieved": len(items)})
        fetched = [
            _fetch(acquirer.github_document, key, {**item, "selector": selectors[0], "url": _quoted(item["url"])})
            for item in items
        ]
    else:
        items = acquirer.sourcegraph_search(key, phrasing) or []
        total = len(items)
        acquirer.write("queries.jsonl", {"source": source, "key": key, "query": phrasing,
                                         "outcome": "answered", "result_count": total,
                                         "retrieved": min(total, FIRST_PAGE)})
        fetched = [_fetch(acquirer.sourcegraph_document, key, selectors[0], item) for item in items[:FIRST_PAGE]]
    return fetched, total



def query(args: argparse.Namespace) -> int:
    source = args.source
    if source not in QUERY_SOURCES:
        fail(f"{source} takes no text query; `walk` it instead")
    github = _load("witness_search_github", REPO / "scripts" / "witness-search-github.py")
    directory = source_dir(source)
    acquirer = github.Acquirer(directory, cache=CACHE / source, **ACQUIRER_OPTIONS)
    new: list[dict[str, str]] = []
    index_path = CACHE / source / "candidate-documents.json"
    index = candidate_index(source)
    for key in args.key:
        selectors = selectors_of(key)
        for phrasing in phrasings(key, source):
            try:
                fetched, total = _one_query(acquirer, source, key, phrasing, selectors, new)
            except github.SearchStopped as error:
                new.append({"key": key, "kind": "query", "subject": phrasing,
                            "result": f"unanswered: {error}", "file": "queries.jsonl"})
                continue
            if fetched is None:
                continue
            new.append({"key": key, "kind": "query", "subject": phrasing, "result": str(total),
                        "file": "queries.jsonl"})
            for document in fetched:
                candidate = f"{document.get('repository')}:{document.get('path')}@{document.get('commit')}"
                if document.get("document"):
                    index[candidate] = document["document"]
                readable = ("declares", "does-not-declare", "excluded-non-openapi-3")
                if key in PREDICATE_ROWS:
                    # The acquirer's own verdict is the census's, which names no
                    # selector for a predicate row, so it reads `selector-unavailable`.
                    readable += ("selector-unavailable",)
                if document.get("disposition") in readable:
                    local = CACHE / source / "documents" / document["document"]
                    if document.get("disposition") == "excluded-non-openapi-3":
                        count = 0
                    elif key in PREDICATE_ROWS:
                        count = predicate_count(key, local)
                    else:
                        try:
                            count = declared(CENSUS.census_document(CENSUS.load_document(local)), selectors)
                        except Exception as error:  # the census's own parse refusal, whatever its type
                            count = None
                            result = unreadable_reason(error, candidate)
                    if count is not None:
                        result = f"census {count}"
                else:
                    result = f"acquisition-failure: {document.get('disposition')}"
                new.append({"key": key, "kind": "document", "subject": candidate, "result": result,
                            "file": "candidates.jsonl"})
        # Filed key by key, so a search stopped part-way keeps every key it finished.
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(json.dumps(index, sort_keys=True, indent=0), encoding="utf-8")
        mine = [r for r in new if r["key"] == key]
        kept = [r for r in read_records(source) if r["key"] == key and r["kind"] in ("screen", "candidate")]
        write_records(source, {key}, kept + _dedupe(mine))
        record_guard_logs(source)
    keys = set(args.key)
    print(f"golden-reach-search: {source}: {len(new)} records for {len(keys)} key(s)")
    return 0


def candidate_index(source: str) -> dict[str, str]:
    """A query source's cache index: each fetched candidate to its cached document's name."""
    path = CACHE / source / "candidate-documents.json"
    if not path.is_file():
        return {}
    try:
        index = json.loads(path.read_text(encoding="utf-8"))
    except ValueError as error:
        fail(f"{path} is not JSON ({error}); delete it and re-run `query` for {source}")
    if not isinstance(index, dict) or not all(isinstance(v, str) for v in index.values()):
        fail(f"{path} is not a map of candidates to cached document names; delete it and re-run `query` for {source}")
    return index


def _dedupe(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    seen, out = set(), []
    for row in rows:
        identity = (row["key"], row["kind"], row["subject"])
        if identity not in seen:
            seen.add(identity)
            out.append(row)
    return out




def declarers(source: str, key: str, root: Path | None) -> list[tuple[str, Path]]:
    """(candidate, local path) of every document the census says declares `key`."""
    out = []
    by_document: dict[str, Path] = {}
    if source == "github-publisher-trees" and root is not None:
        by_digest = {
            hashlib.sha256(path.read_bytes()).hexdigest(): path
            for path in root.rglob("*")
            if path.is_file() and path.suffix in (".json", ".yaml", ".yml")
        }
        by_document = {
            row["document"]: by_digest.get(row["sha256"], root / "missing") for row in pinned_listing(source)
        }
    for row in read_records(source):
        if row["key"] != key or row["kind"] != "document":
            continue
        if not row["result"].startswith("census ") or row["result"] == "census 0":
            continue
        if source in WALKS:
            if root is None:
                fail(f"{source} is a walk; pass --root with its local copy")
            out.append((row["subject"], by_document.get(row["subject"], root / row["subject"])))
        else:
            index = candidate_index(source)
            if row["subject"] in index:
                out.append((row["subject"], CACHE / source / "documents" / index[row["subject"]]))
    return out


def _current_build() -> str:
    """The measured build's short commit, as a probe row records it."""
    return REACH.measured_commit(REACH.DEFAULT_OUT)[:12]


def measured_build() -> str:
    """The commit the instrumented build and its region universe were measured at.

    A site is resolved against today's `src/` and matched against the build's
    regions, so the two must be one source: an edit to `src/` after the build
    shifts every span below it and a probe would read another arm's regions.
    Refused unless `src/` is exactly the measured commit's.
    """
    commit = REACH.measured_commit(REACH.DEFAULT_OUT)
    clean = subprocess.run(["git", "diff", "--quiet", commit, "--", "src/"], cwd=REPO)
    if clean.returncode != 0:
        fail(f"src/ differs from {commit[:12]}, the commit the instrumented build was measured at; "
             "re-run `just golden-reach` (or `golden-reach.py measure`) before probing")
    return commit[:12]


# llmlint: ignore[changed_behavior_has_e2e] A probe runs the instrumented `crozier` that `just golden-reach` builds, with `src/` at the measured commit, so like that measurement it stays outside `just check`; its stale-build refusal is tested, and the probe.jsonl it files is reconciled by `RankedBacklogTests`.
def probe(args: argparse.Namespace) -> int:
    build = measured_build()
    e2e, crozier = REACH._instrumented_binaries(REPO)
    del e2e
    profdata, llvm_cov = REACH._llvm_tool("llvm-profdata"), REACH._llvm_tool("llvm-cov")
    universe = REACH.load_regions(REACH.DEFAULT_OUT / "universe.json")
    results = []
    for key in args.key:
        arms = unreached_sites(key)
        regions = {spec: (site.file, {r for r in universe.get(site.file, ()) if site.holds(r)})
                   for spec in arms for site in [REACH.resolve_site(spec)]}
        pending = declarers(args.source, key, args.root)
        earlier: list[dict[str, Any]] = []
        if args.resume:
            # A stopped probe resumes document by document: what it filed stands.
            earlier = [
                row for row in read_probes(args.source)
                if row["key"] == key and row.get("build") == build
                and not (args.retry_timeouts and row["status"].startswith("timeout"))
            ]
            done = {row["candidate"] for row in earlier}
            pending = [(candidate, path) for candidate, path in pending if candidate not in done]
            if not pending:
                continue
        # The export is read for the files the unreached sites sit in, and nothing else.
        sources = sorted({str(REPO / file) for file, _found in regions.values()})
        # Byte-identical documents (a catalogue's many copies of one version) run once.
        seen: dict[str, tuple[str, list[str]]] = {}

        def one(candidate_path: tuple[str, Path]) -> dict[str, Any]:
            candidate, path = candidate_path
            try:
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
            except OSError as error:
                return {"key": key, "candidate": candidate, "status": f"unreadable: {error.strerror}", "reached": []}
            if digest in seen:
                status, reached = seen[digest]
                return {"key": key, "candidate": candidate, "status": status, "reached": reached, "build": build}
            result = run_one(candidate, path)
            seen[digest] = (result["status"], result["reached"])
            return {**result, "build": build}

        def run_one(candidate: str, path: Path) -> dict[str, Any]:
            with tempfile.TemporaryDirectory(prefix="golden-reach-probe-") as scratch:
                scratch_path = Path(scratch)
                env = dict(os.environ, LLVM_PROFILE_FILE=str(scratch_path / "%p-%m.profraw"))
                try:
                    run = subprocess.run(
                        [str(crozier), "generate", "--spec", str(path), "--output", str(scratch_path / "out"),
                         "--package-name", "fern", "--project-name", "default_package_name"],
                        capture_output=True, text=True, timeout=args.timeout, env=env,
                    )
                except subprocess.TimeoutExpired:
                    return {"key": key, "candidate": candidate, "status": f"timeout after {args.timeout}s", "reached": []}
                profiles = [str(p) for p in scratch_path.glob("*.profraw")]
                if not profiles:
                    return {"key": key, "candidate": candidate, "status": f"no profile (exit {run.returncode})", "reached": []}
                merged = scratch_path / "merged.profdata"
                REACH.run_llvm([profdata, "merge", "-sparse", *profiles, "-o", str(merged)])
                export = scratch_path / "export.json"
                with export.open("w", encoding="utf-8") as sink:
                    REACH.run_llvm([llvm_cov, "export", "-format=text", f"-instr-profile={merged}", str(crozier),
                                    *sources], stdout=sink)
                tier = {"t": REACH.REPORT.load_tier(export, REPO)}
                hit = {f: {tuple(r) for r, n in c.items() if n > 0} for f, c in tier["t"].items()}
            reached = sorted(spec for spec, (file, found) in regions.items() if found & hit.get(file, set()))
            status = "generated" if run.returncode == 0 else f"exit {run.returncode}: {run.stderr.strip()[-160:]}"
            return {"key": key, "candidate": candidate, "status": status, "reached": reached}

        probed: list[dict[str, Any]] = []
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            for start in range(0, len(pending), PROBE_CHUNK):
                probed.extend(pool.map(one, pending[start:start + PROBE_CHUNK]))
                file_probes(args.source, key, earlier + probed)
        results.extend(probed)
    reaching = sum(1 for r in results if r["reached"])
    print(f"golden-reach-search: {args.source}: probed {len(results)} declarer(s), {reaching} reach an unreached arm")
    return 0


def read_probes(source: str) -> list[dict[str, Any]]:
    path = source_dir(source) / "probe.jsonl"
    if not path.is_file():
        return []
    return read_jsonl(path, ("key", "candidate", "status", "reached"),
                      "restore it from git, or re-run `probe` for the source")


@contextlib.contextmanager
def exclusive_lock(path: Path) -> Iterator[None]:
    """Hold an inter-process lock on `path` for the body, waiting as long as it is held.

    `fcntl.flock` where the platform has it and `msvcrt.locking` on Windows,
    both released by the kernel if the holder dies. A platform with neither
    falls back to creating `path` exclusively, which a killed holder leaves
    behind: the wait then names the file to remove.
    """
    if fcntl is not None or msvcrt is not None:
        with path.open("a+b") as handle:
            if fcntl is not None:
                fcntl.flock(handle, fcntl.LOCK_EX)
                yield
                return
            handle.seek(0)
            while True:
                try:
                    # Byte 0, past EOF or not; LK_LOCK gives up after ~10s, so wait again.
                    msvcrt.locking(handle.fileno(), msvcrt.LK_LOCK, 1)
                    break
                except OSError:
                    continue
            try:
                yield
            finally:
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        return
    marker = path.with_name(path.name + ".held")
    for tick in itertools.count(1):
        try:
            os.close(os.open(marker, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
            break
        except FileExistsError:
            if tick % 600 == 0:
                print(f"golden-reach-search: still waiting on {marker}; remove it if no probe is filing",
                      file=sys.stderr)
            time.sleep(0.1)
    try:
        yield
    finally:
        marker.unlink()


def file_probes(source: str, key: str, probed: list[dict[str, Any]]) -> None:
    """One key's probe results into `probe.jsonl`.

    Every declarer's measured reach is kept here. A declarer becomes a Contract B
    `candidate` row only when it is screened (see [`screen`]), so the record's
    candidates are exactly the ones carrying their three screens, and an
    arm-reaching declarer nobody screened stays visible here as outstanding.
    """
    path = source_dir(source) / "probe.jsonl"
    # Probes of other keys of this source may be filing at the same time; the
    # read-modify-write is theirs to wait for, not to interleave with.
    CACHE.mkdir(parents=True, exist_ok=True)
    with exclusive_lock(CACHE / f"{source}.probe.lock"):
        kept = [row for row in read_probes(source) if row["key"] != key]
        path.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in kept + probed), encoding="utf-8")




def screen(args: argparse.Namespace) -> int:
    """File one candidate's three screens, each with the evidence it rests on."""
    if args.declined and args.registered:
        fail("a candidate is registered or declined, not both; pass one of --registered and --declined")
    for outcome in (args.licence, args.ref, args.fern):
        if outcome != "passed" and not outcome.startswith("failed: "):
            fail(f"a screen reads `passed` or `failed: <reason>`, not {outcome!r}")
    census = next(
        (r["result"] for r in read_records(args.source)
         if r["key"] == args.key and r["kind"] == "document" and r["subject"] == args.candidate),
        None,
    )
    if census is None:
        fail(f"{args.candidate} is no declarer of {args.key} in {args.source}'s records; `walk` or `query` {args.source} for {args.key} first, or check the candidate's spelling")
    rows = [
        {"key": args.key, "kind": "candidate", "subject": args.candidate, "result": census, "file": "probe.jsonl"},
        {"key": args.key, "kind": "screen", "subject": f"{args.candidate} licence", "result": args.licence, "file": "screens.jsonl"},
        {"key": args.key, "kind": "screen", "subject": f"{args.candidate} ref", "result": args.ref, "file": "screens.jsonl"},
        {"key": args.key, "kind": "screen", "subject": f"{args.candidate} fern", "result": args.fern, "file": "screens.jsonl"},
    ]
    directory = source_dir(args.source)
    with (directory / "screens.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"key": args.key, "candidate": args.candidate, "licence": args.licence,
                                 "ref": args.ref, "fern": args.fern, "gap_keys": args.gap_keys,
                                 "evidence": args.evidence, "declined": args.declined,
                                 "registered": args.registered}, sort_keys=True) + "\n")
    others = [r for r in read_records(args.source)
              if not (r["key"] == args.key and r["kind"] in ("screen", "candidate")
                      and (r["subject"] == args.candidate or r["subject"].startswith(args.candidate + " ")))]
    replace_records(args.source, others + rows)
    return 0




def _cell(text: str) -> str:
    """A table cell's text, its pipes escaped so a regex phrasing stays one column."""
    return text.replace("|", "\\|")


def _dispositions(key: str) -> list[str]:
    """What became of a candidate that passes every screen: registered, handed off, or declined."""
    out: list[str] = []
    handoff = EVIDENCE / "handoff.tsv"
    if handoff.is_file():
        for row in read_tsv(handoff, HANDOFF_FIELDS, "restore it from git"):
            if row["golden_key"] == key:
                gaps = "" if row["gap_keys"] in ("", "-") else f", declaring `gap` row(s) {row['gap_keys']}"
                out.append(f"- **Hand-off** (see [`handoff.tsv`](../handoff.tsv)): <{row['candidate_url']}>{gaps} — {row['fern_screen']}")
    for source in DECLARED_SOURCES:
        screens = source_dir(source) / "screens.jsonl"
        if not screens.is_file():
            continue
        latest: dict[str, dict[str, Any]] = {}
        for row in read_jsonl(screens, ("key", "candidate"), "restore it from git; `screen` appends to it"):
            if row["key"] == key:
                latest[row["candidate"]] = row
        for candidate, row in sorted(latest.items()):
            if row.get("registered"):
                out.append(f"- **Registered** (`{source}`): `{candidate}` — {row['registered']}")
            if row.get("declined"):
                out.append(f"- **Declined** (`{source}`): `{candidate}` — {row['declined']}")
    return ["", "#### Candidates passing every screen", ""] + out if out else []


def _unreadable(key: str, source: str) -> list[tuple[str, str]]:
    """Documents of one source the census could not read, each with the reason it gave."""
    enumeration = source_dir(source) / "enumeration.tsv.gz"
    if source in WALKS and enumeration.is_file():
        # A walked document the census could not read may declare the row; the
        # walk's enumeration, not a per-key row, is where that is recorded.
        with gzip.open(enumeration, "rt", encoding="utf-8", newline="") as handle:
            return [(row["document"], row["status"])
                    for row in csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
                    if row["status"] != "readable"]
    return [(r["subject"], r["result"]) for r in read_records(source)
            if r["key"] == key and r["kind"] == "document" and not r["result"].startswith("census ")]


def outstanding_items(key: str, source: str, build: str) -> list[tuple[str, str]]:
    """Every item one source still owes one key's search, each with what blocks it.

    Exactly the items [`_outstanding`] counts: a declarer with no probe of
    `build`, one whose probe timed out or left no profile, and every document
    the census could not read.
    """
    records = [r for r in read_records(source) if r["key"] == key]
    declarers = {r["subject"] for r in records if r["kind"] == "document" and r["result"].startswith("census ")
                 and r["result"] != "census 0"}
    probes = {row["candidate"]: row for row in read_probes(source)
              if row["key"] == key and row.get("build") == build}
    items = [(c, f"unprobed on build {build}") for c in sorted(declarers - set(probes))]
    items += [(c, f"probe on build {build}: {probes[c]['status']}") for c in sorted(declarers & set(probes))
              if probes[c]["status"].startswith(("timeout", "no profile"))]
    return items + [(document, reason) for document, reason in _unreadable(key, source)]


def _tally(key: str, source: str, build: str) -> dict[str, int]:
    """What one source's evidence says about one key: declarers, and how each fared."""
    records = [r for r in read_records(source) if r["key"] == key]
    declarers = {r["subject"] for r in records if r["kind"] == "document" and r["result"].startswith("census ")
                 and r["result"] != "census 0"}
    unread = len(_unreadable(key, source))
    # Only a probe of the measured build counts; one run while `src/` differed from
    # it read another arm's regions (see [`measured_build`]) and says nothing.
    probes = {row["candidate"]: row for row in read_probes(source)
              if row["key"] == key and row.get("build") == build}
    screened = {r["subject"].rsplit(" ", 1)[0] for r in records if r["kind"] == "screen"}
    reaching = {c for c, row in probes.items() if row["reached"]}
    passing = {
        candidate for candidate in screened
        if all(r["result"] == "passed" for r in records
               if r["kind"] == "screen" and r["subject"].rsplit(" ", 1)[0] == candidate)
    }
    return {
        "declarers": len(declarers),
        "unreadable": unread,
        "probed": len(declarers & set(probes)),
        "timeouts": sum(1 for c in declarers if probes.get(c, {}).get("status", "").startswith("timeout")),
        "failed": sum(1 for c in declarers if probes.get(c, {}).get("status", "generated") not in ("generated",)
                      and not probes[c]["status"].startswith("timeout")),
        "unprofiled": sum(1 for c in declarers if probes.get(c, {}).get("status", "").startswith("no profile")),
        "reaching": len(reaching),
        "screened": len(reaching & screened),
        "passing": len(passing),
    }


def _outstanding(tally: dict[str, int]) -> int:
    """Declarers the arm may still be in: unprobed, timed out, unprofiled, or unreadable."""
    return (tally["declarers"] - tally["probed"] + tally["timeouts"] + tally["unprofiled"]
            + tally["unreadable"])


def src_commits_since(build: str) -> list[str]:
    """Commits touching `src/` after the measured build, newest first."""
    run = subprocess.run(["git", "log", "--format=%h", f"{build}..HEAD", "--", "src/"],
                         cwd=REPO, capture_output=True, text=True)
    if run.returncode != 0:
        fail(f"cannot read src/'s history since {build}: {run.stderr.strip()} — "
             "fetch that commit, or re-run `just golden-reach` on this checkout")
    return run.stdout.split()


def _outcome(tallies: dict[str, dict[str, int]], src_moved: bool = False) -> str:
    """This search's own reading of the arm it names: something outstanding, or nothing.

    A record searches for the sites its row still leaves unreached, and a
    registered witness reaching one would have taken it off that list, so a
    registration never reads here: which arms one bought is the index's to say.
    Nor does a search whose probes ran on a `src/` that has since moved: each of
    them has to be re-taken before it can say the arm is absent.
    """
    outstanding = src_moved or any(
        _outstanding(t) or t["screened"] < t["reaching"] or t["passing"]
        for t in tallies.values()
    )
    return "search-incomplete" if outstanding else "exhausted"


SEARCHED_FOR = "The unreached handling site(s) searched for: "


def probed_build(commit: str) -> str:
    """The short commit of an earlier build whose probes a record is rendered as of."""
    run = subprocess.run(["git", "rev-parse", "--verify", "-q", f"{commit}^{{commit}}"],
                         cwd=REPO, capture_output=True, text=True)
    if run.returncode != 0:
        fail(f"--build {commit} names no commit in this checkout; pass the build a record's probes "
             "were counted on, as its `build of commit` line spells it")
    return run.stdout.strip()[:12]


def searched_for(key: str) -> str:
    """The arm a committed record searched for, as that record states it.

    A record re-rendered as of an earlier build keeps the arm it searched for then:
    a witness registered since may have reached it, and the ledger would name none.
    """
    path = EVIDENCE / "searches" / f"{key}.md"
    if path.is_file():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith(SEARCHED_FOR):
                return line
    fail(f"{path} states no arm it searched for; render {key} without --build, against the current measurement")
    raise AssertionError


def render(args: argparse.Namespace) -> int:
    """One arm search record per key, one Contract B line per declared source.

    `--build` re-renders a committed record as of the build its probes ran on —
    after its evidence moved, say, while `src/` has moved past that build — so
    only what the evidence changed moves, and the record keeps its searched arm.
    """
    build = probed_build(args.build) if args.build else _current_build()
    ledger = "was measured on when these probes ran" if args.build else "is measured on"
    for key in args.key:
        header = searched_for(key) if args.build else (
            SEARCHED_FOR + ", ".join(f"`{_cell(s)}`" for s in unreached_sites(key)) + ".")
        tallies = {source: _tally(key, source, build) for source in DECLARED_SOURCES}
        moved = src_commits_since(build)
        outcome = _outcome(tallies, bool(moved)) if args.outcome == "auto" else args.outcome
        lines = [
            f"# Arm search: `{key}`",
            "",
            header,
            "Read with: " + ", ".join(f"`{s}`" for s in selectors_of(key)) + ".",
            "",
            "A walked or fetched document declaring the row is a `document` row of the",
            "source's `records.tsv`; one whose instrumented `crozier generate` executes",
            "an unreached site above is a `candidate`, and only a candidate owes the",
            "licence, ref and fern screens. A probe counts only if it ran the instrumented",
            f"build of commit `{build}`, the one the reach ledger {ledger},",
            "with `src/` at that commit; a declarer with no such probe is unprobed and",
            "outstanding, and a re-probe needs `src/` at that commit (or a fresh",
            "`just golden-reach`). Probes run before that rule was enforced read shifted",
            "spans and are not counted. The outcome is this search's own reading;",
            "final reconciliation decides whether the arm's search reads `exhausted`.",
            "",
            "### Witness search (exhaustive)",
            "",
            "| key | source | outcome | queries | walk | candidates | screens |",
            "|---|---|---|---|---|---|---|",
        ]
        if args.build and not ledger_unreached(key):
            table = lines.index("### Witness search (exhaustive)")
            lines[table:table] = [
                "The arm this search looked for is now reached: a witness registered since",
                "reaches every handling site the ledger names for the row. The tables",
                "below record the search as it stood when the arm was still open.",
                "",
            ]
        for source in DECLARED_SOURCES:
            records = [r for r in read_records(source) if r["key"] == key]
            queries = "; ".join(
                f"`{_cell(r['subject'])}` → {_cell(r['result'])}" for r in records if r["kind"] == "query"
            ) or "—"
            walks = "; ".join(
                f"`{r['subject'].rsplit('@', 1)[0]}` at `{r['subject'].rsplit('@', 1)[1]}` → {r['result']} documents"
                for r in records if r["kind"] == "walk") or "—"
            reaching = [r["subject"] for r in records if r["kind"] == "candidate"]
            candidates = ", ".join(f"`{c}`" for c in reaching) or "—"
            screens: dict[str, dict[str, str]] = {}
            for r in records:
                if r["kind"] == "screen":
                    candidate, screen_name = r["subject"].rsplit(" ", 1)
                    screens.setdefault(candidate, {})[screen_name] = r["result"]
            screen_cell = "; ".join(
                f"`{c}` " + " ".join(f"{s} `{screens[c][s]}`" for s in ("licence", "ref", "fern") if s in screens[c])
                for c in reaching if c in screens) or "—"
            lines.append(
                f"| `{key}` | `{source}` | `{outcome}` | {queries} | {walks} | {candidates} | {_cell(screen_cell)} |"
            )
        lines += [
            "",
            "#### Declarers, and how the instrumented run fared on each",
            "",
            "Counted off each source's `records.tsv` and `probe.jsonl`, probes of the",
            f"build `{build}` only. A declarer not probed on it, one whose run",
            "did not finish (a timeout), and one crozier failed on without a profile are",
            "outstanding: the arm may be in them, and nothing here says otherwise.",
            "`outstanding` sums the unprobed, the timed out, the failed without a profile",
            "and the unreadable.",
        ]
        if moved:
            lines += [
                "",
                f"When this record was rendered, `src/` had moved since that build "
                f"({', '.join(f'`{c}`' for c in moved)}), so every probe counted here must be",
                "re-taken on a fresh `just golden-reach` measurement before it is reused.",
            ]
        lines += [
            "",
            "| source | declarers | unreadable | probed | unprobed | timed out | crozier failed | reach an arm | screened | outstanding |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ] + [
            f"| `{source}` | {t['declarers']} | {t['unreadable']} | {t['probed']} | {t['declarers'] - t['probed']} "
            f"| {t['timeouts']} | {t['failed']} | {t['reaching']} | {t['screened']} | {_outstanding(t)} |"
            for source, t in tallies.items()
        ]
        lines += _dispositions(key)
        path = EVIDENCE / "searches" / f"{key}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


OUTSTANDING = EVIDENCE / "outstanding.tsv"
OUTSTANDING_FIELDS = ("key", "source", "item", "blocker", "build", "src_moved_since")
RECORD_BUILD = re.compile(r"^build `([0-9a-f]+)` only\.", re.M)


def record_build(text: str, path: Path) -> str:
    """The build a committed arm-search record counted its probes on, as it states it."""
    found = RECORD_BUILD.search(text)
    if not found:
        fail(f"{path} names no build its probes were counted on; re-render it with `render`")
    return found.group(1)


def outstanding(args: argparse.Namespace) -> int:
    """Every item each committed arm search still owes, one line each, into `outstanding.tsv`.

    A record's `outstanding` column is a count; this is the list it counts, with
    what blocks each item, for whoever continues the search. Each record is read
    as of the build it states, and `src_moved_since` names the commits that make
    every probe of that build owe a fresh `just golden-reach` before reuse.
    """
    del args
    rows: list[dict[str, str]] = []
    for path in sorted((EVIDENCE / "searches").glob("*.md")):
        build = record_build(path.read_text(encoding="utf-8"), path)
        moved = " ".join(src_commits_since(build))
        for source in DECLARED_SOURCES:
            rows += [{"key": path.stem, "source": source, "item": item, "blocker": blocker,
                      "build": build, "src_moved_since": moved}
                     for item, blocker in outstanding_items(path.stem, source, build)]
    with OUTSTANDING.open("w", encoding="utf-8", newline="") as handle:
        # Split on tabs and nothing else, as `records.tsv` is: a quote is text.
        writer = csv.DictWriter(handle, OUTSTANDING_FIELDS, delimiter="\t", lineterminator="\n",
                                quoting=csv.QUOTE_NONE, quotechar=None)
        writer.writeheader()
        writer.writerows(rows)
    print(f"golden-reach-search: {len(rows)} outstanding item(s) across "
          f"{len({row['key'] for row in rows})} arm search(es)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)
    w = sub.add_parser("walk")
    w.add_argument("--source", required=True)
    w.add_argument("--root", type=Path, required=True, help="local copy of the pinned documents")
    w.add_argument("--key", action="append", required=True)
    w.add_argument("--jobs", type=REACH.positive_int, default=8)
    w.add_argument("--census", type=Path, help="a census already taken over these pinned bytes (JSONL.gz)")
    f = sub.add_parser("fetch-pins")
    f.add_argument("--root", type=Path, required=True, help="local copies; fetched pins land in its fetched/")
    q = sub.add_parser("query")
    q.add_argument("--source", required=True)
    q.add_argument("--key", action="append", required=True)
    p = sub.add_parser("probe")
    p.add_argument("--source", required=True)
    p.add_argument("--key", action="append", required=True)
    p.add_argument("--root", type=Path)
    p.add_argument("--jobs", type=REACH.positive_int, default=8)
    p.add_argument("--timeout", type=REACH.positive_int, default=300)
    p.add_argument("--resume", action="store_true", help="skip every declarer already probed")
    p.add_argument("--retry-timeouts", action="store_true", help="with --resume, probe again a declarer that timed out")
    s = sub.add_parser("screen")
    s.add_argument("--source", required=True)
    s.add_argument("--key", required=True)
    s.add_argument("--candidate", required=True)
    s.add_argument("--licence", required=True)
    s.add_argument("--ref", required=True)
    s.add_argument("--fern", required=True)
    s.add_argument("--gap-keys", default="")
    s.add_argument("--evidence", default="")
    s.add_argument("--declined", default="", help="why a candidate passing every screen is not registered")
    s.add_argument("--registered", default="", help="the corpus row a candidate passing every screen is registered as")
    r = sub.add_parser("render")
    r.add_argument("--key", action="append", required=True)
    r.add_argument("--outcome", default="auto", choices=("auto", "exhausted", "search-incomplete", "witness-found"))
    r.add_argument("--build", help="re-render a committed record as of the earlier build its probes ran on")
    sub.add_parser("outstanding")
    args = parser.parse_args(argv)
    return {"walk": walk, "fetch-pins": fetch_pins, "query": query, "probe": probe, "screen": screen, "render": render,
            "outstanding": outstanding}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
