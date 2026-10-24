# Witness search for operation combinations in parameters

This bounded search covers the sixteen `parameters` rows owned by
`prove-operation-combinations` in [combinations.md](../combinations.md). The
certified pair is Fern CLI 5.163.1 and `fernapi/fern-python-sdk` 5.41.3.
Each key is settled one of three ways:

- **Proven by a real witness:** one admissible registered declarer, whose
  complete certified-pair golden crozier byte-matches, is output-sensitive.
  Removing the combination's feature from it moves the same generated files in
  both generators, and crozier byte-matches the certified pair's ablated tree.
- **Proven by a hand-written fixture:** no admissible declarer the certified pair
  generates from exists among those read, so a from-scratch fixture, equally
  output-sensitive, proves the key.
- **Decided output-insensitive:** the feature moves neither generator's output
  on any document tried, a from-scratch one included. Such a key is decided, not
  proven.

Thirteen keys are proven by real witnesses, one by a hand-written fixture, and
two are decided output-insensitive. No owned key is left unproven.

## The search

Measured on 2026-10-24, without a new specification search:

- **APIs.guru:** `APIs-guru/openapi-directory` at
  `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, read from the shared GitHub
  response cache (archive SHA-256
  `816adb9fb4e19dc9ab28d7ad95363de146251fb41164abdb86f953f9f400c644`, no call made).
- **Registered:** every JSON/YAML document below `tests/fixtures/` at the tree
  this record is committed with. That includes every registered corpus source
  and corpus row 3400, which this search registers.
- **Earlier acquisitions:** the GitHub code-search and Sourcegraph documents
  that the earlier searches' `candidate-documents.json` manifests retain. Each
  is named in `census.tsv` by repository, path and full revision.

Generator-vendor and excluded repositories are dropped before counting, under
the `excluded_repository` / `normalize_repo` contract in
`tools/witness-search/witness-search-github-index.py`. No code search, portal or
registry was queried. Three GitHub REST requests were made, all through
`tools/witness-search/rate_limit_guard.py` and the shared cache: the repository
licence reads in [licences/lookup.json](licences/lookup.json), whose guard
ledger is [licences/rate-limit-calls.jsonl](licences/rate-limit-calls.jsonl).
One raw read of row 3400's pinned document went through the same cache
([licences/raw-reads.jsonl](licences/raw-reads.jsonl)); its bytes equal the
acquired copy (`3c3b1c22…be65`).

| population | JSON/YAML files read | OpenAPI 3 | other version or no root OpenAPI 3 marker | unreadable |
|---|---:|---:|---:|---:|
| `apis.guru` | 4138 | 1970 | 2168 | 0 |
| `github-code-search` | 5125 | 4787 | 285 | 53 |
| `registered` | 937 | 285 | 652 | 0 |
| `sourcegraph` | 4078 | 2852 | 1209 | 17 |

[unreadable.tsv](unreadable.tsv) keeps every unreadable input with its
diagnostic; none is counted as a zero.

### The detectors

Each key's detector is exactly its census conjunction: the `selector` cell of
its row in [`witness-search-keys.tsv`](../witness-search-keys.tsv), which the
census declares in `COMBINATIONS` and the combination-list drift test holds to
[combinations.md](../combinations.md). In words:

- the four `*-param-oneof` / `*-anyof` / `*-inline-object` / `*-array-default`
  keys: a query Parameter Object whose own schema declares `oneOf`, `anyOf`,
  non-empty object `properties`, or a `default` on an array;
- the `*-ref-*` keys: a query, header or path Parameter Object whose schema is
  a local `$ref` resolving to a schema with a string-valued `enum`, a primary
  `object` or `array` type, `format: date-time`, or a `pattern`;
- the two `*-enum-items` keys: a query array whose `items` declare a
  string-valued `enum`, inline or through a local `$ref`;
- the three `combo-body-property-named-as-*` keys: an Operation Object with a
  request body, one of whose path, query or header parameters (declared on it
  or its Path Item) has the same `name`, as written, as a property one of the
  body's media schemas writes.

The search fed those rows to the evaluator verbatim. In them `&` joins
conditions at one anchor, `>` follows an object edge and `~>` resolves a local
reference.

### Reproducing the enumeration

Select the sixteen rows above from `witness-search-keys.tsv` into a contract
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
| `combo-body-property-named-as-header-param` | `search-incomplete` | 7 | proven by the hand-written fixture `ferry-desk-header-collision`; no admissible declarer the certified pair generates from |
| `combo-body-property-named-as-path-param` | `search-incomplete` | 1256 | proven: registered `paloalto-cspm-search-manager`; the paired removal moves the same files in both generators |
| `combo-body-property-named-as-query-param` | `search-incomplete` | 509 | proven: registered `k8s-container-service-provider`; the paired removal moves the same files in both generators |
| `combo-header-param-ref-string-enum` | `search-incomplete` | 32 | proven: registered `ecommerce-ai-skills-runtime` (corpus row 3400, registered by this search); the paired removal moves the same files in both generators |
| `combo-path-param-ref-pattern` | `search-incomplete` | 268 | decided output-insensitive in both generators ([shared table](../output-insensitive.tsv)); not proven |
| `combo-path-param-ref-string-enum` | `search-incomplete` | 204 | proven: registered `ramu-shogi`; the paired removal moves the same files in both generators |
| `combo-query-param-anyof` | `search-incomplete` | 525 | proven: registered `openfoodfacts-taxonomy-editor`; the paired removal moves the same files in both generators |
| `combo-query-param-array-default` | `search-incomplete` | 154 | decided output-insensitive in both generators ([shared table](../output-insensitive.tsv)); not proven |
| `combo-query-param-array-inline-enum-items` | `search-incomplete` | 590 | proven: registered `rapidata-identity`; the paired removal moves the same files in both generators |
| `combo-query-param-array-ref-enum-items` | `search-incomplete` | 273 | proven: registered `sftpgo`; the paired removal moves the same files in both generators |
| `combo-query-param-inline-object` | `search-incomplete` | 124 | proven: registered `rapidata-identity`; the paired removal moves the same files in both generators |
| `combo-query-param-oneof` | `search-incomplete` | 173 | proven: registered `helios-verifiable-api`; the paired removal moves the same files in both generators |
| `combo-query-param-ref-array-alias` | `search-incomplete` | 48 | proven: registered `groupe-psa`; the paired removal moves the same files in both generators |
| `combo-query-param-ref-date-time` | `search-incomplete` | 23 | proven: registered `openepcis-dpp-ready`; the paired removal moves the same files in both generators |
| `combo-query-param-ref-object` | `search-incomplete` | 166 | proven: registered `apideck.com-webhook`; the paired removal moves the same files in both generators |
| `combo-query-param-ref-string-enum` | `search-incomplete` | 677 | proven: registered `color.pizza`; the paired removal moves the same files in both generators |

## Renewed search

The hand-written cover of `combo-body-property-named-as-header-param` cites this
record as its renewed search.

| key | renewed outcome | why no declarer is registrable |
|---|---|---|
| `combo-body-property-named-as-header-param` | `none-registrable` | none is registered; the one GitHub declarer, PancrePal-xiaoyibao (Apache-2.0), is refused by the certified pair because its multipart upload's `agent` header shares its name with a form field; the six Sourcegraph declarers are FastEndpoints integration-test outputs (MIT), two of which the certified pair refuses on a path parameter and a query parameter normalizing to one name, and all six of which crozier refuses under registered Fern refusal classes |

## How a removal control is taken

Each control deletes or renames one member of the key's conjunction at every
matching anchor, leaving the rest of the document unchanged. Afterwards the
census counts the key at zero in the ablated document. The removal is chosen so
that only the combination disappears where it can be:

- a parameter's own `oneOf`, `anyOf`, `properties`, items `enum` or array
  `default` is deleted;
- a parameter schema's `$ref` (to a string enum, an object, a date-time alias
  or an array) is replaced by an inline `type: string`, and an array's items
  `$ref` to a string enum likewise;
- a `$ref` target's `pattern` is deleted;
- a body property sharing its name with a parameter is renamed `<name>Field`,
  so both the parameter and the property survive and only the shared name goes.

Each control's edited pointers are listed with it. YAML sources are read with a
YAML 1.1 safe loader that leaves timestamps as strings, so the JSON the ablation
writes generates the same crozier output as the committed source; every control
shows no change between the committed source and that round trip.

**Before.** For a registered witness, the committed source and its complete
certified-pair golden. For the hand-written fixture, its committed
`fern-expected/` tree. For the from-scratch document, a fresh certified-pair
generation of it.

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
fourteen proving controls. In each, crozier's and the certified pair's changed
file sets are equal, and the ablated tree compares with exit 0. Each real
witness's corpus golden test passes with `unmatched: &[]`, and the hand-written
fixture passes `handwritten_fixtures_match_fern_goldens`. So the files the
combination writes byte-match in the witness's own golden.

| key | witness | removed | files that move in both generators |
|---|---|---|---|
| `combo-query-param-oneof` | `helios-verifiable-api` | the query parameter's `oneOf` | 6 files: the verifiable clients, `reference.md`, the hoisted `GetEthV1ProofLogsRequestAddress` and both `__init__.py` |
| `combo-query-param-anyof` | `openfoodfacts-taxonomy-editor` | the query parameter's `anyOf` | 3 files: the root clients and `reference.md` |
| `combo-query-param-ref-string-enum` | `color.pizza` | the query parameters' enum `$ref`s | 3 files: the root clients and `reference.md` |
| `combo-header-param-ref-string-enum` | `ecommerce-ai-skills-runtime` | the two headers' enum `$ref`s | 3 files: the root clients and `reference.md` |
| `combo-path-param-ref-string-enum` | `ramu-shogi` | the path parameters' enum `$ref`s | 3 files: the user-settings clients and `reference.md` |
| `combo-query-param-inline-object` | `rapidata-identity` | the twelve query objects' `properties` | 21 files: the client, customer and organization clients, their hoisted request types and `__init__.py` |
| `combo-query-param-ref-object` | `apideck.com-webhook` | the query parameter's object `$ref` | 3 files: the webhooks clients and `reference.md` |
| `combo-query-param-array-ref-enum-items` | `sftpgo` | the six query arrays' items `$ref`s | 5 files: the events and maintenance clients and `reference.md` |
| `combo-query-param-array-inline-enum-items` | `rapidata-identity` | the four query arrays' items `enum` | 18 files: the hoisted `…RequestSortItem` enums, their clients and `__init__.py` |
| `combo-query-param-ref-date-time` | `openepcis-dpp-ready` | the query parameter's date-time alias `$ref` | 3 files: the life-cycle clients and `reference.md` |
| `combo-query-param-ref-array-alias` | `groupe-psa` | the seven query parameters' array `$ref`s | 11 files: five tag clients and `reference.md` |
| `combo-body-property-named-as-path-param` | `paloalto-cspm-search-manager` | renaming the body property a path parameter shares | 5 files: the search-manager clients, `types/search_model.py`, `README.md` and `reference.md` |
| `combo-body-property-named-as-query-param` | `k8s-container-service-provider` | renaming the body property a query parameter shares | 3 files: the containers clients and `types/container.py` |
| `combo-body-property-named-as-header-param` | `ferry-desk-header-collision` (hand-written) | renaming the body property the `deck` header shares | 3 files: the sailings clients and `reference.md` |

### How the files were attributed

These proofs are attributed by the paired removal itself, not by a new
golden-reach measurement. The changed files are exactly the ones the feature
writes, the witness's complete golden byte-matches them, and the certified
ablated tree byte-matches crozier's ablated output.

The proven rows' reach cells still read `pending measurement`. They enter
[the reach ledger](../golden-reach.tsv) at the next full `just golden-reach`, a
restatement this node leaves to `reconcile-coverage`.

### The witness this search registered

`combo-header-param-ref-string-enum` had no registered declarer. Of its
thirty-two `census.tsv` rows, crozier refuses twenty-two under registered Fern
refusal classes: `example-not-enum-value` takes fifteen, among them the four
Twilio APIs.guru documents, whose `X-Twilio-Webhook-Enabled` example is no enum
value. Four reference sibling files the acquisition does not hold. On four more
(fauna, Mercury's Extend, and agentrail in both acquisitions), replacing the
reference with `type: string` moves no crozier file: they reach the combination
but do not prove it.

The remaining two rows are one document, which qualifies: Sourcegraph's copy
and the registered row it became. kangise's `ecommerce-ai-skills` publishes its
own runtime API under a CC0-1.0 repository licence. Its CSV evidence import sends
`X-Evidence-Platform` and `X-Evidence-Type`, both typed by referenced string
enums. Its candidacy:

- **The certified pair generates it** (complete golden committed).
- **It is output-sensitive.** Inlining the two references as `type: string`
  moves the same three files in both generators.
- **It is now registered** as corpus row 3400, `ecommerce-ai-skills-runtime`,
  with its source bytes, licence (`licenses/ecommerce-ai-skills-CC0-1.0.txt`),
  NOTICE entry, golden, literals overlay and e2e gate wiring.

## Output-insensitive keys

Each key below moves neither generator on every document tried. A from-scratch
document is among them for every key, and crozier matches the certified tree in
both states of each control. Each is a row of
[the shared table](../output-insensitive.tsv) at context `-`, whose complete
before/after maps are the `lighthouse-beacon-log-*-fern.json` and
`lighthouse-beacon-log-*-crozier.json` records here. Their region rows read
`gap`: decided, neither proven nor unproven.

| key | documents tried, none moving either generator |
|---|---|
| `combo-path-param-ref-pattern` | discord-com, cyclonedx-transparency-exchange, tlon-notes and the lighthouse document; tamoss moves no crozier file |
| `combo-query-param-array-default` | appwrite.io-client and the lighthouse document; letta, anchore.io and appwrite.io-server move no crozier file |

Discord's ablated certified tree is byte-identical to its committed golden,
although its `guild_id`-style paths are typed by the `pattern`-bearing
`SnowflakeType`. Crozier records whether a path parameter's named type carries a
`pattern`, but no emitter reads it, and the certified pair's output agrees.

[screening-removal-comparisons.json](screening-removal-comparisons.json) records
these real and from-scratch controls. The from-scratch document and its
ablations are in [removal-controls/](removal-controls/):
`lighthouse-beacon-log.yml` holds a path parameter typed by a `pattern`-bearing
named string and a query array with a list `default`. It is written for this
search and is not a hand-written fixture; it records a decision, not a proof.
The hand-written fixture's ablation is there too
(`ferry-desk-header-collision-combo-body-property-named-as-header-param.json`).

## The certified pair's refusal of a header collision

`combo-body-property-named-as-header-param` generates where the body is JSON:
the hand-written fixture's `deck` header beside a JSON body's `deck` property
takes a prefix on the body field in both generators. Where the body is
multipart, the certified pair refuses the operation, for a query parameter as
for a header. That is PancrePal's upload. Before this search crozier wrote a
client passing the name twice, which `ruff format` rejects as Python. It now
refuses both shapes in both modes under `request-property-name-collision`, whose
[evaluation note](../../fern-refusals/request-property-name-collision/evaluation.md)
records the measured probes.

## Repairs

The ecommerce runtime API's golden exposed three departures from the certified
pair, each fixed in `src/` with unit tests driving the touched function on the
triggering shape. No golden or Fern tree was edited and no departure was
catalogued.

1. **An optional body naming a closed empty object.** `required: false` over a
   `$ref` to `{type: object, additionalProperties: false}` is passed whole as a
   required `request: EmptyRequest`, the way a referenced map is
   (`resolve_request_body`). Crozier had dropped the operation from its client:
   the Daily Ops `execute` and `retry` methods.
2. **A header's fallback example.** Where the body admits no importer example,
   a required header is exampled by its camelCase name (`idempotencyKey`), as
   for text and bytes responses already. An operation whose body Fern drops
   keeps the wire name (`emit.rs`'s `header_slot`). The Weekly Ops
   `POST /v1/agent-runs` shows the first; the `text/csv` evidence import, the
   second.
3. **Fields a `required`-only member promotes.** `allOf: [$ref Base,
   {required: […]}]` keeps the promoted fields first in the model and
   signature, but the docstring example writes them where the base declares
   them (`restore_promoted_declaration_order`). This is the Daily Ops schedule
   `PATCH`.

The fourth repair is the multipart refusal above (`name_refusals.rs`).
