# Search for the schema shape arms

## Search scope

The committed vendored source inventory in
`tests/fixtures/corpus-sources.tsv` was parsed as OpenAPI objects and searched
for each exact trigger below. The six pinned public documents in
`docs/fern-measurements/blocked-witnesses/witnesses.tsv` were also measured with
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
| `allof` | `src/openapi.rs::collapse_sole_composition_member[=None => match sole_ref\(\) \{]` | JSON body allOf of one component ref with sibling title, description or default; speech-ai and vocode | `search-incomplete` | `none-registrable` |
| `allof` | `src/ir.rs::InlineHoister::prop_type_ref[if let Some\(reference\) = annotated_sole_all_of_ref\(prop_schema\)]` | defaulted one-member allOf ref property in a flattened discriminated union variant; vocode | `search-incomplete` | `none-registrable` |
| `allof` | `src/ir.rs::append_member_fields[=\} else if is_inline_struct\(prop_schema\) && annotated_sole_all_of_ref]` | defaulted one-member allOf ref property in a flattened discriminated union variant; vocode | `search-incomplete` | `none-registrable` |
| `oneof-anyof-variant` | `src/ir.rs::InlineHoister::prop_type_ref[=return self.prop_type_ref\(parent\x2c prop\x2c &union\);]` | const anyOf inside a nullable inline property anyOf; rice-shower | `search-incomplete` | `none-registrable` |
| `oneof-anyof-variant` | `src/ir.rs::InlineHoister::hoist_union_variant[if item.reference.is_none\(\) && string_enum_values\(item\).is_some\(\)]` | array of inline enum beside another non-null member of a property union; langchain | `search-incomplete` | `none-registrable` |
| `oneof-anyof-variant` | `src/ir.rs::Builder::field_type_ref[=\.then\(\x7c\x7c string_enum_values\(items\)\)]` | array of inline enum beside another non-null member of a property union; langchain | `search-incomplete` | `none-registrable` |
| `nullable` | `src/ir.rs::Builder::variant_ref[=return if variant.nullable == Some\(true\) \{]` | nullable anyOf member hoisted within an outer union; supabase | `search-incomplete` | `none-registrable` |
| `media-type-form-urlencoded` | `src/ir.rs::hoist_form_object[=field.type_ref.clone\(\)]` | referenced urlencoded component with an inline enum property; supabase | `search-incomplete` | `none-registrable` |
| `response-content` | `src/ir.rs::hoist_error_body_types[=\.find\(\x7c\(media_type\x2c _\)\x7c is_json_like_media_type\(media_type\)\)]` | referenced component response whose inline object uses application/problem+json; kompaz | `search-incomplete` | `none-registrable` |
