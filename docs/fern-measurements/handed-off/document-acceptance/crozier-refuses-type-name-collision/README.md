# crozier-refuses-type-name-collision

Root cause `crozier-refuses-type-name-collision` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

One type crozier refused as declared twice where the certified pair declares it once: a multipart-only component's nested inline type (paios' `CreateImageEditRequestModelOne`), a component its `x-fern-sdk-group-name` places in a tag's package (AssemblyAI's `RedactedAudioStatus`), and two components whose names differ only in their first letter's case (`Shelf`, `shelf`), which the certified pair merges into the later declaration.

## The measurement

`openapi.yml` posts a multipart `RetouchPhotoRequest` whose `options` object declares a `finish` enum (two levels deep), answers a proof with `ProofResponse`/`ProofStatus`, both grouped `photos`, and declares an unreferenced `Shelf` beside a later `shelf`. The multipart body carries no file part, so the README's chosen call is not the other area's `readme-endpoint-choice`; a nested object rather than paios' `anyOf` of strings keeps the part's encoding out of `multipart-scalar-union-part-encoding`. Beside it, from scratch: `first-letter-operationless-probe.openapi.yml` (a `Print`/`print` pair in a document with no operations; the certified pair exits 0 writing one `types/print.py`, kept stripped as `first-letter-operationless-probe.fern-print.py.txt`), and the controls `first-letter-referenced-object-control.openapi.yml` and `first-letter-referenced-enum-control.openapi.yml`, where an operation answers the earlier declaration (the certified pair exits 1: `Unexpected property "id"`; `"WALK" is not a valid example for this enum`). Each `<stem>.fern.log` and `<stem>.exit-code` is the certified pair's run over that document. It was authored from scratch for this measurement (SHA-256 `52bc2d83ec9cfb803a6febbd5e88db18805812043252a71baab00bf4cc2b8617`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `8de865e3942d5134887c75d113ddd24c091506ed420e5f7a1568eb042f320eff`. `fern.log` and `exit-code` (`0`) are that run's.

`expected-literals/` is the same pair's tree with `enum_type` unset (Fern's `Literal` default, crozier's `enum-type: literals`), reduced by `tools/fern-goldens/golden_overlay.py` to the files that differ from `fern-expected/`; its manifest records the complete tree's digest `02b4294fdedc00cedc2fe0120ba82e8dd688d0727a2254b19bc59d406b090c8f` and the files it removes. `fern.literals.log` and `exit-code.literals` are that run's.

`just fern-references measurements handed-off/document-acceptance/crozier-refuses-type-name-collision` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `type-name-collision: component schemas "Shelf" and "shelf" both declare type Shelf; give them distinct names`.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in both enum modes (`fern-expected/` and the rebuilt `expected-literals/` tree), with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

`src/ir.rs`'s `move_inline_body_enums_to_tags` removes a dropped form component's nested types from the root transitively, not only the field types themselves; `src/name_refusals.rs` no longer counts a group-placed component as an enum colliding with its own root declaration, and no longer refuses first-letter-case twins at all: `deduplicate_type_names` keeps the later one, as the certified pair does. Where an operation answers the earlier twin, the certified pair's refusal is its example check, and crozier's example checks refuse the same documents with the same classes (`src/document_refusals/examples.rs`'s `collision_class` now also compares two enums: the earlier's first value, Fern's example of it, must be among the later's).

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`, `enum_bearing_repairs_generate_the_literals_tree_too`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `ir::document_acceptance_tests::a_multipart_components_nested_types_leave_the_root`, `name_refusals::tests::a_group_placed_component_enum_is_no_collision`, `name_refusals::tests::components_differing_in_first_letter_case_are_no_refusal`, `document_refusals::examples::tests::an_earlier_enum_whose_first_value_the_later_drops_collides`.
