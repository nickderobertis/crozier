# crozier-refuses-boolean-schema

Root cause `crozier-refuses-boolean-schema` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

An OpenAPI 3.1 boolean schema (`true` or `false`) as an `allOf`, `oneOf` or `anyOf` member.

## The measurement

`openapi.yml` declares `Humidity: allOf [number, true]`, `DewPoint: allOf [number, false]`, `Label: anyOf [false, string]`, `Unit: oneOf [string, true]`, `Anything: allOf [true]`, `Calibration: allOf [$ref Reading, true]` and a `Seal` object with a `false` property, each its own component so a boolean property (which makes its whole object `typing.Any` to both) does not hide the members. It was authored from scratch for this measurement (SHA-256 `3d17596789ae4547e51a4bf6abd92b91c8e1a60a1acb0142f533fe92c3e2c1ca`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `83fbfec705712ad13232965e86ffe4c9e99b53a8ed96fb5ea3dacad60638707c`. `fern.log` and `exit-code` (`0`) are that run's.

`just fern-references measurements handed-off/document-acceptance/crozier-refuses-boolean-schema` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `could not parse OpenAPI document: `data did not match any variant of untagged enum Composition``.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in `python_enums`, with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

`src/openapi.rs` reads composition members through the tolerant `MaybeSchema` boundary: `de_all_of` drops a boolean `allOf` member, `composition_member` reads a boolean `oneOf`/`anyOf` member as the unconstrained schema (`typing.Any`), `normalize_single_scalar_all_of` reads an `allOf` left with one inline scalar as that scalar (`Humidity = float`), and an `allOf` of booleans alone reads as one empty object, the empty `Anything` model the certified pair writes. The certified pair's `Calibration = Reading` alias follows.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `openapi::document_acceptance_tests::boolean_composition_members_read_as_the_certified_pair_reads_them`, `openapi::document_acceptance_tests::a_single_scalar_all_of_loads_as_its_member`.
