# Witness search for operation combinations in naming and clients

This bounded search covers the ten `naming-clients` rows owned by
`prove-operation-combinations` in [combinations.md](../combinations.md). The
certified pair is Fern CLI 5.163.1 and `fernapi/fern-python-sdk` 5.41.3.
Each key ends one of two ways here:

- **Proven by a real witness:** one admissible registered declarer, whose
  complete certified-pair golden crozier byte-matches, is output-sensitive.
  Removing the combination's feature from it moves the same generated files in
  both generators, and crozier byte-matches the certified pair's ablated tree.
- **Decided output-insensitive:** the feature moves neither generator's output
  on any document tried, a from-scratch one included. Such a key is decided, not
  proven.

Nine keys are proven by already-registered witnesses; no corpus row is added.
One, `combo-document-security-security-nonempty`, is decided output-insensitive.
Five [repairs](#repairs) to `src/` were needed first.

## The search

Measured on 2026-10-25, without a new specification search:

- **APIs.guru:** `APIs-guru/openapi-directory` at
  `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, the revision the corpus's APIs.guru
  rows pin. It was read from the same extracted archive tree the
  [operation-parameter search](../witness-search-operation-combinations-parameters/README.md#the-search)
  read; no call was made.
- **Registered:** every JSON/YAML document below `tests/fixtures/` at the tree
  this record is committed with.
- **Earlier acquisitions:** the GitHub code-search and Sourcegraph documents
  that the earlier searches' `candidate-documents.json` manifests retain. Each
  is named in `census.tsv` by repository, path and full revision.

Generator-vendor and excluded repositories are dropped before counting, under
the `excluded_repository` / `normalize_repo` contract in
`tools/witness-search/witness-search-github-index.py`. No code search, portal or
registry was queried. Four GitHub REST requests were made, all through
`tools/witness-search/rate_limit_guard.py` under its 40%-remaining floor and the
shared response cache: the repository licence reads in
[licences/lookup.json](licences/lookup.json), whose guard ledger is
[licences/rate-limit-calls.jsonl](licences/rate-limit-calls.jsonl).

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

- `combo-tagged-group-and-method-name`: an Operation Object writing `tags`,
  `x-fern-sdk-group-name` and `x-fern-sdk-method-name`;
- `combo-streaming-method-name`: one writing `x-fern-sdk-method-name` and
  `x-fern-streaming`;
- `combo-paginated-grouped-operation`: one writing `x-fern-pagination` and
  `x-fern-sdk-group-name`;
- `combo-oas31-root-response` and `combo-oas31-grouped-response`: one in an
  OpenAPI 3.1 document whose selected success response declares content, placed
  in the root client (no non-empty group and no non-blank tag) or in a grouped
  one;
- `combo-document-security-security-empty` and
  `combo-document-security-security-nonempty`: one in a document requiring a
  non-empty, non-anonymous security list, whose own `security` is empty or
  non-empty;
- `combo-document-operation-security`: one writing `security` in a document that
  writes a `security` array;
- `combo-basic-auth-document-requirement`: an OpenAPI Object writing `security`
  whose components declare an HTTP `basic` scheme;
- `combo-basic-auth-operation-requirement`: an Operation Object writing
  `security` in a document declaring an HTTP `basic` scheme.

The search fed those rows to the evaluator verbatim.

### Reproducing the enumeration

Select the ten rows above from `witness-search-keys.tsv` into a contract with
its header. Then run `just witness-search-local-census --contract CONTRACT
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
| `combo-basic-auth-document-requirement` | `search-incomplete` | 322 | proven: registered `subsloth`, after the second repair below |
| `combo-basic-auth-operation-requirement` | `search-incomplete` | 592 | proven: registered `nexmo-messages`, after the second repair below |
| `combo-document-operation-security` | `search-incomplete` | 1093 | proven: registered `mindee-ocr` |
| `combo-document-security-security-empty` | `search-incomplete` | 575 | proven: registered `audiobookshelf` |
| `combo-document-security-security-nonempty` | `search-incomplete` | 608 | decided output-insensitive in both generators ([shared table](../output-insensitive.tsv)); not proven |
| `combo-oas31-grouped-response` | `search-incomplete` | 1921 | proven: registered `helixdb-http-api` |
| `combo-oas31-root-response` | `search-incomplete` | 891 | proven: registered `electric-sql`, after the first repair below |
| `combo-paginated-grouped-operation` | `search-incomplete` | 6 | proven: registered `truefoundry-trueforge` |
| `combo-streaming-method-name` | `search-incomplete` | 7 | proven: registered `truefoundry-trueforge`, after the third repair below |
| `combo-tagged-group-and-method-name` | `search-incomplete` | 21 | proven: registered `truefoundry-trueforge-5adde28`, after the third repair below |

## How a removal control is taken

Each control deletes or rewrites one member of the key's conjunction at every
matching anchor, `webhooks` operations included, and leaves the rest of the
document unchanged. Afterwards the census counts the key at zero in the ablated
document. Each control's edited pointers are listed with it. YAML sources are
parsed with the census's own loader and written as JSON. Every control shows no
crozier change between the committed source and that round trip, except
`sftpgo`'s, whose before state is therefore taken from the round trip in both
generators.

Where removing one member moved nothing, another member was removed instead,
and both controls are recorded:

- `combo-oas31-root-response` and `combo-oas31-grouped-response`: declaring
  OpenAPI 3.0.3 moves neither generator, on `electric-sql` and `helixdb-http-api`
  alike. Fern indents every method docstring's blank lines whatever the version
  (the first repair), and ruff strips that indent from every docstring without a
  line ending in a backslash. Deleting the root operations' success content, and
  deleting the grouped operations' tags, move the same files in both.
- `combo-tagged-group-and-method-name`: deleting the declared groups makes both
  generators refuse the document, because two stream-condition request types
  then share the name `CreateTurnRequest`
  ([fern-screening/](fern-screening/truefoundry-trueforge-5adde28-group-deleted.log)).
  Deleting the method names instead moves the same files in both.
- `combo-basic-auth-document-requirement`: on `apache.org`, whose root
  `security` is the empty `[]`, deleting it moves neither generator once the
  second repair is in. `subsloth`'s root requires its basic scheme, so deleting
  it makes the credentials optional in both.

**Before.** The witness's committed source and its complete certified-pair
golden. For a from-scratch or acquired document, and for `sftpgo`, a fresh
certified-pair generation.

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
nine proving controls. In each, crozier's and the certified pair's changed file
sets are equal, and each ablated tree compares with exit 0. Each witness's
corpus golden test passes with no `unmatched` allowance, so every file the
combination's removal moves byte-matches in the witness's own golden.

| key | witness | removed | files that move in both generators |
|---|---|---|---|
| `combo-tagged-group-and-method-name` | `truefoundry-trueforge-5adde28` | the method names of the 61 operations writing a tag, a group and a method name | 85: 30 clients and 29 raw clients of the groups those operations sit in, 24 `__init__.py` files, `README.md`, `reference.md` |
| `combo-streaming-method-name` | `truefoundry-trueforge` | the method names of the two `x-fern-streaming` operations | 9: the agent-sessions and sessions clients, the root client, both `__init__.py`, `README.md`, `reference.md` |
| `combo-paginated-grouped-operation` | `truefoundry-trueforge` | `x-fern-pagination` on the seven grouped operations | 11: four groups' clients, `core/pagination.py`, `core/__init__.py`, `README.md` |
| `combo-oas31-root-response` | `electric-sql` | the two root operations' success content | 18: the root clients, the hoisted response types and `__init__.py`, `reference.md` |
| `combo-oas31-grouped-response` | `helixdb-http-api` | the tags of the three grouped operations | 11: the health and queries clients, the root clients, the `__init__.py` files, `README.md`, `reference.md` |
| `combo-document-security-security-empty` | `audiobookshelf` | the one operation's `security: []` | 2: the root client and `core/client_wrapper.py` |
| `combo-basic-auth-document-requirement` | `subsloth` | the document's `security` | 2: the root client and `core/client_wrapper.py` |
| `combo-basic-auth-operation-requirement` | `nexmo-messages` | the one operation's `security` | 2: the root client and `core/client_wrapper.py` |
| `combo-document-operation-security` | `mindee-ocr` | the one operation's `security` | 2: the root client and `core/client_wrapper.py` |

### How the files were attributed

These proofs are attributed by the paired removal itself, not by a new
golden-reach measurement. The changed files are exactly the ones the feature
writes, the witness's complete golden byte-matches them, and the certified
ablated tree byte-matches crozier's ablated output.

The proven rows' reach cells still read `pending measurement`. They enter
[the reach ledger](../golden-reach.tsv) at the next full `just golden-reach`, a
restatement this node leaves to `reconcile-coverage`.

`select-combinations` had named other golden-only witnesses for six of these
keys. Each was measured, and none of the first five proves its key:
`auto-agent-protocol` for the root response (declaring 3.0.3 moves no crozier
file), `adyen-report-notification` for the grouped response (declaring 3.0.3
moves no crozier file) and for the basic operation requirement (deleting its
webhook's `security` moves neither generator), `apache.org` for the basic
document requirement (see above) and `dystore-api` (see below). The sixth,
`airbyte.local-config` for `combo-document-operation-security`, has one
operation's `security: []` beside a root `security: [{}]`; it became
output-sensitive in both generators with the fourth repair, and is not
registered twice, since `mindee-ocr` proves the key.

## Output-insensitive keys

`combo-document-security-security-nonempty` moves neither generator on every
document tried. Under a document that already requires a credential, an
operation's non-empty override leaves the credential required in both: the
certified pair reads an operation as authenticated whenever its effective list
is non-empty, anonymous `{}` entries included (the fourth repair). The override's
scheme names do not reach the client either: the one crozier branch that reads
them, the echoed-body content-type drop in `body_response_same_ref`, is preceded
by the surviving-schema drop, which already decides an echoed body's header.

It is a row of [the shared table](../output-insensitive.tsv) at context `-`,
whose complete before/after maps are the
`lamplighter-rounds-combo-document-security-security-nonempty-fern.json` and
`-crozier.json` records here. Its region row reads `gap`: decided, neither
proven nor unproven.

| document | admissible | result |
|---|---|---|
| `removal-controls/lamplighter-rounds.yml` (from scratch) | not a corpus candidate | no file moves in either generator: a bearer-required document whose echoing `PUT` overrides with an OAuth2 client-credentials requirement |
| the 31 registered declarers with a complete golden | yes | no file moves in either generator ([screening-removal-comparisons.json](screening-removal-comparisons.json)); `sftpgo` measured from its JSON round trip |
| go-wind-cms's app API (`tx7do/go-wind-cms`, `093169df531a`) | MIT, `info.license` and repository `LICENSE` | the certified pair generates it; deleting its login operation's `security: [{}]` moves no file in either generator |
| six more acquired declarers with anonymous overrides | TachiWeb (Apache 2.0 by `info.license`), go-wind-cms's admin API (MIT), OpenMeter's cloud API (Apache-2.0); RedPlanet's three (`NOASSERTION`, not admissible) | crozier: no file moves on the five measured (all but RedPlanet's `openapi-docs.yaml`); not measured in the certified pair |
| openwop's three, bank-api's two, and five test or example copies | no corpus candidate | crozier refuses openwop's under `object-extends-non-object` and bank-api's OpenAPI 3.2.0 |

No admissible declarer is output-sensitive. `lamplighter-rounds.yml` is written
for this search and is not a hand-written fixture; it records a decision, not a
proof.

## Controls that reach but do not prove

[screening-removal-comparisons.json](screening-removal-comparisons.json) keeps
every other control: the ones measured in both generators (with
`certified_pair` filled) and the crozier-only preflights of further declarers
(with it `null`). A declarer whose removal moves no generated file reaches the
combination but does not prove it. Its crozier records were taken with the
release build of the tree this record is committed with.

## Repairs

The controls exposed four departures from the certified pair, and the
from-scratch documents written to drive the repairs end to end exposed a fifth.
Each is fixed in `src/` with a unit test driving the touched function on the
triggering shape. No golden or Fern tree was edited and no departure was
catalogued. Regenerating every registered corpus row and every other document
under `docs/` with crozier before and after all five moves no file.

Two from-scratch measurement cases hold all five through the real binary:
[`harbour-tide-desk`](../../fern-measurements/clients-extensions/harbour-tide-desk/openapi.yml)
(a bearer scheme under a root `security: [{}]`, root and grouped methods whose
descriptions end a line in a backslash, and two `stream-condition` operations)
and
[`lighthouse-keeper-roster`](../../fern-measurements/clients-extensions/lighthouse-keeper-roster/openapi.yml)
(a basic scheme no requirement names). Each has its complete certified-pair
tree, which `clients_extensions_measurements_match_fern` compares whole, and
`crates/crozier-e2e/tests/e2e/naming_clients_shapes.rs` shows each repaired line
is what that comparison turns on.

1. **Every method's docstring indent, whatever the version.** Crozier gave a
   method docstring's blank lines the 8-space indent only on a root-client
   method under OpenAPI 3.1, and wrote an empty return description as a blank
   line (`src/emit.rs`, `pad_docstring_blank_lines`, `push_return_doc`). The
   certified pair indents them under 3.0.3 too, where `electric-sql` re-declared
   as 3.0.3 moved two crozier files and no certified-pair file, and on grouped
   and streaming methods alike, with an empty return description a 12-space
   line, as `harbour-tide-desk` measures, and on binary downloads' raw and
   client methods, root and grouped, as
   [`harbour-chart-vault`](../../fern-measurements/clients-extensions/harbour-chart-vault/openapi.yml)
   measures. Ruff strips both indents unless a
   docstring line ends in a backslash, which is why no committed golden had
   shown the grouped case.
2. **Basic credentials with no requirement.** Crozier dropped an HTTP `basic`
   scheme's credentials when no Security Requirement Object named one
   (`src/ir.rs`, `auth_model`). The certified pair keeps them optional, as for a
   bearer scheme: `nexmo-messages` with its operation's `security` deleted, and
   `apache.org` with its root `security: []` deleted, each kept `username` and
   `password`.
3. **A stream-condition operation nothing names.** With neither a declared
   method name nor an `operationId`, crozier split the operation into
   `stream_stream` and `stream` (`src/ir.rs`, `stream_condition_method_names`).
   The certified pair emits only the buffered half, under the name the
   operation's summary derives, sending `"stream": False`: TrueFoundry's
   `create_and_execute_a_turn_in_a_session` once its method name is deleted.
4. **An anonymous-only security list.** Crozier read `security: [{}]` as
   unauthenticated (`src/ir.rs`, `all_operations_authenticated`). The certified
   pair keeps the credential required: on go-wind-cms's app API with a login
   operation's `[{}]`, and on
   [a from-scratch document](removal-controls/lantern-root-anonymous.yml) whose
   root `security` is `[{}]`, which crozier now byte-matches
   ([comparison](removal-controls/lantern-root-anonymous.json)). Only an empty
   list makes it optional.
5. **A stream condition's field in `reference.md`.** Crozier documented the
   field a stream condition fixes after every other required body field
   (`src/emit.rs`, `reference_entry`). The certified pair keeps its declared
   place: `harbour-tide-desk`'s `stream`, declared first, ahead of `port`.
