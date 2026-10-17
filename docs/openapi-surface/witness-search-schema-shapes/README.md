# Search for the schema shape arms

## Search scope

The committed vendored source inventory in
`tests/fixtures/corpus-sources.tsv` was parsed as OpenAPI objects and searched
for each exact trigger below. The six pinned public documents in
`docs/fern-measurements/blocked-witnesses/witnesses.tsv` and its README's retired
Vocode source were also measured with
Fern CLI 5.67.1 and Python SDK 5.20.0. No new acquisition was made.
This is a bounded search, so its verdict is search-incomplete.

The registered controls are deepsearch-ds-v2 (array enum beside null rather
than another non-null alternative), embedpdf-cloudpdf (a nullable allOf
wrapper), flowdapt and openfoodfacts-taxonomy-editor (ordinary component
properties rather than flattened discriminator variants). Their complete
existing goldens remain controls. None declares these exact arms. Box declares
the referenced urlencoded enum, but its source has no golden: CORPUS.md records
its failed Fern validation. AGCO and Swagger Petstore offer JSON alongside the
form representation, so their selected request never enters the form arm. The real
declarers below still have other residuals or have not been registered, so
none is a registrable proof in this search. Purpose-written fixtures provide
arm evidence only; they do not become corpus rows or change the scenario plan.

## Witness search

| key | arm | trigger and measured public declarer | verdict | renewed result |
|---|---|---|---|---|
| `allof` | `src/openapi.rs::collapse_sole_composition_member[=Some\(member\) => \(member\x2c true\)]` | JSON body allOf of one component ref with sibling title, description or default; speech-ai and vocode | `search-incomplete` | `none-registrable` |
| `allof` | `src/ir.rs::InlineHoister::prop_type_ref[=^ {12}return TypeRef::Named\(ref_to_class\(reference\)\);]` | defaulted one-member allOf ref property in a flattened discriminated union variant; vocode | `search-incomplete` | `none-registrable` |
| `allof` | `src/ir.rs::append_member_fields[=^ {12}base_type_ref\(prop_schema\)$]` | defaulted one-member allOf ref property in a flattened discriminated union variant; vocode | `search-incomplete` | `none-registrable` |
| `oneof-anyof-variant` | `src/ir.rs::InlineHoister::prop_type_ref[=return self.prop_type_ref\(parent\x2c prop\x2c &union\);]` | const anyOf inside a nullable inline property anyOf; rice-shower | `search-incomplete` | `none-registrable` |
| `oneof-array-variant-inline-enum-item` | — | inline string enum array item beside another non-null member of a property `oneOf`; no registered or measured public declarer | `search-incomplete` | `none-registrable` |
| `anyof-array-variant-inline-enum-item` | — | inline string enum array item beside another non-null member of a property `anyOf`; langchain `stream_mode`. deepsearch-ds-v2's two selector matches pair the array with `null`, so the earlier nullable arm takes them and golden-reach measures this arm's `return list;` site unreached | `search-incomplete` | `none-registrable` |
| `oneof-array-variant-inline-const-item` | — | inline string const array item beside another non-null member of a property `oneOf`; no registered or measured public declarer | `search-incomplete` | `none-registrable` |
| `anyof-array-variant-inline-const-item` | — | inline string const array item beside another non-null member of a property `anyOf`; no registered or measured public declarer | `search-incomplete` | `none-registrable` |
| `oneof-anyof-variant` | `src/ir.rs::Builder::field_type_ref[=(?<=\.map\(\x7cvalues\x7c )\(items\x2c values\)]` | array of inline enum beside another non-null member of a property union; langchain | `search-incomplete` | `none-registrable` |
| `nullable` | `src/ir.rs::Builder::variant_ref[=optional_type_ref\(composed\)]` | nullable anyOf member hoisted within an outer union; supabase | `search-incomplete` | `none-registrable` |
| `media-type-form-urlencoded` | `src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | referenced urlencoded component with an inline enum property; supabase | `search-incomplete` | `none-registrable` |
| `response-content` | `src/ir.rs::hoist_error_body_types[=\.map\(\x7c\(_\x2c media\)\x7c media\)]` | referenced component response whose inline object uses application/problem+json; kompaz | `search-incomplete` | `none-registrable` |

## Success-counter anchors

The fresh measurement at `43760d0bf062`, over the source merged with main,
supersedes condition-only anchors.
The one-member body anchor now selects the successful `Some(member)` match arm;
the variant property anchor selects its referenced-type return; the flattened
field anchor selects its fallback conversion; the inline array anchor selects
its enum-list return; and nullable nested composition selects its optional
wrapper. The Builder array anchor starts at the tuple body `(items, values)`
after an enum lookup succeeds, excluding the method-call counter that executes
even when the lookup returns no values.

| handling path | source counter starts (line:column) |
|---|---|
| `collapse_sole_composition_member`: successful allOf member | `4187:18`, `4187:29` |
| `InlineHoister::prop_type_ref`: annotated reference return | `7703:20` |
| `append_member_fields`: fallback type conversion | `10776:13`, `10776:27` |
| `InlineHoister::hoist_union_variant`: hoisted enum list return | `7337:32` |
| `Builder::field_type_ref`: successful enum lookup tuple | `13354:60`, `13354:67` |
| `Builder::variant_ref`: optional composed member | `13682:21`, `13682:39` |
| `hoist_error_body_types`: JSON-suffix media map | `5759:30` |

The last map has no separate successful-result counter. Registered goldens
reach its media-selection call and the flattened field fallback, superseding
those covers. The registered redocly.com-museum golden answers its shared
`400`, `401` and `404` component responses with `application/problem+json`
alone, so its referenced `Error` body passes through this map and hoists no
`{Class}Body`; `problem_json_component_responses_match_registered_museum_golden`
compares that complete tree bidirectionally and fails both an over-hoisted
body model and a retyped error body. Suffix reach does not establish the exact problem-media object
shape: its complete two-mode regression remains at
[`schema-shapes/kiln-problem-response`](../../fern-measurements/schema-shapes/kiln-problem-response/).
The other fixtures retain only covers for successful arms no registered golden
reaches; these coordinates describe the measured source, not stable line IDs.

The hoisted enum list return is now the `hoist_union_variant` case-analysis
branch of four region rows (cases 3e to 3h), not a `oneof-anyof-variant` site.
Golden-reach measures it unreached, so each row is `handwritten`:
kiln-array-mode covers `anyof-array-variant-inline-enum-item`, and
kiln-array-variants covers the `oneOf` enum, `oneOf` const and `anyOf` const rows.
