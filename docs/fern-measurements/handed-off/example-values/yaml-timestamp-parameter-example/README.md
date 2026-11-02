# `yaml-timestamp-parameter-example`

The handed-off root cause `yaml-timestamp-parameter-example` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`GET /tides` declares `since` (required, `format: date-time`) and `until` (optional, the same) with unquoted ISO date-time examples, `recordedOn` (required, plain `string`) and `loggedAfter` (optional, plain `string`) with unquoted timestamps, and `station` (optional, `example: pier-7`); `GET /tides/{gaugeId}` declares one optional `asOf` whose example is an unquoted timestamp. `runtime.txt` records YAML reading each unquoted value as a `datetime`.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py generate measurements handed-off/example-values/yaml-timestamp-parameter-example` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`runtime.txt` records the run the verdict rests on.

## The comparison

The certified pair treats each unquoted timestamp as no example: a required one takes its placeholder (`since=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00")`, `recorded_on="recordedOn"`) and an optional one leaves the call (`until`, `asOf`). crozier writes the declared timestamp, as a `datetime` for a `date-time` parameter and as the string otherwise, including the optional temporal ones, and adds the `import datetime` those need. Both leave out `loggedAfter`, the optional *non-temporal* parameter.

**Verdict: `user-ruling` (design-review ruling 3, `yaml-timestamp-parameter-example`).** crozier keeps the declared timestamp, as the catalogued `kind: usefulness` departure `unquoted-timestamp-parameter-example`; with it applied, crozier's tree byte-matches `fern-expected/`.

**The Nexmo-withdrawal behaviour.** "An unquoted YAML timestamp dropped as an optional non-temporal query-parameter example" is `loggedAfter` here, which both drop. The record's Cyoda document (`Cyoda/cyoda-go@0021e978`, sha256 `5ce9d613…`) is **not** a real witness for that behaviour: every unquoted timestamp it declares sits on a `format: date-time` parameter (`pointInTime`), i.e. a temporal one, which ruling 3 keeps.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
`ruled_example_values_are_what_crozier_writes` asserts the lines crozier writes where a ruling keeps or changes its value, and `declared_value_departures_hold_only_their_lines` shows an adjacent unexplained change still fails.
