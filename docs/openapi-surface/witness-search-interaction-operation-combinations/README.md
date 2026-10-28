# Interaction search for operation combinations

This bounded search reopens the five operation-owned combinations named on
base `bc66bfb087fbd34abfe89f1075912b103e848896`: one in `parameters`, four in `bodies-responses`, and none
in `naming-clients`. A census declaration alone is not proof. The detector for
each key is its conjunction below **and an instrumented crozier run executing
every declared interaction site**. No new combination is claimed proven here;
the outstanding screening is stated explicitly below.

## Populations read

Read on 2026-10-28, starting with the registered corpus:

| population | files read | OpenAPI 3 | other version or no root OpenAPI marker | unreadable |
|---|---:|---:|---:|---:|
| registered | 977 | 293 | 684 | 0 |
| APIs.guru | 4138 | 1970 | 2168 | 0 |
| GitHub code search acquisitions | 5125 | 4787 | 285 | 53 |
| Sourcegraph acquisitions | 4078 | 2852 | 1209 | 17 |

The registered population is every JSON/YAML file under `tests/fixtures/` at
base `bc66bfb087fbd34abfe89f1075912b103e848896`, including each registered source; generated metadata is
classified separately rather than counted as a specification. No source bytes
changed in this dispatch.

APIs.guru is the complete `APIs-guru/openapi-directory` archive at
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, SHA-256
`816adb9fb4e19dc9ab28d7ad95363de146251fb41164abdb86f953f9f400c644`.
The archive was recovered from the shared HTTP response cache and its digest
verified before extraction. An initial 19-document extraction was superseded
by this complete enumeration; none of the counts above comes from that subset.

Earlier acquisitions are the retained `candidate-documents.json` manifests and
`documents/` trees from the earlier searches. The two retained copies were
compared: after the index's repository exclusions, the second contributes no
additional file. Their 5,657 and 5,210 manifest identities resolve to the 5,125
and 4,078 distinct files above. Every one of those 9,203 files was hashed and
matched its recorded SHA-256 filename; there were no mismatches. Each positive
row in [census.tsv](census.tsv) names its publisher, path and full immutable
revision, retaining aliases that name identical bytes. The preceding searches'
committed acquisition ledgers retain those same identities and hashes.

No live specification, GitHub, portal or registry request was made for this
search. YAML was first read with PyYAML 6.0.3's C safe loader and JSON with the
stdlib reader. Every unreadable result was retried with the census's own reader
and its normal fallback. [unreadable.tsv](unreadable.tsv) retains the remaining
70 diagnostics; none is counted as a zero declaration. Every parsed document
was evaluated by the repository census's unchanged conjunction evaluator.

## Detectors

The selectors and interaction declarations are unchanged from the base.
Each detector requires both its selector's positive count and execution of its
interaction site in `golden-reach-sites.tsv`.

| key | conjunction | interaction |
|---|---|---|
| `combo-body-property-named-as-path-param` | `operation.requestBody&operation.requestBody:property-named-as-path-parameter` | `rename_claimed_path_params`: the `!overridden && spread.contains(&param.wire_name)` branch |
| `combo-ref-body-read-only-property` | `requestBody.content>mediaType.schema>schema.$ref~>schema.properties>schema.readOnly` | `append_request_call_args`: the response-heavy referenced body's `&& ep.body_schema_is_open` operand |
| `combo-inline-body-read-only-property` | `requestBody.content>mediaType.schema>schema.properties>schema.readOnly` | the declared inline request body's read-only handling site |
| `combo-success-oneof-nullable` | `operation.context:success-nullable&operation.context:success-oneof` | `build_endpoint`: `Some(if dropped_null {` |
| `combo-success-anyof-nullable` | `operation.context:success-anyof&operation.context:success-nullable` | `build_endpoint`: `Some(if dropped_null {` |

## Verdicts

These are `search-incomplete` verdicts: the bounded populations were read, but
new declarers have not all completed interaction screening. A historical
output-sensitive witness is not promoted to interaction proof. The screening
column of `census.tsv` distinguishes the prior screen from this missing step.

| key | verdict | declarers | outstanding evidence |
|---|---|---:|---|
| `combo-body-property-named-as-path-param` | `search-incomplete` | 1256 | a generating document selecting the URL-encoded spreading branch; sharing a JSON body's property name does not suffice |
| `combo-ref-body-read-only-property` | `search-incomplete` | 731 | an instrumented generating document reaching the response-heavy open-body operand, followed by a complete byte match |
| `combo-inline-body-read-only-property` | `search-incomplete` | 20 | the remaining four Webflow files below, or its expressly permitted witness-blocked fixture |
| `combo-success-oneof-nullable` | `search-incomplete` | 24 | admissibility and instrumented screening of the tooling documents below, or an eligible authored fixture |
| `combo-success-anyof-nullable` | `search-incomplete` | 69 | completed interaction screening; the registered simple-nullable examples take an earlier branch |

### Nullable responses

Scoped golden-only runs over `ebusd`, `deepsearch-ds-v2` and `letta` reproduced
the base's missing interaction reach. A structural screen of the earlier
nullable declarers found no inline union with an explicit null alternative
beside at least two non-null alternatives. It did find outer `nullable: true`
on multi-member unions in three tooling documents: the `Rcmade/hono-docs`
example and two `OpenAPITools/openapi-generator` resources, whose full revisions
and hashes are in `census.tsv`. Whether those qualify as real specification
witnesses was escalated to the manager; no admissibility ruling or generation
result is asserted here. No hand-written cover claims `none-registrable` while
that screening remains outstanding.

## Webflow parity

The real Webflow interface was generated before and after the parameter-map
repair and compared through `just fixtures-diff webflow-v2`, using the parity
engine's normalizations. Its measured residual shrank from **83 to 69 files**,
with **14 closed files and no new mismatches**. Only those fourteen paths were
removed from `WEBFLOW_V2.unmatched`; no allowance was added or widened.

`InlineHoister::hoist_param_enum` now declares structured map values under
`{Request}{Parameter}Value`, including the filter object's nested union types
and the sort-direction enum. A regression driving that function was observed
failing with `Dict[str, Any]` before the repair, then passing afterwards. Its
primitive-map case ensures scalar values still retain their original type.
The IR-module filter passed 209 tests. A structural scan of all 293 registered
OpenAPI documents identified Webflow as the only registered document with a
parameter shape this repair changes.

Of the eleven files moved by removing the inline bodies' `readOnly` flags,
four still mismatch: the two scripts clients, the pages-scripts raw client,
and `reference.md`. The scripts clients share inline type names across
`sites.scripts` and `pages.scripts`; the emitter's global type-to-package map
chooses one owner instead of a local owner for each use. The reference also
still differs in collection-field union selection, worked examples and a
query enum rendered as `Any`. These remain parity gaps, not departures.
The [blocked-witness record](../witness-search-operation-combinations-bodies-responses/README.md#blocked-witnesses)
continues to name Webflow and `osf.io`; no whole-file allowance was widened.

The comparison above is against the committed certified-pair golden. Fresh
certified-pair regeneration and the remaining interaction proofs are still
outstanding; this record does not claim either from the comparison alone.
