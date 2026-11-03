# `example-map-of-model-values`

The handed-off root cause `example-map-of-model-values` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

An archive finder's `POST /records/search` body has `filters`, a map whose values are `oneOf: [string array, $ref Span, array of $ref Span]`, and `bounds`, a map of `Span`; its request example gives `filters` one of each value shape.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/snippet-rendering/example-map-of-model-values` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair writes the array of spans as `Span(from_=…, to=…)` constructors; crozier wrote compact JSON dicts (`{"from":"1921-01-01",…}`), because its union matching took any array as the first alternative, `List[str]`, and printed each object as a string.

**Verdict: `parity-gap-repaired`.** `example_matches_type_through` now admits an array for a list type only when every item fits the item type, so the array of objects selects `List[Span]`. crozier's tree byte-matches `fern-expected/`; every registered corpus golden still byte-matches.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`). `src/emit.rs`'s `a_union_alternative_list_takes_an_array_only_when_every_item_fits` holds the `Span` constructors and the string list.
