# Python enum proofs of the two literals-mode measurements

The `enum-header-params-stringified` and
`enum-extension-names-dropped-under-literals` documents now match in both enum
modes. Their complete certified `python_enums` trees are committed in
`docs/fern-measurements/naming-wire/` and compared by
`naming_wire_measurements_match_fern_under_python_enums`; the literals trees
remain held by `literals_mode_measurements_match_fern`.

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0 sends Python enum headers
as the member's `.value` and emits value descriptions as member docstrings.
The negative real-binary comparisons reject a stringified enum header or a
removed member docstring. Both modes use the same committed OpenAPI documents.
There is no remaining Python enum residual for either shape.
