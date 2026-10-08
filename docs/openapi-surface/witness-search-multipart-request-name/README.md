# Multipart component request name search

## Witness search

At `c2807ce53`, a renewed offline walk parsed all 283 acquired corpus source
records and committed remote-tree fragments without errors.
[sources.tsv](sources.tsv) records hashes of their committed bytes. Local test
inputs are excluded from real-witness evidence. The screen required a multipart
inline object whose property references a component named exactly the operation's
PascalCase identifier plus Request. No complete or partial candidate was found.

The bounded screen follows local references and uses operation identifiers;
method-name extensions, cross-document references and further publisher searches
remain incomplete. Fragment-only sources cannot establish an operation. No network
acquisition was performed and no exhaustive public absence is claimed.

| key | verdict | why |
|---|---|---|
| `request-body-content` | `search-incomplete` | No multipart field referencing the operation-derived request component |

Handling site:

- `src/name_refusals.rs::validate_ir[=body\.content\.len\(\) == 1]`

## Renewed search

| key | result | scope |
|---|---|---|
| `request-body-content` | `none-registrable` | Multipart operation-derived component reference over committed corpus sources |
