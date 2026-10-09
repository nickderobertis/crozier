# Withdrawn witness: corpus row 224, `codat-assess`

Row 224 registered Codat's `assess/1.0` description at `APIs-guru/openapi-directory`
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` under the aggregator's own grant, while
[`../witness-search-blocked-artifacts.tsv`](../witness-search-blocked-artifacts.tsv)
lists the same bytes as grant-blocked: no evidenced publisher redistribution
grant, and the aggregator's grant alone does not suffice. It was the only witness
reaching `ref-pointer-composition-index`'s `ref_to_class` pointer-walk site,
`src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` — case 4 of the
coverage report's `ref_to_class` case table: a `$ref` whose pointer passes
through an `allOf`, `oneOf` or `anyOf` index. The row is
withdrawn (`tests/fixtures/CORPUS.md`, *Row 224 withdrawn*), and this record is the
search for a real specification to take its place.

## What reaching the arm takes

The loader copies a pointer into the place it is used whenever it resolves inside
the component (`normalize_schema_pointer_refs` in `src/openapi.rs`), and copies any
pointer whose text names `properties` the way Fern's importer does. A copied pointer
never reaches `ref_to_class` as a reference. So a declarer of
`schema.$ref:composition-index` reaches the walk only through a pointer that names
no `properties` and either ends on a composition member (`…/oneOf/0`) or passes
through a segment no schema is named by (Codat's
`CategorisedAccount/definitions/accountCategoryDeprecated/allOf/1`).

## Replacement search

Searched on 2026-09-30 in the order the task set. GitHub was read only through
`tools/witness-search/rate_limit_guard.py` (REST `core` and `search` buckets, never GraphQL);
Postman and SwaggerHub were not consulted.

| key | arm | step | what was read | result | outcome |
|---|---|---|---|---|---|
| `ref-pointer-composition-index` | `src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` | 1. Codat's own publication | `codatio/oas` at `2dbdc1f7bcdefaf769ab17fcc99fbb098ef2610b`; `codatio/client-sdk-python` | `codatio/oas` has no licence: `GET /repos/codatio/oas/license` is 404, its repository metadata names none, its README grants nothing, and `yaml/Codat-Assess.yaml` declares no `info.license` (nor, at that commit, any composition-index pointer). `codatio/client-sdk-python` names no licence either and carries no OpenAPI document. Every Codat description fails the publisher-grant screen | `exhausted` |
| `ref-pointer-composition-index` | `src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` | 2. Every real declarer the committed records name | the `ref-pointer-composition-index` rows of the six sources' `records.tsv` under [`../golden-reach-witnesses/`](../golden-reach-witnesses/), with their `screens.jsonl` and `probe.jsonl` | see *The declarers* below: each fails a corpus screen, or its every composition-index pointer is copied and never reaches the walk | `exhausted` |
| `ref-pointer-composition-index` | `src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` | 3. Contract B's six declared sources | [the committed arm search](../golden-reach-witnesses/searches/ref-pointer-composition-index.md), one `exhausted` line per source with nothing outstanding; *The six sources* below restates each one's enumeration or queries and its declarers | every declarer it found is a document of *The candidates* below, and none passes all three screens and reaches the walk | `exhausted` |

**Verdict: `exhausted`.** No real specification declares the shape, reaches the
`ref_to_class` walk and passes all three corpus screens. The arm is covered by the
hand-written fixture `composition-index-pointer`
([`../handwritten/`](../handwritten/AGENTS.md)), an arm-level cover citing this
section.

### The six sources

What each source read for `schema.$ref:composition-index`, as the committed arm
search records it; its `records.tsv`, `probe.jsonl` and `screens.jsonl` under
[`../golden-reach-witnesses/`](../golden-reach-witnesses/) hold every document.
That search hunted `resolve_schema_pointer`'s arms rather than this one, but which
documents declare the selector does not depend on the arm, so no new query was
run: the declarers below are every one it found, and each was re-read for this arm.
A census-refused document is one a full standard parser rejects or reads as no
OpenAPI description, as that search defines it, and is no candidate.

| source | enumeration or queries | declarers | census-refused |
|---|---|---:|---:|
| `apis.guru` | walk of `APIs-guru/openapi-directory` at `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, 4138 documents | 5 | 0 |
| `jentic` | walk of `jentic/jentic-public-apis` at `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743`, 74240 documents | 53 | 0 |
| `github-code-search` | `/anyOf/0 "\"$ref\"" filename:openapi.json` (3 hits) and `/oneOf/0 "$ref:" filename:openapi.yaml` (27 hits), every hit fetched at its commit and censused | 9 | 0 |
| `github-publisher-trees` | 30 publisher repositories walked at pinned commits, 6079 documents | 0 | 46 |
| `sourcegraph` | `file:(openapi\|swagger).*\.(yaml\|yml)$ content:"/oneOf/0" count:all type:file` (6) and `file:(openapi\|swagger).*\.json$ content:"/anyOf/0" count:all type:file` (15) | 8 | 0 |
| `vendor-portals` | 25 vendor repositories walked at pinned commits, 13905 documents (`codatio/oas` among them) | 28 | 161 |

### The candidates

Every declarer above, grouped where the bytes are one publisher's description.
*Reach* is how many of the walk's 19 regions an instrumented crozier run executes:
the golden-only tier of `just golden-reach` for a registered row, and the same
instrumented build run over the document alone (`just handwritten-reach
--handwritten-dir DIR --ledger PATH` over a scratch directory holding each
document as a fixture with this arm's cover, on 2026-10-01) for the rest. That
run over row 224's own bytes executes 7 of 19, the reach the ledger recorded
before the withdrawal, so a reading of 0 is the walk not running. A screen not run is marked
so: a candidate needs every screen, so one failure decides it.

| publisher | documents (source) | licence | ref | Fern 5.67.1 / 5.20.0 | reach |
|---|---|---|---|---|---|
| Codat | `assess/1.0`, the withdrawn row (`apis.guru`) | failed: no publisher grant, only the aggregation's | passed: commit `f04b8d0b` | passed: 95 files | 7/19 |
| Codat | `commerce/2.1.0` (`apis.guru`) | failed: no publisher grant | passed: commit `f04b8d0b` | failed: *Failed to resolve schema reference: PhoneNumber/definitions/phoneNumberType* | not measured |
| Codat | `accounting/2.1.0` (`apis.guru`) | failed: no publisher grant | passed: commit `f04b8d0b` | not run | not measured: crozier cannot read it (a tab where YAML indentation is expected, line 43982) |
| Codat | `accounting`, `bank-feeds` and `commerce` 3.0.0, five copies each (`jentic`) | failed: no publisher grant, only the aggregation's | passed: commit `eb9d12a2` | failed, all three: *Failed to resolve schema reference* (`PagingInfo/definitions/…`, `Companies/allOf/1/definitions/…`) | not measured |
| Codat | 14 product descriptions, JSON and YAML (`vendor-portals`: `codatio/oas`) | failed: the repository has no licence (step 1) | passed: commit `2dbdc1f7` | not run | not measured |
| Vonage | `conversation/2.0.1`, registered as row 223 (`apis.guru`; `LoriMarshall/openapidir` in `github-code-search`, the same blob) | passed: row 223, as registered | passed: commit `f04b8d0b` | passed: row 223's golden | 0/19 (`golden-reach.tsv`; the blob alone: 0/19) |
| Vonage | the same description re-quoted in six test-suite copies: `WebFuzzing/EvoMaster`, `ClintonCao/EvoMaster`, `WebFuzzing/fuzzing-nosql`, `suarezrominajulieta/Evo-tesis` (one blob) and `codingsoo/nlp2rest`, `adityaghatge/nlp2rest` (another) (`github-code-search`, `sourcegraph`) | failed: third-party copies, never Vonage's grant — LGPL-3.0 test suites (both EvoMaster, `fuzzing-nosql`) or no licence (`Evo-tesis`, both `nlp2rest`); the committed screens decline them as copies of row 223's document | passed: each at its commit | not run | 0/19 for each blob |
| Vonage | `conversation` and `conversation-api` 2.0.1, five copies each (`jentic`) | recorded passed on the aggregation's grant, no `info.license` | passed: commit `eb9d12a2` | passed | 0/19 for each |
| D&D 5e API | `dnd5eapi.co`, registered as row 42 (`apis.guru`; five copies in `jentic`) | passed: row 42 (MIT) | passed: row 42's pin | passed: row 42's golden | 0/19 (`golden-reach.tsv`; both `jentic` byte variants: 0/19) |
| EmbedPDF | `embed-pdf-viewer` `cloudpdf/contract/openapi.json`, registered as row 171 (`sourcegraph`) | passed: row 171 (Apache-2.0, the document's `info.license`) | passed: commit `2516e278` | passed: row 171's golden | 0/19 (`golden-reach.tsv`) |
| Render | `render.com` 1.0.0, five copies (`jentic`; `sourcegraph` at `047e4ec2`) | failed: no `info.license`, only the aggregation's grant | passed | not run | 0/19 for both byte variants |
| Gladly | `organization.gladly.com` 1.0, three copies (`jentic`) | failed: no `info.license`, and none of Gladly's licensed repositories (`gladly/rest-api-examples`, `gladly/webhook-examples`, `gladly/app-platform-examples`) carries an OpenAPI description | passed: commit `eb9d12a2` | not run | not measured: crozier cannot read it (`invalid type: null, expected a map`), though its 41 `PayloadsNotifyEndpointRequest/oneOf/<n>` pointers name no `properties` |
| Cvent | `cvent.com` `ea`, five copies (`jentic`) | recorded passed on the aggregation's grant; not re-screened | passed: commit `eb9d12a2` | failed: exit 0 over an unparsed document, an empty SDK ([`handoff.tsv`](../golden-reach-witnesses/handoff.tsv)) | not measured |
| Sellsy | `sellsy.com` 2.128.0, five copies (`jentic`) | recorded passed on the aggregation's grant; not re-screened | passed: commit `eb9d12a2` | failed: exit 0 over an unparsed document, an empty SDK ([`handoff.tsv`](../golden-reach-witnesses/handoff.tsv)) | not measured |
| PagerDuty | `pagerduty.com` 2.0.0, five copies (`jentic`) | recorded passed on the aggregation's grant; not re-screened | passed: commit `eb9d12a2` | failed: *Failed to resolve #/components/requestBodies/…* | not measured |
| Check Point | `api-evangelist/cloudguard` `cloudguard-administration-openapi.json` (`github-code-search`) | failed: no licence (`/license` is 404) | passed: commit `c4b28f4e` | failed: its check reports 33 errors (*Objects can only extend other objects*) | not measured |

Rows 223, 42 and 171 pass every screen as registered, and neither they nor any
copy of them reaches the walk: each composition-index pointer they hold names `properties`
(`channel/properties/from/oneOf/0`, `Monster/allOf/3/properties/actions/items`),
so the loader copies it to its use site and `ref_to_class` never walks it.

### Outstanding

Nothing. Every candidate above fails a screen or is measured not reaching the
walk. Each candidate whose reach is not measured fails the licence or the Fern
screen, which decides it whatever its reach. The census-refused
documents in `github-publisher-trees` and `vendor-portals` are not candidates.

## Selectors no other golden-bearing source declares

The census over row 224's bytes (`tools/surface-census/openapi-surface-census.py`'s
`census_document`, 128 selectors) against the census of the 236 registered
sources that remain (`just golden-reach`'s `.local/golden-reach/census.json`, on
2026-10-01) finds seven selectors no other golden-bearing source declares. Six
are declared by no other registered source at all, and `schema.x-examples` only
by two `DROPPED` rows that carry no golden. Each backs no feature: no region
file's entry table carries it as a key and
[`../witness-search-keys.tsv`](../witness-search-keys.tsv) records it for no key.
So it needs no witness. Every other selector row 224 declared is also declared by
a golden-bearing registered source.

| selector | declared by (registered sources) | region row | `witness-search-keys.tsv` |
|---|---|---|---|
| `mediaType.x-speakeasy-usage-example` | row 224 only | none | none |
| `openapi.x-speakeasy-retries` | row 224 only | none | none |
| `parameter.x-stoplight` | row 224 only | none | none |
| `schema.definitions` | row 224 only | none | none |
| `schema.format=ISO4217` | row 224 only | none | none |
| `schema.x-codat-validation` | row 224 only | none | none |
| `schema.x-examples` | row 224, and `canada-holidays.ca` (3) and `groundhog-day.com` (7), both `DROPPED` with no golden | none | none |
