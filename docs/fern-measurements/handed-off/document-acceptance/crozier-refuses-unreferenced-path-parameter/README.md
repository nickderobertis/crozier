# crozier-refuses-unreferenced-path-parameter

Root cause `crozier-refuses-unreferenced-path-parameter` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **refusal-kept** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

An operation declaring a path parameter its path template does not name (swagger-core's ticket-3303 petstore `GET /pet/{petId}` with `userId`).

## The measurement

`openapi.yml` declares `growerId` in path beside `GET /trees/{treeId}`, written Swagger-2 style with no `schema`, as the real document writes it, with an `info` object. It was authored from scratch for this measurement (SHA-256 `8132313081db6089b8567ac6140f03fcafb6a73571e0bae909f1bc26f57a19c8`).

`fern.log` and `exit-code` (`1`) are the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) fresh run over it; it wrote no tree.

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `path-parameter-unreferenced: GET /trees/{treeId} parameter growerId`.
- crozier on this branch: refuses the document in default and `--fern-strict` modes, exit 1, writing nothing, with the class `path-parameter-unreferenced` that `docs/fern-refusals/README.md` records.

## The verdict

None: the certified pair refuses (`fern generate` exits 1: `Path parameter is unreferenced in endpoint: growerId.`), and crozier refuses as `path-parameter-unreferenced` in both modes. The record's own document has no `info` at all, so the certified pair's parse fails on it first (exit 0 over the empty scaffold): it is refused by both, by crozier now as [`missing-info-object`](../../../../fern-refusals/missing-info-object/evaluation.md).

`runtime.txt` records the runs behind the verdict: crozier at the base and on this branch over the document, and an import of the certified pair's tree where it wrote one.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_refused_cause_is_refused_in_both_modes`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
