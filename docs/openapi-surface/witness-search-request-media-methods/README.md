# Named request media search

## Witness search

At `c2807ce53`, a renewed offline walk parsed all 314 acquired source records
and previously enumerated committed remote-tree fragments without errors.
[sources.tsv](sources.tsv) records hashes computed from the committed bytes.
The screen required an application/json request representation carrying a
method-name extension and an image/audio/video binary-string representation
carrying its own method-name extension, accepting both documented spellings.
No complete declaration or partial named-media candidate was found.

Local references were followed with cycle protection. Cross-document resolution
and publisher searches remain incomplete. Fragment-only documents cannot prove
an operation. No network acquisition was performed and no exhaustive public
absence is claimed.

| key | verdict | why |
|---|---|---|
| `request-body-content` | `search-incomplete` | No named JSON plus named binary request representation |

Handling sites:

- `src/ir.rs::request_media_variants[let mut view = op\.with_sdk_method_name]`
- `src/openapi.rs::Operation::with_sdk_method_name`

## Renewed search

| key | result | scope |
|---|---|---|
| `request-body-content` | `none-registrable` | Complete named-media conjunction over committed source records |
