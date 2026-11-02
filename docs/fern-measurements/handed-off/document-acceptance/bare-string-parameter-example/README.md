# bare-string-parameter-example

Root cause `bare-string-parameter-example` of the [bodies-and-paths record](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

A parameter's or media type's `examples` map holding a bare value (`north: north-sector`), or written as one Reference Object (`examples: {$ref: '#/components/examples/BeaconCode'}`, a `$ref` key whose value is a string).

## The measurement

`openapi.yml` declares both forms on a path and a query parameter and on a `text/plain` request body. It was authored from scratch for this measurement (SHA-256 `eae65b1eb09203f153eba13ce43f321542638ce3a45e76f75941c08a61afb797`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `5c83e8fcd80e14ead8bafaa462536de7f546c78c0ec444a428ca24e6b8be0616`. `fern.log` and `exit-code` (`0`) are that run's.

`tools/fern-goldens/fern-references.py generate measurements handed-off/document-acceptance/bare-string-parameter-example` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `could not parse OpenAPI document: `expected mapping start` at the parameter's `examples` entry`.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in `python_enums`, with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

`src/openapi.rs`'s `de_named_examples` reads a bare value as that example's value (the certified pair works `sector="north-sector"`) and drops a `$ref` entry that is no map (the certified pair writes its placeholder `beacon_code="beaconCode"`), rather than failing the parse.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `openapi::document_acceptance_tests::bare_named_examples_read_as_values_and_a_bare_ref_entry_is_dropped`.
