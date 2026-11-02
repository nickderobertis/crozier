# `R11`

The handed-off root cause `R11` from [`docs/openapi-surface/witness-search-fixture-only-operations-extensions/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-operations-extensions/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`GET /vessels` takes optional array query parameters declaring an array example on the parameter and its schema (`owners[]`), on the schema only over an enum (`hulls[]`), and on the parameter only (`flags`), and an optional scalar `port` declaring `example: falmouth`.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) generated for `openapi.yml` under `python_enums`, through `tools/fern-goldens/fern-references.py`'s own `generated_tree` (the same function its `measurements` family runs), under the shared Fern lock. The directory name is the record's cause name, which `cases.tsv`'s lower-case case names cannot spell, so it has no `cases.tsv` row.

## The comparison

The certified pair leaves every optional array parameter out of the worked call and keeps `port="falmouth"`; crozier passed `owners` and `hulls` (and imported `Hull`).

**Verdict: `user-ruling` (design-review ruling 4, `minimal-worked-call`).** Repaired (`ir::optional_array_declares_example`): crozier now byte-matches `fern-expected/`. The same evidence as `example-optional-members` contradicts the ruling's "every optional parameter" gloss: `port` stays, as in the pair. The full corpus run added dnd5eapi's `examples`-map arrays to the rule.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`).
`ruled_example_values_are_what_crozier_writes` asserts the lines crozier writes where a ruling keeps or changes its value, and `declared_value_departures_hold_only_their_lines` shows an adjacent unexplained change still fails.
