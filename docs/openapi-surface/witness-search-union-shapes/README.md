# Witness search for four union shapes

The real-specification search behind the union repairs that name a component
composition after its last alternative, hoist a property union's composed member,
discriminate `$ref` members by an unrequired one-value tag, and make a required
`readOnly` variant field optional. A shape this search found in a registrable
document is registered in [`../../../tests/fixtures/CORPUS.md`](../../../tests/fixtures/CORPUS.md);
a shape it did not is carried by a hand-written fixture under
[`../handwritten/`](../handwritten/AGENTS.md), whose cover cites the region
file's own `search-incomplete` line and this record as its renewed search.

## Renewed search

One bounded GitHub code search, issued on 2026-10-04 through the acquirer of
`scripts/witness-search-github.py` under `scripts/rate_limit_guard.py`: eight
phrasings, two per shape, each answered and recorded with its count in
[`queries.tsv`](queries.tsv). The first page of each (100 results) was fetched at
its indexed commit through the guard's raw lane, 693 distinct documents in all.
Every one was read by `scripts/openapi-surface-census.py` for this key's
selector, one document at a time; [`census.tsv`](census.tsv) records the count
per document, or the parser's reason it could not be read. Every declarer was
screened on licence, immutable reference and pinned Fern (CLI 5.67.1,
`fernapi/fern-python-sdk` 5.20.0), each outcome in [`screens.tsv`](screens.tsv).

| key | outcome | phrasings | documents | declarers | screens |
|---|---|---|---|---|---|
| `component-same-primitive-union` | `none-registrable` | `"anyOf" "pattern" "components" filename:openapi.json` → 5024; `"anyOf:" "pattern:" "components:" filename:openapi.yaml` → 2508 | 693 (675 read, 18 unreadable) | 35 | every declarer fails one: the 32 OpenAPI Generator petstore samples, `jstz-dev/jstz` and `quay/clair` on Fern's check, `weather-gov/api` on licence |

The petstore samples are a code generator's own test document, and their
`OneOfString` is referenced nowhere, so even a sample Fern accepted would not show
the name reaching a use site.

## The other three shapes

The same 693 documents answered the other three shapes, and each now has a
registered witness, so none carries a hand-written fixture:

| shape | registered witness | how its declarers were found |
|---|---|---|
| a model property's `anyOf` holding an inline `oneOf` or `anyOf` beside another non-`null` member | corpus row 312, `oal-example` | the census, one document at a time |
| `$ref` members tagging one property with a one-value string `enum` or `const` that `required` leaves out | corpus row 311, `qontract-api` | a scan of each document's unions for a shared unrequired single-string tag |
| a required `readOnly` property on a member of a discriminated union | corpus row 310, `openfoodfacts-taxonomy-editor` | a scan of each document's unions for such a member |

Other documents declaring the first shape pass all three screens but are not yet
registered, because crozier diverges from Fern on them in ways apart from the
shape. Each is named with its pinned commit and the divergence that blocks it:

- `vocodedev/vocode-core:docs/openapi.json@e054c33a72787b6a4920f91eb8598ad0bafb4240`
  (MIT) — crozier drops the `buy_number` operation Fern generates under
  `numbers`, and names the environment `DEFAULT` where Fern names it
  `PRODUCTION`.
- `waylayio/waylay-sdk-queries-py:openapi/queries.openapi.yaml@8ab6c18e10f96c3665dbb849ebe2193c16a1659c`
  (ISC) — `execute_query` declares query parameters that its JSON body
  repeats, so the body fields are renamed (`query_input_resource`); Fern's
  generated method takes them and sends the query parameter's value in their
  place, which is a Fern defect crozier does not reproduce.
- `waylayio/waylay-sdk-queries-py:openapi/queries.transformed.openapi.yaml@8ab6c18e10f96c3665dbb849ebe2193c16a1659c`
  (ISC) — the same body-field collision, and union members declaring
  `nullable: true`, which Fern types `Optional[...]` member by member while
  crozier leaves them bare.
- `ushakrishnan/SenseiSeek:public/openapi.json@36d7d62fb4a55acddeb31545283984a68b3e8563` (MIT) — crozier
  names two methods `serve_docs_hel_pmd` and `serve_openapijson` where Fern
  names them `serve_docs_help_md` and `serve_openapi_json`.
- `JudgmentLabs/judgeval:scripts/jql_contract/jql-ir.openapi.json@04a1848fb961c3f3127a14f05479e37fee835f84`
  (Apache-2.0) — `crozier generate` does not terminate on it.

The rest of the first shape's declarers fail a screen:
`NVIDIA-NeMo/nemo-helix` and both copies of `intellifi.nl` fail `fern check`,
and `muhammads1996/markd` and `yimingy72/wuji` grant no licence. For the second
shape, `i-am-bee/agentstack` (Apache-2.0, a `kind` tag) passes the screens and
differs from Fern in 19 files apart from the shape.
