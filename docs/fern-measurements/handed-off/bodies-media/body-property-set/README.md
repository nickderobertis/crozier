# `body-property-set`

The handed-off root cause `body-property-set` from the bodies-and-paths record ([`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md)), which names it as blocking wxpusher; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** an inline allOf member carrying its own anyOf of non-object branches is a union to Fern, so the composed body takes neither its properties nor its required.

`openapi.yml` ("Courier Dispatch Board") was authored from scratch for this measurement. It holds a `$ref` body whose `allOf` joins a base `$ref` and an inline member that declares `route`, `courierToken` and `courierId`, requires `route`, and carries an `anyOf` of required-only branches. `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `just fern-references measurements handed-off/bodies-media/body-property-set` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier merged `route`, `courier_token` and `courier_id` into the body; the certified pair keeps only the base's `parcel` and `fragile`. With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
