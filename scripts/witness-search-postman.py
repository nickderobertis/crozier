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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--keys", type=Path, required=True)
    parser.add_argument("--evidence-dir", type=Path, required=True)
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()
    try:
        with args.keys.open(encoding="utf-8", newline="") as handle:
            keys = [row for row in csv.DictReader(handle, dialect="excel-tab")
                    if row.get("census_status", "supported") == "supported"]
    except OSError as error:
        parser.error(f"cannot read --keys {args.keys}: {error}; regenerate the region-key derivation")
    if not keys or not {"key", "selector"} <= keys[0].keys():
        parser.error("--keys must be the region-key derivation TSV")
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
