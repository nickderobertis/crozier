# How Fern lowers query and header parameters, measured

Each directory here is a document written for the purpose and the tree Fern
generated from it at Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, in
the workspace `scripts/generate-fern-fixture.sh` scaffolds (Route A of
[`../../fern-goldens.md`](../../fern-goldens.md)), comment-stripped by
`crozier internal-strip`. The trees are Fern's output as measured; nothing in
them was edited. `parameter_lowering_measurements_match_fern` in
[`../../../tests/e2e.rs`](../../../tests/e2e.rs) generates each document with
crozier and holds its whole tree to `fern-expected/` under the corpus gate's
normalization.

This is no corpus fixture and no coverage probe: it is never a `CORPUS.md` row
and settles no coverage row. The one real specification registered for these
rules is corpus row 313, `lootlog-battlelog`; why the others have none yet is
[below](#the-real-specification-search).

## The cases

| case | what it pins |
|---|---|
| [`query-union-placement`](query-union-placement/openapi.yml) | where the type hoisted for an inline `anyOf`/`oneOf` parameter is declared, in every cell where `title` and "every member is an enum" disagree with the rule below |
| [`query-array-union-items`](query-array-union-items/openapi.yml) | an array query parameter whose `items` is an inline union names its element `{Op}Request{Param}Item` |
| [`query-scalar-or-array`](query-scalar-or-array/openapi.yml) | when `oneOf`/`anyOf: [scalar, array of that scalar]` is the one-or-many shorthand and when it is a named union |
| [`query-union-enum-member`](query-union-enum-member/openapi.yml) | a union naming a component string enum, with no array member, reaches the URL raw |
| [`header-default-literal`](header-default-literal/openapi.yml) | a string header with a `default`, promoted from three of four operations, is a one-value `Literal` |
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
an array is what makes Fern convert it. A required `[string, $ref Enum]` is
exampled by the enum's first value as a plain string.

**Credential headers.** Fern drops an operation's header parameter only when its
name is exactly the header a declared scheme writes: `Authorization` for bearer,
basic or OAuth2, an apiKey header scheme's own `name`. `authorization`,
`AUTHORIZATION` and `x-kite-key` beside `X-Kite-Key` stay method arguments. A
header argument never makes the README's abbreviated calls read `(...)`.

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

The census selectors below were run over every document already acquired for
the coverage searches (9,638 readable documents across the GitHub code search,
Sourcegraph, publisher-tree, APIs.guru and jentic pools, plus the refusal
registry's population), and each document the census confirmed was screened on
licence, immutable revision and Fern. Live queries were not re-issued, so none
of these is an exhaustive search.

| shape | census selector | what was found |
|---|---|---|
| lower-case `authorization` beside a bearer scheme | header parameter named `authorization` | `lootlog/monorepo` `apps/battlelog/openapi.yaml` at `e2796c4f48ca4a749f53fdc5a127eece50567b56`, MIT: Fern generates, crozier byte-matches — registered as corpus row 313 |
| optional, nullable query composition | `parameter.in=query&!parameter.required&parameter.schema>schema.anyOf>schema.type=null` | four documents; `Stichting-KOMPAZ-1/KOMPAZ-web-frontend` (MIT) generates but differs on method naming; the others grant no licence. Beyond the selector, `langchain-ai/docs`' agent server (MIT), `lenML/Speech-AI-Forge` (AGPL-3.0), `waylayio/waylay-sdk-queries-py` (ISC) and `Q2TM/low-temperature-control` (MIT) declare these placement cells, generate, and differ on model-union variants, descriptions and body headers |
| array query items union | `parameter.in=query&parameter.schema>schema.items>schema.anyOf` | thirteen documents; `konfig-dev/konfig`'s `rated` (MIT) generates and differs on literal header naming, and a `swagger-api/swagger-parser` test resource (Apache-2.0) generates over references that resolve to nothing; the others are refused by Fern or grant no licence |
| required scalar-or-array composition | `parameter.in=query&parameter.required&parameter.schema>schema.oneOf>schema.items>schema.type=integer` | three documents, each refused by Fern; `supabase/supabase`'s `api_v1_openapi.json` (Apache-2.0) declares the `anyOf` spelling, generates, and differs on example values and body-field naming |
| path union naming a component enum | `parameter.in=path&parameter.schema>schema.anyOf>schema.$ref` | twelve documents; one MISP copy (AGPL-3.0) generates and crozier refuses an unresolved reference in it; Fern refuses the others or, for the DigitalOcean copies, writes an empty SDK over a document it never parsed |
| `x-fern-base-path` | `openapi.x-fern-base-path` | one document, OpenRouter's (via jentic), refused by Fern (`type-name-collision`) |

The documents that generate but differ do so on shapes outside parameter
lowering; each becomes a candidate witness once those close.
