# Witness search for worked-example shapes

The real-specification search behind the worked-example repairs: which required
query arrays an example passes, how a `date-time` example Fern cannot read is
written, how a composed request body that is itself an `allOf` parent orders
its example, and how a request example's `null` members and deprecated
properties are shown. A shape this search found in a registrable document is
registered in [`../../../tests/fixtures/CORPUS.md`](../../../tests/fixtures/CORPUS.md);
a shape it did not is carried by a hand-written fixture under
[`../handwritten/`](../handwritten/AGENTS.md), whose cover cites the verdict
below and this record's renewed search.

## The search

One bounded GitHub code search, issued on 2026-10-05 through
`scripts/rate_limit_guard.py`: eleven phrasings, two or three per shape, each
answered and recorded with its count in [`queries.tsv`](queries.tsv). The first
page of each (up to 100 results) was fetched at its indexed commit, 941 distinct
documents in all. Every one was read by `scripts/openapi-surface-census.py` for
the four keys' selectors below, one document at a time; [`census.tsv`](census.tsv)
records the count per document, or why it could not be read. Every declarer was
screened on licence, immutable reference and pinned Fern (CLI 5.67.1,
`fernapi/fern-python-sdk` 5.20.0), and every one Fern generated from was compared
with crozier; each outcome is in [`screens.tsv`](screens.tsv).

## Verdicts

| key | outcome | selector | declarers |
|---|---|---|---|
| `unread-date-time-example` | `search-incomplete` | `schema.example:unread-date-time` | 51 |
| `allof-parent-request-body` | `search-incomplete` | `mediaType.schema:allof-parent-body` | 0 |
| `request-example-nested-null` | `search-incomplete` | `mediaType.example:nested-null-member` | 3 |
| `request-example-deprecated-property` | `search-incomplete` | `mediaType.example:deprecated-property` | 3 |

The search is bounded — the first page of eleven phrasings — so no key is
`exhausted`.

## Renewed search

| key | outcome | why |
|---|---|---|
| `unread-date-time-example` | `none-registrable` | 24 declarers grant no admissible licence, 12 fail Fern's check, and of the 15 Fern generates from no document both byte-matches and has a worked example read the value (below) |
| `allof-parent-request-body` | `none-registrable` | no document declares it |
| `request-example-nested-null` | `none-registrable` | two declarers grant no licence; `dystcz/dystore-api` differs from crozier apart from the shape (below) |
| `request-example-deprecated-property` | `none-registrable` | each declarer differs from crozier apart from the shape, and none names a required deprecated property |

## Documents that pass the screens but are not registered

Each passes licence, reference and Fern, and is named with the reason it is not
registered here.

- `netgsm/netgsm-sms-js:openapi.json@33ca38622067e3730479aded9e56f6b1151bfeb5`
  (MIT) declares `startdate` and `stopdate` with the example
  `dd.MM.yyyy HH:mm:ss`, and Fern's worked call passes its default
  `2024-01-15T09:30:00+00:00`, as crozier does. crozier differs in
  `src/fern/bulk_sms/raw_client.py` and `src/fern/queries/raw_client.py`, where
  Fern sends a `content-type: application/json` header crozier does not: the
  content-type-header gap.
- `dystcz/dystore-api:openapi.yaml@ffd4d907e6909b0e2b137a490765e144e8d537e7`
  (MIT) gives `null` to nested optional members of its cart-line examples, and
  crozier leaves them out as Fern does. crozier differs only in `reference.md`,
  where Fern documents the tag `⚠️ Not supported yet` as
  `client.⚠️_not_supported_yet…`, a path its own package does not have.
- `hatchet-dev/hatchet`, `tesote/sdk` (`v1` and `v2`) and two
  `jentic/jentic-public-apis` documents (`appconnectv3`, `l1.api.cc.email`)
  byte-match, but declare the unread `date-time` examples only on response
  models' properties, which no worked example reads.
- `moov-io/achgateway`, `RedHatInsights/scheduler`,
  `DMontgomery40/BirdStatsGPT`, `louisburroughs/durion-positivity-backend`
  (`pos-people`, `pos-customer`), `NextCenturyCorporation/kairos-pub`,
  `konfig-dev/konfig`, `confluentinc/ccloud-sdk-go-v2` (`flink-artifact`),
  `confluentinc/cmf-sdk-go`, `256foundation/asic-rs` and the `hospitable.com`
  `jentic` document differ from crozier in files apart from the shape; the count
  of each is in [`screens.tsv`](screens.tsv).

## Required query arrays

A required query array needs no hand-written fixture: registered goldens declare
every side of the measured rule. The JSON side is corpus row 340,
`typescript-service-template`, registered from this search (`usersPatch`'s
required `$ref UserID` array, which Fern's example passes); the `text/*` side is
`amazonaws.com-cloudformation` (`text/xml` responses, where it leaves every
required array out); and a required object query parameter beside the array is
declared by the registered `query-parameters-openapi`. The search's phrasings
for that last pairing found one more declarer, `reeli/swagger-faker`, which
grants no licence. The three operations that differ in the decisive attribute
alone are the authored probe
[`parity-required-query-array-examples`](../authored-probes/parity-required-query-array-examples/).

## Request-example nulls at the top level

The registered `webflow-v2` gives top-level request members `null`.
`RTAinJapan/rta-in-japan-twitter-api-docs` (Apache-2.0) does too and crozier leaves them out as Fern
does, but differs where its first named example's `media_ids` is `[]`: Fern
passes a later example's `["710511363345354753"]` and crozier passes `[]`.
