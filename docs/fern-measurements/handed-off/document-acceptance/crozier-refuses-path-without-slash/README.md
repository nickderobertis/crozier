# crozier-refuses-path-without-slash

Root cause `crozier-refuses-path-without-slash` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **parity-gap-repaired** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

A path key without a leading slash: the empty key `''` (Azure-Samples' piping-diagram API).

## The measurement

`openapi.yml` declares `GET ''` beside `GET /firings/{firingId}`. It was authored from scratch for this measurement (SHA-256 `f643d7eae5868da71c0b3fc200b129070507de3e6b37d71de13428c4537de33f`).

`fern-expected/` is the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) complete, freshly generated, comment-stripped tree for it under `enum_type: python_enums`, generated in `tools/fern-goldens/fern-references.py`'s workspace (the one `generate-fern-fixture.sh` scaffolds) and stripped with `crozier internal-strip`; its Contract A digest is `026c50def2db403450da0d00c1ec3b82bc2590c82db5d59eadca00198d5ddce9`. `fern.log` and `exit-code` (`0`) are that run's.

`just fern-references measurements handed-off/document-acceptance/crozier-refuses-path-without-slash` regenerates `fern-expected/` (a `docs/fern-measurements/cases.tsv` row).

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `path-without-leading-slash: paths/`.
- crozier on this branch: generates, by default and under `--fern-strict`, a tree that byte-matches the certified pair's in `python_enums`, with the catalogued departures (the `X-Crozier-*` identity headers and the like) applied as `tests/fixtures/departures-ledger.tsv` records them.

## The verdict

`src/document_refusals.rs` exempts the empty key from `path-without-leading-slash` (any other slashless key stays refused, as the class's probe `paths/things` is), and `src/emit.rs`'s `requests_base_url` passes no path argument for it, as for `/`.

`runtime.txt` records the generated client's `get_status` requesting the base URL itself through `httpx.MockTransport`.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_repaired_cause_generates_its_certified_pair_tree`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `document_refusals::tests::only_the_empty_path_key_is_exempt_from_the_leading_slash`, `emit::document_acceptance_tests::an_empty_path_passes_no_path_argument`.
