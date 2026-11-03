# Certified literals setting for parameter proofs

These nine inputs are independently authored documents. Seven live under
`docs/openapi-surface/handwritten/`. `observatory-client-headers` and
`warehouse-header-token` were retired as hand-written proofs once corpus row
4405 (`loonfs`) covered their shape, and now live under
[`../parameter-lowering/`](../parameter-lowering/README.md). Each input's
complete Python-enum tree and pins are recorded in its own directory. Each was also generated unedited by CLI 5.67.1 with
`fernapi/fern-python-sdk` 5.20.0, `enum_type` unset (literals), package `fern`,
project `default_package_name`, client `FernApi`, extra fields `allow`, retries 2,
all audiences, packaged preview, CI invocation and GitHub metadata.

Every literals tree differs only in `.fern/metadata.json` (the complete certified
file here) and the omission of `src/fern/core/enum.py`. `certified-trees.json`
records each complete stripped tree's Contract A digest. The real-binary test
`parameter_extension_shapes_match_complete_goldens_in_both_enum_modes`
reconstructs the tree, checks that digest, and compares every generated file
bidirectionally through `src/parity.rs`. Neither the source nor generated tree
was edited to fit crozier. The overlay is shared because its bytes are identical
for the original nine inputs; the exact per-input digest guards that claim.

Warehouse Ledger retains its complete certified metadata in
`warehouse-header-token.metadata.json`.
Its separate digest guards that exact literals tree.
