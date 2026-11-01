# `R6`

The root cause `R6` from [`docs/openapi-surface/witness-search-fixture-only-operations-extensions/README.md`](../../../../../docs/openapi-surface/witness-search-fixture-only-operations-extensions/README.md), measured at the certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3) and settled by this node; its row is in [`../../type-declarations.tsv`](../../type-declarations.tsv).

`openapi.yml` was authored from scratch for this rule. `fern-expected/` is the certified pair's complete, comment-stripped python-enums output for it; the document declares no enum, so the enum mode does not change the tree. Both were generated with `tools/fern-goldens/fern-references.py`'s own `generated_tree` pipeline under the shared Fern lock: a cause named `R*` is no lower-case `cases.tsv` case path, so this directory has no `cases.tsv` row.

## Comparison

Path, query and body descriptions that open with a line break: an indented multi-line one, one ending in spaces, and single lines. The certified pair keeps the leading break as a blank line after the type, trims only trailing line breaks, and keeps the em-dash form for `\nOne line.`; crozier dropped the leading break and treated a single line ending in spaces as an em-dash line. Repaired in `src/emit.rs` (`reference_param_suffix`); crozier now byte-matches, and so do OpenAQ and agentstack. `reference-description-leading-newline` is the same rule (its directory holds its own document).

**Verdict: `parity-gap-repaired`.** crozier differed from the certified pair; it now byte-matches the committed tree.

The verdict rests on the generated files alone (names, types, docstrings, `reference.md` lines), not on behaviour, so no `runtime.txt` is owed. `handed_off_type_declarations_match_the_certified_pair` in `crates/crozier-e2e/tests/e2e/handed_off_type_declarations.rs` runs the real `crozier` binary on `openapi.yml` and compares its SDK with this tree file for file, and shows the comparison failing once the rule's bytes are written back the way crozier wrote them before; the `handed_off_type_declarations_tests` unit tests in `src/ir.rs` drive the repaired functions on this document.
