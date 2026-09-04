# Canonical real-world OpenAPI corpus (issue #77)

This manifest tracks the real-world OpenAPI specs with redistribution-compatible
license metadata. `decision` is `link-ok` when the permissively licensed source
is fetched at generation time rather than vendored. Add or change one numbered
row per feature branch and maintain its golden through the manually dispatched
**Fern goldens** workflow; see
[`../../docs/fern-goldens.md`](../../docs/fern-goldens.md).

Every row registered in `tests/e2e.rs` reproduces its Fern 5.20.0 golden
byte-for-byte, with the single accepted upstream exception noted in the batch 4
table (`calorieninjas.com`). A row registered without a golden and without that
exception is a hard harness error, so this ledger records history — which
selections were dropped and why — rather than any outstanding match work. The
measured state is `tests/e2e.rs`; re-measure with `just fixtures-gaps`.

| # | name | method | source | pinned ref | license | decision | shapes |
|---:|---|---|---|---|---|---|---|
| 1 | `6-dot-authentiqio.appspot.com` | api-guru | https://api.apis.guru/v2/specs/6-dot-authentiqio.appspot.com/6/openapi.json | `6` | Apache 2.0 | link-ok | Authentiq API |
| 2 | `airbyte.local-config` | api-guru | https://api.apis.guru/v2/specs/airbyte.local/config/1.0.0/openapi.json | `1.0.0` | MIT | link-ok | Airbyte Configuration API |
| 3 | `anchore.io` | api-guru | https://api.apis.guru/v2/specs/anchore.io/0.1.20/openapi.json | `0.1.20` | Apache 2.0 | link-ok | Anchore Engine API Server |
| 4 | `apache.org` | api-guru | https://api.apis.guru/v2/specs/apache.org/2.5.1/openapi.json | `2.5.1` | Apache 2.0 | link-ok | Airflow API (Stable) |
| 5 | `apache.org-airflow` | api-guru | https://api.apis.guru/v2/specs/apache.org/airflow/2.5.1/openapi.json | `2.5.1` | Apache 2.0 | link-ok | Airflow API (Stable) |
| 6 | `apache.org-qakka` | api-guru | https://api.apis.guru/v2/specs/apache.org/qakka/v1/openapi.json | `v1` | Apache 2.0 | link-ok | Qakka |
| 7 | `apicurio.local-registry` | api-guru | https://api.apis.guru/v2/specs/apicurio.local/registry/2.4.x/openapi.json | `2.4.x` | Apache 2.0 | link-ok | Apicurio Registry API [v2] |
| 8 | `apideck.com-accounting` | api-guru | https://api.apis.guru/v2/specs/apideck.com/accounting/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | Accounting API |
| 9 | `apideck.com-connector` | api-guru | https://api.apis.guru/v2/specs/apideck.com/connector/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | Connector API |
| 10 | `apideck.com-crm` | api-guru | https://api.apis.guru/v2/specs/apideck.com/crm/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | CRM API |
| 11 | `apideck.com-customer-support` | api-guru | https://api.apis.guru/v2/specs/apideck.com/customer-support/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | Customer Support |
| 12 | `apideck.com-ecommerce` | api-guru | https://api.apis.guru/v2/specs/apideck.com/ecommerce/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | Ecommerce API |
| 13 | `apideck.com-ecosystem` | api-guru | https://api.apis.guru/v2/specs/apideck.com/ecosystem/0.0.6/openapi.json | `0.0.6` | Apache 2.0 | link-ok | Ecosystem API |
| 14 | `apideck.com-file-storage` | api-guru | https://api.apis.guru/v2/specs/apideck.com/file-storage/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | File storage API |
| 15 | `apideck.com-hris` | api-guru | https://api.apis.guru/v2/specs/apideck.com/hris/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | HRIS API |
| 16 | `apideck.com-issue-tracking` | api-guru | https://api.apis.guru/v2/specs/apideck.com/issue-tracking/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | Issue Tracking API |
| 17 | `apideck.com-lead` | api-guru | https://api.apis.guru/v2/specs/apideck.com/lead/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | Lead API |
| 18 | `apideck.com-pos` | api-guru | https://api.apis.guru/v2/specs/apideck.com/pos/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | POS API |
| 19 | `apideck.com-proxy` | api-guru | https://api.apis.guru/v2/specs/apideck.com/proxy/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | Proxy API |
| 20 | `apideck.com-sms` | api-guru | https://api.apis.guru/v2/specs/apideck.com/sms/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | SMS API |
| 21 | `apideck.com-vault` | api-guru | https://api.apis.guru/v2/specs/apideck.com/vault/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | Vault API |
| 22 | `apideck.com-webhook` | api-guru | https://api.apis.guru/v2/specs/apideck.com/webhook/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | Webhook API |
| 23 | `apis.guru` | api-guru | https://api.apis.guru/v2/specs/apis.guru/2.2.0/openapi.json | `2.2.0` | CC0 1.0 | link-ok | APIs.guru |
| 24 | `appwrite.io-client` | api-guru | https://api.apis.guru/v2/specs/appwrite.io/client/0.9.3/openapi.json | `0.9.3` | BSD-3-Clause | link-ok | Appwrite |
| 25 | `appwrite.io-server` | api-guru | https://api.apis.guru/v2/specs/appwrite.io/server/0.9.3/openapi.json | `0.9.3` | BSD-3-Clause | link-ok | Appwrite |
| 26 | `asana.com` | api-guru | https://api.apis.guru/v2/specs/asana.com/1.0/openapi.json | `1.0` | Apache 2.0 | link-ok | Asana |
| 27 | `atlassian.com-jira` | api-guru | https://api.apis.guru/v2/specs/atlassian.com/jira/1001.0.0-SNAPSHOT/openapi.json | `1001.0.0-SNAPSHOT` | Apache 2.0 | link-ok | The Jira Cloud platform REST API |
| 28 | `axesso.de` | api-guru | https://api.apis.guru/v2/specs/axesso.de/1.0.0/openapi.json | `1.0.0` | Apache 2.0 | link-ok | Axesso Api |
| 29 | `bbci.co.uk` | api-guru | https://api.apis.guru/v2/specs/bbci.co.uk/1.0/openapi.json | `1.0` | MIT | link-ok | BBC iPlayer Business Layer |
| 30 | `bintable.com` | api-guru | https://api.apis.guru/v2/specs/bintable.com/1.0.0-oas3/openapi.json | `1.0.0-oas3` | Apache 2.0 | link-ok | BIN Lookup API |
| 31 | `box.com` | api-guru | https://api.apis.guru/v2/specs/box.com/2.0.0/openapi.json | `2.0.0` | Apache-2.0 | link-ok | Box Platform API |
| 32 | `bungie.net` | api-guru | https://api.apis.guru/v2/specs/bungie.net/2.18.0/openapi.json | `2.18.0` | BSD License 2.0 | link-ok | Bungie.Net API |
| 33 | `bunq.com` | api-guru | https://api.apis.guru/v2/specs/bunq.com/1.0/openapi.json | `1.0` | Apache 2.0 | link-ok | bunq API |
| 34 | `byautomata.io` | api-guru | https://api.apis.guru/v2/specs/byautomata.io/1.0.1/openapi.json | `1.0.1` | Apache 2.0 | link-ok | Automata Market Intelligence API |
| 35 | `calorieninjas.com` | api-guru | https://api.apis.guru/v2/specs/calorieninjas.com/1.0.0/openapi.json | `1.0.0` | Apache 2.0 | link-ok | CalorieNinjas |
| 36 | `canada-holidays.ca` | api-guru | https://api.apis.guru/v2/specs/canada-holidays.ca/1.8.0/openapi.json | `1.8.0` | MIT | link-ok | Canada Holidays API |
| 37 | `codesearch.debian.net` | api-guru | https://api.apis.guru/v2/specs/codesearch.debian.net/1.4.0/openapi.json | `1.4.0` | Apache 2.0 | link-ok | Debian Code Search |
| 38 | `color.pizza` | api-guru | https://api.apis.guru/v2/specs/color.pizza/1.0.0/openapi.json | `1.0.0` | MIT | link-ok | Color Name API |
| 39 | `conjur.local` | api-guru | https://api.apis.guru/v2/specs/conjur.local/5.3.0/openapi.json | `5.3.0` | Apache 2.0 | link-ok | Conjur |
| 40 | `corrently.io` | api-guru | https://api.apis.guru/v2/specs/corrently.io/2.0.0/openapi.json | `2.0.0` | Apache 2.0 | link-ok | Corrently.io |
| 41 | `discourse.local` | api-guru | https://api.apis.guru/v2/specs/discourse.local/latest/openapi.json | `latest` | MIT | link-ok | Discourse API Documentation |
| 42 | `dnd5eapi.co` | api-guru | https://api.apis.guru/v2/specs/dnd5eapi.co/0.1/openapi.json | `0.1` | MIT License | link-ok | D&D 5e API |
| 43 | `eos.local` | api-guru | https://api.apis.guru/v2/specs/eos.local/1.0.0/openapi.json | `1.0.0` | MIT | link-ok | Net API |
| 44 | `esgenterprise.com` | api-guru | https://api.apis.guru/v2/specs/esgenterprise.com/1.0.0/openapi.json | `1.0.0` | MIT | link-ok | ESG Rating Data |
| 45 | `etherpad.local` | api-guru | https://api.apis.guru/v2/specs/etherpad.local/1.2.15/openapi.json | `1.2.15` | Apache 2.0 | link-ok | Etherpad API |
| 46 | `etsi.local-mec010-2_apppkgmgmt` | api-guru | https://api.apis.guru/v2/specs/etsi.local/MEC010-2_AppPkgMgmt/2.1.1/openapi.json | `2.1.1` | BSD-3-Clause | link-ok | ETSI GS MEC 010-2 - Part 2: Application lifecycle, rules and requirements manage |
| 47 | `gambitcomm.local-mimic` | api-guru | https://api.apis.guru/v2/specs/gambitcomm.local/mimic/21.00/openapi.json | `21.00` | Apache 2.0 | link-ok | MIMIC REST API |
| 48 | `github.com` | api-guru | https://api.apis.guru/v2/specs/github.com/1.1.4/openapi.json | `1.1.4` | MIT | link-ok | GitHub v3 REST API |
| 49 | `gov.bc.ca-news` | api-guru | https://api.apis.guru/v2/specs/gov.bc.ca/news/1.0/openapi.json | `1.0` | Apache 2.0 | link-ok | BC Gov News API Service 1.0 |
| 50 | `groundhog-day.com` | api-guru | https://api.apis.guru/v2/specs/groundhog-day.com/1.2.1/openapi.json | `1.2.1` | MIT | link-ok | Groundhog Day API |
| 51 | `amazonaws.com-cloudformation` | api-guru | https://api.apis.guru/v2/specs/amazonaws.com/cloudformation/2010-05-15/openapi.json | `2010-05-15` | Apache 2.0 License | link-ok | 132 ops, 465 schemas, 859 allOf, 1,523 header/query params, XML request/response, server variables |
| 52 | `netbox.dev` | api-guru | https://api.apis.guru/v2/specs/netbox.dev/3.4/openapi.json | `3.4` | Apache v2 License | link-ok | 844 ops, 233 schemas, 823 nullable, 1,318 readOnly, 6,867 params, custom formats/numeric enums |
| 53 | `squareup.com` | api-guru | https://api.apis.guru/v2/specs/squareup.com/2.0/openapi.json | `2.0` | Apache 2.0 | link-ok | 200 ops, 807 schemas, mutually recursive four-schema graph, two security schemes |
| 54 | `redhat.com-catalog_inventory` | api-guru | https://api.apis.guru/v2/specs/redhat.com/catalog_inventory/1.0.0/openapi.json | `1.0.0` | Apache 2.0 | link-ok | 40 deepObject params, 113 readOnly, multiple servers/server variables, inline bodies |
| 55 | `microcks.local` | api-guru | https://api.apis.guru/v2/specs/microcks.local/1.7.0/openapi.json | `1.7.0` | Apache 2.0 | link-ok | discriminator with two mappings, oneOf/allOf, binary multipart bodies |
| 56 | `xero.com-xero-payroll-au` | api-guru | https://api.apis.guru/v2/specs/xero.com/xero-payroll-au/2.9.4/openapi.json | `2.9.4` | MIT | link-ok | UUID-heavy graph, readOnly fields, inline request bodies, header/path/query mix |
| 57 | `openfigi.com` | api-guru | https://api.apis.guru/v2/specs/openfigi.com/1.4.0/openapi.json | `1.4.0` | Apache 2.0 | link-ok | simple-style path param, wildcard response media, oneOf, alternative document security, server variable |
| 58 | `openbanking.org.uk-account-info-openapi` | api-guru | https://api.apis.guru/v2/specs/openbanking.org.uk/account-info-openapi/3.1.7/openapi.json | `3.1.7` | open-licence (MIT) | link-ok | 209 schemas, 1,188 refs, application/jose+jwe, dual security schemes; Crozier invalid-Python gap |
| 59 | `maif.local-otoroshi` | api-guru | https://api.apis.guru/v2/specs/maif.local/otoroshi/1.5.0-dev/openapi.json | `1.5.0-dev` | Apache 2.0 | link-ok | 22 oneOf, NDJSON request bodies, SSE response, 102 ops, format diversity |
| 60 | `traccar.org` | api-guru | https://api.apis.guru/v2/specs/traccar.org/5.6/openapi.json | `5.6` | Apache 2.0 | link-ok | GPX/XML, CSV, XLSX media, urlencoded request, six servers/two variables |
| 61 | `twilio.com-twilio_voice_v1` | api-guru | https://api.apis.guru/v2/specs/twilio.com/twilio_voice_v1/1.42.0/openapi.json | `1.42.0` | Apache 2.0 | link-ok | 17 path-level servers, 87 nullable nodes, urlencoded bodies, custom formats |
| 62 | `portfoliooptimizer.io` | api-guru | https://api.apis.guru/v2/specs/portfoliooptimizer.io/1.0.9/openapi.json | `1.0.9` | Apache 2.0 | link-ok | 83 operations and 15 oneOf across an all-inline zero-component-schema surface |
| 63 | `reverb.com` | api-guru | https://api.apis.guru/v2/specs/reverb.com/3.0/openapi.json | `3.0` | Apache 2.0 | link-ok | 163 operations, 126 paths, zero component schemas, 21 inline request bodies |
| 64 | `redocly.com-museum` | github-raw | https://raw.githubusercontent.com/Redocly/museum-openapi-example/2770b2b2e59832d245c7b0eb0badf6568d7efb53/openapi.yaml | `2770b2b2e59832d245c7b0eb0badf6568d7efb53` | MIT | link-ok | OpenAPI 3.1; 8 operations/5 paths; allOf; UUID/date/email/binary; image/png and problem+json |
| 65 | `http-toolkit` | github-raw | https://raw.githubusercontent.com/benc-uk/http-toolkit/56534e825a225b0d4133c3a0613526094ff03663/cmd/swagger-ui/openapi.json | `56534e825a225b0d4133c3a0613526094ff03663` | MIT | link-ok | OpenAPI 3.0; 26 operations/16 paths; wildcard paths; GET/POST/PUT/PATCH/DELETE; basic and bearer auth; UUID and binary responses |
| 66 | `frankfurter` | github-raw | https://raw.githubusercontent.com/lineofflight/frankfurter/e8b3311fe0f3d86b18d5c08b22dca707fb010d1c/lib/public/v2/openapi.json | `e8b3311fe0f3d86b18d5c08b22dca707fb010d1c` | MIT | link-ok | OpenAPI 3.1.2; 15 nullable-via-`type`-array schemas; array and object responses; currency enums |
| 67 | `worldcoin-signup-sequencer` | github-raw | https://raw.githubusercontent.com/worldcoin/signup-sequencer/f2870f1412517bfc2377838ff20cb0ee03ddaf72/schemas/openapi-v3.yaml | `f2870f1412517bfc2377838ff20cb0ee03ddaf72` | MIT | link-ok | OpenAPI 3.1; two tuple-array schemas using `prefixItems`; reusable request bodies; bearer authentication |
| 68 | `electric-sql` | github-raw | https://raw.githubusercontent.com/electric-sql/electric/be716ccdb225e7b60919c3f46ea92ad5332ff31a/website/electric-api.yaml | `be716ccdb225e7b60919c3f46ea92ad5332ff31a` | Apache-2.0 | link-ok | OpenAPI 3.1; `patternProperties`; polymorphic query parameters; streaming responses |
| 69 | `tamoss` | github-raw | https://raw.githubusercontent.com/livewyer-ops/tamoss/ccbef170204082f3ae3842c2ffee476f5008e1fb/src/openapi-contract.yaml | `ccbef170204082f3ae3842c2ffee476f5008e1fb` | Apache-2.0 | link-ok | OpenAPI 3.1; `if`/`then`/`else`; eight `const` schemas; eight top-level webhooks with inline bodies |
| 70 | `appng-rest-api` | github-raw | https://raw.githubusercontent.com/appNG/appng/8d9ff98f7d3ddd3e74340bcfb322c12df2ed189b/appng-rest-api/src/main/resources/org/appng/api/rest/appng-openapi.yaml | `8d9ff98f7d3ddd3e74340bcfb322c12df2ed189b` | Apache-2.0 | link-ok | Deployed appNG REST API with three matrix path parameters (`explode: true`) and a cookie parameter |
| 71 | `slurmdb-rest` | github-raw | https://raw.githubusercontent.com/ubccr/slurmdbrest/f9c5e77cc3a1a11c7645dab31c6752cd08577721/api/openapi.yaml | `f9c5e77cc3a1a11c7645dab31c6752cd08577721` | Apache-2.0 | link-ok | SlurmDB REST API with a label path parameter (`explode: false`) and 33 form parameters with explicit `explode` |
| 72 | `nimisampo` | github-raw | https://raw.githubusercontent.com/SemanticComputing/nimisampo.fi/34b8d22fff53a3dd531e89277fdb2f98d69dd1d0/src/server/openapi.yaml | `34b8d22fff53a3dd531e89277fdb2f98d69dd1d0` | MIT | link-ok | Deployed NameSampo API with a query parameter carrying `content: { application/json: ... }` and three `allowReserved` parameters |
| 73 | `free5gc-pdu-session` | github-raw | https://raw.githubusercontent.com/free5gc/openapi/8d0ee35bc671dd9995240c0ff73d4c75075a204a/Nsmf_PDUSession/api/openapi.yaml | `8d0ee35bc671dd9995240c0ff73d4c75075a204a` | Apache-2.0 | link-ok | free5GC PDU Session API with multipart `encoding` properties combining `contentType` and per-part `headers` |
| 74 | `sigstore-rekor` | github-raw | https://raw.githubusercontent.com/trailofbits/sigstore-apis/c6bd8db7b1629104dfe241ad26a838f69199b169/openapi/rekor.openapi.json | `c6bd8db7b1629104dfe241ad26a838f69199b169` | Apache-2.0 | link-ok | Sigstore Rekor API with eight literal `2XX` plus `default` response pairs, 12 discriminators without mappings, and seven nested objects combining `readOnly` and `writeOnly` properties |
| 75 | `letta` | github-raw | https://raw.githubusercontent.com/letta-ai/letta/e3fb00f97009cafe527cde93983cda0dfdd7e574/fern/openapi.json | `e3fb00f97009cafe527cde93983cda0dfdd7e574` | Apache-2.0 | link-ok | Letta API with 10 `text/event-stream` responses, 12 discriminators without mappings, 1 map-of-union schema, and 1,416 `anyOf` plus 87 `oneOf` compositions |
| 76 | `free5gc-namf-communication` | github-raw | https://raw.githubusercontent.com/shynuu/free5gc-cli/7f775ecab0cbe3074b38e528581641cff5520c2f/lib/openapi/Namf_Communication/api/openapi.yaml | `7f775ecab0cbe3074b38e528581641cff5520c2f` | Apache-2.0 | link-ok | free5GC AMF Communication API with `ServiceAreaRestriction/allOf/0/oneOf/0/not` and 142 `application/problem+json` response media entries |
| 77 | `apideck.com-ats` | api-guru | https://api.apis.guru/v2/specs/apideck.com/ats/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | link-ok | ATS API with an inline object nested in `Applicant.properties.social_links.items` |
| 78 | `buildrelay` | github-raw | https://raw.githubusercontent.com/cnorlander/BuildRelay/e5f47309d1ca6fd28267de041e7ed2f61e477723/openapi.json | `e5f47309d1ca6fd28267de041e7ed2f61e477723` | MIT | link-ok | BuildRelay API with a referenced request body and a direct inline-object `500` response body |
| 79 | `tlon-notes` | github-raw | https://raw.githubusercontent.com/tloncorp/tlon-apps/2277696dcebb66270c6953b983e1a580b780071e/desk/app/notes/openapi.json | `2277696dcebb66270c6953b983e1a580b780071e` | MIT | link-ok | Tlon Notes API with four inline, untitled discriminated unions lacking mappings and a recursive `ImportNode` schema |
| 80 | `twilio.com-twilio_messaging_v1` | api-guru | https://api.apis.guru/v2/specs/twilio.com/twilio_messaging_v1/1.42.0/openapi.json | `1.42.0` | Apache 2.0 | link-ok | Twilio Messaging API with a `russell_3000` property that exercises Fern's underscore-before-trailing-digit rename |
| 81 | `livepeer-ai-runner` | github-raw | https://raw.githubusercontent.com/livepeer/ai-runner/50a742cee7c5789ef4a10f8117f30de3758366a9/openapi.yaml | `50a742cee7c5789ef4a10f8117f30de3758366a9` | MIT | link-ok | Livepeer AI Runner with three untagged, groupless root operations alongside ten tagged pipeline operations |
| 82 | `eos.local-extra-fields-forbid` | api-guru | https://api.apis.guru/v2/specs/eos.local/1.0.0/openapi.json | `1.0.0` | MIT | link-ok | Row 43's Net API regenerated with `pydantic_config.extra_fields: forbid`, pinning `extra="forbid"` / `pydantic.Extra.forbid` |
| 83 | `med-anvisa-price` | github-raw | https://raw.githubusercontent.com/breno12321/medAnvisaPrice/43866742c2db0f2064ceb99071ebb058c804580b/docs/apiSchema.yml | `43866742c2db0f2064ceb99071ebb058c804580b` | MIT | link-ok | Latin-1 accented enum values Fern folds into ASCII member names (`SUBSTANCIA = "SUBSTÂNCIA"`) beside accented property names it drops the accent from (`laborat_rio` aliased to `LABORATÓRIO`) |
| 84 | `sac-backend` | github-raw | https://raw.githubusercontent.com/walter1705/SAC/3c0ee7959c334a750496d2db2c26791a5aa0185f/backend/src/main/resources/static/openapi.yaml | `3c0ee7959c334a750496d2db2c26791a5aa0185f` | MIT | link-ok | Second, independent witness of the accent-dropping property rule from another project and language: `tamaño` becomes `tama_o` with the wire name kept as the alias |
| 85 | `kytos-sdntrace-cp` | github-raw | https://raw.githubusercontent.com/kytos-ng/sdntrace_cp/269f4482ecd4125dc1c115e059dbce26b7269216/openapi.yml | `269f4482ecd4125dc1c115e059dbce26b7269216` | MIT | link-ok | Kytos SDNTrace-CP API whose two operations both declare `424`, pinning Fern's `FailedDependencyError` name for a status no golden emitted |
| 86 | `withsecure-gdpr-subject-rights` | github-raw | https://raw.githubusercontent.com/WithSecureOpenSource/gdpr-subject-rights-api/0d2775dbf1c0830671a9efd878f03ae1eaf97995/openapi.yaml | `0d2775dbf1c0830671a9efd878f03ae1eaf97995` | Apache 2.0 | link-ok | WithSecure GDPR subject-rights API whose five operations declare `451`, pinning Fern's `UnavailableForLegalReasonsError` name for a status no golden emitted |
| 87 | `prometheus-x-edge-computing` | github-raw | https://raw.githubusercontent.com/Prometheus-X-association/edge-computing/78ed883317ec8739e985780c998d9f73f1e370a8/spec/openapi.yaml | `78ed883317ec8739e985780c998d9f73f1e370a8` | Apache-2.0 | link-ok | Prometheus-X edge-computing API declaring `408` and `412`, pinning Fern's `RequestTimeoutError` and `PreconditionFailedError` names for two statuses no golden emitted |
| 88 | `exa-gate` | github-raw | https://raw.githubusercontent.com/apaidedie/exa-gate/37cf047d828665004b4900ce672aa3f27b0bb844/docs/openapi.json | `37cf047d828665004b4900ce672aa3f27b0bb844` | MIT | link-ok | Exa Gate API declaring `423` and `426`, pinning Fern's `LockedError` and `UpgradeRequiredError` names for two statuses no golden emitted |
| 89 | `amazonaws.com-cloudfront` | api-guru | https://api.apis.guru/v2/specs/amazonaws.com/cloudfront/2016-11-25/openapi.json | `2016-11-25` | Apache 2.0 License | link-ok | AWS CloudFront API whose 27 operations declare `502`, `505`, `506`, `507`, `508`, `510` and `511`, pinning Fern's `BadGatewayError`, `HttpVersionNotSupportedError`, `VariantAlsoNegotiatesError`, `InsufficientStorageError`, `LoopDetectedError`, `NotExtendedError` and `NetworkAuthenticationRequiredError` names for seven statuses no golden emitted |
| 90 | `khoainats` | github-raw | https://raw.githubusercontent.com/cukhoaimon/khoainats/e680e29affee221e3a6c379b1e51c98ef241da7a/api/generated/.docs/api/openapi.yaml | `e680e29affee221e3a6c379b1e51c98ef241da7a` | MIT | link-ok | Khoai NATS Admin API declaring an `openIdConnect` scheme (`Roles`) beside an HTTP bearer one, with `/v1/noauth` unsecured: `openIdConnect` is the one member of its scheme family Fern imports rather than drops, and this row pins the optional bearer `token` Fern emits for such a document |
| 91 | `helios-verifiable-api` | github-raw | https://raw.githubusercontent.com/a16z/helios/43a8c9f3cdda41a6f383c4db41d9a83f102638b1/verifiable-api/server/openapi.yaml | `43a8c9f3cdda41a6f383c4db41d9a83f102638b1` | MIT | link-ok | 27 component schemas that are remote-URL `$ref`s into six `ethereum/execution-apis` documents, which Fern fetches and resolves transitively — the only reference form Fern was measured to follow rather than discard. Unlike every other row, the golden depends on a third-party fetch at generation time, and those URLs address `refs/heads/main` rather than an immutable ref, so an upstream edit to those six files breaks this row's reproduction for a reason unrelated to crozier |
| 92 | `eozilla` | github-raw | https://raw.githubusercontent.com/eo-tools/eozilla/70187a1bba9fe5a77001a623322f23bb30ea49c7/tools/openapi.yaml | `70187a1bba9fe5a77001a623322f23bb30ea49c7` | Apache-2.0 | link-ok | Eozilla OGC API - Processes server whose `Schema` component closes two cycles through `additionalProperties` (`Schema.properties.<k>` and `Schema.discriminator.mapping` both name `Schema`), the map-of-self form no other golden declares |
| 93 | `openepcis-dpp-ready` | github-raw | https://raw.githubusercontent.com/openepcis/openepcis-dpp-ready/5c1f308d350cfcc9abb80aa6c70262c87141f201/extensions/common/interop/api/en18222-dpp-api.openapi.yaml | `5c1f308d350cfcc9abb80aa6c70262c87141f201` | Apache-2.0 | link-ok | EN 18222 Digital Product Passport API declaring two `type: [string, number, boolean]` arrays — two non-null members each, the multi-type form the other 498 `type` arrays in the corpus never take |
| 94 | `ndw-accessibility-map` | github-raw | https://raw.githubusercontent.com/ndwnu/nls-accessibility-map/46fde7c8b36ac8776eba78079bb53bf42ae17c2b/specification/src/main/resources/nu/ndw/nls/accessibilitymap/specification/v2.yaml | `46fde7c8b36ac8776eba78079bb53bf42ae17c2b` | MIT | link-ok | NDW Location Services accessibility-map API whose two `components.headers` Header Objects (`Accept-encoding`, `Content-encoding`) each declare `allowEmptyValue`, the Header Object field no other registered source declares |
| 95 | `marimo` | github-raw | https://raw.githubusercontent.com/marimo-team/marimo/257ea7a983e2dbe4627f0168072fdcd538c93c5c/packages/openapi/api.yaml | `257ea7a983e2dbe4627f0168072fdcd538c93c5c` | Apache-2.0 | link-ok | Marimo API whose `Base64String` component declares `contentEncoding: base64`, the JSON Schema 2020-12 encoding keyword no prior golden source declares |
| 96 | `blackadi-oauth2` | github-raw | https://raw.githubusercontent.com/blackadi/OAUTH2.0/b6e4cfa1fb060ca5ca3e32185f4a5d88c27163e3/server/src/routes/openapi.json | `b6e4cfa1fb060ca5ca3e32185f4a5d88c27163e3` | MIT | link-ok | OAuth 2.0 authorization-server API declaring `scheme: dpop` (RFC 9449) on `dpopAuth` beside `bearer` and `basic` — the only registered source declaring an IANA HTTP authentication scheme Fern's importer does not support, so its golden pins that crozier drops the scheme exactly as Fern does |
| 97 | `mosip-esignet` | github-raw | https://raw.githubusercontent.com/mosip/esignet/201264c86e98113762451f4a306163233fa79e24/docs/esignet-openapi.yaml | `201264c86e98113762451f4a306163233fa79e24` | MPL-2.0 | link-ok | MOSIP eSignet OIDC/identity API, the second registered witness of `scheme: DPoP` (RFC 9449): `Authorization-DPoP` declares it in the registry's own mixed-case spelling beside four `bearer` schemes, where row 96 declares the lowercase one |
| 98 | `openbankingproject-ch-kundenbeziehung` | github-raw | https://raw.githubusercontent.com/openbankingproject-ch/Open-API-Kundenbeziehung-Legacy/c7439ba67f5790d901d1d20943cae5cb48e8e7fc/api/openapi.yaml | `c7439ba67f5790d901d1d20943cae5cb48e8e7fc` | MIT (declared by the document's `info.license`; the repository carries no license file) | link-ok | Swiss Open Banking customer-relationship API, the third `scheme: DPoP` witness and the corpus's first source declaring `type: mutualTLS` — the 3.1-only Security Scheme type no prior registered source declares |
| 99 | `cyberark-conjur-api` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/9d36c7e3808ebe65d69e81d3c3250598927a575c/apis/openapi/cyberark.com/conjur-api/5.3.2/openapi.json | `9d36c7e3808ebe65d69e81d3c3250598927a575c` | Apache-2.0 (declared by the document's `info.license`, inside a CC0-1.0 repository) | link-ok | CyberArk Conjur 5.3.2, the corpus's only source declaring `scheme: mutual` (RFC 8120): `conjurKubernetesMutualTls` carries it beside a `basic` scheme and an `apiKey` one, so its golden pins that crozier drops the IANA scheme Fern's importer does not support exactly where Fern does. Its `paths` are relative-file `$ref`s into sibling documents the direct spec URL does not carry, which Fern discards without diagnosing; the golden is therefore the endpoint-free client that pairing leaves behind |
| 100 | `adyen-report-notification` | github-raw | https://raw.githubusercontent.com/Adyen/adyen-openapi/4265e8ffe6cc4c35fe6804d5a395598621d3da53/json/BalancePlatformReportNotification-v1.json | `4265e8ffe6cc4c35fe6804d5a395598621d3da53` | MIT | link-ok | Adyen "Report webhooks", the corpus's first source that omits `paths` entirely: a valid OpenAPI 3.1 document whose only API surface is one webhook (`balancePlatform.report.created`) over five component schemas, so its golden pins what Fern emits when the field the whole endpoint pipeline reads is absent |
| 101 | `adyen-managed-risk-notification` | github-raw | https://raw.githubusercontent.com/Adyen/adyen-openapi/4265e8ffe6cc4c35fe6804d5a395598621d3da53/json/BalancePlatformManagedRiskNotification-v1.json | `4265e8ffe6cc4c35fe6804d5a395598621d3da53` | MIT | link-ok | Adyen "Managed risk webhooks", the corpus's first source whose top-level `webhooks` stand alone with no `paths` beside them — eight of them, over 19 component schemas — where row 69's eight webhooks accompany a populated Paths Object; it also declares `jsonSchemaDialect` |
| 102 | `go-kratos-casbin-admin` | github-raw | https://raw.githubusercontent.com/go-kratos/examples/61daed1ec4d5a94d689bc8fab9bc960c6af73ead/casbin/app/admin/openapi.yaml | `61daed1ec4d5a94d689bc8fab9bc960c6af73ead` | MIT | link-ok | The protoc-gen-openapi document the go-kratos Casbin example ships, the corpus's only source carrying an *empty* Paths Object: `paths: {}` beside `components.schemas: {}` and an empty `info.title`, the distinct shape from rows 100 and 101's omitted `paths` |

## Batch 2 — byte-matched (issue #77)

Ten corpora were selected as the next Fern byte-match targets, chosen for OpenAPI
shapes the prior corpora under-exercise. All are `link-ok` rows in the table above
(specs fetched, not vendored); their goldens are workflow-managed.

**Eight are now byte-matched byte-for-byte** — wired into `tests/e2e.rs` +
`test-corpus-match`, with every generator fix on the `src/*.rs` side (no golden edited).
**Two — `bbci.co.uk` and `canada-holidays.ca` — FAILED Fern golden generation: Fern
itself cannot emit an SDK for them, so there is no golden to match. They are dropped;
do not re-select them in a future batch.**

| name | selected for | status |
|---|---|---|
| `bbci.co.uk` | oneOf/anyOf + ~79 free-form maps | **DROPPED** — Fern golden generation failed (do not retry) |
| `gambitcomm.local-mimic` | 356 operations; maps + links | ✅ matched — fixed reserved-word `del` method name |
| `dnd5eapi.co` | oneOf/anyOf/allOf + recursion | ✅ matched — fixed allOf-as-map parse + recursive composition |
| `airbyte.local-config` | 102 ops / 210 schemas; format diversity | ✅ matched |
| `etsi.local-mec010-2_apppkgmgmt` | `application/zip`, binary, custom formats | ✅ matched |
| `apideck.com-webhook` | oneOf/anyOf + deepObject/header params | ✅ matched |
| `apache.org-qakka` | `application/octet-stream` (binary) | ✅ matched |
| `canada-holidays.ca` | recursive schemas + numeric enums | **DROPPED** — Fern golden generation failed (do not retry) |
| `apideck.com-vault` | spaceDelimited/deepObject params, dense anyOf | ✅ matched |
| `6-dot-authentiqio.appspot.com` | `application/jwt` + wildcard media type | ✅ matched — added HEAD operation generation |

## Batch 3 — selected (issue #77)

Thirteen `link-ok` corpora were approved for the next byte-match batch. All 13
passed native `fern check`; their specs are fetched locally and are not vendored.
Fern goldens were generated successfully for 12 corpora, and all 12 are now
byte-matched. `groundhog-day.com` failed Fern golden generation and is dropped.

| name | selected for | status |
|---|---|---|
| `apideck.com-accounting` | 53 ops / 140 schemas; anyOf, maps, deepObject, recursion | ✅ matched |
| `apideck.com-file-storage` | 32 ops / 75 schemas; binary, wildcard media, maps, deepObject | ✅ matched |
| `appwrite.io-client` | 61 ops; `multipart/form-data` | ✅ matched |
| `apideck.com-hris` | 27 ops / 87 schemas; anyOf/allOf, maps, deepObject | ✅ matched |
| `byautomata.io` | Crozier probe emits invalid Python from a slash-containing operation name; intentional generator-gap target | ✅ matched |
| `groundhog-day.com` | mutually recursive `Groundhog`/`Prediction` schemas | **DROPPED** — Fern golden generation failed (do not retry) |
| `apideck.com-connector` | anyOf, recursive schema, maps, deepObject, links, `text/markdown` | ✅ matched |
| `color.pizza` | `image/svg+xml` response media | ✅ matched |
| `apideck.com-proxy` | all-inline schema surface, anyOf, wildcard media | ✅ matched |
| `apis.guru` | typed free-form maps | ✅ matched |
| `apideck.com-ecommerce` | 64 schemas; anyOf, maps, deepObject | ✅ matched |
| `apideck.com-issue-tracking` | 65 schemas; anyOf/allOf, maps, deepObject | ✅ matched |
| `bintable.com` | wildcard response media | ✅ matched |

The status table is the durable result of that generation pass; use the standard
workflow for any future source change or Fern upgrade.

## Batch 4 — byte-matched (issue #77)

Native Fern CLI 5.67.1 screening exhausted the manifest's remaining unused
entries. Exactly eight specs genuinely passed Fern and were selected below;
Docker-backed golden generation succeeded for seven, and all seven are now
byte-matched. `codesearch.debian.net` failed Fern golden generation. Twelve
corpora were dropped in total: that one golden-generation failure plus eleven
screening failures, all marked do not retry. All 50 manifest rows are accounted
for, with no backups to invent.

| name | selected for | status |
|---|---|---|
| `apache.org-airflow` | 50 paths / 85 schemas; 22 allOf, anyOf, discriminator; invalid title-derived `airflow_api_(stable)` package naming made this an intentional generator-gap target | ✅ matched — fixed invalid title-derived package naming |
| `apideck.com-lead` | anyOf/allOf, free-form maps, two deepObject params | ✅ matched |
| `apideck.com-ecosystem` | 12 paths / 32 schemas; 17 free-form maps | ✅ matched |
| `apideck.com-customer-support` | anyOf plus maps | ✅ matched |
| `apideck.com-sms` | compact anyOf corpus | ✅ matched |
| `eos.local` | four paths, all-inline / zero named schemas | ✅ matched |
| `codesearch.debian.net` | compact conventional two-schema baseline | **DROPPED** — Fern golden generation failed (do not retry) |
| `appng-rest-api` | matrix path serialization and cookie parameters | **DROPPED** — Fern golden generation failed: generator exits 1 at 5.20.0 despite `fern check` passing (do not retry) |
| `calorieninjas.com` | minimal one-path / zero-schema boundary case | ⚠️ **ACCEPTED EXCEPTION** — Fern 5.20.0 emits unnamed methods for its `operationId`-less operation and its own Ruff pass rejects the SDK, so no golden exists; the exact failure is fingerprinted in `known-fern-failure.json` and Crozier generates the same spec successfully |
| `conjur.local` | screened but Fern did not produce a usable result | **DROPPED** — Fern falsely returned success while stderr reported an OpenAPI parse failure and an unresolved response reference (do not retry) |
| `asana.com` | screened but failed Fern validation | **DROPPED** — Fern check failed with 17 fatal diagnostics (do not retry) |
| `apideck.com-pos` | screened but failed Fern validation | **DROPPED** — Fern check failed with 4 fatal diagnostics (do not retry) |
| `atlassian.com-jira` | screened but failed Fern validation | **DROPPED** — Fern check failed with 3 fatal diagnostics (do not retry) |
| `axesso.de` | screened but failed Fern validation | **DROPPED** — Fern check failed with 1 fatal diagnostic (do not retry) |
| `box.com` | screened but failed Fern validation | **DROPPED** — Fern check failed with 25 fatal diagnostics (do not retry) |
| `corrently.io` | screened but failed Fern validation | **DROPPED** — Fern check failed with 2 fatal diagnostics and 1 error (do not retry) |
| `esgenterprise.com` | screened but failed Fern validation | **DROPPED** — Fern check failed with 1 fatal diagnostic (do not retry) |
| `etherpad.local` | screened but failed Fern validation | **DROPPED** — Fern check failed with 5 fatal diagnostics (do not retry) |
| `github.com` | screened but failed Fern validation | **DROPPED** — Fern check failed with 29 fatal diagnostics (do not retry) |
| `gov.bc.ca-news` | screened but failed Fern validation | **DROPPED** — Fern check failed with 4 fatal diagnostics (do not retry) |

The status table is the durable result of that generation pass; use the standard
workflow for any future source change or Fern upgrade.

## Batch 5 — byte-matched (issue #77)

Native Fern CLI 5.75.0 screening covered 49 new non-Apideck permissively
licensed OpenAPI 3 candidates. Exactly 10 primaries plus 3 Fern-passing backups
are registered; all 13 passed native Fern check, generated Fern goldens, and are
now byte-matched byte-for-byte.

| name | role | selected for | status |
|---|---|---|---|
| `amazonaws.com-cloudformation` | primary | 132 ops, 465 schemas, 859 allOf, 1,523 header/query params, XML request/response, server variables | ✅ matched |
| `netbox.dev` | primary | 844 ops, 233 schemas, 823 nullable, 1,318 readOnly, 6,867 params, custom formats/numeric enums | ✅ matched |
| `squareup.com` | primary | 200 ops, 807 schemas, mutually recursive four-schema graph, two security schemes | ✅ matched |
| `redhat.com-catalog_inventory` | primary | 40 deepObject params, 113 readOnly, multiple servers/server variables, inline bodies | ✅ matched |
| `microcks.local` | primary | discriminator with two mappings, oneOf/allOf, binary multipart bodies | ✅ matched |
| `xero.com-xero-payroll-au` | primary | UUID-heavy graph, readOnly fields, inline request bodies, header/path/query mix | ✅ matched |
| `openfigi.com` | primary | simple-style path param, wildcard response media, oneOf, alternative document security, server variable | ✅ matched |
| `openbanking.org.uk-account-info-openapi` | primary | 209 schemas, 1,188 refs, application/jose+jwe, dual security schemes; Crozier invalid-Python gap | ✅ matched |
| `maif.local-otoroshi` | primary | 22 oneOf, NDJSON request bodies, SSE response, 102 ops, format diversity | ✅ matched |
| `traccar.org` | primary | GPX/XML, CSV, XLSX media, urlencoded request, six servers/two variables | ✅ matched |
| `twilio.com-twilio_voice_v1` | backup | 17 path-level servers, 87 nullable nodes, urlencoded bodies, custom formats | ✅ matched |
| `portfoliooptimizer.io` | backup | 83 operations and 15 oneOf across an all-inline zero-component-schema surface | ✅ matched |
| `reverb.com` | backup | 163 operations, 126 paths, zero component schemas, 21 inline request bodies | ✅ matched |

### Screened failures

| name | status |
|---|---|
| `amazonaws.com-s3` | DROPPED — 12 Fern duplicate normalized query-parameter errors (do not retry) |
| `digitalocean.com` | DROPPED — Fern false success; stderr parse/unresolved response ref failure (do not retry) |
| `id4i.de` | DROPPED — 3 duplicate organizationId request-property errors (do not retry) |
| `intellifi.nl` | DROPPED — 3 duplicate id request-property errors (do not retry) |
| `meshery.local` | DROPPED — 11 auth-import errors (do not retry) |
| `mist.com` | DROPPED — duplicate device_mac request-property error (do not retry) |
| `nasa.gov-apod` | DROPPED — endpoint requires auth but Fern imports none (do not retry) |
| `nexmo.com-reports` | DROPPED — 23 date-example errors (do not retry) |
| `openpolicy.local` | DROPPED — 2 YAML-frontmatter delimiter errors in endpoint descriptions (do not retry) |
| `opentargets.io` | DROPPED — DRUG_ID/drug_id generated-name collision (do not retry) |
| `osf.io` | DROPPED — YAML-frontmatter delimiter error in endpoint description (do not retry) |
| `sinao.app` | DROPPED — 2 non-array list-default errors (do not retry) |
| `telnyx.com` | DROPPED — 26 enum/default/example/name-collision errors (despite callbacks/multipart) (do not retry) |
| `truora.com` | DROPPED — 70 date placeholder-example errors (do not retry) |
| `twilio.com-api` | DROPPED — 12 normalized duplicate query-parameter errors (do not retry) |
| `velopayments.com` | DROPPED — 15 enum/date/datetime errors (do not retry) |
| `xero.com-xero_bankfeeds` | DROPPED — 13 unsupported-property and statementID/statementId collision errors (do not retry) |
| `xtrf.eu` | DROPPED — 7 response example property/type errors (do not retry) |

The status tables are the durable results of that generation pass; use the
standard workflow for any future source change or Fern upgrade.

## Batch 6 — composition and media selected (issue #77)

Three new permissively licensed, immutable specs passed native Fern CLI 5.75.4
screening and are registered in the match-all-by-default harness. Their
workflow-owned goldens are committed and all three are byte-matched.

| name | selected for | status |
|---|---|---|
| `sigstore-rekor` | literal ranged `2XX` plus `default`; implicit discriminators; nested objects mixing `readOnly` and `writeOnly` | ✅ matched |
| `letta` | SSE; implicit discriminators; map of unions; deep `anyOf`/`oneOf` | ✅ matched |
| `free5gc-namf-communication` | structurally nested `allOf` → `oneOf` → `not`; 142 problem+json responses | ✅ matched |

### Screened failures

| name | status |
|---|---|
| `opencode` | **DROPPED** — Fern check failed with 22 response/request example and missing-discriminant errors (do not retry this ref) |
| `clerk-backend-api` | **DROPPED** — Fern check failed with a duplicate `InvitationObject` and normalized `frontendApi` parameter collision (do not retry this ref or the screened older versions) |
| `temporal-api` | **DROPPED** — Fern check failed with 36 normalized path/query parameter collisions (do not retry this ref) |
| `openfeature-protocol` | **DROPPED** — Fern check failed with nine invalid object-extension errors (do not retry this ref) |
| `cloudevents-subscriptions` | **DROPPED** — Fern check failed with 12 invalid object-extension errors (do not retry this ref) |
| `dapr` | **DROPPED** — Fern reported false success after an OpenAPI parse failure on unresolved `ApiKeyAuth` (do not retry this ref) |
| `apache-superset` | **DROPPED** — Fern check failed with six response-example and unreferenced path-parameter errors (do not retry this ref) |
| `xregistry-endpoint` | **DROPPED** — Fern check failed because ten services require auth while the spec defines none (do not retry this ref) |
| `letta` at `b76b5aeb932873dd5f0642a2ef5d81060f991dd6` | **DROPPED** — Fern check failed on an optional union query parameter; the older registered ref passes (do not retry this ref) |
| `coinbase-cdp` | **DROPPED** — Fern check failed with nine schema and example validation errors (do not retry this ref) |
| `pnp-agents-finder` / `pnp-qna` | **DROPPED** — Fern check rejected their invalid `allOf` object extensions (do not retry these refs) |
| `ably-connector` | **DROPPED** — Fern check rejected three invalid integer defaults (do not retry this ref) |
| `azure-aro-hcp` | **DROPPED** — Fern check failed with three discriminant and example errors (do not retry this ref) |
| `assemblyai-autosdk` | **REJECTED** — source license is revenue-limited rather than Apache-2.0/MIT/BSD/CC0 |
| `sumup` | **DROPPED** — its `readOnly` and `writeOnly` fields occur in separate models, so it does not prove same-model interplay |
| `titiler-openeo` | **DROPPED** — its ranged responses do not include literal `2XX` or `default`; `smart-edge-af` consolidates `not`, `default`, and nested composition |
| `apigee-registry` | **DROPPED** — its read/write-only coverage overlapped `sigstore-rekor`, which also consolidates literal `2XX`/`default` and implicit-discriminator coverage |
| `keycloak-admin` | **DROPPED** — its standalone `2XX` coverage forced a fourth registration; `sigstore-rekor` supplies literal `2XX` plus `default` coverage in the three-spec set |
| `smart-edge-af` | **DROPPED** — `TrafficInfluSub` has sibling `allOf` and `anyOf`, not one composition structurally nested inside the other |
| `jaewook-epcis` | **REJECTED** — Fern check reports 35 endpoint-example errors because `headers` examples are strings rather than maps |
| `mardi-gras` | **REJECTED** — Fern-clean and MIT, but it has no `allOf` and therefore could not consolidate the nested composition requirement |
| `paypal-checkout` | **DROPPED** — the only revision with `not` fails Fern on five invalid carrier enum names; Fern-clean older revisions lack `not` |

## Batch 7 — shape-targeted additions (issue #77)

Five further permissively licensed, immutable specs were added one row at a time,
each selected to pin a naming or structural rule the corpus had exercised only
incidentally. All five passed native Fern check, have workflow-managed Fern 5.20.0
goldens, and are byte-matched.

| name | selected for | status |
|---|---|---|
| `apideck.com-ats` | inline object nested in a component array's `items` | ✅ matched |
| `buildrelay` | direct inline-object `500` response body alongside a referenced request body | ✅ matched |
| `tlon-notes` | recursive `oneOf` with inline, untitled, unmapped variants | ✅ matched |
| `twilio.com-twilio_messaging_v1` | underscore-before-trailing-digit rename (`russell_3000`) and URL-encoded form arrays | ✅ matched |
| `livepeer-ai-runner` | untagged, groupless root operations beside a tagged sub-client | ✅ matched |

The status tables above are the durable results of their generation passes; use
the standard workflow for any future source change or Fern upgrade.

## Batch 8 — generator-setting coverage over a registered source (issue #63)

A generator setting is not expressible in an OpenAPI document, so pinning one
needs no new spec: it needs the *same* spec generated under a different Fern
generator config. Row 82 is that shape — a second row over row 43's already
registered `eos.local` source, differing only in the
`pydantic_config.extra_fields: forbid` that
[`fern-generator-config.txt`](fern-generator-config.txt) declares for it. The
row name is the fixture directory, so the two goldens, cached specs, and
`unmatched` lists stay independent.

| name | selected for | status |
|---|---|---|
| `eos.local-extra-fields-forbid` | `extra_fields: forbid`, unpinned in both the pydantic-v2 `model_config` and the v1 `Config` block until this row | ✅ matched |

Reuse this shape for any future generator setting a document cannot express:
add a row over a small registered source rather than hunting a new spec.

## Batch 9 — the Latin-1 naming asymmetry (issue #77)

Thirty-three gated specs carry non-ASCII bytes, but every one of them carries
them in a *description*: non-ASCII property names and enum values were both
measured at zero. Both strings reach `naming.rs`, and Fern's own naming layer
disagrees with itself over them — one generated SDK turns `LABORATÓRIO` into the
enum member `LABORATORIO` and the property `laborat_rio`. A hand-authored fixture
would have had to guess which behaviour to encode, so the two rows below are real
specs that pin both halves. Latin-1 accents are the only case Fern folds rather
than rejecting: a non-ASCII *schema* name fails `fern check` outright, and a
non-ASCII parameter name or `operationId` passes `check` and then makes Fern emit
invalid Python — see [`../../docs/fern-limitations.md`](../../docs/fern-limitations.md).

| name | selected for | status |
|---|---|---|
| `med-anvisa-price` | accented enum values folded to ASCII member names (`SUBSTANCIA = "SUBSTÂNCIA"`) beside accented property names the accent is dropped from (`laborat_rio`), from one document | ✅ matched — taught the enum path to fold Latin-1/Latin Extended-A accents, and made whitespace a hard boundary for the property digit collapse (`EAN 1` → `ean_1`, not `ean1`) |
| `sac-backend` | a second, independent witness of the property rule from another project and language (`tamaño` → `tama_o`) | ✅ matched — its golden also exposed three unrelated gaps, each re-measured with local Fern 5.20.0 probes: environment naming (`production`/`sandbox` only), parameter-level examples (kept only on `type: string`), and optional enum query parameters (never exampled, inline or `$ref`) |

Neither backup set was needed: both primaries generated and matched. The row-2
divergences are a reminder that a fixture chosen for one shape pays for itself in
the shapes it drags in — three generator rules were replaced with measured ones
because `sac-backend` happened to describe its server in Spanish.
## Batch 10 — the unpinned HTTP status exception names (issue #77)

`error_class_name` maps HTTP statuses to Fern's exception class names, and 21
of them were emitted by no golden — every one a hand-written guess. A wrong
name is never one line: it renames the `errors/` module file, its lazy-import
and `__all__` entries, its `reference.md` row, and every `raise` site in every
raw client that declares the status. Five rows were selected, each for the
statuses it declares, and between them they pin 13 of the 21.

| name | selected for | status |
|---|---|---|
| `kytos-sdntrace-cp` | `424` → `FailedDependencyError` | ✅ matched |
| `withsecure-gdpr-subject-rights` | `451` → `UnavailableForLegalReasonsError` | ✅ matched |
| `prometheus-x-edge-computing` | `408` → `RequestTimeoutError`, `412` → `PreconditionFailedError` | ✅ matched |
| `exa-gate` | `423` → `LockedError`, `426` → `UpgradeRequiredError` | ✅ matched |
| `amazonaws.com-cloudfront` | `502`, `505`, `506`, `507`, `508`, `510`, `511` — the whole `5xx` tail above `503` — plus the non-IANA `498`, `499` and `509` its operations also declare | ✅ matched |

No candidate was dropped: all five primaries carried through, so none of the
screened backups was needed.

### The eight statuses this batch could not pin, and why

Not a shortfall to retry blindly — a measured supply limit in the eligible
pool. Fern generates all eight correctly when probed directly; what is missing
is a redistributable specification that declares them.

| statuses | why unpinned |
|---|---|
| `407`, `421` | **zero** documents in the eligible pool declare them anywhere |
| `414`, `418`, `425`, `431` | one eligible witness each — too thin to register |
| `417`, `428` | two eligible witnesses each. `428` is the one worth reading twice: issue #148 reasoned from RFC 6585 that `PreconditionError` was likely wrong, and it is exactly what Fern emits |

CloudFront also moved two rules the corpus had only approximated: annotated
`$ref` use-site copies now cascade through array elements, and `text/csv` reads
back as a `str` body. It contradicted the environment-member rule too, but batch
9's `production`/`sandbox`-only rule — measured from Fern probes and landed
first — already names its multi-word server description `DEFAULT`, so no third
repair was needed. See `../../docs/matching.md`.

## Batch 11 — security-scheme coverage (issue #77)

Crozier's `auth_model` names four security-scheme shapes — `apiKey` in a header,
HTTP `bearer`, HTTP `basic` and `oauth2` — and sends everything else to one
fallthrough arm. Of the schemes that land there, `openIdConnect` is the only one
Fern's importer keeps rather than drops at import, so it is the only one a golden
can pin as behaviour rather than as an absence. Row 90 is that golden.

| name | selected for | status |
|---|---|---|
| `khoainats` | a document declaring `openIdConnect` — the one scheme in Crozier's fallthrough family Fern imports — with one unsecured operation, so the credential is optional | ✅ matched, no repair needed |

Crozier reproduced the golden byte for byte on its first measurement, so the
predicted divergence (a required token from Fern against an optional one from the
fallthrough) did not occur here: the row's document also declares an HTTP bearer
scheme *ahead* of its `openIdConnect` one, and Crozier selects the first
supported scheme, so it emits the same optional bearer `token` through its
HTTP-bearer arm. All three screened candidates for this row shared that shape —
none declares `openIdConnect` without a supported scheme preceding it — so the
corpus still has no golden that forces the fallthrough arm itself. A future
candidate for that gap must declare `openIdConnect` alone.

### Not registered

| name | status |
|---|---|
| `gh:teamdigitale/api-openapi-samples:openapi-v3/spid-aa-template.yaml` | **unused backup** — the primary carried; it declares HTTP bearer and two `oauth2` schemes and no `openIdConnect` at all |
| `gh:Gravitate-Health/keycloak:openapi.yaml` | **unused backup** — the primary carried; its `openIdConnect` scheme also sits behind an `oauth2` one, so it witnesses the same shape as row 90 |

## Batch 12 — the cross-document reference gap (issue #77)

Every row above is a single self-contained document whose every `$ref` is a
local `#/...` pointer, so nothing pinned whether crozier can open a *second*
document. Of the reference forms that cross a document boundary, a remote-URL
`$ref` is the only one Fern 5.20.0 was measured to follow rather than discard
(see [`../../docs/fern-limitations.md`](../../docs/fern-limitations.md)), so it
is the only one a golden can pin. One row closes it.

| name | selected for | status |
|---|---|---|
| `helios-verifiable-api` | 27 component schemas that are remote-URL `$ref`s into six `ethereum/execution-apis` documents, fetched and resolved transitively | ✅ matched |

Repairing crozier to reproduce it needed cross-document resolution
([`src/refs.rs`](../../src/refs.rs)) plus five rules the golden exposed along the
way — fetched-schema naming, unresolvable references, response aliases,
use-site nullability, and scalar query serialization — all recorded in
[`../../docs/matching.md`](../../docs/matching.md#cross-document-ref-resolution-issue-77).

**This row alone depends on a third-party fetch at generation time**, and the URLs
it references address `refs/heads/main` rather than an immutable ref. An upstream
edit to those six `ethereum/execution-apis` files breaks its reproduction for a
reason unrelated to crozier; regenerate the golden through the standard workflow
if that happens, rather than treating it as a generator regression.

## Batch 13 — the two shapes round 4 measured Fern to implement (issue #77)

[`../../docs/fern-limitations.md`](../../docs/fern-limitations.md)'s round 4
resolved eighteen unmeasured rows and found exactly two where Fern reads the
shape and emits output derived from it, with no golden pinning either.
Rows 92 and 93 are those two. Both licences were re-verified at the source
repository at the pinned ref rather than copied from the screening notes:
`eo-tools/eozilla` and `openepcis/openepcis-dpp-ready` each carry an `LICENSE`
opening `Apache License / Version 2.0, January 2004`.

| name | selected for | status |
|---|---|---|
| `eozilla` | a schema graph that closes a cycle through `additionalProperties` — `Schema.properties` and `Schema.discriminator.mapping` are both maps of `Schema` — where all 335 prior `update_forward_refs` call sites recurse through `properties` or `items` | ✅ matched |
| `openepcis-dpp-ready` | two `type: [string, number, boolean]` schemas: multi-member type arrays with more than one **non-null** member, which the corpus's other 498 `type` arrays never are | ✅ matched |

Neither backup was needed; both primaries passed `fern check`, generated at
`fernapi/fern-python-sdk:5.20.0`, and byte-match.

As in batch 9, each row paid for itself in the shapes it dragged in. Between them
the two goldens exposed eleven divergences, all repaired in `src/*.rs`: two apiKey
schemes whose header names normalize to one `api_key` (crozier emitted the
parameter twice, which Ruff rejects); a camelCase discriminator, its variants'
field order, and a discriminant declared loosely on an `allOf` base; per-wrapper
`update_forward_refs` arguments; the import-name collision Eozilla's own
`ApiError` component causes against crozier's core one; a `2xx` response declared
under the malformed media type `/*`; and three union-member rules probed directly
against Fern 5.20.0. See
[`../../docs/matching.md`](../../docs/matching.md#map-of-self-and-multi-type-arrays-issue-77).
