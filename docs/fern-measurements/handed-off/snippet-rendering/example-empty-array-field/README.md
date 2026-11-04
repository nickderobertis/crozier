# `example-empty-array-field`

The handed-off root cause `example-empty-array-field` from [`docs/openapi-surface/witness-search-fixture-only-schemas/README.md`](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), measured on a from-scratch document. Its triage row is in [`../../snippet-rendering.tsv`](../../snippet-rendering.tsv); the documents it blocked are compared in [`../README.md`](../README.md).

## The document

A tile catalogue's `DELETE /tiles` takes a required `deepObject` query `criteria` of the recursive `Criteria` model (optional `any_of`/`all_of` lists of `Criteria`, values beside them in `additionalProperties`), whose schema example names only `additionalProperties` keys inside its `any_of` items. `POST /tiles/search` sends a body whose request example gives `finish.glazes` an explicit `[]`.

## The certified pair's output

`fern-expected/` is the complete, comment-stripped tree the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, `assets/scaffolding/metadata.json`) generated for `openapi.yml` under `python_enums`, through `just fern-references measurements handed-off/snippet-rendering/example-empty-array-field` (its `docs/fern-measurements/cases.tsv` row), under the shared Fern lock.

## The comparison

The certified pair writes `criteria=Criteria()`; crozier wrote `Criteria(any_of=[])`, the recursion break cutting the list of the model being built to `[]`. The explicit `[]` is worked as the `["glazes"]` placeholder by both. The record's "empty array" is that cut list: payload-tools' `Where.or` example items name only `additionalProperties` keys.

**Verdict: `parity-gap-repaired`.** `named_value_inner` leaves out an optional list field the recursion break empties even where the schema-level example names it. crozier's tree byte-matches `fern-expected/`.

## What holds it

`crates/crozier-e2e/tests/e2e/handed_off_snippet_rendering.rs` runs the real `crozier` binary over `openapi.yml` and compares its whole tree with `fern-expected/`, every catalogued departure held to its `tests/fixtures/departures-ledger.tsv` lines (`handed_off_snippet_rendering_measurements_match_fern`). `src/emit.rs`'s `an_optional_list_the_recursion_break_empties_leaves_the_model_call` holds both lines; `snippet_departures_and_repairs_hold_only_their_lines` fails crozier's former `any_of=[]`.
