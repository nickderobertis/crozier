# `multi-status-success-return-type`

The handed-off root cause `multi-status-success-return-type` from the schemas record ([`witness-search-fixture-only-schemas`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md)), which names it as blocking langfuse_sdk; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** an operation whose only success is 207 returns nothing: Fern reads no 2xx status but 200, 201, 202 and 204.

`openapi.yml` ("Orchard Harvest Ledger") was authored from scratch for this measurement. It holds an operation whose only success is `207`. `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `python3 tools/fern-goldens/fern-references.py generate measurements handed-off/bodies-media/multi-status-success-return-type` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier typed the method by the `207` (`-> BatchOutcome`). With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
