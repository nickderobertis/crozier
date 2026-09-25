#!/usr/bin/env python3
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
  build `just golden-reach` measures with; the row's unreached sites it executes
  go to ``probe.jsonl``. A declarer that executes one is the row's ``candidate``,
  and only a candidate owes the three screens: a declarer that never reaches the
  arm is no witness for it, however it screens.
* ``render`` — the row's search record,
  ``golden-reach-witnesses/searches/<key>.md``: one line per declared source.

Screens are recorded by ``screen``, which takes the outcome and the evidence it
rests on from the caller: a licence, an immutable ref and Fern's acceptance are
each a measurement taken elsewhere (the corpus licence rule, the source's pin,
`scripts/generate-fern-fixture.sh`), and this script only files them.

Every GitHub and Sourcegraph call goes through `scripts/rate_limit_guard.py`, by
way of the acquirer; this script opens no socket of its own.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import http.client
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import urllib.parse
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from pathlib import Path
from typing import Any

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


def _load(name: str, path: Path) -> Any:
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


# ------------------------------------------------------------------ the keys


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
PREDICATE_ROWS: dict[str, tuple[str, Any]] = {
    "media-type-key-parameters": (r"/[A-Za-z0-9.+-]+\s*;\s*[A-Za-z0-9_-]+\s*=", _parameterized_media_keys),
}


def selectors_of(key: str) -> tuple[str, ...]:
    """The census selectors a row's witnesses are read off (its site-table row)."""
    table = REACH.read_sites_table()
    if key not in table:
        fail(f"{key} is not a golden row of the site table")
    if key in PREDICATE_ROWS:
        return (f"predicate:{key}",)
    selectors = tuple(s for s in table[key].selectors if not s.startswith("fixture="))
    if not selectors:
        fail(f"{key} names its witnesses directly; no census selector can search for it")
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


def unreached_sites(key: str) -> tuple[str, ...]:
    """The row's unreached handling sites in the committed ledger — the arm searched for."""
    for _rank, reach in REACH.read_ledger():
        if reach.key == key:
            sites = tuple(spec for spec, hit, _total in reach.sites if not hit)
            if not sites:
                fail(f"{key} reaches every handling site; there is no arm to search for")
            return sites
    fail(f"{key} is not in the ledger")
    raise AssertionError


def declared(counts: dict[str, int], selectors: tuple[str, ...]) -> int:
    return sum(counts.get(selector, 0) for selector in selectors)


# ------------------------------------------------------------------ evidence


def source_dir(source: str) -> Path:
    if source not in DECLARED_SOURCES:
        fail(f"{source} is not a declared source")
    path = EVIDENCE / source
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_records(source: str) -> list[dict[str, str]]:
    path = source_dir(source) / "records.tsv"
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_records(source: str, keys: set[str], rows: list[dict[str, str]]) -> None:
    """Replace `keys`' rows of one source's records.tsv, keeping every other key's."""
    kept = [row for row in read_records(source) if row["key"] not in keys]
    path = source_dir(source) / "records.tsv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, RECORD_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in sorted(kept + rows, key=lambda r: (r["key"], r["kind"], r["subject"])):
            writer.writerow(row)


# The guard's own logs: every call and wait `scripts/rate_limit_guard.py` made for
# this source's searches. Contract B names each evidence file from a records row,
# so each log is filed as a `wait` row under the pseudo-key `*` it answers for.
GUARD_LOGS = (
    "rate-limit-calls.jsonl",
    "rate-limit-waits.jsonl",
    "raw-github-calls.jsonl",
    "raw-github-waits.jsonl",
    "index-pacing-waits.jsonl",
)


def record_guard_logs(source: str) -> None:
    directory = source_dir(source)
    rows = []
    for name in GUARD_LOGS:
        path = directory / name
        if path.is_file():
            calls = sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
            rows.append({"key": "*", "kind": "wait", "subject": f"{source} guard log {name}",
                         "result": f"{calls} entries", "file": name})
    write_records(source, {"*"}, rows)


# ---------------------------------------------------------------------- walk


PIN_FIELDS = ("walk", "document", "revision", "blob", "sha256")


def git_blob(data: bytes) -> str:
    """Git's own content hash of a file, which every publisher-tree pin records."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


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
        with resolved.open(encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle, delimiter="\t"))
    with (shared / "acquisition-manifest.tsv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    immutable = [row for row in rows if len(row["revision"]) == 40]
    if not immutable:
        fail(f"{source}'s acquisition manifest names no document at an immutable ref")
    return immutable


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
        return {"status": f"unreadable: {type(error).__name__}: {str(error)[:120]}", "matched_keys": ""}
    if not isinstance(parsed, dict) or not str(parsed.get("openapi", "")).startswith("3"):
        return {"status": "readable", "matched_keys": "", "counts": "{}"}
    try:
        counts = CENSUS.census_document(parsed, root_path=Path(path))
    except Exception as error:
        return {"status": f"unreadable: {type(error).__name__}: {str(error)[:120]}", "matched_keys": ""}
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
        for line in handle:
            row = json.loads(line)
            taken[row["document"]] = row
    out = []
    for row in listing:
        found = taken.get(row["document"])
        if found is None or found.get("local") == "missing":
            out.append({"status": "unreadable: no local copy", "matched_keys": ""})
        elif found.get("sha256_ok") is False:
            out.append({"status": "unreadable: local bytes differ from the pinned SHA-256", "matched_keys": ""})
        elif "error" in found:
            out.append({"status": f"unreadable: {found['error'][:120]}", "matched_keys": ""})
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
    if args.census:
        results = _precomputed(args.census, listing, keys)
    else:
        jobs = [
            (str(locate(source, args.root, row, by_digest)), row["sha256"], row["document"], keys)
            for row in listing
        ]
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
    git blob where the pin has no SHA-256; any other is fetched through the
    acquirer's exact-commit raw route, whose calls land in this source's evidence
    directory, and kept only if it is the pinned blob. The result is `pins.tsv`.
    """
    source = "github-publisher-trees"
    github = _load("witness_search_github", REPO / "scripts" / "witness-search-github.py")
    acquirer = github.Acquirer(source_dir(source), cache=CACHE / source)
    by_sha: dict[str, Path] = {}
    by_blob: dict[str, Path] = {}
    for path in args.root.rglob("*"):
        if path.is_file() and path.suffix in (".json", ".yaml", ".yml"):
            data = path.read_bytes()
            by_sha.setdefault(hashlib.sha256(data).hexdigest(), path)
            by_blob.setdefault(git_blob(data), path)
    target = args.root / "fetched"
    target.mkdir(parents=True, exist_ok=True)
    shared = SURFACE / f"witness-search-{source}" / "documents.jsonl"
    resolved, fetched, missing = [], 0, 0
    seen: set[tuple[str, str, str]] = set()
    for pin in map(json.loads, shared.read_text(encoding="utf-8").splitlines()):
        # The shared pin lists a few documents twice over, word for word; a walk
        # reads each document once.
        identity = (pin["repository"], pin["path"], pin["commit"])
        if identity in seen:
            continue
        seen.add(identity)
        local = by_sha.get(pin.get("sha256", "")) or by_blob.get(pin["blob"])
        if local is None:
            url = f"{acquirer.raw_github_url}/{pin['repository']}/{pin['commit']}/{urllib.parse.quote(pin['path'])}"
            status, data = acquirer.raw_github_get(url, "*", f"{pin['repository']}:{pin['path']}")
            if status == 200 and git_blob(data) == pin["blob"]:
                local = target / (pin["blob"] + Path(pin["path"]).suffix)
                local.write_bytes(data)
                fetched += 1
        sha256 = hashlib.sha256(local.read_bytes()).hexdigest() if local else ""
        if pin.get("sha256") and sha256 and sha256 != pin["sha256"]:
            fail(f"{pin['path']}: the blob matches but the SHA-256 differs from the pin")
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


# --------------------------------------------------------------------- query


def phrasings(key: str, source: str) -> list[str]:
    with QUERIES.open(encoding="utf-8", newline="") as handle:
        rows = [r for r in csv.DictReader(handle, delimiter="\t") if r["key"] == key and r["source"] == source]
    found = [r["phrasing"] for r in rows]
    if len(found) < 2 or len(set(found)) != len(found):
        fail(f"{QUERIES.name} owes {key} two distinct phrasings for {source}")
    return found


def _quoted(url: str) -> str:
    """A contents URL with its path percent-encoded: result paths may hold a space."""
    parts = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit(parts._replace(path=urllib.parse.quote(urllib.parse.unquote(parts.path))))


def _fetch(read: Any, *args: Any) -> dict[str, Any]:
    """One result's acquisition, a failure to read it recorded rather than raised."""
    try:
        return read(*args)
    except (OSError, ValueError, http.client.HTTPException) as error:
        item = args[-1]
        return {"disposition": "acquisition-failure", "diagnostic": f"{type(error).__name__}: {error}",
                "repository": (item.get("repository") or {}).get("full_name")
                if isinstance(item.get("repository"), dict) else item.get("repository"),
                "path": item.get("path"), "commit": item.get("commit")}


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
        total = int(payload.get("total_count", 0))
        items = payload.get("items", [])[:FIRST_PAGE]
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
    acquirer = github.Acquirer(directory, cache=CACHE / source)
    new: list[dict[str, str]] = []
    index_path = CACHE / source / "candidate-documents.json"
    index: dict[str, str] = json.loads(index_path.read_text()) if index_path.is_file() else {}
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
                        count = declared(CENSUS.census_document(CENSUS.load_document(local)), selectors)
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


def _dedupe(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    seen, out = set(), []
    for row in rows:
        identity = (row["key"], row["kind"], row["subject"])
        if identity not in seen:
            seen.add(identity)
            out.append(row)
    return out


# --------------------------------------------------------------------- probe


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
            index_path = CACHE / source / "candidate-documents.json"
            index = json.loads(index_path.read_text()) if index_path.is_file() else {}
            if row["subject"] in index:
                out.append((row["subject"], CACHE / source / "documents" / index[row["subject"]]))
    return out


def probe(args: argparse.Namespace) -> int:
    e2e, crozier = REACH._instrumented_binaries(REPO)
    del e2e
    profdata, llvm_cov = REACH._llvm_tool("llvm-profdata"), REACH._llvm_tool("llvm-cov")
    universe = {f: {tuple(r) for r in v} for f, v in json.loads((REACH.DEFAULT_OUT / "universe.json").read_text()).items()}
    results = []
    for key in args.key:
        arms = unreached_sites(key)
        regions = {spec: (site.file, {r for r in universe.get(site.file, ()) if site.holds(r)})
                   for spec in arms for site in [REACH.resolve_site(spec)]}
        pending = declarers(args.source, key, args.root)
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
                return {"key": key, "candidate": candidate, "status": status, "reached": reached}
            result = run_one(candidate, path)
            seen[digest] = (result["status"], result["reached"])
            return result

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
                subprocess.run([profdata, "merge", "-sparse", *profiles, "-o", str(merged)], check=True)
                export = scratch_path / "export.json"
                with export.open("w", encoding="utf-8") as sink:
                    subprocess.run([llvm_cov, "export", "-format=text", f"-instr-profile={merged}", str(crozier),
                                    *sources], check=True, stdout=sink)
                tier = {"t": REACH.REPORT.load_tier(export, REPO)}
                hit = {f: {tuple(r) for r, n in c.items() if n > 0} for f, c in tier["t"].items()}
            reached = sorted(spec for spec, (file, found) in regions.items() if found & hit.get(file, set()))
            status = "generated" if run.returncode == 0 else f"exit {run.returncode}: {run.stderr.strip()[-160:]}"
            return {"key": key, "candidate": candidate, "status": status, "reached": reached}

        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            probed = list(pool.map(one, pending))
        file_probes(args.source, key, probed)
        results.extend(probed)
    reaching = sum(1 for r in results if r["reached"])
    print(f"golden-reach-search: {args.source}: probed {len(results)} declarer(s), {reaching} reach an unreached arm")
    return 0


def file_probes(source: str, key: str, probed: list[dict[str, Any]]) -> None:
    """One key's probe results into `probe.jsonl`, and its arm-reaching declarers as candidates."""
    path = source_dir(source) / "probe.jsonl"
    kept = []
    if path.is_file():
        kept = [row for row in map(json.loads, path.read_text(encoding="utf-8").splitlines()) if row["key"] != key]
    path.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in kept + probed), encoding="utf-8")
    census_of = {r["subject"]: r["result"] for r in read_records(source) if r["kind"] == "document" and r["key"] == key}
    candidates = [
        {"key": key, "kind": "candidate", "subject": r["candidate"], "result": census_of[r["candidate"]],
         "file": "probe.jsonl"}
        for r in probed if r["reached"]
    ]
    others = [r for r in read_records(source) if not (r["key"] == key and r["kind"] == "candidate")]
    write_records(source, set(), others + candidates)


# -------------------------------------------------------------------- screen


def screen(args: argparse.Namespace) -> int:
    """File one candidate's three screens, each with the evidence it rests on."""
    for outcome in (args.licence, args.ref, args.fern):
        if outcome != "passed" and not outcome.startswith("failed: "):
            fail(f"a screen reads `passed` or `failed: <reason>`, not {outcome!r}")
    rows = [
        {"key": args.key, "kind": "screen", "subject": f"{args.candidate} licence", "result": args.licence, "file": "screens.jsonl"},
        {"key": args.key, "kind": "screen", "subject": f"{args.candidate} ref", "result": args.ref, "file": "screens.jsonl"},
        {"key": args.key, "kind": "screen", "subject": f"{args.candidate} fern", "result": args.fern, "file": "screens.jsonl"},
    ]
    directory = source_dir(args.source)
    with (directory / "screens.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"key": args.key, "candidate": args.candidate, "licence": args.licence,
                                 "ref": args.ref, "fern": args.fern, "gap_keys": args.gap_keys,
                                 "evidence": args.evidence}, sort_keys=True) + "\n")
    others = [r for r in read_records(args.source)
              if not (r["key"] == args.key and r["kind"] == "screen" and r["subject"].startswith(args.candidate + " "))]
    write_records(args.source, set(), others + rows)
    return 0


# -------------------------------------------------------------------- render


def _cell(text: str) -> str:
    """A table cell's text, its pipes escaped so a regex phrasing stays one column."""
    return text.replace("|", "\\|")


def render(args: argparse.Namespace) -> int:
    """One arm search record per key, one Contract B line per declared source."""
    for key in args.key:
        lines = [
            f"# Arm search: `{key}`",
            "",
            "The unreached handling site(s) searched for: "
            + ", ".join(f"`{_cell(s)}`" for s in unreached_sites(key)) + ".",
            "Read with: " + ", ".join(f"`{s}`" for s in selectors_of(key)) + ".",
            "",
            "A walked or fetched document declaring the row is a `document` row of the",
            "source's `records.tsv`; one whose instrumented `crozier generate` executes",
            "an unreached site above is a `candidate`, and only a candidate owes the",
            "licence, ref and fern screens. The outcome is this search's own reading;",
            "final reconciliation decides whether the arm's search reads `exhausted`.",
            "",
            "### Witness search (exhaustive)",
            "",
            "| key | source | outcome | queries | walk | candidates | screens |",
            "|---|---|---|---|---|---|---|",
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
                f"| `{key}` | `{source}` | `{args.outcome}` | {queries} | {walks} | {candidates} | {_cell(screen_cell)} |"
            )
        path = EVIDENCE / "searches" / f"{key}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)
    w = sub.add_parser("walk")
    w.add_argument("--source", required=True)
    w.add_argument("--root", type=Path, required=True, help="local copy of the pinned documents")
    w.add_argument("--key", action="append", required=True)
    w.add_argument("--jobs", type=int, default=8)
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
    p.add_argument("--jobs", type=int, default=8)
    p.add_argument("--timeout", type=int, default=300)
    s = sub.add_parser("screen")
    s.add_argument("--source", required=True)
    s.add_argument("--key", required=True)
    s.add_argument("--candidate", required=True)
    s.add_argument("--licence", required=True)
    s.add_argument("--ref", required=True)
    s.add_argument("--fern", required=True)
    s.add_argument("--gap-keys", default="")
    s.add_argument("--evidence", default="")
    r = sub.add_parser("render")
    r.add_argument("--key", action="append", required=True)
    r.add_argument("--outcome", required=True, choices=("exhausted", "search-incomplete", "witness-found"))
    args = parser.parse_args(argv)
    return {"walk": walk, "fetch-pins": fetch_pins, "query": query, "probe": probe, "screen": screen, "render": render}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
