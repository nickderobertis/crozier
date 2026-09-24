#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] This Cargo crate has no Nx graph; the paced Postman search command belongs beside the other just-driven witness-search scripts and is exercised by the acquisition tier.
"""Ask Postman's three public API-network indices for every current FIXTURE gap."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

REPO = Path(__file__).resolve().parent.parent
INDICES = ("apinetwork.team", "runtime.collection", "adp.api")
DEFAULT_URL = "https://www.postman.com/_api/ws/proxy"
DEFAULT_WEB = "https://www.postman.com"
DEFAULT_API = "https://api.getpostman.com"
# What a search-all hit is, and the one unauthenticated route Postman documents
# for reading it: a collection's JSON link, a team's public profile. An API or
# a specification is readable only through the Postman API, which requires an
# API key, so its attempt is the keyless request that key would authorise.
HIT_ROUTES = {
    "collection": "{web}/collections/{id}",
    "team": "{web}/{handle}",
    "api": "{api}/apis/{id}",
    "apiDefinition": "{api}/apis/{id}",
    "specification": "{api}/specs/{id}",
}


def load_guard():
    path = REPO / "scripts/rate_limit_guard.py"
    spec = importlib.util.spec_from_file_location("witness_postman_guard", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


GUARD = load_guard()


def phrasings(key: str, selector: str) -> tuple[str, str]:
    first = key.replace("-", " ")
    terms = list(dict.fromkeys(re.findall(r"(?:schema|securityScheme|components)\.([A-Za-z][A-Za-z0-9]*)", selector)))
    if len(terms) > 1:
        second = " ".join(terms)
    elif terms:
        second = f"{first} {terms[0]}"
    else:
        second = selector.replace(":", " ").replace("$", "")
    if second == first:
        second = f"OpenAPI {second}"
    return first, second


def request_body(query: str, offset: int, index: str) -> dict:
    return {"service": "search", "method": "POST", "path": "/search-all", "body": {
        "queryIndices": [index], "queryText": query, "size": 25, "from": offset,
    }}


def search_once(url: str, guard, query: str, offset: int, index: str) -> tuple[int | None, bytes]:
    request = urllib.request.Request(
        url, data=json.dumps(request_body(query, offset, index), separators=(",", ":")).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "crozier-witness-search/1"},
        method="POST",
    )
    guard.acquire("postman", cost=1)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read()
            guard.record(response)
            return response.status, body
    except urllib.error.HTTPError as response:
        body = response.read()
        guard.record(response)
        return response.code, body
    except (OSError, urllib.error.URLError) as error:
        guard.record(SimpleNamespace(status=503, headers={}, url=url))
        return None, str(error).encode()


def load_census():
    path = REPO / "scripts/openapi-surface-census.py"
    spec = importlib.util.spec_from_file_location("witness_postman_census", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def metadata_hits(queries: Path) -> dict[tuple[str, str], dict]:
    """(hit type, id) -> its route fields and the keys whose queries returned it.

    A request hit is read through the collection that holds it, so it adds its
    parent collection rather than a hit of its own."""
    hits: dict[tuple[str, str], dict] = {}
    for line in queries.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        for kind, found in (row.get("data") or {}).items():
            for hit in found:
                document = hit.get("document", {})
                if kind == "request":
                    kind, document = "collection", document.get("collection", {})
                if kind not in HIT_ROUTES or not document.get("id"):
                    continue
                entry = hits.setdefault((kind, str(document["id"])), {
                    "handle": document.get("publicHandle", ""), "keys": set()})
                entry["keys"].add(row["key"])
    return hits


def classify_body(status: int | None, content_type: str, body: bytes,
                  keys: list[dict], census) -> dict:
    """What an acquired body is, decided by parsing it and running the census."""
    if status != 200:
        return {"classification": "source-refused",
                "response": body.decode("utf-8", errors="replace")[:500]}
    if "json" not in content_type:
        return {"classification": "no-document-body",
                "blocker": f"route returned {content_type or 'no content type'}, not a document"}
    try:
        document = json.loads(body)
    except json.JSONDecodeError as error:
        return {"classification": "parse-failure", "blocker": str(error)}
    if isinstance(document, dict) and str(document.get("openapi", "")).startswith("3."):
        selectors = [row["selector"] for row in keys]
        conjunctions = {s: census.compile_conjunction(s) for s in selectors
                        if census.selector_error(s) is None and census.is_conjunction(s)}
        counts = census.census_document(document, conjunctions=conjunctions)
        return {"classification": "openapi-3",
                "selectors": {row["key"]: counts.get(row["selector"], 0) for row in keys}}
    schema = document.get("info", {}).get("schema", "") if isinstance(document, dict) else ""
    return {"classification": "not-openapi-3",
            "document_kind": "postman-collection" if "getpostman.com" in str(schema) else "other-json"}


def acquire_hits(args: argparse.Namespace, keys: list[dict]) -> int:
    queries = args.evidence_dir / "queries.jsonl"
    try:
        hits = metadata_hits(queries)
    except (OSError, ValueError) as error:
        raise SystemExit(f"witness-search-postman: cannot read {queries}: {error}; "
                         "run the search stage first")
    census = load_census()
    guard = GUARD.RateLimitGuard("postman", evidence_dir=args.evidence_dir)
    output = args.evidence_dir / "hit-access.jsonl"
    with output.open("w", encoding="utf-8") as handle:
        for (kind, identifier), entry in sorted(hits.items()):
            url = HIT_ROUTES[kind].format(web=args.web_base.rstrip("/"), api=args.api_base.rstrip("/"),
                                          id=identifier, handle=entry["handle"] or identifier)
            request = urllib.request.Request(url, headers={
                "User-Agent": "crozier-witness-search/1", "Accept": "application/json"})
            while True:
                taken = datetime.now(timezone.utc).isoformat(timespec="seconds")
                content_type = ""
                try:
                    guard.acquire("postman", cost=1)
                except GUARD.SecondaryLimit as error:
                    status, body = None, str(error).encode()
                    break
                try:
                    with urllib.request.urlopen(request, timeout=60) as response:
                        body = response.read()
                        guard.record(response)
                        status, content_type = response.status, response.headers.get("Content-Type", "")
                except urllib.error.HTTPError as response:
                    body = response.read()
                    guard.record(response)
                    status, content_type = response.code, response.headers.get("Content-Type", "")
                except (OSError, urllib.error.URLError) as error:
                    guard.record(SimpleNamespace(status=503, headers={}, url=url))
                    status, body = None, str(error).encode()
                if status not in GUARD.REFUSAL_STATUSES and status is not None:
                    break
                # A throttle is waited out by the next acquire's backoff, never recorded as an answer.
            record = {"hit": kind, "id": identifier, "keys": sorted(entry["keys"]), "url": url,
                      "taken_utc": taken, "status": status, "content_type": content_type,
                      "sha256": hashlib.sha256(body).hexdigest(),
                      **classify_body(status, content_type, body, keys, census)}
            handle.write(json.dumps(record, sort_keys=True) + "\n")
            handle.flush()
    print(f"witness-search-postman: recorded {len(hits)} metadata-hit acquisitions")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--keys", type=Path, required=True)
    parser.add_argument("--evidence-dir", type=Path, required=True)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--acquire-hits", action="store_true",
                        help="read every metadata hit in queries.jsonl through its unauthenticated route")
    parser.add_argument("--web-base", default=DEFAULT_WEB)
    parser.add_argument("--api-base", default=DEFAULT_API)
    args = parser.parse_args()
    try:
        with args.keys.open(encoding="utf-8", newline="") as handle:
            keys = [row for row in csv.DictReader(handle, dialect="excel-tab")
                    if row.get("census_status", "supported") == "supported"]
    except OSError as error:
        parser.error(f"cannot read --keys {args.keys}: {error}; regenerate the region-key derivation")
    if not keys or not {"key", "selector"} <= keys[0].keys():
        parser.error("--keys must be the region-key derivation TSV")
    if args.acquire_hits:
        return acquire_hits(args, keys)
    args.evidence_dir.mkdir(parents=True, exist_ok=True)
    guard = GUARD.RateLimitGuard("postman", evidence_dir=args.evidence_dir)
    rows = []
    for row in keys:
        for query in phrasings(row["key"], row["selector"]):
            for index in INDICES:
                offset = 0
                while True:
                    taken = datetime.now(timezone.utc).isoformat(timespec="seconds")
                    try:
                        status, body = search_once(args.url, guard, query, offset, index)
                    except GUARD.SecondaryLimit as error:
                        rows.append({"key": row["key"], "selector": row["selector"],
                                     "query": query, "index": index, "offset": offset,
                                     "taken_utc": taken, "classification": "source-refused",
                                     "error": str(error)})
                        break
                    result = {"key": row["key"], "selector": row["selector"],
                              "query": query, "index": index, "offset": offset,
                              "request": request_body(query, offset, index), "taken_utc": taken,
                              "status": status, "sha256": hashlib.sha256(body).hexdigest()}
                    if status != 200:
                        result["classification"] = "source-refused"
                        result["response"] = body.decode("utf-8", errors="replace")[:500]
                        rows.append(result)
                        if status in (429, 503):
                            continue  # the next acquire waits out the guard's backoff
                        break
                    try:
                        payload = json.loads(body)
                        totals = payload["meta"]["total"]
                        if not isinstance(totals, dict):
                            raise ValueError("meta.total is not an object")
                        result["totals"] = totals
                        result["data"] = payload.get("data", {})
                        result["classification"] = "answered"
                        rows.append(result)
                        kinds = ("team",) if index == "apinetwork.team" else (
                            "collection",) if index == "runtime.collection" else (
                            "api", "apiDefinition", "specification")
                        count = sum(int(totals.get(kind, 0)) for kind in kinds)
                        if offset + 25 >= count:
                            break
                        offset += 25
                    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
                        result["classification"] = "source-error"
                        result["error"] = str(error)
                        rows.append(result)
                        break
    output = args.evidence_dir / "queries.jsonl"
    output.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
    print(f"witness-search-postman: recorded {len(rows)} request results for {len(keys)} keys")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
