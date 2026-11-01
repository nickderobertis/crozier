# `refusal-null-media-type`

Root cause `refusal-null-media-type` of [`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md),
triaged in [`../../empty-sdk-documents.tsv`](../../empty-sdk-documents.tsv).

**Rule.** A Media Type Object written as `null` (`image/png:` with no value) is
invalid OpenAPI. The certified pair fails to read it and writes its empty SDK.
By the user's design-review ruling `empty-sdk-refused` (2026-11-01): crozier refuses, in default and `fern-strict` modes, every document the certified pair turns into an empty SDK, because an empty SDK is useless, crozier refuses it in both modes as the new refusal class
[`null-media-type`](../../../../fern-refusals/null-media-type/evaluation.md).
Before this change crozier read the entry as empty and generated the whole SDK.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch: a kiln
monitor whose `GET /kiln/snapshot` answers `image/png:` with no value.

**Certified pair.** Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3
(`assets/scaffolding/metadata.json`), run under the shared Fern generation
lock through `tools/fern-goldens/fern-references.py`'s `run_fern` pipeline
(`fern check`, then `fern generate`, `enum_type: python_enums`). Each run's
complete tree went into the shared certified-tree cache under the SHA-256 of the
exact bytes. The committed `fern-expected/` is that tree, comment-stripped, and
`fern.log` is that run's log. The pair exits 0 and writes the 35-file empty SDK (`fern-expected/`).
[`fern.log`](fern.log) reads:

    [api]: Failed to parse openapi document Kiln Monitor
    [api]: Cannot read properties of null (reading 'schema')

The class's committed shapes add the same `null` in a request body (refused by
the pair) and an `image/png: {}` control (generated, 36 files).

**The real document.** `linux-automation/tacd:openapi.yaml@df3958c92643f7e0b06ef1830b9bc2a5e55ab24a`
(SHA-256 `b5dacb83849e3ef5b20249f712ed19ac60838e5052ce0a4de3b6c69aed29bd8c`).
The pair, run on its exact bytes, writes the same 35 files with the same
phrase. crozier on the finished tree refuses it by default and under
`--fern-strict`:

    crozier: invalid OpenAPI document …/tacd.yaml: null-media-type: paths//v1/tac/display/content/get/responses/200/content/image/png

**crozier.** It refuses `openapi.yml` in both modes, naming the class and the
pointer, and writes no tree. `crates/crozier-e2e/tests/e2e/empty_sdk_documents.rs` holds that, the request-body probe's refusal
and the control's generation.

**Verdict.** `user-ruling` (`empty-sdk-refused`).
