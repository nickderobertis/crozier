# crozier-refuses-type-name-collision

Root cause `crozier-refuses-type-name-collision` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

One type declared in two namespaces by crozier where the certified pair declares it once: a multipart-only component's nested inline type (paios' `CreateImageEditRequestModelOne`), and a component its `x-fern-sdk-group-name` places in a tag's package (AssemblyAI's `RedactedAudioStatus`).

## The measurement

`openapi.yml` posts a multipart `RetouchPhotoRequest` whose `options` object declares a `finish` enum (two levels deep), and answers a proof with `ProofResponse`/`ProofStatus`, both grouped `photos`. The multipart body carries no file part, so the README's chosen call is not the other area's `readme-endpoint-choice`; a nested object rather than paios' `anyOf` of strings keeps the part's encoding out of `multipart-scalar-union-part-encoding`. It was authored from scratch for this measurement (SHA-256 `f899518bb38f662f7b867b857005fadb5ad75592b5e9ea33dc41d9adc7a7daf7`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `15e63ee5370518cd8972f1d57635d69b18fb4e20adf468ea82ff74f82e253a2c`. `fern.log` and `exit-code` (`0`) are that run's.

`expected-literals/` is the same pair's tree with `enum_type` unset (Fern's `Literal` default, crozier's `enum-type: literals`), reduced by `tools/fern-goldens/golden_overlay.py` to the files that differ from `fern-expected/`; its manifest records the complete tree's digest `326abefbb5b1fa7cc9a0d3c1d35a449a949c4c2070aa5ffea28c4956c3074d74` and the files it removes. `fern.literals.log` and `exit-code.literals` are that run's.

`tools/fern-goldens/fern-references.py generate measurements handed-off/document-acceptance/crozier-refuses-type-name-collision` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `type-name-collision: enum ProofStatus in namespace photos collides with a schema declaration; give the types distinct declared names`.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in both enum modes (`fern-expected/` and the rebuilt `expected-literals/` tree), with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

`src/ir.rs`'s `move_inline_body_enums_to_tags` removes a dropped form component's nested types from the root transitively, not only the field types themselves; `src/name_refusals.rs` no longer counts a group-placed component as an enum colliding with its own root declaration.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`, `enum_bearing_repairs_generate_the_literals_tree_too`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `ir::document_acceptance_tests::a_multipart_components_nested_types_leave_the_root`, `name_refusals::tests::a_group_placed_component_enum_is_no_collision`.
