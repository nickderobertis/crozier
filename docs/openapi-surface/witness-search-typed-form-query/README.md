# Typed form-query witness search

## Witness search

The missing handling site is
`src/emit.rs::append_request_call_args[\} else if qp\.convert \{]`.
The shape is an object-typed query parameter with explicit `style: form` and
named schema properties, which needs alias-aware conversion.

The 241 registered documents contain two explicit form object query parameters
in HubSpot Events, `objectProperty.{propname}` and `property.{propname}`, on
`GET /events/v3/events/`. Their schemas are bare `{type: object}`. The certified
SDK types them as `Optional[Dict[str, Any]]` and passes each unchanged; there are
no named properties requiring conversion, so their golden does not reach this
handling site. Object presence alone does not prove the typed arm.

The acquisition budget was one Sourcegraph field query with `count:100` and
at most two complete candidate documents. The query looked for the fields
needed by a form object query and returned two files at the server's 100-match
cap. Both complete pinned documents were read, with parameter references and
schema references resolved locally for the typed-shape check. JeffreysPrompts
declares no explicit form parameter. The Paykit SDK's distributed Bachs
description declares one form parameter, but no typed form object query. Its
SDK distribution is not a publisher-provenance grant. Neither document reaches
the requested shape, so licence and certified Fern generation screens were not
owed. The query's cap and unscreened public population remain outstanding.

| key | verdict | remaining work |
|---|---|---|
| `parameter-style-form-query-object` | `search-incomplete` | The bounded screen admitted no witness; the public population remains unscreened. |

Query responses, pinned acquisition records and guarded request ledgers are
retained under [`sourcegraph/`](sourcegraph/). [`queries.tsv`](queries.tsv)
checks their file counts. [`shape-screen.tsv`](shape-screen.tsv) records each
complete document's broad selector count and requested-shape count, with its
immutable source revision and SHA-256. Source bytes stayed in the acquisition
cache rather than being redistributed without an admission.

## Bounded-screen result

| key | result | fixture |
|---|---|---|
| `parameter-style-form-query-object` | `none-registrable` | `ore-bin-screen` |

Each independently authored fixture isolates its requested shape and carries
the complete certified Fern CLI 5.67.1 / SDK 5.20.0 output. The deterministic
handwritten-fixture gate compares every file against crozier.
