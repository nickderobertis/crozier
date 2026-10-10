# `flat-pagination-pager-docs`

**Kind:** `fern-defect`. In its flat tree, Fern returns a paginated method's
page model, yet its `README.md` documents a pager the method does not return.

## The input

[`ledger-records-offset/openapi.yml`](../../openapi-surface/handwritten/ledger-records-offset/openapi.yml),
a crozier-authored document whose `GET /entries` (`listEntries`) declares the
offset form of `x-fern-pagination` (`offset: $request.page`, `results:
$response.entries`) over an `EntryPage` of `Entry` items. The same construct
appears for the cursor form in
[`crane-hire-cursor/openapi.yml`](../fern-measurements/clients-extensions/crane-hire-cursor/openapi.yml)
and for a root contract taken through `x-fern-pagination: true` in
[`beacon-registry-pages/openapi.yml`](../../openapi-surface/handwritten/beacon-registry-pages/openapi.yml).

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, run token-less in the
workspace `tools/fern-goldens/generate-fern-fixture.sh --layout flat` scaffolds
(`organization: fern`, `pydantic_config.enum_type: python_enums`, `fern
generate --group python-sdk --local`), exits 0; the comment-stripped tree is
[`ledger-records-offset-flat/fern-expected`](../../fern-measurements/clients-extensions/ledger-records-offset-flat/fern-expected).

Its `client.py` declares `def list_entries(...) -> EntryPage` and returns the
raw client's parsed page; `core/pagination.py` ships and `core/__init__.py`
exports `SyncPager` and `AsyncPager`. Yet `README.md` lists `Pagination` in its
contents (line 16), says under `## Pagination` that "Paginated requests will
return a `SyncPager` or `AsyncPager`" and walks `pager.iter_pages()` (lines
93–113), and its raw-response snippet reads `pager.response` and
`pager.iter_pages()` off `client.list_entries(...)` (lines 124–134).

## Why it is a defect

Running the README's walk over the tree, with `httpx` and `pydantic`
installed and a local server answering `{"entries": [{"id": "e-1", "amount": 9.5}]}`:

```text
>>> pager = client.list_entries()
>>> type(pager).__name__
'EntryPage'
>>> pager.response
AttributeError: 'EntryPage' object has no attribute 'response'
>>> for page in pager.iter_pages(): ...
AttributeError: 'EntryPage' object has no attribute 'iter_pages'
```

The documentation contradicts the generated method, which returns the page
model, so the documented walk raises `AttributeError`: a defect under the
defect rule. The rest — the page-model return, the pagination runtime and its
`core` exports, the first snippet's plain `client.list_entries()` — is
behaviour, and crozier matches it.

## crozier's output

crozier writes the same flat tree but for `README.md`: no `Pagination` entry
or section, and the raw-response snippet reading the raw client's
`response.headers`, `response.status_code` and `response.data`, which the
method's raw client returns. In the packaged tree, where both tools return a
pager, crozier writes Fern's Pagination section and pager walk unchanged.
`clients_extensions_measurements_match_fern` holds the departure to each flat
case's `flat-pagination-pager-docs` row in
`tests/fixtures/departures-ledger.tsv`, one at the first line of
`README.md`'s differing window, and `truefoundry_trueforge_flat_matches_fern`
holds it the same way over the flat golden of the registered TrueForge
document, whose cursor-paginated methods return their page models too.
