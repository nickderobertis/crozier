# `environment-shape`

Root cause `environment-shape` of [`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** Servers declared on path items, named by `x-fern-server-name`, apply to their operations and build Fern's multi-URL environment; a path server that is one of the document's top-level servers reads `base`.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. Two named top-level servers (`Production`, `Archive`) and three path items: `/nights` and `/plates` name a top-level server, `/alerts` one of its own.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes a `FernApiEnvironment` class with fields `base`, `production`, `archive` and `alerts`, two members assigned without blank lines between them, `environment` kept in the client wrapper, and `base_url=...get_environment().base` on `/nights` and `/plates` but `.alerts` on `/alerts`.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier ignored the path-item servers and wrote a single-URL enum and a `base_url` client argument.
`crozier compare` against the tree then reported these files differing:
['src/fern/alerts/raw_client.py', 'src/fern/client.py', 'src/fern/core/client_wrapper.py', 'src/fern/environment.py', 'src/fern/nights/raw_client.py', 'src/fern/plates/raw_client.py'].

**Change.** `src/openapi.rs` gains one private `PathItem.servers` field, consumed by `normalize_parameters` (copied into every operation declaring none, then emptied); `src/ir.rs::environment_field` reads `base` for any top-level server; `src/emit.rs::environment_file` no longer blank-separates member assignments. The private field was approved by the manager on the terms that no public type or IR shape changes.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file. [`runtime.txt`](runtime.txt) records both SDKs sending the same requests through `httpx.MockTransport`.

**Verdict.** `parity-gap-repaired`.
