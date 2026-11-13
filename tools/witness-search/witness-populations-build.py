#!/usr/bin/env python3
"""Assemble the combination population search's inputs from what the repository records.

* `identities` writes the acquisition plan `population_screen.py acquire` reads:
  every GitHub code-search and Sourcegraph identity the committed candidate
  ledgers record (repository, full commit, path, SHA-256), less those they record
  as no OpenAPI 3 document, and the handed-off documents
  `docs/fern-measurements/handed-off/documents.tsv` names by repository, path and
  commit, each ranked by how many of the combination keys its recorded hits could
  witness: the keys whose selector's field names are all among the field names of
  the ledger keys that found it, with a document the ledgers record as declaring a
  nested-pointer shape first.
* `search` runs the bounded live search (page 1 of each key's YAML and JSON
  code-search queries, and one Sourcegraph query) through the guarded lanes and
  plans its new hits by their git blob; `--replay` derives them from the recorded
  answers and asks nothing.
* `manifest` writes the population manifest `population_screen.py screen` reads:
  every registered corpus row, every OpenAPI document of the pinned APIs.guru
  archive (each held to the digest the committed acquisition manifest records),
  every handed-off document, and every planned identity whose exact bytes the
  store holds, each with its licence evidence, the keys the earlier named census
  already lists it for, and, where its bytes could not be had, why.

Every path is read under `--root` (the repository by default).

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
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from types import ModuleType
from typing import NamedTuple, NoReturn

REPO = Path(__file__).resolve().parents[2]
LEDGERS = {"github": "witness-search-github-code-search", "sourcegraph": "witness-search-sourcegraph"}
ARCHIVE_REVISION = "f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49"
ARCHIVE_REPOSITORY = "APIs-guru/openapi-directory"
RAW = "https://raw.githubusercontent.com"
# The archive's OpenAPI documents, as the directory names them.
ARCHIVE_NAMES = ("openapi.yaml", "openapi.yml", "openapi.json")
# Ledger keys whose selectors read a nested or `$defs` pointer: a document they
# record as declaring is the likeliest witness of the eight pointer keys.
POINTER_LEDGER_KEYS = re.compile(r"pointer|unnamed-segment|undeclared-component-head")
HANDED_OFF_ID = re.compile(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+):(.+)@([0-9a-f]{40})")
EARLIER_POPULATION = {"registered": "registered", "apis-guru": "apis-guru", "handed-off": "handed-off"}
HANDED_OFF_UNFETCHED = (
    "not in the tree, the preflight cache or the response cache, and the raw lane did not return these bytes"
)


def fail(message: str) -> NoReturn:
    raise SystemExit(f"witness-populations-build: {message}")


def _load(name: str, path: Path) -> ModuleType:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(f"cannot load {path}; restore it from git")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SCREEN = _load("witness_populations_population_screen", Path(__file__).with_name("population_screen.py"))


def github() -> ModuleType:
    return _load("witness_populations_github", Path(__file__).with_name("witness-search-github.py"))


@dataclass(frozen=True)
class Tree:
    """The repository files the search reads, under one root."""

    root: Path

    @property
    def surface(self) -> Path:
        return self.root / "docs" / "openapi-surface"

    @property
    def earlier(self) -> Path:
        return self.surface / "witness-search-ledger-remainders" / "census.tsv"

    @property
    def handed_off(self) -> Path:
        return self.root / "docs" / "fern-measurements" / "handed-off" / "documents.tsv"

    @property
    def archive_manifest(self) -> Path:
        return self.surface / "witness-search-apis.guru" / "acquisition-manifest.tsv"

    def selectors(self) -> SCREEN.Selectors:
        return SCREEN.Selectors.read(self.surface / "witness-search-keys.tsv")


def ingredients(selector: str) -> set[str]:
    return set(github().ingredients(selector))


def archive_document(path: str) -> str:
    """`APIs/<provider>[/<service>]/<version>/openapi.yaml` as its provider, service and version."""
    return path.removeprefix("APIs/").rsplit("/", 1)[0]


def earlier_rows(tree: Tree) -> dict[tuple[str, str], set[str]]:
    """`(population, document) -> keys` the earlier named census lists, documents as the new table names them."""
    listed: dict[tuple[str, str], set[str]] = defaultdict(set)
    with tree.earlier.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            population = EARLIER_POPULATION.get(row["source"])
            if population is None:
                fail(f"{tree.earlier}: source {row['source']!r} is none of {', '.join(EARLIER_POPULATION)}")
            document = archive_document(row["document"]) if population == "apis-guru" else row["document"]
            listed[(population, document)].add(row["key"])
    return listed


class LedgerRecord(NamedTuple):
    """One candidate-ledger line the plan reads: a public identity and the ledger key that found it."""

    repository: str
    path: str
    commit: str
    sha256: str
    key: str
    selector: str
    disposition: str
    at: str
    url: str


def ledger_identities(tree: Tree, population: str) -> list[LedgerRecord]:
    """The ledgers' public identities: a full commit and SHA-256, from no repository the exclusion rule names.

    An opaque (screened non-public) identity and an excluded repository's document
    are history the repository rule keeps unfetched, so neither is planned.
    """
    index = _load("witness_populations_index", Path(__file__).with_name("witness-search-github-index.py"))
    rows = []
    for path in sorted((tree.surface / LEDGERS[population]).glob("candidates*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            if not (
                isinstance(record, dict)
                and re.fullmatch(r"[0-9a-f]{40}", str(record.get("commit", "")))
                and re.fullmatch(r"[0-9a-f]{64}", str(record.get("sha256", "")))
                and isinstance(record.get("path"), str)
                and not index.opaque_identity(record["path"])
                and not index.excluded_repository(str(record.get("repository", "")))
            ):
                continue
            rows.append(
                LedgerRecord(
                    str(record.get("repository", "")),
                    record["path"],
                    record["commit"],
                    record["sha256"],
                    str(record.get("key", "")),
                    str(record.get("selector", "")),
                    str(record.get("disposition", "")),
                    str(record.get("at", "")),
                    str(record.get("url", "")),
                )
            )
    return rows


def github_repository(repository: str) -> str | None:
    """`owner/repo` for a GitHub-hosted identity (Sourcegraph names it `github.com/owner/repo`)."""
    name = repository.removeprefix("github.com/")
    return name if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name) else None


def identities(tree: Tree) -> list[SCREEN.Identity]:
    wanted = {key: ingredients(selector) for key, selector in tree.selectors().by_key.items()}
    out = []
    for population in LEDGERS:
        grouped: dict[tuple[str, str], list[LedgerRecord]] = defaultdict(list)
        for record in ledger_identities(tree, population):
            repository = github_repository(record.repository)
            if repository is not None and SCREEN.witness_screen().repository_path(record.path):
                grouped[(repository, record.path)].append(record)
        for (repository, path), records in sorted(grouped.items()):
            if all(record.disposition == "excluded-non-openapi-3" for record in records):
                continue
            # One identity per document: the commit the ledgers read it at last.
            latest = max(records, key=lambda record: (record.at, record.commit))
            fields = set().union(*(ingredients(record.selector) for record in records if record.selector))
            matched = sum(1 for need in wanted.values() if need and need <= fields)
            pointer = any(
                record.disposition == "declares" and POINTER_LEDGER_KEYS.search(record.key) for record in records
            )
            declares = any(record.disposition == "declares" for record in records)
            rank = matched + (100 if pointer else 0) + (10 if declares else 0)
            out.append(
                SCREEN.Identity(
                    population,
                    f"{repository}/{path}",
                    repository,
                    latest.commit,
                    path,
                    latest.sha256,
                    latest.url,
                    rank,
                )
            )
    for row, provenance in handed_off(tree):
        if provenance is not None:
            repository, path, commit = provenance
            out.append(
                SCREEN.Identity("handed-off", row["document"], repository, commit, path, row["sha256"], "", 1000)
            )
    return out


def handed_off(tree: Tree) -> list[tuple[dict[str, str], tuple[str, str, str] | None]]:
    """Each handed-off document with its `(repository, path, commit)`, or None where it records no provenance.

    A row naming a provenance must name a real one: an `owner/name` repository, a
    path inside it and a full commit, beside the SHA-256 of the bytes handed off.
    """
    rows = []
    with tree.handed_off.open(encoding="utf-8", newline="") as handle:
        for number, row in enumerate(csv.DictReader(handle, delimiter="\t"), 2):
            if not SCREEN.SHA.fullmatch(row.get("sha256") or ""):
                fail(f"{tree.handed_off}:{number} names no SHA-256 of its bytes; restore it from git")
            match = HANDED_OFF_ID.fullmatch(row.get("document") or "")
            if match is None:
                rows.append((row, None))
                continue
            repository, path, commit = match.groups()
            if not SCREEN.witness_screen().repository_name(repository) or not SCREEN.witness_screen().repository_path(
                path
            ):
                fail(f"{tree.handed_off}:{number}: {row['document']!r} is no repository, path and commit; restore it")
            rows.append((row, (repository, path, commit)))
    return rows


class Acquisition(NamedTuple):
    """One line of the acquisition ledger: a planned identity, how its bytes were had, and their digest."""

    population: str
    document: str
    commit: str
    pin: str
    how: str
    content_sha256: str

    @property
    def held(self) -> bool:
        return self.how in SCREEN.HELD


def acquisitions(path: Path) -> list[Acquisition]:
    """The acquisition ledger's records; a missing ledger is an acquisition never run."""
    if not path.is_file():
        return []
    out = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        row = json.loads(line) if line.strip() else None
        # Earlier ledger lines name the pin `sha256`, as the plan's column was then called.
        pin = row.get("pin", row.get("sha256")) if isinstance(row, dict) else None
        digest = row.get("content_sha256", pin) if isinstance(row, dict) else None
        if (
            not isinstance(row, dict)
            or not all(isinstance(row.get(field), str) for field in ("population", "document", "commit", "how"))
            or not re.fullmatch(r"[0-9a-f]{40}", row["commit"])
            or not isinstance(pin, str)
            or not (SCREEN.SHA.fullmatch(pin) or SCREEN.BLOB.fullmatch(pin))
            or not isinstance(digest, str)
            or not (SCREEN.SHA.fullmatch(digest) or SCREEN.BLOB.fullmatch(digest))
            or not SCREEN.acquisition_outcome(row["how"])
        ):
            fail(
                f"{path}:{number} is no acquisition record (population, document, commit, pin, how); "
                "restore it from git"
            )
        out.append(Acquisition(row["population"], row["document"], row["commit"], pin, row["how"], digest))
    return out


def licence_evidence(repository: str, commit: str, digest: str, archived: set[str]) -> str:
    """Where a fetched document's licence is read when it declares no `info.license`.

    An aggregation's repository, or any copy byte-identical to an APIs.guru archive
    document, carries an aggregation's grant, which is no publisher grant.
    """
    if SCREEN.is_aggregation(repository) or digest in archived:
        return f"aggregation:{repository}@{commit}"
    return f"repository:{repository}@{commit}"


def tree_digests(tree: Tree) -> dict[str, Path]:
    found = {}
    for path in sorted((tree.root / "tests" / "fixtures" / "corpus-sources").rglob("*")):
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


def archive_digests(tree: Tree) -> dict[str, str]:
    """Each archive document's SHA-256, as the committed acquisition manifest records it at the pinned revision."""
    with tree.archive_manifest.open(encoding="utf-8", newline="") as handle:
        return {
            row["document"]: row["sha256"]
            for row in csv.DictReader(handle, delimiter="\t")
            if row["walk"] == ARCHIVE_REPOSITORY and row["revision"] == ARCHIVE_REVISION
        }


def manifest(tree: Tree, args: argparse.Namespace) -> list[SCREEN.Entry]:
    store_root = args.store or SCREEN.cache_root()
    listed = earlier_rows(tree)
    entries = []

    def keys(population: str, document: str) -> str:
        return ";".join(sorted(listed.pop((population, document), set()))) or "-"

    corpus = SCREEN.corpus_rows(tree.root)
    for name, path in sorted(SCREEN.registered_files(tree.root).items()):
        if name not in corpus or not path.is_file():
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        kind = "corpus-aggregation" if SCREEN.aggregator(corpus[name].source) else "corpus"
        entries.append(
            SCREEN.Entry(
                "registered", name, "-", digest, f"{kind}:{corpus[name].grant or '-'}", keys("registered", name), "-"
            )
        )
    archive = args.archive / "APIs"
    if not archive.is_dir():
        fail(f"{archive} is no directory; pass --archive the extracted openapi-directory tree at {ARCHIVE_REVISION}")
    recorded = archive_digests(tree)
    expected = {document for document in recorded if PurePosixPath(document).name in ARCHIVE_NAMES}
    found = {path.relative_to(args.archive).as_posix() for path in archive.rglob("openapi.*")}
    if expected - found:
        fail(
            f"{args.archive} lacks {len(expected - found)} of the {len(expected)} OpenAPI documents "
            f"{tree.archive_manifest} records (first: {sorted(expected - found)[0]}); extract the pinned archive again"
        )
    for path in sorted(archive.rglob("openapi.*")):
        if path.name not in ARCHIVE_NAMES:
            continue
        data = path.read_bytes()
        relative = path.relative_to(args.archive).as_posix()
        digest = hashlib.sha256(data).hexdigest()
        if recorded.get(relative) != digest:
            fail(
                f"{path} carries sha256 {digest}, and {tree.archive_manifest} records "
                f"{recorded.get(relative, 'no such document')} at {ARCHIVE_REVISION}; extract the pinned archive again"
            )
        SCREEN.store(data, store_root)
        document = archive_document(relative)
        entries.append(
            SCREEN.Entry(
                "apis-guru",
                document,
                f"{RAW}/{ARCHIVE_REPOSITORY}/{ARCHIVE_REVISION}/{relative}",
                digest,
                "no-publisher-grant",
                keys("apis-guru", document),
                "-",
            )
        )
    archived = {entry.sha256 for entry in entries if entry.population == "apis-guru"}
    held = tree_digests(tree)
    preflight = scan(args.preflight) if args.preflight.is_dir() else {}
    for row, provenance in handed_off(tree):
        digest, document = row["sha256"], row["document"]
        for found in (held.get(digest), preflight.get(digest)):
            if found is not None and SCREEN.cached(digest, store_root) is None:
                SCREEN.store(found.read_bytes(), store_root)
        forced = keys("handed-off", document)
        if provenance is None:
            # No recorded provenance names an immutable source for these bytes.
            if forced != "-":
                fail(f"handed-off {document!r} is listed for {forced} but records no source; restore its provenance")
            continue
        repository, path, commit = provenance
        have = SCREEN.cached(digest, store_root) is not None
        entries.append(
            SCREEN.Entry(
                "handed-off",
                document,
                f"{RAW}/{repository}/{commit}/{path}",
                digest,
                licence_evidence(repository, commit, digest, archived),
                forced,
                "-" if have else HANDED_OFF_UNFETCHED,
            )
        )
    missing = [str(path) for path in args.identities if not path.is_file()]
    if missing:
        fail(f"--identities {', '.join(missing)} is no file; pass the acquisition plans the manifest is built from")
    plan = [identity for path in args.identities for identity in SCREEN.read_identities(path)]
    # A code-search hit is planned by its blob, and the acquisition ledger records the content digest it was
    # had at. Bytes are attributed to a planned identity only where the ledger read it at that commit and pin.
    contents = {
        (row.population, row.document, row.commit, row.pin): row.content_sha256
        for row in acquisitions(args.acquisitions)
        if row.held
    }
    seen: set[tuple[str, str]] = set()
    for identity in plan:
        digest = contents.get(
            (identity.population, identity.document, identity.commit, identity.pin),
            identity.content_digest() or "",
        )
        if (
            identity.population not in LEDGERS
            or (identity.population, identity.document) in seen
            or not SCREEN.SHA.fullmatch(digest)
            or SCREEN.cached(digest, store_root) is None
        ):
            continue
        seen.add((identity.population, identity.document))
        entries.append(
            SCREEN.Entry(
                identity.population,
                identity.document,
                f"{RAW}/{identity.repository}/{identity.commit}/{identity.path}",
                digest,
                licence_evidence(identity.repository, identity.commit, digest, archived),
                "-",
                "-",
            )
        )
    if listed:
        fail(f"the earlier named census lists candidates no population names: {sorted(listed)[:5]}")
    # A handed-off document without its bytes owes rows only for keys an earlier census lists it for.
    return [entry for entry in entries if entry.unfetchable == "-" or entry.keys != "-"]


class CodeHit(NamedTuple):
    """One file a code search answered with: where it is, at which commit, and its git blob."""

    repository: str
    path: str
    commit: str
    blob: str
    url: str


class RecordedQuery(NamedTuple):
    """One recorded query: who answered it, for which key, how, and the files it named."""

    source: str
    key: str
    outcome: str
    hits: tuple[CodeHit, ...]


# Who answers the search's queries, and the outcomes the guarded acquirer records for one.
QUERY_SOURCES = ("github-code-search", "sourcegraph")
QUERY_OUTCOME = re.compile(
    r"answered|partitioned|refused|not-queryable|incomplete-stream|acquisition-failure|secondary-limiter"
    r"|outstanding-[a-z-]+"
)


def recorded_queries(evidence: Path) -> list[RecordedQuery]:
    """The search's recorded answers: its live `queries.jsonl`, or the `queries.jsonl.gz` it is committed as."""
    packed = evidence / "queries.jsonl.gz"
    if not (evidence / "queries.jsonl").is_file() and packed.is_file():
        with gzip.open(packed, "rt", encoding="utf-8") as handle:
            rows = [json.loads(line) for line in handle if line.strip()]
    else:
        rows = github().jsonl(evidence / "queries.jsonl")
    for number, row in enumerate(rows, 1):
        results = row.get("results", []) if isinstance(row, dict) else None
        if (
            not isinstance(row, dict)
            or row.get("source") not in QUERY_SOURCES
            or row.get("key") not in SCREEN.KEYS
            or not QUERY_OUTCOME.fullmatch(str(row.get("outcome", "")))
            or not isinstance(results, list)
            or not all(isinstance(item, dict) for item in results)
        ):
            fail(f"{evidence}: query record {number} is no recorded query with a list of results; restore it from git")
    return [
        RecordedQuery(
            row["source"],
            str(row.get("key", "")),
            str(row.get("outcome", "")),
            tuple(
                CodeHit(
                    str(item.get("repository")),
                    str(item.get("path")),
                    str(item.get("commit")),
                    str(item.get("sha")),
                    str(item.get("url", "")),
                )
                for item in row.get("results", [])
            ),
        )
        for row in rows
    ]


def search(tree: Tree, args: argparse.Namespace) -> list[SCREEN.Identity]:
    """The bounded live search's new identities; see the module docstring."""
    selectors = tree.selectors()
    known = {(row.repository, row.path) for row in SCREEN.read_identities(args.identities)}
    if not args.replay:
        client = github()
        acquirer = client.Acquirer(
            args.evidence,
            cache=SCREEN.cache_root() / "acquirer",
            first_page_only=True,
            sourcegraph_url=client.checked_service_url(
                os.environ.get("CROZIER_SOURCEGRAPH_URL", client.SOURCEGRAPH_URL),
                "CROZIER_SOURCEGRAPH_URL",
                "sourcegraph.com",
            ),
        )
        for key, selector in selectors.by_key.items():
            if args.key and key not in args.key:
                continue
            try:
                plan = client.query_plan(selector)["github-code-search"]
            except ValueError as error:
                # An operation-level selector names no schema field a code search can spell.
                if not any(row.key == key for row in recorded_queries(args.evidence)):
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
            # Only page 1 of the `path:openapi` spellings (YAML and JSON): the broadest document-location queries,
            # which bound the pass to two requests a key against the code-search bucket's 10 a minute.
            for query in [query for query in plan if "path:openapi" in query.split()]:
                try:
                    # llmlint: ignore[async_typed_clients_at_boundaries] AGENTS.md keeps the witness tooling stdlib-only and synchronous so it runs installless; the guard admits one code-search request at a time to its paced bucket, which an async client would not speed up.
                    acquirer.github_search(key, query)
                except client.SearchStopped as error:
                    print(f"witness-populations-build: search stopped: {error}", file=sys.stderr)
                    break
        # One anonymous Sourcegraph request in all, for `--sourcegraph-key` when the search covers it:
        # a recorded answer or refusal is not asked again.
        covered = not args.key or args.sourcegraph_key in args.key
        if covered and not any(row.source == "sourcegraph" for row in recorded_queries(args.evidence)):
            query = client.query_plan(selectors.by_key[args.sourcegraph_key])["sourcegraph"][0]
            try:
                # llmlint: ignore[async_typed_clients_at_boundaries] AGENTS.md keeps the witness tooling stdlib-only and synchronous so it runs installless; this is the search's one Sourcegraph request, through the guard's paced lane.
                acquirer.sourcegraph_search(args.sourcegraph_key, query)
            except client.SearchStopped as error:
                print(f"witness-populations-build: sourcegraph: {error}", file=sys.stderr)
    wanted = {key: ingredients(selector) for key, selector in selectors.by_key.items()}
    hits: dict[tuple[str, str], SCREEN.Identity] = {}
    for row in recorded_queries(args.evidence):
        # Ranked as the ledger plan is: the keys whose field names the query that found it spells.
        found_by = wanted.get(row.key, set())
        rank = sum(1 for need in wanted.values() if need and need <= found_by)
        for repository, path, commit, blob, url in row.hits if row.source == "github-code-search" else ():
            if (
                (repository, path) in known
                or not re.fullmatch(r"[0-9a-f]{40}", commit)
                or not re.fullmatch(r"[0-9a-f]{40}", blob)
                or not SCREEN.witness_screen().repository_name(repository)
                or not SCREEN.witness_screen().repository_path(path)
            ):
                continue
            hits.setdefault(
                (repository, path),
                SCREEN.Identity(
                    "github",
                    f"{repository}/{path}",
                    repository,
                    commit,
                    path,
                    f"blob:{blob}",
                    url,
                    rank,
                ),
            )
    return sorted(hits.values())


def write_plan(path: Path, rows: list[SCREEN.Identity]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\t".join(SCREEN.IDENTITY_COLUMNS) + "\n" + "".join("\t".join(map(str, row)) + "\n" for row in rows)
    if path.suffix == ".gz":
        path.write_bytes(gzip.compress(text.encode("utf-8"), mtime=0))
    else:
        path.write_text(text, encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--root", type=Path, default=REPO, help="the repository whose records are read")
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
    live.add_argument("--sourcegraph-key", default="combo-property-defs-pointer", choices=SCREEN.KEYS)
    live.add_argument(
        "--key",
        action="append",
        default=[],
        choices=SCREEN.KEYS,
        help="search only these keys (the Sourcegraph query only when --sourcegraph-key is one of them)",
    )
    live.add_argument(
        "--replay", action="store_true", help="derive identities from the recorded answers, asking nothing"
    )
    args = parser.parse_args(argv)
    tree = Tree(args.root)
    match args.command:
        case "search":
            if not args.replay and (args.evidence / "queries.jsonl.gz").is_file():
                parser.error("the search's answers are committed packed; gunzip queries.jsonl.gz to resume it live")
            rows = search(tree, args)
            write_plan(args.output, rows)
            print(f"witness-populations-build: {len(rows)} new code-search identities")
        case "identities":
            rows = identities(tree)
            write_plan(args.output, rows)
            print(f"witness-populations-build: {len(rows)} identities")
        case _:
            rows = manifest(tree, args)
            SCREEN.write_manifest(args.output, rows)
            print(f"witness-populations-build: {len(rows)} manifest entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
