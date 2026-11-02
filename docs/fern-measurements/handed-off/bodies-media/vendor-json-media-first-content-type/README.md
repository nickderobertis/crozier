# `vendor-json-media-first-content-type`

The handed-off root cause `vendor-json-media-first-content-type` from the schemas record ([`witness-search-fixture-only-schemas`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md)), which names it as blocking visualstudio.com; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** the first JSON key in declaration order is read, so an application/*+json declared before application/json is the body's media type, and a key holding * names no content type.

`openapi.yml` ("Greenhouse Climate Control") was authored from scratch for this measurement. It holds bodies offering `application/*+json` before `application/json` (a spread object, `set_targets`, and an array, `submit_readings`). `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `just fern-references measurements handed-off/bodies-media/vendor-json-media-first-content-type` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier preferred the `application/json` key and sent `content-type: application/json`; the certified pair reads the first JSON key, whose `*` names no content type. With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
