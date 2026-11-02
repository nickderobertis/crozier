# `crozier-refuses-path-pointer-ref`

Root cause `crozier-refuses-path-pointer-ref` of [`witness-search-fixture-only-schemas`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md),
triaged in [`../../empty-sdk-documents.tsv`](../../empty-sdk-documents.tsv).

**The contradiction, settled.** The schemas record said that Fern resolves a
`$ref` into `#/paths/…` and generates DigitalOcean, while
[`refusal-parity-ten-documents.md`](../../../../refusal-parity-ten-documents.md)
(section A) said the pair writes the empty scaffold. The pair was run again on
each exact document of the cause, SHA-256 verified:

| document | SHA-256 | outcome | `fern.log` excerpt |
|---|---|---|---|
| APIs.guru `APIs/digitalocean.com/2.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `5bd3a4800c4396372cb80d99cc82b49463e4a3f136b63d1794c19f13da37cf63` | empty scaffold: exit 0, 35 files | `[api]: Failed to parse openapi document DigitalOcean API` / `[api]: Failed to resolve #/paths/~1v2~11-clicks/get/responses/401` |
| `ogcincubator/developer-website-v3:api/dggs/openapi.yaml@d123c2c2df80940a8af30f9dd2a45c382a7ecff7` | `9ccb483ad815ad25c876c7317b7edfb167452a6325164887cc888b67aa49a382` | empty scaffold: exit 0, 35 files | `[api]: Failed to parse openapi document Building Blocks specified in OGC API - Discrete Global Grid Systems - Part 1: Core` / `[api]: Failed to resolve #/paths/~1dggs~1%7BdggsId%7D~1zones~1%7BzoneId%7D/get/responses/200` |
| `jentic/jentic-public-apis:apis/openapi/codat.io/sync-for-expenses/prealpha/openapi.json@1700c576aa658b5dc3bd06cb376cc959d84e12f8` | `827e170f0c2a997418cfe3682b68f42cd81481396d663c0013d5ddae00128679` | empty scaffold: exit 0, 35 files | `[api]: Failed to parse openapi document Sync for Expenses API` / `[api]: Failed to resolve #/paths/~1companies~1{companyId}~1sync~1expenses~1syncs/parameters/0` |

None of the three is generated in full, so the refusal-parity record is right
and the schemas record was wrong. Its entry is corrected in place. All three are
refused by crozier by default and under `--fern-strict`, as `unresolved-reference`
at their response or parameter pointer, under the user's design-review ruling `empty-sdk-refused` (2026-11-01): crozier refuses, in default and `fern-strict` modes, every document the certified pair turns into an empty SDK, because an empty SDK is useless.

**Where the schemas record's claim held.** DigitalOcean's first pointer in
crozier's order is a header's (`ratelimit-limit`, defined on another
operation's response). Measured alone, the pair resolves a header pointer and
generates the whole SDK, so crozier's refusal of it was a parity gap:

- **Document.** [`openapi.yml`](openapi.yml), authored from scratch: a tide-gauge
  API whose `listReadings` 200 response declares
  `X-Rate-Remaining: {$ref: '#/paths/~1gauges/get/responses/200/headers/X-Rate-Remaining'}`.
  **Certified pair.** Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3
(`assets/scaffolding/metadata.json`), run under the shared Fern generation
lock through `tools/fern-goldens/fern-references.py`'s `run_fern` pipeline
(`fern check`, then `fern generate`, `enum_type: python_enums`). Each run's
complete tree went into the shared certified-tree cache under the SHA-256 of the
exact bytes. The committed `fern-expected/` is that tree, comment-stripped, and
`fern.log` is that run's log. The pair generates 42 files (`fern-expected/`), and its log carries
  no error.
- **[`response-pointer.yml`](response-pointer.yml).** The same document with a
  `404` response `$ref` into the other path instead. The pair exits 0 over it
  and writes the 35-file empty SDK; [`response-pointer.fern.log`](response-pointer.fern.log)
  reads `[api]: Failed to resolve #/paths/~1gauges/get/responses/404`. The
  parameter form is [`../unresolved-reference/`](../unresolved-reference/README.md).

**Change.** `path_header_pointer` in `src/document_refusals.rs` lets a header's
`$ref` into `#/paths/<route>/<method>/responses/<code>/headers/<name>` pass
`check_reference_objects`'s collection check, provided its target exists. A
header pointer naming no header, and every response or parameter pointer into
`#/paths/`, stay `unresolved-reference`. Response headers reach no generated
file, so nothing else changes. The refusal lived in the structural checker,
not in `src/refs.rs`, which resolves only references to other documents.

**Comparison on the finished tree.** crozier's output for `openapi.yml`
byte-matches `fern-expected/` apart from the departures the ledger records, by
default and under `--fern-strict`. The document declares no enum, so
`python_enums` is the only tree. `crates/crozier-e2e/tests/e2e/empty_sdk_documents.rs` holds that, and refuses the response
pointer and a dangling header pointer in both modes. Unit tests of
`path_header_pointer` and the structural check are in `src/document_refusals.rs`.

**Verdict.** `parity-gap-repaired` for the header pointer, the shape the record
named. The cause's three documents stay refused under `empty-sdk-refused`.
