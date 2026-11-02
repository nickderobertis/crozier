# `multipart-encoding-content-type-list`

The handed-off root cause `multipart-encoding-content-type-list` from the schemas record ([`witness-search-fixture-only-schemas`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md)), which names it as blocking craftgo; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** a file part's default content type is its encoding contentType up to the first comma, untrimmed; a value part keeps the whole value.

`openapi.yml` ("Botanical Illustration Uploads") was authored from scratch for this measurement. It holds a file part whose `encoding.contentType` lists `image/png, image/jpeg, image/tiff`. `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `just fern-references measurements handed-off/bodies-media/multipart-encoding-content-type-list` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier sent the whole list as the default content type. With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
