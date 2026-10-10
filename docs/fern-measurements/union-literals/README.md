# Certified literals trees for the union fixtures

Each directory here is named for one hand-written union fixture under
[`../../openapi-surface/handwritten/`](../../openapi-surface/handwritten/AGENTS.md).
Its `fern-expected/` holds the tree Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0
generated from that fixture's unedited `openapi.yml` with `enum_type` unset
(Fern's literals default; crozier's `--enum-type literals`), in the same
workspace as the fixture's own `fern-expected/` but for that setting, stripped
the same way. It is committed as an overlay of `fern-expected/`, by
`tools/fern-goldens/golden_overlay.py reduce`: only the files whose bytes differ,
plus `.crozier-overlay.json`, which names the files Fern omits under the setting
(`src/fern/core/enum.py`) and records the complete tree's Contract A `digest`.

`union_shapes_match_complete_goldens_in_both_enum_modes` in
`crates/crozier-e2e/tests/e2e/unions.rs` rebuilds each complete tree, holds it
to that digest, and compares crozier's literals output with it file by file
through `src/parity.rs`; `union_shape_goldens_match_in_process_in_both_enum_modes`
in `tests/generation.rs` does the same in-process. No file here or in
`fern-expected/` was edited to fit crozier.
