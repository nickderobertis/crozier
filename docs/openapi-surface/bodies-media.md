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
| media-type-range | both | Media Type Object content-map key | gap | Census object-model map-key walk for a `type/*` range other than `*/*`: zero declarations across every registered source (the only other key holding a `*` is `eozilla`'s malformed `/*`, classified below); no `docs/fern-limitations.md` row names it. | `src/ir.rs`: 6 places — `is_binary_response` (where an `image/*` range matches its `starts_with("image/")` test), the binary-body scan in `resolve_request_body`, `reference_body_example`, `selected_json_request_media`, `request_body_ignored` and `has_dispatchable_media`; `src/emit.rs`: 1 place, the bytes-body `content-type` header in `append_request_call_args`. | A range-keyed binary request body is emitted into the raw client as `"content-type": "<range>"` verbatim, while a range-keyed JSON-ish body is dropped from the client method's signature altogether, and a range-keyed response reaches the method's return type in the types module and `reference.md` through `response_schema`'s key-agnostic first-media fallback. | FIXTURE — the world-wide witness search below found one, so what is short is the registration rather than the document. `gotson/komga`'s `komga/docs/openapi.json` at commit `656001eb03bf8b54ca909f3e74fe2ec1b95dac48` declares `image/*` on a response, is MIT, and Fern accepts it at the pin the corpus's provenance records — both `fern check` and a real generate at `fernapi/fern-python-sdk` 5.20.0, exit 0 each. `Feramance/Torrentarr`'s `docs/assets/openapi.json` at commit `b2b8bcec35b2d4bdb131b5bc0b326835982f6327` reaches the same bar with 6 declarations and additionally carries [`document-paths.md`](document-paths.md)'s `duplicate-normalized-paths`, so one registration would close a row in each of two regions. Register one and byte-compare its Fern golden; the outcome, the screening and the five near-misses are the `media-type-range` line of [Witness search (issue #188)](#witness-search-issue-188) below. |
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

Every `Ledger <key>: <verdict>` citation above is re-checked against the
ledger's keyed verdict table. The canonical join command is documented and
gated in [`../openapi-surface-coverage.md`](../openapi-surface-coverage.md).
Nothing here joins on `status_code`: that key carries no verdict — it is a row
label inside the ledger's 407/421 probe table, not a measured feature.

Counts are declaration sites in the source documents, never occurrences in a
generated tree. A `crozier sites` cell counts places that *inspect or emit* a
document's media-type key — a comparison, a prefix or suffix test, a split, or a
propagation of the key into generated bytes — and not the key-agnostic loops
that copy a content map through, nor a lookup by a literal key the feature can
never match. Category precedence is `golden`, then `limitations`, then `gap`;
applying it leaves one `gap` row in this region.

### Witness search (issue #188)

This region carried no witness-search subsection until this change. Its one `gap`
row, `media-type-range`, rested on a census statement about the **registered**
corpus — an object-model map-key walk reporting zero `type/*` keys other than
`*/*` across every registered source — which is a fact about that document set
and not about the world, as the row's own `settlement` cell said. This table
records what searching the world for it found, in the shape
[`security.md`](security.md#witness-search-issue-188),
[`schemas.md`](schemas.md#witness-search-issue-188),
[`parameters.md`](parameters.md#witness-search-issue-188) and
[`oas31-extensions.md`](oas31-extensions.md#witness-search-issue-188) already use,
so the region files' search tables read as one instrument rather than as separate
inventions.

Nothing in the table moves a `category` or a count on its own: the search records
what is true of the world, and registering a document records what is true of the
corpus. A row reading `witness-found` while its `settlement` above still says
`FIXTURE` is the expected state until that registration lands, not an
inconsistency.

`outcome` is one of the five words the index's [settlement rule](../openapi-surface-coverage.md#the-settlement-rule-as-amended)
defines, spelled as the other regions' subsections spell them. No row here reads
`search-incomplete`; the other four, at this region's bar, are these.
`witness-found` — a named real-world document declares the feature, at a
credential-free HTTPS URL ending `.json`, `.yaml` or `.yml`, pinned to an
immutable ref, under a redistribution-compatible license, accepted by Fern, and
under a name that is neither registered in
[`CORPUS.md`](../../tests/fixtures/CORPUS.md) nor listed DROPPED or REJECTED
there or in [`tests/fixtures/AGENTS.md`](../../tests/fixtures/AGENTS.md).
`fern-rejected` — such a document was found and Fern refuses it at the pinned ref.
`witness-blocked` — such a document was found but the corpus may not redistribute
it, or it is reachable at no immutable ref. `none-found` — every source below was
searched and no candidate was verified as declaring it.

**Reading the `fern check` cell.** Every candidate that reached screening was put
through *both* halves at the pin the corpus's own provenance records: `fern check`,
and a real `fern generate --group python-sdk --preview` against
`fernapi/fern-python-sdk` **5.20.0** — the version every
`tests/fixtures/*/expected/.crozier-fern-golden.json` records — with Fern CLI
**5.67.1** pinned in `fern.config.json` and `pydantic_config.enum_type:
python_enums`, over the workspace shape `scripts/generate-fern-fixture.sh`
scaffolds. Both halves are recorded because this repository's rejected ledger is
full of documents that pass the first and are refused by the second, so a check
alone is not an acceptance.

**The instrument, and that it can see what it is looking for.** Every count below
that reads a document rather than a search result is
`scripts/openapi-surface-census.py`'s own loader and object-model walk,
subclassed exactly as `## Method notes` above describes — one hook in `descend`
recording the keys of every `MAP` of `mediaType`, and a key counted only when it
matches ``^[A-Za-z0-9!#$%&'*+.^_`|~-]+/\*$`` and is not `*/*`. A media range is not
a literal string in every serialization a document may use, so the walk was
proved able to see one before it was trusted with a zero: over a four-document
control set written for this search, it reports `image/*` and `text/*` (and not
the sibling `*/*`) on the one that declares them, and nothing on the three that
declare only this node's other shapes. It then reports the witness below —
`gotson/komga`'s single `image/*` — out of that document's own fetched bytes.

**How each source was queried.** Seven sources, the same seven for this row, with
only the searched value changing. The row's last cell gives the exact query text
put to each and what it returned.

**Ran, or refused — and the two are never mixed.** Every source named in a row's
last cell carries one of two words. **Ran** means the source answered, and the row
records the size of what it read: how many documents or results came back, and how
many of them were examined. **Refused** means it did not answer, and the row records
what was attempted and the refusal it returned — a rate limit, an interstitial, an
outage. A refused call returned no result, so it is evidence of nothing: it is never
counted as a zero, and a row's outcome may rest only on its **ran** sources. Where a
call was refused and the same question was then put somewhere that answered, both are
recorded, because the refusal is part of what a repeat of this search will meet.

- **APIs.guru / `openapi-directory`** — searched whole rather than sampled:
  `git clone --depth 1 https://github.com/APIs-guru/openapi-directory` at
  `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, which is **4,138** documents under
  `APIs/`, every one of them loaded and censused by the walk above (4,138 read,
  0 unreadable).
- **jentic / `jentic-public-apis`** — the second complete catalogue, also read
  whole: **74,629** documents at commit
  `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743`, streamed member by member from
  `https://codeload.github.com/jentic/jentic-public-apis/tar.gz/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743`
  and censused in memory (0 unreadable). The tarball rather than a clone because
  a full clone of that catalogue is ~21 GB and this host already held one; the
  stream measures the same tree at the same commit and writes nothing.
- **Sourcegraph public code search** — the literal index, credential-free:
  `GET https://sourcegraph.com/.api/search/stream?v=V3` with
  `q=file:(openapi|swagger)\.(yaml|yml)$ content:"<range>:" count:all type:file`
  and the JSON spelling `q=file:(openapi|swagger)\.json$ content:"\"<range>\":"
  count:all type:file`. Only the literal form is used, and only single-term
  queries: the `and` co-occurrence form fails open — `(content:"{petId}" and
  content:"paths:")` returns 0 where a control must match — so it is recorded as
  unusable rather than as a zero.
- **GitHub code search** — the token-based index, through both engines `gh`
  exposes. `gh search code <term> --filename <name>` is the legacy engine, which
  does no phrase search, so its result sets are filtered afterwards by fetching
  every `(repo, path)` from `https://raw.githubusercontent.com/<repo>/HEAD/<path>`
  and censusing it. `gh api -X GET search/code -f q='"<term>" filename:<name>'`
  is the phrase-capable one, and is what the counts below come from.
- **SwaggerHub public registry** — `GET
  https://api.swaggerhub.com/specs?query=<q>&limit=20`. That search matches API
  name, description and tags rather than document content, so each query records
  its `totalCount` against the registry's own unfiltered total (`GET
  /specs?limit=1` → **802,968**), **and** the 20 returned specs are downloaded
  from their own `https://api.swaggerhub.com/apis/<owner>/<api>/<version>` URLs
  and censused.
- **Postman public API network** — `POST https://www.postman.com/_api/ws/proxy`
  with body `{"service":"search","method":"POST","path":"/search-all","body":
  {"queryIndices":["adp.api"],"queryText":"<q>","size":25,"from":0,"domain":"public"}}`;
  the row records `meta.total` per index and the top names returned. The control
  `queryText: "zzqqxxnonsense"` returns 0 in every index, so a zero here is the
  index answering rather than the call failing.
- **Vendor developer portals** — the portals this row's own feature domain
  implies. Each is fetched at a pinned commit and censused by the walk above, and
  a vendor that publishes no OpenAPI document at a reachable path is recorded as
  such.

| key | outcome | witness | immutable ref | license | fern check | sources searched and the exact query used against each |
|---|---|---|---|---|---|---|
| `media-type-range` | `witness-found` | `gotson/komga` — `komga/docs/openapi.json`, at `https://raw.githubusercontent.com/gotson/komga/656001eb03bf8b54ca909f3e74fe2ec1b95dac48/komga/docs/openapi.json`. Fetched (368,731 bytes) and censused at that exact reference: `openapi: 3.1.0`, and **1** content-map key that is a `type/*` range — `image/*`, on the `default` response of `GET /api/v1/books/{bookId}/pages/{pageNumber}` (`operationId: getBookPageByNumber`). Of this node's four rows it declares **this one only**: `openapi.paths:normalized-collision` 0, `operation.operationId:duplicate` 0, `reference.summary` 0. Komga is a deployed self-hosted media server and this is the document it ships in its own repository; the name is in neither [`CORPUS.md`](../../tests/fixtures/CORPUS.md) nor either DROPPED/REJECTED list. **A second document reaches this bar and is worth more to the corpus than a spare:** `Feramance/Torrentarr` `docs/assets/openapi.json` at commit `b2b8bcec35b2d4bdb131b5bc0b326835982f6327` (MIT, the repository's own; the document declares no `info.license`) carries **6** `image/*` response keys **and 4** declaration sites of [`document-paths.md`](document-paths.md#witness-search-issue-188)'s `duplicate-normalized-paths`, and Fern accepts it at the same pin — `fern check` exit 0 `Found 0 errors and 6 warnings`, generate exit 0, 64 `.py` files. Registering it closes a row in each of two regions, so the node that registers these should weigh it against komga rather than take the first name in this cell | commit `656001eb03bf8b54ca909f3e74fe2ec1b95dac48` | MIT — declared in the document (`info.license.name: MIT`) and as the repository's own license | **exit 0** both halves. `fern check` → `Found 0 errors and 16 warnings`; `fern generate --group python-sdk --preview` at `fernapi/fern-python-sdk` 5.20.0 → `[api]: python-sdk Found 0 errors and 16 warnings`, `fernapi/fern-python-sdk Finished.`, **330** `.py` files written, and the range-keyed response reaches the client as `client.book_pages.get_book_page_by_number(...) -> typing.Iterator[bytes]` | **Which of this row's seven sources answered, and which refused.** All seven **ran**, and each is below with the size of what it read: APIs.guru (4,138 documents read, 0 unreadable), jentic (74,629 read, 0 unreadable), Sourcegraph (10 stream queries answered, whose 88-file union contains the witness), GitHub's phrase-capable `search/code` endpoint (15 result pages and 2 controls answered, none refused, feeding a pooled fetch of 2,383 blobs of which 2,370 arrived and 2,013 censused), SwaggerHub (1 query answered, all 20 returned specs downloaded and censused), Postman (3 queries answered across all four indices) and the vendor portals (21 documents fetched at pinned commits and censused, with 3 further paths recorded as 404 rather than as zeros). Two **refusals** are on this search's record. Sourcegraph refused about a dozen requests between 10:23 and roughly 11:40 UTC on the day of the search, returning Cloudflare's `Just a moment...` HTML interstitial instead of an event stream; every Sourcegraph query below was taken after it resumed. And GitHub's *legacy* engine — `gh search code <term> --filename <name>`, a second engine over the same index rather than an eighth source — did not answer two of **this row's own** lines: `"application/*" --filename swagger.yaml` was refused with `HTTP 403: API rate limit exceeded for user ID 19440155` (request ID `A034:1DBCE7:149E9B2:4223794:6A9BEEFE`, 2026-09-05 10:29 UTC), and `"video/*" --filename openapi.yaml` was recorded as refused by that pass's own guard even though the endpoint had in fact returned results, so it too is treated as unanswered rather than as a zero. Neither is what this row rests on: both questions were re-put to the phrase-capable endpoint, which answered them with the 272 and 67 recorded below. No number below comes from a refused call. The queries, source by source: **APIs.guru:** the whole 4,138-document clone at `f04b8d0b` censused by the map-key walk → **7** documents declare a non-`*/*` range: `elevenlabs.io/1.0` (`audio/*`), `intellifi.nl/2.23.4+0.gb463b49.dirty` (`image/*`), `jellyfin.local/v1` (`audio/*`, `font/*`, `image/*`, `text/*`, `video/*`), `opensuse.org/obs/2.10.50` (`application/*`), `remove.bg/1.0.0` (`image/*`), `seldon.local/engine/0.1` (`text/*`) and `superset.apache.local/superset/v1` (`image/*`). **jentic:** the whole 74,629-document catalogue at `eb9d12a2` censused → **125** files declare one, **25** of them a vendor's primary `openapi.json` — among them `api.maptiler.com`, `api.openverse.org`, `cloudflare.com`, `elevenlabs.io`, `getcockpit.com`, `ibm.com/text-to-speech`, `idwise.com` (`image/*` and `video/*`), `jellyfin.local` (five distinct ranges), `memegen.link` and `mysql.com`. **Sourcegraph:** `file:(openapi\|swagger)\.(yaml\|yml)$ content:"image/*:" count:all type:file` → 56 matches in 35 files; `content:"text/*:"` → 15 in 8; `content:"application/*:"` → 17 in 10; `content:"audio/*:"` → 10 in 7; `content:"video/*:"` → 7 in 4; and the JSON spellings over `file:(openapi\|swagger)\.json$` — `content:"\"image/*\":"` → 86 in 39, `content:"\"text/*\":"` → 2 in 2, `content:"\"application/*\":"` → 8 in 3, `content:"\"audio/*\":"` → 7 in 6, `content:"\"video/*\":"` → 2 in 2. Their union is **88** distinct files, and it contains `github.com/gotson/komga/-/komga/docs/openapi.json` — the witness — so this source's query is shown to reach what it is looking for rather than assumed to. **GitHub:** `gh api -X GET search/code -f q='"image/*" filename:openapi.yaml'` → 448; `"text/*"` → 53; `"application/*"` → 436; `"audio/*"` → 84; `"video/*"` → 67; the same five against `filename:openapi.json` → 333, 10, 684, 46, 30; and against `filename:swagger.yaml` → 118, 9, 272, 13, 5. Every returned `(repo, path)` across this row's and the other rows' queries was fetched and censused: **2,383** distinct blobs attempted, 2,370 fetched, 2,013 parsed (24 unreadable), of which **295** declare a range. A control shows the query reaching a declarer: `q='"image/*" repo:08shiro80/komga-enhanced'` → 5, a fork of the witness. Recorded as a fact about the index rather than about the shape: `q='"image/*" filename:openapi.json repo:gotson/komga'` → **0**, so GitHub's code index does not hold the witness repository itself, only its forks. **SwaggerHub:** `GET /specs?query=image%2F*&limit=20` → `totalCount` **965** against the registry's 802,968 total, so the term discriminates; all 20 returned specs downloaded and censused → **19** of 20 declare `image/*`. Every one of the 20 is reachable only at a mutable `<owner>/<api>/<version>` reference its owner can edit in place, which blocks the lot of them before licence is even reached; 19 of the 20 also declare no `info.license` at all, the exception being `bbo12/admission/1.0.0`, which declares ISC and is blocked on the ref alone. **Postman:** `queryText: "image/*"` over `adp.api` → api **32**, every other index 0, top names `Artifacts and Container Images API`, `imageapi`, `Image API`, `animeshon.image.v1alpha1`; `queryText: "audio/*"` → api 3; `queryText: "text/*"` → api 15; the index exposes names and descriptions rather than OpenAPI documents, so it contributes counts and no censusable bytes. **Vendor portals:** this row's domain is binary-body and content-negotiation APIs, so the portals fetched at pinned commits and censused are `stripe/openapi` `openapi/spec3.yaml` `58e06a32`, `github/rest-api-description` `descriptions/api.github.com/api.github.com.yaml` `3cef12e8`, `box/box-openapi` `openapi.json` `933ec4c5`, `asana/openapi` `defs/asana_oas.yaml` `700bc9a7`, `discord/discord-api-spec` `specs/openapi.json` `e54b849b`, `openai/openai-openapi` `openapi.yaml` `b53b169f`, `Redocly/museum-openapi-example` `openapi.yaml` `2770b2b2`, `intercom/Intercom-OpenAPI` `descriptions/2.11/api.intercom.io.yaml` `3d5adcb2`, `svix/svix-webhooks` `server/openapi.json` `ee528fb2`, `webflow/openapi-spec` `openapi/v2.yml` `f6db6073`, `digitalocean/openapi` `specification/DigitalOcean-public.v2.yaml` `e3df8b79`, `Adyen/adyen-openapi` `json/CheckoutService-v71.json` `f82d1fe6`, `mongodb/openapi` `openapi/v2.json` `20d74e29`, `cohere-ai/cohere-developer-experience` `cohere-openapi.yaml` `c26cd7f4` and `kubernetes/kubernetes` `api/openapi-spec/v3/apis__apps__v1_openapi.json` `b2ec8b6f` → **0** each; `gotson/komga` `656001eb` → **1**, the witness; `apache/superset` `485008224719a7b42162429fccb4a910347c532b` → 4, `cloudflare/api-schemas` `f2df0ca7` → 2, `advplyr/audiobookshelf` `0a797ab8` → 3, `drakkan/sftpgo` `c737df6c` → 10 across five distinct ranges, and `traccar/traccar` `b15554cf` → 1, all five in the candidate ledger below. Three portal paths 404 at the references this dispatch could reach and so contribute nothing either way: `dropbox/dropbox-api-spec` `files.json`, `docker/docker-py` `docs/api.md`, and `elevenlabs/elevenlabs-docs` `fern/apis/api/openapi.json` |

#### The candidate ledger

Five documents outside the witness looked like the answer and are not, and each
is what a repeat of this search finds first. The measured counts are read out of
each document's own fetched bytes by the same map-key walk, and each row says
which of this node's four rows the document declares.

| candidate | ref | license | counted in the fetched bytes | what became of it |
|---|---|---|---|---|
| `drakkan/sftpgo` `openapi/openapi.yaml` | commit `c737df6cd42ef375bf51a2d0a04ea2b1ab9f8842` | AGPL-3.0 (the repository's own, per the GitHub API) | `media-type-range` = **10**, over five distinct ranges — `application/*`, `audio/*`, `image/*`, `text/*`, `video/*`. Of this node's other rows: collisions 0, duplicate `operationId` 0, `reference.summary` 0 | **not a witness — the licence blocks it.** It is the richest declarer found anywhere, and Fern accepts it outright: `fern check` exit 0 and `fern generate` at 5.20.0 exit 0. AGPL-3.0 is outside the Apache/MIT/BSD/CC0 set the corpus redistributes, so it is `witness-blocked` where the recorded witness is `witness-found`, and it is the document to revisit first if that set is ever widened |
| `apache/superset` `docs/static/resources/openapi.json` | commit `485008224719a7b42162429fccb4a910347c532b` | Apache-2.0 | `media-type-range` = **4**, all `image/*`. Of this node's other rows: 0 each | **not a witness — Fern refuses it.** `fern check` exit 1, `Found 4 errors and 99 warnings`, among them `Expected example to be a list. Example is: {"result":[{"id":1,"value":true}]}` three times and `Path parameter is unreferenced in endpoint: user_id.`; the 5.20.0 generate reports the same four and `fernapi/fern-python-sdk Failed.` Its APIs.guru conversion, `superset.apache.local/superset/v1`, is one of that corpus's seven declarers and is the same document |
| `traccar/traccar` `openapi.yaml` | commit `b15554cf3f9808dc462d412834896fe0634a4e0e` | Apache-2.0 (`info.license` and the repository's own) | `media-type-range` = **1**, `image/*`, `openapi: 3.1.0`. Of this node's other rows: 0 each | **not a witness — Fern refuses it.** `fern check` exit 1, `Found 2 errors and 6 warnings`: `Parameters path parameter 'type', query parameter 'type' all normalize to 'type' in generated SDKs.` and `Multiple request properties have the name type.`; the 5.20.0 generate fails on the same two. Worth naming twice over: [`CORPUS.md`](../../tests/fixtures/CORPUS.md) row 60 already registers `traccar.org`, which is APIs.guru's 5.6 conversion of the *same API* — and that registered document declares **no** range at all, which is why the census sees zero here while the vendor's own current document declares one |
| `advplyr/audiobookshelf` `docs/openapi.json` | commit `0a797ab8bee15dc3ca92d1d76155259c46dbec62` | GPL-3.0 (the repository's own, per the GitHub API) | `media-type-range` = **3**, all `image/*`. Of this node's other rows: 0 each | **not a witness — the licence blocks it,** on the same ground as `sftpgo` and one licence family along. It was not screened against Fern, because a licence outside the redistribution set settles it before Fern's verdict could matter |
| `cloudflare/api-schemas` `openapi.json` | commit `f2df0ca75c0fec9047e91a34c20dd666c2dcd1ba` | BSD-3-Clause | `media-type-range` = **2**, both `image/*`, in 24,861,364 fetched bytes. Of this node's other rows: 0 each | **not a witness here — unscreened, on this dispatch's own limit rather than on the document.** Its licence is inside the redistribution set and its ref is immutable, so it is the one candidate that could still reach `witness-found`; but `fern check` over a 24 MB document did not return inside the 900-second timeout this dispatch allowed it (exit 124), and an unfinished check is not an acceptance. Screening it needs a longer budget than a search node has, which is exactly why the recorded witness is the 368 KB document that finished |
