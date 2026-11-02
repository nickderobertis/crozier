# never-compared-request-property-name-collision

Root cause `never-compared-request-property-name-collision` of the [bodies-and-paths (never compared) record](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

A path parameter named like a property of the body's direct `allOf` parent (FOSSology's `PUT /users/{id}` over `allOf: [$ref User, {…}]`).

## The measurement

`openapi.yml` updates a library member at `PUT /members/{id}` whose body is `allOf: [$ref Member, {password, homeShelf}]`, offered as JSON and form-urlencoded. It was authored from scratch for this measurement (SHA-256 `441e073c7fe149d5c7a306d36cdeb8a248effdbe3a3b93b2bf11e280d1f9f19c`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `c82328379cbf23c7895f99de84da6f86b28b1fb081e53bdcedac09333c31be8c`. `fern.log` and `exit-code` (`0`) are that run's.

`tools/fern-goldens/fern-references.py generate measurements handed-off/document-acceptance/never-compared-request-property-name-collision` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `request-property-name-collision: PUT /members/{id} body property "id" collides with another request property; give the properties distinct declared names`.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in `python_enums`, with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

`src/ir.rs`'s `parents_with_inline_members` lowers an `allOf` of `$ref` parents and plain inline objects field by field, the inline members' first (crozier lowered no body for it and dropped the operation as unemittable); the IR's existing rename then gives the path parameter the certified pair's `id_path_param`, and `src/name_refusals.rs`'s collision check treats crozier's own trailing-underscore form as an unrenamed parameter, so a grandparent's property still refuses (the class's probe).

`runtime.txt` records the generated client's `update_member(7, …, id=3)` sending `PUT /members/7` with the body's own `id` through `httpx.MockTransport`.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `ir::document_acceptance_tests::a_parent_and_inline_member_body_is_their_fields_inline_first`, `name_refusals::tests::a_path_parameter_keeps_its_name_against_a_grandparents_body_property`.
