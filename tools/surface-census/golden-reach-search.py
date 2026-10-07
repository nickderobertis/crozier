#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["ruamel.yaml==0.19.1"]
# ///
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
  keys it declares (beside the keys earlier walks matched it for, which it
  keeps), or the measured reason it could not be read. The publisher
  trees' pins name documents rather than archives, so ``fetch-pins`` first
  fetches each one with no local copy at its pinned commit.
* ``query`` — a source that takes a text query (``github-code-search``,
  ``sourcegraph``), through the existing guarded acquirer in
  `tools/witness-search/witness-search-github.py`: each phrasing in
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

Screens are taken by ``screen``, through the one measured screening stage both
witness-search families share (`tools/witness-search/witness_screen.py`): the candidate's
bytes read at its pinned commit, its licence read against the corpus rule, and
pinned Fern run over it, each outcome filed with its pins, exit status and
redacted log. The caller supplies only a passing candidate's disposition
(``--registered`` or ``--declined``) and any licence judgement that refuses it;
an outcome stated as text is refused. A screen filed before that stage carries
no measured record: it is historical, and settles no candidate.

Every GitHub and Sourcegraph call goes through `tools/witness-search/rate_limit_guard.py`, by
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
import signal
import types
import subprocess
import sys
import tempfile
import time
import urllib.parse
from collections import Counter, defaultdict
from collections.abc import Callable, Iterable, Iterator
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

REPO = Path(__file__).resolve().parents[2]
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
# A document the census could not read, settled by a full standard parser: one it
# rejects on syntax, or one it reads that names no OpenAPI or Swagger version, is
# no description a witness could be. Each source's `census-refused.tsv` lists them
# with the parser, its version and the document's digest; `refuse` writes it.
REFUSED_FIELDS = ("document", "sha256", "parser", "verdict", "evidence")
REFUSED_FILE = "census-refused.tsv"
REFUSED_VERDICTS = ("syntax", "not-openapi")
# The full YAML 1.2 parser the search reads YAML with where the census's stdlib
# loader cannot: `refuse` to settle a syntax rejection, `recensus` to count what
# a readable document declares. Pinned here and in the inline script metadata
# above, which `uv run tools/surface-census/golden-reach-search.py` installs.
RUAMEL_YAML_PIN = "0.19.1"
# A document the census read through that parser, named with its loader.
FALLBACK_FIELDS = ("document", "sha256", "loader")
FALLBACK_FILE = "census-fallback.tsv"
FIRST_PAGE = 100
# Keyword arguments every acquirer this script builds is given. A real search
# leaves them empty; the offline tests point them at a loopback server.
ACQUIRER_OPTIONS: dict[str, Any] = {}
# Probe results are filed this many documents at a time, so a stopped run keeps them;
# some catalogue documents take minutes each under an instrumented build.
PROBE_BATCH = 48


def _load(name: str, path: Path) -> ModuleType:
    """A sibling script imported by path: its hyphenated file name is no module name."""
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


REACH = _load("golden_reach", REPO / "tools" / "surface-census" / "golden-reach.py")
CENSUS = _load("openapi_surface_census", REPO / "tools" / "surface-census" / "openapi-surface-census.py")
SCREEN = _load("witness_screen", REPO / "tools" / "witness-search" / "witness_screen.py")


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


def searched_arm(key: str) -> tuple[str, ...]:
    """The sites a row's committed record searched for, where each still resolves in today's `src/`.

    A row a registered witness has since taken off the ledger's unreached list
    still owes its record's declarers a probe on the counted build; this is the
    arm they are probed against. A site a later repair restructured out of `src/`
    resolves nowhere, and a declarer cannot be probed for it.
    """
    arms = []
    for spec in re.findall(r"`((?:[^`\\]|\\.)+)`", searched_for(key)[len(SEARCHED_FOR):]):
        spec = spec.replace("\\|", "|")
        try:
            REACH.resolve_site(spec)
        except SystemExit:
            continue
        arms.append(spec)
    return tuple(arms)


def ledger_sites(key: str) -> tuple[str, ...]:
    """Every handling site the committed ledger names for the row, reached or not."""
    for _rank, reach in REACH.read_ledger():
        if reach.key == key:
            return tuple(spec for spec, _hit, _total in reach.sites)
    fail(f"{key} is not in the ledger; check the key against docs/openapi-surface/golden-reach.tsv")
    raise AssertionError


def probe_arms(key: str) -> tuple[str, ...]:
    """What a probe of `key` reads: the ledger's unreached sites, else the arm its record searched for.

    Where a repair restructured that whole arm out of `src/`, the row's handling
    sites as the ledger names them today stand in for it.
    """
    return ledger_unreached(key) or searched_arm(key) or ledger_sites(key)


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
    # Written beside and moved into place, so a run stopped mid-write leaves the
    # ledger it had rather than a truncated one.
    partial = path.with_name(f".{path.name}.partial")
    with partial.open("w", encoding="utf-8", newline="") as handle:
        # Contract B's reader splits on tabs and nothing else, so a quote is text.
        writer = csv.DictWriter(
            handle, RECORD_FIELDS, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None
        )
        writer.writeheader()
        for row in sorted(unique.values(), key=lambda r: (r["key"], r["kind"], r["subject"], r["result"])):
            writer.writerow(row)
    os.replace(partial, path)


def record_guard_logs(source: str) -> None:
    """The guard's own logs: every call and wait this source's searches made.

    Contract B names each evidence file from a records row, so each log is
    filed as a `wait` row under the pseudo-key `*` it answers for. The names are
    the acquirer's, which writes them.
    """
    github = _load("witness_search_github", REPO / "tools" / "witness-search" / "witness-search-github.py")
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
                  "licence_spdx", "fern_screen", "gap_keys", "disposition")


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


def repeated_documents(listing: list[dict[str, str]]) -> set[str]:
    """Document paths more than one walked tree pins: the publisher trees'
    `openapi.yaml`, which three repositories each hold at their root."""
    seen: Counter[str] = Counter(row["document"] for row in listing)
    return {document for document, count in seen.items() if count > 1}


def document_subject(row: dict[str, str], repeated: set[str]) -> str:
    """A walked document's name in `records.tsv` and `probe.jsonl`: its path, or,
    where another tree pins the same path, `<walk>:<path>` so each is one declarer."""
    return f"{row['walk']}:{row['document']}" if row["document"] in repeated else row["document"]


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


class CensusTimeout(BaseException):
    """A document the census did not finish within the walk's per-document limit.

    A `BaseException`, so the census's own catch-all for a document it cannot
    parse does not record the cut-off as a parse refusal.
    """


def _alarm(_signum: int, _frame: types.FrameType | None) -> None:
    raise CensusTimeout


def _census_one(args: tuple[str, str, str, tuple[tuple[str, tuple[str, ...]], ...], int]) -> dict[str, str]:
    """One document's walk census, bounded by `timeout` seconds where the platform can.

    A document whose census runs past the limit is recorded as unreadable with that
    reason rather than holding up the walk: MongoDB's `v1-deprecated/v1.yaml` held
    a vendor-portals worker for over two hours. Windows has no `SIGALRM`, so there the census is unbounded.
    """
    path, sha256, document, keys, timeout = args
    alarm = getattr(signal, "SIGALRM", None)
    if alarm is None:
        return _census_body(path, sha256, document, keys)
    previous = signal.signal(alarm, _alarm)
    signal.alarm(timeout)
    try:
        return _census_body(path, sha256, document, keys)
    except CensusTimeout:
        return {"status": f"unreadable: census exceeded {timeout}s", "matched_keys": ""}
    finally:
        signal.alarm(0)
        signal.signal(alarm, previous)


def _census_body(path: str, sha256: str, document: str, keys: tuple[tuple[str, tuple[str, ...]], ...]) -> dict[str, str]:
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
    repeated = repeated_documents(listing)
    by_digest: dict[str, Path] = {}
    if source == "github-publisher-trees":
        for path in args.root.rglob("*"):
            if path.is_file() and path.suffix in (".json", ".yaml", ".yml"):
                by_digest.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(), path)
    jobs = [
        (str(locate(source, args.root, row, by_digest)), row["sha256"], row["document"], keys, args.census_timeout)
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
    requested = {key for key, _ in keys}
    earlier = earlier_matches(out, requested)
    records: list[dict[str, str]] = []
    walks: dict[tuple[str, str], int] = defaultdict(int)
    with gzip.open(out, "wt", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, WALK_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row, result in zip(listing, results):
            walks[(row["walk"], row["revision"])] += 1
            # A row another search matched keeps that match: this walk answers for
            # the keys it was given, and the other keys' document records rest on it.
            kept = earlier.get((row["walk"], row["document"], row["sha256"]), []) if result["status"] == "readable" else []
            matched = ",".join(dict.fromkeys([*kept, *filter(None, result["matched_keys"].split(","))]))
            writer.writerow({**{f: row[f] for f in ("walk", "document", "revision", "sha256")},
                             "matched_keys": matched, "status": result["status"]})
            counts = json.loads(result.get("counts") or "{}")
            for key, count in counts.items():
                records.append({"key": key, "kind": "document", "subject": document_subject(row, repeated),
                                "result": f"census {count}", "file": out.name})
    listing_file = "pins.tsv" if source == "github-publisher-trees" else out.name
    for key, _selectors in keys:
        for (tree, revision), count in sorted(walks.items()):
            records.append({"key": key, "kind": "walk", "subject": f"{tree}@{revision}",
                            "result": str(count), "file": listing_file})
    kept = [r for r in read_records(source) if r["key"] in requested and r["kind"] not in ("walk", "document")]
    write_records(source, requested, kept + records)
    unreadable = sum(1 for r in results if r["status"] != "readable")
    print(f"golden-reach-search: {source}: {len(listing)} documents walked, {unreadable} unreadable")
    return 0



def earlier_matches(path: Path, requested: set[str]) -> dict[tuple[str, str, str], list[str]]:
    """Each document's keys an earlier walk matched, other than `requested`, by (walk, document, sha256).

    A walk writes the whole enumeration again but censuses only the keys it is
    given, so the matches of every other key's search are carried over from the
    file it replaces: the same pinned bytes, read by that key's own walk.
    """
    if not path.is_file():
        return {}
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        return {
            (row["walk"], row["document"], row["sha256"]): kept
            for row in csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
            if (kept := [key for key in filter(None, row["matched_keys"].split(",")) if key not in requested])
        }


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
    github = _load("witness_search_github", REPO / "tools" / "witness-search" / "witness-search-github.py")
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


# `acquirer` is `tools/witness-search/witness-search-github.py`'s `Acquirer`, loaded from a
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
    github = _load("witness_search_github", REPO / "tools" / "witness-search" / "witness-search-github.py")
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
        listing = pinned_listing(source)
        repeated = repeated_documents(listing)
        by_document = {
            document_subject(row, repeated): by_digest.get(row["sha256"], root / "missing") for row in listing
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
    """Run every requested key's declarers through the instrumented build, once per document.

    A document is generated once per build however many keys it declares — the
    catalogue rows declared by nearly every document (`recursive-graph` on any
    `$ref`, `non-identifier-operation-id` on any `operationId`) would otherwise
    multiply the run by the keys asked for — and every key reads its own sites off
    that one profile. The run is cached by document digest per build under
    `.local/golden-reach-search/probe-cache/`, so the copy of a document another
    source walked is not generated twice either.
    """
    build = measured_build()
    e2e, crozier = REACH._instrumented_binaries(REPO)
    del e2e
    profdata, llvm_cov = REACH._llvm_tool("llvm-profdata"), REACH._llvm_tool("llvm-cov")
    universe = REACH.load_regions(REACH.DEFAULT_OUT / "universe.json")
    # Every unreached site the ledger names is read off each profile, so a cached
    # run answers any key's arm and not only the keys this invocation asked for.
    all_sites = sorted({spec for _rank, reach in REACH.read_ledger()
                        for spec, hit, _total in reach.sites if not hit})
    # A reached row's searched arm is read too; its profiles are cached apart,
    # since a cached run of the ledger's sites alone never read those regions.
    extra = sorted({spec for key in args.key for spec in probe_arms(key)} - set(all_sites))
    tag = "." + hashlib.sha256("\n".join(extra).encode()).hexdigest()[:12] if extra else ""
    all_sites += extra
    regions = {spec: (site.file, {r for r in universe.get(site.file, ()) if site.holds(r)})
               for spec in all_sites for site in [REACH.resolve_site(spec)]}
    sources = sorted({str(REPO / file) for file, _found in regions.values()})
    cache = load_probe_cache(build + tag)
    plans: dict[str, tuple[tuple[str, ...], list[dict[str, Any]], list[tuple[str, Path]]]] = {}
    for key in args.key:
        arms = probe_arms(key)
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
        plans[key] = (arms, earlier, pending)

    def digest_of(path: Path) -> str | None:
        try:
            return hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError:
            return None

    by_digest: dict[str, Path] = {}
    digest_or_reason: dict[str, str] = {}
    for _arms, _earlier, pending in plans.values():
        for _candidate, path in pending:
            key_path = str(path)
            if key_path in digest_or_reason:
                continue
            digest = digest_of(path)
            if digest is None:
                try:
                    path.read_bytes()
                except OSError as error:
                    digest_or_reason[key_path] = f"unreadable: {error.strerror}"
                continue
            digest_or_reason[key_path] = digest
            by_digest.setdefault(digest, path)
    todo = to_generate(by_digest, cache, args.retry_timeouts)

    def rows_for(key: str) -> list[dict[str, Any]]:
        arms, earlier, pending = plans[key]
        rows = list(earlier)
        for candidate, path in pending:
            digest = digest_or_reason.get(str(path), "")
            if digest.startswith("unreadable: "):
                rows.append({"key": key, "candidate": candidate, "status": digest, "reached": []})
            elif digest in cache:
                result = cache[digest]
                rows.append({"key": key, "candidate": candidate, "status": result["status"],
                             "reached": [spec for spec in result["reached"] if spec in arms], "build": build})
        return rows

    tools = (str(crozier), str(profdata), str(llvm_cov), tuple(sources), args.timeout)
    # One process per run: reading an export back is seconds of Python per
    # document, which threads would serialize.
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        for start in range(0, len(todo), PROBE_BATCH):
            batch = [(digest, str(by_digest[digest]), tools, regions) for digest in todo[start:start + PROBE_BATCH]]
            for digest, result in pool.map(_probe_one, batch):
                cache[digest] = result
                append_probe_cache(build + tag, digest, result)
            file_probes_many(args.source, {key: rows_for(key) for key in plans})
    file_probes_many(args.source, {key: rows_for(key) for key in plans})
    reaching = sum(1 for key in plans for row in rows_for(key) if row["reached"])
    print(f"golden-reach-search: {args.source}: {len(by_digest)} document(s) for {len(plans)} key(s), "
          f"{len(todo)} generated, {reaching} declarer row(s) reach an unreached arm")
    return 0


def to_generate(documents: Iterable[str], cache: dict[str, dict[str, Any]], retry_timeouts: bool) -> list[str]:
    """The document digests a probe generates: every one the build's cache lacks.

    A cached run that timed out is no reading of the arms, so `--retry-timeouts`
    generates it again (under the invocation's `--timeout`) rather than filing
    the cached timeout a second time.
    """
    return [digest for digest in documents
            if digest not in cache
            or (retry_timeouts and cache[digest]["status"].startswith("timeout"))]


def _probe_one(
    job: tuple[str, str, tuple[str, str, str, tuple[str, ...], int], dict[str, tuple[str, set[tuple[int, ...]]]]],
) -> tuple[str, dict[str, Any]]:
    """One document's instrumented `crozier generate`: the unreached sites it executes."""
    digest, path, (crozier, profdata, llvm_cov, sources, timeout), regions = job
    with tempfile.TemporaryDirectory(prefix="golden-reach-probe-") as scratch:
        scratch_path = Path(scratch)
        env = dict(os.environ, LLVM_PROFILE_FILE=str(scratch_path / "%p-%m.profraw"))
        try:
            run = subprocess.run(
                [crozier, "generate", "--spec", path, "--output", str(scratch_path / "out"),
                 "--package-name", "fern", "--project-name", "default_package_name"],
                capture_output=True, text=True, timeout=timeout, env=env,
            )
        except subprocess.TimeoutExpired:
            return digest, {"status": f"timeout after {timeout}s", "reached": []}
        profiles = [str(p) for p in scratch_path.glob("*.profraw")]
        if not profiles:
            return digest, {"status": f"no profile (exit {run.returncode})", "reached": []}
        merged = scratch_path / "merged.profdata"
        REACH.run_llvm([profdata, "merge", "-sparse", *profiles, "-o", str(merged)])
        export = scratch_path / "export.json"
        with export.open("w", encoding="utf-8") as sink:
            REACH.run_llvm([llvm_cov, "export", "-format=text", f"-instr-profile={merged}", crozier,
                            *sources], stdout=sink)
        hit = executed_regions(export, {file for file, _found in regions.values()})
    reached = sorted(spec for spec, (file, found) in regions.items() if found & hit.get(file, set()))
    status = "generated" if run.returncode == 0 else f"exit {run.returncode}: {run.stderr.strip()[-160:]}"
    return digest, {"status": status, "reached": reached}


def executed_regions(export: Path, files: set[str]) -> dict[str, set[tuple[int, int, int, int]]]:
    """The code regions of `files` a coverage export counts as executed.

    What `load_tier` reads, kept to the files a site sits in and to a positive
    count: a region is executed when any object file's copy of it ran, so the
    maximum `load_tier` takes is positive exactly when some copy's count is.
    """
    report = REACH.REPORT
    document = json.loads(export.read_text(encoding="utf-8"))
    root = str(REPO) + "/"
    hit: dict[str, set[tuple[int, int, int, int]]] = defaultdict(set)
    for data in document.get("data", []):
        for function in data.get("functions", []):
            names = [name[len(root):] if name.startswith(root) else None
                     for name in function.get("filenames", [])]
            for raw in function.get("regions", []):
                if raw[4] <= 0 or raw[report.REGION_KIND_INDEX] != report.REGION_CODE_KIND:
                    continue
                name = names[raw[report.REGION_FILE_INDEX]]
                if name in files:
                    hit[name].add((raw[0], raw[1], raw[2], raw[3]))
    return dict(hit)


def probe_cache_path(build: str) -> Path:
    return CACHE / "probe-cache" / f"{build}.jsonl"


def load_probe_cache(build: str) -> dict[str, dict[str, Any]]:
    """One build's runs so far, by document digest; a torn last line is dropped."""
    path = probe_cache_path(build)
    if not path.is_file():
        return {}
    out: dict[str, dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(row, dict) and isinstance(row.get("digest"), str):
            out[row["digest"]] = {"status": row.get("status", ""), "reached": list(row.get("reached", []))}
    return out


def append_probe_cache(build: str, digest: str, result: dict[str, Any]) -> None:
    path = probe_cache_path(build)
    path.parent.mkdir(parents=True, exist_ok=True)
    with exclusive_lock(CACHE / "probe-cache.lock"):
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"digest": digest, **result}, sort_keys=True) + "\n")


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


def file_probes_many(source: str, probed: dict[str, list[dict[str, Any]]]) -> None:
    """Several keys' probe results into `probe.jsonl` in one write, each replacing its key's rows."""
    path = source_dir(source) / "probe.jsonl"
    CACHE.mkdir(parents=True, exist_ok=True)
    with exclusive_lock(CACHE / f"{source}.probe.lock"):
        kept = [row for row in read_probes(source) if row["key"] not in probed]
        rows = kept + [row for key in probed for row in probed[key]]
        path.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in rows), encoding="utf-8")


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




# The measured reason a candidate passing every screen is still no witness: a
# document written to exercise a tool is hand-written, and only a real
# specification is evidence that Fern generates from a shape (the manager's
# ruling on thin-goldens-continue-2). What follows it names what makes it one.
FIXTURE_DECLINE = "not a real-world specification: a test fixture written to exercise a tool"


def fixture_declined(key: str, source: str) -> set[str]:
    """The candidates of one key's search whose latest screen declines them as a test fixture."""
    screens = source_dir(source) / "screens.jsonl"
    if not screens.is_file():
        return set()
    latest: dict[str, dict[str, Any]] = {}
    for row in read_jsonl(screens, ("key", "candidate"), "restore it from git; `screen` appends to it"):
        if row["key"] == key:
            latest[row["candidate"]] = row
    return {c for c, row in latest.items() if str(row.get("declined", "")).startswith(FIXTURE_DECLINE)}


def candidate_ref(source: str, candidate: str) -> tuple[str, str, str, str]:
    """Where a candidate's bytes are pinned: repository, commit, path, and the digest the search read."""
    if source in QUERY_SOURCES:
        found = re.fullmatch(r"(?:github\.com/)?([^/:]+/[^/:]+):(.+)@([0-9a-f]{40})", candidate)
        if not found:
            fail(f"{candidate} names no `<owner>/<repo>:<path>@<commit>` a screen can read at its commit; "
                 f"check its spelling against {source}'s records.tsv, or pass --measured with a record "
                 "tools/witness-search/witness_screen.py measured at the document's pinned commit")
        cached = candidate_index(source).get(candidate, "")
        digest = Path(cached).stem if re.fullmatch(r"[0-9a-f]{64}", Path(cached).stem) else ""
        return found.group(1), found.group(3), found.group(2), digest
    listing = pinned_listing(source)
    repeated = repeated_documents(listing)
    for row in listing:
        if document_subject(row, repeated) == candidate:
            path, prefix = row["document"], row["walk"].replace("/", "--") + "/"
            # A vendor-portal copy is filed under its repository's `<owner>--<repo>/` directory.
            return row["walk"], row["revision"], path.removeprefix(prefix), row.get("sha256", "")
    fail(f"{candidate} is in no {source} pinned listing; check the candidate's spelling against "
         f"{source}'s records.tsv, or re-walk {source} if its listing moved")
    raise AssertionError  # unreachable: `fail` exits


def file_screen(source: str, key: str, candidate: str, row: dict[str, Any]) -> None:
    """Append one screen row and restate the candidate's `records.tsv` rows from it."""
    census = next(
        (r["result"] for r in read_records(source)
         if r["key"] == key and r["kind"] == "document" and r["subject"] == candidate),
        None,
    )
    if census is None:
        fail(f"{candidate} is no declarer of {key} in {source}'s records; `walk` or `query` {source} for {key} first, or check the candidate's spelling")
    rows = [
        {"key": key, "kind": "candidate", "subject": candidate, "result": census, "file": "probe.jsonl"},
        *({"key": key, "kind": "screen", "subject": f"{candidate} {name}", "result": row[name], "file": "screens.jsonl"}
          for name in SCREEN.SCREENS),
    ]
    with (source_dir(source) / "screens.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"key": key, "candidate": candidate, **row}, sort_keys=True) + "\n")
    others = [r for r in read_records(source)
              if not (r["key"] == key and r["kind"] in ("screen", "candidate")
                      and (r["subject"] == candidate or r["subject"].startswith(candidate + " ")))]
    replace_records(source, others + rows)


def screen(args: argparse.Namespace) -> int:
    """Take one candidate's three screens through the measured stage and file them.

    The licence, the ref and Fern are each measured by `tools/witness-search/witness_screen.py`
    — the document read at its pinned commit through the guarded acquirer, its
    licence read against the corpus rule, pinned Fern run over it — and filed with
    the exit status, pins and redacted log behind each. No outcome is taken from
    the caller: `--measured` files a record that stage measured earlier, and is
    refused unless it is whole.
    """
    stated = [flag for flag, value in (("--licence", args.licence), ("--ref", args.ref), ("--fern", args.fern))
              if value is not None]
    if stated:
        fail(f"{', '.join(stated)} free text is no longer a measurement: `screen` takes the licence, ref and "
             "fern screens through the measured stage (tools/witness-search/witness_screen.py) and records each one's exit "
             "status and redacted log — drop " + ", ".join(stated))
    if args.declined and args.registered:
        fail("a candidate is registered or declined, not both; pass one of --registered and --declined")
    if args.declined.startswith(FIXTURE_DECLINE) and not args.declined[len(FIXTURE_DECLINE):].startswith(" — "):
        fail(f"a fixture decline reads `{FIXTURE_DECLINE} — <what makes it one>`: name the repository, the "
             "path at its pinned commit, and the test or fixtures directory it sits in or the test that loads it")
    directory = source_dir(args.source)
    if not any(r["key"] == args.key and r["kind"] == "document" and r["subject"] == args.candidate
               for r in read_records(args.source)):
        fail(f"{args.candidate} is no declarer of {args.key} in {args.source}'s records; `walk` or `query` {args.source} for {args.key} first, or check the candidate's spelling")
    if args.measured:
        record = SCREEN.read_measured(args.measured)
        # A record measured elsewhere is filed only against the document it read.
        repository, commit, path, expected = candidate_ref(args.source, args.candidate)
        document = record.get("document") if isinstance(record, dict) and isinstance(record.get("document"), dict) else {}
        read = (document.get("repository"), document.get("commit"), document.get("path"))
        if read != (repository, commit, path) or (expected and document.get("sha256") not in (expected, "")):
            fail(f"--measured names {read}, not {args.candidate}'s pinned document "
                 f"{(repository, commit, path)}{' with sha256 ' + expected if expected else ''}; pass the record "
                 "measured for this candidate, or drop --measured to measure it now")
    else:
        repository, commit, path, expected = candidate_ref(args.source, args.candidate)
        github = _load("witness_search_github", REPO / "tools" / "witness-search" / "witness-search-github.py")
        acquirer = github.Acquirer(directory, cache=CACHE / args.source, **ACQUIRER_OPTIONS)
        record = SCREEN.measure(
            repository=repository, commit=commit, path=path, raw_base=acquirer.raw_github_url,
            fetch=lambda url, subject: acquirer.raw_github_get(url, args.key, subject),
            logs=directory / SCREEN.LOG_DIR, base=directory, expected_sha256=expected,
            licence_refusal=args.licence_refusal, timeout=args.timeout,
        )
        record_guard_logs(args.source)
    missing = SCREEN.measured_failures(record, directory)
    refusal = (f"{args.candidate}: a screen is filed only with its measured record, and this one lacks "
               + "; ".join(missing) + " — measure it again: run `screen` without --measured") if missing else ""
    if not refusal and args.registered and not all(
            outcome.startswith("passed") for outcome in SCREEN.outcomes(record).values()):
        refusal = (f"--registered claims {args.candidate} passed every screen, and its measured outcomes read "
                   f"{SCREEN.outcomes(record)}; drop --registered to file the refusal as measured")
    if refusal:
        if not args.measured and isinstance(record, dict):
            SCREEN.discard_logs(record, directory)
        fail(refusal)
    result = SCREEN.outcomes(record)
    file_screen(args.source, args.key, args.candidate, {
        **result, "measured": record, "screened_at": record["screened_at"], "gap_keys": args.gap_keys,
        "evidence": args.evidence, "declined": args.declined, "registered": args.registered,
    })
    print(f"golden-reach-search: {args.source}: {args.candidate} — "
          + ", ".join(f"{name} {outcome.split(':', 1)[0]}" for name, outcome in result.items()))
    return 0


def _cell(text: str) -> str:
    """A table cell's text, its pipes escaped so a regex phrasing stays one column."""
    return text.replace("|", "\\|")


def _dispositions(key: str, build: str) -> list[str]:
    """What became of a candidate that passes every screen: registered, handed off, or declined.

    A decline filed while an earlier build's probe reached the arm is kept as it
    was filed, under the build's own reading: that candidate reaches nothing now.
    """
    out: list[str] = []
    handoff = EVIDENCE / "handoff.tsv"
    if handoff.is_file():
        for row in read_tsv(handoff, HANDOFF_FIELDS, "restore it from git"):
            if row["golden_key"] == key:
                gaps = "" if row["gap_keys"] in ("", "-") else f", declaring `gap` row(s) {row['gap_keys']}"
                out.append(f"- **Hand-off** (see [`handoff.tsv`](../handoff.tsv)): <{row['candidate_url']}>{gaps} — "
                           f"{row['fern_screen']} — disposition: {row['disposition']}")
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
            if row.get("declined") and candidate not in _reaching(key, source, build):
                out.append(f"- **No longer a candidate** (`{source}`): `{candidate}` — its probe of build "
                           f"`{build}` executes no unreached site; declined when screened: {row['declined']}")
            elif row.get("declined"):
                out.append(f"- **Declined** (`{source}`): `{candidate}` — {row['declined']}")
    return ["", "#### Candidates passing every screen", ""] + out if out else []


def _unread(key: str, source: str) -> list[tuple[str, str, str]]:
    """Documents of one source the census could not read: name, reason, and digest where known."""
    enumeration = source_dir(source) / "enumeration.tsv.gz"
    if source in WALKS and enumeration.is_file():
        # A walked document the census could not read may declare the row; the
        # walk's enumeration, not a per-key row, is where that is recorded.
        with gzip.open(enumeration, "rt", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE))
        repeated = repeated_documents(rows)
        return [(document_subject(row, repeated), row["status"], row["sha256"])
                for row in rows if row["status"] != "readable"]
    return [(r["subject"], r["result"], "") for r in read_records(source)
            if r["key"] == key and r["kind"] == "document" and not r["result"].startswith("census ")]


def read_refused(source: str) -> dict[str, dict[str, str]]:
    """One source's census-refused documents by name, as `refuse` filed them."""
    path = source_dir(source) / REFUSED_FILE
    if not path.is_file():
        return {}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if tuple(reader.fieldnames or ()) != REFUSED_FIELDS:
            fail(f"{path} has header {reader.fieldnames}, not {list(REFUSED_FIELDS)}; restore it from git "
                 f"or re-run `refuse --source {source}`")
        rows = list(reader)
    for row in rows:
        if row["verdict"] not in REFUSED_VERDICTS or not re.fullmatch(r"[0-9a-f]{64}", row["sha256"]):
            fail(f"{path}: `{row['document']}` is not a {'/'.join(REFUSED_VERDICTS)} verdict over a SHA-256; "
                 f"re-run `refuse --source {source}`")
    return {row["document"]: row for row in rows}


def _refused_split(key: str, source: str) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    """One source's unread documents, split into the census-refused and the still unreadable.

    A walked document is refused only at the digest its parser read; a query
    source's names its commit, so its name is the identity.
    """
    refused_rows = read_refused(source)
    refused, unreadable = [], []
    for document, reason, sha256 in _unread(key, source):
        row = refused_rows.get(document)
        if row is not None and (not sha256 or row["sha256"] == sha256):
            refused.append((document, f"census-refused: {row['verdict']}"))
        else:
            unreadable.append((document, reason))
    return refused, unreadable


def _unreadable(key: str, source: str) -> list[tuple[str, str]]:
    """Documents of one source the census could not read and no full parser refused."""
    return _refused_split(key, source)[1]


def _refused(key: str, source: str) -> list[tuple[str, str]]:
    """Documents of one source a full standard parser refused; none of them is outstanding."""
    return _refused_split(key, source)[0]


HISTORICAL_SCREEN = "screened before the measured stage, with no measured record: re-screen it through `screen`"


def screen_states(key: str, source: str) -> dict[str, str]:
    """[`screen_states_in`] one declared source's evidence directory."""
    return screen_states_in(source_dir(source), key)


def screen_states_in(directory: Path, key: str) -> dict[str, str]:
    """Each screened candidate of one key, as a live decision reads its latest screen.

    `passing` and `refused` are measurements: a row whose measured record holds,
    or a Fern refusal of a candidate whose pinned run in `fern-rescreen.jsonl`
    `fern-rescreen` measured refusing it. Anything else is `historical` — filed before the
    measured stage, readable, and never read as a measurement: the candidate it
    names is still owed its screens.
    """
    screens = directory / "screens.jsonl"
    if not screens.is_file():
        return {}
    latest: dict[str, dict[str, Any]] = {}
    for row in read_jsonl(screens, ("key", "candidate"), "restore it from git; `screen` appends to it"):
        if row["key"] == key:
            latest[row["candidate"]] = row
    rescreen = directory / RESCREEN_FILE
    # A candidate `fern-rescreen` ran pinned Fern over and saw refused: that run,
    # not the wording its screen row was filed with, is the measurement.
    measured_refusals = {row["candidate"] for row in (
        read_jsonl(rescreen, ("sha256", "candidate", "check_exit"), "restore it from git")
        if rescreen.is_file() else []) if str(fern_verdict(row)).startswith("failed: ")}
    states = {}
    for candidate, row in latest.items():
        if "measured" in row and not SCREEN.measured_failures(row["measured"], directory):
            passed = all(outcome.startswith("passed") for outcome in SCREEN.outcomes(row["measured"]).values())
            states[candidate] = "passing" if passed else "refused"
        elif candidate in measured_refusals and row["fern"].startswith("failed: "):
            states[candidate] = "refused"
        else:
            states[candidate] = "historical"
    return states


def outstanding_items(key: str, source: str, build: str) -> list[tuple[str, str]]:
    """Every item one source still owes one key's search, each with what blocks it.

    Exactly the items [`_outstanding`] counts: a declarer with no probe of
    `build`, one whose probe timed out or left no profile, a reaching candidate
    whose only screen is historical, and every document the census could not
    read that no full standard parser refused.
    """
    records = [r for r in read_records(source) if r["key"] == key]
    declarers = {r["subject"] for r in records if r["kind"] == "document" and r["result"].startswith("census ")
                 and r["result"] != "census 0"}
    probes = {row["candidate"]: row for row in read_probes(source)
              if row["key"] == key and row.get("build") == build}
    items = [(c, f"unprobed on build {build}") for c in sorted(declarers - set(probes))]
    items += [(c, f"probe on build {build}: {probes[c]['status']}") for c in sorted(declarers & set(probes))
              if probes[c]["status"].startswith(("timeout", "no profile"))]
    historical = {c for c, state in screen_states(key, source).items() if state == "historical"}
    items += [(c, HISTORICAL_SCREEN) for c in sorted((historical & _reaching(key, source, build))
                                                       - fixture_declined(key, source))]
    return items + [(document, reason) for document, reason in _unreadable(key, source)]


def _tally(key: str, source: str, build: str) -> dict[str, int]:
    """What one source's evidence says about one key: declarers, and how each fared."""
    records = [r for r in read_records(source) if r["key"] == key]
    declarers = {r["subject"] for r in records if r["kind"] == "document" and r["result"].startswith("census ")
                 and r["result"] != "census 0"}
    refused, unreadable = _refused_split(key, source)
    # Only a probe of the measured build counts; one run while `src/` differed from
    # it read another arm's regions (see [`measured_build`]) and says nothing.
    probes = {row["candidate"]: row for row in read_probes(source)
              if row["key"] == key and row.get("build") == build}
    states = screen_states(key, source)
    declined = fixture_declined(key, source)
    # A historical screen settles nothing: only a measured one, or a fixture
    # decline, takes a candidate off the outstanding list.
    screened = {c for c, state in states.items() if state != "historical"} | declined
    historical = {c for c, state in states.items() if state == "historical"} - declined
    reaching = {c for c, row in probes.items() if row["reached"]}
    # A candidate is a declarer this build's probe finds reaching the arm; one
    # screened after an earlier build's probe that no longer reaches it holds
    # nothing open, however its screens read.
    passing = {c for c in (screened & reaching) - declined if states.get(c) == "passing"}
    return {
        "declarers": len(declarers),
        "unreadable": len(unreadable),
        "refused": len(refused),
        "probed": len(declarers & set(probes)),
        "timeouts": sum(1 for c in declarers if probes.get(c, {}).get("status", "").startswith("timeout")),
        "failed": sum(1 for c in declarers if probes.get(c, {}).get("status", "generated") not in ("generated",)
                      and not probes[c]["status"].startswith("timeout")),
        "unprofiled": sum(1 for c in declarers if probes.get(c, {}).get("status", "").startswith("no profile")),
        "reaching": len(reaching),
        "screened": len(reaching & screened),
        "historical": len(reaching & historical),
        "passing": len(passing),
    }


def _reaching(key: str, source: str, build: str) -> set[str]:
    """The declarers of one source whose probe of `build` executes an unreached site."""
    return {row["candidate"] for row in read_probes(source)
            if row["key"] == key and row.get("build") == build and row["reached"]}


def _outstanding(tally: dict[str, int]) -> int:
    """Declarers the arm may still be in: unprobed, timed out, unprofiled, unreadable, or historically screened."""
    return (tally["declarers"] - tally["probed"] + tally["timeouts"] + tally["unprofiled"]
            + tally["unreadable"] + tally["historical"])


def src_commits_since(build: str) -> list[str]:
    """Commits touching `src/` after the measured build, newest first, each cut to eight characters.

    Not `%h`: git lengthens that abbreviation as the object store grows, so the
    same history would render differently in a clone that has fetched more.
    """
    run = subprocess.run(["git", "log", "--format=%H", f"{build}..HEAD", "--", "src/"],
                         cwd=REPO, capture_output=True, text=True)
    if run.returncode != 0:
        fail(f"cannot read src/'s history since {build}: {run.stderr.strip()} — "
             "fetch that commit, or re-run `just golden-reach` on this checkout")
    return [commit[:8] for commit in run.stdout.split()]


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
        reached = not ledger_unreached(key)
        header = searched_for(key) if args.build or reached else (
            SEARCHED_FOR + ", ".join(f"`{_cell(s)}`" for s in unreached_sites(key)) + ".")
        tallies = {source: _tally(key, source, build) for source in DECLARED_SOURCES}
        moved = src_commits_since(build)
        outcome = args.outcome if args.outcome != "auto" else (
            "witness-found" if reached and not args.build else _outcome(tallies, bool(moved)))
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
            "spans and are not counted. The `outcome` column is this arm's search",
            "verdict: `exhausted` when nothing is outstanding, every declarer reaching",
            "the arm is screened, and none that passes every screen is left",
            "unregistered; `search-incomplete` otherwise.",
            "",
            "### Witness search (exhaustive)",
            "",
            "| key | source | outcome | queries | walk | candidates | screens |",
            "|---|---|---|---|---|---|---|",
        ]
        if reached and args.build:
            table = lines.index("### Witness search (exhaustive)")
            lines[table:table] = [
                "The arm this search looked for is now reached: a witness registered since",
                "reaches every handling site the ledger names for the row. The tables",
                "below record the search as it stood when the arm was still open.",
                "",
            ]
        elif reached:
            arms = probe_arms(key)
            gone = [s for s in searched_for(key)[len(SEARCHED_FOR):].split("`, `") if s.strip("`.")
                    and s.strip("`.").replace("\\|", "|") not in arms]
            table = lines.index("### Witness search (exhaustive)")
            lines[table:table] = [
                "The arm this search looked for is now reached, so the search reads",
                "`witness-found`: a witness registered since reaches every handling site the",
                "ledger names for the row. Its declarers are still probed on the counted build,",
                "against the arm as it resolves in today's `src/`, so none is left unprobed."
                + (" A site a later repair restructured out of `src/` resolves nowhere: "
                   + ", ".join(f"`{s.strip('`.')}`" for s in gone) + (
                       ". The declarers are probed against the arm's remaining sites."
                       if len(gone) < len(searched_for(key)[len(SEARCHED_FOR):].split("`, `")) else
                       ". The declarers are probed against the row's handling sites as the ledger "
                       "names them today: " + ", ".join(f"`{_cell(a)}`" for a in arms) + ".")
                   if gone else ""),
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
            candidates, screen_cell = _candidate_cells(records)
            lines.append(
                f"| `{key}` | `{source}` | `{outcome}` | {queries} | {walks} | {candidates} | {screen_cell} |"
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
            "and the unreadable. A document the census could not read that a full",
            "standard parser rejects on syntax, or reads as no OpenAPI or Swagger",
            "description, is `census-refused` instead: listed with that parser's",
            "error, its version and the document's digest in the source's",
            f"`{REFUSED_FILE}`, it is not outstanding, and it never settles a",
            "search on its own.",
        ]
        lines += _historical_note(tallies)
        if moved:
            lines += [
                "",
                f"When this record was rendered, `src/` had moved since that build "
                f"({', '.join(f'`{c}`' for c in moved)}), so every probe counted here must be",
                "re-taken on a fresh `just golden-reach` measurement before it is reused.",
            ]
        lines += [
            "",
            "| source | declarers | unreadable | census-refused | probed | unprobed | timed out | crozier failed "
            "| reach an arm | screened | outstanding |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ] + [
            f"| `{source}` | {t['declarers']} | {t['unreadable']} | {t['refused']} | {t['probed']} "
            f"| {t['declarers'] - t['probed']} "
            f"| {t['timeouts']} | {t['failed']} | {t['reaching']} | {t['screened']} | {_outstanding(t)} |"
            for source, t in tallies.items()
        ]
        if outcome == "exhausted" and ledger_unreached(key):
            lines += ["", _exhausted_verdict(key, build)]
        lines += _dispositions(key, build)
        path = EVIDENCE / "searches" / f"{key}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


def _candidate_cells(records: list[dict[str, str]]) -> tuple[str, str]:
    """A source line's `candidates` and `screens` cells, off its `records.tsv` rows for one key."""
    reaching = [r["subject"] for r in records if r["kind"] == "candidate"]
    screens: dict[str, dict[str, str]] = {}
    for r in records:
        if r["kind"] == "screen":
            candidate, screen_name = r["subject"].rsplit(" ", 1)
            screens.setdefault(candidate, {})[screen_name] = r["result"]
    screen_cell = "; ".join(
        f"`{c}` " + " ".join(f"{s} `{screens[c][s]}`" for s in ("licence", "ref", "fern") if s in screens[c])
        for c in reaching if c in screens) or "—"
    return ", ".join(f"`{c}`" for c in reaching) or "—", _cell(screen_cell)


HISTORICAL_NOTE = "candidate(s) reaching the arm carry only a historical screen"


def _historical_note(tallies: dict[str, dict[str, int]]) -> list[str]:
    historical = sum(t["historical"] for t in tallies.values())
    return [
        "",
        f"{historical} {HISTORICAL_NOTE}: one filed",
        "before the measured screening stage (`tools/witness-search/witness_screen.py`), with no exit",
        "status, pins or redacted log behind its outcomes. A historical screen is kept as",
        "it was filed and settles nothing, so each such candidate is outstanding — counted",
        "in `outstanding` below and listed in `outstanding.tsv` — until it is re-screened.",
    ] if historical else []


def _exhausted_verdict(key: str, build: str) -> str:
    fixtures = sum(len(fixture_declined(key, source) & _reaching(key, source, build))
                   for source in DECLARED_SOURCES)
    return (f"**Verdict: `exhausted`.** No real-world document in the six declared sources "
            "both declares this row and reaches the arm while passing every screen, so the "
            "arm has no real witness and stays open."
            + (f" The {fixtures} test fixture(s) that do reach it are hand-written, not "
               "specifications, and settle nothing." if fixtures else ""))


CELL_BREAK = re.compile(r"(?<!\\) \| ")


GENERATED_DISPOSITIONS = ("- **Hand-off**", "- **Registered**", "- **No longer a candidate**", "- **Declined**")


def _restated_dispositions(section: list[str], generated: list[str]) -> list[str]:
    """A record's dispositions section, the bullets `render` writes restated and any other kept.

    Left exactly as it stands when those bullets have not moved, so a bullet
    written beside them (a withdrawn registration, say) keeps its place.
    """
    wanted = [line for line in generated if line.startswith(GENERATED_DISPOSITIONS)]
    if [line for line in section if line.startswith(GENERATED_DISPOSITIONS)] == wanted:
        return section
    kept = [line for line in section[1:] if line.startswith("- ") and not line.startswith(GENERATED_DISPOSITIONS)]
    return ["#### Candidates passing every screen", "", *wanted, *kept, ""]


def restate(args: argparse.Namespace) -> int:
    """Restate what screening evidence moved since a committed record was rendered, in place.

    A record is rendered once, as of its build; re-rendering one after `src/`
    has moved past that build re-reads everything. This restates only what a
    screen filed since changes — each line's candidates and screens, the
    declarer table's `screened` and `outstanding`, the historical-screen note,
    the candidates passing every screen, and the outcome where those move it —
    and keeps the rest as rendered. A record moved to `exhausted` is refused:
    that reading owes a full `render`.
    """
    keys = args.key or [p.stem for p in probed_records()]
    changed = 0
    for key in keys:
        path = EVIDENCE / "searches" / f"{key}.md"
        text = path.read_text(encoding="utf-8")
        build = record_build(text, path)
        tallies = {source: _tally(key, source, build) for source in DECLARED_SOURCES}
        lines = text.split("\n")
        prefix = f"| `{key}` | `"
        stated = {CELL_BREAK.split(line)[2].strip("`") for line in lines if line.startswith(prefix)}
        outcome = stated.pop() if len(stated) == 1 else fail(
            f"{path.name}: its lines read {sorted(stated)}, not one outcome; render it again with "
            f"`render --key {key} --build {build}` before restating it")
        if outcome != "witness-found":
            restated = _outcome(tallies)
            if restated == "exhausted" and outcome != "exhausted":
                fail(f"{path.name}: its evidence now reads `exhausted`; render it with `render --key {key}`")
            outcome = restated
        dispositions = _dispositions(key, build)
        verdict = [_exhausted_verdict(key, build)] if outcome == "exhausted" else []
        out: list[str] = []
        in_note = in_dispositions = disposed = False
        section: list[str] = []
        for line in lines:
            if in_note or in_dispositions:
                # A paragraph runs to its blank line; the dispositions section to
                # the next heading, which a later section of the record opens.
                if in_note and line:
                    continue
                if in_dispositions and not line.startswith("#"):
                    section.append(line)
                    continue
                if in_dispositions:
                    out += _restated_dispositions(section, dispositions)
                in_note = in_dispositions = False
                if not line:
                    continue
            if line.startswith(prefix):
                cells = CELL_BREAK.split(line)
                source = cells[1].strip("`")
                records = [r for r in read_records(source) if r["key"] == key]
                candidates, screens = _candidate_cells(records)
                line = " | ".join([*cells[:2], f"`{outcome}`", cells[3], cells[4], candidates, screens]) + " |"
            elif (row := re.match(r"^\| `([\w.-]+)` \|((?: \d+ \|){10})$", line)) and row.group(1) in tallies:
                counts = row.group(2).split("|")[:-1]
                t = tallies[row.group(1)]
                counts[-2:] = [f" {t['screened']} ", f" {_outstanding(t)} "]
                line = f"| `{row.group(1)}` |" + "|".join(counts) + "|"
            elif line.startswith("| source | declarers |"):
                while out and out[-1] == "":
                    out.pop()
                out += _historical_note(tallies) + [""]
            elif HISTORICAL_NOTE in line:
                in_note = True
                if out and out[-1] == "":
                    out.pop()
                continue
            elif line.startswith("**Verdict: `exhausted`.**"):
                if out and out[-1] == "":
                    out.pop()
                out += [""] + verdict if verdict else []
                continue
            elif line == "#### Candidates passing every screen":
                section = [line]
                in_dispositions = disposed = True
                continue
            out.append(line)
        if in_dispositions:
            out += _restated_dispositions(section, dispositions)
        if verdict and not any(line.startswith("**Verdict: `exhausted`.**") for line in lines):
            fail(f"{path.name}: its evidence now reads `exhausted`; render it with `render --key {key}`")
        if dispositions and not disposed:
            while out and out[-1] == "":
                out.pop()
            out += dispositions + [""]
        while len(out) > 1 and out[-1] == "" and out[-2] == "":
            out.pop()
        if out[-1] != "":
            out.append("")
        restated_text = "\n".join(out)
        if restated_text != text:
            path.write_text(restated_text, encoding="utf-8")
            changed += 1
    print(f"golden-reach-search: {changed} record(s) restated")
    return 0




OUTSTANDING = EVIDENCE / "outstanding.tsv"
OUTSTANDING_FIELDS = ("key", "source", "item", "blocker", "build", "src_moved_since")
RECORD_BUILD = re.compile(r"^build `([0-9a-f]+)` only\.", re.M)
# A record whose arm only a generation setting reaches: no search ran, so it
# counts no probe build and owes no item (`RankedBacklogTests` gates its form).
CONFIG_GATE_HEADING = "### Configuration gate"


def probed_records() -> list[Path]:
    """Every committed arm-search record that counts probes, leaving out the configuration-gated ones."""
    return [path for path in sorted((EVIDENCE / "searches").glob("*.md"))
            if CONFIG_GATE_HEADING not in path.read_text(encoding="utf-8").splitlines()]


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
    for path in probed_records():
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


YAML_LOADER = f"ruamel.yaml {RUAMEL_YAML_PIN} (YAML 1.2)"


def _ruamel_yaml() -> ModuleType:
    """ruamel.yaml at the pinned version, or a refusal naming how to run with it."""
    try:
        import ruamel.yaml
    except ModuleNotFoundError:
        fail(f"this stage reads YAML with ruamel.yaml {RUAMEL_YAML_PIN}, a full YAML 1.2 parser; run it as "
             "`uv run tools/surface-census/golden-reach-search.py ...`, whose inline metadata pins it")
    if ruamel.yaml.__version__ != RUAMEL_YAML_PIN:
        fail(f"ruamel.yaml {ruamel.yaml.__version__} is installed, not the pinned {RUAMEL_YAML_PIN}; "
             "run through `uv run tools/surface-census/golden-reach-search.py ...`")
    return ruamel.yaml


def yaml_stream(data: bytes) -> list[Any]:
    """Every document of a YAML stream as the pinned ruamel.yaml reads it.

    A timestamp stays the text it is written as, which is how the census's own
    loader reads one, so a census over this reading counts the same example
    shapes the stdlib loader's would.
    """
    ruamel_yaml = _ruamel_yaml()

    class TextTimestamps(ruamel_yaml.constructor.SafeConstructor):
        pass

    TextTimestamps.add_constructor("tag:yaml.org,2002:timestamp", ruamel_yaml.constructor.SafeConstructor.construct_yaml_str)
    reader = ruamel_yaml.YAML(typ="safe", pure=True)
    reader.Constructor = TextTimestamps
    return list(reader.load_all(data))


def _names_a_version(document: Any) -> bool:
    return isinstance(document, dict) and ("openapi" in document or "swagger" in document)


def fallback_reading(path: Path, data: bytes) -> tuple[Any, str] | None:
    """The description the pinned YAML parser reads where the census's stdlib loader cannot.

    Only for a YAML document the stdlib loader refuses: `(document, loader)`
    when the stream holds exactly one document naming an OpenAPI or Swagger
    version (a Jekyll page's front matter ahead of it included), `None` when the
    stdlib loader reads it or the full parser finds no one description in it.
    """
    if path.suffix == ".json":
        return None
    try:
        CENSUS.load_document(path)
        return None
    except Exception:  # the census's own refusal, whatever its type
        pass
    try:
        stream = yaml_stream(data)
    except Exception:  # a syntax rejection: `refuse`'s to file, not a reading
        return None
    described = [(index, document) for index, document in enumerate(stream, start=1)
                 if _names_a_version(document)]
    if len(described) != 1:
        return None
    index, document = described[0]
    where = "" if len(stream) == 1 else f", document {index} of {len(stream)}"
    return document, YAML_LOADER + where


def parse_verdict(path: Path, data: bytes) -> tuple[str, str, str] | None:
    """A full standard parser's reading of a document the census could not read.

    `(parser, verdict, evidence)` when the parser rejects it on syntax, or reads it
    as no OpenAPI or Swagger description; `None` when it reads a description, so
    the census alone failed on it and it stays outstanding. JSON is read with
    Python's `json` module and YAML with ruamel.yaml, a full YAML 1.2 parser.
    """
    if path.suffix == ".json":
        parser = f"python json {sys.version.split()[0]}"
        try:
            parsed = json.loads(data)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            return parser, "syntax", _one_line(f"{type(error).__name__}: {error}")
    else:
        parser = YAML_LOADER
        try:
            # A stream of several documents is YAML all the same; read it whole.
            stream = yaml_stream(data)
        except Exception as error:  # ruamel's parse errors share no base class it exports
            return parser, "syntax", _one_line(f"{type(error).__name__}: {error}")
        if len(stream) != 1:
            if any(_names_a_version(d) for d in stream):
                return None
            return parser, "not-openapi", (f"parses as a stream of {len(stream)} YAML documents, none naming an "
                                           "`openapi` or `swagger` version")
        parsed = stream[0]
    if _names_a_version(parsed):
        return None
    shape = (f"top-level keys {sorted(str(k) for k in parsed)[:12]}" if isinstance(parsed, dict)
             else f"top level is a {type(parsed).__name__}")
    return parser, "not-openapi", f"parses, but names no `openapi` or `swagger` version: {shape}"


def _one_line(text: str) -> str:
    """A parser's message as one TSV cell: whitespace runs, newlines and tabs included, are one space."""
    return " ".join(text.split())


def local_copies(
    source: str, root: Path | None, fetch: bool, every: bool = False, timed_out: bool = False
) -> dict[str, tuple[Path, str]]:
    """Local copies of one source's documents to read again, each with its pinned digest.

    By default these are the documents the census could not read: a walk's
    unreadable enumeration rows (a census cut off by time is not a reading to
    settle), and a query source's parse failures and census refusals, each at
    the cached copy `candidates.jsonl` names. With `every`, a query source's
    every fetched document is returned, read or not, so a census can be taken
    over each again; with `timed_out`, a walked document whose census was cut
    off by time is too. With `fetch`, a query-source copy this checkout's cache
    lacks is fetched at its commit through the acquirer's exact-commit raw
    route, and kept only if it is the candidate's blob (or, where the candidate
    names no blob, its digest).
    """
    unread: dict[str, tuple[Path, str]] = {}
    if source in WALKS:
        if root is None:
            fail(f"{source} is a walk; pass --root with its local copy")
        by_digest: dict[str, Path] = {}
        if source == "github-publisher-trees":
            for path in root.rglob("*"):
                if path.is_file() and path.suffix in (".json", ".yaml", ".yml"):
                    by_digest.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(), path)
        enumeration = source_dir(source) / "enumeration.tsv.gz"
        with gzip.open(enumeration, "rt", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE))
        # A path two trees pin is two documents, each named `<walk>:<path>` as the
        # records name it, so neither copy's reading stands in for the other's.
        repeated = repeated_documents(rows)
        for row in rows:
            cut_off = row["status"].startswith("unreadable: census exceeded")
            if row["status"] != "readable" and (timed_out or not cut_off):
                unread[document_subject(row, repeated)] = (locate(source, root, row, by_digest), row["sha256"])
        return unread
    fetched: dict[str, dict[str, Any]] = {}
    ledger = source_dir(source) / "candidates.jsonl"
    if ledger.is_file():
        for row in read_jsonl(ledger, ("repository", "path", "commit"), "restore it from git"):
            if row.get("document"):
                fetched.setdefault(f"{row['repository']}:{row['path']}@{row['commit']}", row)
    acquirer = None
    index = candidate_index(source)
    for record in read_records(source):
        if record["kind"] != "document":
            continue
        if not (every and record["result"].startswith("census ")) and not record["result"].startswith(
                ("acquisition-failure: parse-failure", "unreadable: ")):
            continue
        row = fetched.get(record["subject"])
        if row is None:
            unread[record["subject"]] = (CACHE / source / "missing", "")
            continue
        local = CACHE / source / "documents" / row["document"]
        if fetch and not local.is_file() and (row.get("blob") or row.get("sha256")):
            if acquirer is None:
                github = _load("witness_search_github", REPO / "tools" / "witness-search" / "witness-search-github.py")
                acquirer = github.Acquirer(source_dir(source), cache=CACHE / source, **ACQUIRER_OPTIONS)
            repository = row["repository"].removeprefix("github.com/")
            url = f"{acquirer.raw_github_url}/{repository}/{row['commit']}/{urllib.parse.quote(row['path'])}"
            status, data = acquirer.raw_github_get(url, "*", f"{repository}:{row['path']}")
            # Sourcegraph names no blob; its candidate's recorded digest pins the bytes instead.
            pinned = git_blob(data) == row["blob"] if row.get("blob") else hashlib.sha256(data).hexdigest() == row["sha256"]
            if status == 200 and pinned:
                local.parent.mkdir(parents=True, exist_ok=True)
                local.write_bytes(data)
        if local.is_file():
            index[record["subject"]] = row["document"]
        unread[record["subject"]] = (local, row.get("sha256") or Path(row["document"]).stem.split(".")[0])
    if fetch:
        path = CACHE / source / "candidate-documents.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(index, sort_keys=True, indent=0), encoding="utf-8")
        if acquirer is not None:
            record_guard_logs(source)
    return unread


def read_fallback(source: str) -> dict[str, dict[str, str]]:
    """One source's documents the census read through the pinned YAML parser, by name."""
    path = source_dir(source) / FALLBACK_FILE
    if not path.is_file():
        return {}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if tuple(reader.fieldnames or ()) != FALLBACK_FIELDS:
            fail(f"{path} has header {reader.fieldnames}, not {list(FALLBACK_FIELDS)}; restore it from git "
                 f"or re-run `recensus --source {source}`")
        return {row["document"]: row for row in reader}


def recensus(args: argparse.Namespace) -> int:
    """Count again each unread document, through the pinned YAML parser where the stdlib census refuses it.

    A walk's unread documents, and a query source's every fetched one, are read
    with the census's stdlib loader first; only a YAML document it refuses and
    ruamel.yaml reads as one description is read through ruamel.yaml. The
    census's own object-model walk counts either reading, and a document it
    reads leaves the unread list as any read one would — a walk's enumeration
    row reads `readable` with the keys it declares, and a query source's record
    its `census N`. Each document read through ruamel.yaml is named with that
    loader in the source's `census-fallback.tsv`. A document the full parser
    also refuses is `refuse`'s to file.
    """
    source = args.source
    # A query source's census was taken when each document was fetched, so a
    # loader repair since reaches it only by counting every cached copy again.
    copies = local_copies(source, args.root, fetch=True, every=source not in WALKS, timed_out=True)
    refused = read_refused(source)
    readings: dict[str, tuple[dict[str, int], Any, str, str]] = {}
    for document, (local, sha256) in sorted(copies.items()):
        if document in refused or not local.is_file():
            continue
        data = local.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if sha256 and digest != sha256:
            continue
        try:
            parsed, loader = CENSUS.load_document(local), ""
        except Exception:  # the census's own refusal, whatever its type
            reading = fallback_reading(local, data)
            if reading is None:
                continue
            parsed, loader = reading
        if not isinstance(parsed, dict):
            continue
        try:
            counts = CENSUS.census_document(parsed, root_path=local) if str(parsed.get("openapi", "")).startswith("3") else {}
        except Exception:  # the census's walk refused this reading too: it stays outstanding
            continue
        readings[document] = (counts, parsed, loader, digest)

    def count(key: str, counts: dict[str, int], parsed: Any) -> int:
        if key in PREDICATE_ROWS:
            return PREDICATE_ROWS[key][1](parsed) if str(parsed.get("openapi", "")).startswith("3") else 0
        return declared(counts, selectors_of(key))

    records = read_records(source)
    if source in WALKS:
        walked = sorted({r["key"] for r in records if r["kind"] == "walk"})
        repeated = repeated_documents(pinned_listing(source))
        enumeration = source_dir(source) / "enumeration.tsv.gz"
        # Read in the dialect `walk` writes, so a status the walk quoted round-trips.
        with gzip.open(enumeration, "rt", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
        added: list[dict[str, str]] = []
        for row in rows:
            if document_subject(row, repeated) not in readings:
                continue
            counts, parsed, _loader, _digest = readings[document_subject(row, repeated)]
            found = {key: n for key in walked for n in [count(key, counts, parsed)] if n}
            row["status"], row["matched_keys"] = "readable", ",".join(found)
            added += [{"key": key, "kind": "document", "subject": document_subject(row, repeated),
                       "result": f"census {n}", "file": enumeration.name} for key, n in found.items()]
        with gzip.open(enumeration, "wt", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, WALK_FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        replace_records(source, records + added)
    else:
        for record in records:
            if record["kind"] == "document" and record["subject"] in readings:
                counts, parsed, _loader, _digest = readings[record["subject"]]
                record["result"] = f"census {count(record['key'], counts, parsed)}"
        replace_records(source, records)
    filed = {document: row for document, row in read_fallback(source).items() if document not in readings}
    filed.update({document: {"document": document, "sha256": digest, "loader": loader}
                  for document, (_counts, _parsed, loader, digest) in readings.items() if loader})
    with (source_dir(source) / FALLBACK_FILE).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, FALLBACK_FIELDS, delimiter="\t", lineterminator="\n",
                                quoting=csv.QUOTE_NONE, quotechar=None)
        writer.writeheader()
        writer.writerows(filed[document] for document in sorted(filed))
    fallback = sum(1 for _counts, _parsed, loader, _digest in readings.values() if loader)
    print(f"golden-reach-search: {source}: {len(readings)} of {len(copies)} documents counted, "
          f"{fallback} through {YAML_LOADER}")
    return 0


def refuse(args: argparse.Namespace) -> int:
    """File which of a source's unread documents a full standard parser refuses.

    Reads every document the census could not read — a walk's unreadable
    enumeration rows, a query source's parse failures and census refusals — at
    its pinned digest and writes the refused ones to the source's
    `census-refused.tsv`. A document the parser reads as a description is left
    out: the census alone failed on it, and it stays outstanding.
    """
    source = args.source
    unread = local_copies(source, args.root, fetch=False)
    rows, kept = [], 0
    for document, (local, sha256) in sorted(unread.items()):
        if not local.is_file():
            continue
        data = local.read_bytes()
        if hashlib.sha256(data).hexdigest() != sha256:
            continue
        verdict = parse_verdict(local, data)
        if verdict is None:
            kept += 1
            continue
        parser, kind, evidence = verdict
        rows.append({"document": document, "sha256": sha256, "parser": parser, "verdict": kind,
                     "evidence": evidence})
    with (source_dir(source) / REFUSED_FILE).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, REFUSED_FIELDS, delimiter="\t", lineterminator="\n",
                                quoting=csv.QUOTE_NONE, quotechar=None)
        writer.writeheader()
        writer.writerows(rows)
    print(f"golden-reach-search: {source}: {len(unread)} unread, {len(rows)} census-refused, "
          f"{kept} read by the full parser (still outstanding), {len(unread) - len(rows) - kept} without local bytes")
    return 0

RESCREEN_FILE = "fern-rescreen.jsonl"
RESCREEN_CACHE = "fern-rescreen-cache.jsonl"


# The pinned, measured Fern runner is the screening stage's own; these names are
# kept here because `fern-rescreen` and its tests read them off this module.
corpus_fern_pins = SCREEN.corpus_fern_pins
fern_workspace_files = SCREEN.fern_workspace_files
fern_label = SCREEN.fern_label
fern_diagnostic = SCREEN.fern_diagnostic
fern_screen_document = SCREEN.fern_screen_document
fern_verdict = SCREEN.fern_verdict
UNPARSED = SCREEN.UNPARSED


# What a kept `candidate` row's result says once the counted build's probe of it
# executes no unreached site: it stays on the record, accounted for, and Contract
# B's gate reads it as no candidate after checking `probe.jsonl` carries that probe.
NOT_REACHING = "its probe of build {build} in probe.jsonl reaches no unreached site"


def retire(args: argparse.Namespace) -> int:
    """Mark the candidates the counted build no longer finds declaring the row or reaching its arm.

    A candidate is a screened declarer whose probe executes an unreached site. A
    census repair can find a document no longer declares the row, and a `src/`
    repair can leave its probe reaching nothing; either way a screen filed
    earlier vouches for nothing now. Every row stays, so nothing returned goes
    unaccounted for: a document the census no longer counts reads `census 0`,
    the census's own reading, and one whose probe of this build reaches no site
    reads its census count followed by [`NOT_REACHING`]. A declarer with no probe
    of this build is left as it is: it is outstanding, not settled.
    """
    build = _current_build()
    keys = set(args.key or (p.stem for p in probed_records()
                            if record_build(p.read_text(encoding="utf-8"), p) == build))
    note = NOT_REACHING.format(build=build)
    marked = 0
    for source in DECLARED_SOURCES:
        records = read_records(source)
        declared = {(r["key"], r["subject"]): r["result"] for r in records
                    if r["kind"] == "document" and r["result"].startswith("census ") and r["result"] != "census 0"}
        probed = {(row["key"], row["candidate"]): row for row in read_probes(source) if row.get("build") == build}
        changed = 0
        for r in records:
            if r["key"] not in keys or r["kind"] != "candidate":
                continue
            pair = (r["key"], r["subject"])
            if pair not in declared:
                result = "census 0"
            elif pair in probed and not probed[pair]["reached"]:
                result = f"{declared[pair]} — {note}"
            else:
                continue
            if r["result"] != result:
                r["result"] = result
                changed += 1
        if changed:
            replace_records(source, records)
        marked += changed
    print(f"golden-reach-search: {marked} candidate(s) marked on build {build}")
    return 0


def fern_rescreen(args: argparse.Namespace) -> int:
    """Take Fern's screen again, measured, for every reaching declarer its last screen refused.

    Only a declarer this build's probe finds reaching the arm is a candidate, and
    only a Fern refusal filed without an exit status is taken again, whatever
    the candidate's other screens read: a refusal is quoted with its status. Each
    distinct document runs once: `fern check` at the pinned CLI, and where that
    exits 0, the generation `generate-fern-fixture.sh` runs, since only a
    generation settles it. The screen is re-filed with the exit status and the
    first diagnostic Fern printed. A run that times out is recorded and leaves the
    old screen in place, so the declarer stays open rather than settled.
    """
    build = _current_build()
    keys = args.key or sorted(p.stem for p in probed_records()
                              if record_build(p.read_text(encoding="utf-8"), p) == build)
    wanted: dict[str, list[tuple[str, str, dict[str, Any]]]] = defaultdict(list)
    paths: dict[str, Path] = {}
    for key in keys:
        reaching = _reaching(key, args.source, build)
        latest: dict[str, dict[str, Any]] = {}
        screens = source_dir(args.source) / "screens.jsonl"
        if screens.is_file():
            for row in read_jsonl(screens, ("key", "candidate"), "restore it from git; `screen` appends to it"):
                if row["key"] == key:
                    latest[row["candidate"]] = row
        located = dict(declarers(args.source, key, args.root)) if reaching else {}
        for candidate in sorted(reaching):
            row = latest.get(candidate)
            # A refusal already measured here stands; only one filed without
            # Fern's exit status is taken again.
            if not row or "measured" in row or row["fern"] == "passed" \
                    or row["fern"].startswith(f"failed: {fern_label()} fern "):
                continue
            path = located.get(candidate)
            if path is None or not path.is_file():
                fail(f"{args.source}: no local bytes for {candidate}; pass --root with the walk's copy, "
                     "or `query` the source again to cache it")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            wanted[digest].append((key, candidate, row))
            paths.setdefault(digest, path)
    cache_path = CACHE / RESCREEN_CACHE
    cache: dict[str, dict[str, Any]] = {}
    if cache_path.is_file():
        for row in read_jsonl(cache_path, ("sha256",), "delete it; a re-screen re-runs"):
            cache[row["sha256"]] = row
    todo = [digest for digest in wanted if digest not in cache or fern_verdict(cache[digest]) is None]
    with tempfile.TemporaryDirectory(prefix="golden-reach-fern-") as scratch, \
            ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {digest: pool.submit(fern_screen_document, paths[digest], Path(scratch), args.timeout)
                   for digest in todo}
        for digest, future in futures.items():
            result = future.result()
            result.pop("logs")
            cache[digest] = result
            CACHE.mkdir(parents=True, exist_ok=True)
            with exclusive_lock(CACHE / f"{RESCREEN_CACHE}.lock"), cache_path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(result, sort_keys=True) + "\n")
    evidence = source_dir(args.source) / RESCREEN_FILE
    kept = [row for row in read_jsonl(evidence, ("sha256", "candidate"), "restore it from git")
            if row["sha256"] not in wanted] if evidence.is_file() else []
    filed = unsettled = 0
    for digest, uses in wanted.items():
        result = cache[digest]
        kept += [dict(result, candidate=candidate) for candidate in sorted({c for _k, c, _r in uses})]
        verdict = fern_verdict(result)
        if verdict is None:
            unsettled += len(uses)
            continue
        for key, candidate, row in uses:
            # Its licence and ref stay as historically filed; the Fern refusal is
            # measured, and `fern-rescreen.jsonl` carries the run that measured it.
            file_screen(args.source, key, candidate, {
                "licence": row["licence"], "ref": row["ref"], "fern": verdict,
                "gap_keys": row.get("gap_keys", ""), "declined": "", "registered": "",
                "evidence": f"{row.get('evidence', '')} — re-screened: {RESCREEN_FILE} sha256 {digest[:12]}".lstrip(" —"),
            })
            filed += 1
    evidence.write_text("".join(json.dumps(r, sort_keys=True) + "\n"
                                for r in sorted(kept, key=lambda r: (r["candidate"], r["sha256"]))), encoding="utf-8")
    print(f"golden-reach-search: {args.source}: {len(wanted)} documents re-screened, {filed} screens re-filed, "
          f"{unsettled} left on their earlier screen by a timeout")
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
    w.add_argument("--census-timeout", type=REACH.positive_int, default=600,
                   help="seconds one document's census may take before it is recorded unreadable")
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
    # Refused when given: an outcome is measured, never stated.
    for stated in ("--licence", "--ref", "--fern"):
        s.add_argument(stated, help=argparse.SUPPRESS)
    s.add_argument("--measured", type=Path, help="a record tools/witness-search/witness_screen.py measured, filed as it stands")
    s.add_argument("--licence-refusal", default="", help="refuse a licence the measured reading would pass, and why")
    s.add_argument("--timeout", type=REACH.positive_int, default=1800)
    s.add_argument("--gap-keys", default="")
    s.add_argument("--evidence", default="")
    s.add_argument("--declined", default="", help="why a candidate passing every screen is not registered")
    s.add_argument("--registered", default="", help="the corpus row a candidate passing every screen is registered as")
    fr = sub.add_parser("fern-rescreen")
    fr.add_argument("--source", required=True)
    fr.add_argument("--key", action="append", help="default: every record counted on the measured build")
    fr.add_argument("--root", type=Path, help="a walk's local copy of the pinned documents")
    fr.add_argument("--jobs", type=REACH.positive_int, default=6)
    fr.add_argument("--timeout", type=REACH.positive_int, default=1800)
    rt = sub.add_parser("retire")
    rt.add_argument("--key", action="append", help="default: every record counted on the measured build")
    r = sub.add_parser("render")
    r.add_argument("--key", action="append", required=True)
    r.add_argument("--outcome", default="auto", choices=("auto", "exhausted", "search-incomplete", "witness-found"))
    r.add_argument("--build", help="re-render a committed record as of the earlier build its probes ran on")
    rs = sub.add_parser("restate", help="restate a committed record's screens and counts from moved evidence")
    rs.add_argument("--key", action="append", help="default: every probed record")
    sub.add_parser("outstanding")
    for name in ("refuse", "recensus"):
        x = sub.add_parser(name)
        x.add_argument("--source", required=True)
        x.add_argument("--root", type=Path, help="a walk's local copy of the pinned documents")
    args = parser.parse_args(argv)
    return {"walk": walk, "fetch-pins": fetch_pins, "query": query, "probe": probe, "screen": screen, "fern-rescreen": fern_rescreen, "retire": retire, "render": render, "restate": restate,
            "outstanding": outstanding, "refuse": refuse, "recensus": recensus}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
