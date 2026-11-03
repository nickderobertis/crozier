# `example-inline-union-member-constructor`

The handed-off root cause `example-inline-union-member-constructor` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

A parcel desk's `POST /checkouts/{checkoutId}` sends `deliveries`, a list of `DeliveryChoice`: an object with a string `method` and two optional object properties, whose `oneOf` branches each pin `method` by `const` and require one of them. The request example gives `[{method: locker}]`. The parent's `method` is a plain string, so the pair writes no orphan enum for it (agentic-commerce's parent `type` enum is another area's `orphan-type-emission`).

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/snippet-rendering/example-inline-union-member-constructor` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

`expected-literals/fern-expected/` is the pair's `literals` overlay of that tree (its `cases.tsv` row `handed-off/snippet-rendering/example-inline-union-member-constructor/expected-literals`), the files the enum mode changes and a manifest of the files it omits.

## The comparison

The certified pair writes the inline member's constructor, `DeliveryChoiceZero(method=DeliveryChoiceZeroMethod.LOCKER)` (`"locker"` in literals mode); crozier writes the same at this node's base.

**Verdict: `already-matching`, cleared by `c0d439ecd` (#672).** Built at `de440bc03` crozier still wrote a dict literal in both agentic-commerce documents' `reference.md`; built at `c0d439ecd` their `reference.md` and checkout clients match (their remaining files are other areas': `union-modelling`'s orphan `SelectedFulfillmentOptionType` and a timestamp header typed `str`). crozier's tree byte-matches `fern-expected/` in both enum modes.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`) and in literals mode against `fern-expected/` with `expected-literals/` laid over it (`handed_off_snippet_rendering_literals_overlays_match_fern`).
