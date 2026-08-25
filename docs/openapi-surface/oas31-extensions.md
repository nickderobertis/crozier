# OpenAPI surface coverage — OAS 3.1 delta and vendor extensions

Classified entries for the `oas31-extensions` region, against the boundary in
`## Scope` below.

## Scope

The document-level 3.0-to-3.1 delta and every `x-` prefixed extension.

## Entries

| key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |
|---|---|---|---|---|---|---|---|
| `openapi-version-field` | both | OpenAPI Object.openapi | golden | Census `openapi.openapi`: all 124 fixtures (1 each; 124 declarations). |  |  |  |
| `openapi-version-3.0.0` | 3.0 | OpenAPI Object.openapi (`3.0.0`) | golden | Exact-patch census `openapi.openapi=3.0.0`: 6-dot-authentiqio.appspot.com, airbyte.local-config, amazonaws.com-cloudformation, amazonaws.com-cloudfront, anchore.io, apideck.com-ats, apideck.com-connector, apideck.com-customer-support, apideck.com-ecommerce, apideck.com-hris, apideck.com-issue-tracking, apideck.com-pos, apideck.com-sms, apis.guru, appwrite.io-client, appwrite.io-server, asana.com, axesso.de, bbci.co.uk, bintable.com, buildrelay, bungie.net, bunq.com, byautomata.io, calorieninjas.com, canada-holidays.ca, conjur.local, eos.local, eos.local-extra-fields-forbid, esgenterprise.com, etsi.local-mec010-2_apppkgmgmt, free5gc-namf-communication, free5gc-pdu-session, gambitcomm.local-mimic, gov.bc.ca-news, groundhog-day.com, helios-verifiable-api, http-toolkit, khoainats, kytos-sdntrace-cp, maif.local-otoroshi, med-anvisa-price, netbox.dev, openbanking.org.uk-account-info-openapi, openfigi.com, prometheus-x-edge-computing, query-parameters-openapi, redhat.com-catalog_inventory, reverb.com, squareup.com and xero.com-xero-payroll-au (1 each; 51 declarations). |  |  |  |
| `openapi-version-3.0.1` | 3.0 | OpenAPI Object.openapi (`3.0.1`) | golden | Exact-patch census `openapi.openapi=3.0.1`: appng-rest-api, atlassian.com-jira, auth-schemes, basic-auth, codesearch.debian.net, cookie-parameters, discriminated-unions, dnd5eapi.co, error-responses, exhaustive, form-bodies, inline-array-request, inline-request-response, integer-enums, oauth-client-credentials, portfoliooptimizer.io, schema-constraints, sigstore-rekor, sse-streaming, traccar.org, twilio.com-twilio_messaging_v1, twilio.com-twilio_voice_v1, withsecure-gdpr-subject-rights and writeonly-fields (1 each; 24 declarations). |  |  |  |
| `openapi-version-3.0.2` | 3.0 | OpenAPI Object.openapi (`3.0.2`) | golden | Exact-patch census `openapi.openapi=3.0.2`: apicurio.local-registry, box.com, corrently.io, etherpad.local and microcks.local (1 each; 5 declarations). |  |  |  |
| `openapi-version-3.0.3` | 3.0 | OpenAPI Object.openapi (`3.0.3`) | golden | Exact-patch census `openapi.openapi=3.0.3`: apache.org, apache.org-airflow, apache.org-qakka, apideck.com-accounting, apideck.com-crm, apideck.com-ecosystem, apideck.com-file-storage, apideck.com-lead, apideck.com-proxy, apideck.com-vault, apideck.com-webhook, audience-filter, audience-filter-strict, bracketed-property-names, client-class-name, color.pizza, digit-leading-property, enum-name-sanitization, enum-query-param, enum-receiver-collision, eozilla, github.com, missing-operation-id, nested-core-imports, nimisampo, operation-id-non-identifier, pydantic-extra-fields, recursive-types, sac-backend, slurmdb-rest and tag-based-grouping (1 each; 31 declarations). |  |  |  |
| `openapi-version-3.0.4` | 3.0 | OpenAPI Object.openapi (`3.0.4`) | gap | Exact-patch census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | `src/openapi.rs` (3 places), `src/ir.rs` (6 places) | The generated tree or boundary error could differ if Fern treats this supported patch spelling differently. | PROBE — compare otherwise identical `3.0.3` and `3.0.4` documents through both generators. |
| `openapi-version-3.1.0` | 3.1 | OpenAPI Object.openapi (`3.1.0`) | golden | Exact-patch census `openapi.openapi=3.1.0`: discourse.local, electric-sql, exa-gate, letta, livepeer-ai-runner, malformed-property-schema, openepcis-dpp-ready, redocly.com-museum, servers-webhooks, tamoss, tlon-notes and worldcoin-signup-sequencer (1 each; 12 declarations). |  |  |  |
| `openapi-version-3.1.1` | 3.1 | OpenAPI Object.openapi (`3.1.1`) | gap | Exact-patch census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | `src/openapi.rs` (3 places), `src/ir.rs` (6 places) | The generated tree or boundary error could differ if Fern treats this supported patch spelling differently. | PROBE — compare otherwise identical `3.1.0` and `3.1.1` documents through both generators. |
| `openapi-version-3.1.2` | 3.1 | OpenAPI Object.openapi (`3.1.2`) | golden | Exact-patch census `openapi.openapi=3.1.2`: frankfurter (1); 1 declaration. |  |  |  |
| `json-schema-dialect` | 3.1 | OpenAPI Object.jsonSchemaDialect | gap | Census `openapi.jsonSchemaDialect`: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | Generated model types could change if Fern applies the selected JSON Schema dialect and crozier does not. | PROBE — compare a dialect-sensitive Schema Object under an explicit document dialect with a no-dialect control. |
| `webhooks` | 3.1 | OpenAPI Object.webhooks | golden | Census `openapi.webhooks`: redocly.com-museum (1), servers-webhooks (1), tamoss (1); 3 declarations. |  |  |  |
| `info-summary` | 3.1 | Info Object.summary | golden | Census `info.summary`: openepcis-dpp-ready (1); 1 declaration. |  |  |  |
| `license-identifier` | 3.1 | License Object.identifier | golden | Census `info.license.identifier`: worldcoin-signup-sequencer (1); 1 declaration. |  |  |  |
| `components-pathItems` | 3.1 | Components Object.pathItems | limitations | `fern-limitations.md` key `components-pathItems`: `discards`. |  |  |  |
| `reference-summary` | 3.1 | Reference Object.summary | gap | Census `reference.summary`: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | Generated method or model documentation could gain the referenced component's summary. | PROBE — compare a non-Schema Reference Object carrying `summary` with the same reference without the sibling. |
| `reference-description` | 3.1 | Reference Object.description | gap | Census `reference.description`: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | Generated docstrings or `reference.md` could gain the reference sibling's description. | PROBE — compare a non-Schema Reference Object carrying `description` with the same reference without the sibling. |
| `webhooks-without-paths` | 3.1 | OpenAPI Object.webhooks without paths | gap | The census join reports 3 `openapi.webhooks` declarations but `openapi.paths` in all 124 sources, hence 0 webhook documents without `paths`; no `fern-limitations.md` row names it. | `src/openapi.rs` (22 places), `src/ir.rs` (14 places), `src/refs.rs` (1 place) read `paths`; `src/ir.rs` (2 places) reads `webhooks` | The generated webhook payload model could be absent or generation could fail when no ordinary path exists. | PROBE — generate a valid 3.1 document whose only API surface is one webhook and compare the complete trees. |
| `paths-absent` | 3.1 | OpenAPI Object.paths | gap | Census `openapi.paths`: all 124 sources declare it, so 0 omit it; no `fern-limitations.md` row names omission. | `src/openapi.rs` (22 places), `src/ir.rs` (14 places), `src/refs.rs` (1 place) | The generated package could fail, be empty, or contain webhook/component-derived files when `paths` is omitted. | PROBE — compare valid 3.1 documents with only `components` and only `webhooks`, both omitting `paths`. |
| `paths-empty` | both | Paths Object (empty) | gap | The census found no source with an empty Paths Object after joining `openapi.paths` declarations to walked Path Item content; no `fern-limitations.md` row names it. | `src/openapi.rs` (22 places), `src/ir.rs` (14 places), `src/refs.rs` (1 place) | The generated package could fail or differ in its empty client and documentation scaffolding. | PROBE — compare an otherwise minimal document carrying `paths: {}` with Fern's output. |
| `extension-openapi` | both | OpenAPI Object.x-* | golden | Census: amazonaws.com-cloudformation (1), amazonaws.com-cloudfront (1), apicurio.local-registry (1), apideck.com-accounting (1), apideck.com-ats (1), apideck.com-crm (1), apideck.com-file-storage (1), apideck.com-hris (1), apideck.com-issue-tracking (1), apideck.com-lead (1), apideck.com-pos (1), apideck.com-vault (1), apis.guru (2), asana.com (1), atlassian.com-jira (2), github.com (1), reverb.com (1), sigstore-rekor (1), twilio.com-twilio_messaging_v1 (1), twilio.com-twilio_voice_v1 (1); 22 declarations. |  |  |  |
| `extension-info` | both | Info Object.x-* | golden | Census: 67 fixtures, 359 declarations: 6-dot-authentiqio.appspot.com (4), airbyte.local-config (5), amazonaws.com-cloudformation (8), amazonaws.com-cloudfront (8), anchore.io (4), apache.org (4), apache.org-airflow (4), apache.org-qakka (5), apicurio.local-registry (6), apideck.com-accounting (8), apideck.com-ats (8), apideck.com-connector (8), apideck.com-crm (8), apideck.com-customer-support (8), apideck.com-ecommerce (8), apideck.com-ecosystem (6), apideck.com-file-storage (8), apideck.com-hris (8), apideck.com-issue-tracking (8), apideck.com-lead (8), apideck.com-pos (8), apideck.com-proxy (7), apideck.com-sms (8), apideck.com-vault (8), apideck.com-webhook (8), apis.guru (5), appwrite.io-client (5), appwrite.io-server (5), asana.com (6), atlassian.com-jira (5), axesso.de (4), bbci.co.uk (7), bintable.com (4), box.com (4), bungie.net (4), bunq.com (4), byautomata.io (3), calorieninjas.com (4), canada-holidays.ca (4), codesearch.debian.net (4), color.pizza (4), conjur.local (4), corrently.io (4), discourse.local (4), dnd5eapi.co (4), eos.local (4), eos.local-extra-fields-forbid (4), esgenterprise.com (4), etherpad.local (4), etsi.local-mec010-2_apppkgmgmt (5), gambitcomm.local-mimic (5), github.com (6), gov.bc.ca-news (5), groundhog-day.com (3), maif.local-otoroshi (5), microcks.local (4), netbox.dev (4), openbanking.org.uk-account-info-openapi (5), openfigi.com (4), portfoliooptimizer.io (4), redhat.com-catalog_inventory (5), reverb.com (4), squareup.com (4), traccar.org (4), twilio.com-twilio_messaging_v1 (5), twilio.com-twilio_voice_v1 (5), xero.com-xero-payroll-au (5). |  |  |  |
| `extension-contact` | both | Contact Object.x-* | golden | Census `info.contact.x-*`: amazonaws.com-cloudformation, amazonaws.com-cloudfront, anchore.io, apache.org, apache.org-airflow, apache.org-qakka, atlassian.com-jira, box.com, bunq.com and xero.com-xero-payroll-au (1 each; 10 declarations). |  |  |  |
| `extension-license` | both | License Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary License extension. | UNREACHABLE — record that tool-specific License metadata has no language-neutral SDK meaning. |
| `extension-server` | both | Server Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Server extension. | UNREACHABLE — record that tool-specific Server metadata has no language-neutral SDK meaning. |
| `extension-server-variable` | both | Server Variable Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Server Variable extension. | UNREACHABLE — record that tool-specific Server Variable metadata has no language-neutral SDK meaning. |
| `extension-components` | both | Components Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Components extension. | UNREACHABLE — record that tool-specific component-map metadata has no language-neutral SDK meaning. |
| `extension-paths` | both | Paths Object.x-* | golden | Census `openapi.paths.x-*`: apicurio.local-registry (1); 1 declaration. |  |  |  |
| `extension-path-item` | both | Path Item Object.x-* | golden | Census `pathItem.x-*`: conjur.local (3), twilio.com-twilio_messaging_v1 (25), twilio.com-twilio_voice_v1 (17); 45 declarations. |  |  |  |
| `extension-operation` | both | Operation Object.x-* | golden | Census: amazonaws.com-cloudformation (132), anchore.io (224), apache.org (73), apache.org-airflow (73), apideck.com-accounting (124), apideck.com-ats (12), apideck.com-connector (18), apideck.com-crm (99), apideck.com-customer-support (11), apideck.com-ecommerce (20), apideck.com-file-storage (78), apideck.com-hris (70), apideck.com-issue-tracking (37), apideck.com-lead (11), apideck.com-pos (107), apideck.com-proxy (12), apideck.com-sms (11), apideck.com-vault (59), apideck.com-webhook (29), appwrite.io-client (61), appwrite.io-server (95), atlassian.com-jira (1,063), audience-filter (4), audience-filter-strict (4), box.com (395), bungie.net (19), byautomata.io (4), conjur.local (3), free5gc-namf-communication (6), free5gc-pdu-session (3), github.com (845), livepeer-ai-runner (10), portfoliooptimizer.io (83), sigstore-rekor (3), squareup.com (653), sse-streaming (1), traccar.org (25), twilio.com-twilio_messaging_v1 (45), twilio.com-twilio_voice_v1 (32), xero.com-xero-payroll-au (7); 4,561 declarations. |  |  |  |
| `extension-external-docs` | both | External Documentation Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary External Documentation extension. | UNREACHABLE — record that tool-specific documentation metadata has no language-neutral SDK meaning. |
| `extension-parameter` | both | Parameter Object.x-* | golden | Census: anchore.io (1), asana.com (35), atlassian.com-jira (53), box.com (1), github.com (21), squareup.com (95), tamoss (2); 208 declarations. |  |  |  |
| `extension-header` | both | Header Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Header extension. | UNREACHABLE — record that tool-specific Header metadata has no language-neutral SDK meaning. |
| `extension-request-body` | both | Request Body Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Request Body extension. | UNREACHABLE — record that tool-specific request metadata has no language-neutral SDK meaning. |
| `extension-media-type` | both | Media Type Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Media Type extension. | UNREACHABLE — record that tool-specific media metadata has no language-neutral SDK meaning. |
| `extension-encoding` | both | Encoding Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Encoding extension. | UNREACHABLE — record that tool-specific encoding metadata has no language-neutral SDK meaning. |
| `extension-responses` | both | Responses Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Responses extension. | UNREACHABLE — record that tool-specific response-map metadata has no language-neutral SDK meaning. |
| `extension-response` | both | Response Object.x-* | golden | Census `response.x-*`: tamoss (114); 114 declarations. |  |  |  |
| `extension-callback` | both | Callback Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Callback extension. | UNREACHABLE — record that tool-specific callback metadata has no language-neutral SDK meaning. |
| `extension-example` | both | Example Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Example extension. | UNREACHABLE — record that tool-specific example metadata has no language-neutral SDK meaning. |
| `extension-link` | both | Link Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Link extension. | UNREACHABLE — record that tool-specific link metadata has no language-neutral SDK meaning. |
| `extension-tag` | both | Tag Object.x-* | golden | Census: apideck.com-accounting (26), apideck.com-ats (12), apideck.com-connector (5), apideck.com-crm (16), apideck.com-customer-support (2), apideck.com-ecommerce (8), apideck.com-file-storage (12), apideck.com-hris (18), apideck.com-issue-tracking (10), apideck.com-lead (2), apideck.com-pos (18), apideck.com-sms (2), apideck.com-vault (4), apideck.com-webhook (1), box.com (68); 204 declarations. |  |  |  |
| `extension-schema` | both | Schema Object.x-* | golden | Census: apicurio.local-registry (13), apideck.com-accounting (276), apideck.com-ats (71), apideck.com-connector (38), apideck.com-crm (153), apideck.com-customer-support (63), apideck.com-ecommerce (122), apideck.com-file-storage (99), apideck.com-hris (138), apideck.com-issue-tracking (94), apideck.com-lead (59), apideck.com-pos (175), apideck.com-proxy (1), apideck.com-sms (33), apideck.com-vault (60), apideck.com-webhook (36), appwrite.io-client (303), appwrite.io-server (372), asana.com (38), box.com (404), bungie.net (1,152), canada-holidays.ca (3), corrently.io (1), etsi.local-mec010-2_apppkgmgmt (153), github.com (1), groundhog-day.com (7), livepeer-ai-runner (9), openbanking.org.uk-account-info-openapi (18), squareup.com (1,651), xero.com-xero-payroll-au (89); 5,632 declarations. JSON Schema keywords themselves belong to the [schemas region](schemas.md), not this row. |  |  |  |
| `extension-discriminator` | both | Discriminator Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary Discriminator extension. | UNREACHABLE — record that tool-specific discriminator metadata has no language-neutral SDK meaning. |
| `extension-xml` | both | XML Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary XML extension. | UNREACHABLE — record that tool-specific XML metadata has no language-neutral SDK meaning. |
| `extension-security-scheme` | both | Security Scheme Object.x-* | golden | Census: amazonaws.com-cloudformation (1), amazonaws.com-cloudfront (1), appwrite.io-client (2), appwrite.io-server (3); 7 declarations. |  |  |  |
| `extension-oauth-flows` | both | OAuth Flows Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary OAuth Flows extension. | UNREACHABLE — record that tool-specific flow-set metadata has no language-neutral SDK meaning. |
| `extension-oauth-flow` | both | OAuth Flow Object.x-* | gap | Census: 0 declarations across 124 sources; no `fern-limitations.md` row names it. | none | No standard generated Python artifact is defined by an arbitrary OAuth Flow extension. | UNREACHABLE — record that tool-specific flow metadata has no language-neutral SDK meaning. |
| `audience-dual-header-policy` | both | Operation Object.x-fern-audiences / x-crozier-audiences | golden | Census: audience-filter (4) and audience-filter-strict (4), split evenly across both spellings; 8 declarations demonstrate the dual-header policy for this supported extension. |  |  |  |
| `x-fern-or-crozier-ignore` | both | Operation and Schema Objects.x-fern-ignore / x-crozier-ignore | gap | Census: 0 declarations across 124 sources; `fern-limitations.md` key `x-fern-or-crozier-ignore` carries only the `supply` registrability qualifier, not a Fern-behavior verdict. | `src/openapi.rs` (10 places) | Generated operation methods and model modules could be retained or removed differently. | PROBE — compare each spelling and their precedence on both an Operation and a component Schema. |
| `codegen-request-body-name-extension` | both | Operation Object.x-codegen-request-body-name | golden | Census: portfoliooptimizer.io (83), sigstore-rekor (3), traccar.org (25); 111 declarations. |  |  |  |
| `is-beta-extension` | both | Schema Object.x-is-beta | golden | Census: squareup.com (208); 208 declarations. |  |  |  |
| `fern-streaming-extension` | both | Operation Object.x-fern-streaming | golden | Census: sse-streaming (1); 1 declaration. |  |  |  |

## Method notes

The feature list is reproducible from OAS 3.0.4 and OAS 3.1.2 — the latest
published patch of each line, and the reason the enumerated patch spellings run
`3.0.0`–`3.0.4` and `3.1.0`–`3.1.2`. Compare the OpenAPI
Object fixed-field tables to obtain the document delta; then compare the named
Object sections in specification order and record every sentence saying that the
object may be extended with Specification Extensions. Reference Objects explicitly
forbid extra properties in 3.1 and Security Requirement Objects do not grant an
extension point, so neither contributes a generic extension row. Schema Object
`x-*` fields remain here, while every JSON Schema keyword is cross-linked to the
[schemas region](schemas.md). The three compound document shapes (webhooks without
paths, absent paths, empty paths) are then added from the 3.1 OpenAPI Description
minimum-content rule. Finally, `src/openapi.rs` supplies the closed list of
extensions crozier reads and the dual-header policy.

Measurements used `just surface-census --json` over all registered sources and
targeted `--selector` checks for every delta and extension prefix. To repeat the
patch-spelling rows, run the same census object-model walk
with `Census.value_of` returning its input unchanged instead of shortening the
version to `major.minor`, and filter the resulting rows for `3.0.0` through `3.0.4`
and `3.1.0` through `3.1.2`. The `openapi.openapi=<patch>` labels in the table are
exact-reporting labels, not selectors accepted by the public grammar. This
temporary mode changes neither source discovery nor the walk; its counts sum to
the ordinary census's version-field declaration total, which is the reconciliation
check for the one-off measurement. Source-site counts are literal distinct `doc.paths`,
`doc.webhooks`, `doc.openapi`, and named extension-field reads found with `rg` in
`src/`; serde fields that are never retained are reported as `none`.

The exact-reporting journey is the census implementation executed in memory with
only its version-label normalization removed. Run it after `just surface-census`
has fetched the registered sources; it does not alter the working tree:

```sh
"$(./scripts/census-python.sh)" - --json $(for v in 3.0.0 3.0.1 3.0.2 3.0.3 3.0.4 3.1.0 3.1.1 3.1.2; do printf '%s ' --selector "openapi.openapi=$v"; done) <<'PY'
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("c", "scripts/openapi-surface-census.py")
c = importlib.util.module_from_spec(spec)
sys.modules["c"] = c
spec.loader.exec_module(c)

BaseCensus = c.Census

class ExactPatchCensus(BaseCensus):
    @staticmethod
    def value_of(selector, member):
        return str(member) if selector == "openapi.openapi" else BaseCensus.value_of(selector, member)

c.Census = ExactPatchCensus
raise SystemExit(c.main())
PY
```
