# Bounded continuation of the schema witness search

Base: `92be4edfa6378d3e509c775f8f9796de40cb9b54`. [`targets.tsv`](targets.tsv)
freezes all 124 targets: 51 feature/supplement rows and 73 distinct arm
covers in the schemas region. Duplicate covers of one arm count once. The
remote-document supplement is covered by the existing loopback journey.
This continuation makes no new GitHub code search and changes no generated output.

## Populations screened

1. The [previous search](../witness-search-fixture-only-schemas/README.md)'s named,
   ungenerated candidates: [`previously-unscreened.tsv`](previously-unscreened.tsv)
   plus [`arm-unscreened.tsv`](arm-unscreened.tsv). Historical timeouts and refusals
   are unscreened, rather than current certified-pair refusals (manager ruling 275).
   The two files retain all 15,553 candidate-target entries and their immutable
   revisions and digests, representing 2,459 distinct byte strings.
2. Exactly the seven [newly admitted documents](../../fern-measurements/handed-off/README.md#newly-admitted-documents).
   [`newly-admitted.tsv`](newly-admitted.tsv) lists the committed sources, smallest
   first; all seven SHA-256 values were verified against the handed-off pins.
   [`selector-prefilters.tsv`](selector-prefilters.tsv) records native census
   counts, including zeroes, for every target key.
   [`newly-admitted-shape-screen.tsv`](newly-admitted-shape-screen.tsv) records
   every target/document decision and the rejected complete trigger. A broad selector is only a
   necessary condition; the previous search's complete-trigger detector and the
   handling path must also apply. None provides a new remaining target witness.
   The formerly declared description, nullable-member, closed-object and sole
   nullable-object targets have already been settled on this base; they are
   excluded from the frozen target set.

Ranking covers the 1,026 retained byte strings only. The 1,433 without retained
bytes are named individually in [`retained-availability.tsv`](retained-availability.tsv),
with the reason **not ranked: bytes not retained locally, fetch needed**; the 43
historical registered source paths that moved are not chased. This is manager
ruling 278, rather than a claim that the missing documents are larger.
Previously measured documents in the handed-off record are not rescreened
(ruling 275). Every remaining target takes at most three smallest admissible
retained candidates, round-robin by round then key and arm; shared byte strings
reuse one certified generation. [`selection.tsv`](selection.tsv) fixes that order.
The mutable remote reference in the STAC source is corpus-refused without
fetching its mutable dependency (ruling 280).

## Certified comparisons

The certified pair is read from `assets/scaffolding/metadata.json`: CLI 5.163.1
and Python generator 5.41.3. Every new generation uses
`tools/fern-goldens/generate-fern-fixture.sh schemas-continuation-screen 5.41.3 <spec>`
under the shared Fern lock, one at a time, with temporary workspaces outside
the checkout and `GIT_CEILING_DIRECTORIES` set. Shared certified-tree entries
are immutable, verified by document SHA-256, and installed by sibling rename.
Manager ruling 277 authorizes this route instead of `just witness-screen`:
that legacy command does not support this record or reuse the shared tree cache.
Licence readings come from the previous committed screens; no new licence fetch
is made. `crozier compare` uses package-name `fern` and project-name
`default_package_name`, all catalogued departures, and the untouched certified
cache tree as its reference. [`screens.tsv`](screens.tsv) records each result;
[`screens/`](screens/) retains generation and comparison diagnostics.

Agentset's `document.properties` meets the older broad nullable-member detector,
but its component takes Builder's path: both `DocumentProperties` and the parent
field retain the member description. It does not execute the InlineHoister path
whose inline response field drops that description. Its whole-tree byte-match
is **byte-match-without-target-behavior**, one screen and no new witness
(manager ruling 281). The authored cover therefore remains.

Isaacus also byte-matches whole, but removing all nine null-first schema
examples changes none of crozier's 127 files. The seven response-only fields
and two optional request fields therefore supply no output-sensitive witness
for the residual null-argument-absence target (manager ruling 282).
[`isaacus-removal.json`](isaacus-removal.json) records every removed path
and the empty whole-tree diff. No authored cover is superseded.

TopHat's `usersMe.user` is required with a nullable reference sibling, but both
SDKs emit required `user: Users`. The existing `required-marker-point` cover
also emits required `point: Point`. This is byte-match-without-target-behavior,
not proof of the made-optional target; its stale name is handed off for audit
(manager ruling 284), without changing a shared key or registering it here.
Spotto likewise emits its required nullable-reference fields (for example
`GetAssetsResponse.query` and `GetAssetLastLocationResponse.lastLocation`) as
required non-optional fields; it supplies no made-optional witness either.

DomainTools and Open-EO exit 0 but log `Failed to parse openapi document` and
emit only 35 scaffold files. They are certified-pair refusals, not successful
SDK generations or parity-gap evidence. Earlier provisional compare statuses
are superseded by this complete-log classification.

The later RS-PYTHON/rs-server revision also supplies no null-first-example
witness: removing both declarations changes none of its 231 crozier files.
[`rsserver-removal.json`](rsserver-removal.json) records the two paths and the
empty whole-tree diff, under the same sensitivity rule as Isaacus.

Eqivo matches the certified trees in both enum modes. Corpus row 5300 is now
registered; its promotion in the target ledger awaits scoped arm measurement.

## GitHub requests

No GitHub code search was made. No GitHub request was made outside the guard.
No live GitHub request was made at all. The guarded acquirer read 88 exact-commit
raw responses from the shared response cache; its own
[`github-cache-hits.jsonl`](guard-logs/github-cache-hits.jsonl) retains those hits.
There are no call or wait logs because neither occurred. Other retained files
were read locally by digest, not fetched. No GraphQL, Sourcegraph, Postman or
SwaggerHub route was used. Certified-tree reuse is not a response-cache hit.

| bucket | live requests | response-cache hits | waits |
|---|---:|---:|---:|
| code_search | 0 | 0 | 0 |
| core | 0 | 0 | 0 |
| raw candidate fetch | 0 | 88 | 0 |

## Verdicts

Current totals: 75 `exhausted`, 49
`search-incomplete`, no new registered witness. Exhaustion is restricted to
these two assigned populations; it makes no claim about previously truncated
search pages. [`census.tsv`](census.tsv) names every outstanding candidate for
each key and arm and gives its current reason beside its prior reading.
[`known-declarers.tsv`](known-declarers.tsv) keeps earlier measured differences
separate from candidates awaiting their first certified screen.

### Target 1: additional-properties-schema

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `additional-properties-schema` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `search-incomplete` | `none-registrable` | 1301 |

### Target 2: allof

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `allof` | arm | `src/ir.rs::Builder::add_object[if let Some\(branches\) = &parent\.one_of \{]` | `search-incomplete` | `none-registrable` | 1144 |

### Target 3: allof

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `allof` | arm | `src/ir.rs::Builder::field_type_ref[if let Some\(declaration\) = scalar_narrowed_enum_type\(]` | `search-incomplete` | `none-registrable` | 1144 |

### Target 4: allof

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `allof` | arm | `src/ir.rs::InlineHoister::prop_type_ref[=^ {12}return TypeRef::Named\(ref_to_class\(reference\)\);]` | `search-incomplete` | `none-registrable` | 1165 |

### Target 5: allof-base-in-cycle-imported-after-class

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `allof-base-in-cycle-imported-after-class` | feature | `-` | `search-incomplete` | `none-registrable` | 5 |

### Target 6: allof-child-of-cyclic-base-imports-base-deferred

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `allof-child-of-cyclic-base-imports-base-deferred` | feature | `-` | `search-incomplete` | `none-registrable` | 4 |

### Target 7: allof-enum-ref-narrowed-by-scalar-member

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `allof-enum-ref-narrowed-by-scalar-member` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 8: allof-extends-oneof-object-refused

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `allof-extends-oneof-object-refused` | feature | `-` | `search-incomplete` | `none-registrable` | 2 |

### Target 9: allof-overlapping-ref-parents-flattened

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `allof-overlapping-ref-parents-flattened` | feature | `-` | `search-incomplete` | `none-registrable` | 38 |

### Target 10: allof-union-branch-not-schema-overrides-property

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `allof-union-branch-not-schema-overrides-property` | feature | `-` | `search-incomplete` | `none-registrable` | 1 |

### Target 11: annotated-ref-shape

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `annotated-ref-shape` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[^ {20}\.map\(\x7c\(target, description\)\x7c]` | `exhausted` | `none-registrable` | 0 |

### Target 12: annotated-ref-target-anyof

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `annotated-ref-target-anyof` | arm | `src/ir.rs::InlineHoister::prop_type_ref[if target.one_of.is_some\(\)]` | `exhausted` | `none-registrable` | 0 |

### Target 13: annotated-ref-target-inheritance-union

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `annotated-ref-target-inheritance-union` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 14: annotated-ref-target-string-const

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `annotated-ref-target-string-const` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 15: anyof-allof-variant

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-allof-variant` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[^ {8}\{$]` | `exhausted` | `none-registrable` | 0 |

### Target 16: anyof-array-variant-annotated-ref-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-array-variant-annotated-ref-item` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[^ {20}\.map\(\x7c\(target, description\)\x7c]` | `exhausted` | `none-registrable` | 0 |

### Target 17: anyof-array-variant-anyof-nullable-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-array-variant-anyof-nullable-item` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[simple_nullable_member\(item\) \{]` | `exhausted` | `none-registrable` | 0 |

### Target 18: anyof-array-variant-closed-object-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-array-variant-closed-object-item` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if item.reference.is_none\(\) && is_inline_struct\(item\) \{]` | `exhausted` | `none-registrable` | 0 |

### Target 19: anyof-array-variant-composed-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-array-variant-composed-item` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if item.reference.is_none\(\) && is_inline_struct\(item\) \{]` | `exhausted` | `none-registrable` | 0 |

### Target 20: anyof-array-variant-inline-enum-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-array-variant-inline-enum-item` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(list\) = self\.hoist_array_item_enum\(&variant_name, variant\) \{]` | `search-incomplete` | `none-registrable` | 1 |

### Target 21: anyof-array-variant-oneof-nullable-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-array-variant-oneof-nullable-item` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[simple_nullable_member\(item\) \{]` | `exhausted` | `none-registrable` | 0 |

### Target 22: anyof-discriminated-union

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-discriminated-union` | arm | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | `exhausted` | `none-registrable` | 0 |

### Target 23: anyof-map-variant-anyof-value

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-map-variant-anyof-value` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `search-incomplete` | `none-registrable` | 9 |

### Target 24: anyof-map-variant-oneof-value

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-map-variant-oneof-value` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `search-incomplete` | `none-registrable` | 2 |

### Target 25: anyof-oneof-variant

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `anyof-oneof-variant` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = variant\.one_of\.as_ref\(\)\.or\(variant\.any_of\.as_ref\(\)\) \{]` | `exhausted` | `none-registrable` | 0 |

### Target 26: array-item-anyof-discriminated-union

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `array-item-anyof-discriminated-union` | arm | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | `exhausted` | `none-registrable` | 0 |

### Target 27: array-item-empty-object

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `array-item-empty-object` | arm | `src/ir.rs::Builder::nested_array_element[if is_inline_struct\(items\) \{]` | `exhausted` | `none-registrable` | 0 |

### Target 28: array-item-inheritance-union

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `array-item-inheritance-union` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 29: array-item-oneof-discriminated-union

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `array-item-oneof-discriminated-union` | arm | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | `exhausted` | `none-registrable` | 0 |

### Target 30: array-item-pointer-walk-allof

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `array-item-pointer-walk-allof` | arm | `src/ir.rs::resolve_schema_pointer[^\s*"allOf" => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 31: array-item-pointer-walk-anyof

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `array-item-pointer-walk-anyof` | arm | `src/ir.rs::resolve_schema_pointer[^\s*"anyOf" => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 32: array-item-pointer-walk-items

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `array-item-pointer-walk-items` | arm | `src/ir.rs::resolve_schema_pointer[^\s*"items" => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 33: array-item-pointer-walk-oneof

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `array-item-pointer-walk-oneof` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 34: array-item-pointer-walk-properties

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `array-item-pointer-walk-properties` | arm | `src/ir.rs::resolve_schema_pointer[^\s*"properties" => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 35: combo-annotated-ref-property-example

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `combo-annotated-ref-property-example` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 36: combo-anyof-beside-properties

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `combo-anyof-beside-properties` | feature | `-` | `search-incomplete` | `none-registrable` | 3 |

### Target 37: combo-oneof-beside-properties

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `combo-oneof-beside-properties` | feature | `-` | `search-incomplete` | `none-registrable` | 4 |

### Target 38: discriminated-variant-date-value-snippet

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `discriminated-variant-date-value-snippet` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 39: discriminator-mapping

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `discriminator-mapping` | arm | `src/emit.rs::ExampleCtx::discriminated_union_value[Some\(m\) if m\.layout\.is_wrapped\(\) => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 40: discriminator-mapping

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `discriminator-mapping` | arm | `src/ir.rs::Builder::discriminated_union[if let Some\(merged\) = merged_mapping_union\(target\x2c &property_name\x2c self\.schemas\) \{]` | `search-incomplete` | `none-registrable` | 179 |

### Target 41: discriminator-mapping

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `discriminator-mapping` | arm | `src/ir.rs::Builder::discriminated_union[if union_target \{]` | `exhausted` | `none-registrable` | 0 |

### Target 42: enum

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `enum` | arm | `src/ir.rs::EnumType::example_member[if let Some\(index\) = self\.members\.example \{]` | `search-incomplete` | `none-registrable` | 1848 |

### Target 43: enum-value-description-extension-dropped

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `enum-value-description-extension-dropped` | feature | `-` | `search-incomplete` | `none-registrable` | 2 |

### Target 44: format-binary

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-binary` | arm | `src/emit.rs::build_example_inner[if s\.type_ref == TypeRef::Primitive\(Prim::Bytes\)]` | `search-incomplete` | `none-registrable` | 440 |

### Target 45: format-binary

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-binary` | arm | `src/ir.rs::scalar_body[=Some\("binary"\)]` | `search-incomplete` | `none-registrable` | 442 |

### Target 46: format-byte

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-byte` | arm | `src/ir.rs::has_byte_text_response[=^ {16}return true;$]` | `search-incomplete` | `none-registrable` | 228 |

### Target 47: format-email

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-email` | arm | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` | `exhausted` | `none-registrable` | 0 |

### Target 48: format-hostname

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-hostname` | arm | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` | `exhausted` | `none-registrable` | 0 |

### Target 49: format-idn-hostname

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-idn-hostname` | arm | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | `exhausted` | `none-registrable` | 0 |

### Target 50: format-int64

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-int64` | arm | `src/ir.rs::bounded_example_literal[=^ {16}exact$]` | `search-incomplete` | `none-registrable` | 624 |

### Target 51: format-ipv4

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-ipv4` | arm | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` | `exhausted` | `none-registrable` | 0 |

### Target 52: format-iri

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-iri` | arm | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | `exhausted` | `none-registrable` | 0 |

### Target 53: format-json-pointer

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-json-pointer` | arm | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | `exhausted` | `none-registrable` | 0 |

### Target 54: format-password

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-password` | arm | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` | `exhausted` | `none-registrable` | 0 |

### Target 55: format-regex

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-regex` | arm | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | `exhausted` | `none-registrable` | 0 |

### Target 56: format-time

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-time` | arm | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | `exhausted` | `none-registrable` | 0 |

### Target 57: format-uri

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-uri` | arm | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` | `exhausted` | `none-registrable` | 0 |

### Target 58: format-uri-reference

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-uri-reference` | arm | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | `exhausted` | `none-registrable` | 0 |

### Target 59: format-uri-template

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-uri-template` | arm | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | `exhausted` | `none-registrable` | 0 |

### Target 60: format-uuid

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `format-uuid` | arm | `src/ir.rs::scalar_body[=Some\("uuid" \x7c "byte"\)]` | `search-incomplete` | `none-registrable` | 473 |

### Target 61: forward-refs-omit-hoisted-variant-models

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `forward-refs-omit-hoisted-variant-models` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 62: inheritance-discriminated-union

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `inheritance-discriminated-union` | arm | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | `exhausted` | `none-registrable` | 0 |

### Target 63: integer-example-beyond-double-precision

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `integer-example-beyond-double-precision` | feature | `-` | `search-incomplete` | `none-registrable` | 23 |

### Target 64: literal-enum-value-quote-escaping

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `literal-enum-value-quote-escaping` | feature | `-` | `search-incomplete` | `none-registrable` | 48 |

### Target 65: literal-example-dollar-escaped-in-docstring

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `literal-example-dollar-escaped-in-docstring` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 66: literal-type-extension-ignored

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `literal-type-extension-ignored` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 67: model-property-construct

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `model-property-construct` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 68: nullable-anyof-member-description-dropped

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `nullable-anyof-member-description-dropped` | feature | `-` | `search-incomplete` | `none-registrable` | 9 |

### Target 69: number-format-uint64-typed-int

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `number-format-uint64-typed-int` | feature | `-` | `search-incomplete` | `none-registrable` | 1 |

### Target 70: oneof

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof` | arm | `src/ir.rs::build_endpoint[Some\(if dropped_null \{]` | `search-incomplete` | `none-registrable` | 803 |

### Target 71: oneof

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof` | arm | `src/ir.rs::hoist_error_body_types[if schema\.discriminator\.is_some\(\)]` | `search-incomplete` | `none-registrable` | 803 |

### Target 72: oneof-anyof-variant

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-anyof-variant` | arm | `src/ir.rs::Builder::field_type_ref[=(?<=\.map\(\x7cvalues\x7c )\(items\x2c values\)]` | `search-incomplete` | `none-registrable` | 18 |

### Target 73: oneof-anyof-variant

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-anyof-variant` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = variant\.one_of\.as_ref\(\)\.or\(variant\.any_of\.as_ref\(\)\) \{]` | `exhausted` | `none-registrable` | 0 |

### Target 74: oneof-anyof-variant

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-anyof-variant` | arm | `src/ir.rs::InlineHoister::prop_type_ref[=return self.prop_type_ref\(parent\x2c prop\x2c &union\);]` | `search-incomplete` | `none-registrable` | 18 |

### Target 75: oneof-array-variant-annotated-ref-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-array-variant-annotated-ref-item` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 76: oneof-array-variant-anyof-discriminated-union-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-array-variant-anyof-discriminated-union-item` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 77: oneof-array-variant-anyof-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-array-variant-anyof-item` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = item.one_of]` | `exhausted` | `none-registrable` | 0 |

### Target 78: oneof-array-variant-anyof-nullable-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-array-variant-anyof-nullable-item` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 79: oneof-array-variant-closed-object-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-array-variant-closed-object-item` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if item.reference.is_none\(\) && is_inline_struct\(item\) \{]` | `exhausted` | `none-registrable` | 0 |

### Target 80: oneof-array-variant-inline-const-item

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-array-variant-inline-const-item` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 81: oneof-bare-object-example-variant

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-bare-object-example-variant` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 82: oneof-closed-empty-object-variant

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-closed-empty-object-variant` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[^ {8}\{$]` | `exhausted` | `none-registrable` | 0 |

### Target 83: oneof-discriminated-union

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-discriminated-union` | arm | `src/ir.rs::Builder::discriminated_union[if !schema\.properties\.is_empty\(\)]` | `search-incomplete` | `none-registrable` | 275 |

### Target 84: oneof-discriminated-union

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-discriminated-union` | arm | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | `search-incomplete` | `none-registrable` | 266 |

### Target 85: oneof-map-variant-anyof-value

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-map-variant-anyof-value` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 86: oneof-map-variant-oneof-value

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `oneof-map-variant-oneof-value` | arm | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]` | `search-incomplete` | `none-registrable` | 1 |

### Target 87: property-anyof-sole-string-enum-member

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-anyof-sole-string-enum-member` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 88: property-map-value-oneof

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-map-value-oneof` | arm | `src/ir.rs::InlineHoister::prop_type_ref[if value.reference.is_none\(\) && value.declared_type_name\(\).is_none\(\) && structured \{]` | `search-incomplete` | `none-registrable` | 29 |

### Target 89: property-oneof-residual

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-oneof-residual` | arm | `src/ir.rs::untagged_inline_discriminator[if untagged \{]` | `search-incomplete` | `none-registrable` | 358 |

### Target 90: property-oneof-sole-string-enum-member

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-oneof-sole-string-enum-member` | feature | `-` | `search-incomplete` | `none-registrable` | 2 |

### Target 91: property-ref-to-nullable-component-annotation

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-ref-to-nullable-component-annotation` | feature | `-` | `search-incomplete` | `none-registrable` | 11 |

### Target 92: property-sole-anyof-closed-object-member

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-sole-anyof-closed-object-member` | arm | `src/ir.rs::InlineHoister::prop_type_ref[if members.len\(\) == 1 && is_inline_struct]` | `exhausted` | `none-registrable` | 0 |

### Target 93: property-sole-anyof-composed-member

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-sole-anyof-composed-member` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 94: property-sole-anyof-empty-object-member

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-sole-anyof-empty-object-member` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 95: property-sole-anyof-struct-member

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-sole-anyof-struct-member` | arm | `src/ir.rs::InlineHoister::prop_type_ref[if members.len\(\) == 1 && is_inline_struct]` | `exhausted` | `none-registrable` | 0 |

### Target 96: property-sole-oneof-composed-member

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-sole-oneof-composed-member` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 97: property-sole-oneof-empty-object-member

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `property-sole-oneof-empty-object-member` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 98: ref-into-component-response-schema-named-by-last-segment

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-into-component-response-schema-named-by-last-segment` | feature | `-` | `search-incomplete` | `none-registrable` | 7 |

### Target 99: ref-pointer-composition-index

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-pointer-composition-index` | arm | `src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` | `exhausted` | `none-registrable` | 0 |

### Target 100: ref-pointer-composition-index

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-pointer-composition-index` | arm | `src/ir.rs::resolve_schema_pointer[^\s*"allOf" => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 101: ref-pointer-composition-index

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-pointer-composition-index` | arm | `src/ir.rs::resolve_schema_pointer[^\s*"anyOf" => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 102: ref-pointer-composition-index

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-pointer-composition-index` | arm | `src/ir.rs::resolve_schema_pointer[^\s*"oneOf" => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 103: ref-pointer-nested-items

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-pointer-nested-items` | arm | `src/ir.rs::ref_to_class["items" => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 104: ref-pointer-nested-items

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-pointer-nested-items` | arm | `src/ir.rs::resolve_schema_pointer[^\s*"items" => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 105: ref-pointer-nested-properties

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-pointer-nested-properties` | arm | `src/ir.rs::ref_to_class["properties" if index]` | `exhausted` | `none-registrable` | 0 |

### Target 106: ref-pointer-nested-properties

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-pointer-nested-properties` | arm | `src/ir.rs::resolve_schema_pointer[^\s*"properties" => \{]` | `exhausted` | `none-registrable` | 0 |

### Target 107: ref-pointer-undeclared-component-head

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-pointer-undeclared-component-head` | arm | `src/ir.rs::Builder::discriminated_union[if all_dangling \{]` | `search-incomplete` | `none-registrable` | 24 |

### Target 108: ref-pointer-undeclared-component-head

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-pointer-undeclared-component-head` | arm | `src/ir.rs::resolve_schema_pointer[=(?<=schemas\.get\(parts\.next\(\)\?\))\?;$]` | `search-incomplete` | `none-registrable` | 24 |

### Target 109: ref-with-nullable-sibling-made-optional

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `ref-with-nullable-sibling-made-optional` | feature | `-` | `search-incomplete` | `none-registrable` | 23 |

### Target 110: reference-literal-single-quote-escaped

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `reference-literal-single-quote-escaped` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 111: remote-document-local-pointer-resolved-against-root

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `remote-document-local-pointer-resolved-against-root` | feature | `-` | `search-incomplete` | `none-registrable` | 379 |

### Target 112: remote-ref-at-use-site-inlined

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `remote-ref-at-use-site-inlined` | feature | `-` | `search-incomplete` | `none-registrable` | 379 |

### Target 113: schema-example-array-null-element

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `schema-example-array-null-element` | feature | `-` | `search-incomplete` | `none-registrable` | 30 |

### Target 114: schema-example-null

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `schema-example-null` | feature | `-` | `search-incomplete` | `none-registrable` | 12 |

### Target 115: schema-example-outside-enum

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `schema-example-outside-enum` | arm | `src/emit.rs::ExampleCtx::example_matches_type_through[=Some\(TypeDecl::Enum\(decl\)\) => value]` | `search-incomplete` | `none-registrable` | 46 |

### Target 116: schema-example-temporal-duplicate-element

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `schema-example-temporal-duplicate-element` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 117: schema-example-union-ref-sentinel

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `schema-example-union-ref-sentinel` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 118: schema-sdk-group-name

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `schema-sdk-group-name` | feature | `-` | `search-incomplete` | `none-registrable` | 2 |

### Target 119: schema-type-name-component

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `schema-type-name-component` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 120: schema-type-name-inline-property

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `schema-type-name-inline-property` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 121: string-json-format-typed-any

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `string-json-format-typed-any` | feature | `-` | `exhausted` | `none-registrable` | 0 |

### Target 122: type-single

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `type-single` | arm | `src/ir.rs::base_type_ref[if let Some\(value\) = schema\.bool_literal\(\) \{]` | `search-incomplete` | `none-registrable` | 2095 |

### Target 123: undiscriminated-ref-oneof-sibling-properties-dropped

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `undiscriminated-ref-oneof-sibling-properties-dropped` | feature | `-` | `search-incomplete` | `none-registrable` | 56 |

### Target 124: union-of-enum-ref-const-and-string-members

| key | kind | arm | verdict | result | outstanding entries |
|---|---|---|---|---|---:|
| `union-of-enum-ref-const-and-string-members` | feature | `-` | `exhausted` | `none-registrable` | 0 |

## Handed-off differences

Earlier measured declarers are grouped by their original root cause in
[`known-declarers.tsv`](known-declarers.tsv), retaining the immutable revision
and digest for each. Their current handed-off status is recorded separately
from their historical difference. No claim that a repaired document still
differs is made. Documents still marked `differs` await residual repair;
`registration-incomplete` documents await their literals overlay/registration.
This continuation changes crozier's output for none of them.

New certified comparisons are grouped below and in
[`new-differences.tsv`](new-differences.tsv). Each group names its files and
links the complete comparison and normalized diff. Crozier output is unchanged.
There are no `default-matched` or `ruling-applied` output decisions here.

### array-ref-member-examples

`cloudfoundry/app-autoscaler:openapi/custom-metrics-api.openapi.yaml@311fe6e3b01ffb61380041dded0215dbc192345d`, SHA-256 `3a8dc3a8efd746de64254da9e8ef7b775f53e59ab6995f056499b42fba580b02`. Crozier uses the author-declared Metric name/value once; the reference writes two placeholder metrics. The source also has unretained sibling references, so it cannot be registered from its root alone.

Files: `README.md`, `reference.md`, `src/fern/custom_metrics_api_v1/client.py`. [Comparison](screens/3a8dc3a8efd746de64254da9e8ef7b775f53e59ab6995f056499b42fba580b02/compare.json).

### binary-upload-example-selection

`tryAGI/AssemblyAI:src/libs/AssemblyAI/openapi.yaml@2be14a9fa14e11f449acb92c863726cbf4641531`, SHA-256 `5316118a34875ed4c530f8450d02f8bafd3c324aeeb756d7806558c4323fa9f7`. The reference chooses an argument-free binary upload and supplies its worked call; crozier selects a different README endpoint and suppresses the upload example.

Files: `README.md`, `reference.md`, `src/fern/files/client.py`. [Comparison](screens/5316118a34875ed4c530f8450d02f8bafd3c324aeeb756d7806558c4323fa9f7/compare.json).

### crozier-refuses-heap-exhausted

`datamodel-code-generator/datamodel-code-generator:tests/data/openapi/openapi_discriminated_oneof_allof_cycle.json@34f144ff3569ef7525c1718a5d818841ed2cc43a`, SHA-256 `d0b3d3045ec6f2daf170dd33f727a8bbfba87975047c95002b5d75aabe381f3f`. The certified pair emits the cyclic models; crozier refuses at components/schemas/X.

Files: `no crozier SDK`. [Comparison](screens/d0b3d3045ec6f2daf170dd33f727a8bbfba87975047c95002b5d75aabe381f3f/compare.json).

### crozier-refuses-response-header-parameter-ref

`softwaremill/tapir:openapi-codegen/sbt-plugin/src/sbt-test/sbt-openapi-codegen/oneOf-json-roundtrip_jsoniter/swagger.yaml@918a0741732024e974c91ffb9dbebf6fbfffdd1e`, SHA-256 `ecbf8491bee63100c41c6ffb32e819c86da3f4a858f2beda8c2702d8f399d5a7`. The reference generates while crozier refuses a response Header Object reference into components.parameters.

Files: `no crozier SDK`. [Comparison](screens/ecbf8491bee63100c41c6ffb32e819c86da3f4a858f2beda8c2702d8f399d5a7/compare.json).

### declared-map-example-vs-placeholder

`the-momentum/open-wearables:docs/openapi.json@b47932b53282cedbb720880466b7ebed8f3897c6`, SHA-256 `a4fdbfae93113a7d47ad4b3467920e33fc4916d05f03cbbf4b5b24380e2be74f`. Crozier uses the author-declared providers map; the reference writes a key/True placeholder map.

Files: `reference.md`, `src/fern/internal_providers/client.py`. [Comparison](screens/a4fdbfae93113a7d47ad4b3467920e33fc4916d05f03cbbf4b5b24380e2be74f/compare.json).

### example-optional-members

`the-momentum/open-wearables:docs/openapi.json@b47932b53282cedbb720880466b7ebed8f3897c6`, SHA-256 `a4fdbfae93113a7d47ad4b3467920e33fc4916d05f03cbbf4b5b24380e2be74f`. The reference includes optional worked-call arguments and their imports; crozier omits them. The existing minimal-worked-call ruling applies to later repair.

Files: `reference.md`, `src/fern/external_health_scores/client.py`, `src/fern/external_mobile_sdk/client.py`, `src/fern/external_summaries/client.py`. [Comparison](screens/a4fdbfae93113a7d47ad4b3467920e33fc4916d05f03cbbf4b5b24380e2be74f/compare.json).

### falsy-property-example

`cloudfoundry/app-autoscaler:openapi/custom-metrics-api.openapi.yaml@311fe6e3b01ffb61380041dded0215dbc192345d`, SHA-256 `3a8dc3a8efd746de64254da9e8ef7b775f53e59ab6995f056499b42fba580b02`. The integer property example 0 is preserved by crozier; the reference writes a placeholder. Existing ruling falsy-property-example governs a later repair, not a new output change here.

Files: `README.md`, `reference.md`, `src/fern/custom_metrics_api_v1/client.py`. [Comparison](screens/3a8dc3a8efd746de64254da9e8ef7b775f53e59ab6995f056499b42fba580b02/compare.json).

### geojson-discriminator-wrapper-and-parent-model

`KORTxyz/ogcapi-gpkg:src/openapi.yaml@94b48d9400e77bc6db147a358d176707f6548e1d`, SHA-256 `7aa3e80e307f90e9c95b404bacb8e78bb4e63ff5d1aa6dd379d658be990a380c`. The reference wraps PointGeoJson as a variant value and retains its enum/discriminant; crozier flattens coordinates and removes the parent discriminant enum. Reference worked examples contain point=, fragments.

Files: `README.md`, `reference.md`, `src/fern/__init__.py`, `src/fern/features/client.py`, `src/fern/types/__init__.py`, `src/fern/types/geometry_geo_json.py`, `src/fern/types/point_geo_json.py`, `src/fern/types/point_geo_json_type.py`. [Comparison](screens/7aa3e80e307f90e9c95b404bacb8e78bb4e63ff5d1aa6dd379d658be990a380c/compare.json).

### nested-null-union-lowering

`chloepriceless/DV-EOS:openapi.json@e2fca78146c468f1ef4a4b540ebe608c11ad47c2`, SHA-256 `1e6f231fdcbbcde28d8665e4c3d6977c5b3fc6427300bdb0f7469edd6557dec9`. Crozier preserves an extra Any union arm and loses optionality of nested list items where the reference drops the null arm and marks the item optional.

Files: `src/fern/prediction/types/fastapi_prediction_import_provider_v1prediction_import_provider_id_put_request_body.py`, `src/fern/types/pydantic_date_time_data_value.py`, `src/fern/types/pydantic_date_time_data_value_one_item.py`. [Comparison](screens/1e6f231fdcbbcde28d8665e4c3d6977c5b3fc6427300bdb0f7469edd6557dec9/compare.json).

### nullable-type-array-datetime-override

`tryAGI/AssemblyAI:src/libs/AssemblyAI/openapi.yaml@2be14a9fa14e11f449acb92c863726cbf4641531`, SHA-256 `5316118a34875ed4c530f8450d02f8bafd3c324aeeb756d7806558c4323fa9f7`. The nullable string type array with x-fern-type optional<datetime> is str in crozier and datetime in the reference.

Files: `src/fern/transcripts/types/transcript_list_item.py`. [Comparison](screens/5316118a34875ed4c530f8450d02f8bafd3c324aeeb756d7806558c4323fa9f7/compare.json).

### nullable-worked-call-object-values

`chloepriceless/DV-EOS:openapi.json@e2fca78146c468f1ef4a4b540ebe608c11ad47c2`, SHA-256 `1e6f231fdcbbcde28d8665e4c3d6977c5b3fc6427300bdb0f7469edd6557dec9`. The reference builds nullable object argument examples; crozier omits those arguments in client snippets and writes None in reference.md.

Files: `reference.md`, `src/fern/optimize/client.py`. [Comparison](screens/1e6f231fdcbbcde28d8665e4c3d6977c5b3fc6427300bdb0f7469edd6557dec9/compare.json).

### optional-json-body-content-type

`agent-infra/sandbox:website/docs/public/v1/openapi.json@7f1afaf8d82bd30531a19caeb1a24dfebbc97d8c`, SHA-256 `8d9a8ecdca11217c65d4fe8ad30e711d1d3d514598a0c8e2fd73bcd81fa7da6e`. Crozier emits an application/json header that the reference omits for the optional RestartRequest body.

Files: `src/fern/browser/raw_client.py`. [Comparison](screens/8d9a8ecdca11217c65d4fe8ad30e711d1d3d514598a0c8e2fd73bcd81fa7da6e/compare.json).

`tryAGI/AssemblyAI:src/libs/AssemblyAI/openapi.yaml@2be14a9fa14e11f449acb92c863726cbf4641531`, SHA-256 `5316118a34875ed4c530f8450d02f8bafd3c324aeeb756d7806558c4323fa9f7`. Crozier emits an application/json header that the certified pair omits on the optional request body.

Files: `src/fern/transcripts/raw_client.py`. [Comparison](screens/5316118a34875ed4c530f8450d02f8bafd3c324aeeb756d7806558c4323fa9f7/compare.json).

### ref-description-propagation

`KORTxyz/ogcapi-gpkg:src/openapi.yaml@94b48d9400e77bc6db147a358d176707f6548e1d`, SHA-256 `7aa3e80e307f90e9c95b404bacb8e78bb4e63ff5d1aa6dd379d658be990a380c`. Descriptions propagate differently through enum references and the propertiesSchema reference/hoist.

Files: `src/fern/types/geospatial_data.py`, `src/fern/types/geospatial_data_properties_schema.py`, `src/fern/types/tile_set.py`. [Comparison](screens/7aa3e80e307f90e9c95b404bacb8e78bb4e63ff5d1aa6dd379d658be990a380c/compare.json).

### reference-tag-heading-case

`agent-infra/sandbox:website/docs/public/v1/openapi.json@7f1afaf8d82bd30531a19caeb1a24dfebbc97d8c`, SHA-256 `8d9a8ecdca11217c65d4fe8ad30e711d1d3d514598a0c8e2fd73bcd81fa7da6e`. The certified pair capitalizes group headings such as Sandbox; crozier keeps sandbox.

Files: `reference.md`. [Comparison](screens/8d9a8ecdca11217c65d4fe8ad30e711d1d3d514598a0c8e2fd73bcd81fa7da6e/compare.json).

### root-alias-body-serialization

`chloepriceless/DV-EOS:openapi.json@e2fca78146c468f1ef4a4b540ebe608c11ad47c2`, SHA-256 `1e6f231fdcbbcde28d8665e4c3d6977c5b3fc6427300bdb0f7469edd6557dec9`. The reference converts and respects annotation metadata for PydanticDateTimeData; crozier sends the request value directly.

Files: `src/fern/measurement/raw_client.py`. [Comparison](screens/1e6f231fdcbbcde28d8665e4c3d6977c5b3fc6427300bdb0f7469edd6557dec9/compare.json).

## Verification

The final verification record is retained in `verification.txt`.
