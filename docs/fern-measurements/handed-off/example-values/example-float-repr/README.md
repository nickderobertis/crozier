# `example-float-repr`

The handed-off root cause `example-float-repr` from [`docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`POST /calibrations` declares `gain: 0.9345407030264767` (17 significant digits) and two more floats. `openapi.json` beside it is the same document as JSON; crozier picks its reader by extension and the defect lived in its JSON reading.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py generate measurements handed-off/example-values/example-float-repr` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`runtime.txt` records the run the verdict rests on.

## The comparison

At this node's base, crozier's output for both spellings byte-matches `fern-expected/`; `runtime.txt` records crozier built at `d9c34ef08` (the parent of `e4eec3d65`) writing `0.9345407030264768` for the JSON spelling.

**Verdict: `already-matching`, cleared by `e4eec3d65` ("read a JSON document's float literals at their correctly rounded value", enabling serde_json's `float_roundtrip`).** The record's document (`ourofoundation/wrappers` timegpt, sha256 `9165e7b9…`) byte-matches its certified-pair tree at this base.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
