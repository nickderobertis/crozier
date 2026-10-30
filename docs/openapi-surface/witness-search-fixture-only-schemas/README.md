# Witness search for the fixture-only `schemas` rows

The rows of [`../schemas.md`](../schemas.md) whose only proof, at base `1748b7946`, was a hand-written fixture: every `handwritten` row (72, five of them combinations), every arm-level hand-written cover of a `golden` row (80 distinct key and arm pairs), and the one residual-only supplement (`schema-example-null`). The certified pair is Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3.

## Outcome

- **Proven by a registered real witness: 9.** Seven rows already had registered, wholly byte-matched witnesses; one more, and one arm, rest on corpus row 4000 (`stellastra-com`), registered here. They are tabled under [The real witnesses](#the-real-witnesses).
- **`exhausted`:** the six feature rows and 46 arms whose cited search already read `exhausted`, confirmed under [Confirmed exhaustive searches](#confirmed-exhaustive-searches).
- **`search-incomplete`, with every outstanding candidate named:** 58 feature rows, the residual supplement and 34 arms (the one added being `kiln-array-mode`'s new arm cover). Each names what stops it under [Feature verdicts](#feature-verdicts) and [Arm verdicts](#arm-verdicts).

## Populations read

Read on 2026-10-29 from copies already on this host; no specification was fetched and no network request was made.

| population | revision | identities read | OpenAPI 3 digests | unreadable |
|---|---|---:|---:|---:|
| APIs.guru | `APIs-guru/openapi-directory` at `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, the revision the corpus's APIs.guru rows pin, read from an earlier search's extraction of that revision's archive | 4138 | 1970 | 0 |
| registered | every JSON and YAML file under `tests/fixtures/` at `1748b7946` | 986 | 289 | 0 |
| github-code-search | the documents earlier searches acquired, the union of both retained `candidate-documents.json` manifests (each file content-addressed by its SHA-256) | 5109 | 4824 | 53 |
| sourcegraph | the same, for Sourcegraph's acquisitions | 4077 | 2862 | 18 |

**Live GitHub: none.** This search made no GitHub request, so `tools/witness-search/rate_limit_guard.py` admitted none: 0 live requests in every bucket (`core`, `search`, `code_search`) and 0 shared-cache hits. GitHub code search was not run for any target in this bound; every `search-incomplete` verdict below owes it.

## Detectors

Every document was read twice: by the census (`tools/witness-search/witness-search-local-census.py` over each target's selector) and by a complete-trigger detector where the selector is broader than the row's shape.

- **A feature row** is declared where its census selector in [`../witness-search-keys.tsv`](../witness-search-keys.tsv) counts a site. Where that selector is a single broad field (`schema.allOf`, `schema.description`, …), the declarer is a document holding the row's complete trigger, read off the parsed document by the detector tabled below; each detector fires on the row's own hand-written fixture.
- **An arm** is declared where the golden row's selector in [`../golden-reach-sites.tsv`](../golden-reach-sites.tsv) counts a site **and** an instrumented `crozier generate` over the document executes the arm, read with `golden-reach-search.py`'s own `_probe_one` against the base's instrumented build. Every arm cover's own fixture executes its arm under that run (85 of 85). The run gave each document 90 seconds and replaced `ruff` with a pass-through, which leaves crozier's own regions as they run; a document that timed out or that crozier refused gives no reading and stays outstanding.
- **A combination** is declared where its conjunction counts a site and the instrumented run executes every interaction site its `golden-reach-sites.tsv` row names.

The instrumented run covered the registered and APIs.guru populations whole. The code-search and Sourcegraph acquisitions were not probed: the run's rate (about 26 documents a minute on this host) put them some six hours out, so every arm and combination declarer there is outstanding, counted per key below. Resume with `probe.py`'s command line over those two populations, as this record's census lists them.

| key | complete trigger |
|---|---|
| `allof-base-in-cycle-imported-after-class` | a component with own `properties` whose `allOf` names a component whose reference closure reaches the child |
| `allof-child-of-cyclic-base-imports-base-deferred` | a component with own `properties` whose `allOf` names a component in a reference cycle the child is not on |
| `allof-enum-ref-narrowed-by-scalar-member` | a property `allOf` of a `$ref` to a string enum beside an inline `type: string` member |
| `allof-extends-oneof-object-refused` | a component with own `properties` whose `allOf` names a component declaring `oneOf` |
| `allof-overlapping-ref-parents-flattened` | an `allOf` of two or more `$ref`s whose targets declare a property name in common |
| `allof-single-ref-empty-properties-alias` | a component writing `properties: {}` and an `allOf` of exactly one `$ref` |
| `allof-union-branch-not-schema-overrides-property` | an `allOf` member whose `oneOf`/`anyOf` branch declares a property schema written as `not` |
| `bigint-format-string-typed-str` | an object property `type: string, format: bigint` |
| `discriminated-variant-date-value-snippet` | a component `oneOf` with a `discriminator`, used by `$ref` as a JSON request body, whose variants declare both a `format: date` and a `format: date-time` property |
| `enum-value-description-extension-dropped` | a string enum whose `x-fern-enum` (or `x-crozier-enum`) gives a member a `description` |
| `forward-refs-omit-hoisted-variant-models` | two components, each a discriminated `oneOf` with an inline variant naming the other |
| `ignore-extension-on-property-kept` | a property writing `x-fern-ignore: true` (or `x-crozier-ignore`) |
| `integer-example-beyond-double-precision` | an `integer`, `format: int64` schema whose int64 example's nearest double leaves the int64 range |
| `integer-format-fallback` | a `type: integer` schema with `format: bigint` |
| `literal-example-dollar-escaped-in-docstring` | a JSON request body requiring a property whose string `const` holds `$` |
| `literal-type-extension-ignored` | a property whose `x-fern-type` (or `x-crozier-type`) is a `literal<…>` |
| `nullable-anyof-member-description-dropped` | a property `anyOf` of `type: 'null'` beside one described inline object or enum member |
| `nullable-single-allof-ref-component-not-optional` | a component writing `nullable: true` and an `allOf` of exactly one `$ref`, no own `properties` |
| `number-format-uint64-typed-int` | an object property `type: number, format: uint64` |
| `oneof-duplicate-members-collapsed` | a `oneOf` with two JSON-identical inline members |
| `property-ref-to-nullable-component-annotation` | an inline JSON request body property `$ref` to a `nullable: true` object component |
| `ref-into-component-response-schema-named-by-last-segment` | a `$ref` into `#/components/responses/…/schema` |
| `ref-with-nullable-sibling-made-optional` | a required property writing `$ref` with a sibling `nullable: true` |
| `reference-literal-single-quote-escaped` | a JSON request body requiring a property whose string `const` holds `'` |
| `string-json-format-typed-any` | an object property `type: string, format: json-string` |
| `undiscriminated-ref-oneof-sibling-properties-dropped` | a schema with `properties` beside a two-member `oneOf` of `$ref`s and no `discriminator` |
| `union-of-enum-ref-const-and-string-members` | a `oneOf` of a `$ref` string enum, a `type: string` `const` and a plain `type: string` |
| `union-of-two-enum-refs-alias` | a component `oneOf` of exactly two `$ref`s to string enums |
| `variant-nullable-value-optional-default-none` | a discriminated `$ref` variant whose non-discriminant property is required and `nullable` |

[`census.tsv`](census.tsv) lists every declarer of every target with its site count, SHA-256 and screening outcome. An APIs.guru document declaring no `info.license` is admissible through the aggregation's CC0-1.0, as the corpus's APIs.guru rows already are; one whose own licence grants nothing is refused.

## The real witnesses

| key | witness | golden | comparison test |
|---|---|---|---|
| `described-ref-oneof-alias-without-docstring` | corpus rows 3400 `ecommerce-ai-skills-runtime`, 305 `hasura-metadata`, 232 `mockserver` and 69 `tamoss`: each writes a described `oneOf` of object `$ref`s as a docstring-less `typing.Union` alias | `tests/fixtures/{ecommerce-ai-skills-runtime,hasura-metadata,mockserver,tamoss}/expected` | `*_matches_fern_output`, `schemas_fixture_only_real_witnesses_declare_their_shapes` |
| `variant-own-fields-before-allof-parent-fields` | corpus row 3478 `ingef-conquery`: `FilterValue_Integer` writes its own `value` before `FilterValueBase`'s `filter` | `tests/fixtures/ingef-conquery/expected`, `expected-literals` | `ingef_conquery_matches_fern_output`, `overlay_goldens_match_fern_output` |
| `cycle-into-cycle` | corpus row 3478 `ingef-conquery` | `tests/fixtures/ingef-conquery/expected` | `ingef_conquery_matches_fern_output` |
| `anyof-array-variant-inline-enum-item` | corpus row 2802 `langchain-agent-server`: each `stream_mode` splits into `…_stream_mode`, `…_zero_item` and `…_one` | `tests/fixtures/langchain-agent-server/expected` | `langchain_agent_server_matches_fern_output` |
| `enum-visit-kwargs-parameter` | corpus row 2802 `langchain-agent-server`: the runs `select` enum's `kwargs` visitor parameter is `kwargs_` | `tests/fixtures/langchain-agent-server/expected` | `langchain_agent_server_matches_fern_output`, `naming_wire_shapes_fail_on_an_unexplained_byte` |
| `type-misspelled-scalar` | corpus row 3002 `panoptes`: `TextFacet.startOpen` is `type: bool`, typed `Optional[Any]` | `tests/fixtures/panoptes/expected` | `panoptes_matches_fern_output` |
| `unread-date-time-example` | corpus row 332 `netgsm-sms`: `dd.MM.yyyy HH:mm:ss` becomes Fern's default instant | `tests/fixtures/netgsm-sms/expected` | `netgsm_sms_matches_fern_output` |
| `empty-description-inline-response-docstring` | corpus row 4000 `stellastra-com`, registered here | `tests/fixtures/stellastra-com/expected` | `stellastra_com_matches_fern_output` |

Each row is `golden` on its census selector, with a [`../golden-reach-sites.tsv`](../golden-reach-sites.tsv) site its witness executes in the scoped measurement. Two needed a census predicate of their own (`components.schemas:described-object-ref-union`, `components.schemas:variant-own-fields-before-base`) and one more (`operation.responses:blank-description-inline-object`). `schemas_fixture_only_real_witnesses_declare_their_shapes` in [`real_witnesses.rs`](../../../crates/crozier-e2e/tests/e2e/real_witnesses.rs) holds each witness to its source and golden. `anyof-array-variant-inline-enum-item`'s witness reaches its `Builder::field_type_ref` site; its `InlineHoister::hoist_union_variant` site is reached by no real specification, so `kiln-array-mode` keeps it as an arm-level cover (below).

Stellastra (`APIs/stellastra.com/1.0/openapi.yaml`, 7 KB) was the smallest admissible APIs.guru document executing the `description` arm. Fern generated its packaged tree through `just fern-goldens-generate --version 5.41.3 --fixture stellastra-com`, and `crozier compare` matched it whole with only the `sdk-identity-header-prefix` departure. Its one string enum is a plain one the literals-overlay set already reaches, so it carries no `expected-literals/`.
Its golden test executes the blank-description arm of `description` (`src/ir.rs::InlineHoister::hoist_object[let docstring = if schema\.description\.as_deref\(\) == Some\(""\) \{]`), measured over every `description` witness, so the arm is reached and `blank-reading-description` retired whole.

The superseded covers went with them: `described-ref-oneof-alias-without-docstring`, `variant-own-fields-before-allof-parent-fields`, `survey-field-selector`, `float-typed-properties` and `chained-reference-cycles` were deleted, with their literals overlays; `unread-date-time-examples` moved to [the examples-docs measurements](../../fern-measurements/examples-docs/README.md), where it keeps the zone-name and negative-offset spellings `netgsm-sms` does not declare; `kiln-array-mode` lost its feature cover.

## Feature verdicts

Declarer counts are distinct `(population, digest)` pairs in `census.tsv`. Every APIs.guru declarer named here also owes its certified-pair screen; every code-search and Sourcegraph declarer owes its licence, immutable-reference and certified-pair screens.

| key | outcome | declarers | outstanding |
|---|---|---|---|
| `allof-base-in-cycle-imported-after-class` | `search-incomplete` | 13 github-code-search, 6 sourcegraph (complete-trigger detector) | 13 github-code-search, 6 sourcegraph; GitHub code search not run |
| `allof-child-of-cyclic-base-imports-base-deferred` | `search-incomplete` | 10 github-code-search, 6 sourcegraph (complete-trigger detector) | 10 github-code-search, 6 sourcegraph; GitHub code search not run |
| `allof-enum-ref-narrowed-by-scalar-member` | `search-incomplete` | 2 sourcegraph (complete-trigger detector) | 2 sourcegraph; GitHub code search not run |
| `allof-extends-oneof-object-refused` | `search-incomplete` | 6 github-code-search, 3 sourcegraph (complete-trigger detector) | 6 github-code-search, 3 sourcegraph; GitHub code search not run |
| `allof-overlapping-ref-parents-flattened` | `search-incomplete` | 4 apis.guru, 1 registered, 22 github-code-search, 27 sourcegraph (complete-trigger detector) | 4 apis.guru, 22 github-code-search, 27 sourcegraph; GitHub code search not run |
| `allof-single-ref-empty-properties-alias` | `search-incomplete` | 3 github-code-search, 2 sourcegraph (complete-trigger detector) | 3 github-code-search, 2 sourcegraph; GitHub code search not run |
| `allof-union-branch-not-schema-overrides-property` | `search-incomplete` | 2 github-code-search, 6 sourcegraph (complete-trigger detector) | 2 github-code-search, 6 sourcegraph; GitHub code search not run |
| `anyof-array-variant-inline-const-item` | `search-incomplete` | 4 github-code-search, 1 sourcegraph (selector `schema.anyOf>schema.type:primary=array&schema.items>!schema.$ref&schema.const:string-valued`) | 4 github-code-search, 1 sourcegraph; GitHub code search not run |
| `bigint-format-string-typed-str` | `search-incomplete` | 0 (complete-trigger detector) | none in the populations read; GitHub code search not run |
| `combo-allof-nullable` | `search-incomplete` | 16 apis.guru, 13 registered, 154 github-code-search, 194 sourcegraph (selector `schema.allOf&schema.nullable`; interaction: `Builder::add_named_shape`'s nullable single-reference arm, executed by no probed declarer) | 16 apis.guru, 154 github-code-search, 194 sourcegraph; GitHub code search not run |
| `combo-annotated-ref-property-example` | `search-incomplete` | 2 apis.guru, 3 registered, 3 github-code-search, 1 sourcegraph (selector `schema.properties>schema.allOf:annotated-ref&schema.example`; a co-occurrence row, read by its conjunction alone) | 2 apis.guru, 3 github-code-search, 1 sourcegraph; GitHub code search not run |
| `combo-anyof-beside-properties` | `search-incomplete` | 23 apis.guru, 12 registered, 124 github-code-search, 178 sourcegraph (selector `schema.anyOf&schema.properties:non-empty`; interaction: `Builder::add_named_shape`'s sibling-field loop and `Builder::discriminated_union`'s shared-base arm, executed by no probed declarer) | 23 apis.guru, 124 github-code-search, 178 sourcegraph; GitHub code search not run |
| `combo-oneof-beside-properties` | `search-incomplete` | 26 apis.guru, 14 registered, 190 github-code-search, 165 sourcegraph (selector `schema.oneOf&schema.properties:non-empty`; interaction: the same two sites over `oneOf`, executed by no probed declarer) | 26 apis.guru, 190 github-code-search, 165 sourcegraph; GitHub code search not run |
| `combo-oneof-schema-example` | `search-incomplete` | 8 apis.guru, 7 registered, 131 github-code-search, 124 sourcegraph (selector `schema.example&schema.oneOf`; interaction: `referenced_example_literal`'s `oneOf` rejection block, executed by no probed declarer) | 8 apis.guru, 131 github-code-search, 124 sourcegraph; GitHub code search not run |
| `component-same-primitive-union` | `search-incomplete` | 16 github-code-search, 33 sourcegraph (selector `components.schemas:same-primitive-union`) | 16 github-code-search, 33 sourcegraph; GitHub code search not run |
| `discriminated-variant-date-value-snippet` | `search-incomplete` | 0 (complete-trigger detector) | none in the populations read; GitHub code search not run |
| `enum-value-description-extension-dropped` | `search-incomplete` | 4 github-code-search, 2 sourcegraph (complete-trigger detector) | 4 github-code-search, 2 sourcegraph; GitHub code search not run |
| `forward-refs-omit-hoisted-variant-models` | `search-incomplete` | 0 (complete-trigger detector) | none in the populations read; GitHub code search not run |
| `ignore-extension-on-property-kept` | `search-incomplete` | 2 sourcegraph (complete-trigger detector) | 2 sourcegraph; GitHub code search not run |
| `integer-example-beyond-double-precision` | `search-incomplete` | 1 github-code-search (complete-trigger detector) | 1 github-code-search; GitHub code search not run |
| `integer-format-fallback` | `search-incomplete` | 2 github-code-search, 11 sourcegraph (complete-trigger detector) | 2 github-code-search, 11 sourcegraph; GitHub code search not run |
| `literal-enum-value-quote-escaping` | `search-incomplete` | 23 apis.guru, 8 registered, 18 github-code-search, 18 sourcegraph (selector `schema.enum:apostrophe-member`) | 23 apis.guru, 18 github-code-search, 18 sourcegraph; GitHub code search not run |
| `literal-example-dollar-escaped-in-docstring` | `search-incomplete` | 2 github-code-search (complete-trigger detector) | 2 github-code-search; GitHub code search not run |
| `literal-type-extension-ignored` | `search-incomplete` | 0 (complete-trigger detector) | none in the populations read; GitHub code search not run |
| `nullable-anyof-member-description-dropped` | `search-incomplete` | 9 github-code-search, 13 sourcegraph (complete-trigger detector) | 9 github-code-search, 13 sourcegraph; GitHub code search not run |
| `nullable-single-allof-ref-component-not-optional` | `search-incomplete` | 1 apis.guru, 4 github-code-search, 2 sourcegraph (complete-trigger detector) | 1 apis.guru, 4 github-code-search, 2 sourcegraph; GitHub code search not run |
| `number-format-uint64-typed-int` | `search-incomplete` | 2 github-code-search, 1 sourcegraph (complete-trigger detector) | 2 github-code-search, 1 sourcegraph; GitHub code search not run |
| `oneof-array-variant-inline-const-item` | `search-incomplete` | 0 (selector `schema.oneOf>schema.type:primary=array&schema.items>!schema.$ref&schema.const:string-valued`) | none in the populations read; GitHub code search not run |
| `oneof-array-variant-inline-enum-item` | `search-incomplete` | 2 apis.guru, 29 github-code-search, 23 sourcegraph (selector `schema.oneOf>schema.type:primary=array&schema.items>!schema.$ref&schema.enum:string-valued`) | 2 apis.guru, 29 github-code-search, 23 sourcegraph; GitHub code search not run |
| `oneof-duplicate-members-collapsed` | `search-incomplete` | 12 github-code-search, 5 sourcegraph (complete-trigger detector) | 12 github-code-search, 5 sourcegraph; GitHub code search not run |
| `oneof-map-variant-anyof-value` | `search-incomplete` | 0 (selector `schema.oneOf>!schema.properties:non-empty&schema.type:primary=object&schema.additionalProperties>!schema.$ref&!schema.oneOf&schema.anyOf:several-non-null-members`) | none in the populations read; GitHub code search not run |
| `property-anyof-sole-string-enum-member` | `search-incomplete` | 2 github-code-search (selector `schema.properties>!schema.nullable&!schema.type&schema.anyOf:sole-member&schema.anyOf>!schema.$ref&schema.enum:string-valued`) | 2 github-code-search; GitHub code search not run |
| `property-oneof-sole-string-enum-member` | `search-incomplete` | 4 github-code-search, 6 sourcegraph (selector `schema.properties>!schema.nullable&!schema.type&schema.oneOf:sole-member&schema.oneOf>!schema.$ref&schema.enum:string-valued`) | 4 github-code-search, 6 sourcegraph; GitHub code search not run |
| `property-ref-to-nullable-component-annotation` | `search-incomplete` | 13 apis.guru, 1 registered, 4 github-code-search, 4 sourcegraph (complete-trigger detector) | 13 apis.guru, 4 github-code-search, 4 sourcegraph; GitHub code search not run |
| `ref-into-component-response-schema-named-by-last-segment` | `search-incomplete` | 1 apis.guru, 2 github-code-search, 7 sourcegraph (complete-trigger detector) | 1 apis.guru, 2 github-code-search, 7 sourcegraph; GitHub code search not run |
| `ref-with-nullable-sibling-made-optional` | `search-incomplete` | 16 github-code-search, 23 sourcegraph (complete-trigger detector) | 16 github-code-search, 23 sourcegraph; GitHub code search not run |
| `reference-literal-single-quote-escaped` | `search-incomplete` | 2 github-code-search (complete-trigger detector) | 2 github-code-search; GitHub code search not run |
| `remote-document-local-pointer-resolved-against-root` | `search-incomplete` | 5 registered, 188 github-code-search, 169 sourcegraph (selector `schema.$ref:cross-document`) | 188 github-code-search, 169 sourcegraph; GitHub code search not run |
| `remote-ref-at-use-site-inlined` | `search-incomplete` | 5 registered, 188 github-code-search, 169 sourcegraph (selector `schema.$ref:cross-document`) | 188 github-code-search, 169 sourcegraph; GitHub code search not run |
| `request-body-property-closed-empty-object` | `search-incomplete` | 2 github-code-search (selector `mediaType.schema:closed-empty-object-property`) | 2 github-code-search; GitHub code search not run |
| `schema-example-array-null-element` | `search-incomplete` | 2 apis.guru, 26 github-code-search, 13 sourcegraph (selector `schema.example:array-null-element`) | 2 apis.guru, 26 github-code-search, 13 sourcegraph; GitHub code search not run |
| `schema-example-null` | `search-incomplete` | 1 apis.guru, 2 registered, 15 github-code-search, 11 sourcegraph (selector `schema.example=null`) | 1 apis.guru, 15 github-code-search, 11 sourcegraph; GitHub code search not run |
| `schema-example-temporal-duplicate-element` | `search-incomplete` | 0 (selector `schema.example:temporal-duplicate-element`) | none in the populations read; GitHub code search not run |
| `schema-example-union-ref-sentinel` | `search-incomplete` | 0 (selector `schema.example:union-ref-sentinel`) | none in the populations read; GitHub code search not run |
| `schema-name-builtin-complex` | `search-incomplete` | 1 sourcegraph (selector `components.schemas:complex-module-name`) | 1 sourcegraph; GitHub code search not run |
| `schema-sdk-group-name` | `search-incomplete` | 4 github-code-search, 2 sourcegraph (selector `schema.x-fern-sdk-group-name:component`) | 4 github-code-search, 2 sourcegraph; GitHub code search not run |
| `schema-type-name-inline-property` | `search-incomplete` | 1 registered (selector `schema.x-fern-type-name:inline-property`) | none in the populations read; GitHub code search not run |
| `schema-x-tags` | `search-incomplete` | 16 github-code-search, 13 sourcegraph (selector `schema.x-tags:component`) | 16 github-code-search, 13 sourcegraph; GitHub code search not run |
| `string-json-format-typed-any` | `search-incomplete` | 1 sourcegraph (complete-trigger detector) | 1 sourcegraph; GitHub code search not run |
| `undiscriminated-ref-oneof-sibling-properties-dropped` | `search-incomplete` | 1 apis.guru, 11 github-code-search, 29 sourcegraph (complete-trigger detector) | 1 apis.guru, 11 github-code-search, 29 sourcegraph; GitHub code search not run |
| `union-of-enum-ref-const-and-string-members` | `search-incomplete` | 0 (complete-trigger detector) | none in the populations read; GitHub code search not run |
| `union-of-two-enum-refs-alias` | `search-incomplete` | 6 github-code-search, 2 sourcegraph (complete-trigger detector) | 6 github-code-search, 2 sourcegraph; GitHub code search not run |
| `variant-nullable-value-optional-default-none` | `search-incomplete` | 29 github-code-search, 6 sourcegraph (complete-trigger detector) | 29 github-code-search, 6 sourcegraph; GitHub code search not run |

## Arm verdicts

`probed` is the arm key's registered and APIs.guru declarers the instrumented run read; `no reach` generated without executing the arm, `timeout` and `refused` gave no reading. A candidate executes the arm and is named; `unprobed` are the code-search and Sourcegraph declarers.

| key | outcome | arm | fixture | probed | no reach | timeout | refused | candidates | unprobed |
|---|---|---|---|---:|---:|---:|---:|---|---|
| `additional-properties-schema` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `survey-map-value-union` | 1072 | 543 | 203 | 289 | none | 2652 github-code-search, 1771 sourcegraph |
| `allof` | `search-incomplete` | `src/ir.rs::Builder::add_named_shape[if schema\.explicitly_nullable\(\) \{]` | `nullable-store` | 645 | 197 | 70 | 372 | none | 1683 github-code-search, 1163 sourcegraph |
| `allof` | `search-incomplete` | `src/ir.rs::Builder::add_object[if let Some\(branches\) = &parent\.one_of \{]` | `union-sample` | 645 | 197 | 70 | 372 | none | 1683 github-code-search, 1163 sourcegraph |
| `allof` | `search-incomplete` | `src/ir.rs::Builder::field_type_ref[if let Some\(declaration\) = scalar_narrowed_enum_type\(]` | `harbour-window`, `measurement-phase` | 645 | 197 | 70 | 372 | none | 1683 github-code-search, 1163 sourcegraph |
| `allof` | `search-incomplete` | `src/ir.rs::InlineHoister::prop_type_ref[=^ {12}return TypeRef::Named\(ref_to_class\(reference\)\);]` | `kiln-variant-trigger` | 645 | 196 | 70 | 372 | `APIs/cpy.re/peertube/5.1.0/openapi.yaml` | 1683 github-code-search, 1163 sourcegraph |
| `anyof-map-variant-anyof-value` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `survey-map-value-union` | 5 | 4 | 1 | 0 | none | 23 github-code-search, 46 sourcegraph |
| `anyof-map-variant-oneof-value` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `survey-map-value-union` | 1 | 1 | 0 | 0 | none | 5 github-code-search, 4 sourcegraph |
| `discriminator-mapping` | `search-incomplete` | `src/ir.rs::Builder::discriminated_union[if let Some\(merged\) = merged_mapping_union\(target\x2c &property_name\x2c self\.schemas\) \{]` | `kitchen-nested-mapping-target` | 57 | 42 | 8 | 6 | none | 493 github-code-search, 358 sourcegraph |
| `enum` | `search-incomplete` | `src/ir.rs::EnumType::example_member[if let Some\(index\) = self\.members\.example \{]` | `harbour-window`, `measurement-phase` | 1883 | 1113 | 270 | 460 | none | 3692 github-code-search, 2216 sourcegraph |
| `format-binary` | `search-incomplete` | `src/emit.rs::build_example_inner[if s\.type_ref == TypeRef::Primitive\(Prim::Bytes\)]` | `json-binary-path`, `json-request-shapes` | 216 | 126 | 41 | 43 | `APIs/noosh.com/1.0/openapi.yaml` | 880 github-code-search, 763 sourcegraph |
| `format-binary` | `search-incomplete` | `src/ir.rs::hoist_form_object[if nullable_binary]` | `multipart-nullable-array` | 216 | 127 | 41 | 43 | none | 880 github-code-search, 763 sourcegraph |
| `format-binary` | `search-incomplete` | `src/ir.rs::scalar_body[=Some\("binary"\)]` | `json-binary-path`, `json-request-shapes` | 216 | 126 | 41 | 43 | `APIs/noosh.com/1.0/openapi.yaml` | 880 github-code-search, 763 sourcegraph |
| `format-byte` | `search-incomplete` | `src/ir.rs::has_byte_text_response[=^ {16}return true;$]` | `byte-text-response`, `byte-text-response-controls` | 314 | 188 | 105 | 16 | `APIs/visualstudio.com/v1/openapi.yaml` | 155 github-code-search, 218 sourcegraph |
| `format-byte` | `search-incomplete` | `src/ir.rs::scalar_body[=Some\("uuid" \x7c "byte"\)]` | `sonar-packet-envelope` | 314 | 187 | 105 | 16 | `APIs/contribly.com/1.0.0/openapi.yaml`; `APIs/id4i.de/1.0.2/openapi.yaml` | 155 github-code-search, 218 sourcegraph |
| `format-date` | `search-incomplete` | `src/ir.rs::scalar_body[=Some\("date"\) =>]` | `skyglass-observation-date` | 223 | 101 | 34 | 52 | `APIs/contribly.com/1.0.0/openapi.yaml`; `APIs/noosh.com/1.0/openapi.yaml` | 685 github-code-search, 509 sourcegraph |
| `format-int64` | `search-incomplete` | `src/ir.rs::bounded_example_literal[=^ {16}exact$]` | `odometer-reading` | 608 | 355 | 152 | 66 | none | 942 github-code-search, 914 sourcegraph |
| `format-uuid` | `search-incomplete` | `src/ir.rs::scalar_body[=Some\("uuid" \x7c "byte"\)]` | `meadow-tag-code` | 344 | 285 | 26 | 29 | none | 1171 github-code-search, 694 sourcegraph |
| `nullable` | `search-incomplete` | `src/ir.rs::Builder::variant_ref[if is_plain_scalar\(variant\) && variant\.nullable == Some\(true\)]` | `thermostat-nullable-member` | 381 | 268 | 39 | 68 | `APIs/journy.io/1.0.0/openapi.yaml` | 1395 github-code-search, 977 sourcegraph |
| `oneof` | `search-incomplete` | `src/ir.rs::build_endpoint[Some\(if dropped_null \{]` | `quiz-nullable-response-union` | 260 | 151 | 36 | 50 | none | 1985 github-code-search, 1407 sourcegraph |
| `oneof` | `search-incomplete` | `src/ir.rs::hoist_error_body_types[if schema\.discriminator\.is_some\(\)]` | `error-body-shapes` | 260 | 151 | 36 | 50 | none | 1985 github-code-search, 1407 sourcegraph |
| `oneof-anyof-variant` | `search-incomplete` | `src/ir.rs::Builder::field_type_ref[=(?<=\.map\(\x7cvalues\x7c )\(items\x2c values\)]` | `kiln-array-mode` | 3 | 3 | 0 | 0 | none | 7 github-code-search, 21 sourcegraph |
| `oneof-anyof-variant` | `search-incomplete` | `src/ir.rs::InlineHoister::prop_type_ref[=return self.prop_type_ref\(parent\x2c prop\x2c &union\);]` | `kiln-nested-reason` | 3 | 3 | 0 | 0 | none | 7 github-code-search, 21 sourcegraph |
| `oneof-discriminated-union` | `search-incomplete` | `src/ir.rs::Builder::discriminated_union[if !schema\.properties\.is_empty\(\)]` | `library-union-shared-fields` | 107 | 65 | 15 | 17 | `APIs/vercel.com/0.0.1/openapi.yaml` | 767 github-code-search, 550 sourcegraph |
| `oneof-discriminated-union` | `search-incomplete` | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | `nested-array-discriminated-unions` | 107 | 66 | 15 | 17 | none | 767 github-code-search, 550 sourcegraph |
| `oneof-map-variant-oneof-value` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `survey-map-value-union` | 1 | 1 | 0 | 0 | none | 7 github-code-search, 3 sourcegraph |
| `oneof-sole-non-null-member` | `search-incomplete` | `src/ir.rs::Builder::add_named_shape[if variants\.len\(\) > 1 && is_inline_object\(only\)]` | `harbor-nullable-inline-object` | 7 | 6 | 1 | 0 | none | 235 github-code-search, 126 sourcegraph |
| `oneof-string-const-variant` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(values\) = string_enum_values\(variant\) \{]` | `compass-choice` | 5 | 3 | 1 | 0 | `APIs/vercel.com/0.0.1/openapi.yaml` | 44 github-code-search, 23 sourcegraph |
| `property-map-value-oneof` | `search-incomplete` | `src/ir.rs::InlineHoister::prop_type_ref[if value.reference.is_none\(\) && value.declared_type_name\(\).is_none\(\) && structured \{]` | `shelf-labels-map-variants` | 14 | 7 | 5 | 0 | `APIs/journy.io/1.0.0/openapi.yaml`; `APIs/vercel.com/0.0.1/openapi.yaml` | 53 github-code-search, 43 sourcegraph |
| `property-oneof-residual` | `search-incomplete` | `src/ir.rs::untagged_inline_discriminator[if untagged \{]` | `atlas-untagged-inline-discriminator` | 124 | 55 | 22 | 27 | none | 805 github-code-search, 603 sourcegraph |
| `ref-pointer-undeclared-component-head` | `search-incomplete` | `src/ir.rs::Builder::discriminated_union[if all_dangling \{]` | `ferry-mapping-outside-schemas` | 13 | 11 | 2 | 0 | none | 59 github-code-search, 37 sourcegraph |
| `ref-pointer-undeclared-component-head` | `search-incomplete` | `src/ir.rs::resolve_schema_pointer[=(?<=schemas\.get\(parts\.next\(\)\?\))\?;$]` | `ref-pointer-ignored-head` | 13 | 11 | 2 | 0 | none | 59 github-code-search, 37 sourcegraph |
| `schema-example-outside-enum` | `search-incomplete` | `src/emit.rs::ExampleCtx::example_matches_type_through[=Some\(TypeDecl::Enum\(decl\)\) => value]` | `enum-media-selection` | 41 | 15 | 11 | 14 | none | 41 github-code-search, 55 sourcegraph |
| `type-single` | `search-incomplete` | `src/ir.rs::base_type_ref[if let Some\(value\) = schema\.bool_literal\(\) \{]` | `verified-seal` | 2251 | 1425 | 277 | 506 | none | 4798 github-code-search, 2826 sourcegraph |
| `anyof-array-variant-inline-enum-item` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(list\) = self\.hoist_array_item_enum\(&variant_name, variant\) \{]` | `kiln-array-mode` | 4 | 4 | 0 | 0 | none | 43 github-code-search, 38 sourcegraph |

The `anyof-array-variant-inline-enum-item` site was not in the instrumented run's site set; its four registered and APIs.guru declarers are read off the scoped golden-reach measurement (three goldens) and crozier's run over the one APIs.guru declarer instead.

## Confirmed exhaustive searches

A cover whose cited search already read `exhausted` keeps citing it. The confirmation owed is that nothing registered since reaches it: no registered golden declares the row or executes the arm in the base's golden-reach ledger, and the instrumented run found no registered or APIs.guru document executing any of these arms except `codat.io/assess`, which [the withdrawn-witness record](../withdrawn-witnesses/codat-assess.md) already decided for `ref-pointer-composition-index`.

| key | outcome | target |
|---|---|---|
| `annotated-ref-shape` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[^ {16}\{$]` (`inline-oneof-variants`) |
| `annotated-ref-target-anyof` | `exhausted` | `src/ir.rs::InlineHoister::prop_type_ref[if target.one_of.is_some\(\)]` (`inline-property-unions`) |
| `anyof-allof-variant` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[^ {8}\{$]` (`inline-anyof-variants`) |
| `anyof-array-variant-annotated-ref-item` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[^ {16}\{$]` (`inline-anyof-variants`) |
| `anyof-array-variant-anyof-nullable-item` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[simple_nullable_member\(item\) \{]` (`inline-anyof-variants`) |
| `anyof-array-variant-closed-object-item` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[if item.reference.is_none\(\) && is_inline_struct\(item\) \{]` (`inline-anyof-variants`) |
| `anyof-array-variant-composed-item` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[if item.reference.is_none\(\) && is_inline_struct\(item\) \{]` (`inline-anyof-variants`) |
| `anyof-array-variant-oneof-nullable-item` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[simple_nullable_member\(item\) \{]` (`inline-anyof-variants`) |
| `anyof-discriminated-union` | `exhausted` | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` (`nested-array-discriminated-unions`) |
| `anyof-oneof-variant` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = variant\.one_of\.as_ref\(\)\.or\(variant\.any_of\.as_ref\(\)\) \{]` (`inline-anyof-variants`) |
| `array-item-anyof-discriminated-union` | `exhausted` | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` (`nested-array-discriminated-unions`) |
| `array-item-empty-object` | `exhausted` | `src/ir.rs::Builder::nested_array_element[if is_inline_struct\(items\) \{]` (`nested-array-elements`) |
| `array-item-oneof-discriminated-union` | `exhausted` | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` (`nested-array-discriminated-unions`) |
| `array-item-pointer-walk-allof` | `exhausted` | `src/ir.rs::resolve_schema_pointer[^\s*"allOf" => \{]` (`ref-pointer-walk`) |
| `array-item-pointer-walk-anyof` | `exhausted` | `src/ir.rs::resolve_schema_pointer[^\s*"anyOf" => \{]` (`ref-pointer-walk`) |
| `array-item-pointer-walk-items` | `exhausted` | `src/ir.rs::resolve_schema_pointer[^\s*"items" => \{]` (`ref-pointer-walk`) |
| `array-item-pointer-walk-properties` | `exhausted` | `src/ir.rs::resolve_schema_pointer[^\s*"properties" => \{]` (`ref-pointer-walk`) |
| `discriminator-mapping` | `exhausted` | `src/emit.rs::ExampleCtx::named_value_inner[Some\(m\) if m\.layout\.is_wrapped\(\) => \{]` (`tidepool-survey-log`) |
| `discriminator-mapping` | `exhausted` | `src/ir.rs::Builder::discriminated_union[if union_target \{]` (`tidepool-survey-log`) |
| `format-email` | `exhausted` | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` (`format-scalar-bodies`) |
| `format-hostname` | `exhausted` | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` (`format-scalar-bodies`) |
| `format-idn-hostname` | `exhausted` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` (`format-scalar-bodies`) |
| `format-ipv4` | `exhausted` | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` (`format-scalar-bodies`) |
| `format-iri` | `exhausted` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` (`format-scalar-bodies`) |
| `format-json-pointer` | `exhausted` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` (`format-scalar-bodies`) |
| `format-password` | `exhausted` | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` (`format-scalar-bodies`) |
| `format-regex` | `exhausted` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` (`format-scalar-bodies`) |
| `format-time` | `exhausted` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` (`format-scalar-bodies`) |
| `format-uri` | `exhausted` | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` (`format-scalar-bodies`) |
| `format-uri-reference` | `exhausted` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` (`format-scalar-bodies`) |
| `format-uri-template` | `exhausted` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` (`format-scalar-bodies`) |
| `inheritance-discriminated-union` | `exhausted` | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` (`nested-array-discriminated-unions`) |
| `oneof-anyof-variant` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = variant\.one_of\.as_ref\(\)\.or\(variant\.any_of\.as_ref\(\)\) \{]` (`inline-oneof-variants`) |
| `oneof-array-variant-anyof-item` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = item.one_of]` (`inline-oneof-variants`) |
| `oneof-array-variant-closed-object-item` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[if item.reference.is_none\(\) && is_inline_struct\(item\) \{]` (`inline-oneof-variants`) |
| `oneof-closed-empty-object-variant` | `exhausted` | `src/ir.rs::InlineHoister::hoist_union_variant[^ {8}\{$]` (`inline-oneof-variants`) |
| `property-sole-anyof-closed-object-member` | `exhausted` | `src/ir.rs::InlineHoister::prop_type_ref[if members.len\(\) == 1 && is_inline_struct]` (`inline-property-unions`) |
| `property-sole-anyof-struct-member` | `exhausted` | `src/ir.rs::InlineHoister::prop_type_ref[if members.len\(\) == 1 && is_inline_struct]` (`inline-property-unions`) |
| `ref-pointer-composition-index` | `exhausted` | `src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` (`composition-index-pointer`) |
| `ref-pointer-composition-index` | `exhausted` | `src/ir.rs::resolve_schema_pointer[^\s*"allOf" => \{]` (`ref-pointer-walk`) |
| `ref-pointer-composition-index` | `exhausted` | `src/ir.rs::resolve_schema_pointer[^\s*"anyOf" => \{]` (`ref-pointer-walk`) |
| `ref-pointer-composition-index` | `exhausted` | `src/ir.rs::resolve_schema_pointer[^\s*"oneOf" => \{]` (`ref-pointer-walk`) |
| `ref-pointer-nested-items` | `exhausted` | `src/ir.rs::ref_to_class["items" => \{]` (`ref-pointer-walk`) |
| `ref-pointer-nested-items` | `exhausted` | `src/ir.rs::resolve_schema_pointer[^\s*"items" => \{]` (`ref-pointer-walk`) |
| `ref-pointer-nested-properties` | `exhausted` | `src/ir.rs::ref_to_class["properties" if index]` (`ref-pointer-walk`) |
| `ref-pointer-nested-properties` | `exhausted` | `src/ir.rs::resolve_schema_pointer[^\s*"properties" => \{]` (`ref-pointer-walk`) |
| `annotated-ref-target-inheritance-union` | `exhausted` | feature row (`glaze-ledger-coats`); 0 declarers in every population read |

## Rows the frozen redo contract owns

The [frozen witness-search-redo contract](../witness-search-redo/contract.md) owns these keys, and its reconciler requires each row's `search:` link to name the key's line in [`../schemas.md`](../schemas.md#witness-search-exhaustive), so their covers keep that citation. This search read them too:

| key | contract verdict | declarers here |
|---|---|---|
| `annotated-ref-target-string-const` | exhausted | 0 |
| `array-item-inheritance-union` | search-incomplete | 0 |
| `array-item-pointer-walk-oneof` | search-incomplete | 1 github-code-search |
| `oneof-array-variant-annotated-ref-item` | exhausted | 0 |
| `oneof-array-variant-anyof-discriminated-union-item` | exhausted | 0 |
| `oneof-array-variant-anyof-nullable-item` | exhausted | 1 github-code-search |
| `oneof-bare-object-example-variant` | exhausted | 9 github-code-search |
| `property-sole-anyof-composed-member` | search-incomplete | 0 |
| `property-sole-anyof-empty-object-member` | search-incomplete | 0 |
| `property-sole-oneof-composed-member` | search-incomplete | 1 sourcegraph |
| `property-sole-oneof-empty-object-member` | search-incomplete | 0 |

## Renewed search

What became of every target this search left open: no declarer in the populations read is registrable yet. `none-registrable` means none was established within this bound, not that the world holds none.

| key | result | why |
|---|---|---|
| `allof-base-in-cycle-imported-after-class` | `none-registrable` | the other declarers' screens are outstanding |
| `allof-child-of-cyclic-base-imports-base-deferred` | `none-registrable` | the other declarers' screens are outstanding |
| `allof-enum-ref-narrowed-by-scalar-member` | `none-registrable` | the other declarers' screens are outstanding |
| `allof-extends-oneof-object-refused` | `none-registrable` | the other declarers' screens are outstanding |
| `allof-overlapping-ref-parents-flattened` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `allof-single-ref-empty-properties-alias` | `none-registrable` | the other declarers' screens are outstanding |
| `allof-union-branch-not-schema-overrides-property` | `none-registrable` | the other declarers' screens are outstanding |
| `anyof-array-variant-inline-const-item` | `none-registrable` | the other declarers' screens are outstanding |
| `bigint-format-string-typed-str` | `none-registrable` | no declarer in the populations read |
| `combo-allof-nullable` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `combo-annotated-ref-property-example` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `combo-anyof-beside-properties` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `combo-oneof-beside-properties` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `combo-oneof-schema-example` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `component-same-primitive-union` | `none-registrable` | the other declarers' screens are outstanding |
| `discriminated-variant-date-value-snippet` | `none-registrable` | no declarer in the populations read |
| `enum-value-description-extension-dropped` | `none-registrable` | the other declarers' screens are outstanding |
| `forward-refs-omit-hoisted-variant-models` | `none-registrable` | no declarer in the populations read |
| `ignore-extension-on-property-kept` | `none-registrable` | the other declarers' screens are outstanding |
| `integer-example-beyond-double-precision` | `none-registrable` | the other declarers' screens are outstanding |
| `integer-format-fallback` | `none-registrable` | the other declarers' screens are outstanding |
| `literal-enum-value-quote-escaping` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `literal-example-dollar-escaped-in-docstring` | `none-registrable` | the other declarers' screens are outstanding |
| `literal-type-extension-ignored` | `none-registrable` | no declarer in the populations read |
| `nullable-anyof-member-description-dropped` | `none-registrable` | the other declarers' screens are outstanding |
| `nullable-single-allof-ref-component-not-optional` | `none-registrable` | the other declarers' screens are outstanding |
| `number-format-uint64-typed-int` | `none-registrable` | the other declarers' screens are outstanding |
| `oneof-array-variant-inline-const-item` | `none-registrable` | no declarer in the populations read |
| `oneof-array-variant-inline-enum-item` | `none-registrable` | the other declarers' screens are outstanding |
| `oneof-duplicate-members-collapsed` | `none-registrable` | the other declarers' screens are outstanding |
| `oneof-map-variant-anyof-value` | `none-registrable` | no declarer in the populations read |
| `property-anyof-sole-string-enum-member` | `none-registrable` | the other declarers' screens are outstanding |
| `property-oneof-sole-string-enum-member` | `none-registrable` | the other declarers' screens are outstanding |
| `property-ref-to-nullable-component-annotation` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `ref-into-component-response-schema-named-by-last-segment` | `none-registrable` | the other declarers' screens are outstanding |
| `ref-with-nullable-sibling-made-optional` | `none-registrable` | the other declarers' screens are outstanding |
| `reference-literal-single-quote-escaped` | `none-registrable` | the other declarers' screens are outstanding |
| `remote-document-local-pointer-resolved-against-root` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `remote-ref-at-use-site-inlined` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `request-body-property-closed-empty-object` | `none-registrable` | the other declarers' screens are outstanding |
| `schema-example-array-null-element` | `none-registrable` | the other declarers' screens are outstanding |
| `schema-example-null` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv); the other declarers' screens are outstanding |
| `schema-example-temporal-duplicate-element` | `none-registrable` | no declarer in the populations read |
| `schema-example-union-ref-sentinel` | `none-registrable` | no declarer in the populations read |
| `schema-name-builtin-complex` | `none-registrable` | the other declarers' screens are outstanding |
| `schema-sdk-group-name` | `none-registrable` | the other declarers' screens are outstanding |
| `schema-type-name-inline-property` | `none-registrable` | the registered declarers do not carry the complete trigger (census.tsv) |
| `schema-x-tags` | `none-registrable` | the other declarers' screens are outstanding |
| `string-json-format-typed-any` | `none-registrable` | the other declarers' screens are outstanding |
| `undiscriminated-ref-oneof-sibling-properties-dropped` | `none-registrable` | the other declarers' screens are outstanding |
| `union-of-enum-ref-const-and-string-members` | `none-registrable` | no declarer in the populations read |
| `union-of-two-enum-refs-alias` | `none-registrable` | the other declarers' screens are outstanding |
| `variant-nullable-value-optional-default-none` | `none-registrable` | the other declarers' screens are outstanding |
| `additional-properties-schema` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `allof` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `anyof-map-variant-anyof-value` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `anyof-map-variant-oneof-value` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `discriminator-mapping` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `enum` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `format-binary` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `format-byte` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `format-date` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `format-int64` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `format-uuid` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `nullable` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `oneof` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `oneof-anyof-variant` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `oneof-discriminated-union` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `oneof-map-variant-oneof-value` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `oneof-sole-non-null-member` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `oneof-string-const-variant` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `property-map-value-oneof` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `property-oneof-residual` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `ref-pointer-undeclared-component-head` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `schema-example-outside-enum` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `type-single` | `none-registrable` | no probed declarer of an open arm is registered; the named candidates' certified-pair screens and the unprobed declarers are outstanding |
| `anyof-array-variant-inline-enum-item` | `none-registrable` | no real specification executes the `InlineHoister::hoist_union_variant` site |
