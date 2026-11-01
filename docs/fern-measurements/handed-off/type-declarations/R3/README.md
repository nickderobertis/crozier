# `R3`

The root cause `R3` from [`docs/openapi-surface/witness-search-fixture-only-operations-extensions/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-operations-extensions/README.md), measured at the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) and settled by this node; its row is in [`../../type-declarations.tsv`](../../type-declarations.tsv).

`openapi.yml` was authored from scratch for this rule. `fern-expected/` is the certified pair's complete, comment-stripped python-enums output for it; the document declares no enum, so the enum mode does not change the tree. It was generated with the `generated_tree` pipeline `just fern-references` runs for every measurement, called directly under the shared Fern lock: a cause named `R*` is no lower-case `cases.tsv` case path, so `just fern-references measurements` cannot name this directory and it has no `cases.tsv` row.

## Comparison

Responses and request bodies written `{nullable: true, oneOf: [$ref X]}`. The certified pair returns `typing.Optional[ClimateReading]` and takes `request: typing.Optional[GreenhouseCreate] = None`, keeping `VentCommand` exported; crozier unwrapped the member and flattened the bodies. Repaired in `src/openapi.rs` (`collapse_sole_composition_member`) and `src/ir.rs` (`nullable_sole_member_ref`, `resolve_request_body`, `build_endpoint`); crozier now byte-matches, and so does keyserv.

**Verdict: `parity-gap-repaired`.** crozier differed from the certified pair; it now byte-matches the committed tree.

The verdict rests on the generated files alone (names, types, docstrings, `reference.md` lines), not on behaviour, so no `runtime.txt` is owed. `handed_off_type_declarations_match_the_certified_pair` in `crates/crozier-e2e/tests/e2e/handed_off_type_declarations.rs` runs the real `crozier` binary on `openapi.yml` and compares its SDK with this tree file for file, and shows the comparison failing once the rule's bytes are written back the way crozier wrote them before; the `handed_off_type_declarations_tests` unit tests in `src/ir.rs` drive the repaired functions on this document.
