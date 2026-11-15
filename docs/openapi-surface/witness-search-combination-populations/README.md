# Combination population screen

This record re-acquires the candidate populations the earlier combination searches could not screen, and screens every candidate of the 22 combination keys below for its complete trigger and an admissible licence, with crozier's own census and no Fern. Its table, [`screen.tsv`](screen.tsv), is the input the four combination proof nodes generate from: one row per candidate and key, read only through `tools/witness-search/population_screen.py`'s `read_screen`, which declares the columns and admitted values and refuses a malformed, duplicate or self-contradicting row. No Fern generation ran, no corpus row was registered and no generator source changed. The [ledger-remainders record](../witness-search-ledger-remainders/README.md) stays as history; the coverage report's `search incomplete` reasons now cite this one.

A `certified-screen-pending` row is an exact trigger over admissible bytes, not a witness: its certified-pair generation and complete comparison are the proof nodes' work. The exact bytes of every such row are kept on this host in `${XDG_CACHE_HOME:-$HOME/.cache}/crozier/witness-populations/<sha256>` (`population_screen.py cached <sha256>` prints the path); elsewhere they are re-fetched from the row's `source`.

## Populations

| population | what was read | documents screened | unfetchable entries |
|---|---|---:|---:|
| `registered` | every registered corpus row's committed source document (`tests/fixtures/corpus-sources.tsv`) | 405 | 0 |
| `apis-guru` | every `openapi.*` document of the pinned APIs.guru archive, `APIs-guru/openapi-directory` at `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`; this is where the earlier census's archive declarations come from | 1970 | 0 |
| `github` | every recorded GitHub code-search identity whose exact bytes this host now holds, recovered from the shared response cache or re-fetched at its commit, and this search's code-search hits fetched the same way | 15108 | 930 |
| `sourcegraph` | every recorded Sourcegraph identity on github.com whose exact bytes this host now holds, recovered or re-fetched the same way | 3922 | 17 |
| `archive` | the APIs.guru served-index versions that have no document at the archive pin (`witness-search-apis.guru/unread-responses.jsonl`) | 0 | 0 |
| `handed-off` | every handed-off document `docs/fern-measurements/handed-off/documents.tsv` names by repository, path and commit | 144 | 0 |


A candidate is a document whose bytes the key's census selector declares, or one the earlier [named census](../witness-search-ledger-remainders/census.tsv) already listed for the key; every one of that census's 749 rows has a row here, as has every candidate the earlier combination searches' named censuses list (below). The archive's documents are named `<provider>[/<service>]/<version>`, the archive path less `APIs/` and the file name, since one service carries several versions.

## Earlier named censuses

Each earlier combination search's census lists candidates of these keys: [`witness-search-interaction-operation-combinations`](../witness-search-interaction-operation-combinations/census.tsv), [`witness-search-interaction-schema-combinations`](../witness-search-interaction-schema-combinations/census.tsv), [`witness-search-operation-combinations-bodies-responses`](../witness-search-operation-combinations-bodies-responses/census.tsv), [`witness-search-operation-combinations-parameters`](../witness-search-operation-combinations-parameters/census.tsv), [`witness-search-schema-combinations-models-unions-refs`](../witness-search-schema-combinations-models-unions-refs/census.tsv), [`witness-search-operation-combinations`](../witness-search-operation-combinations/census.tsv.gz), beside the ledger-remainders one. Read as this table names them, they list 13613 (key, candidate) pairs, and every one has a row. A GitHub or Sourcegraph document one names was planned at the commit and SHA-256 the census read it at ([census-identities.tsv](census-identities.tsv); a census row that kept no digest takes the one a candidate ledger read at that commit, else is pinned by the commit alone) and fetched through the guarded raw lane; where it was refused or never reached, its row is `unfetchable:<reason>` naming what was tried. A candidate named by SHA-256 alone takes the rows of the bytes held under that digest, or the row of the planned identity pinned to it; 172 rows name one that neither reaches, as `sha256:<hex>` in both `document` and `source` (under `github`: the earlier search read them from the retained raw-GitHub response cache), each `unfetchable:` with why no source is known. Two kinds of listing owe no row and are counted here only: 2 (key, fixture) pairs over 2 hand-written fixtures under `tests/fixtures/`, which are crozier's authored documents and no real-API candidate of any population here, and 4 pairs over 1 screened non-public inputs that kept no digest, which no row could name.

## Verdicts

| key | verdict | certified-screen-pending | `registered` | `apis-guru` | `github` | `sourcegraph` | `archive` | `handed-off` | rejected-trigger | rejected-licence | unfetchable |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `combo-allof-unresolved-nested-pointer` | `search-incomplete` | 3 | 0 | 3 | 216 | 8 | 0 | 0 | 0 | 19 | 205 |
| `combo-anyof-beside-properties` | `search-incomplete` | 0 | 14 | 23 | 1845 | 597 | 0 | 5 | 2213 | 4 | 267 |
| `combo-array-defs-pointer` | `search-incomplete` | 0 | 1 | 0 | 173 | 29 | 0 | 0 | 54 | 0 | 149 |
| `combo-array-unresolved-nested-pointer` | `search-incomplete` | 1 | 0 | 6 | 176 | 9 | 0 | 1 | 0 | 42 | 149 |
| `combo-body-property-named-as-path-param` | `search-incomplete` | 2354 | 45 | 410 | 4207 | 830 | 0 | 19 | 2080 | 968 | 109 |
| `combo-header-array-accepted-placements` | `search-incomplete` | 457 | 1 | 2 | 553 | 182 | 0 | 0 | 92 | 35 | 154 |
| `combo-header-string-default` | `search-incomplete` | 22 | 14 | 54 | 883 | 294 | 0 | 9 | 1071 | 65 | 96 |
| `combo-map-beside-oneof` | `search-incomplete` | 12 | 9 | 3 | 997 | 179 | 0 | 8 | 957 | 15 | 212 |
| `combo-map-unresolved-nested-pointer` | `search-incomplete` | 0 | 0 | 2 | 239 | 9 | 0 | 0 | 0 | 12 | 238 |
| `combo-nullable-allof-parent-own-property` | `search-incomplete` | 0 | 2 | 2 | 155 | 8 | 0 | 1 | 21 | 0 | 147 |
| `combo-property-anyof-composed-sibling` | `search-incomplete` | 160 | 4 | 1 | 310 | 21 | 0 | 0 | 0 | 18 | 158 |
| `combo-property-defs-pointer` | `search-incomplete` | 0 | 1 | 0 | 172 | 28 | 0 | 0 | 52 | 0 | 149 |
| `combo-property-unresolved-nested-pointer` | `search-incomplete` | 2 | 0 | 7 | 177 | 11 | 0 | 1 | 0 | 45 | 149 |
| `combo-query-param-inline-object` | `search-incomplete` | 61 | 3 | 33 | 3179 | 105 | 0 | 3 | 3013 | 17 | 232 |
| `combo-request-unresolved-nested-pointer` | `search-incomplete` | 1 | 0 | 0 | 150 | 9 | 0 | 0 | 0 | 9 | 149 |
| `combo-required-query-array-enum-items` | `search-incomplete` | 71 | 8 | 25 | 458 | 202 | 0 | 5 | 499 | 38 | 90 |
| `combo-response-unresolved-nested-pointer` | `search-incomplete` | 4 | 0 | 0 | 153 | 11 | 0 | 0 | 0 | 11 | 149 |
| `combo-success-anyof-nullable` | `search-incomplete` | 178 | 6 | 13 | 2966 | 53 | 0 | 3 | 2719 | 57 | 87 |
| `combo-success-oneof-nullable` | `search-incomplete` | 56 | 2 | 13 | 2917 | 19 | 0 | 1 | 2757 | 52 | 87 |
| `combo-tag-only-operation-id` | `search-incomplete` | 20 | 1 | 1 | 11 | 7 | 0 | 0 | 0 | 0 | 0 |
| `combo-unrequired-tag-anyof-reference` | `search-incomplete` | 135 | 29 | 51 | 1633 | 509 | 0 | 12 | 1973 | 106 | 20 |
| `combo-unrequired-tag-oneof-reference` | `search-incomplete` | 345 | 60 | 74 | 4210 | 1105 | 0 | 35 | 4763 | 276 | 100 |


Every key stays `search-incomplete`: no certified screen runs here, and each has a population below that could not be had whole. The population columns count candidate rows; the last three count rows by status.

## How a row is read

* **trigger** — each key's sites are found in the parsed document, and each site's conditions are judged in order: the census selector's own conditions first, then the earlier search's `needs` (placement, requiredness, tag and default, pointer shape) or, for the five arm keys, the arm's condition as its `combination-cooccurrence.tsv` audit row states it. `exact` is a site meeting every condition; otherwise `partial:<condition>` names the first condition the furthest site misses, and `absent` means no site exists. Nested pointers are resolved by crozier's own component-pointer walk (the census's `local_schema_pointer_target`), which follows schema keywords only. The conditions are `CONDITIONS` in the reader, listed below.
* **licence** — read as `witness_screen.py` reads one (JSON read as JSON): the document's own `info.license` decides wherever it says anything. Only a document declaring none falls back: to the corpus row's recorded grant for a registered one, to nothing for an APIs.guru archive copy (an aggregation is no publisher grant), and to its repository's licence file at the pinned commit for a GitHub, Sourcegraph or handed-off one — read from the shared response cache, fetched through the guarded raw lane only for an exact trigger, and otherwise left `unread:`.
* **status** — `unfetchable:<reason>` where neither could be read; `rejected-trigger` for a `partial:` or `absent` trigger; for an exact one, `certified-screen-pending` under an admissible licence and `rejected-licence` under an inadmissible one. The reader refuses any other pairing.

### Trigger conditions

| key | conditions, in the order judged |
|---|---|
| `combo-allof-unresolved-nested-pointer` | `pointer-not-a-nested-component-pointer`, `nested-pointer-resolves` |
| `combo-anyof-beside-properties` | `no-properties-beside-anyof`, `a-member-is-a-reference`, `members-share-no-one-valued-tag-property`, `no-property-beside-the-tag` |
| `combo-array-defs-pointer` | `items-owner-not-type-array`, `pointer-not-through-a-defs-member`, `defs-pointer-does-not-resolve`, `defs-pointer-not-through-a-properties-segment` |
| `combo-array-unresolved-nested-pointer` | `items-owner-not-type-array`, `pointer-not-a-nested-component-pointer`, `nested-pointer-resolves` |
| `combo-body-property-named-as-path-param` | `no-path-parameter`, `body-writes-no-object-properties`, `no-body-property-named-as-a-path-parameter` |
| `combo-header-array-accepted-placements` | `schema-not-type-array`, `items-are-a-reference`, `items-not-type-string` |
| `combo-header-string-default` | `schema-declares-no-default`, `default-not-a-string`, `required-header-not-type-string`, `header-is-client-managed`, `header-not-on-every-operation` |
| `combo-map-beside-oneof` | `no-additional-properties-beside-oneof`, `additional-properties-neither-a-schema-nor-true`, `properties-declared-beside-the-map` |
| `combo-map-unresolved-nested-pointer` | `map-owner-not-type-object`, `pointer-not-a-nested-component-pointer`, `nested-pointer-resolves` |
| `combo-nullable-allof-parent-own-property` | `not-type-object`, `no-allof-reference-to-a-nullable-parent`, `no-own-property-declared`, `no-own-property-shares-a-nullable-parent-property-name` |
| `combo-property-anyof-composed-sibling` | `anyof-has-fewer-than-two-non-null-members`, `no-anyof-member-is-a-oneof` |
| `combo-property-defs-pointer` | `pointer-not-through-a-defs-member`, `defs-pointer-does-not-resolve`, `defs-pointer-not-through-a-properties-segment` |
| `combo-property-unresolved-nested-pointer` | `pointer-not-a-nested-component-pointer`, `nested-pointer-resolves` |
| `combo-query-param-inline-object` | `schema-is-a-reference`, `schema-not-primary-type-object`, `schema-declares-no-properties`, `parameter-not-required` |
| `combo-request-unresolved-nested-pointer` | `pointer-not-a-nested-component-pointer`, `nested-pointer-resolves` |
| `combo-required-query-array-enum-items` | `parameter-not-required`, `schema-not-primary-type-array`, `items-not-a-reference`, `items-target-declares-no-string-enum` |
| `combo-response-unresolved-nested-pointer` | `pointer-not-a-nested-component-pointer`, `nested-pointer-resolves` |
| `combo-success-anyof-nullable` | `anyof-success-schema-not-nullable` |
| `combo-success-oneof-nullable` | `oneof-success-schema-not-nullable` |
| `combo-tag-only-operation-id` | `operation-id-not-its-first-tag-and-underscores` |
| `combo-unrequired-tag-anyof-reference` | `no-member-is-a-reference`, `no-referenced-member-declares-a-string-enum-property`, `members-share-no-one-valued-tag-property`, `every-member-requires-its-tag` |
| `combo-unrequired-tag-oneof-reference` | `no-member-is-a-reference`, `no-referenced-member-declares-a-string-enum-property`, `union-declares-a-discriminator`, `members-share-no-one-valued-tag-property`, `every-member-requires-its-tag` |


## Registered rows on an aggregation's grant alone

38 registered corpus rows declare no `info.license` and record only an aggregation's grant (or are copied from an aggregation and record no publisher's). Under the ruling corpus rows 223 and 224 were withdrawn on, an aggregation's grant is no publisher grant, so this screen reads each one `inadmissible:` wherever it is a candidate. No corpus row is changed here: whether these rows stay registered is a decision taken to the user.

| row | corpus name | spec | aggregator |
|---|---|---|---|
| 114 | `daniweb-connect` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/daniweb.com/4/openapi.yaml | APIs-guru/openapi-directory |
| 115 | `chaingateway-io` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/chaingateway.io/1.0/openapi.yaml | APIs-guru/openapi-directory |
| 116 | `hubspot-events` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/hubapi.com/events/v3/openapi.yaml | APIs-guru/openapi-directory |
| 119 | `strapi-rest-api` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/strapi.io/strapi-rest-api/5.0.0/openapi.json | jentic/jentic-public-apis |
| 120 | `listennotes` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/listennotes.com/2.0/openapi.yaml | APIs-guru/openapi-directory |
| 121 | `vtex-pricing` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/vtex.local/Pricing-API/1.0/openapi.yaml | APIs-guru/openapi-directory |
| 128 | `agco-ats` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/agco-ats.com/main/v1/openapi.json | jentic/jentic-public-apis |
| 131 | `short-io` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/short.io/main/1.0.0/openapi.json | jentic/jentic-public-apis |
| 147 | `thrivecart` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/thrivecart.com/main/1.0.0/openapi.json | jentic/jentic-public-apis |
| 149 | `fergus` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/fergus.com/fergus-api/v1/openapi.json | jentic/jentic-public-apis |
| 152 | `nextgen` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/nextgen.com/main/1.0/meta/import/input-entry.json | jentic/jentic-public-apis |
| 154 | `skool` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/skool.com/main/1.0.0/openapi.json | jentic/jentic-public-apis |
| 155 | `spendesk` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/spendesk.com/main/1.0.0/openapi.json | jentic/jentic-public-apis |
| 156 | `billie` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/billie.io/main/2.0.0/openapi.json | jentic/jentic-public-apis |
| 157 | `alma-france` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/alma_france_api/main/1.0.0/openapi.json | jentic/jentic-public-apis |
| 158 | `outreach` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/outreach.io/main/2.0/openapi.json | jentic/jentic-public-apis |
| 160 | `billie-entry` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/billie.io/main/2.0.0/meta/import/input-entry.json | jentic/jentic-public-apis |
| 161 | `skool-entry` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/skool.com/main/1.0.0/meta/import/input-entry.json | jentic/jentic-public-apis |
| 163 | `cradl` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/cradl.ai/main/2026-01-28T09%3A00%3A46Z/openapi.json | jentic/jentic-public-apis |
| 193 | `nexmo-messages` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/nexmo.com/messages-olympus/1.4.0/openapi.yaml | APIs-guru/openapi-directory |
| 195 | `mindee-ocr` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/mindee.com/main/0.1.0/openapi.json | jentic/jentic-public-apis |
| 230 | `peopledatalabs` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/peopledatalabs.com/main/5.0/openapi.json | jentic/jentic-public-apis |
| 3479 | `vtex-marketplace-protocol` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/vtex.local/Marketplace-Protocol/1.0/openapi.yaml | APIs-guru/openapi-directory |
| 4000 | `stellastra-com` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/stellastra.com/1.0/openapi.yaml | APIs-guru/openapi-directory |
| 4001 | `contribly-com` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/contribly.com/1.0.0/openapi.yaml | APIs-guru/openapi-directory |
| 4010 | `azure-databox-management` | https://raw.githubusercontent.com/jentic/jentic-public-apis/047e4ec2befca70c4bcdd05f162b2c005fc7cdfe/apis/openapi/azure.com/databoxmanagementclient/2019-09-01/openapi.json | jentic/jentic-public-apis |
| 5300 | `eqivo-apostrophe-enums` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/github.com/v0.1/openapi.yaml | APIs-guru/openapi-directory |
| 5371 | `seldon-wrapper` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/seldon.local/wrapper/0.1/openapi.yaml | APIs-guru/openapi-directory |
| 5502 | `registered-literals-apis-guru-openapi-directory-9031af6a` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/journy.io/1.0.0/openapi.yaml | APIs-guru/openapi-directory |
| 5503 | `registered-literals-apis-guru-openapi-directory-7edd79be` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/keyserv.solutions/1.4.5/openapi.yaml | APIs-guru/openapi-directory |
| 5504 | `registered-literals-apis-guru-openapi-directory-72fccf73` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/nexmo.com/external-accounts/0.1.5/openapi.yaml | APIs-guru/openapi-directory |
| 5505 | `registered-literals-apis-guru-openapi-directory-468bf5ef` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/openaq.local/2.0.0/openapi.yaml | APIs-guru/openapi-directory |
| 5507 | `registered-literals-apis-guru-openapi-directory-a0bd29a9` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/visualstudio.com/v1/openapi.yaml | APIs-guru/openapi-directory |
| 5542 | `registered-literals-jentic-jentic-public-apis-a96f8580` | https://raw.githubusercontent.com/jentic/jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/ironcladapp.com/ironclad/1/openapi.json | jentic/jentic-public-apis |
| 5600 | `registered-literals-apis-guru-openapi-directory-d8d536ea` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/unicourt.com/1.0.0/openapi.yaml | APIs-guru/openapi-directory |
| 5615 | `registered-literals-jentic-jentic-public-apis-2011299d` | https://raw.githubusercontent.com/jentic/jentic-public-apis/c72e13e0f80e71997209aba985eff6ef34869cd7/apis/openapi/assemblyai.com/main/1.3.4/meta/import/input-bundle.json | jentic/jentic-public-apis |
| 5618 | `registered-literals-apis-guru-openapi-directory-608e22dc` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/nexmo.com/subaccounts/1.0.8/openapi.yaml | APIs-guru/openapi-directory |
| 5619 | `registered-literals-apis-guru-openapi-directory-79291d99` | https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/APIs/plaid.com/2020-09-14_1.345.1/openapi.yaml | APIs-guru/openapi-directory |


## Missing populations

| population | what could not be had, what was tried, and why it failed |
|---|---|
| `github` | 46148 of the 61321 planned GitHub documents were never fetched: the earlier acquisition's bytes were not retained on this host, and the manager-ruled bound of about six hours of paced raw fetching was spent on higher-ranked identities first. 179 fetched ones were refused (refused-http-0 13, refused-http-404 166). 713 of the planned documents are this search's own code-search hits, of which 3 were fetched. Each refused document its recorded hits tie to a key, and each unfetched hit, is a candidate the table keeps; with the earlier named censuses' refused, unreached and digest-only candidates (above) they are 3018 `unfetchable:<reason>` rows naming what was tried: a refused document under the keys its recorded hits match by field name (as the plan ranks it) with the SHA-256 the ledger recorded, a hit under the key whose query found it with `-`. A ledger document never asked that no earlier census lists is tied to a key only by the plan's field-name ranking: by the manager's ruling those heuristic associations, never asked within the six-hour bound, are counted (per key, in the table below) rather than listed, and owe no row. |
| `sourcegraph` | 7223 of the 10823 planned Sourcegraph documents were never fetched, on the same terms (bytes not retained on this host; the six-hour bound spent first on higher-ranked identities); 17 fetched ones were refused, and are 78 `unfetchable:<reason>` rows of the table on the same terms. The anonymous Sourcegraph search answered 29602 matches, which name no content digest to pin a fetch to, so none was planned. |
| `archive` | 98 served-index versions were acquired by an earlier run from mutable `api.apis.guru` URLs; 20 are byte-identical to registered corpus sources and are screened under `registered`, and the other 78 were not retained on this host. No immutable source names their bytes, so they were not re-fetched. |
| `handed-off` | 2 of the 146 handed-off documents record bytes only, with no repository, path or commit; their bytes were not retained on this host (not in the tree, the preflight cache or the response cache), so nothing names a source to fetch them from. |


No population above is screened whole, so each one is missing for every key; a key's count of zero pending candidates stands only beside these rows.

| key | population | why not screened whole |
|---|---|---|
| `combo-allof-unresolved-nested-pointer` | github | bytes not retained on this host; 9513 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-allof-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 2089 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-allof-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-allof-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-anyof-beside-properties` | github | bytes not retained on this host; 13384 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-anyof-beside-properties` | sourcegraph | bytes not retained on this host; 2875 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-anyof-beside-properties` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-anyof-beside-properties` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-array-defs-pointer` | github | bytes not retained on this host; 25181 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-array-defs-pointer` | sourcegraph | bytes not retained on this host; 3593 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-array-defs-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-array-defs-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-array-unresolved-nested-pointer` | github | bytes not retained on this host; 25181 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-array-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 3593 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-array-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-array-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-body-property-named-as-path-param` | github | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-body-property-named-as-path-param` | sourcegraph | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-body-property-named-as-path-param` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-body-property-named-as-path-param` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-header-array-accepted-placements` | github | bytes not retained on this host; 40090 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-header-array-accepted-placements` | sourcegraph | bytes not retained on this host; 5034 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-header-array-accepted-placements` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-header-array-accepted-placements` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-header-string-default` | github | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-header-string-default` | sourcegraph | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-header-string-default` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-header-string-default` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-map-beside-oneof` | github | bytes not retained on this host; 7402 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-map-beside-oneof` | sourcegraph | bytes not retained on this host; 1863 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-map-beside-oneof` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-map-beside-oneof` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-map-unresolved-nested-pointer` | github | bytes not retained on this host; 5463 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-map-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 1798 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-map-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-map-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-nullable-allof-parent-own-property` | github | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-nullable-allof-parent-own-property` | sourcegraph | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-nullable-allof-parent-own-property` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-nullable-allof-parent-own-property` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-property-anyof-composed-sibling` | github | bytes not retained on this host; 1065 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-property-anyof-composed-sibling` | sourcegraph | bytes not retained on this host; 658 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-property-anyof-composed-sibling` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-property-anyof-composed-sibling` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-property-defs-pointer` | github | bytes not retained on this host; 26233 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-property-defs-pointer` | sourcegraph | bytes not retained on this host; 3751 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-property-defs-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-property-defs-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-property-unresolved-nested-pointer` | github | bytes not retained on this host; 26233 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-property-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 3751 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-property-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-property-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-query-param-inline-object` | github | bytes not retained on this host; 39972 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-query-param-inline-object` | sourcegraph | bytes not retained on this host; 5027 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-query-param-inline-object` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-query-param-inline-object` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-request-unresolved-nested-pointer` | github | bytes not retained on this host; 27512 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-request-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 3775 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-request-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-request-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-required-query-array-enum-items` | github | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-required-query-array-enum-items` | sourcegraph | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-required-query-array-enum-items` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-required-query-array-enum-items` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-response-unresolved-nested-pointer` | github | bytes not retained on this host; 27512 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-response-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 3775 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-response-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-response-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-success-anyof-nullable` | github | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-success-anyof-nullable` | sourcegraph | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-success-anyof-nullable` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-success-anyof-nullable` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-success-oneof-nullable` | github | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-success-oneof-nullable` | sourcegraph | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-success-oneof-nullable` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-success-oneof-nullable` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-tag-only-operation-id` | github | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-tag-only-operation-id` | sourcegraph | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-tag-only-operation-id` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-tag-only-operation-id` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-unrequired-tag-anyof-reference` | github | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-unrequired-tag-anyof-reference` | sourcegraph | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-unrequired-tag-anyof-reference` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-unrequired-tag-anyof-reference` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-unrequired-tag-oneof-reference` | github | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-unrequired-tag-oneof-reference` | sourcegraph | bytes not retained on this host; 0 ledger documents tied to the key by field name alone never asked within the bound (counted, not listed) |
| `combo-unrequired-tag-oneof-reference` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-unrequired-tag-oneof-reference` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |


## Requests

**GitHub code search** — 32 requests, every one through `tools/witness-search/rate_limit_guard.py` and the shared response cache ([search/rate-limit-calls.jsonl](search/rate-limit-calls.jsonl)), for page 1 of each key's `path:openapi` YAML and JSON queries: 15 answered, 21 reported over 1,000 results and were recorded as partitions this bounded pass did not page, and 4 keys name no schema field a code search can spell ([search/queries.jsonl.gz](search/queries.jsonl.gz)). They yielded 713 new blob-pinned identities. The lowest remaining allowance any call reported was 8 of 10 (80%); no call fell below the guard's 40% floor, and it paused 0 times for the floor. It paused 30 times for its spacing (one code-search request per 30 s, 899 s in all, [search/index-pacing-waits.jsonl](search/index-pacing-waits.jsonl)). No core or contents REST request was made.

| at | bucket | status | remaining | limit |
|---|---|---|---:|---:|
| 2026-11-13 05:46 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:46 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:47 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:47 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:48 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:48 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:49 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:49 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:50 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:51 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:51 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:52 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:52 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:53 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:53 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:54 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:54 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:55 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:55 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:56 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:57 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:57 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:58 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:58 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 05:59 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 05:59 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 06:00 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 06:00 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 06:03 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 06:03 UTC | code_search | 200 | 8 | 10 |
| 2026-11-13 06:04 UTC | code_search | 200 | 9 | 10 |
| 2026-11-13 06:04 UTC | code_search | 200 | 8 | 10 |


Each pause the guard took on the code-search bucket, with the allowance it last reported:

| paused at | cause | seconds | remaining allowance |
|---|---|---:|---:|
| 2026-11-13 05:46 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:47 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:47 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:48 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:48 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:49 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:49 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:50 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:50 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:51 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:52 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:52 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:53 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:53 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:54 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:54 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:55 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:55 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:56 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:57 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:57 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:58 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:58 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 05:59 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 05:59 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 06:00 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 06:00 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 06:03 UTC | spacing | 30 | 9 of 10 |
| 2026-11-13 06:04 UTC | spacing | 30 | 8 of 10 |
| 2026-11-13 06:04 UTC | spacing | 30 | 9 of 10 |


**Sourcegraph** — 2 anonymous search requests through the guard's paced lane, HTTP 200, HTTP 200. The first was the one attempt the manager allowed; the second was an unintended repeat by a re-run of the search command before it learned to skip a recorded answer, and asked the same query.


**Raw lane** — 9987 exact-commit downloads from raw.githubusercontent.com between 2026-11-13 05:45 UTC and 2026-11-13 20:24 UTC, through the acquirer's paced raw lane (2 s spacing; the host publishes no allowance, so no remaining figure exists to log), each logged with its status and digest in [acquisition/raw-github-calls.jsonl](acquisition/raw-github-calls.jsonl): HTTP 200 9798, HTTP 404 189. It paused 9911 times for its spacing. Every answer was written to the shared response cache. Each planned identity it reached is in [acquisition/acquisitions.jsonl](acquisition/acquisitions.jsonl) with how its bytes were had: raw 9873, refused-http-0 76, refused-http-404 349, shared-cache 2585, store 27627.


## Reproduce

```sh
# The acquisition plan from the committed ledgers, and the bounded live search.
uv run --locked --all-packages python tools/witness-search/witness-populations-build.py identities \
  --output docs/openapi-surface/witness-search-combination-populations/identities.tsv.gz
GITHUB_TOKEN=... uv run --locked --all-packages python tools/witness-search/witness-populations-build.py search \
  --evidence docs/openapi-surface/witness-search-combination-populations/search \
  --identities docs/openapi-surface/witness-search-combination-populations/identities.tsv.gz \
  --output docs/openapi-surface/witness-search-combination-populations/search-identities.tsv
# Every GitHub and Sourcegraph document the earlier named censuses list, at the commit they read it at.
uv run --locked --all-packages python tools/witness-search/witness-populations-build.py census \
  --output docs/openapi-surface/witness-search-combination-populations/census-identities.tsv
# Exact bytes into the host store: the store, the shared cache, then the paced raw lane, by rank.
uv run --locked --all-packages python tools/witness-search/population_screen.py acquire \
  --identities <plan> --evidence docs/openapi-surface/witness-search-combination-populations/acquisition \
  --budget-seconds <seconds>
# The manifest, the screen and this README.
uv run --locked --all-packages python tools/witness-search/witness-populations-build.py manifest \
  --identities docs/openapi-surface/witness-search-combination-populations/identities.tsv.gz \
  --identities docs/openapi-surface/witness-search-combination-populations/search-identities.tsv \
  --identities docs/openapi-surface/witness-search-combination-populations/census-identities.tsv \
  --archive <extracted openapi-directory tree>
uv run --locked --all-packages python tools/witness-search/population_screen.py screen --workers 8 --fetch-licence
uv run --locked --all-packages python tools/witness-search/witness-populations-record.py
# The suite holds this README to its evidence (`--check` exits 1 when it is stale).
uv run --locked --all-packages python tools/witness-search/witness-populations-record.py --check
```
