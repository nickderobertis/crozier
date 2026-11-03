# `request-example-union-variant-fields`

The handed-off root cause `request-example-union-variant-fields` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

A greenhouse board's `POST /boards` sends a `Board` whose `panel.reading` is a discriminated union (`source`) of two components; the body declares no example, and `SensorReading` declares a schema-level `example` covering an enum list, a `$ref` enum, an inline object, a list of a further discriminated union (`ThresholdCheck` declaring its own example), a list of a union whose members are themselves `oneOf` components (`alerts`), and a union of plain components (`season`) whose example picks its second member. `POST /boards/preview` sends the same body with a request example (the control). Kong's analytics-dashboards body declares several named examples the pair does not use, and its `AdvancedQuery` the schema example the pair works.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/snippet-rendering/request-example-union-variant-fields` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`expected-literals/fern-expected/` is the pair's `literals` overlay of that tree (its `cases.tsv` row `handed-off/snippet-rendering/request-example-union-variant-fields/expected-literals`), the files the enum mode changes and a manifest of the files it omits.

## The comparison

Without a request example, the certified pair builds `PanelReading_Sensors` from `SensorReading`'s schema example: `channels`, `window=Window.DAILY` and `bench` from its values; the `checks` item as `SensorReadingChecksItem_Threshold(limit=80)`, the threshold variant's own example rather than the `32.5` the reading's example gives; the `alerts` item as `SensorReadingAlertsItem_Vent(operator=…, levels=[…])` from the example's values, the tag choosing the member; and `season` as the tag's member synthesized, `SensorReadingSeason_Autumn(phase=AutumnSeasonPhase.EARLY)`. crozier wrote `PanelReading_Sensors()`. The preview call already matched.

**Verdict: `parity-gap-repaired`.** `discriminated_union_value` (through the new `union_member_value`) builds a member flattened from a component that declares a schema example from that example; its union-typed fields go through `sourced_union_value`, which picks each member by the example's tag and builds it from its own component's example, synthesizes it where its component is an object without one, and builds it from the example's values where crozier hoisted it from a composed variant. crozier's tree byte-matches `fern-expected/` in both enum modes; every registered corpus golden still byte-matches. On Kong's document the README and the dashboard calls now match; what remains is `sort`, the bodies-paths record's `allof-description-wrapper`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`) and in literals mode against `fern-expected/` with `expected-literals/` laid over it (`handed_off_snippet_rendering_literals_overlays_match_fern`). `src/emit.rs`'s `a_union_member_is_built_from_its_components_schema_example` holds the import line and each field's lines; `snippet_departures_and_repairs_hold_only_their_lines` fails the `Window.HOURLY` placeholder crozier wrote before.
