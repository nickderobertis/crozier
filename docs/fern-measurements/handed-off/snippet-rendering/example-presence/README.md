# `example-presence`

The handed-off root cause `example-presence` from [`docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

A darkroom service's binary and upload operations: an argument-less `GET` downloading `application/octet-stream` that declares a JSON `404` (`get_contact_sheet`) and one that declares no error (`get_archive`); a `PUT` whose multipart form's only part is an optional file, with a named media example (`replace_scan`); and three multipart uploads of one required file: answering JSON without a path parameter (`upload_negative`), answering JSON with one (`add_proof`), and answering `text/plain` (`flash_enlarger`).

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/snippet-rendering/example-presence` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair writes a worked example for `get_contact_sheet` (docstrings and `reference.md`), none for `get_archive`, one for `replace_scan` (`reference.md` passes `scan="example_scan"`, the docstrings only `print_id`), one for `upload_negative` and `add_proof`, and none for `flash_enlarger`, whose `reference.md` usage is the bare `client.darkroom.flash_enlarger(...)`. crozier wrote none for `get_contact_sheet` and `replace_scan` and a worked one for `flash_enlarger`; `get_archive` already matched (cleared for real documents by `630240929`, #722). The two JSON uploads' docstrings carry the catalogued `multipart-object-required-file-example` correction.

**Verdict: `parity-gap-repaired`.** `endpoint_has_worked_example` keeps the argument-less binary `GET`'s example when it declares an error, keeps the opaque-multipart example of a form whose only part is an optional file, and drops the example of a required-file upload answering `text/plain` (the shape `byte-text-response-reference-snippet` measures for `format: byte`). crozier's tree byte-matches `fern-expected/` with the catalogued departure applied. Every registered corpus golden still byte-matches.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`). `src/emit.rs`'s `worked_example_presence_follows_the_download_and_upload_shapes` drives `endpoint_has_worked_example` on each operation and reads the `reference.md` and docstring lines; `snippet_departures_and_repairs_hold_only_their_lines` fails the worked `flash_enlarger` call crozier wrote before the repair.
