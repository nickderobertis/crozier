# Plain string-map request witness search

## Witness search

This search uses `operation.requestBody:plain-string-map`. The lowering being
proved is a `typing.Dict[str, str]` request sent with `json=request`.

| key | verdict | remaining work |
|---|---|---|
| `request-body-string-map` | `registered` | Confluent Kafka Connect is corpus row 331, generated afresh at the certified pair and byte-matched across its whole tree. |

On 2026-10-06 two Sourcegraph field queries returned 6,263 YAML and 15,540 JSON
file results. These are search results, not declarations: their counts and
answered responses are retained in [`queries.tsv`](queries.tsv) and
[`sourcegraph/queries.jsonl`](sourcegraph/queries.jsonl). Four complete official
publisher documents were downloaded at immutable revisions through the guarded
publisher-tree acquirer and read by the census. Their recorded counts and
screens are under [`github-publisher-trees/`](github-publisher-trees/).

| publisher document | pinned revision | declarations | disposition |
|---|---|---:|---|
| confluentinc/ccloud-sdk-go-v2, connect/v1/api/openapi.yaml | `8bbb22a67562e5784e8d3a4efa78c5c20b52d6f2` | 1 | Registered as `confluent-kafka-connect`, corpus row 331. Fresh Route A generation at CLI 5.67.1 / SDK 5.20.0 produced 117 files. Crozier preserves the publisher's configuration example in reference.md and both method docstrings and byte-matches the whole golden tree. |
| confluentinc/kafka-rest, api/v3/openapi.yaml | `0d30749e53e54ec0ad52f0532c9fad43de6b95c6` | 0 | Does not declare the shape. |
| confluentinc/schema-registry, core/generated/swagger-ui/schema-registry-api-spec.yaml | `4262e9db6f88502a3cb4b651bef3559ed64740ad` | 1 | Licence, immutable reference and Fern check passed. Certified generation chooses a binary request from the operation's media alternatives, so it does not prove string-map JSON lowering; whole-tree comparison also differs in README method selection. |
| nacos-group/nacos-group.github.io, public/swagger/admin/en/api.json | `428cc2cbcceedeea8c01e44a3c83264640dba6d6` | 0 | Does not declare the shape. |

## Registered witness

| key | result | fixture |
|---|---|---|
| `request-body-string-map` | `registered` | `confluent-kafka-connect` (corpus row 331) |

The registered publisher document supersedes the independently authored
`signal-cabinet-labels` fixture. Both execute the plain-map lowering site; the
registered golden also proves the declared configuration example. The broader
field-search population remains only partially screened; registration settles
this shape without claiming that population was exhausted.
