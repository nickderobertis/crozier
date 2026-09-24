# Guarded GitHub and Sourcegraph witness search checkpoint

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

`outstanding.tsv` is the checkpoint inventory by key and source. It lists
unissued query phrasings verbatim, issued but incomplete phrasings, unfetched
candidate counts, parse or acquisition failures, unscreened declarers, and
publisher trees not yet walked. The exact candidate identities are in each
source's `records.tsv`. A result from a key closed on a licensed, Fern-accepted
witness is `not-owed` where further acquisition was stopped; its closure file
names the witness and the condition for reopening. No key is declared
`exhausted` here. The other three declared sources belong to the sibling search,
and final reconciliation writes each region file's seven-source compact row
after both branches merge.

The publisher set is `witness-search-github-publisher-trees/publisher-set.json`:
the five earlier publisher trees, pinned root-level descriptions in the registered
corpus, and the publisher-owned declarer repositories listed with ownership
reasons in `publisher-declarers.tsv`. Third-party API transcriptions and test
fixtures are excluded from that publisher set. The original eight blocked
artifacts and their missing rights evidence remain in
`../witness-search-github-code-search/blocked-provenance.tsv`;
none is a witness.
