# Withdrawn witness: corpus row 224, `codat-assess`

Row 224 registered Codat's `assess/1.0` description at `APIs-guru/openapi-directory`
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` under the aggregator's own grant, while
[`../witness-search-blocked-artifacts.tsv`](../witness-search-blocked-artifacts.tsv)
lists the same bytes as grant-blocked: no evidenced publisher redistribution
grant, and the aggregator's grant alone does not suffice. It was the only witness
reaching `ref-pointer-composition-index`'s `ref_to_class` pointer-walk site,
`src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` — case 4 of the
`ref_to_class` case table in
[`../../openapi-surface-coverage.md`](../../openapi-surface-coverage.md): a `$ref`
whose pointer passes through an `allOf`, `oneOf` or `anyOf` index. The row is
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
`scripts/rate_limit_guard.py` (REST `core` and `search` buckets, never GraphQL);
Postman and SwaggerHub were not consulted.

| key | arm | step | what was read | result | outcome |
|---|---|---|---|---|---|
| `ref-pointer-composition-index` | `src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` | 1. Codat's own publication | `codatio/oas` at `2dbdc1f7bcdefaf769ab17fcc99fbb098ef2610b`; `codatio/client-sdk-python` | `codatio/oas` has no licence: `GET /repos/codatio/oas/license` is 404, its repository metadata names none, its README grants nothing, and `yaml/Codat-Assess.yaml` declares no `info.license` (nor, at that commit, any composition-index pointer). `codatio/client-sdk-python` names no licence either and carries no OpenAPI document. Every Codat description fails the publisher-grant screen | `exhausted` |
| `ref-pointer-composition-index` | `src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` | 2. Every real declarer the committed records name | the `ref-pointer-composition-index` rows of the six sources' `records.tsv` under [`../golden-reach-witnesses/`](../golden-reach-witnesses/), with their `screens.jsonl` and `probe.jsonl` | see *The declarers* below: each fails a corpus screen, or its every composition-index pointer is copied and never reaches the walk | `exhausted` |
| `ref-pointer-composition-index` | `src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` | 3. Contract B's six declared sources | [the committed arm search](../golden-reach-witnesses/searches/ref-pointer-composition-index.md): `apis.guru`, `jentic`, `github-code-search`, `github-publisher-trees`, `sourcegraph` and `vendor-portals`, each `exhausted` on build `4828cc2b93f0` | its declarers are exactly step 2's; reaching this arm rather than `resolve_schema_pointer`'s changes which declarers could qualify, not which documents declare the selector, so no new query was run | `exhausted` |

**Verdict: `exhausted`.** No real specification declares the shape, reaches the
`ref_to_class` walk and passes all three corpus screens. The arm is covered by the
hand-written fixture `composition-index-pointer`
([`../handwritten/`](../handwritten/AGENTS.md)), an arm-level cover citing this
section.

### The declarers

| publisher | documents | why none qualifies |
|---|---|---|
| Codat | APIs.guru `assess/1.0` (the withdrawn row) and `commerce/2.1.0`; Jentic `accounting`, `bank-feeds` and `commerce` 3.0.0; `codatio/oas` products | no publisher grant (step 1); `commerce/2.1.0` and the Jentic `accounting` 3.0.0 documents are also refused by Fern 5.20.0 (*Failed to resolve schema reference*) |
| Vonage | `nexmo-conversation` (row 223) and its mirrors | every composition-index pointer names `properties`, so each is copied; `golden-reach.tsv` measures the site unreached by it |
| D&D 5e API | `dnd5eapi.co` | `Monster/allOf/3/properties/actions/items` names `properties` and is copied; measured unreached the same way |
| EmbedPDF | `embedpdf-cloudpdf` | every pointer names `properties` and is copied; measured unreached the same way |
| Render | Jentic `render.com` 1.0.0 | every schema pointer names `properties`, and the one other points into `components.parameters`; the document declares no `info.license`, and only the aggregation's grant covers it |
| Gladly | Jentic `organization.gladly.com` 1.0 | its 41 `PayloadsNotifyEndpointRequest/oneOf/<n>` pointers would reach the walk, but crozier's probe cannot read the document (`invalid type: null, expected a map`), it declares no `info.license`, and none of Gladly's licensed repositories (`gladly/rest-api-examples`, `gladly/webhook-examples`, `gladly/app-platform-examples`) carries an OpenAPI description: no publisher grant |
| Cvent, Sellsy | Jentic `cvent.com` `ea`, `sellsy.com` 2.128.0 | Fern 5.20.0 exits 0 over an unparsed document, an empty 35-file SDK ([`handoff.tsv`](../golden-reach-witnesses/handoff.tsv)) |
| PagerDuty | Jentic `pagerduty.com` 2.0.0 | Fern 5.20.0 refuses it (*Failed to resolve #/components/requestBodies/…*) |
| Check Point CloudGuard | `api-evangelist/cloudguard` | no licence (`/license` is 404), and Fern 5.20.0's check reports 33 errors |
