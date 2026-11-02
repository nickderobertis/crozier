# `example-enum-member`

The handed-off root cause `example-enum-member` from [`docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-bodies-paths/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`POST /alerts/subscriptions` takes `kinds`, an array of `AlertKind`, an enum of `*`, `beacon_lit`, `beacon_out` declaring `example: beacon_lit`.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py generate measurements handed-off/example-values/example-enum-member` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`expected-literals/fern-expected/` is the same document generated with `enum_type` unset (the `literals` mode), reduced to an overlay of `fern-expected/` (the files that differ, and `.crozier-overlay.json` naming the files Fern omits); its `cases.tsv` row is `handed-off/example-values/example-enum-member/expected-literals`.

## The comparison

The certified pair works the first member (`AlertKind.ALL`, `"*"` in literals mode); crozier the declared example (`AlertKind.BEACON_LIT`, `"beacon_lit"`).

**Verdict: `ruling-applied:falsy-property-example`.** The pair discards a valid declared value for its own placeholder, ruling 2's principle, so crozier keeps the declared member as `declared-example-over-placeholder`; with it applied crozier's tree byte-matches `fern-expected/` and, in literals mode, the `expected-literals/` overlay.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/` and its literals tree with `expected-literals/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`, `handed_off_example_value_literals_overlays_match_fern`).
`ruled_example_values_are_what_crozier_writes` asserts the lines crozier writes where a ruling keeps or changes its value, and `declared_value_departures_hold_only_their_lines` shows an adjacent unexplained change still fails.
