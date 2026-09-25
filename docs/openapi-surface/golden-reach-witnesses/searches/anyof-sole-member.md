# Arm search: `anyof-sole-member`

The unreached handling site(s) searched for: `src/ir.rs::InlineHoister::hoist_array_item_type[if members.len\(\) == 1 && is_inline_struct]`.
Read with: `schema.anyOf:sole-member`.

A walked or fetched document declaring the row is a `document` row of the
source's `records.tsv`; one whose instrumented `crozier generate` executes
an unreached site above is a `candidate`, and only a candidate owes the
licence, ref and fern screens. A probe counts only if it ran the instrumented
build of commit `8a9454cb74d0`, the one the reach ledger is measured on,
with `src/` at that commit; a declarer with no such probe is unprobed and
outstanding, and a re-probe needs `src/` at that commit (or a fresh
`just golden-reach`). Probes run before that rule was enforced read shifted
spans and are not counted. The outcome is this search's own reading;
final reconciliation decides whether the arm's search reads `exhausted`.

### Witness search (exhaustive)

| key | source | outcome | queries | walk | candidates | screens |
|---|---|---|---|---|---|---|
| `anyof-sole-member` | `apis.guru` | `search-incomplete` | — | `APIs-guru/openapi-directory` at `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` → 4138 documents | — | — |
| `anyof-sole-member` | `jentic` | `search-incomplete` | — | `jentic/jentic-public-apis` at `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` → 74240 documents | — | — |
| `anyof-sole-member` | `github-code-search` | `search-incomplete` | `\anyOf\"" "\"items\"" "\"requestBody\"" "\"array\"" filename:openapi.json` → 0; `anyOf: "items:" "requestBody:" "type: array" filename:openapi.yaml` → 4832 | — | — | — |
| `anyof-sole-member` | `github-publisher-trees` | `search-incomplete` | — | `Adyen/adyen-openapi` at `f82d1fe674e536cc2c6b0d7946e0e827873a4fbf` → 258 documents; `github/rest-api-description` at `3cef12e8a02d612ad032473d4fb87266f2befeae` → 65 documents; `kubernetes/kubernetes` at `b0e6417568f530e79579c5bcd6bbeac799a47669` → 65 documents; `mongodb/openapi` at `1e4aeea7d2d63f749bcae619cf836fbe52c62447` → 63 documents; `twilio/twilio-oai` at `5aa7f31977ce5812f7b7bc1f46a38555ebaa2888` → 120 documents | `descriptions-next/ghes-3.1/dereferenced/ghes-3.1.deref.json`, `descriptions-next/ghes-3.1/dereferenced/ghes-3.1.deref.yaml`, `descriptions-next/ghes-3.1/ghes-3.1.json`, `descriptions-next/ghes-3.1/ghes-3.1.yaml` | `descriptions-next/ghes-3.1/dereferenced/ghes-3.1.deref.json` licence `passed` ref `passed` fern `failed: Fern CLI 5.67.1 / python-sdk 5.20.0 check reports 38 errors, e.g. Expected example to be an object. Example is: undefined`; `descriptions-next/ghes-3.1/dereferenced/ghes-3.1.deref.yaml` licence `passed` ref `passed` fern `failed: Fern CLI 5.67.1 / python-sdk 5.20.0 check reports 38 errors, e.g. Expected example to be an object. Example is: undefined`; `descriptions-next/ghes-3.1/ghes-3.1.json` licence `passed` ref `passed` fern `failed: Fern CLI 5.67.1 / python-sdk 5.20.0 check reports 24 errors, e.g. Expected example to be an object. Example is: undefined`; `descriptions-next/ghes-3.1/ghes-3.1.yaml` licence `passed` ref `passed` fern `failed: Fern CLI 5.67.1 / python-sdk 5.20.0 check reports 24 errors, e.g. Expected example to be an object. Example is: undefined` |
| `anyof-sole-member` | `sourcegraph` | `search-incomplete` | `file:(openapi\|swagger).*\.(yaml\|yml)$ content:"items:" content:"anyOf:" content:"requestBody:" count:all type:file` → 2038; `file:(openapi\|swagger).*\.json$ content:"\"items\"" content:"\"anyOf\"" content:"\"requestBody\"" count:all type:file` → 2589 | — | `github.com/lehhair/OpenCodeUI:openapi_doc.json@8a6d4eae9424317f01e88f3819b14b24e57bab10`, `github.com/lehhair/OpenCodeUI:openapi_formatted.json@8a6d4eae9424317f01e88f3819b14b24e57bab10` | `github.com/lehhair/OpenCodeUI:openapi_doc.json@8a6d4eae9424317f01e88f3819b14b24e57bab10` licence `passed` ref `passed` fern `passed`; `github.com/lehhair/OpenCodeUI:openapi_formatted.json@8a6d4eae9424317f01e88f3819b14b24e57bab10` licence `passed` ref `passed` fern `passed` |
| `anyof-sole-member` | `vendor-portals` | `search-incomplete` | — | `Adyen/adyen-openapi` at `f82d1fe674e536cc2c6b0d7946e0e827873a4fbf` → 259 documents; `Redocly/museum-openapi-example` at `2770b2b2e59832d245c7b0eb0badf6568d7efb53` → 6 documents; `advplyr/audiobookshelf` at `0a797ab8bee15dc3ca92d1d76155259c46dbec62` → 95 documents; `apache/superset` at `485008224719a7b42162429fccb4a910347c532b` → 1515 documents; `asana/openapi` at `700bc9a7970c747209137f83aae07923e7477574` → 6 documents; `box/box-openapi` at `933ec4c5d9f4dbdaaa823efa3a083cf177aecbde` → 14 documents; `cloudflare/api-schemas` at `f2df0ca75c0fec9047e91a34c20dd666c2dcd1ba` → 4 documents; `codatio/oas` at `2dbdc1f7bcdefaf769ab17fcc99fbb098ef2610b` → 43 documents; `cohere-ai/cohere-developer-experience` at `c26cd7f411d63adb703b92ab2653e77b537c0e40` → 123 documents; `digitalocean/openapi` at `e3df8b7958867470943845c80b5d4c6fc2edff3b` → 2925 documents; `discord/discord-api-spec` at `e54b849b5c10f74ad1db4fd4ec219e3ef382cbe8` → 2 documents; `docker/docker-py` at `afc6d1ee308e78b908b96a94298c37fa8c465588` → 8 documents; `drakkan/sftpgo` at `c737df6cd42ef375bf51a2d0a04ea2b1ab9f8842` → 20 documents; `dropbox/dropbox-api-spec` at `6d985dfaf901f1a909aa5e268bcfa524b0b7966e` → 3 documents; `github/rest-api-description` at `3cef12e8a02d612ad032473d4fb87266f2befeae` → 398 documents; `gotson/komga` at `656001eb03bf8b54ca909f3e74fe2ec1b95dac48` → 87 documents; `intercom/Intercom-OpenAPI` at `3d5adcb2eeb0df209d83035c2f5bc69c932b2644` → 48 documents; `kubernetes/kubernetes` at `b2ec8b6fefac451a2dedafc4dd71f2f16c7a6abe` → 7706 documents; `mongodb/openapi` at `20d74e290115694fd3efd36e2f1cd46869bc8483` → 466 documents; `openai/openai-openapi` at `b53b169f44dc0fbf878db3f9a1d3b66f43831f8d` → 2 documents; `stripe/openapi` at `58e06a3214ae1574600fba64d40b770e5da6d505` → 31 documents; `traccar/traccar` at `b15554cf3f9808dc462d412834896fe0634a4e0e` → 7 documents; `twilio/twilio-oai` at `ef1d81e7b6e49e602530601e913eedc21aedd6da` → 133 documents; `webflow/openapi-spec` at `f6db607359a412dd6aa6cd304674731d7f2dbe10` → 2 documents; `zulip/zulip` at `6a82f40579f8adb9149aa0b04ff795c397baae73` → 2 documents | — | — |

#### Declarers, and how the instrumented run fared on each

Counted off each source's `records.tsv` and `probe.jsonl`, probes of the
build `8a9454cb74d0` only. A declarer not probed on it, one whose run
did not finish (a timeout), and one crozier failed on without a profile are
outstanding: the arm may be in them, and nothing here says otherwise.

| source | declarers | unreadable | probed | unprobed | timed out | crozier failed | reach an arm | screened |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `apis.guru` | 6 | 0 | 6 | 0 | 0 | 2 | 0 | 0 |
| `jentic` | 196 | 0 | 196 | 0 | 5 | 40 | 0 | 0 |
| `github-code-search` | 3 | 8 | 3 | 0 | 0 | 0 | 0 | 0 |
| `github-publisher-trees` | 5 | 8 | 0 | 5 | 0 | 0 | 0 | 0 |
| `sourcegraph` | 16 | 3 | 16 | 0 | 0 | 4 | 2 | 2 |
| `vendor-portals` | 118 | 58 | 0 | 118 | 0 | 0 | 0 | 0 |

#### Candidates passing every screen

- **Hand-off** (see [`handoff.tsv`](../handoff.tsv)): <https://raw.githubusercontent.com/lehhair/OpenCodeUI/8a6d4eae9424317f01e88f3819b14b24e57bab10/openapi_doc.json>, declaring `gap` row(s) anyof-anyof-variant — passed: Fern CLI 5.67.1 / python-sdk 5.20.0 generated 399 files; crozier byte-matched all 399 locally after nine repairs kept in src/ with tests/generation.rs tests an_untagged_dotted_operation_id_hangs_off_the_root_client, the_readme_walks_the_root_client_after_its_sub_clients, a_schema_named_for_a_raised_error_class_is_its_body, a_required_const_status_discriminates_a_ref_union, a_union_member_map_names_its_value, a_union_of_one_schema_written_twice_is_that_schema, a_hoisted_models_map_of_inline_objects_names_its_value, a_query_parameter_beside_a_body_keeps_the_content_type_header
- **Declined** (`sourcegraph`): `github.com/lehhair/OpenCodeUI:openapi_formatted.json@8a6d4eae9424317f01e88f3819b14b24e57bab10` — the same API as the handed-off openapi_doc.json in the same repository and commit, formatted differently; the hand-off stands for both
