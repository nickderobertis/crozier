# Model and reference witness searches

## Scalar formats

| key | verdict | complete trigger |
|---|---|---|
| `number-format-uint64-typed-int` | `search-incomplete` | An object property declares `type: number` and `format: uint64`. |
| `string-json-format-typed-any` | `search-incomplete` | An object property declares `type: string` and `format: json-string`. |

The bounded APIs.guru screen at immutable revision
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` reported no exact declaration
for either shape. An unsigned 32-bit number in the SiriKit Cloud Media
specification is a partial candidate: its format does not declare the required
unsigned 64-bit trigger. Telnyx's JSON-related formats are also partial
candidates because their format spelling is not `json-string`. These partial
candidates cannot stand as complete witnesses.

This record renews that bounded result by reading every committed corpus source
on this branch on 2026-10-08. The retained
[`scalar-formats.tsv`](scalar-formats.tsv) records each source's exact SHA-256
and the two declaration counts. The walk reads parsed mappings recursively,
counting nodes with the exact type and format pair, so it includes response,
request and component properties as well as any declarations outside properties.
Neither trigger occurs. This is a bounded search, not a claim that no publisher
uses either format.

## Renewed search

| key | result | proof |
|---|---|---|
| `number-format-uint64-typed-int` | `none-registrable` | No exact declaration in the committed-source renewal; independent `material-register` fixture. |
| `string-json-format-typed-any` | `none-registrable` | No exact declaration in the committed-source renewal; independent `material-register` fixture. |

The fresh fixture declares a material record with both properties and adjacent
`double` and `uuid` controls. Its complete tree is unedited output of Fern CLI
5.67.1 and `fernapi/fern-python-sdk` 5.20.0 with
`pydantic_config.enum_type: python_enums`. A separate complete certified tree
under `docs/fern-measurements/models-refs-literals/material-register/fern-expected`
uses Fern's default literals mode (no generator configuration). The scoped
real-binary test compares both modes bidirectionally through `src/parity.rs`: the
scalar annotations agree, while the certified literals tree omits the enum
runtime module. It counts only as handwritten
proof, never as a publisher witness.

## Remote component identities

| key | verdict | complete trigger |
|---|---|---|
| `remote-document-local-pointer-resolved-against-root` | `search-incomplete` | A root component names a remote component whose property uses a local pointer into that remote document; the dependency is absent from the root. |
| `remote-ref-at-use-site-inlined` | `search-incomplete` | An operation response directly names an absolute-URL reference to a remote component schema. |

The bounded APIs.guru screen at revision
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` found no complete component-fragment
witness. The renewal on 2026-10-08 reads the 282 committed source documents,
recording their SHA-256 and declaration counts in
[`remote-components.tsv`](remote-components.tsv). It distinguishes root
component aliases and operation response schemas from absolute references
elsewhere. No direct component-fragment trigger occurs.

Helios's references name top-level definitions rather than OpenAPI component
schemas. MockServer references a whole JSON Schema document. Fiware's absolute
references occur in example data. Each misses the required trigger and cannot
stand as a complete witness. This bounded search remains incomplete outside
that population.

The independently authored Library Records proof uses two committed documents
under `tests/e2e/fixtures/models-refs-remote/library-records`. A real loopback
HTTP server serves the second document; no network acquisition is needed in
CI. It combines a root Catalogue alias, its remote Curator dependency, and a
direct Curator response. It proves both named identities and a failed-fetch
recovery journey. It is handwritten proof, never a real witness.

Its complete certified packages use Fern CLI 5.67.1 and
`fernapi/fern-python-sdk` 5.20.0: the tree under
`docs/fern-measurements/models-refs-remote/library-records/fern-expected` uses
`pydantic_config.enum_type: python_enums`; the separate tree under
`docs/fern-measurements/models-refs-literals/library-records/fern-expected` uses
default literals mode. The scoped real-binary test compares each complete
package bidirectionally through `src/parity.rs`, with only catalogued identity
departures. Remote acquisition does not introduce a new configuration setting.

## Renewed remote search

| key | result | proof |
|---|---|---|
| `remote-document-local-pointer-resolved-against-root` | `none-registrable` | No complete trigger in the committed-source renewal; independently authored Library Records multi-file HTTP proof. |
| `remote-ref-at-use-site-inlined` | `none-registrable` | No complete trigger in the committed-source renewal; independently authored Library Records multi-file HTTP proof. |
