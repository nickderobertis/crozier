# `falsy-property-example`

The handed-off root cause `falsy-property-example` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`POST /buoys` takes a required header `X-Survey-Ref` declaring `example: ""` and a multipart body whose parts declare `label: ""`, `depth_metres: 0` and `harbour: north-basin`; `POST /buoys/{buoyId}/readings` takes a path parameter declaring `example: ""`, a required query parameter declaring `example: 0`, and a JSON body whose properties declare `""` and `0`.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/example-values/falsy-property-example` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair discards the multipart parts' examples, the header's and the path parameter's `""`, writing `label="label"`, `depth_metres=1`, `harbour="harbour"`, `survey_ref="X-Survey-Ref"` and `buoy_id="buoyId"`; it keeps the JSON body's `""` and `0`, and writes `berth=1` for the query parameter's `0`. crozier writes every declared value except the query parameter's (where it writes `1`, as the pair does).

**Verdict: `user-ruling` (design-review ruling 2, `falsy-property-example`).** crozier keeps the declared `""` and `0`, as the catalogued `kind: usefulness` departure `declared-example-over-placeholder` (`docs/departures/evidence/declared-example-over-placeholder.md`). With it applied, crozier's tree byte-matches `fern-expected/`. On the record's document (openapi-thrift) the falsy values also break the parts' `minLength`/`minimum`; the ruling keeps them regardless.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
`ruled_example_values_are_what_crozier_writes` asserts the lines crozier writes where a ruling keeps or changes its value, and `declared_value_departures_hold_only_their_lines` shows an adjacent unexplained change still fails.
