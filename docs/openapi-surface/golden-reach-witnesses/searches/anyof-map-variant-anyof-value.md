# Arm search: `anyof-map-variant-anyof-value`

Union-repair sites not executed by the registered golden-only runs:

- `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = union_value \{]`

No arm-specific live query or registry walk ran under this directory's
evidence. Each declared source still owes its search, so this record is
`search-incomplete`, not exhaustion. The bounded
[union witness search](../../witness-search-union-scenarios/README.md#witness-search)
read the APIs.guru archive and the already-acquired code-search pools for the
shape and found no registrable declarer reaching the site. The hand-written
arm cover certifies generation without counting as a real match.

### Witness search (exhaustive)

| key | source | outcome | queries | walk | candidates | screens |
|---|---|---|---|---|---|---|
| `anyof-map-variant-anyof-value` | `apis.guru` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |
| `anyof-map-variant-anyof-value` | `jentic` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |
| `anyof-map-variant-anyof-value` | `github-code-search` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |
| `anyof-map-variant-anyof-value` | `github-publisher-trees` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |
| `anyof-map-variant-anyof-value` | `sourcegraph` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |
| `anyof-map-variant-anyof-value` | `vendor-portals` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |

## Bounded renewal

| key | outcome | inspected evidence |
|---|---|---|
| `anyof-map-variant-anyof-value` | `none-registrable` | Registered golden-only measurements execute none of the listed sites, and the union witness search found no registrable declarer reaching them. |

## Known arm candidates

The bounded registered-corpus audit uses
build `475f17eabc10` only.
No arm-specific registry documents have been acquired or probed: the zeros
below count known candidates, while each source still owes its initial search.

| source | declarers | unreadable | census-refused | probed | unprobed | timed out | crozier failed | reach an arm | screened | outstanding |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `apis.guru` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `jentic` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `github-code-search` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `github-publisher-trees` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `sourcegraph` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `vendor-portals` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
