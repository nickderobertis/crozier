# Nonstandard integer-format witness search

## Witness search

The existing selector `schema.format=bigint` records a nonstandard format
value. The shape being proved is an integer response with that value, which
still generates an `int` return annotation.

| key | verdict | remaining work |
|---|---|---|
| `integer-format-fallback` | `search-incomplete` | The field search is answered, but its complete population has not been screened. No accepted document in this bounded screen proves the shape. |

On 2026-10-06 two Sourcegraph field queries returned 79 YAML and 144 JSON file
results. These are search results, not declarations. Their answered responses
and counts are retained in [`queries.tsv`](queries.tsv) and
[`sourcegraph/queries.jsonl`](sourcegraph/queries.jsonl).
Three complete official publisher documents were downloaded at immutable
revisions through the guarded acquirer and read by the census.

| publisher document | pinned revision | declarations | disposition |
|---|---|---:|---|
| formancehq/ledger, openapi.yaml | `d47ba1746cec2173d84eab8ec575be196eae0837` | 30 | The declarations include integer schemas. Licence and immutable-source screens passed, but the certified Fern check rejected the whole document for endpoint errors, including parameter-name collisions and HEAD request bodies. No golden was produced. |
| tonkeeper/opentonapi, api/openapi.yml | `6f98cb7693b8832d0e49798ff7ef1d3de7586bd8` | 0 | Does not declare the format value. |
| apache/fluss, fluss-gateway/openapi.yaml | `faf37fb6b1a0a1a02135bfc4062c6981c58e34ab` | 0 | Does not declare the format value. |

The retained candidate and screening records are under [`sourcegraph/`](sourcegraph/).
The declaring document's measured logs retain Fern CLI 5.67.1 / SDK 5.20.0;
the refusal is a measured upstream outcome, not a crozier mismatch.

## Bounded-screen result

| key | result | fixture |
|---|---|---|
| `integer-format-fallback` | `none-registrable` | `turbine-pulse-counter` |

The independently authored fixture declares one GET operation returning an
integer with the nonstandard format, without models, examples, parameters or
authentication. Its certified complete tree is compared in the deterministic
handwritten-fixture gate. The search remains incomplete rather than claiming
that no real publisher declares the shape.
