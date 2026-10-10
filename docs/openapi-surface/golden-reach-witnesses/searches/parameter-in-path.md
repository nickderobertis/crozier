# Arm search: `parameter-in-path`

New parameter-lowering sites not executed by the registered golden-only runs:

- `src/ir.rs::lifted_client_path_parameters[\.map\(\x7cparameter\x7c ClientPathParameter \{]`

The helper was renamed from `base_path_client_parameters` without changing this
handling; the recorded audit and incomplete verdict are unchanged.

No arm-specific live query or registry walk ran. Each declared source still
owes its search, so this bounded audit is `search-incomplete`, not exhaustion.
The registered corpus measurements find no source reaching these sites.
Hand-written arm covers certify generation without counting as real matches.

### Witness search (exhaustive)

| key | source | outcome | queries | walk | candidates | screens |
|---|---|---|---|---|---|---|
| `parameter-in-path` | `apis.guru` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |
| `parameter-in-path` | `jentic` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |
| `parameter-in-path` | `github-code-search` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |
| `parameter-in-path` | `github-publisher-trees` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |
| `parameter-in-path` | `sourcegraph` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |
| `parameter-in-path` | `vendor-portals` | `search-incomplete` | not searched | not walked | 0 | 0 screened; source search outstanding |

## Bounded renewal

| key | outcome | inspected evidence |
|---|---|---|
| `parameter-in-path` | `none-registrable` | Registered golden-only measurements execute none of the listed sites. This is arm-level evidence; the broader feature has real declarers. |

## Known arm candidates

The bounded registered-corpus audit uses
build `509917e7b94f` only.
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
