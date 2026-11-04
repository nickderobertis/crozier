# `R10`

Root cause `R10` of [`witness-search-fixture-only-operations-extensions`](../../../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** A discriminated union and its variant wrappers are imported in one statement in `types/__init__.py`, at the union's place.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. `PaymentRequestSource`, a discriminated union of `PaymentRequestSourceTag` and `PaymentRequestSourceCard`, whose member modules sort between the union's and its wrappers' names.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) and `expected-literals/` (Fern's default literals; the document declares enums) are the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes `from .payment_request_source import PaymentRequestSource, PaymentRequestSource_Card, PaymentRequestSource_Tag`.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier split it into two statements around the member modules; alone that was absorbed by `init-type-checking-import-order` (so at the base this document compares clean only through the departure), but beside any other change to the block, as in darwin-cli, the file differed.
`crozier compare` against the tree then reported these files differing:
[].

**Change.** `src/emit.rs::module_grouped_imports` gathers every name a module exports into one statement. 57 ledger lines of `init-type-checking-import-order` stopped applying (regenerated with `just departures-ledger`); ruling 7's order is unchanged, since names stay sorted and only statements of one module merge.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree and in literals mode, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
