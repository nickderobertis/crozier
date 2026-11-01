# `reference-section-title`

Root cause `reference-section-title` of [`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** A section grouped by a snake_case operationId prefix that spells a tag the document declares is titled with the tag verbatim.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. The declared tag `Draft Filings` with `draft_filings_list` and `draft_filings_read`, and an undeclared `archive` tag with `archive_list`.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes `## Draft Filings` (and `## Archive`).

**crozier before.** Built at this node's base, `6b4509ab9`, crozier titled it `## DraftFilings`.
`crozier compare` against the tree then reported these files differing:
['reference.md'].

**Change.** `src/ir.rs::module_title` returns the declared tag for a prefix-grouped section.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
