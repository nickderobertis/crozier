# Header enum values and member descriptions

These two complete, comment-stripped trees were generated with Fern CLI
5.67.1 and `fernapi/fern-python-sdk` 5.20.0, with
`pydantic_config.enum_type: python_enums`. Each uses the document of the same
name in [the literals-mode measurements](../literals-mode/README.md), so the
two modes exercise identical inputs.

| case | Python enum behaviour |
|---|---|
| `enum-header-params-stringified` | Required and optional enum headers use the member's `.value`, guarded by `is not None`; ordinary string headers retain their string encoding. |
| `enum-extension-names-dropped-under-literals` | Extension names name the members, and each value description becomes its member's docstring. |

`naming_wire_measurements_match_fern_under_python_enums` drives the real
crozier binary and compares each complete tree through `src/parity.rs`, with
departures pinned in `tests/fixtures/departures-ledger.tsv`.
`naming_wire_shapes_fail_on_an_unexplained_byte` changes the header expression
or removes a member docstring in a temporary reference tree and requires the
comparison to fail. The literals-mode gate continues to compare the same
documents with `--enum-type literals`.

To regenerate, use the workspace and environment described in
[the probe procedure](../../openapi-surface/probes/AGENTS.md#re-running-one),
copying the corresponding literals-mode `openapi.yml`. Preserve the complete
output, apply `crozier internal-strip`, and retain the generator metadata.
Do not edit the generated Python to match crozier.
