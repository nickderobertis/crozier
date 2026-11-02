# `schema-examples-array-parameter-value`

The handed-off root cause `schema-examples-array-parameter-value` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`GET /lamps/{lampId}` and `GET /lamps/{lampId}/manual` (which answers `application/xml`, so the certified pair's importer declines its example) take path, query and `$ref`'d component query parameters whose schemas declare only a 3.1 `examples` array; `PATCH /lamps/{lampId}/settings` takes the same path parameter beside a body shaped like vercel's `update_record` (a `properties` map holding a literal `additionalProperties: false` entry).

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py generate measurements handed-off/example-values/schema-examples-array-parameter-value` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair works every parameter from its `examples` array on the first two operations, including the XML one (where crozier wrote the name: a parity gap, repaired), and writes the name `lamp_id="lampId"` on the vercel-shaped one, where crozier writes `lmp_8f2kq`.

**Verdict: `user-ruling` (design-review ruling 5, `declared-examples-array`).** crozier keeps the array's entry on the vercel-shaped operation, as the catalogued `kind: usefulness` departure `declared-examples-array-parameter-value`; the XML operation's path parameter is repaired to read its inline schema's example as the pair does (`ir::schema_level_parameter_example`). With the departure applied, crozier's tree byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
`ruled_example_values_are_what_crozier_writes` asserts the lines crozier writes where a ruling keeps or changes its value, and `declared_value_departures_hold_only_their_lines` shows an adjacent unexplained change still fails.
