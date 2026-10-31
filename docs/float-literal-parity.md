# Float literals and example-row width: parity and registration

ourofoundation/wrappers `nixtla/timegpt/timegpt-openapi.json` at
`79688dd65e7fb2fb670ad30b01b5db5208c1d928` (sha256
`9165e7b94aa026f4924cc6bd8bc627719680fc028af864e0c2649168ded7705b`) is
Nixtla's TimeGPT document. The certified pair (Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3) generates from it. crozier's output differed
from the pair's in `reference.md` and the root `client.py`, for two causes. This
record gives each cause's outcome and registers the document as corpus row 4301,
`nixtla-timegpt`.

## The two causes

| # | cause | crozier code changed | outcome |
|---|---|---|---|
| 1 | A float literal read one unit in the last place away from its correctly rounded binary64 value: the pair writes `0.9345407030264767` and `0.48729867539182836`, crozier wrote `0.9345407030264768` and `0.4872986753918283`. `serde_json` was built without its `float_roundtrip` feature, so its reader took a fast, approximate path for long decimals. It reads every JSON document (`openapi::load`), and the emitter re-reads every worked example from its JSON text (`parse_example_value` in `src/emit.rs`, among others), so a YAML document's examples moved too | `Cargo.toml`: the workspace `serde_json` dependency enables `float_roundtrip` | repaired |
| 2 | A row of an example matrix kept on one line in a docstring where the pair wraps it: `["TomBrady", "2015-12-03", 0.33533486335091345, 0.35513740030391416],` and five like it. `Example::render_at` kept a list's item flat while `column + flat <= 80`, but the item is then followed by its trailing comma, which the pair counts. An item ending at 80 ran to 81 | `src/emit.rs`: the `List` and `ExplicitList` arms of `Example::render_at` measure each item at its column plus the width of its trailing comma | repaired |

Cause 2 was in the first comparison as well. The finding that started this work
named only cause 1.

## Tests

- `openapi::tests::a_documents_float_literals_read_as_their_correctly_rounded_values`
  loads a JSON and a YAML document whose examples and defaults carry literals a
  fast reader misses by one unit, plus the one-unit neighbour of one of them, and
  requires each to read as its correctly rounded value and render as that
  value's shortest spelling.
- `emit::tests::an_example_rereads_its_floats_as_their_correctly_rounded_values`
  holds the emitter's re-read of an example, including its Python-spelling
  fallback, to the same values.
- `emit::tests::a_wrapped_lists_item_counts_its_trailing_comma_against_the_width`
  holds the boundary for both list kinds: a row that ends at 80 with its comma
  stays flat, a row its comma takes to 81 wraps, and a lone row (no comma) 80
  wide stays flat.

Each failed for its intended reason before its repair: the two float tests with
`float_roundtrip` removed, the width test with the comma uncounted.

## The hand-written fixture

[`kiln-firing-curves`](openapi-surface/handwritten/kiln-firing-curves/) is
written from scratch. Its document is JSON text, so the same bytes read through
either reader. Its literals were chosen by a random search over shortest-spelled
doubles for ones a fast reader misses by one unit. It carries them in a
required query parameter's `default` and `example`, a required body property's
`default` and `example`, and a schema example. That example's matrix has a row
that ends at 80 columns with its comma in the docstring, which stays flat, and
one that ends at 81, which wraps. The certified pair generated its
`fern-expected/` tree through the shared Fern generation lock.
`handwritten_fixtures_match_fern_goldens` byte-matches crozier's output to it
apart from the `sdk-identity-header-prefix` lines the departures ledger records.
At this node's base, crozier's output mismatched it in `README.md`,
`reference.md` and `src/fern/curves/client.py`, read as JSON or as YAML. Its
cover is `required-param-and-body-defaults-ignored`, a shape it also declares.

## The comparison and the registration

`crozier compare` ran crozier on the exact document (the sha256 above) and
compared the output with the certified pair's tree. On the finished tree all 61
files match, apart from `src/fern/core/client_wrapper.py` lines 36 to 40, which
the ledger records under `sdk-identity-header-prefix`. At this node's base, two
files differed: `reference.md` and `src/fern/client.py`.

The corpus rules admit the document: its repository's `LICENSE` at the pinned
revision grants redistribution, the revision is an immutable commit, and the
certified pair generates from the raw document. It is registered as row 4301 in
[`CORPUS.md`](../tests/fixtures/CORPUS.md), with its source bytes in
`tests/fixtures/corpus-sources/nixtla-timegpt/`, its `NOTICE` entry, its
`expected/` golden and a literals-mode `expected-literals/` overlay the certified
pair generated through the shared lock. `nixtla_timegpt_matches_fern_output`
holds the first, and `overlay_goldens_match_fern_output` the second.

## Registered goldens the repair moves

None of the goldens registered before this node. Every corpus generation of a
full `tests/corpus_match/match.sh` run, the literals-mode overlays included, ran
both crozier with the repairs and crozier at this node's base, and compared the
two trees. No tree differed, and all 286 golden tests passed.

## Census suite provenance

The `surface-census` project's `test-census` suite ran twice. The first run
started under `/home/whoop/ai-orchestrator/.venv/bin/pytest`: pytest 9.1.1, the
version `uv.lock` pins, on the same CPython 3.14.7 as the worktree's `.venv`. It
ran under that pytest because the worktree's `.venv` had no pytest installed. It
found two prose counts this row moves, and it stopped at its time limit at
about 53% before reporting a total. After those counts and the census snapshot
were restated (`e84ac3072`), the suite ran to completion as its target's own
command, `uv run --locked --all-packages pytest --cov --cov-report= …`, under
the worktree's `.venv` once that held pytest: 638 passed, 1 skipped. Its tree
differs from the finished one only in this record and in one prose paragraph
of `document-paths.md` (below).

## The census re-pin

Registering the row moves the census to 277 sources (246 under
`corpus-sources/`). `restate-coverage.py --snapshot-json` re-transcribed
`document-paths.md`'s cells and snapshot digest from that walk: `7fe4dde2…`,
over 276 sources, became `514a87c4…`, over 277. That file's history paragraph
for the re-pin was dropped, because `licence-rescreening.md` cites
`document-paths.md` by line number and the added lines broke those citations.

## Offline, source and licence checks

On commit `8bfcd035f`, with neither ignored corpus cache (`.local/corpus`,
`.local/census-fallback-sample`) present before or after:
`nixtla_timegpt_matches_fern_output` (python-enums) and
`overlay_goldens_match_fern_output` (literals mode, this row among its corpora)
passed under `tests/corpus_match/corpus_offline_test.py --deny-network`, whose
socket probe was refused in the same environment. `just test-corpus-sources`,
`just lint-corpus-sources`, `just lint-corpus-licensing`,
`just lint-licence-rescreening` and `just test-licence-rescreening` passed. The
re-screening pair ran on the working tree that became `8bfcd035f`; the other
three ran on `1bbd47399`, which differs from it only in `document-paths.md`'s
paragraph above.
