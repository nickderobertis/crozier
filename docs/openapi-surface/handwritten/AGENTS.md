# Hand-written generation fixtures

OpenAPI documents written for the purpose, each with the tree Fern generated
from it, that crozier is byte-gated against. It shows that crozier matches Fern
on a document somebody wrote to exercise a shape, not that the shape occurs in a
real API — which is why it is weaker proof, and never a `CORPUS.md` row, a
corpus golden, a census source or a `golden-reach.tsv` witness.

<!-- llmlint: ignore[no_redundant_instruction_pointers] A folder AGENTS.md is loaded on its own by an agent working in this folder, not reached through the coverage index, and the acceptance criteria require the category to be written once, in the index's category rules, and linked from here rather than restated. -->
This file states the contract every fixture here is written to. When a fixture
is admitted, what it counts toward, and the `handwritten` category's precedence
and cells are stated in
[the category rules](../../openapi-surface-coverage.md#the-category-rules).

## Layout

One directory per fixture, `docs/openapi-surface/handwritten/<fixture>/`, where
`<fixture>` is a lower-kebab name unique across this directory. It holds exactly
three entries:

- `openapi.yml`: the hand-written OpenAPI document.
<!-- llmlint: ignore[no_redundant_instruction_pointers] The contract fixes that this tree is built the way probes/AGENTS.md prescribes; linking that one procedure keeps a single copy of the pinned Fern workspace recipe, and this folder file is loaded without the index. -->
- `fern-expected/`: the complete comment-stripped tree Fern generated from it at
  Fern CLI 5.67.1 and `fernapi/fern-python-sdk` 5.20.0, the corpus pin, built
  the way [`../probes/AGENTS.md`](../probes/AGENTS.md#re-running-one) prescribes.
  A document Fern refuses cannot be a fixture.
- `evidence.toml`, below.

A `measured` tree in
[`../probe-expected/MANIFEST.tsv`](../probe-expected/MANIFEST.tsv) is already a
hand-written document Fern generated from, and may be copied here as a fixture;
its manifest row stays where it is.

## `evidence.toml`

These keys, and nothing else:

- `fern_cli_version` (string, `"5.67.1"`) and `fern_python_sdk_version` (string,
  `"5.20.0"`).
<!-- llmlint: ignore[no_redundant_instruction_pointers] The contract defines the digest as Contract A's tree digest; linking Contract A keeps one definition of the canonical stream instead of restating it, and this folder file is loaded without the index. -->
- `digest` (string): the lower-case hex SHA-256 of `fern-expected/`'s canonical
  stream, computed exactly as
  [Contract A](../../openapi-surface-coverage.md#what-a-committed-proof-of-non-generation-is)
  computes a tree digest.
- `audiences` (list of strings, optional): the audience filter the fixture is
  generated for. Fern's workspace carries the list under the `python-sdk`
  group's `audiences:` (`FERN_AUDIENCES` in `scripts/generate-fern-fixture.sh`),
  and the gate and `just handwritten-reach` pass each name to crozier as
  `--audience`. Absent, both generate the whole API. It exists for an arm only an
  audience filter runs, such as `discriminator-mapping`'s `collect_schema_refs`
  arm. Label every operation, because Fern drops an unlabelled one and crozier's
  default keeps it.
- One or more `[[covers]]` tables, each with:
  - `key` (string): a region-row key, spelled as its region file spells it.
  - `arm` (string, optional): a handling site exactly as
    [`../golden-reach-sites.tsv`](../golden-reach-sites.tsv) spells it for that
    key. Absent, the cover is **feature-level** and proves the feature itself;
    present, it is **arm-level** and proves one handling site of a `golden` row.
    A site spec's regex usually holds backslashes, so write it as a TOML literal
    string (`'…'`), which keeps them verbatim.
  - `search` (string): `<repo-relative path>#<anchor>` of the committed search
    record whose verdict the cover cites. The anchor is GitHub's for a heading of
    that file, and the record is that heading's section.
  - `verdict` (string): `exhausted`, `search-incomplete` or `config-gated`, the
    verdict that record states for this key: every table line of the section
    whose first cell is the key states it, and no other outcome. An arm-level
    cover's record also names its arm in a code span. A `config-gated` cover is
    arm-level, and its fixture declares the setting its record says gates the arm.
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

A fixture that declares `audiences` is also measured without them. For each of
its arm-level covers, `just handwritten-reach` writes both runs to
[`../handwritten-config-gates.tsv`](../handwritten-config-gates.tsv), with the
same sort and one more column:

```
fixture	key	site	setting	regions_executed	regions
```

`setting` is `audiences=<name>[,<name>…]` for the run with them and `-` for
the run without. This pair is the measured gate a `config-gated` record cites.

## The gate

`handwritten_fixtures_match_fern_goldens` in
[`../../../tests/e2e.rs`](../../../tests/e2e.rs), in `just check`, finds its
fixtures by listing this directory and nothing else, and holds each to every
rule above, naming the fixture and the rule it breaks. It also holds the two
directions: every `handwritten` row has a feature-level cover, every
`handwritten-reach.tsv` row names a live cover, and an arm-level cover goes once
`golden-reach.tsv` reports its arm reached by a real specification.
`scripts/handwritten-fixtures.py gate` reads the documents; the test adds the
digest, the pin and crozier's byte-match. A divergence is repaired in `src/`,
never by editing `fern-expected/`.
