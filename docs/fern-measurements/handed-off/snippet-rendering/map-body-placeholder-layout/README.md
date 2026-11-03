# `map-body-placeholder-layout`

The handed-off root cause `map-body-placeholder-layout` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

A seed bank's `POST /varieties` sends a required body `$ref: VarietyRecord`, a schema declaring only a `title` (typed `typing.Any`); `PUT /varieties/{varietyId}/traits` a required string map component; `PATCH /varieties/{varietyId}/notes` a required inline `additionalProperties: true` object. None declares an example.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/snippet-rendering/map-body-placeholder-layout` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair writes the unknown body's `request={"key": "value"}` on one line in the README, docstrings and `reference.md`; the map bodies' placeholders keep their expanded form in `reference.md`. crozier spread the README's over three lines.

**Verdict: `parity-gap-repaired`.** `build_example_inner` registers a body typed by an alias of the unknown type as an untyped argument, which the README writer's one-pair-dict wrapping already leaves on one line, as it does an unknown field. crozier's tree byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`). `src/emit.rs`'s `an_unknown_typed_body_placeholder_stays_on_one_line_in_the_readme` holds both layouts; `snippet_departures_and_repairs_hold_only_their_lines` fails crozier's former three-line README call.
