# Witness search: unions of only `null`, and of one string enum

The real-specification search for four region keys of
[`schemas.md`](../schemas.md), each a `oneOf`/`anyOf` spelling of two shapes the
repairs of the `composed-schema-lowering` refusal-parity finding settled:

- `anyof-null-only-alternatives`, `oneof-null-only-alternatives`: every
  alternative is `type: null`. crozier emitted an unparseable `typing.Union[]`
  (and panicked in `simple_nullable_member` on an array item); Fern
  (CLI 5.163.1, fern-python-sdk 5.41.3) generates `Optional[Any]`.
- `anyof-sole-string-enum-alternative`, `oneof-sole-string-enum-alternative`:
  the one alternative is a string `enum`. crozier declared a `…Zero` enum
  behind an alias; Fern declares the enum under the owner's name.

## The search

Each key's selector is the census's own, recorded in
[`../witness-search-keys.tsv`](../witness-search-keys.tsv) for the two
`handwritten` keys and in the region rows for the two `golden` ones. The
search was bounded to the document sets already on the host, with no GitHub
query:

- **Every registered corpus source**: none declared any of the four shapes
  before this change registered `openapi-generator-composed-schema-lowering`.
- **The golden-reach search pools** (`github-code-search`, 5,162 documents;
  `sourcegraph`, 4,095), plus the 19 documents of the APIs.guru
  `openapi-directory` snapshot at `f04b8d0`: 9,276 files, of which 151 the
  census could not read.

Every declarer, one row per key and document, is in
[`declarers.tsv`](declarers.tsv): 7 documents declare
`anyof-null-only-alternatives`, 2 `oneof-null-only-alternatives`, 13
`anyof-sole-string-enum-alternative` and 13
`oneof-sole-string-enum-alternative`.

## Screening

By the manager's ruling for this search, one candidate per key was screened
and registered only if crozier byte-matched the certified pair on it:

| document | keys | licence | outcome |
|---|---|---|---|
| OpenAPI Generator `modules/openapi-generator/src/test/resources/3_1/cpp-boost-beast-client/composed-schema-lowering.yaml` at `10e6c21c97ab` | `anyof-null-only-alternatives`, `anyof-sole-string-enum-alternative` | Apache-2.0 (repository LICENSE) | registered: corpus row 3473 |
| OpenAPI Generator `…/3_1/cpp-boost-beast-client/oas31-runtime-regression.yaml` at `10e6c21c97ab` | `oneof-null-only-alternatives` | Apache-2.0 (repository LICENSE) | blocked: the certified pair writes 82 files and crozier matches every one but three, on shapes this change does not touch — `NonAsciiPattern` (Fern `typing.Any`, crozier `Dict[str, Any]`), `RefAnnotationIsolation` and `RefSiblingComposition` (Fern aliases of their `$ref` targets, crozier a model and a map) |
| konfig-sdks/openapi-examples `qualtrics/survey/openapi.yaml` at `161ab49c45e4` | `oneof-sole-string-enum-alternative` | Apache-2.0 (document `info.license`) | fern-rejected: the certified pair exits 1 with `Enum name 1Hour for value +1 hour is not suitable for code generation` |

The smallest `oneof-sole-string-enum-alternative` declarer,
LuisEgui/dunktomic, declares no licence in the document, so it was passed over
for the smallest one granting one without a GitHub query. Every other declarer
is unscreened, OpenAPI Generator's `3_0_3_unit_test_spec.yaml` among them: by
the same ruling none is registered here.

## Verdicts

| key | outcome | declarers | disposition |
|---|---|---:|---|
| `anyof-null-only-alternatives` | `witness-found` | 7 | registered `openapi-generator-composed-schema-lowering` |
| `anyof-sole-string-enum-alternative` | `witness-found` | 13 | registered `openapi-generator-composed-schema-lowering` |
| `oneof-null-only-alternatives` | `search-incomplete` | 2 | proven by the hand-written fixture `dormant-sensor-unions`; the screened declarer is blocked, the other unscreened |
| `oneof-sole-string-enum-alternative` | `search-incomplete` | 13 | proven by the hand-written fixture `dormant-sensor-unions`; the screened declarer is fern-rejected, the rest unscreened |

## Renewed search

The hand-written covers of the two `oneOf` keys cite this record as their
renewed search.

| key | renewed outcome | why no declarer is registrable |
|---|---|---|
| `oneof-null-only-alternatives` | `none-registrable` | the one screened declarer, `oas31-runtime-regression.yaml`, cannot be registered with an empty `unmatched` list while crozier differs from the certified pair on its three files; the other, `3_0_3_unit_test_spec.yaml`, is held back by the ruling above |
| `oneof-sole-string-enum-alternative` | `none-registrable` | the one screened declarer is one the certified pair refuses, and the ruling above held the other twelve back |
