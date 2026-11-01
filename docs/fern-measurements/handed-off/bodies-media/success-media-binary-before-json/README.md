# `success-media-binary-before-json`

The handed-off root cause `success-media-binary-before-json` from the schemas record ([`witness-search-fixture-only-schemas`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md)), which names it as blocking gleez/nats-http-gateway; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** a success response any of whose media types carries a binary string schema is a download: its JSON alternative hoists no model and gives the method no worked example.

`openapi.yml` ("Herbarium Scans") was authored from scratch for this measurement. It holds a success offering a binary `application/text` string before an inline `application/json` object, on a `POST` with a JSON body. `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `python3 tools/fern-goldens/fern-references.py generate measurements handed-off/bodies-media/success-media-binary-before-json` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier hoisted a `RenderScanResponse` model from the JSON alternative and wrote a worked example; the certified pair reads the response as a download, so it declares no model and imports no example (its README is empty and `reference.md` shows `client.specimens.render_scan(...)`). With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
