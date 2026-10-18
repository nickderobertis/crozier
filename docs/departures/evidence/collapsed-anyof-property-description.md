# `collapsed-anyof-property-description`

**Kind:** `richer-documentation`. An object property declaring a description
beside an `anyOf` of two inline string alternatives that both sides type as one
`str`: Fern keeps the first alternative's schema and documents nothing, crozier
documents the property's own description.

## The input

[`marina-skipper-refs/openapi.yml`](../../fern-measurements/examples-docs/marina-skipper-refs/openapi.yml),
a crozier-authored document whose `CharterBooking` (posted as a flattened body)
and `Charter` (returned as a model) each declare the required property
`skipper: {anyOf: [{type: string, format: uuid}, {type: string}], description:
"The skipper's ID or licence number."}`. The real LangChain agent server API
declares the same shape on `assistant_id` of `RunCreateStateful`,
`RunCreateStateless`, `CronCreate` and `ThreadCronCreate`.

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, in the workspace
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds, exits 0; the
comment-stripped tree is the case's `fern-expected/`. `types/charter.py`
declares `skipper: str`, both `book_charter` docstrings list `skipper : str`
with no description, and `reference.md` reads ``**skipper:** `str` `` .

## Both sides are valid; crozier's documents the declared description

```text
fern     types/charter.py:10   skipper: str
crozier  types/charter.py:10   skipper: str = pydantic.Field()
crozier  types/charter.py:12   The skipper's ID or licence number.
fern     reference.md:40       **skipper:** `str`
crozier  reference.md:40       **skipper:** `str` — The skipper's ID or licence number.
```

The source declares the description on the property, not on its first
alternative:

```text
Charter skipper description: "The skipper's ID or licence number." | first member description: None
```

Validating with each tree's own model (`Charter.model_validate`), both accept
`{"skipper": "LIC-2231", "vessel": "Tern"}` as a `str` and both reject a body
without `skipper` (`ValidationError`): the type and requiredness are identical,
and crozier's adds only the specification's text.

## The parity rule

On an aligned pair of lines, the rule accepts a `reference.md` parameter row
that Fern ends bare and crozier ends with the property's description, and a
model field Fern declares `<name>: <type>` that crozier declares
`<name>: <type> = pydantic.Field()`. On lines only crozier writes, it accepts
the description lines under a docstring's `<name> : <type>` entry, and the
docstring block (with the blank line after it) that follows such a model field,
when their text is that description. Each needs the parsed source document to
declare such a property: an `anyOf`/`oneOf` of two or more inline non-null
scalar alternatives, the first undescribed, with the description on the
property. `examples_docs_measurements_match_fern` and
`examples_docs_cases_fail_on_an_adjacent_unexplained_byte` in
`crates/crozier-e2e/tests/e2e/examples_docs.rs` hold the case; the line ledger
is recorded from `src/parity.rs`, never hand-edited.
