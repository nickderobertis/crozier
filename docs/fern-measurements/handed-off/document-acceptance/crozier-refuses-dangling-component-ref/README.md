# crozier-refuses-dangling-component-ref

Root cause `crozier-refuses-dangling-component-ref` of the [schemas record](../../../../openapi-surface/witness-search-fixture-only-schemas/README.md), handed off to the `document-acceptance` area. Verdict: **refusal-kept** (`docs/fern-measurements/handed-off/document-acceptance.tsv`).

## The rule

A response written as a `$ref` to a component the document declares as a schema, not as a response (speakeasy's bolt-embedded `403: {$ref: '#/components/schemas/errors_bolt_api_response'}`).

## The measurement

`openapi.yml` answers `403` with `$ref: '#/components/schemas/payment_error'`. It was authored from scratch for this measurement (SHA-256 `581ce566c97e451c423ab8fb54533ecb0589003e2422c6f22e531607739aaf28`).

`fern.log` and `exit-code` (`0`) are the certified pair's (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) fresh run over it; its tree, the 35-file empty scaffold, is `fern-expected/`.

## The comparison

- crozier at this node's base (`6b4509ab9`): exit 1, `unresolved-reference: paths//payments/post/responses/403: #/components/schemas/payment_error`.
- crozier on this branch: refuses the document in default and `--fern-strict` modes, exit 1, writing nothing, with the class `unresolved-reference` that `docs/fern-refusals/README.md` records.

## The verdict

None: the certified pair's parse fails (`Failed to resolve #/components/schemas/payment_error` in `resolveResponseReference`) and it exits 0 over the 35-file empty scaffold (`fern-expected/`, a client with no operations and no model types; `runtime.txt` imports it), a refusal under the refusal rule. crozier refuses the document as `unresolved-reference` in both modes, as at the base.

`runtime.txt` records the runs behind the verdict: crozier at the base and on this branch over the document, and an import of the certified pair's tree where it wrote one.

## What holds it

- `crates/crozier-e2e/tests/e2e/document_acceptance.rs`: `each_refused_cause_is_refused_in_both_modes`; the narrowed refusals' controls are `narrowed_refusals_still_fire_on_their_controls`.
