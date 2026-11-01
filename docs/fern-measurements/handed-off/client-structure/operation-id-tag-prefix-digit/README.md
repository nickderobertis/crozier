# `operation-id-tag-prefix-digit`

Root cause `operation-id-tag-prefix-digit` of [`witness-search-fixture-only-schemas`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** An operationId that is not purely camelCase (here one with a digit) is one word until punctuation splits it, so a tag spelling only its start strips nothing: the method keeps the whole id.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. `aliasVal2`, `aliasList` and `aliasV3` under `alias`.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes `alias_val2`, `list` and `alias_v3`.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier wrote `val2` and `v3`.
`crozier compare` against the tree then reported these files differing:
['README.md', 'reference.md', 'src/fern/alias/client.py', 'src/fern/alias/raw_client.py'].

**Change.** The `method-name-derivation` rule (`src/ir.rs::tag_location`).

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
