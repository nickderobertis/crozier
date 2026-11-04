# An unusable item in a sourced union list

This supplemental document is derived from this cause's independently authored
Greenhouse Panels measurement. Its `SensorReading` example gives `alerts` a
valid vent alert followed by the scalar `42`; the schema requires the list and
season fields so the absent-example control also demonstrates them.

The complete `fern-expected/` tree was freshly generated with the certified pair
from `assets/scaffolding/metadata.json`, through `fern-references.py`'s
`run_fern` workspace and `strip_into`, under the shared Fern generation lock.
`fern.log` and `exit-code` record that run. The certified `literals` output is committed as the `expected-literals/fern-expected/` overlay, regenerated through the registered measurement case under the same lock. The case is registered in
`docs/fern-measurements/cases.tsv` for repeatable generation.

Fern keeps the first item, `SensorReadingAlertsItem_Vent`, with its declared
`above` operator and `high` level. It synthesizes only the invalid second item
as `SensorReadingAlertsItem_Bench(operator=AlertOperator.BELOW)`. All three
writers retain both constructors and their imports. Crozier previously
replaced the entire list when any item was unusable.

The supplemental verdict is **parity-gap-repaired**, within
`request-example-union-variant-fields`. `sourced_union_value` now falls back
per item. The real-CLI test
`an_invalid_sourced_union_list_item_matches_the_certified_tree` compares the
complete output; the emitter unit test asserts both constructors and operators.
