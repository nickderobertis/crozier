#!/usr/bin/env python3
"""Acquire GitHub and Sourcegraph witness-search results through Contract C.

The search index supplies document identities. Only the surface census over the
fetched document supplies a declaration verdict. Evidence is append-only JSONL
so an interrupted search retains every answered query and outstanding result.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from rate_limit_guard import RateLimitGuard, SecondaryLimit, github_api_url

REPO = Path(__file__).resolve().parent.parent
REGIONS = (
    "bodies-media",
    "document-paths",
    "oas31-extensions",
    "parameters",
    "schemas",
    "security",
)
SOURCEGRAPH_URL = "https://sourcegraph.com"
OPENAPI_VERSION = re.compile(r"3\.[01]\.\d+(?:[-+].*)?")
FIELD = re.compile(r"(?:schema|securityScheme|components)\.([A-Za-z$][A-Za-z0-9$]*)")
DOCUMENT_NAMES = (
    "openapi.yaml",
    "openapi.yml",
    "openapi.json",
    "swagger.yaml",
    "swagger.json",
)


def load(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CENSUS = load("witness_github_census", REPO / "scripts/openapi-surface-census.py")
ROWS = load(
    "witness_github_rows", REPO / "tests/surface_census_test.py"
).RankedBacklogTests.region_rows


def derive_keys(regions: Path) -> dict[str, dict[str, str]]:
    """Read the dispatch key set from the authoritative eight-cell rows."""
    keys = {}
    for region in REGIONS:
        for row in ROWS((regions / f"{region}.md").read_text(encoding="utf-8")):
            if row[3].strip("`") != "gap" or not re.search(r"\bFIXTURE\b", row[7]):
                continue
            key = row[0].strip("`")
            match = re.search(r"census `([^`]+)`", " ".join(row))
            if match is None:
                match = re.search(r"Shape read `([^`]+)`", " ".join(row))
            if match is None:
                raise ValueError(f"{region}/{key}: no selector in its own row")
            selector = match.group(1)
            keys[key] = {
                "region": region,
                "selector": selector,
                "selector_status": "available"
                if CENSUS.selector_error(selector) is None
                else "awaiting-census-grammar",
            }
    return dict(sorted(keys.items()))


def ingredients(selector: str) -> list[str]:
    """The required field spellings visible in a selector."""
    fields = list(dict.fromkeys(FIELD.findall(selector)))
    return fields


def query_plan(selector: str) -> dict[str, list[str]]:
    """Both serializations, and every named document location, for one shape."""
    terms = ingredients(selector)
    if not terms:
        raise ValueError(f"no queryable ingredient in {selector}")
    github = []
    for name in DOCUMENT_NAMES:
        spelling = [
            f'"{term}:"' if name.endswith((".yaml", ".yml")) else f'"\\"{term}\\""'
            for term in terms
        ]
        github.append(" ".join((*spelling, f"filename:{name}")))
    for language in ("YAML", "JSON"):
        spelling = [
            f'"{term}:"' if language == "YAML" else f'"\\"{term}\\""' for term in terms
        ]
        github.append(" ".join((*spelling, "path:openapi", f"language:{language}")))
    sourcegraph = []
    for extension in (r"(yaml|yml)", "json"):
        spelling = [
            f'content:"{term}:"' if extension != "json" else f'content:"\\"{term}\\""'
            for term in terms
        ]
        sourcegraph.append(
            " ".join(
                (
                    rf"file:(openapi|swagger).*\.{extension}$",
                    *spelling,
                    "count:all",
                    "type:file",
                )
            )
        )
    return {"github-code-search": github, "sourcegraph": sourcegraph}


class Acquirer:
    """One process's guarded calls and durable, credential-free evidence."""

    def __init__(
        self,
        evidence: Path,
        *,
        github_url: str | None = None,
        sourcegraph_url: str = SOURCEGRAPH_URL,
    ) -> None:
        self.evidence = evidence
        evidence.mkdir(parents=True, exist_ok=True)
        self.github_url = (github_url or github_api_url()).rstrip("/")
        self.sourcegraph_url = sourcegraph_url.rstrip("/")
        self.guards = {
            host: RateLimitGuard(host, evidence_dir=evidence)
            for host in ("github", "sourcegraph")
        }

    def write(self, filename: str, record: dict[str, Any]) -> None:
        with (self.evidence / filename).open("a", encoding="utf-8") as output:
            output.write(json.dumps(record, sort_keys=True) + "\n")

    def request(self, host: str, bucket: str, url: str) -> tuple[int, bytes, Any]:
        """Bracket one HTTP request, including a refused HTTP response."""
        guard = self.guards[host]
        headers = {"User-Agent": "crozier-witness-search"}
        if host == "github":
            headers["Accept"] = "application/vnd.github+json"
            token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
            if token:
                headers["Authorization"] = f"Bearer {token}"
        else:
            headers["Accept"] = "text/event-stream"
        request = urllib.request.Request(url, headers=headers)
        guard.acquire(bucket, cost=1)
        try:
            try:
                response = urllib.request.urlopen(request, timeout=90)
            except urllib.error.HTTPError as error:
                response = error
        except BaseException as error:
            guard.record(error)
            raise
        guard.record(response)
        return response.status, response.read(), response.headers

    def github_json(self, bucket: str, path: str) -> tuple[int, Any, Any]:
        status, body, headers = self.request("github", bucket, self.github_url + path)
        try:
            return status, json.loads(body), headers
        except json.JSONDecodeError:
            return status, {"diagnostic": body.decode("utf-8", "replace")}, headers

    def github_search(self, key: str, query: str) -> list[dict[str, Any]] | None:
        """Page every result, retaining a non-answer when the API refuses or caps."""
        found = []
        page = 1
        while True:
            path = "/search/code?" + urllib.parse.urlencode(
                {"q": query, "per_page": 100, "page": page}
            )
            try:
                status, payload, _ = self.github_json("code_search", path)
            except SecondaryLimit as error:
                self.write(
                    "queries.jsonl",
                    {
                        "source": "github-code-search",
                        "key": key,
                        "query": query,
                        "page": page,
                        "outcome": "secondary-limiter",
                        "diagnostic": str(error),
                    },
                )
                return None
            if status != 200:
                self.write(
                    "queries.jsonl",
                    {
                        "source": "github-code-search",
                        "key": key,
                        "query": query,
                        "page": page,
                        "outcome": "refused",
                        "status": status,
                        "diagnostic": payload,
                    },
                )
                return None
            items = payload.get("items", [])
            found.extend(items)
            total = payload.get("total_count", 0)
            self.write(
                "queries.jsonl",
                {
                    "source": "github-code-search",
                    "key": key,
                    "query": query,
                    "page": page,
                    "outcome": "answered",
                    "result_count": total,
                    "page_count": len(items),
                    "incomplete_results": payload.get("incomplete_results", False),
                    "results": [
                        {
                            "repository": x["repository"]["full_name"],
                            "path": x["path"],
                            "sha": x["sha"],
                            "url": x["url"],
                        }
                        for x in items
                    ],
                },
            )
            if len(found) >= total or not items:
                return found
            if len(found) >= 1000:
                self.write(
                    "queries.jsonl",
                    {
                        "source": "github-code-search",
                        "key": key,
                        "query": query,
                        "outcome": "outstanding-index-cap",
                        "reported": total,
                        "retrieved": len(found),
                    },
                )
                return None
            page += 1

    def sourcegraph_search(self, key: str, query: str) -> list[dict[str, Any]] | None:
        url = (
            self.sourcegraph_url
            + "/.api/search/stream?"
            + urllib.parse.urlencode({"v": "V3", "q": query})
        )
        try:
            status, data, _ = self.request("sourcegraph", "sourcegraph", url)
        except SecondaryLimit as error:
            self.write(
                "queries.jsonl",
                {
                    "source": "sourcegraph",
                    "key": key,
                    "query": query,
                    "outcome": "secondary-limiter",
                    "diagnostic": str(error),
                },
            )
            return None
        if status != 200:
            self.write(
                "queries.jsonl",
                {
                    "source": "sourcegraph",
                    "key": key,
                    "query": query,
                    "outcome": "refused",
                    "status": status,
                    "diagnostic": data.decode("utf-8", "replace")[:1000],
                },
            )
            return None
        events = []
        for block in data.decode("utf-8", "replace").split("\n\n"):
            event = re.search(r"^event: (.+)$", block, re.M)
            body = re.search(r"^data: (.+)$", block, re.M)
            if event and body:
                events.append((event.group(1), json.loads(body.group(1))))
        matches = [item for name, body in events if name == "matches" for item in body]
        progress = [body for name, body in events if name == "progress"]
        done = progress[-1] if progress else {}
        record = {
            "source": "sourcegraph",
            "key": key,
            "query": query,
            "outcome": "answered" if done.get("done") else "incomplete-stream",
            "result_count": len(matches),
            "progress": done,
            "results": [
                {
                    "repository": x.get("repository"),
                    "path": x.get("path"),
                    "commit": x.get("commit"),
                }
                for x in matches
            ],
        }
        self.write("queries.jsonl", record)
        return matches if done.get("done") else None

    def sourcegraph_document(
        self, key: str, selector: str, item: dict[str, Any]
    ) -> dict[str, Any]:
        repo = item["repository"]
        path = item["path"]
        commit = item["commit"]
        identity = {
            "source": "sourcegraph",
            "key": key,
            "selector": selector,
            "repository": repo,
            "path": path,
            "commit": commit,
        }
        url = (
            self.sourcegraph_url
            + "/"
            + urllib.parse.quote(repo, safe="/")
            + "/-/raw/"
            + urllib.parse.quote(path, safe="/")
            + "?"
            + urllib.parse.urlencode({"rev": commit})
        )
        identity["url"] = url
        try:
            status, data, _ = self.request("sourcegraph", "sourcegraph", url)
        except SecondaryLimit as error:
            record = {
                **identity,
                "disposition": "acquisition-failure",
                "diagnostic": str(error),
            }
            self.write("candidates.jsonl", record)
            return record
        if status != 200:
            record = {
                **identity,
                "disposition": "acquisition-failure",
                "status": status,
                "diagnostic": data.decode("utf-8", "replace")[:1000],
            }
            self.write("candidates.jsonl", record)
            return record
        return self.classify(identity, data)

    def github_document(self, key: str, item: dict[str, Any]) -> dict[str, Any]:
        """Fetch exact result content at its indexed commit, then run the census."""
        identity = {
            "source": "github-code-search",
            "key": key,
            "selector": item["selector"],
            "repository": item["repository"]["full_name"],
            "path": item["path"],
            "blob": item["sha"],
            "url": item["url"],
        }
        url = item["url"]
        if not url.startswith(self.github_url + "/"):
            raise ValueError(f"untrusted GitHub content URL: {url}")
        try:
            status, payload, _ = self.github_json("core", url[len(self.github_url) :])
        except SecondaryLimit as error:
            record = {
                **identity,
                "disposition": "acquisition-failure",
                "diagnostic": str(error),
            }
            self.write("candidates.jsonl", record)
            return record
        if status != 200 or payload.get("encoding") != "base64":
            record = {
                **identity,
                "disposition": "acquisition-failure",
                "status": status,
                "diagnostic": payload,
            }
            self.write("candidates.jsonl", record)
            return record
        data = base64.b64decode(payload["content"])
        return self.classify(identity, data)

    def classify(self, identity: dict[str, Any], data: bytes) -> dict[str, Any]:
        """The selector engine is the sole source of a declaration verdict."""
        digest = hashlib.sha256(data).hexdigest()
        suffix = (
            ".json"
            if data.decode("utf-8-sig", "replace").lstrip().startswith(("{", "["))
            else ".yaml"
        )
        cache = self.evidence / "documents"
        cache.mkdir(exist_ok=True)
        path = cache / (digest + suffix)
        if not path.exists():
            path.write_bytes(data)
        record = {
            **identity,
            "sha256": digest,
            "document": str(path.relative_to(self.evidence)),
        }
        try:
            parsed = CENSUS.load_document(path)
            if not isinstance(parsed, dict) or not OPENAPI_VERSION.fullmatch(
                str(parsed.get("openapi", ""))
            ):
                record.update(disposition="excluded-non-openapi-3", selector_count=0)
            else:
                selector = identity["selector"]
                if CENSUS.selector_error(selector) is not None:
                    record.update(
                        disposition="selector-unavailable",
                        diagnostic=f"census engine does not accept {selector}",
                    )
                else:
                    count = CENSUS.census_document(parsed).get(selector, 0)
                    record.update(
                        disposition="declares" if count else "does-not-declare",
                        selector_count=count,
                    )
        except (CENSUS.DocumentError, ValueError, UnicodeError) as error:
            record.update(disposition="parse-failure", diagnostic=str(error))
        self.write("candidates.jsonl", record)
        return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--regions", type=Path, default=REPO / "docs/openapi-surface")
    parser.add_argument("--derive-only", action="store_true")
    args = parser.parse_args()
    keys = derive_keys(args.regions)
    args.evidence.mkdir(parents=True, exist_ok=True)
    (args.evidence / "keys.json").write_text(
        json.dumps(
            {
                "source_commit": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=REPO, text=True
                ).strip(),
                "derivation": "RankedBacklogTests.region_rows over six region files: category gap and settlement FIXTURE",
                "keys": keys,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    if args.derive_only:
        print(f"derived {len(keys)} FIXTURE gap keys")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
