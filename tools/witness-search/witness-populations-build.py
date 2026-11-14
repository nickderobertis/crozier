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
* `census` writes the acquisition plan of every GitHub and Sourcegraph document
  the earlier named censuses list for a combination key (the ledger-remainders
  census and the earlier combination searches' censuses), at the commit and
  SHA-256 the census read it at.
* `search` runs the bounded live search (page 1 of each key's YAML and JSON
  code-search queries, and one Sourcegraph query) through the guarded lanes and
  plans its new hits by their git blob; `--replay` derives them from the recorded
  answers and asks nothing.
* `manifest` writes the population manifest `population_screen.py screen` reads:
  every registered corpus row, every OpenAPI document of the pinned APIs.guru
  archive (each held to the digest the committed acquisition manifest records),
  every handed-off document, and every planned identity whose exact bytes the
  store holds, each with its licence evidence, the keys the earlier named
  censuses already list it for, and, where its bytes could not be had, why. Every
  candidate those censuses list is an entry: one they name by SHA-256 alone
  takes the bytes held under that digest, or is a `sha256:<hex>` entry; only a
  hand-written fixture, which is no real-API candidate, owes none.

Every path is read under `--root` (the repository by default).

Exit status: 0 when it wrote the file; 1 when an input it reads is missing or not
what the repository records; 2 on a usage error.
"""

from __future__ import annotations

import argparse
import csv
import functools
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


@functools.cache
def selector_fields(selector: str) -> frozenset[str]:
    """A selector's field names, read once per selector: the ledgers repeat a few selectors many times."""
    return frozenset(github().ingredients(selector))


def ingredients(selector: str) -> set[str]:
    return set(selector_fields(selector))


def archive_document(path: str) -> str:
    """`APIs/<provider>[/<service>]/<version>/openapi.yaml` as its provider, service and version."""
    return path.removeprefix("APIs/").rsplit("/", 1)[0]


def earlier_rows(tree: Tree) -> dict[tuple[str, str], set[str]]:
    """`(population, document) -> keys` the earlier named census lists, documents as the new table names them."""
    listed: dict[tuple[str, str], set[str]] = defaultdict(set)
    with tree.earlier.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if not {"key", "source", "document"} <= set(reader.fieldnames or ()):
            fail(f"{tree.earlier} names no key, source and document columns; restore it from git")
        for number, row in enumerate(reader, 2):
            if not all(isinstance(row.get(cell), str) and row[cell] for cell in ("key", "source", "document")):
                fail(f"{tree.earlier}:{number} leaves its key, source or document empty; restore it from git")
            population = EARLIER_POPULATION.get(row["source"])
            if population is None:
                fail(f"{tree.earlier}: source {row['source']!r} is none of {', '.join(EARLIER_POPULATION)}")
            if row["key"] not in SCREEN.KEYS:
                fail(f"{tree.earlier}: key {row['key']!r} is none of the combination keys; restore it from git")
            document = archive_document(row["document"]) if population == "apis-guru" else row["document"]
            listed[(population, document)].add(row["key"])
    return listed


# The earlier combination searches' named censuses, beside the ledger-remainders one: each lists candidates of
# the combination keys by (key, source, document, sha256), the operation-combinations one packed and naming its
# source only through the document's own form.
COMBINATION_CENSUSES = (
    "witness-search-interaction-operation-combinations/census.tsv",
    "witness-search-interaction-schema-combinations/census.tsv",
    "witness-search-operation-combinations-bodies-responses/census.tsv",
    "witness-search-operation-combinations-parameters/census.tsv",
    "witness-search-schema-combinations-models-unions-refs/census.tsv",
    "witness-search-operation-combinations/census.tsv.gz",
)
CENSUS_SOURCE = {"github-code-search": "github", "sourcegraph": "sourcegraph", "apis.guru": "apis-guru"}
# `owner/repo:path@commit`, Sourcegraph's `github.com/` before it, and the packed census's
# ` [sha256:...]` or ` (+N identities, same bytes)` after it.
NAMED = re.compile(
    r"(github\.com/)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+):(.+?)@([0-9a-f]{40})"
    r"(?: \[sha256:[0-9a-f]{64}\]| \(\+\d+ identities, same bytes\))?"
)
# The extracted archive's top directory, which one earlier census names its documents under.
ARCHIVE_TREE = f"APIs-guru-openapi-directory-{ARCHIVE_REVISION[:7]}/"
# A census candidate's rank in the acquisition plan: below the handed-off documents, above every ledger identity.
CENSUS_RANK = 900
DIGEST_ONLY_SEARCHED = (
    "the census recorded only this sha256: no repository, path or commit is kept in it, in this record's "
    "acquisition plans (identities.tsv.gz, census-identities.tsv) or in its population manifest"
)
NON_PUBLIC = "the census names it by a screened non-public identity, whose repository, path and commit stay withheld"
EXCLUDED = "the census names it in a repository the witness search's exclusion rule keeps unfetched"


@dataclass
class NamedCensus:
    """Every candidate the earlier named censuses list for a combination key, as this table names it.

    `listed` holds those named by population and document; `identities` the commit and digest the census
    read a GitHub or Sourcegraph one at; `digests` those named by SHA-256 alone, each with why; `authored`
    the hand-written fixtures, which are no real-API candidates of any population here; and `nonpublic` the
    screened non-public inputs that kept no digest, which nothing names.
    """

    listed: dict[tuple[str, str], set[str]]
    identities: dict[tuple[str, str], SCREEN.Identity]
    digests: dict[str, tuple[set[str], str]]
    authored: dict[str, set[str]]
    nonpublic: dict[str, set[str]]

    def add(self, population: str, document: str, key: str) -> None:
        self.listed[(population, document)].add(key)


def named_census(tree: Tree) -> NamedCensus:
    census = NamedCensus(defaultdict(set), {}, {}, defaultdict(set), defaultdict(set))
    for (population, document), keys in earlier_rows(tree).items():
        census.listed[(population, document)] |= keys
    corpus = {name for name, path in SCREEN.registered_files(tree.root).items() if path.is_file()}
    index = _load("witness_populations_index", Path(__file__).with_name("witness-search-github-index.py"))
    recorded = {
        (github_repository(record.repository) or record.repository, record.path, record.commit): record.sha256
        for population in LEDGERS
        for record in ledger_identities(tree, population)
    }
    for relative in COMBINATION_CENSUSES:
        path = tree.surface / relative
        for number, row in enumerate(census_rows(path), 2):
            key, source, document, digest = row["key"], row.get("source", ""), row["document"], row["sha256"]
            if key not in SCREEN.KEYS:
                continue
            where = f"{path}:{number}"
            if index.opaque_identity(document.split(" ", 1)[0]) and digest == "-":
                # A screened non-public input with no digest has nothing a row could name it by.
                census.nonpublic[document].add(key)
                continue
            if not (SCREEN.SHA.fullmatch(digest) or (digest == "-" and NAMED.fullmatch(document))):
                fail(f"{where} names no SHA-256 for {document!r}; restore it from git")
            if document.startswith("(withheld)"):
                census.digests.setdefault(digest, (set(), DIGEST_ONLY_SEARCHED))[0].add(key)
                continue
            if index.opaque_identity(document.split(" ", 1)[0]):
                census.digests.setdefault(digest, (set(), NON_PUBLIC))[0].add(key)
                continue
            fixture = document.removeprefix("tests/fixtures/")
            if source == "registered" or document.startswith(("corpus-sources/", "tests/fixtures/", "registered")):
                # `corpus-sources/<row>/...` or `registered:<row>` names a corpus row; anything else is a fixture.
                name = fixture.split("/")[1] if fixture.startswith("corpus-sources/") else ""
                name = document.removeprefix("registered:") if document.startswith("registered:") else name
                if name in corpus:
                    census.add("registered", name, key)
                else:
                    census.authored[f"{fixture} ({digest})"].add(key)
                continue
            if source == "apis.guru" or document.startswith(("APIs/", ARCHIVE_TREE)):
                census.add("apis-guru", archive_listing(document), key)
                continue
            named = NAMED.fullmatch(document)
            if named is None or source not in ("", *CENSUS_SOURCE):
                fail(f"{where}: {source or 'its'} document {document!r} is no form this builder reads")
            sourcegraph, repository, file, commit = named.groups()
            if repository == ARCHIVE_REPOSITORY:
                census.add("apis-guru", archive_listing(document), key)
                continue
            if index.excluded_repository(repository):
                census.digests.setdefault(digest, (set(), EXCLUDED))[0].add(key)
                continue
            if not SCREEN.witness_screen().repository_name(repository) or not SCREEN.witness_screen().repository_path(
                file
            ):
                fail(f"{where}: {document!r} names no GitHub repository and path; restore it from git")
            population = "sourcegraph" if sourcegraph or source == "sourcegraph" else "github"
            name = f"{repository}/{file}"
            census.add(population, name, key)
            if digest == "-":
                # A census row that kept no digest takes the one a ledger read at that commit, else the commit's.
                digest = recorded.get((repository, file, commit), f"commit:{commit}")
            census.identities.setdefault(
                (population, name),
                SCREEN.Identity(population, name, repository, commit, file, digest, "", CENSUS_RANK),
            )
    return census


def archive_listing(document: str) -> str:
    """An earlier census's name for an archive document, as this table names it.

    The censuses name one by its archive path, under the extracted tree's top directory (alone or after
    `APIs/`), or as the directory's own `repository:path@revision`, first of the identities sharing its bytes.
    """
    first = document.split("; ", 1)[0]
    named = NAMED.fullmatch(first)
    if named is not None and named.group(2) == ARCHIVE_REPOSITORY:
        first = named.group(3)
    return archive_document(first.removeprefix("APIs/" + ARCHIVE_TREE).removeprefix(ARCHIVE_TREE))


def census_rows(path: Path) -> list[dict[str, str]]:
    """A census table's rows, each with its key, document and sha256; a missing or malformed table refused."""
    if not path.is_file():
        fail(f"{path} is no file; restore the earlier combination search records from git")
    with SCREEN.open_text(path) as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        if not {"key", "document", "sha256"} <= set(reader.fieldnames or ()):
            fail(f"{path} names no key, document and sha256 columns; restore it from git")
        rows = list(reader)
    for number, row in enumerate(rows, 2):
        if not all(isinstance(row.get(cell), str) and row[cell] for cell in ("key", "document", "sha256")):
            fail(f"{path}:{number} leaves its key, document or sha256 empty; restore it from git")
    return rows


class LedgerRecord(NamedTuple):
    """One candidate-ledger line the plan reads: a public identity and the ledger key that found it."""

    repository: SCREEN.Repository
    path: str
    commit: SCREEN.Commit
    sha256: SCREEN.Sha256
    key: str
    selector: str
    disposition: str
    at: str
    url: str


@functools.cache
def ledger_identities(tree: Tree, population: str) -> tuple[LedgerRecord, ...]:
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
                and isinstance(record.get("commit"), str)
                and re.fullmatch(r"[0-9a-f]{40}", record["commit"])
                and isinstance(record.get("sha256"), str)
                and re.fullmatch(r"[0-9a-f]{64}", record["sha256"])
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
    # Read once per tree and population: the plan, the census and the record each walk the ledgers.
    return tuple(rows)


def github_repository(repository: str) -> str | None:
    """`owner/repo` for a GitHub-hosted identity (Sourcegraph names it `github.com/owner/repo`)."""
    name = repository.removeprefix("github.com/")
    return name if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name) else None


class LedgerDocument(NamedTuple):
    """One document the candidate ledgers record, at the commit they read it at last, with the keys it could witness."""

    identity: SCREEN.Identity
    # The combination keys whose selector's field names are all among those of the ledger keys that found it.
    keys: frozenset[SCREEN.Key]


def ledger_documents(tree: Tree) -> list[LedgerDocument]:
    wanted = {key: ingredients(selector) for key, selector in tree.selectors().by_key.items()}
    out = []
    for population in LEDGERS:
        grouped: dict[tuple[str | None, str], list[LedgerRecord]] = defaultdict(list)
        for record in ledger_identities(tree, population):
            grouped[(github_repository(record.repository), record.path)].append(record)
        for (repository, path), records in sorted(grouped.items(), key=lambda item: (item[0][0] or "", item[0][1])):
            # Checked once per document, not once per ledger line naming it.
            if repository is None or not SCREEN.witness_screen().repository_path(path):
                continue
            if all(record.disposition == "excluded-non-openapi-3" for record in records):
                continue
            # One identity per document: the commit the ledgers read it at last.
            latest = max(records, key=lambda record: (record.at, record.commit))
            fields = frozenset().union(*(selector_fields(record.selector) for record in records if record.selector))
            matched = frozenset(key for key, need in wanted.items() if need and need <= fields)
            pointer = any(
                record.disposition == "declares" and POINTER_LEDGER_KEYS.search(record.key) for record in records
            )
            declares = any(record.disposition == "declares" for record in records)
            rank = len(matched) + (100 if pointer else 0) + (10 if declares else 0)
            identity = SCREEN.Identity(
                population, f"{repository}/{path}", repository, latest.commit, path, latest.sha256, latest.url, rank
            )
            out.append(LedgerDocument(identity, matched))
    return out


def identities(tree: Tree) -> list[SCREEN.Identity]:
    out = [document.identity for document in ledger_documents(tree)]
    for row in handed_off(tree):
        if row.provenance is not None:
            repository, path, commit = row.provenance
            out.append(SCREEN.Identity("handed-off", row.document, repository, commit, path, row.sha256, "", 1000))
    return out


class Provenance(NamedTuple):
    """Where a handed-off document was published: its repository, its path there and the commit."""

    repository: SCREEN.Repository
    path: str
    commit: SCREEN.Commit


class HandedOff(NamedTuple):
    """One handed-off document: its identity, the SHA-256 of the bytes handed off, and its provenance if recorded."""

    document: SCREEN.DocumentId
    sha256: SCREEN.Sha256
    provenance: Provenance | None


def handed_off(tree: Tree) -> list[HandedOff]:
    """Each handed-off document, its provenance None where it records none.

    A row naming a provenance must name a real one: an `owner/name` repository, a
    path inside it and a full commit, beside the SHA-256 of the bytes handed off.
    """
    rows = []
    with tree.handed_off.open(encoding="utf-8", newline="") as handle:
        for number, row in enumerate(csv.DictReader(handle, delimiter="\t"), 2):
            digest, document = row.get("sha256") or "", (row.get("document") or "").strip()
            if not SCREEN.SHA.fullmatch(digest) or not document:
                fail(f"{tree.handed_off}:{number} names no document and SHA-256 of its bytes; restore it from git")
            match = HANDED_OFF_ID.fullmatch(document)
            if match is None:
                # A row that records no provenance names no repository or commit at all; one that tries to
                # and does not parse is refused rather than taken for bytes-only.
                if "@" in document or ":" in document:
                    fail(f"{tree.handed_off}:{number}: {document!r} is no repository:path@commit; restore it from git")
                rows.append(HandedOff(document, digest, None))
                continue
            provenance = Provenance(*match.groups())
            if not SCREEN.witness_screen().repository_name(
                provenance.repository
            ) or not SCREEN.witness_screen().repository_path(provenance.path):
                fail(f"{tree.handed_off}:{number}: {document!r} is no repository, path and commit; restore it")
            rows.append(HandedOff(document, digest, provenance))
    return rows


class Acquisition(NamedTuple):
    """One line of the acquisition ledger: a planned identity, how its bytes were had, and their digest.

    `content_sha256` is the SHA-256 of the bytes had, and None for a refusal, which had none.
    """

    population: str
    document: SCREEN.DocumentId
    commit: SCREEN.Commit
    pin: SCREEN.Pin
    how: str
    content_sha256: SCREEN.Sha256 | None

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
            or row["population"] not in SCREEN.ACQUIRED
            or not re.fullmatch(r"[0-9a-f]{40}", row["commit"])
            or not isinstance(pin, str)
            or not any(pattern.fullmatch(pin) for pattern in (SCREEN.SHA, SCREEN.BLOB, SCREEN.COMMIT_PIN))
            or not isinstance(digest, str)
            or not any(pattern.fullmatch(digest) for pattern in (SCREEN.SHA, SCREEN.BLOB, SCREEN.COMMIT_PIN))
            or not SCREEN.acquisition_outcome(row["how"])
            # Bytes had are named by their content's SHA-256; a refusal names none (earlier ledgers repeat its pin).
            or (row["how"] in SCREEN.HELD and not SCREEN.SHA.fullmatch(digest))
        ):
            fail(
                f"{path}:{number} is no acquisition record (an acquired population, document, commit, pin, how, "
                "and a SHA-256 for bytes had); "
                "restore it from git"
            )
        held = row["how"] in SCREEN.HELD
        out.append(
            Acquisition(row["population"], row["document"], row["commit"], pin, row["how"], digest if held else None)
        )
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
    recorded: dict[str, str] = {}
    with tree.archive_manifest.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if not {"walk", "document", "revision", "sha256"} <= set(reader.fieldnames or ()):
            fail(
                f"{tree.archive_manifest}: its header names no walk, document, revision and sha256 columns; "
                "restore it from git"
            )
        for number, row in enumerate(reader, 2):
            if row.get("walk") != ARCHIVE_REPOSITORY or row.get("revision") != ARCHIVE_REVISION:
                continue
            document, digest = row.get("document") or "", row.get("sha256") or ""
            if not SCREEN.witness_screen().repository_path(document) or not SCREEN.SHA.fullmatch(digest):
                fail(f"{tree.archive_manifest}:{number} names no archive path and SHA-256; restore it from git")
            if document in recorded:
                fail(f"{tree.archive_manifest}:{number} records {document} a second time; restore it from git")
            recorded[document] = digest
    return recorded


def manifest(tree: Tree, args: argparse.Namespace) -> list[SCREEN.Entry]:
    store_root = args.store or SCREEN.cache_root()
    census = named_census(tree)
    listed = census.listed
    entries = []
    # Every (population, document, key) a census lists, as each is claimed: the table must end with a row of each.
    owed: set[tuple[str, str, str]] = set()

    def keys(population: str, document: str) -> str:
        claimed = listed.pop((population, document), set())
        owed.update((population, document, key) for key in claimed)
        return ";".join(sorted(claimed)) or "-"

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
    for row in handed_off(tree):
        digest, document, provenance = row.sha256, row.document, row.provenance
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
        if row.held and row.content_sha256 is not None
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
            or (kept := SCREEN.cached(digest, store_root)) is None
            # The ledger's digest is attributed only to bytes that carry the planned pin.
            or not SCREEN.pinned_by(identity, kept)
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
                keys(identity.population, identity.document),
                "-",
            )
        )
    entries = by_digest(entries, census, plan)
    owed.update((population, document, key) for (population, document), ks in listed.items() for key in ks)
    entries += unavailable(tree, args, plan, seen, listed)
    if listed:
        fail(f"the earlier named census lists candidates no population names: {sorted(listed)[:5]}")
    # A handed-off document without its bytes owes rows only for keys an earlier census lists it for.
    entries = [entry for entry in entries if entry.unfetchable == "-" or entry.keys != "-"]
    rowed = {(entry.population, entry.document, key) for entry in entries for key in entry.forced()}
    if owed - rowed:
        fail(
            f"the earlier named census lists {len(owed - rowed)} (population, document, key) candidates the "
            f"manifest gives no row (first: {sorted(owed - rowed)[0]}); each owes a screened or unfetchable row"
        )
    return entries


def by_digest(entries: list[SCREEN.Entry], census: NamedCensus, plan: list[SCREEN.Identity]) -> list[SCREEN.Entry]:
    """`entries`, with each candidate a census names by SHA-256 alone owed a row under its keys.

    Bytes held under that digest take its keys; a planned identity pinned to it is listed for them, so the
    unavailable candidates name it; and a digest neither names is an unfetchable `sha256:<hex>` entry.
    """
    held: dict[str, list[int]] = defaultdict(list)
    for number, entry in enumerate(entries):
        if entry.unfetchable == "-":
            held[entry.sha256].append(number)
    pinned = {identity.content_digest(): identity for identity in plan if identity.population in LEDGERS}
    out = list(entries)
    for digest, (keys, why) in sorted(census.digests.items()):
        if held.get(digest):
            for number in held[digest]:
                entry = out[number]
                out[number] = entry._replace(keys=";".join(sorted({*entry.forced(), *keys})))
        elif digest in pinned:
            census.listed[(pinned[digest].population, pinned[digest].document)] |= keys
        else:
            named = f"sha256:{digest}"
            out.append(SCREEN.Entry("github", named, named, digest, "-", ";".join(sorted(keys)), why))
    return out


class CodeHit(NamedTuple):
    """One file a code search answered with: where it is, at which commit, and its git blob."""

    repository: str
    path: str
    commit: str
    blob: str  # the git blob SHA-1 a code-search hit names; empty for a Sourcegraph match
    url: str


class RecordedQuery(NamedTuple):
    """One recorded query: who answered it, for which key, how, and the files it named."""

    source: str
    key: SCREEN.Key
    outcome: str
    hits: tuple[CodeHit, ...]


# Who answers the search's queries; and the outcome this builder records for a key no code search can spell.
QUERY_SOURCES = ("github-code-search", "sourcegraph")
NOT_QUERYABLE = "not-queryable"
# A recorded hit's fields, each a string: a code-search hit also names its git blob (`sha`), a Sourcegraph one none.
HIT_FIELDS = {
    "github-code-search": ("repository", "path", "commit", "sha"),
    "sourcegraph": ("repository", "path", "commit"),
}


def query_outcomes() -> frozenset[str]:
    """Every outcome a recorded query may carry: the guarded acquirer's own, and `NOT_QUERYABLE`."""
    client = github()
    return frozenset({*client.ANSWER_OUTCOMES, *client.NON_ANSWER_OUTCOMES, NOT_QUERYABLE})


def unavailable(
    tree: Tree,
    args: argparse.Namespace,
    plan: list[SCREEN.Identity],
    held: set[tuple[str, str]],
    listed: dict[tuple[str, str], set[str]],
) -> list[SCREEN.Entry]:
    """An `unfetchable` entry for each known candidate whose bytes were not had, under the keys it is known for.

    A document the raw lane refused carries the keys its recorded hits match by field name (as the plan
    ranks it), and those an earlier census lists it for, with the SHA-256 recorded for it; a code-search hit
    never fetched carries the key whose query found it, and `-`, since only its git blob is known; a
    document an earlier census lists and the bound never fetched carries that census's keys. A ledger
    document never asked within the fetch budget and listed by no census is tied to keys only by the plan's
    field-name ranking: the README counts it among the missing populations, and it owes no row.
    """
    attempts: dict[tuple[str, str], list[Acquisition]] = defaultdict(list)
    for row in acquisitions(args.acquisitions):
        attempts[(row.population, row.document)].append(row)
    ledger = {(d.identity.population, d.identity.document): d.keys for d in ledger_documents(tree)}
    found_by: dict[tuple[str, str], set[str]] = defaultdict(set)
    if args.search_evidence.is_dir():
        for query in recorded_queries(args.search_evidence):
            for hit in query.hits if query.source == "github-code-search" else ():
                found_by[("github", f"{hit.repository}/{hit.path}")].add(query.key)
    options: dict[tuple[str, str], list[SCREEN.Identity]] = defaultdict(list)
    for identity in plan:
        named = (identity.population, identity.document)
        if identity.population in LEDGERS and named not in held:
            options[named].append(identity)
    archived: set[str] = set()
    entries = []
    for named, identities in options.items():
        owed = listed.pop(named, set())
        tried = [
            (identity, rows)
            for identity in identities
            if (
                rows := [
                    row for row in attempts.get(named, []) if (row.commit, row.pin) == (identity.commit, identity.pin)
                ]
            )
        ]
        if any(row.held for _, rows in tried for row in rows):
            if not owed:
                continue
            identity = next(identity for identity, rows in tried if any(row.held for row in rows))
            reason = "had once through the guarded raw lane, and its bytes are no longer in this host's store"
            keys = owed
        elif tried:
            identity, rows = tried[0]
            statuses = sorted({row.how.removeprefix("refused-http-") for row in rows})
            answered = " and ".join(
                "no answer"
                if status == "0"
                else "bytes whose digest is not the recorded one"
                if status == SCREEN.Acquired.DIGEST_DIFFERS
                else f"HTTP {status}"
                for status in statuses
            )
            reason = (
                f"fetched {len(rows)} time(s) at the recorded commit through the guarded raw lane, which gave "
                f"{answered}"
            )
            keys = ledger.get(named, frozenset()) | found_by.get(named, set()) | owed
        elif SCREEN.BLOB.fullmatch((identity := identities[0]).pin):
            reason = (
                "found by the bounded code search and never fetched: the six-hour raw-lane budget was spent on "
                "higher-ranked identities first"
            )
            keys = found_by.get(named, set()) | owed
        elif owed:
            reason = (
                "listed by an earlier named census and never fetched: the guarded raw lane's budget was spent "
                "before it was reached"
            )
            keys = owed
        else:
            continue
        if not keys:
            # Its recorded hits tie it to no combination key: no candidate of any, like a document never asked.
            continue
        digest = identity.content_digest() or "-"
        entries.append(
            SCREEN.Entry(
                identity.population,
                identity.document,
                f"{RAW}/{identity.repository}/{identity.commit}/{identity.path}",
                digest,
                licence_evidence(identity.repository, identity.commit, digest, archived),
                ";".join(sorted(keys)),
                reason,
            )
        )
    return entries


def recorded_queries(evidence: Path) -> list[RecordedQuery]:
    """The search's recorded answers: its live `queries.jsonl`, or the `queries.jsonl.gz` it is committed as."""
    packed = evidence / "queries.jsonl.gz"
    if not (evidence / "queries.jsonl").is_file() and packed.is_file():
        with gzip.open(packed, "rt", encoding="utf-8") as handle:
            rows = [json.loads(line) for line in handle if line.strip()]
    else:
        rows = github().jsonl(evidence / "queries.jsonl")
    outcomes = query_outcomes()
    for number, row in enumerate(rows, 1):
        results = row.get("results", []) if isinstance(row, dict) else None
        if (
            not isinstance(row, dict)
            or row.get("source") not in QUERY_SOURCES
            or row.get("key") not in SCREEN.KEYS
            or row.get("outcome") not in outcomes
            or not isinstance(results, list)
            or not all(
                isinstance(item, dict)
                and all(isinstance(item.get(field), str) for field in HIT_FIELDS[row["source"]])
                and isinstance(item.get("url", ""), str)
                and isinstance(item.get("sha", ""), str)
                for item in results
            )
        ):
            fail(f"{evidence}: query record {number} is no recorded query with a list of results; restore it from git")
    return [
        RecordedQuery(
            row["source"],
            row["key"],
            row["outcome"],
            tuple(
                CodeHit(item["repository"], item["path"], item["commit"], item.get("sha", ""), item.get("url", ""))
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
                            "outcome": NOT_QUERYABLE,
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
    listed = sub.add_parser("census")
    listed.add_argument("--output", type=Path, required=True)
    build = sub.add_parser("manifest")
    build.add_argument("--output", type=Path, default=SCREEN.POPULATION)
    build.add_argument(
        "--identities", type=Path, action="append", required=True, help="an acquisition plan; repeatable"
    )
    build.add_argument("--acquisitions", type=Path, default=SCREEN.RECORD / "acquisition" / "acquisitions.jsonl")
    build.add_argument("--archive", type=Path, required=True, help="the extracted openapi-directory tree")
    build.add_argument(
        "--search-evidence", type=Path, default=SCREEN.RECORD / "search", help="the live search's record"
    )
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
    if args.command == "search" and not args.replay and (args.evidence / "queries.jsonl.gz").is_file():
        parser.error("the search's answers are committed packed; gunzip queries.jsonl.gz to resume it live")
    try:
        match args.command:
            case "search":
                rows = search(tree, args)
                write_plan(args.output, rows)
                print(f"witness-populations-build: {len(rows)} new code-search identities")
            case "identities":
                rows = identities(tree)
                write_plan(args.output, rows)
                print(f"witness-populations-build: {len(rows)} identities")
            case "census":
                rows = sorted(named_census(tree).identities.values())
                write_plan(args.output, rows)
                print(f"witness-populations-build: {len(rows)} census identities")
            case _:
                entries = manifest(tree, args)
                SCREEN.write_manifest(args.output, entries)
                print(f"witness-populations-build: {len(entries)} manifest entries")
    except SCREEN.ScreenError as error:
        fail(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
