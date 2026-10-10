# Multipart object search

## Witness search

At `4ea078430`, the shared census loader read all 283 registered source records.
The local-reference walk followed Request Body and Schema references with
cycle protection and inspected multipart property maps for: a component that
aliases an object; an inline object property named `json`; a nullable binary
`anyOf`; and an array whose binary items alone carry its description. Each
source's recorded SHA-256 was verified against its bytes.
[sources.tsv](sources.tsv) records zero exact declarations for each shape.

The alias and JSON-name scans also recorded whether a required binary file
appeared beside the object. There were no candidates even before that extra
requirement. The bounded scan inspected directly declared property maps; it
does not exhaust public publishers or expand inherited property maps, so
these are incomplete searches, not claims that real APIs cannot declare them.
No network search was run.

| key | verdict | why |
|---|---|---|
| `media-type-multipart` | `search-incomplete` | No complete registered-source witness for either new handling site; publisher and inherited-property searches remain incomplete |

The handling sites are `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]`
and `src/emit.rs::Imports::json_module[=^ {12}self\.json_module_alias = true;$]`.

## Renewed search

| key | outcome | handling site | declarations | handwritten fixture |
|---|---|---|---|---|
| `media-type-multipart` | `none-registrable` | `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | 0 | `multipart-alias-object` |
| `media-type-multipart` | `none-registrable` | `src/emit.rs::Imports::json_module[=^ {12}self\.json_module_alias = true;$]` | 0 | `multipart-json-module` |

The independently authored cartography and survey documents retain a required
file beside each object. The survey document has an adjacent encoded-object
method without a JSON-named argument, proving both module imports coexist.
Both complete trees use Fern CLI 5.67.1, `fernapi/fern-python-sdk` 5.20.0,
organization/package `fern`, project `default_package_name`, packaged preview
layout, no audience filter and `pydantic_config.enum_type: python_enums`.
Separate certified literals trees use the same sources with `enum_type`
unset. These are handwritten proofs, not real witnesses or corpus rows.
