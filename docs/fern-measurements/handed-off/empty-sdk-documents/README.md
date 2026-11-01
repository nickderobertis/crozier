# Handed-off area `empty-sdk-documents`

The documents the certified pair (Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3) turns into an empty SDK: it exits 0 over the
35-file scaffold, and its log reads `Failed to parse openapi document`. Beside
them are the same-class causes the fixture-only searches handed off. Each row of
[`../empty-sdk-documents.tsv`](../empty-sdk-documents.tsv) is decided, with its
measurement directory here. The user's design-review ruling `empty-sdk-refused`
(2026-11-01) applies to every empty SDK: crozier refuses it in default and
`fern-strict` modes, because an empty SDK is useless. The exception is valid
OpenAPI whose empty SDK is only a Fern limitation and whose crozier SDK passes
evaluation. The registry records the ruling as an
[intended departure](../../../fern-refusals/README.md#intended-departures).

Every certified-pair run below took the exact bytes, its SHA-256 verified
against the source record, under the shared Fern generation lock. Every
comparison is on the finished tree.

| document | revision | SHA-256 | cause | the pair | crozier on the finished tree |
|---|---|---|---|---|---|
| APIs.guru `APIs/digitalocean.com/2.0/openapi.yaml` | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | `5bd3a4800c4396372cb80d99cc82b49463e4a3f136b63d1794c19f13da37cf63` | `crozier-refuses-path-pointer-ref`, `unresolved-reference` | empty SDK | refused in both modes, `unresolved-reference` |
| `ogcincubator/developer-website-v3` `api/dggs/openapi.yaml` | `d123c2c2df80940a8af30f9dd2a45c382a7ecff7` | `9ccb483ad815ad25c876c7317b7edfb167452a6325164887cc888b67aa49a382` | `crozier-refuses-path-pointer-ref` | empty SDK | refused in both modes, `unresolved-reference` |
| `jentic/jentic-public-apis` `apis/openapi/codat.io/sync-for-expenses/prealpha/openapi.json` | `1700c576aa658b5dc3bd06cb376cc959d84e12f8` | `827e170f0c2a997418cfe3682b68f42cd81481396d663c0013d5ddae00128679` | `crozier-refuses-path-pointer-ref` | empty SDK | refused in both modes, `unresolved-reference` |
| `dltkddnr04/propresenter-remote` `openapi/propresenter.openapi.json` | `b273aeec98db96f4766d0b4e0d2a8305627396a4` | `44695afa34c9d6e1fce938a62844cf07b30ed296a5e3d2be1779827947394219` | `unresolved-reference` (section A) | empty SDK | refused in both modes, `unresolved-reference` |
| `jeffmikels/ProPresenter-API` `pro7.9.openapi-spec.json` | `6e7490671c94a7c9e588274bdf5df6ece1934248` | `694f7ec93b5aafa776ab61f7e049432f2ac01f8db5ffce4aedbde9f1a38616cc` | `unresolved-reference` (section A) | empty SDK | refused in both modes, `unresolved-reference` |
| `jentic/jentic-public-apis` `apis/openapi/setu.co/main/1.0.0/openapi.json` | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `d2dc23e9de5690536e870a5719d6bd9d2afc25349a30ec1bcd06d05526370414` | `unresolved-reference` (Setu) | empty SDK | refused in both modes, `unresolved-reference` |
| `jentic/jentic-public-apis` `apis/openapi/setu.co/main/1.0.0/meta/import/input-entry.json` | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | `be0196359ca1794934d5c9622d42d608da3426b1f993db7c91e995b7a54815f7` | `unresolved-reference` (Setu) | empty SDK | refused in both modes, `unresolved-reference` |
| `vickz84259/lolesports-api-docs` `openapi.yaml` | `74027a7950c7e4629d3cab01ddd3990457a9956d` | `5737ba80e2e41e0bdf0f3e9079dcd757c16553d3f120b3f6d8bba6f3dc782d9c` | `R1` | empty SDK (its example builder overflows) | generates 243 files in both modes, the valid-OpenAPI exception; not compared, since the pair writes nothing to compare with |
| `linux-automation/tacd` `openapi.yaml` | `df3958c92643f7e0b06ef1830b9bc2a5e55ab24a` | `b5dacb83849e3ef5b20249f712ed19ac60838e5052ce0a4de3b6c69aed29bd8c` | `R1`, `refusal-null-media-type` | empty SDK | refused in both modes, `null-media-type` |
| `outstack/enveloper` `docs/api/openapi.yaml` | `cd8150d6d78c64ff48acdfb886c833a4600515df` | `95595ff60c5a51617e5bd497fb94eeba13e6b3566c271b5bf59403a5789145bf` | `missing-relative-file` (section E) | generates 44 files | byte-matches apart from catalogued departures (see [`missing-relative-file`](missing-relative-file/README.md)) |

The bodies-and-paths record's five other false successes were not re-run here:
two Stripe documents (`extension-reference-cycle`), `beeequeue/arm-server` and
two PagerDuty documents (`unresolved-reference`). Their `documents.tsv` rows
record crozier's strict refusal, and the ruling applies to them unchanged.

Each measurement directory holds a probe document authored from scratch
(`openapi.yml`), the certified pair's fresh output for it (`fern-expected/` and
`fern.log`), and a `README.md` stating the comparison and the verdict.
`crates/crozier-e2e/tests/e2e/empty_sdk_documents.rs` drives the real binary
over every probe in both modes.
