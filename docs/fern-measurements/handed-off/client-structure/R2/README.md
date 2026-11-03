# `R2`

Root cause `R2` of [`witness-search-fixture-only-operations-extensions`](../../../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** A path parameter that does not declare `required: true` is `typing.Optional[...]`, still positional and interpolated; `reference.md` lists it among the optional parameters, and a docstring's worked call names the required path arguments first.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. A shared `components.parameters` `site` and `shelf` without `required`, beside a required `key`, on a binary-body `PUT` and a `DELETE` with a required query parameter.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes `site: typing.Optional[str]` and `shelf: typing.Optional[str]`, listed after `key` and the body in `reference.md`, and `key=` first in the docstring calls.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier typed both `str` and kept them in declaration order everywhere.
`crozier compare` against the tree then reported these files differing:
['reference.md', 'src/fern/client.py', 'src/fern/raw_client.py'].

**Change.** `src/ir.rs` wraps such a parameter's type in `TypeRef::Optional`; `src/emit.rs::reference_entry` lists optional path rows with the optional parameters, and the docstring example writer orders required path arguments first.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
