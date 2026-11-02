# `R5`

The handed-off root cause `R5` from the operations-and-extensions record ([`witness-search-fixture-only-operations-extensions`](../../../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md)), which names it as blocking unicourt; the documents, revisions and SHA-256s are listed in [`../README.md`](../README.md).

**The rule:** an error body that $refs a nullable: true component is Optional[Component], as the same reference is in a success response.

`openapi.yml` ("Canal Lock Keeper") was authored from scratch for this measurement. It holds a `404` whose body `$ref`s a `nullable: true` object component. `fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3) freshly generated from it under `python_enums`, through `tools/fern-goldens/fern-references.py`'s own `generated_tree` (the measurements family's generation), called on this `openapi.yml` with `python-enums` and the packaged layout, under the shared Fern lock. The cause's name, `R5`, is upper-case, which `cases.tsv` does not admit as a case name, so it has no row there. No enum-mode overlay is kept: the rule does not turn on the enum mode.

**The comparison.** Before the repair crozier typed `NotFoundError`'s body `LockFault`. With the repair, `crozier compare` (every catalogued departure applied) reports crozier's tree for this document byte-identical to `fern-expected/`, and `bodies_media.rs` in `crates/crozier-e2e` holds it there, showing that the decisive line written as crozier wrote it before fails the comparison.

**Verdict:** `parity-gap-repaired`. Recorded in [`../../bodies-media.tsv`](../../bodies-media.tsv).
