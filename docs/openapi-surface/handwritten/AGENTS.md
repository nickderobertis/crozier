# Hand-written generation fixtures

OpenAPI documents written for the purpose, each with the tree Fern generated
from it, that crozier is byte-gated against. **A hand-written fixture is a lower
level of proof than a real specification.** It shows that crozier matches Fern on
a document somebody wrote to exercise a shape. It does not show that the shape
occurs in a real API, or that crozier matches Fern on the way a real API writes
it. So a fixture is admitted as generation evidence only where the
real-specification search for its shape has already failed, and it cites that
search. It never counts as a real-specification match, anywhere: it is never a
[`CORPUS.md`](../../../tests/fixtures/CORPUS.md) row, a corpus golden, a census
source, a witness in [`../golden-reach.tsv`](../golden-reach.tsv) or part of the
golden-only tier. A real specification found later supersedes it.

This file states the contract every fixture here is written to. The category a
fixture puts a region row in, its precedence and the row's cells are stated
once, in
[the category rules](../../openapi-surface-coverage.md#the-category-rules). Where
the report counts fixtures is stated in
[*What it says today*](../../openapi-surface-coverage.md#openapi-surface-coverage)
and [the unreached-arm table](../../openapi-surface-coverage.md#every-unreached-arm-and-its-search-verdict).

## Layout

One directory per fixture, `docs/openapi-surface/handwritten/<fixture>/`, where
`<fixture>` is a lower-kebab name unique across this directory. It holds exactly
three entries:

- `openapi.yml`: the hand-written OpenAPI document.
- `fern-expected/`: the complete comment-stripped tree Fern generated from it at
  Fern CLI 5.67.1 and `fernapi/fern-python-sdk` 5.20.0, the corpus pin, built
  the way [`../probes/AGENTS.md`](../probes/AGENTS.md#re-running-one) prescribes.
  A document Fern refuses cannot be a fixture.
- `evidence.toml`, below.

A `measured` tree in
[`../probe-expected/MANIFEST.tsv`](../probe-expected/MANIFEST.tsv) is already a
hand-written document Fern generated from, and may be copied here as a fixture;
the manifest row stays until the reconciliation retires it.

## `evidence.toml`

These keys, and nothing else:

- `fern_cli_version` (string, `"5.67.1"`) and `fern_python_sdk_version` (string,
  `"5.20.0"`).
- `digest` (string): the lower-case hex SHA-256 of `fern-expected/`'s canonical
  stream, computed exactly as
  [Contract A](../../openapi-surface-coverage.md#what-a-committed-proof-of-non-generation-is)
  computes a tree digest.
- One or more `[[covers]]` tables, each with:
  - `key` (string): a region-row key, spelled as its region file spells it.
  - `arm` (string, optional): a handling site exactly as
    [`../golden-reach-sites.tsv`](../golden-reach-sites.tsv) spells it for that
    key. Absent, the cover is **feature-level**: it proves the feature itself,
    and its row is `handwritten`. Present, it is **arm-level**: it proves one
    handling site of a `golden` row, which stays `golden`; the fixture then
    appears only in the report's hand-written column and in
    [`../handwritten-reach.tsv`](../handwritten-reach.tsv), and the arm is still
    counted as unreached by real specifications. A site spec's regex usually
    holds backslashes, so write it as a TOML literal string (`'…'`), which
    keeps them verbatim.
  - `search` (string): `<repo-relative path>#<anchor>` of the committed search
    record whose verdict the cover cites. The anchor is GitHub's for a heading of
    that file, and the record is that heading's section.
  - `verdict` (string): `exhausted` or `search-incomplete`, the verdict that
    record states for this key: every table line of the section whose first cell
    is the key states it, and no other outcome. An arm-level cover's record also
    names its arm in a code span.
  - `renewed` (string): required exactly when `verdict` is `search-incomplete`.
    The repo-relative path of a renewed-search record with a table line whose
    first cell is the key and one of whose cells reads `none-registrable`.

```toml
fern_cli_version = "5.67.1"
fern_python_sdk_version = "5.20.0"
digest = "<64 lower-case hex digits>"

[[covers]]
key = "oneof-bare-object-example-variant"
search = "docs/openapi-surface/schemas.md#witness-search-exhaustive"
verdict = "exhausted"
```

## The feature-level selector

A feature-level cover's fixture must declare its key's shape: the census
selector recorded for that key in
[`../witness-search-keys.tsv`](../witness-search-keys.tsv) counts at least one
site in `openapi.yml`. That file is the key set the real-specification searches
ran over, and a `handwritten` row stays in it with the selector its search used
(`scripts/witness-search-region-keys.py` keeps it), because the row's own
evidence cell names fixtures rather than a selector. Every tool that derives a
search key set from the region files keeps a `handwritten` row the same way — the
GitHub dispatch, the APIs.guru gap screen, the wide scrape's baseline — since the
feature still has no real-specification witness and stays a search target.

## `handwritten-reach.tsv`

[`../handwritten-reach.tsv`](../handwritten-reach.tsv), tab-separated with one
header line, sorted by `fixture`, then `key`, then `site`:

```
fixture	key	site	regions_executed	regions
```

One row per arm-level cover, measured by an instrumented crozier run over that
fixture's `openapi.yml` alone, the way `scripts/golden-reach.py measure` scopes
one golden test. `just handwritten-reach` writes it; like `just golden-reach`
it stays outside `just check`. `golden-reach.tsv` and the golden-only tier never
read a fixture.

## The gate

`handwritten_fixtures_match_fern_goldens` in
[`../../../tests/e2e.rs`](../../../tests/e2e.rs), in `just check`, finds its
fixtures by listing this directory and nothing else, and fails, naming the
fixture and the condition, when any of these fails:

- the two version fields equal the pin, and `fern-expected/`'s digest equals
  `digest`;
- crozier's output over `openapi.yml` byte-matches `fern-expected/` under the
  normalization a corpus golden gets;
- each cover's `key` exists. A feature-level cover's row is `handwritten` and
  the key's selector declares a site in `openapi.yml`. An arm-level cover's row
  is `golden`, its `arm` is a site the site table lists for that key,
  `handwritten-reach.tsv` has its row with `regions_executed` of at least 1, and
  `golden-reach.tsv` still reports the arm unreached — a real specification that
  reaches it supersedes the fixture, and the cover must then go;
- the `search` anchor resolves, the record states `verdict` for the key (and
  names the arm), and a `search-incomplete` cover's `renewed` record names the
  key `none-registrable`;
- both directions: every fixture directory has a valid `evidence.toml` with at
  least one cover; every `handwritten` row has a feature-level cover and the
  cells the category rules fix; every `handwritten-reach.tsv` row names a live
  cover; and nothing here is a `CORPUS.md` row, a corpus golden, a census source
  or a `golden-reach.tsv` witness.

`scripts/handwritten-fixtures.py gate` reads the documents; the test adds the
digest, the pin and crozier's byte-match. A divergence is repaired in `src/`,
never by editing `fern-expected/`.
