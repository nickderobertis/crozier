# OpenAPI surface coverage — Bodies, media types and responses

This inventory was derived from the OpenAPI 3.0.4 and 3.1.1 specification's
fixed-field tables for the Request Body, Media Type, Encoding, Responses,
Response, Link and Callback Objects: one row per fixed field, in the order the
tables list them, plus one row per `components` map this region owns. The two
free-keyed maps get one row per *form* their key can take, since the
specification constrains the key rather than enumerating it — for the Media Type
Object's content map, the media-type and media-range forms of RFC 6838 and
RFC 7231 (a concrete `type/subtype`, a `+json` or `+xml` structured suffix, the
`*/*` and `type/*` ranges, a key whose every `;`-delimited segment is a
well-formed RFC 7231 `parameter=value`, and a key that is none of those), plus
the five named types a generator has to dispatch on — `multipart/*`,
`application/x-www-form-urlencoded`, `application/octet-stream`,
`text/event-stream` and `application/xml`; for the Responses Object, a literal
status code, each `1XX`–`5XX` range, and `default`. Repeating that walk, in that
order, produces the rows below.

## Scope

Request Body, Media Type, Encoding, Responses, Response, Callback and Link
objects, and `components.requestBodies`, `components.responses`,
`components.callbacks`, `components.links`. The `headers` field of a Response
and of an Encoding is this region's, while the Header Object it holds is the
`parameters` region's.

## Entries

| key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |
|---|---|---|---|---|---|---|---|
| request-body-description | both | Request Body Object.description | golden | Census `requestBody.description`: 531 declarations in 28 fixtures: `6-dot-authentiqio.appspot.com`, `apache.org`, `apache.org-airflow`, `apache.org-qakka`, `apicurio.local-registry`, `apideck.com-proxy`, `apideck.com-vault`, `appng-rest-api`, `asana.com`, `atlassian.com-jira`, `bunq.com`, `byautomata.io`, `conjur.local`, `electric-sql`, `eozilla`, `etsi.local-mec010-2_apppkgmgmt`, `free5gc-namf-communication`, `free5gc-pdu-session`, `gambitcomm.local-mimic`, `letta`, `microcks.local`, `openbanking.org.uk-account-info-openapi`, `openepcis-dpp-ready`, `openfigi.com`, `redhat.com-catalog_inventory`, `reverb.com`, `squareup.com`, and `withsecure-gdpr-subject-rights`. | | | |
| request-body-content | both | Request Body Object.content | golden | Census `requestBody.content`: 1,949 declarations in 89 fixtures; the declaring fixtures are all registered fixtures except `audience-filter`, `audience-filter-strict`, `basic-auth`, `cookie-parameters`, `digit-leading-property`, `enum-name-sanitization`, `enum-query-param`, `enum-receiver-collision`, `malformed-property-schema`, `missing-operation-id`, `operation-id-non-identifier`, `query-parameters-openapi`, `sse-streaming`, `tag-based-grouping`, `apideck.com-connector`, `apideck.com-ecommerce`, `apideck.com-ecosystem`, `apis.guru`, `axesso.de`, `bbci.co.uk`, `bintable.com`, `bungie.net`, `calorieninjas.com`, `canada-holidays.ca`, `codesearch.debian.net`, `color.pizza`, `dnd5eapi.co`, `esgenterprise.com`, `etherpad.local`, `gov.bc.ca-news`, `groundhog-day.com`, `http-toolkit`, `frankfurter`, `slurmdb-rest`, and `med-anvisa-price`. | | | |
| request-body-required | both | Request Body Object.required | golden | Census `requestBody.required`: 1,471 declarations in 70 fixtures; the declaring fixtures are all registered fixtures except `audience-filter`, `audience-filter-strict`, `basic-auth`, `bracketed-property-names`, `cookie-parameters`, `digit-leading-property`, `enum-name-sanitization`, `enum-query-param`, `enum-receiver-collision`, `malformed-property-schema`, `missing-operation-id`, `nested-core-imports`, `operation-id-non-identifier`, `query-parameters-openapi`, `recursive-types`, `sse-streaming`, `tag-based-grouping`, `apideck.com-connector`, `apideck.com-ecommerce`, `apideck.com-ecosystem`, `apis.guru`, `appwrite.io-client`, `appwrite.io-server`, `axesso.de`, `bbci.co.uk`, `bintable.com`, `box.com`, `bungie.net`, `calorieninjas.com`, `canada-holidays.ca`, `codesearch.debian.net`, `color.pizza`, `discourse.local`, `dnd5eapi.co`, `eos.local`, `esgenterprise.com`, `etherpad.local`, `gov.bc.ca-news`, `groundhog-day.com`, `amazonaws.com-cloudformation`, `openfigi.com`, `maif.local-otoroshi`, `twilio.com-twilio_voice_v1`, `reverb.com`, `http-toolkit`, `frankfurter`, `worldcoin-signup-sequencer`, `appng-rest-api`, `slurmdb-rest`, `twilio.com-twilio_messaging_v1`, `eos.local-extra-fields-forbid`, `med-anvisa-price`, `kytos-sdntrace-cp`, and `khoainats`. | | | |
| components-request-bodies | both | Components Object.requestBodies | golden | Census `components.requestBodies`: 10 declarations, one each in `6-dot-authentiqio.appspot.com`, `anchore.io`, `apache.org`, `apache.org-airflow`, `calorieninjas.com`, `exa-gate`, `netbox.dev`, `reverb.com`, `squareup.com`, and `traccar.org`. | | | |
| media-type-schema | both | Media Type Object.schema | golden | Census `mediaType.schema`: 10,025 declarations in every registered fixture except `query-parameters-openapi`, `sse-streaming`, and `calorieninjas.com` (121 fixtures). The Schema Object and its keywords are classified in the [schemas region](schemas.md). | | | |
| media-type-example | both | Media Type Object.example | golden | Census `mediaType.example`: 898 declarations in `apache.org`, `apache.org-airflow`, `apideck.com-proxy`, `apideck.com-vault`, `atlassian.com-jira`, `buildrelay`, `conjur.local`, `dnd5eapi.co`, `eozilla`, `etsi.local-mec010-2_apppkgmgmt`, `frankfurter`, `letta`, `sac-backend`, `tamoss`, and `xero.com-xero-payroll-au` (15 fixtures). | | | |
| media-type-examples | both | Media Type Object.examples | golden | Census `mediaType.examples`: 1,101 declarations in `apicurio.local-registry`, `box.com`, `buildrelay`, `canada-holidays.ca`, `electric-sql`, `eozilla`, `github.com`, `groundhog-day.com`, `microcks.local`, `portfoliooptimizer.io`, `redocly.com-museum`, `tamoss`, and `tlon-notes` (13 fixtures). The Example Object is classified in the [parameters region](parameters.md). | | | |
| encoding-object | both | Media Type Object.encoding | golden | Census `mediaType.encoding`: 16 declarations in `free5gc-namf-communication` (7) and `free5gc-pdu-session` (9). Ledger `encoding-object`: `implements (`contentType`) / discards (`headers`)`. | | | |
| media-type-concrete | both | Media Type Object content-map key | golden | Census object-model map-key walk: 10,042 declarations that name both a type and a subtype, in 121 fixtures — every registered source except `bungie.net` (which keys its content maps `*/*` alone), `calorieninjas.com` (which declares no content map at all) and `query-parameters-openapi`, whose one `application/json` key sits under an unquoted-integer status code the instrument's walk does not read (see the method notes). | | | |
| media-type-key-parameters | both | Media Type Object content-map key | golden | Census object-model map-key walk for a key whose every `;`-delimited segment is an RFC 7231 `parameter=value`: 32 declarations, all in `openbanking.org.uk-account-info-openapi` and all spelled `application/json; charset=utf-8`. Crozier's media dispatch reads content keys literally, so this is not the `application/json` that `response_schema` and `selected_json_request_media` look up by name. The corpus's one other `;`-bearing key, `anchore.io`'s `text/plain; utf-8`, carries no `=` and so is not this form; it is counted under `media-type-malformed-key` below. | | | |
| media-type-suffix-json | both | Media Type Object content-map key | golden | Census object-model map-key walk: 30 declarations in `anchore.io` (5), `apicurio.local-registry` (6), `box.com` (9), `github.com` (2), `redocly.com-museum` (3), `free5gc-pdu-session` (1), and `openepcis-dpp-ready` (4). The `free5gc-pdu-session` declaration is the key `application/+json`, which also witnesses `media-type-malformed-key` below. | | | |
| media-type-suffix-xml | both | Media Type Object content-map key | golden | Census map-key walk: 16 declarations in `atlassian.com-jira` (14), `color.pizza` (1), and `traccar.org` (1). | | | |
| xml-request | both | Request Body Object.content `application/xml` key | limitations | Census map-key walk: zero declarations across every registered source. Ledger `xml-request`: `discards`. | | | |
| xml-response | both | Response Object.content `application/xml` key | limitations | Census map-key walk: zero declarations across every registered source. Ledger `xml-response`: `discards`. | | | |
| media-type-wildcard | both | Media Type Object content-map key | golden | Census map-key walk for `*/*`: 179 declarations in `6-dot-authentiqio.appspot.com` (3), `apache.org-qakka` (1), `apicurio.local-registry` (7), `apideck.com-file-storage` (3), `apideck.com-proxy` (3), `atlassian.com-jira` (20), `bintable.com` (1), `bungie.net` (134), and `openfigi.com` (7). | | | |
| media-type-range | both | Media Type Object content-map key | gap | Census object-model map-key walk for a `type/*` range other than `*/*`: zero declarations across every registered source (the only other key holding a `*` is `eozilla`'s malformed `/*`, classified below); no `docs/fern-limitations.md` row names it. | `src/ir.rs`: 6 places — `is_binary_response` (where an `image/*` range matches its `starts_with("image/")` test), the binary-body scan in `resolve_request_body`, `reference_body_example`, `selected_json_request_media`, `request_body_ignored` and `has_dispatchable_media`; `src/emit.rs`: 1 place, the bytes-body `content-type` header in `append_request_call_args`. | A range-keyed binary request body is emitted into the raw client as `"content-type": "<range>"` verbatim, while a range-keyed JSON-ish body is dropped from the client method's signature altogether, and a range-keyed response reaches the method's return type in the types module and `reference.md` through `response_schema`'s key-agnostic first-media fallback. | FIXTURE — register a screened real-world document that declares a `type/*` range on a request body or a response, and byte-compare its Fern golden. |
| media-type-multipart | both | Media Type Object content-map key | golden | Census object-model map-key walk for `multipart/*`: 42 declarations in `form-bodies` (1), `anchore.io` (1), `appwrite.io-client` (1), `appwrite.io-server` (2), `asana.com` (1), `atlassian.com-jira` (4), `box.com` (3), `discourse.local` (1), `microcks.local` (2), `appng-rest-api` (1), `free5gc-pdu-session` (9), `letta` (3), `free5gc-namf-communication` (7), and `livepeer-ai-runner` (6). | | | |
| media-type-form-urlencoded | both | Media Type Object content-map key | golden | Census object-model map-key walk for `application/x-www-form-urlencoded`: 42 declarations in `bracketed-property-names` (1), `form-bodies` (1), `anchore.io` (1), `box.com` (3), `conjur.local` (10), `traccar.org` (1), `twilio.com-twilio_voice_v1` (12), and `twilio.com-twilio_messaging_v1` (13). | | | |
| media-type-octet-stream | both | Media Type Object content-map key | golden | Census map-key walk for `application/octet-stream`: six declarations in `exhaustive`, `apache.org-qakka`, `box.com` (2), `conjur.local`, and `github.com`. | | | |
| media-type-event-stream | both | Media Type Object content-map key | golden | Census map-key walk for `text/event-stream`: 14 declarations in `sse-streaming` (1), `maif.local-otoroshi` (1), `electric-sql` (1), `letta` (10), and `exa-gate` (1). | | | |
| media-type-malformed-key | both | Media Type Object content-map key | golden | Census object-model map-key walk: three declarations of a key RFC 6838 and RFC 7231 do not admit — `/*` (empty type) once in `eozilla`, `application/+json` (a subtype starting with `+`) once in `free5gc-pdu-session`, and `text/plain; utf-8` (a `;`-delimited segment that is not `parameter=value`, the parameter grammar requiring an `=`) once in `anchore.io`. | | | |
| encoding-content-type | both | Encoding Object.contentType | golden | Census `mediaType.encoding.contentType`: 40 reachable declarations in `free5gc-namf-communication` (18) and `free5gc-pdu-session` (22); the ledger's `encoding-object` row counts more off the raw source, for the reason the method notes give. Ledger `encoding-object`: `implements (`contentType`) / discards (`headers`)`. | | | |
| encoding-headers | both | Encoding Object.headers | golden | Census `mediaType.encoding.headers`: 24 reachable declarations in `free5gc-namf-communication` (11) and `free5gc-pdu-session` (13), the same undercount as `encoding-content-type` above. Ledger `encoding-object`: `implements (`contentType`) / discards (`headers`)`. Header Object behavior is classified in the [parameters region](parameters.md). | | | |
| encoding-style | both | Encoding Object.style | golden | Census `mediaType.encoding.style`: 40 declarations in `free5gc-namf-communication` (18) and `free5gc-pdu-session` (22), all `form`. | | | |
| encoding-explode | both | Encoding Object.explode | limitations | Census `mediaType.encoding.explode`: zero declarations across every registered source. Ledger `encoding-explode-or-allowReserved`: `refuses (multipart object `explode`) / ignores (list `explode`, `allowReserved`)`. | | | |
| encoding-allow-reserved | both | Encoding Object.allowReserved | limitations | Census `mediaType.encoding.allowReserved`: zero declarations across every registered source. Ledger `encoding-explode-or-allowReserved`: `refuses (multipart object `explode`) / ignores (list `explode`, `allowReserved`)`. | | | |
| response-status-literal | both | Responses Object status-code key | golden | Census object-model map-key walk: 15,622 literal status declarations in 116 fixtures, every registered source except `calorieninjas.com`, `free5gc-namf-communication`, `free5gc-pdu-session`, `kytos-sdntrace-cp`, `query-parameters-openapi`, `reverb.com`, `sigstore-rekor`, and `worldcoin-signup-sequencer`. Five of those eight — `free5gc-namf-communication`, `free5gc-pdu-session`, `kytos-sdntrace-cp`, `query-parameters-openapi` and `worldcoin-signup-sequencer` — do declare literal status codes, in the unquoted-integer YAML form the instrument's walk does not read (see the method notes). | | | |
| range-1XX | both | Responses Object `1XX` key | limitations | Census map-key walk: zero declarations across every registered source. Ledger `range-1XX`: `discards + supply`. | | | |
| range-2XX | both | Responses Object `2XX` key | golden | Census map-key walk: eight declarations, all in `sigstore-rekor`. | | | |
| range-3XX | both | Responses Object `3XX` key | limitations | Census map-key walk: zero declarations across every registered source. Ledger `range-3XX`: `discards`. | | | |
| range-4XX | both | Responses Object `4XX` key | limitations | Census map-key walk: zero declarations across every registered source. Ledger `range-4XX`: `discards`. | | | |
| range-5XX | both | Responses Object `5XX` key | limitations | Census map-key walk: zero declarations across every registered source. Ledger `range-5XX`: `discards`. | | | |
| response-default | both | Responses Object.default | golden | Census `operation.responses.default`: 782 declarations in `6-dot-authentiqio.appspot.com` (14), `apideck.com-accounting` (53), `apideck.com-ats` (5), `apideck.com-connector` (8), `apideck.com-crm` (40), `apideck.com-customer-support` (5), `apideck.com-ecommerce` (7), `apideck.com-file-storage` (32), `apideck.com-hris` (27), `apideck.com-issue-tracking` (15), `apideck.com-lead` (5), `apideck.com-pos` (46), `apideck.com-proxy` (6), `apideck.com-sms` (5), `apideck.com-vault` (20), `apideck.com-webhook` (9), `appng-rest-api` (3), `box.com` (260), `calorieninjas.com` (1), `free5gc-namf-communication` (12), `free5gc-pdu-session` (9), `reverb.com` (163), `sigstore-rekor` (8), and `slurmdb-rest` (29). | | | |
| response-description | both | Response Object.description | golden | Census `response.description`: 11,102 declarations in every registered fixture except `query-parameters-openapi`, `worldcoin-signup-sequencer`, and `kytos-sdntrace-cp` (121 fixtures). | | | |
| response-headers | both | Response Object.headers | golden | Census `response.headers`: 698 declarations in `apideck.com-proxy`, `apideck.com-vault`, `box.com`, `bunq.com`, `canada-holidays.ca`, `electric-sql`, `eozilla`, `esgenterprise.com`, `github.com`, `groundhog-day.com`, `microcks.local`, `openbanking.org.uk-account-info-openapi`, `openepcis-dpp-ready`, `sigstore-rekor`, and `tamoss` (15 fixtures). | | | |
| response-content | both | Response Object.content | golden | Census `response.content`: 8,018 declarations in every registered fixture except `nested-core-imports`, `query-parameters-openapi`, `recursive-types`, `calorieninjas.com`, `reverb.com`, `worldcoin-signup-sequencer`, `free5gc-namf-communication`, and `kytos-sdntrace-cp` (116 fixtures). | | | |
| response-links | both | Response Object.links | golden | Census `response.links`: 22 declarations in `apideck.com-crm` (6) and `gambitcomm.local-mimic` (16). | | | |
| components-responses | both | Components Object.responses | golden | Census `components.responses`: 39 declarations, one each in `6-dot-authentiqio.appspot.com`, `airbyte.local-config`, `apache.org`, `apache.org-airflow`, `apicurio.local-registry`, `apideck.com-accounting`, `apideck.com-ats`, `apideck.com-connector`, `apideck.com-crm`, `apideck.com-customer-support`, `apideck.com-ecommerce`, `apideck.com-ecosystem`, `apideck.com-file-storage`, `apideck.com-hris`, `apideck.com-issue-tracking`, `apideck.com-lead`, `apideck.com-pos`, `apideck.com-proxy`, `apideck.com-sms`, `apideck.com-vault`, `apideck.com-webhook`, `asana.com`, `bunq.com`, `conjur.local`, `etherpad.local`, `etsi.local-mec010-2_apppkgmgmt`, `exa-gate`, `frankfurter`, `free5gc-pdu-session`, `github.com`, `khoainats`, `med-anvisa-price`, `microcks.local`, `openbanking.org.uk-account-info-openapi`, `openepcis-dpp-ready`, `redocly.com-museum`, `sac-backend`, `sigstore-rekor`, and `tamoss`. | | | |
| link-operation-ref | both | Link Object.operationRef | golden | Census `link.operationRef`: 15 declarations in `gambitcomm.local-mimic`. | | | |
| link-operation-id | both | Link Object.operationId | golden | Census `link.operationId`: 25 declarations in `apideck.com-crm` (24) and `gambitcomm.local-mimic` (1). | | | |
| link-parameters | both | Link Object.parameters | golden | Census `link.parameters`: 40 declarations in `apideck.com-crm` (24) and `gambitcomm.local-mimic` (16). | | | |
| link-requestBody | both | Link Object.requestBody | limitations | Census `link.requestBody`: zero declarations across every registered source. Ledger `link-requestBody`: `discards + supply`. | | | |
| link-description | both | Link Object.description | limitations | Census `link.description`: zero declarations across every registered source. Ledger `link-description`: `discards`. | | | |
| link-server | both | Link Object.server | limitations | Census `link.server`: zero declarations across every registered source. Ledger `link-server`: `discards + supply`. | | | |
| components-links | both | Components Object.links | golden | Census `components.links`: four declarations, one each in `apache.org`, `apache.org-airflow`, `calorieninjas.com`, and `prometheus-x-edge-computing`. Ledger `components-links`: `discards + supply`. | | | |
| callback-runtime-expression | both | Callback Object expression key | golden | Census `operation.callbacks`: 10 Callback Objects in `eozilla` (1), `etsi.local-mec010-2_apppkgmgmt` (1), `free5gc-namf-communication` (5), `free5gc-pdu-session` (2), and `servers-webhooks` (1); the census deliberately treats each runtime-expression key as the Callback Object's free-map name rather than a field selector. | | | |
| components-callbacks | both | Components Object.callbacks | golden | Census `components.callbacks`: four declarations, one each in `apache.org`, `apache.org-airflow`, `calorieninjas.com`, and `prometheus-x-edge-computing`. | | | |

## Method notes

The measurement is `just surface-census --json`, over every registered source it
reports — the vendored half and the fetched `link-ok` half alike. Every
fixed-field row's count is a selector taken straight from that output.

The two free-keyed maps need one step more, because the selector grammar
deliberately emits no selector for a map key: the media types keying a content
map and the status codes keying a Responses Object are *names*, not fields. Both
were counted by importing `scripts/openapi-surface-census.py` and subclassing its
`Census` with two hooks over the same loader, source registry and walk — one in
`descend` recording the keys of every `MAP` of `mediaType`, one in `walk`
recording the keys of every `responses` node other than `default`. Nothing else
about the walk changes, so a key the instrument never reaches is not counted
here either.

That last clause is load-bearing. The walk skips a map key that is not a string
(`openapi-surface-census.py`: *"an unquoted status code or a numeric map key: a
name"*), and a status code written as an unquoted YAML integer — `200:` rather
than `"200":` — is exactly that, so the whole Response Object beneath it is
invisible to the census. Five registered sources write their status codes that
way: `free5gc-namf-communication`, `free5gc-pdu-session`, `kytos-sdntrace-cp`,
`query-parameters-openapi` and `worldcoin-signup-sequencer`. Every Response-side
count above is therefore a **floor** for those five, and the rows say so where it
changes which fixtures a row names. The size of the gap is visible in the
`encoding-object` row of [`../fern-limitations.md`](../fern-limitations.md),
which counted `free5gc-pdu-session`'s Encoding Objects off the raw source and
found several times what the census reaches there (22 `contentType`, 13
`headers`). No row's
*category* turns on it: re-running the same walk with that skip removed moves
counts only, and takes no selector in this region from zero declarations to any.

Every `Ledger <key>: <verdict>` citation above was read off, and is re-checked
against, one command over the ledger's own verdict table:

```
grep -oP '^\| `[A-Za-z0-9._-]+` \| [0-9]+ \| [0-9]+ \| [^|]+' docs/fern-limitations.md
```

It prints one `key | eligible | pool | verdict` line per measured key; the
lines whose key is this region's are the twelve joined above, verdict text
included, so a re-measurement that moves a verdict shows up as a diff against
this file rather than silently. The same output is why nothing
here joins on `status_code`: that key carries no verdict line — it is a row
label inside the ledger's 407/421 probe table, not a measured feature.

Counts are declaration sites in the source documents, never occurrences in a
generated tree. A `crozier sites` cell counts places that *inspect or emit* a
document's media-type key — a comparison, a prefix or suffix test, a split, or a
propagation of the key into generated bytes — and not the key-agnostic loops
that copy a content map through, nor a lookup by a literal key the feature can
never match. Category precedence is `golden`, then `limitations`, then `gap`;
applying it leaves one `gap` row in this region.
