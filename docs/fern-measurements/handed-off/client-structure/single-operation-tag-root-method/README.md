# `single-operation-tag-root-method`

Root cause `single-operation-tag-root-method` of [`witness-search-fixture-only-schemas`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** An operationId whose words are its tag's words is the root client's method, named by the tag.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. `invoiceMatch` under the declared tag `Invoice Match`, beside an `Expenses` tag with two operations.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes `client.invoice_match(...)` on the root client.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier wrote `client.invoice_match.invoice_match(...)`.
`crozier compare` against the tree then reported these files differing:
['README.md', 'reference.md', 'src/fern/__init__.py', 'src/fern/client.py'].

**Change.** The `method-name-derivation` rule (`src/ir.rs::tag_location`, `TagLocation::Root`).

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
