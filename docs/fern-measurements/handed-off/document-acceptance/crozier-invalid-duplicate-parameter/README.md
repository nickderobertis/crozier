# crozier-invalid-duplicate-parameter

Root cause `crozier-invalid-duplicate-parameter` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

An `allOf` body of a `$ref` parent, an inline object and an inline `anyOf` whose branches redeclare the parent's properties (pushboy's `SendNotificationRequest`).

## The measurement

`openapi.yml` sends a doorbell alert whose body is `allOf: [$ref AlertPayload, {deliverAt}, {anyOf: [{headline}, {message}, {muted: const true}]}]`. It was authored from scratch for this measurement (SHA-256 `901480a7145339fc9ca6c6d01b4c11324ffa3ad363f240a84b77782cdb509cf0`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `329837cf9d49837736f4729f210c01aa6cf5c0d7a39eddbc5cc49b1ade60b606`. `fern.log` and `exit-code` (`0`) are that run's.

`expected-literals/` is the same pair's tree with `enum_type` unset (Fern's `Literal` default, crozier's `enum-type: literals`), reduced by `tools/fern-goldens/golden_overlay.py` to the files that differ from `fern-expected/`; its manifest records the complete tree's digest `f7a6f49d540ed2c8192c2f62dd2ac8a3cab366f629c367a62dea7f5fbbd2837e` and the files it removes. `fern.literals.log` and `exit-code.literals` are that run's.

`just fern-references measurements handed-off/document-acceptance/crozier-invalid-duplicate-parameter` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `crozier: formatting src/fern/raw_client.py with ruff failed: ruff exited with exit status: 2: error: Failed to parse src/fern/raw_client.py:26:207: Duplicate parameter "headline"`.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in both enum modes (`fern-expected/` and the rebuilt `expected-literals/` tree), with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

The body is a `$ref` to the component, so its arguments are the component model's fields. `src/ir.rs`'s object lowering (`add_object`) now counts an inline `anyOf` member's branch properties among the model's declared fields, so a parent property a branch redeclares is one field, where the branch's declaration wins and keeps its place: `deliver_at`, `headline`, `message`, `muted`, then the parent's `chime`. crozier wrote `headline`, `message` and `muted` twice, which `ruff format` rejects (`Duplicate parameter`). An inline body of the same members takes `parents_with_inline_members`, which merges an `anyOf` member's branch properties the same way.

`runtime.txt` records crozier at the base failing `ruff format`, the finished branch generating in both modes, and the generated client's `send_alert` sending each property once through `httpx.MockTransport`.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`, `enum_bearing_repairs_generate_the_literals_tree_too`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `ir::document_acceptance_tests::branch_properties_a_parent_redeclares_are_one_field_each`, `ir::document_acceptance_tests::parents_with_inline_members_rewrites_only_parents_beside_plain_members`.
