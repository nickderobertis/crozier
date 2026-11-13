#!/usr/bin/env python3
"""Write the combination population search's README from the evidence it rests on.

Every count the record states is read here, not written by hand: the screen table
through `population_screen.read_screen`, the manifest, the acquisition plan and its
ledger, and the guarded lanes' own request logs. Re-run it after the table, the
manifest or an acquisition moves; `--check` exits 1 when the committed README is
not what the evidence gives.

Exit status: 0 when it wrote the README (or `--check` found it current); 1 when an
input is missing or malformed, or `--check` found it stale; 2 on a usage error.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import gzip
import importlib.util
import json
import sys
import tempfile
from collections import Counter, defaultdict
from collections.abc import Callable
from pathlib import Path
from types import ModuleType
from typing import Any

REPO = Path(__file__).resolve().parents[2]


def _load(name: str, path: Path) -> ModuleType:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"witness-populations-record: cannot load {path}; restore it from git")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SCREEN = _load("witness_populations_record_screen", Path(__file__).with_name("population_screen.py"))
RECORD = SCREEN.RECORD
HANDED_OFF = Path("docs") / "fern-measurements" / "handed-off" / "documents.tsv"
SERVED_ONLY = Path("docs") / "openapi-surface" / "witness-search-apis.guru" / "unread-responses.jsonl"
BUILD = _load("witness_populations_record_build", Path(__file__).with_name("witness-populations-build.py"))
ARCHIVE = f"`{BUILD.ARCHIVE_REPOSITORY}` at `{BUILD.ARCHIVE_REVISION}`"


def instant(value: Any) -> bool:
    try:
        return isinstance(value, str) and datetime.datetime.fromisoformat(value).tzinfo is not None
    except ValueError:
        return False


# What each evidence field must hold for the README to count it.
FIELD_CHECKS: dict[str, Callable[[Any], bool]] = {
    "at": instant,
    "duration_s": lambda value: isinstance(value, int | float) and not isinstance(value, bool) and value >= 0,
    "population": lambda value: value in SCREEN.POPULATIONS,
    "document": lambda value: isinstance(value, str) and bool(value),
    "how": lambda value: isinstance(value, str) and bool(value),
    "status": lambda value: isinstance(value, int | str) and not isinstance(value, bool),
    "url": lambda value: isinstance(value, str) and value.startswith(("https://", "http://")),
    "host": lambda value: isinstance(value, str) and bool(value),
    "source": lambda value: isinstance(value, str) and bool(value),
    "outcome": lambda value: isinstance(value, str) and bool(value),
    "sha256": lambda value: isinstance(value, str) and bool(SCREEN.SHA.fullmatch(value)),
}


def allowance_failure(row: dict[str, Any]) -> bool:
    """A guard call reporting an allowance must report a whole remaining and a positive limit."""
    if "remaining" not in row and "limit" not in row:
        return False
    remaining, limit = row.get("remaining"), row.get("limit")
    return not (type(remaining) is int and type(limit) is int and 0 <= remaining <= limit and limit > 0)


def records(path: Path, fields: tuple[str, ...], lines: list[str]) -> list[dict[str, Any]]:
    """Each line of an evidence log as the object it records, refusing one whose `fields` do not hold."""
    out = []
    for number, line in enumerate((line for line in lines if line.strip()), 1):
        try:
            row = json.loads(line)
        except ValueError as error:
            raise ValueError(f"{path}:{number} is no JSON ({error})") from error
        if (
            not isinstance(row, dict)
            or any(field not in row or not FIELD_CHECKS[field](row[field]) for field in fields)
            or allowance_failure(row)
        ):
            raise ValueError(f"{path}:{number} is no record carrying {', '.join(fields)}")
        out.append(row)
    return out


def jsonl(path: Path, fields: tuple[str, ...], *, required: bool = True) -> list[dict[str, Any]]:
    """An evidence log's records; a missing log is refused unless it is one written only when something happened."""
    if not path.is_file():
        if required:
            raise ValueError(f"{path} is missing")
        return []
    return records(path, fields, path.read_text(encoding="utf-8").splitlines())


def queries_log(search: Path) -> list[dict[str, Any]]:
    """The search's recorded answers: live as `queries.jsonl`, or committed packed as `queries.jsonl.gz`."""
    live, packed = search / "queries.jsonl", search / "queries.jsonl.gz"
    if live.is_file():
        return jsonl(live, ("source", "outcome"))
    if not packed.is_file():
        raise ValueError(f"{live} (or {packed.name}) is missing")
    with gzip.open(packed, "rt", encoding="utf-8") as handle:
        return records(packed, ("source", "outcome"), handle.read().splitlines())


def table(header: list[str], rows: list[list[Any]], right: int = 0) -> str:
    """A Markdown table, its last `right` columns right-aligned."""
    align = ["---"] * (len(header) - right) + ["---:"] * right
    lines = ["| " + " | ".join(header) + " |", "|" + "|".join(align) + "|"]
    lines += ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]
    return "\n".join(lines) + "\n"


def plan_rows(record: Path) -> list[SCREEN.Identity]:
    return SCREEN.read_identities(record / "identities.tsv.gz") + SCREEN.read_identities(
        record / "search-identities.tsv"
    )


def aggregation_only(entries: list[SCREEN.Entry], root: Path = REPO) -> list[list[str]]:
    """Every registered row whose only recorded grant is an aggregation's: number, name, spec, aggregator."""
    corpus = SCREEN.corpus_rows(root)
    found = []
    with tempfile.TemporaryDirectory(prefix="witness-populations-record-") as scratch:
        for entry in entries:
            if entry.population != "registered":
                continue
            data = SCREEN.registered_bytes(entry.document, root)
            if data is None:
                continue
            try:
                document = SCREEN.parse(data, Path(scratch))
            except Exception:  # an unparseable source grants nothing it can be read for
                continue
            verdict = SCREEN.licence_verdict(document, entry, True, lambda *_args: None)
            if verdict.startswith("inadmissible:") and "aggregation" in verdict:
                row = corpus[entry.document]
                named = SCREEN.aggregator(row.source) or "the aggregation its recorded grant names"
                found.append([row.number, f"`{row.name}`", row.source, named])
    return sorted(found, key=lambda cells: int(cells[0]))


def stamp(value: str) -> str:
    return datetime.datetime.fromisoformat(value).strftime("%Y-%m-%d %H:%M UTC")


def render(record: Path, root: Path = REPO) -> str:
    rows = SCREEN.read_screen(record / "screen.tsv")
    entries = SCREEN.read_manifest(record / "population.tsv")
    plan = plan_rows(record)
    attempts = jsonl(record / "acquisition" / "acquisitions.jsonl", ("population", "document", "how"))
    raw_calls = jsonl(record / "acquisition" / "raw-github-calls.jsonl", ("at", "status", "url"))
    raw_waits = jsonl(record / "acquisition" / "raw-github-waits.jsonl", ("at", "duration_s"))
    queries = queries_log(record / "search")
    calls = jsonl(record / "search" / "rate-limit-calls.jsonl", ("at", "host", "status"))
    pacing = jsonl(record / "search" / "index-pacing-waits.jsonl", ("at", "duration_s"))
    # The guard writes its floor-pause log only when it pauses for the floor.
    floor_waits = jsonl(record / "search" / "rate-limit-waits.jsonl", ("at", "duration_s"), required=False)

    by_key: dict[str, Counter[str]] = defaultdict(Counter)
    status: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        by_key[row.key][row.population] += 1
        status[row.key][row.status.split(":", 1)[0]] += 1
    pending = SCREEN.pending_counts(rows)
    screened = Counter(entry.population for entry in entries if entry.unfetchable == "-")
    unfetchable_entries = Counter(entry.population for entry in entries if entry.unfetchable != "-")

    planned: dict[str, set[str]] = defaultdict(set)
    for identity in plan:
        planned[identity.population].add(identity.document)
    asked: dict[str, dict[str, str]] = defaultdict(dict)
    for attempt in attempts:
        asked[attempt["population"]][attempt["document"]] = attempt["how"]
    held = {
        population: {document for document, how in done.items() if how in ("raw", "store", "shared-cache")}
        for population, done in asked.items()
    }
    refused = {
        population: Counter(how for how in done.values() if how not in ("raw", "store", "shared-cache"))
        for population, done in asked.items()
    }
    hits = sum(1 for identity in plan if SCREEN.BLOB.fullmatch(identity.sha256))
    hit_docs = {identity.document for identity in plan if SCREEN.BLOB.fullmatch(identity.sha256)}

    with (root / HANDED_OFF).open(encoding="utf-8", newline="") as handle:
        handed = list(csv.DictReader(handle, delimiter="\t"))
    no_provenance = [row for row in handed if "@" not in row["document"]]
    served = jsonl(root / SERVED_ONLY, ("sha256",))
    registered_digests = {entry.sha256 for entry in entries if entry.population == "registered"}
    served_registered = sum(1 for row in served if row.get("sha256") in registered_digests)

    def unfetched(population: str) -> int:
        return len(planned[population] - set(asked.get(population, {})))

    sourcegraph_queries = [query for query in queries if query.get("source") == "sourcegraph"]
    code = [query for query in queries if query.get("source") == "github-code-search"]
    code_calls = [call for call in calls if call.get("host") == "github"]
    sourcegraph_calls = [call for call in calls if call.get("host") == "sourcegraph"]
    remaining = [(call["remaining"], call["limit"]) for call in code_calls if isinstance(call.get("remaining"), int)]
    lowest = min(remaining, key=lambda pair: pair[0] / pair[1]) if remaining else None
    raw_status = Counter(str(call.get("status")) for call in raw_calls)
    raw_window = (stamp(raw_calls[0]["at"]), stamp(raw_calls[-1]["at"])) if raw_calls else ("-", "-")

    out: list[str] = []
    w = out.append
    w("# Combination population screen\n")
    w(
        "This record re-acquires the candidate populations the earlier combination searches could not screen, "
        "and screens every candidate of the 22 combination keys below for its complete trigger and an "
        "admissible licence, with crozier's own census and no Fern. Its table, [`screen.tsv`](screen.tsv), is "
        "the input the four combination proof nodes generate from: one row per candidate and key, read only "
        "through `tools/witness-search/population_screen.py`'s `read_screen`, which declares the columns and "
        "admitted values and refuses a malformed, duplicate or self-contradicting row. No Fern generation ran, "
        "no corpus row was registered and no generator source changed. The "
        "[ledger-remainders record](../witness-search-ledger-remainders/README.md) stays as history; the "
        "coverage report's `search incomplete` reasons now cite this one.\n"
    )
    w(
        "A `certified-screen-pending` row is an exact trigger over admissible bytes, not a witness: its "
        "certified-pair generation and complete comparison are the proof nodes' work. The exact bytes of every "
        "such row are kept on this host in `${XDG_CACHE_HOME:-$HOME/.cache}/crozier/witness-populations/<sha256>` "
        "(`population_screen.py cached <sha256>` prints the path); elsewhere they are re-fetched from the row's "
        "`source`.\n"
    )
    w("## Populations\n")
    w(
        table(
            ["population", "what was read", "documents screened", "unfetchable entries"],
            [
                [
                    "`registered`",
                    "every registered corpus row's committed source document (`tests/fixtures/corpus-sources.tsv`)",
                    screened["registered"],
                    unfetchable_entries["registered"],
                ],
                [
                    "`apis-guru`",
                    f"every `openapi.*` document of the pinned APIs.guru archive, {ARCHIVE}; this is where the earlier census's archive declarations come from",
                    screened["apis-guru"],
                    unfetchable_entries["apis-guru"],
                ],
                [
                    "`github`",
                    "every recorded GitHub code-search identity whose exact bytes this host now holds, recovered from the shared response cache or re-fetched at its commit, and this search's code-search hits fetched the same way",
                    screened["github"],
                    unfetchable_entries["github"],
                ],
                [
                    "`sourcegraph`",
                    "every recorded Sourcegraph identity on github.com whose exact bytes this host now holds, recovered or re-fetched the same way",
                    screened["sourcegraph"],
                    unfetchable_entries["sourcegraph"],
                ],
                [
                    "`archive`",
                    "the APIs.guru served-index versions that have no document at the archive pin (`witness-search-apis.guru/unread-responses.jsonl`)",
                    screened["archive"],
                    unfetchable_entries["archive"],
                ],
                [
                    "`handed-off`",
                    "every handed-off document `docs/fern-measurements/handed-off/documents.tsv` names by repository, path and commit",
                    screened["handed-off"],
                    unfetchable_entries["handed-off"],
                ],
            ],
            right=2,
        )
    )
    w(
        "\nA candidate is a document whose bytes the key's census selector declares, or one the earlier "
        "[named census](../witness-search-ledger-remainders/census.tsv) already listed for the key; every one of "
        "that census's 749 rows has a row here. The archive's documents are named `<provider>[/<service>]/<version>`, "
        "the archive path less `APIs/` and the file name, since one service carries several versions.\n"
    )
    w("## Verdicts\n")
    header = [
        "key",
        "verdict",
        "certified-screen-pending",
        *[f"`{p}`" for p in SCREEN.POPULATIONS],
        "rejected-trigger",
        "rejected-licence",
        "unfetchable",
    ]
    w(
        table(
            header,
            [
                [
                    f"`{key}`",
                    "`search-incomplete`",
                    pending[key],
                    *[by_key[key][p] for p in SCREEN.POPULATIONS],
                    status[key]["rejected-trigger"],
                    status[key]["rejected-licence"],
                    status[key]["unfetchable"],
                ]
                for key in sorted(SCREEN.KEYS)
            ],
            right=len(header) - 2,
        )
    )
    w(
        "\nEvery key stays `search-incomplete`: no certified screen runs here, and each has a population below "
        "that could not be had whole. The population columns count candidate rows; the last three count rows "
        "by status.\n"
    )
    w("## How a row is read\n")
    w(
        "* **trigger** — each key's sites are found in the parsed document, and each site's conditions are "
        "judged in order: the census selector's own conditions first, then the earlier search's `needs` "
        "(placement, requiredness, tag and default, pointer shape) or, for the five arm keys, the arm's "
        "condition as its `combination-cooccurrence.tsv` audit row states it. `exact` is a site meeting every "
        "condition; otherwise `partial:<condition>` names the first condition the furthest site misses, and "
        "`absent` means no site exists. Nested pointers are resolved by crozier's own component-pointer walk "
        "(the census's `local_schema_pointer_target`), which follows schema keywords only. The conditions are "
        "`CONDITIONS` in the reader, listed below.\n"
        "* **licence** — read as `witness_screen.py` reads one (JSON read as JSON): the document's own "
        "`info.license` decides wherever it says anything. Only a document declaring none falls back: to the "
        "corpus row's recorded grant for a registered one, to nothing for an APIs.guru archive copy (an "
        "aggregation is no publisher grant), and to its repository's licence file at the pinned commit for a "
        "GitHub, Sourcegraph or handed-off one — read from the shared response cache, fetched through the "
        "guarded raw lane only for an exact trigger, and otherwise left `unread:`.\n"
        "* **status** — `unfetchable:<reason>` where neither could be read; `rejected-trigger` for a "
        "`partial:` or `absent` trigger; for an exact one, `certified-screen-pending` under an admissible "
        "licence and `rejected-licence` under an inadmissible one. The reader refuses any other pairing.\n"
    )
    w("### Trigger conditions\n")
    w(
        table(
            ["key", "conditions, in the order judged"],
            [[f"`{key}`", ", ".join(f"`{c}`" for c in SCREEN.CONDITIONS[key])] for key in sorted(SCREEN.KEYS)],
        )
    )
    aggregated = aggregation_only(entries, root)
    w("\n## Registered rows on an aggregation's grant alone\n")
    w(
        f"{len(aggregated)} registered corpus rows declare no `info.license` and record only an aggregation's grant "
        "(or are copied from an aggregation and record no publisher's). Under the ruling corpus rows 223 and 224 "
        "were withdrawn on, an aggregation's grant is no publisher grant, so this screen reads each one "
        "`inadmissible:` wherever it is a candidate. No corpus row is changed here: whether these rows stay "
        "registered is a decision taken to the user.\n"
    )
    w(table(["row", "corpus name", "spec", "aggregator"], aggregated))
    w("\n## Missing populations\n")
    gh_unfetched, sg_unfetched = unfetched("github"), unfetched("sourcegraph")
    gh_why = (
        f"{gh_unfetched} of the {len(planned['github'])} planned GitHub documents were never fetched: the earlier "
        "acquisition's bytes were not retained on this host, and the manager-ruled bound of about six hours of "
        f"paced raw fetching was spent on higher-ranked identities first. {sum(refused.get('github', Counter()).values())} "
        "fetched ones were refused ("
        + (", ".join(f"{how} {n}" for how, n in sorted(refused.get("github", Counter()).items())) or "none")
        + f"). {len(hit_docs)} of the planned documents are this search's own code-search hits, of which "
        f"{len(hit_docs & held.get('github', set()))} were fetched."
    )
    sg_why = (
        f"{sg_unfetched} of the {len(planned['sourcegraph'])} planned Sourcegraph documents were never fetched, on "
        "the same terms (bytes not retained on this host; the six-hour bound spent first on higher-ranked "
        f"identities); {sum(refused.get('sourcegraph', Counter()).values())} fetched ones were refused. The "
        "anonymous Sourcegraph search answered "
        + (f"{sourcegraph_queries[0].get('result_count')} matches" if sourcegraph_queries else "nothing")
        + ", which name no content digest to pin a fetch to, so none was planned."
    )
    archive_why = (
        f"{len(served)} served-index versions were acquired by an earlier run from mutable `api.apis.guru` URLs; "
        f"{served_registered} are byte-identical to registered corpus sources and are screened under `registered`, "
        f"and the other {len(served) - served_registered} were not retained on this host. No immutable source "
        "names their bytes, so they were not re-fetched."
    )
    handed_why = (
        f"{len(no_provenance)} of the {len(handed)} handed-off documents record bytes only, with no repository, path "
        "or commit; their bytes were not retained on this host (not in the tree, the preflight cache or the response "
        "cache), so nothing names a source to fetch them from."
    )
    w(
        table(
            ["population", "what could not be had, what was tried, and why it failed"],
            [["`github`", gh_why], ["`sourcegraph`", sg_why], ["`archive`", archive_why], ["`handed-off`", handed_why]],
        )
    )
    w(
        "\nNo population above is screened whole, so each one is missing for every key; a key's count of zero "
        "pending candidates stands only beside these rows.\n"
    )
    short = {
        "github": f"bytes not retained on this host; {gh_unfetched} planned documents not re-fetched within the bound",
        "sourcegraph": f"bytes not retained on this host; {sg_unfetched} planned documents not re-fetched within the bound",
        "archive": f"{len(served) - served_registered} served-index versions not retained on this host, behind mutable URLs",
        "handed-off": f"{len(no_provenance)} bytes-only documents not retained on this host, with no source recorded",
    }
    w(
        table(
            ["key", "population", "why not screened whole"],
            [[f"`{key}`", population, why] for key in sorted(SCREEN.KEYS) for population, why in short.items()],
        )
    )
    w("\n## Requests\n")
    w(
        f"**GitHub code search** — {len(code_calls)} requests, every one through `tools/witness-search/rate_limit_guard.py` "
        f"and the shared response cache ([search/rate-limit-calls.jsonl](search/rate-limit-calls.jsonl)), for page 1 "
        f"of each key's `path:openapi` YAML and JSON queries: {Counter(q['outcome'] for q in code).get('answered', 0)} "
        f"answered, {Counter(q['outcome'] for q in code).get('partitioned', 0)} reported over 1,000 results and "
        "were recorded as partitions this bounded pass did not page, and "
        f"{Counter(q['outcome'] for q in code).get('not-queryable', 0)} keys name no schema field a code search can "
        f"spell ([search/queries.jsonl.gz](search/queries.jsonl.gz)). They yielded {hits} new blob-pinned identities. "
        + (
            f"The lowest remaining allowance any call reported was {lowest[0]} of {lowest[1]} "
            f"({100 * lowest[0] // lowest[1]}%)"
            if lowest
            else "No call reported an allowance"
        )
        + (
            "; no call fell below the guard's 40% floor"
            if all(left / limit >= 0.4 for left, limit in remaining)
            else "; some calls fell below the guard's 40% floor"
        )
        + f", and it paused {len(floor_waits)} times for the floor. "
        f"It paused {len(pacing)} times for its spacing (the code-search bucket's 10 requests a minute, "
        f"{sum(w['duration_s'] for w in pacing):.0f} s in all, [search/index-pacing-waits.jsonl](search/index-pacing-waits.jsonl)). "
        "No core or contents REST request was made.\n"
    )
    w(
        table(
            ["at", "bucket", "status", "remaining", "limit"],
            [
                [
                    stamp(c["at"]),
                    c.get("bucket", "-"),
                    c.get("status", "-"),
                    c.get("remaining", "-"),
                    c.get("limit", "-"),
                ]
                for c in code_calls
            ],
            right=2,
        )
    )

    def allowance_before(at: str) -> str:
        """The allowance the guard last reported before a pause began."""
        earlier = [c for c in code_calls if c["at"] <= at and isinstance(c.get("remaining"), int)]
        return f"{earlier[-1]['remaining']} of {earlier[-1]['limit']}" if earlier else "none reported yet"

    w("\nEach pause the guard took on the code-search bucket, with the allowance it last reported:\n")
    w(
        table(
            ["paused at", "cause", "seconds", "remaining allowance"],
            [
                [
                    stamp(wait["at"]),
                    wait.get("cause", "-"),
                    f"{wait.get('duration_s', 0):.0f}",
                    allowance_before(str(wait.get("started_at") or wait["at"])),
                ]
                for wait in [*pacing, *floor_waits]
            ],
            right=2,
        )
    )
    w(
        f"\n**Sourcegraph** — {len(sourcegraph_calls)} anonymous search requests through the guard's paced lane, "
        + ", ".join(f"HTTP {c.get('status')}" for c in sourcegraph_calls)
        + ". The first was the one attempt the manager allowed; the second was an unintended repeat by a re-run "
        "of the search command before it learned to skip a recorded answer, and asked the same query.\n"
    )
    w(
        f"\n**Raw lane** — {len(raw_calls)} exact-commit downloads from raw.githubusercontent.com between "
        f"{raw_window[0]} and {raw_window[1]}, through the acquirer's paced raw lane (2 s spacing; the host "
        "publishes no allowance, so no remaining figure exists to log), each logged with its status and digest "
        "in [acquisition/raw-github-calls.jsonl](acquisition/raw-github-calls.jsonl): "
        + ", ".join(f"HTTP {s} {n}" for s, n in sorted(raw_status.items()))
        + f". It paused {len(raw_waits)} times for its spacing. Every answer was written to the shared response "
        "cache. Each planned identity it reached is in "
        "[acquisition/acquisitions.jsonl](acquisition/acquisitions.jsonl) with how its bytes were had: "
        + ", ".join(f"{how} {n}" for how, n in sorted(Counter(a["how"] for a in attempts).items()))
        + ".\n"
    )
    w("\n## Reproduce\n")
    w(
        "```sh\n"
        "# The acquisition plan from the committed ledgers, and the bounded live search.\n"
        "uv run --locked --all-packages python tools/witness-search/witness-populations-build.py identities \\\n"
        "  --output docs/openapi-surface/witness-search-combination-populations/identities.tsv.gz\n"
        "GITHUB_TOKEN=... uv run --locked --all-packages python tools/witness-search/witness-populations-build.py search \\\n"
        "  --evidence docs/openapi-surface/witness-search-combination-populations/search \\\n"
        "  --identities docs/openapi-surface/witness-search-combination-populations/identities.tsv.gz \\\n"
        "  --output docs/openapi-surface/witness-search-combination-populations/search-identities.tsv\n"
        "# Exact bytes into the host store: the store, the shared cache, then the paced raw lane, by rank.\n"
        "uv run --locked --all-packages python tools/witness-search/population_screen.py acquire \\\n"
        "  --identities <plan> --evidence docs/openapi-surface/witness-search-combination-populations/acquisition \\\n"
        "  --budget-seconds <seconds>\n"
        "# The manifest, the screen and this README.\n"
        "uv run --locked --all-packages python tools/witness-search/witness-populations-build.py manifest \\\n"
        "  --identities docs/openapi-surface/witness-search-combination-populations/identities.tsv.gz \\\n"
        "  --identities docs/openapi-surface/witness-search-combination-populations/search-identities.tsv \\\n"
        "  --archive <extracted openapi-directory tree>\n"
        "uv run --locked --all-packages python tools/witness-search/population_screen.py screen --workers 8 --fetch-licence\n"
        "uv run --locked --all-packages python tools/witness-search/witness-populations-record.py\n"
        "# The suite holds this README to its evidence (`--check` exits 1 when it is stale).\n"
        "uv run --locked --all-packages python tools/witness-search/witness-populations-record.py --check\n"
        "```\n"
    )
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--record", type=Path, default=RECORD)
    parser.add_argument("--root", type=Path, default=REPO, help="the repository whose records are read")
    parser.add_argument("--check", action="store_true", help="exit 1 when the committed README is stale")
    args = parser.parse_args(argv)
    try:
        text = render(args.record, args.root)
    except (OSError, ValueError, KeyError) as error:
        print(f"witness-populations-record: {error}; restore the record's inputs from git", file=sys.stderr)
        return 1
    readme = args.record / "README.md"
    if args.check:
        if not readme.is_file() or readme.read_text(encoding="utf-8") != text:
            print(
                f"witness-populations-record: {readme} is not what its evidence gives; re-run without --check",
                file=sys.stderr,
            )
            return 1
        return 0
    readme.write_text(text, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
