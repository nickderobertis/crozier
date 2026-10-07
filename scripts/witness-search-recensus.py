#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["ruamel.yaml==0.19.1"]
# ///
# llmlint: ignore-file[new_code_lands_in_a_project] crozier has no Nx project; this maintenance command belongs in scripts/ beside the acquisition ledgers it appends to.
"""Decide the witness-search candidates the first acquisition left undecided.

Two stages, each appending to a query or walk source's own ledger
(`candidates.jsonl`, or `documents.jsonl` for the publisher trees) so that
`witness-search-github-index.py` re-derives `records.tsv` from it:

`full-yaml` reads every candidate whose latest ledger row is a `parse-failure`
of the census's standard-library loader again, from its cached copy (verified
against the digest the ledger pins, and reacquired at its recorded commit when no
cache holds it), with the full YAML 1.2 parser the
golden-reach arm search pins, and where its strict construction refuses one (a
duplicate key, an application tag) with that parser relaxed on those two rules
alone. What either reading reads is censused by the census's own selector engine
and recorded with the loader named; what both refuse is recorded
`census-refused` with the parser, its version, each error and the document's
digest. A publisher-tree document that reading read before a requested key
joined `keys.json` carries no count for it, so it is read again the same way.

`reacquire-head` requests each candidate whose pinned blob GitHub answered 404
again at the repository's current revision: the repository and its default
branch's head commit through the guarded REST `core` bucket, the file at that
commit through the paced raw lane. A read is censused as any acquisition is, at
that commit, and supersedes the 404; a refusal is recorded with its status and
time and leaves the candidate open.

`reacquire-namesake` seeks each candidate `reacquire-head` left refused in the
repositories GitHub's repository search names exactly as the candidate's own is
named, a fork's parent and siblings among them: each one's history of the path,
through the guarded `core` bucket, and each commit's file through the paced raw
lane, kept only where it hashes to the blob GitHub's search named. A read is
censused as any acquisition is and supersedes the refusal, naming the repository
that served it; otherwise the refusal is extended with what was searched.

Exit 0 means the stage finished, 1 means evidence or a cache needs repair, and 2
means the arguments are invalid.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import hashlib
import importlib.util
import json
import multiprocessing
import os
import signal
import sys
import urllib.parse
from pathlib import Path
from types import ModuleType
from typing import Any

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
REFUSED = "census-refused"
# A document the full parser and the census walk together take longer than this
# over is recorded refused, with the bound, rather than holding the stage open.
DEFAULT_TIMEOUT_S = 600


def _load(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


REACH = _load("golden_reach_search", REPO / "scripts" / "golden-reach-search.py")
CENSUS = REACH.CENSUS
GITHUB = _load("witness_search_github", REPO / "scripts" / "witness-search-github.py")
INDEX = GITHUB.INDEX


def fail(message: str) -> None:
    raise SystemExit(f"witness-search-recensus: {message}")


def ledger_name(source: str) -> str:
    return "documents.jsonl" if source == "github-publisher-trees" else "candidates.jsonl"


def identity(source: str, row: dict[str, Any]) -> tuple[str, ...]:
    """What a later ledger row replaces an earlier one by, as the index reads it."""
    name = INDEX.candidate_name(row)
    revision = INDEX.candidate_revision(row)
    if source == "github-publisher-trees":
        return (name, revision)
    return (row["key"], name, revision)


def latest_rows(evidence: Path, source: str) -> list[tuple[int, dict[str, Any]]]:
    latest: dict[tuple[str, ...], tuple[int, dict[str, Any]]] = {}
    for number, row in INDEX.jsonl(evidence / ledger_name(source)):
        latest[identity(source, row)] = (number, row)
        if row.get("supersedes"):
            latest.pop(identity(source, INDEX.superseded_row(row)), None)
    return sorted(latest.values(), key=lambda item: item[0])


def continuation_rows(evidence: Path, source: str) -> tuple[list[tuple[int, dict[str, Any]]], int]:
    rows = latest_rows(evidence, source)
    eligible = [item for item in rows if not INDEX.opaque_identity(item[1]["path"])]
    return eligible, len(rows) - len(eligible)


def opaque_summary(count: int) -> str:
    version = INDEX.OPAQUE_PREFIX.split(":")[1]
    return f"; {count} opaque {version} record(s) screened by repository rule" if count else ""


def status_of(row: dict[str, Any]) -> str:
    return row.get("disposition") or row.get("status") or ""


def find_copy(digest: str, roots: list[Path]) -> Path | None:
    for root in roots:
        for path in sorted((root / "documents").glob(digest + ".*")) if (root / "documents").is_dir() else ():
            return path
    return None


def one_line(text: str) -> str:
    return " ".join(text.split())


LENIENT_LOADER = f"{REACH.YAML_LOADER}, duplicate keys last-wins, unrecognised tags read untagged"


def lenient_stream(data: bytes) -> list[Any]:
    """The pinned parser's reading with two construction rules relaxed, and only those.

    A duplicate mapping key keeps its last value, and a node under a tag the safe
    constructor does not recognise (`!merge-objects`, `!!python/object/...`) is
    read as the untagged scalar, sequence or mapping it is written as. Syntax is
    not relaxed: a document this refuses is not YAML.
    """
    ruamel_yaml = REACH._ruamel_yaml()
    safe = ruamel_yaml.constructor.SafeConstructor

    class Lenient(safe):
        pass

    def untagged(constructor: Any, suffix: str, node: Any) -> Any:
        if isinstance(node, ruamel_yaml.nodes.MappingNode):
            return constructor.construct_mapping(node, deep=True)
        if isinstance(node, ruamel_yaml.nodes.SequenceNode):
            return constructor.construct_sequence(node, deep=True)
        return constructor.construct_scalar(node)

    Lenient.add_constructor("tag:yaml.org,2002:timestamp", safe.construct_yaml_str)
    Lenient.add_multi_constructor("", untagged)
    reader = ruamel_yaml.YAML(typ="safe", pure=True)
    reader.Constructor = Lenient
    reader.allow_duplicate_keys = True
    return list(reader.load_all(data))


def _alarm(signum: int, frame: Any) -> None:
    raise TimeoutError("census bound reached")


def read_document(path: str, timeout: int) -> dict[str, Any]:
    """One cached document through the full parser and the census: its verdict.

    `{"verdict": "counts", "counts": {...}}` for an OpenAPI 3 description,
    `{"verdict": "not-openapi-3", "reason": ...}` for a stream the parser reads
    but that holds no one OpenAPI 3 description, and `{"verdict": "refused",
    "reason": ...}` where the parser or the census walk refuses it.
    """
    local = Path(path)
    data = local.read_bytes()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(timeout)
    try:
        loader = REACH.YAML_LOADER
        try:
            # YAML 1.2 is a superset of JSON, so one parser reads either spelling.
            stream = REACH.yaml_stream(data)
        except TimeoutError:
            return {"verdict": "refused", "reason": f"{loader}: parse exceeded {timeout} s"}
        except Exception as error:  # ruamel's parse errors share no base class it exports
            strict = f"{loader}: {one_line(f'{type(error).__name__}: {error}')}"
            loader = LENIENT_LOADER
            try:
                stream = lenient_stream(data)
            except TimeoutError:
                return {"verdict": "refused", "reason": f"{strict}; {loader}: parse exceeded {timeout} s"}
            except Exception as lenient:  # a syntax refusal: no reading relaxes it
                return {"verdict": "refused",
                        "reason": f"{strict}; {loader}: {one_line(f'{type(lenient).__name__}: {lenient}')}"}
        described = [document for document in stream if REACH._names_a_version(document)]
        if len(described) != 1:
            return {"verdict": "not-openapi-3", "loader": loader,
                    "reason": f"a stream of {len(stream)} YAML document(s), {len(described)} naming an "
                              "`openapi` or `swagger` version"}
        parsed = described[0]
        if not GITHUB.OPENAPI_VERSION.fullmatch(str(parsed.get("openapi", ""))):
            return {"verdict": "not-openapi-3", "loader": loader,
                    "reason": f"names `openapi` {parsed.get('openapi')!r} / `swagger` {parsed.get('swagger')!r}"}
        try:
            counts = CENSUS.census_document(parsed, root_path=local)
        except TimeoutError:
            return {"verdict": "refused", "reason": f"census walk over the {loader} reading exceeded {timeout} s"}
        except Exception as error:  # the census's own refusal, whatever its type
            return {"verdict": "refused", "reason": f"census walk over the {loader} reading: "
                                                    f"{one_line(f'{type(error).__name__}: {error}')}"}
        return {"verdict": "counts", "counts": counts, "loader": loader}
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)


def verdict_record(source: str, row: dict[str, Any], verdict: dict[str, Any], digest: str,
                   keys: dict[str, dict[str, str]]) -> dict[str, Any]:
    kept = ("source", "key", "selector", "repository", "path", "commit", "blob", "url",
            "acquisition_route", "raw_url", "document", "shared_with_key", "supersedes",
            "reacquired_at_head", "github_refusal", "served_by", "namesakes_searched")
    record: dict[str, Any] = {field: row[field] for field in kept if field in row}
    # A reading repeated for a key added since names the parse failure the first one decided.
    record.update(sha256=digest, loader=verdict.get("loader", REACH.YAML_LOADER),
                  recensus_of=row.get("recensus_of") or status_of(row))
    field = "status" if source == "github-publisher-trees" else "disposition"
    if verdict["verdict"] == "refused":
        record[field] = REFUSED
        record["diagnostic"] = f"{verdict['reason']}; sha256 {digest}"
    elif verdict["verdict"] == "not-openapi-3":
        record[field] = "excluded-non-openapi-3"
        record["diagnostic"] = verdict["reason"]
        if source != "github-publisher-trees":
            record["selector_count"] = 0
    elif source == "github-publisher-trees":
        record[field] = "readable"
        record["selector_counts"] = {key: verdict["counts"].get(value["selector"], 0)
                                     for key, value in sorted(keys.items())}
    else:
        count = verdict["counts"].get(keys[row["key"]]["selector"], 0)
        record[field] = "declares" if count else "does-not-declare"
        record["selector_count"] = count
    return record


def uncounted(source: str, row: dict[str, Any], wanted: set[str]) -> bool:
    """A publisher-tree document the full parser read before a wanted key joined `keys.json`.

    Its reading counted the keys of its day; a key added since has no count on
    it, and the census's stdlib loader cannot supply one, so the full parser
    reads the same cached copy again for every key.
    """
    return (source == "github-publisher-trees" and status_of(row) == "readable"
            and row.get("recensus_of") == "parse-failure"
            and bool(wanted - set(row.get("selector_counts") or {})))


def service_acquirer(evidence: Path, cache: Path) -> Any:
    """An acquirer honouring the acquisition CLI's service overrides, so an offline test drives it locally."""
    return GITHUB.Acquirer(
        evidence, cache=cache,
        sourcegraph_url=GITHUB.checked_service_url(
            os.environ.get("CROZIER_SOURCEGRAPH_URL", GITHUB.SOURCEGRAPH_URL), "CROZIER_SOURCEGRAPH_URL",
            "sourcegraph.com"),
        raw_github_url=GITHUB.checked_service_url(
            os.environ.get("CROZIER_RAW_GITHUB_URL", GITHUB.RAW_GITHUB_URL), "CROZIER_RAW_GITHUB_URL",
            "raw.githubusercontent.com"))


def full_yaml(args: argparse.Namespace) -> int:
    evidence = args.evidence_root / f"witness-search-{args.source}"
    keys = INDEX.read_keys(evidence)
    wanted = set(args.key)
    pending: list[tuple[dict[str, Any], str]] = []
    recounts = 0
    rows, opaque_count = continuation_rows(evidence, args.source)
    for _, row in rows:
        if uncounted(args.source, row, wanted or set(keys)):
            recounts += 1
        elif status_of(row) != "parse-failure":
            continue
        if wanted and args.source != "github-publisher-trees" and row["key"] not in wanted:
            continue
        pending.append((row, row["sha256"]))
    roots = args.cache or [GITHUB.DEFAULT_CACHE]
    acquirer = None
    copies: dict[str, Path] = {}
    for row, digest in pending:
        if digest in copies:
            continue
        local = find_copy(digest, roots)
        if local is None:
            # No cache holds it: reacquire it at its recorded commit into the first.
            acquirer = acquirer or service_acquirer(evidence, roots[0])
            try:
                acquirer.resolve(row, row.get("key", "publisher-trees"))
            except GITHUB.DigestRefused as error:
                fail(f"refused: {error}")
            except (GITHUB.EvidenceError, GITHUB.SearchStopped, GITHUB.SecondaryLimit, OSError) as error:
                fail(f"no cached copy of sha256 {digest} under {[str(r) for r in roots]}, and it cannot be "
                     f"reacquired: {error}; pass the cache it was acquired into with --cache")
            local = find_copy(digest, roots)
            if local is None:
                fail(f"no cached copy of sha256 {digest} under {[str(r) for r in roots]}, and its recorded "
                     "source no longer serves it; pass the cache it was acquired into with --cache")
        if hashlib.sha256(local.read_bytes()).hexdigest() != digest:
            fail(f"{local} does not hash to the pinned sha256 {digest}; re-acquire it at its commit")
        copies[digest] = local
    verdicts: dict[str, dict[str, Any]] = {}
    context = multiprocessing.get_context("fork" if hasattr(signal, "SIGALRM") else "spawn")
    with concurrent.futures.ProcessPoolExecutor(args.jobs, mp_context=context) as pool:
        futures = {pool.submit(read_document, str(path), args.timeout): digest
                   for digest, path in sorted(copies.items())}
        for future in concurrent.futures.as_completed(futures):
            verdicts[futures[future]] = future.result()
    tally: dict[str, int] = {}
    for row, digest in pending:
        record = verdict_record(args.source, row, verdicts[digest], digest, keys)
        stamped = {"at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds"),
                   **record}
        INDEX.append_ledger(evidence / ledger_name(args.source), json.dumps(stamped, sort_keys=True) + "\n")
        verdict = status_of(record)
        tally[verdict] = tally.get(verdict, 0) + 1
    counted_since = f" and {recounts} full-parser reading(s) missing a key's count" if recounts else ""
    print(f"witness-search-recensus: {args.source}: {len(pending) - recounts} parse-failure row(s)"
          f"{counted_since} over {len(copies)} document(s) read again: "
          + ", ".join(f"{count} {verdict}" for verdict, count in sorted(tally.items())) + opaque_summary(opaque_count))
    return 0


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def from_history(acquirer: Any, row: dict[str, Any], base: dict[str, Any], head: str,
                 refusal: str) -> tuple[dict[str, Any] | None, str]:
    """The file at the commit that pins the candidate's own blob, found in the head's history of its path.

    Where the head no longer holds the file but the repository still does in its
    history, each commit touching the path is read, newest first, until one
    serves the blob GitHub's search named: that commit's record, or `None` and
    what the history showed, to be added to the refusal.
    """
    status, commits, _ = acquirer.github_json(
        "core", f"/repos/{row['repository']}/commits?path={urllib.parse.quote(row['path'])}&sha={head}&per_page=100")
    at = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    if status != 200 or not isinstance(commits, list):
        return None, f"the path's history at {head} answered HTTP {status} at {at}"
    for commit in commits:
        sha = commit.get("sha") if isinstance(commit, dict) else None
        if not isinstance(sha, str):
            continue
        raw_url = (acquirer.raw_github_url + "/" + urllib.parse.quote(row["repository"], safe="/") + "/" + sha
                   + "/" + urllib.parse.quote(row["path"], safe="/"))
        got, data = acquirer.raw_github_get(raw_url, row["key"], f"{row['repository']}/{row['path']}@{sha}")
        if got == 200 and git_blob(data) == row.get("blob"):
            return acquirer.classify_and_record(
                {**base, "commit": sha, "blob": row["blob"], "raw_url": raw_url,
                 "acquisition_route": GITHUB.ROUTE_PINNED_RAW_GITHUB, "supersedes": row["commit"],
                 "reacquired_at_head": True, "github_refusal": refusal}, data), ""
    return None, (f"the path's history at {head} lists {len(commits)} commit(s), none serving blob "
                  f"{row.get('blob')}, at {at}")


def mirrored(acquirer: Any, row: dict[str, Any], base: dict[str, Any], refusal: str,
             status: int) -> dict[str, Any]:
    """The pinned blob from Sourcegraph's mirror at the pinned commit, where GitHub no longer serves it.

    Read on the guarded Sourcegraph lane and kept only if its git blob hash is
    the one GitHub's search named, so the bytes are the candidate's own. What
    the mirror serves otherwise joins GitHub's refusal, and its `status`, on an
    unwritten failure record that keeps the candidate at the commit it was
    pinned at.
    """
    url = acquirer.sourcegraph_raw_url(f"github.com/{row['repository']}", row["path"], row["commit"])
    served_status, data = acquirer.sourcegraph_get(url, row["key"], f"{row['repository']}/{row['path']}@{row['commit']}")
    at = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    if served_status == 200 and git_blob(data) == row.get("blob"):
        return acquirer.classify_and_record(
            {**base, "commit": row["commit"], "blob": row["blob"], "url": url,
             "acquisition_route": GITHUB.ROUTE_SOURCEGRAPH_MIRROR, "reacquired_at_head": True,
             "github_refusal": refusal}, data)
    served = f"HTTP {served_status}" if served_status != 200 else f"a blob hashing to {git_blob(data)}, not {row.get('blob')}"
    return {**base, "commit": row["commit"], "blob": row.get("blob"), "disposition": "acquisition-failure",
            "status": status, "reacquired_at_head": True,
            "diagnostic": f"{refusal}; Sourcegraph's mirror at {row['commit']} served {served} at {at}"}


def reacquire_head(args: argparse.Namespace) -> int:
    source = "github-code-search"
    evidence = args.evidence_root / f"witness-search-{source}"
    keys = INDEX.read_keys(evidence)
    wanted = set(args.key)
    rows, opaque_count = continuation_rows(evidence, source)
    pending = [row for _, row in rows
               if status_of(row) == "acquisition-failure" and row.get("status") == 404
               and (args.again or not row.get("reacquired_at_head"))
               and (not wanted or row["key"] in wanted)]
    # A row an earlier head request superseded is re-requested at the commit it pinned.
    pending = [{**row, "commit": row.get("supersedes") or row["commit"]} for row in pending]
    acquirer = service_acquirer(evidence, args.cache_dir)
    heads: dict[str, tuple[int, str, str]] = {}
    tally: dict[str, int] = {}
    for row in pending:
        repository = row["repository"]
        if repository not in heads:
            status, payload, _ = acquirer.github_json("core", f"/repos/{repository}")
            at = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
            if status != 200 or not isinstance(payload, dict) or not payload.get("default_branch"):
                heads[repository] = (status, "", f"GET /repos/{repository} answered HTTP {status} at {at}")
            else:
                branch = payload["default_branch"]
                status, commit, _ = acquirer.github_json(
                    "core", f"/repos/{repository}/commits/{urllib.parse.quote(branch, safe='')}")
                at = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
                sha = commit.get("sha") if isinstance(commit, dict) else None
                heads[repository] = (
                    (status, sha, f"head of {branch}")
                    if status == 200 and isinstance(sha, str)
                    else (status, "", f"GET /repos/{repository}/commits/{branch} answered HTTP {status} at {at}"))
        status, head, note = heads[repository]
        base = {field: row[field] for field in ("source", "key", "selector", "repository", "path")}
        if not head:
            record = mirrored(acquirer, row, base, note, status)
            if record.get("disposition") == "acquisition-failure":
                acquirer.write("candidates.jsonl", record)
        else:
            raw_url = (acquirer.raw_github_url + "/" + urllib.parse.quote(repository, safe="/") + "/" + head
                       + "/" + urllib.parse.quote(row["path"], safe="/"))
            got, data = acquirer.raw_github_get(raw_url, row["key"], f"{repository}/{row['path']}@{head}")
            at = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
            ident = {**base, "commit": head, "raw_url": raw_url, "acquisition_route": GITHUB.ROUTE_PINNED_RAW_GITHUB,
                     "supersedes": row["commit"], "reacquired_at_head": True}
            if got != 200:
                refusal = f"{row['path']} at {head} ({note}) answered HTTP {got} at {at}"
                record, history = from_history(acquirer, row, base, head, refusal)
                if record is None:
                    # Not found at head: the candidate keeps the identity it was pinned at.
                    record = mirrored(acquirer, row, base, f"{refusal}; {history}", got)
                    if record.get("disposition") == "acquisition-failure":
                        acquirer.write("candidates.jsonl", record)
            else:
                ident["blob"] = git_blob(data)
                record = acquirer.classify_and_record(ident, data)
        if status_of(record) == "parse-failure":
            # A document the census's own loader refuses is read at once as `full-yaml` reads one.
            local = acquirer.cache / "documents" / record["document"]
            record = verdict_record(source, record, read_document(str(local), DEFAULT_TIMEOUT_S),
                                    record["sha256"], keys)
            acquirer.write("candidates.jsonl", record)
        verdict = status_of(record)
        tally[verdict] = tally.get(verdict, 0) + 1
    print(f"witness-search-recensus: {len(pending)} 404 candidate(s) requested at head: "
          + ", ".join(f"{count} {verdict}" for verdict, count in sorted(tally.items())) + opaque_summary(opaque_count))
    return 0


def namesakes(acquirer: Any, repository: str) -> tuple[list[str], str]:
    """Every other repository GitHub's repository search names exactly as `repository` is named.

    A fork keeps its parent's name, so these are where a deleted or rewritten
    fork's unchanged file can still be read: its parent and its siblings. The
    search is one guarded `search` call; what it answers is part of the refusal
    when no namesake serves the blob.
    """
    name = repository.split("/", 1)[1]
    status, payload, _ = acquirer.github_json(
        "search", f"/search/repositories?q={urllib.parse.quote(f'{name} in:name')}&per_page=100")
    at = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    if status != 200 or not isinstance(payload, dict) or not isinstance(payload.get("items"), list):
        return [], f"the repository search for `{name}` answered HTTP {status} at {at}"
    found = [item["full_name"] for item in payload["items"]
             if isinstance(item, dict) and isinstance(item.get("full_name"), str)
             and item["full_name"].split("/", 1)[1].lower() == name.lower()
             and item["full_name"].lower() != repository.lower()]
    return found, f"the repository search for `{name}` names {len(found)} namesake(s) ({', '.join(found) or 'none'}) at {at}"


def reacquire_namesake(args: argparse.Namespace) -> int:
    """Read each candidate `reacquire-head` left refused from a namesake repository holding its blob.

    The blob GitHub's search named identifies the bytes, so a namesake's commit
    serving a file that hashes to it serves the candidate's own document. That
    commit's record keeps the candidate's name, names the repository serving it
    in `served_by`, and supersedes the refusal; a candidate no namesake serves
    keeps its refusal, extended with what the search and each history showed.
    """
    source = "github-code-search"
    evidence = args.evidence_root / f"witness-search-{source}"
    keys = INDEX.read_keys(evidence)
    wanted = set(args.key)
    rows, opaque_count = continuation_rows(evidence, source)
    pending = [row for _, row in rows
               if status_of(row) == "acquisition-failure" and row.get("status") == 404
               and row.get("reacquired_at_head")
               and (args.again or not row.get("namesakes_searched"))
               and (not wanted or row["key"] in wanted)]
    acquirer = GITHUB.Acquirer(
        evidence, cache=args.cache_dir,
        raw_github_url=GITHUB.checked_service_url(
            os.environ.get("CROZIER_RAW_GITHUB_URL", GITHUB.RAW_GITHUB_URL), "CROZIER_RAW_GITHUB_URL",
            "raw.githubusercontent.com"))
    searched: dict[str, tuple[list[str], str]] = {}
    tally: dict[str, int] = {}
    for row in pending:
        if row["repository"] not in searched:
            searched[row["repository"]] = namesakes(acquirer, row["repository"])
        found, note = searched[row["repository"]]
        base = {field: row[field] for field in ("source", "key", "selector", "repository", "path")}
        record: dict[str, Any] | None = None
        histories = []
        for namesake in found:
            status, commits, _ = acquirer.github_json(
                "core", f"/repos/{namesake}/commits?path={urllib.parse.quote(row['path'])}&per_page=100")
            at = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
            if status != 200 or not isinstance(commits, list):
                histories.append(f"{namesake}'s history of the path answered HTTP {status} at {at}")
                continue
            for commit in commits:
                sha = commit.get("sha") if isinstance(commit, dict) else None
                if not isinstance(sha, str):
                    continue
                raw_url = (acquirer.raw_github_url + "/" + urllib.parse.quote(namesake, safe="/") + "/" + sha
                           + "/" + urllib.parse.quote(row["path"], safe="/"))
                got, data = acquirer.raw_github_get(raw_url, row["key"], f"{namesake}/{row['path']}@{sha}")
                if got == 200 and git_blob(data) == row.get("blob"):
                    record = acquirer.classify_and_record(
                        {**base, "commit": sha, "blob": row["blob"], "raw_url": raw_url,
                         "acquisition_route": GITHUB.ROUTE_PINNED_RAW_GITHUB, "served_by": namesake,
                         "supersedes": row["commit"], "reacquired_at_head": True, "namesakes_searched": True,
                         "github_refusal": row.get("diagnostic")}, data)
                    break
            if record is not None:
                break
            histories.append(f"{namesake}'s history of the path lists {len(commits)} commit(s), none serving "
                             f"blob {row.get('blob')}, at {at}")
        if record is None:
            record = {**{field: row[field] for field in row if field != "at"}, "namesakes_searched": True,
                      "diagnostic": "; ".join([str(row.get("diagnostic")), note, *histories])}
            acquirer.write("candidates.jsonl", record)
        elif status_of(record) == "parse-failure":
            local = acquirer.cache / "documents" / record["document"]
            record = verdict_record(source, record, read_document(str(local), DEFAULT_TIMEOUT_S),
                                    record["sha256"], keys)
            acquirer.write("candidates.jsonl", record)
        verdict = status_of(record)
        tally[verdict] = tally.get(verdict, 0) + 1
    print(f"witness-search-recensus: {len(pending)} refused candidate(s) sought in namesake repositories: "
          + ", ".join(f"{count} {verdict}" for verdict, count in sorted(tally.items())) + opaque_summary(opaque_count))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--evidence-root", type=Path, default=REPO / "docs/openapi-surface")
    stages = parser.add_subparsers(dest="stage", required=True)
    full = stages.add_parser("full-yaml", help="census each parse failure again through the full YAML parser")
    full.add_argument("--source", choices=INDEX.SOURCES, required=True)
    full.add_argument("--cache", type=Path, action="append",
                      help="an acquisition cache holding documents/<sha256>.<suffix>; repeatable; defaults to "
                           f"the gitignored {GITHUB.DEFAULT_CACHE.relative_to(REPO)}, and a document no cache "
                           "holds is reacquired into the first at its recorded commit")
    full.add_argument("--key", action="append", default=[])
    full.add_argument("--jobs", type=int, default=4)
    full.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_S)
    head = stages.add_parser("reacquire-head", help="request each pinned-blob 404 at the repository's head")
    head.add_argument("--cache-dir", type=Path, required=True)
    head.add_argument("--key", action="append", default=[])
    head.add_argument("--again", action="store_true", help="request candidates an earlier run requested too")
    namesake = stages.add_parser("reacquire-namesake",
                                 help="seek each candidate refused at head in the repositories named as its own is")
    namesake.add_argument("--cache-dir", type=Path, required=True)
    namesake.add_argument("--key", action="append", default=[])
    namesake.add_argument("--again", action="store_true", help="seek candidates an earlier run sought too")
    args = parser.parse_args()
    source = args.source if args.stage == "full-yaml" else "github-code-search"
    unknown = set(args.key) - set(INDEX.read_keys(args.evidence_root / f"witness-search-{source}"))
    if unknown:
        parser.error(f"--key {sorted(unknown)} names no key of witness-search-{source}/keys.json; check the spelling")
    if args.stage == "full-yaml":
        if args.jobs < 1 or args.timeout < 1:
            parser.error("--jobs and --timeout must be positive")
        return full_yaml(args)
    if args.stage == "reacquire-namesake":
        return reacquire_namesake(args)
    return reacquire_head(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError) as error:
        print(f"witness-search-recensus: {error}; inspect the ledger and cache named and rerun",
              file=sys.stderr)
        raise SystemExit(1) from error
