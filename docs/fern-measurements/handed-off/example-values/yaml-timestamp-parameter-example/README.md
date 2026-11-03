# `yaml-timestamp-parameter-example`

The handed-off root cause `yaml-timestamp-parameter-example` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`GET /tides` declares `since` (required, `format: date-time`) and `until` (optional, the same) with unquoted ISO date-time examples, `recordedOn` (required, plain `string`) and `loggedAfter` (optional, plain `string`) with unquoted timestamps, and `station` (optional, `example: pier-7`); `GET /tides/{gaugeId}` declares one optional `asOf` whose example is an unquoted timestamp. `POST /tides/{gaugeId}/readings` (a single `$ref` body) and `POST /tides/{gaugeId}/readings/batch` (an array of it) post `TideReading`, whose schema-level example gives the `date-time` properties `highWaterAt` (required) and `lowWaterAt` (optional) unquoted timestamps and `calibratedAt` the `2000-01-23T04:56:07` sentinel: the schema-example date-time property sub-case, added on the planner's ruling for the residual found on confluent's schema registry. `runtime.txt` records YAML reading each unquoted value as a `datetime`.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/example-values/yaml-timestamp-parameter-example` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`runtime.txt` records the run the verdict rests on.

## The comparison

The certified pair treats each unquoted timestamp as no example: a required one takes its placeholder (`since=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00")`, `recorded_on="recordedOn"`) and an optional one leaves the call (`until`, `asOf`). crozier writes the declared timestamp, as a `datetime` for a `date-time` parameter and as the string otherwise, including the optional temporal ones, and adds the `import datetime` those need. Both leave out `loggedAfter`, the optional *non-temporal* parameter.

**Verdict: `user-ruling` (design-review ruling 3, `yaml-timestamp-parameter-example`).** crozier keeps the declared timestamp, as the catalogued `kind: usefulness` departure `unquoted-timestamp-parameter-example` (and, for the property sub-case below, `declared-timestamp-property-example`); with both applied, crozier's tree byte-matches `fern-expected/`.

**Sub-case: a schema-level object example's date-time property.** On both bodies the certified pair writes its placeholder for all three properties (`high_water_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00")`, and the same for `low_water_at` and `calibrated_at`). crozier writes the declared instants (`"2031-04-02T08:15:00+00:00"`, `"2031-04-02T14:27:00+00:00"`) and, like the pair, the placeholder for the sentinel. Applying ruling 3's principle on the planner's ruling, crozier keeps the declared instants as the catalogued `kind: usefulness` departure `declared-timestamp-property-example`. The second half of `runtime.txt` runs both sides' worked calls against a mock transport: each validates, and crozier's sends the declared instants. The row's verdict stays `user-ruling`.

**The Nexmo-withdrawal behaviour.** "An unquoted YAML timestamp dropped as an optional non-temporal query-parameter example" is `loggedAfter` here, which both drop. The record's Cyoda document (`Cyoda/cyoda-go@0021e978`, sha256 `5ce9d613…`) is **not** a real witness for that behaviour: every unquoted timestamp it declares sits on a `format: date-time` parameter (`pointInTime`), i.e. a temporal one, which ruling 3 keeps.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
`ruled_example_values_are_what_crozier_writes` asserts the lines crozier writes where a ruling keeps or changes its value, and `declared_value_departures_hold_only_their_lines` shows an adjacent unexplained change still fails.
