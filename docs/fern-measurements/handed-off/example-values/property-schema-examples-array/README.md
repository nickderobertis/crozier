# `property-schema-examples-array`

The handed-off root cause `property-schema-examples-array` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`PlotRequest.waypoints` (`type: array` of strings) declares a 3.1 `examples` array whose entry holds a string with a double quote (`hold at "Wolf Rock"`), beside `vessel` and `legs` declaring `examples` too.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/example-values/property-schema-examples-array` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair passes the entry; crozier fell back to `["waypoints"]` because its literal spelled that string with single quotes, which its example parser could not read (SandboxFusion's `print("…")`).

**Verdict: `parity-gap-repaired`.** `emit::parse_example_value` reads a single-quoted Python string; crozier's tree byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
