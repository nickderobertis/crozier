# `readme-endpoint-choice`

The handed-off root cause `readme-endpoint-choice` from [`docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

A kiln log lists `GET /kilns` (a required query), then `POST /kilns/firings`, a multipart upload whose body is `$ref: FiringUpload` (a required binary `controller_log` and a required string `kiln`), then `POST /kilns/glazes` with an inline JSON body.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/snippet-rendering/readme-endpoint-choice` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair's README demonstrates `record_firing`, the first `POST`, with `controller_log="example_controller_log"`; crozier treated a referenced file form as ineligible and demonstrated `add_glaze`. The record's nullable optional file variant is held by the NVIDIA usd-content-agents document, which now byte-matches (`../README.md`).

**Verdict: `parity-gap-repaired`.** `readme_endpoint_eligible` no longer excludes a referenced multipart form with a file part; crozier's tree byte-matches `fern-expected/`. Every registered corpus golden still byte-matches.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`). `src/emit.rs`'s `the_readme_demonstrates_the_first_post_even_when_it_uploads_a_referenced_file_form` drives `readme_endpoint_eligible` and `readme_endpoint` on this document.
