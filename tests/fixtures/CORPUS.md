# Canonical real-world OpenAPI corpus (issue #77)

This manifest tracks 50 real-world OpenAPI specs with redistribution-compatible license metadata. `decision` is `link-ok` when the source spec declares a permissive license, is fetched directly at refresh time, and is intentionally not vendored; generated Fern output comes from `just fixtures-generate-corpus`.

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

## Batch 2 — byte-matched (issue #77)

Ten corpora were selected as the next Fern byte-match targets, chosen for OpenAPI
shapes the prior corpora under-exercise. All are `link-ok` rows in the table above
(specs fetched, not vendored); goldens are generated with
`just fixtures-generate-corpus --only <name>` (needs Docker).

**Eight are now byte-matched byte-for-byte** — wired into `tests/e2e.rs` +
`test-corpus-match`, with every generator fix on the `src/*.rs` side (no golden edited).
**Two — `bbci.co.uk` and `canada-holidays.ca` — FAILED Fern golden generation: Fern
itself cannot emit an SDK for them, so there is no golden to match. They are dropped;
do not re-select them in a future batch.**

| name | selected for | status |
|---|---|---|
| `bbci.co.uk` | oneOf/anyOf + ~79 free-form maps | **DROPPED** — Fern golden generation failed (do not retry) |
| `gambitcomm.local-mimic` | 356 operations; maps + links | ✅ matched (112) — fixed reserved-word `del` method name |
| `dnd5eapi.co` | oneOf/anyOf/allOf + recursion | ✅ matched (263) — fixed allOf-as-map parse + recursive composition |
| `airbyte.local-config` | 102 ops / 210 schemas; format diversity | ✅ matched (284) |
| `etsi.local-mec010-2_apppkgmgmt` | `application/zip`, binary, custom formats | ✅ matched (118) |
| `apideck.com-webhook` | oneOf/anyOf + deepObject/header params | ✅ matched (88) |
| `apache.org-qakka` | `application/octet-stream` (binary) | ✅ matched (40) |
| `canada-holidays.ca` | recursive schemas + numeric enums | **DROPPED** — Fern golden generation failed (do not retry) |
| `apideck.com-vault` | spaceDelimited/deepObject params, dense anyOf | ✅ matched (124) |
| `6-dot-authentiqio.appspot.com` | `application/jwt` + wildcard media type | ✅ matched (64) — added HEAD operation generation |

## Batch 3 — selected (issue #77)

Thirteen `link-ok` corpora are approved for the next byte-match batch. All 13
passed native `fern check`; their specs are fetched locally and are not vendored.
Fern goldens are still pending Docker generation, and byte-match work begins only
after those goldens land.

| name | selected for | status |
|---|---|---|
| `apideck.com-accounting` | 53 ops / 140 schemas; anyOf, maps, deepObject, recursion | selected — Fern golden pending |
| `apideck.com-file-storage` | 32 ops / 75 schemas; binary, wildcard media, maps, deepObject | selected — Fern golden pending |
| `appwrite.io-client` | 61 ops; `multipart/form-data` | selected — Fern golden pending |
| `apideck.com-hris` | 27 ops / 87 schemas; anyOf/allOf, maps, deepObject | selected — Fern golden pending |
| `byautomata.io` | Crozier probe emits invalid Python from a slash-containing operation name; intentional generator-gap target | selected — Fern golden pending |
| `groundhog-day.com` | mutually recursive `Groundhog`/`Prediction` schemas | selected — Fern golden pending |
| `apideck.com-connector` | anyOf, recursive schema, maps, deepObject, links, `text/markdown` | selected — Fern golden pending |
| `color.pizza` | `image/svg+xml` response media | selected — Fern golden pending |
| `apideck.com-proxy` | all-inline schema surface, anyOf, wildcard media | selected — Fern golden pending |
| `apis.guru` | typed free-form maps | selected — Fern golden pending |
| `apideck.com-ecommerce` | 64 schemas; anyOf, maps, deepObject | selected — Fern golden pending |
| `apideck.com-issue-tracking` | 65 schemas; anyOf/allOf, maps, deepObject | selected — Fern golden pending |
| `bintable.com` | wildcard response media | selected — Fern golden pending |

Generate the pending Fern goldens in Docker with:

```sh
for n in \
  apideck.com-accounting \
  apideck.com-file-storage \
  appwrite.io-client \
  apideck.com-hris \
  byautomata.io \
  groundhog-day.com \
  apideck.com-connector \
  color.pizza \
  apideck.com-proxy \
  apis.guru \
  apideck.com-ecommerce \
  apideck.com-issue-tracking \
  bintable.com; do
  just fixtures-generate-corpus --only "$n" || echo "FAILED: $n"
done
```
