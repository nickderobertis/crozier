# `map-body-media-example`

The handed-off root cause `map-body-media-example` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`PUT /lanterns/{lanternId}/labels` posts a string map with a media `example`; `POST /lanterns/{lanternId}/notes` posts `{type: object, additionalProperties: true}` with a nested media `example` (notehub's legacy webhook event).

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/example-values/map-body-media-example` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair passes both examples' entries (one per line in the README); crozier passed `{"key": "value"}` for the free-form map.

**Verdict: `parity-gap-repaired`.** The IR now takes a free-form map body's media example and the README lays it out per entry; crozier's tree byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
