# `R4`

The handed-off root cause `R4` from [`docs/openapi-surface/witness-search-fixture-only-operations-extensions/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-operations-extensions/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`GET /keepers/{keeperId}/shifts`: `keeperId` declares a schema `example` (`KPR-from-schema`) beside a parameter `examples` map (`KPR-from-map`); optional `season` and `page` declare only `examples` maps. The operation also takes an optional `q` whose `examples` value is `""`, and `rosteredOn` (required) and `rosteredAfter` (optional) whose `examples` maps give `null` then an unquoted date; `listKeeperCallbacks` and `searchKeepers` take only an optional `since` (unquoted-date `examples` value) and `q` (`""`) — the shapes of unicourt's `q` and `libraryDate`.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py`'s own `generated_tree` (the same function its `measurements` family runs), under the shared Fern lock. The directory name is the record's cause name, which `cases.tsv`'s lower-case case names cannot spell, so it has no `cases.tsv` row.

## The comparison

The certified pair works `keeper_id` from the schema `example`; crozier from the map. Both treat `season` and `page` alike.

**Verdict: `user-ruling` (design-review ruling 5, `declared-examples-array`).** crozier keeps the map's value, as `declared-examples-array-parameter-value`. The pair leaves out `q` and `rosteredAfter`, writes its date-time placeholder for `rosteredOn`, and writes `list_keeper_callbacks()` and `search_keepers()` empty; crozier keeps the falsy `q` (ruling 2, `declared-example-over-placeholder`) and the unquoted dates (ruling 3, `unquoted-timestamp-parameter-example`), the empty calls included; with it applied, crozier's tree byte-matches `fern-expected/`. On the record's unicourt document the parameter-level `q` (`examples` value `""`) is the falsy case ruling 2 keeps.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
`ruled_example_values_are_what_crozier_writes` asserts the lines crozier writes where a ruling keeps or changes its value, and `declared_value_departures_hold_only_their_lines` shows an adjacent unexplained change still fails.
