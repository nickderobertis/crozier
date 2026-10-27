# Witness search: unions of only `null`, and of one string enum

The real-specification search behind the repairs of the composed-schema-lowering
refusal-parity finding. They settle two shapes:

- **Every alternative is `type: null`.** crozier emitted an unparseable
  `typing.Union[]`, and panicked in `simple_nullable_member` on an array item.
  Fern (CLI 5.163.1, fern-python-sdk 5.41.3) generates `Optional[Any]`.
- **The one alternative is a string `enum`.** crozier declared a `…Zero` enum
  behind an alias. Fern declares the enum under the owner's name.

Two `schemas.md` region keys carry census selectors:
`property-oneof-sole-string-enum-member` and
`property-anyof-sole-string-enum-member`. They are read off `prop_type_ref`'s
cases 20a and 20b, the property arm of the second repair. The all-`null` fold
(`src/openapi.rs`) and the component arm (`Builder::add_named`) are in none of
the census's blind functions, so no selector can name them. Their real witness
is corpus row 3476, `openapi-generator-composed-schema-lowering`, which declares
both shapes on components. That is OpenAPI Generator's
`modules/openapi-generator/src/test/resources/3_1/cpp-boost-beast-client/composed-schema-lowering.yaml`
at `10e6c21c97ab`, Apache-2.0 by its repository LICENSE. Its complete golden is
byte-matched.

## The search

Each key's selector is recorded in
[`../witness-search-keys.tsv`](../witness-search-keys.tsv). The search was
bounded to the document sets already on the host, with no GitHub query:

- **Every registered corpus source** (271): none declares either selector.
- **The golden-reach search pools** (`github-code-search`, 5,162 documents;
  `sourcegraph`, 4,095), plus the 19 documents of the APIs.guru
  `openapi-directory` snapshot at `f04b8d0`: 9,276 files, of which the census
  could not read 151.

Every declarer is in [`declarers.tsv`](declarers.tsv), one row per key and
document. Two documents declare `property-anyof-sole-string-enum-member` and
eight declare `property-oneof-sole-string-enum-member`.

## Screening

The manager ruled that one candidate is screened and registered only if crozier
byte-matches the certified pair on it:

| document | key | licence | outcome |
|---|---|---|---|
| konfig-sdks/openapi-examples `qualtrics/survey/openapi.yaml` at `161ab49c45e4` | `property-oneof-sole-string-enum-member` | Apache-2.0 (document `info.license`) | fern-rejected: the certified pair exits 1 with `Enum name 1Hour for value +1 hour is not suitable for code generation` |

The smallest declarer, LuisEgui/dunktomic, declares no licence in the document.
It was passed over for the smallest one that grants a licence without a GitHub
query. Every other declarer is unscreened, by the same ruling.

Two other documents were screened for the component-level spellings, which carry
no census selector:

- OpenAPI Generator's `…/3_1/cpp-boost-beast-client/oas31-runtime-regression.yaml`
  at `10e6c21c97ab` declares a `oneOf` of only `null` alternatives. It is blocked:
  the certified pair writes 82 files, and crozier matches all but three, on
  shapes this change does not touch. Fern types `NonAsciiPattern` as
  `typing.Any` where crozier writes `Dict[str, Any]`, and Fern makes
  `RefAnnotationIsolation` and `RefSiblingComposition` aliases of their `$ref`
  targets where crozier writes a model and a map.
- OpenAPI Generator's `3_0_3_unit_test_spec.yaml` is unscreened, by the ruling.

## Verdicts

| key | outcome | declarers | disposition |
|---|---|---:|---|
| `property-oneof-sole-string-enum-member` | `search-incomplete` | 8 | proven by the hand-written fixture `dormant-sensor-unions`; the screened declarer is fern-rejected, the rest unscreened |
| `property-anyof-sole-string-enum-member` | `search-incomplete` | 2 | proven by the hand-written fixture `dormant-sensor-unions`; both declarers unscreened |

## Renewed search

The hand-written covers of both keys cite this record as their renewed search.

| key | renewed outcome | why no declarer is registrable |
|---|---|---|
| `property-oneof-sole-string-enum-member` | `none-registrable` | the one screened declarer is one the certified pair refuses, and the ruling above held the other seven back |
| `property-anyof-sole-string-enum-member` | `none-registrable` | the ruling above held both declarers back |
