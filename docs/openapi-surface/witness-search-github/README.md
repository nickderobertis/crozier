# Guarded GitHub and Sourcegraph witness search

`keys.json` in each source directory is derived by `RankedBacklogTests.region_rows`
from the six region files, retaining every `FIXTURE` `gap` row. This checkpoint
has the keys recorded in `keys.json`. The source-specific `queries.jsonl`,
`candidates.jsonl`, `trees.jsonl`, and `documents.jsonl` are the acquisition and
census ledgers.
Each fetched candidate row is a parsed selector result, parser diagnostic, or
acquisition failure; unfetched query results stay outstanding. The only result reduction is repeated hits of the same repository,
path, and pinned revision. Each source's `records.tsv` retains the resulting
candidate identity, digest when fetched, classification, screens, and disposition.
`candidates.tsv` is their consolidated index; regenerate and check both with
`python3 scripts/witness-search-github-index.py` and its `--check` option.

GitHub refuses a pushed file over 100 MB, so a ledger larger than 45 MB is
stored in parts split at line boundaries. The first part keeps the ledger's
own name (`candidates.tsv`), and the rest follow in order as
`candidates.001.tsv`, `candidates.002.tsv`, and so on. The same applies to a
source's `records.tsv`, `candidates.jsonl` and `queries.jsonl`. Read the parts
concatenated in that order; a `records.tsv:N` or `candidates.jsonl:N` reference
counts lines across all of them.

`outstanding.tsv` is the checkpoint inventory by key and source, derived from
the same ledgers by the same index script and held to them by `--check`. It lists
unissued query phrasings verbatim, issued but incomplete phrasings, unfetched
candidate counts, parse or acquisition failures, unscreened declarers, and
publisher trees not yet walked. The exact candidate identities are in each
source's `records.tsv`. A result from a key closed on a licensed, Fern-accepted
witness is `not-owed` where further acquisition was stopped; its closure file
names the witness and the condition for reopening. No key is declared
`exhausted` here. The other declared sources belong to the sibling search, and
final reconciliation writes each region file's compact row over every declared
source after both branches merge.


## Candidates settled against the corpus

A screened candidate whose three screens pass can be settled by corpus
registration rather than by the search:

- `byte-identical to CORPUS row N, sha256 <hex>`: a copy whose bytes equal
  corpus row N's registered source. Registering it again would add no golden.
  `tests/corpus_surface_census_test.py` re-measures each digest against row N's
  fetched document.
- `pending-registration`: a usable candidate the registration node neither
  registered nor disposed. The continuation node owns it.

The publisher set is `witness-search-github-publisher-trees/publisher-set.json`:
the five earlier publisher trees, pinned root-level descriptions in the registered
corpus, and the publisher-owned declarer repositories listed with ownership
reasons in `publisher-declarers.tsv`. Third-party API transcriptions and test
fixtures are excluded from that publisher set. The original eight blocked
artifacts and their missing rights evidence remain in
`../witness-search-github-code-search/blocked-provenance.tsv`;
none is a witness.

## What each source directory holds

`search-index.tsv`, beside each source's `records.tsv`, is that source's evidence
as `key kind subject result file` rows:

- every query string issued, whether a planned phrasing or one of its size
  windows, with its reported count or the non-answer it received;
- every publisher tree at its commit, with its document count;
- every census-confirmed candidate, with the screens it actually ran;
- each rate-limit bucket or paced lane the acquisitions touched, with its calls
  and waits.

This is where the per-key query record lives. No region file carries a
`### Witness search` line for these sources, because final reconciliation
composes each key's compact row. The index script writes `search-index.tsv`
with the other outputs, and `--check` also reconciles it with `records.tsv` and
`queries.jsonl` in both directions.

Code search ran breadth first (`--first-page-only`). Every planned query
answered its first page before any query's size windows and later pages were
read. The evaluate stage fetches each repository, path and revision once and
censuses each digest once. Every key whose results reached that document still
gets its own candidate row, marked `shared_with_key` when the bytes were read
for another key. That deduplication is the only reduction.

GitHub sometimes truncates a window: it returns an empty page before the count
it reported. `--split-truncated-floor` splits such a window in two by file size.
A split window is complete only when both halves are. Splitting stops at a
window no wider than the floor, recorded as `outstanding-index-truncation-floor`,
or when the run's `--split-budget` is spent. A truncated window is never counted
as answered. Each window a query still lacks appears in `outstanding.tsv`, in
that query's `issued_incomplete` entry, with the limit GitHub set: the count it
reported against the results it served. Some windows and pages were never read.
Each of those carries a reason. It names a key closed on a witness through its
closure file, or it says the turn budget ran out first.

The `github/rest-api-description` tree was censused from its codeload archive
at the pinned commit (`acquisition_route` `pinned-archive`, with the archive
URL and SHA-256). Each file's git blob hash was checked against the tree
listing, so these are the bytes the tree names at that commit.

A census-confirmed declarer is screened once per document, and the result is
appended to that source's `screens.jsonl`, with logs under `screens/` and
licence texts under `licences/`:

- **licence**: the repository licence at the pinned commit, read through the
  guarded REST `/repos/{repo}/license?ref=`, together with the document's own
  `info.license`;
- **ref**: whether the revision is an immutable commit;
- **Fern**: `fern check` at CLI 5.67.1, then `fern generate --local` with
  `fernapi/fern-python-sdk` 5.20.0.

A key is closed only by a candidate that passes all three screens and that
review finds to be the publisher's own description. That review applies the
standard in the preamble to the `schemas.md` witness search.

A candidate that passes all three screens but fails that standard is demoted by
a later `screens.jsonl` row. That row carries a `demotion` reason and never
closes a key. Two kinds are demoted: a synthetic test document, including a
byte-identical copy of one, and a third party's edited copy of a publisher's
description.
