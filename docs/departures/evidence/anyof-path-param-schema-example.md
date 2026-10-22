# `anyof-path-param-schema-example`

**Kind:** `richer-documentation`. A path parameter whose schema is an inline
`anyOf`/`oneOf` declaring a schema-level example: Fern's worked calls pass the
parameter's own name, crozier's pass the declared example.

## The input

[`marina-dock-refs/openapi.yml`](../../fern-measurements/examples-docs/marina-dock-refs/openapi.yml),
a crozier-authored document whose `GET /docks/{dock_id_or_code}` declares the
path parameter `dock_id_or_code` as `anyOf: [{type: string, minLength: 4,
maxLength: 16, pattern: '^[a-z]+$'}, {type: string, format: uuid}]` with the
schema-level `example: northbasin`. The real Supabase management API declares
the same shape on `branch_id_or_ref` (`example: abcdefghijklmnopqrst`) across
its `/v1/branches/{branch_id_or_ref}` operations.

## Fern's output

Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3, in the workspace
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds (`organization: fern`,
`pydantic_config.enum_type: python_enums`, `fern generate --group python-sdk
--local --preview`), exits 0; the comment-stripped tree is the case's
`fern-expected/`. Its `README.md` (lines 44 and 64), `reference.md` (line 23)
and both `get_dock` docstrings (`src/fern/docks/client.py` lines 50 and 101)
pass `dock_id_or_code="dock_id_or_code"`.

## Both sides are valid; crozier's documents the declared example

crozier passes `dock_id_or_code="northbasin"` at the same lines. Parsing every
worked call of `get_dock` from each tree's `src/fern/docks/client.py` and
`reference.md` and binding it with `inspect.signature` to the package's own
method (Python 3.12, `httpx` and `pydantic` 2.14.1):

```text
fern     {"dock_id_or_code": "'dock_id_or_code'"}  binds
crozier  {"dock_id_or_code": "'northbasin'"}       binds
```

Validating the declared example against the parameter's schema with
`jsonschema` 4.26.0:

```text
dock_id_or_code example 'northbasin' valid against {"example": "northbasin", "anyOf": [{"type": "string", "minLength": 4, "maxLength": 16, "pattern": "^[a-z]+$", "example": "northbasin"}, {"type": "string", "format": "uuid"}]}
```

Fern's placeholder also binds to the `str` annotation, so neither call is a
defect; crozier's passes the value the specification states for the parameter,
which its composition admits.

## The parity rule

The rule accepts one aligned line pair of `README.md`, `reference.md` or a
high-level `client.py`, each a keyword argument line with the same indentation
and keyword, when the parsed source document declares a path parameter of that
name whose inline `anyOf`/`oneOf` schema carries a string schema-level example,
Fern's value is the parameter's name and crozier's is that example's literal.
Without the source document, for a query parameter, for a composition without
an example or for any other value, it does not apply.
`examples_docs_measurements_match_fern` and
`examples_docs_cases_fail_on_an_adjacent_unexplained_byte` in
`crates/crozier-e2e/tests/e2e/examples_docs.rs` hold the case; the line ledger
is recorded from `src/parity.rs`, never hand-edited.

## Required reference examples and named oneOf examples

The from-scratch [Harbor parcel document](../../openapi-surface/handwritten/harbor-parcel-requests/openapi.yml)
adds two measured reference shapes. `tracking` is a required string query
parameter with a local schema reference and its own example. `category` is a
required body property whose `allOf` has one local string reference and a
separate description-only member, with an example on the property itself.
Fern substitutes their names; Crozier retains their declared strings. The
complete certified tree is that fixture's `fern-expected/`.

Importing each SDK and parsing the actual sync and async method docstrings,
then calling `inspect.signature(method).bind(None, **example_keywords)` and
`pydantic.TypeAdapter(str).validate_python` on the two reference values gives
(Python 3.14.7, pydantic 2.14.0, httpx 0.28.1):

```text
FernApi.submit_parcel {"category": "category", "label": "glassware", "tracking": "tracking"} binds; reference strings validate
AsyncFernApi.submit_parcel {"category": "category", "label": "glassware", "tracking": "tracking"} binds; reference strings validate
FernApi.submit_parcel {"category": "overnight", "label": "glassware", "tracking": "harbor-842"} binds; reference strings validate
AsyncFernApi.submit_parcel {"category": "overnight", "label": "glassware", "tracking": "harbor-842"} binds; reference strings validate
```

The real [RGB Lightning Node source](../../../tests/fixtures/corpus-sources/rgb-lightning-node/openapi.yaml),
corpus row 3203, also declares a named `oneOf` schema example:
`SyncKeychain` admits the string `Colored` or an object carrying
`Vanilla: {lookback: integer}`, and declares `{Vanilla: {lookback: 20}}`.
`SyncOptions.keychain` references it. Fern's call chooses `SyncKeychainZero.COLORED`;
Crozier constructs `SyncKeychainVanilla(vanilla=SyncKeychainVanillaVanilla(lookback=20))`.
This is the specification's example, not a synthesized improvement.

Executing against the certified SDK's actual union annotation proves that
example is admitted and an adjacent invalid value is rejected:

```python
from pydantic import TypeAdapter, ValidationError
from fern.types.sync_keychain import SyncKeychain

adapter = TypeAdapter(SyncKeychain)
value = adapter.validate_python({"Vanilla": {"lookback": 20}}, strict=True)
print(type(value).__name__, value.model_dump(by_alias=True), "valid")
try:
    adapter.validate_python({"Vanilla": {"lookback": "twenty"}}, strict=True)
except ValidationError:
    print("invalid lookback rejected")
else:
    raise AssertionError("invalid lookback accepted")
```

```text
SyncKeychainVanilla {'Vanilla': {'lookback': 20}} valid
invalid lookback rejected
```

The paired removals are committed in
[the real comparisons](../../openapi-surface/witness-search-schema-combinations-examples/paired-removal-comparisons.json)
and [the authored comparisons](../../openapi-surface/witness-search-schema-combinations-examples/handwritten-removal-comparisons.json).
Fern ignores these examples before and after their removal; Crozier's output
changes. They are generating proofs with this declared-content departure,
not output-insensitive decisions.

The extended recognizer admits only the source's exact declared value and
its exact constructor/import substitution. It validates supported schema
assertions, including exactly-one membership, and abstains on an unmodeled
assertion such as `maximum` or `multipleOf`. The loader retains unknown schema
keywords only for this conservative validation; that input-only map is never
serialized into SDK output. Required reference examples are limited to local
unconstrained string targets. Unit tests and the two public-CLI negative
regressions retain unexplained adjacent argument differences.
