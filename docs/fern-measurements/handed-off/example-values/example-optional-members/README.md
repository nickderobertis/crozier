# `example-optional-members`

The handed-off root cause `example-optional-members` from [`docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`GET /signals` takes optional query parameters `$ref`'ing `Moment` (`format: date-time`, `examples: [2032-06-01T04:30:00Z]` **unquoted**), `QuotedMoment` (the same, quoted) and `LampCode` (`examples: [lamp-east]`), a required `observedTo` `$ref`'ing `Moment`, and an optional `limit` declaring `example: 25`.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py generate measurements handed-off/example-values/example-optional-members` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`runtime.txt` records the run the verdict rests on.

## The comparison

The certified pair leaves out only `observedFrom`, whose referenced example YAML reads as a timestamp (`runtime.txt`); it keeps `quoted_from` and `lamp` from their `examples` arrays, and writes its date-time placeholder for the required `observed_to`. crozier wrote `observed_from` too.

**Verdict: `user-ruling` (design-review ruling 4, `minimal-worked-call`).** crozier now leaves an optional parameter out exactly where the certified pair does (`ir::referenced_examples_entry_is_unquoted_timestamp`). The ruling's gloss — that *every* optional parameter leaves the call — is contradicted by the certified pair itself: Cyoda's `getOneEntity` keeps the optional `transactionId`, which declares a plain example, and so do `quoted_from` and `lamp` here; the planner confirmed matching the pair. The required `observed_to` keeps its declared timestamp under ruling 3 (`unquoted-timestamp-parameter-example`), so the tree byte-matches with that departure applied.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
`ruled_example_values_are_what_crozier_writes` asserts the lines crozier writes where a ruling keeps or changes its value, and `declared_value_departures_hold_only_their_lines` shows an adjacent unexplained change still fails.
