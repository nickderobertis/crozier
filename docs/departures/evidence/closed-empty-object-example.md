# `closed-empty-object-example`

**Kind:** `fern-defect`. Fern's usage example passes a required argument whose
schema admits only `{}` the value `{"key": "value"}`, which that schema rejects.

## The input

The hand-written fixture
[`closed-empty-inline-objects`](../../openapi-surface/handwritten/closed-empty-inline-objects/openapi.yml),
a crozier-authored document whose `scheduleFiring` request body requires
`profile`, declared `{type: object, additionalProperties: false}` with no
`properties` and no `example`.

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0 (the certified pair), in
the workspace [`../../openapi-surface/probes/AGENTS.md`](../../openapi-surface/probes/AGENTS.md#re-running-one)
prescribes, generates the tree committed, comment-stripped, as the fixture's
[`fern-expected/`](../../openapi-surface/handwritten/closed-empty-inline-objects/fern-expected/).
It types `profile` `typing.Dict[str, typing.Any]` and examples it as the
free-form placeholder:

- `README.md` lines 45–47 and 68–70 (the sync and async snippets) and
  `reference.md` lines 24–26 write `profile={` / `"key": "value"` / `},`;
- `src/fern/firings/client.py` lines 65 and 167 (the sync and async method
  docstrings) write `profile={"key": "value"},`.

An explicit `example: {}` on the property does not change it: Fern writes the
same placeholder.

## Why it is a defect

The value is invalid for its own schema:

```text
$ uv run --no-project --with jsonschema python -c '
import jsonschema
s = {"type": "object", "additionalProperties": False}
for v in ({"key": "value"}, {}):
    try: jsonschema.validate(v, s); print(v, "valid")
    except jsonschema.ValidationError as e: print(v, "INVALID:", e.message)'
{'key': 'value'} INVALID: Additional properties are not allowed ('key' was unexpected)
{} valid
```

A snippet that sends it sends a body the API's own description forbids. An
example value invalid for its own schema is a defect under the defect rule. An
*open* object's `{"key": "value"}` is valid for its schema, so it stays Fern
behaviour and keeps matching.

## crozier's output

`crozier generate python --spec openapi.yml --package-name fern --project-name
default_package_name` writes the same tree but for those lines, where it passes
`profile={},` on one line. `crozier compare` over the two reports the README's
and `reference.md`'s three-line placeholders, and each docstring line, as this
departure and matches; the
`compare_reports_the_closed_empty_object_departure_and_fails_on_any_other_difference`
journey in `crates/crozier-e2e/tests/e2e/compare.rs` drives exactly that, and the fixture's
`closed-empty-object-example` rows in `tests/fixtures/departures-ledger.tsv` are
those lines.

The same departure applies to a registered real specification: cradl's
`post_models` requires `field_config`, a property closed with
`additionalProperties: false` that declares no `properties` and whose one
`patternProperties` pattern holds only objects (a `oneOf` of two object
schemas). Its golden examples it `{"key": "value"}` in `reference.md` and in
`client.py`'s two docstrings, and validating against the document's own schema
fails the same way:

```text
$ uv run --no-project --with jsonschema python - <<'PY'
import json, jsonschema
d = json.load(open("tests/fixtures/corpus-sources/cradl/openapi.json"))
fc = d["components"]["schemas"]["PostModels"]["properties"]["fieldConfig"]
for v in ({"key": "value"}, {}):
    try: jsonschema.validate(v, fc, resolver=jsonschema.RefResolver.from_schema(d)); print(v, "valid")
    except jsonschema.ValidationError as e: print(v, "INVALID:", e.message)
PY
{'key': 'value'} INVALID: 'value' is not valid under any of the given schemas
{} valid
```

Its `closed-empty-object-example` ledger rows are those three lines. A closed
object whose patterns might hold a string could admit Fern's placeholder, so
crozier keeps it there.
