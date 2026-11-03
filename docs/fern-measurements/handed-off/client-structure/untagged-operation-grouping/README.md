# `untagged-operation-grouping`

Root cause `untagged-operation-grouping` of [`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** An operation declaring `x-fern-sdk-method-name` and no `x-fern-sdk-group-name` is the root client's method whatever its `tags`.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. `bookStay` is tagged `Stays` and names its method `book_stay` without a group; `listStays` and `getStay` are plain `Stays` operations.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes the root client's `book_stay` (`client.book_stay(...)`), beside `client.stays.list_stays` and `client.stays.get_stay`.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier put `book_stay` on the `stays` sub-client, the group its tag names.
`crozier compare` against the tree then reported these files differing:
['README.md', 'reference.md', 'src/fern/client.py', 'src/fern/stays/client.py', 'src/fern/stays/raw_client.py'].

**Change.** `src/ir.rs::declared_group` reads a declared method name with no group as the root group (`[]`).

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
