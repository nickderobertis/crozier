# `R12`

Root cause `R12` of [`witness-search-fixture-only-operations-extensions`](../../../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** A request body that `$ref`s a component marked `x-fern-ignore` keeps its operation, typed `typing.Any` and passed whole (an array of them is `typing.Sequence[typing.Any]`).

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. `create_snippet` and `create_snippets` post the ignored `SnippetInput` (once directly, once as array items); `get_snippet` does not.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes the `snippets` client with `request: typing.Any` and `request: typing.Sequence[typing.Any]`.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier found both operations unemittable and wrote no `snippets` client, only its `__init__.py`.
`crozier compare` against the tree then reported these files differing:
['README.md', 'reference.md', 'src/fern/__init__.py', 'src/fern/client.py'].

**Change.** `src/openapi.rs::filter_ignored` rewrites a request-body reference to a removed component as an untyped schema.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
