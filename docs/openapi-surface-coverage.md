# OpenAPI surface coverage

Which OpenAPI features the registered golden corpus has **never seen** and
[`fern-limitations.md`](fern-limitations.md) has **never ruled on**. Each one is
generator behaviour only crozier vouches for: no golden pins it, no measurement of
Fern contradicts it, and `just check` stays green whatever crozier does with it.
This file is the index; the classified entries live in the six region files
below, and the two backlogs they add up to are
[at the bottom](#ranked-gap-backlog).

**What this is.** A structural census of the OpenAPI 3.0/3.1 object model against
the registered sources, feature by feature, with each feature landed in exactly
one of three categories and each uncovered one carrying what it would take to
settle it.

**What this is not.** It is not a claim about what Fern does — that is
[`fern-limitations.md`](fern-limitations.md), measured against a real Fern run —
and it is not a claim that crozier is *wrong* anywhere. A `gap` row says the
question is unanswered by anything in this repository, not that the answer is bad.
It is also not a fixture backlog on its own: what a `gap` row becomes is decided
by its `settlement` cell, and the corpus registration rules in
[`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md) still govern.

**What it says today.** The walk enumerates 482 features. 372 are `golden`: a
registered source declares the feature and its committed Fern golden
byte-matches, so crozier-versus-Fern parity is *measured* there. 70 are
`limitations`: Fern's behaviour is measured on a locally authored probe and
recorded in [`fern-limitations.md`](fern-limitations.md), which is a verdict
about Fern and not a byte comparison against crozier. 40 are `gap`: 20 of them
`UNREACHABLE` — the shape has no position in a generated Python SDK at all — and
20 `FIXTURE`, every one a branch of `src/ir.rs` that a real document can select
and that no committed golden reaches. So *does crozier byte-match Fern on
every OpenAPI feature and scenario?* **No.** The honest answer is that byte-match
evidence covers 372 of the 482 features this walk can see, that 70 more carry a
Fern verdict and no byte comparison at all, that 40 have neither, and that the
walk cannot see everything — where the remaining distance lies is
[stated in full below](#golden-classified-is-not-golden-exhausted) rather than
left for a reader to infer from a backlog's size.

## The region files

Every object the specification defines belongs to exactly one region, and no
feature appears in two region files.

| region | file | owns |
|---|---|---|
| `parameters` | [`openapi-surface/parameters.md`](openapi-surface/parameters.md) | Parameter, Header and Example objects, and `components.parameters`, `components.headers`, `components.examples` |
| `schemas` | [`openapi-surface/schemas.md`](openapi-surface/schemas.md) | Schema, Discriminator and XML objects, and every JSON Schema keyword wherever it appears, including the ones 3.1 added |
| `bodies-media` | [`openapi-surface/bodies-media.md`](openapi-surface/bodies-media.md) | Request Body, Media Type, Encoding, Responses, Response, Callback and Link objects, and `components.requestBodies`, `components.responses`, `components.callbacks`, `components.links`. The `headers` field of a Response and of an Encoding is this region's, while the Header Object it holds is the `parameters` region's |
| `security` | [`openapi-surface/security.md`](openapi-surface/security.md) | Security Scheme, OAuth Flows, OAuth Flow and Security Requirement objects, and `components.securitySchemes` |
| `document-paths` | [`openapi-surface/document-paths.md`](openapi-surface/document-paths.md) | OpenAPI, Info, Contact, License, Server, Server Variable, Components, Paths, Path Item, Operation, External Documentation, Tag and Reference objects |
| `oas31-extensions` | [`openapi-surface/oas31-extensions.md`](openapi-surface/oas31-extensions.md) | The document-level 3.0-to-3.1 delta and every `x-` prefixed extension |

Where an object is *used* from another region, the using region owns the **field**
and the defining region owns the **object** — as the `bodies-media` row spells out
for the `headers` field a Response and an Encoding carry.

Every region file carries the same skeleton, in this order: a `# ...` title and
one line saying which region it holds, `## Scope` (its row of the table above,
verbatim), `## Entries` (the table below, and nothing else), and `## Method notes`
(what the region measured, which census invocations it ran, and anything it could
not settle).

## The instrument

`just surface-census` is the measurement every `golden` and every `gap` row cites.
It walks the OpenAPI **object model** of each registered source — never a text
match, and never a generated `expected/` tree — and prints one row per
`(selector, fixture, count)`.

```
just surface-census                                # every registered source (fetches first)
just surface-census --selector pathItem.trace      # one feature: who declares it, how often
just surface-census --fixture apideck.com-crm --json
```

The registered sources are both halves of the corpus: the 32 vendored
`tests/fixtures/<name>/openapi.*` documents, and the 137 `link-ok` documents
`scripts/fetch-corpus.sh` fetches into `.local/corpus/<name>/` from
[`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md). An unfetched source
is a hard failure rather than a silent zero, because a source that reports nothing
and a source that declares nothing are the two answers this document must never
confuse. `just test-surface-census` drives the same script offline over the
vendored half and is part of `just check`, so the gate keeps the instrument honest
without needing the network.

### The selector grammar

A **selector** is the dotted path of object-model node kinds down to one declared
field, in the specification's own spelling. The head of a selector is the
lower-camel name of the OpenAPI object that declares the field:

```
parameter.allowEmptyValue     schema.patternProperties      response.links
mediaType.encoding.headers    info.license.identifier       components.pathItems
```

Two closed lists decide the head, and nothing else does:

- **Anchor kinds head their own selector.** `openapi` (the document root),
  `info`, `server`, `components`, `pathItem`, `operation`, `externalDocs`,
  `parameter`, `header`, `requestBody`, `mediaType`, `response`, `callback`,
  `example`, `link`, `tag`, `schema`, `securityScheme`, `securityRequirement`,
  `reference`.
- **Extending kinds append to their parent's selector under the field that holds
  them.** `contact`, `license`, `serverVariable`, `paths`, `responses`,
  `encoding`, `discriminator`, `xml`, `oauthFlows`, `oauthFlow`. So a License
  Object's `identifier` is `info.license.identifier`, an Encoding Object's
  `headers` is `mediaType.encoding.headers`, and a Responses Object's `default`
  is `operation.responses.default`.

A field whose value is drawn from a closed set also emits a **valued selector**,
`<selector>=<value>`: `parameter.in=cookie`, `parameter.style=deepObject`,
`securityScheme.type=mutualTLS`, `schema.format=uuid`. The fields that do this are
themselves a closed list: `openapi.openapi` (major.minor only), `parameter.in`,
`parameter.style`, `header.style`, `mediaType.encoding.style`, `schema.type`,
`schema.format`, `securityScheme.type`, `securityScheme.in`,
`securityScheme.scheme`, `schema.additionalProperties`.

A **boolean** value emits no valued selector, because a boolean field is written
for its presence and a valued spelling of it would be a second name for the field
selector the grammar already has. `schema.additionalProperties` is the one
exception, and is in the list above for that reason alone: it is the field that is
*a schema or a boolean*, and which boolean it carries is a different shape rather
than the same shape written twice — `additionalProperties: false` closes an object
and `src/ir.rs`'s `is_inline_struct` hoists a model for it, while
`additionalProperties: true` opens a map and `is_map` renders it as a dictionary.
A `schema.additionalProperties` whose value is a schema emits no valued selector
at all, exactly as an open set would not.

A **count** is the number of declaration sites in that document — one per place
the field is written, so a schema keyword used in forty schemas counts forty. Map
keys that are *names* rather than fields (a path template, a status code, a
property name, a component name, a security scheme name, a callback expression)
are never selectors; that is the whole difference between this census and a naive
one, and it is why a schema property called `trace` cannot score a `pathItem.trace`
and a property called `name` cannot score a `parameter.name`.

A shape the two kinds above cannot express emits a **predicate selector**,
`<selector>:<predicate>` — the notation
[`security.md`](openapi-surface/security.md)'s method notes already use for a
shape the field selector cannot read (`securityScheme:$ref`). A field selector says a
field was written and a valued selector says which member of a closed set it was
written with; neither can say anything about a field's *array members*, about two
declarations' values *compared*, or about the map keys the count rule above
deliberately excludes as names. The predicates are themselves a closed list of
29, declared in `scripts/openapi-surface-census.py` and restated here, with a
drift gate over the pair:

- `operation.tags:multiple` — one per Operation Object whose `tags` array
  holds more than one member.
- `operation.operationId:duplicate` — one per Operation Object whose
  `operationId` value is declared by more than one Operation Object of the
  same document, so a value written twice counts two.
- `openapi.paths:normalized-collision` — one per Paths Object key that
  collides with at least one other key of the same document after path-
  template-name normalization, so a two-key collision counts two. The
  normalization is crozier's own — `naming::field_name` of `src/naming.rs`,
  the transform that gives a path parameter its Python name and so decides
  which routes `src/emit.rs` renders as one URL — applied to each
  `{expression}` and to nothing else, so `/users/{userId}` and
  `/users/{user_id}` collide while `/{id}/users` and `/users/{id}` do not.
- `openapi.paths:templated-key` — one per Paths Object key carrying at least
  one `{expression}` template expression, so a key with two counts one.
- `openapi.paths:several-template-expressions` — one per Paths Object key
  carrying more than one `{expression}` template expression, so a key with one
  counts none and a key with three counts one. The two are separate readings
  of the same key rather than one selector and a refinement of it: a key with
  exactly one expression is what tells them apart.
- `components.schemas:normalized-collision` — one per `components.schemas` key
  that collides with at least one other key of the same document after class-
  name normalization, so a two-key collision counts two. The normalization is
  again crozier's own — `naming::class_name` of `src/naming.rs`, the transform
  `src/ir.rs`'s `ref_to_class` gives a named schema and so the one that
  decides which components generate as one class — so `OBRate1_0` and
  `OB_Rate1_0` collide while `OBRate1` and `OBRate1_0` do not.
- `openapi.paths:leading-literal-segment` — one per Paths Object key whose
  first non-empty `/`-separated segment is not wholly a `{expression}`
  template expression, which is the segment `src/ir.rs`'s `path_group`
  returns.
- `openapi.paths:template-before-literal-segment` — one per Paths Object key
  whose first non-empty segment is wholly a template expression and which
  carries a later segment that is not, so `path_group` skips one to return the
  other.
- `openapi.paths:all-segments-templated` — one per Paths Object key with no
  non-empty segment that is not wholly a template expression, so a key whose
  every segment is templated counts one and so does a key carrying no segment
  at all. The three above are one reading of a key between them, and the
  reading `path_group` makes: every key takes exactly one of them.
- `schema.type:primary=array` — one per Schema Object whose `type` names
  `array` first among its non-`null` members, which is the member
  `TypeField::primary` of `src/openapi.rs` reads, so a 3.1 `type: [string,
  array]` counts none and `type: [null, array]` counts one. A schema declaring
  `array` anywhere among its types is what `schema.type=array` counts, and the
  two disagree on exactly the key case 3.1 added.
- `schema.properties:non-empty` — one per Schema Object whose `properties` map
  holds at least one entry, so a declared-but-empty `properties: {}` counts
  none.
- `schema.oneOf:sole-member` — one per Schema Object whose `oneOf` array holds
  exactly one member.
- `schema.anyOf:sole-member` — one per Schema Object whose `anyOf` array holds
  exactly one member.
- `schema.oneOf:sole-non-null-member` — one per Schema Object whose `oneOf`
  array holds exactly one member whose primary type is not `null`, beside at
  least one member whose primary type is `null`.
- `schema.anyOf:sole-non-null-member` — one per Schema Object whose `anyOf`
  array holds exactly one member whose primary type is not `null`, beside at
  least one member whose primary type is `null`.
- `schema.enum:string-valued` — one per Schema Object whose `enum` array
  yields at least one string value under crozier's own `string_enum_values` —
  the schema is `type: string`, or declares no `type` and every member is a
  string.
- `schema.const:string-valued` — one per Schema Object whose `const` value
  yields a string under that same reading, which is the spelling
  `string_enum_values` falls back to when no `enum` is written. The two are
  two readings rather than one, because a schema writing both is read by its
  `enum` alone.
- `schema.$ref:cross-document` — one per Schema Object whose `$ref` names
  another document: the value carries a non-empty part before its `#`, or no
  `#` at all, so `./other.yaml#/components/schemas/Author` and a bare
  `common.yaml` count.
- `schema.$ref:same-document-foreign-pointer` — one per Schema Object whose
  `$ref` points inside its own document but outside `components.schemas`, so
  `#/definitions/Foo` from a Swagger conversion and
  `#/components/parameters/Page` count. The two above are the two shapes that
  reach `ref_to_class`'s first case, which names a reference off its last
  segment, and they are two selectors rather than one because only the first
  names a document other than the one being censused: crozier answers it by
  fetching that document, where a same-document pointer is answered — or not —
  inside the bytes already read. Both are declared by registered sources that
  carry committed goldens.
- `schema.$ref:nested-properties` — one per Schema Object whose `$ref` is a
  `#/components/schemas/` pointer carrying a `properties` segment with a
  segment after it, at a position the `ref_to_class` walk reads, so a pointer
  carrying two counts one.
- `schema.$ref:nested-items` — one per Schema Object whose `$ref` is such a
  pointer carrying an `items` segment at a position that same walk reads.
- `schema.$ref:composition-index` — one per Schema Object whose `$ref` is such
  a pointer carrying an `allOf`, `oneOf` or `anyOf` segment at a position that
  same walk reads, the segment whose index contributes no name.
- `schema.$ref:unnamed-segment` — one per Schema Object whose `$ref` is such a
  pointer carrying, at a position that same walk reads, a segment naming none
  of those five — a trailing `properties` included, since with no segment after
  it there is no property name to append. The four above are read off the four
  arms of `ref_to_class`'s own loop, whose read positions are
  `resolve_schema_pointer`'s too.
- `schema.$ref:undeclared-component-head` — one per Schema Object whose `$ref`
  is such a pointer whose head segment names no key of the same document's own
  `components.schemas`, which is what `resolve_schema_pointer`'s
  `schemas.get(parts.next()?)?` returns `None` on.
- `schema.$ref:resolves-to-component` — one per Schema Object whose `$ref`
  resolves under `resolve_ref_from_schemas` of `src/ir.rs`: its **last**
  `/`-separated segment names a key of the same document's own
  `components.schemas`. That is the *other* of the two resolutions
  [the `~>` operator's own paragraph](#the-selector-grammar) distinguishes, and
  the one `~>` performs, so this predicate says a reference resolves where `~>`
  says what it resolves to. It requires no prefix and traverses nothing, so
  `#/definitions/Author` resolves whenever the document declares a component
  named `Author`, and `#/components/schemas/Order/properties/lines` resolves to
  the component named `lines` or to nothing at all. It is neither the negation
  of the entry above nor a second spelling of it: that one reads the *head* of a
  `#/components/schemas/` pointer, and the two disagree on every pointer
  carrying a segment after its head. An arm needing only that a reference
  resolve reads this; an arm going on to read the target's own fields descends
  through `~>`.
- `schema.oneOf:discriminated-union` — one per Schema Object whose `oneOf` is a
  union `discriminated_union` of `src/ir.rs` builds. It is the *reading* of that
  function rather than the shape that resembles it. The written spelling needs a
  `discriminator` whose `propertyName` is non-empty; the inferred spelling needs
  no `discriminator` at all, and finds a property of the first member that every
  member tags itself with, distinctly. Where no non-empty `mapping` is written,
  every member must carry a `discriminant_value` for that property — a one-member
  string `enum`, the `const` that stands in for one, or a string `example` — read
  off the member **resolved**, so a `$ref` member naming no component of this
  document refuses the whole union; where a `mapping` is written, every mapping
  target must resolve instead and no member is read at all. A `discriminator`
  beside a `oneOf` is therefore neither necessary nor sufficient.
- `schema.anyOf:discriminated-union` — one per Schema Object whose `anyOf`,
  written where no `oneOf` is, is such a union. Only the *inferred* spelling
  reaches it: `discriminated_union` refuses a written `discriminator` beside an
  `anyOf` with no `oneOf` outright, because Fern applies an explicit
  discriminator to `oneOf` alone and reads an `anyOf` as an ordinary union
  whatever sibling block a generator emitted beside it. `oneOf` is the head
  wherever both are written, exactly as the `or` in `src/ir.rs` has it, so this
  and the entry above never count one node twice.
- `schema.discriminator:inheritance-union` — one per Schema Object that is the
  base of an inheritance-style discriminated union, OpenAPI's other polymorphism
  spelling: a `discriminator` with a non-empty `propertyName` and a non-empty
  `mapping` every entry of which resolves, on a schema declaring no `oneOf` and
  no `anyOf` of its own. It is the arm `discriminated_union` delegates to before
  it looks at a union head at all. The three above are one reading of
  `discriminated_union` between them, and they are three selectors rather than
  one because the three heads are three cases under
  [the enumeration rule](#the-selector-grammar).
- `schema.allOf:annotated-ref` — one per Schema Object whose `allOf` is the
  annotated-`$ref` shape `described_all_of_ref` of `src/ir.rs` reads: an array
  of at least two members, exactly one of them a Reference Object, and every
  other declaring nothing that determines a type. A member declares nothing
  when it writes none of the ten fields `is_unknown` reads — `$ref`, a `type`
  with a non-`null` member, `oneOf`, `anyOf`, `allOf`, `enum`, `const`, a
  non-empty `properties`, `additionalProperties` or `items` — so a member
  carrying only a `description`, a `title`, a `format`, an `example` or nothing
  at all is one, while `{type: string}` and `{properties: {a: {}}}` are not. It
  is the 3.0 idiom for attaching documentation to a shared schema, and it is one
  predicate rather than a conjunction because none of the three things it asks —
  a member count, that exactly one member is a reference, and what the others
  declare — is a field's presence.

**Twenty-one of the 29 are node-local**, which is what makes them one family:
each is decided from one object-model node's own declared fields and their
values, with no `$ref` resolution and no document-scope comparison. The six
`schema.$ref:` spellings that read a pointer's segment structure are node-local
in exactly that sense — a `$ref` *value* is one of the node's own declared
fields, and reading its segments is not resolving it, and so is
`schema.allOf:annotated-ref`, which reads one node's `allOf` members and no
further. The other
eight — `operation.operationId:duplicate`,
`openapi.paths:normalized-collision`, `components.schemas:normalized-collision`,
`schema.$ref:undeclared-component-head`,
`schema.$ref:resolves-to-component`, `schema.oneOf:discriminated-union`,
`schema.anyOf:discriminated-union` and
`schema.discriminator:inheritance-union` — compare one document's
own values against each other, and say so in their own sentence. Those two
numbers partition the closed list, and a check reconciles the split with it. The last five of
them read **the document context**: the census carries the document's own
`components.schemas` map and the set of its keys, reachable from every node it
walks, and it is the document being censused and nothing else — no fetch, no
cross-document resolution, no second document. A property that would need the
*shape* of the schema a `$ref` points at is still not a predicate of either kind
and is declared nowhere: that is what the `~>` operator below descends for.

A predicate selector is a selector like any other everywhere else: `--selector`
accepts one, refuses a misspelling of one by name, and reports an undeclared one
as absent.

##### The member-only readings

Five readings are a conjunction **member** and are not selectors. They are a
closed list of 5, declared as `MEMBER_ONLY_PREDICATES` in
`scripts/openapi-surface-census.py` and restated here, with a drift gate over the
pair, exactly as the predicates above are.

**Why they are not predicates**, which is the whole reason the list exists apart
from the one above. `resolve_schema_pointer` has exactly one production call
site — `field_type_ref`, on an array-typed property whose `items` is a reference,
behind a `starts_with("#/components/schemas/")` guard — so a node writing such a
pointer anywhere else is one the generator never walks.
`openbanking-brasil-directory` writes exactly that node:
`#/components/schemas/ClientCreationResponse/properties/client_id` sits on a path
parameter's schema. A standalone selector over one of these readings would count
it, and counting a node that selects **no** case of that function's table is the
miscount [the exactness rule](#the-selector-grammar) disqualifies. So each is
declared where a conjunction can carry it as its last member behind that caller
gate, and nowhere else: the census never records one on its own, and `--selector`
refuses one by name as it refuses any undeclared spelling. The five selectors
cases 3 to 7 of `resolve_schema_pointer` actually carry are the conjunctions that
gate them.

What each reads is not the *shape* of a `$ref`'s target — that is what `~>`
descends for — but the *correspondence* between a pointer's later segments and
the nesting they address: a joint property of a value and the document it points
into, which is why they walk the document context rather than resolve through it,
and which is the enumeration hole
[the case analysis](#the-six-blind-regions-of-srcirrs-case-by-case)
recorded as H-pointer-nesting until the conjunctions carrying them closed it.

- `schema.$ref:pointer-walk-reaches=allOf` — one per Schema Object whose `$ref`
  is a `#/components/schemas/` pointer that `resolve_schema_pointer` of
  `src/ir.rs`, walking it through this document, reads a segment spelled `allOf`
  at. It is the *other* of the two resolutions — the one `~>` deliberately does
  not perform — so it requires the prefix, takes the component the **head**
  segment names, and then walks the remaining segments structurally through
  `allOf`, `oneOf`, `anyOf`, `properties` and `items`. Reading the segment is
  what selects the arm, and asking whether the schema at that position declares
  the field it names is the arm's *body*, so this counts a pointer whose target
  declares no `allOf` at all and a trailing `.../allOf` with no index after it.
  What decides whether a **later** segment is read is whether every earlier arm
  resolved — the head naming a declared component, a composition index landing in
  range, a property key being declared, an `items` being written — which is why
  this reading is a joint property of the reference value and the document it
  points into rather than a shape at either end.
- `schema.$ref:pointer-walk-reaches=oneOf` — one per Schema Object whose `$ref`
  is such a pointer that walk reads a segment spelled `oneOf` at, on the same
  terms.
- `schema.$ref:pointer-walk-reaches=anyOf` — one per Schema Object whose `$ref`
  is such a pointer that walk reads a segment spelled `anyOf` at, on the same
  terms. The three above are three arms rather than one: a pointer naming one of
  the composition fields selects that field's arm and no other.
- `schema.$ref:pointer-walk-reaches=properties` — one per Schema Object whose
  `$ref` is such a pointer that walk reads a segment spelled `properties` at. The
  arm consumes the *key* segment after it, which the count rule excludes as a
  name, so what this says is that the walk reached the step rather than which
  property it addressed; a trailing `.../properties` enters the arm and then
  fails for want of a key, which is where this reading and `ref_to_class`'s part
  company.
- `schema.$ref:pointer-walk-reaches=items` — one per Schema Object whose `$ref`
  is such a pointer that walk reads a segment spelled `items` at. It consumes no
  following segment, so a pointer writing two in a row addresses two nesting
  levels and is still one place the shape is written. The five above are read off
  the five arms of `resolve_schema_pointer`'s own segment loop, one apiece, and
  they carry a value after `=` for the reason `schema.type:primary=array` does:
  which of a closed set of five segment spellings the walk read is a position
  rather than a presence.

A shape that is a **combination** of fields rather than one field emits a
**conjunction selector**, the fourth and last kind. The three kinds above each
name one thing about one node and are all position-insensitive, so `$ref`,
`items`, `oneOf` and `properties` are each `golden` on their own while every
combination of them is unnamed, unmeasured and unclassifiable — which is why the
six blind regions of `src/ir.rs`
[the join table names](#the-ranked-list-against-golden-blind-spots) appear in
neither the feature denominator nor the gaps. Two composition operators over the
selectors already defined close that:

- **`&` joins members declared at one object-model node.** Each member is a
  field, valued or predicate selector the grammar already accepts, written in its
  own spelling.
- **`>` descends into the object a field's value is**, so the members after it
  are read against that object rather than the one before it. It composes left to
  right, and a group joined by `&` sits at one position.
- **`~>` descends into the schema the Reference Object written at the group's
  last member *denotes*** — the one it resolves to against the document being
  censused — so the members after it are read against that schema rather than
  against the `$ref` node that names it. It composes exactly as `>` does: the
  member it binds to is the group's last, and a group joined by `&` sits at one
  position. `>` is untouched by it and keeps its one meaning everywhere: descend
  into the object the value **is**, as written.

**Which resolution `~>` performs.** `src/ir.rs` resolves a reference two ways and
they are not interchangeable, so the operator says which of them it is, in terms
a reader can apply to a reference value without opening the crate:

- **`~>` performs the last-segment lookup.** It takes the reference's **last**
  `/`-separated segment and looks that name up in the document's own
  `components.schemas`. It traverses nothing, requires no prefix, and opens no
  second document.
- **`~>` does not perform the pointer walk.** That other resolution requires the
  `#/components/schemas/` prefix, takes the component its **head** segment names,
  and then walks the reference's remaining segments structurally through `allOf`,
  `oneOf`, `anyOf`, `properties` and `items`.

`#/components/schemas/A/properties/b` is a reference value the two answer
differently, and the difference is not a detail: **`~>` yields the component
named `b`** — the whole schema `components.schemas.b`, if the document declares
one, and nothing at all if it does not — while the pointer walk yields `A`'s
property `b`. They differ at the other end too: `#/definitions/Foo`, the shape a
Swagger conversion writes, **`~>` yields the component named `Foo`** and the
pointer walk yields nothing, because the prefix it requires is absent. `~>` is
the last-segment lookup because that is the resolution the arms of
`prop_type_ref`, `hoist_union_variant` and `nested_array_element` that read a
`$ref`'s target actually call —
[which arm performs which](#the-arms-an-observation-surface-answers-for) is
stated per arm — and a descent mirroring the other one would count documents
those arms never reach.

**Reference depth is one.** A reference edge is traversed only from a node the
walk reached *without* traversing one, so no chain of references is followed and
a cycle among `components.schemas` entries cannot be walked round: each node of
one is counted at most once, on its own resolution, and the census completes.
A conjunction spelling a second `~>` therefore holds nowhere. The path-local
re-entry guard `>` already has guards a resolved edge the same way, so a
reference resolving back to a node already on the conjunction's own path does not
hold either.

**`~>` is a second operator rather than a redefinition of `>`, and that was
settled against the code.** `schema.items>schema.$ref`, `schema.oneOf>schema.$ref`
and `schema.anyOf>schema.$ref` all match by finding a Reference Object *at* the
descended-into node, thousands of sites across the corpus; a `>` that resolved
before matching would land on the target, which writes no `$ref`, and all three
would count zero. And `prop_type_ref`'s composition gate is guarded by
`prop_schema.reference.is_none()` while `nested_array_element`'s is preceded by
`if items.reference.is_some() { return None; }`, so a property or an `items` that
*is* a `$ref` to a `oneOf` schema never reaches either composition arm — a
resolving `>` would count those documents under `schema.properties>schema.oneOf`
and `schema.items>schema.oneOf`, which is evidence recorded against documents the
generator sends elsewhere.

A conjunction has exactly one name: a group's members are written in
lexicographic order, except that the member a following descent operator descends
through is written last, since that is the member the operator binds to. The rule
reads the same across `>` and `~>` — what puts a member last is that *a* descent
binds to it, not which one — so an array schema whose `items` declare a `oneOf` is
`schema.type=array&schema.items>schema.oneOf` and nothing else, and a schema one
of whose properties is a `$ref` to a `oneOf` is
`schema.properties>schema.$ref~>schema.oneOf` and nothing else.

The **count rule is the one the grammar already has**, and it is the only count
rule this grammar has: one per node at the *leftmost* position — one per place
the shape is written — for both descent operators and every selector kind alike.
So `schema.items>schema.type=array` counts one per Schema Object whose `items`
value declares an array type, `schema.discriminator&schema.oneOf` would count one
per Schema Object declaring both, and `schema.properties>schema.$ref~>schema.oneOf`
counts one per Schema Object one of whose properties is a Reference Object whose
target declares `oneOf` — one per *referencing* node, never one per target. A
field holding several objects (a `oneOf` list, a `properties` map) satisfies the
members after the `>` when any one of those objects does, which is what keeps the
count one per leftmost node rather than one per member; a `~>` reaches exactly one
schema, so there is nothing there to be satisfied by several.

**Which conjunctions are enumerable.** The operators can spell an unbounded set —
four schema fields alone make fifteen non-empty combinations before nesting, and
unbounded with it — so what bounds the list is not the grammar but the generator:

> A conjunction is worth enumerating **iff two source documents differing only in
> it take different paths through one of the six blind functions** of
> `src/ir.rs` — `resolve_schema_pointer`, `nested_array_element`,
> `hoist_union_variant`, `ref_to_class`, `prop_type_ref`, `path_group`.

The list is therefore read off those functions' own branch structure, one
selector per branch a document can select, and never off the cross-product of the
grammar: `nested_array_element` distinguishes nine cases a document can reach,
where the cross-product of the four fields driving it would offer fifteen
combinations before nesting and unboundedly many with it. The code is the bound, and
[the case analysis below](#the-six-blind-regions-of-srcirrs-case-by-case) is the
derivation, branch by branch, of every entry and of every branch no selector kind
can express. Three conventions that derivation applies, stated once:

- **A function's entry gate is the leftmost member of each of its cases**, not a
  case of its own: two documents differing only in whether they write `items`
  differ in a *field*, which the grammar already names, rather than in a
  conjunction.
- **A branch reached through `x.or(y)` is two cases, not one.**
  `one_of.as_ref().or(&any_of)` is selected identically by a document that writes
  only `anyOf`, and a selector naming `schema.oneOf` does not count that document,
  so both spellings are declared. Where a second `or` sits inside the first the
  cases are their product; where the callee narrows one spelling away, only the
  surviving spelling is declared.
- **A case carries a selector only when that selector is exact; otherwise it is a
  hole.** Exact means the nodes the census counts and the nodes that select the
  branch differ *only* where another case of the same table claims them. Arms in a
  chain overlap by construction — a later arm runs only because the earlier ones
  did not — and an overlap between two listed cases is visible to a reader,
  because both are in the table. What disqualifies a selector is the arm's **own**
  condition reading something no selector kind can express: a JSON value's kind or
  content, a collection's emptiness or length, a boolean field's value, which
  member of a `type` array comes first, or a negation. Then the count silently
  includes documents that select *no* case of the table, and nothing says so.

  This rules out a selector **narrower** than its case — one continuation of
  `resolve_schema_pointer`'s `"allOf"` arm, leaving every other pointer form
  uncounted — and equally one **broader** than it: `schema.oneOf>schema.example&schema.type=object`
  would count a variant declaring `type: object` beside a scalar example, an empty
  `examples`, or an object whose values are themselves schema declarations, and
  `hoist_union_variant` sends all three to `base_type_ref`. Seventy-four of the
  eighty-nine cases below survive this test; the other fifteen name the
  extension that would close them.

  What the test does **not** rule out is a node whose own declaration contradicts
  itself. A schema writing `$ref` beside a sibling keyword is one — 3.0 says the
  siblings are ignored, and `schema.oneOf>schema.allOf` has counted such a node
  since this list was first declared — and a scalar `type` beside an object-only
  keyword (`properties` on a `type: string`) is another. A selector naming the
  object-side keyword counts both, and neither selects the arm; but a
  contradiction is not a shape a document declares, and reading them as leaks
  would make every case of every table a hole. That is the reading these rows have
  always been written under, and it is stated here rather than left implicit.
- **A case's closing selector may be a conjunction of *declared* selectors,
  rather than one predicate that bundles them.** Several arms stack conditions:
  every case of `hoist_union_variant` inside its `type: array` guard reads the
  guard *and* something about the item, and `simple_nullable_member` reads an
  arity *and* refuses a string-enum member. Where an arm's own condition is more
  than one property, its selector joins one declared member per property under the
  `&` and `>` operators above, so a case row carrying
  `schema.oneOf>schema.type:primary=array&schema.items>schema.properties:non-empty`
  is this grammar composing three members it declares separately — not a fifth
  mechanism. A predicate that bundled the three would be a name no other case
  could reuse, and would hide from a reader which property the arm actually reads.

A case earns a selector when every property its own condition reads is one the
grammar can name — a field written, a member of a closed value set, or one of the
node-local predicates above — and those members compose into one conjunction.
The conjunctions are themselves a closed list of 61, declared in
`scripts/openapi-surface-census.py` beside the predicate table and restated here,
with a drift gate over the pair:

- `schema.anyOf>schema.$ref` — one per Schema Object one of whose `anyOf`
  members is a Reference Object.
- `schema.anyOf>schema.allOf` — one per Schema Object one of whose `anyOf`
  members declares `allOf`.
- `schema.items>schema.$ref` — one per Schema Object whose `items` value is a
  Reference Object.
- `schema.items>schema.anyOf` — one per Schema Object whose `items` value
  declares `anyOf`.
- `schema.items>schema.oneOf` — one per Schema Object whose `items` value
  declares `oneOf`.
- `schema.oneOf>schema.$ref` — one per Schema Object one of whose `oneOf`
  members is a Reference Object.
- `schema.oneOf>schema.allOf` — one per Schema Object one of whose `oneOf`
  members declares `allOf`.
- `schema.properties>schema.anyOf` — one per Schema Object one of whose
  properties declares `anyOf`.
- `schema.properties>schema.oneOf` — one per Schema Object one of whose
  properties declares `oneOf`.
- `schema.items>schema.type:primary=array` — one per Schema Object whose
  `items` value declares `array` as its primary type.
- `schema.items>schema.properties:non-empty` — one per Schema Object whose
  `items` value declares a non-empty `properties` map.
- `schema.items>schema.additionalProperties=false` — one per Schema Object
  whose `items` value declares `additionalProperties: false`.
- `schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` holding a `oneOf` with one non-`null` member
  beside a `null` one.
- `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` holding an `anyOf` with one non-`null` member
  beside a `null` one.
- `schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` holding a `oneOf` with one non-`null` member
  beside a `null` one.
- `schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` holding an `anyOf` with one non-`null` member
  beside a `null` one.
- `schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` declaring `oneOf`.
- `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` declaring `anyOf`.
- `schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` declaring `oneOf`.
- `schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` declaring `anyOf`.
- `schema.oneOf>schema.type:primary=array&schema.items>schema.properties:non-empty` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` declaring a non-empty `properties` map.
- `schema.anyOf>schema.type:primary=array&schema.items>schema.properties:non-empty` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` declaring a non-empty `properties` map.
- `schema.oneOf>schema.type:primary=array&schema.items>schema.additionalProperties=false` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` declaring `additionalProperties: false`.
- `schema.anyOf>schema.type:primary=array&schema.items>schema.additionalProperties=false` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` declaring `additionalProperties: false`.
- `schema.oneOf>schema.properties:non-empty` — one per Schema Object one of
  whose `oneOf` members declares a non-empty `properties` map.
- `schema.anyOf>schema.properties:non-empty` — one per Schema Object one of
  whose `anyOf` members declares a non-empty `properties` map.
- `schema.properties>schema.enum:string-valued` — one per Schema Object one of
  whose properties declares a string-valued `enum`.
- `schema.properties>schema.const:string-valued` — one per Schema Object one
  of whose properties declares a string-valued `const`.
- `schema.properties>schema.properties:non-empty` — one per Schema Object one
  of whose properties declares a non-empty `properties` map.
- `schema.properties>schema.additionalProperties=false` — one per Schema
  Object one of whose properties declares `additionalProperties: false`.
- `schema.properties>schema.oneOf:sole-non-null-member` — one per Schema
  Object one of whose properties declares a `oneOf` with one non-`null` member
  beside a `null` one.
- `schema.properties>schema.anyOf:sole-non-null-member` — one per Schema
  Object one of whose properties declares an `anyOf` with one non-`null`
  member beside a `null` one.
- `schema.properties>schema.type:primary=array` — one per Schema Object one of
  whose properties declares `array` as its primary type.
- `schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.properties:non-empty` —
  one per Schema Object one of whose properties declares a one-member `oneOf`
  whose member declares a non-empty `properties` map.
- `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.properties:non-empty` —
  one per Schema Object one of whose properties declares a one-member `anyOf`
  whose member declares a non-empty `properties` map.
- `schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.additionalProperties=false` —
  one per Schema Object one of whose properties declares a one-member `oneOf`
  whose member declares `additionalProperties: false`.
- `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.additionalProperties=false` —
  one per Schema Object one of whose properties declares a one-member `anyOf`
  whose member declares `additionalProperties: false`.
- `schema.properties>schema.allOf:annotated-ref` —
  one per Schema Object one of whose properties is an annotated `$ref` — an
  `allOf` of at least two members, exactly one a Reference Object and every
  other declaring nothing.
- `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.enum:string-valued` —
  one per Schema Object one of whose properties is an annotated `$ref` whose
  target declares a string-valued `enum`.
- `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.const:string-valued` —
  one per Schema Object one of whose properties is an annotated `$ref` whose
  target declares a string-valued `const`.
- `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.oneOf` —
  one per Schema Object one of whose properties is an annotated `$ref` whose
  target declares `oneOf`.
- `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.anyOf` —
  one per Schema Object one of whose properties is an annotated `$ref` whose
  target declares `anyOf`.
- `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.properties:non-empty` —
  one per Schema Object one of whose properties is an annotated `$ref` whose
  target declares a non-empty `properties` map.
- `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.allOf` —
  one per Schema Object one of whose properties is an annotated `$ref` whose
  target declares `allOf`.
- `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.additionalProperties=false` —
  one per Schema Object one of whose properties is an annotated `$ref` whose
  target declares `additionalProperties: false`.
- `schema.oneOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` that are an annotated `$ref` resolving to a
  component of this document.
- `schema.anyOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` that are an annotated `$ref` resolving to a
  component of this document.
- `schema.items>schema.oneOf:discriminated-union` —
  one per Schema Object whose `items` value is a union `discriminated_union`
  of `src/ir.rs` builds from its `oneOf`.
- `schema.items>schema.anyOf:discriminated-union` —
  one per Schema Object whose `items` value is such a union built from its
  `anyOf`, written where no `oneOf` is.
- `schema.items>schema.discriminator:inheritance-union` —
  one per Schema Object whose `items` value is the base of an
  inheritance-style discriminated union, declaring a resolving
  `discriminator` mapping and no composition of its own.
- `schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf:discriminated-union` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` that are a union `discriminated_union` builds
  from their `oneOf`.
- `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` that are such a union built from their `anyOf`.
- `schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:discriminated-union` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` that are a union `discriminated_union` builds
  from their `oneOf`.
- `schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` that are such a union built from their `anyOf`.
- `schema.properties>schema.oneOf:discriminated-union` —
  one per Schema Object one of whose properties is a union
  `discriminated_union` builds from its `oneOf`.
- `schema.properties>schema.anyOf:discriminated-union` —
  one per Schema Object one of whose properties is such a union built from
  its `anyOf`, written where no `oneOf` is.
- `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=allOf` —
  one per Schema Object one of whose properties declares `array` as its primary
  type over `items` that are a component-schema pointer `resolve_schema_pointer`
  reads an `allOf` segment at.
- `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=oneOf` —
  one per Schema Object one of whose properties declares `array` as its primary
  type over `items` that are such a pointer read a `oneOf` segment at.
- `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=anyOf` —
  one per Schema Object one of whose properties declares `array` as its primary
  type over `items` that are such a pointer read an `anyOf` segment at.
- `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=properties` —
  one per Schema Object one of whose properties declares `array` as its primary
  type over `items` that are such a pointer read a `properties` segment at.
- `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=items` —
  one per Schema Object one of whose properties declares `array` as its primary
  type over `items` that are such a pointer read an `items` segment at.

A conjunction selector is a selector like any other everywhere else: `--selector`
accepts one, refuses a misspelling of one by name — and refuses a well-formed
combination nobody declared, because the list is closed by the code rather than
by the operators — and reports an undeclared one as absent.

The last five are the five arms of `resolve_schema_pointer`'s segment loop, each
behind that function's own **caller gate**: `field_type_ref` calls it on an
array-typed property's `items` reference and nowhere else, so the three members in
front of the predicate are what keep the count off a pointer the generator never
walks. `openbanking-brasil-directory` writes one — its
`#/components/schemas/ClientCreationResponse/properties/client_id` sits on a path
parameter's schema — and the predicate counts it while the conjunction does not.

**A selector absent from the census output for every registered source is a
feature no registered source declares.** That absence is the evidence a `gap` row
cites, and `--selector` prints it as such rather than printing nothing.

## The entry table

Every classified feature is one row of an eight-column GitHub-flavoured markdown
table, with this header and this column order:

```
| key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |
```

| column | what goes in it |
|---|---|
| `key` | a stable, unique, lower-kebab identifier for the feature. Where [`fern-limitations.md`](fern-limitations.md) already names the same feature, spell the key **identically to that file's key**, so the two documents join on it |
| `oas` | one of `3.0`, `3.1`, `both` |
| `spec location` | the OpenAPI object and field the row is about, written as `Object Name.field`, so a reader can find it in the specification |
| `category` | exactly one of `golden`, `limitations`, `gap` |
| `evidence` | see the category rules below — each category fixes what belongs here |
| `crozier sites` | **required on a `gap` row, empty otherwise**: the `src/` files that read this feature and how many distinct places in them do, or `none` when crozier reads it nowhere. A measurement, and what the ranking's first two criteria are computed from |
| `why bytes could move` | **required on a `gap` row, empty otherwise**: one sentence naming the generated artifact that would differ if crozier and Fern disagree about this feature |
| `settlement` | **required on a `gap` row, empty otherwise**: one of `FIXTURE`, `PROBE` or `UNREACHABLE`, followed by one sentence saying what settling it takes |

## The category rules

The two interesting conditions genuinely overlap — `fern-limitations.md`'s own
Route 1 evidence *is* a committed golden whose source declares the shape, so a
feature can satisfy both at once, and several already do. Categories are therefore
assigned by **precedence**, tested in this order, so exactly one applies to every
feature:

1. **`golden`** — at least one registered golden fixture's own source document
   declares the feature. This wins over a limitations row because it is the
   stronger evidence: a byte-matching golden is crozier-versus-Fern parity
   evidence, while `fern-limitations.md` measures Fern alone and says so itself
   under *What these measurements do not establish*.
   **Evidence cell:** the fixture names and the declared count the census reports,
   **followed by** the `fern-limitations.md` key and verdict where that file also
   carries a row for the feature.
2. **`limitations`** — no registered golden source declares it, and
   `fern-limitations.md` carries a row for it with a verdict.
   **Evidence cell:** the `fern-limitations.md` key and its verdict, spelled the
   way that file's *How to read a verdict* section spells them (`implements`,
   `discards`, `ignores`, `refuses`, `crashes`, `coincidence`, `unmeasured`) —
   never a synonym.
3. **`gap`** — neither holds. This is the answer the whole document exists to
   produce.
   **Evidence cell:** the census result showing zero declarations across every
   registered source, together with the statement that no `fern-limitations.md`
   row names it.

**The overlap is recorded, not discarded.** Where a feature satisfies both
condition 1 and condition 2, the row's category is `golden` and its `evidence`
cell carries both halves, so a reader asking *which golden-covered features does
the limitations ledger also rule on?* can answer it from the table alone.

The keys `fern-limitations.md` already owns come out as a list with

```
grep -oP '^\| `\K[A-Za-z0-9._-]+(?=` \| *[0-9]+ \|)' docs/fern-limitations.md | sort -u
```

which is how a region joins on that file without reading its three thousand lines.

## The settlement classes

Every `gap` row carries exactly one:

- **`FIXTURE`** — a real-world, redistributable OpenAPI 3 document at an immutable
  ref plausibly declares the feature *and* Fern plausibly emits bytes derived from
  it, so a corpus row can pin it.
- **`PROBE`** — what Fern does with the feature is unknown and no corpus row
  settles it *today*, so the settlement is a locally authored probe recorded in
  [`fern-limitations.md`](fern-limitations.md). The corpus takes real-world
  specifications only; a probe is never proposed as a fixture. Two distinct
  things put a row in this class — a **structural** measurement no single
  specification can hold, and a **witness-supply** shortfall, a shape for which
  no witness has been found at all — and only the first is
  permanent; [The probe backlog](#the-probe-backlog) draws that line and names
  the two kinds, and each row's own `settlement` cell says which it is.
- **`UNREACHABLE`** — the shape has no position in a generated Python SDK at all,
  and saying so is the settlement.

## The ranking rubric

Applied to **`FIXTURE` rows only**, in this strict order, the first difference
deciding and the last being a total tiebreak:

1. **Crozier handling sites, ascending**, from the row's `crozier sites` cell.
   Zero ranks first: crozier emits nothing derived from the shape, so if Fern
   does, a divergence is certain rather than possible.
2. **Blind-spot reach, descending.** The `golden blind spots` region count that
   `just fixtures-coverage` reports for the `src/` file the row's `crozier sites`
   cell names — this repository's own measurement of generator behaviour only
   crozier's own tests assert. A feature handled in a file no golden reaches is
   worth more than the same feature in a densely golden-covered one. A row whose
   `crozier sites` cell is `none` scores zero here and has already won on the
   first criterion.
3. **Emitted-artifact breadth, descending.** How many distinct kinds of generated
   file the feature can move — the types module, the client method signature, the
   raw client body, the errors module, `reference.md`, the core module.
4. **Witness supply, descending.** How many screened real-world documents declare
   the feature.
5. **Key, ascending alphabetically.**

## Ranked gap backlog

The six region files, read as one body of work. Two measurements feed it:

- **`just surface-census`**, for the classifications and for criterion 4. The
  snapshot is pinned by digest in
  [`document-paths.md`'s snapshot reconciliation](openapi-surface/document-paths.md#snapshot-reconciliation)
  rather than restated here, and that pin is now the current walk, so the check it
  guards runs to completion rather than halting on it.
  It reads **169** registered sources, of which
  **152** carry a committed golden. `document-paths`'s own evidence cells are
  transcribed from that walk; the other five region files' cells are still dated
  to the earlier walks each was taken on, except that `schemas`, `bodies-media`
  and `parameters` have had the twenty-eight cells the free-map-key walk repair
  moved republished against it, each as that repair's own difference rather than
  as a re-transcription. Refreshing the rest is each file's own measurement
  against this same pin. No classification in this section depends on
  which walk a cell was taken from — a category moves only when a source is
  registered or a selector is added, and both are recorded in that section's own
  history. **Where a paragraph below says a walk read 164 sources, that is the
  walk it was taken on and not a second count of the corpus**: the conjunction
  classification and the free-map-key repair both ran before the widened licence
  rule's registrations, the one batch that has landed since, which took the walk
  from 164 sources to 169. A walk over more sources can promote a
  row to `golden` and can never demote one, so those paragraphs' conclusions hold
  over the 169 unchanged; only their arithmetic is dated.
- **`just fixtures-coverage`**, for criterion 2 alone. That recipe is outside
  `just check` — it needs network and runs the corpus instrumented — so its
  per-file counts are a dated snapshot (2026-09-06), stated once, in the join
  table under
  [The ranked list against `golden blind spots`](#the-ranked-list-against-golden-blind-spots).
  The gate cannot produce that measurement, but it does reconcile against it:
  see [Refreshing the coverage snapshot](#refreshing-the-coverage-snapshot).

What this section takes from the six region files, `RankedBacklogTests` in
`tests/surface_census_test.py` takes back from them — the per-region counts and
the totals narrated from them, both backlogs' membership and their stated sizes, each ranked row's
owning region, criterion 1, and — while the ranked list has rows — the rubric
order and the median it produces. `just
check` runs it offline, so a region row added, reclassified or re-measured fails
the gate here rather than leaving this section quietly stale. Criteria 3 and 4
are the two the gate cannot take back, because the region files publish no number
for either; each bullet below says where its number comes from.

### What the walk enumerated

| region | features | `golden` | `limitations` | `gap` | `FIXTURE` | `PROBE` | `UNREACHABLE` |
|---|---:|---:|---:|---:|---:|---:|---:|
| [`parameters`](openapi-surface/parameters.md) | 70 | 51 | 19 | 0 | 0 | 0 | 0 |
| [`schemas`](openapi-surface/schemas.md) | 198 | 152 | 21 | 25 | 22 | 0 | 3 |
| [`bodies-media`](openapi-surface/bodies-media.md) | 47 | 36 | 11 | 0 | 0 | 0 | 0 |
| [`security`](openapi-surface/security.md) | 50 | 38 | 12 | 0 | 0 | 0 | 0 |
| [`document-paths`](openapi-surface/document-paths.md) | 70 | 65 | 5 | 0 | 0 | 0 | 0 |
| [`oas31-extensions`](openapi-surface/oas31-extensions.md) | 52 | 33 | 2 | 17 | 0 | 0 | 17 |
| **total** | **487** | **375** | **70** | **42** | **22** | **0** | **20** |

The walk enumerated **487** features and landed each in exactly one category:
**375** `golden`, **70** `limitations`, **42** `gap`. The `gap` column splits by
settlement class into **22** `FIXTURE`, **0** `PROBE` and **20** `UNREACHABLE`.

**What the `golden` count means, and what it does not.** 375 of those 487
features carry byte-match evidence: a registered source declares the feature and
its committed Fern golden byte-matches, so crozier and Fern are compared over
real bytes there and `just check` fails if they diverge. The other 112 do not. 70
carry a Fern verdict measured on a probe and no byte comparison at all, and 42
have neither. Neither
column is a defect count, and neither 375 nor 487 is a claim of exhaustion —
[the section below](#golden-classified-is-not-golden-exhausted) states where the
remaining distance lies, including the part of it this walk cannot enumerate.

**What the `gap` count means.** 42 is the number of OpenAPI shapes for which
crozier's behaviour is vouched for by nothing but crozier: no committed golden's
source declares the shape, so no byte comparison against Fern touches it, and
[`fern-limitations.md`](fern-limitations.md) has never measured Fern on it, so
nothing contradicts whatever crozier does. `just check` is green over all 42
either way. It is not a defect count — 20 of them (`UNREACHABLE`) have no
position in a generated Python SDK at all, and saying so is their settlement.
That leaves 22 for the two backlogs below, every one of them in the fixture one:
they are branches of `src/ir.rs` a real document can select and no committed
golden reaches, named for the first time by the node-local predicate family, by
the pointer-form one after it, by the annotated-`$ref` pass after that, by the
discriminated-union pass after that and by the pointer-walk pass after that. **One
of them is not a shape this corpus has never written** —
`annotated-ref-target-composed` is declared by two registered sources, and both
are documents Fern's own check refuses, so no golden can ever be committed for
either. It is a `gap` for the same reason as the rest — nothing compares crozier's
bytes to Fern's over the branch — and for a different cause, and its own row says
which.

### Reconciliation

**Each feature is classified exactly once.** The 487 rows carry 487 distinct
keys, and no `spec location` string appears in two region files — the assertion
[`document-paths.md`](openapi-surface/document-paths.md#snapshot-reconciliation)
already runs over all six files, re-run here and passing. Thirteen spec
locations carry more than one row, every one of them inside a single region and
every one of them the grammar's field-versus-value split: `Schema Object.format`
heads 28 rows (the field, plus one per registered format value), `Media Type
Object content-map key` 11, `Schema Object.additionalProperties` 4. A field row
and a valued row are two features, not one feature counted twice — the census
emits `schema.format` and `schema.format=uuid` as two selectors.

**Nothing is left unclassified.** Every row's `category` cell holds one of
`golden`, `limitations`, `gap`, and every `gap` row's `settlement` cell holds one
of `FIXTURE`, `PROBE`, `UNREACHABLE`.

**Every ledger key is accounted for.** The canonical join reports 87 keys, of
which 83 are a region row's key verbatim. The other four:

| ledger key | how it is accounted for |
|---|---|
| `status_code` | **Not a feature key.** It is a row label inside the ledger's 407/421 probe table, which the join's `\| key \| N \|` shape matches by accident — the `bodies-media` region's method notes say the same. The join's real yield is 86. |
| `encoding-explode-or-allowReserved` | One ledger row covering two fields; `bodies-media` splits it into `encoding-explode` and `encoding-allow-reserved`, both `limitations`, both citing that verdict. |
| `servers-multiple-path-or-operation` | One ledger row covering two levels; `document-paths` splits it into `pathitem-servers` and `operation-servers`, both `golden`. |
| `relative-file-ref` | A *target form* of `Path Item Object.$ref`, which `document-paths` classifies once as `pathitem-ref` (`golden` since corpus row 99 declares 36 of them, citing verdict `discards`). The walk enumerates the field; the ledger additionally rules on one form of what it points at. |

**The one correction this change records, and the enumeration hole it closes.**
The paragraph this replaces recorded `normalization-collision` — two
`components.schemas` names that collide after identifier normalization
(`OBRate1_0` beside `OB_Rate1_0`) — as *the walk's one enumeration hole*: no
region row carried it, because the selector grammar excludes map keys that are
*names* by design, and it named exactly what closing it would take, a selector
over `components.schemas` keys under `naming::class_name`. That selector is now
declared: `components.schemas:normalized-collision`, in the grammar above beside
the path-side predicate it mirrors. [`schemas.md`](openapi-surface/schemas.md)
carries the row, which is why the walk's total moves from 402 to 403.

**Its category is what the new measurement reports, not what that paragraph
predicted.** The prediction was `limitations`, on the reading that the row's
evidence would be the ledger verdict. The measurement outranks it: the predicate
reports **8** declaration sites in **3** registered sources —
`openbanking.org.uk-account-info-openapi` (4), `amazonaws.com-cloudformation` (2)
and `daniweb-connect` (2), a third witness the old prediction did not know about —
and all three carry a byte-matching committed golden, so under
[the classification precedence](#the-category-rules) the row is `golden`, with the
ledger key `normalization-collision` and its verdict `discards` recorded beside
that evidence rather than instead of it. It moves the `schemas` region's `golden`
count and neither backlog below, since a `golden` row is in neither.

**The same paragraph's reasoning applied to two more rows, and they moved too.**
`document-paths`'s `templated-path-segment` and `several-path-template-variables`
each rested on the same kind of sentence — *path keys are free-map names, so no
selector reports a declaration* — which is a statement about this instrument's
reach rather than about the world, and this document already rules that such a
row's measurement has not been made. Two more predicates over Paths Object keys,
`openapi.paths:templated-key` and `openapi.paths:several-template-expressions`,
make them measurable; 93 golden-bearing sources declare a templated key and 53 a
key carrying more than one expression, so both rows are `golden` and both leave
the ranked `FIXTURE` backlog. That is the whole of the movement in the counts
above.

**One scope boundary is read two ways, and no row is lost to it.** The index's
rule is that the *containing* object's region owns a field while the *held*
object's region owns the object. `document-paths` applies it to `Operation
Object.parameters` and owns that row; `parameters` applies the opposite reading
to `Path Item Object.parameters` and owns that one. Both rows are `golden`, each
field is classified exactly once, and the uniqueness check above passes — so the
partition holds. It is recorded rather than corrected because a later scope edit
should know the two regions disagreed about which side of that line the
`parameters` field falls on.

**The nine conjunctions are classified, and every one of them is `golden`.** The
[conjunction selectors](#the-selector-grammar) were declared without being run;
running them over all 164 registered sources is what takes the walk's total from
403 to 412. Every one of the nine is declared by at least one registered source
carrying a byte-matching committed golden, so under
[the precedence](#the-category-rules) none is `limitations` (no
[`fern-limitations.md`](fern-limitations.md) key names any of them) and none is a
`gap`. **Zero of the nine are gaps**, which is the number the next node's work is
sized by: there is nothing here to settle, and the settlement pass that went
looking took none of the four routes a `gap` row takes and ran no witness
search. What it measured instead is
[what the whole conjunction pass moved in the goldens' six blind regions](#what-the-conjunction-pass-moved-in-those-six-regions) —
nothing — which moves no row's category either way. The measured range runs from
`schema.items>schema.$ref` (4,151 sites in 114 sources, 3,328 of them in the 102
that carry a golden) to `schema.anyOf>schema.allOf` (4 sites in `braintrust-dev`
alone). All nine anchor on a Schema Object, so all nine are
[`schemas.md`](openapi-surface/schemas.md)'s: that region moves from 117 features
to 126 and from 93 `golden` to 102, and neither backlog below changes, since a
`golden` row is in neither. The prediction the blind-spot count invited — that
combinations of golden fields would be where the goldens stop reaching — is the
one the measurement refutes: the corpus was never blind to these shapes, only the
census was. What the rows preserve is the part of that reading that survives, and
each says it in its own evidence cell: a golden pinning a conjunction pins the
bytes for the shapes its own document sends down the branch, not the branch's
whole behaviour.

**The instrument was repaired first, and the classification is the repaired
walk's.** The census used to skip a map key that is not a string *and* the
free-map descent under it, so a Responses Object keyed by an unquoted YAML
integer (`200:`) lost its entire subtree. Six registered sources write their
status codes that way — `free5gc-namf-communication`, `free5gc-pdu-session`,
`kytos-sdntrace-cp`, `marimo`, `query-parameters-openapi` and
`worldcoin-signup-sequencer`, one more than the change that found the defect had
counted. Over the 164 sources the repair moves **89** per-source counts, across
35 selectors, and adds **2,584** declaration sites; it takes no selector from
zero to non-zero corpus-wide, and **no conjunction count moves under it**, so
the classification above is the same either way and is nonetheless taken from
the repaired walk. Twenty-eight evidence cells across
[`schemas.md`](openapi-surface/schemas.md) (ten),
[`bodies-media.md`](openapi-surface/bodies-media.md) (twelve) and
[`parameters.md`](openapi-surface/parameters.md) (six) are republished, each as
the difference the repair makes to the walk its cell was taken on, so a reader
can tell a count that moved because the instrument was repaired from one that
moved because the corpus did. No category moves with them. The repair also closes
a discrepancy the ledger had recorded: `fern-limitations.md`'s `encoding-object`
row counted 99 `contentType` and 58 `headers` off `free5gc-pdu-session`'s raw
source against the census's 22 and 13, and the repaired walk reaches 99 and 58.

**No region's category is overturned.** This node re-derived the census join, the
ledger join and the site counts it ranks on, and found no row whose `category` or
`settlement` cell it would change.

### Golden-classified is not golden-exhausted

The probe backlog below is empty and the fixture one carries eleven rows, and a
backlog's size is the easiest thing in this document to misread either way. It
does not say every OpenAPI feature is byte-matched against Fern; it says every
feature this walk enumerated has been *landed* — in a category, with the evidence
that category demands. The distance between a classified feature and an exhausted
one is real, it is measurable, and it lives in four places. Naming them is the
point of this section, because the one claim this file has never made is that
everything is covered. The eleven rows are what the fourth place looks like when
it is worked: they were part of the unnamed work this section describes until a
predicate family named them, and naming them is what moved them into the
denominator and into a backlog at once.

**A `golden` row is one witness, not a branch.** It says a registered source
declares the feature and its committed Fern golden byte-matches — so the bytes
that document's own shapes produce are pinned, and nothing else is. Three
measured examples already in the tree: `audience-dual-header-policy` is `golden`
on two audience goldens declaring 8 sites between them, leaving the rest of the
branch space to unit tests; `x-fern-or-crozier-ignore` is `golden` on corpus row
108's four `x-fern-ignore` operations, one witness that reaches `filter_ignored`'s
Operation-Object arm and leaves its schema arm and the `x-crozier-*` precedence
untouched; and
`media-type-range` is `golden` on a witness reaching two of crozier's seven reads
of a media-type range, which that row's own cell names against the five it does
not. Every conjunction row says the same thing in its own evidence cell, because
a conjunction row is about a *branch*: a golden pinning one pins the bytes for
the shapes its document sends down the arm, not the arm's behaviour.

**A `limitations` row carries no byte comparison at all.** 70 features are there,
and what settles them is a Fern verdict measured on a locally authored probe. That
is a real measurement of Fern and it is not parity evidence: nothing in it
compares crozier's bytes against Fern's over a registered document, and no
`just check` byte-diff touches the shape. The cost is not rhetorical, and the
refreshed join below is where it shows up as a number — settling those rows put
generator code into `src/` that no committed golden reaches: the object-typed
path parameter block in `src/emit.rs` (125 regions of its union) and
`normalize_security_scheme_refs` in `src/openapi.rs` (18), both driven by shapes
no registered source declares. Each such row stays convertible, and the day a
registrable witness turns up the classification precedence promotes it to
`golden` — which is exactly what makes the gap a *supply* problem rather than a
closed question.

**The enumeration cannot see everything, and it says where it stops.** A feature
is enumerable only where a selector can name it, so
[the walk's 482](#what-the-walk-enumerated) is a
denominator bounded by the grammar rather than by the specification. The sharpest
statement of that bound is
[the case analysis](#the-six-blind-regions-of-srcirrs-case-by-case): of the 89
branches those six functions of `src/ir.rs` offer a document, 69 carry an exact
selector and 20 are enumeration holes, each naming the operator or predicate that
would close it and none of them a row anywhere. **That bound has moved four
times, and moving it is what a reader should expect of it.** It read *"of the 53
branches, 9 carry an exact selector and 44 are enumeration holes"* until the
node-local predicate family was declared, *"of the 76 branches, 40 carry an
exact selector and 36 are enumeration holes"* until the annotated-`$ref` pass read
the four arms inside `prop_type_ref`'s resolution gate at the grain their
selectors need, and *"of the 83 branches, 60 carry an exact selector and 23 are
enumeration holes"* until the discriminated-union pass closed
**H-discriminant-value**. The branch count moves when a case is read at a finer
grain — a disjunction split disjunct by disjunct is more rows describing the same
code — and the hole count moves when the grammar grows. The remaining twenty turn
on a JSON value's kind or content, on a comparison across the document, or on the
*absence* of a declaration, and each says which. The same is true off that file —
the enum-member spellings
`src/naming.rs` lowers, the JSON value
*kinds* the example branches of `src/emit.rs` switch on, and the cross-document
`$ref` path of `src/refs.rs`, which the corpus is single-document by construction
and so can never reach. None of that is in the 482, in the 40 `gap` rows, or in
either backlog. It is not unclassified work; it is unnamed work, and this
document's own instrument is what would have to grow first — which is exactly what
the twenty `FIXTURE` rows are: the four times it did.

**And the thin end is one document wide.** A `golden` row rests on whichever
registered sources happen to declare the shape, and for several that is a single
one: `schema.anyOf>schema.allOf` is `golden` on `braintrust-dev`'s 4 declaration
sites and nothing else. Withdraw that corpus row and the feature is a `gap`
without a line of `src/` changing. That is a fact about this corpus at this
commit rather than a property of the feature, and it is the reason "the backlog
is empty" is a statement about today's registered sources and not a property the
generator has earned.

### The ranked `FIXTURE` backlog

**Where this list stands, and the three ways a row left it.** It carries
twenty-four
rows, and none of them is a row that ever stood here before: the list was
exhausted, and five instrument passes refilled it from the one direction an
exhausted backlog can be refilled from — the instrument, not the corpus.
Twenty-four branches of `src/ir.rs`'s six blind functions now have a name, and no
*golden-bearing* registered source declares any of them, which is what a `gap` is.
They are
[tabled at the end of this section](#the-ranked-fixture-backlog) and narrated in
[the paragraph that added the first eleven](#the-eleven-rows-the-node-local-predicates-added),
[the one that added the next two](#the-two-rows-the-pointer-form-predicates-added),
[the one that added the next five](#the-five-rows-the-annotated-ref-pass-added),
[the one that added the next two](#the-two-rows-the-discriminated-union-pass-added)
and [the one that added the last two](#the-two-rows-the-pointer-walk-pass-added).
Everything below them is history: every row that ever stood here left by one of
three routes, and which route a row took is what decides the evidence the tree
now holds for it. The paragraphs below walk them in the order they happened; this
is the shape they add up to.

- **By a registered witness.** A real-world document was screened for licence and
  immutable ref, put to Fern at 5.20.0, and committed as a corpus row with its
  golden. The row is `golden`, and crozier's bytes are compared against Fern's
  over that document on every `just check`. This is the only route that produces
  parity evidence, and it is the route most of this list took — on the corpus
  rows the paragraphs below name one by one, from row 94 through row 136.
- **By a probe measurement.** No document this corpus could register was to be
  had, so Fern's behaviour was measured on a locally authored probe and recorded
  in [`fern-limitations.md`](fern-limitations.md). The row is `limitations`: it
  carries a Fern verdict and **no** crozier-versus-Fern byte comparison. Twenty-four
  rows left this way — twenty-one on
  [route 2](#the-settlement-rule-as-amended), each naming the blocker that stops
  its real witness being registered, and three on route 3, each naming the source
  its search left unanswered. Every one of them stays convertible: a registrable
  witness found later promotes it to `golden` under
  [the classification precedence](#the-category-rules).
- **By a measurement over goldens already registered.** Two rows needed neither a
  new document nor a probe. `templated-path-segment` and
  `several-path-template-variables` rested on the census being unable to read a
  Paths Object key at all; two predicate selectors closed that, and the registered
  corpus turned out to have been declaring both shapes all along — 93
  golden-bearing sources declare a templated key and 53 a key carrying more than
  one expression. Both are `golden`, on goldens that were already committed. What
  moved was the instrument, not the corpus, which is why this route settles a row
  with parity evidence and costs no document at all.

**Pinned from this backlog:** [`header-allow-empty-value`](openapi-surface/parameters.md)
is pinned by corpus row 94, `ndw-accessibility-map`; its two Header Objects declare
the field and its Fern 5.20.0 golden byte-matches with no exclusions.

The two highest-ranked entries stayed for two rounds, and the issue #188 witness
search
[the `parameters` region records](openapi-surface/parameters.md#witness-search-issue-188)
replaced the earlier GitHub-only look with a seven-source sweep and a measured
reason for each. `header-allow-reserved` reads `witness-blocked`: exactly two
declaring files exist anywhere the sweep reaches and both are synthetic, because
`allowReserved` is defined for query parameters and a Header Object carrying it
is a reader test. `header-deprecated` reads `fern-rejected`: a real API's own
description declares it — the openEHR EHR API — and Fern refuses that document,
as it refuses the only other real declarer. **Both have since been settled by
probe** and are `limitations` now, on the routes
[the settlement rule](#the-settlement-rule-as-amended) gives each — route 3 for
the first, route 2 for the second — with
[the round below](#the-six-rows-a-round-of-probes-settled) recording what was
measured. `header-content` was the third and left this backlog on corpus row 121.

[`content-encoding`](openapi-surface/schemas.md) is pinned by corpus row 95,
`marimo`; its `Base64String` component declares `contentEncoding: base64` and
its Fern 5.20.0 golden byte-matches with no exclusions.

[`format-duration`](openapi-surface/schemas.md) is pinned by corpus row 97,
`mosip-esignet`, registered as one of the three `http-dpop` witnesses; two of its
schemas declare `format: duration` and its Fern 5.20.0 golden byte-matches with
no exclusions.

Six `schemas` rows left this backlog together, on the three witnesses the issue
#188 search recorded as `witness-found` for them and the change that registered
all three as corpus rows 110, 111 and 112:
[`content-media-type`](openapi-surface/schemas.md),
[`content-schema`](openapi-surface/schemas.md) and
[`exclusive-maximum-numeric`](openapi-surface/schemas.md) on
`osparc-simcore-webserver` (24, 24 and 8 declarations),
[`dependent-required`](openapi-surface/schemas.md) on `helixdb-http-api` (2),
[`dollar-defs`](openapi-surface/schemas.md) on `flowdapt` (7), and
[`property-names`](openapi-surface/schemas.md) on all three of
`volview-backend-contract`, `osparc-simcore-webserver` and `helixdb-http-api`
(7, 30 and 2). Each of the three Fern 5.20.0 goldens byte-matches with no
exclusions, so all six rows are `golden` outright.

[`format-json-pointer`](openapi-surface/schemas.md) left it next, alone, on the
witness the same search recorded as `witness-found` for it and the change that
registered that witness as corpus row 113,
`k8s-container-service-provider`: its `Error.pointer` and `ErrorDetail.pointer`
each annotate a string field with the RFC 6901 format, and its Fern 5.20.0 golden
byte-matches with no exclusions, so the row is `golden` outright.

Six `parameters` rows left this backlog together, on the witnesses the issue #188
search recorded as `witness-found` for them and the change that registered all of
them as corpus rows 114-121. Five went on the witness each row names, registered
as rows 114-118:
[`parameter-style-simple-path-array`](openapi-surface/parameters.md) on
`daniweb-connect` (15 declarations),
[`parameter-style-simple-header-scalar`](openapi-surface/parameters.md) on
`chaingateway-io` (26) — beside corpus row 107's two, which the search's own
conjunction pass had reported as none —
[`parameter-style-form-query-object`](openapi-surface/parameters.md) on
`hubspot-events` (2),
[`parameter-style-deepobject-query-array`](openapi-surface/parameters.md) on
`paloalto-remote-networks` (1) and
[`parameter-style-deepobject-query-scalar`](openapi-surface/parameters.md) on
`openintegrationhub-secret-service` (1). The sixth,
[`header-content`](openapi-surface/parameters.md), went on the VTEX Pricing API,
registered as corpus row 121 — the same document the
`parameter-style-simple-header-scalar` search recorded as an alternate — whose 22
Response Header Objects each carry a media type instead of a `schema`. Every one of
those Fern 5.20.0 goldens byte-matches with no exclusions, so all six rows are
`golden` outright.

[`operation-overrides-path-item-parameter`](openapi-surface/parameters.md) left
next, alone, and it is the one row of this batch that was ranked on a nonzero
`crozier sites` count — `src/openapi.rs`'s `normalize_parameters` override branch,
in the file with the largest blind-spot count of any. The corpus already saw the
shape, but only in `asana.com`, which carries no golden because Fern refuses it —
the search put that cheapest candidate to Fern first and records the refusal:
exit 1 at both stages on 17 errors, re-measured there rather than inherited from
the batch-4 ledger.
The witness the same search recorded is the AWS Import/Export Service
description, registered as corpus row 122 — six paths declaring `Action` and
`Version` through `components.parameters` as a plain `type: string`, each path's
`get` and `post` redeclaring both inline as a single-member enum, 24 collisions
against asana's 3. Fern types the argument as the operation's enum, in the
position the path-level declaration held, and crozier reproduces all 152 files
byte for byte, so the row is `golden` outright.

**Every alternate that search recorded is registered too**, because a witness is
not dropped for being redundant: corpus row 119 (`strapi-rest-api`) is the second
declarer of `parameter-style-deepobject-query-array` beside row 117, and rows 120
(`listennotes`) and 121 (`vtex-pricing`) are the second and third of
`parameter-style-simple-header-scalar` beside row 115. One recorded alternate is
**not** registered and is refused on its own record rather than for redundancy:
Setu is a generated composite the fixture ledger disqualifies. The other, LORIS,
was refused for being `GPL-3.0` when that batch ran, and the widened licence rule
has since admitted and registered it as corpus row 133; see
[the two rows it settled](#the-two-rows-a-widened-licence-rule-settled).

Two `security` rows left this backlog together, on the witnesses the issue #188
search recorded as `witness-found` for them and the change that registered all four
as corpus rows 123-126.
[`oauth2-multiple-flows`](openapi-surface/security.md) went on
`openbanking-brasil-directory` (row 123), whose one `oauth2` scheme declares
`clientCredentials` and `authorizationCode` over **disjoint** scope sets — the
sharpest discriminator that row's precedence question can have — and again on
`discord-com` (row 125), whose three flows differ pairwise.
[`security-optional-requirement-operation`](openapi-surface/security.md) went on
all three witnesses the search recorded: `api-openverse-org` (row 124, 6
declarations), `braintrust-dev` (row 126, 148) and `discord-com` (22). **Every
alternate that search recorded is registered**, because a witness is not dropped
for being redundant; none of the four was refused by Fern, so none took the
`fern-rejected` route. Each of the four Fern 5.20.0 goldens byte-matches — the
four documents cost a run of repairs in `src/` between them, recorded in
[`matching.md`](matching.md) — so both rows are `golden` outright. The
same walk shows `helixdb-http-api` (row 111) already declared the optional
requirement once, which the earlier 107-source measurement predates.

[`parameter-style-pipedelimited-query-scalar`](openapi-surface/parameters.md) was
the one row of that batch that stayed, and it has since left with
[`parameter-style-spacedelimited-query-scalar`](openapi-surface/parameters.md);
see [the licence widening below](#the-two-rows-a-widened-licence-rule-settled).
Its first recorded witness — AlayaCare's Billable Item Management API, CC0-1.0 at
an immutable ref — was put to Fern for registration and met the
*exit-0-and-nothing-happened* refusal
[`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md) names: `fern check`
and the 5.20.0 generate both exit 0 over a document Fern never parsed, and the
tree it wrote is an empty SDK. The document is logged REJECTED there, and the row
still carries that evidence.

[`dollar-comment`](openapi-surface/schemas.md) never reached this backlog: it was
a `PROBE` until the issue #188 search found it a publisher-owned, Apache-2.0
witness, and the change that settled it registered that witness as corpus row 109,
`volview-backend-contract`, whose two `$comment` declarations and byte-matching
Fern 5.20.0 golden make the row `golden` outright.
[`format-relative-json-pointer`](openapi-surface/schemas.md) arrived here from the
other direction: the same search found it a publisher-owned witness Fern accepts
whose licence is proprietary, and a witness blocked on redistribution puts a row
in this backlog rather than the probe one. Under
[the amended rule](#the-settlement-rule-as-amended) a blocked witness also
licenses a probe that settles the row as `limitations`, and this row has now taken
that route — with the other twelve `schemas` rows below.

**The thirteen `schemas` rows of this backlog left it together**, measured rather
than registered. Twelve took [route 2](#the-settlement-rule-as-amended) on their
own searches' `witness-blocked` or `fern-rejected` outcomes —
[`contains`](openapi-surface/schemas.md),
[`dollar-anchor`](openapi-surface/schemas.md),
[`format-idn-email`](openapi-surface/schemas.md),
[`format-idn-hostname`](openapi-surface/schemas.md),
[`format-ipv6`](openapi-surface/schemas.md),
[`format-iri`](openapi-surface/schemas.md),
[`format-iri-reference`](openapi-surface/schemas.md),
[`format-relative-json-pointer`](openapi-surface/schemas.md),
[`max-contains`](openapi-surface/schemas.md),
[`min-contains`](openapi-surface/schemas.md),
[`multiple-of`](openapi-surface/schemas.md) and
[`unevaluated-items`](openapi-surface/schemas.md) — and the thirteenth,
[`dependent-schemas`](openapi-surface/schemas.md), took [route 3](#the-settlement-rule-as-amended),
the open-search probe: its search found no usable witness *and* left SwaggerHub's
unread `openapi-3.0.x` family outstanding, so its record reads
`search-incomplete` and its cell names that source rather than a blocker.
All thirteen are `discards` on the fourteen probe documents
[Round 6](fern-limitations.md#round-6--schemas) measures, and every one of them
stays convertible: a registrable witness found later promotes it to `golden`
under [the classification precedence](#the-category-rules), which is what
`dollar-comment` did as corpus row 109.

**The last three `FIXTURE` rows of this backlog's tail left it together**, on the
witnesses the issue #188 searches recorded as `witness-found` for them and the
change that registered two of those witnesses as corpus rows 127 and 128.
[`media-type-range`](openapi-surface/bodies-media.md) went on `torrentarr` (row
127), whose six `image/*` responses are the corpus's only `type/*` key other than
`*/*`; that row's own cell records which of crozier's seven reads of a media-type
range the witness reaches — the two response-side ones — and which five it does
not, so a row settled on one document does not read as covering handling sites it
never touched. [`duplicate-normalized-paths`](openapi-surface/document-paths.md)
went on the same `torrentarr` (4 collision sites), on `agco-ats` (row 128, 2) and
on `short-io` (row 131, 2), and
[`duplicate-operation-id`](openapi-surface/document-paths.md) on `agco-ats` (22
sites over 11 ids), `svix-webhooks` (row 129, 2) and `webflow-v2` (row 132, 2). Both were `PROBE` while the census could not
compare two values at all, and became `FIXTURE` on a measured zero over the
registered sources; neither was ever a [structural probe](#structural-probes),
because one document declaring the collision generates a golden whose raw-client
methods say what Fern did with it — and each row's record now names that method
set on both sides, which is what makes a method lost to a collision visible
rather than hidden behind an empty diff. **Every alternate those searches
recorded is registered too**, because a witness is not dropped for being
redundant, inconvenient or already covered by another document: `gotson/komga`
(row 130) declares `media-type-range` once against Torrentarr's six,
`jentic`'s short.io redistribution (row 131) declares `duplicate-normalized-paths`
where two registered rows already do, and `svix/svix-webhooks` (row 129) and
`webflow/openapi-spec` (row 132) declare `duplicate-operation-id` twice each
against AGCO's 22. Fern accepted all six, so none took the `fern-rejected` route.
Three of the six reach full byte parity and three are registered with a **measured
residual** — every divergent file named in that corpus's `unmatched`, and for
`webflow-v2` every crozier-only module named beside it — which
[`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md)'s batch 14 records
along with what each residual is. The six goldens between them cost a run of
repairs in `src/`, from a `float`-named enum `visit` parameter to an undeclared
path template expression crozier was interpolating without declaring, recorded in
[`matching.md`](matching.md).

[`reference-summary`](openapi-surface/oas31-extensions.md) (#3) is the one row of
that tail that stayed, and it stayed on the searches' own outcome rather than on
anything this repository could do: `fern-rejected`. Five documents declaring a
non-Schema Reference Object `summary` are known — `lomiafrica/pi-spi-sdk`, two
independently-published Okta documents, the Tailscale API as `jaxxstorm/tscli`
vendors it, and `api-evangelist/barclays`' Rewards Earn profile — and Fern
refuses four of them at the pin the corpus's provenance records while the fifth
carries no redistributable licence. Its region-file cell carries that evidence
with each refusal's error count, so `probe-backlog` works from it.

#### The two rows a widened licence rule settled

The two `parameters` rows this backlog carried on a style the specification
defines for arrays alone, declared over a *scalar* schema, left it together on one
document neither of their own searches could use. Both searches had found the
LORIS Data Query Tool API and recorded it blocked on `GPL-3.0`, outside the
admissible set as it then stood; the rule has since widened
([`corpus-licensing.md`](corpus-licensing.md)), the rescreening
([`licence-rescreening.md`](licence-rescreening.md)) put that document through
Fern at both stages and it passed, and it is registered as corpus row 133.
[`parameter-style-spacedelimited-query-scalar`](openapi-surface/parameters.md)
goes on its two `spaceDelimited` query parameters and
[`parameter-style-pipedelimited-query-scalar`](openapi-surface/parameters.md) on
its four `pipeDelimited` ones, all six on `PATCH /queries/{QueryID}`. Its
Fern 5.20.0 golden byte-matches with no exclusions, so both rows are `golden`
outright — the first of the two on the only witness found anywhere, and the second
beside the Fern-rejected AlayaCare document its own search recorded.

**Every other admitted witness of that rescreening is registered too**, because a
witness is not dropped for being redundant: corpus row 134 (`sftpgo`) is the
corpus's densest `media-type-range` declarer and its second
`operation-overrides-path-item-parameter` source, row 135
(`googleapis-servicebroker`) its fourth `duplicate-normalized-paths` declarer, and
row 136 (`audiobookshelf`) its fourth `media-type-range` one. Each of the four
Fern 5.20.0 goldens byte-matches; between them they cost a run of repairs in
`src/`, recorded in [`matching.md`](matching.md). The rescreening's fifth
registrable candidate, Eclipse Ditto — the only admitted `format-iri-reference`
declarer — is **not** registered: Fern's Python generator refuses it at the CLI
version the corpus's goldens are pinned to, which is why
[`format-iri-reference`](openapi-surface/schemas.md) left this backlog on a
measured probe rather than on a corpus row. Its own cell carries that refusal, and
a document Fern's 5.20.0 generator accepts still promotes it to `golden`.

#### The six rows a round of probes settled

Six rows left this backlog together without a document: five of `parameters` and
one of `oas31-extensions`, each carried through `fern check` and a real
`fern generate` on a locally authored probe and recorded in
[`fern-limitations.md`'s Round 6](fern-limitations.md#round-6--parameters-and-the-31-tail).
Four took [route 2](#the-settlement-rule-as-amended) — `header-deprecated` on
openEHR, `parameter-style-matrix-path-scalar` on appNG,
`parameter-style-simple-path-object` on Pinterest and `reference-summary` on
`lomiafrica/pi-spi-sdk` — each naming Fern's own refusal of a real witness as the
blocker. Two took route 3 — `header-allow-reserved` and
`parameter-style-form-cookie-scalar` — each naming the source its search left
unanswered. **All six are `discards`:** the Header Object's `allowReserved` and
`deprecated` reach no byte, `matrix` on a scalar path parameter and `form` on a
cookie parameter reach none either, `simple` on an object-typed path parameter
reaches none while the object schema it crosses reaches plenty, and a Reference
Object's `summary` sibling reaches none. Every one stays convertible: a
registrable witness found later promotes it to `golden` under
[the classification precedence](#the-category-rules), and each row's own cell
says what such a document would have to be.

The round also generated all twelve documents with crozier and byte-compared them
with Fern under the gate's normalization. That is corroborating evidence beside
the verdicts, counted nowhere here — this document credits registered corpus
goldens rather than probes — and it repaid the run: an object-typed path
parameter, a shape **no** registered source declares, diverged in four files and
[the repair went into `src/`](fern-limitations.md#the-crozier-divergence-this-rounds-parameters-measurement-found)
rather than into a region file.

#### The thirteen rows the `schemas` round of probes settled

The thirteen `schemas` rows [named above](#the-ranked-fixture-backlog) left this
backlog the same way and in the same round, on the fourteen probe documents
[Round 6](fern-limitations.md#round-6--schemas) records — twelve on
[route 2](#the-settlement-rule-as-amended) and `dependent-schemas` on route 3.
That round generated every cleanly-generating probe with crozier too and
byte-compared it with Fern under the gate's normalization, finding no differing
file; like the round above, that is corroborating evidence counted nowhere here.

#### The eleven rows the node-local predicates added

**The backlog was exhausted and is not any more, and nothing about the corpus
moved.** The eleven rows below are eleven branches of `src/ir.rs` that this
change named for the first time — the `anyOf` spelling of an arm whose `oneOf`
spelling the corpus declares, the closed-object element of an arm whose
struct element it declares, the one-member composition whose two-member sibling
it declares. Each was reachable by a real document and reached by no golden
before this change and after it alike; what changed is that each now has a
selector, so the census could be *asked*, and the answer came back zero across
all 169 registered sources. That is the mechanism
[the conjunction pass predicted](#the-six-blind-regions-of-srcirrs-case-by-case)
for a future `gap` — *extend the grammar to express one and the census can report
the new selector absent* — happening for the first time.

**They rank as one block**, because their four criteria are identical: each names
one place in `src/ir.rs`, that file's blind-spot count is one number, each moves
the types module and the census reports no witness for any of them. So the total
order among the eleven is criterion 5, the key, and they are alphabetical in the
table below.
Every one is `FIXTURE` rather than `PROBE`: the corpus already declares the
sibling spelling of each, so a screened real-world document plausibly declares
this one, and no structural measurement is involved.

#### The two rows the pointer-form predicates added

**Two more branches, and five that the same pass found the corpus had been
declaring all along.** The pointer-form predicate family named the seven branches
`ref_to_class` and `resolve_schema_pointer` decide from a `$ref` value's own
segment structure, or from that value's head measured against the document's own
`components.schemas` keys. Five of the seven came back `golden`: 29 cross-document
pointers in `helios-verifiable-api` and `ndw-accessibility-map`, 50 same-document
pointers outside `components.schemas` in `conjur.local`, `eos.local`,
`eos.local-extra-fields-forbid` and `dnd5eapi.co`, and the three nesting segments
`dnd5eapi.co` and `openbanking-brasil-directory` write. Two came back zero across
all 169 registered sources and are the rows below — `ref-pointer-unnamed-segment`
and `ref-pointer-undeclared-component-head`, both `FIXTURE`, both in
[`schemas`](openapi-surface/schemas.md).

**They do not rank as one block with the eleven, and one of them is why criterion
1 decides an order here again.** `ref-pointer-undeclared-component-head` names one
place in `src/ir.rs` and ties with the eleven on all four criteria, so it falls
into their alphabetical run at rank 12. `ref-pointer-unnamed-segment` names
**two** — the residual arm of each function, which read the same pointer positions
— so criterion 1 puts it last, and it is the first row since the backlog refilled
that the rubric separates from the block on anything but its key.

**The plan this pass ran under expected the cross-document branch to be
permanently `UNREACHABLE`, and the measurement contradicted it.** Registration is
by direct single-document spec URL, and two screened candidates
(`checkmarx-kics-compare-payload`, `alayacare-rating`) show what an unresolved
external `$ref` does to Fern — but those are measurements of Fern on those two
documents, not proof that no admissible document reaches the branch, and two
registered sources carrying committed goldens do reach it. crozier resolves such a
reference by fetching the named document
([`matching.md`](matching.md#cross-document-ref-resolution-issue-77)), so the
branch is reachable by construction. The row is `golden` on the census, and
[`document-paths.md`'s snapshot reconciliation](openapi-surface/document-paths.md#snapshot-reconciliation)
is what re-measures the selector over the fetched `link-ok` corpus afterwards.
**One existing cell reads against this and is left as it stands**: the
`src/refs.rs` verdict in [the join table below](#the-ranked-list-against-golden-blind-spots)
says *"the corpus is single-document by construction"*, and the census now reports
two registered sources writing a cross-document schema `$ref`. That cell was taken
by an earlier measurement and keeps what that measurement established; the
discrepancy is recorded here rather than silently repaired, and re-measuring
`src/refs.rs`'s golden reach is a `just fixtures-coverage` run this change did not
take.

**What did not move.** These predicates read a `$ref` at the node that writes it,
which the census already visited, so no count rule changed, no existing row's
category, settlement or evidence-cell count moved, and no snapshot digest was
re-pinned.

**All 22 `FIXTURE` gaps remain
across the six regions: the gate recomputes that total off the region files
themselves. The rubric and its
four criteria are how they are ordered, and a row is ranked by [the ranking
rubric](#the-ranking-rubric) — crozier sites ascending, then blind-spot reach
descending, then artifact breadth descending, then witness supply descending,
then key. Each row publishes the measured value of all four, so the order can be
checked rather than trusted.

- **Criterion 1**, `crozier sites`: the integer in the row's own `crozier sites`
  cell, re-measured against `src/`.
- **Criterion 2**, blind-spot reach: the `golden blind spots` count
  `just fixtures-coverage` prints for each `src/` file that cell names, summed
  when it names more than one. A `none` cell scores **0**, as the rubric says.
- **Criterion 3**, artifact breadth: a reading, made here and stated once. The
  region files name the artifacts at risk in prose and publish no count, so this
  column normalizes that prose over the rubric's six kinds — `types/`,
  `client.py`, `raw_client.py`, `errors/`, `reference.md`, `core/` — and lists
  the ones it counted beside the number. Re-read the row's `why bytes could move`
  cell after rewording it.
- **Criterion 4**, witness supply: registered sources the census reports
  declaring the shape, read off the row's own `evidence` cell. A `FIXTURE` gap
  can only score above zero here from a source with no committed golden, which
  is what makes it a gap — 21 of the 22 score zero here, no registered source
  declaring any of them at all. **The one that does not is the first row since
  `parameter-style-matrix-path-scalar` to score above zero**, and it scores 2:
  `annotated-ref-target-composed` is declared by `box.com` (34 sites) and
  `asana.com` (2), both screened-and-dropped documents Fern's own check refuses,
  so neither can carry a golden. That is what criterion 4 is for — a gap with
  witnesses already in the corpus is nearer settling than one with none — and it
  is why that row ranks first.

**The median blind-spot count of this list is 235** — every entry names
`src/ir.rs` and nothing else, and 0 of the 22 entries name no `src/` file at all,
which is the mirror image of the list this one replaced. 0 of the 22 ranked
entries reach no blind region, so criterion 2 separates nothing; criterion 4
separates the first row from the rest and criterion 1 the last row from the rest,
and among the twenty between them criterion 5 decides.

| # | key | region | 1. crozier sites | 2. blind spots | 3. artifacts | 4. witnesses |
|---|---|---|---|---|---|---|
| 1 | [`annotated-ref-target-composed`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **2** |
| 2 | [`annotated-ref-target-closed-object`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 3 | [`annotated-ref-target-oneof`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 4 | [`annotated-ref-target-string-const`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 5 | [`anyof-array-variant-anyof-nullable-item`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 6 | [`anyof-array-variant-closed-object-item`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 7 | [`anyof-array-variant-oneof-nullable-item`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 8 | [`anyof-array-variant-struct-item`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 9 | [`anyof-sole-member`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 10 | [`array-item-inheritance-union`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 11 | [`array-item-pointer-walk-anyof`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 12 | [`array-item-pointer-walk-oneof`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 13 | [`oneof-array-variant-annotated-ref-item`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 14 | [`oneof-array-variant-anyof-discriminated-union-item`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 15 | [`oneof-array-variant-anyof-item`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 16 | [`oneof-array-variant-anyof-nullable-item`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 17 | [`oneof-array-variant-closed-object-item`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 18 | [`property-sole-anyof-closed-object-member`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 19 | [`property-sole-anyof-struct-member`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 20 | [`property-sole-oneof-closed-object-member`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 21 | [`ref-pointer-undeclared-component-head`](openapi-surface/schemas.md) | `schemas` | **1** (`src/ir.rs` 1) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |
| 22 | [`ref-pointer-unnamed-segment`](openapi-surface/schemas.md) | `schemas` | **2** (`src/ir.rs` 2) | **235** (`src/ir.rs` 235) | **1** (types/) | **0** |

### The ranked list against `golden blind spots`

[`tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md#where-the-goldens-are-blind--just-fixtures-coverage)
calls the `golden blind spots` block "the fixture backlog", and it is — the same
backlog as the table above, expressed per `src/` file instead of per feature. The
two are joined below, in the report's own columns: **printed** is the count
`just fixtures-coverage` prints for the file and the one criterion 2 ranks on,
and **by tier** is the breakdown it prints beside it. Printed sums the two
non-golden tiers, so a region both tiers reach counts twice — the report's own
`total 1472 region(s) across 12 file(s)` line is the de-duplicated union, and the
functions named in each verdict are counted from that union.

| `src/` file | printed | by tier | ranked gaps pointing at it | verdict |
|---|---:|---:|---|---|
| `src/settings.rs` | 864 | all-e2e 434, non-e2e 430 | none | **Neither.** `explain` 148, `resolve` 44, `merge` 37, `merge_generator` 28, `load` 21, `read_config` 20: the CLI > env > `crozier.yml` layering behind `crozier config`. No OpenAPI shape reaches it and no Fern golden can — Fern reads a different config format — so neither a corpus row nor a Fern probe is the instrument. The journeys are, and they already reach 434 of the 448. |
| `src/emit.rs` | 437 | all-e2e 137, non-e2e 300 | none | **A shape the walk missed, and now the sharpest measured price of settling a row by probe.** This file is where the block moved most since these cells were last taken — 175 printed to 437 — and the largest new block is one change's: the object-typed path parameter [Round 6](fern-limitations.md#round-6--parameters-and-the-31-tail) found crozier diverging on and repaired. `path_object_value` 39, `without_recording` 31, `path_object_required_fields` 26, `path_field_render` 19 and `path_object_documented` 10 are 125 of this file's 312-region union, and `build_example_inner` rose 7 to 19 beside them. The shape driving all of it is one **no registered source declares**, so no committed golden can reach a line of it: a probe settles a row's category and buys no byte-comparison evidence, and this is what that costs, in regions rather than in argument. `append_request_call_args` 10 — the function the one ranked gap that ever pointed here, `media-type-range`, named — was not among the blind regions when that row was ranked; corpus row 127 settled the row `golden` and the function is blind now. The rest is example rendering, as before: `example_matches_type` 24, `header_first_query_example` 16, `example_is_object` 14, `raw_type_str_ctx` 13, `value_from_example` 10, `named_value_inner` 10, `flat` 9. `type_serializes_as` 8 a committed golden reaches now, as the streaming docstrings `client_stream_docstring` 11 + `raw_stream_docstring` 10 already did. Every `example`/`examples` field is classified `golden`, but the walk enumerates the *field*; those branches switch on the JSON value *kind* an example holds, and example values are not in the grammar's closed list of valued selectors, so no `gap` row could have named them. |
| `src/cli.rs` | 292 | all-e2e 133, non-e2e 159 | none | **Neither**, as `src/settings.rs`: `do_config` 60, `run` 43, `do_init` 26, `do_generate` 12 are the command surface, not document behaviour. |
| `src/ir.rs` | 235 | all-e2e 6, non-e2e 229 | 22 (all of them: the eleven the node-local predicate family named, the two the pointer-form family did, the five the annotated-`$ref` pass did, the two the discriminated-union pass did, and the two the pointer-walk pass did) | **Still wholly unreached, and joined to a ranked gap again — twenty-two of them.** The old verdict opened *"agrees on the file, misses the shapes"*, then became *"no longer joined to a ranked gap at all"* when the backlog emptied. Both halves are answered now, and by the same change. The agreement is back: twenty-two ranked `FIXTURE` rows point here, every one of them a branch of this file's six blind functions that no golden-bearing registered source declares — [the eleven the node-local predicates added](#the-eleven-rows-the-node-local-predicates-added), [the two the pointer-form ones did](#the-two-rows-the-pointer-form-predicates-added), [the five the annotated-`$ref` pass did](#the-five-rows-the-annotated-ref-pass-added), [the two the discriminated-union pass did](#the-two-rows-the-discriminated-union-pass-added), and [the two the pointer-walk pass did](#the-two-rows-the-pointer-walk-pass-added). `resolve_schema_pointer` 25 is the second-largest blind block in this file and the one the pointer-form and pointer-walk passes read between them: five of the seven branches the first named came back `golden`, three of the five the second named did, and the function's last enumeration hole is closed — so the corpus had been sending documents down most of them all along. The other half is unchanged and is the answer to *are this file's regions still unreached?* — **yes, all 235 of them**, which is the count these cells carried before the conjunction pass and the count the refreshed run prints. The blind regions are type-lowering conjunctions: `hoist_union_variant` 43, `resolve_schema_pointer` 25, `nested_array_element` 23, `prop_type_ref` 22, `variant_ref` 21, `field_type_ref` 20, `path_group` 15, `hoist_array_item_type` 13, `error_class_name` 8 — six of them the six this file's [case analysis](#the-six-blind-regions-of-srcirrs-case-by-case) derives its selectors from, whose [before-and-after counts](#what-the-conjunction-pass-moved-in-those-six-regions) that section publishes. Each driving field — `$ref`, `items`, `oneOf`, `properties` — is `golden` on its own, and this verdict used to go on: *"it is their combinations that no golden reaches."* **That was a statement about the instrument, and the measurement contradicts it in one direction and confirms it in another.** The nine conjunctions the first pass declared all came back `golden`. The thirty-nine selectors the second pass declared did not: twenty-eight are `golden` and eleven are `gap`, so the corpus is blind to some of these combinations after all, and it took a finer instrument to say which. The `schemas` region carries thirty-six of the thirty-nine rows and `document-paths` the three `path_group` ones. What stays true of this file is the *branch* reading: a golden pinning a shape pins the bytes for the shapes its own document sends down the arm, not the arm's whole behaviour, and the fifteen cases of these six functions that no selector kind can express are still unmeasured. Two regions built bespoke conjunction passes for exactly this reason (`parameters`' style × `in` × schema matrix, `schemas`' variant scan); the third is now the census's own. |
| `src/openapi.rs` | 218 | all-e2e 84, non-e2e 134 | none | **Accounts for what is left, and no ranked gap points here any more.** The four that did — `http-hoba`, `http-oauth`, `http-scram-sha-1` and `http-scram-sha-256`, one `#[serde(other)]` scheme fallback arm and four IANA scheme members collapsing through it — are `limitations` since [Round 6](fern-limitations.md#round-6--security) measured Fern on all four, and the fifth ranked row this file ever carried, `securityscheme-ref`, is `limitations` on the same round; the `$ref` position it named is `normalize_security_scheme_refs` now, and it is reached by a probe rather than by a golden. `normalize_parameters` was a sixth until corpus row 122 settled `operation-overrides-path-item-parameter` `golden` and it left the ranked list, and the `operation_id` field declaration was a sixth until corpus row 128 settled `duplicate-operation-id` the same way; neither is blind at all now. The largest block, `filter_by_audience` 47 + `audiences` 8, belongs to `audience-dual-header-policy`, classified `golden`: golden-classified is not golden-*exhausted*, since the two audience goldens declare 8 sites between them and leave the rest of the branch space to unit tests. `load` 26 + `expecting` 5 + `de_composition` 5 + the four `visit_*` arms 12 between them are malformed-document deserialization paths the corpus excludes by taking only documents Fern generates. `filter_ignored` 13 is the walk's `x-fern-or-crozier-ignore` — now `golden`, on corpus row 108's four `x-fern-ignore` operations, though golden-classified is not golden-*exhausted*: one witness reaches the Operation-Object arm and leaves the schema arm and the `x-crozier-*` precedence to unit tests. **This file is where the corpus moved most.** `collect_schema_refs` 46, `expand_schema_closure` 32, `operation_schema_seed` 24, `visit_seq` 7 and `normalize_parameters` 3 were all blind two measurements ago and are reached by a committed golden now, and `filter_ignored` fell from 72; that is the whole of the file's 511 → 184. **The 184 has since risen to 218, and the rise is a probe's.** `normalize_security_scheme_refs` 18 is the `$ref` position `securityscheme-ref` named, written when [Round 6](fern-limitations.md#round-6--security) settled that row by probe — code a measurement drove into `src/` that no committed golden reaches, which is what `src/emit.rs` above now shows at four times the size. |
| `src/refs.rs` | 74 | all-e2e 17, non-e2e 57 | none | **Only a probe can settle it.** `resolve_reference` 16, `document` 10, `pointer` 9, `error` 7, `curl_fetch` 7 are the cross-document `$ref` path. The corpus is single-document by construction ([`matching.md`](matching.md#cross-document-ref-resolution-issue-77)), and the ledger's `relative-file-ref` row is already `discards + pipeline` — its own note being that crozier's fixture pipeline cannot register the tree that would make the reference resolve. No corpus row is in reach. |
| `src/schema.rs` | 46 | all-e2e 23, non-e2e 23 | none | **Neither.** `build` 20 emits crozier's own config JSON Schema. |
| `src/lib.rs` | 33 | all-e2e 1, non-e2e 32 | none | **Neither.** `render_files` 29 is the filesystem write path. |
| `src/config.rs` | 31 | all-e2e 13, non-e2e 18 | none | **Neither.** `default_package_name` 10 and `new` 8 are generator-config defaults. |
| `src/naming.rs` | 31 | all-e2e 8, non-e2e 23 | none | **A shape the walk missed, and the half of it that is now enumerated.** `digit_word` 10, `enum_words` 7, `numeric_enum_identifier` 2, `finalize_enum_ident` 2, `sanitize_identifier` 1 are driven by OpenAPI *names* — schema names, enum member spellings — which the grammar excludes as map keys that are names. The schema-name half is no longer unreachable: `components.schemas:normalized-collision` is a predicate selector over exactly those keys, and it is what made `normalization-collision` enumerable above. What still has no selector is the enum-member spellings, which is where four of these five regions sit — a predicate over `schema.enum` members would reach them, and none is declared. |
| `src/pyfmt.rs` | 24 | all-e2e 0, non-e2e 24 | none | **Neither.** `format_source` 24 is the `ruff format` shell-out and its failure paths. |
| `src/main.rs` | 6 | all-e2e 6, non-e2e 0 | none | **Neither.** The binary entry point; `just test-fixtures-coverage` asserts it is reachable at all. |

**Where the two backlogs agree.** At one file, `src/ir.rs`, and every ranked row
is there. That agreement had lapsed — the ranked backlog was empty, so no `src/`
file was named by both, `src/ir.rs` having been the last until
[Round 6](fern-limitations.md#round-6--parameters-and-the-31-tail)
settled `parameter-style-form-cookie-scalar`; `emit.rs` stopped being one when
corpus row 127 settled `media-type-range`, and `openapi.rs` when
[Round 6](fern-limitations.md#round-6--security) settled the five `security`
rows that pointed at it as `limitations`. It is back for a reason worth stating:
the thirteen rows that restored it were read off this file's own blind functions,
so the join is not a coincidence of two independent measurements agreeing but one
measurement finding what the other pointed at.
Ranking on criterion 2 therefore does not fight the repository's own
measurement and does not refine it either, since every ranked row scores the same
235: the order among them falls through to criterion 1, which separates only the
one row naming two places, and then to criterion 5. **The order of size at
the top has moved twice over** — it was
`openapi.rs` 511 > `ir.rs` 201, then `ir.rs` 235 > `openapi.rs` 184, and the
refreshed run makes it `emit.rs` 437 > `ir.rs` 235 > `openapi.rs` 218, on a rise
in `emit.rs` no corpus row caused. None of it changes a ranked row, every one of
which names `ir.rs` and nothing else.

**Where they do not, and the reading that has to change with them.** No ranked
gap points at eleven of the twelve: one
(`src/refs.rs`) is a region only a probe can settle, two (`src/naming.rs`,
`src/emit.rs`) are shapes the walk missed, one (`src/openapi.rs`) is a region
probes have now settled, and the remaining seven are outside the
walk's subject entirely — they carry no OpenAPI-derived code, so neither a
fixture nor a probe is their instrument. The two largest of the twelve,
`src/settings.rs` and `src/emit.rs`, together 1,301 of the block's 2,291 printed
regions — more than half of it — and **the pair no longer makes one point.**
`src/settings.rs` holds no OpenAPI-derived code at all, so no fixture and no
probe could ever shorten it; `src/emit.rs` holds nothing but, and the block it
grew is a shape a *probe* measured and no golden declares. So a reader taking
this block at face value as "the fixture backlog" mis-prioritises in two
different directions now: half of the top is work the corpus cannot do, and the
other half is work the corpus was never asked to do, because a probe settled the
row that drove it.

### The six blind regions of `src/ir.rs`, case by case

The join table's `src/ir.rs` verdict names six functions the goldens never reach
and says why the walk could not name them: *"it is their combinations that no
golden reaches, and the census emits one selector per field and none per
conjunction."* It now emits one per conjunction, and this is the derivation —
every branch of each of those six functions a source document can select, under
[the enumeration rule](#the-selector-grammar), quoting the function and the case
it distinguishes.

**Every case below is in exactly one of two states.** It carries exactly one
selector the census declares — a conjunction, or, where the arm reads one Paths
Object key or one `$ref` value and opens no schema, a predicate — and only where
that selector is
*exact*, counting the nodes the branch is selected by and no others. Otherwise it
is recorded as one of three enumeration holes naming the property no selector kind
can express and what closing it would take — the way `normalization-collision` was
recorded before `components.schemas:normalized-collision` existed. No case is in
neither, and none is in both.

A case number carrying a letter is one arm read at the grain the selectors need.
Two things put a letter on a row. A branch reached through `x.or(y)` is two cases
under [the enumeration rule](#the-selector-grammar), so the `oneOf` and `anyOf`
spellings of one arm are two rows; and where an arm's condition is a *disjunction*
— `is_inline_struct` is four conditions joined by `||`, and this table already
split it into separate cases where `nested_array_element` reads it — each disjunct
is its own row, because a conjunction selector cannot express a disjunction and a
selector naming one disjunct would be narrower than the whole arm.

| hole | what no selector kind can express | what closing it would take |
|---|---|---|
| **H-residual** | a function's residual arm is selected by the *absence* of every case above it | a negation operator over a group's members, deliberately absent: a complement is not a shape a document declares |
| **H-negated-value** | that a value was *not* written — `is_inline_struct`'s `!declares_scalar_type(schema)`, which excludes a schema whose `type` is `string`, `number`, `integer` or `boolean`; the same helper's `additional_properties.is_none()`, which is what makes a declared-but-empty `properties: {}` an inline struct; `sole_inline_all_of`'s nine sibling-absence tests; and `is_bare_object`'s four | the same negation operator H-residual names; every positive spelling is a selector the grammar already has, and only their complement is missing |
| **H-example-value** | the JSON *kind and content* of an `example` or `examples` value — `hoist_union_variant`'s bare-object arm needs `schema_example(variant)` to yield an object that `example_is_schema_definition` does not reject, so a `type: object` variant beside a scalar example, an empty `examples`, or an object whose every value is itself a schema declaration is counted and takes `base_type_ref` | a valued selector over an example's JSON kind (`schema.example=object`) *and* a predicate `schema.example:schema-shaped` for the rejection half — and, beyond both, the negation operator H-negated-value names, because the arm is `is_bare_object` beside that pair and a map schema carrying a concrete example is a coherent document the pair alone counts and `hoist_union_variant` sends to `base_type_ref` |

Every one of the three turns on something the node in front of the walk does not
say — the JSON kind or content of a value, a comparison across the document, or
the *absence* of a declaration — which is what separates them from the node-local
predicate family
[the grammar declares](#the-selector-grammar). Declaring one of them is a change
to the predicate list or to the operators, not to the conjunction list this
section derives; each hole says which, so the next node reads the work off the row
rather than rediscovering it.

#### The five rows the annotated-`$ref` pass added

**Twelve more branches named, seven of them already `golden`.** The
annotated-`$ref` pass declared two predicates and ten conjunctions over one path:
an `allOf` holding exactly one `$ref` beside members that add nothing but a
description — the 3.0 idiom for documenting a shared schema — and the arms of
`prop_type_ref` and `hoist_union_variant` that decide what such a property becomes
in Python. Seven came back `golden`, including the gate itself
(`schema.properties>schema.allOf:annotated-ref`, 351 sites across six sources) and
the two arms that hoist an enum class or a model out of the target. The other five
are the rows below, all `FIXTURE`, all in
[`schemas`](openapi-surface/schemas.md).

**It is the first pass whose gaps are not all measured zeroes**, and the
difference matters for how a reader sizes them. Four of the five are the familiar
shape — the branch is reachable, the corpus has never written it, and the census
reports zero across all 169 sources. `annotated-ref-target-composed` is not:
`box.com` declares it 34 times and `asana.com` twice, and **both are
screened-and-dropped documents Fern's own check refuses** (25 and 17 fatal
diagnostics). The classification precedence reads on the golden rather than on the
declaration, so the row is a `gap` — nothing compares crozier's bytes to Fern's
over that branch — but what it is waiting for is a *redistributable document Fern
accepts*, not a document that declares the shape. That is the first time criterion
4 has separated a row in this list since `parameter-style-matrix-path-scalar`, and
it is why that row ranks first.

**One case of `prop_type_ref` did not earn a selector, and the row says so.** The
plan this pass ran under named four branches inside the resolution gate and
expected an exact selector for each. Three of them split cleanly by disjunct.
The fourth, case 5's closing `full_type_ref_resolved`, is the block's *residual*
arm — selected by the absence of the three above it, reachable by a
`type: string` target, a bare `{}`, an open map, a bare `type: object` and a
`{format: date}` alike, with no positive property common to any two of them. Every
candidate selector for it is narrower than the arm, which
[the exactness rule](#the-selector-grammar) disqualifies as firmly as a broader
one. **The measurement contradicted the plan's premise**, so the case is recorded
as **H-residual**, the hole kind three other cases of the same two tables already
carry, and it names the negation operator as what would close it. Both
`H-annotated-ref` and `H-ref-target` leave the hole table with no case recorded
under either.

**What did not move.** No existing row's category, settlement or evidence-cell
count changed, and no count rule did: `~>` was landed by the change before this
one and is used here for the first time, which adds selectors without moving what
any existing selector counts.

#### The two rows the discriminated-union pass added

**Twelve more branches named, ten of them already `golden`.** The
discriminated-union pass declared three predicates and nine conjunctions over one
condition: `discriminated_union` of `src/ir.rs` returning `Some`, which is the one
place in the generator that reads a union's members *against each other*. The
three arms that call it — `nested_array_element`'s case 2, `hoist_union_variant`'s
case 4 and `prop_type_ref`'s case 13 — are one condition reached from three
places, and they were the whole of the enumeration hole **H-discriminant-value**,
which this pass closes. The hole table is down to four kinds, and no case is
recorded under the fifth.

**The condition is much wider than a `discriminator` beside a `oneOf`, and the
corpus is what shows the difference matters.** `discriminated_union` accepts a
union with no `discriminator` written at all, provided every member tags itself
distinctly on one shared property, and it *refuses* a `discriminator` written
beside an `anyOf` with no `oneOf` — the one place in these six functions the two
union heads are not interchangeable, because Fern applies an explicit
discriminator to `oneOf` alone. A predicate reading only "a `discriminator` beside
a `oneOf`" would have been broader than all three arms and would have put parity
evidence under documents the generator demonstrably sends elsewhere. The reading
is a port of the function rather than a resemblance to it, and
`tests/surface_census_test.py` drives the real census over four documents alike in
every other respect — the canonical written union, the same union one of whose
members carries no discriminable value, a `discriminator` beside an `anyOf`, and a
union with no `discriminator` whose members tag themselves — and asserts that the
selectors answer differently for three of them.

**Ten of the twelve came back `golden`, and two are the rows below.** `letta`
alone declares the `oneOf` reading 76 times, and sixteen registered sources
carrying committed goldens declare it between them; the inheritance spelling is
`ndw-accessibility-map` (5) and `adyen-capital` (1). The two that came back `gap`
are both product cells of shapes the corpus writes separately:

- **[`array-item-inheritance-union`](openapi-surface/schemas.md)** — an
  inheritance-style base written *inline* as an array element. The corpus declares
  inheritance-style bases as named components and inline array elements
  everywhere, and never the two together.
- **[`oneof-array-variant-anyof-discriminated-union-item`](openapi-surface/schemas.md)** —
  an array variant under a `oneOf` head whose element is an `anyOf`-headed union.
  Registered golden-bearing sources write the same element under an `anyOf` head
  (`letta` 3, `truefoundry-trueforge` 1) and write the `oneOf`-headed element under
  a `oneOf` head (`letta` 3); only this corner of the product is unwritten.

**One thing the case analysis said about a neighbouring row turned out to be
wrong, and the row now says what the generator does.** `nested_array_element`'s
case 7 claimed an empty `oneOf: []` selects the hoisted-alias arm, on the reading
that its gate is `Option::is_some`. It does reach that gate, but case 2 runs
first and claims it: `inferred_union_discriminant_property` finds `type`
inferable vacuously over no members at all, so `discriminated_union` returns
`Some` with none and the generator coins a `Union({Ctx}ItemItem)` rather than an
alias. The finding is the instrument's own — the predicate counts the node, which
made the disagreement visible — and it is settled by executing the generator over
`du-nested-empty-oneof` and observing which arm ran, not by reading either.

**One reading in the case analysis is the selector's rather than the code's, and
case 2c says so.** `inheritance_discriminated_union` lets a mapping entry naming
the union's *own* coined class name through without resolving it, and that name is
coined from the call site rather than declared by the document, so no census can
decide it; the predicate requires every entry to resolve instead. The two disagree
only on a mapping naming a component this document does not declare whose class
name is nonetheless the one the caller would coin — a document contradicting
itself, which is the reading
[the exactness rule](#the-selector-grammar) already excuses. Nothing else in these
three tables departs from what `src/ir.rs` tests.

**What did not move.** No existing row's category, settlement or evidence-cell
count changed, and no count rule did: the three predicates and nine conjunctions
name positions the walk did not name before, and `>`, `&`, `~>` and every selector
kind keep the meaning they had.

#### The two rows the pointer-walk pass added

**Five more branches named, three of them already `golden`, and the last
enumeration hole of `resolve_schema_pointer` closed.** The pointer-walk pass
declared five conjunctions over the one function in these six regions that
resolves a reference by *walking its segments structurally through the document*
rather than by looking a name up, and five member-only readings for them to carry.
Its five `match` arms were the whole of the enumeration hole
**H-pointer-nesting**, which this pass closes; the hole table is down to three
kinds, and no case is recorded under the fourth.

**Each of the five is gated, and that is what makes it exact.**
`resolve_schema_pointer` has exactly one production call site — `field_type_ref`,
on an array-typed property whose `items` is a reference, behind a
`starts_with("#/components/schemas/")` guard — so every selector here carries that
gate as its leftmost members. The reading of the arm itself is declared as a
[member-only reading](#the-member-only-readings) rather than a predicate,
*because* a standalone selector over it would count nodes the generator never
walks: `openbanking-brasil-directory` writes
`#/components/schemas/ClientCreationResponse/properties/client_id` on a path
parameter's schema, which selects no case of this function's table at all. An
earlier draft of this pass declared those five as predicates and gave them five
rows of their own; they were withdrawn, with the rows, for exactly that miscount,
and `tests/surface_census_test.py` now drives the real census over the fifteen
documents that used to break it and requires nothing to count them.

**It needed no second descent operator, and that was settled against the arms.**
The plan this pass ran under left the shape open — a predicate family or a
structural descent beside `~>` — and the arms decide it: cases 3 to 7 read nothing
at the resolved target beyond what the walk itself does, so there is no group of
members to evaluate *at* a target and nothing for an operator to descend into.
What each arm reads is one `$ref` value against one document's own
`components.schemas`, which is the document context
[the pointer-form family](#the-two-rows-the-pointer-form-predicates-added)
already put within reach of every node the walk visits. So the five readings sit
in `MEMBER_ONLY_PREDICATES`, reading that context exactly as
`schema.$ref:undeclared-component-head` reads it one segment shallower, and each
is carried by the conjunction that gates it; **`~>` is untouched**: it keeps its meaning,
its count and its depth bound, and every selector already declared with it reports
the same per-source counts it did before this change.

**The two resolutions disagree, and the corpus writes a document that shows it.**
`~>` performs `resolve_ref_from_schemas` — the reference's *last* segment, looked
up, traversing nothing — where these five arms are `resolve_schema_pointer`'s
prefixed walk. `dnd5eapi.co` writes
`#/components/schemas/Monster/allOf/3/properties/actions/items` twice; the walk
reads three segments of it and reaches three of these arms, while `~>` on the same
value would look up a component named `items` and find none. A selector mirroring
the wrong resolution would have counted nothing here and would have counted
`openbanking-brasil-directory`'s path-parameter pointer, which the generator never
walks at all.

**Three of the five came back `golden` and two are the rows below.**
`dnd5eapi.co` declares all three: its `legendary_actions` and `reactions`
properties are arrays whose `items` is
`#/components/schemas/Monster/allOf/3/properties/actions/items`, which the walk
reads an `allOf`, a `properties` and an `items` segment at. Each of the three
conjunctions counts that Schema Object once, because both properties belong to one
node and the count rule is one per node at the leftmost position.
`openbanking-brasil-directory` adds no site to any of them — its pointer is the
ungated one above, and the gate is what excludes it. The `oneOf` and `anyOf` arms
are declared by no registered source, which is the two `gap` rows:
`array-item-pointer-walk-oneof` and `array-item-pointer-walk-anyof`, both
`FIXTURE`, both in [`schemas`](openapi-surface/schemas.md).

**The code has one early `None` the case analysis did not derive, and case 2 now
records it.** After `schemas.get(parts.next()?)?` succeeds, the function reads
`let mut next = Some(parts.next()?);`, so a *bare* `#/components/schemas/Foo`
resolves to nothing even where `Foo` is declared — a third early return that is
neither case 1 nor case 2 nor any arm of the `match`.
`resolve_schema_pointer`'s own unit test already asserted it and this table did
not derive it; it is recorded on case 2's row, with five documents in
`tests/resolving-arm-inputs.json` that drive it through both halves of the
measurement.

**What did not move.** No existing row's category, settlement or evidence-cell
count changed, and no count rule did: the five predicates and five conjunctions
name positions the walk did not name before, and `>`, `&`, `~>`, a field, a valued
and a predicate selector all keep the meaning they had.

#### `resolve_schema_pointer`

Every branch here is selected by the pointer *string* — `match part` reads a
segment of the `$ref` value, never a field of the document — and each arm then
resolves only where the schema at that position declares the field that segment
names, with that index or key. That split is the whole reading of this table:
**the segment is the arm's condition and the resolution is its body**, which is
where `src/ir.rs`'s own `observed_arm!` sites sit and what they record. So case 3
runs over `A/allOf/0` whether or not `A` declares an `allOf`, and over a trailing
`A/allOf` with no index behind it.

**What the five arms of the loop needed was the walk itself, and it is landed.**
The correspondence between a `$ref` value's segments and the nesting they address
is a joint property of a value and the document it points into rather than a
combination of fields at one node, so no conjunction over declared fields names
one: `schema.allOf>schema.properties` would name *one* continuation of the
`"allOf"` arm and leave `allOf/{i}/items`, `allOf/{i}/oneOf/{j}`, a bare
`allOf/{i}` and every deeper form uncounted. The five
`schema.$ref:pointer-walk-reaches=` predicates
[the grammar declares](#the-selector-grammar) make that walk instead — the
prefixed pointer walk, not the last-segment lookup `~>` performs — and answer,
for one reference against one document, which segment spellings the loop read.
A **later** segment is read only where every earlier arm's body resolved, which
is why a predicate over the reference string alone would not do:
`A/items/allOf/0` selects case 3 where `A` writes `items` and selects only case 7
where it does not, and `tests/surface_census_test.py` drives the census over both
documents and over one addressing a position under two arms in sequence.

**Every one of the five carries this function's caller gate**, which is the other
half of what the rows below say. `resolve_schema_pointer` has exactly one
production call site — `field_type_ref`, on an array-typed property whose `items`
is a reference, behind a `starts_with("#/components/schemas/")` guard — so each
selector's three leftmost members are that gate and the predicate is its last.
Without them a row would count a pointer the generator never walks, which
`openbanking-brasil-directory` writes: its
`#/components/schemas/ClientCreationResponse/properties/client_id` sits on a path
parameter's schema, so the predicate counts it and the conjunction does not. The
gate's *positive* conditions are what the members carry; its negations — that the
property is not itself a `$ref`, and that no earlier arm of `field_type_ref`
returned first — are the H-negated-value shape, and every node they leak is one
whose own declaration contradicts itself in the way
[the exactness rule](#the-selector-grammar) already excuses: a `$ref` beside a
sibling `type` and `items`, or an object-only keyword written on an array.

**Three of its arms are decided before any of that**, and the pointer-form
predicate family counts them. Cases 1 and 8 read the string alone, so they are
`ref_to_class`'s cases 1 and 5 under another name and take the same selectors;
case 2 reads the pointer's head against the document's own `components.schemas`
keys, which is the document context the census now carries and the comparison
`components.schemas:normalized-collision` already makes over those same keys.
Case 8 is the one that leans on [the exactness rule](#the-selector-grammar)'s
chain-overlap allowance, and does so visibly: `schema.$ref:unnamed-segment` counts
a pointer whose unknown segment sits behind a segment that did *not* resolve —
`A/allOf/0/zzz` where `A` declares no `allOf` — and that pointer selects case 3,
which is a case of this table carrying a row of its own. It does the same at the
other end: a trailing `properties`, which `ref_to_class` sends to its residual arm
because there is no segment after it to name, this function sends to case 6, where
`parts.next()?` returns `None` inside the arm. What the selector never counts is a
document selecting no case here at all — every pointer it counts carries at least
two segments, so the arity check before case 2 cannot be what stops it, and each
segment either matches an arm or is case 8 — which is the miscount the rule
disqualifies.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1a | `reference.strip_prefix("#/components/schemas/")?` — the reference is not a component-schema pointer; the cross-document spelling, which names another file | `schema.$ref:cross-document` |
| 1b | the same arm, the same-document spelling: a pointer inside this document but outside `components.schemas` | `schema.$ref:same-document-foreign-pointer` |
| 2 | `schemas.get(parts.next()?)?` — the pointer's head names no declared component. **The code has a third early `None` on this entry path that this table does not derive**, and `resolve_schema_pointer`'s own unit test already asserts it: the line after this one is `let mut next = Some(parts.next()?);`, so a *bare* `#/components/schemas/Foo` whose head resolves perfectly well returns `None` before the loop is entered, selecting neither this case nor any arm of the `match`. It is recorded here rather than as a case of its own because it is a third condition on the same entry path as cases 1 and 2 rather than an arm of the loop, and because the observation surface answers per `match` arm and has none to answer for. `tests/resolving-arm-inputs.json`'s five `pw-*-bare-component-pointer` documents drive it: the census counts no walk selector for one and the generator enters no arm | `schema.$ref:undeclared-component-head` |
| 3 | `"allOf" => schema.all_of.as_ref()?.get(parts.next()?.parse::<usize>().ok()?)?` — the walk reads a segment spelled `allOf`, which is the whole of the arm's own condition; whether the schema there declares an `allOf`, and whether the index after it parses and lands in range, is the arm's body | `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=allOf` |
| 4 | `"oneOf" => schema.one_of.as_ref()?.get(…)?` — the same over a segment spelled `oneOf`, which a pointer naming that field reaches identically and a selector naming `allOf` would not count | `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=oneOf` |
| 5 | `"anyOf" => schema.any_of.as_ref()?.get(…)?` — the same over a segment spelled `anyOf` | `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=anyOf` |
| 6 | `"properties" => schema.properties.get(parts.next()?)?` — the walk reads a segment spelled `properties`. The arm consumes the *key* after it, which the count rule excludes as a name, so the selector says the step was reached rather than which property it addressed; a trailing `properties` enters the arm and then fails, where `ref_to_class` sends the same pointer to its residual arm | `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=properties` |
| 7 | `"items" => schema.items.as_deref()?` — the walk reads a segment spelled `items`, which consumes no following segment, so two in a row are two nesting steps at one node | `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=items` |
| 8 | `_ => return None` — a segment none of the five names | `schema.$ref:unnamed-segment` |

#### `nested_array_element`

Its entry gate is `let items = array.items.as_deref()?`, carried as the leftmost
member `schema.items` of every case rather than listed as a case of its own.
Cases 4 to 6b are one arm — `is_inline_struct(items)` — read one disjunct at a
time, which is the grain a conjunction can name: the helper is
`!declares_scalar_type && (properties non-empty || allOf || a declared-but-empty
properties on an object || additionalProperties: false)`, and its scalar-type
guard is what leaves two of the four a hole.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1 | `items.reference.is_none() && items.ty…primary() == Some("array")` — the recursive nested-array descent | `schema.items>schema.type:primary=array` |
| 2a | `self.discriminated_union(&name, &module, items, …)` returning `Some` over an `items` whose union head is `oneOf`, in either the written-`discriminator` spelling or the inferred one | `schema.items>schema.oneOf:discriminated-union` |
| 2b | the same arm over an `items` whose head is `anyOf`, written where no `oneOf` is. Only the *inferred* spelling reaches it: `discriminated_union` refuses a written `discriminator` beside an `anyOf` with no `oneOf` outright, which is the one place in these six functions the two heads are not interchangeable | `schema.items>schema.anyOf:discriminated-union` |
| 2c | the same call over an `items` declaring neither, which `discriminated_union` delegates to `inheritance_discriminated_union` — OpenAPI's other polymorphism spelling, a base object whose `discriminator.mapping` names the subtypes. **The selector reads one thing the code does not test:** the Rust lets a mapping entry naming the union's *own* coined class name through without resolving it, and that name is coined from the call site rather than declared by the document, so the predicate requires every entry to resolve instead. The two disagree only on a mapping naming a component this document does not declare whose class name is nonetheless the one the caller would coin, which is a document contradicting itself | `schema.items>schema.discriminator:inheritance-union` |
| 3 | `if items.reference.is_some() { return None; }` — the arm's own condition is that the field is written, and nothing more | `schema.items>schema.$ref` |
| 4 | `is_inline_struct(items)` → `add_object`, on an `items` whose `properties` are non-empty | `schema.items>schema.properties:non-empty` |
| 5 | the same arm on an `items` declaring `allOf`, which `is_inline_struct` takes only for a schema declaring no scalar `type` | **H-negated-value** |
| 6 | the same arm on an `items` writing `additionalProperties: false`, which `is_object_type` reads as an object however — or whether — the `type` is written | `schema.items>schema.additionalProperties=false` |
| 6b | the same arm on an `items` writing an explicitly empty `properties: {}` beside no `additionalProperties` — `is_inline_struct`'s third disjunct, which the account this table replaces did not derive | **H-negated-value** |
| 7 | `items.one_of.as_ref().or(items.any_of.as_ref())` → the hoisted union alias, `oneOf` spelling; the gate is `Option::is_some`, so an empty `oneOf: []` reaches it. **What the account this row replaces got wrong is which arm an empty one then takes:** case 2 runs first and claims it, because `inferred_union_discriminant_property` finds `type` inferable vacuously over no members at all and `discriminated_union` returns `Some` with none — the generator coins a `Union({Ctx}ItemItem)` for `items: {oneOf: []}` and no alias, which `tests/resolving-arm-inputs.json`'s `du-nested-empty-oneof` drives and `src/ir.rs`'s own observation of the arm confirms. This row's selector still counts the node, which is the chain overlap [the exactness rule](#the-selector-grammar) permits between two listed cases | `schema.items>schema.oneOf` |
| 8 | the same arm, `anyOf` spelling: an `items` declaring only `anyOf` reaches it identically, and an empty `anyOf: []` is claimed by case 2b for the reason case 7 states | `schema.items>schema.anyOf` |
| 9 | the closing `None` | **H-residual** |

#### `hoist_union_variant`

Every caller reaches it through `one_of.as_ref().or(any_of.as_ref())` — the
named-schema, response and request-body hoisters, `prop_type_ref`, and its own
recursion — so a document declaring only `anyOf` selects every case below exactly
as one declaring `oneOf` does, and each case that survives the exactness test is
two. Cases 3 to 7 all sit inside `if variant.ty…primary() == Some("array")` —
case 3 included, which the account this table replaces stated as "cases 4 to 7" —
and that guard is `schema.type:primary=array`, so each of those rows carries it
beside the condition its own row names. Case 3 reads a second `or` inside the
first, because `simple_nullable_member` takes `any_of.or(one_of)` — the opposite
order to every other call site — so its four rows are the product of the two.
What those four rows do **not** spell is the rest of the helper's condition: the
sole non-null member must itself declare no `oneOf` or `anyOf` and must not be a
string enum. Neither is expressible, and neither has to be, because the nodes
they exclude are exactly the nodes cases 4 and 5 claim — the item still declares a
composition, so the gate below fires — which is the chain overlap
[the exactness rule](#the-selector-grammar) permits between two listed cases.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1 | `if let Some(reference) = &variant.reference` — the variant is a Reference Object, `oneOf` head; the first arm, so nothing precedes it | `schema.oneOf>schema.$ref` |
| 2 | the same arm, `anyOf` head | `schema.anyOf>schema.$ref` |
| 3a | `if let Some(member) = simple_nullable_member(item)` — one element member beside `type: null`, typed `List[Optional[…]]`; the item's `anyOf` spelling, which the helper reads first; `oneOf` head | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member` |
| 3b | the same, the item's `oneOf` spelling; `oneOf` head | `schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member` |
| 3c | 3a's item, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member` |
| 3d | 3b's item, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member` |
| 4a | an array variant whose item composes, `hoist_discriminated_union(&item_name, item, …)` returning `Some`; the item's `oneOf` spelling, `oneOf` head. The arm's gate already requires the item to declare a composition, so `discriminated_union`'s inheritance delegation is unreachable from here and the head splits two ways rather than three | `schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf:discriminated-union` |
| 4b | the item's `anyOf` spelling, `oneOf` head | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union` |
| 4c | the item's `oneOf` spelling, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:discriminated-union` |
| 4d | the item's `anyOf` spelling, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union` |
| 5a | the same item falling through to the `TypeDecl::Alias` union over `item.one_of.as_ref().or(item.any_of.as_ref())`; the item's `oneOf` spelling, `oneOf` head | `schema.oneOf>schema.type:primary=array&schema.items>schema.oneOf` |
| 5b | the item's `anyOf` spelling, `oneOf` head | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf` |
| 5c | the item's `oneOf` spelling, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf` |
| 5d | the item's `anyOf` spelling, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf` |
| 6a | `described_all_of_ref(item)` resolving → `hoist_named_copy` of the annotated `$ref`; `oneOf` head. The arm is entered on the resolution, so the selector spells that with `schema.$ref:resolves-to-component` rather than with `~>`: nothing about the target's own fields is read here. **The same continuation `prop_type_ref`'s case 3 carries:** a `hoist_named_copy` returning `None` falls through to case 7 rather than returning, so entering this arm is not the same as taking its product | `schema.oneOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component` |
| 6b | the same arm, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component` |
| 7a | `item.reference.is_none() && is_inline_struct(item)` → `hoist_object`, on an item whose `properties` are non-empty; `oneOf` head | `schema.oneOf>schema.type:primary=array&schema.items>schema.properties:non-empty` |
| 7b | the same, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>schema.properties:non-empty` |
| 7c | the same arm on an item writing `additionalProperties: false`; `oneOf` head | `schema.oneOf>schema.type:primary=array&schema.items>schema.additionalProperties=false` |
| 7d | the same, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>schema.additionalProperties=false` |
| 7e | the same arm on an item declaring `allOf`, either head, which `is_inline_struct` takes only for an item declaring no scalar `type` | **H-negated-value** |
| 7f | the same arm on an item writing an explicitly empty `properties: {}` beside no `additionalProperties`, either head | **H-negated-value** |
| 8a | `is_inline_object(variant)` → `hoist_object` on a variant whose `properties` are non-empty; `oneOf` head. The helper carries no scalar-type guard, so the disjunct is the whole of its own condition | `schema.oneOf>schema.properties:non-empty` |
| 8b | the same, `anyOf` head | `schema.anyOf>schema.properties:non-empty` |
| 9 | the same arm on a variant declaring `allOf` — `is_inline_object` is a disjunction and carries no scalar-type guard, so `all_of.is_some()` is the whole of it; `oneOf` head | `schema.oneOf>schema.allOf` |
| 10 | the same arm, `anyOf` head | `schema.anyOf>schema.allOf` |
| 11 | `is_bare_object(variant) && schema_example(variant).is_some_and(…)` — the arm reads the example's JSON kind and rejects a schema-shaped object, over a helper that is itself four absence tests | **H-example-value** |
| 12 | the closing `base_type_ref(variant)` | **H-residual** |

#### `prop_type_ref`

It is called on each member of `properties`, so `schema.properties` is the
leftmost member of every case. Cases 8a to 8d are `is_inline_struct` read one
disjunct at a time, as in `nested_array_element`; cases 12a to 12f are the same
helper read again, inside the one-member arity its own arm tests.

**Cases 1 to 5 are one path and are read at two grains.** Case 1 is the gate,
which reads the property in front of it and nothing else; cases 2 to 5 sit inside
it *and* inside a resolution the gate does not perform, and each reads a field of
the schema the annotated `$ref` denotes. So case 1's selector stops at the
`schema.allOf:annotated-ref` predicate while every case below it carries the `~>`
descent, whose own resolution is the arm's — a reference that resolves to nothing
takes case 1 and none of 2 to 5. Cases 2 to 4 are then split by disjunct exactly
as cases 8 and 12 are: `string_enum_values` reads an `enum` or a `const`, case 3's
condition is `one_of.is_some() || any_of.is_some()`, and case 4's third clause is
three disjuncts joined by `||`. Where a target satisfies two of the rows below,
both count it and the earlier arm runs — the chain overlap
[the exactness rule](#the-selector-grammar) permits between two listed cases.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1 | the outer `if let (Some(schemas), Some((reference, description))) = (self.schemas, described_all_of_ref(prop_schema))` gate, which the arm-observation surface records on entry — before the resolution below. **The code tests one thing more than the four cases inside this gate state:** it also requires `resolve_ref_from_schemas(schemas, reference)` to return `Some`, and a property whose gate holds over a reference naming no component of this document takes none of cases 2 to 5 at all — it falls through to case 6 and beyond. The surface reports exactly that, case 1 without any of 2 to 5, which is how the disagreement was found, and it is why this row's selector carries no resolution while every row below it does. `self.schemas` is `Some` at every call site that reaches a property | `schema.properties>schema.allOf:annotated-ref` |
| 2a | inside it, `if let Some(values) = string_enum_values(&target)` → a hoisted enum, over a target writing an `enum`, which the helper refuses unless the values are strings | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.enum:string-valued` |
| 2b | the same over a target writing a `const`, the spelling the helper falls back to when no `enum` is written. A target writing both is read by its `enum` alone, exactly as case 7b's selector already reads one, so a target whose `enum` is not string-valued beside a string `const` is counted here and falls to cases 3 to 5 — every one of them a case of this table | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.const:string-valued` |
| 3a | inside it, `if target.one_of.is_some() \|\| target.any_of.is_some()` → `hoist_named_copy`; the `oneOf` disjunct. **The code has one continuation this row does not derive:** `hoist_named_copy` returning `None` — a target whose copy declares nothing — falls through to cases 4 and 5 rather than returning, so entering this arm is not the same as taking its product | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.oneOf` |
| 3b | the same arm's `anyOf` disjunct, which a target declaring only `anyOf` reaches identically | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.anyOf` |
| 4a | inside it, `!is_map(&target) && !is_bare_object(&target) && (…)` → `hoist_object_with_doc`; the `!target.properties.is_empty()` disjunct, which excludes both negated helpers on its own — each of them requires an empty `properties` map | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.properties:non-empty` |
| 4b | the same arm's `target.all_of.is_some()` disjunct. `is_bare_object` is excluded by the `allOf` itself; `is_map` is not, so a target declaring `allOf` beside `type: object` and a schema-valued or `true` `additionalProperties` with no properties is counted here and taken by case 5, which is a case of this table and carries its own row | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.allOf` |
| 4c | the same arm's `is_object_type(&target)` disjunct, on a target closing itself. That is the whole of what the disjunct adds over 4a and 4b: with no properties and no `allOf`, `!is_bare_object` needs an `additionalProperties` written and `!is_map` needs it to be `false`, and a scalar `type` beside it is the contradiction [the exactness rule](#the-selector-grammar) already excuses | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.additionalProperties=false` |
| 5 | inside it, the closing `full_type_ref_resolved(&target, schemas)`, selected by the *absence* of cases 2 to 4: `string_enum_values` yielding nothing, no `oneOf` or `anyOf`, and then `is_map` or `is_bare_object` or none of the three positive disjuncts above. No property is common to every target that reaches it — a `type: string`, a bare `{}`, an open map, a bare `type: object` and a `{format: date}` all do — and every way of reaching it is an emptiness test or a negation. **The plan this row landed under expected an exact selector here and the reading of the code contradicts it**, so the row follows the code: this is the residual arm of the resolution block, the same shape as cases 14 and 16 below | **H-residual** |
| 6 | `if let Some(member) = sole_inline_all_of(prop_schema)` — one inline `allOf` member and nothing else declared. The arity half is `schema.allOf:sole-member`; what remains is nine sibling-absence tests, and without them the selector counts VolView's `TaskSpec.id`, a `type: string` beside a one-member `allOf`, which this function sends to its closing `base_type_ref` | **H-negated-value** |
| 7a | `string_enum_values(prop_schema)` → a hoisted enum, over a written `enum`, which the helper refuses unless the values are strings | `schema.properties>schema.enum:string-valued` |
| 7b | the same over a `const`, the spelling the helper falls back to when no `enum` is written | `schema.properties>schema.const:string-valued` |
| 8a | `prop_schema.reference.is_none() && is_inline_struct(prop_schema)` → `hoist_object`, on a property whose `properties` are non-empty | `schema.properties>schema.properties:non-empty` |
| 8b | the same arm on a property declaring `allOf`, which `is_inline_struct` takes only for a property declaring no scalar `type` | **H-negated-value** |
| 8c | the same arm on a property writing an explicitly empty `properties: {}` beside no `additionalProperties` | **H-negated-value** |
| 8d | the same arm on a property writing `additionalProperties: false` | `schema.properties>schema.additionalProperties=false` |
| 9 | `if let Some(members) = prop_schema.one_of.as_ref().or(prop_schema.any_of.as_ref())` — the composition gate, whose own condition is that the field is written; `oneOf` spelling | `schema.properties>schema.oneOf` |
| 10 | the same gate, `anyOf` spelling: a property declaring only `anyOf` reaches every arm below it identically | `schema.properties>schema.anyOf` |
| 11a | inside it, `non_null.len() == 1 && non_null.len() != members.len()` — the nullable pair collapsing to its one member; `oneOf` spelling | `schema.properties>schema.oneOf:sole-non-null-member` |
| 11b | the same, `anyOf` spelling | `schema.properties>schema.anyOf:sole-non-null-member` |
| 12a | inside it, `members.len() == 1 && is_inline_struct(&members[0])`, on a member whose `properties` are non-empty; `oneOf` spelling | `schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.properties:non-empty` |
| 12b | the same, `anyOf` spelling | `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.properties:non-empty` |
| 12c | the same on a member writing `additionalProperties: false`; `oneOf` spelling | `schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.additionalProperties=false` |
| 12d | the same, `anyOf` spelling | `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.additionalProperties=false` |
| 12e | the same on a member declaring `allOf`, either spelling | **H-negated-value** |
| 12f | the same on a member writing an explicitly empty `properties: {}` beside no `additionalProperties`, either spelling | **H-negated-value** |
| 13a | inside it, `if let Some(union) = self.hoist_discriminated_union(&name, prop_schema, …)`; the property's `oneOf` spelling. The composition gate above it is what puts the arm inside, so this counts no node cases 9 and 10 do not | `schema.properties>schema.oneOf:discriminated-union` |
| 13b | the same arm, the property's `anyOf` spelling, which only the inferred reading reaches for the reason case 2b states | `schema.properties>schema.anyOf:discriminated-union` |
| 14 | inside it, the closing alias over the members left after `is_null_variant` filtering | **H-residual** |
| 15 | `prop_schema.ty…primary() == Some("array")` → `hoist_array_item_type` | `schema.properties>schema.type:primary=array` |
| 16 | the closing `base_type_ref(prop_schema)` | **H-residual** |

#### `ref_to_class`

Wholly a predicate region, and for the reason it was wholly a hole before: the
function opens no schema — it reads the reference *string* and nothing else — so
no conjunction over declared fields changes its path, and every one of its cases
is decided by the pointer's segment structure, which is what a predicate selector
is for and which the grammar now declares six over. Nothing here can fail to be
reached: the loop never returns early, so a pointer's segments alone decide which
arms it takes and how often, and a selector read off one arm counts exactly the
nodes that take it. That is why this table needs no chain-overlap allowance while
`resolve_schema_pointer`'s case 8 does — the two read the same positions, and only
the second can stop before reaching one.

The first case takes two selectors rather than one, because two different shapes
reach it and only one of them names a document other than the one in hand: a
reference into another document, which crozier answers by fetching that document
([`matching.md`](matching.md#cross-document-ref-resolution-issue-77)), and a
reference into this document outside `components.schemas` — `#/definitions/Foo`
from a Swagger conversion, or a pointer into another component map — which is
answered inside the bytes already read. The plan this pass ran under expected the
first to be permanently `UNREACHABLE`, and asked for the split so that recording
both under one name would not put a reachable branch behind that row. **The
measurement contradicted the premise rather than the split**: both halves came
back `golden` — the cross-document spelling at 29 declaration sites across two
registered sources that both carry a committed golden, the same-document one at
50 across four, three of them golden-bearing — and keeping them apart is what
let the census say so of each separately.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1a | `let Some(pointer) = reference.strip_prefix("#/components/schemas/") else { … }` — a foreign pointer, named off its last segment; the cross-document spelling | `schema.$ref:cross-document` |
| 1b | the same arm, the same-document spelling: a pointer outside `components.schemas` | `schema.$ref:same-document-foreign-pointer` |
| 2 | `"properties" if index + 1 < parts.len() => name.push_str(&naming::class_name(parts[index + 1]))` | `schema.$ref:nested-properties` |
| 3 | `"items" => name.push_str("Item")` | `schema.$ref:nested-items` |
| 4 | `"allOf" \| "oneOf" \| "anyOf" => index += 2` — a composition index contributes no name | `schema.$ref:composition-index` |
| 5 | `_ => index += 1` — a segment none of the four names, a trailing `properties` included | `schema.$ref:unnamed-segment` |

#### `path_group`

It reads the request URL and opens no schema, so its three arms are named by
predicates over a Paths Object key rather than by conjunctions over a node's
fields. `openapi.paths:templated-key` says a key carries a template expression and
`openapi.paths:several-template-expressions` says it carries more than one;
neither says *which* segment carries it or whether all of them do, which is the
only thing this function reads, and the three predicates below say exactly that.
They partition every key, so each of the three arms is counted by one of them and
by no other — which is why this table is the one region where no case needs the
chain-overlap allowance at all.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1 | `.find(\|s\| !(s.starts_with('{') && s.ends_with('}')))` returning the key's first segment | `openapi.paths:leading-literal-segment` |
| 2 | the same `find` returning a later segment, having skipped a templated one | `openapi.paths:template-before-literal-segment` |
| 3 | `.unwrap_or("service")` — every segment is templated, or the URL has none | `openapi.paths:all-segments-templated` |

**What the node-local predicate family closed, and what it did not.** The
account this table replaces derived fifty-three cases, nine of them carrying a
conjunction and forty-four recorded as one of sixteen enumeration holes. Eight of
those sixteen were holes only because the grammar had no *node-local* predicate —
a property one object-model node's own declared fields and their values decide,
with no `$ref` resolution and no comparison across the document. Eleven such
predicates are now declared, plus the one valued field
`schema.additionalProperties`, and with them that pass derived seventy-six
cases, forty carrying a selector and thirty-six recorded as one of nine holes.
Seven hole kinds are gone: H-arity, H-empty-collection, H-type-multiplicity,
H-boolean-value, H-enum-value-kind, H-key-segment-position and
H-key-all-templated no longer name any case, because every arm they named is now
counted by its own selector.

**What the pointer-form family closed after it.** Two of those nine holes turned
on a `$ref` *value* rather than on a node's declared fields — H-pointer-form, the
segment structure of the value, and H-pointer-target, whether its head names a
declared component — and both are gone. Seven predicates close them, six read off
the value alone and one, `schema.$ref:undeclared-component-head`, off that value
against the document context this change also lands. The table above therefore
derives seventy-eight cases rather than seventy-six — `ref_to_class`'s first case
and `resolve_schema_pointer`'s are each two rows now, one per shape reaching them
— fifty carrying a selector and twenty-eight recorded as one of seven holes.
`ref_to_class` was wholly a hole and is wholly counted; `resolve_schema_pointer`
kept five, the five whose arm resolves a segment against the schema at that
position, which that pass left recorded as H-pointer-nesting and
[the pointer-walk pass](#the-two-rows-the-pointer-walk-pass-added) closed after
it. **Seven new rows
landed, and all seven are [`schemas`](openapi-surface/schemas.md)'s: five `golden`
and two `gap`, both of the two `FIXTURE`** — which is the size of the settlement
work this pass added, readable off the region file rather than off a report. **What
did not change is the walk**: these predicates read a `$ref` at the node that
writes it, which the census already visited, so no count rule moved, no existing
row's category, settlement or evidence-cell count moved, and no snapshot digest was
re-pinned.

**Three of the arms this pass set out to close stayed holes, and each is a
finding rather than an omission.** `prop_type_ref`'s case 6 was recorded as
H-arity, and its arity half is indeed a declared predicate now — but
`sole_inline_all_of` is that arity *beside nine sibling-absence tests*, and
without a negation operator the arity alone counts VolView's `TaskSpec.id`, a
`type: string` carrying a one-member `allOf`, which the function sends to its
closing `base_type_ref`; the case is H-negated-value. `hoist_union_variant`'s case
11 was recorded as H-example-value, and the two selectors that hole names would
still leave `is_bare_object`'s four absence tests unexpressed, so a map schema
carrying a concrete example — `type: object` beside an `additionalProperties`
schema and an `example` — is counted by them and reaches `base_type_ref`; it is
H-example-value still, and its row now says the negation operator is needed too.
`prop_type_ref`'s case 12 was recorded as H-arity and is now four cases and two
holes rather than one hole, because the arity is only half of it: the other half
is `is_inline_struct`, a *disjunction*, which no conjunction expresses, so each
disjunct is its own case and the two that turn on an absence stay holes.

**Where this pass read `src/ir.rs` differently from the account it replaces.**
Three differences, each recorded on the row it belongs to rather than only here.
The `type: array` guard of `hoist_union_variant` covers **cases 3 to 7**, not
"cases 4 to 7" as that account said: `simple_nullable_member` is read inside the
same `if variant.ty…primary() == Some("array")` block, which is why cases 3a to 3d
carry `schema.type:primary=array` like their neighbours. `is_inline_struct` is a
disjunction of **four** conditions, not the three that account derived where
`nested_array_element` reads it: a `type: object` writing an explicitly empty
`properties: {}` beside no `additionalProperties` is an inline struct, and that
arm is now case 6b there and cases 7f, 8c and 12f in the two other tables that
read the helper. And `simple_nullable_member` reads `any_of.or(one_of)` — the
opposite order to every other call site in the file — which is why case 3 splits
into four rows rather than two, and why row 3a is the `anyOf` spelling.

**What the thirty-nine new selectors classified as.** The census was run over all
169 registered sources and every one of them was put to it by name. **28 are
`golden`** and **11 are `gap`**, all eleven `FIXTURE`; none is `limitations`,
because [`fern-limitations.md`](fern-limitations.md) names no row for any of them.
[`schemas.md`](openapi-surface/schemas.md) owns thirty-six of the thirty-nine —
every selector anchoring on a Schema Object — and
[`document-paths.md`](openapi-surface/document-paths.md) the three
`openapi.paths:` readings `path_group` makes. The two boolean spellings
`schema.additionalProperties` now emits are the exception that adds no row:
[`schemas.md`](openapi-surface/schemas.md)'s `additional-properties-boolean-true`
and `additional-properties-boolean-false` already classify those two features on a
bespoke variant scan, so what the valued selector adds is that the *census* can
now answer for them by name — and those two cells stay dated to the scan they were
taken on, which is the rule
[the measurement bullet](#ranked-gap-backlog) states for every region file.

**Eleven is the first non-empty answer this instrument has given about these six
functions**, and it is what the [conjunction pass](#what-the-conjunction-pass-moved-in-those-six-regions)
predicted would happen: *extend the grammar to express one of these holes and the
census can report the new selector absent across every registered source, which
is a `gap`.* All eleven are the `anyOf` twin, the closed-object element or the
one-member composition of an arm whose sibling spelling the corpus does declare,
which is why each is `FIXTURE` rather than `PROBE` — a real document plausibly
writes it and Fern plausibly emits bytes from it. They are ranked as one block in
[the fixture backlog](#the-eleven-rows-the-node-local-predicates-added).

**What this section did not do, and what has since been done.** The change that
wrote it declared selectors and added no row to any region file: naming a shape
is what makes it classifiable, not what classifies it. The classification has
since been taken. All nine conjunctions were run over the 164 registered sources
and all nine are `golden`; [`schemas.md`](openapi-surface/schemas.md) owns the
nine rows, since every one of them anchors on a Schema Object, and that region's
own counts move with them. The sixteen holes that pass left were untouched by it —
each still named the predicate or valued selector that would close it, and none
was a row anywhere. Nine of them remain; the paragraph below says which closed.

**And the settlement pass found nothing to settle.** The four routes a
conjunction row could take — register a golden for a source the corpus already
holds, screen and register a real-world witness, author a Fern probe, or record
that the shape has no position in a generated Python SDK — are the routes a
`gap` row takes, and the classification left **zero** `gap` rows among the nine.
No route was therefore taken, no source was registered, no probe was authored
and **no witness search was run**, so this node put no source to any query. The
settlement of the conjunction backlog is that the measurement had already
emptied it.

**That is a measured outcome, not an unrun check.** The nine were not assumed
`golden` and skipped. `just surface-census --json` was re-run over all 164
registered sources — 532 selectors, 817,028 declaration sites — and every one of
the nine came back declared by at least one source whose committed golden
byte-matches: 102 such sources for `schema.items>schema.$ref` at the wide end,
one (`braintrust-dev`) for `schema.anyOf>schema.allOf` at the narrow one. That
is condition 1 of [the precedence](#the-category-rules), so `limitations` is
never reached and `gap` never reached either. The distinction is worth the
sentence because a `gap` nobody found and a shape nobody measured read
identically in a table that carries neither row: what this section reports is
that the question was put to the corpus and came back answered, nine times out
of nine.

**And a re-measurement over the corpus as it now stands confirms it.** The nine
were run again for this restatement, over all 169 registered sources rather than
the 164 the classification walk read, and every one is still declared by at least
one source carrying a byte-matching committed golden — from
`schema.items>schema.$ref` (119 sources, 107 of them golden-carrying) down to
`schema.anyOf>schema.allOf`, still `braintrust-dev` alone and still 4 sites, which
is the thin end the paragraph above says a withdrawn corpus row would take to
`gap`. Two selectors' arithmetic moved with the newly registered sources —
`schema.items>schema.$ref` from 4,151 sites in 114 sources to 4,301 in 119, and
`schema.oneOf>schema.$ref` from 676 in 28 to 684 in 31 — and no category moves
with them. [`schemas.md`](openapi-surface/schemas.md)'s cells therefore stay
dated to the walk they were transcribed from, which is the rule
[the measurement bullet](#ranked-gap-backlog) already states for every region
file; re-transcribing two of them here would leave the region file and this index
disagreeing about a number neither classification depends on.

**What it would take for a future conjunction to land as a `gap`.** By the same
precedence, a conjunction is a `gap` exactly when no registered source *carrying
a committed golden* declares it and no [`fern-limitations.md`](fern-limitations.md)
row names it. Two things put one there, and neither is far-fetched:

- **A conjunction whose shape the corpus never writes.** The closed list
  is read off the six blind functions' own cases, and the holes
  [the case analysis](#the-six-blind-regions-of-srcirrs-case-by-case) names are
  shapes no selector kind can express *yet*. Extend the grammar to express one —
  each hole says which kind it would take — and the census can report the new
  selector absent across every registered source, which is a `gap` carrying `FIXTURE` or
  `PROBE` in its settlement cell like any other row in the two backlogs below.
- **A conjunction only the goldenless half of the corpus declares.** Registration
  and golden are two different things: twelve of the 114 sources declaring
  `schema.items>schema.$ref` carry no committed golden, and four of the seventeen
  declaring `schema.anyOf>schema.$ref` carry none. A conjunction declared *only*
  by sources like those is a `gap` whose route is the cheapest of the four —
  register the golden for a document the corpus already holds.

That none of the nine is in either position is a fact about this corpus at this
commit rather than a property of conjunctions, and the margin at the thin end is
one document: `schema.anyOf>schema.allOf` rests on a single golden-carrying
source and `schema.oneOf>schema.allOf` on two, so a corpus row withdrawn there
would take a `golden` row to `gap` without anything in `src/` changing.

#### What the conjunction pass moved in those six regions

Nothing, and the measurement is published here rather than left to be inferred
from that sentence. `just fixtures-coverage` was re-run over the finished tree
and the six functions' blind-region counts are below, beside the counts the run
these cells were last taken on reported — the run recorded with the ranked
backlog itself, in the change that introduced this join table and these six
numbers together (`docs: rank the OpenAPI coverage gaps and record the fixture
and probe backlog`). A count is the
function's share of the de-duplicated union the report's own
`total N region(s)` line counts — the attribution the join table's columns
describe, run per function by the script below.

| blind region of `src/ir.rs` | before | after | |
|---|---:|---:|---|
| `hoist_union_variant` | 24 | 43 | +19 |
| `resolve_schema_pointer` | 25 | 25 | — |
| `nested_array_element` | 25 | 23 | −2 |
| `prop_type_ref` | 20 | 22 | +2 |
| `path_group` | 15 | 15 | — |
| `ref_to_class` | 22 | 2 | −20 |
| **the six** | **131** | **130** | **−1** |

**None of that movement is the conjunction pass's.** The two changes that made
it — the one declaring the nine selectors and the one classifying them — touched
`docs/`, `scripts/openapi-surface-census.py` and `tests/surface_census_test.py`
and nothing else: no `src/` file, no `tests/fixtures/` golden, no `CORPUS.md`
row. A pass that registers no golden cannot move a golden blind spot, and this
pair of columns is what says so with a number instead of an argument. What did
move them is everything else that landed between the two runs — eleven changes
to `src/ir.rs`, 2,608 insertions against 318 deletions, and the corpus rows
other work registered, which is also why `ref_to_class` fell to 2 and why the
file's printed count stands at 235 while `src/openapi.rs`'s fell from 511 to 184
— and has since risen to 218, on a probe rather than on a golden.
So the pair of columns answers *what did the conjunction pass buy in the
generator?* with **nothing**, and it is only by publishing both halves that the
much larger movement beside them is not mistaken for an answer to that
question. **The refresh this document's own numbers are now taken on reproduces
the `after` column digit for digit** — 43, 25, 23, 22, 15 and 2, the same 130 —
so a column that moved elsewhere in the join table moved because the measurement
did, not because the attribution drifted.

**This measurement moves no row's category**, exactly as the previous round's
crozier-versus-Fern comparison of the probe documents did not. The nine
conjunctions are `golden` on the census join and the committed goldens that
byte-match, and a blind-region count is neither of those things.

The per-function attribution is a scratch script, the way
[`schemas.md`](openapi-surface/schemas.md#the-supplementary-variant-scan)'s
variant scan is. Run it from the repo root after `just fixtures-coverage` has
written its exports:

```python
"""Attribute one `src/` file's golden blind regions to the functions holding them.

The report's blind-spot block is per file; this join table's verdicts name
functions, "counted from that union" — the de-duplicated union of the non-golden
tiers minus the golden tier, the same set the report's `total N region(s)` line
counts. This reproduces that attribution. It reuses the recipe's own `load_tier`
and `drop_test_regions`, so the `#[cfg(test)]` exclusion and the shared
denominator keep their single definition in
`scripts/fixtures-coverage-report.py`, and it lands a blind region on the
innermost `fn` whose brace-matched span contains its first line.

    python3 blind-by-function.py src/ir.rs
"""
import importlib.util, re, sys
from pathlib import Path

REPO = Path.cwd()
spec = importlib.util.spec_from_file_location(
    "fixtures_coverage_report", REPO / "scripts" / "fixtures-coverage-report.py"
)
report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report)

recipe = (REPO / "scripts" / "fixtures-coverage.sh").read_text(encoding="utf-8")
out_dir = REPO / re.search(r'^out_dir="\$repo_root/([^"]+)"', recipe, re.M).group(1)
golden = re.search(r"^  --golden-tier (\S+)", recipe, re.M).group(1)
names = re.findall(r'--output-path "\$out_dir/([a-z0-9-]+)\.json"', recipe)
order = [golden] + sorted(n for n in names if n != golden)

tiers = {n: report.load_tier(out_dir / f"{n}.json", REPO) for n in order}
report.drop_test_regions(tiers, REPO)
reached = {
    n: {(f, r) for f, counts in t.items() for r, c in counts.items() if c > 0}
    for n, t in tiers.items()
}
others = [n for n in order if n != golden]
blind = set().union(*(reached[n] for n in others)) - reached[golden]


def spans(lines):
    """(name, first line, last line) per `fn`, by brace matching from its header."""
    out = []
    for i, line in enumerate(lines):
        m = re.search(r"\bfn ([a-z_0-9]+)\s*[(<]", line)
        if not m:
            continue
        depth, started, end = 0, False, len(lines)
        for j in range(i, len(lines)):
            for ch in lines[j]:
                if ch == "{":
                    depth, started = depth + 1, True
                elif ch == "}":
                    depth -= 1
                    if started and depth == 0:
                        end = j + 1
                        break
            if end != len(lines):
                break
        out.append((m.group(1), i + 1, end))
    return out


for target in sys.argv[1:]:
    lines = (REPO / target).read_text(encoding="utf-8").splitlines()
    fns = spans(lines)
    counts: dict[str, int] = {}
    for f, r in blind:
        if f != target:
            continue
        holding = [fn for fn in fns if fn[1] <= r.line_start <= fn[2]]
        name = min(holding, key=lambda fn: fn[2] - fn[1])[0] if holding else "<no fn>"
        counts[name] = counts.get(name, 0) + 1
    print(f"{target}: union {sum(counts.values())} blind region(s)")
    for name, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {name:<34} {n}")
```

**The nine files whose verdicts did not move are what says the attribution is
the join table's own.** Run over this tree, the script reproduces every function
count `src/settings.rs`, `src/cli.rs`, `src/refs.rs`, `src/schema.rs`,
`src/lib.rs`, `src/naming.rs`, `src/config.rs`, `src/pyfmt.rs` and `src/main.rs`
already publish, digit for digit and with no cell edited — so where a count did
move, it moved because the measurement did.

#### The arms an observation surface answers for

Fourteen of the cases above are reached *through* a reference: the arm stops
reading the document in front of it and reads the one it points at. That is where
"the document a selector counts" and "the document the arm enters" come apart, so
a selector read off a **misreading** of one of these arms would be confirmed by
fixtures chosen under the same misreading, and nothing in the tree would say so.

`src/ir.rs`'s `arm_trace` module closes that circle. It answers, for one run of
the real generator over one document, **which of these arms executed** — recorded
at each arm's own site rather than read back off the emitted Python, so an arm
that was misread fails a test instead of agreeing with one. It is `#[cfg(test)]`
throughout and every site records through the `observed_arm!` macro, which
expands to nothing outside a test build: the generated Python cannot move because
of it.

The list of arms it answers for is declared once, in that module's
`OBSERVED_ARMS`, and restated below;
`the_documented_observed_arms_are_the_ones_this_module_declares` fails when the
two disagree in either direction, and
`every_observed_arm_answers_both_ways_over_the_real_generator` drives
`ir::build` over two documents per arm — one under which it runs and one whose
node enters the same function, through the entry gate this section states for it,
and takes a different arm.

**The third column is the finding that separates these fourteen from each
other.** `src/ir.rs` resolves a reference two ways, and they are not
interchangeable:

- **the last-segment lookup** — `resolve_ref_from_schemas`, which is
  `schemas.get(reference.rsplit('/').next()?)`: it takes the reference's last
  `/`-separated segment and looks that name up in the document's own
  `components.schemas`, traversing nothing;
- **the prefixed pointer walk** — `resolve_schema_pointer`, which requires the
  `#/components/schemas/` prefix, takes the component its head segment names, and
  then walks the reference's remaining segments structurally through `allOf`,
  `oneOf`, `anyOf`, `properties` and `items`.

[The selector grammar](#the-selector-grammar) states what each yields for a
reference value the two answer differently. A selector mirroring the wrong one
would count documents its arm never reaches, so each row below says which
resolution the arm's own condition performs — and every case the row lists
performs that one.

| function | cases | which resolution the arm's own condition performs |
|---|---|---|
| `resolve_schema_pointer` | 3, 4, 5, 6, 7 | the prefixed pointer walk — these five arms *are* its segment loop, one per segment spelling it reads |
| `prop_type_ref` | 1, 2, 3, 4, 5, 13 | the last-segment lookup: cases 1 to 5 through `resolve_ref_from_schemas` on the annotated `$ref` case 1's gate finds, case 13 through `discriminated_union`, which resolves each `oneOf` member's `$ref` — and each `mapping` target, by the same last segment — that way |
| `hoist_union_variant` | 4, 6 | the last-segment lookup: case 4 through `discriminated_union` as above, case 6 through `resolve_ref_from_schemas` on the item's annotated `$ref` |
| `nested_array_element` | 2 | the last-segment lookup, through the same `discriminated_union` |

Neither `ref_to_class` nor `path_group` appears: the first reads a reference
*string* and resolves nothing, and the second reads a Paths Object key.

### Refreshing the coverage snapshot

`just fixtures-coverage` is not in `just check` — it needs network and runs the
corpus instrumented — so the gate cannot *produce* the join table's `printed` and
`by tier` columns. It does refuse a table that disagrees with them: the recipe
leaves its per-tier `llvm-cov` exports in `.local/fixtures-coverage/`, and
`RankedBacklogTests` reads them back through the recipe's own report module and
recomputes both columns from them. With no export present that one case skips by
name, the way the corpus byte-diffs skip an unfetched spec; once anyone has run
the recipe, a stale table fails the gate.

So refreshing is: run the recipe, then bring the table to what it printed.

```sh
just fixtures-coverage | sed -n '/golden blind spots/,/^  total/p'
```

Refresh both columns and every ranked row's criterion-2 cell together — criterion
2 is checked against the `printed` column, the quoted `total ... region(s)` line
against the report's own, each file's ranked-gap count against the ranked table,
and the two-largest-files figure above against the `printed` column it sums, so
updating one alone fails rather than passing silently.

Everything else — the rubric order, the published median, the two backlogs
against the six region files, and the two tables' agreement with each other — is
`RankedBacklogTests` in `tests/surface_census_test.py`. Run it with
`just test-surface-census`, which `just check` already does.

## The probe backlog

The other 0 `gap` rows whose settlement is not a fixture. **These are probe
work, not fixture work** — the corpus takes real-world specifications only, and a
probe is never proposed as a fixture
([`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md)). When one is
measured, the result belongs in [`fern-limitations.md`](fern-limitations.md) as a
row with a verdict, at which point the feature's category here becomes
`limitations` and it leaves this list. Nothing below is ranked: a probe costs one
Fern run, so the order to do them in is whichever the next Fern session has
loaded.

**The backlog is empty, and both parts below say why.** It is empty because every
row that stood in it has been settled rather than because the classes were
retired: the last seven were measured in
[`fern-limitations.md`'s Round 5](fern-limitations.md#round-5--the-seven-witness-supply-probes),
each on a committed probe document, and each is `limitations` on the verdict that
round recorded. The two classes remain live, and the rules below are what a new
row entering either is held to — a shape whose settling measurement is a
difference between two documents lands in the first, and a shape whose world-wide
search returns `none-found` lands in the second.

**What the two parts mean now that a third settlement route exists.** When the
split was drawn, a `PROBE` row was the only kind of row a probe could settle: a
`FIXTURE` row whose only real witness turned out to be unregistrable had no
instrument at all, and nine rows stood in exactly that state.
[The settlement rule](#the-settlement-rule-as-amended) now gives that row route 2,
and a row whose search left a required source unanswered route 3, so a locally
authored probe settles rows in three different places rather than one. That does
not merge the two parts, and it does change what the split is *about*. It is no
longer the line between rows a probe can settle and rows it cannot. It is the
line between a probe that is the last word and a probe that is provisional: a
structural row's measurement is permanent, because no corpus row could ever
settle it however many documents were searched, while a witness-supply row's is
not — and neither is a route 2 or route 3 row's. All three of those stay
convertible, and a registrable witness found later promotes any of them to
`golden` under [the classification precedence](#the-category-rules). Both parts
being empty, the whole of that provisional set stands in the `limitations` column
today rather than in this list, which is where a reader counting outstanding
probe work should look for it and would otherwise find nothing.

**What a row here records, and what it does not.** This section used to justify
the whole list in one sentence — that each row asks what Fern does with a shape
*no real-world document can isolate*. That was always a stronger claim than the
evidence under it, and the reclassifications this document has since absorbed
have made it false of most of what remains. What the rows actually record is one
of three weaker things: that **no registered source supplies a witness**, that
**the census cannot detect one**, or that **the measurement is a difference no
single document can carry**. Only the third is a statement about the world; the
first is a statement about this repository's own sample of registered sources,
and the second about the reach of its own instrument. Read either of those first
two as "nobody writes this" and the cost is exact and permanent: a `PROBE` closes
by recording Fern's behaviour in prose and never produces a golden, so the shape
is never byte-compared against Fern again.

Two of the three survive as grounds for a row staying here, and they are what the
list splits on. The one that does not is *the census cannot detect it*: a
selector that cannot express a shape has measured nothing about it, so a row
resting on one is a row whose search has not been done rather than a row with an
answer. A shortfall in the registered sample becomes grounds only once a search
of the *world* has been run and found nothing — that is the witness-supply part —
and a difference no single document can carry is the structural part.

So the list splits in two below, and no row's kind is adjudicated here. Each
row's own `settlement` cell in its region file states which kind it is, in the
terms that row's own evidence supports; the two parts are derived from those
cells rather than decided beside them, and `RankedBacklogTests` in
`tests/surface_census_test.py` reconciles the derivation both ways, so a reworded
cell fails the gate rather than leaving a table here quietly wrong.

**No row in either part rests on a census selector, and the gate refuses one
that does.** A selector reporting zero is `gap` evidence — the census's own
statement that no registered source declares the shape — and it is never on its
own why a row settles `PROBE`. `RankedBacklogTests` refuses a `PROBE` settlement
cell that names a selector as its reason, refuses a witness-supply row with no
line of its region file's witness-search table, and refuses a line there that
omits a required source or names one with no query against it.

### Structural probes

**0 rows.** A structural probe's settling measurement is a **difference between
two documents**: one `openapi` patch level against another, a Reference Object
carrying a field against one without it, the same schema with and without a
keyword. No single document can carry that comparison, so no golden can pin it
and no corpus row could ever settle it however many documents were searched — a
probe is genuinely the only instrument, and such a row would be here permanently.
This is the subset the withdrawn sentence really described, and it is much
smaller than that sentence implied: no `gap` row in the tree is in it today.

That is not the same as the shape being unmeasured. The differential lives in
[`oas31-extensions.md`](openapi-surface/oas31-extensions.md)'s
`openapi-version-3.0.4`, `openapi-version-3.1.1` and `reference-description`
rows, each `golden` on a witness that pins the *declaration* while its
`settlement` cell records that the difference between that document and one at
the other patch level, or without the field, is still unpinned. A row lands in
this part when that residual is the whole of what is left, and none is today.

Two rows left this part rather than being counted in it. `duplicate-operation-id`
and `duplicate-normalized-paths` sat here reading as collisions inside one
document, which is not a difference between two: one document declaring the
collision generates a golden whose raw-client methods say what Fern did with it,
so a corpus row settles either outright. Both became `FIXTURE` gaps, were ranked
in the list above, and are `golden` now — `duplicate-normalized-paths` on corpus
rows 127, 128 and 131 and `duplicate-operation-id` on rows 128, 129 and 132 —
which is a row leaving this part by being reclassified and then settled by a
registered witness, the longest of the three routes a row can take out of here.

### Witness-supply probes

**0 rows.** A witness-supply probe's shape is perfectly isolable in a single
document. Nothing about the shape prevents a corpus row; the supply of documents
does — the authoritative issue #188 search found **no witness at all**, and the
row's own region file records that search as a line of its `### Witness search
(issue #188)` table naming every source put to it and the exact query used
against each. What becomes of a row when that search *does* find a witness is
[the settlement rule](#the-settlement-rule-as-amended) below, which every region
file follows rather than restating.

**The seven that stood here are measured, and the class is not.** `$dynamicAnchor`
and `$dynamicRef` (one probe, because the reference and the anchor it resolves to
are only exercisable together), `$vocabulary` under a custom schema dialect, and
the four IANA HTTP schemes `concealed`, `gnap`, `privatetoken` and `vapid` (two
documents each, the scheme alone and the scheme beside one Fern supports) were all
carried through `fern check` and a real `fern generate` and recorded in
[`fern-limitations.md`'s Round 5](fern-limitations.md#round-5--the-seven-witness-supply-probes),
every one of them `discards`. Each is `limitations` in its region file now, citing
that key and verdict, and each records what a registrable witness would have to
be, so a document found later promotes the row to `golden` under
[the classification precedence](#the-category-rules) rather than leaving it closed.
Their probe documents are committed under
[`openapi-surface/probes/`](openapi-surface/probes/) so the measurements can be
re-run; none is a corpus fixture and no corpus row came out of the round. Round 5
also generated each cleanly-generating probe with crozier and byte-compared it
with Fern under the gate's own normalization, repairing the one divergence it
found in `src/` — corroborating evidence beside the verdicts, which moves no row's
category and is counted nowhere here, because this document credits registered
corpus goldens rather than probes.

#### The settlement rule, as amended

**The rule, in one statement.** A row's search returns one of five outcomes, and
the outcome decides which of three routes settles the row. **Route 1** settles it
with a registered corpus golden, and is the only route that produces
crozier-versus-Fern byte-comparison evidence. **Route 2** and **route 3** settle
it with a locally authored Fern probe recorded in
[`fern-limitations.md`](fern-limitations.md), which makes the row `limitations`
under [the classification precedence](#the-category-rules) and leaves it
convertible to `golden` the day a registrable witness turns up. Each route
carries its own gate, stated with the route below, and none of the three is a way
past searching: a witness the search *did* find never leaves a row here on
witness-supply grounds, however unusable that document turns out to be, and what
it leaves *as* depends on why it is unusable. The five outcomes, and what each
licenses:

1. **`witness-found`** — a real-world document declares the shape, at an
   immutable ref, under a [redistribution-compatible](corpus-licensing.md)
   licence, and Fern accepts it.
   The row becomes `FIXTURE` and takes **route 1**, retiring outright to `golden`
   the moment that document is registered: `dollar-comment` did exactly that, as
   corpus row 109. Route 1's gate is the corpus registration rules themselves
   ([`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md)) and the
   byte-match the golden has to reach; nothing in this section relaxes either.
2. **`witness-blocked`** or **`fern-rejected`** — such a document exists and this
   corpus cannot use it: outside its redistribution set, reachable at no
   immutable ref, or refused by Fern. The row still becomes `FIXTURE`, because
   the search proved the shape has a real-world witness and what is short is that
   document rather than the world — which is what `dollar-anchor` records.
   **Route 2** settles such a row *instead* by a locally authored Fern probe
   recorded in [`fern-limitations.md`](fern-limitations.md), at which point its
   category here becomes `limitations` under
   [the classification precedence](#the-category-rules). Its two gates — the
   recorded exhaustive search, and the blocker the row names — are stated with
   the route below.
3. **`none-found`** — no document reaching that bar was found anywhere the
   region's declared sources reach. The row stays here as a witness-supply probe,
   and no route above or below settles it: what settles it is the probe this
   class itself names, authored and measured, which is how
   [the seven that stood here](#witness-supply-probes) left.
4. **`search-incomplete`** — the outcome for a search a required source did not
   answer: the registry was unreachable, the query was refused, the index
   returned an error rather than a result. The row says so in
   that source's own segment of its `sources searched and the exact query used
   against each` cell, with the word `unanswered` beside what the source did
   instead of answering, so the record names what is outstanding. It says the
   world was not fully asked and therefore leaves the row's question **open**:
   it is the one outcome that licenses neither route 1 nor route 2, because both
   of those rest on what the search found. A record marking a required source
   `unanswered` reads `search-incomplete` rather than `none-found`, and the
   reconciliation refuses that pairing — which is what keeps an unread source
   from becoming evidence of absence. **Route 3** settles such a row nonetheless,
   by a locally authored Fern probe, because a probe claims nothing about the
   world; its gate is the outstanding source, stated with the route below. One
   row in the tree reads this outcome: [`schemas`](openapi-surface/schemas.md)'s
   `dependent-schemas`, whose search found no usable witness and left SwaggerHub's
   `openapi-3.0.x` family unread, and which route 3 settles.

**Route 2's first gate: the recorded exhaustive search.** Route 2 is never a
shortcut past searching, and its gate is a property of this repository rather
than of anything outside it. A row is eligible only where **its own region file** records a search
for that row: a line of that file's `### Witness search (issue #188)` table whose
`outcome` cell reads `witness-blocked` or `fern-rejected`, naming **every source
that region's own witness-search preamble names**, and recording for each both
halves of what it did — the query put to it, in a code span so it can be re-run
verbatim, and after that query what the query returned, a count or `unanswered`.
Both halves, because a source named with no query is one nobody can check was
really asked, and a query with no result is a question with no answer written
down. A row with no search recorded against it is not eligible, and neither is
one whose search returned `none-found` — that is the witness-supply probe
outcome 3 already covers.

**Route 2's second gate: the blocker, which is what keeps the row convertible.**
A row settled this way records that a real witness exists and names precisely what stops that witness
being registered, so that the day the blocker lifts the witness is registrable
and the classification precedence promotes the row to `golden`. It must not read
as permanently settled. A blocker counts only in one of three forms, and each
names what would have to change:

- **`licence`** — the licence the witness carries, spelled as the SPDX identifier
  this corpus is refusing (`AGPL-3.0`, `NOASSERTION`) in a code span of its own,
  or as `none declared` where the publisher declares none. Some *other* quoted
  string does not stand in for it: a licence blocker that quotes `fern check` has
  named no licence.
- **`mutable ref`** — both halves of what makes the reference mutable: the URL
  the document is served at, in a code span, **and**, after it, what can change
  under that same address, said with one of *changes*, *overwrites*, *moves*,
  *replaces*, *updates*, *republishes*, *rewrites* or *mutates* in any
  inflection. The URL alone is not a blocker, because a URL is not by itself
  mutable — and neither is a clause after it that restates the label
  (*"this is a mutable reference"*) or describes the document rather than what
  happens to it. Naming the change is the half that carries the blocker.
- **`fern refusal`** — both halves of Fern's own refusal: the **exit status** it
  returned, and the diagnostic it printed, quoted in a code span of its own — a
  phrase Fern printed, of at least three words carrying letters. A refusal quotes
  several things and only one of them is the diagnostic: the invocation, the exit
  status, the generator version, the pinned ref, the spec URL are all facts
  *about* the run, and none of them is what Fern said. So a refusal whose only
  code span is `fern check`, or `1`, or `5.20.0`, has recorded that Fern ran and
  not why it refused.

A blocker is refused unless it names one of the three *and* carries that form's
payload, so no row is settled behind one too vague to tell anybody what would
have to change for the witness to become registrable. Each form's label with
everything but its payload is the shape that failure takes, which is why the
payload rather than the label is what is checked.

**How a row says it took route 2.** Its `evidence` cell carries what every
`limitations` row carries — the [`fern-limitations.md`](fern-limitations.md) key
and its verdict — and beside it the words **`blocked-witness probe`**, the
outcome its own region file's search recorded, and the blocker after
**`blocker:`**.

**Route 3: the open-search probe, and its gate.** Outcome 4 licenses neither
route above, on the sound ground that an unread source must never become
evidence of absence — and read alone that would leave a row whose search found
no usable witness *and* left a required source unanswered settleable by nothing
at all: no corpus row may pin it, because no witness was found, and no probe may
settle it, because a source went unread. The rule separates the two things
`search-incomplete` conflates. A row may not claim *the world* has no witness
while a source is unread — that stays, unchanged, and it is the whole point of
the outcome. But a locally authored probe claims nothing about the world: it
records what Fern does, and every row settled by one stays convertible, leaving
`limitations` for `golden` under
[the classification precedence](#the-category-rules) the day a witness turns up.
So a probe settlement never rests on absence, and an outstanding source does not
bar it. **Such a row may therefore be settled by a locally authored Fern probe
recorded in [`fern-limitations.md`](fern-limitations.md), at which point its
category here becomes `limitations`.** Two rows of the ranked backlog stood in
exactly that state — `header-allow-reserved`, whose only two declaring documents
anywhere are synthetic, and `parameter-style-form-cookie-scalar`, whose eighteen
declaring files are all tooling fixtures — and route 3 is what settled them, in
[the round below](#the-six-rows-a-round-of-probes-settled). `dependent-schemas`
is the third row to take it, on the SwaggerHub family its own search left
unanswered, in [the `schemas` round](#the-thirteen-rows-the-schemas-round-of-probes-settled).

**What separates route 3 from the two routes above.** Route 1 settles a row whose
search found a witness this corpus can register, and it settles it with a corpus
golden rather than with a probe — so a recorded search reading `witness-found` is
refused here, because route 1 is what settles that. Route 2 settles a row whose
search found a real witness this corpus cannot use, and names that witness's
**blocker** — the licence, the mutable reference, or Fern's refusal — as the
thing that would have to change. Route 3 settles a row whose search found no
usable witness and left a required source unanswered, and what it names in the
blocker's place is the **outstanding source**: the one that did not answer,
together with what it did instead of answering. That outstanding source, recorded
as `unanswered` in the row's own witness-search line, is what licenses the route;
so every outcome but `witness-found` is admissible under it, because what settles
the row is the probe rather than the outcome word.

**Why the largest unread source stays unread.** The source outstanding on both
rows above is SwaggerHub's `openapi-3.0.x` family — **414,968** specs, over which
the registry exposes no body search, so reading it means fetching and parsing
every body. This repository's own record says twice that a SwaggerHub version
reference is editable in place by its owner: the
[`http-hoba` witness-search line](openapi-surface/security.md#witness-search-issue-188)
records the `Auth Test` document's `1.0.0` reference that way, and
[`schemas.md`](openapi-surface/schemas.md)'s SwaggerHub bulk-read row records the
same of the registry as a whole. A witness found there therefore carries no
immutable ref **by construction**, and is unregistrable whatever licence it
declares. Reading the family can move a row from `search-incomplete` to
`witness-blocked` on a mutable-ref blocker, or to `none-found`; both of those
settle by a locally authored probe as `limitations`, which is what route 3
already gives. So the read can change the prose of *why* a row is settled, and
neither the row's category nor the instrument that settles it. The source is left
unread on that judgement, rather than forgotten.

**How a row says it took route 3.** Its `evidence` cell carries what every
`limitations` row carries — the [`fern-limitations.md`](fern-limitations.md) key
and its verdict, spelled from that file's own
[verdict vocabulary](fern-limitations.md#how-to-read-a-verdict) — and beside it
the words **`open-search probe`**, the outstanding source after
**`outstanding:`** together with what it did instead of answering, and the
statement that the row **stays convertible** to `golden`.

**What this rule replaced, and why the record stays.** The rule above is not the
one this document started with, and the difference is worth keeping visible for a
reader arriving at a row the old reading cannot explain. It used to close with
one sentence covering outcomes 1 and 2 together: a witness-supply probe
*"leaves this list the day any witness turns up, blocked or not, and it leaves as
a `FIXTURE` rather than as a measured probe."* Under it, a `FIXTURE` row whose
only real-world witness is outside the corpus's redistribution set, reachable at
no immutable ref, or refused by Fern could be settled by nothing at all: no
corpus row may pin it, because the document cannot be registered, and no probe
may measure it, because a witness was found. Nine rows of the ranked backlog
stood in exactly that state, and every further search put more there. Route 2 is
the way out of it and route 3 the way out of the same dead end on
`search-incomplete`; between them, twenty-four rows have taken those routes and
emptied the ranked backlog, which the eleven rows a later change *named* have
since refilled from the instrument's side rather than the corpus's. **Both routes buy a Fern verdict and cost the
parity evidence route 1 would have produced** — which is why the rule spends more
words on their gates than on route 1's, and why neither is the first thing to
reach for.

**Nothing else moves.** `golden` still beats `limitations` still beats `gap`; the
corpus still takes real-world specifications only; a probe is still never
proposed as a corpus fixture; and a probe still produces no byte-comparison
evidence. A row settled by route 2 or route 3 therefore carries a measured Fern
verdict and no crozier-versus-Fern parity evidence — that is the whole of what
these routes buy and the whole of what they cost.

**The gate reads all of it.** `RankedBacklogTests` in
[`../tests/surface_census_test.py`](../tests/surface_census_test.py) accepts a
row conforming to the above and refuses one settled with no recorded search, one
whose recorded search drops a source its region declares, one that names every
source but records no query against one or no result for one, one whose search
returned any outcome other than the two that license this route — a witness the
corpus can use, or no witness at all — one naming no blocker in any of the three
forms or naming a form without its payload, and one for which
[`fern-limitations.md`](fern-limitations.md) records no probe and no verdict,
which is the gate that keeps a row from being reclassified without the
measurement that settles it. It reads route 3 to the same standard, and refuses
a row taking it that names no outstanding source — either because its own
witness-search line records none as `unanswered`, or because its `evidence` cell
names none after `outstanding:` with what that source did instead of answering —
one that does not say the row stays convertible, one whose recorded search
returned `witness-found`, since route 1 is what settles that, and one for which
[`fern-limitations.md`](fern-limitations.md) records no probe and no verdict.

#### The rows, and how they are derived

The rows come out of the six region files with

```
grep -h 'witness.supply' docs/openapi-surface/*.md | grep -oP '^\| `?\K[a-z0-9-]+'
```

the same way the ledger keys do above, and that command is what the table below
is built from. It returns nothing today, and `grep` exits 1 on no match:
`RankedBacklogTests` runs it and holds its answer — empty or not — to the same
derivation taken off the `settlement` cells, so an emptied backlog is checked
rather than assumed and a row that keeps the marker phrase while moving to
`FIXTURE` still fails the gate.

**So this backlog's membership is provisional in a way the fixture backlog's is
not.** A row can leave it without any Fern run at all — `dollar-anchor` did,
moving to `FIXTURE` on a publisher-owned witness Fern accepts that the corpus may
not redistribute, and `format-relative-json-pointer` has since left the same way —
so a reader taking these rows as a fixed body of Fern measurements will
over-count the probe work by however many are waiting on a document rather than
on a probe. A row can also leave it *straight to `golden`*, which `dollar-comment`
did: its witness was redistributable, Fern accepted it, and registering it as
corpus row 109 settled the shape with a byte-matching golden rather than with a
probe. The last seven left it the third way, by being measured: Round 5 carried
each through Fern and recorded a verdict, and each is `limitations` today.

| key | region | spec location | the Fern measurement that settles it |
|---|---|---|---|
