# Candidate ledger

`candidates.tsv` contains only documents confirmed to declare a key by that
key's census selector. It has no `securityscheme-ref` row: the branch-point
`securityScheme:$ref` selector is [unsupported by the census](../witness-search-keys.tsv),
so none of the four registry sources was evaluated for that key. Its search
remains outstanding for final reconciliation.
Adding a candidate here requires a selector output over the parsed document;
an earlier keyword hit or another key's census output does not qualify.

`python3 scripts/witness-search-registries-index.py` rebuilds `candidates.tsv`
from the four sources' `records.tsv` and `outstanding.tsv` from their ledgers.
Its `--check` option, run by `just test-witness-search-acquisition`, fails when
either committed file is stale.

## Outstanding items

`outstanding.tsv` lists, by key and source, every item that keeps this node's
search open, grouped by the blocker that keeps it open. Its `items` cell lists
each identity and its `evidence` cell names the ledger that records it. A key
with any row here does not read `exhausted`, and this node records none as
`exhausted`. The kinds are:

- `selector-unavailable`: `securityscheme-ref`, whose selector the census does
  not support, in each of the four sources. That search is delegated to
  `search-github-continue`; nothing here records it as searched.
- `inconclusive-screen`: a declarer whose Fern screen did not finish.
- `unreadable-document`: a walked file with a recorded parser failure.
- `portal-unanswered`: a portal whose pinned tree could not be read.
- `query-refused`: a Postman `search-all` page the index refused.
- `<hit>-body-unacquired`: a Postman metadata hit whose body no
  unauthenticated route returned.

## The eight grant-blocked artifacts

[`../witness-search-blocked-artifacts.tsv`](../witness-search-blocked-artifacts.tsv)
records the eight wide-scrape artifacts as provenance only: publisher, artifact,
pinned ref, keys and the missing licence evidence. None is a witness, and none
counts toward any key's search. The replacement search for their three keys
over this node's four sources found:

- `annotated-ref-target-closed-object` and `annotated-ref-target-oneof`: the
  pinned `zulip/zulip` description at `6a82f40579f8adb9149aa0b04ff795c397baae73`
  is a replacement witness. It passes the licence, immutable-ref and Fern
  screens, as recorded in `../witness-search-vendor-portals/`. Every other
  declarer of either key in `candidates.tsv` was rejected on its licence screen
  or is `not-owed` after that witness.
- `ref-pointer-unnamed-segment`: 104 declarers, none registrable. 102 have no
  evidenced publisher grant: 14 from APIs.guru, 48 from jentic and all 40 of
  Codat's own pinned `codatio/oas` files. The other two jentic declarers pass
  the licence screen, but Fern exits 0 with an empty SDK. The search across all
  seven sources is final reconciliation's to conclude.
