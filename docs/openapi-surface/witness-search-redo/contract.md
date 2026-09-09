# Witness-search redo contract

This additive contract is not an outcome ledger. The two shards collect corresponding
content, while [`../schemas.md`](../schemas.md) remains the sole owner of final outcomes.
Until reconciliation is explicitly enabled, an empty records table is valid and is
invisible to every existing outcome reader.

The `catalogue-portals` shard exclusively owns `apis.guru`, `jentic`, and
`vendor-portals`. The `code-platforms` shard exclusively owns `sourcegraph`,
`github-code-search`, `swaggerhub`, and `postman`. An authoritative reconciliation
requires one record for every key/source pair. Every record has exactly these fields:
`key`, `selector`, `source`, `query`, `result`, `candidates`, `provenance`,
`licence-screen`, and `fern-screen`. `query` is the exact rerunnable query in a code
span. `result` is a nonnegative integer or `unanswered`; an unanswered source is never
written as zero. A positive result requires candidates, immutable provenance, and both
screens. Zero and `unanswered` require all four supporting fields to be `—`.

Only all seven answered sources, each returning zero, permits `none-found`. Any
`unanswered` source requires `search-incomplete`; otherwise a nonzero result requires
`witness-found`. The reconciliation entry point is
`scripts/witness-search-redo.py CONTRACT SHARD SHARD --reconcile --schemas docs/openapi-surface/schemas.md`.
It reads exactly one authoritative eight-cell table row per owned key. That same row
must contain the words `search outcome` followed by the outcome in a code span, plus
all seven bold source-family names, each followed by its exact query in a code span,
an arrow, and its count or `unanswered`. The query and result must equal the
corresponding shard record. Facts on another row cannot satisfy it.

## Owned keys

| key | selector |
|---|---|
| `annotated-ref-target-closed-object` | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.additionalProperties=false` |
| `annotated-ref-target-composed` | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.allOf` |
| `annotated-ref-target-oneof` | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.oneOf` |
| `annotated-ref-target-string-const` | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.const:string-valued` |
| `anyof-array-variant-anyof-nullable-item` | `schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member` |
| `anyof-array-variant-closed-object-item` | `schema.anyOf>schema.type:primary=array&schema.items>schema.additionalProperties=false` |
| `anyof-array-variant-empty-object-item` | `schema.anyOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| `anyof-array-variant-oneof-nullable-item` | `schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member` |
| `anyof-array-variant-struct-item` | `schema.anyOf>schema.type:primary=array&schema.items>schema.properties:non-empty` |
| `anyof-sole-member` | `schema.anyOf:sole-member` |
| `array-item-inheritance-union` | `schema.items>schema.discriminator:inheritance-union` |
| `array-item-pointer-walk-anyof` | `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=anyOf` |
| `array-item-pointer-walk-oneof` | `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=oneOf` |
| `oneof-array-variant-annotated-ref-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component` |
| `oneof-array-variant-anyof-discriminated-union-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union` |
| `oneof-array-variant-anyof-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf` |
| `oneof-array-variant-anyof-nullable-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member` |
| `oneof-array-variant-closed-object-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.additionalProperties=false` |
| `oneof-array-variant-composed-item` | `schema.oneOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf` |
| `oneof-array-variant-empty-object-item` | `schema.oneOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| `oneof-bare-object-example-variant` | `schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&!schema.example:schema-shaped&!schema.properties:non-empty&schema.example=object&schema.type:primary=object` |
| `property-sole-anyof-closed-object-member` | `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.additionalProperties=false` |
| `property-sole-anyof-composed-member` | `schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf` |
| `property-sole-anyof-empty-object-member` | `schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| `property-sole-anyof-struct-member` | `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.properties:non-empty` |
| `property-sole-oneof-closed-object-member` | `schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.additionalProperties=false` |
| `property-sole-oneof-composed-member` | `schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.type:primary-scalar&schema.allOf` |
| `property-sole-oneof-empty-object-member` | `schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| `ref-pointer-undeclared-component-head` | `schema.$ref:undeclared-component-head` |
| `ref-pointer-unnamed-segment` | `schema.$ref:unnamed-segment` |
