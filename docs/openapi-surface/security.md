# OpenAPI surface coverage — Security

Classified entries for the `security` region, against the boundary in
`## Scope` below.

**How this region's feature list was enumerated.** Not by reading the corpus and
writing down what it holds — that would classify only what is already covered.
The list comes off the specification, in five mechanical steps a reader can
repeat against [OAS 3.0.3](https://spec.openapis.org/oas/v3.0.3) and
[OAS 3.1.1](https://spec.openapis.org/oas/v3.1.1):

1. Take the objects this region owns from its `## Scope` row: Security Scheme,
   OAuth Flows, OAuth Flow, Security Requirement, and `components.securitySchemes`.
2. For each object, take **every row of its fixed-field table**, in both
   versions. The two tables are identical field for field, which is why no row
   here reads `3.0` and every field row reads `both`.
3. Where a field's value is drawn from a set the specification enumerates, take
   **one feature per member** — every member, with no catch-all, since a member no
   source declares is exactly what this document exists to surface — and diff
   *those* lists across the two versions; that diff is the region's only `3.1`
   row. `type` has 5 members (3.0 names four and 3.1 adds `mutualTLS`) and `in`
   has 3, both closed in the specification's own text. `scheme` is the open one:
   the specification defers to the [IANA HTTP Authentication Scheme
   Registry](https://www.iana.org/assignments/http-authschemes/http-authschemes.xhtml),
   so the member list is fetched from the registry's own machine-readable copy —
   `curl -sS https://www.iana.org/assignments/http-authschemes/authschemes.csv` —
   which names **14** schemes today: `basic`, `bearer`, `concealed`, `digest`,
   `dpop`, `gnap`, `hoba`, `mutual`, `negotiate`, `oauth`, `privatetoken`,
   `scram-sha-1`, `scram-sha-256`, `vapid`. Re-fetching the CSV is how a future
   reader picks up a scheme the registry has added since.
4. The Security Requirement Object has **no fixed fields** — its keys are scheme
   names — so its features come from the value shapes its own prose defines (a
   scheme with scopes, a scheme with an empty scope list, the empty requirement
   `{}` that makes authentication optional, an empty `security: []`, several
   requirements as alternatives, several schemes in one requirement as a
   conjunction) crossed with the **two positions** the specification allows the
   list to appear in (the OpenAPI Object's `security`, the Operation Object's
   `security`). Six shapes × two positions = twelve features. The `{}` row is the
   one whose two positions land in different categories, which is exactly why the
   cross is taken rather than assumed.
5. Drop what another region owns, cross-linking instead of duplicating — see
   *Region boundaries* under `## Method notes`.

Steps 2–4 are what makes this a walk rather than a survey: ten of the fourteen
IANA schemes, an OAuth Flows Object declaring two flows, an operation-level `{}`
and a `$ref`-valued security scheme are all features no corpus reading would have
produced, because nothing in the corpus declares them. Thirteen of the fifty rows
below are that kind of row.

## Scope

Security Scheme, OAuth Flows, OAuth Flow and Security Requirement objects, and
`components.securitySchemes`.

## Entries

| key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |
|---|---|---|---|---|---|---|---|
| `securityscheme-type-apikey` | both | `Security Scheme Object.type` = `apiKey` | golden | census `securityScheme.type=apiKey`: 30 golden-bearing sources, 45 sites — `amazonaws.com-cloudformation`, `amazonaws.com-cloudfront`, `apideck.com-accounting`, `apideck.com-ats`, `apideck.com-connector`, `apideck.com-crm`(3), `apideck.com-customer-support`, `apideck.com-ecommerce`, `apideck.com-file-storage`, `apideck.com-hris`, `apideck.com-issue-tracking`, `apideck.com-lead`(3), `apideck.com-proxy`(2), `apideck.com-sms`, `apideck.com-vault`(2), `apideck.com-webhook`, `appwrite.io-client`(3), `appwrite.io-server`(4), `auth-schemes`, `buildrelay`, `bungie.net`, `byautomata.io`, `exa-gate`, `netbox.dev`, `openepcis-dpp-ready`(3), `openfigi.com`, `portfoliooptimizer.io`, `slurmdb-rest`(2), `squareup.com`, `tlon-notes`(2) |  |  |  |
| `securityscheme-type-http` | both | `Security Scheme Object.type` = `http` | golden | census `securityScheme.type=http`: 35 golden-bearing sources, 42 sites — `airbyte.local-config`, `apache.org`(2), `apache.org-airflow`(2), `auth-schemes`(2), `basic-auth`, `client-class-name`, `cookie-parameters`, `discriminated-unions`, `error-responses`, `exa-gate`, `exhaustive`, `form-bodies`, `gambitcomm.local-mimic`, `http-toolkit`(2), `inline-array-request`, `inline-request-response`, `integer-enums`, `khoainats`, `letta`, `livepeer-ai-runner`, `maif.local-otoroshi`, `openepcis-dpp-ready`(2), `pydantic-extra-fields`, `redhat.com-catalog_inventory`, `redocly.com-museum`, `sac-backend`, `schema-constraints`, `servers-webhooks`, `sse-streaming`, `tamoss`(2), `traccar.org`, `twilio.com-twilio_messaging_v1`, `twilio.com-twilio_voice_v1`, `worldcoin-signup-sequencer`(2), `writeonly-fields` |  |  |  |
| `securityscheme-type-oauth2` | both | `Security Scheme Object.type` = `oauth2` | golden | census `securityScheme.type=oauth2`: 10 golden-bearing sources, 11 sites — `auth-schemes`, `bungie.net`, `free5gc-namf-communication`, `free5gc-pdu-session`, `microcks.local`, `oauth-client-credentials`, `openbanking.org.uk-account-info-openapi`(2), `reverb.com`, `squareup.com`, `xero.com-xero-payroll-au` |  |  |  |
| `securityscheme-type-openidconnect` | both | `Security Scheme Object.type` = `openIdConnect` | golden | census `securityScheme.type=openIdConnect`: 4 golden-bearing sources, 4 sites — `apache.org`, `apache.org-airflow`, `khoainats`, `openepcis-dpp-ready` |  |  |  |
| `mutualTLS` | 3.1 | `Security Scheme Object.type` = `mutualTLS` | limitations | `fern-limitations.md` key `mutualTLS`, verdict `discards + supply`; census `securityScheme.type=mutualTLS` reports *(declared by no registered source)* over all 124 registered sources |  |  |  |
| `securityscheme-description` | both | `Security Scheme Object.description` | golden | census `securityScheme.description`: 32 golden-bearing sources, 51 sites — `amazonaws.com-cloudformation`, `amazonaws.com-cloudfront`, `apideck.com-accounting`, `apideck.com-ats`, `apideck.com-connector`, `apideck.com-crm`(3), `apideck.com-customer-support`, `apideck.com-ecommerce`, `apideck.com-file-storage`, `apideck.com-hris`, `apideck.com-issue-tracking`, `apideck.com-lead`(3), `apideck.com-proxy`(2), `apideck.com-sms`, `apideck.com-vault`(2), `apideck.com-webhook`, `appwrite.io-client`(3), `appwrite.io-server`(4), `buildrelay`, `bungie.net`(2), `byautomata.io`, `microcks.local`, `openbanking.org.uk-account-info-openapi`(2), `openepcis-dpp-ready`(3), `portfoliooptimizer.io`, `sac-backend`, `slurmdb-rest`(2), `tamoss`(2), `tlon-notes`(2), `traccar.org`, `worldcoin-signup-sequencer`(2), `xero.com-xero-payroll-au` |  |  |  |
| `securityscheme-name` | both | `Security Scheme Object.name` (the `apiKey` parameter name) | golden | census `securityScheme.name`: 30 golden-bearing sources, 45 sites — `amazonaws.com-cloudformation`, `amazonaws.com-cloudfront`, `apideck.com-accounting`, `apideck.com-ats`, `apideck.com-connector`, `apideck.com-crm`(3), `apideck.com-customer-support`, `apideck.com-ecommerce`, `apideck.com-file-storage`, `apideck.com-hris`, `apideck.com-issue-tracking`, `apideck.com-lead`(3), `apideck.com-proxy`(2), `apideck.com-sms`, `apideck.com-vault`(2), `apideck.com-webhook`, `appwrite.io-client`(3), `appwrite.io-server`(4), `auth-schemes`, `buildrelay`, `bungie.net`, `byautomata.io`, `exa-gate`, `netbox.dev`, `openepcis-dpp-ready`(3), `openfigi.com`, `portfoliooptimizer.io`, `slurmdb-rest`(2), `squareup.com`, `tlon-notes`(2) |  |  |  |
| `apikey-header` | both | `Security Scheme Object.in` = `header` | golden | census `securityScheme.in=header`: 30 golden-bearing sources, 44 sites — `amazonaws.com-cloudformation`, `amazonaws.com-cloudfront`, `apideck.com-accounting`, `apideck.com-ats`, `apideck.com-connector`, `apideck.com-crm`(3), `apideck.com-customer-support`, `apideck.com-ecommerce`, `apideck.com-file-storage`, `apideck.com-hris`, `apideck.com-issue-tracking`, `apideck.com-lead`(3), `apideck.com-proxy`(2), `apideck.com-sms`, `apideck.com-vault`(2), `apideck.com-webhook`, `appwrite.io-client`(3), `appwrite.io-server`(4), `auth-schemes`, `buildrelay`, `bungie.net`, `byautomata.io`, `exa-gate`, `netbox.dev`, `openepcis-dpp-ready`(3), `openfigi.com`, `portfoliooptimizer.io`, `slurmdb-rest`(2), `squareup.com`, `tlon-notes`. This is the ledger's unnamed *control* row, so it joins no key |  |  |  |
| `apiKey-query` | both | `Security Scheme Object.in` = `query` | limitations | `fern-limitations.md` key `apiKey-query`, verdict `discards + supply`; census `securityScheme.in=query`: 0 golden-bearing sources. Its three registered sources — `bbci.co.uk`, `esgenterprise.com`, `etherpad.local` — are all `CORPUS.md` **DROPPED** rows with no golden |  |  |  |
| `apiKey-cookie` | both | `Security Scheme Object.in` = `cookie` | golden | census `securityScheme.in=cookie`: 1 golden-bearing sources, 1 sites — `tlon-notes`; `fern-limitations.md` key `apiKey-cookie`, verdict `discards`. `tlon-notes` pairs `eyreCookie` with a header `apiKey`, which is the ledger's *"pair one with a supported scheme"* case, so the golden pins the discard rather than the scheme |  |  |  |
| `http-basic` | both | `Security Scheme Object.scheme` = `basic` (RFC 7617) | golden | census `securityScheme.scheme=basic`: 15 golden-bearing sources, 15 sites — `apache.org`, `apache.org-airflow`, `auth-schemes`, `basic-auth`, `gambitcomm.local-mimic`, `http-toolkit`, `maif.local-otoroshi`, `openepcis-dpp-ready`, `redhat.com-catalog_inventory`, `redocly.com-museum`, `tamoss`, `traccar.org`, `twilio.com-twilio_messaging_v1`, `twilio.com-twilio_voice_v1`, `worldcoin-signup-sequencer` |  |  |  |
| `http-bearer` | both | `Security Scheme Object.scheme` = `bearer` (RFC 6750) | golden | census `securityScheme.scheme=bearer`: 25 golden-bearing sources, 25 sites — `airbyte.local-config`, `auth-schemes`, `client-class-name`, `cookie-parameters`, `discriminated-unions`, `error-responses`, `exa-gate`, `exhaustive`, `form-bodies`, `http-toolkit`, `inline-array-request`, `inline-request-response`, `integer-enums`, `khoainats`, `letta`, `livepeer-ai-runner`, `openepcis-dpp-ready`, `pydantic-extra-fields`, `sac-backend`, `schema-constraints`, `servers-webhooks`, `sse-streaming`, `tamoss`, `worldcoin-signup-sequencer`, `writeonly-fields` |  |  |  |
| `http-digest` | both | `Security Scheme Object.scheme` = `digest` (RFC 7616) | limitations | `fern-limitations.md` key `http-digest`, verdict `discards + licence`; census `securityScheme.scheme=digest` and `securityScheme.scheme=Digest` both report *(declared by no registered source)* over all 124 registered sources |  |  |  |
| `http-negotiate` | both | `Security Scheme Object.scheme` = `negotiate` (RFC 4559) | golden | census `securityScheme.scheme=negotiate`: 2 golden-bearing sources, 2 sites — `apache.org`, `apache.org-airflow` |  |  |  |
| `http-concealed` | both | `Security Scheme Object.scheme` = `concealed` (RFC 9729) | gap | census `securityScheme.scheme=concealed` and `securityScheme.scheme=Concealed` both report *(declared by no registered source)* over all 124 registered sources, both spellings asked for because the field is case-insensitive. No `fern-limitations.md` row names it — that file's only `http` `scheme` row is `http-digest`. A world-wide search for a real-world document declaring it is recorded in the `http-concealed` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `src/openapi.rs` — 1 (`HttpAuthScheme`'s `#[serde(other)]` fallback, `src/openapi.rs:219`, collapses every scheme that is not `bearer` or `basic` into `Other`) and `src/ir.rs` — 1 (the `matches!(scheme.scheme, Some(Bearer \| Basic))` predicate in `auth_model`, `src/ir.rs:370`, which never selects it) | With `concealed` unselectable, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token`, `core/client_wrapper.py` sends `Authorization: Bearer` and `reference.md` documents that signature — all of it wrong if Fern refuses the document or emits a different credential | `PROBE` — the ledger's four-dropped-schemes finding is that an importer-unsupported scheme cannot be isolated in a real-world document (alone, Fern refuses it; paired with a supported scheme, Fern generates from the other one and it leaves no trace), so no corpus row is in reach; a probe declaring `concealed` alone and then beside a supported scheme, carried through `fern check` and `fern generate`, settles it in [`../fern-limitations.md`](../fern-limitations.md) |
| `http-dpop` | both | `Security Scheme Object.scheme` = `dpop` (RFC 9449) | gap | census `securityScheme.scheme=dpop` and `securityScheme.scheme=DPoP` both report *(declared by no registered source)* over all 124 registered sources, both spellings asked for because the field is case-insensitive. No `fern-limitations.md` row names it — that file's only `http` `scheme` row is `http-digest`. A world-wide search for a real-world document declaring it is recorded in the `http-dpop` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `src/openapi.rs` — 1 (`HttpAuthScheme`'s `#[serde(other)]` fallback, `src/openapi.rs:219`, collapses every scheme that is not `bearer` or `basic` into `Other`) and `src/ir.rs` — 1 (the `matches!(scheme.scheme, Some(Bearer \| Basic))` predicate in `auth_model`, `src/ir.rs:370`, which never selects it) | With `dpop` unselectable, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token`, `core/client_wrapper.py` sends `Authorization: Bearer` and `reference.md` documents that signature — all of it wrong if Fern refuses the document or emits a different credential | `PROBE` — the ledger's four-dropped-schemes finding is that an importer-unsupported scheme cannot be isolated in a real-world document (alone, Fern refuses it; paired with a supported scheme, Fern generates from the other one and it leaves no trace), so no corpus row is in reach; a probe declaring `dpop` alone and then beside a supported scheme, carried through `fern check` and `fern generate`, settles it in [`../fern-limitations.md`](../fern-limitations.md) |
| `http-gnap` | both | `Security Scheme Object.scheme` = `gnap` (RFC 9635) | gap | census `securityScheme.scheme=gnap` and `securityScheme.scheme=GNAP` both report *(declared by no registered source)* over all 124 registered sources, both spellings asked for because the field is case-insensitive. No `fern-limitations.md` row names it — that file's only `http` `scheme` row is `http-digest`. A world-wide search for a real-world document declaring it is recorded in the `http-gnap` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `src/openapi.rs` — 1 (`HttpAuthScheme`'s `#[serde(other)]` fallback, `src/openapi.rs:219`, collapses every scheme that is not `bearer` or `basic` into `Other`) and `src/ir.rs` — 1 (the `matches!(scheme.scheme, Some(Bearer \| Basic))` predicate in `auth_model`, `src/ir.rs:370`, which never selects it) | With `gnap` unselectable, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token`, `core/client_wrapper.py` sends `Authorization: Bearer` and `reference.md` documents that signature — all of it wrong if Fern refuses the document or emits a different credential | `PROBE` — the ledger's four-dropped-schemes finding is that an importer-unsupported scheme cannot be isolated in a real-world document (alone, Fern refuses it; paired with a supported scheme, Fern generates from the other one and it leaves no trace), so no corpus row is in reach; a probe declaring `gnap` alone and then beside a supported scheme, carried through `fern check` and `fern generate`, settles it in [`../fern-limitations.md`](../fern-limitations.md) |
| `http-hoba` | both | `Security Scheme Object.scheme` = `hoba` (RFC 7486) | gap | census `securityScheme.scheme=hoba` and `securityScheme.scheme=HOBA` both report *(declared by no registered source)* over all 124 registered sources, both spellings asked for because the field is case-insensitive. No `fern-limitations.md` row names it — that file's only `http` `scheme` row is `http-digest`. A world-wide search for a real-world document declaring it is recorded in the `http-hoba` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `src/openapi.rs` — 1 (`HttpAuthScheme`'s `#[serde(other)]` fallback, `src/openapi.rs:219`, collapses every scheme that is not `bearer` or `basic` into `Other`) and `src/ir.rs` — 1 (the `matches!(scheme.scheme, Some(Bearer \| Basic))` predicate in `auth_model`, `src/ir.rs:370`, which never selects it) | With `hoba` unselectable, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token`, `core/client_wrapper.py` sends `Authorization: Bearer` and `reference.md` documents that signature — all of it wrong if Fern refuses the document or emits a different credential | `PROBE` — the ledger's four-dropped-schemes finding is that an importer-unsupported scheme cannot be isolated in a real-world document (alone, Fern refuses it; paired with a supported scheme, Fern generates from the other one and it leaves no trace), so no corpus row is in reach; a probe declaring `hoba` alone and then beside a supported scheme, carried through `fern check` and `fern generate`, settles it in [`../fern-limitations.md`](../fern-limitations.md) |
| `http-mutual` | both | `Security Scheme Object.scheme` = `mutual` (RFC 8120) | gap | census `securityScheme.scheme=mutual`: 1 registered source, `conjur.local`, and **0 golden-bearing sources** — `conjur.local` is a `CORPUS.md` **DROPPED** row; `securityScheme.scheme=Mutual` reports *(declared by no registered source)*. No `fern-limitations.md` row names it — its `mutualTLS` row is the `type` of that name, not this `scheme`. A world-wide search for a real-world document declaring it is recorded in the `http-mutual` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `src/openapi.rs` — 1 (`HttpAuthScheme`'s `#[serde(other)]` fallback, `src/openapi.rs:219`, collapses every scheme that is not `bearer` or `basic` into `Other`) and `src/ir.rs` — 1 (the `matches!(scheme.scheme, Some(Bearer \| Basic))` predicate in `auth_model`, `src/ir.rs:370`, which never selects it) | With `mutual` unselectable, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token`, `core/client_wrapper.py` sends `Authorization: Bearer` and `reference.md` documents that signature — all of it wrong if Fern refuses the document or emits a different credential | `PROBE` — the ledger's four-dropped-schemes finding is that an importer-unsupported scheme cannot be isolated in a real-world document (alone, Fern refuses it; paired with a supported scheme, Fern generates from the other one and it leaves no trace), so no corpus row is in reach (the one real-world witness, `conjur.local`, is DROPPED because Fern failed on it); a probe declaring `mutual` alone and then beside a supported scheme, carried through `fern check` and `fern generate`, settles it in [`../fern-limitations.md`](../fern-limitations.md) |
| `http-oauth` | both | `Security Scheme Object.scheme` = `oauth` (RFC 5849) | gap | census `securityScheme.scheme=oauth` and `securityScheme.scheme=OAuth` both report *(declared by no registered source)* over all 124 registered sources, both spellings asked for because the field is case-insensitive. No `fern-limitations.md` row names it — that file's only `http` `scheme` row is `http-digest`. A world-wide search for a real-world document declaring it is recorded in the `http-oauth` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `src/openapi.rs` — 1 (`HttpAuthScheme`'s `#[serde(other)]` fallback, `src/openapi.rs:219`, collapses every scheme that is not `bearer` or `basic` into `Other`) and `src/ir.rs` — 1 (the `matches!(scheme.scheme, Some(Bearer \| Basic))` predicate in `auth_model`, `src/ir.rs:370`, which never selects it) | With `oauth` unselectable, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token`, `core/client_wrapper.py` sends `Authorization: Bearer` and `reference.md` documents that signature — all of it wrong if Fern refuses the document or emits a different credential | `PROBE` — the ledger's four-dropped-schemes finding is that an importer-unsupported scheme cannot be isolated in a real-world document (alone, Fern refuses it; paired with a supported scheme, Fern generates from the other one and it leaves no trace), so no corpus row is in reach; a probe declaring `oauth` alone and then beside a supported scheme, carried through `fern check` and `fern generate`, settles it in [`../fern-limitations.md`](../fern-limitations.md) |
| `http-privatetoken` | both | `Security Scheme Object.scheme` = `privatetoken` (RFC 9577) | gap | census `securityScheme.scheme=privatetoken` and `securityScheme.scheme=PrivateToken` both report *(declared by no registered source)* over all 124 registered sources, both spellings asked for because the field is case-insensitive. No `fern-limitations.md` row names it — that file's only `http` `scheme` row is `http-digest`. A world-wide search for a real-world document declaring it is recorded in the `http-privatetoken` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `src/openapi.rs` — 1 (`HttpAuthScheme`'s `#[serde(other)]` fallback, `src/openapi.rs:219`, collapses every scheme that is not `bearer` or `basic` into `Other`) and `src/ir.rs` — 1 (the `matches!(scheme.scheme, Some(Bearer \| Basic))` predicate in `auth_model`, `src/ir.rs:370`, which never selects it) | With `privatetoken` unselectable, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token`, `core/client_wrapper.py` sends `Authorization: Bearer` and `reference.md` documents that signature — all of it wrong if Fern refuses the document or emits a different credential | `PROBE` — the ledger's four-dropped-schemes finding is that an importer-unsupported scheme cannot be isolated in a real-world document (alone, Fern refuses it; paired with a supported scheme, Fern generates from the other one and it leaves no trace), so no corpus row is in reach; a probe declaring `privatetoken` alone and then beside a supported scheme, carried through `fern check` and `fern generate`, settles it in [`../fern-limitations.md`](../fern-limitations.md) |
| `http-scram-sha-1` | both | `Security Scheme Object.scheme` = `scram-sha-1` (RFC 7804) | gap | census `securityScheme.scheme=scram-sha-1` and `securityScheme.scheme=SCRAM-SHA-1` both report *(declared by no registered source)* over all 124 registered sources, both spellings asked for because the field is case-insensitive. No `fern-limitations.md` row names it — that file's only `http` `scheme` row is `http-digest`. A world-wide search for a real-world document declaring it is recorded in the `http-scram-sha-1` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `src/openapi.rs` — 1 (`HttpAuthScheme`'s `#[serde(other)]` fallback, `src/openapi.rs:219`, collapses every scheme that is not `bearer` or `basic` into `Other`) and `src/ir.rs` — 1 (the `matches!(scheme.scheme, Some(Bearer \| Basic))` predicate in `auth_model`, `src/ir.rs:370`, which never selects it) | With `scram-sha-1` unselectable, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token`, `core/client_wrapper.py` sends `Authorization: Bearer` and `reference.md` documents that signature — all of it wrong if Fern refuses the document or emits a different credential | `PROBE` — the ledger's four-dropped-schemes finding is that an importer-unsupported scheme cannot be isolated in a real-world document (alone, Fern refuses it; paired with a supported scheme, Fern generates from the other one and it leaves no trace), so no corpus row is in reach; a probe declaring `scram-sha-1` alone and then beside a supported scheme, carried through `fern check` and `fern generate`, settles it in [`../fern-limitations.md`](../fern-limitations.md) |
| `http-scram-sha-256` | both | `Security Scheme Object.scheme` = `scram-sha-256` (RFC 7804) | gap | census `securityScheme.scheme=scram-sha-256` and `securityScheme.scheme=SCRAM-SHA-256` both report *(declared by no registered source)* over all 124 registered sources, both spellings asked for because the field is case-insensitive. No `fern-limitations.md` row names it — that file's only `http` `scheme` row is `http-digest`. A world-wide search for a real-world document declaring it is recorded in the `http-scram-sha-256` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `src/openapi.rs` — 1 (`HttpAuthScheme`'s `#[serde(other)]` fallback, `src/openapi.rs:219`, collapses every scheme that is not `bearer` or `basic` into `Other`) and `src/ir.rs` — 1 (the `matches!(scheme.scheme, Some(Bearer \| Basic))` predicate in `auth_model`, `src/ir.rs:370`, which never selects it) | With `scram-sha-256` unselectable, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token`, `core/client_wrapper.py` sends `Authorization: Bearer` and `reference.md` documents that signature — all of it wrong if Fern refuses the document or emits a different credential | `PROBE` — the ledger's four-dropped-schemes finding is that an importer-unsupported scheme cannot be isolated in a real-world document (alone, Fern refuses it; paired with a supported scheme, Fern generates from the other one and it leaves no trace), so no corpus row is in reach; a probe declaring `scram-sha-256` alone and then beside a supported scheme, carried through `fern check` and `fern generate`, settles it in [`../fern-limitations.md`](../fern-limitations.md) |
| `http-vapid` | both | `Security Scheme Object.scheme` = `vapid` (RFC 8292) | gap | census `securityScheme.scheme=vapid` and `securityScheme.scheme=vapid` both report *(declared by no registered source)* over all 124 registered sources, both spellings asked for because the field is case-insensitive. No `fern-limitations.md` row names it — that file's only `http` `scheme` row is `http-digest`. A world-wide search for a real-world document declaring it is recorded in the `http-vapid` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `src/openapi.rs` — 1 (`HttpAuthScheme`'s `#[serde(other)]` fallback, `src/openapi.rs:219`, collapses every scheme that is not `bearer` or `basic` into `Other`) and `src/ir.rs` — 1 (the `matches!(scheme.scheme, Some(Bearer \| Basic))` predicate in `auth_model`, `src/ir.rs:370`, which never selects it) | With `vapid` unselectable, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token`, `core/client_wrapper.py` sends `Authorization: Bearer` and `reference.md` documents that signature — all of it wrong if Fern refuses the document or emits a different credential | `PROBE` — the ledger's four-dropped-schemes finding is that an importer-unsupported scheme cannot be isolated in a real-world document (alone, Fern refuses it; paired with a supported scheme, Fern generates from the other one and it leaves no trace), so no corpus row is in reach; a probe declaring `vapid` alone and then beside a supported scheme, carried through `fern check` and `fern generate`, settles it in [`../fern-limitations.md`](../fern-limitations.md) |
| `securityscheme-bearerformat` | both | `Security Scheme Object.bearerFormat` | golden | census `securityScheme.bearerFormat`: 5 golden-bearing sources, 5 sites — `airbyte.local-config`, `openepcis-dpp-ready`, `sac-backend`, `tamoss`, `worldcoin-signup-sequencer` |  |  |  |
| `securityscheme-openidconnecturl` | both | `Security Scheme Object.openIdConnectUrl` | golden | census `securityScheme.openIdConnectUrl`: 4 golden-bearing sources, 4 sites — `apache.org`, `apache.org-airflow`, `khoainats`, `openepcis-dpp-ready` |  |  |  |
| `securityscheme-flows` | both | `Security Scheme Object.flows` (the OAuth Flows Object) | golden | census `securityScheme.flows`: 10 golden-bearing sources, 11 sites — `auth-schemes`, `bungie.net`, `free5gc-namf-communication`, `free5gc-pdu-session`, `microcks.local`, `oauth-client-credentials`, `openbanking.org.uk-account-info-openapi`(2), `reverb.com`, `squareup.com`, `xero.com-xero-payroll-au` |  |  |  |
| `oauth2-implicit` | both | `OAuth Flows Object.implicit` | limitations | `fern-limitations.md` key `oauth2-implicit`, verdict `supply` (a qualifier-only cell — see *Two verdict cells* below); census `securityScheme.flows.implicit` reports *(declared by no registered source)* over all 124 registered sources |  |  |  |
| `oauth2-password` | both | `OAuth Flows Object.password` | limitations | `fern-limitations.md` key `oauth2-password`, verdict `supply` (a qualifier-only cell — see *Two verdict cells* below); census `securityScheme.flows.password` reports *(declared by no registered source)* over all 124 registered sources |  |  |  |
| `oauth2-clientcredentials` | both | `OAuth Flows Object.clientCredentials` | golden | census `securityScheme.flows.clientCredentials`: 7 golden-bearing sources, 7 sites — `auth-schemes`, `free5gc-namf-communication`, `free5gc-pdu-session`, `microcks.local`, `oauth-client-credentials`, `openbanking.org.uk-account-info-openapi`, `reverb.com` |  |  |  |
| `oauth2-authorizationcode` | both | `OAuth Flows Object.authorizationCode` | golden | census `securityScheme.flows.authorizationCode`: 4 golden-bearing sources, 4 sites — `bungie.net`, `openbanking.org.uk-account-info-openapi`, `squareup.com`, `xero.com-xero-payroll-au` |  |  |  |
| `oauth2-multiple-flows` | both | `OAuth Flows Object` declaring more than one of its four flows | gap | shape read `oauthFlows:multiple-flows`: 0 of the 107 golden-bearing sources declare it — each of the 11 declared OAuth Flows Objects names exactly one flow (`clientCredentials` 7, `authorizationCode` 4) — and 0 of all 124 registered sources. No `fern-limitations.md` row names it: `oauth2-implicit` and `oauth2-password` are about a flow standing alone, not about two standing together | `src/ir.rs` — 1 place: the `authorization_code.or(client_credentials).or(implicit).or(password)` chain in `oauth_scope_enum` (`src/ir.rs:418`) | `src/<pkg>/types/oauth_scope.py`'s `OauthScope` members are read from whichever flow that chain reaches first, so a Fern that prefers a different flow emits a different member set, and `types/__init__.py` and `reference.md` move with it | `FIXTURE` — screen for a redistributable real-world document at an immutable ref whose one `oauth2` scheme declares two flows with *different* `scopes` maps (the flows must differ, or the golden cannot tell the orders apart), register it, and the byte-compare settles the precedence |
| `oauthflow-authorizationurl` | both | `OAuth Flow Object.authorizationUrl` | golden | census `securityScheme.flows.authorizationCode.authorizationUrl`: 4 golden-bearing sources, 4 sites — `bungie.net`, `openbanking.org.uk-account-info-openapi`, `squareup.com`, `xero.com-xero-payroll-au`. The field's other position, `flows.implicit`, is `oauth2-implicit`'s |  |  |  |
| `oauthflow-tokenurl` | both | `OAuth Flow Object.tokenUrl` | golden | census `securityScheme.flows.authorizationCode.tokenUrl` + `securityScheme.flows.clientCredentials.tokenUrl`: 10 distinct golden-bearing sources, 11 sites — `auth-schemes`, `bungie.net`, `free5gc-namf-communication`, `free5gc-pdu-session`, `microcks.local`, `oauth-client-credentials`, `openbanking.org.uk-account-info-openapi`(2), `reverb.com`, `squareup.com`, `xero.com-xero-payroll-au` |  |  |  |
| `oauthflow-refreshurl` | both | `OAuth Flow Object.refreshUrl` | golden | census `securityScheme.flows.clientCredentials.refreshUrl`: 1 golden-bearing sources, 1 sites — `microcks.local`. `…authorizationCode.refreshUrl` is declared once, by `asana.com`, which is **DROPPED** |  |  |  |
| `oauthflow-scopes` | both | `OAuth Flow Object.scopes` | golden | census `securityScheme.flows.authorizationCode.scopes` + `securityScheme.flows.clientCredentials.scopes`: 10 distinct golden-bearing sources, 11 sites — `auth-schemes`, `bungie.net`, `free5gc-namf-communication`, `free5gc-pdu-session`, `microcks.local`, `oauth-client-credentials`, `openbanking.org.uk-account-info-openapi`(2), `reverb.com`, `squareup.com`, `xero.com-xero-payroll-au`. Both value shapes are covered — 9 sites carry a non-empty map, and 2 (`auth-schemes`, `oauth-client-credentials`) carry the empty map the specification allows |  |  |  |
| `security-requirement-scopes-document` | both | `OpenAPI Object.security` → `Security Requirement Object`, scheme → non-empty scope list | golden | shape read `document:with-scopes`: 2 golden-bearing sources, 2 sites — `free5gc-namf-communication`, `free5gc-pdu-session` |  |  |  |
| `security-requirement-scopes-operation` | both | `Operation Object.security` → `Security Requirement Object`, scheme → non-empty scope list | golden | shape read `operation:with-scopes`: 7 golden-bearing sources, 451 sites — `bungie.net`(57), `khoainats`, `microcks.local`(32), `openbanking.org.uk-account-info-openapi`(29), `reverb.com`(108), `squareup.com`(195), `xero.com-xero-payroll-au`(29) |  |  |  |
| `security-requirement-noscopes-document` | both | `OpenAPI Object.security` → `Security Requirement Object`, scheme → `[]` | golden | shape read `document:noscopes`: 32 golden-bearing sources, 47 sites — `amazonaws.com-cloudformation`, `amazonaws.com-cloudfront`, `apideck.com-accounting`, `apideck.com-ats`, `apideck.com-connector`, `apideck.com-crm`(3), `apideck.com-customer-support`, `apideck.com-ecommerce`, `apideck.com-file-storage`, `apideck.com-hris`, `apideck.com-issue-tracking`, `apideck.com-lead`(3), `apideck.com-proxy`(2), `apideck.com-sms`, `apideck.com-vault`(2), `apideck.com-webhook`, `buildrelay`, `exa-gate`(2), `gambitcomm.local-mimic`, `letta`, `microcks.local`, `netbox.dev`, `openepcis-dpp-ready`(6), `openfigi.com`, `portfoliooptimizer.io`, `redhat.com-catalog_inventory`, `redocly.com-museum`, `sac-backend`, `slurmdb-rest`(2), `tamoss`(2), `tlon-notes`(2), `traccar.org` |  |  |  |
| `security-requirement-noscopes-operation` | both | `Operation Object.security` → `Security Requirement Object`, scheme → `[]` | golden | shape read `operation:noscopes`: 43 golden-bearing sources, 873 sites — `apideck.com-accounting`(53), `apideck.com-ats`(5), `apideck.com-connector`(8), `apideck.com-crm`(40), `apideck.com-customer-support`(5), `apideck.com-ecommerce`(7), `apideck.com-file-storage`(32), `apideck.com-hris`(27), `apideck.com-issue-tracking`(15), `apideck.com-lead`(5), `apideck.com-proxy`(6), `apideck.com-sms`(5), `apideck.com-vault`(17), `apideck.com-webhook`(9), `appwrite.io-client`(117), `appwrite.io-server`(229), `auth-schemes`(4), `basic-auth`, `client-class-name`(2), `cookie-parameters`, `discriminated-unions`, `error-responses`(2), `exa-gate`, `exhaustive`(54), `form-bodies`(2), `http-toolkit`(4), `inline-array-request`, `inline-request-response`(2), `integer-enums`, `khoainats`, `livepeer-ai-runner`(10), `maif.local-otoroshi`(101), `oauth-client-credentials`, `pydantic-extra-fields`(2), `sac-backend`(13), `schema-constraints`, `servers-webhooks`, `squareup.com`(4), `sse-streaming`, `twilio.com-twilio_messaging_v1`(45), `twilio.com-twilio_voice_v1`(32), `worldcoin-signup-sequencer`(4), `writeonly-fields` |  |  |  |
| `security-optional-requirement-document` | both | `OpenAPI Object.security` containing `{}` (authentication optional) | golden | shape read `document:optional-empty-object`: 5 golden-bearing sources, 5 sites — `airbyte.local-config`, `free5gc-namf-communication`, `free5gc-pdu-session`, `openepcis-dpp-ready`, `openfigi.com` |  |  |  |
| `security-optional-requirement-operation` | both | `Operation Object.security` containing `{}` (authentication optional for that operation) | gap | shape read `operation:optional-empty-object`: 0 of the 107 golden-bearing sources declare it. The one registered source that does, `atlassian.com-jira` (221 sites), is a `CORPUS.md` **DROPPED** row with no golden, so nothing pins it. No `fern-limitations.md` row names it — `operation-security-alternatives` is about several requirements, not about the empty one | `src/ir.rs` — 3 places: `all_operations_authenticated` (`src/ir.rs:627`), `body_response_same_ref` (`src/ir.rs:2544`) and `operation_uses_basic_auth` (`src/ir.rs:2569`), each folding `op.security` over `doc.security` and testing `!r.is_empty()` | An operation-level `{}` makes that one operation unauthenticated, which flips `all_operations_authenticated` and so decides whether the credential in `client.py`/`core/client_wrapper.py` (and its signature in `reference.md`) is required or `typing.Optional[...] = None` for the **whole** SDK | `FIXTURE` — real-world documents do declare it (`atlassian.com-jira` 221 times), so screen for one Fern can generate, register it, and the byte-compare settles whether Fern reads `{}` as opting the operation out |
| `security-empty-list-document` | both | `OpenAPI Object.security` = `[]` | golden | shape read `document:empty-list`: 5 golden-bearing sources, 5 sites — `apache.org`, `apache.org-airflow`, `apideck.com-ecosystem`, `apis.guru`, `prometheus-x-edge-computing` |  |  |  |
| `security-empty-list-operation` | both | `Operation Object.security` = `[]` (opting out of the document default) | golden | shape read `operation:empty-list`: 5 golden-bearing sources, 10 sites — `airbyte.local-config`, `apideck.com-vault`(3), `exa-gate`(3), `sac-backend`(2), `squareup.com` |  |  |  |
| `security-alternatives-document` | both | `OpenAPI Object.security` holding several Security Requirement Objects (alternatives) | golden | shape read `document:alternatives`: 7 golden-bearing sources, 7 sites — `exa-gate`, `free5gc-namf-communication`, `free5gc-pdu-session`, `openepcis-dpp-ready`, `openfigi.com`, `tamoss`, `tlon-notes` |  |  |  |
| `operation-security-alternatives` | both | `Operation Object.security` holding several Security Requirement Objects (alternatives) | golden | shape read `operation:alternatives`: 2 golden-bearing sources, 3 sites — `khoainats`, `worldcoin-signup-sequencer`(2); `fern-limitations.md` key `operation-security-alternatives`, verdict `ignores + supply` |  |  |  |
| `security-conjunction-document` | both | `OpenAPI Object.security` → one Security Requirement Object naming several schemes (conjunction) | golden | shape read `document:conjunction`: 6 golden-bearing sources, 6 sites — `apideck.com-crm`, `apideck.com-lead`, `apideck.com-proxy`, `apideck.com-vault`, `openepcis-dpp-ready`, `slurmdb-rest` |  |  |  |
| `security-conjunction-operation` | both | `Operation Object.security` → one Security Requirement Object naming several schemes (conjunction) | golden | shape read `operation:conjunction`: 2 golden-bearing sources, 151 sites — `appwrite.io-client`(56), `appwrite.io-server`(95) |  |  |  |
| `components-securityschemes` | both | `Components Object.securitySchemes` | golden | census `components.securitySchemes`: 69 golden-bearing sources, 69 sites — `airbyte.local-config`, `amazonaws.com-cloudformation`, `amazonaws.com-cloudfront`, `apache.org`, `apache.org-airflow`, `apideck.com-accounting`, `apideck.com-ats`, `apideck.com-connector`, `apideck.com-crm`, `apideck.com-customer-support`, `apideck.com-ecommerce`, `apideck.com-file-storage`, `apideck.com-hris`, `apideck.com-issue-tracking`, `apideck.com-lead`, `apideck.com-proxy`, `apideck.com-sms`, `apideck.com-vault`, `apideck.com-webhook`, `appwrite.io-client`, `appwrite.io-server`, `auth-schemes`, `basic-auth`, `buildrelay`, `bungie.net`, `byautomata.io`, `client-class-name`, `cookie-parameters`, `discriminated-unions`, `error-responses`, `exa-gate`, `exhaustive`, `form-bodies`, `free5gc-namf-communication`, `free5gc-pdu-session`, `gambitcomm.local-mimic`, `http-toolkit`, `inline-array-request`, `inline-request-response`, `integer-enums`, `khoainats`, `letta`, `livepeer-ai-runner`, `maif.local-otoroshi`, `microcks.local`, `netbox.dev`, `oauth-client-credentials`, `openbanking.org.uk-account-info-openapi`, `openepcis-dpp-ready`, `openfigi.com`, `portfoliooptimizer.io`, `pydantic-extra-fields`, `redhat.com-catalog_inventory`, `redocly.com-museum`, `reverb.com`, `sac-backend`, `schema-constraints`, `servers-webhooks`, `slurmdb-rest`, `squareup.com`, `sse-streaming`, `tamoss`, `tlon-notes`, `traccar.org`, `twilio.com-twilio_messaging_v1`, `twilio.com-twilio_voice_v1`, `worldcoin-signup-sequencer`, `writeonly-fields`, `xero.com-xero-payroll-au` |  |  |  |
| `securityscheme-ref` | both | `Components Object.securitySchemes` holding a Reference Object instead of a Security Scheme Object | gap | shape read `securityScheme:$ref`: 0 of the 107 golden-bearing sources declare it, and 0 of all 124 registered sources. No `fern-limitations.md` row names it — `pathitem-ref` and `relative-file-ref` are the Reference features that file rules on, and both are [`document-paths.md`](document-paths.md)'s. A world-wide search for a real-world document declaring it is recorded in the `securityscheme-ref` row of [Witness search (issue #188)](#witness-search-issue-188) below. | `none` — `SecurityScheme` (`src/openapi.rs:142`) declares no `$ref` field and `src/refs.rs` resolves references for `components.schemas` only, so the node deserializes to the default scheme and its `type` becomes `SecuritySchemeType::Other` | With no scheme recognised, `auth_model` falls through to `Auth::Bearer { required: false }`, so `client.py` takes an optional `token` and `core/client_wrapper.py` sends `Authorization: Bearer` — where a Fern that resolves the reference would emit the referenced scheme's credential (an `api_key` and its own header, say) | `PROBE` — 0 of 124 screened real-world documents declare it, so no corpus row is in reach; a probe declaring one `$ref`-valued scheme beside a supported one, carried through `fern check` and `fern generate`, records in [`../fern-limitations.md`](../fern-limitations.md) whether Fern resolves it |

## Method notes

### What was measured, and with what

Two instruments, and the second is the first one imported rather than a new one.

**The census, for every feature the selector grammar can name.** Run in full once,
and re-run per selector for the absences the `gap` and `limitations` rows cite:

```
just surface-census --json                                    # 407 selectors, 603390 sites, 124 sources
just surface-census --selector securityScheme.type=mutualTLS \
                    --selector securityScheme.scheme=digest \
                    --selector securityScheme.flows.implicit \
                    --selector securityScheme.flows.password
```

That second invocation prints each of the four as `(declared by no registered
source)`, which is the evidence those rows cite — the instrument reports an
absence as an absence rather than as nothing.

The fourteen IANA `scheme` rows are asked the same way, in **both spellings**: an
`auth-scheme` is case-insensitive per RFC 7235, while the census records the
literal string a document wrote, so `Digest` and `digest` are two selectors and
only asking for both proves an absence.

```sh
just surface-census $(for n in Concealed DPoP GNAP HOBA Mutual OAuth PrivateToken \
                               SCRAM-SHA-1 SCRAM-SHA-256 vapid; do
  printf ' --selector securityScheme.scheme=%s --selector securityScheme.scheme=%s' \
         "$n" "$(printf %s "$n" | tr A-Z a-z)"
done)
```

Every one of those twenty prints `(declared by no registered source)` except
`securityScheme.scheme=mutual`, which prints `conjur.local 1` — a DROPPED row, so
`http-mutual` is a `gap` all the same. Across all 124 registered sources the field
takes exactly four values, all lowercase: `basic`, `bearer`, `mutual`,
`negotiate`. Ten of the fourteen registry names are therefore `gap` rows, and each
carries its own site, artifact and settlement cells rather than sharing a
catch-all — a catch-all would have read `golden` off `negotiate` alone and hidden
nine unmeasured schemes behind it.

**The census imported, for the shapes the grammar cannot name.** A Security
Requirement Object's keys are *scheme names*, so the grammar stops at
`openapi.security` / `operation.security` and emits no selector for what the list
holds: `[]` and `[{}]` and `[{a: []}, {b: []}]` are one selector with one count.
Twelve of this file's rows are about exactly that difference, and two more
(`securityscheme-ref`, `oauth2-multiple-flows`) turn on a shape the grammar
flattens the same way. All fourteen are measured by importing the census script's
own loader and registered-source list and reading the parsed object model — never
by opening a fixture. The whole read is repeatable
from the repository root:

```sh
"$(./scripts/census-python.sh)" - <<'PY'
import collections, importlib.util, sys
from pathlib import Path
root = Path.cwd()
spec = importlib.util.spec_from_file_location("census", root / "scripts/openapi-surface-census.py")
census = importlib.util.module_from_spec(spec); sys.modules["census"] = census
spec.loader.exec_module(census)
fx = root / "tests/fixtures"
aliases = census.corpus_aliases(fx)
sources = census.registered_sources(fx, root / ".local/corpus", False)
golden = {s.fixture for s in sources if (fx / aliases.get(s.fixture, s.fixture) / "expected").is_dir()}
hits = collections.defaultdict(collections.Counter)
METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
FLOWS = ("implicit", "password", "clientCredentials", "authorizationCode")

def requirements(node, where, name):
    if not isinstance(node, list):
        return
    if not node:
        hits[where + ":empty-list"][name] += 1
        return
    if len(node) > 1:
        hits[where + ":alternatives"][name] += 1
    for req in node:
        if not isinstance(req, dict):
            continue
        if not req:
            hits[where + ":optional-empty-object"][name] += 1
            continue
        if len(req) > 1:
            hits[where + ":conjunction"][name] += 1
        for scopes in req.values():
            hits[where + (":with-scopes" if scopes else ":noscopes")][name] += 1

for source in sources:
    if source.path is None or source.fixture not in golden:
        continue
    doc = census.load_document(source.path)
    requirements(doc.get("security"), "document", source.fixture)
    for item in (doc.get("paths") or {}).values():
        if not isinstance(item, dict):
            continue
        for method, op in item.items():
            if method in METHODS and isinstance(op, dict):
                requirements(op.get("security"), "operation", source.fixture)
    for scheme in ((doc.get("components") or {}).get("securitySchemes") or {}).values():
        if not isinstance(scheme, dict):
            continue
        if "$ref" in scheme:
            hits["securityScheme:$ref"][source.fixture] += 1
        flows = scheme.get("flows")
        if isinstance(flows, dict) and len([f for f in FLOWS if f in flows]) > 1:
            hits["oauthFlows:multiple-flows"][source.fixture] += 1
KEYS = [f"{where}:{shape}"
        for where in ("document", "operation")
        for shape in ("with-scopes", "noscopes", "optional-empty-object",
                      "empty-list", "alternatives", "conjunction")]
KEYS += ["securityScheme:$ref", "oauthFlows:multiple-flows"]
for key in KEYS:  # a fixed list, so a shape no source declares prints as 0 rather than vanishing
    counts = hits[key]
    print(f"{key:34} sources={len(counts):3} sites={sum(counts.values()):5}")
PY
```

### A registered source is not always a golden

The census's 124 registered sources are **not** 124 goldens, and rule 1 of the
[category rules](../openapi-surface-coverage.md#the-category-rules) is about *a
registered golden fixture's own source document*. Seventeen registered sources
carry no committed `expected/` tree — sixteen are `CORPUS.md` **DROPPED** rows
(Fern refused or failed on them) and `calorieninjas.com` is the accepted-exception
row `AGENTS.md` names. So every count in this file is filtered to the **107
golden-bearing sources**, `tests/fixtures/<dir>/expected` being the test, with
`corpus-aliases.tsv` mapping manifest names to fixture directories.

The filter is not cosmetic: it moves rows. `apiKey-query` is declared by three
registered sources and by no golden — all three are DROPPED — so it classifies
`limitations`, matching the ledger instead of contradicting it. `http-mutual`'s
only witness is `conjur.local`, DROPPED because Fern falsely returned success on
it, so the scheme is a `gap` while its registry neighbour `http-negotiate` is
`golden` on `apache.org` and `apache.org-airflow`. `oauthflow-refreshurl` loses
`asana.com` and rests on `microcks.local`. Read unfiltered, three rows change
category outright — `apiKey-query` and `http-mutual` would claim golden coverage
no golden provides, and `security-optional-requirement-operation` would stop being
a gap on the strength of `atlassian.com-jira` — and several more would cite a
source whose Fern output does not exist.

### Two verdict cells that are qualifiers, not verdicts

`oauth2-implicit` and `oauth2-password` carry `supply` in the verdict column of
[`fern-limitations.md`](../fern-limitations.md#what-round-3-did-not-register-and-why)'s
gap table — a *qualifier* under that file's own [*How to read a
verdict*](../fern-limitations.md#how-to-read-a-verdict), which lists `supply`
beside `licence` and `pipeline` as things joined to a verdict rather than as one.
Both rows quote the ledger's cell verbatim rather than inventing the verdict it
omits. What the ledger does measure for both flows is in its auth probe table:
Fern emits `token` → `Authorization: Bearer`, required when every operation is
secured. That is an `implements`-shaped result the gap table's supply cell does
not carry, and only a probe recorded in that file can promote it.

### Region boundaries

Five surfaces touch this region and none is classified here:

- **`OpenAPI Object.security` and `Operation Object.security` as *fields***, i.e.
  whether a document declares them at all, belong to
  [`document-paths.md`](document-paths.md), which owns the OpenAPI and Operation
  objects. This region owns what the *list* holds — the Security Requirement
  Object and its value shapes — which is why its twelve requirement rows all name
  a shape and none of them names the bare field. The census measures the fields as
  `openapi.security` (48 sources) and `operation.security` (58 sources, 1748
  sites) over all 124 registered sources; those two numbers are that region's to
  classify, filter included.
- **`x-` extensions on a Security Scheme Object** belong to
  [`oas31-extensions.md`](oas31-extensions.md). The census finds two:
  `securityScheme.x-amazon-apigateway-authtype` and `securityScheme.x-appwrite`.
- **The Reference Object itself** (`$ref`, `summary`, `description`) is
  [`document-paths.md`](document-paths.md)'s. `securityscheme-ref` above is not
  that object — it is the Security Scheme *position* holding one, which only this
  region can classify.
- **`Security Scheme Object.in`** reuses the Parameter Object's `in` vocabulary
  but is its own field on its own object; `parameter.in` is
  [`parameters.md`](parameters.md)'s.
- **No JSON Schema keyword appears in this region.** OAuth `scopes` is a
  `string → string` map, not a schema, so nothing here belongs to
  [`schemas.md`](schemas.md).

### Deliberate exclusions

Enumeration step 3 takes a feature per member of a value set the specification
enumerates; it does **not** take a feature per *cardinality of a free-keyed map*.
So "a document declaring several security schemes" (24 registered sources do) and
"a document declaring two `oauth2` schemes" (`openbanking.org.uk-account-info-openapi`
does) are not rows here: the keys of `components.securitySchemes` are names, which
is the same rule that keeps them out of the census. `oauth2-multiple-flows` is a
row despite looking similar because the OAuth Flows Object's four flows are
**fixed fields**, not map keys, so declaring two of them is a shape of the object
rather than a count of names.

### One instrument artifact, found while measuring

The census reports `securityRequirement.x-api-key`, 1 site, in
`calorieninjas.com`. It is not an extension: that document names its security
scheme `x-api-key`, and a Security Requirement Object's keys are scheme names. The
walk tests a key for the `x-` prefix before it tests whether the enclosing object
keys its map by name, so a scheme whose name starts with `x-` is recorded as a
vendor extension of the requirement. No row in this file rests on it — the
requirement rows are measured by the shape read above, not by that selector — and
the source is a golden-less accepted-exception row either way. Fixing it belongs
to `scripts/openapi-surface-census.py`, not to this file.

### What this region could not settle

`etherpad.local` and `appng-rest-api` each declare a **sole** `apiKey` scheme in
`query` and `cookie` respectively, with a document-level `security` that secures
every operation — precisely the two rows
[`fern-limitations.md`](../fern-limitations.md#the-importer-drops-four-security-schemes-outright)
measured as `fern check` **exit 1**. Both are DROPPED in `CORPUS.md`, and
`etherpad.local`'s reason is recorded as a *check* failure with five fatal
diagnostics, which is consistent. Whether the sole-scheme refusal is what dropped
them is not settled here: settling it means running Fern, which this pass does
not do.

### Witness search (issue #188)

Ten of this region's eleven `PROBE` rows are IANA `scheme` members whose
`settlement` cells rest on the ledger's four-dropped-schemes finding. That
finding is a claim about **Fern** — an importer-unsupported scheme cannot be
isolated, because alone Fern refuses the document and paired with a supported
scheme it leaves no trace in the output. It is not a claim about whether any
real-world document *declares* the scheme, and this table answers only the
second question: for each row, was a document found in the world that declares
the feature, and what is true of that document.

Nothing here moves a `category`, a `settlement` or a count; the reclassification
that follows is a separate change. **A row below reading `witness-found` beside a
`settlement` of `PROBE` in the entry table is therefore the expected intermediate
state and not an inconsistency** — the search records what is true of the world,
and the reclassification records what is true of the corpus.

`outcome` is one of four words. `witness-found` — a named real-world document
declares the feature, at a credential-free HTTPS URL ending `.json`, `.yaml` or
`.yml` (the direct-spec-URL rule [`fern-goldens.md`](../fern-goldens.md) states),
pinned to an immutable ref, under a redistribution-compatible license, accepted
by `fern check`, and under a name that is neither registered in
[`CORPUS.md`](../../tests/fixtures/CORPUS.md) nor listed DROPPED or REJECTED
there or in [`tests/fixtures/AGENTS.md`](../../tests/fixtures/AGENTS.md).
`fern-rejected` — all of that, and Fern refuses the raw document. `witness-blocked`
— a document declares it and can be recorded as neither, for the reason the row
names. `none-found` — every source below was searched and no candidate was
verified as declaring it. Each row records the **best** outcome its whole
candidate set reached, names the document it is recorded on, and names the other
candidates and what became of each.

**Reading the `fern check` cell.** Fern's exit code is not by itself its verdict:
on three of the `securityscheme-ref` candidates it printed `Failed to parse
openapi document` and a `CliError` out of `resolveSecuritySchemeReference`, then
printed `All checks passed` and exited 0 — the same false success `CORPUS.md`
records against `conjur.local` and `dapr`. A document Fern failed to parse is not
a document Fern accepted, so those rows read `fern-rejected` and the cell carries
both what Fern printed and the exit code. Every check ran the local `fern` CLI
against the workspace shape `scripts/generate-fern-fixture.sh` scaffolds — CLI
`5.67.1` pinned in `fern.config.json`, `fernapi/fern-python-sdk` `5.20.0`,
`pydantic_config.enum_type: python_enums` — over the document fetched at the ref
the row names.

**How each source was queried.** Six sources, the same six for every row, with
only the searched value changing. Each row's last cell gives the exact query text
with that value substituted, and the count it returned.

* **APIs.guru / `openapi-directory`** — searched whole rather than sampled:
  `git clone --depth 1 https://github.com/APIs-guru/openapi-directory` at
  `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, which is **4,138** spec documents
  under 701 provider directories, then one `grep -rilE` per row over `APIs/`.
* **GitHub code search** — `gh search code <value> --filename openapi.yaml`, then
  `--filename openapi.json`, then `--filename swagger.yaml`. Two forms were tried
  first and are recorded because they mislead: `gh api -X GET search/code -f
  q='dpop path:openapi.yaml'` returned **HTTP 403** *"API rate limit exceeded for
  user ID …"* at 19:39 UTC while `gh api rate_limit` reported `code_search` 10/10
  and `search` 30/30 remaining — the secondary limiter, which no polling waits
  out — and `gh search code securitySchemes path:openapi.yaml` returns `[]` where
  `gh search code securitySchemes --filename openapi.yaml` returns hits, so the
  `path:` qualifier is not honoured through that API. The engine behind `gh` is
  also the legacy one, which does not do phrase search, so the searched term is
  the bare scheme value and the result set is filtered **afterwards**: all
  **726** distinct `(repo, path)` results across the 30 queries were fetched from
  `https://raw.githubusercontent.com/<repo>/HEAD/<path>` and grepped with the same
  regex, so each row's GitHub count is read out of documents rather than out of a
  result snippet. Queries ran one per 20s and none was refused.
* **Sourcegraph public code search** — a second credential-free index over the
  same file names: `GET https://sourcegraph.com/.api/search/stream?v=V3` with
  `q=file:(openapi|swagger)\.(yaml|yml|json) content:"scheme: <value>" count:100`
  and the JSON spelling `content:"\"scheme\": \"<value>\""`. Only the literal form
  is used: its regexp forms fail open, returning 0 even for a control
  (`content:/scheme:\s*bearer/` → 0 where `content:"scheme: bearer"` → 100).
* **SwaggerHub public registry** — `GET
  https://api.swaggerhub.com/specs?query=<value>&limit=20`. That search matches
  API name, description and tags rather than document content (`query=petstore` →
  129,570, `query=zzqqxxnonsense` → 0), so a row records the count it returned and
  the top names, **and** the top 20 returned documents were fetched from their own
  `X-Swagger` URLs and grepped.
* **Postman public API network** — `POST https://www.postman.com/_api/ws/proxy`
  with body `{"service":"search","method":"POST","path":"/search-all","body":
  {"queryIndices":["adp.api"],"queryText":"<value>","size":3,"from":0}}`; the row
  records `meta.total` for `api`, `apiDefinition`, `specification` and
  `collection`. The `apinetwork.collection` and `apinetwork.api` indices are
  refused by that endpoint (*"The following indices are not allowed"*), so
  `adp.api` — the API/definition index — is the one asked.
* **Vendor developer portals** — each row names the portals its own feature
  domain implies. Every one was fetched and grepped rather than read, and a
  vendor that publishes no OpenAPI document at all is recorded as such.

| key | outcome | witness | immutable ref | license | fern check | sources searched and the exact query used against each |
|---|---|---|---|---|---|---|
| `http-concealed` | `none-found` | none — no candidate was verified as declaring it. The nearest, the SwaggerHub `Auth Test` document that carries this table's `hoba` and `scram` rows, declares nine other IANA schemes and not `concealed` | — | — | not run — no candidate to run it on | **APIs.guru** `grep -rilE '"?scheme"?[[:space:]]*:[[:space:]]*"?concealed"?[[:space:],]*$' APIs/` over the 4,138 documents at `f04b8d0b` → 0 files. **GitHub** `gh search code concealed --filename openapi.yaml` → 30 results, `--filename openapi.json` → 20, `--filename swagger.yaml` → 3; all 53 fetched and grepped → 0 declare it. **Sourcegraph** `content:"scheme: concealed"` → 0 matches; `content:"\"scheme\": \"concealed\""` → 0. **SwaggerHub** `GET /specs?query=concealed&limit=20` → 163 results, top three all `1Password Connect`; the 20 returned documents fetched and grepped → 0 declare it. **Postman** `queryText: "concealed"` over `adp.api` → api 0, apiDefinition 0, specification 0, collection 0. **Vendor portals** RFC 9729 concealed authentication ships today only in MASQUE/relay products, so Cloudflare's published schema was fetched — `raw.githubusercontent.com/cloudflare/api-schemas/main/openapi.json` (24,855,060 bytes) and its `openapi.yaml` twin (18,358,009 bytes) → 0 — with the identity portals nearest the HTTP-auth-scheme domain: `okta/okta-management-openapi-spec` `dist/legacy-v1-swagger/spec.json` (633,378 bytes), `ory/hydra` `spec/api.json` (189,711 bytes) and `ory/kratos` `spec/api.json` (398,714 bytes) → 0 |
| `http-dpop` | `witness-found` | `mosip/esignet` — `docs/esignet-openapi.yaml`, at `https://raw.githubusercontent.com/mosip/esignet/201264c86e98113762451f4a306163233fa79e24/docs/esignet-openapi.yaml`. Fetched and read at that exact reference: **1** declaration, `Authorization-DPoP` with `type: http` and `scheme: DPoP`, beside four `bearer` schemes. The name is in neither `CORPUS.md` nor either DROPPED/REJECTED list | commit `201264c86e98113762451f4a306163233fa79e24` | MPL-2.0 — declared in the document (`info.license.name: MPL-2.0`) and as the repository's own license | **exit 0**, `All checks passed`, nothing on stderr but the CLI's upgrade banner | **APIs.guru** `grep -rilE '"?scheme"?[[:space:]]*:[[:space:]]*"?dpop"?[[:space:],]*$' APIs/` over the 4,138 documents at `f04b8d0b` → 0 files. **GitHub** `gh search code dpop --filename openapi.yaml` → 30, `--filename openapi.json` → 27, `--filename swagger.yaml` → 28; fetched and grepped, **7** documents declare it. **Sourcegraph** `content:"scheme: dpop"` → 0; `content:"\"scheme\": \"dpop\""` → 0 (its index does not hold these repositories). **SwaggerHub** `GET /specs?query=dpop&limit=20` → 710 results whose top names are unrelated (`7pace Timetracker API Reference`); the 20 returned documents fetched and grepped → 0 declare it. **Postman** `queryText: "dpop"` over `adp.api` → api 0, apiDefinition 0, specification 0, collection 0. **Vendor portals** `okta/okta-management-openapi-spec` `dist/legacy-v1-swagger/spec.json`, `ory/hydra` `spec/api.json`, `ory/kratos` `spec/api.json` → 0 each; Curity publishes no OpenAPI document at a public repository path (`curityio/openapi-specifications` → 404, and `gh search repos "curity openapi"` → no results). **The other candidates** `blackadi/OAUTH2.0` `server/src/routes/openapi.json` at `b6e4cfa1fb060ca5ca3e32185f4a5d88c27163e3` (repository MIT; `scheme: dpop` beside `bearer` and `basic`; `fern check` exit 0 `All checks passed`) and `openbankingproject-ch/Open-API-Kundenbeziehung-Legacy` `api/openapi.yaml` at `c7439ba67f5790d901d1d20943cae5cb48e8e7fc` (the document declares `info.license: MIT`, the repository carries no license file; `scheme: DPoP` beside `bearer`; `fern check` exit 0) also reach `witness-found`, and are the MIT-licensed fallbacks should MPL-2.0 be judged outside the corpus's Apache/MIT/BSD/CC0 set. `zerkerlabs/treeship` `docs/content/docs/api/hub-openapi.yaml` at `322a55f11e6799cf79b3dcf1bc1c874eb2630099` (Apache-2.0) declares `DPoP` as its **only** scheme and `fern check` exits 1 with ten `Endpoint requires auth, but no auth is defined` errors — the four-dropped-schemes finding reproduced on a real document. `rapinoinfeliz/SDRNexus`, `mishrasanjeev/grantex` and `routerarchitects/mc-cds-ui` declare it under no license or `NOASSERTION` |
| `http-gnap` | `none-found` | none — the one candidate was fetched and read and does not declare the feature: Interledger Open Payments' authorization-server document names its scheme `GNAP` but declares it `type: apiKey` with `in: header`, not `Security Scheme Object.scheme`, at `https://raw.githubusercontent.com/interledger/open-payments/v1.0/openapi/auth-server.yaml`, in its resource-server twin, and in `interledger/open-payments-specifications` `openapi/auth-server.yaml` at `8bc9eb5ea500a17b55da614268dca563865e30d4` alike | — | — | not run — no candidate declares the feature | **APIs.guru** `grep -rilE '"?scheme"?[[:space:]]*:[[:space:]]*"?gnap"?[[:space:],]*$' APIs/` over the 4,138 documents at `f04b8d0b` → 0 files. **GitHub** `gh search code gnap --filename openapi.yaml` → 30, `--filename openapi.json` → 30, `--filename swagger.yaml` → 12; all 72 fetched and grepped → 0 declare it. **Sourcegraph** `content:"scheme: gnap"` → 0; `content:"\"scheme\": \"gnap\""` → 0. **SwaggerHub** `GET /specs?query=gnap&limit=20` → 736 results whose top names are unrelated (`XLS Alphabank Campaign API`); the 20 returned documents fetched and grepped → 0 declare it. **Postman** `queryText: "gnap"` over `adp.api` → api 0, apiDefinition 0, specification 0, collection 0. **Vendor portals** GNAP's deployed implementation is Interledger Open Payments, whose three documents above are the candidate recorded; `ory/hydra` `spec/api.json` and `ory/kratos` `spec/api.json` → 0 |
| `http-hoba` | `witness-blocked` | SwaggerHub `Auth Test` 1.0.0, published by user `0UH3TN5N_1` at `https://api.swaggerhub.com/apis/0UH3TN5N_1/query/1.0.0`. Fetched and read at that reference: **1** declaration, `scheme_7` with `type: http` and `scheme: hoba`, among thirteen schemes that also cover `basic`, `bearer`, `digest`, `mutual`, `negotiate`, `oauth`, `scram-sha-1` and `scram-sha-256` | none — SwaggerHub exposes only the mutable `1.0.0` version reference, which its owner can edit in place; there is no commit or digest to pin | none — the document declares no `info.license` and the SwaggerHub API carries no license property, so it is not redistributable | not run — three properties block the document before Fern's verdict could matter: no license, no immutable ref, and a reference that does not end `.json`, `.yaml` or `.yml` as `fern-goldens.md` requires of a direct spec URL | **APIs.guru** `grep -rilE '"?scheme"?[[:space:]]*:[[:space:]]*"?hoba"?[[:space:],]*$' APIs/` over the 4,138 documents at `f04b8d0b` → 0 files. **GitHub** `gh search code hoba --filename openapi.yaml` → 30, `--filename openapi.json` → 30, `--filename swagger.yaml` → 18; all 78 fetched and grepped → 0 declare it. **Sourcegraph** `content:"scheme: hoba"` → 0; `content:"\"scheme\": \"hoba\""` → 0. **SwaggerHub** `GET /specs?query=hoba&limit=20` → 726 results whose top names are unrelated (`Legalesign API`); the 20 returned documents fetched and grepped → 0 declare it. The witness above was instead reached through this row's neighbour query `GET /specs?query=scram-sha-1&limit=10`, whose result set is only 3 documents and so was fetched whole: `faithy97007/fast-api/0.1.0` → 0, `0UH3TN5N_1/query/1.0.0` → the `Auth Test` document, `W1KT0R/your-api/1.0.0` → 0. **Postman** `queryText: "hoba"` over `adp.api` → api 1, apiDefinition 0, specification 0, collection 0; the one API is `hoba-backend` by `warped-meteor-692351`, a name match with no OpenAPI document exposed. **Vendor portals** HOBA has no vendor implementation with a developer portal — the IANA registry entry for it cites RFC 7486 and nothing else — so the identity portals nearest the domain were fetched and grepped: `okta/okta-management-openapi-spec` `dist/legacy-v1-swagger/spec.json`, `ory/hydra` `spec/api.json`, `ory/kratos` `spec/api.json` → 0 each |
| `http-mutual` | `witness-found` | `jentic/jentic-public-apis` — `apis/openapi/cyberark.com/conjur-api/5.3.2/openapi.json`, a self-contained bundle of CyberArk Conjur 5.3.2, at `https://raw.githubusercontent.com/jentic/jentic-public-apis/9d36c7e3808ebe65d69e81d3c3250598927a575c/apis/openapi/cyberark.com/conjur-api/5.3.2/openapi.json`. Fetched and read at that exact reference: **1** declaration, `conjurKubernetesMutualTls` with `type: http` and `scheme: mutual`, beside `basicAuth` (`http`/`basic`) and an `apiKey` scheme. This is a different document at a different source and ref from `conjur.local`, APIs.guru's 5.3.0 conversion, which is a `CORPUS.md` **DROPPED** row and was not retried | commit `9d36c7e3808ebe65d69e81d3c3250598927a575c` | Apache-2.0 declared in the document (`info.license.name`), inside a CC0-1.0 repository | **exit 0**, `All checks passed`, nothing on stderr but the CLI's upgrade banner — so not the false success `CORPUS.md` records against `conjur.local` | **APIs.guru** `grep -rilE '"?scheme"?[[:space:]]*:[[:space:]]*"?mutual"?[[:space:],]*$' APIs/` over the 4,138 documents at `f04b8d0b` → 1 file, `APIs/conjur.local/5.3.0/openapi.yaml`, which is the DROPPED row. **GitHub** `gh search code mutual --filename openapi.yaml` → 30, `--filename openapi.json` → 30, `--filename swagger.yaml` → 30; fetched and grepped, 3 declare it — the DROPPED `conjur.local`, the witness above, and `konfig-dev/konfig` `sdks/db/intermediate-fixed-specs/cyberark/conjur/openapi.yaml`, a third copy of the same Conjur document. **Sourcegraph** `content:"scheme: mutual"` → 3 matches (`APIs-guru/openapi-directory`, `WebFuzzing/EvoMaster` and `konfig-dev/konfig`, all copies of Conjur); `content:"\"scheme\": \"mutual\""` → 1 (the witness). **SwaggerHub** `GET /specs?query=mutual&limit=3` → 4,599 results whose top names are unrelated (`0Wallet Game Service API`), a set its content-blind metadata search cannot narrow further; the `Auth Test` document reached through the `scram-sha-1` query also declares `scheme: mutual`, under no license. **Postman** `queryText: "mutual"` over `adp.api` → api 0, apiDefinition 0, specification 0, collection 0. **Vendor portals** CyberArk is the vendor RFC 8120 implies: upstream `cyberark/conjur-openapi-spec` `spec/openapi.yml` at `90442c4db65695666f1c5545824c76968c5a7339` (Apache-2.0) was fetched and declares it too, and `fern check` exits 0 on it — but its `paths` are relative-file `$ref`s into sibling documents, so no single direct spec URL carries the whole API, which is why the self-contained bundle is the one recorded |
| `http-oauth` | `fern-rejected` | `jentic/jentic-public-apis` — `apis/openapi/thenounproject.com/noun-project-api/2.0.0/openapi.json`, at `https://raw.githubusercontent.com/jentic/jentic-public-apis/9d36c7e3808ebe65d69e81d3c3250598927a575c/apis/openapi/thenounproject.com/noun-project-api/2.0.0/openapi.json`. Fetched and read at that exact reference: **1** declaration, `OAuth1` with `type: http` and `scheme: oauth`, its only security scheme | commit `9d36c7e3808ebe65d69e81d3c3250598927a575c` | CC0-1.0, the repository's license; the document declares no `info.license` of its own | **exit 1** — `[sdk] 1 error`, `path: v2.yml -> service`, `issue: Service requires auth, but no auth is defined.`, `Found 1 error and 2 warnings` — the four-dropped-schemes finding reproduced on a real document that declares `oauth` alone | **APIs.guru** `grep -rilE '"?scheme"?[[:space:]]*:[[:space:]]*"?oauth"?[[:space:],]*$' APIs/` over the 4,138 documents at `f04b8d0b` → 2 files, `APIs/here.com/tracking/2.1.192/openapi.yaml` and `APIs/twitter.com/current/2.62/openapi.yaml`; the live registry serves 2.1.191 and 2.61 of the same two, both fetched from `api.apis.guru` and both still declaring it. **GitHub** `gh search code oauth --filename openapi.yaml` → 30, `--filename openapi.json` → 30, `--filename swagger.yaml` → 30; fetched and grepped, `Alia5/steaminputdb.com` `openapi.yaml` declares `scheme: OAuth` under AGPL-3.0. **Sourcegraph** `content:"scheme: oauth"` → 4 matches, `content:"\"scheme\": \"oauth\""` → 5, which between them are the HERE and X/Twitter documents, their `konfig-dev/konfig` and `DataFire/Integrations` mirrors, and the witness above. **SwaggerHub** `GET /specs?query=oauth&limit=3` → 199,548 results, top names `Swagger Petstore - OpenAPI 3.0` and two OAuth2 sample projects — a set its content-blind metadata search cannot narrow; the `Auth Test` document reached through the `scram-sha-1` query also declares `scheme: oauth`, under no license. **Postman** `queryText: "oauth"` over `adp.api` → api 16, apiDefinition 0, specification 0, collection 0; the index exposes no OpenAPI document to grep. **Vendor portals** Trello `https://developer.atlassian.com/cloud/trello/swagger.v3.json` (261,671 bytes) → 0; Flickr's APIs.guru document declares no `securitySchemes` at all; X publishes the declaration but under its own terms. **The other candidates, and what blocked each** `here.com/tracking` 2.1.191 pairs `scheme: oauth` with `bearer` but is under the *HERE Documentation License*; `twitter.com/current` 2.61, `xdevplatform/xdk` `specs/openapi.json` at `84c26540df30c0b798e50e34151c56d5d262ba1c` and `konfig-dev/konfig` `sdks/db/intermediate-fixed-specs/x/openapi.yaml` are three copies of one X document under the *Twitter/X Developer Agreement and Policy* — `xdk` additionally fails `fern check` exit 1 on an unrelated `ActivityStreamingResponsePayload` discriminant error; `Alia5/steaminputdb.com` is AGPL-3.0. All four are `witness-blocked` on license, which is why the CC0 document that Fern refuses is the better outcome recorded |
| `http-privatetoken` | `none-found` | none — no candidate was verified as declaring it | — | — | not run — no candidate to run it on | **APIs.guru** `grep -rilE '"?scheme"?[[:space:]]*:[[:space:]]*"?privatetoken"?[[:space:],]*$' APIs/` over the 4,138 documents at `f04b8d0b` → 0 files. **GitHub** `gh search code privatetoken --filename openapi.yaml` → 8 results, `--filename openapi.json` → 2, `--filename swagger.yaml` → 0; all 10 fetched and grepped → 0 declare it. **Sourcegraph** `content:"scheme: privatetoken"` → 0; `content:"\"scheme\": \"privatetoken\""` → 0. **SwaggerHub** `GET /specs?query=privatetoken&limit=20` → 2,885 results whose top names are unrelated (`LIVE PUBLIC REST API Docs v1.0.0`); the 20 returned documents fetched and grepped → 0 declare it. **Postman** `queryText: "privatetoken"` over `adp.api` → api 0, apiDefinition 0, specification 0, collection 0. **Vendor portals** RFC 9577 Private Access Tokens are issued by Cloudflare and Apple: Cloudflare's `raw.githubusercontent.com/cloudflare/api-schemas/main/openapi.json` (24,855,060 bytes) and `openapi.yaml` (18,358,009 bytes) → 0, and Apple publishes no OpenAPI document for Private Access Tokens at all |
| `http-scram-sha-1` | `witness-blocked` | SwaggerHub `Auth Test` 1.0.0, published by user `0UH3TN5N_1` at `https://api.swaggerhub.com/apis/0UH3TN5N_1/query/1.0.0`. Fetched and read at that reference: **1** declaration, `scheme_11` with `type: http` and `scheme: scram-sha-1` | none — SwaggerHub exposes only the mutable `1.0.0` version reference, which its owner can edit in place | none — the document declares no `info.license` and the SwaggerHub API carries no license property, so it is not redistributable | not run — the same three properties block it as for `http-hoba`: no license, no immutable ref, and a reference that does not end `.json`, `.yaml` or `.yml` | **APIs.guru** `grep -rilE '"?scheme"?[[:space:]]*:[[:space:]]*"?scram-sha-1"?[[:space:],]*$' APIs/` over the 4,138 documents at `f04b8d0b` → 0 files. **GitHub** `gh search code scram-sha-1 --filename openapi.yaml` → 0 results, `gh search code scram-sha-1 --filename openapi.json` → 0, `gh search code scram-sha-1 --filename swagger.yaml` → 8. Those 8 fall inside a 39-document union with the `scram-sha-256` queries, and all 39 were fetched from `https://raw.githubusercontent.com/<repo>/HEAD/<path>` (39 of 39 at HTTP 200) and grepped → 0 declare it: every match is a Kafka or MongoDB SASL mechanism enum value or a prose mention (`enum: [PLAIN, SCRAM-SHA-256, …]` in `RootShell-coder/kafka-menu`, an `authMechanism` description table in `clearblade.com` 3.0) rather than a Security Scheme Object `scheme`. The broader `gh search code scram --filename openapi.yaml` → 30, `--filename openapi.json` → 30, `--filename swagger.yaml` → 30 was also run — each capped at the 30-result limit, all 90 fetched and grepped → 0 declare it — and is recorded as a superset beside the exact query above, not in place of it. **Sourcegraph** `content:"scheme: scram-sha-1"` → 0; `content:"\"scheme\": \"scram-sha-1\""` → 0. **SwaggerHub** `GET /specs?query=scram-sha-1&limit=10` → only 3 results, so all three were fetched and grepped: `faithy97007/fast-api/0.1.0` → 0, `0UH3TN5N_1/query/1.0.0` → the witness above, `W1KT0R/your-api/1.0.0` → 0. **Postman** `queryText: "scram-sha-1"` over `adp.api` → api 2, apiDefinition 0, specification 0, collection 0; both are workspace-share links exposing no OpenAPI document to grep. **Vendor portals** RFC 7804 SCRAM over HTTP is a database-vendor domain: `mongodb/openapi` `openapi/v2.json` (4,099,640 bytes) → 0, `confluentinc/kafka-rest` `api/v3/openapi.yaml` (175,554 bytes) → 0, `scylladb/scylladb` `api/api-doc/storage_service.json` (146,321 bytes) → 0, and RabbitMQ publishes its management API as hand-written HTML rather than an OpenAPI document (`deps/rabbitmq_management/priv/www/api/index.html`, 82,167 bytes, fetched and confirmed not to be one) |
| `http-scram-sha-256` | `witness-blocked` | SwaggerHub `Auth Test` 1.0.0, published by user `0UH3TN5N_1` at `https://api.swaggerhub.com/apis/0UH3TN5N_1/query/1.0.0`. Fetched and read at that reference: **1** declaration, `scheme_12` with `type: http` and `scheme: scram-sha-256` | none — SwaggerHub exposes only the mutable `1.0.0` version reference, which its owner can edit in place | none — the document declares no `info.license` and the SwaggerHub API carries no license property, so it is not redistributable | not run — the same three properties block it as for `http-hoba`: no license, no immutable ref, and a reference that does not end `.json`, `.yaml` or `.yml` | **APIs.guru** `grep -rilE '"?scheme"?[[:space:]]*:[[:space:]]*"?scram-sha-256"?[[:space:],]*$' APIs/` over the 4,138 documents at `f04b8d0b` → 0 files. **GitHub** `gh search code scram-sha-256 --filename openapi.yaml` → 16 results, `gh search code scram-sha-256 --filename openapi.json` → 15, `gh search code scram-sha-256 --filename swagger.yaml` → 8. Those 39 results fall inside a 39-document union with the `scram-sha-1` queries, and all 39 were fetched from `https://raw.githubusercontent.com/<repo>/HEAD/<path>` (39 of 39 at HTTP 200) and grepped → 0 declare it: every match is a Kafka or MongoDB SASL mechanism enum value or a prose mention (`SCRAM_MECHANISM_SCRAM_SHA_256: SCRAM-SHA-256` in `redpanda-data/console`, `enum: [PLAIN, SCRAM-SHA-256, …]` in `RootShell-coder/kafka-menu`) rather than a Security Scheme Object `scheme`. The broader `gh search code scram --filename openapi.yaml` → 30, `--filename openapi.json` → 30, `--filename swagger.yaml` → 30 was also run — each capped at the 30-result limit, all 90 fetched and grepped → 0 declare it — and is recorded as a superset beside the exact query above, not in place of it. **Sourcegraph** `content:"scheme: scram-sha-256"` → 0; `content:"\"scheme\": \"scram-sha-256\""` → 0. **SwaggerHub** `GET /specs?query=scram-sha-256&limit=20` → 689 results whose top names are all `Streetlights Kafka API`, an AsyncAPI sample; the 20 returned documents fetched and grepped → 0 declare it, and the witness above was reached instead through this row's neighbour query `GET /specs?query=scram-sha-1&limit=10`, whose 3 results were fetched whole. **Postman** `queryText: "scram-sha-256"` over `adp.api` → api 0, apiDefinition 0, specification 0, collection 0. **Vendor portals** the same database-vendor set as `http-scram-sha-1`: `mongodb/openapi` `openapi/v2.json`, `confluentinc/kafka-rest` `api/v3/openapi.yaml`, `scylladb/scylladb` `api/api-doc/storage_service.json` → 0 each, and RabbitMQ publishes no OpenAPI document |
| `http-vapid` | `none-found` | none — no candidate was verified as declaring it | — | — | not run — no candidate to run it on | **APIs.guru** `grep -rilE '"?scheme"?[[:space:]]*:[[:space:]]*"?vapid"?[[:space:],]*$' APIs/` over the 4,138 documents at `f04b8d0b` → 0 files. **GitHub** `gh search code vapid --filename openapi.yaml` → 30, `--filename openapi.json` → 30, `--filename swagger.yaml` → 22; all 82 fetched and grepped → 0 declare it. **Sourcegraph** `content:"scheme: vapid"` → 0; `content:"\"scheme\": \"vapid\""` → 0. **SwaggerHub** `GET /specs?query=vapid&limit=20` → 117 results whose top names are unrelated (`Commerce Admin REST endpoints`); the 20 returned documents fetched and grepped → 0 declare it. **Postman** `queryText: "vapid"` over `adp.api` → api 0, apiDefinition 0, specification 0, collection 0. **Vendor portals** RFC 8292 VAPID is the Web Push domain: `gotify/server` `docs/spec.json` (94,742 bytes) → 0; `binwiederhier/ntfy` publishes no OpenAPI or Swagger document at all — its whole tree at `main` holds 0 paths matching `openapi` or `swagger`; `mozilla-services/autopush-rs` `docs/openapi.yaml` → 404 and `pushpad/pushpad-api` `openapi.yaml` → 404, neither vendor publishing one |
| `securityscheme-ref` | `fern-rejected` | `Open-EO/openeo-api` — `extensions/workspaces/openapi.yaml`, at `https://raw.githubusercontent.com/Open-EO/openeo-api/1881dae18b3c2c417f1305774cf295c81d60d400/extensions/workspaces/openapi.yaml`. Fetched and read at that exact reference: **1** reference-valued scheme, `components.securitySchemes.Bearer` holding `$ref: '../../openapi.yaml#/components/securitySchemes/Bearer'` in place of a Security Scheme Object | commit `1881dae18b3c2c417f1305774cf295c81d60d400` | Apache-2.0, the repository's license | **not accepted, exit 0** — Fern printed `[api]: Failed to parse openapi document openEO API - Workspaces Extension` and `[api]: Failed to resolve ../../openapi.yaml#/components/securitySchemes/Bearer`, with a `CliError` raised from `resolveSecuritySchemeReference`, and then printed `All checks passed` and exited 0. That is the false success `CORPUS.md` records against `conjur.local` and `dapr`; a document Fern failed to parse is not one Fern accepted, so this is `fern-rejected` | **APIs.guru** the shape is a `$ref` in a scheme position rather than a value, so the query is `grep -rl 'components/securitySchemes/' APIs/` over the 4,138 documents at `f04b8d0b` → 0 files. **GitHub** `gh search code securitySchemes --filename openapi.yaml` → 30, `--filename openapi.json` → 30, `--filename swagger.yaml` → 30; all fetched and every one parsed for a `$ref` inside its `securitySchemes` map, which found `exastro-suite/exastro-it-automation` `docs/openapi/ita_api_organization/openapi.yaml` (Apache-2.0 — but its `$ref` replaces the whole `securitySchemes` map rather than one scheme, a different shape) and `Tierion/boltwall` `openapi.yaml` (a false positive: the `$ref` sits under an `x-lsat` extension inside a scheme, not in a scheme position). **Sourcegraph** `content:"#/components/securitySchemes/"` → 24 matches and `content:"securitySchemes/"` → 32, which supplied the candidates below plus `getkin/kin-openapi`, `swagger-api/apidom` and `yaklang/yaklang` test fixtures (not real-world API documents) and `dapr/dapr` `swagger/swagger.json`, a `CORPUS.md` **DROPPED** row that was not retried. **SwaggerHub** `GET /specs?query=securitySchemes&limit=3` → 154,319 results, top names `Swagger Petstore - OpenAPI 3.0` and `0x API` — a set its content-blind metadata search can neither narrow nor enumerate, so this source could not answer for this row. **Postman** `queryText: "securitySchemes"` over `adp.api` → api 0, apiDefinition 0, specification 0, collection 0. **Vendor portals** the portals whose documents are split across files: `apify/apify-docs` `apify-api/openapi/openapi.yaml` at `522de71b25a299e348ba1da8f12b2608093b5712` → 2 reference-valued schemes, `apache/gravitino` `docs/open-api/idp/openapi.yaml` at `dad9a08dcdf397ed9558e4c36d57bdd49b75f3bf` → 1, and `flightctl/flightctl` `api/imagebuilder/v1alpha1/openapi.yaml` → 0 (its `securitySchemes` mention is a comment). **The other candidates** the Apify and Gravitino documents are both Apache-2.0, both declare the feature, and both fail `fern check` exactly as the recorded witness does — `Failed to resolve components/securitySchemes/httpBearer.yaml` and `Failed to resolve ../openapi.yaml#/components/securitySchemes/BasicAuth`, each from `resolveSecuritySchemeReference`, each followed by `All checks passed` and exit 0 — so all three reach `fern-rejected` and none reaches better; `KasperiP/lukittu` `apps/web/docs/openapi/openapi.yaml` (AGPL-3.0) and `bytechefhq/bytechef` `server/ee/libs/embedded/embedded-unified/embedded-unified-rest/openapi/v1/crm/openapi.yaml` (`NOASSERTION`) declare it under licenses that block them |

Every count above was read out of a document fetched at the reference its row
names, never out of a search-result snippet, and every date-sensitive refusal is
recorded as it was observed rather than as a claim about the service. Re-running
a row means re-running the six queries its own cell spells out; nothing here is a
guarantee that the world holds no witness beyond those six sources, only a record
of what they answered.
