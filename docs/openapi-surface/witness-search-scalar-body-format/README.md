# Formatted scalar-body witness search

## Witness search

The missing handling sites are
`src/ir.rs::scalar_body[=Some\("uuid" \x7c "byte"\)]` for UUID and byte,
and `src/ir.rs::scalar_body[=Some\("date"\) =>]` for date. The shape is a
request body whose media schema directly declares `type: string` and the format,
not a model property, parameter or response carrying that format.

The complete 241-source registered census declares UUID in 42 sources (841
sites), byte in 13 (77 sites), and date in 35 (204 sites). None of those documents
declares a direct string request body with these formats, and their fresh
individual golden measurements do not reach these handling sites.

The acquisition budget was three Sourcegraph field queries with `count:100`,
and at most two complete public candidate documents per format. Each query
returned two files and hit the server's 100-match limit. A match is not a file,
and a field result is not a declaration of the request shape. The retained
query progress records state the cap, fork and archive exclusions. This is a
bounded screen, not an exhausted search of public specifications.

Kuber.jl's indexed generated Kubernetes description was not admitted as a
publisher-owned document. The canonical Kubernetes apps/v1 description was
fetched from its publisher at an immutable revision instead. The other two
complete documents were the Beto catalogue description and OpenAI's Orchard
API. Orchard declares three byte schemas, all outside a direct string request
body. None of these complete documents declares any requested body shape, so
licence and certified Fern generation screens were not owed for them.

| key | verdict | remaining work |
|---|---|---|
| `format-uuid` | `search-incomplete` | The bounded screen admitted no witness; the public population remains unscreened. |
| `format-byte` | `search-incomplete` | The bounded screen admitted no witness; the public population remains unscreened. |
| `format-date` | `search-incomplete` | The bounded screen admitted no witness; the public population remains unscreened. |

Query responses, pinned acquisition records and guarded request ledgers are
retained under [`sourcegraph/`](sourcegraph/). [`queries.tsv`](queries.tsv)
checks their file counts. [`shape-screen.tsv`](shape-screen.tsv) records each
complete document's broad selector count and requested-shape count, with its
immutable source revision and SHA-256. Source bytes stayed in the acquisition
cache rather than being redistributed without an admission.

## Bounded-screen result

| key | result | fixture |
|---|---|---|
| `format-uuid` | `none-registrable` | `meadow-tag-code` |
| `format-byte` | `none-registrable` | `sonar-packet-envelope` |
| `format-date` | `none-registrable` | `skyglass-observation-date` |

Each independently authored fixture isolates its requested shape and carries
the complete certified Fern CLI 5.67.1 / SDK 5.20.0 output. The deterministic
handwritten-fixture gate compares every file against crozier.
