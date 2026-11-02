# `extension-reference-cycle`: the bodies-and-paths record's Stripe false successes

The document group the bodies-and-paths record lists under
[The certified pair's false successes](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md#the-certified-pairs-false-successes) whose class is
[`extension-reference-cycle`](../../../../fern-refusals/extension-reference-cycle/evaluation.md),
triaged in [`../../empty-sdk-documents.tsv`](../../empty-sdk-documents.tsv).

**Rule.** An extension whose value reaches a `$ref` back into the schema that
carries it, through an object member (Stripe's
`x-stripeProperty.referenced_resource`), sends the pair's importer into
unbounded recursion. It logs `Failed to parse openapi document` and `Maximum
call stack size exceeded`, exits 0 and writes the 35-file empty SDK. By
the user's design-review ruling `empty-sdk-refused` (2026-11-01): crozier refuses, in default and `fern-strict` modes, every document the certified pair turns into an empty SDK, because an empty SDK is useless, crozier keeps refusing it in both modes.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch: an allotment
ledger whose `handOverPlot` body property `tenant` carries
`x-ledgerProperty.names_resource: {$ref: Tenant}`, and whose `Tenant.id`
carries the same extension back to `Tenant`.

**Certified pair.** Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3
(`assets/scaffolding/metadata.json`), run under the shared Fern generation
lock through `tools/fern-goldens/fern-references.py`'s `run_fern` pipeline
(`fern check`, then `fern generate`, `enum_type: python_enums`). The committed
`fern-expected/` is that run's tree, comment-stripped, and `fern.log` is its
log. The pair exits 0 and writes the 35-file empty SDK; [`fern.log`](fern.log)
reads `[api]: Failed to parse openapi document Allotment Ledger` and
`[api]: Maximum call stack size exceeded`.

**The real documents.** Each was fetched at its recorded revision and its
SHA-256 verified. The pair's run on each is the committed population log at
the pair, named below:

| document | SHA-256 | the pair (recorded log at the pair) | crozier on the finished tree |
|---|---|---|---|
| `stripe/openapi:preview/openapi.spec3.sdk.json@58e06a3214ae1574600fba64d40b770e5da6d505` | `60caefaab927e1b1b4a42125a5309a50300bb17552c2f5f8794108e9a7d529d4` | exit 0, `Maximum call stack size exceeded` ([check](../../../../openapi-surface/fern-refusals/logs/60caefaab927e1b1b4a42125a5309a50300bb17552c2f5f8794108e9a7d529d4.check.log), [generate](../../../../openapi-surface/fern-refusals/logs/60caefaab927e1b1b4a42125a5309a50300bb17552c2f5f8794108e9a7d529d4.generate.log)) | refused by default and under `--fern-strict`, no tree: `extension-reference-cycle: paths//v2/core/account_links/post/requestBody/content/application/json/schema/properties/account/x-stripeProperty` |
| `stripe/openapi:latest/openapi.spec3.sdk.json@58e06a3214ae1574600fba64d40b770e5da6d505` | `92363b86025d012852f648554372bf5fa6146af1472fb63f3c29d7c5fe6bd19a` | exit 0, `Maximum call stack size exceeded` ([check](../../../../openapi-surface/fern-refusals/logs/92363b86025d012852f648554372bf5fa6146af1472fb63f3c29d7c5fe6bd19a.check.log), [generate](../../../../openapi-surface/fern-refusals/logs/92363b86025d012852f648554372bf5fa6146af1472fb63f3c29d7c5fe6bd19a.generate.log)) | refused in both modes, no tree, the same element |

**crozier.** It refuses `openapi.yml` by default and under `--fern-strict`,
naming `extension-reference-cycle` and the extension's pointer, and writes no
tree (`crates/crozier-e2e/tests/e2e/empty_sdk_documents.rs`).

**Verdict.** `user-ruling` (`empty-sdk-refused`).
