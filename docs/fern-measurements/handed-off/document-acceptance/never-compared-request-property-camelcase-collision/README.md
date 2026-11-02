# never-compared-request-property-camelcase-collision

Root cause `never-compared-request-property-camelcase-collision` of the [bodies-and-paths (never compared) record](../../../../openapi-surface/witness-search-fixture-only-bodies-paths/README.md), handed off to the `document-acceptance` area. Verdict: **refusal-kept** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

A query parameter `shelf[]` beside `shelf` (api-platform's schema-generator `GET /books/{id}/reviews` with `book` and `book[]`).

## The measurement

`openapi.yml` lists loans filtered by `shelf` and `shelf[]`. It was authored from scratch for this measurement (SHA-256 `c81a5a3903a46fb20977112fb1ac9aa70736db0e5486c7611b4b12523b8bbff0`).

`fern.log` and `exit-code` (`1`) are the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) fresh run over it; it wrote no tree.

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `crozier: formatting src/fern/raw_client.py with ruff failed: ruff exited with exit status: 2: error: Failed to parse src/fern/raw_client.py:20:65: Duplicate parameter "shelf"`.
- crozier on this branch: refuses the document in default and `--fern-strict` modes, exit 1, writing nothing, with the class `request-property-camelcase-collision` that `docs/fern-refusals/README.md` records.

## The verdict

The certified pair refuses (`fern generate` exits 1: `Multiple request properties resolve to the same generated name shelf after camelCase normalization`). crozier wrote a method taking `shelf` twice, which `ruff format` rejects (`runtime.txt`); `src/name_refusals.rs` now trims non-alphanumeric ends before comparing names, so crozier refuses it as `request-property-camelcase-collision` in both modes. `shelves[]` beside `shelf` still generates.

`runtime.txt` records the runs behind the verdict: crozier at the base and on this branch over the document, and an import of the certified pair's tree where it wrote one.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_refused_cause_is_refused_in_both_modes`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
- Unit tests: `name_refusals::tests::a_bracketed_query_name_collides_with_its_bare_name`.
