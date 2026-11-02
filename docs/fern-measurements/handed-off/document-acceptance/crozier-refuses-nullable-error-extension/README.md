# crozier-refuses-nullable-error-extension

Root cause `crozier-refuses-nullable-error-extension` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

An `allOf` extension of a `nullable` parent with required properties, under the first success response, while the response's example omits a property the extension requires (plaid's `Warning.cause`).

## The measurement

`openapi.yml` mirrors that path: `ExportResponse.notices[]` → `Notice.reason` → `Reason: allOf [$ref LedgerError (nullable, required), {accountId}]`, each object declaring `additionalProperties: true`. It was authored from scratch for this measurement (SHA-256 `29420f50097d74076dfe0e3eaaac19c78dc43ba9782b52c9d33ff5904523f0ab`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `c6aeb9d1c204a05956839611cbbb20e8820a59d5e874968827b8d2e8ba026e51`. `fern.log` and `exit-code` (`0`) are that run's.

`tools/fern-goldens/fern-references.py generate measurements handed-off/document-acceptance/crozier-refuses-nullable-error-extension` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `example-missing-required-property: POST /exports/get response extends nullable #/components/schemas/LedgerError`.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in `python_enums`, with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

Variants measured at the certified pair (logs kept in the shared cache) isolate the rule: the extension refuses (`Example is missing required property`) when reached directly or through closed objects, and generates when an object above it on the path declares `additionalProperties: true` (the response root or the `Notice` holding the property; the extension's or the parent's own declaration does not count). `src/document_refusals/examples.rs`'s `nullable_parent_example` now walks with `reach_closed`, which visits an open object but not its members.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `document_refusals::tests::a_nullable_extension_behind_an_open_object_is_not_refused`.
