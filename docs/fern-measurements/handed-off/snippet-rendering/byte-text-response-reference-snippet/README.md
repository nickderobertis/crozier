# `byte-text-response-reference-snippet`

The handed-off root cause `byte-text-response-reference-snippet` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

A film lab's `POST /reels/{reelId}/develop/{pass}` uploads one required file and answers `text/plain` `{type: string, format: byte}` (declaring a JSON `404`); `POST /reels/{reelId}/notes` uploads one required file and answers a plain `text/plain` string; `GET /reels/{reelId}/log` takes no body and answers `text/plain` bytes.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/snippet-rendering/byte-text-response-reference-snippet` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair's `reference.md` gives both uploads the bare `client.reels.<method>(...)` usage and their docstrings no `Examples` section, and works the `GET`. crozier worked both uploads.

**Verdict: `parity-gap-repaired`.** The rule is the upload's, not the response format's alone: a multipart upload with a required file part answering `text/plain`, a string or `format: byte`, gets no worked example (`endpoint_has_worked_example`, shared with `example-presence`'s `flash_enlarger`); a `text/plain` byte answer without a file upload keeps its example. crozier's tree byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`). `src/emit.rs`'s `worked_example_presence_follows_the_download_and_upload_shapes` holds the three operations and the bare `develop_reel(...)` usage.
