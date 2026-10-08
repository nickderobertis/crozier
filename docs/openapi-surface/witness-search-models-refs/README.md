# Model and reference witness searches

## Scalar formats

| key | verdict | complete trigger |
|---|---|---|
| `number-format-uint64-typed-int` | `search-incomplete` | An object property declares `type: number` and `format: uint64`. |
| `string-json-format-typed-any` | `search-incomplete` | An object property declares `type: string` and `format: json-string`. |

The bounded APIs.guru screen at immutable revision
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` reported no exact declaration
for either shape. An unsigned 32-bit number in the SiriKit Cloud Media
specification is a partial candidate: its format does not declare the required
unsigned 64-bit trigger. Telnyx's JSON-related formats are also partial
candidates because their format spelling is not `json-string`. These partial
candidates cannot stand as complete witnesses.

This record renews that bounded result by reading every committed corpus source
on this branch on 2026-10-08. The retained
[`scalar-formats.tsv`](scalar-formats.tsv) records each source's exact SHA-256
and the two declaration counts. The walk reads parsed mappings recursively,
counting nodes with the exact type and format pair, so it includes response,
request and component properties as well as any declarations outside properties.
Neither trigger occurs. This is a bounded search, not a claim that no publisher
uses either format.

## Renewed search

| key | result | proof |
|---|---|---|
| `number-format-uint64-typed-int` | `none-registrable` | No exact declaration in the committed-source renewal; independent `material-register` fixture. |
| `string-json-format-typed-any` | `none-registrable` | No exact declaration in the committed-source renewal; independent `material-register` fixture. |

The fresh fixture declares a material record with both properties and adjacent
`double` and `uuid` controls. Its complete tree is unedited output of Fern CLI
5.67.1 and `fernapi/fern-python-sdk` 5.20.0 with
`pydantic_config.enum_type: python_enums`. A separate complete certified tree
under `docs/fern-measurements/models-refs-literals/material-register/fern-expected`
uses Fern's default literals mode (no generator configuration). The scoped
real-binary test compares both modes bidirectionally through `src/parity.rs`: the
scalar annotations agree, while the certified literals tree omits the enum
runtime module. It counts only as handwritten
proof, never as a publisher witness.

## Remote component identities

| key | verdict | complete trigger |
|---|---|---|
| `remote-document-local-pointer-resolved-against-root` | `search-incomplete` | A root component names a remote component whose property uses a local pointer into that remote document; the dependency is absent from the root. |
| `remote-ref-at-use-site-inlined` | `search-incomplete` | An operation response directly names an absolute-URL reference to a remote component schema. |

The bounded APIs.guru screen at revision
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` found no complete component-fragment
witness. The renewal on 2026-10-08 reads the 282 committed source documents,
recording their SHA-256 and declaration counts in
[`remote-components.tsv`](remote-components.tsv). It distinguishes root
component aliases and operation response schemas from absolute references
elsewhere. No direct component-fragment trigger occurs.

Helios's references name top-level definitions rather than OpenAPI component
schemas. MockServer references a whole JSON Schema document. Fiware's absolute
references occur in example data. Each misses the required trigger and cannot
stand as a complete witness. This bounded search remains incomplete outside
that population.

The independently authored Library Records proof uses two committed documents
under `tests/e2e/fixtures/models-refs-remote/library-records`. A real loopback
HTTP server serves the second document; no network acquisition is needed in
CI. It combines a root Catalogue alias, its remote Curator dependency, and a
direct Curator response. It proves both named identities and a failed-fetch
recovery journey. It is handwritten proof, never a real witness.

Its complete certified packages use Fern CLI 5.67.1 and
`fernapi/fern-python-sdk` 5.20.0: the tree under
`docs/fern-measurements/models-refs-remote/library-records/fern-expected` uses
`pydantic_config.enum_type: python_enums`; the separate tree under
`docs/fern-measurements/models-refs-literals/library-records/fern-expected` uses
default literals mode. The scoped real-binary test compares each complete
package bidirectionally through `src/parity.rs`, with only catalogued identity
departures. Remote acquisition does not introduce a new configuration setting.

## Renewed remote search

| key | result | proof |
|---|---|---|
| `remote-document-local-pointer-resolved-against-root` | `none-registrable` | No complete trigger in the committed-source renewal; independently authored Library Records multi-file HTTP proof. |
| `remote-ref-at-use-site-inlined` | `none-registrable` | No complete trigger in the committed-source renewal; independently authored Library Records multi-file HTTP proof. |

## Composition models

The bounded APIs.guru screen at full revision
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` found no accepted complete
witnesses for these compositions. Nexmo Reports 2.2.2 declares overlapping
parents, but Fern's whole-document generation refuses a date example. Komga's
`SearchOperatorIsNotNullT` and `SearchOperatorIsNullT` are partial: their
parents are discriminated unions carrying an `operator` field, rather than the
ordinary object parents required by the trigger. Neither substitutes for an
accepted complete witness. The remaining shapes had no complete candidate in
that bounded screen.

The 2026-10-08 renewal walks the 282 committed corpus documents, follows local
schema references through their properties, arrays and compositions, and checks
each complete trigger. The per-source hashes, counts and declaration paths are
retained in `model-shapes.tsv`. These six triggers have no complete declaration
in that population. Searches outside it remain incomplete. Fresh standalone
fixtures recreate only the stated compositions. They are handwritten proofs,
never publisher witnesses. Their complete certified trees use Fern CLI 5.67.1
and `fernapi/fern-python-sdk` 5.20.0 with
`pydantic_config.enum_type: python_enums`.

| key | verdict | proof |
|---|---|---|
| `allof-base-in-cycle-imported-after-class` | `search-incomplete` | Independently authored `circuit-readings`; complete trigger absent from the committed-source renewal. |
| `allof-child-of-cyclic-base-imports-base-deferred` | `search-incomplete` | Independently authored `garden-crown`; complete trigger absent from the committed-source renewal. |
| `allof-overlapping-ref-parents-flattened` | `search-incomplete` | Independently authored `artefact-catalogue`; complete trigger absent from the committed-source renewal. |
| `allof-single-ref-empty-properties-alias` | `search-incomplete` | Independently authored `mineral-sample`; complete trigger absent from the committed-source renewal. |
| `nullable-single-allof-ref-component-not-optional` | `search-incomplete` | Independently authored `nullable-store`; complete trigger absent from the committed-source renewal. |
| `allof-union-branch-not-schema-overrides-property` | `search-incomplete` | Independently authored `sampling-branches`; complete trigger absent from the committed-source renewal. |

## Renewed composition search

| key | result | proof |
|---|---|---|
| `allof-base-in-cycle-imported-after-class` | `none-registrable` | Committed-source renewal; independent `circuit-readings` proof. |
| `allof-child-of-cyclic-base-imports-base-deferred` | `none-registrable` | Committed-source renewal; independent `garden-crown` proof. |
| `allof-overlapping-ref-parents-flattened` | `none-registrable` | Committed-source renewal; independent `artefact-catalogue` proof. |
| `allof-single-ref-empty-properties-alias` | `none-registrable` | Committed-source renewal; independent `mineral-sample` proof. |
| `nullable-single-allof-ref-component-not-optional` | `none-registrable` | Committed-source renewal; independent `nullable-store` proof. |
| `allof-union-branch-not-schema-overrides-property` | `none-registrable` | Committed-source renewal; independent `sampling-branches` proof. |

The scoped composed-models real-binary test also compares every fixture under
default literals mode against a separately certified complete tree under
`docs/fern-measurements/models-refs-literals/<fixture>/fern-expected`. The
source and pins are identical; only the enum setting differs. No enum declaration
is substituted to make a mode pass.

## Property metadata

The bounded APIs.guru screen at immutable full revision
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` and the 2026-10-08 committed-source
renewal have no accepted complete witness for these shapes. The renewal's
282-source hashes, complete-trigger counts and paths are in `model-shapes.tsv`.
GitHub's nullable request-component declaration is a complete declaration
candidate, but its whole document is refused by the certified Fern pair, so it
cannot supply an accepted golden. Mist 0.37.7 declares an empty inline response
description, but Fern refuses duplicate device_mac declarations. AssemblyAI's
specification candidate declares the complete enum-value description shape;
Fern accepts it in Python-enums mode, while crozier refuses
`#/components/links/GetTranscriptById` at
`paths//v2/transcript/post/responses/200/links/GetTranscriptById` even though the
component is declared. It is disqualified for this dispatch under the scope
ruling: component-link resolution is not an assigned scenario. Its redistribution
grant and publisher revision have not been independently confirmed. That
candidate remains a follow-up witness, rather than an accepted migration proof. No unrelated refusal is relaxed for these candidates.
The remaining triggers have no complete declaration in the bounded renewal;
searches outside that population remain incomplete.

Every fresh fixture recreates only its stated shape, with adjacent ordinary
properties as controls. All complete certified trees use Fern CLI 5.67.1 and
`fernapi/fern-python-sdk` 5.20.0. Primary trees use
`pydantic_config.enum_type: python_enums`; separate complete literals trees use
Fern's unset default. These are handwritten proofs, never real witnesses.

| key | verdict | proof |
|---|---|---|
| `empty-description-inline-response-docstring` | `search-incomplete` | Independently authored `blank-reading-description`; no accepted complete witness in the bounded search. |
| `enum-value-description-extension-dropped` | `search-incomplete` | Independently authored `compass-member-notes`; no accepted complete witness in the bounded search. |
| `ignore-extension-on-property-kept` | `search-incomplete` | Independently authored `gauge-public-fields`; no accepted complete witness in the bounded search. |
| `literal-type-extension-ignored` | `search-incomplete` | Independently authored `verified-seal`; no accepted complete witness in the bounded search. |
| `nullable-anyof-member-description-dropped` | `search-incomplete` | Independently authored `nullable-observer-notes`; no accepted complete witness in the bounded search. |
| `property-ref-to-nullable-component-annotation` | `search-incomplete` | Independently authored `reservoir-ledger`; no accepted complete witness in the bounded search. |
| `ref-with-nullable-sibling-made-optional` | `search-incomplete` | Independently authored `required-marker-point`; no accepted complete witness in the bounded search. |

## Renewed metadata search

| key | result | proof |
|---|---|---|
| `empty-description-inline-response-docstring` | `none-registrable` | Committed-source renewal; independent `blank-reading-description` proof. |
| `enum-value-description-extension-dropped` | `none-registrable` | Committed-source renewal; independent `compass-member-notes` proof. |
| `ignore-extension-on-property-kept` | `none-registrable` | Committed-source renewal; independent `gauge-public-fields` proof. |
| `literal-type-extension-ignored` | `none-registrable` | Committed-source renewal; independent `verified-seal` proof. |
| `nullable-anyof-member-description-dropped` | `none-registrable` | Committed-source renewal; independent `nullable-observer-notes` proof. |
| `property-ref-to-nullable-component-annotation` | `none-registrable` | Committed-source renewal; independent `reservoir-ledger` proof. |
| `ref-with-nullable-sibling-made-optional` | `none-registrable` | Committed-source renewal; independent `required-marker-point` proof. |

## Remaining model identities

The immutable bounded APIs.guru screen and the 2026-10-08 renewal over the 282 committed corpus sources found no accepted complete witness for these four triggers. Source hashes and complete-trigger declarations are in `model-shapes.tsv`. Partial object unions and ordinary response references lack the recorded trigger. Searches outside that population remain incomplete. Each standalone proof is independently authored and records the certified pair and Python-enums settings; separate literals trees preserve its default-mode output.

| key | verdict | proof |
|---|---|---|
| `allof-enum-ref-narrowed-by-scalar-member` | `search-incomplete` | Independently authored `measurement-phase`; bounded complete-trigger search found no accepted witness. |
| `allof-extends-oneof-object-refused` | `search-incomplete` | Independently authored `union-sample`; bounded complete-trigger search found no accepted witness. |
| `forward-refs-omit-hoisted-variant-models` | `search-incomplete` | Independently authored `woven-thread`; bounded complete-trigger search found no accepted witness. |
| `ref-into-component-response-schema-named-by-last-segment` | `search-incomplete` | Independently authored `parcel-response`; bounded complete-trigger search found no accepted witness. |

## Renewed model identity search

| key | result | proof |
|---|---|---|
| `allof-enum-ref-narrowed-by-scalar-member` | `none-registrable` | Committed-source renewal; independent `measurement-phase` proof. |
| `allof-extends-oneof-object-refused` | `none-registrable` | Committed-source renewal; independent `union-sample` proof. |
| `forward-refs-omit-hoisted-variant-models` | `none-registrable` | Committed-source renewal; independent `woven-thread` proof. |
| `ref-into-component-response-schema-named-by-last-segment` | `none-registrable` | Committed-source renewal; independent `parcel-response` proof. |

## Model handling arms

The bounded committed-source search above did not establish an accepted whole-document real witness for these specific handling arms. These fixture runs prove the stated arm, without counting as real witnesses.

| key | verdict | handling arm and proof |
|---|---|---|
| `type-single` | `search-incomplete` | `src/ir.rs::base_type_ref[=Some\("json-string"\) => TypeRef::Primitive\(Prim::Any\)]`: `material-register`. |
| `type-single` | `search-incomplete` | `src/ir.rs::base_type_ref[if let Some\(value\) = schema\.bool_literal\(\) \{]`: `verified-seal`. |
| `allof` | `search-incomplete` | `src/ir.rs::Builder::add_named[if schema\.explicitly_nullable\(\) \{]`: `nullable-store`. |
| `allof` | `search-incomplete` | `src/ir.rs::Builder::add_object[if let Some\(branches\) = &parent\.one_of \{]`: `union-sample`. |
| `allof` | `search-incomplete` | `src/ir.rs::Builder::field_type_ref[if let Some\(declaration\) = scalar_narrowed_enum_type\(]`: `measurement-phase`. |
| `allof` | `search-incomplete` | `src/ir.rs::InlineHoister::prop_type_ref[if let Some\(declaration\) = self\.schemas\.and_then\(]`: `measurement-phase`. |
| `enum` | `search-incomplete` | `src/ir.rs::EnumType::example_member[if let Some\(selection\) = &self\.example_selection \{]`: `measurement-phase`. |
| `description` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_object[let docstring = if schema\.description\.as_deref\(\) == Some\(""\) \{]`: `blank-reading-description`. |
| `allof` | `search-incomplete` | `src/ir.rs::Builder::add_object[=\.map\(\x7c\(\(base_name\x2c _\)\x2c _\)\x7c base_name\.clone\(\)\)]`: `circuit-readings`. |

## Renewed handling-arm search

| key | result | proof |
|---|---|---|
| `type-single` | `none-registrable` | Bounded committed-source renewal recorded above; arm-level independent fixtures. |
| `allof` | `none-registrable` | Bounded committed-source renewal recorded above; arm-level independent fixtures. |
| `enum` | `none-registrable` | Bounded committed-source renewal recorded above; arm-level independent fixtures. |
| `description` | `none-registrable` | Bounded committed-source renewal recorded above; arm-level independent fixtures. |
