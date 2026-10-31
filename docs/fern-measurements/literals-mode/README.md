# 49 parity shapes, measured under Fern's default enum type

Each case is one shape crozier and Fern generate identically, measured with
`pydantic_config.enum_type` unset — Fern's own default, `literals` — the mode
the shape was first observed in. The documents were written for the purpose;
none is a real specification, and none settles a coverage row.

Each `fern-expected/` is the output of
`tools/fern-goldens/generate-fern-fixture.sh --enum-type literals` at Fern CLI
5.163.1 and `fernapi/fern-python-sdk` 5.41.3, comment-stripped by
`crozier internal-strip`, and never edited. Where the case's document is a
hand-written fixture, the script reduced Fern's tree to an overlay of that
fixture's `fern-expected/` (Fern's `python_enums` tree): the files whose bytes
differ, plus `.crozier-overlay.json` naming the files Fern omits. Where the
case carries its own `openapi.yml`, the script reduced it against nothing, so
`fern-expected/` is the complete tree and its manifest removes nothing.

`literals_mode_measurements_match_fern` in
[`../../../crates/crozier-e2e/tests/e2e/literals_mode.rs`](../../../crates/crozier-e2e/tests/e2e/literals_mode.rs)
rebuilds each complete tree, generates the document with crozier's
`--enum-type literals`, and compares the two whole through `src/parity.rs`
under the corpus gate's normalization, every departure held to
[the ledger](../../../tests/fixtures/departures-ledger.tsv).

## The cases

| case | what it pins | document | tree |
|---|---|---|---|
| `buoy-depth-response` | a JSON success response with no `description` key ends the docstring's `Returns` at its type | [superseded fixture](../superseded-fixtures/buoy-depth-response/) | overlay |
| `discriminated-variant-date-value-snippet` | discriminated variants valued `date` and `date-time` take `dt.date` and `dt.datetime`, and the worked call passes `datetime.date.fromisoformat(...)` | [hand-written fixture](../../openapi-surface/handwritten/discriminated-variant-date-value-snippet/) | overlay |
| `dotted-mapping-key-variant-class-name` | mapping keys `door.locked` and `door.unlocked` name `Notice_DoorLocked` and `Notice_DoorUnlocked`, not the target schemas | [document](dotted-mapping-key-variant-class-name/openapi.yml) | complete tree |
| `empty-path-segment-double-slash-kept` | a path with an empty segment keeps its `//` in the request URL | [hand-written fixture](../../openapi-surface/handwritten/empty-path-segment-double-slash-kept/) | overlay |
| `enum-extension-names-dropped-under-literals` | `x-fern-enum` names and descriptions leave a described symbol-valued enum a bare `Literal` alias with no docstring | [document](enum-extension-names-dropped-under-literals/openapi.yml) | complete tree |
| `enum-header-params-stringified` | required and optional `$ref` string-enum headers are sent as `str(...)`, guarded by `is not None` | [document](enum-header-params-stringified/openapi.yml) | complete tree |
| `enum-union-body-example-first-member-value` | a request body that is a union of string enums, with no example, is worked with the first member's first value | [hand-written fixture](../../openapi-surface/handwritten/enum-union-body-example-first-member-value/) | overlay |
| `example-imports-case-insensitive-order` | an async docstring imports `AsyncFernApi` before `AWing`, sorting names ignoring case | [hand-written fixture](../../openapi-surface/handwritten/example-imports-case-insensitive-order/) | overlay |
| `ferry-slot-query` | a required query `anyOf` of a uuid and a one-value enum is worked with its default as a plain string | [hand-written fixture](../../openapi-surface/handwritten/ferry-slot-query/) | overlay |
| `fortune-cookie-const` | a const holding `'` is written `\'` in the README and `reference.md`, bare in the docstrings | [hand-written fixture](../../openapi-surface/handwritten/fortune-cookie-const/) | overlay |
| `greenhouse-vents` | with no `POST`, the README demonstrates the first argument-free `GET` over a later argument-free `PUT` | [hand-written fixture](../../openapi-surface/handwritten/greenhouse-vents/) | overlay |
| `group-path-ending-in-api-nested-package` | an `x-fern-sdk-group-name` of `[beacon, api]` writes `beacon/api/` under an intermediate `beacon` client | [hand-written fixture](../../openapi-surface/handwritten/group-path-ending-in-api-nested-package/) | overlay |
| `invoice-renderer` | an operation answering only `text/plain` is worked with neither its named nor its singular request example | [hand-written fixture](../../openapi-surface/handwritten/invoice-renderer/) | overlay |
| `literal-enum-description-omitted` | a described component string enum is a `Literal` alias with no docstring | [document](literal-enum-description-omitted/openapi.yml) | complete tree |
| `literal-enum-value-quote-escaping` | enum values carrying a backslash, quotes of both kinds and a non-ASCII character are each quoted as Python writes them, one per line | [hand-written fixture](../../openapi-surface/handwritten/literal-enum-value-quote-escaping/) | overlay |
| `literal-prefixed-integer-path-segment` | an integer parameter after literal text in its segment is a positional `int` interpolated after that text | [hand-written fixture](../../openapi-surface/handwritten/literal-prefixed-integer-path-segment/) | overlay |
| `multipart-inline-object-part-json-encoded` | an inline object part of a multipart body is hoisted and sent as `json.dumps(jsonable_encoder(...))` | [hand-written fixture](../../openapi-surface/handwritten/multipart-inline-object-part-json-encoded/) | overlay |
| `multipart-part-encoding-charset-tuple` | `encoding.<part>.contentType` reaches the file part's default content type and the JSON part's tuple, `charset` included | [hand-written fixture](../../openapi-surface/handwritten/multipart-part-encoding-charset-tuple/) | overlay |
| `multipart-single-value-enum-part-kept-optional` | an optional one-value string enum part stays an optional argument defaulting to `OMIT` | [document](multipart-single-value-enum-part-kept-optional/openapi.yml) | complete tree |
| `odometer-reading` | an int64 example past 2^53 takes its nearest double, except where that leaves the int64 range (the `int64-example-rounded-out-of-range` departure) | [hand-written fixture](../../openapi-surface/handwritten/odometer-reading/) | overlay |
| `open-object-body-example-extra-keys-dropped` | an open body's example key outside `properties` is left out of the worked call | [document](open-object-body-example-extra-keys-dropped/openapi.yml) | complete tree |
| `passport-scan` | the README passes a multipart body's optional file part beside its required one | [hand-written fixture](../../openapi-surface/handwritten/passport-scan/) | overlay |
| `patch-inline-nullable-unrequired-props-omit` | a PATCH body of unrequired nullable properties takes each as `Optional[...] = OMIT`, sent with `omit=OMIT` | [superseded fixture](../superseded-fixtures/patch-inline-nullable-unrequired-props-omit/) | overlay |
| `poster-upload` | the README passes a multipart body's file part before the scalar parts declared ahead of it | [hand-written fixture](../../openapi-surface/handwritten/poster-upload/) | overlay |
| `pottery-commission` | a body `$ref` to an `allOf` of a base and an inline member is worked base field first | [superseded fixture](../superseded-fixtures/pottery-commission/) | overlay |
| `prompt-variable` | a const holding `$` is a one-value `Literal` alias, passed bare everywhere but Fern's docstrings (the `docstring-literal-dollar-escape` departure) | [hand-written fixture](../../openapi-surface/handwritten/prompt-variable/) | overlay |
| `query-param-ref-to-enum-or-array-union-converted` | an optional query parameter naming a one-or-many enum union is sent through `convert_and_respect_annotation_metadata` | [hand-written fixture](../../openapi-surface/handwritten/query-param-ref-to-enum-or-array-union-converted/) | overlay |
| `required-and-nullable-property-defaults-none` | a required `nullable: true` property is `Optional[...] = None` | [document](required-and-nullable-property-defaults-none/openapi.yml) | complete tree |
| `required-param-and-body-defaults-ignored` | a required query integer and a required body string keep no default despite declaring one | [hand-written fixture](../../openapi-surface/handwritten/required-param-and-body-defaults-ignored/) | overlay |
| `seismic-trace-export` | a root binary download posting a JSON body has no worked example, and the README demonstrates the next operation | [hand-written fixture](../../openapi-surface/handwritten/seismic-trace-export/) | overlay |
| `sensor-batch-query` | a required query array of nullable union items is worked as `[]` in the docstrings | [hand-written fixture](../../openapi-surface/handwritten/sensor-batch-query/) | overlay |
| `snake-case-component-name-pascal-class` | a component named `honey_yield` is `class HoneyYield` in `types/honey_yield.py` | [document](snake-case-component-name-pascal-class/openapi.yml) | complete tree |
| `stream-error-status-raises-typed-error` | a `400` typed `string` beside an event-stream `200` raises `BadRequestError` from inside `_stream()`, parsed as `str` after `_response.read()` | [hand-written fixture](../../openapi-surface/handwritten/stream-error-status-raises-typed-error/) | overlay |
| `string-body-example-backslash-escaped` | a string body example holding `\n` and `\t` is written with each backslash escaped | [hand-written fixture](../../openapi-surface/handwritten/string-body-example-backslash-escaped/) | overlay |
| `tram-route-query` | a required object query parameter's array field is worked with two items | [hand-written fixture](../../openapi-surface/handwritten/tram-route-query/) | overlay |
| `undiscriminated-ref-oneof-sibling-properties-dropped` | properties beside an undiscriminated `oneOf` of two `$ref`s are dropped from the union alias | [hand-written fixture](../../openapi-surface/handwritten/undiscriminated-ref-oneof-sibling-properties-dropped/) | overlay |
| `union-of-enum-ref-const-and-string-members` | a union of an enum `$ref`, a string `const` and a plain string is `typing.Union[Mordant, ShadeOne, str]` | [hand-written fixture](../../openapi-surface/handwritten/union-of-enum-ref-const-and-string-members/) | overlay |
| `variant-optional-const-discriminant-merged` | a variant's optional `const` named like the discriminator leaves only the variant literal, first | [document](variant-optional-const-discriminant-merged/openapi.yml) | complete tree |
| `water-pump-station` | the README demonstrates a nested group's `POST` over top-level groups' `GET`s | [hand-written fixture](../../openapi-surface/handwritten/water-pump-station/) | overlay |
| `weather-radar-stream` | the README's streaming section imports the model its call constructs | [hand-written fixture](../../openapi-surface/handwritten/weather-radar-stream/) | overlay |

Two cases carry their own document because no hand-written fixture gates
their `python_enums` output. Under `python_enums`,
`enum-header-params-stringified` still differs: Fern sends `.value` and crozier
sends `str(...)`. `enum-extension-names-dropped-under-literals` now matches
Fern's whole tree. Both are measured in
[`../python-enums-residuals/`](../python-enums-residuals/README.md). Seven more
cases carry their own document because a real specification's golden proves the
shape under `python_enums`.
