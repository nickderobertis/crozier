# Candidate ledger

**Scope, as amended by the manager.** This node writes no region-file
`### Witness search` line. Neither form the gate accepts can hold this node's
segments on their own. The compact row must name every declared source and
reconcile against the sibling search's consolidated ledger. The per-source
seven-cell line reads `records.tsv` as `key kind subject result file`, which
the candidate-record ledgers here do not use. Final reconciliation writes each
key's row from this directory's `candidates.tsv` and `outstanding.tsv` and the
per-source `records.tsv`. Postman carries no search obligation.

`candidates.tsv` contains only documents confirmed to declare a key by that
key's census selector. It has no `securityscheme-ref` row: the branch-point
`securityScheme:$ref` selector is [unsupported by the census](../witness-search-keys.tsv),
so none of this node's sources was evaluated for that key. Its search
remains outstanding for final reconciliation.
Adding a candidate here requires a selector output over the parsed document;
an earlier keyword hit or another key's census output does not qualify.

`python3 scripts/witness-search-registries-index.py` rebuilds `candidates.tsv`
from each of this node's sources' `records.tsv`, and `outstanding.tsv` from their ledgers.
Its `--check` option, run by `just test-witness-search-acquisition`, fails when
either committed file is stale.


## Candidates settled against the corpus

A screened candidate whose three screens pass can be settled by corpus
registration rather than by the search:

- `byte-identical to CORPUS row N, sha256 <hex>`: a copy whose bytes equal
  corpus row N's registered source. Registering it again would add no golden.
  `tests/corpus_surface_census_test.py` re-measures each digest against row N's
  fetched document.
- `pending-registration`: a usable candidate the registration node neither
  registered nor disposed. The continuation node owns it.

## Outstanding items

`outstanding.tsv` lists, by key and source, every item that keeps this node's
search open, grouped by the blocker that keeps it open. Its `items` cell lists
each identity and its `evidence` cell names the ledger that records it. A key
with any row here does not read `exhausted`, and this node records none as
`exhausted`. The kinds, which the acquisition tier reconciles with the ones the
script emits, are:

- `selector-unavailable`: `securityscheme-ref`, whose selector the census does
  not support, in each of this node's sources. That search is delegated to
  `search-github-continue`; nothing here records it as searched.
- `inconclusive-screen`: a declarer whose Fern screen did not finish.
- `unreadable-document`: a walked file with a recorded parser failure.
- `portal-unanswered`: a portal whose pinned tree could not be read.

Postman is not a declared source, by the user's decision, so no key lists it as
searched or outstanding.

## The eight grant-blocked artifacts

[`../witness-search-blocked-artifacts.tsv`](../witness-search-blocked-artifacts.tsv)
records the eight wide-scrape artifacts as provenance only: publisher, artifact,
pinned ref, keys and the missing licence evidence. None is a witness, and none
counts toward any key's search. The replacement search for their three keys
over this node's declared sources found:

- `annotated-ref-target-closed-object` and `annotated-ref-target-oneof`: the
  pinned `zulip/zulip` description at `6a82f40579f8adb9149aa0b04ff795c397baae73`
  is a replacement witness. It passes the licence, immutable-ref and Fern
  screens, as recorded in `../witness-search-vendor-portals/`. Every other
  declarer of either key in `candidates.tsv` was rejected on its licence screen
  or is `not-owed` after that witness.
- `ref-pointer-unnamed-segment`: 104 declarers, none registrable. 102 have no
  evidenced publisher grant: 14 from APIs.guru, 48 from jentic and all 40 of
  Codat's own pinned `codatio/oas` files. The other two jentic declarers pass
  the licence screen, but Fern exits 0 with an empty SDK. The search across every
  declared source is final reconciliation's to conclude.
