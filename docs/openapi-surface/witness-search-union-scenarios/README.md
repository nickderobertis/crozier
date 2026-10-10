# Witness search for fifteen union shapes

The real-specification search behind the union repairs of
`src/ir.rs::Builder::discriminated_union`, `variant_ref`, `field_type_ref`,
`add_named`, `InlineHoister` and `build_endpoint`, the two union extensions of
`src/openapi.rs`, and the union refusals of
`src/document_refusals/type_not_defined.rs` and `src/name_refusals.rs`. Each
shape is named below by its scenario id. A shape this search found in a
registrable document is registered in
[`../../../tests/fixtures/CORPUS.md`](../../../tests/fixtures/CORPUS.md); a shape
it did not is proven by an independently written fixture under
[`../handwritten/`](../handwritten/AGENTS.md) whose cover cites this record,
which is both its search record and its renewed search.

## What was searched

**APIs.guru.** The `openapi-directory` archive at
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, fetched once through the raw lane of
`tools/witness-search/rate_limit_guard.py` (SHA-256
`7a0bdff93afc94d373c7e596d24739cc8aff7d93c4e8b75a82e9c0cf7e0606a1`, the digest
[`../witness-search-apis.guru/acquisitions.jsonl`](../witness-search-apis.guru/acquisitions.jsonl)
already records): 4,138 JSON and YAML entries, of which 1,927 parse as OpenAPI
3 documents.

**The acquired pools.** The 9,258 documents the GitHub REST code-search and
Sourcegraph public-document acquisitions left in this checkout's search cache
(`.local/golden-reach-search/`), each named by its repository, path and pinned
commit: 7,664 parse as OpenAPI 3 documents. No new search endpoint was queried.
Purpose-written tool examples are excluded from admission.

Every document was read once by one detector per shape, each written from the
shape's trigger and checked to fire on its own fixture and on no other:

| shape | what a declarer writes |
|---|---|
| `discriminated-false-extension-ignored` | `x-fern-discriminated: false` or `x-crozier-discriminated: false` beside a `oneOf` or `anyOf` |
| `discriminator-mapping-unresolved-members` | a component `oneOf` of two or more `$ref`s with a `discriminator.mapping`, every member and target naming a `#/components/schemas/` entry the document does not declare |
| `discriminator-property-rename-extension-refused` | `x-fern-property-name` or `x-crozier-property-name` on the `discriminator` of a `oneOf` or `anyOf` |
| `get-request-body-union-member-refused` | a `GET` operation whose JSON body is a `$ref` to a member of a component union whose members all tag one property with a single string value |
| `inline-oneof-discriminator-without-tag-values` | a property `oneOf` of two or more inline objects with a `discriminator` that maps nothing, no member giving its property an `enum` or `const` |
| `map-value-union-not-hoisted` | an inline request-body property union with an inline member whose `additionalProperties` is a `oneOf` or `anyOf` of two or more non-null members |
| `nested-oneof-mapping-target-wrapped-as-value` | a component union whose `discriminator.mapping` names a schema that is itself a `oneOf` or `anyOf` of two or more `$ref`s and declares no properties |
| `nullable-single-inline-object-oneof-component` | a component `oneOf` or `anyOf` of exactly one inline object with `required` properties and `{type: "null"}` |
| `nullable-union-component-optional-on-last-member` | an OpenAPI 3.0 component with `nullable: true` beside a `oneOf` or `anyOf` of two or more plain scalars |
| `oneof-sibling-properties-base-class` | a component union of two or more inline objects tagged by a shared one-value property, with sibling `properties` of its own |
| `single-member-oneof-response-hoisted` | an inline 2xx JSON response schema whose `oneOf` or `anyOf` holds exactly one `$ref` |
| `titled-inline-object-array-item-union-members-any` | an inline request-body array property whose `items` is a `oneOf` of two or more inline `type: object` members, each titled and requiring nothing |
| `union-member-nullability-dropped` | an OpenAPI 3.0 component `oneOf` or `anyOf` with a plain scalar member carrying `nullable: true` |
| `union-null-member-typed-any` | an inline 2xx JSON response schema whose `oneOf` or `anyOf` holds two or more non-null members and `{type: "null"}` |

The refusal shape `explicit-discriminator-members-lack-property` is a document
fault Fern refuses, so it is settled by its registry class rather than a
witness; see [`../../fern-refusals/type-not-defined/evaluation.md`](../../fern-refusals/type-not-defined/evaluation.md).

## Every declarer, and what became of it

Seven shapes have declarers: 78 distinct documents in all, each screened in
[`screens.tsv`](screens.tsv) on the certified pair (Fern CLI 5.67.1,
`fernapi/fern-python-sdk` 5.20.0, Python enums, package `fern`) and then on
crozier's complete tree through `src/parity.rs`. A declarer the pair refuses,
or on which crozier differs from Fern or refuses apart from the shape, cannot
be registered as a byte-matched golden; the licence screen
([`../../corpus-licensing.md`](../../corpus-licensing.md)) was taken only for a
declarer that came out byte-equal.

- `single-member-oneof-response-hoisted`: 15 declarers. Input Output's token
  metadata server API at `input-output-hk/offchain-metadata-tools@91eba72d6e5e3b17cd49f625c9546f2c82df5a65`
  (Apache-2.0 in the repository's `LICENSE`) byte-matches after two repairs and
  is **registered as corpus row 1200**; its four earlier versions at the same
  commit match too and are not registered beside it. Every other declarer is
  refused by the pair or differs apart from the shape.
- `union-member-nullability-dropped`: 17 declarers. Waylay's
  `queries.transformed.openapi.yaml` declares the component shape exactly and
  crozier's `Datum` now matches Fern's, but the document's aggregation unions
  carry nullable array and map members crozier lowers differently; Grafikart's
  `filemanager-element` differs in a multipart union field and an inline
  request union's members. The rest are refused or differ more widely.
- `nullable-union-component-optional-on-last-member` (11),
  `nullable-single-inline-object-oneof-component` (5),
  `nested-oneof-mapping-target-wrapped-as-value` (3),
  `map-value-union-not-hoisted` (1) and `oneof-sibling-properties-base-class`
  (28): every declarer is refused by the pair, refused by crozier on another
  shape, or differs from Fern apart from the shape.

The other seven shapes have no declarer in either population.

**The map-member arm, read as census conjunctions.** The repair for
`map-value-union-not-hoisted` is `hoist_union_variant`'s cases 14a to 14d: an
`object` member declaring no properties whose `additionalProperties` holds an
inline `oneOf` (14a, 14c) or `anyOf` (14b, 14d) of two or more non-`null`
members, under a `oneOf` head (14a, 14b) or an `anyOf` head (14c, 14d). The
census counted each over the same two populations (13,234 documents read, 174
unreadable). The `anyOf`-head pair needs no search: registered sources already
declare both (`hasura-metadata`; `deepsearch-ds-v2`, `opencodeui`,
`waylay-queries`), on component unions the inline arm never sees. Case 14b has
no declarer. Case 14a has eight: the subsloth project's media API contract
(`knirski/subsloth@b4acb8e87ee47a4154f40c431b7c91d8d27d1b64`, Apache-2.0 in the
repository's `LICENSE`) is byte-equal and **registered as corpus row 1201**;
`roe-ai/roe-python` differs from Fern apart from the shape, and the other six
are refused by the pair. Every one is in [`screens.tsv`](screens.tsv).

## Witness search

The search is **search-incomplete**: it covers APIs.guru and the acquired pools,
not every public API description, so it is no claim that none exists. The
renewed search above found nothing registrable for any key below.

The feature-level keys:

| key | verdict | shape | renewed outcome |
|---|---|---|---|
| `discriminated-extension` | `search-incomplete` | `discriminated-false-extension-ignored` | none-registrable |
| `discriminator-property-name-extension` | `search-incomplete` | `discriminator-property-rename-extension-refused` | none-registrable |
| `get-request-body-union-member` | `search-incomplete` | `get-request-body-union-member-refused` | none-registrable |
| `oneof-map-variant-anyof-value` | `search-incomplete` | `map-value-union-not-hoisted` | none-registrable |

The arm-level keys, each a handling site of a `golden` row that no registered
golden reaches (the last three rows' witnesses, rows 1201, 305, 194, 196 and
329 among them, declare their shape on component unions, which lower through
the component builder instead):

| key | verdict | arm | shape | renewed outcome |
|---|---|---|---|---|
| `nullable` | `search-incomplete` | `src/ir.rs::Builder::variant_ref[if is_plain_scalar\(variant\) && variant\.nullable == Some\(true\)]` | `union-member-nullability-dropped` | none-registrable |
| `nullable` | `search-incomplete` | `src/ir.rs::Builder::add_named[\(false, _\) if variants\.iter\(\)\.all\(is_plain_scalar\) => \{]` | `nullable-union-component-optional-on-last-member` | none-registrable |
| `oneof` | `search-incomplete` | `src/ir.rs::build_endpoint[Some\(if dropped_null \{]` | `union-null-member-typed-any` | none-registrable |
| `property-oneof-residual` | `search-incomplete` | `src/ir.rs::untagged_inline_discriminator[if untagged \{]` | `inline-oneof-discriminator-without-tag-values` | none-registrable |
| `additional-properties-schema` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `map-value-union-not-hoisted` | none-registrable |
| `discriminator-mapping` | `search-incomplete` | `src/ir.rs::Builder::discriminated_union[if union_target \{]` | `nested-oneof-mapping-target-wrapped-as-value` | none-registrable |
| `discriminator-mapping` | `search-incomplete` | `src/emit.rs::ExampleCtx::named_value_inner[Some\(m\) if m\.wrapped => \{]` | `nested-oneof-mapping-target-wrapped-as-value` | none-registrable |
| `oneof-sole-non-null-member` | `search-incomplete` | `src/ir.rs::Builder::add_named[if variants\.len\(\) > 1 && is_inline_object\(only\)]` | `nullable-single-inline-object-oneof-component` | none-registrable |
| `oneof-discriminated-union` | `search-incomplete` | `src/ir.rs::Builder::discriminated_union[if !schema\.properties\.is_empty\(\)]` | `oneof-sibling-properties-base-class` | none-registrable |
| `items-oneof-element` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_array_item_type[if member\.title\.is_some\(\)$]` | `titled-inline-object-array-item-union-members-any` | none-registrable |
| `ref-pointer-undeclared-component-head` | `search-incomplete` | `src/ir.rs::Builder::discriminated_union[if all_dangling \{]` | `discriminator-mapping-unresolved-members` | none-registrable |
| `oneof-map-variant-oneof-value` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `map-value-union-not-hoisted` | none-registrable |
| `anyof-map-variant-oneof-value` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `map-value-union-not-hoisted` | none-registrable |
| `anyof-map-variant-anyof-value` | `search-incomplete` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `map-value-union-not-hoisted` | none-registrable |

`single-member-oneof-response-hoisted`'s two sites,
`src/ir.rs::build_endpoint[Some\(schema\) if sole_reference_member\(schema\)\.is_some\(\) => \{]`
under `oneof-sole-member` and
`src/ir.rs::InlineHoister::hoist_array_item_type[if let Some\(reference\) = sole_reference_member\(item_schema\) \{]`
under `anyof-sole-member`, are reached by corpus row 1200 and need no fixture.
