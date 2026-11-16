# null-info-paths-components

Root cause `null-info-paths-components` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **refusal-kept** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

A document whose `info` and `paths` are written empty (null) beside `components.schemas` (datamodel-code-generator's `multiple_required_any_of.yaml`).

## The measurement

`openapi.yml` writes `info:` and `paths:` empty beside three component schemas. It was authored from scratch for this measurement (SHA-256 `b46ef9a3adba59aee60c823281c647b5707f3fce3a7f8fb32d0f5dc7c85dbd10`).

`fern.log` and `exit-code` (`0`) are the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) fresh run over it; its tree, the 35-file empty scaffold, is `fern-expected/`.

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 0, `generated 39 files into <tmp>/x`.
- crozier on this branch: refuses the document in default and `--fern-strict` modes, exit 1, writing nothing, with the class `missing-info-object` that `docs/fern-refusals/README.md` records.

## The verdict

The certified pair reads `info.version` first and fails (`Cannot read properties of null (reading 'version')`), exiting 0 over the empty scaffold (`fern-expected/`; `runtime.txt` imports it and finds no operation and no model type): a refusal under the refusal rule, and an empty SDK, which design-review ruling `empty-sdk-refused` keeps crozier refusing. crozier generated the components' models at the base; it now refuses the document in both modes with the new class [`missing-info-object`](../../../../fern-refusals/missing-info-object/evaluation.md) (`src/document_refusals.rs`), decided in `docs/fern-refusals/README.md`.

`runtime.txt` records the runs behind the verdict: crozier at the base and on this branch over the document, and an import of the certified pair's tree where it wrote one.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_refused_cause_is_refused_in_both_modes`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `document_refusals::tests::a_missing_or_null_info_is_refused_in_both_modes`.

**Regenerated at the certified pair.** The trees under this record's
`fern-expected/` (and `expected-literals/` or `literals/`, where it has them)
were regenerated at Fern CLI 5.200.0 / `fernapi/fern-python-sdk` 5.41.25, the
certified pair, one Fern run at a time through
`tools/fern-goldens/fern-references.py`'s own `generated_tree` (and
`reduce_overlay` for an overlay), and crozier's comparison holds the record to
them. Statements above that name Fern CLI 5.163.1 / fern-python-sdk 5.41.3
describe the measurement as first taken, at the pair certified then; a digest,
log or exit code they cite is that run's.
