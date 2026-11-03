# `unresolved-reference`: the Setu documents

The document group [`fern-refusals/unresolved-reference/evaluation.md`](../../../../fern-refusals/unresolved-reference/evaluation.md)
records (Setu), triaged in [`../../empty-sdk-documents.tsv`](../../empty-sdk-documents.tsv)
under its refusal class.

**Rule.** An error response naming a `components/responses` entry the document
never declares is one the certified pair cannot resolve: it writes its 35-file
empty SDK. By the user's design-review ruling `empty-sdk-refused` (2026-11-01): crozier refuses, in default and `fern-strict` modes, every document the certified pair turns into an empty SDK, because an empty SDK is useless, crozier keeps refusing it in both modes as
`unresolved-reference`.

**Document.** [`openapi.yml`](openapi.yml), authored from scratch: a ferry
timetable whose `listSailings` answers
`'400': {$ref: '#/components/responses/BAD_PORT'}` with no `BAD_PORT` declared.

**Certified pair.** Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3
(`assets/scaffolding/metadata.json`), run under the shared Fern generation
lock through `tools/fern-goldens/fern-references.py`'s `run_fern` pipeline
(`fern check`, then `fern generate`, `enum_type: python_enums`). Each run's
complete tree went into the shared certified-tree cache under the SHA-256 of the
exact bytes. The committed `fern-expected/` is that tree, comment-stripped, and
`fern.log` is that run's log. The pair exits 0 and writes the 35-file empty SDK (`fern-expected/`);
[`fern.log`](fern.log) reads `[api]: Failed to parse openapi document Ferry
Timetable` and `[api]: Failed to resolve #/components/responses/BAD_PORT`.

**The real documents.** Each was run through the pair on its exact bytes, SHA-256
verified:

| document | SHA-256 | the pair | crozier on the finished tree |
|---|---|---|---|
| `jentic/jentic-public-apis:apis/openapi/setu.co/main/1.0.0/openapi.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `d2dc23e9de5690536e870a5719d6bd9d2afc25349a30ec1bcd06d05526370414` | exit 0, 35 files, `Failed to resolve #/components/responses/BAD_REQUEST` | refused in both modes, `paths//users/login/post/responses/400: #/components/responses/BAD_REQUEST` |
| `jentic/jentic-public-apis:apis/openapi/setu.co/main/1.0.0/meta/import/input-entry.json@eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `be0196359ca1794934d5c9622d42d608da3426b1f993db7c91e995b7a54815f7` | exit 0, 35 files, the same | refused in both modes, the same |

The bodies-and-paths record's
[false successes](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md#the-certified-pairs-false-successes)
holds these two and five more documents, triaged as rows of their own:

- both Stripe documents, in [`../extension-reference-cycle/`](../extension-reference-cycle/README.md);
- arm-server and both PagerDuty documents, in
  [`../response-outside-responses/`](../response-outside-responses/README.md).

**crozier.** It refuses `openapi.yml` by default and under `--fern-strict`,
naming `unresolved-reference` and the pointer, and writes no tree (`crates/crozier-e2e/tests/e2e/empty_sdk_documents.rs`).

**Verdict.** `user-ruling` (`empty-sdk-refused`).
