# never-compared-type-name-collision

Root cause `never-compared-type-name-collision` of the [bodies-and-paths (never compared) record](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

Two component schemas whose names differ only in their first letter's case (konfig-sdks' peach-payments `PaymentType`, `paymentType`).

## The measurement

`openapi.yml` declares `TransferMode` (two values) and later `transferMode` (four), each referenced. It was authored from scratch for this measurement (SHA-256 `d8be91c36b08a921dda939352693bfa1b9862797bd5fdf1f0da86f9f54957f64`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `6e7d5a340c6409f2968307b8ff09fdd2131a6a2a587de8f3e17b9362fb2ee9e5`. `fern.log` and `exit-code` (`0`) are that run's.

`expected-literals/` is the same pair's tree with `enum_type` unset (Fern's `Literal` default, crozier's `enum-type: literals`), reduced by `tools/fern-goldens/golden_overlay.py` to the files that differ from `fern-expected/`; its manifest records the complete tree's digest `d86dc20c2ef2715ecd82cddb03801df6cfafe80fccf4f72c6f0d3423f6305847` and the files it removes. `fern.literals.log` and `exit-code.literals` are that run's.

`tools/fern-goldens/fern-references.py generate measurements handed-off/document-acceptance/never-compared-type-name-collision` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `type-name-collision: component schemas "TransferMode" and "transferMode" both declare type TransferMode; give them distinct names`.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in both enum modes (`fern-expected/` and the rebuilt `expected-literals/` tree), with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

The certified pair writes one `TransferMode` enum with the later declaration's values; crozier's `deduplicate_type_names` already keeps the later declaration, so `src/name_refusals.rs` drops the first-letter-case refusal. The konfig-dev copy of the same API stays refused by both, for its `PaymentResponse` collision.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`, `enum_bearing_repairs_generate_the_literals_tree_too`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `name_refusals::tests::components_differing_in_first_letter_case_are_no_refusal`.
