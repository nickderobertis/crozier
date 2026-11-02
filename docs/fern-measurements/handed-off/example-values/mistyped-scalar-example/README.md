# `mistyped-scalar-example`

The handed-off root cause `mistyped-scalar-example` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`POST /depots` declares `postcode: string` with `example: 40213`, `capacity: int64` with `example: "900"`, `code: string` with `examples: [551188]`, and `aliases` items with `examples: [7781, west quay]`; `POST /depots/compare` gives `level: number` the string `"3"` in its media example; `DELETE /depots/purge` gives a `string` body a list example.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/example-values/mistyped-scalar-example` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair discards each value of the wrong JSON type: `postcode="postcode"`, `capacity=1000000`, `code="code"`, `aliases=["west quay"]` (the first fitting entry), `level=1.1`, `request="string"`. crozier wrote the mistyped values, which their own schemas reject.

**Verdict: `parity-gap-repaired`.** crozier was the side writing invalid values; `ir::typed_schema_example`, `ir::scalar_example_fits` and the emit-side guards now discard them, and its tree byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
