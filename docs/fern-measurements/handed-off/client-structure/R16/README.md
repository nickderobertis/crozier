# `R16`

Root cause `R16` of [`witness-search-fixture-only-operations-extensions`](../../../../openapi-surface/witness-search-fixture-only-operations-extensions/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** A tag named `core` writes its group's clients into the runtime `core/` package: its `__init__.py` stays the runtime's, the group's clients import the runtime as siblings (`.client_wrapper`) and are formatted like every other generated client.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. A `core` tag with `get_status` beside a `files` tag.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes `core/__init__.py` exporting the runtime, and `core/client.py`/`core/raw_client.py` importing `.client_wrapper`, `.request_options`, `.api_error` and friends.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier overwrote `core/__init__.py` with the group's empty one and imported `..core.client_wrapper`.
`crozier compare` against the tree then reported these files differing:
['src/fern/core/__init__.py', 'src/fern/core/client.py', 'src/fern/core/raw_client.py'].

**Change.** `src/emit.rs` leaves the runtime `core/__init__.py` in place for a group of that name, `Imports::core_prefix` resolves the runtime as siblings there, and `format_python_files` formats the group's `client.py`/`raw_client.py`.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file.

**Verdict.** `parity-gap-repaired`.
