# Withdrawn witness: corpus row 223, `nexmo-conversation`

Row 223 registered the Vonage (Nexmo) Conversation API 2.0.1 at
`APIs-guru/openapi-directory` `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` under
the aggregator's CC0-1.0 alone: the document declares no `info.license`. That is
the evidence row 224 was withdrawn on ([`codat-assess.md`](codat-assess.md)): an
aggregation's grant without a publisher grant does not pass the licence screen
of [`../../corpus-licensing.md`](../../corpus-licensing.md). The search below
found no grant from Vonage, so the row is withdrawn (`tests/fixtures/CORPUS.md`,
*Row 223 withdrawn*). Its committed source, golden, `tests/e2e.rs` corpus and
test, and `just test-corpus-match` line are removed.

## The publisher-grant search

Searched on 2026-10-02. GitHub was read only through
`scripts/rate_limit_guard.py` (REST `core`, `search` and `code_search` buckets,
never GraphQL). Postman and SwaggerHub were not consulted.

| step | what was read | result |
|---|---|---|
| 1. The document's own origin | its `info.x-origin`, `https://raw.githubusercontent.com/nexmo/api-specification/master/definitions/conversation.yml` | `GET /repos/nexmo/api-specification` is 404, and so are `Vonage/api-specification`, `Vonage/api-specifications` and `Vonage/vonage-oas`. The publisher repository no longer exists, so no grant can be read from it |
| 2. Every repository of the two publisher organisations | `GET /orgs/Vonage/repos` (148 repositories) and `GET /orgs/Nexmo/repos` (145), each name read for a specification, OpenAPI, portal or Conversation repository | `Vonage/server-sdk-specification`, `Nexmo/server-sdk-specification`, `Nexmo/conversation-docs` and `Vonage/extend-library-specs` grant nothing (no licence). `Nexmo/oas_parser` and `Nexmo/nexmo-oas-renderer` are MIT, but their trees (`d2ab3271`, `d655f943`) carry only test fixtures (`petstore-*.yml`, `voice.yml`, `reports.yml`), never the Conversation API. `Vonage/swagger-codegen` is `NOASSERTION`. The two of those trees read, `Vonage/server-sdk-specification` at `31fdfd08` and `Nexmo/conversation-docs` at `fdc9c463`, hold no OpenAPI description either |
| 3. Code search in both organisations | `org:Vonage "The Conversation API enables you to build conversation features"` (0), `org:Nexmo "The Conversation API enables you to build conversation features"` (0), `org:Vonage-Community "The Conversation API enables you to build conversation features"` (0), `org:Vonage filename:conversation.yml` (0), `org:Vonage x-nexmo-developer-collection-description-shown` (0), `org:Nexmo x-nexmo-developer-collection-description-shown` (1: `Nexmo/oas_parser` `spec/fixtures/voice.yml`, the Voice API) | Vonage publishes no copy of the description on GitHub |

**Verdict:** no publisher grant. The only copies are the aggregation's and the
third-party test-suite copies [`codat-assess.md`](codat-assess.md#the-candidates)
already declines.

## Selectors no other golden-bearing source declares

The census over the 236 registered sources before the withdrawal
(`just surface-census --json`, on 2026-10-02) finds three selectors
row 223 alone declares. None of them is a key in any region file's entry table,
and [`../witness-search-keys.tsv`](../witness-search-keys.tsv) records none of
them for any key. So they back no feature and need no witness. That is the rule
row 224's seven such selectors were settled under
([`codat-assess.md`](codat-assess.md#selectors-no-other-golden-bearing-source-declares)).
The run's planner confirmed it for these three as how this withdrawal meets the
requirement that every census selector the row alone witnessed keeps a witness:
a selector that backs neither a region row nor a witness-search key owes none.

| selector | declared by (registered sources) | region row | `witness-search-keys.tsv` |
|---|---|---|---|
| `info.x-label` | row 223 only | none | none |
| `schema.format=dateTime` | row 223 only | none | none |
| `schema.x-nexmo-developer-collection-description-shown` | row 223 only | none | none |

## The reach row 223 alone carried

`just golden-reach` was re-run without the row: its golden test measured alone
before the withdrawal, then the 218 remaining golden tests at `c7fdee1b2`.
Every `golden-reach.tsv` row still reaches every site it reached before, and
no site's last witness was row 223. Two sites lost regions only row 223
executed:

- `src/ir.rs::inferred_union_discriminant_property` under `oneof-discriminated-union`
  went from 58 to 46 of 59 regions.
- `src/ir.rs::Builder::discriminated_union` went from 213 to 212 of 229.

A region-by-region comparison of row 223's measured run against the union of
the other 218 found four behaviours no remaining golden executes. None of them
is a site `golden-reach-sites.tsv` declares.

| behaviour | crozier site | now witnessed by | real-specification search |
|---|---|---|---|
| A `$ref` whose text names `properties` is copied at the reference: a plain component with `properties` in its name, and a pointer ending on a composition member | `src/openapi.rs::inline_schema_pointers` (`if reference.contains("properties")`) and `properties_reference_target` | hand-written [`ref-pointer-walk`](../handwritten/ref-pointer-walk/) (`route_properties`, `Route/properties/from/oneOf/0`) | `search-incomplete` |
| A union variant copied that way is named after its reference (`ComponentsSchemasRoutePropertiesFromOneOf0`), and its `type` tag kept on the standalone variant | `src/ir.rs::reference_path_class_name` and `Builder::discriminated_union`'s `origin_name` arm | hand-written `ref-pointer-walk` (`Route.to`) | `search-incomplete` |
| A union of such copies is tagged by its inferred `type` property, each value distinct | `src/ir.rs::inferred_union_discriminant_property` | hand-written `ref-pointer-walk` (`Route.to`) | `search-incomplete` |
| An unquoted YAML timestamp is no example for an optional, non-temporal string query parameter, which then goes unshown | `src/emit.rs`, the query-parameter example loop's `yaml_unquoted_timestamps` arm | hand-written `ref-pointer-walk` (`listRoutes`' `since`) | `search-incomplete`. **Open gap:** no real specification is known to witness it |

These are hand-written evidence, a lower level of proof than a real
specification. They count toward no real-specification match. The fixture's
Fern tree was regenerated with Fern CLI 5.67.1 and `fernapi/fern-python-sdk`
5.20.0, unedited, and crozier byte-matches it (`handwritten_fixtures_match_fern_goldens`).
Its arm-level covers stand unchanged, since `just handwritten-reach` measures
them as before.

Each search reads `search-incomplete` because no search was run for these
regions. The committed arm searches for
[`ref-pointer-nested-properties`](../golden-reach-witnesses/searches/ref-pointer-nested-properties.md)
and [`ref-pointer-composition-index`](../golden-reach-witnesses/searches/ref-pointer-composition-index.md)
found the documents declaring `$ref` pointers through `properties` or a
composition index. But they probed each declarer only for the pointer-walk sites
they name, never for these. No census selector reads an unquoted YAML timestamp
as an example at all. A real-specification search for each behaviour, by
Contract B, is still owed. It needs census selectors and declared sites for
these branches first, and the run's planner assigned it outside this
withdrawal: the selectors and sites to the coverage restatement (#361), the
searches to a follow-up. Until those land, the four behaviours rest only on
hand-written evidence, and the YAML-timestamp drop is an open gap.
