# `subpackage-order`

Root cause `subpackage-order` of [`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** A package's sub-clients are ordered by the first operation that belongs directly to each child; a child holding only nested operations comes last.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. Four operations declare nested groups in this order: `[library, loans, renewals]`, `[library, archive, boxes]`, `[library, members]`, `[library, loans]`.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes `library`'s children `members`, `loans`, `archive`, in that order.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier ordered them `loans`, `members`, `archive`, placing `loans` at the first operation of its child `renewals`.
`crozier compare` against the tree then reported these files differing:
['reference.md', 'src/fern/library/client.py'].

**Change.** `src/emit.rs::module_children` registers an endpoint-owning child at its own first operation only.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
