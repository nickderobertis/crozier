# `path-param-serialization`

The handed-off root cause `path-param-serialization` from the bodies-and-paths record ([`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md)), which names it as blocking walletd; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** a path union with a member outside Fern's httpx data primitives (an int64, uint32 or uint64 integer, a float number, a dated, uuid or byte string) is converted through convert_and_respect_annotation_metadata before encode_path_param.

`openapi.yml` ("Ledger Block Explorer") was authored from scratch for this measurement. It holds a path parameter typed `oneOf: [string with pattern, integer with format uint64]`. `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `python3 tools/fern-goldens/fern-references.py generate measurements handed-off/bodies-media/path-param-serialization` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier interpolated `encode_path_param(id)`; the certified pair converts the `GetBlockRequestId` union first, because `uint64` is not among the primitives fern-python-sdk sends as plain data (the same union over a format-less `integer` is interpolated directly). With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
