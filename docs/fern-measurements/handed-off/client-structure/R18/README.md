# `R18`

Root cause `R18` of [`witness-search-fixture-only-operations-extensions`](../../../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** Required `content-length` and `x-forwarded-for` header parameters reach neither the client wrapper nor a method; another required header is promoted as usual.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. `placeOrder` declares required `content-length`, `x-forwarded-for` and `x-channel` headers.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes no `content_length` or `x_forwarded_for` anywhere, and `channel` on the client wrapper.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier already matched: crozier built at this node's base byte-matches the tree, as it does corpus row 3479 (`vtex-marketplace-protocol`).
`crozier compare` against the tree then reported these files differing:
[].

**Change.** None. The commit that cleared it is `de440bc03` (#669, the `vtex-output-parity` node).

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `already-matching`.
