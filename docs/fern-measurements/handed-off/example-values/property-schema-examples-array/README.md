# `property-schema-examples-array`

The handed-off root cause `property-schema-examples-array` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../example-values.tsv`](../../example-values.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

`PlotRequest.waypoints` (`type: array` of strings) declares a 3.1 `examples` array whose entry holds a string with a double quote (`hold at "Wolf Rock"`), beside `vessel` and `legs` declaring `examples` too. `berths` (an array of a string enum `quay-north`, `quay-south`, `mooring-buoy`) declares the entry `[harbour, anchorage]`, naming no member, and the scalar enum `tide` declares `spring`, naming none either (vercel's `CreateProjectEnvRequestBodyGitBranch.target`, whose `examples` entry `[production, preview]` names no member of its item enum).

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/example-values/property-schema-examples-array` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`expected-literals/fern-expected/` is the same document generated with `enum_type` unset (the `literals` mode), reduced to an overlay of `fern-expected/` (the files that differ, and `.crozier-overlay.json` naming the files Fern omits); its `cases.tsv` row is `handed-off/example-values/property-schema-examples-array/expected-literals`.

## The comparison

The certified pair passes the entry; crozier fell back to `["waypoints"]` because its literal spelled that string with single quotes, which its example parser could not read (SandboxFusion's `print("…")`). For `berths` the certified pair works each entry naming no member as the enum's first member (`PlotRequestBerthsItem.QUAY_NORTH` twice; `"quay-north"` twice in the literals mode), and `tide` as `PlotRequestTide.FLOOD`; crozier wrote `tide` the same way but passed the list's strings `"harbour", "anchorage"` through, values its own `typing.List[PlotRequestBerthsItem]` signature rejects.

**Verdict: `parity-gap-repaired`.** `emit::parse_example_value` reads a single-quoted Python string, and `emit::ExampleCtx::value_from_example` works a list item naming no member of its enum as the enum's synthesized first member; crozier's tree byte-matches `fern-expected/` and the `expected-literals/` overlay.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_example_values.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/` and its literals tree with `expected-literals/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_example_value_measurements_match_fern`, `handed_off_example_value_literals_overlays_match_fern`); the `emit` unit tests `an_examples_entry_holding_a_double_quote_is_worked` and `an_examples_entry_naming_no_enum_member_is_worked_as_the_first_member` assert the lines.
