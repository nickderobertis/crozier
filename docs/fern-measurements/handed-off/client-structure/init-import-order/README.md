# `init-import-order`

Root cause `init-import-order` of [`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** Ruling 7 (`init-import-order`): no change. The certified pair orders a lazy `__init__.py`'s type-checking imports by module path; crozier keeps its own sorted order, and the catalogued departure absorbs the permutation.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. Two tag packages, `arboretum` and `yew_walk`, each re-exporting a hoisted enum at the root, a named environment and a root type, so the root block's order differs between the two generators.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) and `expected-literals/` (Fern's default literals; the document declares enums) are the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes the root `__init__.py` with `.arboretum`, `.client`, `.environment`, `.version` and `.yew_walk` interleaved by module path.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier the same statements in crozier's order (it still does: the output for this cause is unchanged).
`crozier compare` against the tree then reported these files differing:
[].

**Change.** None. `crozier compare` applies `init-type-checking-import-order` to `src/fern/__init__.py` in both enum modes and the trees then byte-match.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree and in literals mode, with the catalogued departures applied, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `user-ruling` (departure `init-type-checking-import-order`).
