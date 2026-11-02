# `param-oneof-ref-and-const-example`

The handed-off root cause `param-oneof-ref-and-const-example` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`POST /watches/{watchId}/end` takes a path parameter `oneOf: [$ref WatchId, {const: every}]`, and `GET /watches` a query parameter `oneOf: [{const: mine}, $ref WatchId]`; `WatchId` declares `examples: [7c1e2a90-…]`.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py generate measurements handed-off/example-values/param-oneof-ref-and-const-example` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`expected-literals/fern-expected/` is the same document generated with `enum_type` unset (the `literals` mode), reduced to an overlay of `fern-expected/` (the files that differ, and `.crozier-overlay.json` naming the files Fern omits); its `cases.tsv` row is `handed-off/example-values/param-oneof-ref-and-const-example/expected-literals`.

## The comparison

The certified pair works both from `WatchId`'s example, wherever the `const` sits; crozier wrote the `const` (`"every"`, `…ScopeZero.MINE`).

**Verdict: `default-matched`.** Both values are declared by the author, so no ruling's principle applies; crozier matches the pair (`ir::parameter_example_value`, `emit::ExampleCtx::union_parameter_string_example`), byte-matching `fern-expected/` and the `expected-literals/` overlay.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/` and its literals tree with `expected-literals/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`, `handed_off_example_value_literals_overlays_match_fern`).
