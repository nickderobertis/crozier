#!/usr/bin/env python3
"""Assemble the combination population search's inputs from what the repository records.

* `identities` writes the acquisition plan `population_screen.py acquire` reads:
  every GitHub code-search and Sourcegraph identity the committed candidate
  ledgers record (repository, full commit, path, SHA-256), less those they record
  as no OpenAPI 3 document, and the handed-off documents whose bytes are not in
  the tree, each ranked by how many of the combination keys its recorded hits
  could witness — the keys whose selector's field names are all among the field
  names of the ledger keys that found it, with a document the ledgers record as
  declaring a nested-pointer shape first.
* `manifest` writes the population manifest `population_screen.py screen` reads:
  every registered corpus row, every OpenAPI document of the pinned APIs.guru
  archive, every handed-off document, and every GitHub or Sourcegraph identity
  whose exact bytes the store holds, each with its licence evidence, the keys the
  earlier named census already lists it for, and — where its bytes could not be
  had — why. Archive documents are copied into the store, by digest, as they are
  read.

Exit status: 0 when it wrote the file; 1 when an input it reads is missing or not
what the repository records; 2 on a usage error.
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
import sys
from collections import defaultdict
from pathlib import Path
from types import ModuleType
from typing import Any

REPO = Path(__file__).resolve().parents[2]
SURFACE = REPO / "docs" / "openapi-surface"
EARLIER = SURFACE / "witness-search-ledger-remainders" / "census.tsv"
HANDED_OFF = REPO / "docs" / "fern-measurements" / "handed-off" / "documents.tsv"
LEDGERS = {"github": "witness-search-github-code-search", "sourcegraph": "witness-search-sourcegraph"}
ARCHIVE_REVISION = "f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49"
ARCHIVE_REPOSITORY = "APIs-guru/openapi-directory"
RAW = "https://raw.githubusercontent.com"
# Ledger keys whose selectors read a nested or `$defs` pointer: a document they
# record as declaring is the likeliest witness of the eight pointer keys.
POINTER_LEDGER_KEYS = re.compile(r"pointer|unnamed-segment|undeclared-component-head")
# Repositories that redistribute other publishers' descriptions: their own licence
# is an aggregation's grant, never a publisher's.
AGGREGATIONS = frozenset({"apis-guru/openapi-directory", "jentic/jentic-public-apis"})
HANDED_OFF_ID = re.compile(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+):(.+)@([0-9a-f]{40})")
EARLIER_POPULATION = {"registered": "registered", "apis-guru": "apis-guru", "handed-off": "handed-off"}


def fail(message: str) -> None:
    raise SystemExit(f"witness-populations-build: {message}")


def _load(name: str, path: Path) -> ModuleType:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(f"cannot load {path}; restore it from git")
        raise AssertionError
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SCREEN = _load("witness_populations_population_screen", Path(__file__).with_name("population_screen.py"))


def ingredients(selector: str) -> set[str]:
    github = _load("witness_populations_github", Path(__file__).with_name("witness-search-github.py"))
    return set(github.ingredients(selector))


def earlier_rows() -> dict[tuple[str, str], set[str]]:
    """`(population, document) -> keys` the earlier named census lists, documents as the new table names them."""
    listed: dict[tuple[str, str], set[str]] = defaultdict(set)
    with EARLIER.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            population = EARLIER_POPULATION[row["source"]]
            listed[
                (population, archive_document(row["document"]) if population == "apis-guru" else row["document"])
            ].add(row["key"])
    return listed


def archive_document(path: str) -> str:
    """`APIs/<provider>[/<service>]/<version>/openapi.yaml` as its provider, service and version."""
    return path.removeprefix("APIs/").rsplit("/", 1)[0]


def ledger_identities(population: str) -> list[dict[str, Any]]:
    """The ledgers' public identities: a full commit and SHA-256, from no repository the exclusion rule names.

    An opaque (screened non-public) identity and an excluded repository's document
    are history the repository rule keeps unfetched, so neither is planned.
    """
    index = _load("witness_populations_index", Path(__file__).with_name("witness-search-github-index.py"))
    rows = []
    for path in sorted((SURFACE / LEDGERS[population]).glob("candidates*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            if not (
                re.fullmatch(r"[0-9a-f]{40}", str(record.get("commit", "")))
                and re.fullmatch(r"[0-9a-f]{64}", str(record.get("sha256", "")))
                and record.get("path")
                and not index.opaque_identity(record["path"])
                and not index.excluded_repository(str(record.get("repository", "")))
            ):
                continue
            rows.append(record)
    return rows


def github_repository(repository: str) -> str | None:
    """`owner/repo` for a GitHub-hosted identity (Sourcegraph names it `github.com/owner/repo`)."""
    name = repository.removeprefix("github.com/")
    return name if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name) else None


def identities(_args: argparse.Namespace) -> list[list[str]]:
    selectors = SCREEN.Selectors.read()
    wanted = {key: ingredients(selector) for key, selector in selectors.by_key.items()}
    out: list[list[str]] = []
    for population in LEDGERS:
        grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for record in ledger_identities(population):
            repository = github_repository(record["repository"])
            if repository is None:
                continue
            grouped[(repository, record["path"])].append(record)
        for (repository, path), records in sorted(grouped.items()):
            if all(record.get("disposition") == "excluded-non-openapi-3" for record in records):
                continue
            # One identity per document: the commit the ledgers read it at last.
            latest = max(records, key=lambda record: (record.get("at", ""), record["commit"]))
            fields = set().union(
                *(ingredients(record.get("selector", "")) for record in records if record.get("selector"))
            )
            matched = sum(1 for need in wanted.values() if need and need <= fields)
            pointer = any(
                record.get("disposition") == "declares" and POINTER_LEDGER_KEYS.search(record.get("key", ""))
                for record in records
            )
            declares = any(record.get("disposition") == "declares" for record in records)
            rank = matched + (100 if pointer else 0) + (10 if declares else 0)
            out.append(
                [
                    population,
                    f"{repository}/{path}",
                    repository,
                    latest["commit"],
                    path,
                    latest["sha256"],
                    latest.get("url", ""),
                    str(rank),
                ]
            )
    with HANDED_OFF.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            match = HANDED_OFF_ID.fullmatch(row["document"])
            if match:
                repository, path, commit = match.groups()
                out.append(["handed-off", row["document"], repository, commit, path, row["sha256"], "", "1000"])
    return out


def jsonl_rows(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def licence_evidence(repository: str, commit: str, digest: str, archived: set[str]) -> str:
    """Where a fetched document's licence is read when it declares no `info.license`.

    An aggregation's repository, or any copy byte-identical to an APIs.guru archive
    document, carries an aggregation's grant, which is no publisher grant.
    """
    if repository.lower() in AGGREGATIONS or digest in archived:
        return f"aggregation:{repository}@{commit}"
    return f"repository:{repository}@{commit}"


def tree_digests() -> dict[str, Path]:
    found = {}
    for path in sorted((REPO / "tests" / "fixtures" / "corpus-sources").rglob("*")):
        if path.is_file():
            found.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(), path)
    return found


def scan(root: Path) -> dict[str, Path]:
    found: dict[str, Path] = {}
    for directory, _dirs, files in os.walk(root):
        for name in sorted(files):
            path = Path(directory) / name
            try:
                if path.stat().st_size <= 50_000_000:
                    found.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(), path)
            except OSError:
                continue
    return found


def manifest(args: argparse.Namespace) -> list[list[str]]:
    store_root = args.store or SCREEN.cache_root()
    listed = earlier_rows()
    entries: list[list[str]] = []

    def keys(population: str, document: str) -> str:
        return ";".join(sorted(listed.pop((population, document), set()))) or "-"

    corpus = SCREEN.corpus_rows()
    grants = {name: row.grant for name, row in corpus.items()}
    for name, path in sorted(SCREEN.registered_files().items()):
        if name not in grants or not path.is_file():
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        kind = "corpus-aggregation" if SCREEN.aggregator(corpus[name].source) else "corpus"
        entries.append(
            ["registered", name, "-", digest, f"{kind}:{grants[name] or '-'}", keys("registered", name), "-"]
        )
    archive = args.archive / "APIs"
    if not archive.is_dir():
        fail(f"{archive} is no directory; pass --archive the extracted openapi-directory tree at {ARCHIVE_REVISION}")
    for path in sorted(archive.rglob("openapi.*")):
        if path.suffix not in (".yaml", ".yml", ".json"):
            continue
        data = path.read_bytes()
        SCREEN.store(data, store_root)
        relative = path.relative_to(args.archive).as_posix()
        document = archive_document(relative)
        source = f"{RAW}/{ARCHIVE_REPOSITORY}/{ARCHIVE_REVISION}/{relative}"
        entries.append(
            [
                "apis-guru",
                document,
                source,
                hashlib.sha256(data).hexdigest(),
                "no-publisher-grant",
                keys("apis-guru", document),
                "-",
            ]
        )
    archived = {entry[3] for entry in entries if entry[0] == "apis-guru"}
    tree = tree_digests()
    preflight = scan(args.preflight) if args.preflight.is_dir() else {}
    with HANDED_OFF.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            digest, document = row["sha256"], row["document"]
            match = HANDED_OFF_ID.fullmatch(document)
            for found in (tree.get(digest), preflight.get(digest)):
                if found is not None and SCREEN.cached(digest, store_root) is None:
                    SCREEN.store(found.read_bytes(), store_root)
            forced = keys("handed-off", document)
            if match is None:
                # No recorded provenance names an immutable source for these bytes.
                if forced != "-":
                    fail(
                        f"handed-off {document!r} is listed for {forced} but records no source; restore its provenance"
                    )
                continue
            repository, path, commit = match.groups()
            source = f"{RAW}/{repository}/{commit}/{path}"
            have = SCREEN.cached(digest, store_root) is not None
            entries.append(
                [
                    "handed-off",
                    document,
                    source,
                    digest,
                    licence_evidence(repository, commit, digest, archived),
                    forced,
                    "-"
                    if have
                    else "not in the tree, the preflight cache or the response cache, and the raw lane did not return these bytes",
                ]
            )
    plan = [identity for path in args.identities if path.is_file() for identity in SCREEN.read_identities(path)]
    # A code-search hit is planned by its blob; the acquisition ledger records the content digest it was had at.
    contents = {
        (row["population"], row["document"]): row.get("content_sha256", row["sha256"])
        for row in jsonl_rows(args.acquisitions)
        if row.get("how") in ("raw", "store", "shared-cache")
    }
    seen: set[tuple[str, str]] = set()
    for identity in plan:
        digest = contents.get((identity.population, identity.document), identity.sha256)
        if (
            identity.population not in LEDGERS
            or (identity.population, identity.document) in seen
            or not SCREEN.SHA.fullmatch(digest)
            or SCREEN.cached(digest, store_root) is None
        ):
            continue
        seen.add((identity.population, identity.document))
        source = f"{RAW}/{identity.repository}/{identity.commit}/{identity.path}"
        entries.append(
            [
                identity.population,
                identity.document,
                source,
                digest,
                licence_evidence(identity.repository, identity.commit, digest, archived),
                "-",
                "-",
            ]
        )
    if listed:
        fail(f"the earlier named census lists candidates no population names: {sorted(listed)[:5]}")
    # A handed-off document without its bytes owes rows only for keys an earlier census lists it for.
    return [entry for entry in entries if entry[6] == "-" or entry[5] != "-"]


def recorded_queries(evidence: Path) -> list[dict[str, Any]]:
    """The search's recorded answers: its live `queries.jsonl`, or the `queries.jsonl.gz` it is committed as."""
    packed = evidence / "queries.jsonl.gz"
    if not (evidence / "queries.jsonl").is_file() and packed.is_file():
        with gzip.open(packed, "rt", encoding="utf-8") as handle:
            return [json.loads(line) for line in handle if line.strip()]
    github = _load("witness_populations_github", Path(__file__).with_name("witness-search-github.py"))
    return github.jsonl(evidence / "queries.jsonl")


def search(args: argparse.Namespace) -> list[list[str]]:
    """The bounded live search: page 1 of each key's YAML and JSON code-search queries, and one Sourcegraph query.

    Every request goes through the acquirer's guarded lanes (`rate_limit_guard.py`
    pacing and floor, the shared response cache), which log it under `--evidence`.
    A hit is planned by its git blob; one already planned by content is left out.
    """
    github = _load("witness_populations_github", Path(__file__).with_name("witness-search-github.py"))
    selectors = SCREEN.Selectors.read()
    acquirer = github.Acquirer(args.evidence, cache=SCREEN.cache_root() / "acquirer", first_page_only=True)
    known = {(row.repository, row.path) for row in SCREEN.read_identities(args.identities)}
    hits: dict[tuple[str, str], list[str]] = {}
    for key, selector in selectors.by_key.items() if not args.replay else ():
        try:
            plan = github.query_plan(selector)["github-code-search"]
        except ValueError as error:
            # An operation-level selector names no schema field a code search can spell.
            acquirer.write(
                "queries.jsonl",
                {
                    "source": "github-code-search",
                    "key": key,
                    "query": selector,
                    "outcome": "not-queryable",
                    "diagnostic": str(error),
                },
            )
            continue
        # The plan's last two queries are its `path:openapi` YAML and JSON spellings.
        for query in plan[-2:]:
            try:
                acquirer.github_search(key, query)
            except github.SearchStopped as error:
                print(f"witness-populations-build: search stopped: {error}", file=sys.stderr)
                break
    wanted = {key: ingredients(selector) for key, selector in selectors.by_key.items()}
    for row in recorded_queries(args.evidence):
        # Ranked as the ledger plan is: the keys whose field names the query that found it spells.
        found_by = wanted.get(str(row.get("key")), set())
        rank = str(sum(1 for need in wanted.values() if need and need <= found_by))
        for item in row.get("results", []) if row.get("source") == "github-code-search" else []:
            identity = (item.get("repository"), item.get("path"))
            commit, blob = item.get("commit"), item.get("sha")
            if (
                identity in known
                or not re.fullmatch(r"[0-9a-f]{40}", str(commit))
                or not re.fullmatch(r"[0-9a-f]{40}", str(blob))
            ):
                continue
            hits.setdefault(
                identity,
                [
                    "github",
                    f"{identity[0]}/{identity[1]}",
                    identity[0],
                    commit,
                    identity[1],
                    f"blob:{blob}",
                    item.get("url", ""),
                    rank,
                ],
            )
    # One anonymous Sourcegraph request in all: a recorded answer or refusal is not asked again.
    if args.replay or any(row.get("source") == "sourcegraph" for row in recorded_queries(args.evidence)):
        return sorted(hits.values())
    sourcegraph = github.query_plan(selectors.by_key[args.sourcegraph_key])["sourcegraph"][0]
    try:
        acquirer.sourcegraph_search(args.sourcegraph_key, sourcegraph)
    except github.SearchStopped as error:
        print(f"witness-populations-build: sourcegraph: {error}", file=sys.stderr)
    return sorted(hits.values())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="command", required=True)
    plan = sub.add_parser("identities")
    plan.add_argument("--output", type=Path, required=True)
    build = sub.add_parser("manifest")
    build.add_argument("--output", type=Path, default=SCREEN.POPULATION)
    build.add_argument(
        "--identities", type=Path, action="append", required=True, help="an acquisition plan; repeatable"
    )
    build.add_argument("--acquisitions", type=Path, default=SCREEN.RECORD / "acquisition" / "acquisitions.jsonl")
    build.add_argument("--archive", type=Path, required=True, help="the extracted openapi-directory tree")
    build.add_argument("--preflight", type=Path, default=SCREEN.cache_root().parent / "remaining-witness-preflight")
    build.add_argument("--store", type=Path)
    live = sub.add_parser("search")
    live.add_argument("--evidence", type=Path, required=True)
    live.add_argument(
        "--identities", type=Path, required=True, help="the ledger plan, whose identities are not repeated"
    )
    live.add_argument("--output", type=Path, required=True)
    live.add_argument("--sourcegraph-key", default="combo-property-defs-pointer")
    live.add_argument(
        "--replay", action="store_true", help="derive identities from the recorded answers, asking nothing"
    )
    args = parser.parse_args(argv)
    if args.command == "search":
        if not args.replay and (args.evidence / "queries.jsonl.gz").is_file():
            parser.error("the search's answers are committed packed; gunzip queries.jsonl.gz to resume it live")
        rows = search(args)
        with args.output.open("w", encoding="utf-8", newline="") as handle:
            handle.write("\t".join(SCREEN.IDENTITY_COLUMNS) + "\n")
            handle.writelines("\t".join(row) + "\n" for row in rows)
        print(f"witness-populations-build: {len(rows)} new code-search identities")
        return 0
    if args.command == "identities":
        rows = identities(args)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with (
            gzip.open(args.output, "wt", encoding="utf-8", newline="")
            if args.output.suffix == ".gz"
            else args.output.open("w", encoding="utf-8", newline="")
        ) as handle:
            handle.write("\t".join(SCREEN.IDENTITY_COLUMNS) + "\n")
            handle.writelines("\t".join(row) + "\n" for row in rows)
        print(f"witness-populations-build: {len(rows)} identities")
        return 0
    rows = manifest(args)
    SCREEN.write_manifest(args.output, [SCREEN.Entry(*row) for row in rows])
    print(f"witness-populations-build: {len(rows)} manifest entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
