# JSON request shape search

## Witness search

Only corpus sources and committed remote-tree fragments are recorded here;
local test inputs are excluded from real-witness evidence.

At `27de039f4`, a renewed offline walk inspected the acquired source documents
and the previously enumerated committed remote-tree fragments. The shared census
loader parsed all 283 source records; each record's SHA-256 was computed from
its actual committed bytes. [sources.tsv](sources.tsv) records the results.

The exact conjunctions inspected were: a referenced allOf object with no own
properties and open additional properties; an inline body with own properties
and an object parent reference; a tagged inline binary JSON string; a nullable
object component referenced by a 3.0 body; an explicitly optional free-form
object body; JSON media with a direct example and no schema; a titled object
body and response sharing one reference without other inputs; and a media
example reference on an untitled body retained as the success response's parent.
No complete declarations were found. No real witness is claimed.

This walk follows local references with cycle protection. It does not resolve
cross-document references or exhaust public publishers. Component fragments
alone cannot declare an operation's complete trigger. The result is therefore
an incomplete search, renewed against the committed bytes, rather than a claim
of exhaustive absence. Publisher searches and cross-document expansion remain
incomplete. No network acquisition was performed.

| key | verdict | why |
|---|---|---|
| `request-body-content` | `search-incomplete` | No complete registered-source declaration for the new JSON request handling sites |
| `request-body-required` | `search-incomplete` | No exact explicitly optional free-form request declaration |
| `format-binary` | `search-incomplete` | No tagged inline binary JSON request declaration |

The handling sites are:

- `src/ir.rs::resolve_request_body[let Some\(schema\) = media\.schema\.as_ref\(\) else]`
- `src/ir.rs::resolve_request_body[\x7c\x7c is_map\(schema\)]`
- `src/ir.rs::resolve_request_body[if is_optional\(target\) \&\&]`
- `src/ir.rs::resolve_request_body[let own_count = fields\.len\(\)]`
- `src/ir.rs::inline_body_source_names[\&\& !is_optional\(target\)]`
- `src/ir.rs::scalar_body[Some\("binary"\)]`
- `src/emit.rs::build_example_inner[if s\.type_ref == TypeRef::Primitive\(Prim::Bytes\)]`

- `src/ir.rs::request_body_has_all_of[!schema\.properties\.is_empty\(\)]`

## Renewed search

| key | result | scope |
|---|---|---|
| `request-body-content` | `none-registrable` | Complete conjunctions over the committed source records above |
| `request-body-required` | `none-registrable` | Exact optional, non-nullable open map input |
| `format-binary` | `none-registrable` | Tagged inline binary JSON request, with and without path parameters |
