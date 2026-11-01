# `request-body-optionality`

The handed-off root cause `request-body-optionality` from the bodies-and-paths record ([`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md)), which names it as blocking tilecast; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** a required: false body that is an inline closed empty object is passed whole as a required request: Dict[str, Any], as the same object behind a $ref already was.

`openapi.yml` ("Lighthouse Lamp Log") was authored from scratch for this measurement. It holds a `required: false` body that is an inline closed empty object (`log_check`) beside one with an optional property (`log_trim`). `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `python3 tools/fern-goldens/fern-references.py generate measurements handed-off/bodies-media/request-body-optionality` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier made `log_check`'s `request` `typing.Optional[typing.Dict[str, typing.Any]] = None`. With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
