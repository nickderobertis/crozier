# OpenAPI surface coverage — Schemas

Classified entries for the `schemas` region.

### How this region was enumerated

The feature list is copied from the two normative surfaces in specification
order, not from crozier's data model, so a future reader can repeat the walk and
get the same list:

1. **The OAS 3.0 Schema Object's own fixed-field list** — the selected, adjusted
   subset of JSON Schema Draft Wright-00 that
   [OAS 3.0.3 § Schema Object](https://spec.openapis.org/oas/v3.0.3#schema-object)
   enumerates, from `title` to `deprecated`, with `additionalProperties` taken in
   all three of its forms.
2. **Each JSON Schema 2020-12 vocabulary OAS 3.1 adopts**, one vocabulary at a
   time so none is skipped: Core, Applicator, Unevaluated, Validation, Meta-data,
   Format-Annotation and Format-Assertion, and Content. `format` is one keyword
   over an open set of values, so it is walked as **two closed lists and no
   third**: the nineteen values the
   [2020-12 format registry](https://json-schema.org/draft/2020-12/json-schema-validation#name-defined-formats)
   defines, from `date-time` to `regex`, and the values the OAS Data Types tables
   define themselves —
   [3.0.3 § Data Types](https://spec.openapis.org/oas/v3.0.3#data-types) adds
   `int32`, `int64`, `float`, `double`, `byte`, `binary` and `password` to the
   registry's `date` and `date-time`, and
   [3.1.0 § Data Types](https://spec.openapis.org/oas/v3.1.0#data-types) keeps
   all of those but `byte` and `binary`, which `contentEncoding` and
   `contentMediaType` replace. Any other value is a custom spelling neither
   specification defines, and the corpus is full of them — the census reports 50
   distinct `schema.format` values across the registered sources, of which these
   two lists name 26.
3. **OAS 3.1's own additions to a schema node** — `discriminator`, `xml`,
   `externalDocs`, and `example` beside the `examples` that supersedes it.
4. **The shapes that are structure rather than a single keyword** — a boolean
   schema (`true` and `false`) in each position one may appear, a `$ref` carrying
   sibling keywords, a recursive and a mutually recursive graph, a cycle closed
   through `additionalProperties`, and each composition keyword nested inside
   another — followed by the fixed fields of the Discriminator and XML Objects,
   which this region also owns.

A keyword appearing in more than one of those lists is one row, not several:
`items`, `properties`, `additionalProperties`, `allOf`/`anyOf`/`oneOf`/`not`,
`title`, `description`, `default`, `deprecated`, `readOnly`, `writeOnly`, `enum`,
`required` and the numeric and string bounds are 3.0 fixed fields *and* 2020-12
vocabulary members, so they carry `both` in the `oas` column. To repeat the walk:
take the four lists above in order, de-duplicate, and query each keyword as
`schema.<field>` — or `schema.format=<value>` for a format — with `just
surface-census --json`.

#### One row or two, where the two specifications differ

A keyword whose 3.0 and 3.1 spellings or semantics differ is **one row with
`oas: both` when both spellings classify the same way, and two rows when they do
not**:

- **`exclusiveMinimum` — one row.** Both spellings are declared by registered
  sources (54 boolean declarations in three 3.0 documents, 22 numeric ones in two
  3.1 documents), so both are `golden` and the evidence cell carries each.
- **`exclusiveMaximum` — two rows.** Every one of its declarations is the 3.0
  boolean form, so the boolean spelling is `golden` and the numeric 3.1 spelling
  is a `gap`. The spellings classify differently, so they cannot share a row.
- **`type` — three rows.** `type-single` (a string, either specification),
  `type-array-with-null` and `type-array-multi-nonnull` (3.1 array forms) are the
  three shapes the enumeration names, and the array forms are what a 3.0 document
  cannot express.
- **`nullable` against a `null` type member — two rows.** They are different
  keywords with different version ranges, not two spellings of one: `nullable` is
  a 3.0 fixed field, `type: [..., "null"]` is the 3.1 replacement, and both are
  `golden` on their own evidence.
- **`format: byte` and `format: binary` — one row each, `oas: 3.0`.** They are
  not two spellings of one keyword but two values 3.1 withdrew: 3.0's Data Types
  table defines both, 3.1's does not, and `contentEncoding`/`contentMediaType`
  carry the meaning there. Each is `golden` on its own evidence, and the 3.1
  replacements are the `content-encoding` and `content-media-type` rows.
- **`example` against `examples` — two rows**, for the same reason: `example` is
  a singular free-form value in both specifications, `examples` is the 3.1 array
  that supersedes it.

#### The instrument, and the one thing it cannot see

`just surface-census` is the classification instrument: it walks each registered
source document's OpenAPI object model and reports, per selector, how many
declaration sites each source carries. Every `golden` row below quotes it.

What the census records is that a *keyword* is declared, never the *kind of
value* it carries or the *shape of the graph* it sits in — `schema.type` counts a
declaration whether the value is a string or an array, `schema.additionalProperties`
counts one whether the value is `true`, `false` or a schema, and no selector
exists for a boolean schema, for a `$ref` with siblings, or for a reference cycle.
Twenty-five of this region's rows are exactly those variants, so they are measured
by a **supplementary variant scan** — a subclass of the census's own walker that
splits the value kinds it merges. Its evidence cells are marked
`variant scan <fact>`; the scan, the command that runs it, and the self-check that
proves its parts add back up to the census's totals are in
[Method notes](#method-notes).

#### What belongs to another region

Cross-linked rather than duplicated, because every feature belongs to exactly one
region file:

- `components.schemas` and the collision behaviour of the names that key it
  (`docs/fern-limitations.md` `normalization-collision`) belong to
  [`document-paths.md`](document-paths.md) with the Components Object, as does a
  Path Item `$ref` (`pathitem-ref`, `relative-file-ref`).
- The `schema` field of a Parameter, Header, Media Type, Request Body or Response
  belongs to that object's region ([`parameters.md`](parameters.md),
  [`bodies-media.md`](bodies-media.md)); the Schema Object it holds is classified
  here.
- XML *payloads* — `application/xml` request and response bodies
  (`docs/fern-limitations.md` `xml-request`, `xml-response`) — belong to
  [`bodies-media.md`](bodies-media.md). The XML Object that annotates a schema is
  classified here.
- `x-` extensions on a schema node belong to
  [`oas31-extensions.md`](oas31-extensions.md).

## Scope

Schema, Discriminator and XML objects, and every JSON Schema keyword wherever it
appears, including the ones 3.1 added.

## Entries

| key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |
|---|---|---|---|---|---|---|---|
| title | both | Schema Object.title | golden | census `schema.title`: 9624 declarations in 52 fixtures — `6-dot-authentiqio.appspot.com` (3), `amazonaws.com-cloudformation` (66), `amazonaws.com-cloudfront` (27), `apicurio.local-registry` (19), `apideck.com-accounting` (284), `apideck.com-ats` (60), `apideck.com-connector` (8), `apideck.com-crm` (44), `apideck.com-customer-support` (41), `apideck.com-ecommerce` (123), `apideck.com-file-storage` (8), `apideck.com-hris` (83), `apideck.com-issue-tracking` (49), `apideck.com-lead` (18), `apideck.com-pos` (130), `apideck.com-sms` (29), `apideck.com-vault` (29), `apideck.com-webhook` (6), `auth-schemes` (2), `box.com` (227), `canada-holidays.ca` (3), `client-class-name` (1), `cookie-parameters` (1), `discriminated-unions` (3), `eos.local` (4), `eos.local-extra-fields-forbid` (4), `error-responses` (2), `exhaustive` (24), `form-bodies` (2), `github.com` (2073), `groundhog-day.com` (2), `inline-array-request` (1), `inline-request-response` (5), `integer-enums` (3), `khoainats` (2), `letta` (2827), `livepeer-ai-runner` (157), `microcks.local` (1), `netbox.dev` (2639), `oauth-client-credentials` (3), `openbanking.org.uk-account-info-openapi` (436), `pydantic-extra-fields` (1), `recursive-types` (3), `redhat.com-catalog_inventory` (40), `schema-constraints` (2), `servers-webhooks` (3), `sigstore-rekor` (23), `sse-streaming` (1), `tamoss` (61), `twilio.com-twilio_messaging_v1` (21), `twilio.com-twilio_voice_v1` (19), `writeonly-fields` (1) |  |  |  |
| multiple-of | both | Schema Object.multipleOf | gap | census `schema.multipleOf`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"multipleOf"' src/` finds no production read | The numeric field annotations in the generated `types/` modules would differ if Fern renders a `multipleOf` bound crozier never reads. | FIXTURE — a redistributable real-world document declaring `multipleOf` on a component schema, registered as a corpus row whose Fern golden byte-matches, settles it. |
| maximum | both | Schema Object.maximum | golden | census `schema.maximum`: 512 declarations in 37 fixtures — `amazonaws.com-cloudformation` (17), `apideck.com-accounting` (1), `apideck.com-ats` (1), `apideck.com-connector` (1), `apideck.com-crm` (1), `apideck.com-customer-support` (1), `apideck.com-ecommerce` (1), `apideck.com-ecosystem` (1), `apideck.com-file-storage` (2), `apideck.com-hris` (15), `apideck.com-issue-tracking` (1), `apideck.com-lead` (1), `apideck.com-pos` (2), `apideck.com-sms` (1), `apideck.com-vault` (1), `apideck.com-webhook` (1), `atlassian.com-jira` (1), `bbci.co.uk` (1), `box.com` (49), `canada-holidays.ca` (7), `dnd5eapi.co` (5), `eozilla` (1), `free5gc-namf-communication` (29), `free5gc-pdu-session` (44), `github.com` (4), `groundhog-day.com` (3), `kytos-sdntrace-cp` (2), `letta` (15), `netbox.dev` (115), `portfoliooptimizer.io` (142), `redhat.com-catalog_inventory` (1), `redocly.com-museum` (1), `sac-backend` (2), `schema-constraints` (2), `squareup.com` (25), `twilio.com-twilio_messaging_v1` (8), `twilio.com-twilio_voice_v1` (7) |  |  |  |
| exclusive-maximum-boolean | 3.0 | Schema Object.exclusiveMaximum | golden | variant scan `exclusiveMaximum=boolean`: 8 declarations in 2 fixtures — `groundhog-day.com` (2), `portfoliooptimizer.io` (6); both are 3.0 documents (census `openapi.openapi=3.0`), and they are every one of the census's 8 `schema.exclusiveMaximum` declarations |  |  |  |
| exclusive-maximum-numeric | 3.1 | Schema Object.exclusiveMaximum | gap | variant scan `exclusiveMaximum=numeric`: 0 declarations across all 124 registered sources — all 8 `schema.exclusiveMaximum` declarations the census reports carry the 3.0 boolean form; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"exclusiveMaximum"' src/` finds no production read | The upper-bound field annotations in the generated `types/` modules would differ if Fern reads the 3.1 numeric spelling of the bound. | FIXTURE — a 3.1 corpus row declaring a numeric `exclusiveMaximum` settles it; the 3.0 boolean spelling is already golden as `exclusive-maximum-boolean`. |
| minimum | both | Schema Object.minimum | golden | census `schema.minimum`: 774 declarations in 44 fixtures — `amazonaws.com-cloudformation` (26), `apache.org` (3), `apache.org-airflow` (3), `apideck.com-accounting` (1), `apideck.com-ats` (1), `apideck.com-connector` (1), `apideck.com-crm` (2), `apideck.com-customer-support` (1), `apideck.com-ecommerce` (1), `apideck.com-ecosystem` (1), `apideck.com-file-storage` (2), `apideck.com-hris` (15), `apideck.com-issue-tracking` (1), `apideck.com-lead` (1), `apideck.com-pos` (2), `apideck.com-sms` (1), `apideck.com-vault` (1), `apideck.com-webhook` (1), `apis.guru` (3), `bbci.co.uk` (1), `box.com` (14), `canada-holidays.ca` (7), `dnd5eapi.co` (5), `electric-sql` (4), `eozilla` (8), `exa-gate` (3), `frankfurter` (1), `free5gc-namf-communication` (40), `free5gc-pdu-session` (58), `github.com` (4), `groundhog-day.com` (7), `kytos-sdntrace-cp` (2), `letta` (16), `netbox.dev` (122), `openepcis-dpp-ready` (1), `portfoliooptimizer.io` (326), `redhat.com-catalog_inventory` (2), `sac-backend` (3), `schema-constraints` (2), `sigstore-rekor` (9), `squareup.com` (32), `tamoss` (10), `twilio.com-twilio_messaging_v1` (16), `twilio.com-twilio_voice_v1` (14) |  |  |  |
| exclusive-minimum | both | Schema Object.exclusiveMinimum | golden | variant scan `exclusiveMinimum=boolean`: 54 declarations in 3 fixtures — `eozilla` (1), `groundhog-day.com` (3), `portfoliooptimizer.io` (50) — the 3.0 boolean spelling, all three 3.0 documents; and variant scan `exclusiveMinimum=numeric`: 22 declarations in 2 fixtures — `frankfurter` (2), `tamoss` (20) — the 3.1 numeric spelling, both 3.1 documents; together they are the census's 76 `schema.exclusiveMinimum` declarations |  |  |  |
| max-length | both | Schema Object.maxLength | golden | census `schema.maxLength`: 1850 declarations in 21 fixtures — `amazonaws.com-cloudformation` (174), `amazonaws.com-cloudfront` (2), `apideck.com-ecommerce` (1), `apideck.com-hris` (1), `apideck.com-pos` (15), `apideck.com-sms` (1), `apis.guru` (3), `atlassian.com-jira` (62), `box.com` (51), `calorieninjas.com` (1), `free5gc-namf-communication` (4), `github.com` (23), `letta` (152), `netbox.dev` (554), `openbanking.org.uk-account-info-openapi` (277), `sac-backend` (22), `schema-constraints` (2), `squareup.com` (363), `twilio.com-twilio_messaging_v1` (93), `twilio.com-twilio_voice_v1` (43), `xero.com-xero-payroll-au` (6) |  |  |  |
| min-length | both | Schema Object.minLength | golden | census `schema.minLength`: 1335 declarations in 33 fixtures — `amazonaws.com-cloudformation` (184), `amazonaws.com-cloudfront` (2), `apache.org` (3), `apache.org-airflow` (3), `apideck.com-accounting` (8), `apideck.com-ats` (4), `apideck.com-crm` (10), `apideck.com-customer-support` (8), `apideck.com-ecommerce` (3), `apideck.com-hris` (9), `apideck.com-issue-tracking` (3), `apideck.com-lead` (5), `apideck.com-pos` (5), `apideck.com-sms` (1), `apis.guru` (5), `atlassian.com-jira` (5), `bbci.co.uk` (1), `box.com` (10), `buildrelay` (3), `calorieninjas.com` (1), `conjur.local` (14), `eozilla` (1), `free5gc-namf-communication` (4), `github.com` (4), `letta` (153), `netbox.dev` (284), `openbanking.org.uk-account-info-openapi` (276), `openepcis-dpp-ready` (1), `sac-backend` (16), `schema-constraints` (4), `squareup.com` (169), `twilio.com-twilio_messaging_v1` (93), `twilio.com-twilio_voice_v1` (43) |  |  |  |
| pattern | both | Schema Object.pattern | golden | census `schema.pattern`: 943 declarations in 34 fixtures — `amazonaws.com-cloudformation` (128), `amazonaws.com-cloudfront` (6), `anchore.io` (10), `apache.org` (1), `apache.org-airflow` (1), `apideck.com-accounting` (4), `apideck.com-ats` (1), `apideck.com-ecommerce` (2), `apideck.com-hris` (28), `apideck.com-vault` (2), `apideck.com-webhook` (3), `bbci.co.uk` (2), `box.com` (3), `canada-holidays.ca` (1), `conjur.local` (1), `dnd5eapi.co` (1), `eos.local` (4), `eos.local-extra-fields-forbid` (4), `free5gc-namf-communication` (68), `free5gc-pdu-session` (66), `github.com` (15), `letta` (176), `netbox.dev` (83), `openbanking.org.uk-account-info-openapi` (141), `redhat.com-catalog_inventory` (3), `redocly.com-museum` (2), `schema-constraints` (1), `sigstore-rekor` (30), `squareup.com` (1), `tamoss` (12), `tlon-notes` (3), `twilio.com-twilio_messaging_v1` (93), `twilio.com-twilio_voice_v1` (43), `worldcoin-signup-sequencer` (4) |  |  |  |
| max-items | both | Schema Object.maxItems | golden | census `schema.maxItems`: 73 declarations in 15 fixtures — `amazonaws.com-cloudformation` (22), `atlassian.com-jira` (6), `box.com` (6), `eozilla` (1), `etsi.local-mec010-2_apppkgmgmt` (1), `exa-gate` (1), `free5gc-namf-communication` (1), `github.com` (11), `letta` (7), `openbanking.org.uk-account-info-openapi` (2), `openfigi.com` (2), `portfoliooptimizer.io` (3), `schema-constraints` (1), `sigstore-rekor` (3), `worldcoin-signup-sequencer` (6) |  |  |  |
| min-items | both | Schema Object.minItems | golden | census `schema.minItems`: 668 declarations in 25 fixtures — `amazonaws.com-cloudformation` (6), `amazonaws.com-cloudfront` (1), `apache.org` (1), `apache.org-airflow` (1), `apideck.com-accounting` (1), `apis.guru` (2), `atlassian.com-jira` (6), `bbci.co.uk` (1), `box.com` (7), `discourse.local` (3), `eozilla` (3), `etsi.local-mec010-2_apppkgmgmt` (29), `exa-gate` (1), `free5gc-namf-communication` (51), `free5gc-pdu-session` (40), `github.com` (17), `letta` (8), `openbanking.org.uk-account-info-openapi` (53), `openepcis-dpp-ready` (1), `openfigi.com` (2), `portfoliooptimizer.io` (420), `schema-constraints` (1), `sigstore-rekor` (6), `tamoss` (1), `worldcoin-signup-sequencer` (6) |  |  |  |
| unique-items | both | Schema Object.uniqueItems | golden | census `schema.uniqueItems`: 172 declarations in 7 fixtures — `apideck.com-issue-tracking` (1), `atlassian.com-jira` (80), `bbci.co.uk` (1), `discourse.local` (3), `eozilla` (2), `netbox.dev` (62), `portfoliooptimizer.io` (23) |  |  |  |
| max-properties | both | Schema Object.maxProperties | golden | census `schema.maxProperties`: 10 declarations in 3 fixtures — `amazonaws.com-cloudformation` (1), `atlassian.com-jira` (5), `github.com` (4) |  |  |  |
| min-properties | both | Schema Object.minProperties | golden | census `schema.minProperties`: 12 declarations in 5 fixtures — `amazonaws.com-cloudformation` (1), `apis.guru` (4), `atlassian.com-jira` (5), `free5gc-pdu-session` (1), `openbanking.org.uk-account-info-openapi` (1) |  |  |  |
| required | both | Schema Object.required | golden | census `schema.required`: 6787 declarations in 95 fixtures — `6-dot-authentiqio.appspot.com` (4), `airbyte.local-config` (136), `amazonaws.com-cloudformation` (66), `amazonaws.com-cloudfront` (72), `anchore.io` (31), `apache.org` (5), `apache.org-airflow` (5), `apache.org-qakka` (2), `apicurio.local-registry` (22), `apideck.com-accounting` (82), `apideck.com-ats` (14), `apideck.com-connector` (9), `apideck.com-crm` (53), `apideck.com-customer-support` (15), `apideck.com-ecommerce` (29), `apideck.com-ecosystem` (22), `apideck.com-file-storage` (42), `apideck.com-hris` (38), `apideck.com-issue-tracking` (24), `apideck.com-lead` (12), `apideck.com-pos` (56), `apideck.com-sms` (9), `apideck.com-vault` (19), `apideck.com-webhook` (11), `apis.guru` (3), `appng-rest-api` (10), `appwrite.io-client` (53), `appwrite.io-server` (64), `asana.com` (34), `atlassian.com-jira` (231), `auth-schemes` (2), `bbci.co.uk` (69), `bintable.com` (1), `box.com` (174), `buildrelay` (3), `bunq.com` (61), `byautomata.io` (6), `canada-holidays.ca` (2), `client-class-name` (1), `codesearch.debian.net` (2), `conjur.local` (6), `cookie-parameters` (1), `discourse.local` (178), `discriminated-unions` (2), `dnd5eapi.co` (1), `electric-sql` (3), `eos.local` (3), `eos.local-extra-fields-forbid` (3), `eozilla` (14), `error-responses` (2), `etsi.local-mec010-2_apppkgmgmt` (28), `exa-gate` (5), `exhaustive` (15), `form-bodies` (4), `frankfurter` (5), `free5gc-namf-communication` (80), `free5gc-pdu-session` (51), `github.com` (2899), `groundhog-day.com` (10), `http-toolkit` (3), `inline-array-request` (2), `inline-request-response` (7), `integer-enums` (1), `khoainats` (1), `kytos-sdntrace-cp` (4), `letta` (438), `livepeer-ai-runner` (31), `maif.local-otoroshi` (81), `microcks.local` (32), `netbox.dev` (393), `oauth-client-credentials` (3), `openbanking.org.uk-account-info-openapi` (235), `openepcis-dpp-ready` (9), `openfigi.com` (1), `portfoliooptimizer.io` (288), `prometheus-x-edge-computing` (5), `pydantic-extra-fields` (1), `recursive-types` (2), `redhat.com-catalog_inventory` (1), `redocly.com-museum` (4), `reverb.com` (21), `sac-backend` (10), `schema-constraints` (2), `servers-webhooks` (3), `sigstore-rekor` (73), `squareup.com` (164), `tamoss` (61), `tlon-notes` (71), `traccar.org` (1), `twilio.com-twilio_messaging_v1` (10), `twilio.com-twilio_voice_v1` (5), `withsecure-gdpr-subject-rights` (6), `worldcoin-signup-sequencer` (5), `writeonly-fields` (1), `xero.com-xero-payroll-au` (8) |  |  |  |
| enum | both | Schema Object.enum | golden | census `schema.enum`: 5601 declarations in 76 fixtures — `airbyte.local-config` (35), `amazonaws.com-cloudformation` (362), `amazonaws.com-cloudfront` (16), `anchore.io` (30), `apache.org` (9), `apache.org-airflow` (9), `apicurio.local-registry` (11), `apideck.com-accounting` (33), `apideck.com-ats` (9), `apideck.com-connector` (17), `apideck.com-crm` (17), `apideck.com-customer-support` (9), `apideck.com-ecommerce` (13), `apideck.com-ecosystem` (8), `apideck.com-file-storage` (5), `apideck.com-hris` (21), `apideck.com-issue-tracking` (13), `apideck.com-lead` (9), `apideck.com-pos` (35), `apideck.com-sms` (5), `apideck.com-vault` (15), `apideck.com-webhook` (4), `appng-rest-api` (7), `asana.com` (43), `atlassian.com-jira` (121), `bbci.co.uk` (56), `box.com` (335), `buildrelay` (2), `bungie.net` (155), `canada-holidays.ca` (10), `codesearch.debian.net` (3), `color.pizza` (1), `conjur.local` (8), `corrently.io` (3), `discourse.local` (14), `discriminated-unions` (2), `dnd5eapi.co` (32), `electric-sql` (8), `enum-name-sanitization` (3), `enum-query-param` (1), `enum-receiver-collision` (2), `eozilla` (8), `etsi.local-mec010-2_apppkgmgmt` (13), `exa-gate` (2), `exhaustive` (5), `frankfurter` (4), `free5gc-namf-communication` (29), `free5gc-pdu-session` (28), `github.com` (3019), `groundhog-day.com` (2), `helios-verifiable-api` (2), `integer-enums` (2), `letta` (209), `livepeer-ai-runner` (1), `maif.local-otoroshi` (14), `med-anvisa-price` (1), `microcks.local` (8), `netbox.dev` (246), `openbanking.org.uk-account-info-openapi` (159), `openepcis-dpp-ready` (4), `openfigi.com` (4), `portfoliooptimizer.io` (24), `recursive-types` (2), `redhat.com-catalog_inventory` (2), `redocly.com-museum` (1), `reverb.com` (21), `sac-backend` (5), `sigstore-rekor` (17), `squareup.com` (140), `tamoss` (19), `tlon-notes` (64), `twilio.com-twilio_messaging_v1` (13), `twilio.com-twilio_voice_v1` (9), `withsecure-gdpr-subject-rights` (6), `worldcoin-signup-sequencer` (1), `xero.com-xero-payroll-au` (26); the member kinds the scan finds are string, integer, boolean and null (`enum-member-float` and `enum-member-object` are rows of their own below) |  |  |  |
| type-single | both | Schema Object.type | golden | census `schema.type`: 108256 declarations in 124 fixtures — `6-dot-authentiqio.appspot.com` (60), `airbyte.local-config` (557), `amazonaws.com-cloudformation` (1049), `amazonaws.com-cloudfront` (271), `anchore.io` (821), `apache.org` (512), `apache.org-airflow` (512), `apache.org-qakka` (35), `apicurio.local-registry` (212), `apideck.com-accounting` (907), `apideck.com-ats` (292), `apideck.com-connector` (227), `apideck.com-crm` (692), `apideck.com-customer-support` (335), `apideck.com-ecommerce` (381), `apideck.com-ecosystem` (314), `apideck.com-file-storage` (364), `apideck.com-hris` (526), `apideck.com-issue-tracking` (304), `apideck.com-lead` (220), `apideck.com-pos` (699), `apideck.com-proxy` (22), `apideck.com-sms` (155), `apideck.com-vault` (355), `apideck.com-webhook` (164), `apis.guru` (40), `appng-rest-api` (195), `appwrite.io-client` (382), `appwrite.io-server` (470), `asana.com` (1046), `atlassian.com-jira` (3774), `audience-filter` (7), `audience-filter-strict` (9), `auth-schemes` (9), `axesso.de` (52), `basic-auth` (1), `bbci.co.uk` (412), `bintable.com` (9), `box.com` (2631), `bracketed-property-names` (7), `buildrelay` (31), `bungie.net` (5304), `bunq.com` (4807), `byautomata.io` (87), `calorieninjas.com` (1), `canada-holidays.ca` (52), `client-class-name` (5), `codesearch.debian.net` (20), `color.pizza` (70), `conjur.local` (160), `cookie-parameters` (6), `corrently.io` (164), `digit-leading-property` (2), `discourse.local` (2891), `discriminated-unions` (6), `dnd5eapi.co` (473), `electric-sql` (105), `enum-name-sanitization` (4), `enum-query-param` (3), `enum-receiver-collision` (3), `eos.local` (38), `eos.local-extra-fields-forbid` (38), `eozilla` (166), `error-responses` (9), `esgenterprise.com` (8), `etherpad.local` (1860), `etsi.local-mec010-2_apppkgmgmt` (178), `exa-gate` (41), `exhaustive` (149), `form-bodies` (12), `frankfurter` (64), `free5gc-namf-communication` (408), `free5gc-pdu-session` (434), `gambitcomm.local-mimic` (1168), `github.com` (43141), `gov.bc.ca-news` (263), `groundhog-day.com` (58), `helios-verifiable-api` (32), `http-toolkit` (41), `inline-array-request` (9), `inline-request-response` (17), `integer-enums` (4), `khoainats` (4), `kytos-sdntrace-cp` (41), `letta` (5442), `livepeer-ai-runner` (160), `maif.local-otoroshi` (712), `malformed-property-schema` (3), `med-anvisa-price` (47), `microcks.local` (268), `missing-operation-id` (2), `nested-core-imports` (4), `netbox.dev` (10392), `nimisampo` (105), `oauth-client-credentials` (10), `openbanking.org.uk-account-info-openapi` (1167), `openepcis-dpp-ready` (62), `openfigi.com` (46), `operation-id-non-identifier` (4), `portfoliooptimizer.io` (1393), `prometheus-x-edge-computing` (31), `pydantic-extra-fields` (5), `query-parameters-openapi` (26), `recursive-types` (9), `redhat.com-catalog_inventory` (215), `redocly.com-museum` (33), `reverb.com` (547), `sac-backend` (106), `schema-constraints` (14), `servers-webhooks` (8), `sigstore-rekor` (231), `slurmdb-rest` (477), `squareup.com` (3065), `sse-streaming` (3), `tag-based-grouping` (8), `tamoss` (378), `tlon-notes` (306), `traccar.org` (340), `twilio.com-twilio_messaging_v1` (484), `twilio.com-twilio_voice_v1` (261), `withsecure-gdpr-subject-rights` (43), `worldcoin-signup-sequencer` (23), `writeonly-fields` (6), `xero.com-xero-payroll-au` (413); the variant scan splits those into three disjoint parts — 106386 single-string declarations in 124 fixtures, a further 1370 in the 3.1 null-only form `type: "null"` (`letta`), and 500 array-valued ones the two `type-array-*` rows own |  |  |  |
| allof | both | Schema Object.allOf | golden | census `schema.allOf`: 2105 declarations in 33 fixtures — `amazonaws.com-cloudformation` (859), `amazonaws.com-cloudfront` (317), `anchore.io` (15), `apache.org` (22), `apache.org-airflow` (22), `apicurio.local-registry` (2), `apideck.com-accounting` (1), `apideck.com-ats` (1), `apideck.com-crm` (1), `apideck.com-file-storage` (1), `apideck.com-hris` (1), `apideck.com-issue-tracking` (1), `apideck.com-lead` (1), `apideck.com-pos` (1), `appng-rest-api` (1), `asana.com` (127), `atlassian.com-jira` (136), `box.com` (261), `bungie.net` (194), `dnd5eapi.co` (36), `eozilla` (6), `exhaustive` (2), `free5gc-namf-communication` (2), `free5gc-pdu-session` (2), `github.com` (36), `gov.bc.ca-news` (17), `livepeer-ai-runner` (4), `microcks.local` (2), `openepcis-dpp-ready` (11), `redocly.com-museum` (2), `sac-backend` (2), `tamoss` (15), `tlon-notes` (4) |  |  |  |
| oneof | both | Schema Object.oneOf | golden | census `schema.oneOf`: 441 declarations in 26 fixtures — `apideck.com-webhook` (3), `atlassian.com-jira` (3), `bbci.co.uk` (3), `box.com` (15), `discriminated-unions` (1), `dnd5eapi.co` (5), `electric-sql` (1), `eozilla` (7), `exhaustive` (2), `free5gc-namf-communication` (3), `free5gc-pdu-session` (1), `github.com` (230), `helios-verifiable-api` (2), `letta` (87), `maif.local-otoroshi` (22), `microcks.local` (2), `nimisampo` (1), `openepcis-dpp-ready` (2), `openfigi.com` (2), `portfoliooptimizer.io` (15), `query-parameters-openapi` (2), `recursive-types` (1), `sigstore-rekor` (17), `tamoss` (3), `tlon-notes` (10), `worldcoin-signup-sequencer` (1) |  |  |  |
| anyof | both | Schema Object.anyOf | golden | census `schema.anyOf`: 1530 declarations in 28 fixtures — `apache.org` (1), `apache.org-airflow` (1), `apideck.com-accounting` (6), `apideck.com-ats` (5), `apideck.com-connector` (3), `apideck.com-crm` (5), `apideck.com-customer-support` (5), `apideck.com-ecommerce` (5), `apideck.com-file-storage` (4), `apideck.com-hris` (5), `apideck.com-issue-tracking` (5), `apideck.com-lead` (5), `apideck.com-pos` (5), `apideck.com-proxy` (3), `apideck.com-sms` (5), `apideck.com-vault` (9), `apideck.com-webhook` (4), `atlassian.com-jira` (3), `bbci.co.uk` (6), `box.com` (1), `dnd5eapi.co` (3), `free5gc-namf-communication` (1), `github.com` (20), `letta` (1416), `livepeer-ai-runner` (1), `openepcis-dpp-ready` (1), `tamoss` (1), `withsecure-gdpr-subject-rights` (1) |  |  |  |
| not | both | Schema Object.not | golden | census `schema.not`: 5 declarations in 2 fixtures — `free5gc-namf-communication` (3), `tamoss` (2) |  |  |  |
| items | both | Schema Object.items | golden | census `schema.items`: 6544 declarations in 103 fixtures — `airbyte.local-config` (69), `amazonaws.com-cloudformation` (98), `amazonaws.com-cloudfront` (22), `anchore.io` (92), `apache.org` (53), `apache.org-airflow` (53), `apache.org-qakka` (3), `apicurio.local-registry` (24), `apideck.com-accounting` (53), `apideck.com-ats` (18), `apideck.com-connector` (32), `apideck.com-crm` (37), `apideck.com-customer-support` (27), `apideck.com-ecommerce` (24), `apideck.com-ecosystem` (11), `apideck.com-file-storage` (7), `apideck.com-hris` (29), `apideck.com-issue-tracking` (9), `apideck.com-lead` (9), `apideck.com-pos` (35), `apideck.com-sms` (3), `apideck.com-vault` (25), `apideck.com-webhook` (8), `apis.guru` (3), `appng-rest-api` (27), `appwrite.io-client` (36), `appwrite.io-server` (49), `asana.com` (109), `atlassian.com-jira` (451), `audience-filter` (1), `audience-filter-strict` (1), `axesso.de` (5), `bbci.co.uk` (20), `bintable.com` (2), `box.com` (216), `buildrelay` (5), `bungie.net` (446), `bunq.com` (329), `byautomata.io` (11), `canada-holidays.ca` (4), `client-class-name` (1), `codesearch.debian.net` (5), `color.pizza` (3), `conjur.local` (17), `corrently.io` (14), `discourse.local` (228), `dnd5eapi.co` (78), `electric-sql` (7), `eos.local` (1), `eos.local-extra-fields-forbid` (1), `eozilla` (23), `error-responses` (1), `etherpad.local` (18), `etsi.local-mec010-2_apppkgmgmt` (33), `exa-gate` (2), `exhaustive` (16), `frankfurter` (6), `free5gc-namf-communication` (52), `free5gc-pdu-session` (40), `gambitcomm.local-mimic` (118), `github.com` (1005), `gov.bc.ca-news` (44), `groundhog-day.com` (3), `helios-verifiable-api` (8), `inline-array-request` (2), `inline-request-response` (1), `kytos-sdntrace-cp` (1), `letta` (393), `livepeer-ai-runner` (9), `maif.local-otoroshi` (71), `malformed-property-schema` (1), `med-anvisa-price` (1), `microcks.local` (26), `missing-operation-id` (1), `netbox.dev` (333), `nimisampo` (14), `oauth-client-credentials` (1), `openbanking.org.uk-account-info-openapi` (205), `openepcis-dpp-ready` (9), `openfigi.com` (6), `operation-id-non-identifier` (1), `portfoliooptimizer.io` (520), `prometheus-x-edge-computing` (2), `pydantic-extra-fields` (1), `query-parameters-openapi` (6), `recursive-types` (2), `redhat.com-catalog_inventory` (18), `redocly.com-museum` (3), `reverb.com` (28), `sac-backend` (3), `schema-constraints` (1), `sigstore-rekor` (11), `slurmdb-rest` (75), `squareup.com` (423), `tag-based-grouping` (2), `tamoss` (30), `tlon-notes` (10), `traccar.org` (41), `twilio.com-twilio_messaging_v1` (28), `twilio.com-twilio_voice_v1` (9), `withsecure-gdpr-subject-rights` (4), `worldcoin-signup-sequencer` (5), `xero.com-xero-payroll-au` (67) |  |  |  |
| properties | both | Schema Object.properties | golden | census `schema.properties`: 12547 declarations in 121 fixtures — `6-dot-authentiqio.appspot.com` (17), `airbyte.local-config` (164), `amazonaws.com-cloudformation` (207), `amazonaws.com-cloudfront` (182), `anchore.io` (130), `apache.org` (81), `apache.org-airflow` (81), `apache.org-qakka` (3), `apicurio.local-registry` (30), `apideck.com-accounting` (134), `apideck.com-ats` (40), `apideck.com-connector` (41), `apideck.com-crm` (82), `apideck.com-customer-support` (31), `apideck.com-ecommerce` (56), `apideck.com-ecosystem` (32), `apideck.com-file-storage` (66), `apideck.com-hris` (79), `apideck.com-issue-tracking` (47), `apideck.com-lead` (30), `apideck.com-pos` (106), `apideck.com-proxy` (4), `apideck.com-sms` (23), `apideck.com-vault` (56), `apideck.com-webhook` (27), `apis.guru` (6), `appng-rest-api` (27), `appwrite.io-client` (54), `appwrite.io-server` (65), `asana.com` (379), `atlassian.com-jira` (535), `audience-filter` (3), `audience-filter-strict` (4), `auth-schemes` (2), `axesso.de` (5), `bbci.co.uk` (85), `bintable.com` (1), `box.com` (513), `bracketed-property-names` (2), `buildrelay` (6), `bungie.net` (746), `bunq.com` (552), `byautomata.io` (19), `canada-holidays.ca` (15), `client-class-name` (1), `codesearch.debian.net` (2), `color.pizza` (15), `conjur.local` (21), `cookie-parameters` (1), `corrently.io` (28), `digit-leading-property` (1), `discourse.local` (274), `discriminated-unions` (2), `dnd5eapi.co` (104), `electric-sql` (13), `enum-name-sanitization` (1), `enum-query-param` (1), `enum-receiver-collision` (1), `eos.local` (8), `eos.local-extra-fields-forbid` (8), `eozilla` (23), `error-responses` (2), `esgenterprise.com` (1), `etherpad.local` (456), `etsi.local-mec010-2_apppkgmgmt` (30), `exa-gate` (7), `exhaustive` (19), `form-bodies` (4), `frankfurter` (8), `free5gc-namf-communication` (92), `free5gc-pdu-session` (86), `gambitcomm.local-mimic` (24), `github.com` (3414), `gov.bc.ca-news` (23), `groundhog-day.com` (16), `helios-verifiable-api` (15), `http-toolkit` (3), `inline-array-request` (2), `inline-request-response` (7), `integer-enums` (1), `khoainats` (2), `kytos-sdntrace-cp` (12), `letta` (534), `livepeer-ai-runner` (33), `maif.local-otoroshi` (88), `malformed-property-schema` (1), `med-anvisa-price` (2), `microcks.local` (39), `nested-core-imports` (2), `netbox.dev` (406), `nimisampo` (10), `oauth-client-credentials` (3), `openbanking.org.uk-account-info-openapi` (271), `openepcis-dpp-ready` (16), `openfigi.com` (5), `operation-id-non-identifier` (1), `portfoliooptimizer.io` (312), `prometheus-x-edge-computing` (12), `pydantic-extra-fields` (1), `query-parameters-openapi` (2), `recursive-types` (3), `redhat.com-catalog_inventory` (35), `redocly.com-museum` (7), `reverb.com` (42), `sac-backend` (20), `schema-constraints` (2), `servers-webhooks` (3), `sigstore-rekor` (76), `slurmdb-rest` (122), `squareup.com` (660), `sse-streaming` (1), `tag-based-grouping` (2), `tamoss` (71), `tlon-notes` (73), `traccar.org` (35), `twilio.com-twilio_messaging_v1` (46), `twilio.com-twilio_voice_v1` (38), `withsecure-gdpr-subject-rights` (15), `worldcoin-signup-sequencer` (7), `writeonly-fields` (1), `xero.com-xero-payroll-au` (54) |  |  |  |
| additional-properties-boolean-true | both | Schema Object.additionalProperties | golden | variant scan `additionalProperties=true`: 219 declarations in 32 fixtures — `airbyte.local-config` (5), `anchore.io` (10), `apideck.com-accounting` (3), `apideck.com-ats` (1), `apideck.com-connector` (1), `apideck.com-crm` (1), `apideck.com-customer-support` (1), `apideck.com-ecommerce` (1), `apideck.com-file-storage` (2), `apideck.com-hris` (1), `apideck.com-issue-tracking` (2), `apideck.com-lead` (1), `apideck.com-pos` (1), `apideck.com-sms` (1), `apideck.com-vault` (5), `apideck.com-webhook` (4), `appwrite.io-client` (2), `appwrite.io-server` (2), `atlassian.com-jira` (47), `discourse.local` (3), `dnd5eapi.co` (3), `eozilla` (1), `etsi.local-mec010-2_apppkgmgmt` (1), `exa-gate` (1), `github.com` (16), `letta` (93), `microcks.local` (3), `openbanking.org.uk-account-info-openapi` (1), `openepcis-dpp-ready` (1), `servers-webhooks` (1), `sigstore-rekor` (2), `tamoss` (2); `docs/fern-limitations.md` `boolean-schema-true`: coincidence (`additionalProperties`, `items`) / discards (property position) |  |  |  |
| additional-properties-boolean-false | both | Schema Object.additionalProperties | golden | variant scan `additionalProperties=false`: 1177 declarations in 27 fixtures — `airbyte.local-config` (6), `apideck.com-accounting` (32), `apideck.com-ats` (13), `apideck.com-connector` (4), `apideck.com-crm` (25), `apideck.com-customer-support` (12), `apideck.com-ecommerce` (15), `apideck.com-ecosystem` (17), `apideck.com-file-storage` (19), `apideck.com-hris` (20), `apideck.com-issue-tracking` (16), `apideck.com-lead` (10), `apideck.com-pos` (17), `apideck.com-sms` (3), `apideck.com-vault` (12), `apideck.com-webhook` (5), `apis.guru` (3), `atlassian.com-jira` (441), `bbci.co.uk` (79), `discourse.local` (185), `eozilla` (1), `exa-gate` (7), `github.com` (38), `letta` (78), `openbanking.org.uk-account-info-openapi` (99), `redhat.com-catalog_inventory` (15), `tamoss` (5) |  |  |  |
| additional-properties-schema | both | Schema Object.additionalProperties | golden | variant scan `additionalProperties=schema`: 534 declarations in 24 fixtures — `amazonaws.com-cloudformation` (1), `apicurio.local-registry` (1), `apis.guru` (2), `appng-rest-api` (7), `asana.com` (2), `atlassian.com-jira` (44), `box.com` (16), `bungie.net` (291), `dnd5eapi.co` (5), `electric-sql` (1), `eozilla` (7), `exhaustive` (10), `gambitcomm.local-mimic` (19), `github.com` (13), `helios-verifiable-api` (2), `http-toolkit` (2), `letta` (44), `livepeer-ai-runner` (2), `maif.local-otoroshi` (39), `microcks.local` (9), `query-parameters-openapi` (1), `sigstore-rekor` (3), `squareup.com` (11), `tamoss` (2); the three forms together are the census's 1930 `schema.additionalProperties` declarations |  |  |  |
| description | both | Schema Object.description | golden | census `schema.description`: 33363 declarations in 82 fixtures — `6-dot-authentiqio.appspot.com` (30), `airbyte.local-config` (117), `amazonaws.com-cloudformation` (982), `amazonaws.com-cloudfront` (444), `anchore.io` (343), `apache.org` (261), `apache.org-airflow` (261), `apache.org-qakka` (17), `apicurio.local-registry` (120), `apideck.com-accounting` (609), `apideck.com-ats` (160), `apideck.com-connector` (163), `apideck.com-crm` (370), `apideck.com-customer-support` (163), `apideck.com-ecommerce` (271), `apideck.com-ecosystem` (28), `apideck.com-file-storage` (274), `apideck.com-hris` (340), `apideck.com-issue-tracking` (197), `apideck.com-lead` (117), `apideck.com-pos` (394), `apideck.com-proxy` (7), `apideck.com-sms` (109), `apideck.com-vault` (194), `apideck.com-webhook` (111), `apis.guru` (30), `appng-rest-api` (136), `appwrite.io-client` (250), `appwrite.io-server` (285), `asana.com` (537), `atlassian.com-jira` (2470), `box.com` (2085), `buildrelay` (18), `bungie.net` (2165), `bunq.com` (2976), `byautomata.io` (6), `canada-holidays.ca` (22), `codesearch.debian.net` (8), `conjur.local` (35), `corrently.io` (98), `discourse.local` (56), `dnd5eapi.co` (258), `electric-sql` (51), `eos.local` (30), `eos.local-extra-fields-forbid` (30), `eozilla` (2), `etsi.local-mec010-2_apppkgmgmt` (119), `exhaustive` (9), `frankfurter` (34), `gambitcomm.local-mimic` (4), `github.com` (6023), `groundhog-day.com` (3), `helios-verifiable-api` (4), `http-toolkit` (3), `kytos-sdntrace-cp` (28), `letta` (2283), `livepeer-ai-runner` (102), `maif.local-otoroshi` (532), `med-anvisa-price` (1), `microcks.local` (210), `netbox.dev` (289), `nimisampo` (14), `openbanking.org.uk-account-info-openapi` (938), `openepcis-dpp-ready` (50), `openfigi.com` (4), `portfoliooptimizer.io` (555), `prometheus-x-edge-computing` (31), `redhat.com-catalog_inventory` (17), `redocly.com-museum` (23), `reverb.com` (152), `sac-backend` (99), `sigstore-rekor` (158), `slurmdb-rest` (381), `squareup.com` (2695), `tamoss` (253), `tlon-notes` (28), `traccar.org` (34), `twilio.com-twilio_messaging_v1` (271), `twilio.com-twilio_voice_v1` (114), `withsecure-gdpr-subject-rights` (20), `worldcoin-signup-sequencer` (10), `xero.com-xero-payroll-au` (242) |  |  |  |
| format | both | Schema Object.format | golden | census `schema.format`: 20862 declarations in 81 fixtures — `6-dot-authentiqio.appspot.com` (1), `airbyte.local-config` (60), `amazonaws.com-cloudformation` (4), `amazonaws.com-cloudfront` (1), `anchore.io` (41), `apache.org` (68), `apache.org-airflow` (68), `apache.org-qakka` (5), `apicurio.local-registry` (37), `apideck.com-accounting` (24), `apideck.com-ats` (10), `apideck.com-connector` (6), `apideck.com-crm` (22), `apideck.com-customer-support` (19), `apideck.com-ecommerce` (5), `apideck.com-ecosystem` (11), `apideck.com-file-storage` (6), `apideck.com-hris` (27), `apideck.com-issue-tracking` (6), `apideck.com-lead` (1), `apideck.com-pos` (17), `apideck.com-sms` (5), `apideck.com-vault` (5), `apideck.com-webhook` (6), `apis.guru` (6), `appng-rest-api` (6), `appwrite.io-client` (72), `appwrite.io-server` (82), `asana.com` (80), `atlassian.com-jira` (906), `axesso.de` (6), `bbci.co.uk` (3), `box.com` (410), `buildrelay` (2), `bungie.net` (2050), `canada-holidays.ca` (4), `codesearch.debian.net` (1), `conjur.local` (2), `cookie-parameters` (1), `corrently.io` (2), `discourse.local` (1), `discriminated-unions` (2), `electric-sql` (1), `eozilla` (15), `esgenterprise.com` (5), `etsi.local-mec010-2_apppkgmgmt` (13), `exhaustive` (22), `form-bodies` (1), `frankfurter` (12), `free5gc-namf-communication` (84), `free5gc-pdu-session` (134), `gambitcomm.local-mimic` (484), `github.com` (14325), `gov.bc.ca-news` (16), `inline-request-response` (2), `integer-enums` (1), `letta` (106), `livepeer-ai-runner` (6), `maif.local-otoroshi` (96), `microcks.local` (12), `netbox.dev` (834), `nimisampo` (2), `openbanking.org.uk-account-info-openapi` (53), `openepcis-dpp-ready` (6), `openfigi.com` (1), `query-parameters-openapi` (4), `redhat.com-catalog_inventory` (70), `redocly.com-museum` (10), `reverb.com` (18), `sac-backend` (25), `schema-constraints` (2), `sigstore-rekor` (35), `slurmdb-rest` (1), `squareup.com` (42), `tamoss` (19), `traccar.org` (28), `twilio.com-twilio_messaging_v1` (98), `twilio.com-twilio_voice_v1` (78), `worldcoin-signup-sequencer` (1), `writeonly-fields` (3), `xero.com-xero-payroll-au` (106); the per-value rows below classify each 2020-12 registry format separately |  |  |  |
| default | both | Schema Object.default | golden | census `schema.default`: 2552 declarations in 57 fixtures — `airbyte.local-config` (12), `anchore.io` (11), `apache.org` (15), `apache.org-airflow` (15), `apache.org-qakka` (2), `apicurio.local-registry` (4), `apideck.com-accounting` (3), `apideck.com-ats` (2), `apideck.com-connector` (1), `apideck.com-crm` (3), `apideck.com-customer-support` (2), `apideck.com-ecommerce` (2), `apideck.com-ecosystem` (1), `apideck.com-file-storage` (3), `apideck.com-hris` (3), `apideck.com-issue-tracking` (4), `apideck.com-lead` (3), `apideck.com-pos` (4), `apideck.com-proxy` (1), `apideck.com-sms` (2), `apideck.com-vault` (12), `apideck.com-webhook` (1), `appwrite.io-client` (56), `appwrite.io-server` (69), `asana.com` (6), `atlassian.com-jira` (237), `axesso.de` (2), `bbci.co.uk` (3), `box.com` (35), `byautomata.io` (2), `canada-holidays.ca` (8), `codesearch.debian.net` (3), `conjur.local` (5), `discourse.local` (2), `electric-sql` (2), `eozilla` (16), `frankfurter` (1), `free5gc-namf-communication` (5), `free5gc-pdu-session` (16), `github.com` (1090), `gov.bc.ca-news` (35), `http-toolkit` (6), `letta` (503), `livepeer-ai-runner` (54), `netbox.dev` (136), `nimisampo` (11), `openepcis-dpp-ready` (1), `openfigi.com` (1), `portfoliooptimizer.io` (89), `redhat.com-catalog_inventory` (5), `redocly.com-museum` (2), `reverb.com` (21), `sac-backend` (2), `schema-constraints` (2), `sigstore-rekor` (1), `tamoss` (18), `tlon-notes` (1) |  |  |  |
| nullable | 3.0 | Schema Object.nullable | golden | census `schema.nullable`: 7540 declarations in 38 fixtures — `anchore.io` (27), `apache.org` (123), `apache.org-airflow` (123), `apideck.com-accounting` (280), `apideck.com-ats` (76), `apideck.com-connector` (9), `apideck.com-crm` (201), `apideck.com-customer-support` (150), `apideck.com-ecommerce` (56), `apideck.com-ecosystem` (5), `apideck.com-file-storage` (13), `apideck.com-hris` (124), `apideck.com-issue-tracking` (61), `apideck.com-lead` (61), `apideck.com-pos` (104), `apideck.com-sms` (14), `apideck.com-vault` (33), `apideck.com-webhook` (13), `asana.com` (68), `atlassian.com-jira` (7), `bbci.co.uk` (1), `box.com` (364), `buildrelay` (2), `eozilla` (2), `exhaustive` (25), `free5gc-namf-communication` (3), `free5gc-pdu-session` (4), `github.com` (4343), `groundhog-day.com` (1), `letta` (105), `netbox.dev` (823), `nimisampo` (8), `openfigi.com` (23), `redhat.com-catalog_inventory` (1), `sac-backend` (5), `tlon-notes` (6), `twilio.com-twilio_messaging_v1` (189), `twilio.com-twilio_voice_v1` (87) |  |  |  |
| discriminator | both | Schema Object.discriminator | golden | census `schema.discriminator`: 99 declarations in 11 fixtures — `apache.org` (1), `apache.org-airflow` (1), `appng-rest-api` (1), `atlassian.com-jira` (3), `discriminated-unions` (1), `letta` (68), `microcks.local` (1), `openepcis-dpp-ready` (1), `recursive-types` (1), `sigstore-rekor` (12), `tlon-notes` (9) |  |  |  |
| read-only | both | Schema Object.readOnly | golden | census `schema.readOnly`: 6166 declarations in 29 fixtures — `apache.org` (106), `apache.org-airflow` (106), `apideck.com-accounting` (42), `apideck.com-ats` (19), `apideck.com-connector` (9), `apideck.com-crm` (54), `apideck.com-customer-support` (36), `apideck.com-ecommerce` (7), `apideck.com-ecosystem` (20), `apideck.com-file-storage` (23), `apideck.com-hris` (26), `apideck.com-issue-tracking` (11), `apideck.com-lead` (4), `apideck.com-pos` (9), `apideck.com-sms` (17), `apideck.com-vault` (44), `apideck.com-webhook` (4), `asana.com` (167), `atlassian.com-jira` (948), `box.com` (6), `bunq.com` (2974), `github.com` (64), `gov.bc.ca-news` (3), `netbox.dev` (1318), `redhat.com-catalog_inventory` (113), `schema-constraints` (1), `sigstore-rekor` (19), `writeonly-fields` (2), `xero.com-xero-payroll-au` (14) |  |  |  |
| write-only | both | Schema Object.writeOnly | golden | census `schema.writeOnly`: 3147 declarations in 10 fixtures — `apache.org` (2), `apache.org-airflow` (2), `apideck.com-crm` (1), `apideck.com-file-storage` (2), `atlassian.com-jira` (150), `box.com` (1), `bunq.com` (2974), `schema-constraints` (2), `sigstore-rekor` (12), `writeonly-fields` (1) |  |  |  |
| xml | both | Schema Object.xml | golden | census `schema.xml`: 97 declarations in 3 fixtures — `amazonaws.com-cloudfront` (33), `atlassian.com-jira` (60), `byautomata.io` (4) |  |  |  |
| externaldocs | both | Schema Object.externalDocs | golden | census `schema.externalDocs`: 1 declarations in 1 fixture — `xero.com-xero-payroll-au` (1) |  |  |  |
| example | both | Schema Object.example | golden | census `schema.example`: 10938 declarations in 57 fixtures — `airbyte.local-config` (12), `anchore.io` (1), `apicurio.local-registry` (34), `apideck.com-accounting` (722), `apideck.com-ats` (225), `apideck.com-connector` (132), `apideck.com-crm` (569), `apideck.com-customer-support` (265), `apideck.com-ecommerce` (292), `apideck.com-ecosystem` (42), `apideck.com-file-storage` (271), `apideck.com-hris` (401), `apideck.com-issue-tracking` (236), `apideck.com-lead` (170), `apideck.com-pos` (533), `apideck.com-proxy` (9), `apideck.com-sms` (119), `apideck.com-vault` (247), `apideck.com-webhook` (116), `apis.guru` (5), `appng-rest-api` (5), `asana.com` (367), `atlassian.com-jira` (66), `axesso.de` (22), `bintable.com` (2), `box.com` (1426), `buildrelay` (2), `canada-holidays.ca` (20), `codesearch.debian.net` (7), `conjur.local` (52), `corrently.io` (28), `dnd5eapi.co` (25), `electric-sql` (8), `eozilla` (6), `etherpad.local` (1117), `frankfurter` (11), `free5gc-namf-communication` (59), `free5gc-pdu-session` (58), `github.com` (1883), `groundhog-day.com` (1), `khoainats` (2), `kytos-sdntrace-cp` (25), `maif.local-otoroshi` (430), `med-anvisa-price` (43), `microcks.local` (4), `nimisampo` (21), `redhat.com-catalog_inventory` (30), `redocly.com-museum` (22), `sac-backend` (78), `schema-constraints` (2), `slurmdb-rest` (101), `squareup.com` (346), `tamoss` (3), `tlon-notes` (9), `withsecure-gdpr-subject-rights` (15), `worldcoin-signup-sequencer` (7), `xero.com-xero-payroll-au` (234) |  |  |  |
| deprecated | both | Schema Object.deprecated | golden | census `schema.deprecated`: 219 declarations in 13 fixtures — `airbyte.local-config` (2), `amazonaws.com-cloudfront` (2), `apache.org` (1), `apache.org-airflow` (1), `apideck.com-accounting` (5), `apideck.com-crm` (2), `apideck.com-customer-support` (1), `apideck.com-hris` (1), `discourse.local` (1), `github.com` (9), `letta` (189), `schema-constraints` (1), `tamoss` (4) |  |  |  |
| dollar-schema | 3.1 | Schema Object.$schema | golden | census `schema.$schema`: 23 declarations in 1 fixture — `sigstore-rekor` (23), which is a **3.0** document (census `openapi.openapi=3.0`), so the golden pins what Fern does with the keyword in a dialect that does not define it |  |  |  |
| dollar-vocabulary | 3.1 | Schema Object.$vocabulary | gap | census `schema.$vocabulary`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"$vocabulary"' src/` finds no production read | Every module under `types/` is downstream of the dialect, so a Fern that honours a non-default `$vocabulary` could emit different models for the same document. | PROBE — no screened real-world document in the registered corpus declares `$vocabulary`, so a local probe declaring a custom dialect, recorded in `docs/fern-limitations.md`, is the only available settlement. |
| dollar-id | 3.1 | Schema Object.$id | golden | census `schema.$id`: 23 declarations in 1 fixture — `sigstore-rekor` (23), which is a **3.0** document (census `openapi.openapi=3.0`), so the golden pins what Fern does with the keyword in a dialect that does not define it |  |  |  |
| dollar-anchor | 3.1 | Schema Object.$anchor | gap | census `schema.$anchor`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"$anchor"' src/` finds no production read | A `$ref` resolved through an anchor names a different component, so the module names and cross-module imports under `types/` would differ. | PROBE — no registered source declares an anchor; a local probe pairing `$anchor` with a plain-name `$ref`, recorded in `docs/fern-limitations.md`, settles it. |
| dollar-dynamic-anchor | 3.1 | Schema Object.$dynamicAnchor | gap | census `schema.$dynamicAnchor`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"$dynamicAnchor"' src/` finds no production read | Dynamic resolution picks a different subschema per use site, so the field annotations in `types/` would differ from the static resolution crozier performs. | PROBE — recursive dynamic scoping has no witness in the registered corpus; a local probe recorded in `docs/fern-limitations.md` settles it. |
| dollar-ref | both | Schema Object.$ref | golden | census `schema.$ref`: 20335 declarations in 105 fixtures — `6-dot-authentiqio.appspot.com` (28), `airbyte.local-config` (543), `amazonaws.com-cloudformation` (1352), `amazonaws.com-cloudfront` (639), `anchore.io` (292), `apache.org` (175), `apache.org-airflow` (175), `apache.org-qakka` (11), `apicurio.local-registry` (162), `apideck.com-accounting` (393), `apideck.com-ats` (90), `apideck.com-connector` (71), `apideck.com-crm` (174), `apideck.com-customer-support` (61), `apideck.com-ecommerce` (92), `apideck.com-ecosystem` (54), `apideck.com-file-storage` (144), `apideck.com-hris` (167), `apideck.com-issue-tracking` (82), `apideck.com-lead` (36), `apideck.com-pos` (269), `apideck.com-sms` (23), `apideck.com-vault` (65), `apideck.com-webhook` (56), `apis.guru` (7), `appng-rest-api` (56), `appwrite.io-client` (61), `appwrite.io-server` (82), `asana.com` (491), `atlassian.com-jira` (1121), `audience-filter` (3), `audience-filter-strict` (4), `auth-schemes` (2), `axesso.de` (4), `bbci.co.uk` (48), `bintable.com` (2), `box.com` (1139), `buildrelay` (5), `bungie.net` (992), `bunq.com` (1628), `byautomata.io` (10), `canada-holidays.ca` (9), `client-class-name` (2), `codesearch.debian.net` (3), `color.pizza` (29), `conjur.local` (92), `cookie-parameters` (1), `corrently.io` (15), `digit-leading-property` (1), `discriminated-unions` (4), `dnd5eapi.co` (217), `enum-name-sanitization` (3), `enum-receiver-collision` (3), `eos.local` (12), `eos.local-extra-fields-forbid` (12), `eozilla` (71), `error-responses` (6), `etsi.local-mec010-2_apppkgmgmt` (109), `exa-gate` (7), `exhaustive` (61), `form-bodies` (2), `frankfurter` (5), `free5gc-namf-communication` (197), `free5gc-pdu-session` (241), `gambitcomm.local-mimic` (44), `github.com` (2411), `gov.bc.ca-news` (104), `groundhog-day.com` (5), `helios-verifiable-api` (111), `http-toolkit` (17), `inline-array-request` (1), `inline-request-response` (2), `integer-enums` (4), `khoainats` (4), `letta` (1093), `livepeer-ai-runner` (79), `maif.local-otoroshi` (267), `med-anvisa-price` (1), `microcks.local` (79), `netbox.dev` (1121), `oauth-client-credentials` (3), `openbanking.org.uk-account-info-openapi` (760), `openepcis-dpp-ready` (61), `openfigi.com` (12), `prometheus-x-edge-computing` (37), `pydantic-extra-fields` (2), `query-parameters-openapi` (10), `recursive-types` (6), `redhat.com-catalog_inventory` (145), `redocly.com-museum` (38), `sac-backend` (52), `schema-constraints` (2), `servers-webhooks` (4), `sigstore-rekor` (35), `slurmdb-rest` (175), `squareup.com` (1140), `tamoss` (156), `tlon-notes` (84), `traccar.org` (91), `twilio.com-twilio_messaging_v1` (54), `twilio.com-twilio_voice_v1` (26), `withsecure-gdpr-subject-rights` (29), `worldcoin-signup-sequencer` (18), `writeonly-fields` (2), `xero.com-xero-payroll-au` (139) |  |  |  |
| dollar-dynamic-ref | 3.1 | Schema Object.$dynamicRef | gap | census `schema.$dynamicRef`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"$dynamicRef"' src/` finds no production read | The referenced model decides the annotation and the import a `types/` module emits, so an unresolved `$dynamicRef` changes both. | PROBE — as `dollar-dynamic-anchor`, the pair is only exercisable from a local probe recorded in `docs/fern-limitations.md`. |
| dollar-defs | 3.1 | Schema Object.$defs | gap | census `schema.$defs`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"$defs"' src/` finds no production read | A `$defs` subschema is a named type, so whether Fern emits a module for it decides whether `types/` carries one and what `types/__init__.py` exports. | FIXTURE — real 3.1 documents carry `$defs`; screening one into the corpus and byte-matching its Fern golden settles it. |
| dollar-comment | 3.1 | Schema Object.$comment | gap | census `schema.$comment`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"$comment"' src/` finds no production read | `$comment` is the one schema string Fern could plausibly route into a generated docstring in `types/`, which crozier never emits. | PROBE — no registered source declares `$comment`; a local probe recorded in `docs/fern-limitations.md` settles it. |
| prefix-items | 3.1 | Schema Object.prefixItems | golden | census `schema.prefixItems`: 2 declarations in 1 fixture — `worldcoin-signup-sequencer` (2) |  |  |  |
| contains | 3.1 | Schema Object.contains | gap | census `schema.contains`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it, and the one hit `grep -rF '"contains"' src/` returns is a test document inside `src/ir.rs` | An array schema's `contains` could narrow the `typing.List[...]` element annotation a `types/` module emits. | FIXTURE — a redistributable 3.1 document declaring `contains`, registered as a corpus row whose Fern golden byte-matches, settles it. |
| pattern-properties | 3.1 | Schema Object.patternProperties | golden | census `schema.patternProperties`: 1 declarations in 1 fixture — `electric-sql` (1) |  |  |  |
| dependent-schemas | 3.1 | Schema Object.dependentSchemas | gap | census `schema.dependentSchemas`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"dependentSchemas"' src/` finds no production read | Conditional properties change which fields a generated model in `types/` declares. | FIXTURE — a 3.1 corpus row declaring `dependentSchemas` settles it. |
| property-names | 3.1 | Schema Object.propertyNames | gap | census `schema.propertyNames`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"propertyNames"' src/` finds no production read | A constrained key type could change the `typing.Dict[...]` key annotation crozier always emits as `str`. | FIXTURE — a 3.1 corpus row declaring `propertyNames` settles it. |
| if | 3.1 | Schema Object.if | golden | census `schema.if`: 1 declarations in 1 fixture — `tamoss` (1) |  |  |  |
| then | 3.1 | Schema Object.then | golden | census `schema.then`: 1 declarations in 1 fixture — `tamoss` (1) |  |  |  |
| else | 3.1 | Schema Object.else | golden | census `schema.else`: 1 declarations in 1 fixture — `tamoss` (1) |  |  |  |
| unevaluated-items | 3.1 | Schema Object.unevaluatedItems | gap | census `schema.unevaluatedItems`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"unevaluatedItems"' src/` finds no production read | The list element annotation in `types/` would differ if Fern applies the keyword to the tail a `prefixItems` schema leaves unevaluated. | FIXTURE — a 3.1 corpus row pairing `prefixItems` with `unevaluatedItems` settles it. |
| unevaluated-properties | 3.1 | Schema Object.unevaluatedProperties | golden | census `schema.unevaluatedProperties`: 3 declarations in 1 fixture — `tamoss` (3) |  |  |  |
| type-array-with-null | 3.1 | Schema Object.type | golden | variant scan `type=array-with-null`: 498 declarations in 3 fixtures — `discourse.local` (479), `frankfurter` (15), `tlon-notes` (4); all three are 3.1 documents (census `openapi.openapi=3.1`), and the count matches `docs/fern-limitations.md`'s own round-4 measurement of `type-array-nullable` (498 occurrences in 3 documents) |  |  |  |
| type-array-multi-nonnull | 3.1 | Schema Object.type | golden | variant scan `type=array-multi-nonnull`: 2 declarations in 1 fixture — `openepcis-dpp-ready` (2); `docs/fern-limitations.md` `type-array-multi-nonnull`: implements |  |  |  |
| const | 3.1 | Schema Object.const | golden | census `schema.const`: 147 declarations in 3 fixtures — `exa-gate` (1), `letta` (138), `tamoss` (8); every one is a string `const` (variant scan `const=string`, 147) |  |  |  |
| const-boolean | 3.1 | Schema Object.const | limitations | variant scan `const=boolean`: 0 declarations across all 124 registered sources; `docs/fern-limitations.md` `const-boolean`: discards |  |  |  |
| const-integer | 3.1 | Schema Object.const | limitations | variant scan `const=integer`: 0 declarations across all 124 registered sources; `docs/fern-limitations.md` `const-integer`: discards |  |  |  |
| enum-member-float | both | Schema Object.enum | limitations | variant scan `enum-member=float`: 0 declarations across all 124 registered sources (the member kinds declared are string, integer, boolean and null); `docs/fern-limitations.md` `enum-member-float`: discards + supply |  |  |  |
| enum-member-object | both | Schema Object.enum | limitations | variant scan `enum-member=object`: 0 declarations across all 124 registered sources; `docs/fern-limitations.md` `enum-member-object`: discards + supply |  |  |  |
| max-contains | 3.1 | Schema Object.maxContains | gap | census `schema.maxContains`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"maxContains"' src/` finds no production read | The bound lands in the same `types/` list annotation `maxItems` does, and crozier reads neither. | FIXTURE — a 3.1 corpus row pairing `contains` with `maxContains` settles it. |
| min-contains | 3.1 | Schema Object.minContains | gap | census `schema.minContains`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"minContains"' src/` finds no production read | As `max-contains`: the `types/` list annotation is the artifact at risk. | FIXTURE — a 3.1 corpus row pairing `contains` with `minContains` settles it. |
| dependent-required | 3.1 | Schema Object.dependentRequired | gap | census `schema.dependentRequired`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"dependentRequired"' src/` finds no production read | Which fields a generated model in `types/` marks optional is exactly what `required` decides, and `dependentRequired` is its conditional form. | FIXTURE — a 3.1 corpus row declaring `dependentRequired` settles it. |
| examples | 3.1 | Schema Object.examples | golden | census `schema.examples`: 230 declarations in 3 fixtures — `discourse.local` (61), `letta` (165), `openepcis-dpp-ready` (4) |  |  |  |
| format-assertion-vocabulary | 3.1 | Schema Object.format | gap | census `schema.$vocabulary`: 0 declarations across all 124 registered sources — the assertion vocabulary can only be selected through `$vocabulary`, which no source declares; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"$vocabulary"' src/` finds no production read | No generated artifact: the `types/` annotation derives from the format *value*, which the per-value rows below own, and a Python SDK asserts no format at all. | UNREACHABLE — recording that the annotation-versus-assertion split has no position in a generated Python SDK is the settlement. |
| format-date-time | both | Schema Object.format | golden | census `schema.format=date-time`: 2317 declarations in 48 fixtures — `6-dot-authentiqio.appspot.com` (1), `amazonaws.com-cloudformation` (4), `amazonaws.com-cloudfront` (1), `anchore.io` (35), `apache.org` (44), `apache.org-airflow` (44), `apicurio.local-registry` (11), `apideck.com-accounting` (14), `apideck.com-ats` (6), `apideck.com-crm` (19), `apideck.com-customer-support` (16), `apideck.com-ecommerce` (2), `apideck.com-ecosystem` (11), `apideck.com-file-storage` (3), `apideck.com-hris` (2), `apideck.com-issue-tracking` (5), `apideck.com-pos` (14), `apideck.com-sms` (4), `apideck.com-vault` (3), `apideck.com-webhook` (3), `apis.guru` (3), `asana.com` (40), `atlassian.com-jira` (23), `box.com` (155), `buildrelay` (1), `bungie.net` (76), `canada-holidays.ca` (1), `cookie-parameters` (1), `eozilla` (5), `exhaustive` (4), `free5gc-namf-communication` (5), `free5gc-pdu-session` (13), `github.com` (1145), `gov.bc.ca-news` (2), `letta` (96), `maif.local-otoroshi` (1), `microcks.local` (2), `netbox.dev` (319), `openbanking.org.uk-account-info-openapi` (30), `openepcis-dpp-ready` (1), `query-parameters-openapi` (2), `redhat.com-catalog_inventory` (64), `sac-backend` (6), `tamoss` (18), `traccar.org` (27), `twilio.com-twilio_messaging_v1` (24), `twilio.com-twilio_voice_v1` (10), `writeonly-fields` (1) |  |  |  |
| format-date | both | Schema Object.format | golden | census `schema.format=date`: 88 declarations in 22 fixtures — `airbyte.local-config` (2), `apideck.com-accounting` (9), `apideck.com-ats` (2), `apideck.com-crm` (2), `apideck.com-customer-support` (2), `apideck.com-hris` (9), `apideck.com-pos` (2), `asana.com` (25), `atlassian.com-jira` (2), `canada-holidays.ca` (2), `eozilla` (1), `esgenterprise.com` (1), `exhaustive` (3), `frankfurter` (9), `github.com` (2), `netbox.dev` (6), `openfigi.com` (1), `query-parameters-openapi` (1), `redocly.com-museum` (3), `twilio.com-twilio_messaging_v1` (1), `twilio.com-twilio_voice_v1` (2), `writeonly-fields` (1) |  |  |  |
| format-time | both | Schema Object.format | golden | census `schema.format=time`: 3 declarations in 1 fixture — `maif.local-otoroshi` (3) |  |  |  |
| format-duration | both | Schema Object.format | gap | census `schema.format=duration`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` for this value — `src/ir.rs` reads `schema.format` in 10 places and names only `binary`, `byte`, `date`, `date-time`, `int64` and `uuid`; every other value falls to a catch-all that cannot tell one unnamed value from another — `_ => TypeRef::Primitive(Prim::Str)` in `base_type_ref`, `_ => return None` in `scalar_body` | A `types/` field crozier annotates `str` would differ if Fern maps this registered format to `datetime.timedelta` instead. | FIXTURE — a redistributable document declaring `format: duration`, registered as a corpus row whose Fern golden byte-matches, settles it. |
| format-email | both | Schema Object.format | golden | census `schema.format=email`: 62 declarations in 20 fixtures — `airbyte.local-config` (3), `apideck.com-accounting` (1), `apideck.com-ats` (1), `apideck.com-crm` (1), `apideck.com-customer-support` (1), `apideck.com-ecommerce` (1), `apideck.com-hris` (2), `apideck.com-issue-tracking` (1), `apideck.com-lead` (1), `apideck.com-pos` (1), `apideck.com-sms` (1), `asana.com` (1), `box.com` (2), `discourse.local` (1), `github.com` (31), `maif.local-otoroshi` (4), `netbox.dev` (4), `redocly.com-museum` (1), `sac-backend` (3), `sigstore-rekor` (1) |  |  |  |
| format-idn-email | both | Schema Object.format | gap | census `schema.format=idn-email`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` for this value — `src/ir.rs` reads `schema.format` in 10 places and names only `binary`, `byte`, `date`, `date-time`, `int64` and `uuid`; every other value falls to a catch-all that cannot tell one unnamed value from another — `_ => TypeRef::Primitive(Prim::Str)` in `base_type_ref`, `_ => return None` in `scalar_body` | A `types/` field crozier annotates `str` would differ if Fern maps this registered format to a narrower Python type, as it does for `date` and `date-time`. | FIXTURE — a redistributable document declaring `format: idn-email`, registered as a corpus row whose Fern golden byte-matches, settles it. |
| format-hostname | both | Schema Object.format | golden | census `schema.format=hostname`: 1 declarations in 1 fixture — `maif.local-otoroshi` (1) |  |  |  |
| format-idn-hostname | both | Schema Object.format | gap | census `schema.format=idn-hostname`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` for this value — `src/ir.rs` reads `schema.format` in 10 places and names only `binary`, `byte`, `date`, `date-time`, `int64` and `uuid`; every other value falls to a catch-all that cannot tell one unnamed value from another — `_ => TypeRef::Primitive(Prim::Str)` in `base_type_ref`, `_ => return None` in `scalar_body` | A `types/` field crozier annotates `str` would differ if Fern maps this registered format to a narrower Python type, as it does for `date` and `date-time`. | FIXTURE — a redistributable document declaring `format: idn-hostname`, registered as a corpus row whose Fern golden byte-matches, settles it. |
| format-ipv4 | both | Schema Object.format | golden | census `schema.format=ipv4`: 3 declarations in 1 fixture — `maif.local-otoroshi` (3) |  |  |  |
| format-ipv6 | both | Schema Object.format | gap | census `schema.format=ipv6`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` for this value — `src/ir.rs` reads `schema.format` in 10 places and names only `binary`, `byte`, `date`, `date-time`, `int64` and `uuid`; every other value falls to a catch-all that cannot tell one unnamed value from another — `_ => TypeRef::Primitive(Prim::Str)` in `base_type_ref`, `_ => return None` in `scalar_body` | A `types/` field crozier annotates `str` would differ if Fern maps this registered format to a narrower Python type, as it does for `date` and `date-time`. | FIXTURE — a redistributable document declaring `format: ipv6`, registered as a corpus row whose Fern golden byte-matches, settles it. |
| format-uuid | both | Schema Object.format | golden | census `schema.format=uuid`: 130 declarations in 17 fixtures — `airbyte.local-config` (21), `apache.org-qakka` (2), `atlassian.com-jira` (12), `box.com` (3), `buildrelay` (1), `exhaustive` (3), `free5gc-namf-communication` (11), `free5gc-pdu-session` (8), `gov.bc.ca-news` (1), `letta` (2), `maif.local-otoroshi` (2), `netbox.dev` (2), `redhat.com-catalog_inventory` (6), `redocly.com-museum` (4), `schema-constraints` (1), `writeonly-fields` (1), `xero.com-xero-payroll-au` (50) |  |  |  |
| format-uri | both | Schema Object.format | golden | census `schema.format=uri`: 9231 declarations in 22 fixtures — `airbyte.local-config` (4), `apideck.com-ats` (1), `apideck.com-connector` (5), `apideck.com-ecommerce` (2), `apideck.com-vault` (2), `apideck.com-webhook` (3), `asana.com` (13), `atlassian.com-jira` (152), `canada-holidays.ca` (1), `eozilla` (6), `etsi.local-mec010-2_apppkgmgmt` (5), `frankfurter` (3), `github.com` (8485), `letta` (5), `maif.local-otoroshi` (3), `netbox.dev` (416), `openbanking.org.uk-account-info-openapi` (6), `openepcis-dpp-ready` (5), `sigstore-rekor` (3), `tamoss` (1), `twilio.com-twilio_messaging_v1` (61), `twilio.com-twilio_voice_v1` (49) |  |  |  |
| format-uri-reference | both | Schema Object.format | golden | census `schema.format=uri-reference`: 1 declarations in 1 fixture — `eozilla` (1) |  |  |  |
| format-iri | both | Schema Object.format | gap | census `schema.format=iri`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` for this value — `src/ir.rs` reads `schema.format` in 10 places and names only `binary`, `byte`, `date`, `date-time`, `int64` and `uuid`; every other value falls to a catch-all that cannot tell one unnamed value from another — `_ => TypeRef::Primitive(Prim::Str)` in `base_type_ref`, `_ => return None` in `scalar_body` | A `types/` field crozier annotates `str` would differ if Fern maps this registered format to a narrower Python type, as it does for `date` and `date-time`. | FIXTURE — a redistributable document declaring `format: iri`, registered as a corpus row whose Fern golden byte-matches, settles it. |
| format-iri-reference | both | Schema Object.format | gap | census `schema.format=iri-reference`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` for this value — `src/ir.rs` reads `schema.format` in 10 places and names only `binary`, `byte`, `date`, `date-time`, `int64` and `uuid`; every other value falls to a catch-all that cannot tell one unnamed value from another — `_ => TypeRef::Primitive(Prim::Str)` in `base_type_ref`, `_ => return None` in `scalar_body` | A `types/` field crozier annotates `str` would differ if Fern maps this registered format to a narrower Python type, as it does for `date` and `date-time`. | FIXTURE — a redistributable document declaring `format: iri-reference`, registered as a corpus row whose Fern golden byte-matches, settles it. |
| format-uri-template | both | Schema Object.format | golden | census `schema.format=uri-template`: 4653 declarations in 1 fixture — `github.com` (4653) |  |  |  |
| format-json-pointer | both | Schema Object.format | gap | census `schema.format=json-pointer`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` for this value — `src/ir.rs` reads `schema.format` in 10 places and names only `binary`, `byte`, `date`, `date-time`, `int64` and `uuid`; every other value falls to a catch-all that cannot tell one unnamed value from another — `_ => TypeRef::Primitive(Prim::Str)` in `base_type_ref`, `_ => return None` in `scalar_body` | A `types/` field crozier annotates `str` would differ if Fern maps this registered format to a narrower Python type, as it does for `date` and `date-time`. | FIXTURE — a redistributable document declaring `format: json-pointer`, registered as a corpus row whose Fern golden byte-matches, settles it. |
| format-relative-json-pointer | both | Schema Object.format | gap | census `schema.format=relative-json-pointer`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` for this value — `src/ir.rs` reads `schema.format` in 10 places and names only `binary`, `byte`, `date`, `date-time`, `int64` and `uuid`; every other value falls to a catch-all that cannot tell one unnamed value from another — `_ => TypeRef::Primitive(Prim::Str)` in `base_type_ref`, `_ => return None` in `scalar_body` | A `types/` field crozier annotates `str` would differ if Fern maps this registered format to a narrower Python type, as it does for `date` and `date-time`. | PROBE — the value is vanishingly rare in real documents, so a local probe recorded in `docs/fern-limitations.md` is the practical settlement. |
| format-regex | both | Schema Object.format | golden | census `schema.format=regex`: 1 declarations in 1 fixture — `eozilla` (1) |  |  |  |
| format-int32 | both | Schema Object.format | golden | census `schema.format=int32`: 2205 declarations in 18 fixtures — `airbyte.local-config` (1), `anchore.io` (1), `apache.org-qakka` (1), `apicurio.local-registry` (1), `appng-rest-api` (6), `appwrite.io-client` (65), `appwrite.io-server` (77), `atlassian.com-jira` (215), `box.com` (7), `bungie.net` (1201), `free5gc-namf-communication` (45), `free5gc-pdu-session` (64), `gambitcomm.local-mimic` (477), `gov.bc.ca-news` (10), `maif.local-otoroshi` (31), `microcks.local` (1), `openbanking.org.uk-account-info-openapi` (1), `xero.com-xero-payroll-au` (1) |  |  |  |
| format-int64 | both | Schema Object.format | golden | census `schema.format=int64`: 1046 declarations in 20 fixtures — `airbyte.local-config` (26), `apache.org-qakka` (1), `apicurio.local-registry` (24), `atlassian.com-jira` (494), `axesso.de` (6), `bbci.co.uk` (2), `box.com` (191), `bungie.net` (189), `exhaustive` (3), `free5gc-pdu-session` (3), `github.com` (6), `gov.bc.ca-news` (1), `integer-enums` (1), `maif.local-otoroshi` (39), `microcks.local` (3), `openbanking.org.uk-account-info-openapi` (1), `sac-backend` (12), `slurmdb-rest` (1), `squareup.com` (42), `worldcoin-signup-sequencer` (1); `int_prim` in `src/ir.rs` reads this value by name and maps it to `Prim::Long` |  |  |  |
| format-float | both | Schema Object.format | golden | census `schema.format=float`: 51 declarations in 7 fixtures — `appwrite.io-client` (3), `appwrite.io-server` (3), `bungie.net` (10), `openbanking.org.uk-account-info-openapi` (15), `redocly.com-museum` (1), `reverb.com` (18), `sac-backend` (1) |  |  |  |
| format-double | both | Schema Object.format | golden | census `schema.format=double`: 102 declarations in 13 fixtures — `apideck.com-hris` (14), `atlassian.com-jira` (6), `bbci.co.uk` (1), `bungie.net` (4), `corrently.io` (2), `discriminated-unions` (2), `esgenterprise.com` (4), `exhaustive` (4), `inline-request-response` (2), `maif.local-otoroshi` (9), `microcks.local` (2), `schema-constraints` (1), `xero.com-xero-payroll-au` (51) |  |  |  |
| format-password | both | Schema Object.format | golden | census `schema.format=password`: 7 declarations in 5 fixtures — `apache.org` (1), `apache.org-airflow` (1), `conjur.local` (1), `sac-backend` (3), `traccar.org` (1) |  |  |  |
| format-byte | 3.0 | Schema Object.format | golden | census `schema.format=byte`: 61 declarations in 8 fixtures — `apache.org-qakka` (1), `atlassian.com-jira` (1), `bungie.net` (5), `exhaustive` (3), `free5gc-namf-communication` (9), `free5gc-pdu-session` (12), `gov.bc.ca-news` (2), `sigstore-rekor` (28); 3.1 keeps no such format, replacing it with the `content-encoding` row's keyword; `scalar_body` in `src/ir.rs` reads this value by name |  |  |  |
| format-binary | 3.0 | Schema Object.format | golden | census `schema.format=binary`: 88 declarations in 19 fixtures — `airbyte.local-config` (3), `anchore.io` (2), `apicurio.local-registry` (1), `apideck.com-file-storage` (3), `asana.com` (1), `atlassian.com-jira` (1), `box.com` (8), `eozilla` (1), `etsi.local-mec010-2_apppkgmgmt` (2), `exhaustive` (1), `form-bodies` (1), `free5gc-namf-communication` (14), `free5gc-pdu-session` (34), `github.com` (1), `letta` (3), `livepeer-ai-runner` (6), `microcks.local` (3), `nimisampo` (2), `redocly.com-museum` (1); 3.1 keeps no such format, replacing it with the `content-media-type` row's keyword; `src/ir.rs` reads this value by name in 8 of its 10 `schema.format` reads |  |  |  |
| content-encoding | 3.1 | Schema Object.contentEncoding | golden | census `schema.contentEncoding`: 1 declaration in 1 fixture — `marimo` (1), pinned by corpus row 95 |  |  |  |
| content-media-type | 3.1 | Schema Object.contentMediaType | gap | census `schema.contentMediaType`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"contentMediaType"' src/` finds no production read | As `content-encoding`: the `types/` field annotation for the embedded document is the artifact at risk. | FIXTURE — a 3.1 corpus row declaring `contentMediaType` settles it. |
| content-schema | 3.1 | Schema Object.contentSchema | gap | census `schema.contentSchema`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — `src/openapi.rs`'s `Schema` declares no field for it and `grep -rF '"contentSchema"' src/` finds no production read | A `contentSchema` names a model for an embedded document, so `types/` could carry a module crozier never emits. | FIXTURE — a 3.1 corpus row declaring `contentSchema` settles it. |
| boolean-schema-true | 3.1 | Schema Object (boolean form) | limitations | variant scan: 0 declarations of a literal `true` schema in any position other than `additionalProperties` across all 124 registered sources (the `additionalProperties` position is the `additional-properties-boolean-true` row); `docs/fern-limitations.md` `boolean-schema-true`: coincidence (`additionalProperties`, `items`) / discards (property position) |  |  |  |
| boolean-schema-false | 3.1 | Schema Object (boolean form) | golden | variant scan `boolean-schema=false@schema.unevaluatedProperties`: 3 declarations in 1 fixture — `tamoss` (3) — the only literal `false` schema any registered source declares outside the `additionalProperties` position that `additional-properties-boolean-false` owns |  |  |  |
| ref-siblings | both | Schema Object.$ref | golden | variant scan `ref-siblings`: 1080 declarations in 20 fixtures — `airbyte.local-config` (5), `apache.org` (11), `apache.org-airflow` (11), `apicurio.local-registry` (24), `apideck.com-hris` (1), `asana.com` (20), `atlassian.com-jira` (1), `bunq.com` (853), `corrently.io` (1), `dnd5eapi.co` (4), `exhaustive` (4), `helios-verifiable-api` (1), `letta` (53), `maif.local-otoroshi` (10), `microcks.local` (18), `redocly.com-museum` (3), `sac-backend` (2), `tamoss` (43), `twilio.com-twilio_messaging_v1` (14), `worldcoin-signup-sequencer` (1); the sibling keywords declared are `description` (1037), `readOnly` (874), `type` (874), `writeOnly` (853), `default` (29), `nullable` (28), `deprecated` (2), `allOf` (1) and `example` (1). OAS 3.0 defines the siblings as ignored and 3.1 allows them, so the row is `both`: `letta`, `redocly.com-museum`, `tamoss` and `worldcoin-signup-sequencer` are the 3.1 documents among the twenty |  |  |  |
| recursive-graph | both | Schema Object.$ref | golden | variant scan `self-recursive-schema`: 21 declarations in 11 fixtures — `apideck.com-connector` (1), `appng-rest-api` (4), `atlassian.com-jira` (3), `bbci.co.uk` (1), `bungie.net` (3), `bunq.com` (3), `corrently.io` (1), `dnd5eapi.co` (1), `eozilla` (2), `recursive-types` (1), `tlon-notes` (1) — component schemas that reference themselves |  |  |  |
| mutually-recursive-graph | both | Schema Object.$ref | golden | variant scan `mutually-recursive-schema`: 13 declarations in 9 fixtures — `apideck.com-accounting` (1), `atlassian.com-jira` (2), `bunq.com` (1), `canada-holidays.ca` (1), `dnd5eapi.co` (1), `groundhog-day.com` (1), `openepcis-dpp-ready` (2), `recursive-types` (1), `squareup.com` (3) — reference cycles closed through two or more distinct component schemas |  |  |  |
| cycle-via-additionalProperties | both | Schema Object.additionalProperties | golden | variant scan `cycle-via-additionalProperties`: 2 declarations in 2 fixtures — `appng-rest-api` (1), `eozilla` (1); `docs/fern-limitations.md` `cycle-via-additionalProperties`: implements |  |  |  |
| nesting-depth-ge-15 | both | Schema Object (inline nesting depth) | golden | variant scan `schema-depth>=15`: 91 declarations in 1 fixture — `openbanking.org.uk-account-info-openapi` (91); `docs/fern-limitations.md` `nesting-depth-ge-15`: implements — the same 91 nodes that file measured |  |  |  |
| all-of-nested-composition | both | Schema Object.allOf | golden | variant scan `allOf-nested-in-composition`: 6 declarations in 3 fixtures — `box.com` (3), `exhaustive` (2), `tamoss` (1) — `allOf` declared on a schema that is itself a member of an `allOf`, `anyOf`, `oneOf` or `not` |  |  |  |
| any-of-nested-composition | both | Schema Object.anyOf | golden | variant scan `anyOf-nested-in-composition`: 2 declarations in 2 fixtures — `box.com` (1), `free5gc-namf-communication` (1) — `anyOf` declared on a schema that is itself a member of an `allOf`, `anyOf`, `oneOf` or `not` |  |  |  |
| one-of-nested-composition | both | Schema Object.oneOf | golden | variant scan `oneOf-nested-in-composition`: 36 declarations in 4 fixtures — `box.com` (8), `free5gc-namf-communication` (1), `letta` (26), `sigstore-rekor` (1) — `oneOf` declared on a schema that is itself a member of an `allOf`, `anyOf`, `oneOf` or `not` |  |  |  |
| not-nested-composition | both | Schema Object.not | golden | variant scan `not-nested-in-composition`: 3 declarations in 1 fixture — `free5gc-namf-communication` (3) — `not` declared on a schema that is itself a member of an `allOf`, `anyOf`, `oneOf` or `not` |  |  |  |
| discriminator-property-name | both | Discriminator Object.propertyName | golden | census `schema.discriminator.propertyName`: 99 declarations in 11 fixtures — `apache.org` (1), `apache.org-airflow` (1), `appng-rest-api` (1), `atlassian.com-jira` (3), `discriminated-unions` (1), `letta` (68), `microcks.local` (1), `openepcis-dpp-ready` (1), `recursive-types` (1), `sigstore-rekor` (12), `tlon-notes` (9) |  |  |  |
| discriminator-mapping | both | Discriminator Object.mapping | golden | census `schema.discriminator.mapping`: 68 declarations in 7 fixtures — `atlassian.com-jira` (3), `discriminated-unions` (1), `letta` (56), `microcks.local` (1), `openepcis-dpp-ready` (1), `recursive-types` (1), `tlon-notes` (5) |  |  |  |
| xml-name | both | XML Object.name | golden | census `schema.xml.name`: 69 declarations in 3 fixtures — `amazonaws.com-cloudfront` (22), `atlassian.com-jira` (43), `byautomata.io` (4) |  |  |  |
| xml-namespace | both | XML Object.namespace | golden | census `schema.xml.namespace`: 11 declarations in 1 fixture — `amazonaws.com-cloudfront` (11) |  |  |  |
| xml-prefix | both | XML Object.prefix | gap | census `schema.xml.prefix`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — crozier never deserializes the XML Object: `src/openapi.rs`'s `Schema` has no `xml` field and `grep -rF '"xml"' src/` finds no production read | No generated artifact: `docs/fern-limitations.md` `xml-request` and `xml-response` (both `discards`, both `bodies-media` rows) measure Fern dropping XML payloads whole, so element metadata reaches no emitted Python. | UNREACHABLE — recording that the generated Python SDK has no XML serializer for the prefix to shape is the settlement. |
| xml-attribute | both | XML Object.attribute | golden | census `schema.xml.attribute`: 28 declarations in 1 fixture — `atlassian.com-jira` (28) |  |  |  |
| xml-wrapped | both | XML Object.wrapped | gap | census `schema.xml.wrapped`: 0 declarations across all 124 registered sources; no `docs/fern-limitations.md` row names it | `none` — as `xml-prefix`; the one hit `grep -rF '"wrapped"' src/` returns is a test document inside `src/ir.rs` | No generated artifact, for the reason `xml-prefix` gives: the measured Fern behaviour is to drop the XML payload that `wrapped` would shape. | UNREACHABLE — as `xml-prefix`. |

## Method notes

### What was run

    just surface-census --json      # 407 selectors, 603390 declaration sites, 124 sources
                                    # (31 vendored + 93 fetched link-ok)

Every `census …` evidence cell is a slice of that output; a single selector can
be re-checked without the whole run:

    just surface-census --selector schema.patternProperties

The joins on the measured-Fern ledger are against the key list that

    grep -oP '^\| `\K[A-Za-z0-9._-]+(?=` \| *[0-9]+ \|)' docs/fern-limitations.md | sort -u

reports, and each `limitations` row spells its verdict the way that file's
`How to read a verdict` section spells it.

### The supplementary variant scan

Twenty-five of the rows above are value kinds or graph shapes the census grammar
merges (see [above](#the-instrument-and-the-one-thing-it-cannot-see)). This scan
splits them, and it does that by **subclassing the census's own `Census`** rather
than walking documents itself: `walk` and `descend` are overridden to observe the
schema nodes the inherited traversal already reaches and then delegate to it, so
`$ref` transparency, the alias guard, MAP/LIST descent and `x-` skipping keep
their single definition in `scripts/openapi-surface-census.py`. It reads the same
sources through the same `registered_sources()` and `load_document`, and refuses
an unfetched or non-mapping source the way the census does, so a source that
reports nothing is never confused with one that declares nothing. Save it to a
scratch file and run it from the repo root, under the interpreter the census
recipes use, after `just surface-census` has fetched the `link-ok` half:

    "$(./scripts/census-python.sh)" /tmp/variant-scan.py

```python
"""Variant scan: the value kinds and graph shapes the census does not split.

Subclasses the census's own `Census`, so the traversal contract — `$ref`
transparency, the alias guard, MAP/LIST descent, `x-` skipping — keeps its single
definition in `scripts/openapi-surface-census.py` and this scan only observes the
nodes that walk already reaches. Run from the repo root under the interpreter
`scripts/census-python.sh` names, after `just surface-census` has fetched the
link-ok half.
"""
import collections, importlib.util, sys
spec = importlib.util.spec_from_file_location("c", "scripts/openapi-surface-census.py")
c = importlib.util.module_from_spec(spec); sys.modules["c"] = c; spec.loader.exec_module(c)
COMPOSITION = ("allOf", "anyOf", "oneOf", "not")
facts, sources = collections.Counter(), collections.defaultdict(collections.Counter)

class VariantCensus(c.Census):
    """The census's walk, with the value kinds and reference edges it merges noted."""

    def __init__(self, fixture):
        super().__init__()
        self.fixture, self.position, self.owner, self.depth = fixture, "openapi", None, 0
        self.edges = collections.defaultdict(set)

    def note(self, fact, n=1):
        facts[fact] += n
        sources[fact][self.fixture] += n

    def walk(self, node, kind, prefix, seen):
        """Observe a schema node, then hand it to the census's own traversal."""
        if kind == "schema":
            if isinstance(node, bool):
                return self.note(f"boolean-schema={str(node).lower()}@{self.position}")
            if isinstance(node, dict) and id(node) not in seen:
                self.note_schema(node)
        super().walk(node, kind, prefix, seen)

    def descend(self, value, child, selector, seen):
        """Carry the position, the schema depth and the owning component name down."""
        position, depth, owner = self.position, self.depth, self.owner
        self.position = selector
        if child.kind == "schema":
            self.depth += 1
        if selector == "components.schemas" and isinstance(value, dict):
            for name, entry in value.items():
                self.owner = name
                super().descend({name: entry}, child, selector, seen)
        else:
            super().descend(value, child, selector, seen)
        self.position, self.depth, self.owner = position, depth, owner

    def note_schema(self, node):
        if self.depth >= 15:
            self.note("schema-depth>=15")
        if "additionalProperties" in node:
            v = node["additionalProperties"]
            self.note("additionalProperties=" + ("true" if v is True else "false" if v is False
                      else "schema" if isinstance(v, dict) else "other"))
        for kw in ("exclusiveMaximum", "exclusiveMinimum"):
            if kw in node:
                kind = self.kind_of(node[kw])
                self.note(f"{kw}=" + ("numeric" if kind in ("integer", "float")
                          else kind if kind == "boolean" else "other"))
        t = node.get("type")
        if isinstance(t, list):
            self.note("type=array")
            if "null" in t:
                self.note("type=array-with-null")
            if len([x for x in t if x != "null"]) >= 2:
                self.note("type=array-multi-nonnull")
        elif isinstance(t, str):
            self.note("type=scalar" + ("-null" if t == "null" else ""))
        if "const" in node:
            self.note("const=" + self.kind_of(node["const"]))
        members = node.get("enum")
        if isinstance(members, list):
            for member in members:
                self.note("enum-member=" + self.kind_of(member))
        elif members is not None:  # not a list: it has no members to classify
            self.note("enum-not-a-list")
        if "$ref" in node:
            if any(k in c._SCHEMA_FIELDS for k in node if k != "$ref"):
                self.note("ref-siblings")
            target = node["$ref"]
            if self.owner and isinstance(target, str) and target.startswith("#/components/schemas/"):
                self.edges[self.owner].add((target.rsplit("/", 1)[-1],
                                            self.position == "schema.additionalProperties"))
        if self.position.endswith(COMPOSITION):
            for kw in COMPOSITION:
                if kw in node:
                    self.note(f"{kw}-nested-in-composition")

    @staticmethod
    def kind_of(value):
        for kind, test in (("boolean", bool), ("integer", int), ("float", float),
                           ("string", str), ("object", dict), ("array", list)):
            if isinstance(value, test):
                return kind
        return "null" if value is None else "other"

    def note_cycles(self):
        """Classify the `$ref` edges between component schemas into cycle facts."""
        colour, stack = {}, []
        def visit(n):
            colour[n], _ = 1, stack.append(n)
            for target, via_ap in sorted(self.edges.get(n, ())):
                if target == n:
                    self.note("self-recursive-schema")
                    if via_ap:
                        self.note("cycle-via-additionalProperties")
                elif colour.get(target) == 1:
                    self.note("mutually-recursive-schema")
                    cycle = stack[stack.index(target):]
                    if any(t == b and ap for a, b in zip(cycle, cycle[1:] + [target])
                           for t, ap in self.edges.get(a, ())):
                        self.note("cycle-via-additionalProperties")
                elif not colour.get(target):
                    visit(target)
            stack.pop(); colour[n] = 2
        sys.setrecursionlimit(20000)
        for n in sorted(self.edges):
            if not colour.get(n):
                visit(n)

registered = c.registered_sources(c.Path("tests/fixtures"), c.Path(".local/corpus"), False)
unfetched = [s.fixture for s in registered if s.path is None]
if unfetched:  # a source reporting nothing and one declaring nothing are not the same answer
    sys.exit(f"variant-scan: {len(unfetched)} registered source(s) have not been fetched, "
             f"starting with {unfetched[0]!r}. Run 'just surface-census', which fetches first.")
for s in registered:
    try:
        document = c.load_document(s.path)
    except c.DocumentError as error:
        sys.exit(f"variant-scan: {s.fixture}: {error}")
    if not isinstance(document, dict):
        sys.exit(f"variant-scan: {s.fixture}: {s.path} is not an OpenAPI document "
                 "(its root is not a mapping)")
    scan = VariantCensus(s.fixture)
    scan.walk(document, "openapi", "openapi", frozenset())
    scan.note_cycles()
for fact, n in sorted(facts.items()):
    where = ", ".join(f"{f} ({k})" for f, k in sorted(sources[fact].items()))
    k = len(sources[fact])
    print(f"{fact}: {n} declarations in {k} fixture{'s' if k != 1 else ''} — {where}")
```

**The self-check that makes it trustworthy.** For every keyword the scan splits,
its parts must add back up to the census's own count for that keyword, because
both are counting the same declaration sites:

| keyword | census | variant scan |
|---|---|---|
| `schema.additionalProperties` | 1930 | 219 `true` + 1177 `false` + 534 schema = 1930 |
| `schema.type` | 108256 | 106386 single + 1370 `"null"` single + 500 array = 108256 |
| `schema.exclusiveMinimum` | 76 | 54 boolean + 22 numeric = 76 |
| `schema.exclusiveMaximum` | 8 | 8 boolean + 0 numeric = 8 |
| `schema.const` | 147 | 147 string + 0 boolean + 0 integer = 147 |

Two of its results are corroborated by `docs/fern-limitations.md`'s own
independent round-4 counts: `type-array-with-null` at 498 occurrences in 3
documents, and `nesting-depth-ge-15` at 91 nodes in
`openbanking.org.uk-account-info-openapi`.

**Nothing gates that table, so re-run it rather than trusting it.** `just check`
runs `just test-surface-census`, which covers the census script; the subclass
above lives in this file and is nobody's test. Subclassing removes the way the two
could disagree about *which nodes exist* — there is one traversal, and a rename in
the script fails the scan loudly on the next run rather than quietly counting
something else — but the numbers in the table are still two separate runs, so the
reconciliation is to take them again, about four minutes together:

    just surface-census --json                             # the census half
    "$(./scripts/census-python.sh)" /tmp/variant-scan.py   # the scan half

Re-running is also how a maintainer learns that the corpus itself moved: a
registered row added or refreshed changes both halves, and the table above is the
count as of the run that wrote it. The follow-up in
[Two things a future maintainer should know](#two-things-a-future-maintainer-should-know)
retires the split entirely by teaching the script to emit these selectors itself.

### What the classification rests on, row by row

- **`golden`** (82 rows) — a registered source declares the feature. The evidence
  is the census, or the variant scan for the variants it cannot see.
- **`limitations`** (5 rows) — no registered source declares it and the ledger
  rules on it: `const-boolean`, `const-integer`, `enum-member-float`,
  `enum-member-object`, and `boolean-schema-true` outside the
  `additionalProperties` position.
- **`gap`** (29 rows) — neither: 20 settle with a `FIXTURE`, 6 need a `PROBE`,
  and 3 are `UNREACHABLE` — `format-assertion-vocabulary`, `xml-prefix` and
  `xml-wrapped`.

Every `gap` row's `crozier sites` cell is `none`, and each row states the `grep`
that measured it rather than resting on a list copied out of the source. The
whole-file version of that measurement — the set of wire keys crozier can read at
all — is re-derived, not restated:

    awk '/^pub struct Schema \{/,/^\}/' src/openapi.rs | grep -E 'serde\(|    pub '

Every field of that struct either carries a `rename` to its wire key or takes its
Rust name verbatim, and the two `#[serde(skip)]` fields are not wire keys at all.
Read the output as the closed set: `Schema` has no `deny_unknown_fields` and no
flattened catch-all, so serde silently drops every key outside it and no `src/`
file can reach one. Re-run the command after touching the struct; a keyword added
there turns some `gap` row's `none` into a real site.

The format rows are the one nuance, and the same rule applies:

    grep -n '\.format' src/ir.rs

returns eleven lines, one of them a doc comment and ten of them reads of
`schema.format`, and the values they name are `binary`, `byte`, `date`,
`date-time`, `int64` and `uuid`. An unnamed format is read as the keyword and
dropped as a value, which is why those rows say `none` *for this value*.

### Two things a future maintainer should know

- The census grammar carries `schema.definitions`, a Draft-4 leftover neither
  OpenAPI 3.0 nor 3.1 defines. It is not enumerated above and no registered
  source declares it.
- The variant scan lives in this document rather than in `scripts/` because
  extending the instrument was out of this classification's scope. Teaching
  `scripts/openapi-surface-census.py` to emit valued selectors for
  `schema.additionalProperties`, `schema.const`, `schema.enum` members and
  `schema.type` arity — and a selector for a boolean schema — would retire the
  scan and let those 25 rows quote `just surface-census` directly.
