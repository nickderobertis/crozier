# `optional-lowered-required-query-array-example`

**Kind:** `richer-documentation`. A required query array that both signatures
take as an optional argument, on an operation whose worked call Fern writes
without required query arrays: where the parameter declares an array example,
crozier passes it and Fern leaves the parameter out. Where it declares none,
crozier leaves it out too and matches Fern.

## The input

[`marina-tide-channels/openapi.yml`](../../fern-measurements/examples-docs/marina-tide-channels/openapi.yml),
a crozier-authored document with two operations, each taking a required query
array `gauges` (`items: {type: number}`) beside a required query parameter
`since` whose `anyOf` is led by an untyped `type: Timestamp` member, which both
sides example as the unknown placeholder `{"key": "value"}`:

- `GET /tides/{station_id}` declares no example for `gauges`. Both sides leave
  it out. The real rice-shower controller API's `getThermoMetrics` and
  `getHeaterMetrics` are this shape, and crozier matches Fern there.
- `GET /tides/{station_id}/surge` declares `example: [3, 7]` on the `gauges`
  schema.

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, in the workspace
`tools/fern-goldens/generate-fern-fixture.sh` scaffolds, exits 0; the
comment-stripped tree is the case's `fern-expected/`. Both signatures read
`gauges: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None`,
and every worked call of `get_surge` omits `gauges`, declared example or not.

## Both sides are valid; crozier's documents the declared example

Binding every worked call of `get_surge` in each tree's client docstrings and
`reference.md` to the package's own method:

```text
fern     {"station_id": "'station_id'", "since": "{'key': 'value'}"}                         binds
crozier  {"station_id": "'station_id'", "gauges": "[3.0, 7.0]", "since": "{'key': 'value'}"}  binds (docstring)
crozier  {"station_id": "'station_id'", "gauges": "[3, 7]", "since": "{'key': 'value'}"}      binds (reference.md)
```

Validating the declared example with `jsonschema` 4.26.0:

```text
gauges required example [3, 7] valid against {"type": "array", "items": {"type": "number"}}
```

The specification marks `gauges` required; crozier's call passes the value it
declares for it. A synthesized `[1.1]` would be no declared content, so
`get_tides` has none.

## The parity rule

The rule accepts a line only crozier writes in `README.md`, `reference.md` or a
high-level `client.py` when it belongs to a list argument — `<name>=[a, b],` on
one line, or `<name>=[` through `],` with one item per line — whose items
equal, value for value, the array example the parsed source document declares
for a required `type: array` query parameter passed as `<name>`. A list that is
not the declared example, a nested list, or a missing source document leaves
the line a difference. `examples_docs_measurements_match_fern` and
`examples_docs_cases_fail_on_an_adjacent_unexplained_byte` in
`crates/crozier-e2e/tests/e2e/examples_docs.rs` hold the case; the line ledger
is recorded from `src/parity.rs`, never hand-edited.
