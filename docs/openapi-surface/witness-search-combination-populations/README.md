# Combination population screen

This record re-acquires the candidate populations the earlier combination searches could not screen, and screens every candidate of the 22 combination keys below for its complete trigger and an admissible licence, with crozier's own census and no Fern. Its table, [`screen.tsv`](screen.tsv), is the input the four combination proof nodes generate from: one row per candidate and key, read only through `tools/witness-search/population_screen.py`'s `read_screen`, which declares the columns and admitted values and refuses a malformed, duplicate or self-contradicting row. No Fern generation ran, no corpus row was registered and no generator source changed. The [ledger-remainders record](../witness-search-ledger-remainders/README.md) stays as history; the coverage report's `search incomplete` reasons now cite this one.

A `certified-screen-pending` row is an exact trigger over admissible bytes, not a witness: its certified-pair generation and complete comparison are the proof nodes' work. The exact bytes of every such row are kept on this host in `${XDG_CACHE_HOME:-$HOME/.cache}/crozier/witness-populations/<sha256>` (`population_screen.py cached <sha256>` prints the path); elsewhere they are re-fetched from the row's `source`.

## Populations

| population | what was read | documents screened | unfetchable entries |
|---|---|---:|---:|
| `registered` | every registered corpus row's committed source document (`tests/fixtures/corpus-sources.tsv`) | 405 | 0 |
| `apis-guru` | every `openapi.*` document of the pinned APIs.guru archive, `APIs-guru/openapi-directory` at `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`; this is where the earlier census's archive declarations come from | 1970 | 0 |
| `github` | every recorded GitHub code-search identity whose exact bytes this host now holds, recovered from the shared response cache or re-fetched at its commit, and this search's code-search hits fetched the same way | 1626 | 0 |
| `sourcegraph` | every recorded Sourcegraph identity on github.com whose exact bytes this host now holds, recovered or re-fetched the same way | 572 | 0 |
| `archive` | the APIs.guru served-index versions that have no document at the archive pin (`witness-search-apis.guru/unread-responses.jsonl`) | 0 | 0 |
| `handed-off` | every handed-off document `docs/fern-measurements/handed-off/documents.tsv` names by repository, path and commit | 144 | 0 |


A candidate is a document whose bytes the key's census selector declares, or one the earlier [named census](../witness-search-ledger-remainders/census.tsv) already listed for the key; every one of that census's 749 rows has a row here. The archive's documents are named `<provider>[/<service>]/<version>`, the archive path less `APIs/` and the file name, since one service carries several versions.

## Verdicts

| key | verdict | certified-screen-pending | `registered` | `apis-guru` | `github` | `sourcegraph` | `archive` | `handed-off` | rejected-trigger | rejected-licence | unfetchable |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `combo-allof-unresolved-nested-pointer` | `search-incomplete` | 0 | 0 | 3 | 4 | 1 | 0 | 0 | 0 | 8 | 0 |
| `combo-anyof-beside-properties` | `search-incomplete` | 0 | 14 | 23 | 238 | 92 | 0 | 5 | 372 | 0 | 0 |
| `combo-array-defs-pointer` | `search-incomplete` | 0 | 1 | 0 | 13 | 19 | 0 | 0 | 33 | 0 | 0 |
| `combo-array-unresolved-nested-pointer` | `search-incomplete` | 2 | 0 | 6 | 18 | 0 | 0 | 1 | 0 | 23 | 0 |
| `combo-body-property-named-as-path-param` | `search-incomplete` | 668 | 45 | 399 | 195 | 116 | 0 | 19 | 0 | 106 | 0 |
| `combo-header-array-accepted-placements` | `search-incomplete` | 94 | 1 | 2 | 70 | 40 | 0 | 0 | 15 | 4 | 0 |
| `combo-header-string-default` | `search-incomplete` | 0 | 14 | 54 | 114 | 50 | 0 | 9 | 235 | 6 | 0 |
| `combo-map-beside-oneof` | `search-incomplete` | 5 | 9 | 3 | 121 | 74 | 0 | 8 | 209 | 1 | 0 |
| `combo-map-unresolved-nested-pointer` | `search-incomplete` | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 3 | 0 |
| `combo-nullable-allof-parent-own-property` | `search-incomplete` | 0 | 2 | 2 | 1 | 3 | 0 | 1 | 9 | 0 | 0 |
| `combo-property-anyof-composed-sibling` | `search-incomplete` | 16 | 4 | 1 | 12 | 5 | 0 | 0 | 0 | 6 | 0 |
| `combo-property-defs-pointer` | `search-incomplete` | 0 | 1 | 0 | 11 | 17 | 0 | 0 | 29 | 0 | 0 |
| `combo-property-unresolved-nested-pointer` | `search-incomplete` | 2 | 0 | 7 | 18 | 2 | 0 | 1 | 0 | 26 | 0 |
| `combo-query-param-inline-object` | `search-incomplete` | 15 | 3 | 20 | 22 | 14 | 0 | 3 | 45 | 2 | 0 |
| `combo-request-unresolved-nested-pointer` | `search-incomplete` | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `combo-required-query-array-enum-items` | `search-incomplete` | 27 | 8 | 25 | 40 | 19 | 0 | 5 | 69 | 1 | 0 |
| `combo-response-unresolved-nested-pointer` | `search-incomplete` | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 0 |
| `combo-success-anyof-nullable` | `search-incomplete` | 25 | 6 | 0 | 14 | 7 | 0 | 3 | 0 | 5 | 0 |
| `combo-success-oneof-nullable` | `search-incomplete` | 18 | 2 | 1 | 17 | 4 | 0 | 1 | 0 | 7 | 0 |
| `combo-tag-only-operation-id` | `search-incomplete` | 7 | 1 | 1 | 4 | 1 | 0 | 0 | 0 | 0 | 0 |
| `combo-unrequired-tag-anyof-reference` | `search-incomplete` | 23 | 29 | 51 | 191 | 106 | 0 | 12 | 360 | 6 | 0 |
| `combo-unrequired-tag-oneof-reference` | `search-incomplete` | 91 | 60 | 74 | 474 | 181 | 0 | 35 | 709 | 24 | 0 |


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
| `combo-unrequired-tag-oneof-reference` | `no-member-is-a-reference`, `no-referenced-member-declares-a-string-enum-property`, `members-share-no-one-valued-tag-property`, `every-member-requires-its-tag`, `union-declares-a-discriminator` |


## Missing populations

| population | what could not be had, what was tried, and why it failed |
|---|---|
| `github` | 56129 of the 59282 planned GitHub documents were never fetched: the earlier acquisition's bytes were not retained on this host, and the manager-ruled bound of about six hours of paced raw fetching was spent on higher-ranked identities first. 43 fetched ones were refused (refused-http-404 43). 713 of the planned documents are this search's own code-search hits, of which 0 were fetched. |
| `sourcegraph` | 10364 of the 10607 planned Sourcegraph documents were never fetched, on the same terms (bytes not retained on this host; the six-hour bound spent first on higher-ranked identities); 2 fetched ones were refused. The anonymous Sourcegraph search answered 29602 matches, which name no content digest to pin a fetch to, so none was planned. |
| `archive` | 98 served-index versions were acquired by an earlier run from mutable `api.apis.guru` URLs; 20 are byte-identical to registered corpus sources and are screened under `registered`, and the other 78 were not retained on this host. No immutable source names their bytes, so they were not re-fetched. |
| `handed-off` | 2 of the 146 handed-off documents record bytes only, with no repository, path or commit; their bytes were not retained on this host (not in the tree, the preflight cache or the response cache), so nothing names a source to fetch them from. |


No population above is screened whole, so each one is missing for every key; a key's count of zero pending candidates stands only beside these rows.

| key | population | why not screened whole |
|---|---|---|
| `combo-allof-unresolved-nested-pointer` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-allof-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-allof-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-allof-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-anyof-beside-properties` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-anyof-beside-properties` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-anyof-beside-properties` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-anyof-beside-properties` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-array-defs-pointer` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-array-defs-pointer` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-array-defs-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-array-defs-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-array-unresolved-nested-pointer` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-array-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-array-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-array-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-body-property-named-as-path-param` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-body-property-named-as-path-param` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-body-property-named-as-path-param` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-body-property-named-as-path-param` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-header-array-accepted-placements` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-header-array-accepted-placements` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-header-array-accepted-placements` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-header-array-accepted-placements` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-header-string-default` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-header-string-default` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-header-string-default` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-header-string-default` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-map-beside-oneof` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-map-beside-oneof` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-map-beside-oneof` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-map-beside-oneof` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-map-unresolved-nested-pointer` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-map-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-map-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-map-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-nullable-allof-parent-own-property` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-nullable-allof-parent-own-property` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-nullable-allof-parent-own-property` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-nullable-allof-parent-own-property` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-property-anyof-composed-sibling` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-property-anyof-composed-sibling` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-property-anyof-composed-sibling` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-property-anyof-composed-sibling` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-property-defs-pointer` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-property-defs-pointer` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-property-defs-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-property-defs-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-property-unresolved-nested-pointer` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-property-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-property-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-property-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-query-param-inline-object` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-query-param-inline-object` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-query-param-inline-object` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-query-param-inline-object` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-request-unresolved-nested-pointer` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-request-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-request-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-request-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-required-query-array-enum-items` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-required-query-array-enum-items` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-required-query-array-enum-items` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-required-query-array-enum-items` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-response-unresolved-nested-pointer` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-response-unresolved-nested-pointer` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-response-unresolved-nested-pointer` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-response-unresolved-nested-pointer` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-success-anyof-nullable` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-success-anyof-nullable` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-success-anyof-nullable` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-success-anyof-nullable` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-success-oneof-nullable` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-success-oneof-nullable` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-success-oneof-nullable` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-success-oneof-nullable` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-tag-only-operation-id` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-tag-only-operation-id` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-tag-only-operation-id` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-tag-only-operation-id` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-unrequired-tag-anyof-reference` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-unrequired-tag-anyof-reference` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-unrequired-tag-anyof-reference` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-unrequired-tag-anyof-reference` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |
| `combo-unrequired-tag-oneof-reference` | github | bytes not retained on this host; 56129 planned documents not re-fetched within the bound |
| `combo-unrequired-tag-oneof-reference` | sourcegraph | bytes not retained on this host; 10364 planned documents not re-fetched within the bound |
| `combo-unrequired-tag-oneof-reference` | archive | 78 served-index versions not retained on this host, behind mutable URLs |
| `combo-unrequired-tag-oneof-reference` | handed-off | 2 bytes-only documents not retained on this host, with no source recorded |


## Requests

**GitHub code search** — 32 requests, every one through `tools/witness-search/rate_limit_guard.py` and the shared response cache ([search/rate-limit-calls.jsonl](search/rate-limit-calls.jsonl)), for page 1 of each key's `path:openapi` YAML and JSON queries: 15 answered, 21 reported over 1,000 results and were recorded as partitions this bounded pass did not page, and 4 keys name no schema field a code search can spell ([search/queries.jsonl.gz](search/queries.jsonl.gz)). They yielded 713 new blob-pinned identities. The lowest remaining allowance any call reported was 8 of 10 (80%); no call fell below the guard's 40% floor, so it paused 0 times for the floor. It paused 30 times for its spacing (the code-search bucket's 10 requests a minute, 899 s in all, [search/index-pacing-waits.jsonl](search/index-pacing-waits.jsonl)). No core or contents REST request was made.

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


**Sourcegraph** — 2 anonymous search requests through the guard's paced lane, HTTP 200, HTTP 200. The first was the one attempt the manager allowed; the second was an unintended repeat by a re-run of the search command before it learned to skip a recorded answer, and asked the same query.


**Raw lane** — 2538 exact-commit downloads from raw.githubusercontent.com between 2026-11-13 05:45 UTC and 2026-11-13 07:26 UTC, through the acquirer's paced raw lane (2 s spacing; the host publishes no allowance, so no remaining figure exists to log), each logged with its status and digest in [acquisition/raw-github-calls.jsonl](acquisition/raw-github-calls.jsonl): HTTP 200 2494, HTTP 404 44. It paused 2537 times for its spacing. Every answer was written to the shared response cache. Each planned identity it reached is in [acquisition/acquisitions.jsonl](acquisition/acquisitions.jsonl) with how its bytes were had: raw 2494, refused-http-0 1, refused-http-404 44, shared-cache 336, store 665.


## Reproduce

```sh
# The acquisition plan from the committed ledgers, and the bounded live search.
uv run --locked --all-packages python tools/witness-search/witness-populations-build.py identities \
  --output docs/openapi-surface/witness-search-combination-populations/identities.tsv.gz
GITHUB_TOKEN=... uv run --locked --all-packages python tools/witness-search/witness-populations-build.py search \
  --evidence docs/openapi-surface/witness-search-combination-populations/search \
  --identities docs/openapi-surface/witness-search-combination-populations/identities.tsv.gz \
  --output docs/openapi-surface/witness-search-combination-populations/search-identities.tsv
# Exact bytes into the host store: the store, the shared cache, then the paced raw lane, by rank.
uv run --locked --all-packages python tools/witness-search/population_screen.py acquire \
  --identities <plan> --evidence docs/openapi-surface/witness-search-combination-populations/acquisition \
  --budget-seconds <seconds>
# The manifest, the screen and this README.
uv run --locked --all-packages python tools/witness-search/witness-populations-build.py manifest \
  --identities <plan> --archive <extracted openapi-directory tree>
uv run --locked --all-packages python tools/witness-search/population_screen.py screen --workers 8 --fetch-licence
uv run --locked --all-packages python tools/witness-search/witness-populations-record.py
```
