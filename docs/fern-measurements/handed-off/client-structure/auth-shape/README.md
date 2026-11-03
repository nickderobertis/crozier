# `auth-shape`

Root cause `auth-shape` of [`witness-search-fixture-only-bodies-paths`](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), triaged in
[`../../client-structure.tsv`](../../client-structure.tsv).

**Rule.** A header `apiKey` scheme carrying `x-bearer-format` (any value) sends its key behind `Bearer `; two additional header `apiKey` schemes naming one header are one credential. A scheme sharing the primary key's header stays its own (the hand-written `twin-key-relay` fixture, and `docs/openapi-surface/probes/securityscheme-ref.yml` regenerated at the certified pair into the shared cache, both show two).

**Document.** [`openapi.yml`](openapi.yml), authored from scratch for this
measurement. The primary scheme is an `Authorization` header key with `x-bearer-format: bearer`; `agentHeader` and `proxyAgent` both name `X-Desk-Agent`.

**Certified pair.** `fern-expected/` (`enum_type: python_enums`) is the complete, comment-stripped tree Fern CLI
5.163.1 with `fernapi/fern-python-sdk` 5.41.3 freshly generated from
`openapi.yml` through `tools/fern-goldens/fern-references.py`'s
`generated_tree` pipeline (the one the `measurements` family uses), under the
shared Fern generation lock. It writes `headers["Authorization"] = f"Bearer {self.api_key}"` and one `desk_agent` argument, assignment, header line and docstring entry.

**crozier before.** Built at this node's base, `6b4509ab9`, crozier sent the raw key and duplicated the `desk_agent` argument, assignment, header line and docstring entry.
`crozier compare` against the tree then reported these files differing:
['src/fern/client.py', 'src/fern/core/client_wrapper.py'].

**Change.** `src/openapi.rs`'s `SecurityScheme` gains one `pub(crate)` `x-bearer-format` field (manager-approved), read by `src/ir.rs::auth_model`; `src/ir.rs::additional_api_key_global_headers` skips an additional scheme whose header an earlier additional scheme already sent.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches the tree, held by
`crates/crozier-e2e/tests/e2e/client_structure.rs`, which also writes back the
pre-change form of the deciding line and requires the comparison to name the
file. [`runtime.txt`](runtime.txt) records both SDKs sending the same requests through `httpx.MockTransport`.

**Verdict.** `parity-gap-repaired`.
