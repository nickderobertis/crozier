# Witness search for a misspelled scalar type, an empty closed object and two reference-cycle shapes

The real-specification search behind the repairs that read `type: float` as a
number, type an object closed with `additionalProperties: false` and declaring
no `properties` as `Dict[str, Any]`, write a model's trailing deferred imports
in field order, and repair a model with only the cycles its own references
close. A shape this search found in a registrable document is registered in
[`../../../tests/fixtures/CORPUS.md`](../../../tests/fixtures/CORPUS.md); a
shape it did not is carried by a hand-written fixture under
[`../handwritten/`](../handwritten/AGENTS.md), whose cover cites the region
file's own `search-incomplete` line and this record as its renewed search.

## Renewed search

One bounded GitHub code search, issued on 2026-10-05 through the acquirer of
`tools/witness-search/witness-search-github.py` under `tools/witness-search/rate_limit_guard.py`: eight
phrasings, two per repair, each answered and recorded with its count in
[`queries.tsv`](queries.tsv). The first page of each (100 results; 16 for the
last, which returned 16) was fetched at its indexed commit through the
acquirer's exact-commit raw route, 703 distinct documents in all. Every one was
read by `tools/surface-census/openapi-surface-census.py` for the selectors below, one
document at a time; [`census.tsv`](census.tsv) records the count per document,
or the parser's reason it could not be read (44 could not). Every declarer of
any of them was screened on licence, immutable reference and pinned Fern (CLI
5.67.1, `fernapi/fern-python-sdk` 5.20.0), each outcome in
[`screens.tsv`](screens.tsv); a declarer passing all three was then compared
with crozier.

| key | outcome | phrasings | documents | declarers | screens |
|---|---|---|---|---|---|
| `request-body-property-closed-empty-object` | `none-registrable` | `"additionalProperties": false "requestBody" "responses" filename:openapi.json` → 21248; `"additionalProperties: false" "requestBody:" "responses:" filename:openapi.yaml` → 9408 | 703 (659 read, 44 unreadable) | 1 | `dcp-ai-protocol/dcp-ai` passes all three, and crozier diverges from Fern on it apart from the shape: Fern's worked example for `verify_bundle` builds the second variant of a union where crozier builds the first |
| `type-misspelled-scalar` | `none-registrable` | `"type": "float" "components" "schemas" filename:openapi.json` → 3432; `"type: float" "components:" "schemas:" filename:openapi.yaml` → 122 | 703 (659 read, 44 unreadable) | 4 | `5GZORRO/slice-manager`, `easysoft/zendata` and `oqlos/oqlos` fail Fern's check; `jentic/jentic-public-apis`'s BulkSMS description passes all three, but declares the names only on query parameters, where Fern types an unknown name `str` and crozier `Any`, a divergence apart from the property shape |
| `cycle-into-cycle` | `none-registrable` | `"$ref" "replies" "author" "components" filename:openapi.json` → 587; `"$ref:" "subcategories:" "parent:" "components:" filename:openapi.yaml` → 16 | 703 (659 read, 44 unreadable) | 5 | `GetStream/protocol` fails on licence (`NOASSERTION`); `Open-EO/openeo-api` and both `apostrophecms` copies fail Fern; `qoretechnologies/qore`'s Bitbucket description passes all three, and crozier diverges from Fern on it apart from the shape: an `allOf` base class inside a reference cycle, which Fern flattens into the model |

The selectors are `mediaType.schema:closed-empty-object-property`,
`schema.type:misspelled-scalar` and `components.schemas:cycle-into-cycle`.

## The shapes the same documents witnessed

| shape | registered witness | how its declarers were found |
|---|---|---|
| `type: float` on a property (census `schema.type=float`) | corpus row 313, `breizhsport-catalogue` | the census, one document at a time |
| an empty closed object as an inline success response | corpus row 314, `protoform-conformance` | the census over the closed-object phrasings, read at the response |
| a model's fields reaching two or more reference cycles out of sorted order (census `components.schemas:fields-reach-cycles-unsorted`) | corpus row 315, `ere-ps-app` | the census, one document at a time |

Each registered document mismatches crozier at the commit before these repairs
and byte-matches after them. Other declarers pass all three screens and byte-match
too, and are not registered because one witness per shape suffices:
`measure-your-life-squad/measure-your-life` and `i10416/wikipedia4s` for
`type: float`, and the APIs.guru copy of Google's AutoML v1beta1 for the cycle
order.
