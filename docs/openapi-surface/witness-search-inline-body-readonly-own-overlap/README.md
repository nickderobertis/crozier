# Inline body read-only own overlap search

## Witness search

Only corpus sources and committed remote-tree fragments are recorded here;
local test inputs are excluded from real-witness evidence.

At `20ffc7147`, an offline walk inspected the same 283 source records the
[JSON request shape search](../witness-search-json-request-shapes/README.md)
enumerated. The shared census loader parsed every record, and each record's
SHA-256 was computed from its committed bytes. [sources.tsv](sources.tsv)
records the results.

The conjunction inspected was a JSON request body whose resolved schema has its
own `properties`, where one property is `readOnly` (declared, or through a
`$ref` to a readOnly component) and an `allOf` `$ref` parent also declares a
property with that name. The `readonly-shadow-required` column counts the
subset where the parent requires that property, a shape pinned Fern refuses.
No record declares either. No real witness is claimed.

The walk follows local references with cycle protection. It does not resolve
cross-document references or exhaust public publishers, so the result is an
incomplete search rather than a claim of exhaustive absence. No network
acquisition was performed.

| key | verdict | why |
|---|---|---|
| `request-body-content` | `search-incomplete` | No registered-source inline body whose own readOnly property shadows an inherited one |

The handling site is:

- `src/ir.rs::resolve_request_body[if let Some\(own\) = fields$]`

## Renewed search

| key | result | scope |
|---|---|---|
| `request-body-content` | `none-registrable` | The readOnly own-over-parent conjunction over the committed source records above |
