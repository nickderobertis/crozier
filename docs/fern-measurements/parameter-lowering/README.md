# How Fern lowers query and header parameters, measured

Each directory here is a document written for the purpose and the tree Fern
generated from it at Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, in
the workspace `tools/fern-goldens/generate-fern-fixture.sh` scaffolds (Route A of
[`../../fern-goldens.md`](../../fern-goldens.md)), comment-stripped by
`crozier internal-strip`. The trees are Fern's output as measured; nothing in
them was edited. `parameter_lowering_measurements_match_fern` in
[`../../../crates/crozier-e2e/tests/e2e.rs`](../../../crates/crozier-e2e/tests/e2e.rs) generates each document with
crozier and holds its whole tree to `fern-expected/` under the corpus gate's
normalization.

This is no corpus fixture and no coverage probe: it is never a `CORPUS.md` row
and settles no coverage row. The one real specification registered for these
rules is corpus row 317, `lootlog-battlelog`; why the others have none yet is
[below](#the-real-specification-search).

## The cases

| case | what it pins |
|---|---|
| [`query-union-placement`](query-union-placement/openapi.yml) | where the type hoisted for an inline `anyOf`/`oneOf` parameter is declared, in every cell where `title` and "every member is an enum" disagree with the rule below |
| [`query-array-union-items`](query-array-union-items/openapi.yml) | an array query parameter whose `items` is an inline union names its element `{Op}Request{Param}Item` |
| [`query-scalar-or-array`](query-scalar-or-array/openapi.yml) | when `oneOf`/`anyOf: [scalar, array of that scalar]` is the one-or-many shorthand and when it is a named union |
| [`query-union-enum-member`](query-union-enum-member/openapi.yml) | a union naming a component string enum, with no array member, reaches the URL raw |
| [`header-default-literal`](header-default-literal/openapi.yml) | a string header with a `default`, promoted from three of four operations, is a one-value `Literal` |
| [`header-default-constants`](header-default-constants/openapi.yml) | an unpromoted header whose schema defaults to a string — plain or an inline enum, required or not — is sent as that constant and leaves the method; an integer default keeps the argument. Fern's Markdown still passes and documents it, a defect the [`constant-header-docs-arguments`](../../departures/evidence/constant-header-docs-arguments.md) departure corrects |
| [`query-nullable-30`](query-nullable-30/openapi.yml), [`query-nullable-31`](query-nullable-31/openapi.yml) | a required query parameter whose schema admits `null` is an optional argument; array items that admit `null` lose their `Optional` in the signature and exampled `[]` in a docstring. Fern's `reference.md` and worked calls keep the items' nullability, a defect the [`nullable-items-docs`](../../departures/evidence/nullable-items-docs.md) departure corrects |
| [`header-defaults-managed`](header-defaults-managed/openapi.yml) | a header with a string default on every operation, required or not, is a trailing `Optional` client field falling back to the default, written after the credential; the apiKey scheme's own header is not promoted again; `Origin`, `Cookie` and `Content-Type` parameters are dropped while `Referer`, `Host` and `Accept-Encoding` stay arguments; an empty default keeps the argument |
| [`query-union-temporal-member`](query-union-temporal-member/openapi.yml) | a query union with a `date` or `date-time` member is converted on the way out, whatever its other members |
| [`single-operation-headers`](single-operation-headers/openapi.yml) | a document's only operation has its headers promoted to the client, required ones as required fields |
| [`base-path-string`](base-path-string/openapi.yml), [`base-path-object-literal`](base-path-object-literal/openapi.yml) | `x-fern-base-path: /v2`, and its object form `{path: /v2}`, prefix every route |
| [`base-path-templated-string`](base-path-templated-string/openapi.yml) | the string form naming a placeholder: [refused](base-path-templated-string/fern-refusal.txt) |
| [`base-path-lifted-default`](base-path-lifted-default/openapi.yml), [`base-path-lifted-unincluded`](base-path-lifted-unincluded/openapi.yml), [`base-path-lifted-required`](base-path-lifted-required/openapi.yml), [`base-path-lifted-list`](base-path-lifted-list/openapi.yml), [`base-path-lifted-bare`](base-path-lifted-bare/openapi.yml) | the object form's placeholder lifted to the client, with and without `paths-include-base-path` and a `default`, with `parameters` as a list and with none; their trees carry the Fern defects the [`lifted-base-path-docs-examples`](../../departures/evidence/lifted-base-path-docs-examples.md) and [`lifted-base-path-positional-example`](../../departures/evidence/lifted-base-path-positional-example.md) departures correct, and match through them |

## The rules

**Placement.** For a `oneOf`/`anyOf` query parameter with two or more non-null
members, Fern declares the hoisted type in the tag's own `types/` exactly when
the parameter is required and not nullable, or optional and nullable; otherwise
in the package root's. Nullable means a `type: null` member or a schema-level
`nullable: true`; a member's own nullability (`{type: [string, "null"]}`,
`{type: integer, nullable: true}`) does not count. `title`, `default`, `const`
or one-value `enum` members and `$ref` members do not move it. A header or path
composition, a sole non-null string enum and a composition with a sibling
string `enum` are always tag-local. Measured over 24 cells
(required × null member × scalar mix, one-value enums, `const`s × `title`),
then over `oneOf`, header, path, 3.0 `nullable`, `type` arrays and a `default`.

**Array items.** Every inline items union of two or more non-null members is
hoisted as `{Param}Item` in the tag, required or not, `oneOf` or `anyOf`, with
`$ref`, inline-enum, scalar and three-member unions alike; an inline enum member
is a `{Param}ItemZero` enum. The value is written raw, and a required one is
exampled by its element's first member.

**One or many.** `oneOf`/`anyOf: [scalar, array of that scalar]` is Fern's
optional `Union[T, Sequence[T]]` shorthand only where the parameter is required
exactly when it is nullable. A required, non-null one is a named union in the
tag, a required argument converted on the way out and exampled by its scalar
(`batch=1`); an optional nullable one is a named union too. Over an inline enum
it is always a union, its array member's element a `{Union}OneItem` enum.

**Write serialization.** A union whose members reach nothing but scalars — a
`$ref` to a component string enum among them — is passed raw; a member that is
an array, or a `date` or `date-time` string, is what makes Fern convert it. A required `[string, $ref Enum]` is
exampled by the enum's first value as a plain string.

**Credential headers.** Fern drops an operation's header parameter only when its
name is exactly the header a declared scheme writes: `Authorization` for bearer,
basic or OAuth2, an apiKey header scheme's own `name`. `authorization`,
`AUTHORIZATION` and `x-kite-key` beside `X-Kite-Key` stay method arguments. A
header argument never makes the README's abbreviated calls read `(...)`.

**Constant headers.** A header no promotion takes, whose schema's `default` is
a non-empty string — `type: string` or an inline string enum, nullable or not,
required or not — is sent as that constant in the order the operation declares its
headers, and the method does not take it. An integer default, or an empty
string, keeps the argument.

**Managed headers.** `User-Agent`, `Content-Type`, `Origin` and `Cookie`
header parameters, in any letter case, are dropped from the method and from
promotion; `Referer`, `Host` and `Accept-Encoding` are ordinary arguments.

**Nullable query parameters.** A required query parameter whose own schema
admits `null` (`nullable: true`, a `type` list naming `null`, a `null`
alternative) is `Optional[T] = None`, yet its worked example still passes it. A
one-or-many array whose items admit `null` is `Optional[Union[T, Sequence[T]]]`
and a docstring passes `[]` for it.

**Promotion.** A header on every operation is promoted to the client with its
declared optionality — on a single-operation document too. One with a string
`default` on every operation is optional whatever it declares: a trailing
field after `logging`, falling back to the default, written after the
credential. A header an apiKey scheme already writes is never promoted again.

**Defaulted headers.** A header promoted from at least three quarters but not
all of the operations, whose first declaration is a string with a string
`default`, is `Optional[typing.Literal["<default>"]] = None`, required or not
and enum or not. An integer or boolean default, or a default only a later
declaration carries, keeps the plain type.

**Base path.** The string form prefixes every route. The object form's `path`
does the same unless `paths-include-base-path: true`; each `{placeholder}` in
it is lifted out of every method into a client constructor argument the routes
read from the client wrapper, ahead of promoted headers and the credential. A
map-form `parameters` entry with a string `default` makes it
`Optional[str] = "<default>"` on the client; otherwise it is a required `str`.
A lifted operation's JSON body loses its `content-type` header, as an operation
with no parameters does. The string form naming a placeholder is refused, with
or without the routes including it:

| spelling | Fern | case |
|---|---|---|
| `x-fern-base-path: /v2` | generates; routes `v2/…` | `base-path-string` |
| `{path: /v2}` | generates; the same tree | `base-path-object-literal` |
| `{path: /{edition}, paths-include-base-path: true, parameters: {edition: {type: string, default: v2}}}` | generates; `edition: Optional[str] = "v2"` | `base-path-lifted-default` |
| the same without `paths-include-base-path`, routes not prefixed | generates; the same client | `base-path-lifted-unincluded` |
| `parameters` a list of Parameter Objects with a `default` | generates; `edition: str`, the default not read | `base-path-lifted-list` |
| no `parameters`, or a map entry without `default` | generates; `edition: str` | `base-path-lifted-bare`, `base-path-lifted-required` |
| `x-fern-base-path: /{edition}` | refuses: `File has missing path-parameter: edition` | `base-path-templated-string` |

crozier reads `x-crozier-base-path` the same way, and it wins when both appear.
Where Fern refuses the templated string form, crozier lifts its placeholder as a
required argument.

## The real-specification search

Each shape was searched for among the documents already acquired for the
coverage searches — 9,638 readable documents across the GitHub code search and
Sourcegraph pools, the earlier witness-search cache and the refusal registry's
population — and every declarer was screened on licence, immutable revision and
pinned Fern, then compared with crozier on the finished tree. Live queries were
not re-issued, so none of these is an exhaustive search. The three shapes still
carried by hand-written fixtures, with every declarer and its screens, are
recorded in
[`../../openapi-surface/witness-search-parameter-lowering/`](../../openapi-surface/witness-search-parameter-lowering/README.md).

| shape | what was found |
|---|---|
| lower-case `authorization` beside a bearer scheme | `lootlog/monorepo` `apps/battlelog/openapi.yaml` at `e2796c4f48ca4a749f53fdc5a127eece50567b56`, MIT: Fern generates, crozier byte-matches — corpus row 317 |
| a query union naming a component string enum, no array member | `dreek1337/Ego` `openapi.yaml` at `e0ebe7a5219488545820408b46f67f4f9fa9c83c`, MIT: Fern generates, crozier byte-matches — corpus row 318 |
| array query items union, subset-promoted defaulted header, `x-fern-base-path` | no registrable declarer; see the record above |
| inline query composition placement | `Stichting-KOMPAZ-1/KOMPAZ-web-frontend` `openapi.json` at `a847053e46b98324c57183af2b2c09abe01f8ecf` (MIT), `langchain-ai/docs` `src/langsmith/agent-server-openapi.json` at `264fdf88d3fc53d5d2397fadf3b6dba36b95dd0e` (MIT), `lenML/Speech-AI-Forge` `docs/openapi.json` at `a41b70abba866ecded6e1e90beea6cc68e3fd0ae` (AGPL-3.0), `waylayio/waylay-sdk-queries-py` `openapi/queries.openapi.yaml` at `8ab6c18e10f96c3665dbb849ebe2193c16a1659c` (ISC) and `Q2TM/low-temperature-control` `apps/rice-shower/docs/openapi.yaml` at `b100b3633a68a41ba63181379455e98b4814da19` (MIT) declare these cells and Fern generates each; each still differs from crozier outside parameter lowering — method names a tag's own prefix shortens (KOMPAZ), nested model-union aliases and descriptions (langchain, rice-shower), multipart file parts, a JSON-encoded form field and untagged sub-clients (Speech-AI-Forge), and body fields that repeat query parameters (waylay) |
| required scalar-or-array composition | `supabase/supabase` `apps/docs/spec/api_v1_openapi.json` at `36371de15127206280d2d40786e8578dfe1b681a` (Apache-2.0) declares the `anyOf` spelling and Fern generates; it still differs on path-parameter example values, body fields renamed after a query collision, and where a body enum is declared |

Each document that generates but differs becomes a candidate witness once the
shape it differs on matches.
