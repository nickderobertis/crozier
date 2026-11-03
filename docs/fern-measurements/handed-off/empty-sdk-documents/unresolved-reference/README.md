# `unresolved-reference`: section A of the refusal-parity record

The document group of [`refusal-parity-ten-documents.md`](../../../../refusal-parity-ten-documents.md),
section A ("a `$ref` into another path's definition"), triaged in
[`../../empty-sdk-documents.tsv`](../../empty-sdk-documents.tsv) under its
refusal class.

**Rule.** A response's or a parameter's `$ref` into another path's definition is
one the certified pair cannot resolve: it writes its 35-file empty SDK. By
the user's design-review ruling `empty-sdk-refused` (2026-11-01): crozier refuses, in default and `fern-strict` modes, every document the certified pair turns into an empty SDK, because an empty SDK is useless, crozier keeps refusing it in both modes as
[`unresolved-reference`](../../../../fern-refusals/unresolved-reference/evaluation.md).

**Document.** [`openapi.yml`](openapi.yml), authored from scratch: the
tide-gauge API, whose `listReadings` lists
`$ref: '#/paths/~1gauges/get/parameters/0'` among its parameters. That is the
form of propresenter-remote and Codat. The response form, DigitalOcean's,
dggs' and pro7.9's, is
[`../crozier-refuses-path-pointer-ref/response-pointer.yml`](../crozier-refuses-path-pointer-ref/README.md).

**Certified pair.** Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3
(`assets/scaffolding/metadata.json`), run under the shared Fern generation
lock through `tools/fern-goldens/fern-references.py`'s `run_fern` pipeline
(`fern check`, then `fern generate`, `enum_type: python_enums`). Each run's
complete tree went into the shared certified-tree cache under the SHA-256 of the
exact bytes. The committed `fern-expected/` is that tree, comment-stripped, and
`fern.log` is that run's log. The pair exits 0 and writes the 35-file empty SDK (`fern-expected/`);
[`fern.log`](fern.log) reads `[api]: Failed to parse openapi document Tide
Gauges` and `[api]: Failed to resolve #/paths/~1gauges/get/parameters/0`.

**The real documents.** Each was run through the pair on its exact bytes, SHA-256
verified:

| document | SHA-256 | the pair | crozier on the finished tree |
|---|---|---|---|
| APIs.guru `APIs/digitalocean.com/2.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `5bd3a4800c4396372cb80d99cc82b49463e4a3f136b63d1794c19f13da37cf63` | exit 0, 35 files, `Failed to resolve #/paths/~1v2~11-clicks/get/responses/401` | refused in both modes, at `#/paths/~1v2~11-clicks/get/responses/401` |
| `dltkddnr04/propresenter-remote:openapi/propresenter.openapi.json@b273aeec98db96f4766d0b4e0d2a8305627396a4` | `44695afa34c9d6e1fce938a62844cf07b30ed296a5e3d2be1779827947394219` | exit 0, 35 files, `Failed to resolve #/paths/~1v1~1looks/get/parameters/0` | refused in both modes, at that pointer |
| `jeffmikels/ProPresenter-API:pro7.9.openapi-spec.json@6e7490671c94a7c9e588274bdf5df6ece1934248` | `694f7ec93b5aafa776ab61f7e049432f2ac01f8db5ffce4aedbde9f1a38616cc` | exit 0, 35 files, `Failed to resolve #/paths/~1version/get/responses/404` | refused in both modes, at that pointer |

The record's account is current. Before this change crozier refused DigitalOcean
first at a header pointer; it now resolves that one, as the pair does, and
refuses at the response pointer the pair fails on.

**crozier.** It refuses `openapi.yml` by default and under `--fern-strict`,
naming `unresolved-reference` and the pointer, and writes no tree (`crates/crozier-e2e/tests/e2e/empty_sdk_documents.rs`).

**Verdict.** `user-ruling` (`empty-sdk-refused`).
