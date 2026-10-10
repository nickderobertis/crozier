# Canonical real-world OpenAPI corpus (issue #77)

This manifest tracks the real-world OpenAPI specs whose licence permits the
redistribution of a golden generated from them. Which licences those are — and
which are refused, and why each half was decided that way — is stated once, in
[`../../docs/corpus-licensing.md`](../../docs/corpus-licensing.md); no row of
this manifest restates it. `decision` is `committed` for registered sources: every file is stored under
`corpus-sources/` with its pinned URL and SHA-256 in `corpus-sources.tsv`.
URLs are used only to rebuild Fern goldens or audit those committed copies. Add or change one numbered row per feature
branch and maintain its golden through the manually dispatched **Fern goldens**
workflow; see
[`../../docs/fern-goldens.md`](../../docs/fern-goldens.md).

Every row registered in `crates/crozier-e2e/tests/e2e.rs` reproduces its Fern 5.20.0 golden
byte-for-byte, with the single accepted upstream exception noted in the batch 4
table (`calorieninjas.com`) and the **three rows batch 14 registers with a
measured residual** (rows 130-132). A row registered without a golden and without
that exception is a hard harness error. A row registered with a residual declares
it: every divergent file is named in that corpus's `unmatched`, every file crozier
emits that its golden lacks is named in `crozier_only_files`, and both lists fail
the gate the moment one of their entries starts matching — so a residual is
enumerated work, never a suppression. The measured state is `crates/crozier-e2e/tests/e2e.rs`;
re-measure with `just fixtures-gaps`.

A row withdrawn from the corpus leaves the table below, keeping its number, for a
*withdrawn* table under the batch that registered it, whose `decision` reads
`withdrawn` and whose last column says why; no recipe fetches it and no test
compares it. Row 224 is the one so far.

| # | name | method | source | pinned ref | license | decision | shapes |
|---:|---|---|---|---|---|---|---|
| 1 | `6-dot-authentiqio.appspot.com` | api-guru | https://api.apis.guru/v2/specs/6-dot-authentiqio.appspot.com/6/openapi.json | `6` | Apache 2.0 | committed | Authentiq API |
| 2 | `airbyte.local-config` | api-guru | https://api.apis.guru/v2/specs/airbyte.local/config/1.0.0/openapi.json | `1.0.0` | MIT | committed | Airbyte Configuration API |
| 3 | `anchore.io` | api-guru | https://api.apis.guru/v2/specs/anchore.io/0.1.20/openapi.json | `0.1.20` | Apache 2.0 | committed | Anchore Engine API Server |
| 4 | `apache.org` | api-guru | https://api.apis.guru/v2/specs/apache.org/2.5.1/openapi.json | `2.5.1` | Apache 2.0 | committed | Airflow API (Stable) |
| 5 | `apache.org-airflow` | api-guru | https://api.apis.guru/v2/specs/apache.org/airflow/2.5.1/openapi.json | `2.5.1` | Apache 2.0 | committed | Airflow API (Stable) |
| 6 | `apache.org-qakka` | api-guru | https://api.apis.guru/v2/specs/apache.org/qakka/v1/openapi.json | `v1` | Apache 2.0 | committed | Qakka |
| 7 | `apicurio.local-registry` | api-guru | https://api.apis.guru/v2/specs/apicurio.local/registry/2.4.x/openapi.json | `2.4.x` | Apache 2.0 | committed | Apicurio Registry API [v2] |
| 8 | `apideck.com-accounting` | api-guru | https://api.apis.guru/v2/specs/apideck.com/accounting/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | Accounting API |
| 9 | `apideck.com-connector` | api-guru | https://api.apis.guru/v2/specs/apideck.com/connector/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | Connector API |
| 10 | `apideck.com-crm` | api-guru | https://api.apis.guru/v2/specs/apideck.com/crm/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | CRM API |
| 11 | `apideck.com-customer-support` | api-guru | https://api.apis.guru/v2/specs/apideck.com/customer-support/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | Customer Support |
| 12 | `apideck.com-ecommerce` | api-guru | https://api.apis.guru/v2/specs/apideck.com/ecommerce/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | Ecommerce API |
| 13 | `apideck.com-ecosystem` | api-guru | https://api.apis.guru/v2/specs/apideck.com/ecosystem/0.0.6/openapi.json | `0.0.6` | Apache 2.0 | committed | Ecosystem API |
| 14 | `apideck.com-file-storage` | api-guru | https://api.apis.guru/v2/specs/apideck.com/file-storage/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | File storage API |
| 15 | `apideck.com-hris` | api-guru | https://api.apis.guru/v2/specs/apideck.com/hris/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | HRIS API |
| 16 | `apideck.com-issue-tracking` | api-guru | https://api.apis.guru/v2/specs/apideck.com/issue-tracking/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | Issue Tracking API |
| 17 | `apideck.com-lead` | api-guru | https://api.apis.guru/v2/specs/apideck.com/lead/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | Lead API |
| 18 | `apideck.com-pos` | api-guru | https://api.apis.guru/v2/specs/apideck.com/pos/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | POS API |
| 19 | `apideck.com-proxy` | api-guru | https://api.apis.guru/v2/specs/apideck.com/proxy/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | Proxy API |
| 20 | `apideck.com-sms` | api-guru | https://api.apis.guru/v2/specs/apideck.com/sms/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | SMS API |
| 21 | `apideck.com-vault` | api-guru | https://api.apis.guru/v2/specs/apideck.com/vault/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | Vault API |
| 22 | `apideck.com-webhook` | api-guru | https://api.apis.guru/v2/specs/apideck.com/webhook/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | Webhook API |
| 23 | `apis.guru` | api-guru | https://api.apis.guru/v2/specs/apis.guru/2.2.0/openapi.json | `2.2.0` | CC0 1.0 | committed | APIs.guru |
| 24 | `appwrite.io-client` | api-guru | https://api.apis.guru/v2/specs/appwrite.io/client/0.9.3/openapi.json | `0.9.3` | BSD-3-Clause | committed | Appwrite |
| 25 | `appwrite.io-server` | api-guru | https://api.apis.guru/v2/specs/appwrite.io/server/0.9.3/openapi.json | `0.9.3` | BSD-3-Clause | committed | Appwrite |
| 26 | `asana.com` | api-guru | https://api.apis.guru/v2/specs/asana.com/1.0/openapi.json | `1.0` | Apache 2.0 | committed | Asana |
| 27 | `atlassian.com-jira` | api-guru | https://api.apis.guru/v2/specs/atlassian.com/jira/1001.0.0-SNAPSHOT/openapi.json | `1001.0.0-SNAPSHOT` | Apache 2.0 | committed | The Jira Cloud platform REST API |
| 28 | `axesso.de` | api-guru | https://api.apis.guru/v2/specs/axesso.de/1.0.0/openapi.json | `1.0.0` | Apache 2.0 | committed | Axesso Api |
| 29 | `bbci.co.uk` | api-guru | https://api.apis.guru/v2/specs/bbci.co.uk/1.0/openapi.json | `1.0` | MIT | committed | BBC iPlayer Business Layer |
| 30 | `bintable.com` | api-guru | https://api.apis.guru/v2/specs/bintable.com/1.0.0-oas3/openapi.json | `1.0.0-oas3` | Apache 2.0 | committed | BIN Lookup API |
| 31 | `box.com` | api-guru | https://api.apis.guru/v2/specs/box.com/2.0.0/openapi.json | `2.0.0` | Apache-2.0 | committed | Box Platform API |
| 32 | `bungie.net` | api-guru | https://api.apis.guru/v2/specs/bungie.net/2.18.0/openapi.json | `2.18.0` | BSD License 2.0 | committed | Bungie.Net API |
| 33 | `bunq.com` | api-guru | https://api.apis.guru/v2/specs/bunq.com/1.0/openapi.json | `1.0` | Apache 2.0 | committed | bunq API |
| 34 | `byautomata.io` | api-guru | https://api.apis.guru/v2/specs/byautomata.io/1.0.1/openapi.json | `1.0.1` | Apache 2.0 | committed | Automata Market Intelligence API |
| 35 | `calorieninjas.com` | api-guru | https://api.apis.guru/v2/specs/calorieninjas.com/1.0.0/openapi.json | `1.0.0` | Apache 2.0 | committed | CalorieNinjas |
| 36 | `canada-holidays.ca` | api-guru | https://api.apis.guru/v2/specs/canada-holidays.ca/1.8.0/openapi.json | `1.8.0` | MIT | committed | Canada Holidays API |
| 37 | `codesearch.debian.net` | api-guru | https://api.apis.guru/v2/specs/codesearch.debian.net/1.4.0/openapi.json | `1.4.0` | Apache 2.0 | committed | Debian Code Search |
| 38 | `color.pizza` | api-guru | https://api.apis.guru/v2/specs/color.pizza/1.0.0/openapi.json | `1.0.0` | MIT | committed | Color Name API |
| 39 | `conjur.local` | api-guru | https://api.apis.guru/v2/specs/conjur.local/5.3.0/openapi.json | `5.3.0` | Apache 2.0 | committed | Conjur |
| 40 | `corrently.io` | api-guru | https://api.apis.guru/v2/specs/corrently.io/2.0.0/openapi.json | `2.0.0` | Apache 2.0 | committed | Corrently.io |
| 41 | `discourse.local` | api-guru | https://api.apis.guru/v2/specs/discourse.local/latest/openapi.json | `latest` | MIT | committed | Discourse API Documentation |
| 42 | `dnd5eapi.co` | api-guru | https://api.apis.guru/v2/specs/dnd5eapi.co/0.1/openapi.json | `0.1` | MIT License | committed | D&D 5e API |
| 43 | `eos.local` | api-guru | https://api.apis.guru/v2/specs/eos.local/1.0.0/openapi.json | `1.0.0` | MIT | committed | Net API |
| 44 | `esgenterprise.com` | api-guru | https://api.apis.guru/v2/specs/esgenterprise.com/1.0.0/openapi.json | `1.0.0` | MIT | committed | ESG Rating Data |
| 45 | `etherpad.local` | api-guru | https://api.apis.guru/v2/specs/etherpad.local/1.2.15/openapi.json | `1.2.15` | Apache 2.0 | committed | Etherpad API |
| 46 | `etsi.local-mec010-2_apppkgmgmt` | api-guru | https://api.apis.guru/v2/specs/etsi.local/MEC010-2_AppPkgMgmt/2.1.1/openapi.json | `2.1.1` | BSD-3-Clause | committed | ETSI GS MEC 010-2 - Part 2: Application lifecycle, rules and requirements manage |
| 47 | `gambitcomm.local-mimic` | api-guru | https://api.apis.guru/v2/specs/gambitcomm.local/mimic/21.00/openapi.json | `21.00` | Apache 2.0 | committed | MIMIC REST API |
| 48 | `github.com` | api-guru | https://api.apis.guru/v2/specs/github.com/1.1.4/openapi.json | `1.1.4` | MIT | committed | GitHub v3 REST API |
| 49 | `gov.bc.ca-news` | api-guru | https://api.apis.guru/v2/specs/gov.bc.ca/news/1.0/openapi.json | `1.0` | Apache 2.0 | committed | BC Gov News API Service 1.0 |
| 50 | `groundhog-day.com` | api-guru | https://api.apis.guru/v2/specs/groundhog-day.com/1.2.1/openapi.json | `1.2.1` | MIT | committed | Groundhog Day API |
| 51 | `amazonaws.com-cloudformation` | api-guru | https://api.apis.guru/v2/specs/amazonaws.com/cloudformation/2010-05-15/openapi.json | `2010-05-15` | Apache 2.0 License | committed | 132 ops, 465 schemas, 859 allOf, 1,523 header/query params, XML request/response, server variables |
| 52 | `netbox.dev` | api-guru | https://api.apis.guru/v2/specs/netbox.dev/3.4/openapi.json | `3.4` | Apache v2 License | committed | 844 ops, 233 schemas, 823 nullable, 1,318 readOnly, 6,867 params, custom formats/numeric enums |
| 53 | `squareup.com` | api-guru | https://api.apis.guru/v2/specs/squareup.com/2.0/openapi.json | `2.0` | Apache 2.0 | committed | 200 ops, 807 schemas, mutually recursive four-schema graph, two security schemes |
| 54 | `redhat.com-catalog_inventory` | api-guru | https://api.apis.guru/v2/specs/redhat.com/catalog_inventory/1.0.0/openapi.json | `1.0.0` | Apache 2.0 | committed | 40 deepObject params, 113 readOnly, multiple servers/server variables, inline bodies |
| 55 | `microcks.local` | api-guru | https://api.apis.guru/v2/specs/microcks.local/1.7.0/openapi.json | `1.7.0` | Apache 2.0 | committed | discriminator with two mappings, oneOf/allOf, binary multipart bodies |
| 56 | `xero.com-xero-payroll-au` | api-guru | https://api.apis.guru/v2/specs/xero.com/xero-payroll-au/2.9.4/openapi.json | `2.9.4` | MIT | committed | UUID-heavy graph, readOnly fields, inline request bodies, header/path/query mix |
| 57 | `openfigi.com` | api-guru | https://api.apis.guru/v2/specs/openfigi.com/1.4.0/openapi.json | `1.4.0` | Apache 2.0 | committed | simple-style path param, wildcard response media, oneOf, alternative document security, server variable |
| 58 | `openbanking.org.uk-account-info-openapi` | api-guru | https://api.apis.guru/v2/specs/openbanking.org.uk/account-info-openapi/3.1.7/openapi.json | `3.1.7` | open-licence (MIT) | committed | 209 schemas, 1,188 refs, application/jose+jwe, dual security schemes; Crozier invalid-Python gap |
| 59 | `maif.local-otoroshi` | api-guru | https://api.apis.guru/v2/specs/maif.local/otoroshi/1.5.0-dev/openapi.json | `1.5.0-dev` | Apache 2.0 | committed | 22 oneOf, NDJSON request bodies, SSE response, 102 ops, format diversity |
| 60 | `traccar.org` | api-guru | https://api.apis.guru/v2/specs/traccar.org/5.6/openapi.json | `5.6` | Apache 2.0 | committed | GPX/XML, CSV, XLSX media, urlencoded request, six servers/two variables |
| 61 | `twilio.com-twilio_voice_v1` | api-guru | https://api.apis.guru/v2/specs/twilio.com/twilio_voice_v1/1.42.0/openapi.json | `1.42.0` | Apache 2.0 | committed | 17 path-level servers, 87 nullable nodes, urlencoded bodies, custom formats |
| 62 | `portfoliooptimizer.io` | api-guru | https://api.apis.guru/v2/specs/portfoliooptimizer.io/1.0.9/openapi.json | `1.0.9` | Apache 2.0 | committed | 83 operations and 15 oneOf across an all-inline zero-component-schema surface |
| 63 | `reverb.com` | api-guru | https://api.apis.guru/v2/specs/reverb.com/3.0/openapi.json | `3.0` | Apache 2.0 | committed | 163 operations, 126 paths, zero component schemas, 21 inline request bodies |
| 64 | `redocly.com-museum` | github-raw | https://raw.githubusercontent.com/Redocly/museum-openapi-example/2770b2b2e59832d245c7b0eb0badf6568d7efb53/openapi.yaml | `2770b2b2e59832d245c7b0eb0badf6568d7efb53` | MIT | committed | OpenAPI 3.1; 8 operations/5 paths; allOf; UUID/date/email/binary; image/png and problem+json |
| 65 | `http-toolkit` | github-raw | https://raw.githubusercontent.com/benc-uk/http-toolkit/56534e825a225b0d4133c3a0613526094ff03663/cmd/swagger-ui/openapi.json | `56534e825a225b0d4133c3a0613526094ff03663` | MIT | committed | OpenAPI 3.0; 26 operations/16 paths; wildcard paths; GET/POST/PUT/PATCH/DELETE; basic and bearer auth; UUID and binary responses |
| 66 | `frankfurter` | github-raw | https://raw.githubusercontent.com/lineofflight/frankfurter/e8b3311fe0f3d86b18d5c08b22dca707fb010d1c/lib/public/v2/openapi.json | `e8b3311fe0f3d86b18d5c08b22dca707fb010d1c` | MIT | committed | OpenAPI 3.1.2; 15 nullable-via-`type`-array schemas; array and object responses; currency enums |
| 67 | `worldcoin-signup-sequencer` | github-raw | https://raw.githubusercontent.com/worldcoin/signup-sequencer/f2870f1412517bfc2377838ff20cb0ee03ddaf72/schemas/openapi-v3.yaml | `f2870f1412517bfc2377838ff20cb0ee03ddaf72` | MIT | committed | OpenAPI 3.1; two tuple-array schemas using `prefixItems`; reusable request bodies; bearer authentication |
| 68 | `electric-sql` | github-raw | https://raw.githubusercontent.com/electric-sql/electric/be716ccdb225e7b60919c3f46ea92ad5332ff31a/website/electric-api.yaml | `be716ccdb225e7b60919c3f46ea92ad5332ff31a` | Apache-2.0 | committed | OpenAPI 3.1; `patternProperties`; polymorphic query parameters; streaming responses |
| 69 | `tamoss` | github-raw | https://raw.githubusercontent.com/livewyer-ops/tamoss/ccbef170204082f3ae3842c2ffee476f5008e1fb/src/openapi-contract.yaml | `ccbef170204082f3ae3842c2ffee476f5008e1fb` | Apache-2.0 | committed | OpenAPI 3.1; `if`/`then`/`else`; eight `const` schemas; eight top-level webhooks with inline bodies |
| 70 | `appng-rest-api` | github-raw | https://raw.githubusercontent.com/appNG/appng/8d9ff98f7d3ddd3e74340bcfb322c12df2ed189b/appng-rest-api/src/main/resources/org/appng/api/rest/appng-openapi.yaml | `8d9ff98f7d3ddd3e74340bcfb322c12df2ed189b` | Apache-2.0 | committed | Deployed appNG REST API with three matrix path parameters (`explode: true`) and a cookie parameter |
| 71 | `slurmdb-rest` | github-raw | https://raw.githubusercontent.com/ubccr/slurmdbrest/f9c5e77cc3a1a11c7645dab31c6752cd08577721/api/openapi.yaml | `f9c5e77cc3a1a11c7645dab31c6752cd08577721` | Apache-2.0 | committed | SlurmDB REST API with a label path parameter (`explode: false`) and 33 form parameters with explicit `explode` |
| 72 | `nimisampo` | github-raw | https://raw.githubusercontent.com/SemanticComputing/nimisampo.fi/34b8d22fff53a3dd531e89277fdb2f98d69dd1d0/src/server/openapi.yaml | `34b8d22fff53a3dd531e89277fdb2f98d69dd1d0` | MIT | committed | Deployed NameSampo API with a query parameter carrying `content: { application/json: ... }` and three `allowReserved` parameters |
| 73 | `free5gc-pdu-session` | github-raw | https://raw.githubusercontent.com/free5gc/openapi/8d0ee35bc671dd9995240c0ff73d4c75075a204a/Nsmf_PDUSession/api/openapi.yaml | `8d0ee35bc671dd9995240c0ff73d4c75075a204a` | Apache-2.0 | committed | free5GC PDU Session API with multipart `encoding` properties combining `contentType` and per-part `headers` |
| 74 | `sigstore-rekor` | github-raw | https://raw.githubusercontent.com/trailofbits/sigstore-apis/c6bd8db7b1629104dfe241ad26a838f69199b169/openapi/rekor.openapi.json | `c6bd8db7b1629104dfe241ad26a838f69199b169` | Apache-2.0 | committed | Sigstore Rekor API with eight literal `2XX` plus `default` response pairs, 12 discriminators without mappings, and seven nested objects combining `readOnly` and `writeOnly` properties |
| 75 | `letta` | github-raw | https://raw.githubusercontent.com/letta-ai/letta/e3fb00f97009cafe527cde93983cda0dfdd7e574/fern/openapi.json | `e3fb00f97009cafe527cde93983cda0dfdd7e574` | Apache-2.0 | committed | Letta API with 10 `text/event-stream` responses, 12 discriminators without mappings, 1 map-of-union schema, and 1,416 `anyOf` plus 87 `oneOf` compositions |
| 76 | `free5gc-namf-communication` | github-raw | https://raw.githubusercontent.com/shynuu/free5gc-cli/7f775ecab0cbe3074b38e528581641cff5520c2f/lib/openapi/Namf_Communication/api/openapi.yaml | `7f775ecab0cbe3074b38e528581641cff5520c2f` | Apache-2.0 | committed | free5GC AMF Communication API with `ServiceAreaRestriction/allOf/0/oneOf/0/not` and 142 `application/problem+json` response media entries |
| 77 | `apideck.com-ats` | api-guru | https://api.apis.guru/v2/specs/apideck.com/ats/9.3.0/openapi.json | `9.3.0` | Apache 2.0 | committed | ATS API with an inline object nested in `Applicant.properties.social_links.items` |
| 78 | `buildrelay` | github-raw | https://raw.githubusercontent.com/cnorlander/BuildRelay/e5f47309d1ca6fd28267de041e7ed2f61e477723/openapi.json | `e5f47309d1ca6fd28267de041e7ed2f61e477723` | MIT | committed | BuildRelay API with a referenced request body and a direct inline-object `500` response body |
| 79 | `tlon-notes` | github-raw | https://raw.githubusercontent.com/tloncorp/tlon-apps/2277696dcebb66270c6953b983e1a580b780071e/desk/app/notes/openapi.json | `2277696dcebb66270c6953b983e1a580b780071e` | MIT | committed | Tlon Notes API with four inline, untitled discriminated unions lacking mappings and a recursive `ImportNode` schema |
| 80 | `twilio.com-twilio_messaging_v1` | api-guru | https://api.apis.guru/v2/specs/twilio.com/twilio_messaging_v1/1.42.0/openapi.json | `1.42.0` | Apache 2.0 | committed | Twilio Messaging API with a `russell_3000` property that exercises Fern's underscore-before-trailing-digit rename |
| 81 | `livepeer-ai-runner` | github-raw | https://raw.githubusercontent.com/livepeer/ai-runner/50a742cee7c5789ef4a10f8117f30de3758366a9/openapi.yaml | `50a742cee7c5789ef4a10f8117f30de3758366a9` | MIT | committed | Livepeer AI Runner with three untagged, groupless root operations alongside ten tagged pipeline operations |
| 82 | `eos.local-extra-fields-forbid` | api-guru | https://api.apis.guru/v2/specs/eos.local/1.0.0/openapi.json | `1.0.0` | MIT | committed | Row 43's Net API regenerated with `pydantic_config.extra_fields: forbid`, pinning `extra="forbid"` / `pydantic.Extra.forbid` |
| 83 | `med-anvisa-price` | github-raw | https://raw.githubusercontent.com/breno12321/medAnvisaPrice/43866742c2db0f2064ceb99071ebb058c804580b/docs/apiSchema.yml | `43866742c2db0f2064ceb99071ebb058c804580b` | MIT | committed | Latin-1 accented enum values Fern folds into ASCII member names (`SUBSTANCIA = "SUBSTÂNCIA"`) beside accented property names it drops the accent from (`laborat_rio` aliased to `LABORATÓRIO`) |
| 84 | `sac-backend` | github-raw | https://raw.githubusercontent.com/walter1705/SAC/3c0ee7959c334a750496d2db2c26791a5aa0185f/backend/src/main/resources/static/openapi.yaml | `3c0ee7959c334a750496d2db2c26791a5aa0185f` | MIT | committed | Second, independent witness of the accent-dropping property rule from another project and language: `tamaño` becomes `tama_o` with the wire name kept as the alias |
| 85 | `kytos-sdntrace-cp` | github-raw | https://raw.githubusercontent.com/kytos-ng/sdntrace_cp/269f4482ecd4125dc1c115e059dbce26b7269216/openapi.yml | `269f4482ecd4125dc1c115e059dbce26b7269216` | MIT | committed | Kytos SDNTrace-CP API whose two operations both declare `424`, pinning Fern's `FailedDependencyError` name for a status no golden emitted |
| 86 | `withsecure-gdpr-subject-rights` | github-raw | https://raw.githubusercontent.com/WithSecureOpenSource/gdpr-subject-rights-api/0d2775dbf1c0830671a9efd878f03ae1eaf97995/openapi.yaml | `0d2775dbf1c0830671a9efd878f03ae1eaf97995` | Apache 2.0 | committed | WithSecure GDPR subject-rights API whose five operations declare `451`, pinning Fern's `UnavailableForLegalReasonsError` name for a status no golden emitted |
| 87 | `prometheus-x-edge-computing` | github-raw | https://raw.githubusercontent.com/Prometheus-X-association/edge-computing/78ed883317ec8739e985780c998d9f73f1e370a8/spec/openapi.yaml | `78ed883317ec8739e985780c998d9f73f1e370a8` | Apache-2.0 | committed | Prometheus-X edge-computing API declaring `408` and `412`, pinning Fern's `RequestTimeoutError` and `PreconditionFailedError` names for two statuses no golden emitted |
| 88 | `exa-gate` | github-raw | https://raw.githubusercontent.com/apaidedie/exa-gate/37cf047d828665004b4900ce672aa3f27b0bb844/docs/openapi.json | `37cf047d828665004b4900ce672aa3f27b0bb844` | MIT | committed | Exa Gate API declaring `423` and `426`, pinning Fern's `LockedError` and `UpgradeRequiredError` names for two statuses no golden emitted |
| 89 | `amazonaws.com-cloudfront` | api-guru | https://api.apis.guru/v2/specs/amazonaws.com/cloudfront/2016-11-25/openapi.json | `2016-11-25` | Apache 2.0 License | committed | AWS CloudFront API whose 27 operations declare `502`, `505`, `506`, `507`, `508`, `510` and `511`, pinning Fern's `BadGatewayError`, `HttpVersionNotSupportedError`, `VariantAlsoNegotiatesError`, `InsufficientStorageError`, `LoopDetectedError`, `NotExtendedError` and `NetworkAuthenticationRequiredError` names for seven statuses no golden emitted |
| 90 | `khoainats` | github-raw | https://raw.githubusercontent.com/cukhoaimon/khoainats/e680e29affee221e3a6c379b1e51c98ef241da7a/api/generated/.docs/api/openapi.yaml | `e680e29affee221e3a6c379b1e51c98ef241da7a` | MIT | committed | Khoai NATS Admin API declaring an `openIdConnect` scheme (`Roles`) beside an HTTP bearer one, with `/v1/noauth` unsecured: `openIdConnect` is the one member of its scheme family Fern imports rather than drops, and this row pins the optional bearer `token` Fern emits for such a document |
| 91 | `helios-verifiable-api` | github-raw | https://raw.githubusercontent.com/a16z/helios/43a8c9f3cdda41a6f383c4db41d9a83f102638b1/verifiable-api/server/openapi.yaml | `43a8c9f3cdda41a6f383c4db41d9a83f102638b1` | MIT | committed | 27 component schemas that are remote-URL `$ref`s into seven `ethereum/execution-apis` documents, which Fern fetches and resolves transitively — the only reference form Fern was measured to follow rather than discard. All seven referenced documents are committed alongside the root; routine checks resolve them locally. Upstream writes those seven references against `refs/heads/main`, so `tests/fixtures/corpus-remote-ref-pins.tsv` records a pinned commit URL and a SHA-256 for each, and `tools/corpus/fetch-corpus.sh` substitutes them into the fetched document before publishing it: this row's inputs are upstream's bytes plus exactly that recorded substitution, and no longer whatever the branch serves today |
| 92 | `eozilla` | github-raw | https://raw.githubusercontent.com/eo-tools/eozilla/70187a1bba9fe5a77001a623322f23bb30ea49c7/tools/openapi.yaml | `70187a1bba9fe5a77001a623322f23bb30ea49c7` | Apache-2.0 | committed | Eozilla OGC API - Processes server whose `Schema` component closes two cycles through `additionalProperties` (`Schema.properties.<k>` and `Schema.discriminator.mapping` both name `Schema`), the map-of-self form no other golden declares |
| 93 | `openepcis-dpp-ready` | github-raw | https://raw.githubusercontent.com/openepcis/openepcis-dpp-ready/5c1f308d350cfcc9abb80aa6c70262c87141f201/extensions/common/interop/api/en18222-dpp-api.openapi.yaml | `5c1f308d350cfcc9abb80aa6c70262c87141f201` | Apache-2.0 | committed | EN 18222 Digital Product Passport API declaring two `type: [string, number, boolean]` arrays — two non-null members each, the multi-type form the other 498 `type` arrays in the corpus never take |
| 94 | `ndw-accessibility-map` | github-raw | https://raw.githubusercontent.com/ndwnu/nls-accessibility-map/46fde7c8b36ac8776eba78079bb53bf42ae17c2b/specification/src/main/resources/nu/ndw/nls/accessibilitymap/specification/v2.yaml | `46fde7c8b36ac8776eba78079bb53bf42ae17c2b` | MIT | committed | NDW Location Services accessibility-map API whose two `components.headers` Header Objects (`Accept-encoding`, `Content-encoding`) each declare `allowEmptyValue`, the Header Object field no other registered source declares |
| 95 | `marimo` | github-raw | https://raw.githubusercontent.com/marimo-team/marimo/257ea7a983e2dbe4627f0168072fdcd538c93c5c/packages/openapi/api.yaml | `257ea7a983e2dbe4627f0168072fdcd538c93c5c` | Apache-2.0 | committed | Marimo API whose `Base64String` component declares `contentEncoding: base64`, the JSON Schema 2020-12 encoding keyword no prior golden source declares |
| 96 | `blackadi-oauth2` | github-raw | https://raw.githubusercontent.com/blackadi/OAUTH2.0/b6e4cfa1fb060ca5ca3e32185f4a5d88c27163e3/server/src/routes/openapi.json | `b6e4cfa1fb060ca5ca3e32185f4a5d88c27163e3` | MIT | committed | OAuth 2.0 authorization-server API declaring `scheme: dpop` (RFC 9449) on `dpopAuth` beside `bearer` and `basic` — the only registered source declaring an IANA HTTP authentication scheme Fern's importer does not support, so its golden pins that crozier drops the scheme exactly as Fern does |
| 97 | `mosip-esignet` | github-raw | https://raw.githubusercontent.com/mosip/esignet/201264c86e98113762451f4a306163233fa79e24/docs/esignet-openapi.yaml | `201264c86e98113762451f4a306163233fa79e24` | MPL-2.0 | committed | MOSIP eSignet OIDC/identity API, the second registered witness of `scheme: DPoP` (RFC 9449): `Authorization-DPoP` declares it in the registry's own mixed-case spelling beside four `bearer` schemes, where row 96 declares the lowercase one |
| 98 | `openbankingproject-ch-kundenbeziehung` | github-raw | https://raw.githubusercontent.com/openbankingproject-ch/Open-API-Kundenbeziehung-Legacy/c7439ba67f5790d901d1d20943cae5cb48e8e7fc/api/openapi.yaml | `c7439ba67f5790d901d1d20943cae5cb48e8e7fc` | MIT (declared by the document's `info.license`; the repository carries no license file) | committed | Swiss Open Banking customer-relationship API, the third `scheme: DPoP` witness and the corpus's first source declaring `type: mutualTLS` — the 3.1-only Security Scheme type no prior registered source declares |
| 99 | `cyberark-conjur-api` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/9d36c7e3808ebe65d69e81d3c3250598927a575c/apis/openapi/cyberark.com/conjur-api/5.3.2/openapi.json | `9d36c7e3808ebe65d69e81d3c3250598927a575c` | Apache-2.0 (declared by the document's `info.license`, inside a CC0-1.0 repository) | committed | CyberArk Conjur 5.3.2, the corpus's only source declaring `scheme: mutual` (RFC 8120): `conjurKubernetesMutualTls` carries it beside a `basic` scheme and an `apiKey` one, so its golden pins that crozier drops the IANA scheme Fern's importer does not support exactly where Fern does. Its `paths` are relative-file `$ref`s into sibling documents the direct spec URL does not carry, which Fern discards without diagnosing; the golden is therefore the endpoint-free client that pairing leaves behind |
| 100 | `adyen-report-notification` | github-raw | https://raw.githubusercontent.com/Adyen/adyen-openapi/4265e8ffe6cc4c35fe6804d5a395598621d3da53/json/BalancePlatformReportNotification-v1.json | `4265e8ffe6cc4c35fe6804d5a395598621d3da53` | MIT | committed | Adyen "Report webhooks", the corpus's first source that omits `paths` entirely: a valid OpenAPI 3.1 document whose only API surface is one webhook (`balancePlatform.report.created`) over five component schemas, so its golden pins what Fern emits when the field the whole endpoint pipeline reads is absent |
| 101 | `adyen-managed-risk-notification` | github-raw | https://raw.githubusercontent.com/Adyen/adyen-openapi/4265e8ffe6cc4c35fe6804d5a395598621d3da53/json/BalancePlatformManagedRiskNotification-v1.json | `4265e8ffe6cc4c35fe6804d5a395598621d3da53` | MIT | committed | Adyen "Managed risk webhooks", the corpus's first source whose top-level `webhooks` stand alone with no `paths` beside them — eight of them, over 19 component schemas — where row 69's eight webhooks accompany a populated Paths Object; it also declares `jsonSchemaDialect` |
| 102 | `go-kratos-casbin-admin` | github-raw | https://raw.githubusercontent.com/go-kratos/examples/61daed1ec4d5a94d689bc8fab9bc960c6af73ead/casbin/app/admin/openapi.yaml | `61daed1ec4d5a94d689bc8fab9bc960c6af73ead` | MIT | committed | The protoc-gen-openapi document the go-kratos Casbin example ships, the first of the corpus's two independent witnesses of an *empty* Paths Object: `paths: {}` beside `components.schemas: {}` and an empty `info.title`, the distinct shape from rows 100 and 101's omitted `paths`; row 103 is the second |
| 103 | `descope-authzcache` | github-raw | https://raw.githubusercontent.com/descope/authzcache/0a333ee3b1152b869c3b41061e43aa0b63ed68a0/pkg/authzcache/proto/v1/doc/authz.openapi.yaml | `0a333ee3b1152b869c3b41061e43aa0b63ed68a0` | MIT | committed | The `protoc-gen-openapi` document Descope's authzcache service ships, a second and independent witness of the empty Paths Object row 102 pins: the same `paths: {}` beside `components.schemas: {}` and an empty `info.title`, from another repository and another project |
| 104 | `swagger-petstore` | github-raw | https://raw.githubusercontent.com/swagger-api/swagger-petstore/d57941e8fe959e508796b27469b1e8bba73392dc/src/main/resources/openapi.yaml | `d57941e8fe959e508796b27469b1e8bba73392dc` | Apache-2.0 | committed | The Swagger Petstore reference document, the corpus's only source declaring `openapi: 3.0.4` — the patch level OpenAPI's own 3.0 maintenance release added, which no other registered source and no vendor portal the witness search put to it reaches — over 13 paths, an `apiKey` and an OAuth2 implicit scheme, and a `multipart/form-data` upload |
| 105 | `cyclonedx-transparency-exchange` | github-raw | https://raw.githubusercontent.com/CycloneDX/transparency-exchange-api/26c944ec226850ca0bbe0de5a18137ced1ca7c9d/spec/openapi.yaml | `26c944ec226850ca0bbe0de5a18137ced1ca7c9d` | Apache-2.0 | committed | The OWASP Transparency Exchange API specification, the corpus's only source declaring `openapi: 3.1.1` and its second declaring `jsonSchemaDialect` (`https://spec.openapis.org/oas/3.1/dialect/base`, beside row 101's), over 23 paths whose schemas lean on 3.1 type arrays and `$ref` siblings |
| 106 | `adyen-capital` | github-raw | https://raw.githubusercontent.com/Adyen/adyen-openapi/4265e8ffe6cc4c35fe6804d5a395598621d3da53/json/CapitalService-v1.json | `4265e8ffe6cc4c35fe6804d5a395598621d3da53` | MIT | committed | Adyen "Capital API", the document the `json-schema-dialect` witness search itself named, and the corpus's third source declaring `jsonSchemaDialect` — `https://spec.openapis.org/oas/3.1/dialect/base` over 10 paths and 54 component schemas, where row 101 declares it over a webhook-only document and row 105 over a `3.1.1` one, so this row is the dialect's first witness beside an ordinary populated Paths Object with `apiKey` and `basic` schemes |
| 107 | `apivideo-android-uploader` | github-raw | https://raw.githubusercontent.com/apivideo/api.video-android-uploader/01952c8755c2e3557b6a1785a83ca1e473ab5ffa/api/openapi.yaml | `01952c8755c2e3557b6a1785a83ca1e473ab5ffa` | MIT | committed | The api.video document its Android uploader ships, the corpus's only source declaring a Reference Object `description` sibling: `components.parameters.filterBy` is a `$ref` to `filterBy_2` carrying its own `description`, the shape OpenAPI 3.1 promoted to a first-class Reference Object field, over four paths, a `bearerAuth` and an `apiKey` scheme and a `multipart/form-data` upload |
| 108 | `truefoundry-trueforge` | github-raw | https://raw.githubusercontent.com/truefoundry/trueforge/284762ff19269da458790531304fbaee16c6b6ee/docs/openapi.json | `284762ff19269da458790531304fbaee16c6b6ee` | MIT | committed | The TrueForge API document, the corpus's only source declaring `x-fern-ignore` — four Operation Objects carry it — and its only source declaring Fern's SDK-shaping extensions beside it: `x-fern-sdk-group-name` at 54 sites, eight of them two-level nested groups, `x-fern-sdk-method-name` at 54, `x-fern-pagination` at 7 and `x-fern-streaming` at 2, over 40 paths and 218 component schemas with no `operationId` anywhere, so this row is what pins nested sub-clients, cursor pagination and per-node ignore against Fern |
| 109 | `volview-backend-contract` | github-raw | https://raw.githubusercontent.com/Kitware/VolView/496ada04c1d07235f98c92a68b5c374c7188ee87/backend-contract/generated/openapi.json | `496ada04c1d07235f98c92a68b5c374c7188ee87` | Apache-2.0 | committed | The neutral backend contract VolView's own client calls, the corpus's only source declaring `$comment`: `components.schemas.TaskSpec` and `components.schemas.AnnotationsFile` each carry the JSON Schema 2020-12 annotation keyword, over nine paths, 15 component schemas and a `jsonSchemaDialect` of `https://json-schema.org/draft/2020-12/schema` — the dialect URI no other registered source names, where rows 101, 105 and 106 name the OAS 3.1 dialect |
| 110 | `osparc-simcore-webserver` | github-raw | https://raw.githubusercontent.com/ITISFoundation/osparc-simcore/7fa7c73d34bb3bf4d22477a1bc5d9970c2824607/services/web/server/src/simcore_service_webserver/api/v0/openapi.json | `7fa7c73d34bb3bf4d22477a1bc5d9970c2824607` | MIT | committed | The web API the IT'IS Foundation's own oSPARC front end calls, the corpus's only source declaring the JSON Schema 2020-12 string-encoding pair `contentMediaType` (24 sites) and `contentSchema` (24), the only one declaring `exclusiveMaximum` with a *numeric* value (8, the 3.1 spelling beside the 3.0 boolean the corpus already carries) and the second declaring `propertyNames` (30, beside row 109's 7), over 214 paths and 480 component schemas |
| 111 | `helixdb-http-api` | github-raw | https://raw.githubusercontent.com/HelixDB/helix-db/f19b488b3d48ec1da90f3dfcbac40f1c43d1e596/docs/openapi.json | `f19b488b3d48ec1da90f3dfcbac40f1c43d1e596` | Apache-2.0 | committed | The HTTP API HelixDB's own database serves, the corpus's only source declaring `dependentRequired` — `components.schemas.ReadQueryRequest` and `components.schemas.WriteQueryRequest` each carry one — beside two `propertyNames`, over three paths, 17 component schemas and a `bearerAuth` scheme, in 25 KB |
| 112 | `flowdapt` | github-raw | https://raw.githubusercontent.com/emergentmethods/flowdapt/e8f34d411564e6c0e6542fe67d0604c23de1cf91/openapi.json | `e8f34d411564e6c0e6542fe67d0604c23de1cf91` | Apache-2.0 | committed | The API the Flowdapt server publishes for itself, the corpus's only source declaring `$defs` — seven JSON Schema subschema bundles inside `components.schemas` — over 15 paths and 42 component schemas of an `openapi: 3.0.2` document, so the golden pins what Fern does with a 2020-12 definitions keyword written in a 3.0 document |
| 113 | `k8s-container-service-provider` | github-raw | https://raw.githubusercontent.com/dcm-project/k8s-container-service-provider/2fb9a6decfdb290e819a1571ecb11ca4966ec19a/api/v1alpha1/openapi.yaml | `2fb9a6decfdb290e819a1571ecb11ca4966ec19a` | Apache-2.0 | committed | The API the DCM project's own Kubernetes container service provider serves, the corpus's only source declaring `format: json-pointer` — `components.schemas.Error.pointer` and `components.schemas.ErrorDetail.pointer` each annotate a string field with the RFC 6901 format, on the RFC 7807 problem detail the service returns — over three paths, five operations and 18 component schemas of an `openapi: 3.0.4` document |
| 114 | `daniweb-connect` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/daniweb.com/4/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`) | committed | The DaniWeb Connect API DaniWeb's own developer portal describes (`info.x-origin` records `https://www.daniweb.com/connect/developers/swagger`), the corpus's only source crossing `style: simple` with `in: path` over an **array** schema — 15 of them, the `ID` parameter of `/apps/{ID}`, `/audiences/{ID}`, `/conversations/{ID}` and twelve more, each `{in: path, style: simple, schema: {type: array, items: {type: integer}, maxItems: 100}}` — so this row pins the request URL Fern interpolates a list-valued path segment into, over 51 paths and 82 component schemas |
| 115 | `chaingateway-io` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/chaingateway.io/1.0/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`) | committed | The Ethereum gateway Chaingateway.io describes for itself (`info.x-origin` records `https://chaingateway.io/downloads/openapiv3.json`), the corpus's densest source crossing `style: simple` with `in: header` over a scalar schema — 26 of them across 21 operations, five of which declare two, where row 107 declares the crossing twice — so this row pins the header a Fern client sends for an explicitly-styled header parameter, over 21 paths and 45 component schemas |
| 116 | `hubspot-events` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/hubapi.com/events/v3/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`) | committed | HubSpot's Events API v3 (`info.x-origin` records `https://api.hubspot.com/api-catalog-public/v1/apis/events/v3/events`), the corpus's only source crossing `style: form` with `in: query` over an **object** schema — `objectProperty.{propname}` and `property.{propname}` on `GET /events/v3/events/`, each `{in: query, style: form, explode: true, schema: {type: object}}` — so this row pins the argument Fern declares for a free-form object query parameter whose name itself carries a template |
| 117 | `paloalto-remote-networks` | github-raw | https://raw.githubusercontent.com/PaloAltoNetworks/pan.dev/b9122449813f2a5fb2e1f9e403aae3d50c9712f4/openapi-specs/sase/config-orch/paloaltonetworks-Remote_Networks.yaml | `b9122449813f2a5fb2e1f9e403aae3d50c9712f4` | MIT (the repository's own licence; the document declares no `info.license`) | committed | The Configuration Orchestration API Palo Alto Networks publishes on its own developer portal, the corpus's only source crossing `style: deepObject` with an **array** schema — `components.parameters.RemoteNetworksNames`, `{in: query, style: deepObject, explode: true}` over `{type: array}` — so this row pins what Fern serialises when the object-only style meets a list |
| 118 | `openintegrationhub-secret-service` | github-raw | https://raw.githubusercontent.com/openintegrationhub/openintegrationhub/f82a32f8ce88a464874c1fcd3a39afd8e7e4908a/services/secret-service/doc/openapi.json | `f82a32f8ce88a464874c1fcd3a39afd8e7e4908a` | Apache-2.0 (`info.license` `Apache 2.0`, and the repository's own licence) | committed | The description the Open Integration Hub's Secrets Service ships beside its own source, the corpus's only source crossing `style: deepObject` with a **scalar** schema — `components.parameters.pageSize`, `{in: query, style: deepObject, schema: {type: integer}}` — the crossing the specification leaves undefined, so this row pins what Fern does with a style its schema cannot satisfy, over seven paths, 13 operations and 29 component schemas |
| 119 | `strapi-rest-api` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/strapi.io/strapi-rest-api/5.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`) | committed | Strapi's REST API, the second registered declarer of `style: deepObject` over an **array** schema — `components.parameters.fields`, `{in: query, style: deepObject, explode: true}` over `{type: array}`, beside row 117's one — so the two goldens pin the crossing on an independent document each, over four paths, 13 component parameters and 12 component schemas |
| 120 | `listennotes` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/listennotes.com/2.0/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`) | committed | The Listen Notes podcast API (`info.x-origin` records the publisher-served `https://listen-api.listennotes.com/api/v2/openapi.yaml`), a second and independent declarer of `style: simple` over an `in: header` scalar — `components.parameters.apiKeyParam` — and the corpus's densest `openapi: 3.1.0` source, over 23 paths and 102 component schemas whose four Response Header Objects reach the Header Object rows from the `components.headers` side |
| 121 | `vtex-pricing` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/vtex.local/Pricing-API/1.0/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`, and `vtex/openapi-schemas` declares none either, which is why the aggregation's copy is the one registered) | committed | VTEX's Pricing API (`info.x-origin` records VTEX's own `vtex/openapi-schemas` copy), the corpus's only source declaring a Header Object's `content` — 22 Response Header Objects carry a media type instead of a `schema` — and its densest `style: simple` header declarer at 28, over nine paths, five component schemas and two `apiKey` header schemes |
| 122 | `aws-importexport` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/amazonaws.com/importexport/2010-06-01/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | Apache-2.0 (`info.license` `Apache 2.0 License`; the aggregating repository is CC0-1.0) | committed | The AWS Import/Export Service description (`info.x-origin` records the publisher-served `https://raw.githubusercontent.com/aws/aws-sdk-js/master/apis/importexport-2010-06-01.normal.json`), the corpus's densest declarer of a parameter redeclared at both levels: each of its six paths declares `Action` and `Version` through `components.parameters`, and each path's `get` and `post` redeclare both `(name, in)` pairs inline — 24 Operation-over-Path-Item collisions, against the three the corpus already saw in a source with no golden. It pins whether Fern honours the specification's rule that the operation-level parameter wins |
| 123 | `openbanking-brasil-directory` | github-raw | https://raw.githubusercontent.com/OpenBanking-Brasil/specs-directory/37423cbc93982e05eac255db6226ed599a5baace/openapi.yaml | `37423cbc93982e05eac255db6226ed599a5baace` | MIT (declared by the document's `info.license`, `https://mit-license.org`; the repository carries no license file) | committed | The participant directory API Open Banking Brasil publishes for itself, the corpus's only source whose OAuth Flows Object declares **more than one** flow: `components.securitySchemes.oAuth` names `clientCredentials` (scopes `directory:admin`, `directory:software`) and `authorizationCode` (scope `directory:website`), whose scope sets are **disjoint** — so its golden pins which flow Fern reads a scope enum out of, where the corpus's other ten Flows Objects each name exactly one. It declares that scheme beside an `apiKey` one (`authorizer`), over 48 paths |
| 124 | `api-openverse-org` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/api.openverse.org/main/1.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | MIT (declared by the document's `info.license`, inside a CC0-1.0 repository) | committed | The Openverse media-search API, the corpus's first golden-bearing declarer of an **operation-level** optional security requirement — 6 Operation Objects whose `security` array holds `{}` — over 17 paths, so its golden pins whether an operation that opts authentication out still reaches the generated client's constructor |
| 125 | `discord-com` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/discord.com/main/10/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | MIT (declared by the document's `info.license`, inside a CC0-1.0 repository) | committed | Discord's own API v10, the second registered declarer of an **operation-level** optional security requirement — 22 Operation Objects whose `security` array holds `{}` — and the second whose OAuth Flows Object declares more than one flow (three, whose scope sets differ pairwise), so one `openapi: 3.1.0` document witnesses both of this batch's shapes over 128 paths |
| 126 | `braintrust-dev` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/braintrust.dev/main/1.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | Apache-2.0 (declared by the document's `info.license`, inside a CC0-1.0 repository) | committed | Braintrust's own API, the corpus's densest declarer of an **operation-level** optional security requirement — 148 Operation Objects whose `security` array holds `{}` — against the single `bearerAuth` scheme (`type: http`, `scheme: bearer`) Fern's importer supports, so it witnesses row 124's shape at 25 times the density over 71 paths |
| 127 | `torrentarr` | github-raw | https://raw.githubusercontent.com/Feramance/Torrentarr/b2b8bcec35b2d4bdb131b5bc0b326835982f6327/docs/assets/openapi.json | `b2b8bcec35b2d4bdb131b5bc0b326835982f6327` | MIT (the repository's own `LICENSE`; the document declares no `info.license`) | committed | The Torrentarr automation API, the corpus's only source declaring a **media type range** other than `*/*`: six `200` responses key their content on `image/*` over `{type: string, format: binary}` (`…/artist/{artist_id}/thumbnail`, `…/movie/{id}/thumbnail` and `…/series/{id}/thumbnail`, each under both `/api` and `/web`), which Fern emits as streamed `typing.Iterator[bytes]` methods, so this row pins what a range-keyed binary response becomes. It is also the corpus's first source declaring **two path templates that normalize to one**: `/api/arr/{category}/open/{kind}/{entryId}` beside `…/{entry_id}`, and the same pair under `/web/`, four keys in two groups that crozier's own `naming::field_name` folds to two. The collision is inside one document, so the golden's own raw clients say what Fern did with it — all four operations survive, as `redirect_to_arr_ui_for_movie_series_artist_author_api`, `api_arr_open_item`, `redirect_to_arr_ui_for_movie_series_artist_author_web` and `web_arr_open_item`, each pair rendering the identical request URL. Over 88 paths and a `bearerAuth` scheme |
| 128 | `agco-ats` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/agco-ats.com/main/v1/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`) | committed | AGCO's Advanced Technical Support API, the corpus's first source that **collides with itself** in two independent ways. Its Paths Object declares `/api/v2/Releases/{ReleaseId}` beside `/api/v2/Releases/{releaseId}`, two keys crozier's own `naming::field_name` normalizes to one `/api/v2/Releases/{release_id}`; and 22 of its Operation Objects share 11 `operationId` values, each written exactly twice (`Clients_Get` on `/api/v2/Clients` and `/api/v2/Clients/{ID}`, `Users_Get`, `Licenses_Get`, `PackageTypes_Get`, `UpdateGroups_Get`, `Vouchers_Get`, `ContentRelease_GetContentReleaseVersion`, `AuthorizationCodeDefinitions_GetAuthorizationCodeDefinition`, `PackageReports_Default`, `UserPermissions_Put` and `UserPermissions_GetPermissions`). Both collisions are inside one document, so the golden's own raw-client method set is what says what Fern did with them — it keeps both colliding routes, deconflicting the second's path parameter as `release_id_`, and it collapses each duplicated `operationId` to a single method. Over 163 paths and an `apiKey` header scheme |
| 129 | `svix-webhooks` | github-raw | https://raw.githubusercontent.com/svix/svix-webhooks/ee528fb27439a298da69c628fa1fabd70e9d55b9/server/openapi.json | `ee528fb27439a298da69c628fa1fabd70e9d55b9` | MIT (the repository's own `LICENSE`; the document declares no `info.license`) | committed | The Svix webhook-sending API, the second registered declarer of a duplicated `operationId` beside row 128 — `GET /api/v1/health` and `HEAD /api/v1/health` both carry `operationId: v1.health.get` — and the sharpest small illustration of what the collision costs, since the two operations differ only in HTTP method and one of them reaches no client method at all. Over 27 paths |
| 130 | `komga` | github-raw | https://raw.githubusercontent.com/gotson/komga/656001eb03bf8b54ca909f3e74fe2ec1b95dac48/komga/docs/openapi.json | `656001eb03bf8b54ca909f3e74fe2ec1b95dac48` | MIT (declared by the document's `info.license` and by the repository's own `LICENSE`) | committed | The API the Komga comics server publishes for itself, the second registered declarer of a **media type range** other than `*/*` beside row 127 — one `image/*` `default` response over `{type: string, format: binary}` on `GET /api/v1/books/{bookId}/pages/{pageNumber}`, against Torrentarr's six, and on the same response side — so the two goldens pin the range on an independent publisher each, over 139 paths of an `openapi: 3.1.0` document. **Registered with a measured `unmatched` set of 32 of its 338 files, not at full parity.** The measured cause is the *binary/streaming response*: Fern makes **30** `httpx_client.stream(...)` calls returning `typing.Iterator[bytes]` under a `@contextlib.contextmanager`, and crozier makes **6**. Komga keys its ranges on `default` — `GET /api/v1/books/{bookId}/pages/{pageNumber}` declares `400` of `*/*` and `default` of `image/*`, and no `200` at all — which crozier's `is_binary_response` never reaches, so `get_book_page_by_number` comes out as `HttpResponse[None]` where Fern streams it, and its `request_options` docstring loses Fern's `chunk_size` note. Two smaller causes ride along: crozier emits `content-type: application/json` on 13 request bodies Fern leaves to httpx, and types an array header parameter `typing.List` where Fern writes `typing.Sequence`. The `media-type-range` classification this row is registered for rests on row 127, which pins the `200` spelling byte for byte; this residual is the `default` spelling |
| 131 | `short-io` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/short.io/main/1.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`) | committed | The Short.io link API, the third registered declarer of two path templates that normalize to one — `/links/{link_id}` beside `/links/{linkId}`, folding to one `/links/{link_id}` under crozier's `naming::field_name` — and the first whose two colliding keys carry an *uneven* set of operations: `{link_id}` declares only `DELETE` while `{linkId}` declares `POST` and `GET`, and Fern keeps all three, across `client.link_management` and `client.link_queries`. Over 45 paths. **Registered with a measured `unmatched` set of 65 of its 198 files (77 when batch 14 registered it), not at full parity.** The measured cause is *hoisted per-operation models*: 59 of the 65 sit under a `types/` package. Two effects, both readable in the diff. Fern declares a module per `anyOf` member of a hoisted response type — `post_links_duplicate_link_id_response_ttl`, `…_expires_at`, `…_source` and 31 more — which crozier folds inline and never emits, so those entries report *"Crozier did not emit this Fern file"*. And where both emit a model, crozier carries the document's full declared property set while Fern narrows it: `BadRequestErrorBody` is `error` plus an optional `message` in the golden, against crozier's `error`, `success`, `message`, `field`, `link_id`, `code` and `status_code`. Neither effect touches the colliding `links` methods this row is registered for — all three survive on both sides |
| 132 | `webflow-v2` | github-raw | https://raw.githubusercontent.com/webflow/openapi-spec/f6db607359a412dd6aa6cd304674731d7f2dbe10/openapi/v2.yml | `f6db607359a412dd6aa6cd304674731d7f2dbe10` | MIT (declared by the document's `info.license` and by the repository's own `LICENSE`) | committed | Webflow's Data API v2, the third registered declarer of a duplicated `operationId` and the one where Fern's answer differs from rows 128 and 129's: `GET /forms/{form_id}/submissions` and `GET /sites/{site_id}/forms/{form_id}/submissions` both carry `operationId: list-submissions` and **both** survive, under different sub-clients sharing one response type, where AGCO and Svix each lose an operation. Over 75 paths of an `openapi: 3.1.0` document. **Registered with a measured `unmatched` set of 364 of its 1,495 files, and 148 crozier-only modules declared beside it in `crates/crozier-e2e/tests/e2e.rs`'s `crozier_only_files`, not at full parity.** Two measured causes, independent of each other. Its `servers` carry `x-fern-server-name: Data API`, so Fern names the environment member `FernApiEnvironment.DATA_API` and threads `base_url=self._client_wrapper.get_environment().base` through every raw-client call — 127 and 252 divergent lines respectively — where crozier writes `DEFAULT` and no `base_url`. And Fern names a `oneOf` request body's hoisted variants differently from crozier's `…_request_body_zero`/`…_one`, which is exactly what the 148 declared crozier-only modules under `collections/fields`, `collections/items` and the package root are. Neither cause touches the two `list-submissions` methods this row is registered for — both survive on both sides |
| 133 | `loris-dataquery` | github-raw | https://raw.githubusercontent.com/aces/Loris/3305a00312178ea75f135be1564beaf222b25822/modules/dataquery/static/schema.yml | `3305a00312178ea75f135be1564beaf222b25822` | GPL-3.0 (declared by the document's `info.license`, `GNU Public License, Version 3`, and by the repository's own `LICENSE`) | committed | The Data Query Tool API the LORIS neuroimaging platform ships inside its own source tree, the corpus's only source declaring **`style: spaceDelimited`** over a query parameter — `share` and `star` on `PATCH /queries/{QueryID}`, each over `{type: boolean}` — and its densest declarer of **`style: pipeDelimited`** over one, at four (`adminname`, `dashboardname`, `loginpagename` and `name`, each over `{type: string}`, on that same operation). Both are the specification's array-only serialisations declared over a *scalar* schema, the crossing it leaves undefined, so this golden pins what Fern emits for a style the schema cannot satisfy. It redeclares `style: simple` over an `in: path` scalar five times besides, across four path items. Over six paths, nine component schemas and an `apiKey` header scheme |
| 134 | `sftpgo` | github-raw | https://raw.githubusercontent.com/drakkan/sftpgo/c737df6cd42ef375bf51a2d0a04ea2b1ab9f8842/openapi/openapi.yaml | `c737df6cd42ef375bf51a2d0a04ea2b1ab9f8842` | AGPL-3.0 (declared by the document's `info.license`, `AGPL-3.0-only`, and by the repository's own `LICENSE`) | committed | The administration API the SFTPGo file-transfer server publishes for itself, the third registered declarer of a **media type range** other than `*/*` and by far the densest — ten content-map keys over five distinct ranges (`application/*`, `text/*`, `image/*`, `audio/*` and `video/*`, each declared on both `POST /shares/{id}/{fileName}` and `POST /user/files/upload`) against rows 127 and 130's six and one — and the first to declare one on the **request** side, where both of those declare theirs on responses only. It is also the second registered declarer of a parameter redeclared at both levels: `PUT /quotas/folders/{name}/usage` redeclares its path item's own `mode` query parameter, one Operation-over-Path-Item collision beside row 122's 24, and the one where the two declarations are otherwise identical — same `required`, same `description`, same two-member `enum` — so the golden pins that the operation-level declaration is taken even where nothing about it differs. Over 76 paths, 116 component schemas and three security schemes — `http` `basic`, `http` `bearer` and an `apiKey` header |
| 135 | `googleapis-servicebroker` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/googleapis.com/servicebroker/v1alpha1/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | Creative Commons Attribution 3.0 (the document's own `info.license`, Google's grant over its own description; the aggregating repository is CC0-1.0) | committed | Google's Service Broker API (`info.x-origin` records the publisher-served `https://servicebroker.googleapis.com/$discovery/rest?version=v1alpha1`), the fourth registered declarer of **two path templates that normalize to one** and the first where one colliding group is nested inside another: `/v1alpha1/{parent}/v2/service_instances/{instanceId}` beside `…/{instance_id}`, and one segment deeper `…/{instanceId}/service_bindings/{bindingId}` beside `…/{instanceId}/service_bindings/{binding_id}` — four keys in two groups that crozier's own `naming::field_name` folds to two, where the deeper pair agrees on the `{instanceId}` spelling it inherits and collides only on its own leaf. The collisions are inside one document, so the golden's own raw clients say what Fern did with them. Over 13 paths, 21 component schemas, 11 component parameters and two `oauth2` schemes |
| 136 | `audiobookshelf` | github-raw | https://raw.githubusercontent.com/advplyr/audiobookshelf/0a797ab8bee15dc3ca92d1d76155259c46dbec62/docs/openapi.json | `0a797ab8bee15dc3ca92d1d76155259c46dbec62` | GPL-3.0 (the repository's own `LICENSE`; the document declares no `info.license`) | committed | The API the Audiobookshelf self-hosted audiobook server publishes for itself, the fourth registered declarer of a **media type range** other than `*/*` — three `200` responses keyed on `image/*` over `{type: string, format: binary}`, one each for the `GET`, `POST` and `PATCH` of `/api/authors/{id}/image` — and the only registered source declaring a range **beside two concrete media types of its own type**: that `GET`'s response content map is `image/webp`, `image/jpeg` and `image/*`, all three over the same binary schema, so this golden pins which of an overlapping set Fern picks. Over 31 paths, 91 component schemas and a `bearerAuth` `http` scheme |
| 137 | `steaminputdb` | github-raw | https://raw.githubusercontent.com/Alia5/steaminputdb.com/a2bd0c37fd3d22e6b9e153b49e9a6e7de5a00393/openapi.yaml | `a2bd0c37fd3d22e6b9e153b49e9a6e7de5a00393` | AGPL-3.0 (declared by the document's `info.license`, `GNU Affero General Public License v3.0`, and by the repository's own `LICENSE.txt`) | committed | The API the SteamInputDB controller-configuration site publishes for itself, the corpus's only source whose sole Security Scheme Object mixes three vocabularies at once: `type: oauth2` carrying `flows.implicit` beside a stray `scheme: OAuth`, an `in: query`, a `name: Steam Auth` and an `openIdConnectUrl`. It is the corpus's **only** declarer of `securityScheme.scheme=OAuth` and its only **golden-bearing** declarer of `securityScheme.in=query` — the other three are DROPPED rows — and Fern reads neither key, importing the scheme as an optional bearer `token` on a document that declares no `security` requirement anywhere, which is what this golden says crozier must do too. Its `implicit` flow writes `scopes: null` where the specification makes the map required, and is the corpus's only `securityScheme.flows.implicit.tokenUrl`, a field an implicit flow has no use for. Its two colliding method names come from a shared **`summary`** rather than a shared `operationId` — four other registered sources collide that way too (`color.pizza`, `openbanking-brasil-directory`, `portfoliooptimizer.io`, `reverb.com`), and this is the one where the two colliding operations are the `GET` and `POST` of a single path and both carry a request body: `/v1/steam/login` declares no `operationId` anywhere in the document and both operations read `Log in with Steam`, so one `log_in_with_steam` survives — and the `OpenIDBody` both of their bodies `$ref` is inlined into it and dropped from the type layer, where a schema two *surviving* endpoints shared would have been kept. Four of its request schemas carry a `readOnly: true` `$schema` property Fern drops from every method it inlines them into, and its one multi-line operation description indents its second line with three tabs, which its `reference.md` entry keeps and its `client.py` docstring does not. Over 8 paths, 72 component schemas and an `openapi: 3.1.0` document's 96 `type: null` union members |
| 138 | `paypal-catalog-products` | github-raw | https://raw.githubusercontent.com/paypal/paypal-rest-api-specifications/90e8041ffe02d80c452d2b476bedd59a8d219bdc/openapi/catalogs_products_v1.json | `90e8041ffe02d80c452d2b476bedd59a8d219bdc` | Apache-2.0 (the publisher repository's pinned `LICENSE`) | committed | PayPal Catalog Products API; four sole-member `anyOf` wrappers on error detail items. |
| 139 | `folio-mod-authtoken` | github-raw | https://raw.githubusercontent.com/folio-org/mod-authtoken/172586c71fe936ac0b4d104b95acd508e88e43d3/src/main/resources/openapi/token-1.0.yaml | `172586c71fe936ac0b4d104b95acd508e88e43d3` | Apache-2.0 (the publisher repository’s pinned `LICENSE`) | committed | FOLIO mod-authtoken’s six endpoint API; `components.schemas.refreshToken` names `schemas/refreshToken.json` under the same revision, while `tokenResponse` and four other component aliases name sibling JSON files. Fern’s generated `src/fern/types/refresh_token.py` and the token client methods derive from those references. |
| 140 | `raybot` | github-raw | https://raw.githubusercontent.com/tbe-team/raybot/4428dea2f79b833aead4c89df5bd8d9e32b7b0c8/api/openapi/openapi.yml | `4428dea2f79b833aead4c89df5bd8d9e32b7b0c8` | MIT (publisher repository’s pinned `LICENSE` and the document’s `info.license`) | committed | Raybot’s published robot-control API references 23 sibling Path Item files; `/version` names `paths/version.yml`, whose `get` operation generates `src/fern/version/client.py`, and `/health` names `paths/health.yml`, generating `src/fern/health/client.py`. Each Path Item then references pinned parameter and schema files under the same revision. |
| 144 | `paloalto-cspm-alerts` | github-raw | https://raw.githubusercontent.com/PaloAltoNetworks/pan.dev/4e989cdd4bbda669dc73c0d3f5db90bb4989bee3/openapi-specs/cspm/Alerts.json | `4e989cdd4bbda669dc73c0d3f5db90bb4989bee3` | MIT (the publisher repository's own `LICENSE`; the document declares no `info.license`) | committed | Prisma Cloud Alerts API (Palo Alto Networks, publisher-owned `pan.dev`); annotated `$ref`s to composed and `oneOf` targets |
| 145 | `paloalto-cspm-reports` | github-raw | https://raw.githubusercontent.com/PaloAltoNetworks/pan.dev/4e989cdd4bbda669dc73c0d3f5db90bb4989bee3/openapi-specs/cspm/Reports.json | `4e989cdd4bbda669dc73c0d3f5db90bb4989bee3` | MIT (the publisher repository's own `LICENSE`; the document declares no `info.license`) | committed | Prisma Cloud Reports API; annotated `$ref`s to `oneOf` targets |
| 146 | `paloalto-cspm-search-manager` | github-raw | https://raw.githubusercontent.com/PaloAltoNetworks/pan.dev/4e989cdd4bbda669dc73c0d3f5db90bb4989bee3/openapi-specs/cspm/SearchManager.json | `4e989cdd4bbda669dc73c0d3f5db90bb4989bee3` | MIT (the publisher repository's own `LICENSE`; the document declares no `info.license`) | committed | Prisma Cloud Search Manager API; annotated `$ref`s to `oneOf` targets |
| 147 | `thrivecart` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/thrivecart.com/main/1.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | ThriveCart API; `$ref` pointers under an undeclared component head |
| 148 | `truefoundry-trueforge-5adde28` | github-raw | https://raw.githubusercontent.com/truefoundry/trueforge/5adde289683b642203b06b39ca687e9d977ca7a5/docs/openapi.json | `5adde289683b642203b06b39ca687e9d977ca7a5` | MIT (the publisher repository's own `LICENSE`; the document declares no `info.license`) | committed | TrueForge API at a later revision than row 108; annotated `$ref`s to closed-object targets |
| 149 | `fergus` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/fergus.com/fergus-api/v1/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | Fergus API; `anyOf` array variants with struct items |
| 150 | `groupe-psa` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/groupe-psa.io/main/3.19.2/meta/import/input-entry.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document's own `info.license` names `Groupe PSA Licence`) | committed | Groupe PSA Connected Car B2B API; annotated `$ref`s to composed targets |
| 151 | `timelyapp` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/timelyapp.com/main/V1/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document's own `info.license` names `Timely`) | committed | Timely API; `anyOf` array variants with struct items |
| 152 | `nextgen` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/nextgen.com/main/1.0/meta/import/input-entry.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | NextGen Enterprise API USCDI Routes; `$ref` pointers under an undeclared component head, non-identifier component schema names |
| 153 | `auto-agent-protocol` | github-raw | https://raw.githubusercontent.com/auto-agent-protocol/auto-agent-protocol/5d31c27b11c36a018754f34830954d836a55afe5/releases/v1.0/artifacts/openapi-rest.yaml | `5d31c27b11c36a018754f34830954d836a55afe5` | Apache-2.0 (declared by the document's `info.license`) | committed | Auto Agent Protocol A2A HTTP+JSON binding; a `$ref` pointer through an unnamed segment |
| 154 | `skool` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/skool.com/main/1.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | Skool API; `$ref` pointers under an undeclared component head |
| 155 | `spendesk` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/spendesk.com/main/1.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | Spendesk API; `$ref` pointers under an undeclared component head |
| 156 | `billie` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/billie.io/main/2.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | Billie Direct API; `$ref` pointers under an undeclared component head |
| 157 | `alma-france` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/alma_france_api/main/1.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | Alma Payments API; `$ref` pointers under an undeclared component head |
| 158 | `outreach` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/outreach.io/main/2.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | Outreach API; `$ref` pointers under an undeclared component head |
| 159 | `tally` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/tally.so/main/1.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document's own `info.license` names `MIT`) | committed | Tally API; `$ref` pointers under an undeclared component head |
| 160 | `billie-entry` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/billie.io/main/2.0.0/meta/import/input-entry.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | Billie Direct API, jentic's import entry: row 156's document with its object keys in another order |
| 161 | `skool-entry` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/skool.com/main/1.0.0/meta/import/input-entry.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | Skool API, jentic's import entry: row 154's document with its object keys in another order |
| 162 | `timelyapp-entry` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/timelyapp.com/main/V1/meta/import/input-entry.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | Timely API, jentic's import entry: row 151's document with its object keys in another order |
| 163 | `cradl` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/cradl.ai/main/2026-01-28T09%3A00%3A46Z/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document declares no `info.license`) | committed | Cradl API; `anyOf` array variants with struct and closed-object items |
| 164 | `zulip` | github-raw | https://raw.githubusercontent.com/zulip/zulip/6a82f40579f8adb9149aa0b04ff795c397baae73/zerver/openapi/zulip.yaml | `6a82f40579f8adb9149aa0b04ff795c397baae73` | Apache-2.0 (declared by the document's `info.license` and by the repository's own `LICENSE`) | committed | Zulip REST API; annotated `$ref`s to closed-object and `oneOf` targets, `oneOf` array variants with closed-object items |
| 165 | `zulip-jentic` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/zulip.com/zulip/1.0.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document's own `info.license` names `Apache 2.0`) | committed | Zulip REST API, the jentic-public-apis aggregation's JSON import of `https://zulip.com/api/rest`: a different revision of row 164's document, re-serialized |
| 166 | `zulip-jentic-entry` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/zulip.com/zulip/1.0.0/meta/import/input-entry.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE.md`; the document's own `info.license` names `Apache 2.0`) | committed | Zulip REST API, jentic's import entry: row 165's document with its object keys in another order |
| 167 | `viskit-studio` | github-raw | https://raw.githubusercontent.com/MyuriKanao/viskit-studio/58b149008088c837332b57353c0f6e1fe19bbe8d/packages/schemas/openapi.yaml | `58b149008088c837332b57353c0f6e1fe19bbe8d` | MIT (the repository's own `LICENSE`; the document declares no `info.license`) | committed | VisKit Studio API; the publisher's own description, declaring `anyof-array-variant-anyof-nullable-item` |
| 168 | `milvus-restful-v2-3` | github-raw | https://raw.githubusercontent.com/milvus-io/web-content/d3c35ec9b46dcc2befd205a87a785896d99ce332/API_Reference/milvus-restful/v2.3.x/Restful%20API%20v2.openapi.json | `d3c35ec9b46dcc2befd205a87a785896d99ce332` | Apache-2.0 (the repository's own `LICENSE`; the document declares no `info.license`) | committed | Milvus RESTful API v2 (the v2.3.x reference); the publisher's own description, declaring `anyof-array-variant-empty-object-item` |
| 169 | `milvus-restful-v2-4` | github-raw | https://raw.githubusercontent.com/milvus-io/web-content/d3c35ec9b46dcc2befd205a87a785896d99ce332/API_Reference/milvus-restful/v2.4.x/openapi.json | `d3c35ec9b46dcc2befd205a87a785896d99ce332` | Apache-2.0 (the repository's own `LICENSE`; the document declares no `info.license`) | committed | Milvus RESTful API (the v2.4.x reference); the publisher's own description, declaring `anyof-array-variant-empty-object-item` |
| 170 | `ramu-shogi` | github-raw | https://raw.githubusercontent.com/SH11235/ramu-shogi/22504221b837d01c9366a5d6c8c6a9b88f9f782b/packages/api-contract/src/generated/openapi.json | `22504221b837d01c9366a5d6c8c6a9b88f9f782b` | GPL-3.0 (the repository's own `LICENSE`; the document declares no `info.license`) | committed | Ramu Shogi API contract; the publisher's own description, declaring `anyof-array-variant-oneof-nullable-item` |
| 171 | `embedpdf-cloudpdf` | github-raw | https://raw.githubusercontent.com/embedpdf/embed-pdf-viewer/2516e2786ee894383220ecd436fbd248182ef444/cloudpdf/contract/openapi.json | `2516e2786ee894383220ecd436fbd248182ef444` | Apache-2.0 (declared by the document's `info.license`; the repository's licence reads NOASSERTION) | committed | CloudPDF contract API; the publisher's own description, declaring `array-item-pointer-walk-anyof` |
| 172 | `langchain-agent-protocol` | github-raw | https://raw.githubusercontent.com/langchain-ai/agent-protocol/fb81f3e27ee507557926ecf923d0f933a1c76d44/openapi.json | `fb81f3e27ee507557926ecf923d0f933a1c76d44` | MIT (the repository's own `LICENSE`; the document declares no `info.license`) | committed | LangChain Agent Protocol; the publisher's own description, declaring `oneof-array-variant-anyof-item` |
| 173 | `hse` | github-raw | https://raw.githubusercontent.com/hse-project/hse/6d5207f88044a3bd9b3539260074395317e276d5/docs/openapi.json | `6d5207f88044a3bd9b3539260074395317e276d5` | Apache-2.0 (declared by the document's `info.license`; the repository carries no licence file GitHub recognises) | committed | HSE REST API; the publisher's own description, declaring `oneof-array-variant-composed-item` |
| 174 | `milvus-vector-operations` | github-raw | https://raw.githubusercontent.com/milvus-io/web-content/d3c35ec9b46dcc2befd205a87a785896d99ce332/scripts/apifox-docs/meta/openapi/03-vector-operations.json | `d3c35ec9b46dcc2befd205a87a785896d99ce332` | Apache-2.0 (the repository's own `LICENSE`; the document declares no `info.license`) | committed | Milvus vector operations (apifox export); the publisher's own description, declaring `oneof-array-variant-empty-object-item` |
| 175 | `npq-registration` | github-raw | https://raw.githubusercontent.com/DFE-Digital/npq-registration/17f95361371e9bb8c3f1e41c90f5e78bda069ce5/public/api/docs/v3/swagger.yaml | `17f95361371e9bb8c3f1e41c90f5e78bda069ce5` | MIT (the repository's own `LICENSE`; the document declares no `info.license`) | committed | NPQ registration API v3; the publisher's own description, declaring `property-sole-anyof-closed-object-member`, `property-sole-anyof-struct-member` |
| 176 | `mistle-control-plane` | github-raw | https://raw.githubusercontent.com/mistlehq/mistle/2b11ccefc658c5b707310d3cc471d5c5928554f3/apps/control-plane-api/openapi/control-plane.internal.v1.json | `2b11ccefc658c5b707310d3cc471d5c5928554f3` | MIT (the repository's own `LICENSE`; the document declares no `info.license`) | committed | Mistle control-plane internal API v1; the publisher's own description, declaring `property-sole-oneof-closed-object-member` |
| 177 | `osparc-payments` | github-raw | https://raw.githubusercontent.com/ITISFoundation/osparc-simcore/69b034b82f243b30953d025793c0f171fdb3c92e/services/payments/openapi.json | `69b034b82f243b30953d025793c0f171fdb3c92e` | MIT (the repository's own `LICENSE`; the document declares no `info.license`) | committed | o²S²PARC payments service; the publisher's own description, declaring `oauth2-password` |
| 178 | `huatuo-node` | github-raw | https://raw.githubusercontent.com/ccfos/huatuo/36175d6e91fdc7b79e818496e1587eb0ca79a18d/apis/v1/node/openapi.gen.json | `36175d6e91fdc7b79e818496e1587eb0ca79a18d` | Apache-2.0 (the repository's own `LICENSE`; the document declares no `info.license`) | committed | HuaTuo node API v1; the publisher's own description, declaring `securityscheme-ref` |
| 179 | `huatuo-server` | github-raw | https://raw.githubusercontent.com/ccfos/huatuo/36175d6e91fdc7b79e818496e1587eb0ca79a18d/apis/v1/server/openapi.gen.json | `36175d6e91fdc7b79e818496e1587eb0ca79a18d` | Apache-2.0 (the repository's own `LICENSE`; the document declares no `info.license`) | committed | HuaTuo server API v1; the publisher's own description, declaring `securityscheme-ref` |
| 191 | `openlinksw-osdb` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/openlinksw.com/osdb/1.0.0/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | CC-BY-SA 3.0 (declared by the document's `info.license`, inside the CC0-1.0 `APIs-guru/openapi-directory` aggregation) | committed | OpenLink OSDB REST API v1; string schemas declaring `format: uri-template` |
| 192 | `ziptax-node` | github-raw | https://raw.githubusercontent.com/ZipTax/ziptax-node/ac6cc26208ad2bdd594886ea323e4b0a5ffd8da0/docs/openapi.json | `ac6cc26208ad2bdd594886ea323e4b0a5ffd8da0` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | ZipTax's sales-tax API as its Node SDK repository publishes it; its 34 operations are labelled `x-fern-audiences` by API version (`v10`-`v60`) and generated for `v60`, which keeps 27 and filters out 7 |
| 193 | `nexmo-messages` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/nexmo.com/messages-olympus/1.4.0/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | CC0-1.0 (the `APIs-guru/openapi-directory` aggregation's own `LICENSE`; the document declares no `info.license`, and its publisher repository `nexmo/api-specification` no longer exists) | committed | The Vonage (Nexmo) Messages API 1.4.0; operation-level unions whose members compose with `allOf` |
| 194 | `deepsearch-ds-v2` | github-raw | https://raw.githubusercontent.com/DS4SD/deepsearch-toolkit/be22375ecea319b495a11e27cd0308fdcda81ba1/tools/swagger-client-generator/openapi-ds-v2.json | `be22375ecea319b495a11e27cd0308fdcda81ba1` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | IBM Deep Search (DS) API 3.0.0 as the DS4SD toolkit pins it; properties whose `anyOf` is a discriminated union |
| 195 | `mindee-ocr` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/mindee.com/main/0.1.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`) | committed | The Mindee OCR API as its publisher serves it (`info.x-jentic-source-url` is `https://api.mindee.net/openapi.json`); array items declaring `oneOf` |
| 196 | `opencodeui` | github-raw | https://raw.githubusercontent.com/lehhair/OpenCodeUI/8a6d4eae9424317f01e88f3819b14b24e57bab10/openapi_doc.json | `8a6d4eae9424317f01e88f3819b14b24e57bab10` | GPL-3.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The opencode server API as the OpenCodeUI web client pins it (a different document from the DROPPED `opencode` row); array items whose `anyOf` is one inline object |
| 216 | `sim-logs` | github-raw | https://raw.githubusercontent.com/simstudioai/sim/0e477d760ca6e7eb6f347cf876191e01d6ca00d7/apps/docs/openapi-v2-logs.json | `0e477d760ca6e7eb6f347cf876191e01d6ca00d7` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document's `info.license` is Apache 2.0) | committed | Sim API v2 — Logs; the publisher's own description, declaring `anyof-array-variant-closed-object-item` |
| 217 | `sim-tables` | github-raw | https://raw.githubusercontent.com/simstudioai/sim/0e477d760ca6e7eb6f347cf876191e01d6ca00d7/apps/docs/openapi-v2-tables.json | `0e477d760ca6e7eb6f347cf876191e01d6ca00d7` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document's `info.license` is Apache 2.0) | committed | Sim Tables API v2; the publisher's own description, declaring `anyof-array-variant-closed-object-item` |
| 218 | `vellum-gateway` | github-raw | https://raw.githubusercontent.com/vellum-ai/vellum-assistant/74e3c467f7cb65736e0c59bda3bcce152de35783/gateway/openapi.json | `74e3c467f7cb65736e0c59bda3bcce152de35783` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | Vellum Gateway API 0.11.8; the publisher's own description, declaring `anyof-array-variant-closed-object-item` |
| 219 | `dot-ai` | github-raw | https://raw.githubusercontent.com/vfarcic/dot-ai/056941fc025b64fd9771d79333706eca513566df/schema/openapi.json | `056941fc025b64fd9771d79333706eca513566df` | MIT (the publisher repository's pinned `LICENSE`; the document's `info.license` is MIT) | committed | DevOps AI Toolkit REST API 2.3.1; the publisher's own description, declaring `anyof-array-variant-closed-object-item` |
| 220 | `paloalto-code-technologies` | github-raw | https://raw.githubusercontent.com/PaloAltoNetworks/pan.dev/4e989cdd4bbda669dc73c0d3f5db90bb4989bee3/openapi-specs/code/Technologies.json | `4e989cdd4bbda669dc73c0d3f5db90bb4989bee3` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | Prisma Cloud Technologies API; the publisher's own description, declaring `anyof-array-variant-struct-item` |
| 221 | `marimo-plugins` | github-raw | https://raw.githubusercontent.com/marimo-team/marimo/433386f4573e4ad77a22439db68276e6196d3307/frontend/plugins.openapi.yaml | `433386f4573e4ad77a22439db68276e6196d3307` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | marimo plugin contracts 1.0.0; the publisher's own description, declaring `anyof-array-variant-struct-item` |
| 222 | `otoroshi` | github-raw | https://raw.githubusercontent.com/MAIF/otoroshi/e912f12c40eaf6de0cdda2e8c43db5cf226a301d/otoroshi/conf/schemas/openapi.json | `e912f12c40eaf6de0cdda2e8c43db5cf226a301d` | Apache-2.0 (the publisher repository's pinned `LICENCE`; the document's `info.license` is Apache 2.0) | committed | Otoroshi Admin API 16.12.0-dev as its repository pins it (a different document from row 59's APIs.guru 1.5.0-dev); declaring `ref-pointer-undeclared-component-head` |
| 225 | `googleapis-monitoring-v1` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/googleapis.com/monitoring/v1/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | Creative Commons Attribution 3.0 (the document's own `info.license`, Google's grant over its own description; the aggregating repository is CC0-1.0) | committed | Google Cloud Monitoring API v1 (dashboards); enum members with leading zeros |
| 226 | `docu-goapiserver` | github-raw | https://raw.githubusercontent.com/JuaniGit/docu-goapiserver/45632ead37e9915e251896ae62e378ba738f0529/openapi.yaml | `45632ead37e9915e251896ae62e378ba738f0529` | MIT (the repository's `LICENSE` at the pinned commit; the document declares no `info.license`) | committed | Primula Tracker API V3 (OpenAPI 3.1); an `anyOf` variant that is itself an `anyOf` |
| 227 | `onevoice` | github-raw | https://raw.githubusercontent.com/f1xgun/onevoice/5dab014aaf878650bbf19aea528f72a0fe265e35/docs/api/spec/openapi.yaml | `5dab014aaf878650bbf19aea528f72a0fe265e35` | MIT (the repository's `LICENSE` at the pinned commit; the document declares no `info.license`) | committed | OneVoice API 1.0.0; a `mutualTLS` security scheme beside a supported one |
| 228 | `xfsc-oidc-identity-resolver` | github-raw | https://raw.githubusercontent.com/eclipse-xfsc/notarization-service/4851a2be805d16c866ce04da7998ddc5056dc1a1/services/oidc-identity-resolver/deploy/openapi/openapi.yaml | `4851a2be805d16c866ce04da7998ddc5056dc1a1` | Apache-2.0 (the repository's `LICENSE` at the pinned commit; the document declares no `info.license`) | committed | Eclipse XFSC notarization service's OIDC identity resolver API; `openIdConnect` security schemes only |
| 229 | `adyen-acs-notification` | github-raw | https://raw.githubusercontent.com/Adyen/adyen-openapi/f82d1fe674e536cc2c6b0d7946e0e827873a4fbf/json/BalancePlatformAcsNotification-v1.json | `f82d1fe674e536cc2c6b0d7946e0e827873a4fbf` | MIT (the repository's `LICENSE` at the pinned commit, recorded in `witness-search-vendor-portals/publisher-grants.tsv`; the document declares no `info.license`) | committed | Adyen Authentication webhooks v1 (OpenAPI 3.1); enum members whose names lead with a digit |
| 230 | `peopledatalabs` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/peopledatalabs.com/main/5.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC0-1.0 (the aggregating repository's own `LICENSE`; the document declares no `info.license`) | committed | People Data Labs API 5.0; an enum value led by a number past Fern's number-to-words range (`10001+`) |
| 231 | `standrig` | github-raw | https://raw.githubusercontent.com/sayaka-aiart/StandRig/33e15309c44f8122a88e01ed7e71efc9989cb652/docs/openapi.json | `33e15309c44f8122a88e01ed7e71efc9989cb652` | Apache-2.0 (the repository's `LICENSE` at the pinned commit; the document declares no `info.license`) | committed | StandRig Modeling Tools core API 0.2.0 (OpenAPI 3.1); an `anyOf` alternative that is a string `const` |
| 232 | `mockserver` | github-raw | https://raw.githubusercontent.com/mock-server/mockserver-monorepo/ff83158d204c5eb7ab5fabc8ba74ffd3a76f5037/jekyll-www.mock-server.com/mockserver-openapi.yaml | `ff83158d204c5eb7ab5fabc8ba74ffd3a76f5037` | Apache-2.0 (the repository's `LICENSE.md` at the pinned commit; the document's `info.license` is Apache 2.0) | committed | MockServer's own control-plane API description; its draft-04 meta-schema `$ref` is pinned in `corpus-remote-ref-pins.tsv` |
| 301 | `ideaconsult-enanomapper` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/ideaconsult.net/enanomapper/4.0.0/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | LGPL (the document's own `info.license`, `API available under GNU Lesser General Public License`, inside the CC0-1.0 `APIs-guru/openapi-directory` aggregation) | committed | The eNanoMapper database API 4.0.0 as Ideaconsult publishes it; operations declaring `externalDocs` |
| 302 | `openaire-graph` | github-raw | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/graph.openaire.eu/main/2.0/openapi.json | `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` | CC-BY (the document's own `info.license` names https://graph.openaire.eu/docs/license, which grants re-use under CC-BY; the aggregating repository is CC0-1.0) | committed | The OpenAIRE Graph API 2.0 as its publisher serves it (`info.x-jentic-source-url` is `https://graph.openaire.eu/docs/apis/home/`); schemas declaring `xml.attribute` |
| 303 | `qredence-fleet-rlm` | github-raw | https://raw.githubusercontent.com/Qredence/fleet-rlm/0322623598b6cda0eea580694264e69a40081f10/openapi.yaml | `0322623598b6cda0eea580694264e69a40081f10` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | fleet-rlm 0.7.10 (OpenAPI 3.1), Qredence's own server description; a `oneOf` variant that is itself an `anyOf` |
| 304 | `fiware-context-generator` | github-raw | https://raw.githubusercontent.com/live-buildings/context-generator/354bf6920d20955aabb55f4778a4d8a3d855440b/swaggers/swagger.yaml | `354bf6920d20955aabb55f4778a4d8a3d855440b` | MIT (the publisher repository's pinned `LICENSE`, FIWARE Foundation; the document declares no `info.license`) | committed | The LiveBuildings data model API 0.0.1, the context generator's own description; an array item's `oneOf` member that is an `anyOf` |
| 305 | `hasura-metadata` | github-raw | https://raw.githubusercontent.com/hasura/graphql-engine/94915fe51d6d21bd7f6d4452dc16221bef8cfefd/metadata.openapi.json | `94915fe51d6d21bd7f6d4452dc16221bef8cfefd` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | Hasura GraphQL Engine's metadata schema as its repository publishes it: 334 component schemas and no paths; properties whose `oneOf` holds an `anyOf` |
| 306 | `zoonk` | github-raw | https://raw.githubusercontent.com/zoonk/zoonk/4546e69762e30f245c9306acb95aa56fc69d2682/apps/apple/Zoonk/openapi.json | `4546e69762e30f245c9306acb95aa56fc69d2682` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | Zoonk's API as its repository publishes it for the Apple client: 48 paths and 69 component schemas; `MeDeletion`'s `oneOf` offers a closed empty object |
| 307 | `apideck.com-ecosystem-client-class-name` | api-guru | https://api.apis.guru/v2/specs/apideck.com/ecosystem/0.0.6/openapi.json | `0.0.6` | Apache 2.0 | committed | Row 13's Ecosystem API regenerated with `client_class_name: EcosystemClient`, the class name of its own `Ecosystem` resource's sub-client |
| 308 | `yourbrand-ticketing` | github-raw | https://raw.githubusercontent.com/marinasundstrom/YourBrand/6ef617804cb34ceba4b847c62ab122042d86abbe/src/CustomerRelations/Ticketing/Ticketing.Client/OpenAPIs/swagger.yaml | `6ef617804cb34ceba4b847c62ab122042d86abbe` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | YourBrand's Ticketing service API as its repository publishes it for the Ticketing client: 32 paths and 64 component schemas; two `application/json` bodies are bare `{type: string, format: duration}` strings |
| 309 | `huatuo-node-tree` | github-raw | https://raw.githubusercontent.com/ccfos/huatuo/36175d6e91fdc7b79e818496e1587eb0ca79a18d/apis/v1/node/openapi.yaml | `36175d6e91fdc7b79e818496e1587eb0ca79a18d` | Apache-2.0 (the repository's own `LICENSE`; the document declares no `info.license`) | committed | HuaTuo node API v1 as its repository authors it, the source `openapi.gen.json` (row 178) is bundled from: `components.securitySchemes.BearerAuth` is `$ref: '../components.yaml#/components/securitySchemes/BearerAuth'`, a security scheme declared in another document of the same pinned tree, and thirteen schema references name `../components.yaml#/components/schemas/…`. Fern's generated bearer `token` and `Authorization` header, and its `ErrorResponse`, `Error`, `ErrorCode` and `ObservationScope` types, derive from those references. |
| 310 | `openfoodfacts-taxonomy-editor` | github-raw | https://raw.githubusercontent.com/openfoodfacts/taxonomy-editor/dc63220b1f9e9b7837dcb7d71a1964546d2e6ed3/backend/openapi/openapi.json | `dc63220b1f9e9b7837dcb7d71a1964546d2e6ed3` | AGPL-3.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The Open Food Facts taxonomy editor's API as its FastAPI backend publishes it: 25 paths and 16 component schemas; `EntryNodeSearchResult.filters` items are a `filterType`-discriminated `oneOf` of seven `$ref` members whose `readOnly` properties `required` also lists |
| 311 | `qontract-api` | github-raw | https://raw.githubusercontent.com/app-sre/qontract-reconcile/4f643a29084cb9b9e8c90e878e03bbe6ac80a5db/qontract_api/openapi.json | `4f643a29084cb9b9e8c90e878e03bbe6ac80a5db` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The Qontract API as qontract-reconcile's FastAPI service publishes it: 34 paths and 145 component schemas; the Quay-repository and Slack-usergroup task results' `actions` items are `$ref`-only unions whose members tag `action_type` with a one-value `enum` that `required` leaves out |
| 312 | `oal-example` | github-raw | https://raw.githubusercontent.com/oxlip-lang/oal/9c76fd5fd74c1f64c62a219aa2156b021a820f4a/examples/openapi.yaml | `9c76fd5fd74c1f64c62a219aa2156b021a820f4a` | Apache-2.0 (`info.license`, and the publisher repository's pinned `LICENSE.txt`) | committed | The example description the OAL project compiles from its own API language and publishes: 4 paths and 6 component schemas; `obj3.stuff` is an `anyOf` whose first member is an inline `oneOf` beside an inline object |
| 313 | `breizhsport-catalogue` | github-raw | https://raw.githubusercontent.com/ImNotAOwl/e-commerce_microservices_CATALOGUE_API/460aed0c7e313e2289330e76bb6607f4eef9c4f3/openapi.yaml | `460aed0c7e313e2289330e76bb6607f4eef9c4f3` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The BreizhSport Catalogue API its own repository publishes: 3 paths and 3 component schemas; `Article.rating` is declared `type: float` beside `price` and `quantity` declared `type: int` |
| 314 | `protoform-conformance` | github-raw | https://raw.githubusercontent.com/malinskibeniamin/protoform/a179fc14356cc98dce69402ae62c406107b0bf5b/openapi.yaml | `a179fc14356cc98dce69402ae62c406107b0bf5b` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The Protoform bookstore Connect API its own repository publishes: five unary Book RPCs; `DeleteBook`'s success response is an inline object closed with `additionalProperties: false` that declares no `properties` |
| 315 | `ere-ps-app` | github-raw | https://raw.githubusercontent.com/ere-health/ere-ps-app/9d8958380a7bdf3fc2e94bd6747cf59bb6d96de5/openapi/openapi.json | `9d8958380a7bdf3fc2e94bd6747cf59bb6d96de5` | GPL-3.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The `ere-ps-app` API its own repository publishes: 25 paths and 121 component schemas, 48 of whose models reach two or more reference cycles in an order no sort of their members reproduces |
| 316 | `typescript-service-template` | github-raw | https://raw.githubusercontent.com/adiwajshing/typescript-service-template/bec0143414f9ec292e4a33dd3ee1c576984559d6/openapi.yaml | `bec0143414f9ec292e4a33dd3ee1c576984559d6` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The description a TypeScript service template publishes for its users API: one path, three operations and five component schemas; `usersPatch` takes a required query array of `$ref UserID` items and answers `application/json` |
| 317 | `lootlog-battlelog` | github-raw | https://raw.githubusercontent.com/lootlog/monorepo/e2796c4f48ca4a749f53fdc5a127eece50567b56/apps/battlelog/openapi.yaml | `e2796c4f48ca4a749f53fdc5a127eece50567b56` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | Lootlog's Battle Log API as its repository publishes it: OpenAPI 3.0.0, one `http: bearer` scheme, and `POST /internal/delete-user-data` declares an optional header parameter spelled `authorization` in lower case |
| 318 | `ego-microservices` | github-raw | https://raw.githubusercontent.com/dreek1337/Ego/e0ebe7a5219488545820408b46f67f4f9fa9c83c/openapi.yaml | `e0ebe7a5219488545820408b46f67f4f9fa9c83c` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | Ego's microservices API as its repository publishes it: OpenAPI 3.1.0, 20 paths and 60 component schemas; the paginated listings' query `offset` and `limit` are `anyOf: [integer, $ref Empty]`, where `Empty` is a component string enum |
| 319 | `millenium-falcon-challenge` | github-raw | https://raw.githubusercontent.com/jondavies00/millenium-falcon-challenge/508e939a0ae568f13c10f872580d7c9605e29a97/openapi.json | `508e939a0ae568f13c10f872580d7c9605e29a97` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The Millennium Falcon challenge's odds API as its FastAPI app publishes it: 1 path and 6 component schemas; `POST /odds` posts a `Body_odds_odds_post` JSON body nothing else references |
| 320 | `maximo-wxo-integration` | github-raw | https://raw.githubusercontent.com/IBM/maximo-wxo-integration/54a2c3879173a44c8ed6d321d09066c9975de488/openapi.json | `54a2c3879173a44c8ed6d321d09066c9975de488` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | IBM's Maximo integration API as its FastAPI wrapper publishes it, at OpenAPI 3.0.0: 9 paths and no component schemas; five success responses are an inline `application/json` declaring the empty schema `{}` |
| 321 | `mi-music` | github-raw | https://raw.githubusercontent.com/jokezc/mi_music/2a114dff3bb9528a3e772ef7de0f850fe488ff27/docs/openapi.json | `2a114dff3bb9528a3e772ef7de0f850fe488ff27` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | mi_music's API as its FastAPI service publishes it: 42 paths and 30 component schemas; `GET /downloadlog` answers a schemaless `text/plain`, `GET /music/{file_path}` and `GET /proxy` a schemaless `audio/mpeg` (the latter beside `video/mp4`), and 37 operations ride HTTP Basic security with titled `$ref` bodies |
| 322 | `g4brym-download-manager` | github-raw | https://raw.githubusercontent.com/G4brym/download-manager/459a6d8ef8dbee4289b7b5b629e1377e623c2b4e/swagger/openapi.json | `459a6d8ef8dbee4289b7b5b629e1377e623c2b4e` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | download-manager's API as its FastAPI service publishes it, at OpenAPI 3.0.2: 6 paths and 7 component schemas; two parameterless operations post an inline array titled `Files`, one of `$ref` items and one of strings |
| 323 | `opentosca-license-engine` | github-raw | https://raw.githubusercontent.com/OpenTOSCA/license-engine/ebf2f4a2a750feb31d3e6eff8fdd22dab4c00d65/src/main/resources/openapi/openapi.json | `ebf2f4a2a750feb31d3e6eff8fdd22dab4c00d65` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The OpenTOSCA license engine's API as its repository publishes it, at OpenAPI 3.0.2: 14 paths and 10 component schemas; `POST /licenses/check/` posts an inline string array titled `Usedlicenses` with no parameter, and twelve success responses are an inline `application/json` declaring `{}` |
| 324 | `chat-rest-api` | github-raw | https://raw.githubusercontent.com/Ke11nyk/chat-rest-api/e761a7bf0d32147aff6571b9f9d325abd010e545/docs/openapi.yaml | `e761a7bf0d32147aff6571b9f9d325abd010e545` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | chat-rest-api's API as its repository publishes it, at OpenAPI 3.0.0: 5 paths and 1 component schema; `GET /message/content/{id}` declares the error keys `404-message` and `404-file`, and its success lists a schemaless `text/plain` before a schemaless `application/octet-stream` |
| 325 | `esp32-streamline-bridge` | github-raw | https://raw.githubusercontent.com/lutyjj/esp32-streamline/f50f678a3569d5c10e250cdd03e16cf1d17df16a/docs/bridge-openapi.json | `f50f678a3569d5c10e250cdd03e16cf1d17df16a` | GPL-3.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The StreamLine bridge API as esp32-streamline publishes it: 13 paths and 25 component schemas; `GET /api/recordings/{recording_id}/file` and `GET /streamline.wav` answer a schemaless `audio/wav` |
| 326 | `cphos-ai-question` | github-raw | https://raw.githubusercontent.com/CPHOS/AI_Question/951028cbbcfb1ab15ee26dc02824029cb50fd1ab/docs/api/openapi.json | `951028cbbcfb1ab15ee26dc02824029cb50fd1ab` | AGPL-3.0 (`info.license` `AGPL-3.0-or-later`, and the publisher repository's pinned `LICENSE`) | committed | CPhOS's physics-question generation API as its FastAPI service publishes it: 31 paths and 45 component schemas; `GET /api/tasks/{task_id}/artifacts/{name}` answers a schemaless `application/pdf` listed before `text/markdown`, beside JSON error responses |
| 327 | `flask-example-heroku` | github-raw | https://raw.githubusercontent.com/rctatman/flask_example_heroku/2703c6ee5627d8543703a4cd9436c260fc4723c8/openapi.yaml | `2703c6ee5627d8543703a4cd9436c260fc4723c8` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | A Python package-name extractor's API as its repository publishes it, at OpenAPI 3.0.0: 1 path and no component schemas; `POST /extractpackages` declares a required request body whose `application/json` media type has no schema |
| 328 | `oip-web-api` | github-raw | https://raw.githubusercontent.com/g10101k/Oip/e3a6ecd60b1204c64907d543b37652f4230fee89/src/OipOpenApi.json | `e3a6ecd60b1204c64907d543b37652f4230fee89` | MIT (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The Oip service web API as its repository's Swashbuckle build publishes it, at OpenAPI 3.0.1: 2 paths and 2 component schemas; the parameterless `POST /api/module-federation/register-module` declares `requestBody.description: ""` over a single-use `$ref` body with optional properties |
| 329 | `waylay-queries` | github-raw | https://raw.githubusercontent.com/waylayio/waylay-sdk-queries-py/8ab6c18e10f96c3665dbb849ebe2193c16a1659c/openapi/queries.openapi.yaml | `8ab6c18e10f96c3665dbb849ebe2193c16a1659c` | ISC (the publisher repository's pinned `LICENSE.txt`; the document declares no `info.license`) | committed | Waylay's published time-series query API: `execute_query` accepts query overrides and distinct renamed JSON body arguments for the same keys; the `body-query-parameter-value` departure preserves those body values where Fern sends the query values |
| 330 | `marimo-client-class-name` | github-raw | https://raw.githubusercontent.com/marimo-team/marimo/257ea7a983e2dbe4627f0168072fdcd538c93c5c/packages/openapi/api.yaml | `257ea7a983e2dbe4627f0168072fdcd538c93c5c` | Apache-2.0 | committed | Row 95 with `client_class_name: DispatchClient`, proving configured client and raw-client names for package-root operations |
| 331 | `confluent-kafka-connect` | github-raw | https://raw.githubusercontent.com/confluentinc/ccloud-sdk-go-v2/8bbb22a67562e5784e8d3a4efa78c5c20b52d6f2/connect/v1/api/openapi.yaml | `8bbb22a67562e5784e8d3a4efa78c5c20b52d6f2` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | Confluent's Kafka Connect API: connector-plugin configuration validation posts a plain string map with a declared request example; source SHA-256 `4d183aef6bb6e0b176e334c7e2d7ebc28e9cb022c4c0ef69956de9347a596839` |
| 332 | `netgsm-sms` | github-raw | https://raw.githubusercontent.com/netgsm/netgsm-sms-js/33ca38622067e3730479aded9e56f6b1151bfeb5/openapi.json | `33ca38622067e3730479aded9e56f6b1151bfeb5` | MIT (the publisher repository's pinned `LICENSE`) | committed | NetGSM's SMS API: required query arrays beside JSON responses and JSON request-body content-type headers; source SHA-256 `9b728d109dc796d8dd166616d5be2425f4530703ef059ec0a561709421509ae3` |
| 1200 | `offchain-metadata-tools` | github-raw | https://raw.githubusercontent.com/input-output-hk/offchain-metadata-tools/91eba72d6e5e3b17cd49f625c9546f2c82df5a65/docs/api/0.5.0.0/openapi.yaml | `91eba72d6e5e3b17cd49f625c9546f2c82df5a65` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | Input Output's Cardano token metadata server API (`tokens.cardano.org`): `GET /metadata/{subject}/properties/{properties}` answers an inline `oneOf` whose only member is `$ref Property`, which Fern returns as `Property` itself |
| 1201 | `subsloth` | github-raw | https://raw.githubusercontent.com/knirski/subsloth/b4acb8e87ee47a4154f40c431b7c91d8d27d1b64/api/subsloth.openapi.yaml | `b4acb8e87ee47a4154f40c431b7c91d8d27d1b64` | Apache-2.0 (the publisher repository's pinned `LICENSE`; the document declares no `info.license`) | committed | The subsloth project's own media API contract: its component `SubtitlesValue` offers, as a `oneOf` member, an `object` map whose value is a `oneOf` of three non-null members |
| 1600 | `zylon-private-gpt` | github-raw | https://raw.githubusercontent.com/zylon-ai/private-gpt/8119842ae6f1f5ecfaf42b06fa0d1ffec675def4/fern/openapi/openapi.json | `8119842ae6f1f5ecfaf42b06fa0d1ffec675def4` | Apache-2.0 (the publisher repository's own `LICENSE`; the document declares no `info.license`) | committed | The PrivateGPT API as its publisher last declared it for Fern before the 2026 revamp: two operations whose `x-fern-streaming` names a `stream-condition` and no `format`, each answering a lone `application/json` 200 and named only by a tagged FastAPI `operationId`, so this row pins JSON-lines streaming halves and their naming against Fern |
| 1800 | `aws-mobileanalytics` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/amazonaws.com/mobileanalytics/2014-06-05/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | The document info.license grants redistribution under the policy in docs/corpus-licensing.md; the aggregator preserves publisher attribution | committed | AWS Mobile Analytics, converted from the publisher model identified in info.x-origin; the only operation declares required X-Amz-Client-Context header |

## Batch 2 — byte-matched (issue #77)

Ten corpora were selected as the next Fern byte-match targets, chosen for OpenAPI
shapes the prior corpora under-exercise. All are rows in the table above, their
sources committed under `corpus-sources/`; their goldens are workflow-managed.

**Eight are now byte-matched byte-for-byte** — wired into `crates/crozier-e2e/tests/e2e.rs` +
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

Thirteen corpora were approved for the next byte-match batch. All 13 passed
native `fern check`; their sources are committed under `corpus-sources/`.
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
| `assemblyai-autosdk` | **REJECTED** — the source license caps redistribution at a revenue ceiling this repository cannot undertake to honour, which the [licence rule](../../docs/corpus-licensing.md) refuses whatever else a licence grants |
| `sumup` | **DROPPED** — its `readOnly` and `writeOnly` fields occur in separate models, so it does not prove same-model interplay |
| `titiler-openeo` | **DROPPED** — its ranged responses do not include literal `2XX` or `default`; `smart-edge-af` consolidates `not`, `default`, and nested composition |
| `apigee-registry` | **DROPPED** — its read/write-only coverage overlapped `sigstore-rekor`, which also consolidates literal `2XX`/`default` and implicit-discriminator coverage |
| `keycloak-admin` | **DROPPED** — its standalone `2XX` coverage forced a fourth registration; `sigstore-rekor` supplies literal `2XX` plus `default` coverage in the three-spec set |
| `smart-edge-af` | **DROPPED** — `TrafficInfluSub` has sibling `allOf` and `anyOf`, not one composition structurally nested inside the other |
| `jaewook-epcis` | **REJECTED** — Fern check reports 35 endpoint-example errors because `headers` examples are strings rather than maps |
| `mardi-gras` | **REJECTED** — Fern-clean and MIT, but it has no `allOf` and therefore could not consolidate the nested composition requirement |
| `paypal-checkout` | **DROPPED** — the only revision with `not` fails Fern on five invalid carrier enum names; Fern-clean older revisions lack `not` |
| `fern-docs-fai` (`fern-api/docs` `fern/apis/fai/openapi.json`) | **DROPPED** — every revision declaring `x-fern-audiences` or a component `x-fern-ignore` fails the Fern 5.20.0 generate: `Multiple request properties have the name domain` on `create_feedback` (do not retry any of its 70 revisions) |
| `count-co` (jentic `count.co/main/1.0` at `eb9d12a2`) | **DROPPED** — the Fern 5.20.0 generate reports `Found 8 errors`, each `Path parameter is unreferenced in endpoint` (do not retry this ref) |
| `instabase-aihub` (`instabase/aihub-openapi` at `a25f51e5`) | **DROPPED** — the Fern 5.20.0 generate reports `Found 1 errors`: `Expected example to be an object. Example is: [{"custom":{}}]` (do not retry this ref) |
| `ziptax-reference` (`ZipTax/ziptax-reference` at `918973a8`) | **DROPPED** — the Fern 5.20.0 generate reports `Multiple request properties resolve to the same generated name merchantType after camelCase normalization`; row 192 registers the same API from `ZipTax/ziptax-node`, whose older document predates that field |

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

## Row 307 — a sub-client named like the root client

`client_class_name` set to the class name of one of the document's own
resource sub-clients makes the root `client.py` define a class the sub-client
import would otherwise bind — a collision first observed on a privately held
specification whose configured client name equals one of its own resources'
sub-client class names (that evidence is held privately). That spec cannot be
published, so this row reproduces the collision
over row 13's Apache-2.0 Ecosystem API instead: its `Ecosystem` resource's
sub-client is `EcosystemClient`, the name a consumer of the "Ecosystem API"
would give its client, and its four other resources pin that a sub-client
colliding with nothing stays unaliased.

| name | selected for | status |
|---|---|---|
| `apideck.com-ecosystem-client-class-name` | `client_class_name: EcosystemClient`, imported by Fern as `ecosystem_client_EcosystemClient` | ✅ matched |

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
| `helios-verifiable-api` | 27 component schemas that are remote-URL `$ref`s into seven `ethereum/execution-apis` documents, fetched and resolved transitively, each pinned to an immutable commit by `corpus-remote-ref-pins.tsv` | ✅ matched |

Repairing crozier to reproduce it needed cross-document resolution
([`src/refs.rs`](../../src/refs.rs)) plus five rules the golden exposed along the
way — fetched-schema naming, unresolvable references, response aliases,
use-site nullability, and scalar query serialization — all recorded in
[`../../docs/matching.md`](../../docs/matching.md#cross-document-ref-resolution-issue-77).

**This row alone depends on a third-party fetch at generation time**, and the URLs
it references address `refs/heads/main` rather than an immutable ref. That is
why it is also the only row with records in
[`corpus-remote-ref-pins.tsv`](corpus-remote-ref-pins.tsv): the fetch substitutes
an immutable commit URL for each of the seven `ethereum/execution-apis`
references and verifies the SHA-256 it recorded for it, so an upstream edit to
those files no longer reaches this row. Moving a pin forward is an ordinary
regeneration —
[`../../docs/fern-goldens.md`](../../docs/fern-goldens.md#moving-a-remote-ref-pin-forward).

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

## Batch 14 — the fixture backlog's tail, and its recorded residuals (issue #188)

Six documents, closing the last three `FIXTURE` rows of
[`../../docs/openapi-surface-coverage.md`](../../docs/openapi-surface-coverage.md)'s
ranked backlog that had a witness. **Every witness the issue #188 searches
recorded as usable is registered** — a witness is not dropped for being
redundant, inconvenient, or already covered by another document — and Fern
accepted all six at `fernapi/fern-python-sdk:5.20.0`, so none took the
`fern-rejected` route.

| # | name | settles | state |
|---:|---|---|---|
| 127 | `torrentarr` | `media-type-range`, `duplicate-normalized-paths` | ✅ byte-matched, no generator change |
| 128 | `agco-ats` | `duplicate-normalized-paths`, `duplicate-operation-id` | ✅ byte-matched after three repairs |
| 129 | `svix-webhooks` | `duplicate-operation-id` | ✅ byte-matched after six repairs |
| 130 | `komga` | `media-type-range` | ⚠️ registered with 25 of 338 files in `unmatched` (40 when batch 14 registered it, 31 until row 302's numbered-operationId repair) |
| 131 | `short-io` | `duplicate-normalized-paths` | ⚠️ registered with 65 of 198 files in `unmatched` (77 when batch 14 registered it) |
| 132 | `webflow-v2` | `duplicate-operation-id` | ⚠️ registered with 305 of 1,495 files (365 when batch 14 registered it, 364 until Batch 18's repairs, 312 until Batch 19's hoisted-map repair, 306 until row 232's example-quoting repair) in `unmatched` and 148 crozier-only modules declared |

**What the three byte-matched rows cost.** AGCO: `float` joined
`naming::is_reserved`'s builtin set; hoisted operation-scoped types are deduped by
`(module, name)` so two operations sharing one `operationId` declare theirs once;
and a JSON body drops the explicit `content-type` header when its referenced
schema survives in the public type layer, no query parameter rides beside it, and
the Request Body Object offers several media types. Svix: an undeclared path
template expression becomes a required `str` argument (three of its operations
declare none, and crozier was interpolating a name the method did not take — not
valid Python); a declared `http` `bearer` scheme wires the client's optional
`token` even with no Security Requirement Object anywhere; a dotted `operationId`
whose group is not the tag keeps that group (`v1.application.list` →
`v1application_list`); a declared tag titles a dotted-id section verbatim; an
array parameter takes its item schema's example as a one-element list; a nullable
inline `additionalProperties` value type is `Optional`; and a description opening
on a line break keeps it. Two more came from Short.io and Webflow at the document
boundary: a bare string in a schema position names the `type` it spells, and a
Schema Object's `examples` is read from a map of named Example Objects as well as
from a sequence, with an explicit `properties: null` reading as the absent key.
All are recorded in
[`../../docs/matching.md`](../../docs/matching.md#documents-that-collide-with-themselves-issue-188).

**Why the three residual rows are registered rather than dropped.** Fern accepted
each of them, so nothing removes them from the registration route; what they carry
is crozier's own measured parity gap, enumerated file by file. Deleting the tree
would have left no measured reason for the gap, which is the opposite of what this
backlog is for. Each residual is a distinct body of work, named here so the next
change has an exact set to shorten:

- **`komga` (25 files, 40 when this batch registered it, 31 until row 302's numbered-operationId repair joined `getGenres_1` into `get_genres1`).** Binary/streaming responses. Fern makes **30**
  `httpx_client.stream(...)` calls returning `typing.Iterator[bytes]` under a
  `@contextlib.contextmanager`; crozier makes **6**. Komga keys its ranges on
  `default` — `GET /api/v1/books/{bookId}/pages/{pageNumber}` declares `400` of
  `*/*` and `default` of `image/*`, and no `200` — which crozier's
  `is_binary_response` never reaches, so `get_book_page_by_number` is
  `HttpResponse[None]` where Fern streams it. Two smaller causes ride along: a
  `content-type` header on 13 request bodies Fern leaves to httpx, and
  `typing.List` where Fern writes `typing.Sequence` for an array header parameter.
  So the `default`-response spelling of `media-type-range` **is** in this residual;
  the `200` spelling the row's classification rests on is pinned byte for byte by
  corpus row 127.
- **`short-io` (65 files).** Hoisted per-operation models — 59 of the 65 sit under
  a `types/` package. Fern declares a module per `anyOf` member of a hoisted
  response type (`post_links_duplicate_link_id_response_ttl` and 33 more) that
  crozier folds inline and never emits; and where both emit a model, crozier
  carries the document's full declared property set while Fern narrows it
  (`BadRequestErrorBody` is `error` plus an optional `message` in the golden,
  against crozier's seven fields).
- **`webflow-v2` (305 files + 148 crozier-only modules).** Two independent
  divergences. Its `servers` carry `x-fern-server-name: Data API`, so Fern names
  the environment member `DATA_API` and threads
  `base_url=self._client_wrapper.get_environment().base` through every raw client,
  where crozier writes `DEFAULT`; and Fern names a `oneOf` request body's hoisted
  variants differently from crozier's `…_request_body_zero`/`…_one`, which is what
  the 148 declared crozier-only modules are.

Licences were verified at each source repository at the pinned ref rather than
copied from the screening notes: `gotson/komga`, `svix/svix-webhooks`,
`webflow/openapi-spec` and `Feramance/Torrentarr` each carry an MIT `LICENSE`, and
the two `jentic/jentic-public-apis` redistributions are CC0-1.0 by the aggregating


## Batch 15 — the candidates a widened licence rule admitted (issue #188)

Five documents, from the rescreening
[`../../docs/licence-rescreening.md`](../../docs/licence-rescreening.md) ran after
the corpus's admissible-licence rule widened
([`../../docs/corpus-licensing.md`](../../docs/corpus-licensing.md)). **Every
candidate that record admits, Fern accepts and the corpus's other two screens
allow is registered** — a witness is not dropped for being redundant, and rows 134
and 136 are each a further declarer of a shape another row already pins, while row
137 was passed over once for declaring no enumerated coverage row and is registered
all the same: a byte-matching golden is parity evidence in its own right, and
*"it settles no backlog row"* is not one of this corpus's three admission screens.
It settles one in the end, jointly — `oauth2-implicit`, whose evidence cell read
*(declared by no registered source)* off a 124-source walk and now names five
golden-bearing declarers, this row among them. Its other two census firsts,
`securityScheme.scheme=OAuth` and a golden-bearing `securityScheme.in=query`, are
**strays on an `oauth2` Security Scheme Object** rather than the `http`- and
`apiKey`-shaped rows that carry those selectors, so `http-oauth` stays a `gap` and
`apiKey-query` stays `limitations`; each row's evidence cell now records the
declaration and why it is not that row's shape.

| # | name | settles | state |
|---:|---|---|---|
| 133 | `loris-dataquery` | `parameter-style-spacedelimited-query-scalar`, `parameter-style-pipedelimited-query-scalar` | ✅ byte-matched after one repair |
| 134 | `sftpgo` | `media-type-range`, `operation-overrides-path-item-parameter` | ✅ byte-matched after eleven repairs |
| 135 | `googleapis-servicebroker` | `duplicate-normalized-paths` | ✅ byte-matched after two repairs |
| 136 | `audiobookshelf` | `media-type-range` | ✅ byte-matched after six repairs |
| 137 | `steaminputdb` | `oauth2-implicit` (jointly — one of five declarers) | ✅ byte-matched after six repairs |

**The two candidates this batch does not register, and the rule that excludes
each.** Both are admitted by the widened rule and both are accepted by Fern at the
*preview* CLI the rescreening screened at; neither survives the corpus's own
`Fern must accept it FIRST` screen, read at the CLI
[`../../tools/fern-goldens/generate-fern-fixture.sh`](../../tools/fern-goldens/generate-fern-fixture.sh)
pins.

- **Eclipse Ditto's HTTP API** is publisher-owned and immutably pinned, and is the
  only admitted declarer of `format-iri-reference` anywhere the issue #188
  searches reached. Fern's Python generator **refuses it at the CLI version this
  corpus generates at**: exit 1 on `Multiple request properties have the name
  thingId`, where the rescreening measured exit 0 at Fern CLI 5.114.1.
  `format-iri-reference` stays a `gap` on it.
- **The CureDAO API** (`curedao/curedao-monorepo` `docs/openapi-huge.yml`) is the
  **exit-0-and-nothing-happened** failure [`AGENTS.md`](AGENTS.md)'s screening
  section names, and it exits 0 at *both* CLIs. The document declares no `openapi`
  version key at all — its top-level keys are `x-stoplight`, `info`, `servers`,
  `tags`, `paths` and `components` — so Fern logs
  `is not a valid OpenAPI, AsyncAPI, or OpenRPC file. Skipping...`, prints
  `All checks passed`, and writes an **empty SDK**: 36 files, a zero-byte
  `README.md`, a 12-byte `reference.md`, no `types/`, no sub-client and no
  endpoint. A golden like that pins nothing about crozier's OpenAPI behaviour, so
  the document fails the screen rather than the licence.

Both are logged in [`AGENTS.md`](AGENTS.md)'s REJECTED table with their exact
diagnostics and the CLI each belongs to.

**What the five rows cost.** Google's Service Broker: a dotted `operationId`'s
kept group snake-cases as one name with its dots as word separators, and a
parameter's leading punctuation drops out of the class it hoists. LORIS: a
flattened body over an untitled surviving schema loses its explicit
`content-type`, which is also what SFTPGo's six such bodies and Audiobookshelf's
two measure. Audiobookshelf: a request body `$ref`ing a plain scalar is one
argument (without it, eight `Authors` operations had no client at all); a
one-member composition is an alias to that member; a union member `$ref`ing a
`nullable` schema stays `Optional`; a declared example is substituted by the
parameter's own name on a `text/*` endpoint as well as a binary one; and a body
property follows its `$ref` for an example. SFTPGo: an untyped `enum` is a string,
`copy` is a protected pydantic field name, a content-map key is matched with its
parameters ignored, a multipart array of binary strings is a list of `core.File`,
an `allOf` of one `$ref` is an alias, and a `*/*` binary download documents its own
arguments. SteamInputDB: an OAuth Flow Object's
`scopes: null` reads as no scopes; an `oauth2` scheme reaches the client wrapper
with no Security Requirement Object declared anywhere; a typeless property keeps
its description when the field wraps it in `Optional`; the inlined-body drop
counts *surviving* endpoints rather than the document's operations; an inline
`readOnly: true` property is dropped from the request it is inlined into; and a
tab in an operation description survives into `reference.md`, expanded to spaces
only where `ruff format` performs that expansion. All are recorded in
[`../../docs/matching.md`](../../docs/matching.md#what-the-widened-licence-rules-witnesses-cost-issue-188).

Two of those repairs also shortened a batch-14 residual: `komga`'s `unmatched` is
re-measured from 40 of its 338 files to 32.

Licences were verified at each source repository at the pinned ref rather than
copied from the screening record: `aces/Loris` and `advplyr/audiobookshelf` each
carry a `GPL-3.0` `LICENSE`, `drakkan/sftpgo` an `AGPL-3.0` one,
`Alia5/steaminputdb.com` an `AGPL-3.0` `LICENSE.txt` beside the document's own
`info.license` `identifier: AGPL-3.0`, and the Google Service Broker document
carries its own `Creative Commons Attribution 3.0` `info.license` inside the
CC0-1.0 `APIs-guru/openapi-directory` aggregation.

## Batch 16 — PayPal catalogue products

Row 138 registers the first document in the reconciliation's preferred-document
order. The pinned publisher document has four sole-member `anyOf` detail-item
wrappers; Fern retains concrete item models for all four. The standard census
reports no declaration of the other 29 owned selectors. The source is fetched
unmodified; the golden is generated at Python 5.20.0 / CLI 5.67.1 and byte-matches
with `unmatched: &[]`. See the [registration measurement](../../docs/openapi-surface/schemas.md#paypal-registration-measurement).

The repairs spell numeric schema names as whole numbers, infer the optional
singleton `name` discriminator across referenced union members, normalize
punctuation in discriminator-derived names, retain the first typed base of a
composed error response, retain described constant headers in documentation and
place them before optional request headers, and use declared examples for named
array request bodies. The byte comparison and missing/malformed-source recovery
journey run the real CLI over the pinned document.

When a diagnostic `TMPDIR` lives inside another Git checkout, set
`GIT_CEILING_DIRECTORIES` to that temporary root during generation. Otherwise
Fern records that unrelated parent checkout's commit in its metadata. This
registration was regenerated with that boundary; no generated metadata was edited.

## Batch 17 — the witness searches' candidates

Rows 144 onward register the candidates the two witness-search ledgers,
[`../../docs/openapi-surface/witness-search-github/candidates.tsv`](../../docs/openapi-surface/witness-search-github/candidates.tsv)
and
[`../../docs/openapi-surface/witness-search-registries/candidates.tsv`](../../docs/openapi-surface/witness-search-registries/candidates.tsv),
mark usable: a licence that grants redistribution, an immutable ref, and Fern's
acceptance of the raw document, each re-measured here rather than inherited. They
are registered in the order the coverage document's ranking rubric gives their
keys. Every golden is generated at Python 5.20.0 / CLI 5.67.1 from the fetched,
unmodified document and byte-matches with `unmatched: &[]`.

| # | name | settles | state |
|---:|---|---|---|
| 144 | `paloalto-cspm-alerts` | `annotated-ref-target-composed`, `annotated-ref-target-oneof` (jointly) | ✅ byte-matched after this batch's repairs |
| 145 | `paloalto-cspm-reports` | `annotated-ref-target-oneof` (jointly) | ✅ byte-matched after this batch's repairs |
| 146 | `paloalto-cspm-search-manager` | `annotated-ref-target-oneof` (jointly) | ✅ byte-matched after this batch's repairs |
| 147 | `thrivecart` | `ref-pointer-undeclared-component-head` | ✅ byte-matched with no repair of its own |
| 148 | `truefoundry-trueforge-5adde28` | `annotated-ref-target-closed-object` | ✅ byte-matched after this batch's repairs |
| 149 | `fergus` | `anyof-array-variant-struct-item` | ✅ byte-matched after this batch's repairs |
| 150 | `groupe-psa` | `annotated-ref-target-composed` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 151 | `timelyapp` | `anyof-array-variant-struct-item` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 152 | `nextgen` | `schema-name-nonidentifier-name`; `ref-pointer-undeclared-component-head` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 153 | `auto-agent-protocol` | `ref-pointer-unnamed-segment` | ✅ byte-matched after this batch's repairs |
| 154 | `skool` | `ref-pointer-undeclared-component-head` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 155 | `spendesk` | `ref-pointer-undeclared-component-head` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 156 | `billie` | `ref-pointer-undeclared-component-head` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 157 | `alma-france` | `ref-pointer-undeclared-component-head` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 158 | `outreach` | `ref-pointer-undeclared-component-head` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 159 | `tally` | `ref-pointer-undeclared-component-head` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 160 | `billie-entry` | `ref-pointer-undeclared-component-head` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 161 | `skool-entry` | `ref-pointer-undeclared-component-head` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 162 | `timelyapp-entry` | `anyof-array-variant-struct-item` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 163 | `cradl` | `anyof-array-variant-closed-object-item`; `anyof-array-variant-struct-item` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 164 | `zulip` | `oneof-array-variant-closed-object-item`; `annotated-ref-target-oneof`, `annotated-ref-target-closed-object`, `annotated-ref-target-composed` (jointly; already `golden`) | ✅ byte-matched after this batch's repairs |
| 165 | `zulip-jentic` | `oneof-array-variant-closed-object-item`, `annotated-ref-target-oneof`, `annotated-ref-target-closed-object`, `annotated-ref-target-composed` (jointly; already `golden`) | ✅ byte-matched |
| 166 | `zulip-jentic-entry` | `oneof-array-variant-closed-object-item`, `annotated-ref-target-oneof`, `annotated-ref-target-closed-object`, `annotated-ref-target-composed` (jointly; already `golden`) | ✅ byte-matched |

The repairs send a parameterised JSON request media type
(`application/json; charset=UTF-8`) verbatim as the `content-type` of every
request that carries it, find a single-use body's JSON representation by the same
selection the body itself uses, so the model is dropped from the type layer and
its hoisted use-site copies move into the tag's package, document a union's
use-site copy with the annotation that names it, fall back to the target's own
description for a field whose annotation adds none, and spell a bare `=` enum
value `EQUAL_TO`. Row 148's repairs keep the component schemas an
`x-fern-ignore` operation alone references, as Fern does; flatten a one-member
`oneOf` over an inline object into that object rather than inferring a
discriminated union from its single-valued tag; list a package's nested
sub-clients in `reference.md` after every sibling that owns endpoints; and
synthesize a query parameter's worked-example value only where Fern's importer
builds no example of its own — read off Fern's own `ExampleEndpointFactory` and
`generatePrimitiveStringExample`, which also closes one of `webflow-v2`'s
residual files. Row 149's repairs follow Fern's own importer where crozier had
fitted heuristics: union variants are named by Fern's `getUniqueSubTypeNames`,
which alone reproduces every earlier golden's variant names; a query parameter's
enum-only composition is a tag-local enum; a lone composition, inline object or
inline-object array beside `null` is typed and documented as that member; a
nested `allOf` flattens into one object, whose repeated property is one field or,
in an inline body, one prefixed argument; an `allOf` of inline objects is no
composition for the content-type rule; a description's indentation-only last line
is a line of its own; and a datetime example is moved to UTC. Together they also
close twelve of `short-io`'s residual files (77 -> 65). Row 150's repairs, each
read off Fern's importer source or a `fern ir` bisection of the document: a
non-string `required` entry requires nothing; an enum mixing kinds is its base
type; an `allOf` around one inline element is that element, so an annotation on
a `$ref` to it loses its description while a component so written keeps the
element's; an annotated `$ref` component is a flat copy; a restated base property
takes the base's schema keys with it, and extends only where both require it; an
array component's enum element is a class, and a query `$ref` to such an array is
allow-multiple; a lone-`allOf` response is its `$ref`; descriptions keep an opening
line break and an indentation-only last line; and a request body whose base
requires a property its restatement leaves optional and example-less gets no
importer example, so Fern's fallback lists two items. Row 151's repairs make an
`anyOf` member declaring `properties: {}` an empty model rather than a map, and a
property whose lone `allOf` `$ref` sits beside properties of its own a model
rather than that `$ref`. Row 152's repairs break a class name's words on every
character an identifier cannot hold (Postman-exported component names such as
`{{baseUrl}}/persons/:personId-Request`), name an operation whose `operationId`
is such a URL by all of its words rather than by its first `{…}`, carry a bare
scalar body's schema `example` into its worked call, and leave an untyped request
body's `{"key": "value"}` placeholder on one line in the README. Row 153's
repairs type a pointer through a segment no generated type is named by (a
`$defs` member) as unknown and drop the description beside it, declare the
property types of an object whose `anyOf` only restates `required`, keep a
restated base property's description, and wrap a one-pair dict argument in the
README. Row 154's repair guards an empty response where the success body is a
`$ref` to a component the document never declares, which Fern types unknown.
Row 155's repair follows Fern's importer, which builds no worked example for an
operation whose success body is such a `$ref`; its IR fallback then keys a
bare-object body by the key type's sample, `{"string": {"key": "value"}}`.
Row 156's repair makes every server Fern names (a `Production` or `Sandbox`
description) an environment member, the first of them the default, as Fern's
`buildEnvironments` does; crozier had kept the first server alone.
Row 157 needed no repair of its own: its seven `$ref: ApiResponse` success
bodies take rows 154 and 155's empty-body guard and example fallback.
Row 158's repair sends a flattened body's vendor JSON media type
(`application/vnd.api+json`) as its `content-type`, where crozier had written
`application/json`; a Fern 5.20.0 probe shows the same for an inline object body,
which an older generation test had asserted the other way.
Row 159's repairs, each read off Fern's importer: a `discriminator` that maps
nothing strips its tag from the variants like an inferred one when every
variant's one-value tag names it (Tally's 45 `Block` members); an enum value is
spelled out only when it is one of Fern's mapped symbols *whole* (`*` is `ALL`,
`image/*` is `IMAGE`), and a later value whose member name an earlier one took
is dropped rather than suffixed; and an inline object restating an `allOf`
parent's property with a schema of its own inlines that parent, as a component
already did.
Row 148 is a later revision of row 108's document, registered
under a name of its own because the shape it witnesses is absent at row 108's
commit. The three Prisma Cloud documents are separate descriptions in
Palo Alto Networks' own `pan.dev` repository; each is a row of its own because
each is a document Fern generates on its own.

Rows 160 to 162 are jentic's `meta/import/input-entry.json` copies of Billie,
Skool and Timely. Each holds the same document as rows 156, 154 and 151 with
its object keys in another order, which is a different input to Fern. Each
golden byte-matches with no repair of its own.

Row 163's repairs, read off Fern's IR for Cradl:
- a list of lists of inline objects names its leaf model one `Item` per level
  (`GroundTruthListOneItemItem`);
- a `$ref` member's sibling `nullable` is not read;
- a property union's `nullable` array member keeps its `Optional`;
- a `nullable` closed object with no properties is `Optional[Dict[str, Any]]`.

Row 164, Zulip's own description, byte-matches its 1014-file golden after the
repairs below, each read off the golden or a `fern ir` run:
- Unions and enums:
  - a string `$ref` narrowed by an inline `enum` is an enum documented by
    the reference;
  - union variants past the nineteenth are named in words (`…FiftyEight`);
  - union members that are string enums or untitled inline objects hoist
    models of their own.
- Restatements:
  - a restatement conflicts with its parent's property only if the child
    does not require it or makes it nullable, whatever the parent requires;
  - an empty restatement takes a property the parent declares inline;
  - an unknown field takes no docstring from its parent;
  - an annotated `$ref` to a composed target, or to a map value, is a flat
    copy;
  - a component that is a bare object is a map whatever its example.
- Error bodies: the last declaration of a status names `{Class}Body`, and
  earlier `oneOf` declarations leave their variant models behind.
- Urlencoded bodies:
  - a part's `encoding.contentType` is ignored;
  - a union body is one `request` sent through `data=`, and Fern builds no
    example for it, so its path parameter passes its name;
  - fields take their annotation's docstring and example.
- YAML examples: a timestamp-shaped example stops being a string only when
  the YAML writes it unquoted.

These also shrank `short-io`'s residual from 65 files to 61.

The usable candidates the two ledgers held beyond these rows and their
byte-identical copies are registered or disposed of in Batch 18 below.

## Batch 18 — the witness searches' candidates, continued

Rows 167 to 179 register the usable candidates Batch 17 left: every candidate in
the two ledgers whose three screens pass and whose key was still a `gap` row, each
screened again here rather than inherited. Every golden is generated at Python
5.20.0 / CLI 5.67.1 from the fetched, unmodified document with Route A, and every
row byte-matches with `unmatched: &[]`.

| # | name | settles | state |
|---:|---|---|---|
| 167 | `viskit-studio` | `anyof-array-variant-anyof-nullable-item` | ✅ byte-matched after this batch's repairs |
| 168 | `milvus-restful-v2-3` | `anyof-array-variant-empty-object-item` (jointly) | ✅ byte-matched after this batch's repairs |
| 169 | `milvus-restful-v2-4` | `anyof-array-variant-empty-object-item` (jointly) | ✅ byte-matched after this batch's repairs |
| 170 | `ramu-shogi` | `anyof-array-variant-oneof-nullable-item` | ✅ byte-matched after this batch's repairs |
| 171 | `embedpdf-cloudpdf` | `array-item-pointer-walk-anyof` | ✅ byte-matched after this batch's repairs |
| 172 | `langchain-agent-protocol` | `oneof-array-variant-anyof-item` | ✅ byte-matched with no repair of its own |
| 173 | `hse` | `oneof-array-variant-composed-item` | ✅ byte-matched with no repair of its own |
| 174 | `milvus-vector-operations` | `oneof-array-variant-empty-object-item` | ✅ byte-matched after this batch's repairs |
| 175 | `npq-registration` | `property-sole-anyof-closed-object-member`, `property-sole-anyof-struct-member` | ✅ byte-matched after this batch's repairs |
| 176 | `mistle-control-plane` | `property-sole-oneof-closed-object-member` | ✅ byte-matched with no repair of its own |
| 177 | `osparc-payments` | `oauth2-password` | ✅ byte-matched after this batch's repairs |
| 178 | `huatuo-node` | `securityscheme-ref` (jointly) | ✅ byte-matched after this batch's repairs |
| 179 | `huatuo-server` | `securityscheme-ref` (jointly) | ✅ byte-matched after this batch's repairs |

The repairs, each read off Fern's importer source or the golden itself:
- References and types:
  - a `$ref` pointing *inside* a component schema — through `properties`,
    `items` or a composition member — is copied where it is used, as Fern's
    `resolveSchemaReference` walks it, so CloudPDF's pointers become models named
    for their use site or plain scalars; one ending on a composition member stays
    unknown, as the committed probe measured;
  - a lone pointer `allOf` member beside only annotations is its holder's schema;
  - a union whose members all convert alike is that member (`Optional[float]`),
    and a nullable element union is an optional element;
  - an inline discriminated-union variant takes the fields the model lowering
    gave it, undocumented;
  - an object whose `required` is not a list is unknown, and its request builds
    no importer example;
  - a union member of `type: object` with `properties: {}` is an empty model,
    closed or not, and an inline union element of a component array is a named
    `{Name}Item` alias;
  - a list element beside `null` is `Optional` in a component union too;
  - an `allOf` member adding only nullability makes the composition an optional
    flat copy of its `$ref` (Ramu Shogi's `GetUserSettingsResponse.document`),
    and an earlier error body's enum survives a later union declaration of the
    same status.
- Naming:
  - a FastAPI `operationId` loses its `{path}_{method}` suffix under a tag, by
    Fern's `maybeGetFastApiEndpointLocation`;
  - `x-enum-varnames` loses the prefix all its names share, by Fern's
    `stripCommonPrefix`;
  - an enum drops a later value only when its pre-casing name matches an
    earlier one case-blind, so NPQ's `created_at` and `-created_at` both stay;
  - a model field shadowing `BaseModel.validate` is `validate_`, and an example
    spells a model-only rename by its plain name.
- Requests, headers and examples:
  - a promoted header is typed by its schema (`Optional[int]`, sent as `str()`);
  - only a binary media family is sent as bytes, so `application/proto` carries
    no request;
  - a referenced map body stays required;
  - an inline JSON body property keeps its description's whitespace;
  - an empty model takes any example, an inline path-parameter pattern keeps its
    example, a required nullable field is left out of a constructed example, and
    an argument-less binary `POST` is documented.
- Package layout: a nested client's types are re-exported by its parent package
  and imported by dotted path, its enums import `core` from their own depth, and
  the README anchors on a top-level client.

They also shrink `webflow-v2`'s residual from 364 files to 312.

Every other usable candidate in the two ledgers is now disposed of:
- **A byte-identical copy** of a row above or of Batch 17's names that row and
  the shared sha256 in its ledger disposition — among them Milvus's
  `v2.3.x/openapi.json` and `v2.4.x/Restful API v2.openapi.json`, the same bytes
  as rows 169 and 168 under other paths.
- **Eight documents whose keys were already `golden`** were left
  `pending-registration; owner thin-goldens-continue` in their ledger
  disposition: SimStudio's `openapi-v2-logs.json` and `openapi-v2-tables.json`,
  Vellum's gateway, `vfarcic/dot-ai`, Palo Alto's `code/Technologies.json`,
  marimo's `plugins.openapi.yaml`, MockServer's own description and Otoroshi's
  schema bundle. Batch 20 registers seven of them as rows 216 to 222, and their
  dispositions now name those rows. MockServer's mutable absolute `$ref` to the
  draft-04 meta-schema kept it out of that batch; once
  `corpus-remote-ref-pins.tsv` pinned that `$ref` to an immutable commit copy,
  it was registered as row 232.
- **The three jentic documents** the `golden-reach-witnesses` handoff proposed —
  DigitalOcean, Cvent and Sellsy — are Fern refusals, recorded in
  [`AGENTS.md`](AGENTS.md#specs-already-tried-and-rejected-do-not-re-attempt-without-a-fix-upstream)
  with their measured exit status and diagnostics.

## Batch 19 — golden-reach witnesses (rows 191–215)

These rows buy arms the [golden reach ranking](../../docs/openapi-surface-coverage.md#golden-reach-row-by-row)
found no earlier witness reaching. Each was chosen by running the instrumented
crozier over candidate documents and keeping those that execute the arm, then
screened for licence, immutable ref and Fern acceptance, and checked against every
`gap` row's selector so that no registration here settles a `gap` row. Row 191
gives `format-uri-template` its first golden-bearing witness — its only earlier
declarer, `github.com`, is a DROPPED row — and row 192 gives
`audience-dual-header-policy` its first real-world one, generated for an audience
so the filter removes operations rather than keeping all of them.

| # | name | row it buys an arm for | status |
|---:|---|---|---|
| 191 | `openlinksw-osdb` | `format-uri-template` | ✅ byte-matched after two repairs |
| 192 | `ziptax-node` | `audience-dual-header-policy` | ✅ byte-matched after one repair |
| 193 | `nexmo-messages` | `all-of-nested-composition` | ✅ byte-matched after five repairs |
| 194 | `deepsearch-ds-v2` | `property-anyof-discriminated-union` | ✅ byte-matched after three repairs |
| 195 | `mindee-ocr` | none — see below | ✅ byte-matched with no repair |
| 196 | `opencodeui` | `anyof-sole-member` | ✅ byte-matched |

The repairs: a `:` separates words in a generated class name (`osdb:output_type`
hoists `ExecBodyOsdbOutputType`); a `2XX` range key is no success status, so a
bodyless one beside a `default` body no longer makes the method optional; and a
`204` is empty whatever content it declares, so an unknown body beside one is
`typing.Optional[typing.Any]` while a lone `204` or a schemaless `200` stays
`typing.Any`.

Row 193, the Vonage Messages API as APIs.guru pins it (its publisher repository
no longer exists), is the corpus's first operation-level union whose members are
themselves compositions: a `oneOf` of five channel `oneOf`s over `allOf` members,
which is the inline-object arm of `hoist_union_variant` no earlier witness took.
Its repairs: a member that is itself a union is a named `{Parent}{Ordinal}` union
and a union of one member is that member; an `allOf` member that redeclares a
property of a composed `$ref` base flattens that base and extends the base's own
bases instead; an untitled, undiscriminated inline union body leaves its content
type to httpx; an inline union error body is the `{ErrorClass}Body` discriminated
union; and a redeclared base enum keeps the base's description.

Row 194 was found by the arm searches the golden-reach records under
`docs/openapi-surface/golden-reach-witnesses/` hold: a Sourcegraph result at its
indexed commit that the instrumented `crozier` run showed executing its row's
unreached site, declaring no `gap` selector. IBM's Deep Search API as the DS4SD
toolkit pins it needed three repairs: a nullable map of an inline union hoists its
value to `{Owner}{Prop}Value`; a query parameter whose schema declares no type is
a `str`; and an endpoint with an untyped path parameter is exampled by Fern's
other writer, the parameter by its own name and a free-form map body as one
`"string"` entry. Row 195, the Mindee OCR API as its publisher serves it and
jentic pins it, was registered for `items-oneof-element` on a probe that ran while
`src/` no longer matched the instrumented build, so it read another arm's regions;
re-probed on a consistent build it executes no site of that row, and the
golden-only ledger agrees. It stays as a real specification that byte-matches as
generated, and buys no arm. All five
goldens are generated at Python 5.20.0 / CLI 5.67.1 and match with
`unmatched: &[]`.

The same searches found the opencode server API as `lehhair/OpenCodeUI` publishes
it — a different document from the DROPPED `opencode` row, which Fern refused —
reaching `anyof-sole-member`'s arm. It declares `schema.anyOf>schema.anyOf`, the
`gap` row `anyof-anyof-variant`, so it is handed off rather than registered
([`handoff.tsv`](../../docs/openapi-surface/golden-reach-witnesses/handoff.tsv)).
It was byte-matched locally against its measured Fern 5.20.0 output first, and
the nine repairs that took are kept, each with a `tests/generation.rs` test on a
fragment of the document: an untagged dotted `operationId` hangs off the root
client; the README walks the root client's operations after every sub-client's; a
component schema named for an error class the document raises is renamed
`{Name}Body`, and such a `$ref` body is never downgraded as a coined one; `status`
joins the property names Fern infers a discriminant from over `$ref` members; a
union member that is a map of an inline union or object hoists its value; a union
of one schema written twice is that schema; a hoisted model's map of an inline
object hoists its value; and a query parameter beside a body keeps the
`content-type` header. The hoisted-map repair also closes six of `webflow-v2`'s
open files, which proves it now; the other eight rest on the measured golden until
the hand-off's registration commits it.

## Batch 20 — the golden-reach continuation's pending witnesses (rows 216–260)

The two witness-search ledgers left eight usable documents whose keys were
already `golden` marked `pending-registration; owner thin-goldens-continue`.
Seven are registered here, each generated by Route A at Python 5.20.0 / CLI
5.67.1 and byte-matching with `unmatched: &[]`:

| # | name | the key its ledger row names | status |
|---:|---|---|---|
| 216 | `sim-logs` | `anyof-array-variant-closed-object-item` | ✅ byte-matched with no repair |
| 217 | `sim-tables` | `anyof-array-variant-closed-object-item` | ✅ byte-matched after five repairs |
| 218 | `vellum-gateway` | `anyof-array-variant-closed-object-item` | ✅ byte-matched after two repairs |
| 219 | `dot-ai` | `anyof-array-variant-closed-object-item` | ✅ byte-matched after two repairs |
| 220 | `paloalto-code-technologies` | `anyof-array-variant-struct-item` | ✅ byte-matched after one repair |
| 221 | `marimo-plugins` | `anyof-array-variant-struct-item` | ✅ byte-matched after ten repairs |
| 222 | `otoroshi` | `ref-pointer-undeclared-component-head` | ✅ byte-matched after three repairs |

The repairs were read off Fern's own sources — the CLI 5.67.1 importer bundle and
the `fernapi/fern-python-sdk:5.20.0` generator — rather than inferred from one
golden, and each is pinned offline by a `tests/generation.rs` test on a fragment
of its document:
- Parsing and naming: a `"servers": null` reads as no servers (Palo Alto); a tag's
  words are stripped from an operationId they prefix, so Vellum's
  `credential_requests_peek` under `credential-requests` is `peek`
  (`getEndpointLocation`); `application/x-ndjson` is JSON (`MediaType.isJSON`,
  Otoroshi's bulk bodies).
- Types: an inline-object array beside `null` hoists its element (Vellum); a
  component that is only `type: "null"` is `Optional[Any]`, and a response naming
  a nullable component is optional (marimo); a union's members tagged by a string
  `const` — on `type` whether or not it is required, on any property when it is —
  are discriminated (`getPossibleDiscriminants`: marimo's search filters, Sim's
  upload transfers); a nullable map's nullability reaches a map nested as its
  value (marimo); a map property whose value is `anyOf: [string, null]` is
  `Dict[str, Optional[str]]` (Sim); a `$ref` to an undeclared component is the
  unknown type with no field docs (Otoroshi).
- Requests: a `$ref` to a `type: "null"` or `{}` component is an optional or a
  required `request`; a `$ref` body sent as one `request` collapses to its bare
  type name and loses its `content-type` unless its target is titled, whatever the
  request body's own description says (`buildRequest`); a propertyless model that
  is an operation's only input is documented as `request` in `reference.md`.
- Examples: an empty map example is synthesized as `{"key": "value"}` (dot-ai);
  a body component's 3.1 `examples` array fills its fields, while a map declaring
  only `examples` gives a property none (Sim); a union's later enum alternative is
  exampled by its member outside a path parameter (marimo); a required unexampled
  `{}` property fails the importer's request example, so the fallback's two-item
  lists show (marimo); the docstring writer puts headers before query parameters
  (Sim); a 3.1 response naming a `{}` component guards the empty body (marimo),
  which also closes one of `komga`'s residual files; and an argument-free client
  is constructed on one line in the README (dot-ai).

The eighth, MockServer's own description
(`mock-server/mockserver-monorepo@ff83158d204c5eb7ab5fabc8ba74ffd3a76f5037`,
`jekyll-www.mock-server.com/mockserver-openapi.yaml`, Apache-2.0), `$ref`s
`http://json-schema.org/draft-04/schema`, a mutable absolute reference that
`tools/corpus/fetch-corpus.sh` refuses unpinned. It is registered below as row 232:
`corpus-remote-ref-pins.tsv` pins that reference to `json-schema-org/json-schema-spec`
at `d4c5b3a2…`, the commit the json-schema.org site's `_includes/draft-04`
submodule pins, with its digest. Its first probe crashed crozier (an
annotated-reference cycle, and a class with an empty name hoisted for the
meta-schema), so it is a golden for the bugs it exposed whatever its reach
measures; the three closures that named it as their witness name row 232 again.

### Rows 223–232: witnesses the arm searches found

The instrumented probes of build `1131cbbcb0e3` found nine Fern-accepted,
licensed documents that execute a handling site no earlier golden reached, and
MockServer (row 232) is the witness the batch above set aside. Each is
registered here with its Fern 5.20.0 golden and byte-matches with
`unmatched: &[]`:

| # | name | the row whose unreached site it reached | status |
|---:|---|---|---|
| 223 | `nexmo-conversation` | `ref-pointer-composition-index`, `ref-pointer-nested-properties` | ⛔ withdrawn for a missing publisher grant; its source, golden and test are removed |
| 224 | `codat-assess` | `ref-pointer-composition-index` | ⛔ withdrawn for a disputed grant; its golden and test are removed |
| 225 | `googleapis-monitoring-v1` | `enum-leading-zero-member` | ✅ byte-matched after one repair |
| 226 | `docu-goapiserver` | `anyof-anyof-variant` | ✅ byte-matched after four repairs |
| 227 | `onevoice` | `mutualTLS` | ✅ byte-matched after one repair |
| 228 | `xfsc-oidc-identity-resolver` | `securityscheme-type-openidconnect` | ✅ byte-matched after one repair |
| 229 | `adyen-acs-notification` | `enum-leading-digit-identifier` | ✅ byte-matched after one repair |
| 230 | `peopledatalabs` | `enum-leading-digit-identifier` | ✅ byte-matched after five repairs |
| 231 | `standrig` | `anyof-string-const-variant` | ✅ byte-matched after three repairs |
| 232 | `mockserver` | `oneof-array-variant-closed-object-item` | ✅ byte-matched after the repairs listed under MockServer below |

Each repair is pinned offline by a `tests/generation.rs` fragment of its document:
- Pointers: Fern's importer converts any reference whose text names `properties`
  as a copy at the reference, walking the whole pointer to a composition member,
  and names a discriminated variant so copied after the pointer (Vonage); a
  schema `$ref` into `#/components/parameters/<name>/schema` is that schema
  copied with its description (Codat; since row 224's withdrawal the hand-written
  `composition-index-pointer` fixture's Fern tree pins it).
- Requests: an inline schema in `components.requestBodies` keeps its
  `content-type`, and an optional query parameter whose example YAML reads as a
  timestamp is left out of the worked call (Vonage).
- Names: a zero-led digit run collapses onto the word before it like any other
  (`ALIGN_PERCENTILE_05` is `ALIGN_PERCENTILE05`); only a name *led* by one,
  which Fern refuses, keeps crozier's legal fallback (Cloud Monitoring); and a
  value that is a number *whole* is spelled as that number with its leading
  zeros read away, so `01` is `ONE` (Adyen); past 9,999 Fern's speller writes
  `undefined`, so `10001+` is `UNDEFINED`, and consecutive single letters join
  as lodash re-splits Fern's `upperFirst(camelCase(…))` name, so `u.s.` is `US`
  (People Data Labs).
- Layout: a tab written into generated Python is four spaces (Fern's code
  writer), identical inline body-union members collapse to `Union[typing.Any]`,
  and the README passes that body's placeholder on one line (People Data Labs).
- Types: an `anyOf` variant that is one member beside `null` is that member made
  optional (Primula Tracker).
- Typeless shapes: a schema with no `type` but a `const` is `str`, an inline
  object's property whose alternatives are all booleans is one `bool`, and a
  body closed with `additionalProperties: false` but declaring no `properties`
  is a `Dict[str, Any]` request (StandRig).
- Auth: an `openIdConnect` scheme is a bearer token, required on OAuth2's terms
  (XFSC); a requirement naming only schemes Fern does not support — a cookie
  `apiKey`, `mutualTLS` — defines no auth at all (OneVoice).
- Examples: a binary download the importer declines shows only Fern's first IR
  *error* example, so one declaring no error response has none (Codat, pinned
  the same way since row 224's withdrawal); an array
  body and a `$ref`-to-union body take the media type's example, an enum variant
  matches only its own values, and an unknown body's example drops its `null`
  members (Primula Tracker).
- MockServer: a `$ref` naming a whole remote document is one component named
  after its file, with `#` meaning it and `#/definitions/<name>` a component of
  its own; an annotated reference that cycles back terminates; a degraded
  `Union[Any]` keeps its declared properties as reference edges, so a model
  holding it repairs its forward references; `allOf` of a scalar reference plus
  annotations is that scalar; `json` is a reserved field name; a later error
  body leaves an earlier enum property behind as a type; an optional `$ref` to a
  composition is a required argument, and an inline body field renamed for a
  parameter collision is sent under its renamed argument. Its examples: a union
  is exampled as Fern's heuristic picks and narrows it; a free-form value drops
  nulls and empty arrays; a map of models constructs each value; a string
  holding `"` is single-quoted; a binary download's inline body drops its media
  example; and `reference.md` documents the singular `example`, writing a
  free-form map value on one line. Its names: sub-client imports sort
  case-insensitively, and a summary's one-letter words join as camel-casing
  joins them (`load_ag_rpc_…`).

### Row 224 withdrawn

| # | name | method | source | pinned ref | license | decision | withdrawn because |
|---:|---|---|---|---|---|---|---|
| 224 | `codat-assess` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/codat.io/assess/1.0/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | CC0-1.0 (the `APIs-guru/openapi-directory` aggregation's own `LICENSE`; the document declares no `info.license`) | withdrawn | its only grant is the aggregator's, and `docs/openapi-surface/witness-search-blocked-artifacts.tsv` refuses these bytes for want of a publisher grant. Codat Assess 1.0; `$ref` pointers into a sibling `definitions` map's composition members |

Row 224 registered Codat's `assess/1.0` description at `APIs-guru/openapi-directory`
`f04b8d0b` under the aggregator's own grant, while
`docs/openapi-surface/witness-search-blocked-artifacts.tsv` lists the same bytes as
grant-blocked: the publisher grants no redistribution of them, and an aggregation
grant alone does not suffice. Nothing crozier claims rests on that dispute any more:
the row's decision is `withdrawn`, so no recipe fetches it, and its golden, its
`crates/crozier-e2e/tests/e2e.rs` corpus and test, and its `just test-corpus-match` line are removed.
The replacement search — Codat's own publication, every real document the committed
arm searches name as declaring `schema.$ref:composition-index`, and those six
sources — found no document that passes all three corpus screens and reaches the
`ref_to_class` pointer walk; its record is
`docs/openapi-surface/withdrawn-witnesses/codat-assess.md`. That arm is covered
instead by the hand-written `composition-index-pointer` fixture, which is never a
corpus row.

### Row 223 withdrawn

| # | name | method | source | pinned ref | license | decision | withdrawn because |
|---:|---|---|---|---|---|---|---|
| 223 | `nexmo-conversation` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/nexmo.com/conversation/2.0.1/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | CC0-1.0 (the `APIs-guru/openapi-directory` aggregation's own `LICENSE`; the document declares no `info.license`) | withdrawn | its only grant is the aggregator's: Vonage publishes no copy of the description under any licence, and its `x-origin`, `nexmo/api-specification`, no longer exists. The Vonage (Nexmo) Conversation API 2.0.1; `$ref` pointers into a component's composition members and nested properties |

Row 223 was held to the standard row 224 was withdrawn under: an aggregation's
grant alone does not suffice. The search for Vonage's own grant found none — no
repository of the `Vonage` or `Nexmo` organisations carries the Conversation API
description, and those that carry other OpenAPI documents grant nothing for this
one. Its committed source, golden, `crates/crozier-e2e/tests/e2e.rs` corpus and test, and `just
test-corpus-match` line are removed. Every census selector it alone declared backs
no feature, and every `golden-reach.tsv` site it reached is still reached by a
remaining golden. The four behaviours only its golden executed are now carried by
the hand-written `ref-pointer-walk` fixture, which is never a corpus row. The record is
`docs/openapi-surface/withdrawn-witnesses/nexmo-conversation.md`.

OneVoice's paths are all relative `$ref`s into sibling files, which Fern leaves
unresolved without a diagnostic, so its golden is the document's types and
client wrapper only; the wrapper is what pins the auth arm.

## Rows 301–330 — the remaining-gap searches' witnesses

The search that closed the census's last open shapes registers a real-world
witness for each one a licensed, immutably pinned document Fern generates from
declares. Each byte-matches its Fern 5.20.0 golden with `unmatched: &[]`:

| # | name | the row it witnesses | status |
|---:|---|---|---|
| 301 | `ideaconsult-enanomapper` | `operation-external-docs` | ✅ byte-matched after two repairs |
| 302 | `openaire-graph` | `xml-attribute` | ✅ byte-matched after two repairs |
| 303 | `qredence-fleet-rlm` | `oneof-anyof-variant` | ✅ byte-matched after two repairs |
| 304 | `fiware-context-generator` | `oneof-anyof-variant` | ✅ byte-matched after two repairs |
| 305 | `hasura-metadata` | `oneof-anyof-variant` | ✅ byte-matched after seven repairs |
| 306 | `zoonk` | `oneof-closed-empty-object-variant` | ✅ byte-matched after four repairs |
| 308 | `yourbrand-ticketing` | `format-duration` | ✅ byte-matched after two repairs |

Each repair is pinned offline by a `tests/generation.rs` fragment of its document:
- Examples: a required enum-typed query parameter is exampled by the enum's
  first member whatever example it declares (`type`, exampled `bystudytype`, is
  `BYINVESTIGATION`), and an optional one whose declared example Fern discards
  (a number on a `type: string` parameter) is left out of the call rather than
  given its default (eNanoMapper, OpenAIRE).
- Names: `reference.md` spells a query parameter's `[]` out as `_array`
  (`property_uris[]` is `property_uris_array`), as it does a form field's
  (eNanoMapper); and a springdoc duplicate suffix joins the name it numbers
  (`getById_1` is `get_by_id1`), which also moved six of Komga's residual files
  to parity (OpenAIRE).
- Types: a 3.1 multipart part declaring `contentMediaType:
  application/octet-stream` is a file, as `format: binary` is, and a component
  union member composing an `anyOf` of its own is that union, the properties
  declared beside it unread (fleet-rlm).
- Alternatives: a union whose members all lower to `str` collapses to `str`,
  keeping the member's description, and a JSON-like success response that
  declares no schema is `typing.Any` (FIWARE). Its two GitHub Pages `$ref`s
  are pinned in `corpus-remote-ref-pins.tsv`.
- Maps: a schema declaring `additionalProperties` beside `oneOf` or `anyOf`
  is a map before it is a union, at the component, property and array-item
  level, and its null member no longer makes it optional; a map value that is
  only `additionalProperties: true` is `typing.Any`, and a `type: "null"`
  array item `Optional[Any]` (Hasura).
- Discriminators and names: a mapping value naming no component makes the
  union an alias of `typing.Any` and keeps the discriminant property; a
  discriminant is inferred from any property of the first member, not only
  `type`; a model referencing a `Config` component imports it as
  `types_config_Config`, clear of pydantic's own `Config` class;
  and a JSON document with an integer past `u64` loads through the YAML
  reader, as Fern's does (Hasura).
- Tagged unions and aliases: a map whose value is a `oneOf` of objects each
  tagging itself with a one-member `enum` is a discriminated union, as it is at
  a property; an `allOf` member that is such a `oneOf` lends the model none of
  its branches' properties; a request body component that is only `allOf` one
  `$ref` stays in the type layer as an alias, which `reference.md` documents as
  the `request`; and a `nullable` beside a response's lone `allOf` `$ref` makes
  the method return it optionally (Zoonk).
- Parameters and collisions: a query parameter whose sole `oneOf` member is a
  nullable `oneOf` of one `$ref` is that `$ref`, optional once; and a body field
  renamed for a parameter collision is sent from its renamed argument when Fern
  drops the body schema from the type layer, from the parameter's when the
  schema is also a response or a second request (YourBrand). Both were measured
  on pinned Fern over the probe in
  [`docs/fern-measurements/yourbrand-repairs/`](../../docs/fern-measurements/yourbrand-repairs/README.md)
  before crozier was repaired.

The screened documents these searches found that could not be registered are
recorded with their measured reason in each search's record: the Open Build
Service API (`opensuse.org/obs/2.10.50`, GPL-2.0, which declares
`xml.attribute` 164 times) passes `fern check` and its generate exits 0 over a
document Fern never parsed (`Failed to resolve
#/paths/~1architectures/get/responses/401`), writing an empty SDK.

## Row 309 — a security scheme declared in another document (issue #351)

A `components.securitySchemes` entry may be a Reference Object naming a scheme
in another document. Pinned Fern follows one into a document present beside
it, so a client generated from such a description keeps its credential; the
absent document is the `unresolved-reference` refusal class. The row pins the
two-file tree with `tree` records in `corpus-remote-ref-pins.tsv`:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 309 | `huatuo-node-tree` | `securityscheme-ref` across documents | ✅ byte-matched after two repairs |

The repairs: a security scheme a relative `$ref` names is resolved from that
document, following a reference inside it, and a sibling file's
`#/components/schemas/<Name>` is imported as the component it names with the
components of that file it references, rather than inlined.

## Row 310 — a required `readOnly` property on a discriminated-union member

A property both `required` and `readOnly` is server-populated, so Fern types it
`Optional` in a model; it does the same inside the variant class a member of a
discriminated union becomes. The taxonomy editor's search-filter members
declare `negated`, `language`, `inherited` and the property pair that way:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 310 | `openfoodfacts-taxonomy-editor` | `read-only` on a discriminated-union member | ✅ byte-matched after one repair |

The repair: a variant class's field is optional when its property is
`readOnly`, as a plain model's is.

## Row 311 — `$ref` members tagged by an unrequired one-value enum

A `oneOf` or `anyOf` of `$ref` members with no `discriminator`, each tagging
one property with a one-value string `enum` that `required` leaves out (what
FastAPI writes for a Pydantic `Literal["x"] = "x"` field), is a discriminated
union to Fern whatever the property is named: it generates the
`{Union}_{Variant}` classes and strips the tag from the member models. The
Qontract API tags its task results' actions on `action_type`:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 311 | `qontract-api` | `anyof-discriminated-union` over unrequired `action_type` tags | ✅ byte-matched after two repairs |

The repairs: such members discriminate under any property name, where crozier
read an unrequired tag only under the names it had met (`message_type`,
`mcp_server_type`, `name`, a `const` `type`); and a docstring example's
`from … import` names are ordered case-insensitively, as isort orders them
(`OcmGroupsCluster` before `OcmGroupUser`).

## Row 312 — a property `anyOf` holding an inline composition

A model property's `anyOf` whose member is itself an inline `oneOf` or `anyOf`
beside another non-`null` member is a union with a named member to Fern: the
member is the union `{Model}{Prop}{Ordinal}`, discriminated or not, as it is in
a component union. The OAL example's `obj3.stuff` offers an inline `oneOf`
first:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 312 | `oal-example` | `anyof-oneof-variant` at a model property | ✅ byte-matched after one repair |

The repair: a property union's member composing two or more alternatives of
its own is hoisted to `{Owner}{Prop}{Ordinal}` rather than inlined as a nested
`typing.Union`.

## Row 313 — `type: float`

`float` is not an OpenAPI type, yet Fern reads a property declared `type:
float` as a number, `float`, whatever `format` beside it says; `int`, `double`,
`int32`, `long`, `bool` and `decimal` stay unknown (`typing.Any`). The
BreizhSport catalogue declares `Article.rating` that way, beside two `type: int`
properties:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 313 | `breizhsport-catalogue` | `type: float` on a model property and an inline request-body property | ✅ byte-matched after one repair |

The repair: `type: float` is read as a `number` whose `format` no longer
narrows it, before anything else reads the document.

## Row 314 — an empty closed object as an inline success response

Fern types an object closed with `additionalProperties: false` that declares no
`properties` as `Dict[str, Any]` wherever it sits, as it does `{type:
object}`. Protoform's `DeleteBook` answers with one:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 314 | `protoform-conformance` | an empty closed object as an inline success response | ✅ byte-matched after one repair |

The repair: such an object is no inline struct to hoist, so the method returns
`typing.Dict[str, typing.Any]` rather than an empty
`…DeleteBookResponse` model.

## Row 315 — fields reaching separate reference cycles out of order

A model whose fields reach two or more separate reference cycles writes its
trailing deferred imports field by field, each cycle's members sorted, rather
than as one sorted block. The `ere-ps-app` API's models reach their
cycles in an order no sort of the members reproduces, 48 of them:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 315 | `ere-ps-app` | fields reaching two or more reference cycles out of sorted order | ✅ byte-matched after one repair |

The repair: the deferred imports follow Fern's per-field order, each name at
the first place a field reaches it, and an `update_forward_refs` call names
only the cycles its model's own references close.

## Row 316 — a required query array of named items, answering JSON

Fern's worked example passes a required query array with one sampled item
whatever its item type, unless the operation's success body is `text/*` or it
takes a required object or map query parameter beside the array; then it leaves
every required query array out. The registered goldens held the omitting sides
only (`amazonaws.com-cloudformation`'s `text/xml` operations), where crozier's
earlier rule — leave out arrays of named items — gave the same bytes. A TypeScript
service template's `usersPatch` takes a required array of `$ref UserID` items and
answers `application/json`:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 316 | `typescript-service-template` | a required query array of `$ref` items under a JSON response | ✅ byte-matched after one repair |

The repair: the omission is keyed on the response media type and a required
object or map query parameter beside the array, as measured, rather than on the
item type (see `docs/matching.md`, *What a worked example shows*).

## Row 317 — a lower-case `authorization` header beside a bearer scheme

Fern drops an operation's header parameter only when its name is exactly the
header a declared security scheme writes: `Authorization` for a bearer, basic or
OAuth2 scheme, an apiKey scheme's own `name` otherwise. Any other spelling stays
an ordinary optional method argument, sent under the name it declares. Every
`Authorization` header parameter the corpus held before this row was spelled
exactly so, so a case-insensitive comparison matched it too:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 317 | `lootlog-battlelog` | a header parameter spelled `authorization` beside an `http: bearer` scheme | ✅ byte-matched after two repairs |

The repairs: the credential-header check compares the spelling exactly, and a
component property's nested names are re-cased across the owner/property join,
so the map value under the one-letter `f.w` properties is
`CreateBattleDtoEventsItemFwValue`.

## Row 318 — a query union naming a component string enum

A query parameter composing two or more members, none an array and one a `$ref`
to a component string enum, reaches nothing but scalars, so Fern sends its value
raw; only an array member makes it convert the value on the way out. Ego's
paginated listings declare `offset` and `limit` that way, beside the enum
`Empty` its FastAPI app writes for an unset value:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 318 | `ego-microservices` | a query union with a `$ref` member naming a component string enum and no array member | ✅ byte-matched |

The repair that made it match predates the registration: the scalar check proves
the hoisted alias scalar by resolving its members across the root and hoisted
types alike.

## Rows 319–328 — request bodies and schemaless responses

A request body's model, its JSON content-type header, a success response that
declares no schema, and a status key spelled with a suffix are each decided by
a rule Fern applies whatever else a document says; each row below declares one
of those shapes in a combination no earlier row did, and each byte-matches its
Fern 5.20.0 golden with `unmatched: &[]`:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 319 | `millenium-falcon-challenge` | a FastAPI `Body_*` JSON body posted once, whose model Fern drops | ✅ byte-matched after one repair |
| 320 | `maximo-wxo-integration` | an inline `{}` success in an OpenAPI 3.0 document, guarded against an empty body | ✅ byte-matched after one repair |
| 321 | `mi-music` | schemaless `text/plain`, `audio/mpeg` and `video/mp4` successes; titled bodies under HTTP Basic | ✅ byte-matched after three repairs |
| 322 | `g4brym-download-manager` | a titled inline array body in a parameterless 3.0 operation | ✅ byte-matched after one repair |
| 323 | `opentosca-license-engine` | a titled inline array body and inline `{}` successes in a 3.0 document | ✅ byte-matched after two repairs |
| 324 | `chat-rest-api` | error keys spelled `404-message` and `404-file`; a text media type listed before a download | ✅ byte-matched after three repairs |
| 325 | `esp32-streamline-bridge` | schemaless `audio/wav` successes | ✅ byte-matched after one repair |
| 326 | `cphos-ai-question` | a schemaless `application/pdf` success listed before `text/markdown` | ✅ byte-matched after two repairs |
| 327 | `flask-example-heroku` | a JSON request body declaring no schema | ✅ byte-matched after one repair |
| 328 | `oip-web-api` | an empty `requestBody.description` over a body with optional fields | ✅ byte-matched after one repair |

The repairs: a single-use JSON body's model is dropped whatever its name, where
crozier kept every `Body_*` model (row 319); an unknown success body is guarded
in 3.0 as in 3.1 (rows 320, 323); a schemaless `text/*` success returns `str`
(rows 321, 324), and a schemaless `audio/*` or `video/*` one streams bytes (row 321); a titled
schema keeps the JSON content-type header under HTTP Basic security (row 321); an
inline container body's header follows its own `title` or `description`, not
the document version or its items (rows 322, 323); a response key is read by its
leading integer, so `404-message` and `404-file` both raise `NotFoundError`
(row 324); the first of a text and a download media type in a success's
content decides between `str` and a byte stream (row 324), and a Markdown media
type listed after a download leaves the download's worked example its path
arguments (row 326); a schemaless `audio/wav` or `application/pdf` success
streams bytes (rows 325, 326); and a JSON request body declaring no schema
sends nothing, where crozier dropped the whole method (row 327); and an empty
`requestBody.description` is a description, so the body keeps its JSON
content-type header (row 328).

## Row 329 — a JSON body property sharing its name with a query parameter

Where an inline JSON body property and a query parameter share a name, Fern
keeps both in the signature, renaming the body argument, and then sends the
query parameter's value under the body's key. The Waylay query API's
`execute_query` declares that collision on several properties:

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 329 | `waylay-queries` | inline JSON body properties sharing their names with query parameters | ✅ byte-matched after one repair, with the `body-query-parameter-value` departure |

The repair: crozier keeps Fern's signature and query mapping, and sends the
renamed body argument under the body key. That one substitution is the
catalogued `body-query-parameter-value` departure, a Fern defect
([evidence](../../docs/departures/evidence/body-query-parameter-value.md)),
pinned line by line in `departures-ledger.tsv`.


## Row 1200 — an inline success response that is a one-member `oneOf` of a `$ref`

Input Output's token metadata server answers
`GET /metadata/{subject}/properties/{properties}` with an inline
`oneOf: [$ref Property]`, and its metadata query answers a list whose items are
`anyOf: [$ref Property]`. Fern reads each one-member composition as the
reference itself: the method returns `Property` and the list is
`List[Property]`, with no alias of its own.

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 1200 | `offchain-metadata-tools` | an inline success response `oneOf` whose only member is a `$ref` | ✅ byte-matched after two repairs |

The repairs: `build_endpoint` returns a one-`$ref` response composition as that
reference, and `hoist_array_item_type` reads a one-`$ref` item composition the
same way. The search that found it is
[`witness-search-union-scenarios`](../../docs/openapi-surface/witness-search-union-scenarios/README.md).

## Row 1201 — a `oneOf` member that is a map of a `oneOf`

The subsloth project's media API contract declares `SubtitlesValue`, a component
`oneOf` whose second member is `{type: object, additionalProperties: {oneOf:
[a URI string, $ref SubtitleTrack, an array of SubtitleTrack]}}`: the census
conjunction `schema.oneOf>!schema.properties:non-empty&schema.type:primary=object&schema.additionalProperties>!schema.$ref&schema.oneOf:several-non-null-members`.

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 1201 | `subsloth` | a `oneOf` member that is an `object` map of an inline `oneOf` of two or more non-null members | ✅ byte-matched |

The site is a component union, which lowers through the component builder's map
member; the inline hoister's arm for the same shape is proven by the hand-written
`survey-map-value-union` fixture. The search that found it is
[`witness-search-union-scenarios`](../../docs/openapi-surface/witness-search-union-scenarios/README.md).

## Row 332 — query-array examples beside JSON bodies

The publisher's SMS description carries required query arrays and JSON request
bodies. Its whole generated tree now byte-matches the certified pair; the
request-body content-type repair removed the differences that previously
blocked this real witness. `netgsm_sms_matches_fern_output` compares it in the
deterministic corpus gate, with no unmatched files.

## Row 1600 — stream-condition halves of a publisher's FastAPI document

The PrivateGPT API (`zylon-ai/private-gpt`, Apache-2.0) is the first registered
document declaring `x-fern-streaming` with a `stream-condition` and no `format`.
Its `/v1/completions` and `/v1/chat/completions` each answer a lone
`application/json` 200 and carry a tagged FastAPI `operationId` and no
`x-fern-sdk-method-name`. The pin is the last revision before the publisher's
2026 revamp dropped the extension. It was found by the streaming witness search
([record](../../docs/openapi-surface/witness-search-streaming/README.md)).

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 1600 | `zylon-private-gpt` | a `stream-condition` without `format` over a JSON-only success; the halves named from a tagged FastAPI `operationId` | ✅ byte-matched after this row's repairs |

The repairs: the streaming half streams newline-delimited JSON (`iter_lines`,
`json.loads`) rather than buffering; it is named from the whole `operationId`
(`prompt_completion_v1completions_post_stream`) while the buffered half keeps the
operation's own name (`prompt_completion`); no worked example passes the
condition field; `reference.md` documents it after the required fields; a
docstring example whose `response = ` assignment overflows width 80 is
parenthesized as Fern's snippet formatter lays it out; and `reference.md` heads
each stream with the iterator its method returns (the
`stream-reference-return-type` departure).

## Row 2400 — an optional one-value enum part of a multipart body

The converter's `convert` operation posts a `multipart/form-data`
body whose `validate` part is an optional string enum of one value. Fern keeps
it an optional argument defaulting to `OMIT` rather than a constant, and
crozier generates the same. The witness search that found it is
[`witness-search-prove-matches`](../../docs/openapi-surface/witness-search-prove-matches/README.md).

| # | name | method | source | pinned ref | license | decision | shapes |
|---:|---|---|---|---|---|---|---|
| 2400 | `mermade-openapi-converter` | github-raw | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/mermade.org.uk/openapi-converter/1.0.0/openapi.yaml | `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | MIT (`info.license`, inside the aggregating repository's own CC0-1.0 `LICENSE`) | committed | Mike Ralphson's Swagger2OpenAPI converter (`info.x-origin` records the publisher's own `Mermade/openapi-webconverter` contract), whose `multipart/form-data` bodies carry an optional one-value string enum part, `validate: [on]` |

| # | name | the shape it witnesses | status |
|---:|---|---|---|
| 2400 | `mermade-openapi-converter` | `multipart-single-value-enum-part-kept-optional` | ✅ byte-matched with no repair of its own |
