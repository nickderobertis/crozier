# Witness search for the parameter-lowering shapes

The real-specification search behind three of the parameter-lowering repairs
that [`../../fern-measurements/parameter-lowering/`](../../fern-measurements/parameter-lowering/README.md)
measures: an array query parameter whose `items` is an inline union, a string
header with a `default` promoted from at least three quarters but not all of a
document's operations, and a document-level `x-fern-base-path` (or
`x-crozier-base-path`). None of the three has a registrable real specification,
so each is carried by a hand-written fixture under
[`../handwritten/`](../handwritten/AGENTS.md) whose cover cites its region
file's own `search-incomplete` line under `### Witness search (exhaustive)`
and this record as its renewed search.

## Witness search

No registered golden source declares any of the three shapes: the census walk
over the 226 registered sources counts no site of
`parameter.schema:query-items-union`,
`parameter.schema:subset-header-string-default` or `openapi.x-fern-base-path`.

The search for an unregistered declarer was bounded. Each key's census
selector was run, one document at a time, over the documents already acquired
for the coverage searches and kept in this checkout's caches — the GitHub code
search and Sourcegraph pools under `.local/golden-reach-search/`, the documents
the [refusal registry](../../fern-refusals/README.md) holds, and the earlier
witness-search cache: 9,753 files, of which 9,638 parsed and 115 did not. No
live query was issued for these keys at any declared source, so the search is
not exhaustive and each line reads `search-incomplete`.

| key | outcome | search | note |
|---|---|---|---|
| `query-array-items-union` | `search-incomplete` | `parameter.schema:query-items-union` over the 9,638 cached documents | 16 declarers; none registrable ([renewed search](#renewed-search)) |
| `header-subset-string-default` | `search-incomplete` | `parameter.schema:subset-header-string-default` over the 9,638 cached documents | 13 declarers; none registrable ([renewed search](#renewed-search)) |
| `base-path-extension` | `search-incomplete` | `openapi.x-fern-base-path` over the 9,638 cached documents | 1 declarer; refused by Fern ([renewed search](#renewed-search)) |

## Renewed search

Every declarer was screened with `scripts/witness_screen.py screen` — licence
under [`../../corpus-licensing.md`](../../corpus-licensing.md), the bytes read at
the pinned commit, and `fern check` and the generation at Fern CLI 5.67.1 with
`fernapi/fern-python-sdk` 5.20.0 — except where the refusal registry already
records Fern's verdict on the same bytes, or where `fern check` at the pinned CLI
failed first. Every declarer passing the three screens was generated with Fern
and compared with `crozier compare` on the finished tree. Each outcome is a row
of [`screens.tsv`](screens.tsv), keyed by the document's repository, path and
commit and by its SHA-256.

| key | outcome | declarers | what keeps each from registration |
|---|---|---|---|
| `query-array-items-union` | `none-registrable` | 16 | 11 fail `fern check` or are in the refusal registry; `bundesAPI/dwd-api` and the `konfig-sdks/openapi-examples` copy grant nothing; `konfig-dev/konfig`'s two copies are third-party copies of other publishers' descriptions (and its `agrimetrics` copy fails Fern's generation); the `swagger-api/swagger-parser` test resource passes the screens but its union members reference components it never defines, so crozier writes `Any` where Fern hoists an item alias |
| `header-subset-string-default` | `none-registrable` | 13 | 8 fail `fern check`, grant nothing, or generate only where crozier refuses an unresolved reference; the five passing every screen each differ from crozier on a shape outside these rules (below) |
| `base-path-extension` | `none-registrable` | 1 | OpenRouter's description in `jentic/jentic-public-apis` fails `fern check` (`type-name-collision`) |

The five `header-subset-string-default` declarers that pass every screen, with
what still differs:

- `APIs-guru/openapi-directory:APIs/vtex.local/Marketplace-Protocol/1.0/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`
  (CC0) — crozier writes `null` for a JSON `null` in a worked example where
  Fern writes `None`, and hoists three nested response objects Fern leaves
  inline.
- `makenotion/notion-mcp-server:scripts/notion-openapi.json@730ae781ba28beeaf0865025a3f2ed4c25ea2387`
  and the copy of the same description in `Klavis-AI/klavis` (MIT) — the
  `MovePageParentRequest` body union: crozier writes discriminated variant
  classes where Fern writes one model per member with its own `type` enum.
- `ballerina-platform/openapi-tools:openapi-cli/src/test/resources/generators/client/file_provider/swagger/openapi.yaml@ec1eec54e9404ce1e5fbe709b76187c588b512ab`
  (Apache-2.0) — a code generator's own test document; crozier places its one
  untagged operation on the root client where Fern gives it a `send_email`
  sub-client.
- `nextcloud/client-sdks:go/api/openapi.yaml@02bc7281ee36fe8862a61e94e12c91381c5866bf`
  (AGPL-3.0) — `reference.md` worked examples for binary downloads, and a tag
  named `core` that Fern merges into the package's own `core` module.

Each becomes a candidate witness once the shape it differs on matches.

## Registered from the same search

The same bounded search, run with a selector for a query union whose members
include a `$ref` to a component string enum and no array, found Ego's
microservices description (`dreek1337/Ego`, MIT), which passes every screen
and which crozier byte-matches whole. It is corpus row 316,
`ego-microservices`, so that shape carries no hand-written fixture.
