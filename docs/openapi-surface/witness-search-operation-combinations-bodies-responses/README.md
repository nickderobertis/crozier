# Witness search for operation combinations in bodies and responses

This bounded search covers the thirty `bodies-responses` rows owned by
`prove-operation-combinations` in [combinations.md](../combinations.md). The
certified pair is Fern CLI 5.163.1 and `fernapi/fern-python-sdk` 5.41.3.
Each key ends one of three ways here:

- **Proven by a real witness:** one admissible registered declarer, whose
  complete certified-pair golden crozier byte-matches, is output-sensitive.
  Removing the combination's feature from it moves the same generated files in
  both generators, and crozier byte-matches the certified pair's ablated tree.
- **Decided output-insensitive:** the feature moves neither generator's output
  on any document tried, a from-scratch one included. Such a key is decided, not
  proven.
- **Unproven, witness blocked:** admissible declarers the certified pair
  generates from exist, but unrelated residuals keep crozier from byte-matching
  every file the combination's removal moves. A hand-written fixture is not
  admitted while they exist, so the key stays named as unproven.

Twenty-eight keys are proven by real witnesses, three of them by corpus rows this
search registers (3470, 3471 and 3472). One key is decided output-insensitive.
One, `combo-inline-body-read-only-property`, is unproven: its witnesses are
[blocked](#blocked-witnesses).

## The search

Measured on 2026-10-24, without a new specification search:

- **APIs.guru:** `APIs-guru/openapi-directory` at
  `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, the revision the corpus's APIs.guru
  rows pin. It was read from the same extracted archive tree the
  [operation-parameter search](../witness-search-operation-combinations-parameters/README.md#the-search)
  read; no call was made.
- **Registered:** every JSON/YAML document below `tests/fixtures/` at the tree
  this record is committed with, corpus rows 3470 to 3472 included.
- **Earlier acquisitions:** the GitHub code-search and Sourcegraph documents
  that the earlier searches' `candidate-documents.json` manifests retain. Each
  is named in `census.tsv` by repository, path and full revision.

Generator-vendor and excluded repositories are dropped before counting, under
the `excluded_repository` / `normalize_repo` contract in
`tools/witness-search/witness-search-github-index.py`. No code search, portal or
registry was queried. Sixteen GitHub REST requests were made, all through
`tools/witness-search/rate_limit_guard.py` under its 40%-remaining floor and the
shared response cache: the repository licence reads in
[licences/lookup.json](licences/lookup.json), whose guard ledger is
[licences/rate-limit-calls.jsonl](licences/rate-limit-calls.jsonl). Three raw
reads of the new rows' pinned documents went through the same cache
([licences/raw-reads.jsonl](licences/raw-reads.jsonl)); each equals the
acquired copy byte for byte.

| population | JSON/YAML files read | OpenAPI 3 | other version or no root OpenAPI 3 marker | unreadable |
|---|---:|---:|---:|---:|
| `apis.guru` | 4138 | 1970 | 2168 | 0 |
| `github-code-search` | 5125 | 4787 | 285 | 53 |
| `registered` | 952 | 288 | 664 | 0 |
| `sourcegraph` | 4078 | 2852 | 1209 | 17 |

[unreadable.tsv](unreadable.tsv) keeps every unreadable input with its
diagnostic; none is counted as a zero.

### The detectors

Each key's detector is exactly its census conjunction: the `selector` cell of
its row in [`witness-search-keys.tsv`](../witness-search-keys.tsv), which the
census declares in `COMBINATIONS` and the combination-list drift test holds to
[combinations.md](../combinations.md). In words:

- the request-media keys: an Operation Object whose request body offers the
  named media types (`multipart/form-data`, `application/x-www-form-urlencoded`,
  `application/octet-stream`, a JSON type), beside declared parameters, a
  header parameter, or another media type, or whose form body's schema declares
  `oneOf`;
- the two `combo-params-beside-inline-*-body` keys: an operation with its own
  `parameters` whose request media schema declares `oneOf` or `anyOf` inline;
- the read-only and optional-body keys: a request media schema whose properties,
  inline or through a local `$ref`, write `readOnly`, or a body not marked
  `required` whose `$ref` target is a `oneOf` union or an `additionalProperties`
  map;
- the success keys: the success response the census selects (as
  `success_response_entry` does) declaring content, beside a union, a nullable
  union, a `204`, a `2XX` range, two media alternatives (JSON, text, a download
  type, a binary schema), or a second success status with other media;
- the error keys: a 4xx/5xx response with two media types, a `oneOf` or an
  inline object body, two statuses sharing one schema reference, or a status
  another operation declares with a different schema;
- the three `combo-echo-body-effective-*` keys: an operation whose JSON request
  body and selected success representation write the same `$ref`, with OAuth2,
  other required, or anonymous effective security.

The search fed those rows to the evaluator verbatim.

### Reproducing the enumeration

Select the thirty rows above from `witness-search-keys.tsv` into a contract
with its header. Then run `just witness-search-local-census --contract CONTRACT
--all-documents-jsonl --documents SOURCE=DIR` for each population. Join each
positive count to the manifest identities, minus excluded repositories, as
[census.tsv](census.tsv) does. Each `census.tsv` row is one `(source, document)`
declarer with its site count, SHA-256 and screening outcome.

## Verdicts

Every key is `search-incomplete`: these bounded cached populations cannot
exhaust the public population. The declarer count is the key's number of
`census.tsv` rows. Once a key had one admitted, output-sensitive, generating
witness, further declarers keep their recorded screening state.

| key | outcome | declarers | disposition |
|---|---|---:|---|
| `combo-echo-body-effective-anonymous` | `search-incomplete` | 567 | proven: registered `oal-example` |
| `combo-echo-body-effective-non-oauth-required` | `search-incomplete` | 538 | proven: registered `redocly.com-museum` |
| `combo-echo-body-effective-oauth2` | `search-incomplete` | 467 | proven: registered `swagger-petstore` |
| `combo-error-multiple-media` | `search-incomplete` | 323 | proven: registered `subsloth` |
| `combo-error-object` | `search-incomplete` | 1048 | proven: registered `buildrelay` |
| `combo-error-oneof` | `search-incomplete` | 229 | proven: registered `volview-backend-contract` |
| `combo-error-status-different-schemas` | `search-incomplete` | 1577 | proven: registered `withsecure-gdpr-subject-rights` |
| `combo-errors-shared-ref` | `search-incomplete` | 2696 | proven: registered `exa-gate` |
| `combo-form-urlencoded-beside-json-body` | `search-incomplete` | 154 | proven: registered `swagger-petstore`, after the first repair below |
| `combo-form-urlencoded-body-with-params` | `search-incomplete` | 415 | proven: registered `listennotes` |
| `combo-form-urlencoded-union-body` | `search-incomplete` | 27 | proven: registered `grantly` (corpus row 3471, registered by this search), after the third repair below |
| `combo-inline-body-read-only-property` | `search-incomplete` | 20 | unproven, witness blocked: `webflow-v2` and `osf.io` generate under the certified pair, but unrelated residuals keep the files the combination moves from byte-matching ([blocked witnesses](#blocked-witnesses)) |
| `combo-multipart-beside-json-body` | `search-incomplete` | 154 | proven: registered `mindee-ocr` |
| `combo-multipart-body-with-params` | `search-incomplete` | 780 | proven: registered `mindee-ocr` |
| `combo-no-content-beside-body-response` | `search-incomplete` | 631 | proven: registered `oal-example` |
| `combo-octet-stream-body-header-param` | `search-incomplete` | 46 | proven: registered `get-a-room` (corpus row 3470, registered by this search) |
| `combo-optional-ref-map-body` | `search-incomplete` | 294 | proven: registered `oip-web-api` |
| `combo-optional-ref-union-body` | `search-incomplete` | 107 | proven: registered `openintegrationhub-secret-service` |
| `combo-params-beside-inline-anyof-body` | `search-incomplete` | 170 | proven: registered `apideck.com-proxy`, after the second repair below |
| `combo-params-beside-inline-oneof-body` | `search-incomplete` | 225 | proven: registered `apideck.com-webhook` |
| `combo-range-beside-concrete-success` | `search-incomplete` | 7 | decided output-insensitive in both generators ([shared table](../output-insensitive.tsv)); not proven |
| `combo-ref-body-read-only-property` | `search-incomplete` | 731 | proven: registered `steaminputdb` |
| `combo-success-anyof` | `search-incomplete` | 428 | proven: registered `vellum-gateway` |
| `combo-success-anyof-nullable` | `search-incomplete` | 69 | proven: registered `deepsearch-ds-v2` |
| `combo-success-json-beside-binary-schema` | `search-incomplete` | 162 | proven: registered `microcks.local` |
| `combo-success-json-beside-download` | `search-incomplete` | 104 | proven: registered `osparc-simcore-webserver` |
| `combo-success-oneof` | `search-incomplete` | 949 | proven: registered `dashy-route-api` |
| `combo-success-oneof-nullable` | `search-incomplete` | 24 | proven: registered `ebusd` (corpus row 3472, registered by this search) |
| `combo-success-statuses-mixed-media` | `search-incomplete` | 612 | proven: registered `oal-example` |
| `combo-success-text-beside-download` | `search-incomplete` | 52 | proven: registered `chat-rest-api` |

## How a removal control is taken

Each control deletes or rewrites one member of the key's conjunction at every
matching anchor and leaves the rest of the document unchanged. Afterwards the
census counts the key at zero in the ablated document. Each control's edited
pointers are listed with it. YAML sources are parsed with the census's own
loader and written as JSON. Every control shows no crozier change between the
committed source and that round trip, except `unqork.yml`'s (below), whose
before state is therefore taken from the round trip in both generators.

Where removing one member moved nothing, the other member was removed instead,
and both controls are recorded:

- `combo-octet-stream-body-header-param`: deleting the header parameters moves
  neither generator, because both clear an octet-stream operation's headers;
  deleting the octet-stream body moves the same files in both, and the three
  `X-Get-A-Room-*` headers become arguments.
- `combo-optional-ref-union-body` and `combo-optional-ref-map-body`: marking the
  body `required` moves no crozier file, because a referenced union or map is
  passed whole and required either way; inlining the reference moves the same
  files in both generators.
- `combo-error-multiple-media`: crozier types an error with its first media type
  whose schema is known, so keeping the first type moves nothing where both
  share one schema. Keeping the last instead moves `subsloth`'s, whose two types
  differ.

**Before.** The witness's committed source and its complete certified-pair
golden. For the from-scratch document and `unqork.yml`, a fresh certified-pair
generation.

**After.** One fresh serial certified-pair generation of the ablated document,
under `flock ~/.cache/crozier-run-generation.lock`.

Crozier generates both states with the release build of the tree this record is
committed with. `crozier compare` then holds crozier's ablated output against
the certified ablated tree. The records keep each changed file's before/after
SHA-256 in both engines, the corpus marker excluded.

**Formatting condition.** Every comparison in this record ran under one neutral
condition: crozier generated from a fresh temporary working directory, outside
crozier's repository, so no repository ruff configuration applied; the
certified pair generated in its own temporary Fern workspace; `crozier compare`
ran from a temporary directory.

## Proven keys

[paired-removal-comparisons.json](paired-removal-comparisons.json) holds the
twenty-eight proving controls. In each, crozier's and the certified pair's
changed file sets are equal, and each ablated tree compares with exit 0. Each
witness's corpus golden test passes with no `unmatched` allowance, so every file
the combination's removal moves byte-matches in the witness's own golden.

| key | witness | removed | files that move in both generators |
|---|---|---|---|
| `combo-multipart-body-with-params` | `mindee-ocr` | multipart bodies beside parameters turned into JSON | 5: the prediction and workflows clients, `reference.md` |
| `combo-form-urlencoded-body-with-params` | `listennotes` | urlencoded bodies beside parameters turned into JSON | 8: two raw clients, three hoisted form types, both `__init__.py`, `reference.md` |
| `combo-multipart-beside-json-body` | `mindee-ocr` | the JSON alternative beside the multipart body | 4: the prediction clients, `README.md`, `reference.md` |
| `combo-form-urlencoded-beside-json-body` | `swagger-petstore` | the JSON alternatives beside the urlencoded bodies | 3: the pet, store and user raw clients |
| `combo-params-beside-inline-oneof-body` | `apideck.com-webhook` | the inline `oneOf` bodies, moved to named components | 13: the webhooks clients, their request types and `__init__.py`, `reference.md` |
| `combo-params-beside-inline-anyof-body` | `apideck.com-proxy` | the inline `anyOf` bodies, moved to named components | 20: the execute clients, their request types and `__init__.py`, `README.md`, `reference.md` |
| `combo-ref-body-read-only-property` | `steaminputdb` | `readOnly` on the referenced bodies' properties | 5: the search and steam clients, `reference.md` |
| `combo-optional-ref-union-body` | `openintegrationhub-secret-service` | the optional bodies' union reference, inlined | 9: the auth-clients clients, their request types and `__init__.py`, `README.md`, `reference.md` |
| `combo-optional-ref-map-body` | `oip-web-api` | the optional body's map reference, inlined | 3: `RegisterModuleDto` and both `__init__.py` |
| `combo-success-oneof` | `dashy-route-api` | the success `oneOf`, replaced by its first member | 3: the keys clients, `reference.md` |
| `combo-success-anyof` | `vellum-gateway` | the success `anyOf`, replaced by its first member | 13: the credential-requests response types and `__init__.py` |
| `combo-success-anyof-nullable` | `deepsearch-ds-v2` | the success unions' `null` members | 3: the data-indices clients, `reference.md` |
| `combo-no-content-beside-body-response` | `oal-example` | the 204 response | 3: the root clients, `reference.md` |
| `combo-success-json-beside-download` | `osparc-simcore-webserver` | the success response's JSON alternative | 3: the auth clients, `reference.md` |
| `combo-success-text-beside-download` | `chat-rest-api` | the success response's text alternative | 3: the root clients, `reference.md` |
| `combo-success-json-beside-binary-schema` | `microcks.local` | the success response's JSON alternative | 3: the mock clients, `reference.md` |
| `combo-errors-shared-ref` | `exa-gate` | the error bodies repeating another status's reference | 7: six error classes and the root raw client |
| `combo-error-multiple-media` | `subsloth` | every error media type but the last | 5: two error classes and three raw clients |
| `combo-error-oneof` | `volview-backend-contract` | the error `oneOf`, replaced by its first member | 6: the hoisted `ConflictErrorBody` types and both `__init__.py` |
| `combo-error-object` | `buildrelay` | the inline error object's `properties` | 5: `InternalServerErrorBody`, the error class, the jobs raw client, both `__init__.py` |
| `combo-error-status-different-schemas` | `withsecure-gdpr-subject-rights` | different schemas at one error status, made the first operation's | 3: the 451 error class and two raw clients |
| `combo-echo-body-effective-oauth2` | `swagger-petstore` | the success schemas repeating the body's reference, inlined | 25: the pet clients and the response types they hoist |
| `combo-echo-body-effective-non-oauth-required` | `redocly.com-museum` | the success schema repeating the body's reference, inlined | 7: the events clients, the hoisted response type, `reference.md` |
| `combo-echo-body-effective-anonymous` | `oal-example` | the success schemas repeating the body's reference, inlined | 7: the root clients, two hoisted response types, `reference.md` |
| `combo-success-statuses-mixed-media` | `oal-example` | the other success status | 3: the root clients, `reference.md` |
| `combo-octet-stream-body-header-param` | `get-a-room` | the octet-stream body beside the header parameters | 3: the rooms clients, `reference.md` |
| `combo-form-urlencoded-union-body` | `grantly` | the form body's `oneOf`, replaced by its first member | 11: the protocol clients, the discriminated `PostTokenRequest` types, `__init__.py`, `README.md`, `reference.md` |
| `combo-success-oneof-nullable` | `ebusd` | the success union's `null` member | 3: the root clients, `reference.md` |

### How the files were attributed

These proofs are attributed by the paired removal itself, not by a new
golden-reach measurement. The changed files are exactly the ones the feature
writes, the witness's complete golden byte-matches them, and the certified
ablated tree byte-matches crozier's ablated output.

The proven rows' reach cells still read `pending measurement`. They enter
[the reach ledger](../golden-reach.tsv) at the next full `just golden-reach`, a
restatement this node leaves to `reconcile-coverage`.

### The witnesses this search registered

Three keys had no registered declarer, so a witness was registered for each.
Each is published in its publisher's own repository, pinned at a full revision,
with committed source bytes, a `NOTICE` entry, a complete golden, a literals
overlay and e2e gate wiring:

- **3470, `get-a-room`** (Apache-2.0, by `info.license` and repository
  `LICENSE`): its attachment upload sends three headers beside an octet-stream
  body. The certified pair generates it and crozier byte-matches it as acquired.
- **3471, `grantly`** (MIT, by `info.license`; the repository has no
  `LICENSE`): its OAuth `/token` posts an urlencoded `oneOf` of two grants, each
  tagging `grant_type` with a one-value enum. The certified pair discriminates
  the union; crozier did not until the third repair below.
- **3472, `ebusd`** (GPL-3.0, repository `LICENSE`): a success response whose
  `oneOf` admits `null`. The certified pair generates it and crozier
  byte-matches it as acquired.

Other declarers of these keys keep their screening in [census.tsv](census.tsv).
For `combo-success-oneof-nullable`, `gatOS`, `YAQMC` and `mesastream` also
generate under the certified pair, with crozier divergences on unrelated shapes;
they are not repaired, since one witness per key suffices.

## Blocked witnesses

`combo-inline-body-read-only-property` has two admissible declarers that the
certified pair generates from. Neither proves it: each still mismatches files
for reasons unrelated to the combination. The other declarers lack a licence
grant or fall under registered Fern refusal classes ([census.tsv](census.tsv)).

| key | candidate | files still mismatched | unrelated shapes |
|---|---|---:|---|
| `combo-inline-body-read-only-property` | `webflow-v2` | 6 | of the 11 files deleting the inline bodies' `readOnly` moves in both generators: deepObject map query parameters, whose value types the certified pair hoists and crozier types `Any` or an inline union (the collection-items clients); inline types `sites.scripts` and `pages.scripts` share, which the certified pair places in each package and crozier in one (the two scripts clients, one raw client); and in `reference.md`, those two plus collection-field union selection, worked-example values and a query enum typed `Any` |
| `combo-inline-body-read-only-property` | `osf.io` | 69 | of its 583 generated files, across most clients: worked-example layout in `README.md` and `reference.md` and divergences in most tag clients; not attributed further |

Before this search, `webflow-v2`'s golden listed the redirects, webhooks and
sites-scripts raw clients in its `unmatched` residual, because crozier kept an
inline body's `readOnly` properties as optional arguments. The fourth repair
below drops them, and those five files left the list. Its removal control moves
the same eleven files in both generators, and the ablated tree mismatches the
certified pair in exactly the 38 files the committed golden does, so the
remaining hunks predate the combination and do not move with it. The control is
kept with the screening controls, since it does not prove the key.

## Output-insensitive keys

`combo-range-beside-concrete-success` moves neither generator on every document
tried. Crozier never selects a `2XX` range as the success response, and the
certified pair agrees: deleting the range moves no file in either generator, and
crozier matches the certified tree in both states. It is a row of
[the shared table](../output-insensitive.tsv) at context `-`, whose complete
before/after maps are the `tidepool-courier-combo-range-beside-concrete-success-fern.json`
and `-crozier.json` records here. Its region row reads `gap`: decided, neither
proven nor unproven.

| document | admissible | result |
|---|---|---|
| `removal-controls/tidepool-courier.yml` (from scratch) | not a corpus candidate | no file moves in either generator: a `200` and a `201` each beside a `2XX` with another schema |
| `openapi-to-plantuml`'s `unqork.yml` | no: a converter's test-resource copy of Unqork's definition, not the publisher's | no file moves in either generator |
| the five OpenAPITools petstore samples and one copy of them | Apache-2.0 | crozier refuses them under `object-extends-non-object`; the certified pair refuses the measured one too ([fern-screening/](fern-screening/openapitools-usedatetimeoffset.log)) |

No admissible declarer the certified pair generates from was found.
`tidepool-courier.yml` is written for this search and is not a hand-written
fixture; it records a decision, not a proof. Its control and `unqork.yml`'s are
in [removal-controls/](removal-controls/).

## Controls that reach but do not prove

[screening-removal-comparisons.json](screening-removal-comparisons.json) keeps
the controls that do not prove their key: those whose removal moved no crozier
file, and one blocked witness's. A declarer whose removal moves
no generated file reaches the combination but does not prove it; each key above
was then proven by another declarer or another member's removal:

- `swagger-petstore` for `combo-form-urlencoded-body-with-params`: its form
  bodies sit beside JSON alternatives, which win.
- `paloalto-cspm-search-manager` for `combo-ref-body-read-only-property`.
- the required-only controls of both optional-body keys.
- `mermade-openapi-converter`, `6-dot-authentiqio.appspot.com` and `eozilla`
  for `combo-error-multiple-media`, with the first media type kept.
- `get-a-room`'s header-deletion control, measured in both generators.
- `webflow-v2` for `combo-inline-body-read-only-property`: output-sensitive and
  measured in both generators, but [blocked](#blocked-witnesses).

`komga` declares `combo-success-json-beside-download`, but the clients its
download operations write are residuals in its golden's `unmatched` list, so
it is no witness.

## Repairs

The controls exposed four departures from the certified pair. Each is fixed in
`src/ir.rs` with a unit test driving the touched function on the triggering
shape. No golden or Fern tree was edited and no departure was catalogued.
Regenerating every registered row with crozier before and after the repairs
moves only `webflow-v2`.

1. **A path parameter sharing an urlencoded field's name.** Where the form body
   names a model a response also uses, the body is no inline request type, but
   its fields are still spread. The certified pair names the path argument
   `username_`; crozier had passed `username` twice
   (`rename_claimed_path_params`). This is `swagger-petstore`'s
   `PUT /user/{username}` once its JSON alternative is gone.
2. **A referenced union under wildcard media.** A `*/*` body whose schema
   references a union sends no `content-type` header, as an inline union already
   did (`resolve_request_body`). This is Apideck's proxy verbs once their
   `anyOf` payloads are named.
3. **A discriminated urlencoded union.** Form members that each tag one property
   with a one-value enum form a discriminated union, as JSON ones do
   (`resolve_request_body`). This is Grantly's `/token`.
4. **Read-only inline body properties.** An inline request body drops its own
   `readOnly` properties, unless an `allOf` parent declares the same name, as
   the [`inline-body-readonly-own-overlap`](../handwritten/inline-body-readonly-own-overlap/)
   fixture already pins (`resolve_request_body`). This is Webflow's redirect and
   webhook creation. The key it serves stays unproven until the
   [blocking residuals](#blocked-witnesses) are repaired.
