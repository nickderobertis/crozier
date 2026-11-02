# `example-placeholder-shape`

The handed-off root cause `example-placeholder-shape` from [`docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

Three bodies whose schema an array example does not fit: `{type: object, additionalProperties: {}}` with a named example of strings, the same with `propertyNames` and an optional body exampled with objects (SeekStorm's `index_document` shape), and a bare `{type: object, format: json}` (Cyoda's `createCollection` shape).

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py generate measurements handed-off/example-values/example-placeholder-shape` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair turns each array example into the object keyed by index (`{"0": "focus", "1": "tilt"}`), in every writer, and puts one entry per line in the README; crozier wrote `{"key": "value"}` (and a list for the bare object's docstring). The record's `{"string": {"key": "value"}}` on SeekStorm is that document's importer fallback (its other named example nests arrays), not this rule.

**Verdict: `default-matched`.** No ruling names it and both sides synthesize, so crozier matches the pair (`ir::index_keyed_map_example`); its tree byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
