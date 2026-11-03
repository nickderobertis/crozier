# `unresolved-reference`: the bodies-and-paths record's arm-server and PagerDuty false successes

The document group the bodies-and-paths record lists under
[The certified pair's false successes](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md#the-certified-pairs-false-successes) whose class is
[`unresolved-reference`](../../../../fern-refusals/unresolved-reference/evaluation.md),
triaged in [`../../empty-sdk-documents.tsv`](../../empty-sdk-documents.tsv).
The directory is named for the shape, since this node's
[`unresolved-reference/`](../unresolved-reference/README.md) holds the
refusal-parity record's section A.

**Rule.** A response whose `$ref` names something other than a
`components/responses` entry is one the pair cannot resolve. That covers
PagerDuty's `#/components/requestBodies/…` and arm-server's `#/$defs/400`. The
pair logs `Failed to parse openapi document` and `Failed to resolve <pointer>`,
exits 0 and writes the 35-file empty SDK. By the user's design-review ruling `empty-sdk-refused` (2026-11-01): crozier refuses, in default and `fern-strict` modes, every document the certified pair turns into an empty SDK, because an empty SDK is useless, crozier keeps refusing
it in both modes.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch: a seed
bank whose `replacePacket` answers `200` with
`$ref: '#/components/requestBodies/PacketBody'`, PagerDuty's form.
[`defs-pointer.yml`](defs-pointer.yml) is the same API answering `400` with
`$ref: '#/$defs/BadPacket'`, arm-server's form.

**Certified pair.** Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3
(`assets/scaffolding/metadata.json`), run under the shared Fern generation
lock through `tools/fern-goldens/fern-references.py`'s `run_fern` pipeline
(`fern check`, then `fern generate`, `enum_type: python_enums`). The committed
`fern-expected/` is that run's tree, comment-stripped, and `fern.log` is its
log. The pair exits 0 and writes the 35-file empty SDK for each:
[`fern.log`](fern.log) reads `[api]: Failed to resolve
#/components/requestBodies/PacketBody`, and
[`defs-pointer.fern.log`](defs-pointer.fern.log) reads `[api]: Failed to
resolve #/$defs/BadPacket`.

**The real documents.** Each was fetched at its recorded revision and its
SHA-256 verified. The pair's run on each is the committed population log at
the pair, named below. The record names PagerDuty `84fcb3ad…` at
`…/2.0.0/openapi.json`, which serves those bytes; `documents.tsv` locates the
same digest at `…/meta/import/input-bundle.json`.

| document | SHA-256 | the pair (recorded log at the pair) | crozier on the finished tree |
|---|---|---|---|
| `beeequeue/arm-server:docs/openapi.yaml@86c9359fc9df49b9d42cf21dc67bdc99b1658fbf` | `79211321295936c435fd6781a48695018d2645aa2e2d5d539626eadb3eb0c17c` | exit 0, `Failed to resolve #/$defs/400` ([check](../../../../openapi-surface/fern-refusals/logs/79211321295936c435fd6781a48695018d2645aa2e2d5d539626eadb3eb0c17c.check.log), [generate](../../../../openapi-surface/fern-refusals/logs/79211321295936c435fd6781a48695018d2645aa2e2d5d539626eadb3eb0c17c.generate.log)) | refused by default and under `--fern-strict`, no tree: `unresolved-reference: paths//api/ids/get/responses/400: #/$defs/400` |
| `jentic/jentic-public-apis:apis/openapi/pagerduty.com/pagerduty-api/2.0.0/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `84fcb3ada8922a0a9c2ffe8efa6a93e7c35998ccda9db5d0f42fd340a8b1a936` | exit 0, `Failed to resolve #/components/requestBodies/OrchestrationCacheVariableDataPutResponse` ([check](../../../../openapi-surface/fern-refusals/logs/84fcb3ada8922a0a9c2ffe8efa6a93e7c35998ccda9db5d0f42fd340a8b1a936.check.log), [generate](../../../../openapi-surface/fern-refusals/logs/84fcb3ada8922a0a9c2ffe8efa6a93e7c35998ccda9db5d0f42fd340a8b1a936.generate.log)) | refused in both modes, no tree: `unresolved-reference: paths//event_orchestrations/{id}/cache_variables/{cache_variable_id}/data/put/responses/200: #/components/requestBodies/OrchestrationCacheVariableDataPutResponse` |
| `jentic/jentic-public-apis:apis/openapi/pagerduty.com/pagerduty-api/2.0.0/meta/import/input-entry.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `a0f7d0ded3d88daa940ed8b6e8fd1534c9f2c12752457e7d5b71f4c5f0d3f2b0` | exit 0, the same ([check](../../../../openapi-surface/fern-refusals/logs/a0f7d0ded3d88daa940ed8b6e8fd1534c9f2c12752457e7d5b71f4c5f0d3f2b0.check.log), [generate](../../../../openapi-surface/fern-refusals/logs/a0f7d0ded3d88daa940ed8b6e8fd1534c9f2c12752457e7d5b71f4c5f0d3f2b0.generate.log)) | refused in both modes, no tree, the same element |

**crozier.** It refuses both probes by default and under `--fern-strict`,
naming `unresolved-reference` and the pointer, and writes no tree (`crates/crozier-e2e/tests/e2e/empty_sdk_documents.rs`).

**Verdict.** `user-ruling` (`empty-sdk-refused`).
