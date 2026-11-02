# `example-value-source`

The handed-off root cause `example-value-source` from [`docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

One operation per sub-rule the record lists (each named in its `description`): a multipart text part's example; a binary download's query example; a binary download's array body example; a `format: uri` and a pattern-only string; path parameters beside one with an empty schema; a union-typed property's example (object variants, and a `oneOf` of a string and a list inside an array item); an array body's schema example; a map property's schema example (`anyOf` value); a required array query example; a media named example for an enum field, as JSON and as an urlencoded form (with a property-level enum example beside it); `format: uint64`; bounded integers on a JSON and on a text operation; a header on an operation whose body has no worked example; and path parameters' own examples on importer-declined operations.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/example-values/example-value-source` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`expected-literals/fern-expected/` is the same document generated with `enum_type` unset (the `literals` mode), reduced to an overlay of `fern-expected/` (the files that differ, and `.crozier-overlay.json` naming the files Fern omits); its `cases.tsv` row is `handed-off/example-values/example-value-source/expected-literals`.

## The comparison

Sub-rule by sub-rule (certified pair → crozier at base → outcome):

| sub-rule | certified pair | crozier at base | outcome |
|---|---|---|---|
| multipart text part example | `title="title"` | `"Lizard Point"` | kept (ruling 2's principle), `declared-example-over-placeholder` |
| binary download's query example | `scale="scale"` | `"1:25000"` | kept, same departure |
| path parameter beside an empty schema (an example holding `/`) | `harbour_slug="harbourSlug"` | `"cornwall/porthleven"` | kept, same departure |
| binary download's array body media example | as crozier | — | matched at base |
| `format: uri` / pattern-only string | name placeholders | format/pattern samples | matched through the catalogued `schema-rejected-name-example` |
| union-typed property example, object variants | as crozier | — | matched at base |
| union-typed property example, `oneOf [string, array]` (guardian's `filterValue`) | `match="match"` | `["depth"]` | kept, `declared-example-over-placeholder` |
| array body's schema example | `["Mount's Bay", …]` | `["string"]` | repaired |
| map property's schema example | `{"night": True, …}` | `{"key": 1}` | repaired |
| required array query example | `["PLY", "FAL"]` | `["codes"]` | repaired |
| media named example for an enum field (JSON) | as crozier | — | matched at base |
| the same in an urlencoded form | `OVERNIGHT_STAY` (`tier` property example → first member) | first member | repaired |
| `uint64` placeholder | `1000000` | `1` | repaired |
| bounded integer, JSON operation | as crozier | — | matched at base |
| bounded integer, importer-declined | `depth=1024` (maximum) | `1` | repaired |
| header on an importer-declined operation | `watch_token="watchToken"` | `"xWatchToken"` | repaired |
| path parameter's own example, importer-declined | `"bcn:west-4"`, `"ltn:east-2"` | names | repaired |

**Verdict: `ruling-applied:falsy-property-example`** (the planner's ruling for this one row): the kept sub-rules follow ruling 2's principle as `declared-example-over-placeholder`, every other differing sub-rule is repaired to match the pair. With the catalogued departures applied, crozier's tree byte-matches `fern-expected/` and the `expected-literals/` overlay.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/` and its literals tree with `expected-literals/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`, `handed_off_example_value_literals_overlays_match_fern`).
`ruled_example_values_are_what_crozier_writes` asserts the lines crozier writes where a ruling keeps or changes its value, and `declared_value_departures_hold_only_their_lines` shows an adjacent unexplained change still fails.
