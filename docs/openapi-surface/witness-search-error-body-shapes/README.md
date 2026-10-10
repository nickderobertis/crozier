# Error body shape search

## Witness search

Only corpus sources and committed remote-tree fragments are recorded here;
local test inputs are excluded from real-witness evidence.

At `7f7f31b79`, a renewed offline walk parsed 283 acquired source records,
including previously enumerated committed remote-tree fragments. Every record
in [sources.tsv](sources.tsv) carries the SHA-256 of its committed bytes; there
were no parse errors. It screened inline JSON error responses for a sole inline
object member containing both a string enum and a reference property, and for
a mapped discriminated union containing the status-named BadRequestError
component whose members compose a base reference and discriminant enums.
Neither screen found a declaration. The latter is a necessary but incomplete
screen of the whole trigger: it does not prove the additional non-union error
keeps the base discriminant. No partial candidate or complete real witness was
found in this bounded screen.

Local references were followed with cycle protection. Cross-document resolution
and publisher searches remain incomplete. Component fragments cannot establish
a complete operation. No network acquisition was performed, and this record
claims no exhaustive public absence.

| key | verdict | why |
|---|---|---|
| `oneof-sole-member` | `search-incomplete` | No inline error object with both required trigger properties |
| `oneof` | `search-incomplete` | No mapped status-named composed error union candidate |

Handling sites:

- `src/ir.rs::error_body_type[\x5bonly\x5d if only\.reference\.is_none]`
- `src/ir.rs::hoist_error_body_types[if let \x5bonly\x5d = members\.as_slice\(\)]`
- `src/ir.rs::hoist_error_body_types[if schema\.discriminator\.is_some\(\)]`

## Renewed search

| key | result | scope |
|---|---|---|
| `oneof-sole-member` | `none-registrable` | Inline error-member conjunction over committed source records |
| `oneof` | `none-registrable` | Necessary status-named union screen over committed source records |
