# Object alias request search

## Witness search

Only corpus sources and committed remote-tree fragments are recorded here;
local test inputs are excluded from real-witness evidence.

At `c2807ce53`, a renewed offline walk parsed all 283 acquired source records
and previously enumerated committed remote-tree fragments without errors.
[sources.tsv](sources.tsv) records hashes computed from their committed bytes.
The screen required an application/json body reference to a component whose
only key is a reference and whose locally resolved terminal schema explicitly
declares type object. No complete declaration or partial candidate was found.

Local references were followed with cycle protection. Implicit objects through
allOf, cross-document resolution and publisher searches remain incomplete.
Fragment-only sources cannot establish an operation. No network acquisition
was performed and no exhaustive public absence is claimed.

| key | verdict | why |
|---|---|---|
| `request-body-content` | `search-incomplete` | No pure component alias reaching an explicitly declared object body |

Handling sites:

- `src/ir.rs::resolve_request_body[resolve_form_object_alias\(target]`
- `src/ir.rs::build_endpoint[=let aliased_inline_request =]`


- `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]`

## Renewed search

| key | result | scope |
|---|---|---|
| `request-body-content` | `none-registrable` | Explicit terminal-object alias conjunction over committed source records |
