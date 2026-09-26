#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier has no Nx project; this evidence index is a maintenance script beside its acquisition command in scripts/.
"""Reconcile acquired search results into per-source and consolidated candidate rows.

Exit 0 means the index is current or was regenerated; exit 1 means evidence or
committed output needs repair. Invalid arguments exit 2.
"""

from __future__ import annotations

import argparse
import csv
import functools
import io
import json
import re
import sys
from pathlib import Path
from typing import Any

SOURCES = ("github-code-search", "github-publisher-trees", "sourcegraph")
RAW_DECLARING = frozenset({"declares", "readable"})
RAW_OUTSTANDING = frozenset({
    "acquisition-failure", "parse-failure", "acquisition-outstanding", "selector-unavailable",
})
RAW_ZERO = frozenset({"does-not-declare", "excluded-non-openapi-3"})
RAW_STATUSES = RAW_DECLARING | RAW_OUTSTANDING | RAW_ZERO
FIELDS = (
    "source",
    "key",
    "candidate",
    "revision",
    "digest",
    "census",
    "licence_screen",
    "revision_screen",
    "fern_screen",
    "disposition",
    "evidence",
)
CENTRAL_FIELDS = (*FIELDS[:-1], "record")
DIAGNOSTIC_LIMIT = 2000
DISPOSITIONS = ("witness-found", "rejected", "outstanding", "not-owed")
# Why an issued query is still short when its ledger names no index limit or
# refusal: a size window never issued, pages never requested, or pages GitHub
# served empty before its reported count. The first two stopped on this search's
# own budget, so their reason also names why acquisition stopped.
UNISSUED_WINDOW = "unissued-window"
UNREAD_PAGES = "unread-pages"
SHORT_SERVED = "short-served"
UNREAD = (UNISSUED_WINDOW, UNREAD_PAGES)
# A screened candidate can also be settled against the corpus itself: a copy
# whose bytes equal a registered row's source document, named with the digest
# that proves it, or one left for a later registration node to register.
PENDING_REGISTRATION = "pending-registration"
BYTE_IDENTICAL = re.compile(r"byte-identical to CORPUS row \d+, sha256 [0-9a-f]{64}")


def known_disposition(disposition: str) -> bool:
    return (
        disposition in DISPOSITIONS
        or disposition == PENDING_REGISTRATION
        or BYTE_IDENTICAL.fullmatch(disposition) is not None
    )
# GitHub refuses a pushed blob over 100 MB and warns over 50 MB. A ledger that
# outgrows SHARD_BYTES keeps its first line-aligned part at its own path and
# continues in numbered siblings: candidates.tsv, candidates.001.tsv, ...
SHARD_BYTES = 45_000_000


def ledger_parts(path: Path) -> list[Path]:
    """Every part of one ledger in order, starting with its own path."""
    parts = [path]
    while (part := path.with_name(f"{path.stem}.{len(parts):03d}{path.suffix}")).is_file():
        parts.append(part)
    return parts


def read_ledger(path: Path) -> str:
    return "".join(part.read_text(encoding="utf-8") for part in ledger_parts(path))


def write_ledger(path: Path, text: str, limit: int | None = None) -> None:
    limit = SHARD_BYTES if limit is None else limit
    chunks: list[list[str]] = []
    size = limit
    for line in text.splitlines(keepends=True):
        encoded = len(line.encode("utf-8"))
        if size + encoded > limit:
            chunks.append([])
            size = 0
        chunks[-1].append(line)
        size += encoded
    stale = ledger_parts(path)[max(len(chunks), 1):]
    for number, chunk in enumerate(chunks or [[]]):
        part = path if number == 0 else path.with_name(f"{path.stem}.{number:03d}{path.suffix}")
        part.write_text("".join(chunk), encoding="utf-8")
    for part in stale:
        part.unlink()


def append_ledger(path: Path, line: str, limit: int | None = None) -> None:
    limit = SHARD_BYTES if limit is None else limit
    parts = ledger_parts(path)
    target = parts[-1]
    encoded = len(line.encode("utf-8"))
    if target.is_file() and 0 < target.stat().st_size and target.stat().st_size + encoded > limit:
        target = path.with_name(f"{path.stem}.{len(parts):03d}{path.suffix}")
    with target.open("a", encoding="utf-8") as output:
        output.write(line)


LEDGER_REQUIRED_FIELDS = {
    "queries.jsonl": ("source", "key", "query", "outcome"),
    "candidates.jsonl": ("source", "key", "repository", "path", "disposition"),
    "documents.jsonl": ("source", "repository", "path"),
    "screens.jsonl": ("source", "repository", "path"),
}


def jsonl(path: Path) -> list[tuple[int, dict[str, Any]]]:
    if not path.is_file():
        return []
    rows = []
    for number, line in enumerate(read_ledger(path).splitlines(), 1):
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"{path}:{number}: {error}") from error
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{number}: expected a JSON object")
        required = LEDGER_REQUIRED_FIELDS.get(path.name, ())
        for field in required:
            if not isinstance(row.get(field), str) or not row[field]:
                raise ValueError(f"{path}:{number}: missing or invalid {field}")
        if path.name == "screens.jsonl":
            for field in ("license", "ref", "fern", "disposition"):
                if not isinstance(row.get(field), str) or not row[field]:
                    raise ValueError(f"{path}:{number}: missing or invalid {field}")
            keys = row.get("keys") or [row.get("key")]
            if not isinstance(keys, list) or any(
                not isinstance(key, str) or not key for key in keys
            ):
                raise ValueError(f"{path}:{number}: missing or invalid keys")
        if path.name == "documents.jsonl" and "selector_counts" in row:
            counts = row["selector_counts"]
            if not isinstance(counts, dict) or any(
                not isinstance(key, str) or not isinstance(value, int)
                for key, value in counts.items()
            ):
                raise ValueError(f"{path}:{number}: invalid selector_counts")
        if path.name == "trees.jsonl" and "paths" in row:
            paths = row["paths"]
            if not isinstance(row.get("repository"), str) or not isinstance(row.get("commit"), str) or not isinstance(paths, list) or any(
                not isinstance(item, dict)
                or not isinstance(item.get("path"), str)
                or not isinstance(item.get("blob"), str)
                for item in paths
            ):
                raise ValueError(f"{path}:{number}: invalid publisher tree paths")
        if path.name == "queries.jsonl" and row["outcome"] == "partitioned":
            windows = row.get("windows")
            if not isinstance(windows, list) or not windows or any(
                not isinstance(window, dict) or not isinstance(window.get("query"), str)
                for window in windows
            ):
                raise ValueError(f"{path}:{number}: partitioned query lacks its size windows")
            if not isinstance(row.get("reported"), int) or isinstance(row.get("reported"), bool):
                raise ValueError(f"{path}:{number}: partitioned query lacks its reported count")
        limit_fields = (
            load_search().INDEX_LIMIT_FIELDS.get(row["outcome"], ())
            if path.name == "queries.jsonl" else ()
        )
        for field in limit_fields:
            if not isinstance(row.get(field), int) or isinstance(row.get(field), bool):
                raise ValueError(f"{path}:{number}: {row['outcome']} lacks an integer {field}")
        if path.name == "queries.jsonl" and row["outcome"] == "answered":
            for field in ("result_count", "retrieved_total", "page", "page_count"):
                if field in row and (
                    not isinstance(row[field], int) or isinstance(row[field], bool)
                ):
                    raise ValueError(f"{path}:{number}: {field} is not an integer")
            results = row.get("results")
            if not isinstance(results, list) or any(
                not isinstance(item, dict)
                or not isinstance(item.get("repository"), str)
                or not isinstance(item.get("path"), str)
                for item in results
            ):
                raise ValueError(f"{path}:{number}: invalid answered query results")
        if path.name == "candidates.jsonl":
            if not isinstance(row.get("disposition"), str) or (
                "selector_count" in row and not isinstance(row["selector_count"], int)
            ):
                raise ValueError(f"{path}:{number}: invalid candidate disposition or selector_count")
        if path.name.endswith("waits.jsonl") and "duration_s" in row and (
            not isinstance(row["duration_s"], (int, float)) or isinstance(row["duration_s"], bool)
        ):
            raise ValueError(f"{path}:{number}: duration_s is not a number")
        rows.append((number, row))
    return rows


def normalize_repo(value: str) -> str:
    return value.removeprefix("github.com/")


def candidate_name(row: dict[str, Any]) -> str:
    return f"{normalize_repo(row['repository'])}:{row['path']}"


def screen_value(value: str) -> str:
    if value.startswith("passed"):
        return "pass"
    if value.startswith("not-run:"):
        return value
    return "failed: " + value.split(": ", 1)[-1]


def screens(directory: Path) -> dict[tuple[str, str, str], dict[str, Any]]:
    found = {}
    for _, row in jsonl(directory / "screens.jsonl"):
        for key in row.get("keys") or [row.get("key")]:
            if key:
                found[(key, candidate_name(row), row.get("sha256", ""))] = row
    return found


def classify(
    source: str,
    key: str,
    row: dict[str, Any],
    evidence: str,
    screened: dict[tuple[str, str, str], dict[str, Any]],
    *,
    closed: bool = False,
) -> dict[str, str]:
    name = candidate_name(row)
    revision = (
        row.get("commit") or f"blob:{row.get('blob') or row.get('sha') or 'unresolved'}"
    )
    digest = row.get("sha256") or "not-fetched"
    count = row.get("selector_count", row.get("selector_counts", {}).get(key, 0))
    status = row.get("disposition") or row.get("status") or "acquisition-outstanding"
    if status not in RAW_STATUSES:
        raise ValueError(f"unknown acquisition status: {status}")
    if status in RAW_DECLARING and count:
        census = f"census {count}"
        screen = screened.get((key, name, digest))
        if screen:
            licence = screen_value(screen["license"])
            ref = screen_value(screen["ref"])
            fern = screen_value(screen["fern"])
            settled = screen["disposition"]
            disposition = (
                settled
                if settled in ("witness-found", "not-owed", PENDING_REGISTRATION)
                or BYTE_IDENTICAL.fullmatch(settled)
                else "rejected"
            )
        else:
            licence = ref = fern = (
                "not-run: key closed by found witness"
                if closed
                else "not-run: declaration screen outstanding"
            )
            disposition = "not-owed" if closed else "outstanding"
    elif status in RAW_OUTSTANDING:
        # The ledger row keeps the parser's whole diagnostic; the record cites it.
        diagnostic = str(row.get("diagnostic") or "document not yet fetched")
        if len(diagnostic) > DIAGNOSTIC_LIMIT:
            diagnostic = diagnostic[:DIAGNOSTIC_LIMIT] + f" [{len(diagnostic)} characters; whole text in the ledger row]"
        census = f"{status}: {diagnostic}"
        licence = ref = fern = f"not-run: {status}"
        disposition = (
            "not-owed"
            if closed and status == "acquisition-outstanding"
            else "outstanding"
        )
    else:
        census = (
            "census 0"
            if status in ("does-not-declare", "readable")
            else f"{status}: not OpenAPI 3"
        )
        licence = ref = fern = "not-run: census found no declaration"
        disposition = "rejected"
    return {
        "source": source,
        "key": key,
        "candidate": name,
        "revision": revision,
        "digest": digest,
        "census": census,
        "licence_screen": licence,
        "revision_screen": ref,
        "fern_screen": fern,
        "disposition": disposition,
        "evidence": evidence,
    }


def source_rows(root: Path, source: str) -> list[dict[str, str]]:
    directory = root / f"witness-search-{source}"
    screened = screens(directory)
    key_data = json.loads((directory / "keys.json").read_text(encoding="utf-8"))
    if not isinstance(key_data, dict) or not isinstance(key_data.get("keys"), dict):
        raise ValueError(f"{directory / 'keys.json'}: keys must be a mapping")
    if any(not isinstance(key, str) or not key for key in key_data["keys"]):
        raise ValueError(f"{directory / 'keys.json'}: keys must be nonempty strings")
    keys = sorted(key_data["keys"])
    latest: dict[tuple[str, str, str], dict[str, str]] = {}
    resolved_blobs = set()
    filename = (
        "documents.jsonl" if source == "github-publisher-trees" else "candidates.jsonl"
    )
    for number, row in jsonl(directory / filename):
        targets = keys if source == "github-publisher-trees" else [row["key"]]
        for key in targets:
            closed = (directory / f"closure-{key}.json").is_file()
            result = classify(
                source, key, row, f"{filename}:{number}", screened, closed=closed
            )
            latest[(key, result["candidate"], result["revision"])] = result
            if source == "github-code-search" and row.get("blob"):
                resolved_blobs.add((key, result["candidate"], row["blob"]))
    if source == "github-publisher-trees":
        for number, tree in jsonl(directory / "trees.jsonl"):
            if "paths" not in tree:
                continue
            for path in tree["paths"]:
                item = {
                    "repository": tree["repository"],
                    "path": path["path"],
                    "commit": tree["commit"],
                    "blob": path.get("blob"),
                }
                for key in keys:
                    identity = (key, candidate_name(item), tree["commit"])
                    if identity not in latest:
                        latest[identity] = classify(
                            source,
                            key,
                            item,
                            f"trees.jsonl:{number}",
                            screened,
                            closed=(directory / f"closure-{key}.json").is_file(),
                        )
    else:
        for number, query in jsonl(directory / "queries.jsonl"):
            if query.get("outcome") != "answered":
                continue
            key = query["key"]
            closed = (directory / f"closure-{key}.json").is_file()
            for item in query.get("results", []):
                name = candidate_name(item)
                revision = (
                    item.get("commit") or f"blob:{item.get('sha') or 'unresolved'}"
                )
                identity = (key, name, revision)
                if identity in latest:
                    continue
                # GitHub search supplies a blob SHA; the contents acquisition
                # resolves it to a pinned commit. Match by blob before creating
                # an outstanding row for the unresolved query hit.
                if (
                    source == "github-code-search"
                    and (key, name, item.get("sha")) in resolved_blobs
                ):
                    continue
                latest[identity] = classify(
                    source,
                    key,
                    item,
                    f"queries.jsonl:{number}",
                    screened,
                    closed=closed,
                )
    return sorted(
        latest.values(), key=lambda row: (row["key"], row["candidate"], row["revision"])
    )


OUTSTANDING_FIELDS = (
    "key",
    "source",
    "outcome",
    "planned_queries",
    "answered_queries",
    "unissued_queries",
    "issued_incomplete",
    "unacquired_candidates",
    "failed_candidates",
    "unscreened_declarers",
    "unwalked_trees",
    "refusals",
    "candidate_records",
)


def query_state(
    rows: list[dict[str, Any]], source: str, key: str, query: str
) -> tuple[str, dict[str, Any] | None, list[dict[str, Any]]]:
    """`complete`, `unissued` or `incomplete` for one recorded query.

    With its last row, and the non-answer each unfinished size window it was
    partitioned into last recorded. A GitHub query is complete when every window
    was paged to its reported count; a Sourcegraph query when its stream reported
    done.
    """
    mine = [row for row in rows if row["key"] == key and row["query"] == query]
    if not mine:
        return "unissued", None, []
    last = mine[-1]
    refusal = (
        [{
            "query": query, "outcome": last["outcome"],
            "status": last.get("status", "not-reported"),
            "at": last.get("at", "not-recorded"),
            "diagnostic": str(last.get("diagnostic", ""))[:300],
        }]
        if last["outcome"] in load_search().NON_ANSWER_OUTCOMES
        else []
    )
    if source == "sourcegraph":
        if any(r["outcome"] == "answered" for r in mine):
            return "complete", last, []
        return "incomplete", last, refusal
    partition = next((r for r in mine if r["outcome"] == "partitioned"), None)
    if partition:
        states, refusals = [], []
        for window in partition["windows"]:
            state, _, found = query_state(rows, source, key, window["query"])
            states.append(state)
            refusals.extend(found or (
                [{"query": window["query"], "outcome": UNISSUED_WINDOW,
                  "reason": "this size window was never issued"}]
                if state == "unissued" else []
            ))
        if all(state == "complete" for state in states):
            return "complete", last, []
        return "incomplete", last, refusals
    answered = [r for r in mine if r["outcome"] == "answered"]
    if answered and not any(r.get("incomplete_results") for r in answered) and (
        answered[-1].get("retrieved_total", 0) >= answered[-1].get("result_count", 0)
    ):
        return "complete", last, []
    limit = index_limit(query, mine)
    if refusal or limit:
        return "incomplete", last, refusal or [limit]
    read = answered[-1] if answered else last
    reported, served = read.get("result_count", 0), read.get("retrieved_total", 0)
    short = (
        f"GitHub reported {reported} and served {served} before an empty page {read.get('page')}"
        if read.get("page_count") == 0
        else f"{served} of {reported} reported results read; page {read.get('page', 0) + 1} onward never requested"
    )
    outcome = SHORT_SERVED if read.get("page_count") == 0 else UNREAD_PAGES
    return "incomplete", last, [{"query": query, "outcome": outcome, "reason": short}]


def index_limit(query: str, rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Why GitHub's index left this unpartitioned window short, from its own rows.

    The most specific recorded limit wins: a window split down to its floor, a
    one-byte window still over the page limit, then a truncation not yet split.
    """
    search = load_search()
    by_outcome = {row["outcome"]: row for row in rows}
    floor = by_outcome.get(search.TRUNCATION_FLOOR)
    if floor:
        width = floor["upper"] - floor["lower"] + 1
        reason = (
            f"GitHub reported {floor['reported']} and served {floor['retrieved']} in a "
            f"{width}-byte window, at or under the {floor['floor']}-byte split floor"
        )
        return {"query": query, "outcome": floor["outcome"], "reason": reason}
    cap = by_outcome.get(search.INDEX_CAP)
    if cap:
        reason = (
            f"a window of files of {cap['size']} bytes still reports {cap['reported']} "
            "results, over the 1,000 GitHub pages"
            if isinstance(cap.get("size"), int)
            else f"GitHub reported {cap['reported']} and pages at most "
            f"{cap.get('retrieved', 1000)} of them"
        )
        return {"query": query, "outcome": cap["outcome"], "reason": reason}
    truncated = by_outcome.get(search.TRUNCATION)
    if truncated:
        reason = (
            f"GitHub reported {truncated['reported']} and served {truncated['retrieved']} "
            f"before an empty page {truncated['page']}; not yet split by size"
        )
        return {"query": query, "outcome": truncated["outcome"], "reason": reason}
    if search.INCOMPLETE_RESULTS in by_outcome:
        return {"query": query, "outcome": search.INCOMPLETE_RESULTS,
                "reason": "GitHub flagged the response incomplete_results"}
    return None


def read_keys(directory: Path) -> dict[str, dict[str, str]]:
    """One source's keys.json, refused unless every key carries its selector."""
    path = directory / "keys.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    keys = data.get("keys") if isinstance(data, dict) else None
    if not isinstance(keys, dict) or any(
        not isinstance(key, str) or not key
        or not isinstance(value, dict) or not isinstance(value.get("selector"), str)
        for key, value in keys.items()
    ):
        raise ValueError(f"{path}: every key must map to an object carrying its selector")
    return keys


def outstanding_rows(root: Path, records: dict[str, list[dict[str, str]]]) -> list[dict[str, str]]:
    """The per-key, per-source inventory of what this search still owes."""
    search = load_search()
    out = []
    for source in SOURCES:
        directory = root / f"witness-search-{source}"
        keys = read_keys(directory)
        queries = [row for _, row in jsonl(directory / "queries.jsonl")]
        walked: dict[tuple[str, str], set[str]] = {}
        for _, row in jsonl(directory / "documents.jsonl"):
            if row.get("status") != "acquisition-failure":
                walked.setdefault((row["repository"], row.get("commit", "")), set()).add(row["path"])
        trees = {
            (row["repository"], row["commit"]): row
            for _, row in jsonl(directory / "trees.jsonl")
            if "paths" in row
        }
        unwalked = []
        if source == "github-publisher-trees":
            declared = json.loads(
                (directory / "publisher-set.json").read_text(encoding="utf-8")
            )
            publishers = declared.get("publishers") if isinstance(declared, dict) else None
            if not isinstance(publishers, list) or any(
                not isinstance(publisher, dict)
                or not isinstance(publisher.get("repository"), str)
                or not isinstance(publisher.get("commit"), str)
                for publisher in publishers
            ):
                raise ValueError(
                    f"{directory / 'publisher-set.json'}: publishers must be objects naming a repository and a commit"
                )
            for publisher in publishers:
                identity = (publisher["repository"], publisher["commit"])
                label = f"{identity[0]}@{identity[1]}"
                if identity not in trees:
                    unwalked.append(f"{label}: tree not listed")
                    continue
                missing = [
                    item["path"] for item in trees[identity]["paths"]
                    if item["path"] not in walked.get(identity, set())
                ]
                if missing:
                    unwalked.append(f"{label}: {len(missing)} documents outstanding")
        for key in sorted(keys):
            planned = (
                [] if source == "github-publisher-trees"
                else search.query_plan(keys[key]["selector"])[source]
            )
            closed = (directory / f"closure-{key}.json").is_file()
            stopped = (
                f"; acquisition for this key stopped once closure-{key}.json closed it on a "
                "witness, and the turn budget went to the open keys"
                if closed else "; the turn budget ran out before it was read"
            )
            answered, unissued, incomplete, refusals = 0, [], [], []
            for query in planned:
                state, last, found = query_state(queries, source, key, query)
                if state == "complete":
                    answered += 1
                elif state == "unissued":
                    unissued.append(query)
                else:
                    incomplete.append({
                        "query": query,
                        "outcome": last["outcome"],
                        "windows": [
                            {**leaf, "reason": leaf["reason"] + stopped}
                            if leaf["outcome"] in UNREAD else leaf
                            for leaf in found
                            if leaf["outcome"] not in search.NON_ANSWER_OUTCOMES
                        ],
                    })
                    refusals.extend(
                        leaf for leaf in found
                        if leaf["outcome"] in search.NON_ANSWER_OUTCOMES
                    )
            mine = [row for row in records[source] if row["key"] == key]
            open_rows = [row for row in mine if row["disposition"] == "outstanding"]
            unacquired = sum(row["census"].startswith("acquisition-outstanding") for row in open_rows)
            unscreened = sum(row["census"].startswith("census ") for row in open_rows)
            failed = len(open_rows) - unacquired - unscreened
            owed = bool(unissued or incomplete or open_rows or unwalked)
            if closed:
                outcome = "witness-found; search continuation owed" if owed else "witness-found"
            elif owed:
                outcome = "search-incomplete"
            elif any(row["census"].startswith("census ") for row in mine):
                outcome = "declarers screened; none registrable"
            else:
                outcome = "none-found"
            out.append({
                "key": key,
                "source": source,
                "outcome": outcome,
                "planned_queries": str(len(planned)),
                "answered_queries": str(answered),
                "unissued_queries": json.dumps(unissued, separators=(",", ":")),
                "issued_incomplete": json.dumps(incomplete, separators=(",", ":")),
                "unacquired_candidates": str(unacquired),
                "failed_candidates": str(failed),
                "unscreened_declarers": str(unscreened),
                "unwalked_trees": json.dumps(unwalked, separators=(",", ":")),
                "refusals": json.dumps(refusals, separators=(",", ":")),
                "candidate_records": f"witness-search-{source}/records.tsv",
            })
    return out


SEARCH_INDEX_FIELDS = ("key", "kind", "subject", "result", "file")
RAW_LANE = "raw.githubusercontent.com"


def query_result(rows: list[dict[str, Any]]) -> str:
    """What one issued query string returned: its reported count, or its non-answer."""
    for row in rows:
        if row["outcome"] == "partitioned":
            return f"{row['reported']} (partitioned by size)"
    answered = [row for row in rows if row["outcome"] == "answered"]
    if answered:
        first = answered[0]
        reported = first.get("result_count", len(first.get("results", [])))
        retrieved = answered[-1].get("retrieved_total", reported)
        if retrieved < reported:
            return f"{reported} ({retrieved} retrieved)"
        return str(reported)
    last = rows[-1]
    return (
        f"no answer yet: {last['outcome']} HTTP {last.get('status', 'not-reported')} "
        f"at {last.get('at', 'not-recorded')}"
    )


def search_index_rows(
    root: Path, source: str, records: list[dict[str, str]]
) -> list[dict[str, str]]:
    """One source's evidence as `key kind subject result file` rows.

    Every query string issued (a planned phrasing or one of its size windows) with
    what it returned; every publisher tree at its commit with its document count;
    every census-confirmed candidate with its count and each of its three screens;
    and each rate-limit bucket or paced lane the acquisitions touched with the
    waits recorded against it.
    """
    directory = root / f"witness-search-{source}"
    keys = sorted(read_keys(directory))
    out = []
    by_query: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for _, row in jsonl(directory / "queries.jsonl"):
        by_query.setdefault((row["key"], row["query"]), []).append(row)
    for (key, query), rows in sorted(by_query.items()):
        out.append({"key": key, "kind": "query", "subject": query,
                    "result": query_result(rows), "file": "queries.jsonl"})
    if source == "github-publisher-trees":
        walked: dict[tuple[str, str], int] = {}
        for _, row in jsonl(directory / "documents.jsonl"):
            if row.get("status") != "acquisition-failure":
                identity = (row["repository"], row.get("commit", ""))
                walked[identity] = walked.get(identity, 0) + 1
        for _, tree in jsonl(directory / "trees.jsonl"):
            if "paths" not in tree:
                continue
            identity = (tree["repository"], tree["commit"])
            listed = len(tree["paths"])
            read = walked.get(identity, 0)
            for key in keys:
                out.append({
                    "key": key, "kind": "walk", "subject": f"{identity[0]}@{identity[1]}",
                    "result": str(listed) if read >= listed else f"{listed} ({read} censused)",
                    "file": "documents.jsonl",
                })
    for row in records:
        if not row["census"].startswith("census "):
            continue
        candidate = f"{row['candidate']}@{row['revision']}"
        out.append({"key": row["key"], "kind": "candidate", "subject": candidate,
                    "result": row["census"], "file": "records.tsv"})
        for screen, field in (("licence", "licence_screen"), ("ref", "revision_screen"),
                              ("fern", "fern_screen")):
            if row[field].startswith("not-run"):
                continue  # the candidate row's disposition in records.tsv says why
            out.append({"key": row["key"], "kind": "screen", "subject": f"{candidate} {screen}",
                        "result": row[field], "file": "screens.jsonl"})
    search = load_search()
    lanes: dict[str, dict[str, Any]] = {}
    for name in search.CALL_LEDGERS:
        for _, row in jsonl(directory / name):
            lane = (
                RAW_LANE if name == search.RAW_CALLS
                else row.get("bucket") or row.get("lane") or "unlabelled"
            )
            lanes.setdefault(lane, {"calls": 0, "waits": {}})["calls"] += 1
    for name in search.WAIT_LEDGERS:
        for _, row in jsonl(directory / name):
            lane = (
                RAW_LANE if name == search.RAW_WAITS
                else row.get("bucket") or row.get("lane") or "unlabelled"
            )
            entry = lanes.setdefault(lane, {"calls": 0, "waits": {}})
            count, total = entry["waits"].get(name, (0, 0.0))
            entry["waits"][name] = (count + 1, total + float(row.get("duration_s") or 0))
    for lane, entry in sorted(lanes.items()):
        waits = "; ".join(
            f"{count} waits {total:.0f} s in {name}"
            for name, (count, total) in sorted(entry["waits"].items())
        ) or "0 waits"
        for key in keys:
            out.append({"key": key, "kind": "wait", "subject": lane,
                        "result": f"{entry['calls']} calls; {waits}",
                        "file": search.RAW_CALLS if lane == RAW_LANE else search.CALLS_FILE})
    return out


def search_index_failures(directory: Path) -> list[str]:
    """Reconcile one source's search-index.tsv with its records.tsv and query ledger.

    Both directions: every census-confirmed record is an indexed candidate with
    the same count and every screen it ran, and every indexed candidate or
    screen is such a record; every issued query string is indexed once, and
    every indexed query was issued.
    """
    def table(name: str) -> list[dict[str, str]]:
        path = directory / name
        if not path.is_file():
            return []
        lines = path.read_text(encoding="utf-8").splitlines()
        header = lines[0].split("\t") if lines else []
        return [dict(zip(header, line.split("\t"))) for line in lines[1:]]

    failures = []
    csv.field_size_limit(sys.maxsize)
    index = table("search-index.tsv")
    with io.StringIO(read_ledger(directory / "records.tsv"), newline="") as stream:
        records = list(csv.DictReader(stream, delimiter="\t"))
    expected = set()
    for row in records:
        if not row["census"].startswith("census "):
            continue
        candidate = f"{row['candidate']}@{row['revision']}"
        expected.add((row["key"], "candidate", candidate, row["census"]))
        for screen, field in (("licence", "licence_screen"), ("ref", "revision_screen"),
                              ("fern", "fern_screen")):
            if not row[field].startswith("not-run"):
                expected.add((row["key"], "screen", f"{candidate} {screen}", row[field]))
    indexed = {
        (row["key"], row["kind"], row["subject"], row["result"])
        for row in index if row.get("kind") in ("candidate", "screen")
    }
    for missing in sorted(expected - indexed):
        failures.append(f"{directory.name}: records.tsv {missing[1]} {missing[2]!r} is not indexed")
    for extra in sorted(indexed - expected):
        failures.append(f"{directory.name}: indexed {extra[1]} {extra[2]!r} has no records.tsv row")
    issued = {(row["key"], row["query"]) for _, row in jsonl(directory / "queries.jsonl")}
    queried = [(row["key"], row["subject"]) for row in index if row.get("kind") == "query"]
    if len(queried) != len(set(queried)):
        failures.append(f"{directory.name}: a query is indexed twice")
    for missing in sorted(issued - set(queried)):
        failures.append(f"{directory.name}: issued query {missing[1]!r} is not indexed")
    for extra in sorted(set(queried) - issued):
        failures.append(f"{directory.name}: indexed query {extra[1]!r} was never issued")
    return failures


@functools.lru_cache(maxsize=1)
def load_search() -> Any:
    """The acquisition module: its query plan, outcome split and ledger names."""
    import importlib.util

    path = Path(__file__).resolve().parent / "witness-search-github.py"
    spec = importlib.util.spec_from_file_location("witness_github_search_plan", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def render(rows: list[dict[str, str]], fields: tuple[str, ...]) -> str:
    for row in rows:
        if not known_disposition(row["disposition"]):
            raise ValueError(f"unknown candidate disposition: {row['disposition']}")
    output = io.StringIO()
    writer = csv.DictWriter(
        output, fieldnames=fields, delimiter="\t", lineterminator="\n"
    )
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def render_plain(rows: list[dict[str, str]], fields: tuple[str, ...]) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--evidence-root", type=Path, default=Path("docs/openapi-surface")
    )
    parser.add_argument("--check", action="store_true")
    parser.add_argument(
        "--shard-bytes", type=int, default=SHARD_BYTES,
        help="largest part a written records.tsv or candidates.tsv is split into",
    )
    args = parser.parse_args()
    if args.shard_bytes <= 0:
        parser.error("--shard-bytes must be positive")
    changed = []
    central = []
    records = {}
    for source in SOURCES:
        directory = args.evidence_root / f"witness-search-{source}"
        rows = source_rows(args.evidence_root, source)
        records[source] = rows
        target = directory / "records.tsv"
        expected = render(rows, FIELDS)
        if args.check:
            if not target.is_file() or read_ledger(target) != expected:
                changed.append(str(target))
        else:
            write_ledger(target, expected, args.shard_bytes)
        index_target = directory / "search-index.tsv"
        index_text = "".join(
            "\t".join(row[field] for field in SEARCH_INDEX_FIELDS) + "\n"
            for row in [dict(zip(SEARCH_INDEX_FIELDS, SEARCH_INDEX_FIELDS)),
                        *search_index_rows(args.evidence_root, source, rows)]
        )
        if args.check:
            if not index_target.is_file() or index_target.read_text(encoding="utf-8") != index_text:
                changed.append(str(index_target))
        else:
            index_target.write_text(index_text, encoding="utf-8")
        if args.check:
            changed.extend(search_index_failures(directory))
        for number, row in enumerate(rows, 2):
            central.append(
                {
                    **{field: row[field] for field in FIELDS if field != "evidence"},
                    "record": f"witness-search-{source}/records.tsv:{number}",
                }
            )
    central.sort(
        key=lambda row: (row["source"], row["key"], row["candidate"], row["revision"])
    )
    target = args.evidence_root / "witness-search-github/candidates.tsv"
    target.parent.mkdir(parents=True, exist_ok=True)
    expected = render(central, CENTRAL_FIELDS)
    inventory = args.evidence_root / "witness-search-github/outstanding.tsv"
    owed = render_plain(outstanding_rows(args.evidence_root, records), OUTSTANDING_FIELDS)
    if args.check:
        if not target.is_file() or read_ledger(target) != expected:
            changed.append(str(target))
        if not inventory.is_file() or inventory.read_text(encoding="utf-8") != owed:
            changed.append(str(inventory))
        if changed:
            print(
                "candidate records differ from evidence: "
                + ", ".join(changed)
                + "; rerun scripts/witness-search-github-index.py without --check",
                file=sys.stderr,
            )
            return 1
        return 0
    write_ledger(target, expected, args.shard_bytes)
    inventory.write_text(owed, encoding="utf-8")
    print(f"{target}: {len(central)} candidate records")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError) as error:
        print(
            f"witness-search-github-index: {error}; inspect the source evidence and rerun the index",
            file=sys.stderr,
        )
        raise SystemExit(1) from error
