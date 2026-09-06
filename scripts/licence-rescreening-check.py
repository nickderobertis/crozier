#!/usr/bin/env python3
"""Hold `docs/licence-rescreening.md` to the shape a registering node can read.

The screening record is **one line per document** that the six
`docs/openapi-surface/*.md` region files record as blocked on a licence. The
node that registers witnesses works from that record and from nothing else, so
a line missing its verdict, its reason, its pinned reference, either half of
the Fern screen, or naming a coverage row no region file carries is worse than
no line at all: it reads as a screening that happened. A line covering several
documents at once is worse still, because it hides the ones nobody screened.

This gate therefore does two things.

**It derives the authoritative candidate set from the region files** rather
than trusting the record's own account of its scope:

* a **ledger row** (a table under a `### Witness search (issue #188)` heading
  whose first column is `candidate`) is in scope when its licence cell or its
  verdict cell names a licence among what blocks the candidate. Every document
  that row's candidate cell names is one candidate;
* a **witness row** (first column `key`) is in scope when its outcome is
  `witness-blocked` and it records a licence rather than `—`.

Every derived document must be carried by exactly one record line, and every
in-scope row must be cited by at least one — so a grouped line, a dropped
document and a dropped row all fail.

**And it holds each line to the whole contract.** Every line must carry:

* one document and no more, named the way its region row names it;
* a `source` citation `<region>.md:<line>` per region row it answers, which
  must be a real table row in that region's witness search naming that
  document;
* the reference it was screened at — a fetch URL with the byte count and MD5 of
  what came back, and either a 40-character commit, an APIs.guru version
  reference, or an explicit `no immutable ref — <why the world offers none>`;
* an **admission verdict**, exactly `admitted` or `still-blocked`, and the
  reason behind it;
* the **exit status** of a real `fern check` and of a real
  `fern generate --group python-sdk --preview`. `not run` is not an outcome:
  every candidate is screened at the reference its region row records;
* **coverage rows** the region files carry, read off their `## Entries`
  tables, or an explicit `none`. Only a coverage-row key may be written in
  backticks in that column.

Run: `just lint-licence-rescreening` (part of `just check`).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RECORD = "docs/licence-rescreening.md"
REGION_DIR = "docs/openapi-surface"
REGIONS = (
    "bodies-media",
    "document-paths",
    "oas31-extensions",
    "parameters",
    "schemas",
    "security",
)
WITNESS_HEADING = "### Witness search (issue #188)"
TABLE_HEADING = "## The record"
COLUMNS = (
    "candidate",
    "source",
    "pinned ref",
    "licence",
    "admission",
    "why the rule reaches it or does not",
    "rows it declares",
    "document check",
    "generate",
)
VERDICTS = ("admitted", "still-blocked")
# A reason has to say something. Anything this short is a label, not a reason.
MIN_REASON = 25

# The phrases the region files use when a licence is among what blocks a
# candidate. Kept as one list so the scope is readable rather than inferred.
LICENCE_OBSTACLE = re.compile(
    r"licen[cs]e blocks it|blocked on licen[cs]e|licen[cs]e outside the set"
    r"|outside the (?:corpus's )?(?:admissible |redistribution )?set"
    r"|not redistributable|no licen[cs]e this corpus can rest on"
    r"|no redistributable licen[cs]e|nothing licenses the corpus"
    r"|nothing grants redistribution|declares? no licen[cs]e|no licen[cs]e[,.]"
    r"|licen[cs]e is the only thing|licen[cs]e-blocked"
    r"|licen[cs]e would have blocked|no licen[cs]e anywhere"
    r"|declare no licen[cs]e|none declared|no license|NOASSERTION|proprietar",
    re.I,
)

TICK = re.compile(r"`([^`]+)`")
KEY = re.compile(r"`([a-z0-9][a-z0-9.\-]*)`")
DOC_PATH = re.compile(r"^[\w][\w./+@-]*\.(?:json|ya?ml)$")
SLUG = re.compile(r"^[\w.@-]+/[\w.@-]+$")
TRIPLE = re.compile(r"^[\w.@-]+/[\w.@-]+/[\w.@ +-]+$")
URL = re.compile(r"^https?://\S+$")
COMMIT = re.compile(r"\b[0-9a-f]{40}\b")
NO_REF = re.compile(r"no immutable ref — (?P<why>[^|]+)")
APIS_GURU = re.compile(r"APIs\.guru `[^`]+`")
FETCH = re.compile(r"https?://\S+")
MD5 = re.compile(r"MD5 `[0-9a-f]{32}`")
BYTES = re.compile(r"[\d,]+ bytes")
EXIT = re.compile(r"exit\*{0,2}\s*\*{0,2}(-?\d+)")
SOURCE = re.compile(r"\[?`?([a-z0-9-]+)\.md`?\]?[^:]*:(\d+)")


def documents_in(cell: str) -> list[str]:
    """Every document a candidate cell names, as `owner/repo:path` or a token.

    The shapes the region files actually use: a repository slug followed by one
    or more document paths, a bare repository slug where no path was recorded, a
    SwaggerHub `owner/api/version` reference, an APIs.guru `host/version`
    reference, and a bare URL. A slug that is followed by a path belongs to that
    path rather than standing on its own.
    """
    found: list[tuple[str, str]] = []
    slug: str | None = None
    for token in (raw.strip() for raw in TICK.findall(cell)):
        if URL.match(token):
            found.append(("url", token))
        elif DOC_PATH.match(token):
            found.append(("path", f"{slug}:{token}" if slug else token))
        elif TRIPLE.match(token):
            found.append(("triple", token))
        elif SLUG.match(token):
            slug = token
            found.append(("slug", token))
    consumed: set[int] = set()
    for index, (kind, value) in enumerate(found):
        if kind != "path" or ":" not in value:
            continue
        owner = value.split(":", 1)[0]
        for back in range(index - 1, -1, -1):
            if found[back] == ("slug", owner):
                consumed.add(back)
                break
    documents = [
        value for index, (_, value) in enumerate(found) if index not in consumed
    ]
    if not documents:
        # A row naming its document without a slug or a path — an APIs.guru
        # host, say. Its first code span is the document.
        first = TICK.search(cell)
        if first:
            documents = [first.group(1).strip()]
    return documents


def region_tables(root: Path, region: str):
    """`(line number, kind, cells)` for every table row of a region's search."""
    lines = (root / REGION_DIR / f"{region}.md").read_text(encoding="utf-8").split("\n")
    try:
        start = next(
            index for index, line in enumerate(lines) if line.strip() == WITNESS_HEADING
        )
    except StopIteration:
        return
    header: list[str] | None = None
    kind: str | None = None
    for offset, line in enumerate(lines[start:], start=start + 1):
        if not line.startswith("|"):
            if line.startswith("#"):
                header = None
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split(" | ")]
        if set("".join(cells)) <= {"-", ":"}:
            continue
        if header is None:
            header = cells
            kind = {"key": "witness", "candidate": "ledger"}.get(cells[0])
            continue
        if kind:
            yield offset, kind, cells


def authoritative(root: Path) -> tuple[dict[str, str], dict[str, str]]:
    """The candidate set: `document -> where`, and `region:line -> where`."""
    documents: dict[str, str] = {}
    rows: dict[str, str] = {}
    for region in REGIONS:
        for line, kind, cells in region_tables(root, region):
            where = f"{region}.md:{line}"
            if kind == "ledger":
                if len(cells) < 5:
                    continue
                if not (
                    LICENCE_OBSTACLE.search(cells[2])
                    or LICENCE_OBSTACLE.search(cells[-1])
                ):
                    continue
                rows[where] = where
                for document in documents_in(cells[0]):
                    documents.setdefault(document, where)
            else:
                if len(cells) < 5 or cells[1].strip("`") != "witness-blocked":
                    continue
                licence = cells[4] if len(cells) == 7 else cells[3]
                if licence.strip() in ("—", "-", ""):
                    continue
                rows[where] = where
    return documents, rows


def region_keys(root: Path) -> dict[str, str]:
    """Every coverage-row key the six region files carry, to its region."""
    keys: dict[str, str] = {}
    for region in REGIONS:
        lines = (
            (root / REGION_DIR / f"{region}.md").read_text(encoding="utf-8").split("\n")
        )
        try:
            start = next(
                index for index, line in enumerate(lines) if line.strip() == "## Entries"
            )
        except StopIteration:
            continue
        for line in lines[start + 1 :]:
            if line.startswith("## "):
                break
            if not line.startswith("| "):
                continue
            cell = line.strip().strip("|").split(" | ")[0].strip().strip("`")
            if cell != "key" and re.fullmatch(r"[a-z0-9][a-z0-9.\-]*", cell):
                keys[cell] = region
    return keys


def record_rows(text: str) -> tuple[list[str], list[tuple[int, list[str]]]]:
    """The record table's header cells and its `(line number, cells)` rows."""
    lines = text.split("\n")
    try:
        start = next(
            index for index, line in enumerate(lines) if line.strip() == TABLE_HEADING
        )
    except StopIteration:
        return [], []
    header: list[str] = []
    rows: list[tuple[int, list[str]]] = []
    for offset, line in enumerate(lines[start + 1 :], start=start + 2):
        if line.startswith("## "):
            break
        if not line.startswith("| "):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split(" | ")]
        if not header:
            header = cells
            continue
        if set("".join(cells)) <= {"-", ":"}:
            continue
        rows.append((offset, cells))
    return header, rows


def check_ref(cell: str) -> str | None:
    if not FETCH.search(cell):
        return "the pinned ref names no fetch URL, so nothing says what was read"
    if not MD5.search(cell) or not BYTES.search(cell):
        return (
            "the pinned ref carries no `N bytes` and MD5 `<hash>` fingerprint of"
            " what the fetch returned"
        )
    if COMMIT.search(cell) or APIS_GURU.search(cell):
        return None
    match = NO_REF.search(cell)
    if match and len(match.group("why").strip()) >= MIN_REASON:
        return None
    return (
        "the pinned ref is neither a 40-character commit, an APIs.guru version"
        " reference, nor `no immutable ref — <why the world offers none>`"
    )


def check_fern(cell: str, command: str) -> str | None:
    if command not in cell:
        return f"names no `{command}` command, so nothing says what was run"
    if "not run" in cell:
        return (
            f"records `{command}` as `not run`: every candidate is screened at"
            " the reference its region row records"
        )
    if not EXIT.search(cell):
        return f"carries no `{command}` exit status"
    return None


def check_rows(cell: str, keys: dict[str, str]) -> str | None:
    named = KEY.findall(cell)
    unknown = [key for key in named if key not in keys]
    if unknown:
        return "names coverage row(s) no region file carries: " + ", ".join(
            sorted(set(unknown))
        )
    if not named and "none" not in cell.lower():
        return "names no coverage row and does not say `none`"
    return None


def covers(recorded: str, derived: str) -> bool:
    """Whether a record line's document is the derived one.

    A region row that names a repository without a document path derives the
    bare slug; the record resolves a path for it, so `owner/repo:path` answers
    `owner/repo`.
    """
    return recorded == derived or recorded.startswith(f"{derived}:")


def check(root: Path) -> list[str]:
    problems: list[str] = []
    record = root / RECORD
    if not record.is_file():
        return [f"{RECORD}:0 — the screening record is missing"]
    header, rows = record_rows(record.read_text(encoding="utf-8"))
    if not rows:
        return [
            f"{RECORD}:0 — no table under `{TABLE_HEADING}`, so the record"
            " records nothing"
        ]
    if header != list(COLUMNS):
        return [
            f"{RECORD}:0 — the record's columns are {header}, not"
            f" {list(COLUMNS)}; this check reads them by position"
        ]
    keys = region_keys(root)
    derived, in_scope = authoritative(root)
    seen: dict[str, int] = {}
    cited: set[str] = set()
    for line, cells in rows:
        where = f"{RECORD}:{line}"
        if len(cells) != len(COLUMNS):
            problems.append(
                f"{where} — {len(cells)} cells, not {len(COLUMNS)}: {cells[0][:60]}"
            )
            continue
        candidate, source, ref, licence, verdict, why, declares, checked, generated = (
            cells
        )
        documents = documents_in(candidate)
        if len(documents) != 1:
            problems.append(
                f"{where} — names {len(documents)} documents, not 1"
                f" ({', '.join(documents) or 'none'}); one line is one document,"
                " so a group has to be split"
            )
            continue
        document = documents[0]
        if document in seen:
            problems.append(
                f"{where} — {document} is already recorded at line {seen[document]}"
            )
        seen[document] = line
        citations = SOURCE.findall(source)
        if not citations:
            problems.append(
                f"{where} — no `<region>.md:<line>` source citation, so nothing"
                " ties the line to the region ledger it answers"
            )
        for region, cited_line in citations:
            place = f"{region}.md:{cited_line}"
            cited.add(place)
            if region not in REGIONS:
                problems.append(f"{where} — {place} is not a region file")
                continue
            body = (root / REGION_DIR / f"{region}.md").read_text(encoding="utf-8")
            body_lines = body.split("\n")
            index = int(cited_line) - 1
            if index < 0 or index >= len(body_lines):
                problems.append(f"{where} — {place} is past the end of that file")
                continue
            row = body_lines[index]
            if not row.startswith("| "):
                problems.append(f"{where} — {place} is not a table row")
                continue
            slug = document.split(":")[0]
            tail = document.split(":")[-1]
            if slug not in row and tail not in row:
                problems.append(
                    f"{where} — {place} does not name {document}, so the"
                    " provenance citation does not hold"
                )
        if not licence:
            problems.append(f"{where} — no licence recorded for {document}")
        if verdict not in VERDICTS:
            problems.append(
                f"{where} — admission is {verdict!r}, not one of"
                f" {' / '.join(VERDICTS)}"
            )
        if len(why) < MIN_REASON:
            problems.append(
                f"{where} — the admission verdict carries no reason"
                f" ({len(why)} characters)"
            )
        for problem in (
            check_ref(ref),
            check_rows(declares, keys),
            check_fern(checked, "fern check"),
            check_fern(generated, "fern generate --group python-sdk --preview"),
        ):
            if problem:
                problems.append(f"{where} — {problem}")
    for document, place in sorted(derived.items()):
        if not any(covers(recorded, document) for recorded in seen):
            problems.append(
                f"{RECORD}:0 — {place} names {document}, which no line of the"
                " record screens"
            )
    for place in sorted(in_scope):
        if place not in cited:
            problems.append(
                f"{RECORD}:0 — {place} is blocked on a licence and no line of"
                " the record cites it"
            )
    return problems


def main() -> int:
    problems = check(REPO)
    if not problems:
        return 0
    print(f"licence-rescreening: {RECORD} does not hold:", file=sys.stderr)
    for problem in problems:
        print(f"  {problem}", file=sys.stderr)
    print(
        "\nEvery line is one document's whole screening: where the region"
        " ledger records it, the reference it was fetched at, the admission"
        " verdict and its reason, what `fern check` and `fern generate`"
        " returned, and coverage rows the region files carry.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
