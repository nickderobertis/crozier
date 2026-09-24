#!/usr/bin/env python3
"""Acquire GitHub and Sourcegraph witness-search results through Contract C.

The search index supplies document identities. Only the surface census over the
fetched document supplies a declaration verdict. Evidence is append-only JSONL
so an interrupted search retains every answered query and outstanding result.
"""

from __future__ import annotations

import argparse
import base64
import csv
import datetime
import email.utils
import functools
import gzip
import hashlib
import http.client
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from rate_limit_guard import (
    REFUSAL_STATUSES,
    RateLimitGuard,
    SecondaryLimit,
    github_api_url,
)

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
RAW_GITHUB_URL = "https://raw.githubusercontent.com"
RAW_SPACING_S = 2.0
RAW_BACKOFF_BASE_S = 10.0
RAW_TRANSFER_ATTEMPT_BUDGET = 3
CODE_SEARCH_SPACING_S = 30.0
CODE_SEARCH_REFUSAL_COOLDOWN_S = 300.0
SOURCEGRAPH_SPACING_S = 10.0
SOURCEGRAPH_REFUSAL_COOLDOWN_S = 3600.0
OPENAPI_VERSION = re.compile(r"3\.\d+\.\d+(?:[-+].*)?")
FIELD = re.compile(r"(?:schema|securityScheme|components)\.([A-Za-z$][A-Za-z0-9$]*)")
DOCUMENT_NAMES = (
    "openapi.yaml",
    "openapi.yml",
    "openapi.json",
    "swagger.yaml",
    "swagger.json",
)


class SearchStopped(RuntimeError):
    """A refusal leaves the affected key outstanding and stops this source run."""


class MissingScope(ValueError):
    """A named publisher subtree is absent at the pinned commit."""


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
                "selector_status": (
                    "available"
                    if CENSUS.selector_error(selector) is None
                    else "parsed Reference Object; census selector unavailable"
                    if selector == "securityScheme:$ref"
                    else "unavailable"
                ),
            }
    return dict(sorted(keys.items()))


def ingredients(selector: str) -> list[str]:
    """The required field spellings visible in a selector."""
    fields = list(dict.fromkeys(FIELD.findall(selector)))
    for composition in ("oneOf", "anyOf"):
        if f"pointer-walk-reaches={composition}" in selector:
            fields.append(composition)
    return fields


def distinguishing_phrase(selector: str, language: str, variant: int) -> str | None:
    """A selector value makes a query specific to its branch, beyond field names."""
    yaml = language == "YAML"
    if "unnamed-segment" in selector:
        return '"/definitions/"' if variant else '"/$defs/"'
    if "undeclared-component-head" in selector:
        return (
            '"#/components/schemas/Unknown"'
            if variant
            else '"#/components/schemas/undefined"'
        )
    if selector == "securityScheme:$ref":
        return '"securitySchemes/"' if variant else '"#/components/securitySchemes/"'
    if "primary=array" in selector:
        return '"type: array"' if yaml else '"array"'
    if "additionalProperties=false" in selector:
        return '"additionalProperties: false"' if yaml else '"false"'
    if "!schema.properties:non-empty" in selector:
        return '"properties: {}"' if yaml else '"{}"'
    if "annotated-ref" in selector:
        term = "title" if variant else "description"
        return f'"{term}:"' if yaml else f'"\\"{term}\\""'
    if "flows.password" in selector:
        return '"password:"' if yaml else '"password"'
    return None


def query_plan(selector: str) -> dict[str, list[str]]:
    """Both serializations, and every named document location, for one shape."""
    terms = ingredients(selector)
    if not terms:
        raise ValueError(f"no queryable ingredient in {selector}")
    github = []
    for index, name in enumerate(DOCUMENT_NAMES):
        language = "YAML" if name.endswith((".yaml", ".yml")) else "JSON"
        spelling = [
            f'"{term}:"' if language == "YAML" else f'"\\"{term}\\""' for term in terms
        ]
        extra = distinguishing_phrase(selector, language, index % 2)
        github.append(
            " ".join((*spelling, *([extra] if extra else []), f"filename:{name}"))
        )
    for index, language in enumerate(("YAML", "JSON")):
        spelling = [
            f'"{term}:"' if language == "YAML" else f'"\\"{term}\\""' for term in terms
        ]
        extra = distinguishing_phrase(selector, language, index)
        github.append(
            " ".join(
                (
                    *spelling,
                    *([extra] if extra else []),
                    "path:openapi",
                    f"language:{language}",
                )
            )
        )
    sourcegraph = []
    for index, extension in enumerate((r"(yaml|yml)", "json")):
        language = "JSON" if extension == "json" else "YAML"
        spelling = [
            f'content:"{term}:"' if language == "YAML" else f'content:"\\"{term}\\""'
            for term in terms
        ]
        extra = distinguishing_phrase(selector, language, index)
        sourcegraph.append(
            " ".join(
                (
                    rf"file:(openapi|swagger).*\.{extension}$",
                    *spelling,
                    *([f"content:{extra}"] if extra else []),
                    "count:all",
                    "type:file",
                )
            )
        )
    return {"github-code-search": github, "sourcegraph": sourcegraph}


def publisher_set() -> list[dict[str, Any]]:
    """Prior trees, registered publishers, and publisher-owned declarer repositories."""
    wide = REPO / "docs/openapi-surface/witness-scrape-wide/trees.json.gz"
    trees = json.load(gzip.open(wide, "rt", encoding="utf-8"))["trees"]
    selected = [
        {
            "repository": item["repo"],
            "commit": item["ref"],
            "scope": item["scope"],
            "derivation": "witness-scrape-wide publisher tree",
        }
        for item in trees
        if item["repo"] != "APIs-guru/openapi-directory"
    ]
    corpus = REPO / "tests/fixtures/CORPUS.md"
    for line in corpus.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\| \d+ \|", line):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 8 or cells[2] != "github-raw" or cells[6] != "link-ok":
            continue
        url = urllib.parse.urlsplit(cells[3])
        if url.hostname != "raw.githubusercontent.com":
            continue
        parts = url.path.strip("/").split("/")
        if len(parts) != 4 or not parts[-1].startswith(("openapi.", "swagger.")):
            continue
        repository = "/".join(parts[:2])
        if "example" in repository.lower() or repository in {
            item["repository"] for item in selected
        }:
            continue
        selected.append(
            {
                "repository": repository,
                "commit": parts[2],
                "scope": "",
                "derivation": f"CORPUS.md row {cells[0]} root-level {parts[-1]}",
            }
        )
    declarers = (
        REPO
        / "docs/openapi-surface/witness-search-github-publisher-trees/publisher-declarers.tsv"
    )
    with declarers.open(encoding="utf-8", newline="") as stream:
        for item in csv.DictReader(stream, delimiter="\t"):
            repository = item["repository"]
            if repository in {row["repository"] for row in selected}:
                continue
            selected.append(
                {
                    "repository": repository,
                    "commit": item["commit"],
                    "scope": "",
                    "derivation": f"{item['source']} declarer: {item['ownership_evidence']}",
                }
            )
    return selected


class Acquirer:
    """One process's guarded calls and durable, credential-free evidence."""

    def __init__(
        self,
        evidence: Path,
        *,
        cache: Path | None = None,
        github_url: str | None = None,
        sourcegraph_url: str = SOURCEGRAPH_URL,
        raw_github_url: str = RAW_GITHUB_URL,
        code_search_spacing_s: float = CODE_SEARCH_SPACING_S,
        code_search_refusal_cooldown_s: float = CODE_SEARCH_REFUSAL_COOLDOWN_S,
        sourcegraph_spacing_s: float = SOURCEGRAPH_SPACING_S,
        sourcegraph_refusal_cooldown_s: float = SOURCEGRAPH_REFUSAL_COOLDOWN_S,
    ) -> None:
        self.evidence = evidence
        evidence.mkdir(parents=True, exist_ok=True)
        self.cache = cache or evidence
        self.cache.mkdir(parents=True, exist_ok=True)
        self.github_url = (github_url or github_api_url()).rstrip("/")
        self.sourcegraph_url = sourcegraph_url.rstrip("/")
        self.raw_github_url = raw_github_url.rstrip("/")
        self.raw_last_request: float | None = None
        self.extra_pacing = {
            ("github", "code_search"): (
                code_search_spacing_s,
                code_search_refusal_cooldown_s,
            ),
            ("sourcegraph", "sourcegraph"): (
                sourcegraph_spacing_s,
                sourcegraph_refusal_cooldown_s,
            ),
        }
        self.guards = {
            host: RateLimitGuard(host, evidence_dir=evidence)
            for host in ("github", "sourcegraph")
        }

    def write(self, filename: str, record: dict[str, Any]) -> None:
        record = {
            "at": datetime.datetime.now(datetime.timezone.utc).isoformat(
                timespec="milliseconds"
            ),
            **record,
        }
        with (self.evidence / filename).open("a", encoding="utf-8") as output:
            output.write(json.dumps(record, sort_keys=True) + "\n")

    def request(
        self, host: str, bucket: str, url: str, *, accept: str | None = None
    ) -> tuple[int, bytes, Any]:
        """Bracket one HTTP request, including a refused HTTP response."""
        guard = self.guards[host]
        headers = {"User-Agent": "crozier-witness-search"}
        if host == "github":
            headers["Accept"] = accept or "application/vnd.github+json"
            token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
            if token:
                headers["Authorization"] = f"Bearer {token}"
        else:
            headers["Accept"] = "text/event-stream"
        request = urllib.request.Request(url, headers=headers)
        self.wait_for_index_pacing(host, bucket)
        guard.acquire(bucket, cost=1)
        try:
            try:
                response = urllib.request.urlopen(request, timeout=90)
            except urllib.error.HTTPError as error:
                response = error
            body = response.read()
        except BaseException as error:
            guard.record(error)
            raise
        guard.record(response)
        return response.status, body, response.headers

    def wait_for_index_pacing(self, host: str, bucket: str) -> None:
        """Space index calls across process restarts and cool after refusals."""
        if (host, bucket) not in self.extra_pacing:
            return
        spacing, cooldown = self.extra_pacing[(host, bucket)]
        calls = [
            row
            for row in jsonl(self.evidence / "rate-limit-calls.jsonl")
            if row.get("host") == host
            and (row.get("bucket") or row.get("lane")) == bucket
        ]
        if not calls:
            return
        last = calls[-1]
        last_time = datetime.datetime.fromisoformat(last["at"]).timestamp()
        refusal = next(
            (
                row
                for row in reversed(calls)
                if row.get("status") in ((403, 429) if host == "github" else (429, 503))
            ),
            None,
        )
        spacing_until = last_time + spacing
        refusal_until = (
            datetime.datetime.fromisoformat(refusal["at"]).timestamp() + cooldown
            if refusal
            else 0.0
        )
        deadline = max(spacing_until, refusal_until)
        duration = max(0.0, deadline - time.time())
        if duration:
            cause = "refusal-cooldown" if refusal_until >= spacing_until else "spacing"
            started = datetime.datetime.now(datetime.timezone.utc).isoformat()
            time.sleep(duration)
            self.write(
                "index-pacing-waits.jsonl",
                {
                    "host": host,
                    "bucket": bucket,
                    "cause": cause,
                    "duration_s": duration,
                    "started_at": started,
                    "last_status": last.get("status"),
                },
            )

    def github_json(self, bucket: str, path: str) -> tuple[int, Any, Any]:
        status, body, headers = self.request("github", bucket, self.github_url + path)
        try:
            return status, json.loads(body), headers
        except json.JSONDecodeError:
            return status, {"diagnostic": body.decode("utf-8", "replace")}, headers

    def github_contents(self, path: str) -> tuple[int, bytes | None, Any]:
        """Read a contents path, including large files through its raw media type."""
        status, payload, _ = self.github_json("core", path)
        if status != 200:
            return status, None, payload
        if payload.get("encoding") == "base64":
            return status, base64.b64decode(payload["content"]), payload
        if payload.get("encoding") == "none":
            status, data, _ = self.request(
                "github",
                "core",
                self.github_url + path,
                accept="application/vnd.github.raw+json",
            )
            if status == 200:
                try:
                    maybe_metadata = json.loads(data)
                except (json.JSONDecodeError, UnicodeDecodeError):
                    maybe_metadata = None
                if not (
                    isinstance(maybe_metadata, dict)
                    and maybe_metadata.get("encoding") == "none"
                    and "download_url" in maybe_metadata
                ):
                    return (
                        status,
                        data,
                        {"raw_media_type": "application/vnd.github.raw+json"},
                    )
            return (
                status,
                None,
                {"raw_media_type_response": data.decode("utf-8", "replace")[:1000]},
            )
        return status, None, payload

    def git_tree(
        self, repository: str, sha: str, *, recursive: bool = False
    ) -> dict[str, Any]:
        path = (
            "/repos/"
            + urllib.parse.quote(repository, safe="/")
            + "/git/trees/"
            + urllib.parse.quote(sha, safe="")
            + ("?recursive=1" if recursive else "")
        )
        status, payload, _ = self.github_json("core", path)
        if status != 200:
            raise SearchStopped(
                f"GitHub git tree {repository}@{sha}: HTTP {status}; publisher walk outstanding"
            )
        return payload

    def scope_sha(self, repository: str, commit: str, scope: str) -> str:
        sha = commit
        for segment in scope.split("/") if scope else ():
            entries = self.git_tree(repository, sha)["tree"]
            child = next(
                (
                    item
                    for item in entries
                    if item["path"] == segment and item["type"] == "tree"
                ),
                None,
            )
            if child is None:
                raise MissingScope(
                    f"publisher scope {repository}@{commit}/{scope} missing {segment}"
                )
            sha = child["sha"]
        return sha

    def scope_files(
        self, repository: str, commit: str, scope: str
    ) -> list[dict[str, str]]:
        sha = self.scope_sha(repository, commit, scope)
        payload = self.git_tree(repository, sha, recursive=True)
        if not payload.get("truncated"):
            return [
                {
                    "path": "/".join(filter(None, (scope, item["path"]))),
                    "blob": item["sha"],
                }
                for item in payload["tree"]
                if item["type"] == "blob"
            ]

        def descend(tree_sha: str, prefix: str) -> list[dict[str, str]]:
            entries = self.git_tree(repository, tree_sha)["tree"]
            files = []
            for item in entries:
                path = "/".join(filter(None, (prefix, item["path"])))
                if item["type"] == "tree":
                    files.extend(descend(item["sha"], path))
                elif item["type"] == "blob":
                    files.append({"path": path, "blob": item["sha"]})
            return files

        return descend(sha, scope)

    def publisher_walk(
        self, publisher: dict[str, Any], keys: dict[str, dict[str, str]]
    ) -> None:
        repository = publisher["repository"]
        commit = publisher["commit"]
        prior = next(
            (
                row
                for row in jsonl(self.evidence / "trees.jsonl")
                if row.get("repository") == repository
                and row.get("commit") == commit
                and "paths" in row
            ),
            None,
        )
        if prior:
            paths = {item["path"]: item for item in prior["paths"]}
        else:
            scopes = (
                publisher["scope"]
                if isinstance(publisher["scope"], list)
                else [publisher["scope"]]
            )
            paths = {}
            missing_scopes = []
            for scope in scopes:
                try:
                    files = self.scope_files(repository, commit, scope)
                except MissingScope as error:
                    missing_scopes.append(str(error))
                    continue
                for item in files:
                    if item["path"].lower().endswith((".yaml", ".yml", ".json")):
                        paths[item["path"]] = item
            self.write(
                "trees.jsonl",
                {
                    **publisher,
                    "candidate_document_count": len(paths),
                    "missing_scopes": missing_scopes,
                    "paths": sorted(paths.values(), key=lambda x: x["path"]),
                },
            )
        done = {
            (row["repository"], row["path"], row["commit"])
            for row in jsonl(self.evidence / "documents.jsonl")
            if row.get("status") not in ("acquisition-failure",)
        }
        for path, item in sorted(paths.items()):
            if (repository, path, commit) in done:
                continue
            url = (
                self.raw_github_url
                + "/"
                + urllib.parse.quote(repository, safe="/")
                + "/"
                + commit
                + "/"
                + urllib.parse.quote(path, safe="/")
            )
            identity = {
                "source": "github-publisher-trees",
                "repository": repository,
                "path": path,
                "commit": commit,
                "blob": item["blob"],
                "url": url,
                "acquisition_route": "pinned-raw-github",
            }
            try:
                status, data = self.raw_github_get(
                    url, "publisher-trees", f"{repository}/{path}@{commit}"
                )
            except OSError as error:
                self.write(
                    "documents.jsonl",
                    {
                        **identity,
                        "status": "acquisition-failure",
                        "diagnostic": f"{type(error).__name__}: {error}",
                    },
                )
                continue
            if status != 200:
                self.write(
                    "documents.jsonl",
                    {
                        **identity,
                        "status": "acquisition-failure",
                        "http_status": status,
                        "diagnostic": data.decode("utf-8", "replace")[:1000],
                    },
                )
                if status in (403, 429):
                    raise SearchStopped(
                        f"GitHub refused publisher contents {repository}/{path}: HTTP {status}"
                    )
                continue
            result = self.census_tree_document(data, keys)
            self.write("documents.jsonl", {**identity, **result})

    def census_tree_document(
        self, data: bytes, keys: dict[str, dict[str, str]]
    ) -> dict[str, Any]:
        digest = hashlib.sha256(data).hexdigest()
        suffix = (
            ".json"
            if data.decode("utf-8-sig", "replace").lstrip().startswith(("{", "["))
            else ".yaml"
        )
        path = self.cache / "documents" / (digest + suffix)
        path.parent.mkdir(exist_ok=True)
        if not path.exists():
            path.write_bytes(data)
        try:
            parsed = CENSUS.load_document(path)
            if not isinstance(parsed, dict) or not OPENAPI_VERSION.fullmatch(
                str(parsed.get("openapi", ""))
            ):
                return {"sha256": digest, "status": "excluded-non-openapi-3"}
            counts = CENSUS.census_document(parsed)
            selected = {
                key: counts.get(value["selector"], 0)
                for key, value in keys.items()
                if value["selector"] != "securityScheme:$ref"
            }
            schemes = (parsed.get("components") or {}).get("securitySchemes") or {}
            selected["securityscheme-ref"] = (
                sum(
                    isinstance(value, dict) and isinstance(value.get("$ref"), str)
                    for value in schemes.values()
                )
                if isinstance(schemes, dict)
                else 0
            )
            return {"sha256": digest, "status": "readable", "selector_counts": selected}
        except (CENSUS.DocumentError, ValueError, UnicodeError) as error:
            return {
                "sha256": digest,
                "status": "parse-failure",
                "diagnostic": str(error),
            }

    def github_search(self, key: str, query: str) -> list[dict[str, Any]] | None:
        """Partition a large query by file size, then page every window."""
        return self._github_window(key, query, 0, None)

    def _github_window(
        self, key: str, query: str, lower: int, upper: int | None
    ) -> list[dict[str, Any]] | None:
        previous = [
            row
            for row in jsonl(self.evidence / "queries.jsonl")
            if row.get("source") == "github-code-search"
            and row.get("key") == key
            and row.get("query") == query
        ]
        partition = next(
            (row for row in previous if row.get("outcome") == "partitioned"), None
        )
        if partition:
            found = []
            complete = True
            for child in partition["windows"]:
                part = self._github_window(
                    key, child["query"], child["lower"], child["upper"]
                )
                if part is None:
                    complete = False
                else:
                    found.extend(part)
            return found if complete else None
        answered = [row for row in previous if row.get("outcome") == "answered"]
        if answered and answered[0].get("result_count", 0) > 1000:
            return self._partition_window(
                key, query, lower, upper, answered[0]["result_count"]
            )
        if answered and answered[-1].get("retrieved_total") >= answered[-1].get(
            "result_count"
        ):
            return [item for row in answered for item in row["results"]]
        if answered and answered[-1].get("page_count") == 0:
            if not any(
                row.get("outcome") == "outstanding-index-truncation" for row in previous
            ):
                self.write(
                    "queries.jsonl",
                    {
                        "source": "github-code-search",
                        "key": key,
                        "query": query,
                        "outcome": "outstanding-index-truncation",
                        "reported": answered[-1]["result_count"],
                        "retrieved": answered[-1]["retrieved_total"],
                        "page": answered[-1]["page"],
                    },
                )
            return None
        found = [item for row in answered for item in row["results"]]
        page = len(answered) + 1
        while True:
            path = "/search/code?" + urllib.parse.urlencode(
                {"q": query, "per_page": 100, "page": page}
            )
            try:
                status, payload, _ = self.github_json("code_search", path)
            except OSError as error:
                self.write(
                    "queries.jsonl",
                    {
                        "source": "github-code-search",
                        "key": key,
                        "query": query,
                        "page": page,
                        "outcome": "acquisition-failure",
                        "diagnostic": f"{type(error).__name__}: {error}",
                    },
                )
                raise SearchStopped(
                    f"GitHub code search transport failed for {query!r} page {page}: {error}"
                ) from error
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
                raise SearchStopped(str(error)) from error
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
                raise SearchStopped(
                    f"GitHub refused {query!r} page {page}: HTTP {status}; key {key} outstanding"
                )
            items = payload.get("items", [])
            total = payload.get("total_count", 0)
            if page == 1 and total > 1000:
                return self._partition_window(key, query, lower, upper, total)
            found.extend(items)
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
                    "retrieved_total": len(found),
                    "incomplete_results": payload.get("incomplete_results", False),
                    "results": [
                        {
                            "repository": x["repository"]["full_name"],
                            "path": x["path"],
                            "sha": x["sha"],
                            "url": x["url"],
                            "commit": urllib.parse.parse_qs(
                                urllib.parse.urlsplit(x["url"]).query
                            ).get("ref", [None])[0],
                        }
                        for x in items
                    ],
                },
            )
            if payload.get("incomplete_results"):
                self.write(
                    "queries.jsonl",
                    {
                        "source": "github-code-search",
                        "key": key,
                        "query": query,
                        "outcome": "outstanding-incomplete-results",
                    },
                )
                return None
            if len(found) >= total:
                return found
            if not items:
                self.write(
                    "queries.jsonl",
                    {
                        "source": "github-code-search",
                        "key": key,
                        "query": query,
                        "outcome": "outstanding-index-truncation",
                        "reported": total,
                        "retrieved": len(found),
                        "page": page,
                    },
                )
                return None
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

    def _partition_window(
        self, key: str, query: str, lower: int, upper: int | None, total: int
    ) -> list[dict[str, Any]] | None:
        if upper is not None and lower >= upper:
            self.write(
                "queries.jsonl",
                {
                    "source": "github-code-search",
                    "key": key,
                    "query": query,
                    "outcome": "outstanding-index-cap",
                    "reported": total,
                    "size": lower,
                },
            )
            return None
        midpoint = (
            (lower + upper) // 2
            if upper is not None
            else max(lower + 100000, lower * 2)
        )
        base = re.sub(r" size:[^ ]+", "", query)
        windows = [
            {
                "query": base + f" size:{lower}..{midpoint - 1}",
                "lower": lower,
                "upper": midpoint - 1,
            },
            {
                "query": base
                + (
                    f" size:{midpoint}..{upper}"
                    if upper is not None
                    else f" size:>={midpoint}"
                ),
                "lower": midpoint,
                "upper": upper,
            },
        ]
        self.write(
            "queries.jsonl",
            {
                "source": "github-code-search",
                "key": key,
                "query": query,
                "outcome": "partitioned",
                "reported": total,
                "windows": windows,
            },
        )
        return self._github_window(key, query, lower, upper)

    def sourcegraph_search(self, key: str, query: str) -> list[dict[str, Any]] | None:
        url = (
            self.sourcegraph_url
            + "/.api/search/stream?"
            + urllib.parse.urlencode({"v": "V3", "q": query})
        )
        try:
            status, data = self.sourcegraph_get(url, key, query)
        except OSError as error:
            self.write(
                "queries.jsonl",
                {
                    "source": "sourcegraph",
                    "key": key,
                    "query": query,
                    "outcome": "acquisition-failure",
                    "diagnostic": f"{type(error).__name__}: {error}",
                },
            )
            raise SearchStopped(
                f"Sourcegraph search transport failed for {query!r}: {error}"
            ) from error
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
            raise SearchStopped(str(error)) from error
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

    def sourcegraph_get(self, url: str, key: str, subject: str) -> tuple[int, bytes]:
        """A refusal opens guard backoff; the next attempt waits for it."""
        while True:
            status, data, _ = self.request("sourcegraph", "sourcegraph", url)
            if status not in REFUSAL_STATUSES:
                return status, data
            self.write(
                "refusals.jsonl",
                {
                    "source": "sourcegraph",
                    "key": key,
                    "subject": subject,
                    "status": status,
                    "outcome": "waiting-on-guard",
                },
            )

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
        github_repo = (
            repo.removeprefix("github.com/") if repo.startswith("github.com/") else None
        )
        raw = bool(github_repo and re.fullmatch(r"[0-9a-f]{40}", commit))
        if raw:
            url = (
                self.raw_github_url
                + "/"
                + urllib.parse.quote(github_repo, safe="/")
                + "/"
                + commit
                + "/"
                + urllib.parse.quote(path, safe="/")
            )
            identity["acquisition_route"] = "pinned-raw-github"
        else:
            url = (
                self.sourcegraph_url
                + "/"
                + urllib.parse.quote(repo, safe="/")
                + "/-/raw/"
                + urllib.parse.quote(path, safe="/")
                + "?"
                + urllib.parse.urlencode({"rev": commit})
            )
            identity["acquisition_route"] = "sourcegraph-paced"
        identity["url"] = url
        try:
            if raw:
                status, data = self.raw_github_get(url, key, f"{repo}/{path}@{commit}")
            else:
                status, data = self.sourcegraph_get(url, key, f"{repo}/{path}@{commit}")
        except OSError as error:
            record = {
                **identity,
                "disposition": "acquisition-failure",
                "diagnostic": f"{type(error).__name__}: {error}",
            }
            self.write("candidates.jsonl", record)
            return record
        except SecondaryLimit as error:
            record = {
                **identity,
                "disposition": "acquisition-failure",
                "diagnostic": str(error),
            }
            self.write("candidates.jsonl", record)
            raise SearchStopped(str(error)) from error
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

    def raw_github_get(self, url: str, key: str, subject: str) -> tuple[int, bytes]:
        """The manager-authorized exact-commit raw route has its own paced lane."""
        refusals = 0
        incomplete_reads = 0
        while True:
            if self.raw_last_request is not None:
                duration = self.raw_last_request + RAW_SPACING_S - time.monotonic()
                if duration > 0:
                    self._raw_wait(duration, "spacing", key, subject)
            request = urllib.request.Request(
                url, headers={"User-Agent": "crozier-witness-search"}
            )
            try:
                response = urllib.request.urlopen(request, timeout=90)
            except urllib.error.HTTPError as error:
                response = error
            status = response.status
            self.raw_last_request = time.monotonic()
            try:
                data = response.read()
            except http.client.IncompleteRead as error:
                incomplete_reads += 1
                self.write(
                    "raw-github-calls.jsonl",
                    {
                        "key": key,
                        "subject": subject,
                        "status": "IncompleteRead",
                        "attempt": incomplete_reads,
                        "url": url,
                        "received_bytes": len(error.partial),
                        "missing_bytes": error.expected,
                    },
                )
                if incomplete_reads >= RAW_TRANSFER_ATTEMPT_BUDGET:
                    raise OSError(
                        f"IncompleteRead after {incomplete_reads} attempts: "
                        f"received {len(error.partial)} bytes, missing {error.expected}"
                    ) from error
                self._raw_wait(
                    RAW_BACKOFF_BASE_S * 2 ** (incomplete_reads - 1),
                    "IncompleteRead backoff",
                    key,
                    subject,
                )
                continue
            self.write(
                "raw-github-calls.jsonl",
                {"key": key, "subject": subject, "status": status, "url": url},
            )
            if status not in (429, 503):
                return status, data
            refusals += 1
            if refusals >= 5:
                raise SearchStopped(
                    f"raw GitHub refused {subject} five times (HTTP {status})"
                )
            retry = response.headers.get("Retry-After")
            try:
                retry_seconds = float(retry) if retry is not None else 0.0
            except ValueError:
                stamp = email.utils.parsedate_to_datetime(retry)
                retry_seconds = max(
                    (
                        stamp - datetime.datetime.now(datetime.timezone.utc)
                    ).total_seconds(),
                    0,
                )
            self._raw_wait(
                max(retry_seconds, RAW_BACKOFF_BASE_S * 2 ** (refusals - 1)),
                f"HTTP {status} backoff",
                key,
                subject,
            )

    def _raw_wait(self, duration: float, cause: str, key: str, subject: str) -> None:
        started = time.monotonic()
        time.sleep(duration)
        self.write(
            "raw-github-waits.jsonl",
            {
                "key": key,
                "subject": subject,
                "cause": cause,
                "duration_s": round(time.monotonic() - started, 3),
            },
        )

    def github_document(self, key: str, item: dict[str, Any]) -> dict[str, Any]:
        """Fetch exact result content at its indexed commit, then run the census."""
        identity = {
            "source": "github-code-search",
            "key": key,
            "selector": item["selector"],
            "repository": item["repository"]["full_name"]
            if isinstance(item["repository"], dict)
            else item["repository"],
            "path": item["path"],
            "blob": item["sha"],
            "commit": item.get("commit")
            or urllib.parse.parse_qs(urllib.parse.urlsplit(item["url"]).query).get(
                "ref", [None]
            )[0],
            "url": item["url"],
        }
        url = item["url"]
        if not url.startswith(self.github_url + "/"):
            raise ValueError(f"untrusted GitHub content URL: {url}")
        try:
            status, data, diagnostic = self.github_contents(url[len(self.github_url) :])
        except OSError as error:
            record = {
                **identity,
                "disposition": "acquisition-failure",
                "diagnostic": f"{type(error).__name__}: {error}",
            }
            self.write("candidates.jsonl", record)
            return record
        except SecondaryLimit as error:
            record = {
                **identity,
                "disposition": "acquisition-failure",
                "diagnostic": str(error),
            }
            self.write("candidates.jsonl", record)
            raise SearchStopped(str(error)) from error
        if status != 200 or data is None:
            record = {
                **identity,
                "disposition": "acquisition-failure",
                "status": status,
                "diagnostic": diagnostic,
            }
            self.write("candidates.jsonl", record)
            if status in (403, 429):
                raise SearchStopped(
                    f"GitHub refused contents read for {identity['repository']}/{identity['path']}: HTTP {status}"
                )
            return record
        return self.classify(identity, data)

    def classify(self, identity: dict[str, Any], data: bytes) -> dict[str, Any]:
        """The selector engine is the sole source of a declaration verdict."""
        digest = hashlib.sha256(data).hexdigest()
        suffix = (
            ".json"
            if data.decode("utf-8-sig", "replace").lstrip().startswith(("{", "["))
            else ".yaml"
        )
        cache = self.cache / "documents"
        cache.mkdir(exist_ok=True)
        path = cache / (digest + suffix)
        if not path.exists():
            path.write_bytes(data)
        record = {
            **identity,
            "sha256": digest,
            "document": path.name,
        }
        try:
            parsed = CENSUS.load_document(path)
            if not isinstance(parsed, dict) or not OPENAPI_VERSION.fullmatch(
                str(parsed.get("openapi", ""))
            ):
                record.update(disposition="excluded-non-openapi-3", selector_count=0)
            else:
                selector = identity["selector"]
                if selector == "securityScheme:$ref":
                    schemes = (parsed.get("components") or {}).get(
                        "securitySchemes"
                    ) or {}
                    if not isinstance(schemes, dict):
                        raise ValueError("components.securitySchemes is not a mapping")
                    count = sum(
                        isinstance(value, dict) and isinstance(value.get("$ref"), str)
                        for value in schemes.values()
                    )
                    record.update(
                        disposition="declares" if count else "does-not-declare",
                        selector_count=count,
                        selector_method="parsed security scheme Reference Object; census selector unavailable",
                    )
                elif CENSUS.selector_error(selector) is not None:
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
    parser.add_argument("--cache", type=Path)
    parser.add_argument("--regions", type=Path, default=REPO / "docs/openapi-surface")
    parser.add_argument("--derive-only", action="store_true")
    parser.add_argument(
        "--source",
        choices=("github-code-search", "github-publisher-trees", "sourcegraph"),
    )
    parser.add_argument("--key", action="append", default=[])
    parser.add_argument("--stage", choices=("search", "evaluate", "walk"))
    args = parser.parse_args()
    keys = derive_keys(args.regions)
    args.evidence.mkdir(parents=True, exist_ok=True)
    (args.evidence / "keys.json").write_text(
        json.dumps(
            {
                "source_commit": subprocess.check_output(
                    ["git", "merge-base", "origin/main", "HEAD"], cwd=REPO, text=True
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
    if not args.source or not args.stage:
        parser.error("--source and --stage are required except for --derive-only")
    if (args.source == "github-publisher-trees") != (args.stage == "walk"):
        parser.error(
            "publisher trees require --source github-publisher-trees --stage walk"
        )
    unknown = set(args.key) - set(keys)
    if unknown:
        parser.error(f"unknown key(s): {', '.join(sorted(unknown))}")
    selected = args.key or list(keys)
    if args.source.startswith("github-") and not (
        os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    ):
        os.environ["GH_TOKEN"] = subprocess.check_output(
            ["gh", "auth", "token"], text=True
        ).strip()
    acquirer = Acquirer(args.evidence, cache=args.cache)
    if args.stage == "walk":
        publishers = publisher_set()
        (args.evidence / "publisher-set.json").write_text(
            json.dumps(
                {
                    "derivation": "five wide-scrape publisher trees; link-ok corpus github-raw publisher repositories with root-level openapi.* or swagger.*; publisher-owned declarer repositories recorded in publisher-declarers.tsv",
                    "declarer_exclusions": "Third-party transcriptions and test fixtures are not publisher trees: api-evangelist, JithendraNara/nvidia-nim-unified-skill, APIs-guru/openapi-directory, CommunityToolkit/Datasync, openapi-ts/openapi-typescript. Publishers surfaced only by the sibling registry search await final reconciliation.",
                    "publishers": publishers,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        for publisher in publishers:
            try:
                acquirer.publisher_walk(publisher, keys)
            except (SearchStopped, SecondaryLimit, OSError) as error:
                acquirer.write(
                    "trees.jsonl",
                    {**publisher, "status": "outstanding", "diagnostic": str(error)},
                )
                print(
                    f"witness-search-github: {error}; publisher walk outstanding",
                    file=sys.stderr,
                )
                return 1
        return 0
    if args.stage == "search":
        completed = {
            (row["key"], row["query"])
            for row in jsonl(args.evidence / "queries.jsonl")
            if row.get("source") == args.source
            and row.get("outcome") == "answered"
            and not row.get("incomplete_results")
            and (
                args.source == "sourcegraph"
                or row.get("retrieved_total") >= row.get("result_count")
            )
        }
        for key in selected:
            for query in query_plan(keys[key]["selector"])[args.source]:
                if (key, query) in completed:
                    continue
                if args.source == "github-code-search":
                    try:
                        acquirer.github_search(key, query)
                    except SearchStopped as error:
                        print(
                            f"witness-search-github: {error}; wait for the guard's backoff before resuming",
                            file=sys.stderr,
                        )
                        return 1
                else:
                    try:
                        acquirer.sourcegraph_search(key, query)
                    except SearchStopped as error:
                        print(
                            f"witness-search-github: {error}; source remains outstanding",
                            file=sys.stderr,
                        )
                        return 1
    else:
        queries = [
            row
            for row in jsonl(args.evidence / "queries.jsonl")
            if row.get("source") == args.source
            and row.get("key") in selected
            and row.get("outcome") == "answered"
        ]
        complete = {
            (
                row["key"],
                row["repository"],
                row["path"],
                row.get("commit") or row.get("blob"),
            )
            for row in jsonl(args.evidence / "candidates.jsonl")
            if row.get("disposition") != "acquisition-failure"
        }
        candidates = {}
        for query in queries:
            for item in query["results"]:
                identity = (
                    query["key"],
                    item["repository"],
                    item["path"],
                    item.get("commit")
                    or urllib.parse.parse_qs(
                        urllib.parse.urlsplit(item.get("url", "")).query
                    ).get("ref", [None])[0]
                    or item.get("sha"),
                )
                candidates[identity] = item
        for identity, item in sorted(candidates.items(), key=candidate_priority):
            if identity in complete:
                continue
            key = identity[0]
            selector = keys[key]["selector"]
            try:
                if args.source == "sourcegraph":
                    acquirer.sourcegraph_document(key, selector, item)
                else:
                    acquirer.github_document(key, {**item, "selector": selector})
            except SearchStopped as error:
                print(
                    f"witness-search-github: {error}; source remains outstanding",
                    file=sys.stderr,
                )
                return 1
    return 0


def jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def candidate_priority(
    item: tuple[tuple[str, str, str, str], dict[str, Any]],
) -> tuple[int, str]:
    """Real publisher descriptions before tooling fixtures; no candidate is dropped."""
    identity, _ = item
    repository = identity[1].removeprefix("github.com/").lower()
    path = identity[2].lower()
    penalty = 0
    if repository in registered_github_repos():
        penalty -= 10
    if repository in {"apis-guru/openapi-directory", "jentic/jentic-public-apis"}:
        penalty += 20
    if any(part in path for part in ("/test/", "/tests/", "/fixture/", "/fixtures/")):
        penalty += 10
    if any(
        part in path for part in ("/example/", "/examples/", "/sample/", "/samples/")
    ):
        penalty += 5
    if path.count("/") > 3:
        penalty += 1
    return penalty, "/".join(identity)


@functools.lru_cache(maxsize=1)
def registered_github_repos() -> frozenset[str]:
    """Corpus publisher roots provide a reproducible candidate priority."""
    found = set()
    for line in (
        (REPO / "tests/fixtures/CORPUS.md").read_text(encoding="utf-8").splitlines()
    ):
        if not re.match(r"^\| \d+ \|", line):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 8 or cells[2] != "github-raw":
            continue
        url = urllib.parse.urlsplit(cells[3])
        if url.hostname == "raw.githubusercontent.com":
            found.add("/".join(url.path.strip("/").split("/")[:2]).lower())
    return frozenset(found)


if __name__ == "__main__":
    raise SystemExit(main())
