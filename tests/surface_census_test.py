#!/usr/bin/env python3
"""Boundary tests for `just surface-census` (`just test-surface-census`).

The census decides which OpenAPI features `docs/openapi-surface-coverage.md`
calls covered and which it calls a gap, so its whole value is that the number is
*measured*. These drive the real thing: the real
`scripts/openapi-surface-census.py`, the real vendored source documents, the real
filesystem. Nothing is mocked, and no fixture is written to make a case pass that
the corpus does not already contain.

Two things make this the gate's copy of the recipe rather than a paraphrase of it:

* The script under test is **read out of the justfile**, from the `surface-census`
  recipe itself. Renaming or rewiring the recipe fails these tests instead of
  silently leaving them testing a file nothing runs.
* Every end-to-end case passes `--vendored-only`, which is the same code path the
  unscoped recipe runs over both halves of the corpus — minus the fetch that would
  put the network inside `just check`.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FIXTURES = REPO / "tests" / "fixtures"

# The vendored sources these cases assert against, and what each one is here for:
# a 3.1 document with webhooks and a callback whose only `name:` line is a schema
# property; a document whose `type:` lines mean three different things; the only
# vendored document declaring cookie parameters; and the widest document in the
# corpus, which reuses one YAML anchor 53 times.
WEBHOOKS = "servers-webhooks"
DISCRIMINATED = "discriminated-unions"
COOKIES = "cookie-parameters"
EXHAUSTIVE = "exhaustive"
# The vendored source that keys its one Responses Object with an unquoted YAML
# integer, which is what makes it the walk's free-map-key regression witness.
UNQUOTED_STATUS = "query-parameters-openapi"


def grep_speaks_pcre() -> bool:
    """Whether this `grep` really does PCRE — asked by running one, not by reading prose.

    A grep without PCRE refuses in its own wording, and every implementation words
    it differently: BSD grep on macOS says `invalid option -- P`, a GNU grep built
    without libpcre says something else again, and either could reword next
    release. Sniffing stderr for a phrase therefore fails *open* — the guard misses,
    the command "succeeds" with no output, and an empty join set reads as "no
    limitations row names this feature", which is the miscategorisation this whole
    test exists to prevent. So probe the capability instead, with the two PCRE
    constructs the documented command actually depends on: `\\K` and a lookahead.
    """
    probe = subprocess.run(
        ["grep", "-oP", r"a\Kb(?=c)"], input="abc\n", capture_output=True, text=True
    )
    return probe.returncode == 0 and probe.stdout.strip() == "b"


def recipe_body(name: str) -> list[str]:
    """The command lines of one justfile recipe, so a rewiring fails here."""
    source = (REPO / "justfile").read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(source):
        if not re.match(rf"^{re.escape(name)}( +[\w*\"=]+)*:", line):
            continue
        body: list[str] = []
        for candidate in source[index + 1 :]:
            if not candidate.startswith(" ") and candidate.strip():
                break
            if candidate.strip():
                body.append(candidate.strip())
        return body
    raise AssertionError(f"the justfile has no `{name}` recipe")


def script_under_test() -> Path:
    """The census script as the `surface-census` recipe names it.

    Every token is considered, not just the first: the recipe leads with the
    interpreter `scripts/census-python.sh` resolves, so the script it runs is an
    argument rather than the command.
    """
    for command in recipe_body("surface-census"):
        for token in command.split():
            candidate = REPO / token
            if candidate.suffix == ".py":
                return candidate
    raise AssertionError("the `surface-census` recipe runs no Python script")


SCRIPT = script_under_test()


def load_census():
    """Import the script as a module for the loader's own unit cases."""
    spec = importlib.util.spec_from_file_location("openapi_surface_census", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    # Registered before execution because the module defines dataclasses, whose
    # type resolution reads the module out of sys.modules.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


census = load_census()


# The bound turns a wedged gate into a failing test.
CENSUS_TIMEOUT = 60


def run(*args: str) -> subprocess.CompletedProcess:
    """The real script, as its own process, exactly as the recipe invokes it."""
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=CENSUS_TIMEOUT,
    )


def rows(completed: subprocess.CompletedProcess) -> dict[tuple[str, str], int]:
    """The reported (selector, fixture) -> count, parsed off the text report."""
    parsed: dict[tuple[str, str], int] = {}
    for line in completed.stdout.splitlines():
        selector, _, remainder = line.partition("  ")
        remainder = remainder.strip()
        if remainder.startswith("("):
            continue
        fixture, _, count = remainder.rpartition("  ")
        parsed[(selector.strip(), fixture.strip())] = int(count)
    return parsed


def write_fixture(root: Path, name: str, document: str) -> Path:
    directory = root / name
    directory.mkdir(parents=True)
    (directory / "openapi.yml").write_text(textwrap.dedent(document), encoding="utf-8")
    return directory


# --- the amended settlement rule -------------------------------------------
# `docs/openapi-surface-coverage.md`'s `#### The settlement rule, as amended`
# is the prose; these are the same rule as something that fails. A row whose
# region file records a `witness-blocked` or `fern-rejected` search may be
# settled by a locally authored Fern probe and become `limitations` — so the
# recorded search, the named blocker and the recorded probe are all gates, and
# each is read here off real region-file content rather than assumed.

WITNESS_SEARCH_HEADING = "### Witness search (issue #188)"
AMENDED_ROUTE = "blocked-witness probe"
OPEN_SEARCH_ROUTE = "open-search probe"
BLOCKED_OUTCOMES = ("witness-blocked", "fern-rejected")
SEARCH_INCOMPLETE = "search-incomplete"
UNANSWERED = "unanswered"
# `fern-limitations.md`'s own `How to read a verdict` vocabulary, which is what
# "a row with a verdict" in that file means.
LEDGER_VERDICTS = (
    "implements",
    "discards",
    "ignores",
    "refuses",
    "crashes",
    "coincidence",
    "unmeasured",
)


def table_cells(line: str, width: int) -> list[str] | None:
    """One markdown table row as `width` cells, or None if the line is not one.

    `\\|` inside a cell is an escaped pipe, not a column break — one region row's
    `crozier sites` cell holds a Rust `match` pattern that uses it. An *un*escaped
    one in the last column is not so easily dismissed: `parameters.md`'s search
    row quotes a `(yaml|yml)$` regex in its query cell, and a parser demanding
    exactly `width` cells drops that row silently, which is a search going unread
    rather than a search failing. So the overflow is folded back into the last
    column, where it came from.
    """
    if not line.startswith("| "):
        return None
    cells = [
        cell.replace("\x00", "\\|").strip()
        for cell in line.replace("\\|", "\x00").strip().strip("|").split("|")
    ]
    if len(cells) < width:
        return None
    return cells[: width - 1] + ["|".join(cells[width - 1 :])]


def source_key(label: str) -> str:
    """One source's identity, so a declaration and a row's cell join on it.

    A region declares `**Vendor developer portals**` and its rows write
    `**Vendor portals:**` or `**vendor portals**`; `**APIs.guru /
    \\`openapi-directory\\`**` is written both ways too. The leading word is
    what never varies, so that is the key.
    """
    return label.strip("*: ").split()[0].strip("`").lower()


def witness_search_table(text: str) -> dict[str, list[str]]:
    """key -> the seven cells of that key's line in one region file's search table."""
    if WITNESS_SEARCH_HEADING not in text:
        return {}
    found = {}
    for line in text.split(WITNESS_SEARCH_HEADING, 1)[1].splitlines():
        cells = table_cells(line, 7)
        if cells and cells[0].startswith("`"):
            found[cells[0].strip("`")] = cells
    return found


def witness_search_outcome(row: list[str]) -> str:
    """The `outcome` cell, whose backticks two regions write and two do not."""
    return row[1].strip("`* ")


def declared_witness_sources(text: str) -> dict[str, str]:
    """The sources this region's own witness-search preamble says it searched.

    Required per region rather than from one shared list, because the regions
    genuinely searched different sets — `security` names six and `schemas`
    five — and a list pruned to the intersection would let a row delete the
    Sourcegraph evidence its own region demanded and still pass. Each region
    declares its set as the bulleted bold labels above its table, which is
    the contract this reads; a region that owns a witness-supply row and
    declares nothing fails rather than being waved through.
    """
    if WITNESS_SEARCH_HEADING not in text:
        return {}
    preamble = text.split(WITNESS_SEARCH_HEADING, 1)[1].split("\n| key | outcome", 1)[0]
    return {
        source_key(label): label
        for label in re.findall(r"^[-*] \*\*([^*]+)\*\*", preamble, re.M)
    }


def witness_sources_queried(cell: str, declared: dict[str, str]) -> dict[str, str]:
    """Each declared source's bold label in `cell`, mapped to the text under it.

    A row states its sources as bold labels in one cell, so a source's segment
    runs from its own label to the next *source* label — which is where the
    query put to it has to be. Bold spans that are not sources (a count, an
    emphasised value) are not boundaries.
    """
    spans = [
        (match.start(), match.end(), source_key(match.group(0)))
        for match in re.finditer(r"\*\*[^*]+\*\*", cell)
    ]
    found: dict[str, tuple[int, int]] = {}
    for start, end, key in spans:
        if key in declared and key not in found:
            found[key] = (start, end)
    starts = sorted(start for start, _end in found.values())
    return {
        key: cell[end : next((s for s in starts if s > start), len(cell))]
        for key, (start, end) in found.items()
    }


def unanswered_sources(cell: str, declared: dict[str, str]) -> list[str]:
    """The declared sources this record marks `unanswered` — the ones that did not answer."""
    queried = witness_sources_queried(cell, declared)
    return sorted(
        declared[name]
        for name, segment in queried.items()
        if re.search(rf"\b{UNANSWERED}\b", segment, re.I)
    )


def is_licence_identifier(span: str) -> bool:
    """Whether one code span is a licence the corpus could be refusing.

    An SPDX identifier is a single unspaced token carrying a capital or a
    version digit — `MIT`, `Apache-2.0`, `AGPL-3.0`, `NOASSERTION`. That is
    narrow on purpose: the failure this refuses is a licence blocker that quotes
    something else entirely, `fern check` or `golden`, and reads as though it had
    named a licence.
    """
    return bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.+-]*", span) and re.search(r"[A-Z0-9]", span))


def is_fern_invocation(span: str) -> bool:
    """Whether one code span is the command rather than what the command printed.

    Anything opening with the word `fern` is the invocation however it goes on —
    `fern check`, `fern generate --group python-sdk` — because Fern's own
    diagnostics do not name the tool back at the reader.
    """
    return bool(re.match(r"(?i)^\s*fern\b", span))


def is_diagnostic_text(span: str) -> bool:
    """Whether one code span is a phrase Fern printed, not a token about the run.

    A refusal quotes several things and only one of them is the diagnostic: the
    invocation, the exit status, the generator version, the pinned ref, the spec
    URL. Each of those is a single token or a command, while a diagnostic is a
    sentence — `Service requires auth, but no auth is defined.`,
    `Type name must begin with a letter`. Three words carrying letters is what
    separates the two, and it is why a refusal reading `exits` with the status
    alone in a code span names no diagnostic at all.
    """
    span = span.strip()
    if is_fern_invocation(span) or re.match(r"(?i)^https?://", span):
        return False
    return len([word for word in span.split() if re.search(r"[A-Za-z]{2}", word)]) >= 3


# The clause after a mutable ref's URL has to say what changes at that address,
# so what says it is a closed list rather than a word count: `this is a mutable
# reference` is four words restating the label and naming no change at all.
# `mutable` itself is deliberately absent from the list for that reason.
MUTABLE_CHANGE = re.compile(
    r"\b(?:chang|overwrit|overwrote|mov|replac|updat|re-?publish|rewrit|rewrote|mutat)\w*\b",
    re.I,
)


def blocker_form(evidence: str) -> str | None:
    """Which of the rule's three blocker forms this `evidence` cell names, if any.

    A blocker exists to tell a reader what would have to change for the witness to
    become registrable, so each form is recognised by that payload and never by
    its label: the label plus any code span at all is exactly the shape that lets
    a row be settled behind a blocker nobody can act on. So a licence names a
    licence and not some other quoted string, a mutable ref names the URL *and*
    what changes beneath it, and a Fern refusal names the exit status *and* the
    diagnostic Fern printed — the invocation being the one code span a refusal
    always has and the one that says nothing.
    """
    named = re.search(r"\*\*blocker:\*\*(.*)$", evidence, re.S | re.I)
    if not named:
        return None
    text = named.group(1)
    spans = re.findall(r"`([^`]+)`", text)
    if re.search(r"\bfern refusal\b", text, re.I):
        # `exit 1`, `exits **1**`, `exit status 1`: the status is what has to be
        # there, not one spelling of the word in front of it.
        status = re.search(r"\bexit\w*\b[^\d]{0,40}\d", text, re.I)
        return "fern refusal" if status and any(map(is_diagnostic_text, spans)) else None
    if re.search(r"\bmutable ref\b", text, re.I):
        url = re.search(r"`https?://[^`]+`", text)
        # A URL is not by itself mutable, so the clause saying what changes under
        # that same address is the half that carries the blocker — and saying so
        # is naming the change, not filling the space after the URL with words.
        return "mutable ref" if url and MUTABLE_CHANGE.search(text[url.end() :]) else None
    if re.search(r"\blicen[cs]e\b", text, re.I):
        if re.search(r"\bnone declared\b", text, re.I):
            return "licence"
        return "licence" if any(is_licence_identifier(span) for span in spans) else None
    return None


# What a source did *instead* of answering, as a closed list rather than a word
# count: an `evidence` cell naming an outstanding source has to say what happened
# at it, and "SwaggerHub is outstanding" restates the label and says nothing. The
# words are the ones the recorded searches in this tree actually use — a refusal,
# an unreachable endpoint, an error, a cap, or a body nobody read.
UNANSWERED_BEHAVIOUR = re.compile(
    r"\b(?:refus\w*|declin\w*|unreachab\w*|unavailab\w*|error\w*|fail\w*|"
    r"time[ds]?.?out|timeout\w*|rate.?limit\w*|limiter|unread|capp\w*|"
    r"no body search|exposes no\b|went unread)",
    re.I,
)


def outstanding_source_form(evidence: str, outstanding: list[str]) -> str | None:
    """The outstanding source this `evidence` cell names, and what it did instead.

    Route 3's counterpart to `blocker_form`. A route-3 row is licensed by a source
    that did not answer, so the cell names one — joined to the row's own recorded
    search, which is where `unanswered` is on the record — and says what happened
    at it. Naming a source the record does not mark `unanswered` is not naming an
    outstanding source, and naming one with no account of what it did instead of
    answering leaves a reader nothing to act on.
    """
    named = re.search(r"\*\*outstanding:\*\*(.*)$", evidence, re.S | re.I)
    if not named:
        return None
    text = named.group(1)
    for label in outstanding:
        hit = re.search(rf"\b{re.escape(source_key(label))}\b", text, re.I)
        if hit and UNANSWERED_BEHAVIOUR.search(text[hit.end() :]):
            return label
    return None


def states_convertible(evidence: str) -> bool:
    """Whether the cell says the row stays convertible, and to what.

    Both halves, because the word alone is a claim with no destination: a row
    stays convertible *to `golden`*, which is the category the classification
    precedence moves it to the day a witness turns up.
    """
    return bool(re.search(r"\bconvertible\b", evidence, re.I) and "`golden`" in evidence)


def ledger_verdict(key: str, ledger: str) -> str | None:
    """The verdict `fern-limitations.md` records for `key`, or None if it records none."""
    for line in ledger.splitlines():
        cells = table_cells(line, 2)
        if not cells or cells[0].strip("`") != key:
            continue
        for cell in cells[1:]:
            for verdict in LEDGER_VERDICTS:
                if re.search(rf"\b{verdict}\b", cell):
                    return verdict
    return None


def source_record_failure(label: str, segment: str) -> str | None:
    """Why one source's segment is not a record of what the search asked it.

    Two halves, and a segment carrying one of them records nothing usable: the
    query, in a code span so it can be re-run verbatim, and after it what the
    query returned — a count, or `unanswered` where the source did not answer. A
    source named with no query is a source nobody can check was really asked, and
    a query with no result is a question with no answer written down; either way
    "no witness was found" rests on that source having been read, and it has not.
    """
    query = re.search(r"`[^`]+`", segment)
    if not query:
        return f"names {label} with no query in a code span"
    if not re.search(rf"\d|\b{UNANSWERED}\b", segment[query.end() :], re.I):
        return f"names {label} with a query and no result after it"
    return None


def blocked_witness_probe_failures(
    key: str, region: str, cells: list[str], region_text: str, ledger: str
) -> list[str]:
    """Every way one row fails the amended settlement rule; empty means it conforms.

    The rule's own five gates, in the order the index states them: a recorded
    search, an outcome that licenses the route, a search that asked every source
    the region declares, a blocker in one of three forms, and a probe with a
    verdict in the ledger.
    """
    searched = witness_search_table(region_text)
    if key not in searched:
        return [
            f"{key}: settled as a {AMENDED_ROUTE} with no line in "
            f"{region}.md's `{WITNESS_SEARCH_HEADING}` table — the recorded "
            f"search is the gate, and nothing records one for this row"
        ]
    row = searched[key]
    failures = []
    outcome = witness_search_outcome(row)
    if outcome not in BLOCKED_OUTCOMES:
        failures.append(
            f"{key}: its recorded search returned `{outcome}`; only "
            f"`witness-blocked` and `fern-rejected` license a {AMENDED_ROUTE}, "
            f"because only they record a real-world witness this corpus cannot use"
        )
    declared = declared_witness_sources(region_text)
    if not declared:
        failures.append(
            f"{key}: {region}.md's `{WITNESS_SEARCH_HEADING}` section declares no "
            f"sources, so no search recorded under it can be the exhaustive one "
            f"this route requires"
        )
    else:
        queried = witness_sources_queried(row[6], declared)
        missing = sorted(declared[name] for name in set(declared) - set(queried))
        if missing:
            failures.append(
                f"{key}: its recorded search omits {missing}, which {region}.md "
                f"declares its search put to every row"
            )
        incomplete = sorted(
            reason
            for reason in (
                source_record_failure(declared[name], segment)
                for name, segment in queried.items()
            )
            if reason
        )
        if incomplete:
            failures.append(
                f"{key}: its recorded search {'; '.join(incomplete)} — every "
                f"required source is recorded with the query put to it and what "
                f"that query returned, or the search of it is not on the record"
            )
    if blocker_form(cells[4]) is None:
        failures.append(
            f"{key}: its `evidence` cell names no blocker in any of the rule's "
            f"three forms — the licence the witness carries, what makes its "
            f"reference mutable, or Fern's refusal with its exit status and "
            f"diagnostic — so nothing says what would have to change for the "
            f"witness to become registrable"
        )
    if ledger_verdict(key, ledger) is None:
        failures.append(
            f"{key}: `docs/fern-limitations.md` records no probe and no verdict "
            f"for it, so the measurement that settles it has not been taken"
        )
    return failures


def open_search_probe_failures(
    key: str, region: str, cells: list[str], region_text: str, ledger: str
) -> list[str]:
    """Every way one row fails route 3 of the settlement rule; empty means it conforms.

    Route 3 settles a row whose recorded search found no usable witness and left a
    required source unanswered. Its gates, in the order the index states them: a
    recorded search, an outcome other than `witness-found` — a witness this corpus
    can register is route 1's to settle — an outstanding source on that record and
    named in the `evidence` cell with what it did instead of answering, the
    statement that the row stays convertible, and a probe with a verdict in the
    ledger.
    """
    searched = witness_search_table(region_text)
    if key not in searched:
        return [
            f"{key}: settled as an {OPEN_SEARCH_ROUTE} with no line in "
            f"{region}.md's `{WITNESS_SEARCH_HEADING}` table — the outstanding "
            f"source this route rests on is recorded there, and nothing records "
            f"a search for this row at all"
        ]
    row = searched[key]
    failures = []
    outcome = witness_search_outcome(row)
    if outcome == "witness-found":
        failures.append(
            f"{key}: its recorded search returned `witness-found`, so the corpus "
            f"can register that document; route 1 is what settles that, and an "
            f"{OPEN_SEARCH_ROUTE} may not stand in for a golden"
        )
    declared = declared_witness_sources(region_text)
    if not declared:
        failures.append(
            f"{key}: {region}.md's `{WITNESS_SEARCH_HEADING}` section declares no "
            f"sources, so no source of its can be the outstanding one this route "
            f"rests on"
        )
    else:
        outstanding = unanswered_sources(row[6], declared)
        if not outstanding:
            failures.append(
                f"{key}: its recorded search marks no required source "
                f"`{UNANSWERED}`, so it names no outstanding source — a search "
                f"every source answered licenses route 1 or route 2 on what it "
                f"found, never an {OPEN_SEARCH_ROUTE}"
            )
        elif outstanding_source_form(cells[4], outstanding) is None:
            failures.append(
                f"{key}: its `evidence` cell names no outstanding source after "
                f"`outstanding:` — one of {outstanding}, which its own recorded "
                f"search marks `{UNANSWERED}`, together with what that source did "
                f"instead of answering"
            )
    if not states_convertible(cells[4]):
        failures.append(
            f"{key}: its `evidence` cell does not say the row stays convertible "
            f"to `golden`, so nothing says a witness found later reopens it "
            f"rather than the probe closing it for good"
        )
    if ledger_verdict(key, ledger) is None:
        failures.append(
            f"{key}: `docs/fern-limitations.md` records no probe and no verdict "
            f"for it, so the measurement that settles it has not been taken"
        )
    return failures


def unread_source_failures(
    key: str, region: str, row: list[str], declared: dict[str, str]
) -> list[str]:
    """A search claiming absence while a source it required did not answer.

    `none-found` is a claim about the world, and it is only as good as the set of
    sources that answered. A record naming one of them `unanswered` has not asked
    the world, so the rule spells that `search-incomplete` and this refuses the
    other spelling — which is what keeps an unread source from becoming evidence
    of absence.
    """
    outstanding = unanswered_sources(row[6], declared)
    if outstanding and witness_search_outcome(row) == "none-found":
        return [
            f"{key}: {region}.md records {outstanding} as `{UNANSWERED}` while "
            f"the row reads `none-found`; a search a required source did not "
            f"answer is `{SEARCH_INCOMPLETE}`, not evidence of absence"
        ]
    return []


class RecipeWiringTests(unittest.TestCase):
    """The gate must run this file, and this file must test the recipe's script."""

    def test_the_unscoped_recipe_fetches_the_corpus_then_censuses_it(self) -> None:
        self.assertEqual(
            [
                "./scripts/fetch-corpus.sh",
                '"$(./scripts/census-python.sh)" ./scripts/openapi-surface-census.py "$@"',
            ],
            recipe_body("surface-census"),
        )
        self.assertTrue(SCRIPT.is_file(), SCRIPT)

    def test_the_gate_runs_this_file_offline(self) -> None:
        self.assertEqual(
            [f'"$(./scripts/census-python.sh)" tests/{Path(__file__).name}'],
            recipe_body("test-surface-census"),
        )
        check = next(
            line for line in (REPO / "justfile").read_text(encoding="utf-8").splitlines()
            if line.startswith("check:")
        )
        self.assertIn("test-surface-census", check.split())


class GrammarContractTests(unittest.TestCase):
    """The doc states the selector grammar; the script implements it. Pin them together.

    Six region passes classify features against
    `docs/openapi-surface-coverage.md`'s closed lists, so a list that drifted from
    the walk would silently invalidate their evidence. These re-derive the doc's
    lists and compare them to the tables the census actually walks.
    """

    DOC = REPO / "docs" / "openapi-surface-coverage.md"

    def backticked(self, start: str, end: str) -> set[str]:
        text = self.DOC.read_text(encoding="utf-8")
        self.assertIn(start, text, f"the grammar section no longer says {start!r}")
        body = text.split(start, 1)[1].split(end, 1)[0]
        return set(re.findall(r"`([A-Za-z][A-Za-z.]*)`", body))

    def test_the_documented_anchor_kinds_are_the_ones_that_head_a_selector(self) -> None:
        documented = self.backticked("- **Anchor kinds head their own selector.**", "- **")
        self.assertEqual(
            {name for name, kind in census.OBJECTS.items() if kind.anchor}, documented
        )

    def test_the_documented_extending_kinds_are_the_ones_that_extend_a_selector(self) -> None:
        documented = self.backticked(
            "- **Extending kinds append to their parent's selector under the field that holds",
            "So a License",
        )
        self.assertEqual(
            {name for name, kind in census.OBJECTS.items() if not kind.anchor}, documented
        )

    def test_the_documented_valued_fields_are_the_ones_that_emit_a_value(self) -> None:
        documented = self.backticked("themselves a closed list:", "\n\nA **count**")
        self.assertEqual(census.VALUED, documented)

    def test_the_documented_predicate_selectors_are_the_ones_the_script_declares(self) -> None:
        """The third kind of selector: `<selector>:<predicate>`.

        The list lives in the script and is restated in the grammar section, so a
        member added to one and not the other has to fail here — the way the
        valued-field list above is already reconciled.
        """
        text = self.DOC.read_text(encoding="utf-8")
        start = "A shape the two kinds above cannot express emits a **predicate selector**,"
        self.assertIn(start, text, "the grammar section documents no predicate selector")
        body = text.split(start, 1)[1].split("A predicate selector is a selector", 1)[0]
        # A predicate spelling may carry a value of its own — `schema.type:primary=array`
        # names which member of a `type` array the arm reads, which is a position
        # rather than a presence — so the pattern admits one, and the `=` does not
        # make the spelling a valued selector over a field nothing declares. It
        # admits a `$` too, because the field a pointer-form predicate reads is
        # spelled `$ref`: the gate widens to the spelling rather than the spelling
        # bending to the gate.
        documented = set(
            re.findall(r"`([A-Za-z][A-Za-z.$]*:[a-z-]+(?:=[A-Za-z0-9-]+)?)`", body)
        )
        self.assertEqual(set(census.PREDICATES), documented)
        stated = re.search(
            r"The predicates are themselves a closed list of\s+(\d+)",
            text,
        )
        self.assertIsNotNone(stated, "the grammar no longer states how many predicates there are")
        self.assertEqual(len(census.PREDICATES), int(stated.group(1)))

    def test_the_documented_member_only_readings_are_the_ones_the_script_declares(self) -> None:
        """The member-only list lives in the script and is restated in the grammar.

        The same two-way reconciliation the predicate and conjunction lists get. A
        reading added to `MEMBER_ONLY_PREDICATES` and not to the grammar section
        fails here, and so does one documented and not declared — which keeps a
        reading from being quietly promoted back to a selector, or quietly
        dropped, without the section that explains why it is neither saying so.
        """
        text = self.DOC.read_text(encoding="utf-8")
        start = "##### The member-only readings"
        self.assertIn(start, text, "the grammar section documents no member-only reading")
        body = text.split(start, 1)[1].split("\nA shape that is a **combination**", 1)[0]
        documented = set(
            re.findall(r"^- `([A-Za-z][A-Za-z.$]*:[a-z-]+(?:=[A-Za-z]+)?)`", body, re.M)
        )
        self.assertEqual(set(census.MEMBER_ONLY_PREDICATES), documented)
        stated = re.search(r"They are a\s+closed list of (\d+)", body)
        self.assertIsNotNone(stated, "the section no longer states how many there are")
        self.assertEqual(len(census.MEMBER_ONLY_PREDICATES), int(stated.group(1)))

    def test_no_member_only_reading_is_also_a_declared_selector(self) -> None:
        """The two lists are disjoint, and a member-only reading is not askable."""
        self.assertEqual(
            set(), set(census.MEMBER_ONLY_PREDICATES) & set(census.PREDICATES)
        )
        self.assertEqual(
            set(), set(census.MEMBER_ONLY_PREDICATES) & set(census.CONJUNCTIONS)
        )
        for reading in sorted(census.MEMBER_ONLY_PREDICATES):
            with self.subTest(reading=reading):
                self.assertIsNotNone(
                    census.selector_error(reading),
                    f"{reading} is member-only and must be refused as a --selector",
                )

    # The predicates that compare one document's own values against each other
    # rather than reading the node in front of the walk. The script names them in
    # its own `PREDICATES` header comment and the grammar section names them in
    # prose; this list is the third statement of the same partition, and the case
    # below holds all three together. A predicate added to the closed list is
    # node-local unless it is here.
    DOCUMENT_COMPARING_PREDICATES = frozenset({
        "operation.operationId:duplicate",
        "openapi.paths:normalized-collision",
        "components.schemas:normalized-collision",
        "schema.$ref:undeclared-component-head",
        "schema.$ref:resolves-to-component",
        "schema.oneOf:discriminated-union",
        "schema.anyOf:discriminated-union",
        "schema.discriminator:inheritance-union",
    })

    def test_the_documented_node_local_split_partitions_the_predicate_list(self) -> None:
        """The two counts the grammar states about its own predicates, recomputed.

        `test_the_documented_predicate_selectors_are_the_ones_the_script_declares`
        holds the set and its total; this holds the *split* the paragraph after it
        states — how many predicates are node-local and how many compare one
        document's values against each other. Both are spelled as words, and they
        have to partition the closed list, so a predicate added to one family and
        counted in neither fails here. Nothing else derives the split: the
        paragraph drifted once already, when a node-local predicate was added and
        the word before "of the 26" stayed put.
        """
        words = {
            "Twenty": 20, "Twenty-one": 21, "Twenty-two": 22,
            "Twenty-three": 23, "Twenty-four": 24, "Twenty-five": 25,
            "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        }
        text = self.DOC.read_text(encoding="utf-8")
        stated = re.search(
            r"\*\*([A-Z][a-z-]+) of the (\d+) are node-local\*\*", text
        )
        self.assertIsNotNone(stated, "the grammar no longer states its node-local count")
        self.assertEqual(len(census.PREDICATES), int(stated.group(2)))
        body = text.split(stated.group(0), 1)[1].split("\n\nA predicate selector", 1)[0]
        other = re.search(r"The other\n?([a-z-]+) —", body)
        self.assertIsNotNone(other, "the grammar no longer counts the other family")
        node_local = words[stated.group(1)]
        comparing = words[other.group(1)]
        self.assertEqual(
            len(census.PREDICATES),
            node_local + comparing,
            "the two stated families do not partition the closed list",
        )
        self.assertEqual(len(self.DOCUMENT_COMPARING_PREDICATES), comparing)
        for selector in sorted(self.DOCUMENT_COMPARING_PREDICATES):
            with self.subTest(selector=selector):
                self.assertIn(selector, census.PREDICATES)
                self.assertIn(
                    f"`{selector}`",
                    body,
                    f"{selector} is document-comparing and the paragraph does not name it",
                )

    # ------------------------------------------------------------------
    # The fourth kind of selector: `<member>&<member>` and `<group>><group>`
    # ------------------------------------------------------------------

    CONJUNCTION_LIST = (
        "The conjunctions are themselves a closed list of",
        "A conjunction selector is a selector like any other",
    )
    CASE_ANALYSIS = (
        "### The six blind regions of `src/ir.rs`, case by case",
        "### Refreshing the coverage snapshot",
    )

    def documented_conjunctions(self) -> dict[str, str]:
        """The closed list as the grammar section restates it: spelling -> sentence."""
        text = self.DOC.read_text(encoding="utf-8")
        start, end = self.CONJUNCTION_LIST
        self.assertIn(start, text, "the grammar section documents no conjunction selector")
        body = text.split(start, 1)[1].split(end, 1)[0]
        found: dict[str, str] = {}
        for bullet in body.split("\n- `")[1:]:
            spelling, _, sentence = " ".join(bullet.split()).partition("` — ")
            self.assertTrue(sentence, f"the {spelling!r} bullet says nothing about what it counts")
            found[spelling] = sentence.rstrip(".")
        return found

    def case_rows(self) -> dict[str, list[list[str]]]:
        """The case analysis as `#### function` -> its numbered rows' cells."""
        text = self.DOC.read_text(encoding="utf-8")
        start, end = self.CASE_ANALYSIS
        self.assertIn(start, text, "the index carries no case analysis of the blind regions")
        body = text.split(start, 1)[1].split(end, 1)[0]
        found: dict[str, list[list[str]]] = {}
        function = None
        for line in body.splitlines():
            heading = re.match(r"^#### `([a-z_]+)`$", line)
            if heading:
                function = heading.group(1)
                found[function] = []
                continue
            # A case number may carry a letter: one arm read at the grain the
            # selectors need, either its two `x.or(y)` spellings or one disjunct
            # of a condition joined by `||`.
            row = re.match(r"^\| \d+[a-z]? \| ", line.replace("\\|", "\x00"))
            if row and function is not None:
                cells = [c.replace("\x00", "\\|").strip() for c in
                         line.replace("\\|", "\x00").strip().strip("|").split("|")]
                self.assertEqual(3, len(cells), f"{function}: {line}")
                found[function].append(cells)
        return found

    def documented_holes(self) -> set[str]:
        text = self.DOC.read_text(encoding="utf-8")
        start, end = self.CASE_ANALYSIS
        body = text.split(start, 1)[1].split(end, 1)[0]
        return set(re.findall(r"^\| \*\*(H-[a-z-]+)\*\* \|", body, re.M))

    def test_the_documented_conjunction_selectors_are_the_ones_the_script_declares(self) -> None:
        """The fourth kind of selector: a combination of fields, not one field.

        Declared in the script and restated in the grammar section, spelling *and*
        sentence, so an entry added to one and not the other fails here — the way
        the valued-field and predicate lists above are already reconciled.
        """
        self.assertEqual(census.CONJUNCTIONS, self.documented_conjunctions())
        stated = re.search(
            r"closed list of (\d+), declared in", self.DOC.read_text(encoding="utf-8")
        )
        self.assertIsNotNone(stated, "the grammar no longer states how many conjunctions there are")
        self.assertEqual(len(census.CONJUNCTIONS), int(stated.group(1)))

    def test_every_conjunction_is_spelled_in_its_one_canonical_order(self) -> None:
        """One shape, one name: two spellings of one conjunction would be two rows."""
        for spelling in census.CONJUNCTIONS:
            with self.subTest(spelling=spelling):
                self.assertEqual(spelling, census.canonical_conjunction(spelling))

    def test_the_case_analysis_covers_the_six_blind_functions_of_the_rule(self) -> None:
        """The rule names six functions; the derivation has to work all six."""
        rule = self.DOC.read_text(encoding="utf-8").split(
            "> A conjunction is worth enumerating", 1
        )[1].split("\n\n", 1)[0]
        named = set(re.findall(r"`([a-z_]+)`", rule))
        self.assertEqual(6, len(named), f"the rule names {sorted(named)}")
        self.assertEqual(named, set(self.case_rows()))

    def test_every_case_carries_one_declared_selector_or_one_declared_hole(self) -> None:
        """No case in neither state, and none in both."""
        holes = self.documented_holes()
        for function, rows_of in self.case_rows().items():
            self.assertTrue(rows_of, f"{function} lists no case")
            for cells in rows_of:
                with self.subTest(function=function, case=cells[0]):
                    verdict = cells[2]
                    hole = re.fullmatch(r"\*\*(H-[a-z-]+)\*\*", verdict)
                    selector = re.fullmatch(r"`(.+)`", verdict)
                    self.assertTrue(hole or selector, f"{verdict!r} is neither")
                    if hole:
                        self.assertIn(hole.group(1), holes)
                    else:
                        # A conjunction, or — where the arm reads one Paths Object
                        # key and opens no schema — the predicate that reads it.
                        self.assertIn(
                            selector.group(1),
                            set(census.CONJUNCTIONS) | set(census.PREDICATES),
                        )

    def test_every_declared_conjunction_is_read_off_a_case_of_a_blind_region(self) -> None:
        """The list is bounded by the generator's branches, not by what `&` can spell."""
        derived = {
            re.fullmatch(r"`(.+)`", cells[2]).group(1)
            for rows_of in self.case_rows().values()
            for cells in rows_of
            if re.fullmatch(r"`(.+)`", cells[2])
        }
        self.assertEqual(set(census.CONJUNCTIONS), derived & set(census.CONJUNCTIONS))
        self.assertEqual(set(), derived - set(census.CONJUNCTIONS) - set(census.PREDICATES))

    # ------------------------------------------------------------------
    # The case table, and what ties it to the code it is a reading of
    # ------------------------------------------------------------------

    BLIND_FUNCTIONS = (
        "resolve_schema_pointer",
        "nested_array_element",
        "hoist_union_variant",
        "prop_type_ref",
        "ref_to_class",
        "path_group",
    )

    @staticmethod
    def function_body(name: str) -> list[str]:
        """One `fn` of `src/ir.rs`, brace-matched from its header line.

        The same reading `docs/openapi-surface-coverage.md`'s per-function
        attribution script makes, and the only definition of "this function's
        body" the honesty check below has.
        """
        lines = (REPO / "src" / "ir.rs").read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines):
            if not re.search(rf"\bfn {re.escape(name)}\s*[(<]", line):
                continue
            depth, started = 0, False
            for cursor in range(index, len(lines)):
                for char in lines[cursor]:
                    if char == "{":
                        depth, started = depth + 1, True
                    elif char == "}":
                        depth -= 1
                        if started and depth == 0:
                            return lines[index : cursor + 1]
        raise AssertionError(f"src/ir.rs declares no fn {name}")

    @classmethod
    def function_digest(cls, name: str) -> str:
        """One function body's digest: blank lines and `//` lines dropped, runs collapsed."""
        kept = [
            " ".join(line.split())
            for line in cls.function_body(name)
            if line.strip() and not line.strip().startswith("//")
        ]
        return hashlib.sha256("\n".join(kept).encode("utf-8")).hexdigest()[:16]

    def test_the_case_table_and_the_case_analysis_carry_the_same_cases(self) -> None:
        """The two statements of one derivation, reconciled in both directions.

        `scripts/openapi-surface-census.py`'s `CASES` is the machine-readable
        table the residual selectors are composed from; the case analysis in
        `docs/openapi-surface-coverage.md` restates it for a reader. A case in
        one and not the other fails here, and so does a case whose verdict
        differs — which is what stops the residual being composed from a table
        nobody reads while a reader takes the size of the instrument off a table
        nothing composes.
        """
        documented = {
            function: [(cells[0], cells[2].strip("`") if cells[2].startswith("`")
                        else re.fullmatch(r"\*\*(H-[a-z-]+)\*\*", cells[2]).group(1))
                       for cells in rows_of]
            for function, rows_of in self.case_rows().items()
        }
        declared = {
            function: [(case.number, census.case_verdict(function, case)) for case in cases]
            for function, cases in census.CASES.items()
        }
        self.assertEqual(set(self.BLIND_FUNCTIONS), set(declared))
        self.assertEqual(declared, documented)

    def test_every_case_of_the_table_is_well_formed(self) -> None:
        """A case is a selector or a hole, never both and never neither.

        And every block a case names is declared, every case a block's residual
        is scoped to sits in that block, and a residual's own selector is
        composed rather than written — which is what makes adding a case to the
        table change what the residual matches with no selector text edited.
        """
        for function, cases in census.CASES.items():
            numbers = [case.number for case in cases]
            self.assertEqual(len(numbers), len(set(numbers)), f"{function} repeats a case")
            for case in cases:
                with self.subTest(function=function, case=case.number):
                    stated = [
                        field
                        for field in (case.selector, case.hole, case.residual)
                        if field is not None
                    ]
                    self.assertEqual(
                        1,
                        len(stated),
                        "a case carries exactly one of a selector, a hole and a "
                        "residual sentence",
                    )
                    if case.block is not None:
                        self.assertIn(case.block, census.BLOCKS)
                    if case.opens is not None:
                        self.assertIn(case.opens, census.BLOCKS)
                    if case.residual is not None:
                        self.assertIsNotNone(case.block)
                        self.assertTrue(case.residual, "a residual publishes a sentence")

    def test_the_case_table_is_a_reading_of_the_functions_it_names(self) -> None:
        """The honesty check: a branch added, removed or edited without re-derivation.

        The table is a reading of six functions of `src/ir.rs` and nothing else
        ties it to them, so each function's normalized body carries a digest in
        the table. Any of the three changes moves the body and fails here; what
        the digest cannot do is say which case moved, and it fires on a change
        that moves no branch at all. Both limits are stated in
        `docs/openapi-surface-coverage.md` rather than left implicit.
        """
        self.assertEqual(set(self.BLIND_FUNCTIONS), set(census.BLIND_FUNCTION_DIGESTS))
        for name in self.BLIND_FUNCTIONS:
            with self.subTest(function=name):
                self.assertEqual(
                    census.BLIND_FUNCTION_DIGESTS[name],
                    self.function_digest(name),
                    f"src/ir.rs's {name} changed; re-derive its rows of the case "
                    "table in scripts/openapi-surface-census.py and of the case "
                    "analysis in docs/openapi-surface-coverage.md, then re-pin "
                    "the digest",
                )

    def test_the_digest_moves_when_a_branch_of_a_named_function_moves(self) -> None:
        """The check above, proved against a branch this case adds and removes.

        A digest nobody has seen fail is a digest that might be computed over
        the wrong span, so this one takes the real `nested_array_element` body,
        inserts one branch into it, and asserts the digest is not the pinned
        one — the failure the check exists to produce, induced on purpose.
        """
        lines = self.function_body("nested_array_element")
        self.assertTrue(lines[0].strip().startswith("fn nested_array_element"))
        edited = [lines[0], "        if items.pattern.is_some() { return None; }", *lines[1:]]
        kept = [
            " ".join(line.split())
            for line in edited
            if line.strip() and not line.strip().startswith("//")
        ]
        self.assertNotEqual(
            census.BLIND_FUNCTION_DIGESTS["nested_array_element"],
            hashlib.sha256("\n".join(kept).encode("utf-8")).hexdigest()[:16],
        )

    def test_the_case_analysis_states_the_totals_its_own_rows_add_up_to(self) -> None:
        """The paragraph a reader takes the size of this instrument from.

        The exactness rule publishes how many of the cases below carry a selector
        and how many name the extension that would close them; both are counted
        off the rows themselves, so a case added, closed or reopened without the
        sentence moving fails here.
        """
        words = {
            0: "zero", 1: "one", 3: "three", 4: "four", 5: "five", 7: "seven", 8: "eight",
            9: "nine", 94: "ninety-four", 95: "ninety-five",
            15: "fifteen", 20: "twenty", 23: "twenty-three",
            28: "twenty-eight", 36: "thirty-six", 40: "forty", 50: "fifty",
            60: "sixty", 69: "sixty-nine", 74: "seventy-four", 76: "seventy-six",
            78: "seventy-eight", 83: "eighty-three", 89: "eighty-nine",
        }
        rows_of = [cells for rows in self.case_rows().values() for cells in rows]
        selectors = [c for c in rows_of if re.fullmatch(r"`(.+)`", c[2])]
        holes = [c for c in rows_of if re.fullmatch(r"\*\*(H-[a-z-]+)\*\*", c[2])]
        self.assertEqual(len(rows_of), len(selectors) + len(holes))
        stated = re.search(
            r"\b([A-Za-z-]+) of the\n  ([a-z-]+) cases below survive this test; the "
            r"other ([a-z-]+) names? the\n  extension that would close (?:them|it)",
            self.DOC.read_text(encoding="utf-8"),
        )
        self.assertIsNotNone(stated, "the exactness rule no longer states its own totals")
        self.assertEqual(
            (words[len(selectors)], words[len(rows_of)], words[len(holes)]),
            tuple(group.lower() for group in stated.groups()),
        )
        kinds = re.search(
            r"an enumeration hole of ([a-z-]+) remaining kinds?",
            self.DOC.read_text(encoding="utf-8"),
        )
        self.assertIsNotNone(kinds, "the case analysis no longer states its hole-kind count")
        self.assertEqual(words[len(self.documented_holes())], kinds.group(1))

    def test_each_region_file_repeats_the_index_s_boundary_verbatim(self) -> None:
        """Six copies of the region boundaries; the index's table is the original."""
        text = self.DOC.read_text(encoding="utf-8")
        owns = {
            cells[1].strip("`"): cells[3]
            for line in text.splitlines()
            if line.startswith("| `") and "openapi-surface/" in line
            for cells in [[cell.strip() for cell in line.split("|")]]
        }
        self.assertEqual(6, len(owns), "the index no longer lists six regions")
        for region, boundary in sorted(owns.items()):
            with self.subTest(region=region):
                body = (REPO / "docs" / "openapi-surface" / f"{region}.md").read_text(
                    encoding="utf-8"
                )
                self.assertIn("\n## Scope\n", body, f"{region}.md has no ## Scope section")
                scope = body.split("\n## Scope\n", 1)[1].split("\n## ", 1)[0]
                self.assertEqual(
                    " ".join(boundary.split()).rstrip("."),
                    " ".join(scope.split()).rstrip("."),
                    f"{region}.md's ## Scope is not the index's `owns` cell",
                )

    def test_the_stated_corpus_sizes_are_the_measured_ones(self) -> None:
        """31 vendored / 93 link-ok / 124 registered is restated in prose; measure it."""
        vendored = census.registered_sources(FIXTURES, REPO / ".local" / "corpus", True)
        registered = census.registered_sources(FIXTURES, REPO / ".local" / "corpus", False)
        counts = (len(vendored), len(registered) - len(vendored), len(registered))
        doc = self.DOC.read_text(encoding="utf-8")
        stated = re.search(
            r"the (\d+) vendored\n`tests/fixtures/<name>/openapi\.\*` documents, and the (\d+) `link-ok`", doc
        )
        self.assertIsNotNone(stated, "the instrument section no longer states the corpus split")
        self.assertEqual(counts[:2], (int(stated.group(1)), int(stated.group(2))))
        script = SCRIPT.read_text(encoding="utf-8")
        in_script = re.search(r"and (\d+) of the (\d+) registered sources are `link-ok`", script)
        self.assertIsNotNone(in_script, "the script's docstring no longer states the corpus split")
        self.assertEqual(
            (counts[1], counts[2]), (int(in_script.group(1)), int(in_script.group(2)))
        )

    def test_the_verdict_vocabulary_is_the_one_fern_limitations_defines(self) -> None:
        """A `limitations` row quotes that file's verdict; the enum is its property."""
        ledger = (REPO / "docs" / "fern-limitations.md").read_text(encoding="utf-8")
        section = ledger.split("## How to read a verdict", 1)[1].split("\nA verdict is", 1)[0]
        defined = re.findall(r"^\| \*\*(\w+)\*\* \|", section, re.M)
        self.assertGreater(len(defined), 3, "the verdict table no longer parses")
        quoted = self.backticked("section spells them (", ") —")
        self.assertEqual(set(defined), quoted)

    def test_the_documented_join_command_still_finds_the_limitations_keys(self) -> None:
        """The key-extraction recipe encodes that file's column layout.

        Its failure mode is an EMPTY list, not an error, so a region would join on
        nothing and read it as "no limitations row names this feature" — the wrong
        category. This runs the documented pattern, and where GNU grep is present
        (the Linux gate leg) runs the command itself and requires the same answer.
        """
        doc = self.DOC.read_text(encoding="utf-8")
        pattern = re.search(r"^grep -oP '(.+)' docs/fern-limitations\.md", doc, re.M)
        self.assertIsNotNone(pattern, "the index no longer documents the join command")
        ledger = (REPO / "docs" / "fern-limitations.md").read_text(encoding="utf-8")
        # The same expression with PCRE's \K — which Python's re does not have —
        # rewritten as the capture group it is shorthand for.
        self.assertIn("\\K", pattern.group(1), "the documented pattern lost its \\K anchor")
        before, _, after = pattern.group(1).partition("\\K")
        keys = set(re.findall(f"{before}({after})", ledger, re.M))
        self.assertGreater(len(keys), 40, "the documented pattern extracts almost no keys")
        for key in keys:
            self.assertRegex(key, r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

        if not grep_speaks_pcre():
            self.skipTest("this grep has no PCRE support, so the command cannot run here")
        grep = subprocess.run(
            ["grep", "-oP", pattern.group(1), "docs/fern-limitations.md"],
            cwd=REPO, capture_output=True, text=True,
        )
        # Fail loudly on a refusal rather than comparing against empty output:
        # every way this command can go wrong has to be a red, not a quiet zero.
        self.assertEqual(0, grep.returncode, grep.stderr)
        self.assertEqual(keys, set(grep.stdout.split()))

    def test_bodies_media_ledger_citations_match_the_keyed_verdicts(self) -> None:
        """A cited verdict is the ledger's exact text, not a stale paraphrase."""
        region = (
            REPO / "docs" / "openapi-surface" / "bodies-media.md"
        ).read_text(encoding="utf-8")
        citations = re.findall(
            r"Ledger `(?P<key>[A-Za-z0-9._-]+)`: `(?P<verdict>.*?)`\.", region
        )
        self.assertGreater(len(citations), 10, "bodies-media.md has almost no Ledger citations")

        ledger = (REPO / "docs" / "fern-limitations.md").read_text(encoding="utf-8")
        verdicts: dict[str, str] = {}
        for line in ledger.splitlines():
            cells = [cell.strip() for cell in line.split("|")]
            if len(cells) < 6 or not re.fullmatch(r"`[A-Za-z0-9._-]+`", cells[1]):
                continue
            if not cells[2].isdigit() or not cells[3].isdigit():
                continue
            verdicts[cells[1].strip("`")] = cells[4]

        failures = []
        for key, cited in citations:
            if key not in verdicts:
                failures.append(f"missing ledger key: {key}")
            elif not verdicts[key]:
                failures.append(f"missing ledger verdict for key: {key}")
            elif cited != verdicts[key]:
                failures.append(
                    f"verdict mismatch for {key}: cited {cited!r}, ledger has {verdicts[key]!r}"
                )
        self.assertFalse(failures, "\n" + "\n".join(failures))

    @unittest.skipUnless(os.name == "posix", "the shim is a /bin/sh script")
    def test_the_join_command_is_skipped_not_failed_where_grep_lacks_pcre(self) -> None:
        """Exercise the join case with a real `grep` that refuses `-P`."""
        real = shutil.which("grep")
        if real is None:
            self.skipTest("no grep on PATH to fall back to")
        case = (
            f"{type(self).__name__}"
            ".test_the_documented_join_command_still_finds_the_limitations_keys"
        )
        with tempfile.TemporaryDirectory() as shim:
            refuser = Path(shim) / "grep"
            refuser.write_text(
                textwrap.dedent(
                    f"""\
                    #!/bin/sh
                    for arg in "$@"; do
                      case "$arg" in
                        -*P*) echo "grep: invalid option -- P" >&2; exit 2;;
                      esac
                    done
                    exec {real} "$@"
                    """
                ),
                encoding="utf-8",
            )
            refuser.chmod(0o755)
            run = subprocess.run(
                [sys.executable, str(Path(__file__).resolve()), case],
                cwd=REPO, capture_output=True, text=True,
                env={**os.environ, "PATH": f"{shim}{os.pathsep}{os.environ['PATH']}"},
            )
        self.assertEqual(0, run.returncode, run.stderr)
        self.assertIn("skipped=1", run.stderr)

    def test_the_region_files_carry_the_agreed_table_header(self) -> None:
        """Six files, one skeleton: the regions have to compose into one table."""
        header = (
            "| key | oas | spec location | category | evidence | crozier sites | "
            "why bytes could move | settlement |"
        )
        self.assertIn(header, self.DOC.read_text(encoding="utf-8"))
        regions = sorted(p.stem for p in (REPO / "docs" / "openapi-surface").glob("*.md"))
        self.assertEqual(
            ["bodies-media", "document-paths", "oas31-extensions", "parameters",
             "schemas", "security"],
            regions,
        )
        for region in regions:
            with self.subTest(region=region):
                text = (REPO / "docs" / "openapi-surface" / f"{region}.md").read_text(
                    encoding="utf-8"
                )
                self.assertIn(header, text)
                self.assertIn(f"openapi-surface/{region}.md", self.DOC.read_text(encoding="utf-8"))
                for section in ("## Scope", "## Entries", "## Method notes"):
                    self.assertIn(section, text)


class CensusReportTests(unittest.TestCase):
    """What the instrument answers: who declares a feature, and who does not."""

    def test_a_declared_feature_names_its_sources_and_its_declaration_count(self) -> None:
        completed = run("--vendored-only", "--selector", "operation.callbacks")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({("operation.callbacks", WEBHOOKS): 1}, rows(completed))
        self.assertIn("32 vendored", completed.stderr)

    def test_a_valued_selector_reports_one_member_of_a_closed_set(self) -> None:
        completed = run("--vendored-only", "--selector", "parameter.in=cookie")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({("parameter.in=cookie", COOKIES): 2}, rows(completed))

    def test_a_feature_no_registered_source_declares_is_reported_as_absent(self) -> None:
        """The evidence a `gap` row cites has to be printed, not inferred from silence."""
        completed = run("--vendored-only", "--selector", "pathItem.trace")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({}, rows(completed))
        self.assertIn("pathItem.trace", completed.stdout)
        self.assertIn("(declared by no registered source)", completed.stdout)

        as_json = run("--vendored-only", "--json", "--selector", "pathItem.trace")
        payload = json.loads(as_json.stdout)
        self.assertEqual([], payload["rows"])
        self.assertEqual(["pathItem.trace"], payload["absent_selectors"])

    def test_every_declaration_site_counts_including_a_reused_yaml_anchor(self) -> None:
        """`security: *ref_0` declares the field again; the census counts both uses."""
        source = (FIXTURES / EXHAUSTIVE / "openapi.yml").read_text(encoding="utf-8")
        written = len(re.findall(r"^ *security:", source, re.M))
        anchored = len(re.findall(r"^ *security: \*", source, re.M))
        self.assertGreater(anchored, 1, "the exhaustive fixture no longer reuses an anchor")
        completed = run("--vendored-only", "--fixture", EXHAUSTIVE, "--selector", "operation.security")
        self.assertEqual({("operation.security", EXHAUSTIVE): written}, rows(completed))

    def test_a_vendor_extension_is_reported_under_the_object_that_carries_it(self) -> None:
        """The `oas31-extensions` region is built on this: `x-` keys are census rows."""
        counted = rows(run("--vendored-only", "--selector", "operation.x-fern-audiences"))
        self.assertEqual(
            {
                ("operation.x-fern-audiences", "audience-filter"): 2,
                ("operation.x-fern-audiences", "audience-filter-strict"): 2,
            },
            counted,
        )
        for fixture, count in counted.items():
            with self.subTest(fixture=fixture[1]):
                source = (FIXTURES / fixture[1] / "openapi.yml").read_text(encoding="utf-8")
                self.assertEqual(count, len(re.findall(r"^ *x-fern-audiences:", source, re.M)))

    def test_the_document_version_is_censused_as_its_major_minor(self) -> None:
        """3.0-vs-3.1 is the delta a region asks about; the patch level is noise."""
        counted = rows(run("--vendored-only", "--selector", "openapi.openapi=3.1"))
        self.assertIn(("openapi.openapi=3.1", WEBHOOKS), counted)
        declared = (FIXTURES / WEBHOOKS / "openapi.yml").read_text(encoding="utf-8")
        self.assertIn("openapi: 3.1.0", declared, "the fixture no longer declares a patch level")
        every = {selector for selector, _ in rows(run("--vendored-only"))}
        versions = {s for s in every if s.startswith("openapi.openapi=")}
        self.assertEqual({"openapi.openapi=3.0", "openapi.openapi=3.1"}, versions)

    def test_the_json_report_carries_the_sources_it_read(self) -> None:
        completed = run("--vendored-only", "--fixture", WEBHOOKS, "--json")
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(
            [{
                "fixture": WEBHOOKS,
                "origin": "vendored",
                "path": f"tests/fixtures/{WEBHOOKS}/openapi.yml",
            }],
            payload["sources"],
        )
        self.assertIn(
            {"selector": "openapi.webhooks", "fixture": WEBHOOKS, "count": 1},
            payload["rows"],
        )


class ConjunctionCensusTests(unittest.TestCase):
    """What the fourth kind of selector answers, driven end to end over the corpus.

    A conjunction has no counting logic of its own — the census composes its
    members under `&` and `>` as it walks — so the only way to know a spelling
    counts what it says is to run the real script over the real vendored documents
    and assert every entry's number. One exemplar would leave the other eight
    unproven, which is exactly how a mis-composed member would survive.

    Each map below is the whole answer for one selector: every registered vendored
    source that declares it and how many times. An empty map is the other answer
    the instrument must be able to give — a shape the corpus has never seen — and
    it is the evidence a `gap` row would cite.

    The closed list and not more: a case carries a selector only where every
    property the arm's own condition reads is one the grammar can name — a field
    written, a member of a closed value set, or one of the predicates — because
    anything else the arm reads, an example's JSON kind or the *absence* of a
    sibling declaration, is a condition no selector kind expresses and a selector
    ignoring it would count documents the generator sends elsewhere. Every case
    that carries no selector is an enumeration hole, and
    `GrammarContractTests` holds the two states to the case analysis's own rows.

    The numbers are the census's own, and an independent count over every vendored
    document agrees with all nine. They were taken before the free-map-key walk
    repair `FreeMapKeyWalkTests` guards and are unchanged by it: that repair
    restores the Response Object subtree under an unquoted `200:` status code,
    which moves the plain `schema.properties`, `schema.items` and `schema.type`
    selectors on `query-parameters-openapi` and reaches no conjunction — so the
    classification these numbers carry is the repaired walk's as well.
    """

    # The nine the conjunction pass declared, kept apart from the twenty-eight the
    # node-local predicate family added, so each pass's own coverage is readable.
    PRE_EXISTING = (
        "schema.anyOf>schema.$ref",
        "schema.anyOf>schema.allOf",
        "schema.items>schema.$ref",
        "schema.items>schema.anyOf",
        "schema.items>schema.oneOf",
        "schema.oneOf>schema.$ref",
        "schema.oneOf>schema.allOf",
        "schema.properties>schema.anyOf",
        "schema.properties>schema.oneOf",
    )

    DECLARED = {
        "schema.anyOf>schema.$ref": {},
        "schema.anyOf>schema.allOf": {},
        "schema.items>schema.$ref": {
            "audience-filter": 1, "audience-filter-strict": 1, "crozier-sdk-extensions": 1, "exhaustive": 7, "inline-array-request": 1, "inline-request-response": 1, "oauth-client-credentials": 1, "query-parameters-openapi": 2, "recursive-types": 2
        },
        "schema.items>schema.anyOf": {},
        "schema.items>schema.oneOf": {},
        "schema.oneOf>schema.$ref": {
            "discriminated-unions": 1, "query-parameters-openapi": 2, "recursive-types": 1
        },
        "schema.oneOf>schema.allOf": {"exhaustive": 1},
        "schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&!schema.example:schema-shaped&!schema.properties:non-empty&schema.example=object&schema.type:primary=object": {},
        "schema.properties>schema.anyOf": {},
        "schema.properties>schema.oneOf": {},
        "schema.items>schema.type:primary=array": {},
        "schema.items>schema.properties:non-empty": {"inline-array-request": 1},
        "schema.items>schema.additionalProperties=false": {},
        "schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member": {},
        "schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member": {},
        "schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member": {},
        "schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member": {},
        "schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf": {},
        "schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf": {},
        "schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf": {},
        "schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf": {},
        "schema.oneOf>schema.type:primary=array&schema.items>schema.properties:non-empty": {},
        "schema.anyOf>schema.type:primary=array&schema.items>schema.properties:non-empty": {},
        "schema.oneOf>schema.type:primary=array&schema.items>schema.additionalProperties=false": {},
        "schema.anyOf>schema.type:primary=array&schema.items>schema.additionalProperties=false": {},
        "schema.oneOf>schema.properties:non-empty": {},
        "schema.anyOf>schema.properties:non-empty": {},
        "schema.properties>schema.enum:string-valued": {
            "discriminated-unions": 2, "exhaustive": 2, "recursive-types": 2
        },
        "schema.properties>schema.const:string-valued": {},
        "schema.properties>schema.properties:non-empty": {
            "inline-request-response": 2, "nested-core-imports": 1
        },
        "schema.properties>schema.additionalProperties=false": {},
        "schema.properties>schema.oneOf:sole-non-null-member": {},
        "schema.properties>schema.anyOf:sole-non-null-member": {},
        "schema.properties>schema.type:primary=array": {
            "crozier-sdk-extensions": 1, "exhaustive": 3, "inline-request-response": 1, "malformed-property-schema": 1, "query-parameters-openapi": 2, "recursive-types": 2, "schema-constraints": 1
        },
        "schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.properties:non-empty": {},
        "schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.properties:non-empty": {},
        "schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.additionalProperties=false": {},
        "schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.additionalProperties=false": {},
        # The ten the annotated-`$ref` pass declared. Every one is zero over the
        # vendored half: no vendored document writes an `allOf` of a `$ref` beside
        # a description at all, which `AnnotatedRefSelectorDiscriminationTests`
        # answers for by constructing the documents rather than borrowing them.
        "schema.properties>schema.allOf:annotated-ref": {},
        "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.enum:string-valued": {},
        "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.const:string-valued": {},
        "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.oneOf": {},
        "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.anyOf": {},
        "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.properties:non-empty": {},
        "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.allOf": {},
        "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.additionalProperties=false": {},
        "schema.oneOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component": {},
        "schema.anyOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component": {},
        # The nine the discriminated-union pass declared. Every one is zero over
        # the vendored half: the two vendored documents that declare a union
        # `discriminated_union` builds — `discriminated-unions` and
        # `recursive-types` — write it as a named component, which no conjunction
        # anchored on `items`, on a union member or on a property reaches.
        # `DiscriminatedUnionSelectorDiscriminationTests` answers for all nine by
        # constructing the documents rather than borrowing them.
        "schema.items>schema.oneOf:discriminated-union": {},
        "schema.items>schema.anyOf:discriminated-union": {},
        "schema.items>schema.discriminator:inheritance-union": {},
        "schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf:discriminated-union": {},
        "schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union": {},
        "schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:discriminated-union": {},
        "schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union": {},
        "schema.properties>schema.oneOf:discriminated-union": {},
        "schema.properties>schema.anyOf:discriminated-union": {},
        # The five the pointer-walk pass declared. Every one is zero over the
        # vendored half for the reason
        # `PointerFormSelectorDiscriminationTests` already asserts: no vendored
        # document writes a `#/components/schemas/` pointer carrying a segment
        # after its head at all, so none of these arms is reachable there.
        # `PointerWalkSelectorDiscriminationTests` answers for all five by
        # constructing the documents rather than borrowing them.
        "schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=allOf": {},
        "schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=oneOf": {},
        "schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=anyOf": {},
        "schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=properties": {},
        "schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=items": {},
        # The thirteen the negation pass declared beside the seven residual arms
        # below. Every one is zero over the vendored half: none of these documents
        # writes an `allOf` on a property, an item or a sole composition member
        # without a scalar `type` beside it, and none writes an explicitly empty
        # `properties: {}` at all.
        "schema.items>!schema.type:primary-scalar&schema.allOf": {},
        "schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object": {},
        "schema.oneOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf": {},
        "schema.anyOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf": {},
        "schema.oneOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object": {},
        "schema.anyOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object": {},
        "schema.properties>!schema.$ref&!schema.additionalProperties&!schema.anyOf&!schema.enum&!schema.items&!schema.oneOf&!schema.properties&!schema.type&schema.allOf:sole-member&schema.allOf>!schema.$ref": {},
        "schema.properties>!schema.type:primary-scalar&schema.allOf": {},
        "schema.properties>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object": {},
        "schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.type:primary-scalar&schema.allOf": {},
        "schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf": {},
        "schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object": {},
        "schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object": {},
        # The seven residual arms, whose selectors are composed from the case
        # table rather than written. They are the most-travelled paths in the six
        # functions and the vendored half declares four of them, which is what a
        # residual arm should look like: `prop_type_ref`'s own residual is the
        # widest number in this table.
        "schema.items>!schema.$ref&!schema.additionalProperties=false&!schema.anyOf&!schema.anyOf:discriminated-union&!schema.discriminator:inheritance-union&!schema.oneOf&!schema.oneOf:discriminated-union&!schema.properties:non-empty&!schema.type:primary=array": {"client-class-name": 1, "error-responses": 1, "exhaustive": 9, "malformed-property-schema": 1, "missing-operation-id": 1, "operation-id-non-identifier": 1, "pydantic-extra-fields": 1, "query-parameters-openapi": 5, "schema-constraints": 1, "tag-based-grouping": 2},
        "schema.oneOf>!schema.$ref&!schema.allOf&!schema.properties:non-empty": {"exhaustive": 1, "query-parameters-openapi": 2},
        "schema.anyOf>!schema.$ref&!schema.allOf&!schema.properties:non-empty": {},
        "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>!schema.additionalProperties=false&!schema.allOf&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty": {},
        "schema.properties>!schema.oneOf:discriminated-union&!schema.oneOf:sole-non-null-member&schema.oneOf": {},
        "schema.properties>!schema.anyOf:discriminated-union&!schema.anyOf:sole-non-null-member&schema.anyOf": {},
        "schema.properties>!schema.additionalProperties=false&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty&!schema.type:primary=array": {"audience-filter": 3, "audience-filter-strict": 4, "auth-schemes": 2, "bracketed-property-names": 2, "client-class-name": 1, "cookie-parameters": 1, "crozier-sdk-extensions": 5, "digit-leading-property": 1, "discriminated-unions": 2, "enum-name-sanitization": 1, "enum-query-param": 1, "enum-receiver-collision": 1, "error-responses": 2, "exhaustive": 16, "form-bodies": 4, "inline-array-request": 2, "inline-request-response": 6, "integer-enums": 1, "nested-core-imports": 1, "oauth-client-credentials": 3, "operation-id-non-identifier": 1, "pydantic-extra-fields": 1, "query-parameters-openapi": 2, "recursive-types": 2, "schema-constraints": 2, "servers-webhooks": 3, "sse-streaming": 1, "tag-based-grouping": 2, "writeonly-fields": 1},
    }

    # A conjunction no vendored source declares, asserted as absent rather than as
    # silence — the other half of what `--selector` has to answer.
    ABSENT = "schema.items>schema.anyOf"

    def test_the_closed_list_is_the_one_this_case_answers_for(self) -> None:
        """An entry added to the script and not here would go unmeasured."""
        self.assertEqual(set(census.CONJUNCTIONS), set(self.DECLARED))

    def test_every_conjunction_counts_what_its_own_composition_implies(self) -> None:
        completed = run("--vendored-only", "--json")
        self.assertEqual(0, completed.returncode, completed.stderr)
        reported: dict[str, dict[str, int]] = {selector: {} for selector in census.CONJUNCTIONS}
        for row in json.loads(completed.stdout)["rows"]:
            if row["selector"] in census.CONJUNCTIONS:
                reported[row["selector"]][row["fixture"]] = row["count"]
        for selector, expected in self.DECLARED.items():
            with self.subTest(selector=selector):
                self.assertEqual(expected, reported[selector], census.CONJUNCTIONS[selector])

    def test_a_conjunction_reports_one_row_per_source_declaring_it(self) -> None:
        """`--selector` takes a conjunction like any other selector."""
        selector = "schema.oneOf>schema.$ref"
        completed = run("--vendored-only", "--selector", selector)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(
            {(selector, fixture): count for fixture, count in self.DECLARED[selector].items()},
            rows(completed),
        )

    def test_an_any_of_only_document_is_counted_by_its_own_spelling(self) -> None:
        """The correction the `anyOf` half of the closed list exists for.

        `nested_array_element`, `hoist_union_variant` and `prop_type_ref` all reach
        their union arms through `one_of.as_ref().or(any_of.as_ref())`, so a
        document that writes only `anyOf` selects those branches exactly as one
        writing `oneOf` does. A closed list naming only the `oneOf` spelling would
        report this document as declaring none of them — silence that reads as
        "the corpus has never seen this shape" when the corpus is looking at it.
        """
        document = """\
            openapi: 3.0.3
            info: {title: any-of-only, version: "1"}
            paths: {}
            components:
              schemas:
                Bag:
                  type: object
                  properties:
                    choice:
                      anyOf:
                        - type: string
                        - type: integer
                    many:
                      type: array
                      items:
                        anyOf:
                          - type: string
                          - type: integer
            """
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "any-of-only", document)
            completed = run("--vendored-only", "--fixtures-root", str(root))
        self.assertEqual(0, completed.returncode, completed.stderr)
        counted = rows(completed)
        for selector in ("schema.items>schema.anyOf", "schema.properties>schema.anyOf"):
            with self.subTest(selector=selector):
                self.assertEqual(1, counted.get((selector, "any-of-only")))
        for selector in ("schema.items>schema.oneOf", "schema.properties>schema.oneOf"):
            with self.subTest(selector=selector):
                self.assertNotIn((selector, "any-of-only"), counted)

    def test_example_value_selectors_and_case_11_distinguish_the_real_readings(self) -> None:
        """The public CLI reads example first, then the first examples member."""
        selector = (
            "schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&"
            "!schema.example:schema-shaped&!schema.properties:non-empty&"
            "schema.example=object&schema.type:primary=object"
        )
        document = """\
            openapi: 3.0.3
            info: {title: examples, version: "1"}
            paths: {}
            components:
              schemas:
                Root:
                  oneOf:
                    - {type: object, example: scalar}
                    - {type: object, example: {field: value}}
                    - {type: object, example: {field: {type: string}}}
                    - {type: object, examples: []}
                    - {type: object, examples: [{field: from-list}]}
                    - {type: object, example: scalar-wins, examples: [{field: ignored}]}
            """
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "examples", document)
            completed = run(
                "--vendored-only",
                "--fixtures-root", str(root),
                "--selector", "schema.example=object",
                "--selector", "schema.example:schema-shaped",
                "--selector", selector,
            )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(
            {
                ("schema.example=object", "examples"): 3,
                ("schema.example:schema-shaped", "examples"): 1,
                (selector, "examples"): 1,
            },
            rows(completed),
        )

    def test_case_11_is_absent_from_the_registered_corpus(self) -> None:
        """The recorded gap is measured over every registered source, end to end."""
        selector = (
            "schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&"
            "!schema.example:schema-shaped&!schema.properties:non-empty&"
            "schema.example=object&schema.type:primary=object"
        )
        sources = census.registered_sources(FIXTURES, REPO / ".local" / "corpus", False)
        self.assertEqual(169, len(sources))
        declared: dict[tuple[str, str], int] = {}
        for offset in range(0, len(sources), 57):
            fixture_args = list(itertools.chain.from_iterable(
                ("--fixture", source.fixture) for source in sources[offset : offset + 57]
            ))
            completed = run("--selector", selector, *fixture_args)
            self.assertEqual(0, completed.returncode, completed.stderr)
            declared.update(rows(completed))
        self.assertEqual({}, declared)

    def test_a_misspelling_of_a_conjunction_is_refused_by_name(self) -> None:
        for selector, expected in (
            ("schema.items>schema.oneof", "Did you mean: schema.items>schema.oneOf"),
            ("schema.oneOf&schema.discriminator", "is not one of the conjunction selectors"),
            ("schema.items>schema.maxLength", "is not one of the conjunction selectors"),
            # Withdrawn as inexact: the arm also reads the example's JSON kind and
            # rejects a schema-shaped object, so this spelling counted documents
            # `hoist_union_variant` sends to `base_type_ref`. H-example-value now.
            (
                "schema.oneOf>schema.example&schema.type=object",
                "is not one of the conjunction selectors",
            ),
            # Withdrawn as inexact: `is_inline_struct` needs `properties` to be
            # non-empty, so a declared-empty `properties: {}` was counted and is
            # not an inline object at all. H-empty-collection now.
            (
                "schema.properties>schema.properties",
                "is not one of the conjunction selectors",
            ),
        ):
            with self.subTest(selector=selector):
                completed = run("--vendored-only", "--selector", selector)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn(repr(selector), completed.stderr)
                self.assertIn(expected, completed.stderr)
                self.assertNotIn("declared by no registered source", completed.stdout)

    def test_a_conjunction_no_registered_source_declares_is_reported_as_absent(self) -> None:
        self.assertEqual({}, self.DECLARED[self.ABSENT], "the corpus now declares the absent case")
        completed = run("--vendored-only", "--selector", self.ABSENT)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({}, rows(completed))
        self.assertIn(self.ABSENT, completed.stdout)
        self.assertIn("(declared by no registered source)", completed.stdout)

        as_json = run("--vendored-only", "--json", "--selector", self.ABSENT)
        payload = json.loads(as_json.stdout)
        self.assertEqual([], payload["rows"])
        self.assertEqual([self.ABSENT], payload["absent_selectors"])


class ResolvingDescentTests(unittest.TestCase):
    """The second descent operator, driven through the census's real evaluator.

    `>` descends into the object a field's value *is*; `~>` descends into the
    schema the Reference Object written at a group's last member *denotes*,
    resolved against the document being censused. The closed list carries seven
    conjunctions spelled with `~>` — the annotated-`$ref` pass read them off
    `prop_type_ref`'s cases 2 to 4 — and the exemplar below is deliberately not
    one of them, because what these cases exercise is the *operator* rather than
    any declared spelling: they hand the census their own compiled conjunction and
    run the **real** walk over it:
    `census_document` is the function the command line calls per document, and
    `load_document` is the loader it reads every source with. Nothing is a
    stand-in.
    """

    # The exemplar: a Schema Object one of whose properties is a Reference
    # Object whose target declares `oneOf`. Under `>` alone this shape has no
    # name at all — `schema.properties>schema.oneOf` counts the node that
    # *writes* `oneOf` inline, and `prop_type_ref`'s composition gate is guarded
    # by `prop_schema.reference.is_none()`, so the two are different documents.
    RESOLVING = "schema.properties>schema.$ref~>schema.oneOf"
    WRITTEN = "schema.properties>schema.oneOf"

    @staticmethod
    def document(schemas: str) -> str:
        return textwrap.dedent(
            """\
            openapi: 3.0.3
            info: {title: resolving, version: "1"}
            paths: {}
            components:
              schemas:
            """
        ) + textwrap.indent(textwrap.dedent(schemas), "    ")

    def counts(self, schemas: str, *selectors: str) -> dict[str, int]:
        """The real census over one constructed document, for these selectors.

        The document is written to disk and read back by the census's own
        loader, and walked by `census_document` — the whole of what the command
        line does per source, with the conjunctions to evaluate handed in.
        """
        compiled = {selector: census.compile_conjunction(selector) for selector in selectors}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "openapi.yml"
            path.write_text(self.document(schemas), encoding="utf-8")
            document = census.load_document(path)
        counted = census.census_document(document, compiled)
        return {selector: counted.get(selector, 0) for selector in selectors}

    # Three documents alike in every respect but the one the operator reads.
    TARGET_DECLARES_IT = """\
        Bag:
          type: object
          properties:
            pick: {$ref: '#/components/schemas/Choice'}
        Choice:
          oneOf: [{type: string}, {type: integer}]
        """
    TARGET_DOES_NOT = """\
        Bag:
          type: object
          properties:
            pick: {$ref: '#/components/schemas/Choice'}
        Choice:
          allOf: [{type: string}]
        """
    RESOLVES_TO_NOTHING = """\
        Bag:
          type: object
          properties:
            pick: {$ref: '#/components/schemas/Absent'}
        Choice:
          oneOf: [{type: string}, {type: integer}]
        """

    def test_the_operator_reads_the_target_and_not_the_referencing_node(self) -> None:
        """One answer per document, and three different answers between them."""
        self.assertEqual(
            {self.RESOLVING: 1},
            self.counts(self.TARGET_DECLARES_IT, self.RESOLVING),
            "the referencing node is where the conjunction holds",
        )
        self.assertEqual(
            {self.RESOLVING: 0},
            self.counts(self.TARGET_DOES_NOT, self.RESOLVING),
            "a target declaring `allOf` instead is a document it holds at no node of",
        )
        self.assertEqual(
            {self.RESOLVING: 0},
            self.counts(self.RESOLVES_TO_NOTHING, self.RESOLVING),
            "a reference naming no component of this document resolves to nothing",
        )

    def test_a_document_whose_reference_resolves_to_nothing_is_completed_over(self) -> None:
        """The unresolvable case is answered, not raised and not hung.

        `--vendored-only --fixtures-root` runs the same document through the
        command line, under the suite's own timeout, so a resolver that failed or
        span on a dangling reference fails here rather than wedging the census.
        """
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "dangling-reference", self.document(self.RESOLVES_TO_NOTHING))
            completed = run("--vendored-only", "--fixtures-root", str(root))
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn(("schema.$ref", "dangling-reference"), rows(completed))

    def test_the_written_descent_still_reads_the_node_it_descends_into(self) -> None:
        """`>` is untouched: it never resolves, before this operator or after it.

        A property — and an `items` — that *is* a `$ref` to a schema declaring
        `oneOf` is counted by neither written spelling, which is the whole reason
        `~>` is a second operator rather than a redefinition of the first:
        `prop_type_ref`'s composition gate is guarded by
        `prop_schema.reference.is_none()` and `nested_array_element`'s is
        preceded by `if items.reference.is_some() { return None; }`, so the
        generator sends both of these documents elsewhere.
        """
        self.assertEqual(
            {self.WRITTEN: 0, self.RESOLVING: 1},
            self.counts(self.TARGET_DECLARES_IT, self.WRITTEN, self.RESOLVING),
        )
        items = """\
            Bag:
              type: array
              items: {$ref: '#/components/schemas/Choice'}
            Choice:
              oneOf: [{type: string}, {type: integer}]
            """
        self.assertEqual(
            {"schema.items>schema.oneOf": 0, "schema.items>schema.$ref~>schema.oneOf": 1},
            self.counts(items, "schema.items>schema.oneOf", "schema.items>schema.$ref~>schema.oneOf"),
        )

    def test_the_operator_performs_the_last_segment_lookup_and_not_the_pointer_walk(self) -> None:
        """Which of `src/ir.rs`'s two resolutions `~>` is.

        `#/components/schemas/Outer/properties/inner` is the reference value the
        two answer differently. The last-segment lookup
        (`resolve_ref_from_schemas`) yields the component named `inner`, which
        declares `oneOf`; the prefixed pointer walk (`resolve_schema_pointer`)
        yields `Outer`'s property `inner`, which declares `type: string` and no
        `oneOf`. The operator counts the node, so it is the first.
        """
        self.assertEqual(
            {self.RESOLVING: 1},
            self.counts(
                """\
                Bag:
                  type: object
                  properties:
                    pick: {$ref: '#/components/schemas/Outer/properties/inner'}
                Outer:
                  properties:
                    inner: {type: string}
                inner:
                  oneOf: [{type: string}, {type: integer}]
                """,
                self.RESOLVING,
            ),
        )
        self.assertEqual(
            {self.RESOLVING: 0},
            self.counts(
                """\
                Bag:
                  type: object
                  properties:
                    pick: {$ref: '#/components/schemas/Outer/properties/inner'}
                Outer:
                  properties:
                    inner:
                      oneOf: [{type: string}, {type: integer}]
                """,
                self.RESOLVING,
            ),
            "the pointer walk's answer declares `oneOf` and the operator still counts nothing",
        )

    CYCLE = """\
        A:
          oneOf: [{type: string}, {type: integer}]
          properties:
            link: {$ref: '#/components/schemas/B'}
        B:
          oneOf: [{type: string}, {type: integer}]
          properties:
            link: {$ref: '#/components/schemas/A'}
        """
    CYCLE_WITHOUT_THE_SHAPE = """\
        A:
          properties:
            link: {$ref: '#/components/schemas/B'}
        B:
          properties:
            link: {$ref: '#/components/schemas/A'}
        """

    def test_a_cycle_of_references_terminates_and_is_counted_once_per_node(self) -> None:
        """Reference depth is one, so a cycle is not walked round at all.

        `A` and `B` reference each other and both declare `oneOf`, so each one's
        own depth-one resolution declares the shape and each holds — exactly
        twice between them. A node reached again by going round the cycle would
        make it three or more, or would not terminate.
        """
        self.assertEqual({self.RESOLVING: 2}, self.counts(self.CYCLE, self.RESOLVING))
        self.assertEqual(
            {self.RESOLVING: 0},
            self.counts(self.CYCLE_WITHOUT_THE_SHAPE, self.RESOLVING),
            "neither node's depth-one resolution declares the shape",
        )

    def test_a_second_resolving_descent_is_the_bound_rather_than_a_longer_chain(self) -> None:
        """The bound stated in the grammar, as something that fails.

        `A` names `B` and `B` names `C`, which declares the shape. One resolving
        descent reaches `B` and stops; the two-`~>` spelling would need the edge
        out of a node this descent reached *by* traversing one, and holds nowhere.
        """
        chain = """\
            A:
              properties:
                link: {$ref: '#/components/schemas/B'}
            B:
              properties:
                link: {$ref: '#/components/schemas/C'}
            C:
              oneOf: [{type: string}, {type: integer}]
            """
        two = "schema.properties>schema.$ref~>schema.properties>schema.$ref~>schema.oneOf"
        self.assertEqual(
            {self.RESOLVING: 1, two: 0},
            self.counts(chain, self.RESOLVING, two),
        )

    def test_a_conjunction_using_the_operator_has_exactly_one_name(self) -> None:
        """The canonicalization rule reads the same across both operators.

        Every writing below is the same shape: a Schema Object declaring
        `title` and `description` beside a property that is a Reference Object
        also declaring both, whose target declares `oneOf` beside
        `discriminator`. What varies is the order of the members a descent does
        *not* bind to — the member it does bind to is written last whichever
        operator it is, which is the rule already stated for `>` and unchanged
        across `~>`.
        """
        canonical = (
            "schema.description&schema.title&schema.properties"
            ">schema.description&schema.title&schema.$ref"
            "~>schema.discriminator&schema.oneOf"
        )
        for spelling in (
            canonical,
            "schema.title&schema.description&schema.properties"
            ">schema.title&schema.description&schema.$ref"
            "~>schema.oneOf&schema.discriminator",
            "schema.title&schema.description&schema.properties"
            ">schema.description&schema.title&schema.$ref"
            "~>schema.discriminator&schema.oneOf",
        ):
            with self.subTest(spelling=spelling):
                self.assertEqual(canonical, census.canonical_conjunction(spelling))
        self.assertEqual(canonical, census.canonical_conjunction(canonical))

    def test_an_undeclared_spelling_of_the_operator_is_still_refused(self) -> None:
        """The closed list is closed by the generator's branches, not by the operators.

        A conjunction is declared only where a case of a blind region is read off
        it, which `test_every_declared_conjunction_is_read_off_a_case_of_a_blind_region`
        holds the list to. Seven declared spellings use `~>` now; the exemplar
        these cases run the evaluator over is not one of them, and `--selector`
        refuses it by name exactly as it refuses any well-formed combination
        nobody declared.
        """
        using = [
            selector for selector in census.CONJUNCTIONS
            if census.RESOLVING_DESCENT in selector
        ]
        self.assertEqual(8, len(using), f"the closed list spells {len(using)} with `~>`")
        self.assertNotIn(self.RESOLVING, census.CONJUNCTIONS)
        completed = run("--vendored-only", "--selector", self.RESOLVING)
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn(repr(self.RESOLVING), completed.stderr)
        self.assertIn("is not one of the conjunction selectors", completed.stderr)



# --- the node-local selector family ----------------------------------------
# The building blocks the discrimination table below composes. Each is one shape
# an arm of `src/ir.rs` reads, written once so the table reads as the difference
# between a document that selects a branch and one that misses it by a single
# property.
STRUCT = {"properties": {"id": {"type": "string"}}}
EMPTY_PROPERTIES = {"properties": {}}
CLOSED_OBJECT = {"type": "object", "additionalProperties": False}
OPEN_OBJECT = {"type": "object", "additionalProperties": True}
NULLABLE_ONE_OF = {"oneOf": [{"type": "null"}, {"type": "string"}]}
NULLABLE_ANY_OF = {"anyOf": [{"type": "null"}, {"type": "string"}]}
TWO_ONE_OF = {"oneOf": [{"type": "string"}, {"type": "integer"}]}
TWO_ANY_OF = {"anyOf": [{"type": "string"}, {"type": "integer"}]}


def array_of(items: dict) -> dict:
    """An array schema over one item schema."""
    return {"type": "array", "items": items}


def schema_source(title: str, root: dict) -> dict:
    """A source document whose one interesting node is `components.schemas.Root`."""
    return {
        "openapi": "3.0.3",
        "info": {"title": title, "version": "1"},
        "paths": {},
        "components": {"schemas": {"Root": root, "Other": {"type": "string"}}},
    }


def paths_source(title: str, key: str) -> dict:
    """A source document whose one interesting node is a Paths Object key."""
    return {
        "openapi": "3.0.3",
        "info": {"title": title, "version": "1"},
        "paths": {
            key: {
                "get": {
                    "operationId": "read",
                    "responses": {"200": {"description": "ok"}},
                }
            }
        },
    }


def write_json_fixture(root: Path, name: str, document: dict) -> None:
    directory = root / name
    directory.mkdir(parents=True)
    (directory / "openapi.json").write_text(
        json.dumps(document, indent=2), encoding="utf-8"
    )


# The twelve the annotated-`$ref` pass declared, kept apart from the node-local
# table the same way its own successors are: they are
# one path through `src/ir.rs` — `described_all_of_ref` resolving, and the arms
# that read what it resolved to — and `AnnotatedRefSelectorDiscriminationTests`
# is the case that answers for every one of them.
ANNOTATED_REF_SELECTORS = frozenset({
    "schema.properties>schema.allOf:annotated-ref",
    "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.enum:string-valued",
    "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.const:string-valued",
    "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.oneOf",
    "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.anyOf",
    "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.properties:non-empty",
    "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.allOf",
    "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.additionalProperties=false",
    "schema.oneOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component",
    "schema.anyOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component",
    "schema.allOf:annotated-ref",
    "schema.$ref:resolves-to-component",
})


# The twelve the discriminated-union pass declared, kept apart for the same
# reason: they are one condition in `src/ir.rs` — `discriminated_union` returning
# `Some` — reached from three arms, and
# `DiscriminatedUnionSelectorDiscriminationTests` is the case that answers for
# every one of them.
DISCRIMINATED_UNION_SELECTORS = frozenset({
    "schema.items>schema.oneOf:discriminated-union",
    "schema.items>schema.anyOf:discriminated-union",
    "schema.items>schema.discriminator:inheritance-union",
    "schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf:discriminated-union",
    "schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union",
    "schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:discriminated-union",
    "schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union",
    "schema.properties>schema.oneOf:discriminated-union",
    "schema.properties>schema.anyOf:discriminated-union",
    "schema.oneOf:discriminated-union",
    "schema.anyOf:discriminated-union",
    "schema.discriminator:inheritance-union",
})


# The pointer-form family, declared by the pass after the node-local one and
# discriminated by `PointerFormSelectorDiscriminationTests` below. Named here
# because the node-local table's own completeness assertion is "every selector
# that pass declared", and these are not its.
POINTER_FORM_PREDICATES = frozenset({
    "schema.$ref:cross-document",
    "schema.$ref:same-document-foreign-pointer",
    "schema.$ref:nested-properties",
    "schema.$ref:nested-items",
    "schema.$ref:composition-index",
    "schema.$ref:unnamed-segment",
    "schema.$ref:undeclared-component-head",
})


# The twenty-three the negation pass declared, kept apart from the tables above
# for the same reason each of those is: they are one operator — `!`, the
# complement of a member at one node — and the arms it made expressible, and
# `NegationSelectorDiscriminationTests` is the case that answers for every one of
# them.
NEGATION_SELECTORS = frozenset({
    "schema.type:primary=object",
    "schema.type:primary-scalar",
    "schema.allOf:sole-member",
    "schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&!schema.example:schema-shaped&!schema.properties:non-empty&schema.example=object&schema.type:primary=object",
    "schema.items>!schema.type:primary-scalar&schema.allOf",
    "schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
    "schema.oneOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf",
    "schema.anyOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf",
    "schema.oneOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
    "schema.anyOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
    "schema.properties>!schema.$ref&!schema.additionalProperties&!schema.anyOf&!schema.enum&!schema.items&!schema.oneOf&!schema.properties&!schema.type&schema.allOf:sole-member&schema.allOf>!schema.$ref",
    "schema.properties>!schema.type:primary-scalar&schema.allOf",
    "schema.properties>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
    "schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.type:primary-scalar&schema.allOf",
    "schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf",
    "schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
    "schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
    "schema.items>!schema.$ref&!schema.additionalProperties=false&!schema.anyOf&!schema.anyOf:discriminated-union&!schema.discriminator:inheritance-union&!schema.oneOf&!schema.oneOf:discriminated-union&!schema.properties:non-empty&!schema.type:primary=array",
    "schema.oneOf>!schema.$ref&!schema.allOf&!schema.properties:non-empty",
    "schema.anyOf>!schema.$ref&!schema.allOf&!schema.properties:non-empty",
    "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>!schema.additionalProperties=false&!schema.allOf&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty",
    "schema.properties>!schema.oneOf:discriminated-union&!schema.oneOf:sole-non-null-member&schema.oneOf",
    "schema.properties>!schema.anyOf:discriminated-union&!schema.anyOf:sole-non-null-member&schema.anyOf",
    "schema.properties>!schema.additionalProperties=false&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty&!schema.type:primary=array",
})


# The five segment spellings `resolve_schema_pointer`'s `match part` names, in the
# order its arms are numbered — case 3 to case 7.
_POINTER_WALK_ARMS = ("allOf", "oneOf", "anyOf", "properties", "items")


# The five the pointer-walk pass declared: one conjunction per arm of
# `resolve_schema_pointer`'s segment loop, each carrying that function's caller
# gate in front of the reading of the arm.
# `PointerWalkSelectorDiscriminationTests` is the case that answers for all five.
POINTER_WALK_SELECTORS = frozenset(
    "schema.properties>schema.type:primary=array"
    f"&schema.items>schema.$ref:pointer-walk-reaches={arm}"
    for arm in _POINTER_WALK_ARMS
)


# The five readings those conjunctions carry as their last member, and the whole
# of `census.MEMBER_ONLY_PREDICATES`. Each is half a shape's name rather than a
# name: `resolve_schema_pointer` is called from exactly one place —
# `field_type_ref`, on an array-typed property whose `items` is a reference,
# behind a `starts_with("#/components/schemas/")` guard — so a node writing such a
# pointer anywhere else is one the generator never walks. Standing alone the
# reading would count those nodes, which select **no** case of that function's
# table, and that is the miscount the exactness rule disqualifies. So none of the
# five is a declared selector: the census refuses it as a `--selector` and never
# records it, and it reaches a count only through the conjunction that gates it.
POINTER_WALK_MEMBERS = frozenset(
    f"schema.$ref:pointer-walk-reaches={arm}" for arm in _POINTER_WALK_ARMS
)


class NodeLocalSelectorDiscriminationTests(unittest.TestCase):
    """What each node-local selector counts, over inputs that discriminate its branch.

    Every entry below is one selector and three documents: one whose node selects
    the `src/ir.rs` arm the selector was read off, one *near miss* satisfying every
    part of the selector's condition but one, and — where an arm's condition can
    also be satisfied by a node an earlier or later case of the same function's
    table claims — one exercising that permitted overlap. The near miss is what
    makes the assertion mean something: a selector that counted both would be
    broader than its arm, which this document ranks as worse than the hole it
    replaced.

    The census is driven for real, as its own process, over real documents on the
    real filesystem, in one run over a fixtures root holding all of them. What this
    class establishes is each selector's *extension* over those inputs and nothing
    more; that those same nodes select the arm the selector was derived from is
    established by executing the generator, in `src/ir.rs`'s own test module, over
    the same shapes.
    """

    # selector, slug, the branch it was read off, and the three documents.
    CASES: tuple[dict, ...] = (
        # --- the predicates, each read at the node that declares it -----------
        {
            "selector": "schema.type:primary=array",
            "slug": "primary-array",
            "branch": "the `type: array` guard of nested_array_element case 1",
            "select": ("schema", array_of({"type": "string"})),
            "near": ("schema", {"type": ["string", "array"], "items": {"type": "string"}}),
        },
        {
            "selector": "schema.properties:non-empty",
            "slug": "properties-non-empty",
            "branch": "the `properties` disjunct of `is_inline_struct`",
            "select": ("schema", STRUCT),
            "near": ("schema", EMPTY_PROPERTIES),
        },
        {
            "selector": "schema.oneOf:sole-member",
            "slug": "one-of-sole-member",
            "branch": "prop_type_ref case 12's `members.len() == 1`",
            "select": ("schema", {"oneOf": [{"type": "string"}]}),
            "near": ("schema", TWO_ONE_OF),
        },
        {
            "selector": "schema.anyOf:sole-member",
            "slug": "any-of-sole-member",
            "branch": "prop_type_ref case 12's `members.len() == 1`, `anyOf` spelling",
            "select": ("schema", {"anyOf": [{"type": "string"}]}),
            "near": ("schema", TWO_ANY_OF),
        },
        {
            "selector": "schema.oneOf:sole-non-null-member",
            "slug": "one-of-sole-non-null",
            "branch": "prop_type_ref case 11's nullable pair",
            "select": ("schema", NULLABLE_ONE_OF),
            "near": ("schema", TWO_ONE_OF),
        },
        {
            "selector": "schema.anyOf:sole-non-null-member",
            "slug": "any-of-sole-non-null",
            "branch": "prop_type_ref case 11's nullable pair, `anyOf` spelling",
            "select": ("schema", NULLABLE_ANY_OF),
            "near": ("schema", TWO_ANY_OF),
        },
        {
            "selector": "schema.enum:string-valued",
            "slug": "enum-string-valued",
            "branch": "prop_type_ref case 7a's `string_enum_values`",
            "select": ("schema", {"enum": ["alpha", "beta"]}),
            "near": ("schema", {"enum": [1, 2]}),
        },
        {
            "selector": "schema.const:string-valued",
            "slug": "const-string-valued",
            "branch": "prop_type_ref case 7b's `const` fallback",
            "select": ("schema", {"const": "alpha"}),
            "near": ("schema", {"const": 1}),
        },
        {
            "selector": "schema.additionalProperties=false",
            "slug": "additional-properties-false",
            "branch": "the closed-object disjunct of `is_inline_struct`",
            "select": ("schema", CLOSED_OBJECT),
            "near": ("schema", OPEN_OBJECT),
        },
        {
            "selector": "schema.additionalProperties=true",
            "slug": "additional-properties-true",
            "branch": "`is_map`'s open-map arm, the other boolean of the same field",
            "select": ("schema", OPEN_OBJECT),
            "near": ("schema", {"type": "object", "additionalProperties": {"type": "string"}}),
        },
        {
            "selector": "openapi.paths:leading-literal-segment",
            "slug": "leading-literal",
            "branch": "path_group case 1",
            "select": ("paths", "/widgets/{id}"),
            "near": ("paths", "/{id}/widgets"),
        },
        {
            "selector": "openapi.paths:template-before-literal-segment",
            "slug": "template-before-literal",
            "branch": "path_group case 2",
            "select": ("paths", "/{tenant}/widgets/{id}"),
            "near": ("paths", "/{tenant}/{id}"),
        },
        {
            "selector": "openapi.paths:all-segments-templated",
            "slug": "all-templated",
            "branch": "path_group case 3",
            "select": ("paths", "/{tenant}/{id}"),
            "near": ("paths", "/{tenant}/widgets"),
        },
        # --- nested_array_element ---------------------------------------------
        {
            "selector": "schema.items>schema.type:primary=array",
            "slug": "nae-1",
            "branch": "nested_array_element case 1",
            "select": ("schema", array_of(array_of(STRUCT))),
            "near": ("schema", array_of({"type": ["string", "array"], "items": STRUCT})),
            "overlap": ("schema", array_of({"$ref": "#/components/schemas/Other", "type": "array"})),
            "overlap_selector": "schema.items>schema.$ref",
        },
        {
            "selector": "schema.items>schema.properties:non-empty",
            "slug": "nae-4",
            "branch": "nested_array_element case 4",
            "select": ("schema", array_of(STRUCT)),
            "near": ("schema", array_of(EMPTY_PROPERTIES)),
            "overlap": ("schema", array_of({**array_of({"type": "string"}), **STRUCT})),
            "overlap_selector": "schema.items>schema.type:primary=array",
        },
        {
            "selector": "schema.items>schema.additionalProperties=false",
            "slug": "nae-6",
            "branch": "nested_array_element case 6",
            "select": ("schema", array_of(CLOSED_OBJECT)),
            "near": ("schema", array_of(OPEN_OBJECT)),
            "overlap": ("schema", array_of({**STRUCT, "additionalProperties": False})),
            "overlap_selector": "schema.items>schema.properties:non-empty",
        },
        # --- hoist_union_variant, cases 3a to 3d ------------------------------
        {
            "selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member",
            "slug": "huv-3a",
            "branch": "hoist_union_variant case 3a",
            "select": ("schema", {"oneOf": [array_of(NULLABLE_ANY_OF)]}),
            "near": ("schema", {"oneOf": [array_of(TWO_ANY_OF)]}),
            "overlap": ("schema", {"oneOf": [array_of(
                {"anyOf": [{"type": "null"}, {"oneOf": [{"type": "string"}]}]}
            )]}),
            "overlap_selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf",
        },
        {
            "selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member",
            "slug": "huv-3b",
            "branch": "hoist_union_variant case 3b",
            "select": ("schema", {"oneOf": [array_of(NULLABLE_ONE_OF)]}),
            "near": ("schema", {"oneOf": [array_of(TWO_ONE_OF)]}),
            "overlap": ("schema", {"oneOf": [array_of(
                {"oneOf": [{"type": "null"}, {"anyOf": [{"type": "string"}]}]}
            )]}),
            "overlap_selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf",
        },
        {
            "selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member",
            "slug": "huv-3c",
            "branch": "hoist_union_variant case 3c",
            "select": ("schema", {"anyOf": [array_of(NULLABLE_ANY_OF)]}),
            "near": ("schema", {"anyOf": [array_of(TWO_ANY_OF)]}),
            "overlap": ("schema", {"anyOf": [array_of(
                {"anyOf": [{"type": "null"}, {"oneOf": [{"type": "string"}]}]}
            )]}),
            "overlap_selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf",
        },
        {
            "selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member",
            "slug": "huv-3d",
            "branch": "hoist_union_variant case 3d",
            "select": ("schema", {"anyOf": [array_of(NULLABLE_ONE_OF)]}),
            "near": ("schema", {"anyOf": [array_of(TWO_ONE_OF)]}),
            "overlap": ("schema", {"anyOf": [array_of(
                {"oneOf": [{"type": "null"}, {"anyOf": [{"type": "string"}]}]}
            )]}),
            "overlap_selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf",
        },
        # --- hoist_union_variant, cases 5a to 5d ------------------------------
        {
            "selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf",
            "slug": "huv-5a",
            "branch": "hoist_union_variant case 5a",
            "select": ("schema", {"oneOf": [array_of(TWO_ONE_OF)]}),
            "near": ("schema", {"oneOf": [{"type": ["string", "array"], "items": TWO_ONE_OF}]}),
            "overlap": ("schema", {"oneOf": [array_of(NULLABLE_ONE_OF)]}),
            "overlap_selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member",
        },
        {
            "selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf",
            "slug": "huv-5b",
            "branch": "hoist_union_variant case 5b",
            "select": ("schema", {"oneOf": [array_of(TWO_ANY_OF)]}),
            "near": ("schema", {"oneOf": [{"type": ["string", "array"], "items": TWO_ANY_OF}]}),
            "overlap": ("schema", {"oneOf": [array_of(NULLABLE_ANY_OF)]}),
            "overlap_selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member",
        },
        {
            "selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf",
            "slug": "huv-5c",
            "branch": "hoist_union_variant case 5c",
            "select": ("schema", {"anyOf": [array_of(TWO_ONE_OF)]}),
            "near": ("schema", {"anyOf": [{"type": ["string", "array"], "items": TWO_ONE_OF}]}),
            "overlap": ("schema", {"anyOf": [array_of(NULLABLE_ONE_OF)]}),
            "overlap_selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member",
        },
        {
            "selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf",
            "slug": "huv-5d",
            "branch": "hoist_union_variant case 5d",
            "select": ("schema", {"anyOf": [array_of(TWO_ANY_OF)]}),
            "near": ("schema", {"anyOf": [{"type": ["string", "array"], "items": TWO_ANY_OF}]}),
            "overlap": ("schema", {"anyOf": [array_of(NULLABLE_ANY_OF)]}),
            "overlap_selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member",
        },
        # --- hoist_union_variant, cases 7a to 7d ------------------------------
        {
            "selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.properties:non-empty",
            "slug": "huv-7a",
            "branch": "hoist_union_variant case 7a",
            "select": ("schema", {"oneOf": [array_of(STRUCT)]}),
            "near": ("schema", {"oneOf": [array_of(EMPTY_PROPERTIES)]}),
            "overlap": ("schema", {"oneOf": [array_of({**STRUCT, **TWO_ONE_OF})]}),
            "overlap_selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf",
        },
        {
            "selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.properties:non-empty",
            "slug": "huv-7b",
            "branch": "hoist_union_variant case 7b",
            "select": ("schema", {"anyOf": [array_of(STRUCT)]}),
            "near": ("schema", {"anyOf": [array_of(EMPTY_PROPERTIES)]}),
            "overlap": ("schema", {"anyOf": [array_of({**STRUCT, **TWO_ONE_OF})]}),
            "overlap_selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf",
        },
        {
            "selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.additionalProperties=false",
            "slug": "huv-7c",
            "branch": "hoist_union_variant case 7c",
            "select": ("schema", {"oneOf": [array_of(CLOSED_OBJECT)]}),
            "near": ("schema", {"oneOf": [array_of(OPEN_OBJECT)]}),
            "overlap": ("schema", {"oneOf": [array_of({**STRUCT, "additionalProperties": False})]}),
            "overlap_selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.properties:non-empty",
        },
        {
            "selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.additionalProperties=false",
            "slug": "huv-7d",
            "branch": "hoist_union_variant case 7d",
            "select": ("schema", {"anyOf": [array_of(CLOSED_OBJECT)]}),
            "near": ("schema", {"anyOf": [array_of(OPEN_OBJECT)]}),
            "overlap": ("schema", {"anyOf": [array_of({**STRUCT, "additionalProperties": False})]}),
            "overlap_selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.properties:non-empty",
        },
        # --- hoist_union_variant, cases 8a and 8b -----------------------------
        {
            "selector": "schema.oneOf>schema.properties:non-empty",
            "slug": "huv-8a",
            "branch": "hoist_union_variant case 8a",
            "select": ("schema", {"oneOf": [STRUCT]}),
            "near": ("schema", {"oneOf": [EMPTY_PROPERTIES]}),
            "overlap": ("schema", {"oneOf": [{**STRUCT, "allOf": [{"type": "object"}]}]}),
            "overlap_selector": "schema.oneOf>schema.allOf",
        },
        {
            "selector": "schema.anyOf>schema.properties:non-empty",
            "slug": "huv-8b",
            "branch": "hoist_union_variant case 8b",
            "select": ("schema", {"anyOf": [STRUCT]}),
            "near": ("schema", {"anyOf": [EMPTY_PROPERTIES]}),
            "overlap": ("schema", {"anyOf": [{**STRUCT, "allOf": [{"type": "object"}]}]}),
            "overlap_selector": "schema.anyOf>schema.allOf",
        },
        # --- prop_type_ref ----------------------------------------------------
        {
            "selector": "schema.properties>schema.enum:string-valued",
            "slug": "ptr-7a",
            "branch": "prop_type_ref case 7a",
            "select": ("schema", {"properties": {"kind": {"enum": ["alpha", "beta"]}}}),
            "near": ("schema", {"properties": {"kind": {"enum": [1, 2]}}}),
            "overlap": ("schema", {"properties": {"kind": {"enum": ["alpha"], **STRUCT}}}),
            "overlap_selector": "schema.properties>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>schema.const:string-valued",
            "slug": "ptr-7b",
            "branch": "prop_type_ref case 7b",
            "select": ("schema", {"properties": {"kind": {"const": "alpha"}}}),
            "near": ("schema", {"properties": {"kind": {"const": 1}}}),
            "overlap": ("schema", {"properties": {"kind": {"const": "alpha", **STRUCT}}}),
            "overlap_selector": "schema.properties>schema.properties:non-empty",
        },
        {
            "selector": "schema.example:schema-shaped",
            "slug": "schema-shaped-example",
            "branch": "`example_is_schema_definition`",
            "select": ("schema", {"example": {"field": {"type": "string"}}}),
            "near": ("schema", {"example": {"field": {"description": "metadata"}}}),
        },
        {
            "selector": "schema.properties>schema.properties:non-empty",
            "slug": "ptr-8a",
            "branch": "prop_type_ref case 8a",
            "select": ("schema", {"properties": {"nested": STRUCT}}),
            "near": ("schema", {"properties": {"nested": EMPTY_PROPERTIES}}),
            "overlap": ("schema", {"properties": {"nested": {**STRUCT, **TWO_ONE_OF}}}),
            "overlap_selector": "schema.properties>schema.oneOf",
        },
        {
            "selector": "schema.properties>schema.additionalProperties=false",
            "slug": "ptr-8d",
            "branch": "prop_type_ref case 8d",
            "select": ("schema", {"properties": {"bag": CLOSED_OBJECT}}),
            "near": ("schema", {"properties": {"bag": OPEN_OBJECT}}),
            "overlap": ("schema", {"properties": {"bag": {**STRUCT, "additionalProperties": False}}}),
            "overlap_selector": "schema.properties>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>schema.oneOf:sole-non-null-member",
            "slug": "ptr-11a",
            "branch": "prop_type_ref case 11a",
            "select": ("schema", {"properties": {"maybe": NULLABLE_ONE_OF}}),
            "near": ("schema", {"properties": {"maybe": TWO_ONE_OF}}),
            "overlap": ("schema", {"properties": {"maybe": {**NULLABLE_ONE_OF, **STRUCT}}}),
            "overlap_selector": "schema.properties>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>schema.anyOf:sole-non-null-member",
            "slug": "ptr-11b",
            "branch": "prop_type_ref case 11b",
            "select": ("schema", {"properties": {"maybe": NULLABLE_ANY_OF}}),
            "near": ("schema", {"properties": {"maybe": TWO_ANY_OF}}),
            "overlap": ("schema", {"properties": {"maybe": {**NULLABLE_ANY_OF, **STRUCT}}}),
            "overlap_selector": "schema.properties>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>schema.type:primary=array",
            "slug": "ptr-15",
            "branch": "prop_type_ref case 15",
            "select": ("schema", {"properties": {"many": array_of(STRUCT)}}),
            "near": ("schema", {"properties": {"many": {
                "type": ["string", "array"], "items": STRUCT
            }}}),
            "overlap": ("schema", {"properties": {"many": {
                **array_of(STRUCT), **TWO_ONE_OF
            }}}),
            "overlap_selector": "schema.properties>schema.oneOf",
        },
        {
            "selector": "schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.properties:non-empty",
            "slug": "ptr-12a",
            "branch": "prop_type_ref case 12a",
            "select": ("schema", {"properties": {"wrapper": {"oneOf": [STRUCT]}}}),
            "near": ("schema", {"properties": {"wrapper": {"oneOf": [STRUCT, {"type": "string"}]}}}),
            "overlap": ("schema", {"properties": {"wrapper": {"oneOf": [STRUCT], **STRUCT}}}),
            "overlap_selector": "schema.properties>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.properties:non-empty",
            "slug": "ptr-12b",
            "branch": "prop_type_ref case 12b",
            "select": ("schema", {"properties": {"wrapper": {"anyOf": [STRUCT]}}}),
            "near": ("schema", {"properties": {"wrapper": {"anyOf": [STRUCT, {"type": "string"}]}}}),
            "overlap": ("schema", {"properties": {"wrapper": {"anyOf": [STRUCT], **STRUCT}}}),
            "overlap_selector": "schema.properties>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.additionalProperties=false",
            "slug": "ptr-12c",
            "branch": "prop_type_ref case 12c",
            "select": ("schema", {"properties": {"wrapper": {"oneOf": [CLOSED_OBJECT]}}}),
            "near": ("schema", {"properties": {"wrapper": {"oneOf": [OPEN_OBJECT]}}}),
            "overlap": ("schema", {"properties": {"wrapper": {
                "oneOf": [{**STRUCT, "additionalProperties": False}]
            }}}),
            "overlap_selector": "schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.additionalProperties=false",
            "slug": "ptr-12d",
            "branch": "prop_type_ref case 12d",
            "select": ("schema", {"properties": {"wrapper": {"anyOf": [CLOSED_OBJECT]}}}),
            "near": ("schema", {"properties": {"wrapper": {"anyOf": [OPEN_OBJECT]}}}),
            "overlap": ("schema", {"properties": {"wrapper": {
                "anyOf": [{**STRUCT, "additionalProperties": False}]
            }}}),
            "overlap_selector": "schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.properties:non-empty",
        },
    )

    # The predicates declared before this family was named: the three that compare
    # one document's values against each other, and the two key-shape readings the
    # path-template pass added. Everything else in the two closed lists is a
    # selector this node declared, and is what the table has to cover.
    PRE_EXISTING_PREDICATES = (
        "operation.tags:multiple",
        "operation.operationId:duplicate",
        "openapi.paths:normalized-collision",
        "openapi.paths:templated-key",
        "openapi.paths:several-template-expressions",
        "components.schemas:normalized-collision",
    )
    DECLARED_HERE = frozenset(
        set(census.PREDICATES)
        | set(census.CONJUNCTIONS)
        | {"schema.additionalProperties=false", "schema.additionalProperties=true"}
    ) - frozenset(ConjunctionCensusTests.PRE_EXISTING) - frozenset(
        PRE_EXISTING_PREDICATES
    ) - POINTER_FORM_PREDICATES - ANNOTATED_REF_SELECTORS - DISCRIMINATED_UNION_SELECTORS \
        - POINTER_WALK_SELECTORS - NEGATION_SELECTORS

    @classmethod
    def setUpClass(cls) -> None:
        """One census run over a root holding every document the table names."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for case in cls.CASES:
                for role in ("select", "near", "overlap"):
                    if role not in case:
                        continue
                    kind, payload = case[role]
                    name = f"{case['slug']}-{role}"
                    document = (
                        schema_source(name, payload)
                        if kind == "schema"
                        else paths_source(name, payload)
                    )
                    write_json_fixture(root, name, document)
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        assert completed.returncode == 0, completed.stderr
        payload = json.loads(completed.stdout)
        cls.reported = {
            (row["selector"], row["fixture"]): row["count"] for row in payload["rows"]
        }

    def test_the_table_covers_every_selector_this_node_declared(self) -> None:
        """A selector declared and never discriminated is one nobody measured."""
        self.assertEqual(self.DECLARED_HERE, {case["selector"] for case in self.CASES})

    def test_each_selector_counts_its_own_node_and_not_its_near_miss(self) -> None:
        for case in self.CASES:
            selector, slug = case["selector"], case["slug"]
            with self.subTest(selector=selector, branch=case["branch"]):
                self.assertEqual(
                    1,
                    self.reported.get((selector, f"{slug}-select")),
                    f"{selector} does not count the node that selects {case['branch']}",
                )
                self.assertNotIn(
                    (selector, f"{slug}-near"),
                    self.reported,
                    f"{selector} counts a node missing {case['branch']} by one property",
                )

    def test_each_permitted_overlap_is_counted_by_both_cases(self) -> None:
        """The overlap this document permits, made visible rather than assumed.

        An arm runs only because the earlier ones did not, so a node satisfying two
        cases' conditions is counted by both selectors and reaches one arm. That is
        the overlap the exactness rule allows, and these documents are the ones it
        is allowed on.
        """
        for case in self.CASES:
            if "overlap" not in case:
                continue
            selector, slug = case["selector"], case["slug"]
            with self.subTest(selector=selector):
                self.assertEqual(1, self.reported.get((selector, f"{slug}-overlap")))
                self.assertEqual(
                    1,
                    self.reported.get((case["overlap_selector"], f"{slug}-overlap")),
                    "the overlap document is not counted by the case that claims it",
                )

    def test_the_entries_carrying_no_overlap_are_the_ones_no_case_can_claim(self) -> None:
        """Which entries are exempt from the overlap assertion, and why each is.

        Two kinds are, and both are stated here rather than left as a gap in the
        table. A **member predicate** is not an arm — `schema.properties:non-empty`
        is one property several arms read — so it has no case of its own for
        another case to overlap with, and the overlaps of the arms that read it are
        the conjunctions' own, asserted above. The **three path readings**
        partition every Paths Object key between them, each key taking exactly one,
        so `path_group` has no node two of its three arms claim. Every entry that
        is neither carries an overlap document.
        """
        exempt = {case["selector"] for case in self.CASES if "overlap" not in case}
        self.assertEqual(
            {
                selector
                for selector in self.DECLARED_HERE
                if not census.is_conjunction(selector)
            },
            exempt,
            "a conjunction read off one arm must exercise the overlap its case permits",
        )

    def test_a_misspelling_of_a_node_local_selector_is_refused_by_name(self) -> None:
        """The refusal, driven through the real script rather than the module."""
        for selector, expected in (
            ("schema.properties:nonempty", "Did you mean: schema.properties:non-empty"),
            ("schema.type:primary=arrays", "Did you mean: schema.type:primary=array"),
            ("openapi.paths:leading-template-segment", "is not one of the predicate selectors"),
            ("schema.items>schema.properties:nonempty", "is not one of the conjunction selectors"),
        ):
            with self.subTest(selector=selector):
                completed = run("--vendored-only", "--selector", selector)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn(repr(selector), completed.stderr)
                self.assertIn(expected, completed.stderr)

    def test_a_node_local_selector_no_source_declares_is_reported_as_absent(self) -> None:
        """Absent, not silent: the answer a `gap` row would cite."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json_fixture(root, "bare", schema_source("bare", {"type": "string"}))
            completed = run(
                "--vendored-only", "--fixtures-root", str(root),
                "--selector", "schema.items>schema.additionalProperties=false",
            )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({}, rows(completed))
        self.assertIn("(declared by no registered source)", completed.stdout)


# The one place the annotated-`$ref` inputs are written. `src/ir.rs`'s own test
# module reads the same file and drives the same documents through the
# arm-observation surface, so what this case establishes about a selector's
# extension and what that one establishes about which arm ran compose onto the
# same documents rather than onto two hand-copied sets of them.
RESOLVING_ARM_INPUTS = REPO / "tests" / "resolving-arm-inputs.json"


def substituted(node, schemas, body):
    """One envelope with its two placeholder strings replaced.

    The envelope is shared data rather than two copies of one OpenAPI document,
    so a change to the operation that carries the body reaches both halves of the
    measurement at once. `src/ir.rs`'s `resolving_arm_document` is this function.
    """
    if isinstance(node, dict):
        return {key: substituted(value, schemas, body) for key, value in node.items()}
    if isinstance(node, list):
        return [substituted(value, schemas, body) for value in node]
    if node == "{schemas}":
        return schemas
    if node == "{body}":
        return body
    return node


class AnnotatedRefSelectorDiscriminationTests(unittest.TestCase):
    """What each annotated-`$ref` selector counts, over inputs that bound it both ways.

    The same instrument the node-local and pointer-form families are held to, at
    the grain those two did not need. Each selector here composes several members
    over a resolving descent, so one near miss would leave every other member of
    its condition unproven. The table therefore ranges over **two** enumerations
    the arm itself bounds:

    - against a **broader** selector, one document per separately satisfiable part
      of the condition — a document satisfying every other part and not that one,
      whose node does not select the arm and which the selector counts zero. A
      selector that dropped or weakened any single member fails on that member's
      own document rather than surviving because one chosen near miss happened to
      vary a different one. `schema.allOf` and `schema.$ref`, the two members a
      descent binds to, are not separately satisfiable: the annotated-`$ref`
      predicate beside them already requires an `allOf` holding a Reference
      Object, so no document satisfies the rest of the condition without them.
    - against a **narrower** selector, one document per way the arm's own
      condition admits of being satisfied that the case analysis distinguishes —
      the reference written first or second inside the `allOf`, an annotating
      member carrying a description, nothing at all, or a type-determining field
      written as JSON `null`, the `enum` spelling with and without a `type`,
      `array` as the sole type or as the first non-`null` member of a 3.1 list,
      and a resolving reference written with and without the
      `#/components/schemas/` prefix.

    Where the arm permits a node another case of the same function's table also
    claims, the overlap document is driven too and both selectors are asserted to
    count it, which is the chain overlap
    `docs/openapi-surface-coverage.md`'s exactness rule permits.

    Every document is constructed: no vendored source writes an `allOf` of one
    `$ref` beside a description at all, which `ConjunctionCensusTests` reports as
    ten zeroes over the vendored half. The census is still driven for real, as its
    own process, over real documents on the real filesystem, in one run over a
    fixtures root holding all of them.
    """

    @classmethod
    def setUpClass(cls) -> None:
        payload = json.loads(RESOLVING_ARM_INPUTS.read_text(encoding="utf-8"))
        cls.spec = payload
        # The shared file carries every pass's cases; this one answers for its own.
        cls.cases = [
            case for case in payload["cases"]
            if case["selector"] in ANNOTATED_REF_SELECTORS
        ]
        cls.names = {
            name
            for case in cls.cases
            for role in ("select", "near", "overlap")
            for name in case[role]
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in sorted(cls.names):
                fragment = payload["documents"][name]
                write_json_fixture(root, name, substituted(
                    payload["envelope"], fragment["schemas"], fragment["body"]
                ))
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        assert completed.returncode == 0, completed.stderr
        report = json.loads(completed.stdout)
        cls.reported = {
            (row["selector"], row["fixture"]): row["count"] for row in report["rows"]
        }
        cls.censused = {source["fixture"] for source in report["sources"]}

    def test_the_table_covers_every_selector_this_pass_declared(self) -> None:
        """A selector declared and never discriminated is one nobody measured."""
        self.assertEqual(
            ANNOTATED_REF_SELECTORS, {case["selector"] for case in self.cases}
        )

    def test_every_document_the_table_names_was_censused(self) -> None:
        """No case rests on a document the run never read."""
        self.assertLessEqual(self.names, set(self.spec["documents"]))
        self.assertEqual(self.names, self.censused)

    def test_each_selector_counts_every_form_of_its_own_branch(self) -> None:
        """The narrower half: one positive per way the arm admits of being reached."""
        for case in self.cases:
            selector = case["selector"]
            for name, entry in sorted(case["select"].items()):
                with self.subTest(selector=selector, document=name, form=entry["form"]):
                    self.assertEqual(
                        1,
                        self.reported.get((selector, name)),
                        f"{selector} does not count {entry['form']}",
                    )

    def test_each_selector_counts_no_document_missing_one_part_of_its_condition(self) -> None:
        """The broader half: one negative per separately satisfiable part."""
        for case in self.cases:
            selector = case["selector"]
            for name, entry in sorted(case["near"].items()):
                with self.subTest(selector=selector, document=name, part=entry["part"]):
                    self.assertNotIn(
                        (selector, name),
                        self.reported,
                        f"{selector} counts a document dropping {entry['part']}",
                    )

    def test_each_permitted_overlap_is_counted_by_both_cases(self) -> None:
        """The overlap the exactness rule permits, made visible rather than assumed."""
        for case in self.cases:
            selector = case["selector"]
            for name, overlap in sorted(case["overlap"].items()):
                with self.subTest(selector=selector, document=name):
                    self.assertEqual(1, self.reported.get((selector, name)), overlap["why"])
                    self.assertEqual(
                        1,
                        self.reported.get((overlap["selector"], name)),
                        "the overlap document is not counted by the case that claims it",
                    )

    def test_the_two_annotated_all_of_shapes_are_told_apart(self) -> None:
        """The distinction the whole family rests on, asserted on its own.

        An `allOf` of one `$ref` beside a member declaring only a description is
        an annotated reference; the same `allOf` beside a member declaring
        anything else is a composition, and `described_all_of_ref` refuses it.
        """
        for selector in (
            "schema.allOf:annotated-ref",
            "schema.properties>schema.allOf:annotated-ref",
        ):
            with self.subTest(selector=selector):
                self.assertEqual(1, self.reported.get((selector, "gate-ref-first")))
                self.assertNotIn((selector, "gate-typed-member"), self.reported)

    def test_a_reference_that_resolves_and_one_that_does_not_are_told_apart(self) -> None:
        """The other distinction: two documents alike but for what the `$ref` names.

        `gate-ref-first` and `gate-dangling-ref` differ in one thing — whether
        `components.schemas` declares the component the annotated reference names.
        The gate's own selector counts both, because `prop_type_ref` enters case 1
        before resolving; every selector reading the target counts only the first.
        """
        gate = "schema.properties>schema.allOf:annotated-ref"
        target = gate + "&schema.allOf>schema.$ref~>schema.properties:non-empty"
        self.assertEqual(1, self.reported.get((gate, "gate-ref-first")))
        self.assertEqual(1, self.reported.get((gate, "gate-dangling-ref")))
        self.assertEqual(1, self.reported.get((target, "props-select")))
        self.assertNotIn((target, "props-dangling"), self.reported)

    def test_each_selector_reports_one_row_per_document_declaring_it(self) -> None:
        """`--selector` takes each of these like any other selector.

        The JSON report the rest of this case reads is one of two answers the
        census gives; this is the other, and it is the one a `gap` row's evidence
        is read out of. Each selector is asked for by name over the same fixtures
        root and its answer is the per-document table, not a bare total.
        """
        payload = self.spec
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in sorted(self.names):
                fragment = payload["documents"][name]
                write_json_fixture(root, name, substituted(
                    payload["envelope"], fragment["schemas"], fragment["body"]
                ))
            for case in self.cases:
                selector = case["selector"]
                with self.subTest(selector=selector):
                    completed = run(
                        "--vendored-only", "--fixtures-root", str(root),
                        "--selector", selector,
                    )
                    self.assertEqual(0, completed.returncode, completed.stderr)
                    expected = {
                        (selector, name): count
                        for (reported, name), count in self.reported.items()
                        if reported == selector
                    }
                    self.assertTrue(expected, f"{selector} counts nothing to report")
                    self.assertEqual(expected, rows(completed))

    def test_each_selector_has_exactly_one_name(self) -> None:
        """One shape, one name: every writing the grammar admits canonicalizes to it.

        A group's members are written in lexicographic order except that the
        member a descent binds to comes last, since that is the member the
        operator binds to — so the writings one of these selectors admits are the
        permutations of each group's *other* members, and each has to canonicalize
        to the declared spelling. Every group of these ten carries exactly one
        member the descent does not bind to, so each admits one writing and the
        declared spelling is it; the case that exercises the rule over a group
        with several is `ResolvingDescentTests`'s own, which permutes a
        four-member `~>` conjunction six ways.
        """
        for case in self.cases:
            selector = case["selector"]
            if not census.is_conjunction(selector):
                continue
            with self.subTest(selector=selector):
                self.assertEqual(selector, census.canonical_conjunction(selector))
                groups = census.conjunction_parts(selector)
                writings = [""]
                for members, operator in groups:
                    head, last = (members, []) if operator is None else (members[:-1], members[-1:])
                    writings = [
                        prefix + "&".join([*order, *last]) + (operator or "")
                        for prefix in writings
                        for order in itertools.permutations(head)
                    ]
                for writing in writings:
                    self.assertEqual(
                        selector,
                        census.canonical_conjunction(writing),
                        f"{writing} is a second name for one shape",
                    )

    def test_a_misspelling_of_an_annotated_ref_selector_is_refused_by_name(self) -> None:
        """The refusal, driven through the real script rather than the module."""
        for selector, expected in (
            ("schema.allOf:annotated-refs", "Did you mean: schema.allOf:annotated-ref"),
            ("schema.$ref:resolves-to-components", "Did you mean: schema.$ref:resolves-to-component"),
            (
                "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.oneof",
                "is not one of the conjunction selectors",
            ),
        ):
            with self.subTest(selector=selector):
                completed = run("--vendored-only", "--selector", selector)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn(repr(selector), completed.stderr)
                self.assertIn(expected, completed.stderr)

    def test_an_annotated_ref_selector_no_source_declares_is_reported_as_absent(self) -> None:
        """Absent, not silent, over a document set this check supplies itself."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json_fixture(root, "bare", schema_source("bare", {"type": "string"}))
            for selector in sorted(ANNOTATED_REF_SELECTORS):
                with self.subTest(selector=selector):
                    completed = run(
                        "--vendored-only", "--fixtures-root", str(root),
                        "--selector", selector,
                    )
                    self.assertEqual(0, completed.returncode, completed.stderr)
                    self.assertEqual({}, rows(completed))
                    self.assertIn("(declared by no registered source)", completed.stdout)



class DiscriminatedUnionSelectorDiscriminationTests(unittest.TestCase):
    """What each discriminated-union selector counts, over inputs that bound it both ways.

    The same instrument the three families before it are held to, over the one
    condition in `src/ir.rs` that compares a union's members *against each other*.
    A `discriminator` written beside a `oneOf` is the shape that resembles this
    condition and is not it, so a table resting on one chosen positive would
    confirm the resemblance; this one therefore ranges over **two** enumerations
    the arm itself bounds:

    - against a **broader** selector, one document per separately satisfiable part
      of the condition — a document satisfying every other part and not that one,
      whose node does not select the arm and which the selector counts zero. The
      parts of the cross-member reading are its own: a resolving `mapping`, a
      discriminable value on every resolved member, a non-empty `propertyName`
      with something inferable in its place, resolving `$ref` members, and
      distinct tags. Which composition head the union is built from is *not*
      separately satisfiable in that sense: a node writing a `oneOf` union beside
      an `anyOf` still selects the arm, so a document dropping only the head would
      be a negative the arm runs on, which is not what a near miss is for. The two
      head spellings are two selectors instead, each with its own positives.
    - against a **narrower** selector, one document per way the arm's own
      condition admits of being satisfied that the case analysis distinguishes —
      the written spelling with a `mapping` and without one, the three tag
      spellings `discriminant_value` reads (a one-member string `enum`, a `const`,
      a string `example`), the inferred spelling with no `discriminator` written
      at all, a `mapping` written as pointers and as bare component names, and
      `array` written as the sole type and as the first non-`null` member of a 3.1
      type list. A union whose members are `$ref`s and which tags them with
      something other than a required one-member `enum` is four more forms, one per
      property name `src/ir.rs` supports by name in that position — `type` (which
      also needs a string `example`), `role`, `message_type` and
      `mcp_server_type` — beside the three negatives that bound them: a
      `message_type` value `preserve_const_discriminant` keeps, a `type` written
      but not required, and a tag property naming none of the four.

    Where the arm permits a node another case of the same function's table also
    claims, the overlap document is driven too and both selectors are asserted to
    count it, which is the chain overlap
    `docs/openapi-surface-coverage.md`'s exactness rule permits.

    Every document is constructed and shared with `src/ir.rs`'s own observation of
    which arm ran, through `tests/resolving-arm-inputs.json`. The census is driven
    for real, as its own process, over real documents on the real filesystem, in
    one run over a fixtures root holding all of them.
    """

    @classmethod
    def setUpClass(cls) -> None:
        payload = json.loads(RESOLVING_ARM_INPUTS.read_text(encoding="utf-8"))
        cls.spec = payload
        cls.cases = [
            case for case in payload["cases"]
            if case["selector"] in DISCRIMINATED_UNION_SELECTORS
        ]
        cls.names = {
            name
            for case in cls.cases
            for role in ("select", "near", "overlap")
            for name in case[role]
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in sorted(cls.names):
                fragment = payload["documents"][name]
                write_json_fixture(root, name, substituted(
                    payload["envelope"], fragment["schemas"], fragment["body"]
                ))
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        assert completed.returncode == 0, completed.stderr
        report = json.loads(completed.stdout)
        cls.reported = {
            (row["selector"], row["fixture"]): row["count"] for row in report["rows"]
        }
        cls.censused = {source["fixture"] for source in report["sources"]}

    def test_the_table_covers_every_selector_this_pass_declared(self) -> None:
        """A selector declared and never discriminated is one nobody measured."""
        self.assertEqual(
            DISCRIMINATED_UNION_SELECTORS, {case["selector"] for case in self.cases}
        )

    def test_every_document_the_table_names_was_censused(self) -> None:
        """No case rests on a document the run never read."""
        self.assertEqual(self.names, self.censused)

    def test_each_selector_counts_every_form_of_its_own_branch(self) -> None:
        """The narrower half: one positive per way the arm admits of being reached."""
        for case in self.cases:
            selector = case["selector"]
            for name, entry in sorted(case["select"].items()):
                with self.subTest(selector=selector, document=name, form=entry["form"]):
                    self.assertEqual(
                        1,
                        self.reported.get((selector, name)),
                        f"{selector} does not count {entry['form']}",
                    )

    def test_each_selector_counts_no_document_missing_one_part_of_its_condition(self) -> None:
        """The broader half: one negative per separately satisfiable part."""
        for case in self.cases:
            selector = case["selector"]
            for name, entry in sorted(case["near"].items()):
                with self.subTest(selector=selector, document=name, part=entry["part"]):
                    self.assertNotIn(
                        (selector, name),
                        self.reported,
                        f"{selector} counts a document dropping {entry['part']}",
                    )

    def test_each_permitted_overlap_is_counted_by_both_cases(self) -> None:
        """The overlap the exactness rule permits, made visible rather than assumed."""
        for case in self.cases:
            selector = case["selector"]
            for name, overlap in sorted(case["overlap"].items()):
                with self.subTest(selector=selector, document=name):
                    self.assertEqual(1, self.reported.get((selector, name)), overlap["why"])
                    self.assertEqual(
                        1,
                        self.reported.get((overlap["selector"], name)),
                        "the overlap document is not counted by the case that claims it",
                    )

    def test_the_condition_is_read_rather_than_the_shape_that_resembles_it(self) -> None:
        """The four documents the whole family rests on, asserted together.

        A `discriminator` beside a `oneOf` is what the condition *looks* like. The
        four below are alike but for one thing each, and the selectors have to
        answer differently for three of them: the canonical written union counts;
        the same union one of whose members carries no discriminable value does
        not; a `discriminator` beside an `anyOf` with no `oneOf` does not, because
        `discriminated_union` refuses that spelling outright; and a union with no
        `discriminator` at all whose members tag themselves counts exactly as the
        first does, which is the inferred spelling the resemblance misses in the
        other direction.
        """
        for selector, position in (
            ("schema.properties>schema.oneOf:discriminated-union", "prop"),
            ("schema.items>schema.oneOf:discriminated-union", "nested"),
        ):
            with self.subTest(selector=selector):
                self.assertEqual(
                    1, self.reported.get((selector, f"du-{position}-oneof-enum-tag")),
                    "a discriminator beside a oneOf whose members each carry a "
                    "discriminable value is counted",
                )
                self.assertNotIn(
                    (selector, f"du-{position}-oneof-untagged-member"), self.reported,
                    "a member carrying no discriminable value is not this shape",
                )
                self.assertNotIn(
                    (selector, f"du-{position}-anyof-with-discriminator"), self.reported,
                    "a discriminator beside an anyOf with no oneOf is refused",
                )
                self.assertEqual(
                    1, self.reported.get((selector, f"du-{position}-oneof-inferred")),
                    "the inferred spelling, with no discriminator written at all, "
                    "is counted exactly as the written one is",
                )

    def test_each_selector_reports_one_row_per_document_declaring_it(self) -> None:
        """`--selector` takes each of these like any other selector."""
        payload = self.spec
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in sorted(self.names):
                fragment = payload["documents"][name]
                write_json_fixture(root, name, substituted(
                    payload["envelope"], fragment["schemas"], fragment["body"]
                ))
            for case in self.cases:
                selector = case["selector"]
                with self.subTest(selector=selector):
                    completed = run(
                        "--vendored-only", "--fixtures-root", str(root),
                        "--selector", selector,
                    )
                    self.assertEqual(0, completed.returncode, completed.stderr)
                    expected = {
                        (selector, name): count
                        for (reported, name), count in self.reported.items()
                        if reported == selector
                    }
                    self.assertTrue(expected, f"{selector} counts nothing to report")
                    self.assertEqual(expected, rows(completed))

    def test_each_selector_has_exactly_one_name(self) -> None:
        """One shape, one name: every writing the grammar admits canonicalizes to it."""
        for case in self.cases:
            selector = case["selector"]
            if not census.is_conjunction(selector):
                continue
            with self.subTest(selector=selector):
                self.assertEqual(selector, census.canonical_conjunction(selector))
                groups = census.conjunction_parts(selector)
                writings = [""]
                for members, operator in groups:
                    head, last = (members, []) if operator is None else (members[:-1], members[-1:])
                    writings = [
                        prefix + "&".join([*order, *last]) + (operator or "")
                        for prefix in writings
                        for order in itertools.permutations(head)
                    ]
                for writing in writings:
                    self.assertEqual(
                        selector,
                        census.canonical_conjunction(writing),
                        f"{writing} is a second name for one shape",
                    )

    def test_a_misspelling_of_a_discriminated_union_selector_is_refused_by_name(self) -> None:
        """The refusal, driven through the real script rather than the module."""
        for selector, expected in (
            ("schema.oneOf:discriminated-unions", "Did you mean: schema.oneOf:discriminated-union"),
            (
                "schema.discriminator:inheritance-unions",
                "Did you mean: schema.discriminator:inheritance-union",
            ),
            (
                "schema.items>schema.oneOf:discriminated-unions",
                "is not one of the conjunction selectors",
            ),
        ):
            with self.subTest(selector=selector):
                completed = run("--vendored-only", "--selector", selector)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn(repr(selector), completed.stderr)
                self.assertIn(expected, completed.stderr)

    def test_a_discriminated_union_selector_no_source_declares_is_reported_as_absent(self) -> None:
        """Absent, not silent, over a document set this check supplies itself."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json_fixture(root, "bare", schema_source("bare", {"type": "string"}))
            for selector in sorted(DISCRIMINATED_UNION_SELECTORS):
                with self.subTest(selector=selector):
                    completed = run(
                        "--vendored-only", "--fixtures-root", str(root),
                        "--selector", selector,
                    )
                    self.assertEqual(0, completed.returncode, completed.stderr)
                    self.assertEqual({}, rows(completed))
                    self.assertIn("(declared by no registered source)", completed.stdout)

    def test_the_preserved_const_discriminants_are_the_ones_the_generator_preserves(self) -> None:
        """The one copied literal across the generator/instrument seam, gated.

        `_PRESERVED_CONST_DISCRIMINANTS` is a verbatim copy of the values
        `preserve_const_discriminant` of `src/ir.rs` matches, and the census
        reads it to decide which `const` tag `inferred_discriminant_property_with`
        refuses as a `message_type` tag. Only one of the seven has a shared-input
        document, so without this the other six could be added to or removed from
        the Rust and leave the census silently misreading the arm it ports. This
        re-derives the Rust's own list from its `matches!` arm and requires the
        two to be the same set, in either direction.
        """
        source = (REPO / "src" / "ir.rs").read_text(encoding="utf-8")
        body = re.search(
            r"fn preserve_const_discriminant\(value: &str\) -> bool \{\n"
            r"\s*matches!\(\n\s*value,\n(.*?)\n\s*\)\n\s*\}",
            source,
            re.DOTALL,
        )
        self.assertIsNotNone(
            body, "`preserve_const_discriminant` is no longer a `matches!` over string literals"
        )
        self.assertEqual(
            set(re.findall(r'"([^"]+)"', body.group(1))),
            set(census._PRESERVED_CONST_DISCRIMINANTS),
        )


class DocumentContextTests(unittest.TestCase):
    """The document context every node of the walk can read, and its one boundary.

    `Census` carries the censused document's own `components.schemas` map and the
    set of its keys, so a predicate at any node can compare a value against them —
    which is what `schema.$ref:undeclared-component-head` does and what a resolving
    walk would build a resolver on. The boundary is that it is *this* document and
    nothing else: a `$ref` naming another file is a string to this instrument, and
    the last case here proves that by putting the other file on disk beside the
    one being censused.
    """

    def test_the_context_is_the_documents_own_map_and_its_string_keys(self) -> None:
        document = {
            "openapi": "3.0.3",
            "info": {"title": "context", "version": "1"},
            "paths": {},
            # A numeric key is a name the count rule excludes, so the key set holds
            # the strings and the map holds everything the document wrote.
            "components": {"schemas": {"Root": {"type": "string"}, 7: {}}},
        }
        built = census.Census(document)
        self.assertIs(document["components"]["schemas"], built.component_schemas)
        self.assertEqual(frozenset({"Root"}), built.component_names)

    def test_a_document_declaring_no_component_schemas_carries_an_empty_context(
        self,
    ) -> None:
        """Empty rather than absent, so a predicate reading it needs no guard."""
        for document in (None, {}, {"components": None}, {"components": {"schemas": []}}):
            with self.subTest(document=document):
                built = census.Census(document)
                self.assertEqual({}, built.component_schemas)
                self.assertEqual(frozenset(), built.component_names)

    def test_the_context_is_reachable_from_a_node_outside_components(self) -> None:
        """A `$ref` deep in a Path Item is measured against the same names.

        Driven through the real script: the two documents differ only in whether
        the pointer's head is a key of `components.schemas`, and the head sits at a
        response schema rather than beside the map it is compared with.
        """
        def source(title: str, head: str) -> dict:
            return {
                "openapi": "3.0.3",
                "info": {"title": title, "version": "1"},
                "paths": {
                    "/widgets": {
                        "get": {
                            "operationId": "read",
                            "responses": {
                                "200": {
                                    "description": "ok",
                                    "content": {
                                        "application/json": {
                                            "schema": {
                                                "$ref": f"#/components/schemas/{head}"
                                            }
                                        }
                                    },
                                }
                            },
                        }
                    }
                },
                "components": {"schemas": {"Declared": {"type": "string"}}},
            }

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json_fixture(root, "deep-declared", source("deep-declared", "Declared"))
            write_json_fixture(root, "deep-undeclared", source("deep-undeclared", "Missing"))
            completed = run(
                "--vendored-only", "--fixtures-root", str(root),
                "--selector", "schema.$ref:undeclared-component-head",
            )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(
            {("schema.$ref:undeclared-component-head", "deep-undeclared"): 1},
            rows(completed),
        )

    def test_the_census_reads_no_document_but_the_one_it_is_censusing(self) -> None:
        """The other file is on disk, beside the source, and is never opened.

        `neighbour.yaml` declares `patternProperties`, a keyword the censused
        document does not write, and the censused document's one `$ref` names it.
        The real script reports the reference and nothing the neighbour declares —
        no fetch, no cross-document resolution, no second document.
        """
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json_fixture(
                root,
                "neighbouring-file",
                {
                    "openapi": "3.0.3",
                    "info": {"title": "neighbouring-file", "version": "1"},
                    "paths": {},
                    "components": {
                        "schemas": {
                            "Root": {"$ref": "./neighbour.yaml#/components/schemas/Secret"}
                        }
                    },
                },
            )
            (root / "neighbouring-file" / "neighbour.yaml").write_text(
                "components:\n"
                "  schemas:\n"
                "    Secret:\n"
                "      patternProperties:\n"
                "        '^x-':\n"
                "          type: string\n",
                encoding="utf-8",
            )
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        self.assertEqual(0, completed.returncode, completed.stderr)
        counted = {
            row["selector"]: row["count"] for row in json.loads(completed.stdout)["rows"]
        }
        self.assertEqual(1, counted.get("schema.$ref:cross-document"))
        self.assertNotIn("schema.patternProperties", counted)



class PointerFormSelectorDiscriminationTests(unittest.TestCase):
    """What each pointer-form selector counts, over inputs that discriminate its branch.

    The same instrument `NodeLocalSelectorDiscriminationTests` applies to the
    node-local family, applied to the seven `schema.$ref:` spellings: one selector
    and up to three documents each — one whose node selects the `src/ir.rs` arm the
    selector was read off, one *near miss* satisfying every part of the selector's
    condition but one, and, where another case of the same function's table also
    claims a node this branch permits, one exercising that permitted overlap.

    Every document here is constructed rather than borrowed, because
    `test_no_vendored_source_declares_a_pointer_form_selector` establishes that the
    offline half of the corpus writes none of these `$ref` values. The census is
    still driven for real, as its own process, over real documents on the real
    filesystem, in one run over a fixtures root holding all of them.
    """

    # selector, slug, the branch it was read off, and the `$ref` values.
    CASES: tuple[dict, ...] = (
        {
            "selector": "schema.$ref:cross-document",
            "slug": "ref-cross-document",
            "branch": "ref_to_class case 1a / resolve_schema_pointer case 1a",
            "select": "./other.yaml#/components/schemas/Author",
            "near": "#/definitions/Foo",
        },
        {
            "selector": "schema.$ref:same-document-foreign-pointer",
            "slug": "ref-same-document-foreign",
            "branch": "ref_to_class case 1b / resolve_schema_pointer case 1b",
            "select": "#/definitions/Foo",
            "near": "#/components/schemas/Other",
        },
        {
            "selector": "schema.$ref:nested-properties",
            "slug": "ref-nested-properties",
            "branch": "ref_to_class case 2",
            "select": "#/components/schemas/Other/properties/name",
            # `properties` with nothing after it fails `index + 1 < parts.len()`
            # and takes the residual arm instead: one property short of the branch.
            "near": "#/components/schemas/Other/properties",
            "overlap": "#/components/schemas/Other/properties/name/items",
            "overlap_selector": "schema.$ref:nested-items",
        },
        {
            "selector": "schema.$ref:nested-items",
            "slug": "ref-nested-items",
            "branch": "ref_to_class case 3",
            "select": "#/components/schemas/Other/items",
            "near": "#/components/schemas/Other/item",
            "overlap": "#/components/schemas/Other/allOf/0/items",
            "overlap_selector": "schema.$ref:composition-index",
        },
        {
            "selector": "schema.$ref:composition-index",
            "slug": "ref-composition-index",
            "branch": "ref_to_class case 4",
            "select": "#/components/schemas/Other/allOf/0",
            "near": "#/components/schemas/Other/allof/0",
            "overlap": "#/components/schemas/Other/allOf/0/properties/name",
            "overlap_selector": "schema.$ref:nested-properties",
        },
        {
            "selector": "schema.$ref:unnamed-segment",
            "slug": "ref-unnamed-segment",
            "branch": "ref_to_class case 5 / resolve_schema_pointer case 8",
            "select": "#/components/schemas/Other/zzz",
            "near": "#/components/schemas/Other/items",
            # The overlap `resolve_schema_pointer`'s case 8 leans on, and the one
            # the coverage document names: `Other` declares no `allOf`, so this
            # pointer stops in that function's case 3 and never reaches case 8,
            # while `ref_to_class` reads the same positions and does reach its own
            # residual arm. Both cases are in the same table and both carry rows.
            "overlap": "#/components/schemas/Other/allOf/0/zzz",
            "overlap_selector": "schema.$ref:composition-index",
        },
        {
            "selector": "schema.$ref:undeclared-component-head",
            "slug": "ref-undeclared-head",
            "branch": "resolve_schema_pointer case 2",
            "select": "#/components/schemas/Missing",
            "near": "#/components/schemas/Other",
            "overlap": "#/components/schemas/Missing/zzz",
            "overlap_selector": "schema.$ref:unnamed-segment",
        },
    )

    @classmethod
    def setUpClass(cls) -> None:
        """One census run over a root holding every document the table names."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for case in cls.CASES:
                for role in ("select", "near", "overlap"):
                    if role not in case:
                        continue
                    name = f"{case['slug']}-{role}"
                    write_json_fixture(
                        root, name, schema_source(name, {"$ref": case[role]})
                    )
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        assert completed.returncode == 0, completed.stderr
        payload = json.loads(completed.stdout)
        cls.reported = {
            (row["selector"], row["fixture"]): row["count"] for row in payload["rows"]
        }

    def test_the_table_covers_every_pointer_form_selector(self) -> None:
        """A selector declared and never discriminated is one nobody measured."""
        self.assertEqual(
            set(POINTER_FORM_PREDICATES), {case["selector"] for case in self.CASES}
        )

    def test_each_selector_counts_its_own_node_and_not_its_near_miss(self) -> None:
        for case in self.CASES:
            selector, slug = case["selector"], case["slug"]
            with self.subTest(selector=selector, branch=case["branch"]):
                self.assertEqual(
                    1,
                    self.reported.get((selector, f"{slug}-select")),
                    f"{selector} does not count the node that selects {case['branch']}",
                )
                self.assertNotIn(
                    (selector, f"{slug}-near"),
                    self.reported,
                    f"{selector} counts a node missing {case['branch']} by one property",
                )

    def test_each_permitted_overlap_is_counted_by_both_cases(self) -> None:
        """The overlap this document permits, made visible rather than assumed."""
        for case in self.CASES:
            if "overlap" not in case:
                continue
            selector, slug = case["selector"], case["slug"]
            with self.subTest(selector=selector):
                self.assertEqual(1, self.reported.get((selector, f"{slug}-overlap")))
                self.assertEqual(
                    1,
                    self.reported.get((case["overlap_selector"], f"{slug}-overlap")),
                    "the overlap document is not counted by the case that claims it",
                )

    def test_the_two_entries_carrying_no_overlap_are_the_two_halves_of_one_arm(
        self,
    ) -> None:
        """Which entries are exempt from the overlap assertion, and why both are.

        `ref_to_class`'s first case and `resolve_schema_pointer`'s are each split
        into a cross-document and a same-document row, and the two conditions
        partition the references that reach the arm: a value carrying a non-empty
        part before its `#`, or no `#` at all, is the first, and every other value
        outside `#/components/schemas/` is the second. No node satisfies both, and
        no later case of either table is reached by a reference that strips no
        prefix, so neither half has an overlap to exercise.
        """
        self.assertEqual(
            {
                "schema.$ref:cross-document",
                "schema.$ref:same-document-foreign-pointer",
            },
            {case["selector"] for case in self.CASES if "overlap" not in case},
        )

    def test_one_source_writing_a_foreign_pointer_and_an_undeclared_head(self) -> None:
        """The two shapes a real document writes, in one source, counted apart.

        A Swagger conversion's `#/definitions/Foo` and a pointer into another
        component map both reach `ref_to_class`'s first case; a
        `#/components/schemas/` pointer whose head names nothing this document
        declares reaches `resolve_schema_pointer`'s second. No vendored source
        writes either, so the source is constructed — and the real script is driven
        over it, rather than the walk being stubbed.
        """
        document = {
            "openapi": "3.0.3",
            "info": {"title": "foreign-and-undeclared", "version": "1"},
            "paths": {},
            "components": {
                "schemas": {
                    "Other": {"type": "string"},
                    "FromDefinitions": {"$ref": "#/definitions/Foo"},
                    "FromParameters": {"$ref": "#/components/parameters/Page"},
                    "Dangling": {"$ref": "#/components/schemas/NeverDeclared"},
                    "Declared": {"$ref": "#/components/schemas/Other"},
                }
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json_fixture(root, "foreign-and-undeclared", document)
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        self.assertEqual(0, completed.returncode, completed.stderr)
        counts = {
            row["selector"]: row["count"]
            for row in json.loads(completed.stdout)["rows"]
            if row["fixture"] == "foreign-and-undeclared"
        }
        self.assertEqual(2, counts.get("schema.$ref:same-document-foreign-pointer"))
        self.assertEqual(1, counts.get("schema.$ref:undeclared-component-head"))
        # The declared-head pointer is the control: it is a component-schema
        # pointer whose head this document writes, so it selects no case of either
        # function's table and no pointer-form selector counts it.
        self.assertNotIn("schema.$ref:cross-document", counts)
        self.assertNotIn("schema.$ref:unnamed-segment", counts)

    def test_a_pointer_repeating_a_segment_kind_counts_once_for_that_node(self) -> None:
        """The count rule the predicate sentences publish: one per node, not per segment.

        `ref_to_class` takes the same arm twice for a pointer carrying two `items`
        segments, and the census records one — a Schema Object is one place the
        shape is written, however deep the pointer that writes it. The second
        source is the control that keeps the de-duplication node-scoped rather than
        source-scoped: two Schema Objects each writing one `items` pointer count
        two. Driven through the real script, so a `sorted(set(...))` turned into a
        list fails here.
        """
        def source(title: str, schemas: dict) -> dict:
            return {
                "openapi": "3.0.3",
                "info": {"title": title, "version": "1"},
                "paths": {},
                "components": {"schemas": {"Other": {"type": "string"}, **schemas}},
            }

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json_fixture(
                root,
                "repeated-segments",
                source(
                    "repeated-segments",
                    {
                        "TwiceItems": {
                            "$ref": "#/components/schemas/Other/items/items"
                        },
                        "TwiceProperties": {
                            "$ref": "#/components/schemas/Other/properties/a/properties/b"
                        },
                    },
                ),
            )
            write_json_fixture(
                root,
                "two-nodes-one-segment-each",
                source(
                    "two-nodes-one-segment-each",
                    {
                        "First": {"$ref": "#/components/schemas/Other/items"},
                        "Second": {"$ref": "#/components/schemas/Other/items"},
                    },
                ),
            )
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        self.assertEqual(0, completed.returncode, completed.stderr)
        counted = {
            (row["selector"], row["fixture"]): row["count"]
            for row in json.loads(completed.stdout)["rows"]
        }
        self.assertEqual(
            1,
            counted.get(("schema.$ref:nested-items", "repeated-segments")),
            "a pointer carrying two `items` segments is counted more than once",
        )
        self.assertEqual(
            1,
            counted.get(("schema.$ref:nested-properties", "repeated-segments")),
            "a pointer carrying two `properties` segments is counted more than once",
        )
        self.assertEqual(
            2,
            counted.get(("schema.$ref:nested-items", "two-nodes-one-segment-each")),
            "the de-duplication is source-scoped rather than node-scoped",
        )

    def test_no_vendored_source_declares_a_pointer_form_selector(self) -> None:
        """Why every document above is constructed, asserted rather than assumed.

        The offline half of the corpus writes none of these `$ref` values, so there
        is no vendored source to drive the discriminating inputs off. Should one
        arrive, this fails and the case above it takes that source instead.
        """
        completed = run(
            "--vendored-only",
            *[arg for s in sorted(POINTER_FORM_PREDICATES) for arg in ("--selector", s)],
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({}, rows(completed))
        for selector in sorted(POINTER_FORM_PREDICATES):
            with self.subTest(selector=selector):
                self.assertIn(
                    f"{selector}", completed.stdout
                )
        self.assertEqual(
            len(POINTER_FORM_PREDICATES),
            completed.stdout.count("(declared by no registered source)"),
        )

    def test_a_misspelling_of_a_pointer_form_selector_is_refused_by_name(self) -> None:
        """The refusal, driven through the real script rather than the module."""
        for selector, expected in (
            ("schema.$ref:nested-property", "Did you mean: schema.$ref:nested-properties"),
            ("schema.$ref:crossdocument", "Did you mean: schema.$ref:cross-document"),
            # The spelling the enumeration hole proposed, which the family split in
            # two: it names no predicate, and the refusal says so rather than
            # guessing which half was meant.
            ("schema.$ref:foreign-pointer", "is not one of the predicate selectors"),
        ):
            with self.subTest(selector=selector):
                completed = run("--vendored-only", "--selector", selector)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn(repr(selector), completed.stderr)
                self.assertIn(expected, completed.stderr)

    def test_a_pointer_form_selector_no_source_declares_is_reported_as_absent(
        self,
    ) -> None:
        """Absent, not silent: the answer the two `gap` rows cite."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json_fixture(root, "bare", schema_source("bare", {"type": "string"}))
            completed = run(
                "--vendored-only", "--fixtures-root", str(root),
                "--selector", "schema.$ref:undeclared-component-head",
            )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({}, rows(completed))
        self.assertIn("(declared by no registered source)", completed.stdout)


class PointerWalkSelectorDiscriminationTests(unittest.TestCase):
    """What each pointer-walk selector counts, over inputs that bound it both ways.

    The same instrument the three families before it are held to, over the one
    resolution nothing else in this census performs. `resolve_schema_pointer` of
    `src/ir.rs` requires the `#/components/schemas/` prefix, takes the component
    its **head** segment names, and then walks the reference's remaining segments
    structurally through `allOf`, `oneOf`, `anyOf`, `properties` and `items`. Its
    five `match` arms are its five segment spellings, and each is selected by a
    joint property of the reference value *and* the document it points into: a
    later segment is read only where every earlier arm's body resolved. So the
    documents below vary both halves, and three of them make the point on their
    own — `pw-{arm}-head` addresses a position the document declares,
    `pw-{arm}-earlier-segment-unresolved` writes the same later segment behind an
    earlier one the document does not declare, and each case's overlap document
    addresses a position under two of these arms in sequence.

    Each arm carries exactly one selector: the conjunction that puts
    `resolve_schema_pointer`'s **caller gate** in front of the reading of the arm
    — a property of a Schema Object, whose primary type is `array`, whose `items`
    is that pointer, which is the one place in the generator that calls the
    function at all. The reading on its own is a member of
    `census.MEMBER_ONLY_PREDICATES` and not a selector, because a pointer written
    outside that gate still *is* the shape it reads while the generator never
    walks it; `test_no_member_only_reading_is_ever_recorded_as_a_selector` and
    `test_a_pointer_the_generator_never_walks_is_counted_by_nothing` below hold
    that, over the three caller-gate documents each arm carries.

    - against a **broader** selector, one document per separately satisfiable part
      of the condition — a document satisfying every other part and not that one,
      whose node does not select the arm and which the selector counts zero. So a
      selector that dropped or weakened any single member fails on that member's
      own document rather than surviving because one chosen near miss happened to
      vary a different one.
    - against a **narrower** selector, one document per way the arm's own
      condition admits of being satisfied that the case analysis distinguishes —
      the segment read immediately after the head, read through the `properties`
      arm, read through the `items` arm; read where the schema at that position
      declares the field the segment names and where it declares nothing of the
      sort, since the arm is selected by the *segment* and its body is what then
      fails; read with the index or key segment after it missing, out of range or
      unusable; and the property's own `type` written as a bare `array` and as a
      3.1 list naming `null` first.

    Every document is constructed:
    `PointerFormSelectorDiscriminationTests` establishes that no vendored source
    writes a `#/components/schemas/` pointer carrying a segment at all, so there
    is none to borrow. The census is still driven for real, as its own process,
    over real documents on the real filesystem, in one run over a fixtures root
    holding all of them; and `src/ir.rs`'s
    `every_shared_input_reaches_the_arm_its_selector_was_read_off` drives the real
    generator over these same documents and asserts, at the arm's own site, that
    each one this case requires a selector to count enters the arm and each one it
    requires to count zero does not.
    """

    @classmethod
    def setUpClass(cls) -> None:
        payload = json.loads(RESOLVING_ARM_INPUTS.read_text(encoding="utf-8"))
        cls.spec = payload
        cls.cases = [
            case for case in payload["cases"]
            if case["selector"] in POINTER_WALK_SELECTORS
        ]
        cls.names = {
            name
            for case in cls.cases
            for role in ("select", "near", "overlap")
            for name in case[role]
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in sorted(cls.names):
                fragment = payload["documents"][name]
                write_json_fixture(root, name, substituted(
                    payload["envelope"], fragment["schemas"], fragment["body"]
                ))
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        assert completed.returncode == 0, completed.stderr
        report = json.loads(completed.stdout)
        cls.reported = {
            (row["selector"], row["fixture"]): row["count"] for row in report["rows"]
        }
        cls.censused = {source["fixture"] for source in report["sources"]}

    def test_the_table_covers_every_selector_this_pass_declared(self) -> None:
        """A selector declared and never discriminated is one nobody measured."""
        self.assertEqual(
            POINTER_WALK_SELECTORS, {case["selector"] for case in self.cases}
        )

    def test_every_document_the_table_names_was_censused(self) -> None:
        """No case rests on a document the run never read."""
        self.assertLessEqual(self.names, set(self.spec["documents"]))
        self.assertEqual(self.names, self.censused)

    def test_each_selector_counts_every_form_of_its_own_branch(self) -> None:
        """The narrower half: one positive per way the arm admits of being reached."""
        for case in self.cases:
            selector = case["selector"]
            for name, entry in sorted(case["select"].items()):
                with self.subTest(selector=selector, document=name, form=entry["form"]):
                    self.assertEqual(
                        1,
                        self.reported.get((selector, name)),
                        f"{selector} does not count {entry['form']}",
                    )

    def test_each_selector_counts_no_document_missing_one_part_of_its_condition(self) -> None:
        """The broader half: one negative per separately satisfiable part."""
        for case in self.cases:
            selector = case["selector"]
            for name, entry in sorted(case["near"].items()):
                with self.subTest(selector=selector, document=name, part=entry["part"]):
                    self.assertNotIn(
                        (selector, name),
                        self.reported,
                        f"{selector} counts a document dropping {entry['part']}",
                    )

    def test_no_member_only_reading_is_ever_recorded_as_a_selector(self) -> None:
        """Half a shape's name is never a row.

        Each of the five `MEMBER_ONLY_PREDICATES` spellings is matchable as a
        conjunction member and is not a selector, so the census — driven for real
        over every document this table names, which between them write every form
        of every one of the five arms — reports no row under any of them, on any
        document. This is the property the withdrawn standalone predicates broke.
        """
        recorded = sorted(
            (selector, fixture)
            for (selector, fixture) in self.reported
            if selector in POINTER_WALK_MEMBERS
        )
        self.assertEqual(
            [], recorded, "a member-only reading was recorded as a selector of its own"
        )

    def test_a_pointer_the_generator_never_walks_is_counted_by_nothing(self) -> None:
        """The exactness repair, over the documents that used to break it.

        Three documents per arm drop one member of `resolve_schema_pointer`'s
        caller gate: the pointer written on a component rather than on a property,
        on a property that is not array-typed, and on a property whose `$ref` is
        not under `items`. Each still *writes* the segment its arm reads, so the
        withdrawn standalone predicate counted all three while the generator walks
        none of them — a count over nodes selecting no case of that function's
        table, which is the miscount the exactness rule disqualifies.
        `openbanking-brasil-directory` writes the real instance of the first:
        `#/components/schemas/ClientCreationResponse/properties/client_id` sits on
        a path parameter's schema. Nothing counts any of them now.
        """
        gate = ("not-a-property", "not-array-typed", "ref-not-under-items")
        seen = 0
        for case in self.cases:
            for name in sorted(n for n in case["near"] if n.endswith(gate)):
                seen += 1
                with self.subTest(arm=case["arm"], document=name):
                    self.assertEqual(
                        0,
                        self.reported.get((case["selector"], name), 0),
                        f"{name} writes a pointer {case['arm']} never walks",
                    )
                    for member in sorted(POINTER_WALK_MEMBERS):
                        self.assertNotIn(
                            (member, name),
                            self.reported,
                            f"{member} counted {name}, which the generator never walks",
                        )
        self.assertEqual(
            15, seen, "three caller-gate documents for each of the five arms"
        )

    def test_each_permitted_overlap_is_counted_by_both_cases(self) -> None:
        """The overlap the exactness rule permits, made visible rather than assumed."""
        for case in self.cases:
            selector = case["selector"]
            for name, overlap in sorted(case["overlap"].items()):
                with self.subTest(selector=selector, document=name):
                    self.assertEqual(1, self.reported.get((selector, name)), overlap["why"])
                    self.assertEqual(
                        1,
                        self.reported.get((overlap["selector"], name)),
                        "the overlap document is not counted by the case that claims it",
                    )

    def test_the_walk_reads_the_pointer_against_the_document_and_not_its_text(self) -> None:
        """Three documents whose outcomes are not all the same, on one selector.

        The finding this family exists for. `resolve_schema_pointer` walks a
        pointer's segments *through* the document, so a predicate reading the
        reference string alone cannot name its arms: the same segment sequence
        selects different arms in different documents. All three references below
        carry an `allOf` segment; only two of them reach it.
        """
        addressed = "pw-allof-after-items"      # `Root/items/allOf/0`, `Root` writing `items`
        stopped = "pw-allof-earlier-segment-unresolved"  # the same pointer, `Root` writing none
        sequenced = "pw-allof-with-properties"  # `Root/allOf/0/properties/b`, two arms in a row
        gated = (
            "schema.properties>schema.type:primary=array"
            "&schema.items>schema.$ref:pointer-walk-reaches="
        )
        allof, items, properties = gated + "allOf", gated + "items", gated + "properties"
        for name in (addressed, stopped, sequenced):
            self.assertIn(name, self.censused, f"{name} was not censused")
        self.assertEqual(
            "#/components/schemas/Root/items/allOf/0",
            self.spec["documents"][addressed]["schemas"]["Holder"]
                ["properties"]["list"]["items"]["$ref"],
        )
        self.assertEqual(
            self.spec["documents"][addressed]["schemas"]["Holder"],
            self.spec["documents"][stopped]["schemas"]["Holder"],
            "the two documents differ in what they declare, not in what they point with",
        )
        # Addressed: `Root` declares `items`, so the walk resolves that step and
        # reads the `allOf` segment behind it — both arms.
        self.assertEqual(1, self.reported.get((allof, addressed)))
        self.assertEqual(1, self.reported.get((items, addressed)))
        # Stopped: the same segments, a document declaring no `items` on `Root`.
        # The walk enters the `items` arm, resolves nothing, and never reads the
        # segment after it — so the `allOf` selectors must not count it.
        self.assertEqual(1, self.reported.get((items, stopped)))
        self.assertNotIn((allof, stopped), self.reported)
        # Sequenced: a position under two of these arms in sequence, and what each
        # selector involved counts.
        self.assertEqual(1, self.reported.get((allof, sequenced)))
        self.assertEqual(1, self.reported.get((properties, sequenced)))
        self.assertNotIn((items, sequenced), self.reported)

    def test_each_selector_reports_one_row_per_document_declaring_it(self) -> None:
        """`--selector` takes each of these like any other selector."""
        payload = self.spec
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in sorted(self.names):
                fragment = payload["documents"][name]
                write_json_fixture(root, name, substituted(
                    payload["envelope"], fragment["schemas"], fragment["body"]
                ))
            for case in self.cases:
                selector = case["selector"]
                with self.subTest(selector=selector):
                    completed = run(
                        "--vendored-only", "--fixtures-root", str(root),
                        "--selector", selector,
                    )
                    self.assertEqual(0, completed.returncode, completed.stderr)
                    expected = {
                        (selector, name): count
                        for (reported, name), count in self.reported.items()
                        if reported == selector
                    }
                    self.assertTrue(expected, f"{selector} counts nothing to report")
                    self.assertEqual(expected, rows(completed))

    def test_each_selector_has_exactly_one_name(self) -> None:
        """One shape, one name: every writing the grammar admits canonicalizes to it.

        A group's members are written in lexicographic order except that the
        member a descent binds to comes last, so the writings one of these five
        admits are the permutations of each group's *other* members. Each of the
        three groups carries at most one such member — `schema.type:primary=array`
        in the middle one — so each admits exactly one writing and the declared
        spelling is it. The case that exercises the rule over a group with several
        is `ResolvingDescentTests`'s own, which permutes a four-member `~>`
        conjunction six ways.
        """
        for case in self.cases:
            selector = case["selector"]
            if not census.is_conjunction(selector):
                continue
            with self.subTest(selector=selector):
                self.assertEqual(selector, census.canonical_conjunction(selector))
                writings = [""]
                for members, operator in census.conjunction_parts(selector):
                    head, last = (
                        (members, []) if operator is None else (members[:-1], members[-1:])
                    )
                    writings = [
                        prefix + "&".join([*order, *last]) + (operator or "")
                        for prefix in writings
                        for order in itertools.permutations(head)
                    ]
                for writing in writings:
                    self.assertEqual(
                        selector,
                        census.canonical_conjunction(writing),
                        f"{writing} is a second name for one shape",
                    )

    def test_a_misspelling_of_a_pointer_walk_selector_is_refused_by_name(self) -> None:
        """The refusal, driven through the real script rather than the module.

        The last two entries are the member-only readings themselves, spelled
        exactly right. They are refused for the same reason a typo is: neither is
        a selector the census declares, so asking for one names nothing to count.
        """
        gated = (
            "schema.properties>schema.type:primary=array"
            "&schema.items>schema.$ref:pointer-walk-reaches="
        )
        for selector, expected in (
            (gated + "allof", "Did you mean: " + gated + "allOf"),
            (gated + "item", "is not one of the conjunction selectors"),
            ("schema.$ref:pointer-walk-allOf", "is not one of the predicate selectors"),
            (
                "schema.$ref:pointer-walk-reaches=allOf",
                "is not one of the predicate selectors",
            ),
            (
                "schema.$ref:pointer-walk-reaches=properties",
                "is not one of the predicate selectors",
            ),
        ):
            with self.subTest(selector=selector):
                completed = run("--vendored-only", "--selector", selector)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn(repr(selector), completed.stderr)
                self.assertIn(expected, completed.stderr)

    def test_a_pointer_walk_selector_no_source_declares_is_reported_as_absent(self) -> None:
        """Absent, not silent, over a document set this check supplies itself."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json_fixture(root, "bare", schema_source("bare", {"type": "string"}))
            for selector in sorted(POINTER_WALK_SELECTORS):
                with self.subTest(selector=selector):
                    completed = run(
                        "--vendored-only", "--fixtures-root", str(root),
                        "--selector", selector,
                    )
                    self.assertEqual(0, completed.returncode, completed.stderr)
                    self.assertEqual({}, rows(completed))
                    self.assertIn("(declared by no registered source)", completed.stdout)


def components_source(title: str, schemas: dict) -> dict:
    """A source document whose whole surface is the `components.schemas` given.

    Unlike `schema_source` it adds no second component: the negation family reads
    what a node does *not* declare, so a bystander schema nobody asked about would
    be counted by half of it.
    """
    return {
        "openapi": "3.0.3",
        "info": {"title": title, "version": "1"},
        "paths": {},
        "components": {"schemas": schemas},
    }


ANNOTATED = [{"$ref": "#/components/schemas/Target"}, {"description": "annotated"}]


def _array_variant(head: str, item: dict) -> dict:
    """One union head whose sole variant is an array over `item`."""
    return {head: [{"type": "array", "items": item}]}


ALL_OF_ITEM = {"allOf": [{"type": "object"}]}
SCALAR_ALL_OF_ITEM = {"type": "string", "allOf": [{"type": "object"}]}
EMPTY_OBJECT_ITEM = {"type": "object", "properties": {}}
CLOSED_EMPTY_OBJECT_ITEM = {"type": "object", "properties": {}, "additionalProperties": False}
STRUCT_ALL_OF_ITEM = {"properties": {"id": {"type": "string"}}, "allOf": [{"title": "x"}]}
STRUCT_EMPTY_ITEM = {
    "type": "object",
    "properties": {},
    "oneOf": [{"type": "string"}, {"type": "integer"}],
}


class NegationSelectorDiscriminationTests(unittest.TestCase):
    """What each selector the negation operator made expressible counts.

    Every entry below is one selector and up to three documents: one whose node
    selects the `src/ir.rs` arm the selector was read off, one *near miss*
    satisfying every part of the selector's condition but one, and — where the
    arm's condition can also be satisfied by a node another case of the same
    function's table claims — one exercising that permitted overlap. A residual
    arm's entry is the same shape as any other's, because a residual is an arm:
    what is different is that its selector is composed from the case table rather
    than written, which `test_a_case_added_to_the_table_moves_the_residual_it_is_in`
    drives a real, patched copy of the script to show.

    The census is driven for real, as its own process, over real documents on the
    real filesystem, in one run over a fixtures root holding all of them.
    """

    CASES: tuple[dict, ...] = (
        # --- the three predicates the operator needed -------------------------
        {
            "selector": "schema.type:primary=object",
            "slug": "primary-object",
            "branch": "`is_object_type`'s first disjunct",
            "select": {"Root": {"type": "object"}},
            "near": {"Root": {"type": ["string", "object"]}},
        },
        {
            "selector": "schema.type:primary-scalar",
            "slug": "primary-scalar",
            "branch": "`declares_scalar_type`",
            "select": {"Root": {"type": "string"}},
            "near": {"Root": {"type": ["object", "string"]}},
        },
        {
            "selector": "schema.allOf:sole-member",
            "slug": "all-of-sole-member",
            "branch": "`sole_inline_all_of`'s arity",
            "select": {"Root": {"allOf": [{"title": "one"}]}},
            "near": {"Root": {"allOf": [{"title": "one"}, {"title": "two"}]}},
        },
        {
            "selector": "schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&!schema.example:schema-shaped&!schema.properties:non-empty&schema.example=object&schema.type:primary=object",
            "slug": "huv-11",
            "branch": "hoist_union_variant case 11",
            "select": {"Root": {"oneOf": [{"type": "object", "example": {"id": "one"}}]}},
            "near": {"Root": {"oneOf": [{"type": "object", "example": {"id": {"type": "string"}}}]}},
        },
        # --- `is_inline_struct` read where the three tables read it -----------
        {
            "selector": "schema.items>!schema.type:primary-scalar&schema.allOf",
            "slug": "nae-5",
            "branch": "nested_array_element case 5",
            "select": {"Root": {"type": "array", "items": ALL_OF_ITEM}},
            "near": {"Root": {"type": "array", "items": SCALAR_ALL_OF_ITEM}},
            "overlap": {"Root": {"type": "array", "items": STRUCT_ALL_OF_ITEM}},
            "overlap_selector": "schema.items>schema.properties:non-empty",
        },
        {
            "selector": "schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
            "slug": "nae-6b",
            "branch": "nested_array_element case 6b",
            "select": {"Root": {"type": "array", "items": EMPTY_OBJECT_ITEM}},
            "near": {"Root": {"type": "array", "items": CLOSED_EMPTY_OBJECT_ITEM}},
            "overlap": {"Root": {"type": "array", "items": STRUCT_EMPTY_ITEM}},
            "overlap_selector": "schema.items>schema.oneOf",
        },
        {
            "selector": "schema.oneOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf",
            "slug": "huv-7e",
            "branch": "hoist_union_variant case 7e",
            "select": {"Root": _array_variant("oneOf", ALL_OF_ITEM)},
            "near": {"Root": _array_variant("oneOf", SCALAR_ALL_OF_ITEM)},
            "overlap": {"Root": _array_variant("oneOf", STRUCT_ALL_OF_ITEM)},
            "overlap_selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.properties:non-empty",
        },
        {
            "selector": "schema.anyOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf",
            "slug": "huv-7f",
            "branch": "hoist_union_variant case 7f",
            "select": {"Root": _array_variant("anyOf", ALL_OF_ITEM)},
            "near": {"Root": _array_variant("anyOf", SCALAR_ALL_OF_ITEM)},
            "overlap": {"Root": _array_variant("anyOf", STRUCT_ALL_OF_ITEM)},
            "overlap_selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.properties:non-empty",
        },
        {
            "selector": "schema.oneOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
            "slug": "huv-7g",
            "branch": "hoist_union_variant case 7g",
            "select": {"Root": _array_variant("oneOf", EMPTY_OBJECT_ITEM)},
            "near": {"Root": _array_variant("oneOf", CLOSED_EMPTY_OBJECT_ITEM)},
            "overlap": {"Root": _array_variant("oneOf", STRUCT_EMPTY_ITEM)},
            "overlap_selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf",
        },
        {
            "selector": "schema.anyOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
            "slug": "huv-7h",
            "branch": "hoist_union_variant case 7h",
            "select": {"Root": _array_variant("anyOf", EMPTY_OBJECT_ITEM)},
            "near": {"Root": _array_variant("anyOf", CLOSED_EMPTY_OBJECT_ITEM)},
            "overlap": {"Root": _array_variant("anyOf", STRUCT_EMPTY_ITEM)},
            "overlap_selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf",
        },
        {
            "selector": "schema.properties>!schema.type:primary-scalar&schema.allOf",
            "slug": "ptr-8b",
            "branch": "prop_type_ref case 8b",
            "select": {"Root": {"properties": {"p": ALL_OF_ITEM}}},
            "near": {"Root": {"properties": {"p": SCALAR_ALL_OF_ITEM}}},
            "overlap": {"Root": {"properties": {"p": STRUCT_ALL_OF_ITEM}}},
            "overlap_selector": "schema.properties>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
            "slug": "ptr-8c",
            "branch": "prop_type_ref case 8c",
            "select": {"Root": {"properties": {"p": EMPTY_OBJECT_ITEM}}},
            "near": {"Root": {"properties": {"p": CLOSED_EMPTY_OBJECT_ITEM}}},
            "overlap": {"Root": {"properties": {"p": STRUCT_EMPTY_ITEM}}},
            "overlap_selector": "schema.properties>schema.oneOf",
        },
        {
            "selector": "schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.type:primary-scalar&schema.allOf",
            "slug": "ptr-12e",
            "branch": "prop_type_ref case 12e",
            "select": {"Root": {"properties": {"p": {"oneOf": [ALL_OF_ITEM]}}}},
            "near": {"Root": {"properties": {"p": {"oneOf": [SCALAR_ALL_OF_ITEM]}}}},
            "overlap": {"Root": {"properties": {"p": {"oneOf": [STRUCT_ALL_OF_ITEM]}}}},
            "overlap_selector": "schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf",
            "slug": "ptr-12f",
            "branch": "prop_type_ref case 12f",
            "select": {"Root": {"properties": {"p": {"anyOf": [ALL_OF_ITEM]}}}},
            "near": {"Root": {"properties": {"p": {"anyOf": [SCALAR_ALL_OF_ITEM]}}}},
            "overlap": {"Root": {"properties": {"p": {"anyOf": [STRUCT_ALL_OF_ITEM]}}}},
            "overlap_selector": "schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
            "slug": "ptr-12g",
            "branch": "prop_type_ref case 12g",
            "select": {"Root": {"properties": {"p": {"oneOf": [EMPTY_OBJECT_ITEM]}}}},
            "near": {"Root": {"properties": {"p": {"oneOf": [CLOSED_EMPTY_OBJECT_ITEM]}}}},
            "overlap": {"Root": {"properties": {"p": {"oneOf": [STRUCT_EMPTY_ITEM]}}}},
            "overlap_selector": "schema.properties>!schema.oneOf:discriminated-union&!schema.oneOf:sole-non-null-member&schema.oneOf",
        },
        {
            "selector": "schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object",
            "slug": "ptr-12h",
            "branch": "prop_type_ref case 12h",
            "select": {"Root": {"properties": {"p": {"anyOf": [EMPTY_OBJECT_ITEM]}}}},
            "near": {"Root": {"properties": {"p": {"anyOf": [CLOSED_EMPTY_OBJECT_ITEM]}}}},
            "overlap": {"Root": {"properties": {"p": {"anyOf": [STRUCT_EMPTY_ITEM]}}}},
            "overlap_selector": "schema.properties>!schema.anyOf:discriminated-union&!schema.anyOf:sole-non-null-member&schema.anyOf",
        },
        # --- `sole_inline_all_of`, whose nine absence tests are nine members ---
        {
            "selector": "schema.properties>!schema.$ref&!schema.additionalProperties&!schema.anyOf&!schema.enum&!schema.items&!schema.oneOf&!schema.properties&!schema.type&schema.allOf:sole-member&schema.allOf>!schema.$ref",
            "slug": "ptr-6",
            "branch": "prop_type_ref case 6",
            "select": {"Root": {"properties": {"p": {"allOf": [{"title": "inline"}]}}}},
            # VolView's `TaskSpec.id`, the document the arity alone miscounts.
            "near": {"Root": {"properties": {"p": {"type": "string", "allOf": [{"title": "inline"}]}}}},
            "overlap": {"Root": {"properties": {"p": {"allOf": [{"title": "inline"}]}}}},
            "overlap_selector": "schema.properties>!schema.type:primary-scalar&schema.allOf",
        },
        # --- the residual arms, composed from the case table ------------------
        {
            "selector": "schema.items>!schema.$ref&!schema.additionalProperties=false&!schema.anyOf&!schema.anyOf:discriminated-union&!schema.discriminator:inheritance-union&!schema.oneOf&!schema.oneOf:discriminated-union&!schema.properties:non-empty&!schema.type:primary=array",
            "slug": "nae-9",
            "branch": "nested_array_element case 9, its closing `None`",
            "select": {"Root": {"type": "array", "items": {"type": "string"}}},
            "near": {
                "Root": {"type": "array", "items": {"$ref": "#/components/schemas/Target"}},
                "Target": {"type": "string"},
            },
            "overlap": {"Root": {"type": "array", "items": ALL_OF_ITEM}},
            "overlap_selector": "schema.items>!schema.type:primary-scalar&schema.allOf",
        },
        {
            "selector": "schema.oneOf>!schema.$ref&!schema.allOf&!schema.properties:non-empty",
            "slug": "huv-12a",
            "branch": "hoist_union_variant case 12a, its closing `base_type_ref`",
            "select": {"Root": {"oneOf": [{"type": "string"}, {"type": "integer"}]}},
            "near": {
                "Root": {"oneOf": [{"$ref": "#/components/schemas/Target"}]},
                "Target": {"type": "string"},
            },
            "overlap": {"Root": _array_variant("oneOf", {"properties": {"id": {"type": "string"}}})},
            "overlap_selector": "schema.oneOf>schema.type:primary=array&schema.items>schema.properties:non-empty",
        },
        {
            "selector": "schema.anyOf>!schema.$ref&!schema.allOf&!schema.properties:non-empty",
            "slug": "huv-12b",
            "branch": "hoist_union_variant case 12b, the same arm through the other head",
            "select": {"Root": {"anyOf": [{"type": "string"}, {"type": "integer"}]}},
            "near": {
                "Root": {"anyOf": [{"$ref": "#/components/schemas/Target"}]},
                "Target": {"type": "string"},
            },
            "overlap": {"Root": _array_variant("anyOf", {"properties": {"id": {"type": "string"}}})},
            "overlap_selector": "schema.anyOf>schema.type:primary=array&schema.items>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>!schema.additionalProperties=false&!schema.allOf&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty",
            "slug": "ptr-5",
            "branch": "prop_type_ref case 5, the resolution block's own residual",
            "select": {
                "Root": {"properties": {"p": {"allOf": ANNOTATED}}},
                "Target": {"type": "string"},
            },
            "near": {
                "Root": {"properties": {"p": {"allOf": ANNOTATED}}},
                "Target": {"type": "string", "enum": ["alpha", "beta"]},
            },
            "overlap": {
                "Root": {"properties": {"p": {"allOf": ANNOTATED}}},
                "Target": {"type": "string"},
            },
            "overlap_selector": "schema.properties>schema.allOf:annotated-ref",
        },
        {
            "selector": "schema.properties>!schema.oneOf:discriminated-union&!schema.oneOf:sole-non-null-member&schema.oneOf",
            "slug": "ptr-14a",
            "branch": "prop_type_ref case 14a, the composition block's own residual",
            "select": {"Root": {"properties": {"p": {"oneOf": [{"type": "string"}, {"type": "integer"}]}}}},
            "near": {"Root": {"properties": {"p": {"oneOf": [{"type": "null"}, {"type": "string"}]}}}},
            "overlap": {"Root": {"properties": {"p": {"oneOf": [{"properties": {"id": {"type": "string"}}}]}}}},
            "overlap_selector": "schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>!schema.anyOf:discriminated-union&!schema.anyOf:sole-non-null-member&schema.anyOf",
            "slug": "ptr-14b",
            "branch": "prop_type_ref case 14b, the same residual through the other spelling",
            "select": {"Root": {"properties": {"p": {"anyOf": [{"type": "string"}, {"type": "integer"}]}}}},
            "near": {"Root": {"properties": {"p": {"anyOf": [{"type": "null"}, {"type": "string"}]}}}},
            "overlap": {"Root": {"properties": {"p": {"anyOf": [{"properties": {"id": {"type": "string"}}}]}}}},
            "overlap_selector": "schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.properties:non-empty",
        },
        {
            "selector": "schema.properties>!schema.additionalProperties=false&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty&!schema.type:primary=array",
            "slug": "ptr-16",
            "branch": "prop_type_ref case 16, the function's own residual",
            "select": {"Root": {"properties": {"p": {"type": "string"}}}},
            "near": {"Root": {"properties": {"p": {"oneOf": [{"type": "string"}, {"type": "integer"}]}}}},
            # Case 1 is the gate this residual deliberately does not negate: its
            # own arm falls through when the annotated `$ref` resolves to nothing.
            "overlap": {
                "Root": {"properties": {"p": {"allOf": ANNOTATED}}},
                "Target": {"type": "string"},
            },
            "overlap_selector": "schema.properties>schema.allOf:annotated-ref",
        },
    )

    @classmethod
    def censused(cls, documents: dict[str, dict]) -> dict[tuple[str, str], int]:
        """The real script's own output over a fixtures root holding `documents`."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, schemas in documents.items():
                write_json_fixture(root, name, components_source(name, schemas))
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        assert completed.returncode == 0, completed.stderr
        return {
            (row["selector"], row["fixture"]): row["count"]
            for row in json.loads(completed.stdout)["rows"]
        }

    @classmethod
    def setUpClass(cls) -> None:
        documents = {
            f"{case['slug']}-{role}": case[role]
            for case in cls.CASES
            for role in ("select", "near", "overlap")
            if role in case
        }
        cls.reported = cls.censused(documents)

    def test_the_table_covers_every_selector_this_pass_declared(self) -> None:
        """A selector declared and never discriminated is one nobody measured."""
        self.assertEqual(NEGATION_SELECTORS, {case["selector"] for case in self.CASES})
        for selector in sorted(NEGATION_SELECTORS):
            with self.subTest(selector=selector):
                self.assertIn(
                    selector, set(census.PREDICATES) | set(census.CONJUNCTIONS)
                )

    def test_each_selector_counts_its_own_node_and_not_its_near_miss(self) -> None:
        for case in self.CASES:
            selector, slug = case["selector"], case["slug"]
            with self.subTest(selector=selector, branch=case["branch"]):
                self.assertEqual(
                    1,
                    self.reported.get((selector, f"{slug}-select")),
                    f"{selector} does not count the node that selects {case['branch']}",
                )
                self.assertNotIn(
                    (selector, f"{slug}-near"),
                    self.reported,
                    f"{selector} counts a node missing {case['branch']} by one property",
                )

    def test_each_permitted_overlap_is_counted_by_both_cases(self) -> None:
        """The overlap a residual inherits, made visible rather than assumed.

        A residual is not narrowed by a case whose own condition reaches into a
        subtree, or by a case recorded as a hole, or by a gate that falls through,
        so it counts the nodes those cases claim. Each document below is one of
        those nodes, and both selectors count it.
        """
        for case in self.CASES:
            if "overlap" not in case:
                continue
            selector, slug = case["selector"], case["slug"]
            with self.subTest(selector=selector):
                self.assertEqual(1, self.reported.get((selector, f"{slug}-overlap")))
                self.assertEqual(
                    1,
                    self.reported.get((case["overlap_selector"], f"{slug}-overlap")),
                    "the overlap document is not counted by the case that claims it",
                )

    def test_the_entries_carrying_no_overlap_are_the_predicates_and_exact_case(self) -> None:
        """Which entries are exempt from the overlap assertion, and why.

        A predicate is a property several arms read rather than an arm, so it has
        no case of its own for another case to overlap with; the overlaps of the
        arms that read it are the conjunctions' own, asserted above.
        """
        exempt = {case["selector"] for case in self.CASES if "overlap" not in case}
        self.assertEqual(
            {selector for selector in NEGATION_SELECTORS
             if not census.is_conjunction(selector)} | {
                "schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&!schema.example:schema-shaped&!schema.properties:non-empty&schema.example=object&schema.type:primary=object"
             },
            exempt,
        )

    def test_a_residual_inside_a_gate_counts_no_node_the_gate_excludes(self) -> None:
        """The scoping property, over a document constructed for it.

        `prop_type_ref`'s case 5 is the residual of the resolution block alone,
        and that block is entered only where the annotated `$ref` *resolves*. A
        property whose annotated `$ref` names no component of the document
        satisfies every negated member — the target it would be read against does
        not exist — and the gate is what has to stop it being counted.
        """
        residual = census.RESIDUAL_SELECTORS[("prop_type_ref", "5")]
        reported = self.censused({
            "resolving": {
                "Root": {"properties": {"p": {"allOf": ANNOTATED}}},
                "Target": {"type": "string"},
            },
            "dangling": {"Root": {"properties": {"p": {"allOf": ANNOTATED}}}},
        })
        self.assertEqual(1, reported.get((residual, "resolving")))
        self.assertNotIn((residual, "dangling"), reported)
        # The gate itself holds over both, which is what makes the difference the
        # residual's own and not the gate member's.
        gate = "schema.properties>schema.allOf:annotated-ref"
        self.assertEqual(1, reported.get((gate, "resolving")))
        self.assertEqual(1, reported.get((gate, "dangling")))

    def test_a_case_added_to_the_table_moves_the_residual_it_is_in(self) -> None:
        """The composition, proved by adding a case to a real copy of the script.

        A residual selector nobody wrote is only worth the claim if adding a case
        to `CASES` changes what it matches with no selector text edited. This
        copies the real script, inserts one case into `nested_array_element`'s
        block, and drives *that* script over a document the real residual counts
        and the patched one must not.
        """
        addition = (
            '        Case("8z", block="nested_array_element", '
            'selector="schema.items>schema.title"),\n'
        )
        source = SCRIPT.read_text(encoding="utf-8")
        marker = '        Case("8", block="nested_array_element", selector="schema.items>schema.anyOf"),\n'
        self.assertIn(marker, source)
        patched_source = source.replace(marker, marker + addition, 1)
        self.assertIn("schema.items>schema.title", patched_source)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            patched = root / "patched-census.py"
            patched.write_text(patched_source, encoding="utf-8")
            spec = importlib.util.spec_from_file_location("patched_census", patched)
            module = importlib.util.module_from_spec(spec)
            sys.modules["patched_census"] = module
            spec.loader.exec_module(module)
            try:
                patched_residual = module.RESIDUAL_SELECTORS[("nested_array_element", "9")]
            finally:
                del sys.modules["patched_census"]
            real_residual = census.RESIDUAL_SELECTORS[("nested_array_element", "9")]
            self.assertNotEqual(real_residual, patched_residual)
            self.assertIn("!schema.title", patched_residual)
            self.assertNotIn("!schema.title", real_residual)

            fixtures = root / "fixtures"
            write_json_fixture(
                fixtures,
                "titled-item",
                components_source(
                    "titled-item",
                    {"Root": {"type": "array", "items": {"type": "string", "title": "t"}}},
                ),
            )
            (fixtures / "CORPUS.md").write_text("", encoding="utf-8")
            arguments = ["--vendored-only", "--fixtures-root", str(fixtures), "--json"]
            real = subprocess.run(
                [sys.executable, str(SCRIPT), *arguments, "--selector", real_residual],
                capture_output=True, text=True, timeout=CENSUS_TIMEOUT,
            )
            self.assertEqual(0, real.returncode, real.stderr)
            self.assertEqual(
                [1], [row["count"] for row in json.loads(real.stdout)["rows"]]
            )
            moved = subprocess.run(
                [sys.executable, str(patched), *arguments, "--selector", patched_residual],
                capture_output=True, text=True, timeout=CENSUS_TIMEOUT,
            )
            self.assertEqual(0, moved.returncode, moved.stderr)
            self.assertEqual([], json.loads(moved.stdout)["rows"])

    def test_a_misspelling_of_a_negation_selector_is_refused_by_name(self) -> None:
        """The refusal, driven through the real script rather than the module."""
        for selector, expected in (
            ("schema.type:primary-scalars", "Did you mean: schema.type:primary-scalar"),
            ("schema.allOf:sole-members", "Did you mean: schema.allOf:sole-member"),
            (
                "schema.items>!schema.type:primary-scalar&schema.allOff",
                "is not one of the conjunction selectors",
            ),
        ):
            with self.subTest(selector=selector):
                completed = run("--vendored-only", "--selector", selector)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn(expected, completed.stderr)

    def test_a_selector_of_negated_members_alone_is_refused_by_name(self) -> None:
        """The one shape the operator does not spell, refused for what it is."""
        for selector in ("!schema.oneOf", "!schema.oneOf&!schema.anyOf"):
            with self.subTest(selector=selector):
                completed = run("--vendored-only", "--selector", selector)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn("negated members alone", completed.stderr)
                self.assertIn("at least one positive member", completed.stderr)
        # And a descent bound to a negated member, the other malformed spelling.
        completed = run("--vendored-only", "--selector", "!schema.items>schema.oneOf")
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("descends through a field the node writes", completed.stderr)

    def test_a_negation_selector_no_source_declares_is_reported_as_absent(self) -> None:
        """Absent, not silent: the phrase a `gap` row cites as its evidence."""
        absent = "schema.anyOf>!schema.$ref&!schema.allOf&!schema.properties:non-empty"
        completed = run("--vendored-only", "--selector", absent)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({}, rows(completed))
        self.assertIn("(declared by no registered source)", completed.stdout)


class ObjectModelWalkTests(unittest.TestCase):
    """The distinction the whole instrument rests on: fields, not matching text."""

    def test_the_walk_disagrees_with_a_naive_text_match_on_a_property_name(self) -> None:
        """`servers-webhooks` writes `name:` once — as a schema *property* name.

        A text match scores that as a declared `name` field (the same mistake as
        scoring a `trace` operation off a path parameter called `trace`). The walk
        knows the keys under `properties` are names, so it reports no `.name`
        selector at all for this document, and the property shows up where it
        belongs: as one more `schema.properties` declaration.
        """
        source = FIXTURES / WEBHOOKS / "openapi.yml"
        naive = len(re.findall(r"^ *name:", source.read_text(encoding="utf-8"), re.M))
        self.assertEqual(1, naive, "the fixture's only `name:` line moved")

        completed = run("--vendored-only", "--fixture", WEBHOOKS)
        self.assertEqual(0, completed.returncode, completed.stderr)
        declared = {selector for selector, _ in rows(completed)}
        self.assertEqual(
            [], [selector for selector in declared if selector.endswith(".name")]
        )
        self.assertIn("schema.properties", declared)

    def test_the_walk_separates_three_different_meanings_of_one_key(self) -> None:
        """`discriminated-unions` writes `type:` nine times, meaning three things."""
        source = FIXTURES / DISCRIMINATED / "openapi.yml"
        naive = len(re.findall(r"^ *type:", source.read_text(encoding="utf-8"), re.M))
        counted = rows(run("--vendored-only", "--fixture", DISCRIMINATED))
        schema_types = counted[("schema.type", DISCRIMINATED)]
        scheme_types = counted[("securityScheme.type", DISCRIMINATED)]
        # The remainder are the `type` PROPERTIES of Circle and Square: named, not
        # declared, and so not a selector anywhere in the report.
        self.assertEqual(naive, schema_types + scheme_types + 2)
        self.assertLess(schema_types, naive)

    def test_a_reference_is_counted_once_and_not_followed(self) -> None:
        """A `$ref` in a schema is a keyword; a `$ref` elsewhere is a Reference Object."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "refs", """\
                openapi: 3.0.3
                info: {title: refs, version: "1"}
                paths:
                  /a:
                    get:
                      responses:
                        "200":
                          $ref: "#/components/responses/Ok"
                components:
                  responses:
                    Ok:
                      description: ok
                  schemas:
                    A:
                      $ref: "#/components/schemas/B"
                """)
            counted = rows(run("--vendored-only", "--fixtures-root", str(root)))
        self.assertEqual(1, counted[("reference.$ref", "refs")])
        self.assertEqual(1, counted[("schema.$ref", "refs")])


class FreeMapKeyWalkTests(unittest.TestCase):
    """A free-keyed map's key is a name; the object it names is still surface.

    YAML lets a Responses Object be keyed `200:` rather than `"200":`, and the
    two documents declare the same thing. The walk used to skip a non-string key
    outright — correctly refusing to emit a selector for it, but taking the
    descent with it — so every Response Object under an unquoted status code,
    and every media type, schema and header beneath, went unvisited. Six
    registered sources write their status codes that way, so this was not an
    edge case the corpus never reached: it was an undercount published as
    evidence.

    These drive the real script over real documents, one pair written here to
    isolate the spelling and one vendored source that writes the unquoted form.
    """

    RESPONSES = """\
        openapi: 3.0.3
        info: {{title: statuses, version: "1"}}
        paths:
          /a:
            get:
              responses:
                {key}:
                  description: ok
                  headers:
                    X-Rate:
                      schema: {{type: integer}}
                  content:
                    application/json:
                      schema:
                        type: array
                        items: {{$ref: "#/components/schemas/A"}}
        components:
          schemas:
            A: {{type: object, properties: {{id: {{type: string}}}}}}
        """

    def surface(self, key: str) -> dict[str, int]:
        """Every selector one document declares, keyed the way its Responses is."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "statuses", self.RESPONSES.format(key=key))
            counted = rows(run("--vendored-only", "--fixtures-root", str(root)))
        return {selector: count for (selector, _fixture), count in counted.items()}

    def test_an_unquoted_status_code_declares_what_the_quoted_spelling_declares(self) -> None:
        quoted = self.surface('"200"')
        self.assertIn("mediaType.schema", quoted)  # the subtree the skip used to lose
        self.assertEqual(quoted, self.surface("200"))

    def test_the_key_itself_is_still_a_name_in_either_spelling(self) -> None:
        """The descent is restored; the selector the grammar refuses to emit is not."""
        for key in ('"200"', "200"):
            with self.subTest(key=key):
                declared = self.surface(key)
                self.assertEqual(
                    [], [selector for selector in declared if selector.endswith(".200")]
                )
                self.assertNotIn("responses.200", declared)

    def test_the_vendored_source_that_writes_an_unquoted_status_code_is_read(self) -> None:
        """`query-parameters-openapi` writes `200:`; its one response is surface.

        The counts are this source's own, so a walk that loses the subtree again
        reports zero for the three response-side selectors and one fewer array
        schema, and fails here rather than in a region file's evidence cell.
        """
        counted = rows(run("--vendored-only", "--fixture", UNQUOTED_STATUS))
        source = (FIXTURES / UNQUOTED_STATUS / "openapi.yml").read_text(encoding="utf-8")
        self.assertIn("\n        200:\n", source, "the fixture no longer writes `200:`")
        for selector, count in (
            ("response.description", 1),
            ("response.content", 1),
            ("mediaType.schema", 1),
            ("schema.properties", 3),
            ("schema.type=array", 7),
        ):
            with self.subTest(selector=selector):
                self.assertEqual(count, counted.get((selector, UNQUOTED_STATUS), 0))


class SourceSelectionTests(unittest.TestCase):
    """Which documents the census is allowed to open, and which it must refuse to."""

    def test_it_reads_every_vendored_source_and_only_its_own_document(self) -> None:
        payload = json.loads(run("--vendored-only", "--json").stdout)
        vendored = sorted(
            directory.name
            for directory in FIXTURES.iterdir()
            if directory.is_dir() and any((directory / n).is_file() for n in census.SPEC_NAMES)
        )
        self.assertEqual(vendored, sorted(s["fixture"] for s in payload["sources"]))
        self.assertGreater(len(vendored), 20, "the vendored corpus shrank unexpectedly")
        for source in payload["sources"]:
            self.assertEqual("vendored", source["origin"])
            self.assertRegex(source["path"], r"^tests/fixtures/[^/]+/openapi\.(yml|yaml|json)$")
        declared = {row["fixture"] for row in payload["rows"]}
        self.assertEqual(set(vendored), declared, "a vendored source declared nothing")

    def test_a_generated_expected_tree_is_never_read(self) -> None:
        """A census that read the output would be measuring the answer, not the question."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = write_fixture(root, "planted", """\
                openapi: 3.0.3
                info: {title: planted, version: "1"}
                paths: {}
                """)
            expected = fixture / "expected" / "src"
            expected.mkdir(parents=True)
            # A generated tree that would light up three selectors if it were read.
            (expected / "openapi.yml").write_text(
                "openapi: 3.1.0\npaths:\n  /x:\n    trace:\n      responses:\n"
                '        "200": {description: ok}\n',
                encoding="utf-8",
            )
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        payload = json.loads(completed.stdout)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(
            [str(fixture / "openapi.yml")], [source["path"] for source in payload["sources"]]
        )
        self.assertEqual(
            [], [row for row in payload["rows"] if row["selector"] == "pathItem.trace"]
        )

    def test_an_unfetched_link_ok_source_is_a_hard_failure_not_a_silent_zero(self) -> None:
        """93 of the 124 registered sources are fetched; a silent zero would lie."""
        with tempfile.TemporaryDirectory() as directory:
            completed = run("--corpus-root", directory)
            self.assertEqual(1, completed.returncode, completed.stdout)
            self.assertIn("have not been fetched", completed.stderr)
            self.assertIn("just surface-census", completed.stderr)

            allowed = run("--corpus-root", directory, "--allow-unfetched", "--selector", "openapi.info")
            self.assertEqual(0, allowed.returncode, allowed.stderr)
            self.assertIn("is unfetched", allowed.stderr)
            self.assertIn("32 vendored, 0 fetched", allowed.stderr)

            payload = json.loads(
                run("--corpus-root", directory, "--allow-unfetched", "--json").stdout
            )
            corpus = [s for s in payload["sources"] if s["origin"] == "corpus"]
            self.assertGreater(len(corpus), 50, "the link-ok half is missing from the report")
            # Listed as registered but read as nothing: a path of null is the
            # difference between "declares nothing" and "was never opened".
            self.assertEqual({None}, {source["path"] for source in corpus})
            self.assertEqual(
                set(), {row["fixture"] for row in payload["rows"]} & {s["fixture"] for s in corpus}
            )

    def test_a_selector_the_grammar_cannot_emit_is_refused(self) -> None:
        """An unrefused typo would manufacture the evidence a `gap` row cites."""
        for selector, expected in (
            ("pathitem.trace", "Did you mean: pathItem.trace"),
            ("schema.notAKeyword", "is not a selector of the OpenAPI object model"),
            ("operation.tags=x", "is not one of the fields that emit a valued selector"),
            ("parameter.in=", "valued selector with no value"),
            ("notAnObject.x-thing", "is not an object the census walks"),
            ("operation.tags:mutliple", "Did you mean: operation.tags:multiple"),
            ("openapi.paths:collision", "is not one of the predicate selectors"),
        ):
            with self.subTest(selector=selector):
                completed = run("--vendored-only", "--selector", selector)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn(expected, completed.stderr)
                self.assertNotIn("declared by no registered source", completed.stdout)

    def test_every_selector_the_census_emits_is_one_the_grammar_accepts(self) -> None:
        """The enumeration that refuses a typo and the walk that emits must agree."""
        emitted = {selector for selector, _ in rows(run("--vendored-only"))}
        self.assertGreater(len(emitted), 50, "the vendored census reported almost nothing")
        refused = {s: census.selector_error(s) for s in emitted if census.selector_error(s)}
        self.assertEqual({}, refused, "the census emits selectors its own grammar refuses")

    def test_a_source_whose_root_is_not_a_mapping_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "listy", "- openapi: 3.0.3\n")
            completed = run("--vendored-only", "--fixtures-root", str(root))
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("is not an OpenAPI document", completed.stderr)
        self.assertIn("root is not a mapping", completed.stderr)

    def test_a_fixtures_root_without_the_corpus_manifest_is_refused(self) -> None:
        """The link-ok half is read out of CORPUS.md; its absence is not zero rows."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "solo", "openapi: 3.0.3\ninfo: {title: solo, version: \"1\"}\n")
            completed = run("--fixtures-root", str(root), "--corpus-root", directory)
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("missing corpus manifest", completed.stderr)

    def test_an_unknown_fixture_name_is_refused_with_what_the_names_are(self) -> None:
        completed = run("--vendored-only", "--fixture", "not-a-fixture")
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("no registered source is named 'not-a-fixture'", completed.stderr)
        self.assertIn("CORPUS.md", completed.stderr)

    def test_an_unreadable_document_names_the_file_and_the_line(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "broken", """\
                openapi: 3.0.3
                info:
                  title: broken
                paths:
                  /a: !ruby/object:Thing
                """)
            completed = run("--vendored-only", "--fixtures-root", str(root))
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("broken", completed.stderr)
        self.assertIn("openapi.yml:5:", completed.stderr)
        self.assertIn("YAML tags are not supported", completed.stderr)

    def test_a_bad_invocation_is_refused(self) -> None:
        completed = run("--nonsense")
        self.assertEqual(2, completed.returncode, completed.stdout)
        self.assertIn("unrecognized arguments", completed.stderr)
        missing = run("--vendored-only", "--fixtures-root", "/nonexistent-root")
        self.assertEqual(1, missing.returncode, missing.stdout)
        self.assertIn("missing fixtures root", missing.stderr)


@unittest.skipIf(os.name == "nt", "scripts/corpus-lib.sh is a POSIX shell library")
class CorpusManifestAgreementTests(unittest.TestCase):
    """The census reads CORPUS.md; so does scripts/corpus-lib.sh. Pin them together.

    `manifest_rows` and `corpus_aliases` are second readers of the manifest and
    the alias file — the first is the shell library `scripts/fetch-corpus.sh`
    uses. A row grammar that drifted would leave the census counting a different
    set of registered sources than the fetch populates, and it would drift
    *quietly*: a source the census never lists is one it can never report as
    declaring anything, which is the one direction a "never seen" census must not
    err in.
    """

    def shell(self, snippet: str) -> str:
        return subprocess.run(
            ["bash", "-c", f". scripts/corpus-lib.sh\n{snippet}"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout

    def test_the_census_registers_exactly_the_rows_the_fetcher_fetches(self) -> None:
        shell_rows = [
            line.split("\t")[0]
            for line in self.shell("corpus_rows tests/fixtures/CORPUS.md").splitlines()
            if line.strip()
        ]
        self.assertGreater(len(shell_rows), 50, "corpus-lib.sh reported almost no rows")
        self.assertEqual(shell_rows, list(census.manifest_rows(FIXTURES / "CORPUS.md")))

    def test_the_census_resolves_an_alias_the_way_the_fetcher_does(self) -> None:
        aliases = census.corpus_aliases(FIXTURES)
        self.assertTrue(aliases, "the alias file is empty or unreadable")
        for name in [*aliases, "apideck.com-crm"]:
            with self.subTest(name=name):
                self.assertEqual(
                    self.shell(f'corpus_fixture_for "{name}"').strip(),
                    aliases.get(name, name),
                )


class YamlSubsetTests(unittest.TestCase):
    """The loader is the census's one non-obvious dependency, so it is pinned here.

    `just check` installs no Python packages and runs on Linux, macOS and Windows,
    so the loader is standard-library-only; these cases are the constructs real
    OpenAPI documents in the corpus actually use.
    """

    def load(self, document: str):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "openapi.yml"
            path.write_text(textwrap.dedent(document), encoding="utf-8")
            return census.load_document(path)

    def refusal(self, document: str) -> str:
        with self.assertRaises(census.DocumentError) as raised:
            self.load(document)
        return str(raised.exception)

    def test_anchors_aliases_and_merge_keys(self) -> None:
        self.assertEqual(
            {"a": ["x"], "b": ["x"], "c": {"k": 1, "j": 2}},
            self.load("""\
                a: &ref
                  - x
                b: *ref
                c:
                  <<: {k: 1}
                  j: 2
                """),
        )

    def test_a_block_sequence_may_sit_at_its_key_s_own_indentation(self) -> None:
        self.assertEqual(
            {"servers": [{"url": "u", "description": "d"}], "after": 1},
            self.load("""\
                servers:
                - url: u
                  description: d
                after: 1
                """),
        )

    def test_block_scalars_fold_chomp_and_keep(self) -> None:
        loaded = self.load("""\
            literal: |
              one
              two
            folded: >-
              one
              two

              three
            kept: |+
              one

            """)
        self.assertEqual("one\ntwo\n", loaded["literal"])
        self.assertEqual("one two\nthree", loaded["folded"])
        self.assertEqual("one\n\n", loaded["kept"])

    def test_a_scalar_may_be_written_under_its_key_and_wrap(self) -> None:
        self.assertEqual(
            {"description": "one two", "next": 1},
            self.load("""\
                description:
                  one
                  two
                next: 1
                """),
        )

    def test_a_quoted_scalar_spans_lines_without_losing_its_escapes(self) -> None:
        """A real corpus document (slurmdb-rest) writes both in one scalar: a `\\n`
        escape that must survive, and a trailing `\\` that cancels the source
        break along with the next line's indentation."""
        loaded = self.load('description: "a\\nb\\\n  c d"\n')
        self.assertEqual("a\nbc d", loaded["description"])

    def test_a_hash_inside_a_quoted_scalar_is_not_a_comment(self) -> None:
        self.assertEqual(
            {"a": {"$ref": "#/components/schemas/A"}, "b": 1},
            self.load("""\
                a:
                  $ref: "#/components/schemas/A"  # a real comment
                b: 1
                """),
        )

    def test_an_escaped_quote_does_not_end_the_scalar_a_comment_could_follow(self) -> None:
        self.assertEqual(
            {"a": 'he said "hi" # not a comment', "b": 1},
            self.load('a: "he said \\"hi\\" # not a comment"  # a real one\nb: 1\n'),
        )
        self.assertEqual(
            {"a": 'say " hi', "b": 1},
            self.load('a: "say \\" hi"  # a real one\nb: 1\n'),
        )

    def test_flow_collections_and_url_keys(self) -> None:
        self.assertEqual(
            {"info": {"title": "t", "tags": [1, "two"]}, "https://x.test": "y"},
            self.load("""\
                info: {title: t, tags: [1, two]}
                https://x.test: y
                """),
        )

    def test_the_core_schema_resolves_plain_scalars(self) -> None:
        self.assertEqual(
            {"n": None, "t": True, "f": False, "i": -3, "x": 1.5, "s": "3.0.1", "q": "1"},
            self.load("n: ~\nt: true\nf: false\ni: -3\nx: 1.5\ns: 3.0.1\nq: '1'\n"),
        )

    def test_unsupported_constructs_are_refused_by_name_and_line(self) -> None:
        for document, expected in (
            ("a: 1\n---\nb: 2\n", "more than one YAML document"),
            ("%YAML 1.2\n---\na: 1\n", "YAML directives are not supported"),
            ("a:\n\t- 1\n", "tabs cannot indent YAML"),
            ('a: "unterminated\n', "never closed"),
            ("a: [1, 2\n", "never closed"),
            ("? [a]\n: 1\n", "explicit `? ` mapping keys"),
            (": 1\n", "an empty mapping key"),
            ("info:\n  : 1\n", "an empty mapping key"),
            ("a: 1\nb\n", "expected a `key: value` mapping entry"),
        ):
            with self.subTest(document=document):
                self.assertIn(expected, self.refusal(document))

    def test_a_json_source_is_read_as_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "openapi.json"
            path.write_text('{"openapi": "3.1.0"}', encoding="utf-8")
            self.assertEqual({"openapi": "3.1.0"}, census.load_document(path))
            path.write_text("{oops", encoding="utf-8")
            with self.assertRaises(census.DocumentError) as raised:
                census.load_document(path)
            self.assertIn("is not valid JSON", str(raised.exception))


class FlowCollectionRegressionTests(unittest.TestCase):
    """The flow-collection parser, pinned against the defect that wedged the gate.

    A one-line edit disabled the branch that consumes the `:` of a flow *mapping*.
    `flow_node` stops at `,]}:` without consuming what it stopped at, so the loop
    re-entered on the same cursor and appended forever — 9.6 GB of RSS and no
    output, on eight of the vendored documents, for every selector. The three
    properties below are what make that unrepeatable: it terminates, it terminates
    with the *right values*, and a cursor that cannot advance is an error.
    """

    # `info: { title: Widget API, version: 1.0.0 }` is the shape that stalled.
    FLOW_MAPPINGS = "audience-filter"

    def test_the_whole_vendored_corpus_censuses_within_the_timeout(self) -> None:
        """The unscoped vendored run — the exact invocation that never returned."""
        completed = run("--vendored-only")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("32 vendored", completed.stderr)
        self.assertGreater(len(rows(completed)), 100)

    def test_a_flow_mapping_parses_to_its_entries_not_a_list_of_its_keys(self) -> None:
        """Terminating is not enough: the disabled branch also built the wrong value."""
        document = census.load_document(FIXTURES / self.FLOW_MAPPINGS / "openapi.yml")
        self.assertEqual({"title": "Widget API", "version": "1.0.0"}, document["info"])
        widget = document["components"]["schemas"]["Widget"]["properties"]
        self.assertEqual({"type": "string"}, widget["id"])

        counted = rows(run("--vendored-only", "--fixture", self.FLOW_MAPPINGS))
        self.assertEqual(1, counted[("info.title", self.FLOW_MAPPINGS)])
        self.assertEqual(1, counted[("info.version", self.FLOW_MAPPINGS)])

    def test_the_recursive_callback_construct_terminates_with_its_count(self) -> None:
        """A Callback holds a Path Item holding Operations that may declare callbacks.

        The object model is recursive by construction, so the walk carries an
        ancestor set and a `$ref` is counted as a Reference Object rather than
        followed. This is the selector the wedged run was scoped to, so it is
        pinned bounded and by count rather than merely by "it finished".
        """
        completed = run("--vendored-only", "--selector", "operation.callbacks")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({("operation.callbacks", WEBHOOKS): 1}, rows(completed))

    def test_a_flow_collection_that_cannot_advance_is_a_parse_error_not_a_hang(self) -> None:
        """The guard that makes the failure mode a message instead of an OOM.

        `{a]` balances by bracket count, so it reaches the collection loop, where
        `flow_node` stops at the `]` the loop does not recognise and consumes
        nothing. Without the progress check that is an infinite append.
        """
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "openapi.yml"
            path.write_text("info: {a]\n", encoding="utf-8")
            with self.assertRaises(census.DocumentError) as raised:
                census.load_document(path)
        self.assertIn("stalls", str(raised.exception))


@unittest.skipIf(
    os.name == "nt",
    "the POSIX shell resolver's semantics are not reproduced by MSYS",
)
class CensusInterpreterTests(unittest.TestCase):
    """Pin the census interpreter's repository provenance."""

    RESOLVER = REPO / "scripts" / "census-python.sh"

    def shell(self) -> str:
        shell = shutil.which("bash")
        if shell is None:
            self.skipTest("no bash on PATH to run the resolver")
        return shell

    def shell_path(self, path: Path) -> str:
        """Return the spelling Bash uses for a native path."""
        completed = subprocess.run(
            [self.shell(), "-c", 'cd "$1" && pwd -P', "census-path", str(path)],
            capture_output=True,
            text=True,
            timeout=CENSUS_TIMEOUT,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        return completed.stdout.strip()

    def resolve(self, path: str | None = None) -> subprocess.CompletedProcess:
        # Resolved before PATH is replaced: these cases hand the resolver a PATH
        # with no interpreter on it, which would otherwise hide `bash` too.
        shell = self.shell()
        environment = dict(os.environ)
        if path is not None:
            environment["PATH"] = path
        return subprocess.run(
            [shell, str(self.RESOLVER)],
            cwd=REPO,
            capture_output=True,
            text=True,
            env=environment,
            timeout=CENSUS_TIMEOUT,
        )

    def test_both_census_recipes_resolve_the_interpreter_through_the_resolver(self) -> None:
        for recipe in ("surface-census", "test-surface-census"):
            with self.subTest(recipe=recipe):
                body = " ".join(recipe_body(recipe))
                self.assertIn('"$(./scripts/census-python.sh)"', body)
                self.assertNotRegex(body, r"(?<!census-)\bpython3 ")

    def test_the_resolver_names_a_real_interpreter_that_is_not_a_virtualenv(self) -> None:
        completed = self.resolve()
        self.assertEqual(0, completed.returncode, completed.stderr)
        interpreter = completed.stdout.strip()
        exists = subprocess.run(
            [self.shell(), "-c", 'test -f "$1"', "census-python", interpreter],
            timeout=CENSUS_TIMEOUT,
        )
        self.assertEqual(0, exists.returncode, interpreter)
        prefixes = subprocess.run(
            [
                self.shell(), "-c", '"$1" -c "$2"', "census-python", interpreter,
                "import sys; print(sys.prefix); print(sys.base_prefix)",
            ],
            capture_output=True,
            text=True,
            timeout=CENSUS_TIMEOUT,
        )
        self.assertEqual(0, prefixes.returncode, prefixes.stderr)
        # This repository commits no virtualenv, so PATH's system Python is the
        # answer here. A deliberate local `.venv` would win instead, which is the
        # preference the next case drives.
        self.assertFalse((REPO / ".venv").exists(), "this case assumes no local .venv")
        first, second = prefixes.stdout.split()
        self.assertEqual(first, second, "the resolver chose a virtualenv")

    def test_a_repo_local_venv_is_preferred_over_anything_on_path(self) -> None:
        """The first branch, driven rather than tolerated.

        A `.venv` beside the resolver IS this repository's own environment, so it
        outranks PATH — including a perfectly good system Python that would other-
        wise be chosen. Driven by copying the real resolver into a root that has
        one, because the resolver locates the repository from its own path.
        """
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            local = root / ".venv" / ("Scripts" if os.name == "nt" else "bin")
            local.mkdir(parents=True)
            interpreter = local / ("python.exe" if os.name == "nt" else "python3")
            shutil.copy2(Path(sys.executable).resolve(), interpreter)
            copied = root / "scripts" / self.RESOLVER.name
            shutil.copy2(self.RESOLVER, copied)

            completed = subprocess.run(
                [self.shell(), str(copied)], capture_output=True, text=True,
                timeout=CENSUS_TIMEOUT,
            )
            expected = f"{self.shell_path(local)}/{interpreter.name}"

            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertTrue(
                os.path.samefile(expected, completed.stdout.strip()),
                f"{expected!r} and {completed.stdout.strip()!r} are not the same file",
            )

    def test_a_foreign_virtualenv_is_refused_by_name_rather_than_used(self) -> None:
        """Driven against a real virtualenv, because that is the case that happened."""
        with tempfile.TemporaryDirectory() as directory:
            foreign = Path(directory) / "other-project" / ".venv"
            built = subprocess.run(
                [sys.executable, "-m", "venv", "--without-pip", str(foreign)],
                capture_output=True, text=True, timeout=CENSUS_TIMEOUT,
            )
            if built.returncode != 0:
                self.skipTest(f"this interpreter cannot build a venv: {built.stderr}")

            scripts = foreign / ("Scripts" if os.name == "nt" else "bin")
            completed = self.resolve(path=str(scripts))
            self.assertEqual(1, completed.returncode, completed.stdout)
            self.assertEqual("", completed.stdout.strip())
            self.assertIn("another project's virtualenv", completed.stderr)
            self.assertIn(str(foreign), completed.stderr)

    def test_no_python3_at_all_is_a_named_failure_rather_than_a_fall_through(self) -> None:
        with tempfile.TemporaryDirectory() as empty:
            completed = self.resolve(path=empty)
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertEqual("", completed.stdout.strip())
        self.assertIn("no python3 on PATH", completed.stderr)


class PyYamlOracleTests(unittest.TestCase):
    """Where a real YAML implementation is available, the loader must agree with it.

    **This oracle is optional by design, not required.** The gate installs no
    Python packages and runs on the Linux/macOS/Windows matrix, so the interpreter
    `scripts/census-python.sh` resolves may legitimately have no PyYAML — making
    its absence an error would fail the gate on a correct host. The loader's
    behaviour is therefore pinned unconditionally by `YamlSubsetTests` and
    `FlowCollectionRegressionTests`, which need nothing installed; this class is a
    bonus check that runs wherever PyYAML happens to be importable. The skip names
    the interpreter, so a skip is always attributable rather than anonymous.
    """

    def test_the_census_matches_pyyaml_on_every_vendored_document(self) -> None:
        try:
            import yaml
        except ImportError:
            self.skipTest(f"PyYAML is not importable on {sys.executable}")
        documents = sorted(FIXTURES.glob("*/openapi.y*ml"))
        self.assertGreater(len(documents), 20)
        for path in documents:
            with self.subTest(document=path.name):
                mine = census.census_document(census.load_document(path))
                theirs = census.census_document(yaml.safe_load(path.read_text(encoding="utf-8")))
                self.assertEqual(theirs, mine)



class RankedBacklogTests(unittest.TestCase):
    """The index's synthesis restates the six region files; recompute it from them.

    `## Ranked gap backlog` is an aggregate — per-region category counts, one
    ranked `FIXTURE` list, one `PROBE` list, and a per-`src/`-file join against
    `just fixtures-coverage`. Every number in it is owned somewhere else, so
    without these the section goes stale silently the first time a region row is
    added or reclassified. The coverage figures are the one input no offline gate
    can re-derive; what is checked here is that the two tables carrying them agree
    with each other, which is what the ranking's second criterion rests on.
    """

    DOC = REPO / "docs" / "openapi-surface-coverage.md"
    REGIONS = REPO / "docs" / "openapi-surface"
    CATEGORIES = ("golden", "limitations", "gap")
    SETTLEMENTS = ("FIXTURE", "PROBE", "UNREACHABLE")
    PROBE_KINDS = ("structural", "witness-supply")
    WITNESS_SEARCH = WITNESS_SEARCH_HEADING

    @classmethod
    def setUpClass(cls) -> None:
        cls.doc = cls.DOC.read_text(encoding="utf-8")
        cls.entries = {}
        for path in sorted(cls.REGIONS.glob("*.md")):
            for cells in cls.region_rows(path.read_text(encoding="utf-8")):
                cls.entries[cells[0].strip("`")] = (path.stem, cells)

    @staticmethod
    def region_rows(text: str) -> list[list[str]]:
        """Every entry-table row of one region file, as its eight cells.

        `\\|` inside a cell is an escaped pipe, not a column break — one row's
        `crozier sites` cell holds a Rust `match` pattern that uses it.
        """
        rows = []
        for line in text.splitlines():
            if not line.startswith("| "):
                continue
            cells = [
                cell.replace("\x00", "\\|").strip()
                for cell in line.replace("\\|", "\x00").strip().strip("|").split("|")
            ]
            if len(cells) == 8 and cells[3].strip("`") in RankedBacklogTests.CATEGORIES:
                rows.append(cells)
        return rows

    def section(self, start: str, end: str | None = None) -> str:
        self.assertIn(start, self.doc, f"the index no longer carries {start!r}")
        body = self.doc.split(start, 1)[1]
        return body if end is None else body.split(end, 1)[0]

    def settlement_of(self, cells: list[str]) -> str:
        first = cells[7].lstrip("`*").split(" ", 1)[0].strip("`*—")
        self.assertIn(first, self.SETTLEMENTS, f"unknown settlement class in {cells[0]}")
        return first

    def gaps(self, settlement: str) -> set[str]:
        return {
            key
            for key, (_region, cells) in self.entries.items()
            if cells[3].strip("`") == "gap" and self.settlement_of(cells) == settlement
        }

    def ranked_rows(self) -> list[tuple[int, str, tuple[int, int, int, int], str]]:
        """(rank, key, the four published criteria, the whole line)."""
        out = []
        for line in self.section(
            "### The ranked `FIXTURE` backlog", "### The ranked list against"
        ).splitlines():
            row = re.match(r"\| (\d+) \| \[`([^`]+)`\]", line)
            if not row:
                continue
            measured = [int(value) for value in re.findall(r"\*\*(\d+)\*\*", line)]
            self.assertEqual(
                4, len(measured), f"{row.group(2)} does not publish four measured criteria"
            )
            out.append((int(row.group(1)), row.group(2), tuple(measured), line))
        self.assertEqual(
            bool(self.gaps("FIXTURE")),
            bool(out),
            "the ranked backlog table does not parse to the `FIXTURE` gaps there are",
        )
        return out

    def blind_spot_table(self) -> dict[str, tuple[int, str, str]]:
        """`src/` file -> (printed count, per-tier breakdown, the ranked-gaps cell)."""
        found = {}
        for line in self.section("| `src/` file | printed |", "**Where the two").splitlines():
            row = re.match(r"\| `(src/[a-z_]+\.rs)` \| (\d+) \| ([^|]+) \| ([^|]+) \|", line)
            if row:
                found[row.group(1)] = (
                    int(row.group(2)), row.group(3).strip(), row.group(4).strip()
                )
        self.assertTrue(found, "the golden blind spots join table no longer parses")
        return found

    def test_every_enumerated_feature_is_classified_exactly_once(self) -> None:
        """One key per feature, and no spec location owned by two regions."""
        keys = [
            cells[0].strip("`")
            for path in sorted(self.REGIONS.glob("*.md"))
            for cells in self.region_rows(path.read_text(encoding="utf-8"))
        ]
        self.assertEqual(len(keys), len(set(keys)), "a feature key appears in two rows")
        stated = re.search(r"The (\d+) rows carry (\d+) distinct\s+keys", self.doc)
        self.assertIsNotNone(stated, "the reconciliation no longer states the row count")
        self.assertEqual(
            [len(keys), len(set(keys))],
            [int(stated.group(1)), int(stated.group(2))],
            "the reconciliation's row count is not the walk's own",
        )
        owners: dict[str, set[str]] = {}
        for region, cells in self.entries.values():
            owners.setdefault(cells[2], set()).add(region)
        shared = {loc: sorted(names) for loc, names in owners.items() if len(names) > 1}
        self.assertEqual({}, shared, "a spec location is classified in two region files")

    def test_the_summary_table_is_the_six_region_files_own_row_counts(self) -> None:
        """Per-region totals, recomputed from the tables they aggregate."""
        stated = {}
        for line in self.section("### What the walk enumerated", "The walk enumerated").splitlines():
            row = re.match(
                r"\| \[`([a-z0-9-]+)`\][^|]*\|" + r"\s*(\d+)\s*\|" * 7, line
            )
            if row:
                stated[row.group(1)] = [int(row.group(n)) for n in range(2, 9)]
        self.assertEqual(6, len(stated), "the summary table no longer lists six regions")
        totals = re.search(
            r"\| \*\*total\*\* \|" + r"\s*\*\*(\d+)\*\*\s*\|" * 7,
            self.section("### What the walk enumerated", "The walk enumerated"),
        )
        self.assertIsNotNone(totals, "the summary table no longer carries a total row")
        self.assertEqual(
            [sum(column) for column in zip(*stated.values())],
            [int(totals.group(n)) for n in range(1, 8)],
            "the total row is not the six region rows' own column sums",
        )
        for region, numbers in sorted(stated.items()):
            with self.subTest(region=region):
                rows = [c for r, c in self.entries.values() if r == region]
                counts = [len(rows)]
                counts += [
                    sum(1 for cells in rows if cells[3].strip("`") == category)
                    for category in self.CATEGORIES
                ]
                counts += [
                    sum(
                        1
                        for cells in rows
                        if cells[3].strip("`") == "gap"
                        and self.settlement_of(cells) == settlement
                    )
                    for settlement in self.SETTLEMENTS
                ]
                self.assertEqual(counts, numbers)

    def test_the_prose_totals_are_the_summary_tables_own_column_sums(self) -> None:
        """The narrated per-category and per-settlement totals are the table's own."""
        rows = list(self.entries.values())
        totals = [len(rows)]
        totals += [
            sum(1 for _r, cells in rows if cells[3].strip("`") == category)
            for category in self.CATEGORIES
        ]
        prose = self.section("The walk enumerated", "**What the `gap` count means.**")
        narrated = [int(value.replace(",", "")) for value in re.findall(r"\*\*([\d,]+)\*\*", prose)]
        self.assertEqual(totals + [len(self.gaps(s)) for s in self.SETTLEMENTS], narrated)
        self.assertEqual(
            totals[3],
            sum(len(self.gaps(s)) for s in self.SETTLEMENTS),
            "the settlement classes do not partition the gap rows",
        )

    def test_the_gap_count_paragraph_recomputes_its_own_numbers(self) -> None:
        """What `gap` means restates the gap total twice, then its two parts."""
        gap = sum(
            1 for _region, cells in self.entries.values() if cells[3].strip("`") == "gap"
        )
        unreachable = len(self.gaps("UNREACHABLE"))
        prose = self.section("**What the `gap` count means.**", "### Reconciliation")
        self.assertEqual(
            [gap, gap, unreachable, gap - unreachable],
            [int(value) for value in re.findall(r"\b(\d+)\b", prose)],
            "the paragraph's counts are not the walk's own gap totals",
        )

    def ledger_keys(self) -> set[str]:
        """The keys the index's own documented join reports, run here."""
        pattern = re.search(
            r"^grep -oP '(.+)' docs/fern-limitations\.md", self.doc, re.M
        )
        self.assertIsNotNone(pattern, "the index no longer documents the join command")
        before, _, after = pattern.group(1).partition("\\K")
        ledger = (REPO / "docs" / "fern-limitations.md").read_text(encoding="utf-8")
        return set(re.findall(f"{before}({after})", ledger, re.M))

    def test_the_reconciliation_counts_the_rows_it_narrates(self) -> None:
        """How many spec locations carry several rows, and the three named by size."""
        owners: dict[str, int] = {}
        for _region, cells in self.entries.values():
            owners[cells[2]] = owners.get(cells[2], 0) + 1
        shared = {loc: count for loc, count in owners.items() if count > 1}
        flat = " ".join(
            self.section(
                "**Each feature is classified exactly once.**", "**Nothing is left"
            ).split()
        )
        stated = re.search(r"(\w+) spec locations carry more than one row", flat)
        self.assertIsNotNone(stated, "the reconciliation no longer counts the shared locations")
        self.assertEqual(len(shared), {"Thirteen": 13}.get(stated.group(1)))
        named = 0
        for location, count in sorted(shared.items()):
            if f"`{location}`" not in flat:
                continue
            named += 1
            with self.subTest(location=location):
                follows = re.search(
                    rf"`{re.escape(location)}`(?: heads)? (\d+)", flat
                )
                self.assertIsNotNone(follows, f"{location} is named without its row count")
                self.assertEqual(count, int(follows.group(1)))
        self.assertEqual(3, named, "the reconciliation no longer names three locations by size")

    def test_the_ledger_join_counts_the_keys_it_reports(self) -> None:
        """Every key the join reports, split into the ones a region row spells
        verbatim and the remainder each accounted for by a row of its own."""
        keys = self.ledger_keys()
        verbatim = keys & set(self.entries)
        text = self.section("**Every ledger key is accounted for.**", "**The one correction")
        stated = re.search(
            r"canonical join reports (\d+) keys, of\nwhich (\d+) are a region row's key verbatim", text
        )
        self.assertIsNotNone(stated, "the reconciliation no longer counts the join")
        self.assertEqual((len(keys), len(verbatim)), (int(stated.group(1)), int(stated.group(2))))
        unaccounted = sorted(keys - verbatim)
        self.assertEqual(
            len(unaccounted),
            len(re.findall(r"^\| `([^`]+)` \|", text, re.M)),
            "the table of unaccounted keys is not the join's own remainder",
        )
        for key in unaccounted:
            self.assertIn(f"| `{key}` |", text, f"{key} has no row saying how it is accounted for")
        yielded = re.search(r"The join's real yield is (\d+)\.", text)
        self.assertIsNotNone(yielded, "the reconciliation no longer states the join's real yield")
        self.assertEqual(len(keys) - 1, int(yielded.group(1)), "one key is the non-feature label")

    def test_the_ranked_backlog_is_every_fixture_gap_in_rubric_order(self) -> None:
        """One total order over every `FIXTURE` row, by the four published numbers."""
        ranked = self.ranked_rows()
        self.assertEqual(self.gaps("FIXTURE"), {key for _n, key, _m, _line in ranked})
        self.assertEqual(
            list(range(1, len(ranked) + 1)), [n for n, _key, _m, _line in ranked]
        )
        sortable = [
            ((sites, -blind, -breadth, -witnesses, key), rank)
            for rank, key, (sites, blind, breadth, witnesses), _line in ranked
        ]
        self.assertEqual(sorted(sortable), sortable, "the ranked table is not in rubric order")
        stated = re.search(r"All (\d+) `FIXTURE` gaps", self.doc)
        self.assertIsNotNone(stated, "the ranked backlog no longer states its own size")
        self.assertEqual(len(ranked), int(stated.group(1)))

    def test_the_ranked_table_names_each_keys_owning_region(self) -> None:
        """The `region` column and the per-row link, against the file the key is in."""
        for _rank, key, _measured, line in self.ranked_rows():
            with self.subTest(key=key):
                region = self.entries[key][0]
                self.assertIn(f"](openapi-surface/{region}.md)", line)
                self.assertIn(f"| `{region}` |", line)

    def test_criterion_one_is_the_region_rows_own_crozier_sites_count(self) -> None:
        """Criterion 1 is the `crozier sites` cell's own integer, not a second copy.

        A cell spells its count several ways — ``` `src/ir.rs`: 6 places ```,
        `src/ir.rs (3 places)`, ``` `src/ir.rs` — 1 ``` — so the count is every
        integer that follows a `src/` file name, and a `src/ir.rs:627` line
        reference is excluded by the digit that follows its colon.
        """
        for _rank, key, measured, _line in self.ranked_rows():
            with self.subTest(key=key):
                cell = self.entries[key][1][5]
                if cell.lstrip("`").startswith("none"):
                    self.assertEqual(0, measured[0], "a `none` cell scores zero sites")
                    continue
                counted = re.findall(r"src/[a-z_]+\.rs`?(?!:\d)[^0-9A-Za-z]{0,14}(\d+)", cell)
                self.assertTrue(counted, f"{key}'s `crozier sites` cell states no count")
                self.assertEqual(sum(int(n) for n in counted), measured[0])

    def test_criterion_three_counts_the_artifact_kinds_its_own_cell_lists(self) -> None:
        """Criterion 3 is a reading of the region row's prose, so it is stated once.

        The region files name the artifacts in prose and publish no breadth
        number; this column normalizes that prose over the vocabulary the criteria
        list defines. What is checkable is that the number is the list beside it
        and that every name in the list is one of the six.
        """
        vocabulary = set(
            re.findall(
                r"`([a-z_./]+)`",
                self.section("**Criterion 3**, artifact breadth", "- **Criterion 4**"),
            )
        )
        self.assertEqual(6, len(vocabulary), "the criteria list no longer names six kinds")
        for _rank, key, measured, line in self.ranked_rows():
            with self.subTest(key=key):
                listed = line.split("|")[6].split("(", 1)[1].rsplit(")", 1)[0].split(", ")
                self.assertEqual(measured[2], len(listed))
                self.assertEqual(set(), set(listed) - vocabulary, "an artifact kind is not one of the six")

    def test_the_ranked_backlog_publishes_its_own_median_blind_spot_count(self) -> None:
        """The number the extension rule is stated in, recomputed from the rows.

        An exhausted backlog has no median, so the index must publish none — the
        `FIXTURE` gaps having all been settled, a number here could only be a
        leftover from the last list that had rows.
        """
        blind = sorted(measured[1] for _n, _key, measured, _line in self.ranked_rows())
        stated = re.search(
            r"\*\*The median blind-spot count of this list is (\d+)\*\*", self.doc
        )
        if not blind:
            self.assertIsNone(stated, "an empty ranked list has no median to publish")
            return
        median = blind[len(blind) // 2] if len(blind) % 2 else (
            blind[len(blind) // 2 - 1] + blind[len(blind) // 2]
        ) // 2
        self.assertIsNotNone(stated, "the ranked backlog no longer publishes its median")
        self.assertEqual(median, int(stated.group(1)))

    def test_each_ranked_row_reads_its_blind_spot_count_off_the_join_table(self) -> None:
        """Criterion 2 is the join table's own `printed` column, summed per row."""
        blind_spots = self.blind_spot_table()
        for _rank, key, measured, line in self.ranked_rows():
            with self.subTest(key=key):
                named = re.findall(r"`(src/[a-z_]+\.rs)` \d+", line)
                sites_named, blind_named = named[: len(named) // 2], named[len(named) // 2 :]
                self.assertEqual(
                    sites_named,
                    blind_named,
                    "criterion 2 does not score the files criterion 1 names",
                )
                self.assertEqual(
                    sum(blind_spots[name][0] for name in blind_named),
                    measured[1],
                    "criterion 2 is not the join table's printed count",
                )
                if not named:
                    self.assertEqual(
                        (0, 0), (measured[0], measured[1]), "a `none` row must score zero twice"
                    )

    def test_the_join_table_names_the_ranked_gaps_that_point_at_each_file(self) -> None:
        """The `ranked gaps pointing at it` cells are the ranked table's own counts."""
        pointing: dict[str, int] = {}
        for _rank, _key, _measured, line in self.ranked_rows():
            for name in set(re.findall(r"`(src/[a-z_]+\.rs)` \d+", line)):
                pointing[name] = pointing.get(name, 0) + 1
        for name, (_printed, _by_tier, cell) in sorted(self.blind_spot_table().items()):
            with self.subTest(file=name):
                stated = 0 if cell.startswith("none") else int(re.match(r"(\d+)", cell).group(1))
                self.assertEqual(pointing.get(name, 0), stated)

    def test_the_join_table_is_the_coverage_reports_own_blind_spot_block(self) -> None:
        """The one input outside `just check`, reconciled whenever its export exists.

        `just fixtures-coverage` needs network and an instrumented corpus run, so
        the gate cannot produce the measurement — but it can refuse a table that
        disagrees with the last one produced. The recipe's own
        `blind_spots()` renders the comparison, and the export paths and tier
        names are read out of `scripts/fixtures-coverage.sh`, so renaming either
        fails this case rather than turning it into a permanent silent skip. It
        skips, named, when the exports are absent, the way the corpus byte-diffs
        skip an unfetched spec.
        """
        recipe = (REPO / "scripts" / "fixtures-coverage.sh").read_text(encoding="utf-8")
        out_dir = re.search(r'^out_dir="\$repo_root/([^"]+)"', recipe, re.M)
        golden = re.search(r"^  --golden-tier (\S+)", recipe, re.M)
        self.assertTrue(out_dir and golden, "fixtures-coverage.sh no longer names its exports")
        exports = REPO / out_dir.group(1)
        names = re.findall(r'--output-path "\$out_dir/([a-z0-9-]+)\.json"', recipe)
        self.assertIn(golden.group(1), names, "the golden tier has no export in the recipe")
        order = [golden.group(1)] + sorted(name for name in names if name != golden.group(1))
        missing = sorted(name for name in order if not (exports / f"{name}.json").is_file())
        if missing:
            self.skipTest(
                f"no {', '.join(missing)} export in {exports}; run `just fixtures-coverage`"
            )
        spec = importlib.util.spec_from_file_location(
            "fixtures_coverage_report", REPO / "scripts" / "fixtures-coverage-report.py"
        )
        report = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(report)
        tiers = {name: report.load_tier(exports / f"{name}.json", REPO) for name in order}
        report.drop_test_regions(tiers, REPO)
        measured, total = {}, None
        for line in report.blind_spots(tiers, golden.group(1), order):
            row = re.match(r"  (src/\S+)\s+(\d+)\s+\((.+)\)$", line)
            if row:
                measured[row.group(1)] = (int(row.group(2)), row.group(3))
            elif line.startswith("  total "):
                total = line.strip()
        self.assertTrue(measured, "the report's blind-spot block no longer parses")
        self.assertEqual(
            measured,
            {name: cells[:2] for name, cells in self.blind_spot_table().items()},
            "the join table is not the last `just fixtures-coverage` run's blind spots",
        )
        self.assertIn(
            f"`{total}`", self.doc, "the join table does not quote the report's own total line"
        )

    def test_the_ranked_backlog_counts_its_own_populations(self) -> None:
        """The "N of the M" figures the criteria list and the join narrate.

        An exhausted backlog has no population to narrate, so the index must
        narrate none rather than restate the last list's shares against zero.
        """
        ranked = self.ranked_rows()
        zero_witness = sum(1 for _n, _key, measured, _line in ranked if measured[3] == 0)
        no_file = sum(1 for _n, _key, measured, _line in ranked if measured[0] == 0)
        flat = " ".join(self.doc.split())
        populations = re.findall(r"(\d+) of the (\d+)(?= ranked| entries| score)", flat)
        if not ranked:
            self.assertEqual([], populations, "an empty ranked list narrates no population")
            return
        for population, total in populations:
            self.assertEqual(len(ranked), int(total), "a population is stated against the wrong total")
            self.assertIn(
                int(population), (zero_witness, no_file), "a stated population is neither count"
            )
        self.assertIn(f"{zero_witness} of the {len(ranked)} score zero", flat)
        self.assertIn(f"{no_file} of the {len(ranked)} entries name no", flat)
        self.assertIn(f"{no_file} of the {len(ranked)} ranked entries reach no", flat)

    def test_the_two_largest_unranked_files_sum_as_the_join_narrates(self) -> None:
        """The share of the block the two files no ranked gap points at hold."""
        table = self.blind_spot_table()
        unranked = sorted(
            (count, name)
            for name, (count, _tier, cell) in table.items()
            if cell.startswith("none")
        )
        largest = sum(count for count, _name in unranked[-2:])
        flat = " ".join(self.doc.split())
        stated = re.search(r"together ([\d,]+) of the block's ([\d,]+) printed regions", flat)
        self.assertIsNotNone(stated, "the join no longer states the two largest files' share")
        self.assertEqual(
            (largest, sum(count for count, _tier, _cell in table.values())),
            tuple(int(value.replace(",", "")) for value in stated.groups()),
        )
        paragraph = flat[: stated.start()][-200:]
        for _count, name in unranked[-2:]:
            self.assertIn(f"`{name}`", paragraph, f"{name} is not one of the two named")

    # ------------------------------------------------------------------
    # The conjunction rows: one per declared conjunction, in the region that
    # owns the object it anchors on.
    # ------------------------------------------------------------------

    BLIND_FUNCTIONS = (
        "resolve_schema_pointer", "nested_array_element", "hoist_union_variant",
        "ref_to_class", "prop_type_ref", "path_group",
    )
    NOT_EXHAUSTED = "does not pin\nthe whole of the branch's behaviour"

    def conjunction_rows(self) -> dict[str, tuple[str, list[str]]]:
        """selector -> the one region row whose evidence cell cites it."""
        found: dict[str, tuple[str, list[str]]] = {}
        for selector in census.CONJUNCTIONS:
            citing = [
                (region, cells)
                for region, cells in self.entries.values()
                if f"`{selector}`" in cells[4]
            ]
            self.assertEqual(
                1, len(citing),
                f"{selector}: {len(citing)} region rows cite it; exactly one must",
            )
            found[selector] = citing[0]
        return found

    # The predicates read off a *branch*, which carry rows of their own exactly as
    # the conjunctions composing them do: a selector declared and never classified
    # is a measurement nobody took. The eleven node-local ones the node-local pass
    # declared, and the three cross-member readings of `discriminated_union` the
    # discriminated-union pass added. The five predicates that predate the
    # family are not here — they are about a whole document's keys or values rather
    # than about one arm of a blind function, and their rows say so instead; nor
    # are the seven `schema.$ref:` pointer-form ones, whose rows name two functions
    # apiece because the two read the same positions.
    #
    # The pointer-walk pass read five branches off `resolve_schema_pointer`'s
    # segment loop and they are **not** here either, for a different reason than
    # any of the above: what it declared for them are conjunctions, not predicates.
    # The reading of each arm on its own is a `census.MEMBER_ONLY_PREDICATES`
    # member rather than a selector, so it carries no row and this rule does not
    # reach it — see the note where the five names would otherwise sit, below.
    BRANCH_PREDICATES = {
        "schema.type:primary=array": "schemas",
        "schema.properties:non-empty": "schemas",
        "schema.oneOf:sole-member": "schemas",
        "schema.anyOf:sole-member": "schemas",
        "schema.oneOf:sole-non-null-member": "schemas",
        "schema.anyOf:sole-non-null-member": "schemas",
        "schema.enum:string-valued": "schemas",
        "schema.const:string-valued": "schemas",
        "openapi.paths:leading-literal-segment": "document-paths",
        "openapi.paths:template-before-literal-segment": "document-paths",
        "openapi.paths:all-segments-templated": "document-paths",
        "schema.oneOf:discriminated-union": "schemas",
        "schema.anyOf:discriminated-union": "schemas",
        "schema.discriminator:inheritance-union": "schemas",
        # The three the negation pass declared, two of them readings of a `type`
        # array's primary member and one an `allOf` arity.
        "schema.type:primary=object": "schemas",
        "schema.type:primary-scalar": "schemas",
        "schema.allOf:sole-member": "schemas",
        # The five `pointer-walk-reaches=` readings are deliberately absent: a
        # member of `census.MEMBER_ONLY_PREDICATES` is not a selector, so it
        # carries no row of its own. The rows for `resolve_schema_pointer`'s cases
        # 3 to 7 are the five gated conjunctions, which
        # `test_every_declared_conjunction_carries_exactly_one_classified_row`
        # holds to the same one-row rule.
    }

    def predicate_rows(self) -> dict[str, tuple[str, list[str]]]:
        """selector -> the one region row whose evidence cell cites it."""
        found: dict[str, tuple[str, list[str]]] = {}
        for selector in self.BRANCH_PREDICATES:
            citing = [
                (region, cells)
                for region, cells in self.entries.values()
                if f"`{selector}`" in cells[4]
            ]
            self.assertEqual(
                1, len(citing),
                f"{selector}: {len(citing)} region rows cite it; exactly one must",
            )
            found[selector] = citing[0]
        return found

    def test_every_branch_predicate_carries_one_row_in_the_region_that_owns_it(self) -> None:
        """A predicate read off an arm is classified where the object it anchors on lives.

        `schema.…` predicates anchor on a Schema Object and belong to `schemas`;
        the three `openapi.paths:` readings anchor on the Paths Object and belong
        to `document-paths`. Each row names the arm it was read off and the case
        number of it, so a reader lands on the branch rather than on the field.
        """
        for selector, (region, cells) in sorted(self.predicate_rows().items()):
            with self.subTest(selector=selector):
                self.assertEqual(self.BRANCH_PREDICATES[selector], region)
                self.assertIn(cells[3].strip("`"), self.CATEGORIES)
                named = [fn for fn in self.BLIND_FUNCTIONS if f"`{fn}`" in cells[4]]
                self.assertTrue(
                    named,
                    "a predicate row names the blind function whose arm it was read off",
                )
                self.assertRegex(cells[4], r"case \d+")

    def test_every_golden_branch_predicate_row_says_it_is_not_golden_exhausted(self) -> None:
        """The same caveat the conjunction rows carry, for the same reason."""
        caveat = " ".join(self.NOT_EXHAUSTED.split())
        for selector, (_region, cells) in sorted(self.predicate_rows().items()):
            if cells[3].strip("`") != "golden":
                continue
            with self.subTest(selector=selector):
                self.assertIn(caveat, " ".join(cells[4].split()))

    def test_every_branch_predicate_rows_evidence_is_the_census_own_output(self) -> None:
        """Every vendored source a predicate row names, against the real script."""
        reported: dict[str, dict[str, int]] = {s: {} for s in self.BRANCH_PREDICATES}
        payload = json.loads(run("--vendored-only", "--json").stdout)
        for row in payload["rows"]:
            if row["selector"] in reported:
                reported[row["selector"]][row["fixture"]] = row["count"]
        vendored = {source["fixture"] for source in payload["sources"]}
        for selector, (_region, cells) in sorted(self.predicate_rows().items()):
            for name, count in re.findall(r"`([a-z0-9][a-z0-9.\-_]*)` \((\d+)\)", cells[4]):
                if name not in vendored:
                    continue
                with self.subTest(selector=selector, fixture=name):
                    self.assertEqual(reported[selector].get(name, 0), int(count))

    def test_every_declared_conjunction_carries_exactly_one_classified_row(self) -> None:
        """The closed list is the row set: a selector declared and never classified
        is a measurement nobody took, and two rows for one shape are two answers."""
        rows = self.conjunction_rows()
        self.assertEqual(set(census.CONJUNCTIONS), set(rows))
        for selector, (region, cells) in sorted(rows.items()):
            with self.subTest(selector=selector):
                self.assertEqual(
                    "schemas", region,
                    "every conjunction anchors on a Schema Object, so the "
                    "`schemas` region owns its row",
                )
                self.assertIn(cells[3].strip("`"), self.CATEGORIES)

    def test_every_conjunction_row_names_the_branch_it_is_about(self) -> None:
        """What a conjunction row carries that an ordinary row does not.

        A field row is about a field; a conjunction row is about a *branch*, so it
        names the generator function and the case, which is what tells a reader it
        is a live code path rather than a shape somebody thought of.
        """
        for selector, (_region, cells) in sorted(self.conjunction_rows().items()):
            with self.subTest(selector=selector):
                named = [fn for fn in self.BLIND_FUNCTIONS if f"`{fn}`" in cells[4]]
                self.assertEqual(
                    1, len(named),
                    "a conjunction row names exactly one of the six blind functions "
                    f"of `src/ir.rs`; this one names {named}",
                )
                self.assertRegex(
                    cells[4], r"case \d+",
                    "a conjunction row names the case of that function it distinguishes",
                )

    def test_every_golden_conjunction_row_says_it_is_not_golden_exhausted(self) -> None:
        """The document's own caveat, stated where it bites hardest.

        A golden pins the bytes for the shapes its own document sends down the
        branch, not the branch's whole behaviour — and the branch is what the row
        is about, so a `golden` conjunction row that omits this reads as a stronger
        claim than the measurement supports.
        """
        caveat = " ".join(self.NOT_EXHAUSTED.split())
        for selector, (_region, cells) in sorted(self.conjunction_rows().items()):
            if cells[3].strip("`") != "golden":
                continue
            with self.subTest(selector=selector):
                self.assertIn(caveat, " ".join(cells[4].split()))

    def test_every_conjunction_rows_evidence_is_the_census_own_output(self) -> None:
        """The counts a row publishes, against the census this gate can run.

        The rows are classified off the whole 164-source walk, which needs the
        network; what is checkable offline is every vendored source a row names —
        its published count has to be that source's own, measured here by the real
        script over the real documents. A transposed digit or a source named under
        the wrong selector fails here rather than in a reader's head.
        """
        reported: dict[str, dict[str, int]] = {s: {} for s in census.CONJUNCTIONS}
        payload = json.loads(run("--vendored-only", "--json").stdout)
        for row in payload["rows"]:
            if row["selector"] in reported:
                reported[row["selector"]][row["fixture"]] = row["count"]
        vendored = {source["fixture"] for source in payload["sources"]}
        checked = 0
        for selector, (_region, cells) in sorted(self.conjunction_rows().items()):
            for name, count in re.findall(r"`([a-z0-9][a-z0-9.\-_]*)` \((\d+)\)", cells[4]):
                if name not in vendored:
                    continue
                checked += 1
                with self.subTest(selector=selector, fixture=name):
                    self.assertEqual(reported[selector].get(name, 0), int(count))
        self.assertTrue(checked, "no conjunction row names a vendored source to check")

    def test_every_conjunction_row_rests_on_a_source_carrying_a_golden(self) -> None:
        """A `golden` row names a witness whose golden really is committed."""
        fixtures_root = REPO / "tests" / "fixtures"
        alias = census.corpus_aliases(fixtures_root)
        for selector, (_region, cells) in sorted(self.conjunction_rows().items()):
            if cells[3].strip("`") != "golden":
                continue
            with self.subTest(selector=selector):
                named = re.findall(r"`([a-z0-9][a-z0-9.\-_]*)` \(\d+\)", cells[4])
                backed = [
                    name for name in named
                    if (fixtures_root / alias.get(name, name) / "expected").is_dir()
                ]
                self.assertTrue(
                    backed,
                    f"{selector}: the row is `golden` but names no source carrying "
                    f"a committed golden (named {named})",
                )

    def test_the_probe_backlog_is_every_probe_gap_and_nothing_else(self) -> None:
        """The other backlog: probe work, listed apart from the fixture work."""
        listed = set(
            re.findall(r"^\| \[`([^`]+)`\]", self.section("## The probe backlog"), re.M)
        )
        self.assertEqual(self.gaps("PROBE"), listed)
        self.assertEqual(set(), listed & {key for _n, key, _m, _l in self.ranked_rows()})
        stated = re.search(r"The other (\d+) `gap` rows", self.doc)
        self.assertIsNotNone(stated, "the probe backlog no longer states its own size")
        self.assertEqual(len(listed), int(stated.group(1)))

    def test_the_documented_witness_supply_derivation_is_the_region_files_own(self) -> None:
        """The probe backlog derives its witness-supply set; run the command it prints.

        The index deliberately publishes no count beside that command — a number
        there would be the transcription the section promises not to make — so the
        command *is* the contract, and an untested one silently returns a shorter
        list the day a settlement cell is reworded. This runs it, and holds it to
        the two things that make its answer meaningful: it agrees with the same
        derivation done here, and every key it names is really a `PROBE` gap row.
        That last clause is the one with teeth. A row keeping the marker phrase
        while moving to `FIXTURE` — which is what `dollar-anchor` did — reads as a
        probe in this list and as fixture work everywhere else, and nothing but
        this assertion would say so.

        **An empty answer is a legitimate one, and is checked rather than
        assumed.** This used to require the command to exit 0, on the reading that
        a `grep` finding nothing meant the marker had been reworded out from under
        it. Round 5 measured the last seven witness-supply rows into
        `limitations`, so the true answer is now the empty set and `grep` exits 1
        on it. What replaces the exit-status assertion is stricter, not looser:
        the command's answer must equal the derivation taken off the `settlement`
        cells here, and the two are compared whichever way they come out — so a
        marker reworded while a row still settles `PROBE` gives a non-empty
        derivation against an empty command answer and fails, exactly as before.
        """
        command = re.search(
            r"^grep -h '[^']+' docs/openapi-surface/\*\.md \| grep -oP '[^']+'$",
            self.doc,
            re.M,
        )
        self.assertIsNotNone(command, "the probe backlog no longer documents its derivation")

        marker = re.search(r"grep -h '([^']+)'", command.group(0)).group(1)
        derived = {
            key
            for key, (_region, cells) in self.entries.items()
            if re.search(marker, cells[7])
        }

        if not grep_speaks_pcre():
            self.skipTest("this grep has no PCRE support, so the command cannot run here")
        run = subprocess.run(
            ["bash", "-c", command.group(0)], cwd=REPO, capture_output=True, text=True
        )
        # A pipeline's exit status is its last command's, and `grep` exits 1 on no
        # match — the correct status for an empty backlog. Any other non-zero is a
        # broken command rather than an empty answer, and stays a red.
        self.assertIn(run.returncode, (0, 1), run.stderr)
        self.assertEqual((run.returncode == 0), bool(derived), run.stderr)
        self.assertEqual(derived, set(run.stdout.split()))
        self.assertEqual(
            set(),
            derived - self.gaps("PROBE"),
            "a row keeps the witness-supply marker but no longer settles PROBE",
        )

    def probe_kind(self, key: str, cells: list[str]) -> str:
        """Which of the two kinds this `PROBE` row's own settlement cell declares.

        The declaration is the bolded word, so a cell may say *why it is not the
        other one* — `witness-supply` grounds "rather than structural ones" — in
        prose without declaring both.
        """
        declared = [
            kind
            for kind in self.PROBE_KINDS
            if re.search(rf"\*\*{re.escape(kind)}\*\*", cells[7])
        ]
        self.assertEqual(
            1,
            len(declared),
            f"{key}: a PROBE settlement cell declares exactly one of "
            f"**structural** or **witness-supply**; this one declares {declared}",
        )
        return declared[0]

    def census_selectors_cited(self, cell: str) -> list[str]:
        """What in `cell` names a census selector: a selector span, or the word.

        The selector set is read out of the script's own grammar rather than
        transcribed, so a selector declared tomorrow is covered today. A code span
        counts only when the *whole* span is a selector — a Rust `match` pattern
        that happens to contain `scheme.scheme` is not a citation of one.
        """
        selectors, _prefixes = census.grammar()
        cited = [
            f"`{span}`"
            for span in re.findall(r"`([^`]+)`", cell)
            if span.partition("=")[0].partition(":")[0] in selectors
        ]
        return cited + re.findall(r"(?i)\b(?:the |a )?(selectors?)\b", cell)

    def region_text(self, region: str) -> str:
        return (self.REGIONS / f"{region}.md").read_text(encoding="utf-8")

    def witness_search_rows(self, region: str) -> dict[str, str]:
        """key -> the `sources searched and the exact query` cell, per region file."""
        return {
            key: row[6]
            for key, row in witness_search_table(self.region_text(region)).items()
        }

    def declared_witness_sources(self, region: str) -> dict[str, str]:
        return declared_witness_sources(self.region_text(region))

    def witness_sources_queried(self, cell: str, declared: dict[str, str]) -> dict[str, str]:
        return witness_sources_queried(cell, declared)

    def test_every_probe_row_is_one_of_two_kinds_and_cites_no_census_selector(self) -> None:
        """A `PROBE` row says which kind it is, and never settles on the census.

        A selector reporting zero is `gap` evidence — the census's own statement
        that no *registered* source declares the shape — and reading it as a
        settlement is what put twenty-five rows in this class on a 124-spec
        sample. A shape the grammar cannot express has measured nothing at all.
        """
        for key in sorted(self.gaps("PROBE")):
            _region, cells = self.entries[key]
            with self.subTest(key=key):
                self.probe_kind(key, cells)
                cited = self.census_selectors_cited(cells[7])
                # `assertFalse`, not `assertEqual([], …)`: the diff would push the
                # message that names the row below the list it is about.
                self.assertFalse(
                    cited,
                    f"{key}: its PROBE settlement cell names a census selector as "
                    f"its reason ({', '.join(cited)}); a selector reporting zero "
                    f"belongs in the `evidence` cell as `gap` evidence, and a "
                    f"selector that cannot express the shape has measured nothing "
                    f"about it",
                )

    def test_every_witness_supply_probe_names_its_sources_and_their_queries(self) -> None:
        """The issue's own acceptance criterion, as a failure rather than a memo.

        A witness-supply `PROBE` claims the world supplies no witness. The only
        thing that backs a claim that size is the search itself, so the row is
        held to carrying one: a line of its own region file's witness-search
        table, naming every source that region declares it searched, with the
        query put to each. Without this, "0 declarations across the registered
        sources" reads as the same claim and nothing says otherwise.
        """
        for key in sorted(self.gaps("PROBE")):
            region, cells = self.entries[key]
            if self.probe_kind(key, cells) != "witness-supply":
                continue
            with self.subTest(key=key):
                declared = self.declared_witness_sources(region)
                self.assertTrue(
                    declared,
                    f"{key}: settles PROBE on witness-supply grounds, but "
                    f"{region}.md's `{self.WITNESS_SEARCH}` section declares no "
                    f"sources — list them as bulleted bold labels above its table",
                )
                searched = self.witness_search_rows(region)
                # Not `assertIn`: the container is every witness-search cell in the
                # region, and printing it buries the message that names the row.
                self.assertTrue(
                    key in searched,
                    f"{key}: settles PROBE on witness-supply grounds with no row "
                    f"in {region}.md's `{self.WITNESS_SEARCH}` table",
                )
                queried = self.witness_sources_queried(searched[key], declared)
                missing = sorted(declared[name] for name in set(declared) - set(queried))
                self.assertFalse(
                    missing,
                    f"{key}: its witness-search row omits {missing}, which "
                    f"{region}.md declares its search put to every row",
                )
                for name, segment in sorted(queried.items()):
                    self.assertTrue(
                        "`" in segment or "→" in segment,
                        f"{key}: its witness-search row names {declared[name]} with "
                        f"no query against it — a source is named with the exact "
                        f"query put to it and what that returned",
                    )

    def test_the_index_states_one_settlement_rule_and_names_what_it_amended(self) -> None:
        """One rule, not two: the amendment and the sentence it replaced, in one place.

        The rule it replaced is quoted rather than paraphrased, because a reader
        arriving at a `FIXTURE` row that a blocked witness put there needs to know
        the old reading is gone. The quote is asserted verbatim so a reworded
        amendment cannot leave the old rule standing somewhere unquoted.
        """
        rule = self.section("#### The settlement rule, as amended", "\n#### ")
        flat = " ".join(rule.split())
        self.assertIn(
            "leaves this list the day any witness turns up, blocked or not, and "
            "it leaves as a `FIXTURE` rather than as a measured probe",
            flat,
            "the amended rule does not quote the rule it replaced",
        )
        for outcome in ("witness-found", *BLOCKED_OUTCOMES, "none-found", SEARCH_INCOMPLETE):
            self.assertIn(f"**`{outcome}`**", flat, f"the rule does not define `{outcome}`")
        for demanded in (
            AMENDED_ROUTE,               # how a row says it took the route
            "`blocker:`",                # and where it names its blocker
            "still beats",               # the precedence that does not move
            "no byte-comparison evidence",
        ):
            self.assertIn(demanded, flat, f"the rule no longer states {demanded!r}")

    def test_the_new_outcome_is_defined_once_and_only_deferred_to(self) -> None:
        """`search-incomplete` is the index's to define; a region file points at it.

        Four outcomes were glossed in three region files at once, which is how a
        vocabulary drifts. The fifth is defined where the settlement rule that
        gives it meaning is, and a region file naming it links there rather than
        re-glossing it.
        """
        self.assertIn(
            SEARCH_INCOMPLETE, self.section("#### The settlement rule, as amended", "\n#### ")
        )
        naming = [
            path
            for path in sorted(self.REGIONS.glob("*.md"))
            if SEARCH_INCOMPLETE in path.read_text(encoding="utf-8")
        ]
        self.assertTrue(naming, "no region file names the outcome its own tables may read")
        for path in naming:
            with self.subTest(region=path.stem):
                self.assertIn(
                    "openapi-surface-coverage.md#the-settlement-rule-as-amended",
                    path.read_text(encoding="utf-8"),
                    "a region file names the outcome without deferring to its definition",
                )

    def test_no_recorded_search_calls_an_unanswered_source_evidence_of_absence(self) -> None:
        """Every recorded search in the tree, held to the outcome its own record supports."""
        for path in sorted(self.REGIONS.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            declared = declared_witness_sources(text)
            if not declared:
                continue
            for key, row in sorted(witness_search_table(text).items()):
                with self.subTest(region=path.stem, key=key):
                    self.assertEqual(
                        [], unread_source_failures(key, path.stem, row, declared)
                    )

    def test_every_blocked_witness_probe_row_meets_the_amended_settlement_rule(self) -> None:
        """Route 2, read over every region row in the tree that claims it.

        Twenty-one rows claim it today, across four of the six region files, so
        this reads the real documents end to end: every one of those rows is held
        to the recorded search, the blocker form and the ledger verdict at the
        gate rather than at review, over the real six region files and the real
        ledger. `AmendedSettlementRuleTests` below stays, because a fixture is
        the only way to watch the reconciliation *refuse* a row.
        """
        ledger = (REPO / "docs" / "fern-limitations.md").read_text(encoding="utf-8")
        for key, (region, cells) in sorted(self.entries.items()):
            if AMENDED_ROUTE not in cells[4]:
                continue
            with self.subTest(key=key):
                self.assertEqual(
                    "limitations",
                    cells[3].strip("`"),
                    f"{key}: a row settled by the amended route is `limitations`",
                )
                self.assertEqual(
                    [],
                    blocked_witness_probe_failures(
                        key, region, cells, self.region_text(region), ledger
                    ),
                )

    def test_every_open_search_probe_row_meets_the_amended_settlement_rule(self) -> None:
        """Route 3, read over every region row in the tree that claims it.

        Three rows claim it today — `parameters`' `header-allow-reserved` and
        `parameter-style-form-cookie-scalar`, and `schemas`' `dependent-schemas` —
        so this reads the real documents end to end, holding each to its
        outstanding source, its convertibility statement and its ledger verdict.
        `OpenSearchProbeRuleTests` below stays for the refusals, which no row in
        the tree exhibits.
        """
        ledger = (REPO / "docs" / "fern-limitations.md").read_text(encoding="utf-8")
        for key, (region, cells) in sorted(self.entries.items()):
            if OPEN_SEARCH_ROUTE not in cells[4]:
                continue
            with self.subTest(key=key):
                self.assertEqual(
                    "limitations",
                    cells[3].strip("`"),
                    f"{key}: a row settled by route 3 is `limitations`",
                )
                self.assertEqual(
                    [],
                    open_search_probe_failures(
                        key, region, cells, self.region_text(region), ledger
                    ),
                )

    def test_the_rule_states_route_three_and_what_separates_it_from_the_others(self) -> None:
        """The third settlement route, stated where the other two are.

        A route the gate enforces and the index does not state is a rule nobody
        can follow, so the words a conforming row carries are asserted here: the
        route's own marker, where it names its outstanding source, and the
        convertibility the route rests on.
        """
        flat = " ".join(self.section("#### The settlement rule, as amended", "\n#### ").split())
        for demanded in (
            f"**`{OPEN_SEARCH_ROUTE}`**",  # how a row says it took the route
            "`outstanding:`",              # and where it names its outstanding source
            "stays convertible",
            "`witness-found`, since route 1 is what settles that",
            "records no probe and no verdict",
        ):
            self.assertIn(demanded, flat, f"the rule no longer states {demanded!r}")

    def test_the_rule_records_why_the_largest_unread_source_is_unread(self) -> None:
        """A source left unread on a judgement, with the judgement's own grounds.

        The 414,968-spec SwaggerHub family is the biggest thing neither settled
        row's search read, and this repository's own record says its version
        references are editable in place. What the rule has to carry is why that
        makes the read unable to move either the row's category or the instrument
        that settles it — otherwise a later reader sees a source somebody forgot.
        """
        flat = " ".join(self.section("#### The settlement rule, as amended", "\n#### ").split())
        self.assertIn("414,968", flat, "the rule no longer names the unread family's size")
        self.assertIn("editable in place", flat, "the rule no longer says why it is unregistrable")
        for record in ("openapi-surface/security.md", "openapi-surface/schemas.md"):
            self.assertIn(record, flat, f"the rule does not cite {record}'s own record")
        self.assertIn(
            "neither the row's category nor the instrument that settles it",
            flat,
            "the rule no longer says what reading the family could not change",
        )

    def test_the_probe_backlog_splits_by_the_kind_each_region_row_declares(self) -> None:
        """The index's two named parts are the region files' own settlement cells."""
        kinds: dict[str, set[str]] = {kind: set() for kind in self.PROBE_KINDS}
        for key in sorted(self.gaps("PROBE")):
            kinds[self.probe_kind(key, self.entries[key][1])].add(key)
        for kind, expected in kinds.items():
            heading = f"### {kind[0].upper()}{kind[1:]} probes"
            with self.subTest(kind=kind):
                body = self.section(heading, "\n### " if kind == "structural" else None)
                listed = set(re.findall(r"^\| \[`([^`]+)`\]", body, re.M))
                self.assertEqual(
                    expected, listed, f"{heading} is not the rows whose cells say {kind}"
                )
                stated = re.match(r"\s*\*\*(\d+) rows?\.\*\*", body)
                self.assertIsNotNone(stated, f"{heading} no longer states its own size")
                self.assertEqual(len(expected), int(stated.group(1)))

    def test_the_stated_registered_and_golden_source_counts_are_measured(self) -> None:
        """The registered and golden-bearing source counts, measured rather than
        transcribed off whichever walk the section was last written on."""
        sources = census.registered_sources(FIXTURES, REPO / ".local" / "corpus", False)
        aliases = census.corpus_aliases(FIXTURES)
        golden = sum(
            1
            for source in sources
            if (FIXTURES / aliases.get(source.fixture, source.fixture) / "expected").is_dir()
        )
        stated = re.search(
            r"It reads \*\*(\d+)\*\* registered sources, of which\n\s*\*\*(\d+)\*\* carry a committed golden",
            self.doc,
        )
        self.assertIsNotNone(stated, "the section no longer states the source counts")
        self.assertEqual(
            (len(sources), golden), (int(stated.group(1)), int(stated.group(2)))
        )


class RegionFixture:
    """A real region file and a real ledger on disk, read back as the gate reads them.

    The skeleton all six region files carry: a witness-search preamble of bulleted
    bold sources and the seven-column table under it, and an entry row in the
    eight-column shape. Both settlement-rule suites below write it to a real
    temporary tree and parse it back with the parsers the gate itself uses, so
    what they exercise is the reconciliation over region-file content rather than
    a hand-built cell list.
    """

    REGION = """\
# OpenAPI surface coverage — a sample region

## Scope

| `sample` | `openapi-surface/sample.md` | one sample object |

## Entries

| key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |
|---|---|---|---|---|---|---|---|
{entry}

## Method notes

### Witness search (issue #188)

`outcome` is one of the five words the index's settlement rule defines.

- **APIs.guru / `openapi-directory`** — a `--depth 1` clone of the repository,
  grepped for the JSON and the YAML spelling of the keyword.
- **GitHub code search** — `gh search code '"<keyword>" filename:openapi.yaml'`
  and the same query over `openapi.json`.

| key | outcome | witness | immutable ref | license | fern check | sources searched and the exact query used against each |
|---|---|---|---|---|---|---|
{search}
"""

    def written(self, entry: str, search: str, ledger: str) -> tuple[str, list[str], str]:
        """`entry`/`search`/`ledger` on the real filesystem, read back as the gate reads them."""
        directory = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, directory)
        root = Path(directory)
        (root / "openapi-surface").mkdir()
        region = root / "openapi-surface" / "sample.md"
        region.write_text(self.REGION.format(entry=entry, search=search), encoding="utf-8")
        (root / "fern-limitations.md").write_text(ledger, encoding="utf-8")
        text = region.read_text(encoding="utf-8")
        rows = RankedBacklogTests.region_rows(text)
        self.assertEqual(1, len(rows), "the sample region file no longer parses as one entry row")
        return text, rows[0], (root / "fern-limitations.md").read_text(encoding="utf-8")


class AmendedSettlementRuleTests(RegionFixture, unittest.TestCase):
    """The amended settlement rule, driven over real region-file content.

    `RankedBacklogTests` reads every row in the tree that takes this route, so the
    conforming half is observed over the real documents. What no real row
    exhibits is the *refusing* half — a row that drops a declared source, names a
    blocker without its payload, or carries no ledger verdict — and a
    reconciliation nobody has watched refuse anything would pass just as green if
    it read nothing at all. So these write real region-file content — the skeleton all six carry, a
    witness-search preamble of bulleted bold sources and the seven-column table
    under it, and an entry row in the eight-column shape — to a real temporary
    tree, parse it back off disk with the parsers the gate itself uses, and run the
    real reconciliation over it: once on a row that conforms to the rule, and once
    per way of failing it.
    """

    ENTRY = (
        "| `sample-shape` | both | Schema Object.sample | limitations | ledger "
        "`sample-shape`, verdict `discards`; settled as a **blocked-witness probe** "
        "on the `witness-blocked` outcome the search below records. {blocker} |  |  |  |"
    )
    BLOCKER = (
        "**blocker:** licence — the one witness is published under `NOASSERTION`, "
        "outside the corpus's redistribution set; a re-licence makes it registrable "
        "and promotes this row to `golden`"
    )
    SEARCH = (
        "| `sample-shape` | {outcome} | Sample API, `sample-org/sample-api` "
        "`openapi.yaml` — **1** declaration counted in the fetched bytes | "
        "`https://raw.githubusercontent.com/sample-org/sample-api/"
        "0f1e2d3c4b5a69788796a5b4c3d2e1f00f1e2d3c/openapi.yaml` | proprietary "
        "(`NOASSERTION`) | clean, exit 0 | {sources} |"
    )
    BOTH_SOURCES = (
        "**APIs.guru** `grep -rlF '\"x-sample\"' APIs` → 0 hits. "
        "**GitHub code search** `gh search code '\"x-sample\" filename:openapi.yaml'` "
        "→ 3 hits, every one a synthetic fixture."
    )
    ONE_SOURCE = "**APIs.guru** `grep -rlF '\"x-sample\"' APIs` → 0 hits."
    LEDGER = (
        "| key | witnesses | goldens | verdict | finding |\n"
        "|---|---|---|---|---|\n"
        "| `sample-shape` | 1 | 0 | discards | the probe records that Fern accepts "
        "the shape and emits nothing derived from it |\n"
    )

    def reconcile(
        self,
        *,
        blocker: str | None = None,
        outcome: str = "witness-blocked",
        sources: str | None = None,
        search: str | None = None,
        ledger: str | None = None,
    ) -> list[str]:
        entry = self.ENTRY.format(blocker=self.BLOCKER if blocker is None else blocker)
        if search is None:
            search = self.SEARCH.format(
                outcome=outcome, sources=self.BOTH_SOURCES if sources is None else sources
            )
        text, cells, read_ledger = self.written(
            entry, search, self.LEDGER if ledger is None else ledger
        )
        return blocked_witness_probe_failures("sample-shape", "sample", cells, text, read_ledger)

    def only_failure(self, failures: list[str]) -> str:
        self.assertEqual(1, len(failures), failures)
        self.assertTrue(failures[0].startswith("sample-shape: "), failures[0])
        return failures[0]

    def test_a_row_that_meets_the_rule_is_accepted(self) -> None:
        """The route the amendment opens, taken correctly: a blocked witness, a probe."""
        self.assertEqual([], self.reconcile())

    def test_a_row_with_no_recorded_search_is_refused(self) -> None:
        """The recorded exhaustive search is the gate, and this row records none."""
        self.assertIn(
            "no line in sample.md's `### Witness search (issue #188)` table",
            self.only_failure(self.reconcile(search="")),
        )

    def test_a_row_whose_search_omits_a_declared_source_is_refused(self) -> None:
        """Every source the region's own preamble names, or the search is not exhaustive."""
        self.assertIn(
            "omits ['GitHub code search']",
            self.only_failure(self.reconcile(sources=self.ONE_SOURCE)),
        )

    NO_QUERY_SOURCES = (
        "**APIs.guru** `grep -rlF '\"x-sample\"' APIs` → 0 hits. "
        "**GitHub code search** — searched, and nothing it returned was a witness."
    )
    NO_RESULT_SOURCES = (
        "**APIs.guru** `grep -rlF '\"x-sample\"' APIs` → 0 hits. "
        "**GitHub code search** `gh search code '\"x-sample\" filename:openapi.yaml'`."
    )

    def test_a_row_naming_every_source_but_querying_one_of_them_is_refused(self) -> None:
        """Naming a source is not asking it; the query has to be on the record."""
        self.assertIn(
            "names GitHub code search with no query in a code span",
            self.only_failure(self.reconcile(sources=self.NO_QUERY_SOURCES)),
        )

    def test_a_row_recording_a_query_and_not_what_it_returned_is_refused(self) -> None:
        """A question with no answer written down settles nothing about the world."""
        self.assertIn(
            "names GitHub code search with a query and no result after it",
            self.only_failure(self.reconcile(sources=self.NO_RESULT_SOURCES)),
        )

    def test_a_row_whose_search_found_a_usable_witness_is_refused(self) -> None:
        """`witness-found` is fixture work: the corpus can register that document."""
        self.assertIn(
            "its recorded search returned `witness-found`",
            self.only_failure(self.reconcile(outcome="witness-found")),
        )

    def test_a_row_whose_search_found_nothing_is_refused(self) -> None:
        """`none-found` is the witness-supply probe the unamended rule already covers."""
        self.assertIn(
            "its recorded search returned `none-found`",
            self.only_failure(self.reconcile(outcome="none-found")),
        )

    def test_a_row_whose_search_did_not_finish_is_refused(self) -> None:
        """`search-incomplete` settles nothing, so it licenses nothing either."""
        self.assertIn(
            "its recorded search returned `search-incomplete`",
            self.only_failure(self.reconcile(outcome=SEARCH_INCOMPLETE)),
        )

    def test_a_row_naming_no_blocker_is_refused(self) -> None:
        """A convertible row names what would have to change; this one names nothing."""
        self.assertIn(
            "names no blocker",
            self.only_failure(self.reconcile(blocker="The witness cannot be registered.")),
        )

    # Each of these carries its form's label and everything but the payload that
    # makes the form act on anything. The last three are the deceptive ones: they
    # quote a code span, which a check reading the label plus "some code span"
    # accepts, and none of them names a licence or a diagnostic.
    VAGUE_BLOCKERS = (
        ("no licence at all", "**blocker:** the licence is wrong"),
        ("no URL", "**blocker:** mutable ref — the upstream moves"),
        ("no exit status and no diagnostic", "**blocker:** fern refusal — Fern says no"),
        (
            "a licence blocker quoting a command instead of a licence",
            "**blocker:** licence — the corpus cannot redistribute it, as `fern check` shows",
        ),
        (
            "a licence blocker quoting a word that is no licence",
            "**blocker:** licence — this row is blocked; see `golden`",
        ),
        (
            "a mutable ref naming the URL and not what changes beneath it",
            "**blocker:** mutable ref — served at `https://example.test/openapi.yaml`",
        ),
        (
            "a Fern refusal whose only code span is the invocation",
            "**blocker:** fern refusal — `fern check` exits **1**",
        ),
        (
            "a Fern refusal quoting the diagnostic and no exit status",
            "**blocker:** fern refusal — `Service requires auth, but no auth is defined.`",
        ),
        (
            "a Fern refusal whose only code span is the exit status itself",
            "**blocker:** fern refusal — exits `1`",
        ),
        (
            "a Fern refusal quoting the generator version rather than a diagnostic",
            "**blocker:** fern refusal — `fern check` exits **1** at `5.20.0`",
        ),
        (
            "a Fern refusal quoting the pinned ref rather than a diagnostic",
            "**blocker:** fern refusal — `fern check` exits **1** at commit "
            "`8d9ff98f7d3ddd3e74340bcfb322c12df2ed189b`",
        ),
        (
            "a Fern refusal quoting the spec URL rather than a diagnostic",
            "**blocker:** fern refusal — `fern check` exits **1** on "
            "`https://example.test/openapi.yaml`",
        ),
        (
            "a Fern refusal whose longer invocation is its only prose span",
            "**blocker:** fern refusal — exits **1** running "
            "`fern generate --group python-sdk --log-level debug`",
        ),
        (
            "a mutable ref restating the label instead of naming the change",
            "**blocker:** mutable ref — `https://example.test/openapi.yaml`; "
            "this is a mutable reference",
        ),
        (
            "a mutable ref whose words after the URL describe the document",
            "**blocker:** mutable ref — `https://example.test/openapi.yaml`, "
            "an OpenAPI 3.1 document the publisher serves",
        ),
    )

    def test_a_blocker_too_vague_to_act_on_is_refused(self) -> None:
        """The label alone is not a blocker: each form names the thing that would change."""
        for missing, vague in self.VAGUE_BLOCKERS:
            with self.subTest(missing=missing):
                self.assertIn("names no blocker", self.only_failure(self.reconcile(blocker=vague)))

    def test_each_of_the_three_blocker_forms_is_accepted(self) -> None:
        """And the three complete ones are, so the refusal above is about content."""
        for good in (
            "**blocker:** licence — the witness declares `none declared`",
            "**blocker:** licence — the witness carries `AGPL-3.0`",
            "**blocker:** mutable ref — served only at "
            "`https://example.test/openapi.yaml`, which the publisher overwrites in place",
            "**blocker:** mutable ref — `https://example.test/openapi.yaml`, whose "
            "body changes whenever the publisher redeploys",
            "**blocker:** fern refusal — `fern check` exits **1** with "
            "`Service requires auth, but no auth is defined.`",
        ):
            with self.subTest(blocker=good):
                self.assertEqual([], self.reconcile(blocker=good))

    def test_a_row_with_no_probe_recorded_in_the_ledger_is_refused(self) -> None:
        """The probe is the measurement that settles it; without one nothing does."""
        self.assertIn(
            "records no probe and no verdict",
            self.only_failure(self.reconcile(ledger="| key | witnesses |\n|---|---|\n")),
        )

    def unread(self, outcome: str, sources: str) -> list[str]:
        """The other refusal: a recorded search read against the outcome it claims."""
        text, _cells, _ledger = self.written(
            self.ENTRY.format(blocker=self.BLOCKER),
            self.SEARCH.format(outcome=outcome, sources=sources),
            self.LEDGER,
        )
        return unread_source_failures(
            "sample-shape",
            "sample",
            witness_search_table(text)["sample-shape"],
            declared_witness_sources(text),
        )

    UNANSWERED_SOURCES = (
        "**APIs.guru** `grep -rlF '\"x-sample\"' APIs` → 0 hits. "
        "**GitHub code search** `gh search code '\"x-sample\" filename:openapi.yaml'` "
        "→ **unanswered**: the endpoint returned HTTP 502 on every attempt."
    )

    def test_a_none_found_row_whose_search_a_source_did_not_answer_is_refused(self) -> None:
        """An unread source is not evidence of absence, however the row spells it."""
        self.assertIn(
            "records ['GitHub code search'] as `unanswered` while the row reads "
            "`none-found`",
            self.only_failure(self.unread("none-found", self.UNANSWERED_SOURCES)),
        )

    def test_search_incomplete_is_the_spelling_an_unanswered_source_takes(self) -> None:
        """The outcome the amendment adds, doing the job the refusal above leaves open."""
        self.assertEqual([], self.unread(SEARCH_INCOMPLETE, self.UNANSWERED_SOURCES))

    def test_a_none_found_row_every_source_answered_is_accepted(self) -> None:
        """And a search that really did ask the world still reads `none-found`."""
        self.assertEqual([], self.unread("none-found", self.BOTH_SOURCES))


class OpenSearchProbeRuleTests(RegionFixture, unittest.TestCase):
    """Route 3, driven over real region-file content the same way route 2 is.

    No row in the tree takes route 3 today either, so the reconciliation reading
    the real six region files observes nothing about it. These write real
    region-file content to a real temporary tree, parse it back off disk with the
    parsers the gate itself uses, and run the real reconciliation over it: once on
    a row that conforms to the route, and once per way of failing it.
    """

    ENTRY = (
        "| `sample-shape` | both | Schema Object.sample | limitations | ledger "
        "`sample-shape`, verdict `discards`; settled as an **open-search probe** on "
        "the `{outcome}` outcome the search below records. {outstanding} "
        "{convertible} |  |  |  |"
    )
    OUTSTANDING = (
        "**outstanding:** GitHub code search — the secondary limiter refused every "
        "attempt while `gh api rate_limit` still reported budget, so it answered "
        "nothing."
    )
    CONVERTIBLE = (
        "The row stays convertible: a registrable witness promotes it to `golden` "
        "under the classification precedence."
    )
    SEARCH = (
        "| `sample-shape` | {outcome} | none reached — every source that answered "
        "declares it **0** times | — | — | — | {sources} |"
    )
    OUTSTANDING_SOURCES = (
        "**APIs.guru** `grep -rlF '\"x-sample\"' APIs` → 0 hits. "
        "**GitHub code search** `gh search code '\"x-sample\" filename:openapi.yaml'` "
        "→ **unanswered**: refused with `HTTP 403: API rate limit exceeded for user "
        "ID 19440155` on every attempt."
    )
    ANSWERED_SOURCES = (
        "**APIs.guru** `grep -rlF '\"x-sample\"' APIs` → 0 hits. "
        "**GitHub code search** `gh search code '\"x-sample\" filename:openapi.yaml'` "
        "→ 3 hits, every one a synthetic fixture."
    )
    LEDGER = (
        "| key | witnesses | goldens | verdict | finding |\n"
        "|---|---|---|---|---|\n"
        "| `sample-shape` | 0 | 0 | discards | the probe records that Fern accepts "
        "the shape and emits nothing derived from it |\n"
    )

    def reconcile(
        self,
        *,
        outcome: str = SEARCH_INCOMPLETE,
        outstanding: str | None = None,
        convertible: str | None = None,
        sources: str | None = None,
        search: str | None = None,
        ledger: str | None = None,
    ) -> list[str]:
        entry = self.ENTRY.format(
            outcome=outcome,
            outstanding=self.OUTSTANDING if outstanding is None else outstanding,
            convertible=self.CONVERTIBLE if convertible is None else convertible,
        )
        if search is None:
            search = self.SEARCH.format(
                outcome=outcome,
                sources=self.OUTSTANDING_SOURCES if sources is None else sources,
            )
        text, cells, read_ledger = self.written(
            entry, search, self.LEDGER if ledger is None else ledger
        )
        return open_search_probe_failures("sample-shape", "sample", cells, text, read_ledger)

    def only_failure(self, failures: list[str]) -> str:
        self.assertEqual(1, len(failures), failures)
        self.assertTrue(failures[0].startswith("sample-shape: "), failures[0])
        return failures[0]

    def test_a_row_that_meets_the_route_is_accepted(self) -> None:
        """The route the amendment opens, taken correctly: an unread source, a probe."""
        self.assertEqual([], self.reconcile())

    def test_a_row_with_no_recorded_search_is_refused(self) -> None:
        """The outstanding source lives on the record, and this row records none."""
        self.assertIn(
            "no line in sample.md's `### Witness search (issue #188)` table",
            self.only_failure(self.reconcile(search="")),
        )

    def test_a_row_whose_search_found_a_usable_witness_is_refused(self) -> None:
        """`witness-found` is route 1's: the corpus can register that document."""
        self.assertIn(
            "its recorded search returned `witness-found`",
            self.only_failure(self.reconcile(outcome="witness-found")),
        )

    def test_a_row_whose_evidence_names_no_outstanding_source_is_refused(self) -> None:
        """The source that did not answer is what licenses the route, so it is named."""
        self.assertIn(
            "names no outstanding source after `outstanding:`",
            self.only_failure(
                self.reconcile(outstanding="The search left a source outstanding.")
            ),
        )

    # Each of these carries the marker and everything but a source the record
    # really marks `unanswered`, said with what it did instead of answering. The
    # third and fourth are the deceptive ones: they name a source, which a check
    # reading the label plus "some name" accepts, and neither names one this
    # region's own search left outstanding.
    VAGUE_OUTSTANDING = (
        ("no marker at all", "GitHub code search was refused by the secondary limiter."),
        ("a marker and no source", "**outstanding:** two of the three queries."),
        (
            "a source the record shows answered",
            "**outstanding:** APIs.guru — the clone was refused.",
        ),
        (
            "a source that is not one this region declares",
            "**outstanding:** SwaggerHub public registry — it exposes no body search.",
        ),
        (
            "the outstanding source with no account of what it did",
            "**outstanding:** GitHub code search.",
        ),
    )

    def test_an_outstanding_source_too_vague_to_act_on_is_refused(self) -> None:
        """The marker alone is not a source: the cell names one and what it did."""
        for missing, vague in self.VAGUE_OUTSTANDING:
            with self.subTest(missing=missing):
                self.assertIn(
                    "names no outstanding source after `outstanding:`",
                    self.only_failure(self.reconcile(outstanding=vague)),
                )

    def test_each_way_of_naming_what_the_source_did_instead_is_accepted(self) -> None:
        """And the complete ones are, so the refusal above is about content."""
        for good in (
            "**outstanding:** GitHub code search, which the secondary limiter refused.",
            "**outstanding:** GitHub code search — the endpoint was unreachable on "
            "every attempt.",
            "**outstanding:** GitHub code search — its index returned an error "
            "rather than a result.",
            "**outstanding:** GitHub code search — the 414,968 bodies behind it went "
            "unread, since it exposes no body search.",
        ):
            with self.subTest(outstanding=good):
                self.assertEqual([], self.reconcile(outstanding=good))

    def test_a_row_whose_search_marks_no_source_unanswered_is_refused(self) -> None:
        """A search every source answered settles on what it found, not on a probe."""
        self.assertIn(
            "marks no required source `unanswered`",
            self.only_failure(self.reconcile(sources=self.ANSWERED_SOURCES)),
        )

    def test_a_row_that_does_not_say_it_stays_convertible_is_refused(self) -> None:
        """A probe settles what Fern does; it must not read as closing the row."""
        self.assertIn(
            "does not say the row stays convertible to `golden`",
            self.only_failure(
                self.reconcile(convertible="The probe is the settlement available.")
            ),
        )

    def test_a_row_promised_convertible_with_no_destination_is_refused(self) -> None:
        """`convertible` on its own names no category to convert to."""
        self.assertIn(
            "does not say the row stays convertible to `golden`",
            self.only_failure(self.reconcile(convertible="The row stays convertible.")),
        )

    def test_a_row_with_no_probe_recorded_in_the_ledger_is_refused(self) -> None:
        """The probe is the measurement that settles it; without one nothing does."""
        self.assertIn(
            "records no probe and no verdict",
            self.only_failure(self.reconcile(ledger="| key | witnesses |\n|---|---|\n")),
        )



DOCUMENT = """openapi: 3.0.3
info: {{title: {name}, version: "1"}}
paths:
{paths}
"""

OPERATION = """    {method}:
{fields}
      responses:
        "200":
          description: ok"""


def document(name: str, routes: list[tuple[str, list[str]]]) -> str:
    """One source document declaring `routes`: a path key and its operations' fields."""
    paths = []
    for path, operations in routes:
        paths.append(f"  {json.dumps(path)}:")
        for index, fields in enumerate(operations):
            method = ("get", "post", "put", "delete")[index]
            body = "\n".join(f"      {line}" for line in fields.splitlines())
            paths.append(OPERATION.format(method=method, fields=body))
    return DOCUMENT.format(name=name, paths="\n".join(paths))


COMPONENTS_DOCUMENT = """openapi: 3.0.3
info: {{title: {name}, version: "1"}}
paths:
  /widgets:
    get:
      responses:
        "200":
          description: ok
components:
  schemas:
{schemas}
"""


def component_document(name: str, schema_names: list[str]) -> str:
    """One source document whose `components.schemas` declares `schema_names`."""
    schemas = "\n".join(
        f"    {json.dumps(key)}: {{type: object}}" for key in schema_names
    )
    return COMPONENTS_DOCUMENT.format(name=name, schemas=schemas)


class PredicateSelectorTests(unittest.TestCase):
    """The third kind of selector: a shape the field selector cannot express.

    `operation.tags` counts the field and not its members, `operation.operationId`
    records declarations and not values, and a Paths Object key — like a
    `components.schemas` key — is a *name* the grammar excludes, so nothing about
    its own shape can be read off a field selector. Six real shapes were invisible
    to the instrument that is supposed to say whether the corpus has ever seen
    them. These drive the real script over real documents on the real filesystem,
    once for a document that declares each shape and once for one that does not.

    The node-local members the predicate family gained later are discriminated in
    `NodeLocalSelectorDiscriminationTests`, which asserts a near miss for each one
    rather than an absence for all of them; what stays here is the refusal, the
    acceptance and the absent-report every predicate has to answer.
    """

    def census(self, sources: dict[str, str], *selectors: str) -> subprocess.CompletedProcess:
        """Run the real script over a fixtures root holding `sources`."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, body in sources.items():
                write_fixture(root, name, body)
            arguments = ["--vendored-only", "--fixtures-root", str(root)]
            for selector in selectors:
                arguments += ["--selector", selector]
            completed = run(*arguments)
        self.assertEqual(0, completed.returncode, completed.stderr)
        return completed

    def counts(self, sources: dict[str, str], selector: str) -> dict[str, int]:
        """The reported count per source for one selector; absent sources are 0."""
        completed = self.census(sources, selector)
        return {fixture: count for (_selector, fixture), count in rows(completed).items()}

    def test_a_multi_tag_operation_is_counted_once_per_operation(self) -> None:
        """`operation.tags:multiple`: the array's members, which the field cannot show."""
        sources = {
            "two-tagged": document("two-tagged", [
                ("/widgets", ["tags: [alpha, beta]", "tags: [alpha, beta, gamma]"]),
                ("/gadgets", ["tags: [alpha]"]),
            ]),
            "single-tagged": document("single-tagged", [
                ("/widgets", ["tags: [alpha]", "tags: []"]),
            ]),
        }
        self.assertEqual({"two-tagged": 2}, self.counts(sources, "operation.tags:multiple"))
        # The field selector still counts every declaration, multiple or not: the
        # predicate adds a reading of `tags`, it does not replace one.
        self.assertEqual(
            {"two-tagged": 3, "single-tagged": 2},
            self.counts(sources, "operation.tags"),
        )

    def test_a_duplicated_operation_id_counts_every_operation_that_writes_it(self) -> None:
        """`operation.operationId:duplicate`: two values compared, not two declarations."""
        sources = {
            "repeated-id": document("repeated-id", [
                ("/widgets", ["operationId: listWidgets", "operationId: listWidgets"]),
                ("/gadgets", ["operationId: listGadgets"]),
            ]),
            "thrice-repeated-id": document("thrice-repeated-id", [
                ("/widgets", ["operationId: one", "operationId: one", "operationId: one"]),
            ]),
            "distinct-ids": document("distinct-ids", [
                ("/widgets", ["operationId: listWidgets", "operationId: createWidget"]),
            ]),
        }
        self.assertEqual(
            {"repeated-id": 2, "thrice-repeated-id": 3},
            self.counts(sources, "operation.operationId:duplicate"),
        )

    def test_a_link_objects_operation_id_is_not_an_operations(self) -> None:
        """The object-model rule holds for the predicate too.

        `apideck.com-crm` writes `"operationId": "usersOne"` seven times and
        declares no duplicate: six of the seven are Link Objects naming the
        operation they follow. A text match over that document reports six
        duplicates that no Operation Object declares.
        """
        source = """\
            openapi: 3.0.3
            info: {title: linked, version: "1"}
            paths:
              /widgets:
                get:
                  operationId: listWidgets
                  responses:
                    "200":
                      description: ok
                      links:
                        next:
                          operationId: listWidgets
            """
        counted = self.counts({"linked": source}, "operation.operationId:duplicate")
        self.assertEqual({}, counted)
        self.assertEqual({"linked": 1}, self.counts({"linked": source}, "link.operationId"))

    def test_a_normalized_path_collision_counts_every_colliding_key(self) -> None:
        """`openapi.paths:normalized-collision`: the map keys the grammar excludes."""
        sources = {
            "colliding-paths": document("colliding-paths", [
                ("/users/{userId}", ["operationId: a"]),
                ("/users/{user_id}", ["operationId: b"]),
                ("/gadgets", ["operationId: c"]),
            ]),
            "three-colliding-paths": document("three-colliding-paths", [
                ("/z/{itemId}", ["operationId: a"]),
                ("/z/{item_id}", ["operationId: b"]),
                ("/z/{itemID}", ["operationId: c"]),
            ]),
            "distinct-paths": document("distinct-paths", [
                ("/users/{userId}", ["operationId: a"]),
                ("/users/{ownerId}", ["operationId: b"]),
            ]),
        }
        self.assertEqual(
            {"colliding-paths": 2, "three-colliding-paths": 3},
            self.counts(sources, "openapi.paths:normalized-collision"),
        )

    # Templates spanning what crozier's normalization distinguishes: the variable
    # name alone, where the variable sits, how many segments there are, literals
    # mixed with variables, and every case `naming::field_name` treats specially —
    # camel and acronym boundaries, a reserved name, a digit-leading name, a
    # digit-bearing word joining its neighbour, a digit-adjacent underscore
    # collapsing, and a non-identifier character folding to a boundary. The
    # expectation on each line is what crozier's own transform implies, not what
    # this script happens to compute: `NamingMirrorTests` below pins the transform
    # against `src/naming.rs`'s own expectations.
    NORMALIZATION_CASES: tuple[tuple[str, list[str], int], ...] = (
        ("camel-and-snake", ["/users/{userId}", "/users/{user_id}"], 2),
        ("acronym-boundary", ["/users/{userID}", "/users/{user_id}"], 2),
        ("distinct-variable-names", ["/users/{userId}", "/users/{ownerId}"], 0),
        ("variable-position", ["/{id}/users", "/users/{id}"], 0),
        ("segment-count", ["/users/{id}", "/users/{id}/roles"], 0),
        ("literal-not-a-variable", ["/users/{id}", "/users/id"], 0),
        ("literals-and-two-variables",
         ["/a/{fooBar}/b/{baz-qux}", "/a/{foo_bar}/b/{bazQux}"], 2),
        ("literal-segment-differs",
         ["/a/{fooBar}/b/{bazQux}", "/a/{fooBar}/c/{bazQux}"], 0),
        ("one-variable-differs",
         ["/a/{fooBar}/b/{bazQux}", "/a/{fooBar}/b/{quxBaz}"], 0),
        ("reserved-name", ["/x/{list}", "/x/{list_}"], 2),
        ("reserved-name-control", ["/x/{list}", "/x/{lists}"], 0),
        ("digit-leading-name", ["/x/{2fa-enabled}", "/x/{2fa_enabled}"], 2),
        ("digit-leading-control", ["/x/{2fa}", "/x/{2Fa}"], 0),
        ("digit-word-joins", ["/x/{user2FA}", "/x/{user2fa}"], 2),
        ("digit-boundary-collapses", ["/x/{address_line_1}", "/x/{addressLine1}"], 2),
        ("non-identifier-folds", ["/x/{filter[name]}", "/x/{filterName}"], 2),
        ("no-variables-at-all", ["/a", "/b"], 0),
    )

    def test_the_path_normalization_is_croziers_own(self) -> None:
        """Every case crozier's `naming::field_name` distinguishes, in one run."""
        sources = {
            name: document(name, [(path, ["operationId: op"]) for path in paths])
            for name, paths, _expected in self.NORMALIZATION_CASES
        }
        counted = self.counts(sources, "openapi.paths:normalized-collision")
        self.assertEqual(
            {name: expected for name, _paths, expected in self.NORMALIZATION_CASES if expected},
            counted,
        )

    def test_a_templated_path_key_is_read_apart_from_a_multiply_templated_one(self) -> None:
        """The two Paths Object key predicates, and the case that tells them apart.

        A key carrying exactly one template expression is what separates them:
        `openapi.paths:templated-key` reports it and
        `openapi.paths:several-template-expressions` does not, so an
        implementation where both mean *carries any template expression* fails
        the second assertion on `one-template` and on `mixed`.
        """
        sources = {
            "no-template": document("no-template", [
                ("/widgets", ["operationId: a"]),
                ("/gadgets", ["operationId: b"]),
            ]),
            "one-template": document("one-template", [
                ("/widgets/{id}", ["operationId: a"]),
                ("/gadgets", ["operationId: b"]),
            ]),
            "several-templates": document("several-templates", [
                ("/users/{userId}/roles/{roleId}", ["operationId: a"]),
            ]),
            "mixed": document("mixed", [
                ("/widgets", ["operationId: a"]),
                ("/widgets/{id}", ["operationId: b"]),
                ("/users/{userId}/roles/{roleId}", ["operationId: c"]),
                ("/a/{x}/b/{y}/c/{z}", ["operationId: d"]),
            ]),
        }
        self.assertEqual(
            {"one-template": 1, "several-templates": 1, "mixed": 3},
            self.counts(sources, "openapi.paths:templated-key"),
        )
        self.assertEqual(
            {"several-templates": 1, "mixed": 2},
            self.counts(sources, "openapi.paths:several-template-expressions"),
        )

    def test_a_callback_expression_is_not_a_templated_path_key(self) -> None:
        """The object-model rule holds for these two predicates as well.

        `{$request.body#/callbackUrl}` keys a Callback Object and carries braces
        exactly the way a path template does, so a predicate reading every
        free-keyed map's keys would score it as a templated route. Only the Paths
        Object's own keys are routes.
        """
        source = """\
            openapi: 3.0.3
            info: {title: callbacks, version: "1"}
            paths:
              /subscribe:
                post:
                  operationId: subscribe
                  callbacks:
                    onEvent:
                      "{$request.body#/callbackUrl}":
                        post:
                          responses:
                            "200":
                              description: ok
                  responses:
                    "200":
                      description: ok
            """
        for selector in (
            "openapi.paths:templated-key",
            "openapi.paths:several-template-expressions",
        ):
            with self.subTest(selector=selector):
                self.assertEqual({}, self.counts({"callbacks": source}, selector))
        self.assertEqual(
            {"callbacks": 1}, self.counts({"callbacks": source}, "operation.callbacks")
        )

    def test_a_component_name_collision_counts_every_colliding_key(self) -> None:
        """`components.schemas:normalized-collision`: the other excluded map key."""
        sources = {
            "colliding-names": component_document(
                "colliding-names", ["OBRate1_0", "OB_Rate1_0", "Widget"]
            ),
            "three-colliding-names": component_document(
                "three-colliding-names", ["ob_rate1_0", "OBRate1_0", "obRate1-0"]
            ),
            "distinct-names": component_document(
                "distinct-names", ["OBRate1_0", "OBRate2_0"]
            ),
        }
        self.assertEqual(
            {"colliding-names": 2, "three-colliding-names": 3},
            self.counts(sources, "components.schemas:normalized-collision"),
        )
        # The field selector still counts the one `schemas` declaration each
        # document writes: the predicate adds a reading of that map's keys rather
        # than replacing one.
        self.assertEqual(
            {"colliding-names": 1, "three-colliding-names": 1, "distinct-names": 1},
            self.counts(sources, "components.schemas"),
        )

    # Names spanning what crozier's `naming::class_name` folds together and what it
    # keeps apart: case and punctuation, an underscore run, a leading digit spelled
    # out as an English word, a character `sanitize_identifier` coerces, and the
    # digit boundary a class name — unlike a field name — does not collapse. Each
    # expectation is what crozier's own transform implies; `NamingMirrorTests` below
    # pins the transform against `src/naming.rs`'s own expectations.
    CLASS_NAME_CASES: tuple[tuple[str, list[str], int], ...] = (
        ("case-and-punctuation", ["OBRate1_0", "OB_Rate1_0"], 2),
        ("underscore-run-folds", ["ob_rate_1_0", "OBRate1_0"], 2),
        ("camel-and-snake", ["nested_user", "NestedUser"], 2),
        ("digit-leading-name-spelled-out", ["9lives", "NineLives"], 2),
        ("sanitized-character-folds", ["filter[name]", "filter(name)"], 2),
        ("digit-suffix-control", ["OBRate1", "OBRate1_0"], 0),
        ("distinct-names-control", ["Widget", "Gadget"], 0),
    )

    def test_the_class_name_normalization_is_croziers_own(self) -> None:
        """Every case crozier's `naming::class_name` distinguishes, in one run."""
        sources = {
            name: component_document(name, names)
            for name, names, _expected in self.CLASS_NAME_CASES
        }
        self.assertEqual(
            {name: expected for name, _n, expected in self.CLASS_NAME_CASES if expected},
            self.counts(sources, "components.schemas:normalized-collision"),
        )

    def test_a_document_declaring_none_of_them_reports_each_as_absent(self) -> None:
        """Absent, not missing: the phrase a `gap` row cites as its evidence."""
        # No path key at all: three of the predicates read every Paths Object key
        # and one of the three counts any key there is, so a document with routes
        # cannot be the one that declares none.
        plain = {"plain": """\
            openapi: 3.0.3
            info: {title: plain, version: "1"}
            paths: {}
            components:
              schemas:
                Widget:
                  description: a widget
            """}
        completed = self.census(plain, *sorted(census.PREDICATES))
        self.assertEqual({}, rows(completed))
        for selector in census.PREDICATES:
            with self.subTest(selector=selector):
                self.assertIn(selector, completed.stdout)
        self.assertEqual(
            len(census.PREDICATES),
            completed.stdout.count("(declared by no registered source)"),
        )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "plain", plain["plain"])
            arguments = ["--vendored-only", "--fixtures-root", str(root), "--json"]
            for selector in sorted(census.PREDICATES):
                arguments += ["--selector", selector]
            payload = json.loads(run(*arguments).stdout)
        self.assertEqual([], payload["rows"])
        self.assertEqual(sorted(census.PREDICATES), payload["absent_selectors"])

    def test_each_predicate_selector_is_accepted_by_name(self) -> None:
        """The refusal that guards a typo must not refuse the three real ones."""
        for selector in sorted(census.PREDICATES):
            with self.subTest(selector=selector):
                self.assertIsNone(census.selector_error(selector))


class NamingMirrorTests(unittest.TestCase):
    """`openapi.paths:normalized-collision` normalizes the way crozier does.

    The census is Python and crozier is Rust, so the transform is mirrored rather
    than shared. What keeps the mirror honest is that `src/naming.rs`'s own unit
    tests already pin `field_name` case by case, against Fern's measured output —
    so those expectations are read out of the Rust source here and re-asserted
    against the port. A change to crozier's casing fails this test.
    """

    NAMING = REPO / "src" / "naming.rs"

    @staticmethod
    def unescape(literal: str) -> str:
        return literal.replace('\\"', '"').replace("\\\\", "\\")

    def cases(self, function: str = "field_name", minimum: int = 25) -> list[tuple[str, str]]:
        pattern = re.compile(
            rf'assert_eq!\(\s*{function}\("((?:[^"\\]|\\.)*)"\),'
            r'\s*"((?:[^"\\]|\\.)*)"\s*,?\s*\)'
        )
        found = [
            (self.unescape(wire), self.unescape(expected))
            for wire, expected in pattern.findall(self.NAMING.read_text(encoding="utf-8"))
        ]
        self.assertGreater(
            len(found), minimum, f"src/naming.rs no longer pins {function} case by case"
        )
        return found

    def test_the_port_reproduces_croziers_own_field_name_expectations(self) -> None:
        for wire, expected in self.cases():
            with self.subTest(wire=wire):
                self.assertEqual(expected, census.field_name(wire))

    def test_the_port_reproduces_croziers_own_class_name_expectations(self) -> None:
        """The class-name side of the same mirror.

        `components.schemas:normalized-collision` folds two component names the
        way `naming::class_name` does, so the port is pinned against that
        function's own expectations and against those of the two helpers it
        composes — a change to crozier's casing fails here rather than silently
        moving a census count.
        """
        for function, port, minimum in (
            ("class_name", census.class_name, 1),
            ("to_pascal_case", census.to_pascal_case, 3),
            ("sanitize_identifier", census.sanitize_identifier, 3),
        ):
            for wire, expected in self.cases(function, minimum):
                with self.subTest(function=function, wire=wire):
                    self.assertEqual(expected, port(wire))

    def test_the_reserved_set_is_croziers_own(self) -> None:
        """The trailing-`_` rule is only right if the reserved set is the same one.

        Both directions, because both are collisions the census would invent. A
        name crozier reserves and the port does not leaves `/x/{list}` and
        `/x/{list_}` apart, which crozier renders as one URL; a name the port
        reserves and crozier does not brings `/x/{id}` and `/x/{id_}` together,
        which crozier renders as two. The `field_name` cases above cannot catch
        the second — they only exercise the words `src/naming.rs` happens to pin.
        """
        source = self.NAMING.read_text(encoding="utf-8")
        listed = set()
        for marker in ("const RESERVED_BUILTINS: &[&str] =", "const PYTHON_KEYWORDS: &[&str] = &["):
            self.assertIn(marker, source, f"src/naming.rs no longer declares {marker!r}")
            body = source.split(marker, 1)[1].split("];", 1)[0]
            listed |= set(re.findall(r'"([^"]+)"', body))
        self.assertEqual(
            listed,
            set(census._PYTHON_KEYWORDS) | set(census._RESERVED_BUILTINS),
            "the port's reserved set is not crozier's",
        )
        for name in listed:
            with self.subTest(name=name):
                self.assertTrue(census.is_reserved(name))
        self.assertFalse(census.is_reserved("widget"))

    def test_a_path_template_normalizes_only_its_expressions(self) -> None:
        """The literal text is what distinguishes two routes; it must not move."""
        self.assertEqual(
            "/users/{user_id}/roles/{role_id}",
            census.normalized_path("/users/{userId}/roles/{roleID}"),
        )
        self.assertEqual("/users/userId", census.normalized_path("/users/userId"))


if __name__ == "__main__":
    unittest.main(verbosity=1, buffer=False, argv=[sys.argv[0], *sys.argv[1:]])
