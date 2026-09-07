#!/usr/bin/env python3
"""Pin the absolute-URL `$ref`s a fetched corpus document makes into other documents.

A corpus row whose root document names another document by absolute URL is only
reproducible if that URL is immutable. `helios-verifiable-api` names seven
`ethereum/execution-apis` documents at `refs/heads/main`, so its byte-match
verdict used to depend on whatever somebody edited upstream that morning. The
repair is `tests/fixtures/corpus-remote-ref-pins.tsv`: a committed table of
`mutable_url -> pinned_url` substitutions, each carrying the SHA-256 of the bytes
the pinned URL serves, applied to the *fetched document* at fetch time.

Nothing under `src/` learns about pinning. crozier keeps fetching whatever URL the
document it is handed contains; this module decides which document it is handed.

Three callers share this one parser, which is why the filename is underscored
where every script beside it is hyphenated: `scripts/fern-goldens` **imports** it
(so the provenance it records and the substitution the fetch applies cannot
disagree), while `scripts/corpus-lib.sh` and `scripts/fetch-corpus.sh` run it as
a CLI.

Commands
--------
`check`
    The offline gate (`just lint-corpus-remote-ref-pins`). Opens no socket.
`apply <corpus_name> <file> [--as NAME]`
    Rewrite `<file>` in place, then prove the post-condition, then fetch each
    `pinned_url` once and compare its SHA-256. `--as` names the file whose suffix
    decides the parser, because the caller applies this to a suffix-less
    temporary before publishing it under its canonical name.
`verify <corpus_name> <file>`
    Assert offline, without rewriting, that `<file>` is already in the state
    `apply` would leave it in.

`verify` is `apply`'s post-state expressed as a predicate: `apply` requires every
record's `mutable_url` to occur and replaces every occurrence of it with the
`pinned_url`, so a document `apply` has just written always passes `verify`, and
`apply` re-runs `verify`'s predicate on its own output to keep the two from
drifting.

Why `verify` demands more than the post-condition
------------------------------------------------
A cache written under a *previous* pin — an older but perfectly immutable commit —
satisfies "every absolute `$ref` is immutably addressed" and would be reused, so
moving a pin forward would never take effect on `fetch-corpus.sh --if-missing`.
For a row that has records `verify` therefore also requires that every current
`pinned_url` occurs, that every corresponding `mutable_url` is absent, and that no
absolute URL naming a mapped reference's file at any *other* commit remains.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator, Mapping
from urllib.parse import urlsplit

MANIFEST_RELATIVE = ("tests", "fixtures", "corpus-remote-ref-pins.tsv")
CORPUS_RELATIVE = ("tests", "fixtures", "CORPUS.md")
CENSUS_RELATIVE = ("scripts", "openapi-surface-census.py")

COLUMNS = ("corpus_name", "mutable_url", "pinned_url", "sha256")

#: The one host this repository treats as immutably addressable. A second host
#: must arrive as a deliberate extension of this decision, not as a silent pass.
IMMUTABLE_HOST = "raw.githubusercontent.com"
CANONICAL_ORIGIN = f"https://{IMMUTABLE_HOST}"
REVISION_RE = re.compile(r"[0-9a-f]{40}")
DIGEST_RE = re.compile(r"[0-9a-f]{64}")

#: Test-only seam. A `pinned_url` always names `IMMUTABLE_HOST` because the
#: immutability predicate demands it, so the boundary suite could not otherwise
#: drive the digest fetch through real `curl` against its own loopback server.
#: When set, this replaces the origin of a `pinned_url` FOR THAT FETCH ONLY: it
#: never affects the recorded URL, the predicate, the substitution written into
#: the document, `expected_state`, or anything under `src/`. It refuses any value
#: that is not a loopback origin, so it cannot redirect a fetch off this machine.
ORIGIN_ENV = "CROZIER_CORPUS_PIN_ORIGIN"
LOOPBACK_ORIGIN_RE = re.compile(r"http://(?:127\.0\.0\.1|localhost):[0-9]{1,5}")

#: Matches `scripts/corpus-lib.sh`'s `--max-time` posture for a referenced
#: document: long enough for a large schema, short enough to fail rather than hang.
FETCH_TIMEOUT_SECONDS = 30


class PinError(RuntimeError):
    """An actionable command-boundary error."""


@dataclass(frozen=True)
class PinRecord:
    """One `mutable_url -> pinned_url` substitution and the digest that pins it."""

    corpus_name: str
    mutable_url: str
    pinned_url: str
    sha256: str

    @property
    def reference_identity(self) -> tuple[str, str, str, str]:
        """`(host, owner, repo, path after the ref segment)` — the file this names.

        Two URLs share an identity exactly when they name the same file at
        possibly different revisions, which is what makes a superseded pin
        recognizable.
        """
        return reference_identity(self.pinned_url)


def default_root() -> Path:
    return Path(__file__).resolve().parent.parent


def manifest_path(root: Path) -> Path:
    return root.joinpath(*MANIFEST_RELATIVE)


# ---------------------------------------------------------------------------
# The immutability predicate
# ---------------------------------------------------------------------------


def _path_segments(url: str) -> list[str]:
    return urlsplit(url).path.split("/")[1:]


def immutability_failure(url: str) -> str | None:
    """Why `url` is not immutably addressed, or `None` when it is."""
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return f"{url!r} is not an absolute http(s) URL"
    if (
        parsed.hostname != IMMUTABLE_HOST
        or parsed.port is not None
        or parsed.username is not None
        or parsed.password is not None
        or parsed.scheme != "https"
    ):
        return (
            f"{url!r} is not a plain https URL on {IMMUTABLE_HOST}, the one host this "
            "repository can address immutably"
        )
    segments = _path_segments(url)
    if len(segments) < 4 or not all(segments):
        return (
            f"{url!r} has no /<owner>/<repo>/<ref>/<path> shape, so it names no revision"
        )
    if not REVISION_RE.fullmatch(segments[2]):
        return (
            f"{url!r} addresses {segments[2]!r} rather than a 40-character commit SHA, "
            "so the bytes it serves can change"
        )
    return None


def is_immutable(url: str) -> bool:
    return immutability_failure(url) is None


def reference_identity(url: str) -> tuple[str, str, str, str]:
    """The identity of an immutably addressed URL. Only call it on one."""
    segments = _path_segments(url)
    return (IMMUTABLE_HOST, segments[0], segments[1], "/".join(segments[3:]))


def strip_fragment(reference: str) -> str:
    return reference.split("#", 1)[0]


def is_absolute_reference(reference: str) -> bool:
    parsed = urlsplit(strip_fragment(reference))
    return bool(parsed.scheme) and bool(parsed.netloc)


# ---------------------------------------------------------------------------
# The manifest
# ---------------------------------------------------------------------------


def load_records(root: Path | None = None) -> list[PinRecord]:
    """Every record in the manifest, structurally validated.

    Whether a `corpus_name` names a real CORPUS.md row is `check`'s question, not
    this one's: `apply` runs against one row and must not care that some other
    row was renamed.
    """
    root = default_root() if root is None else root
    path = manifest_path(root)
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise PinError(
            f"could not read pin manifest {path}: {error}; restore it from git"
        ) from error

    records: list[PinRecord] = []
    seen: set[tuple[str, str]] = set()
    for number, line in enumerate(lines, start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cells = line.split("\t")
        site = f"{path} line {number}"
        if len(cells) != len(COLUMNS):
            raise PinError(
                f"{site}: has {len(cells)} tab-separated column(s); expected exactly "
                f"{len(COLUMNS)} ({', '.join(COLUMNS)}) — rewrite the record with one "
                "tab between each column"
            )
        record = PinRecord(*cells)
        for column, value in zip(COLUMNS, cells):
            if not value.strip() or value != value.strip():
                raise PinError(
                    f"{site}: {column} is {value!r}; every column must carry a "
                    "non-empty value with no surrounding whitespace"
                )
        if not is_absolute_reference(record.mutable_url):
            raise PinError(
                f"{site}: mutable_url {record.mutable_url!r} is not an absolute URL; "
                "record the `$ref` exactly as the upstream root document writes it, "
                "with the `#fragment` removed"
            )
        failure = immutability_failure(record.pinned_url)
        if failure is not None:
            raise PinError(
                f"{site}: pinned_url {failure}; pin the reference to a commit URL such "
                f"as {CANONICAL_ORIGIN}/<owner>/<repo>/<40-hex-sha>/<path>"
            )
        if not DIGEST_RE.fullmatch(record.sha256):
            raise PinError(
                f"{site}: sha256 {record.sha256!r} is not 64 lowercase hexadecimal "
                f"characters; measure it with `curl -fsSL {record.pinned_url} | sha256sum`"
            )
        key = (record.corpus_name, record.mutable_url)
        if key in seen:
            raise PinError(
                f"{site}: duplicate record for {record.corpus_name} "
                f"{record.mutable_url}; keep one record per reference and delete the rest"
            )
        seen.add(key)
        records.append(record)

    _reject_prefixes(path, records)
    _reject_disorder(path, records)
    return records


def _sort_key(record: PinRecord) -> tuple[str, str]:
    return (record.corpus_name, record.mutable_url)


def _reject_prefixes(path: Path, records: list[PinRecord]) -> None:
    """One `mutable_url` prefixing another would make substitution order matter."""
    for record in records:
        for other in records:
            if other is record or other.corpus_name != record.corpus_name:
                continue
            if other.mutable_url.startswith(record.mutable_url):
                raise PinError(
                    f"{path}: {record.corpus_name} records {record.mutable_url!r}, "
                    f"which is a prefix of {other.mutable_url!r}; substituting one "
                    "would corrupt the other, so split the reference or drop a record"
                )


def _reject_disorder(path: Path, records: list[PinRecord]) -> None:
    ordered = sorted(records, key=_sort_key)
    if records != ordered:
        first = next(
            record for record, want in zip(records, ordered) if record != want
        )
        raise PinError(
            f"{path}: records are not sorted; {first.corpus_name} "
            f"{first.mutable_url} is out of order — sort the records by corpus name "
            "then mutable URL"
        )


def records_for(corpus_name: str, root: Path | None = None) -> list[PinRecord]:
    """This row's records, in manifest order. Empty for a row with no pins."""
    return [
        record for record in load_records(root) if record.corpus_name == corpus_name
    ]


def corpus_names(root: Path) -> set[str]:
    """The canonical CORPUS.md numbered rows' names.

    A third reader of that table (`scripts/corpus-lib.sh` and
    `scripts/fern-goldens` have the other two), deliberately: `scripts/fern-goldens`
    imports this module, so importing it back would be circular. Only the name
    cell is read here.
    """
    header = ["#", "name", "method", "source", "pinned ref", "license", "decision", "shapes"]
    path = root.joinpath(*CORPUS_RELATIVE)
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise PinError(f"could not read corpus manifest {path}: {error}") from error
    names: set[str] = set()
    in_manifest = False
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells == header:
            in_manifest = True
            continue
        if not line.strip().startswith("|"):
            in_manifest = False
            continue
        if in_manifest and cells and cells[0].isdigit() and len(cells) == len(header):
            names.add(cells[1].strip("` "))
    if not names:
        raise PinError(f"no numbered corpus rows found in {path}")
    return names


# ---------------------------------------------------------------------------
# Reading the document
# ---------------------------------------------------------------------------


_CENSUS_CACHE: dict[Path, Any] = {}


def _census(root: Path):
    """The repository's one OpenAPI document reader, imported lazily.

    `check` never opens a document, so it must not need this module present.
    """
    path = root.joinpath(*CENSUS_RELATIVE)
    cached = _CENSUS_CACHE.get(path)
    if cached is not None:
        return cached
    name = "openapi_surface_census"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise PinError(
            f"could not load the OpenAPI document reader {path}; restore it from git"
        )
    module = importlib.util.module_from_spec(spec)
    # Registered before execution because the reader defines dataclasses, and
    # `@dataclass` resolves annotations through `sys.modules[cls.__module__]`.
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except OSError as error:
        del sys.modules[name]
        raise PinError(
            f"could not load the OpenAPI document reader {path}: {error}; "
            "restore it from git"
        ) from error
    _CENSUS_CACHE[path] = module
    return module


def document_references(root: Path, path: Path) -> list[str]:
    """Every `$ref` value in `path`, read as a document rather than as text.

    Text would score the absolute URL a `description` carries — helios' own
    description links to its GitHub page — as a cross-document reference.
    """
    census = _census(root)
    try:
        document = census.load_document(path)
    except census.DocumentError as error:
        raise PinError(
            f"could not read {path} as an OpenAPI document: {error}; the pin guard "
            "cannot check a document it cannot parse"
        ) from error
    if not isinstance(document, dict):
        raise PinError(
            f"{path} is not an OpenAPI document (its root is not a mapping); the pin "
            "guard cannot check it"
        )
    return list(_iter_references(document))


def _iter_references(node: Any) -> Iterator[str]:
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "$ref" and isinstance(value, str):
                yield value
            else:
                yield from _iter_references(value)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_references(item)


# ---------------------------------------------------------------------------
# The predicate `verify` asserts and `apply` establishes
# ---------------------------------------------------------------------------


def post_condition_failure(root: Path, path: Path, manifest: Path) -> str | None:
    """The rule EVERY row obeys: no absolute-URL `$ref` that is not immutable."""
    for reference in document_references(root, path):
        if not is_absolute_reference(reference):
            continue
        address = strip_fragment(reference)
        failure = immutability_failure(address)
        if failure is not None:
            return (
                f"{path}: absolute `$ref` {failure}; add a record substituting it for "
                f"an immutable URL to {manifest}"
            )
    return None


def verification_failure(
    root: Path, corpus_name: str, path: Path, records: list[PinRecord]
) -> str | None:
    """Why `path` is not in the state `apply` leaves it in, or `None` when it is."""
    manifest = manifest_path(root)
    failure = post_condition_failure(root, path, manifest)
    if failure is not None:
        return failure
    if not records:
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        return f"{path}: could not be read: {error}; fetch the corpus source again"
    by_identity = {record.reference_identity: record for record in records}
    for record in records:
        if record.mutable_url in text:
            return (
                f"{path}: still carries the mutable URL {record.mutable_url}; "
                f"{manifest} records a pin for it"
            )
        if record.pinned_url not in text:
            return (
                f"{path}: does not carry the pinned URL {record.pinned_url} that "
                f"{manifest} records for {corpus_name}"
            )
    for reference in document_references(root, path):
        if not is_absolute_reference(reference):
            continue
        address = strip_fragment(reference)
        record = by_identity.get(reference_identity(address))
        if record is not None and address != record.pinned_url:
            return (
                f"{path}: `$ref` {address} names the same file as the superseded pin "
                f"for {record.mutable_url}; {manifest} now pins {record.pinned_url}"
            )
    return None


# ---------------------------------------------------------------------------
# Fetching a pinned document's bytes
# ---------------------------------------------------------------------------


def origin_override(environ: Mapping[str, str] | None = None) -> str | None:
    environ = os.environ if environ is None else environ
    value = environ.get(ORIGIN_ENV)
    if not value:
        return None
    if not LOOPBACK_ORIGIN_RE.fullmatch(value):
        raise PinError(
            f"{ORIGIN_ENV} is {value!r}; it exists only so the boundary suite can point "
            "the digest fetch at its own server, so it must be an http://127.0.0.1:<port> "
            "or http://localhost:<port> origin — unset it to fetch from "
            f"{CANONICAL_ORIGIN}"
        )
    return value


def fetch_bytes(url: str, override: str | None) -> bytes:
    target = override + url[len(CANONICAL_ORIGIN) :] if override else url
    try:
        result = subprocess.run(
            [
                "curl",
                "--silent",
                "--show-error",
                "--fail",
                "--location",
                "--max-time",
                str(FETCH_TIMEOUT_SECONDS),
                # `--` so a URL beginning with `-` can never be read as an option.
                "--",
                target,
            ],
            capture_output=True,
            check=False,
        )
    except OSError as error:
        raise PinError(
            f"could not run `curl` to fetch {target}: {error}; install curl — the pin "
            "guard verifies each pinned document's digest with it"
        ) from error
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", "replace").strip()
        raise PinError(
            f"could not fetch {target}: {detail or f'curl exited {result.returncode}'}; "
            "check the URL is reachable, then re-run the fetch"
        )
    return result.stdout


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------


def check(root: Path) -> None:
    """The offline gate: the manifest is well-formed and names real corpus rows."""
    records = load_records(root)
    names = corpus_names(root)
    manifest = manifest_path(root)
    for record in records:
        if record.corpus_name not in names:
            raise PinError(
                f"{manifest}: corpus_name {record.corpus_name!r} is not a canonical "
                f"CORPUS.md numbered row; correct the name or delete the record"
            )


def apply(root: Path, corpus_name: str, path: Path, document_name: str | None = None) -> None:
    """Substitute this row's pins into `path`, prove the result, and check digests."""
    records = records_for(corpus_name, root)
    manifest = manifest_path(root)
    override = origin_override()
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        raise PinError(
            f"could not read {path}: {error}; fetch the corpus source again"
        ) from error

    for record in records:
        if record.mutable_url not in text:
            raise PinError(
                f"{path}: {manifest} records a pin for {record.mutable_url}, which the "
                f"fetched {corpus_name} document does not reference; re-measure the "
                "record against the document or delete it"
            )
        text = text.replace(record.mutable_url, record.pinned_url)

    suffix = Path(document_name or path.name).suffix
    handle, staged_name = tempfile.mkstemp(dir=str(path.parent), prefix=".pin.", suffix=suffix)
    staged = Path(staged_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="") as stream:
            stream.write(text)
        failure = verification_failure(root, corpus_name, staged, records)
        if failure is not None:
            raise PinError(failure)
        for record in records:
            measured = hashlib.sha256(fetch_bytes(record.pinned_url, override)).hexdigest()
            if measured != record.sha256:
                raise PinError(
                    f"{manifest}: {record.pinned_url} serves sha256 {measured}, but the "
                    f"record for {corpus_name} {record.mutable_url} says {record.sha256}; "
                    "an immutable URL cannot change its bytes, so re-measure the record "
                    "or correct the pinned URL"
                )
        os.replace(staged, path)
    finally:
        staged.unlink(missing_ok=True)


def verify(root: Path, corpus_name: str, path: Path) -> None:
    records = records_for(corpus_name, root)
    failure = verification_failure(root, corpus_name, path, records)
    if failure is not None:
        raise PinError(failure)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="repository root (defaults to this script's own repository)",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="validate the pin manifest offline")
    for name, help_text in (
        ("apply", "substitute a row's pins into a fetched document"),
        ("verify", "assert a document already carries a row's pins"),
    ):
        command = commands.add_parser(name, help=help_text)
        command.add_argument("corpus_name")
        command.add_argument("file", type=Path)
        if name == "apply":
            command.add_argument(
                "--as",
                dest="document_name",
                default=None,
                help="the filename whose suffix decides the parser (default: FILE's own)",
            )
    args = parser.parse_args(argv)
    root = (args.root or default_root()).resolve()
    try:
        if args.command == "check":
            check(root)
        elif args.command == "apply":
            apply(root, args.corpus_name, args.file, args.document_name)
        else:
            verify(root, args.corpus_name, args.file)
    except PinError as error:
        print(f"corpus-remote-ref-pins: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
