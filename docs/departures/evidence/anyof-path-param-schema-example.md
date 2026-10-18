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

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, in the workspace
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds (`organization: fern`,
`pydantic_config.enum_type: python_enums`, `fern generate --group python-sdk
--local --preview`), exits 0; the comment-stripped tree is the case's
`fern-expected/`. Its `README.md`, `reference.md` and both `get_dock`
docstrings pass `dock_id_or_code="dock_id_or_code"`.

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
dock_id_or_code example 'northbasin' valid against {"anyOf": [{"type": "string", "minLength": 4, "maxLength": 16, "pattern": "^[a-z]+$", "example": "northbasin"}, {"type": "string", "format": "uuid"}]}
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
