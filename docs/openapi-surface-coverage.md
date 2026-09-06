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
`tests/fixtures/<name>/openapi.*` documents, and the 132 `link-ok` documents
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
`securityScheme.scheme`.

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
six, declared in `scripts/openapi-surface-census.py` and restated here, with a
drift gate over the pair:

- `operation.tags:multiple` — one per Operation Object whose `tags` array holds
  more than one member.
- `operation.operationId:duplicate` — one per Operation Object whose
  `operationId` value is declared by more than one Operation Object of the same
  document, so a value written twice counts two.
- `openapi.paths:normalized-collision` — one per Paths Object key that collides
  with at least one other key of the same document after path-template-name
  normalization, so a two-key collision counts two. The normalization is
  crozier's own — `naming::field_name` of `src/naming.rs`, the transform that
  gives a path parameter its Python name and so decides which routes
  `src/emit.rs` renders as one URL — applied to each `{expression}` and to
  nothing else, so `/users/{userId}` and `/users/{user_id}` collide while
  `/{id}/users` and `/users/{id}` do not.
- `openapi.paths:templated-key` — one per Paths Object key carrying at least one
  `{expression}` template expression, so a key with two counts one.
- `openapi.paths:several-template-expressions` — one per Paths Object key
  carrying more than one `{expression}` template expression, so a key with one
  counts none and a key with three counts one. The two are separate readings of
  the same key rather than one selector and a refinement of it: a key with
  exactly one expression is what tells them apart.
- `components.schemas:normalized-collision` — one per `components.schemas` key
  that collides with at least one other key of the same document after
  class-name normalization, so a two-key collision counts two. The normalization
  is again crozier's own — `naming::class_name` of `src/naming.rs`, the transform
  `src/ir.rs`'s `ref_to_class` gives a named schema and so the one that decides
  which components generate as one class — so `OBRate1_0` and `OB_Rate1_0`
  collide while `OBRate1` and `OBRate1_0` do not.

A predicate selector is a selector like any other everywhere else: `--selector`
accepts one, refuses a misspelling of one by name, and reports an undeclared one
as absent.

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

A conjunction has exactly one name: a group's members are written in
lexicographic order, except that the member a following `>` descends through is
written last, since that is the member the operator binds to. So an array schema
whose `items` declare a `oneOf` is `schema.type=array&schema.items>schema.oneOf`
and nothing else.

The **count rule is the one the grammar already has**: one per node at the
*leftmost* position — one per place the shape is written. So
`schema.items>schema.type=array` counts one per Schema Object whose `items` value
declares an array type, and `schema.discriminator&schema.oneOf` would count one
per Schema Object declaring both. A field holding several objects (a `oneOf`
list, a `properties` map) satisfies the members after the `>` when any one of
those objects does, which is what keeps the count one per leftmost node rather
than one per member.

**Which conjunctions are enumerable.** The operators can spell an unbounded set —
four schema fields alone make fifteen non-empty combinations before nesting, and
unbounded with it — so what bounds the list is not the grammar but the generator:

> A conjunction is worth enumerating **iff two source documents differing only in
> it take different paths through one of the six blind functions** of
> `src/ir.rs` — `resolve_schema_pointer`, `nested_array_element`,
> `hoist_union_variant`, `ref_to_class`, `prop_type_ref`, `path_group`.

The list is therefore read off those functions' own branch structure, one
selector per branch a document can select, and never off the cross-product of the
grammar: `nested_array_element` distinguishes seven shapes an `items` value can
be, where the cross-product of the four fields driving it would offer fifteen
before nesting. The code is the bound, and
[the case analysis below](#the-six-blind-regions-of-srcirrs-case-by-case) is the
derivation, branch by branch, of every entry and of every branch no selector kind
can express. Three conventions that derivation applies, stated once:

- **A function's entry gate is the leftmost member of each of its cases**, not a
  case of its own: two documents differing only in whether they write `items`
  differ in a *field*, which the grammar already names, rather than in a
  conjunction.
- **A branch's negative conjuncts are not spelled.** `items.reference.is_none()
  && items.ty == "array"` is named by its positive half; the negation is the
  complement of another case of the same function, and no selector kind can
  express a complement.
- **A branch reached through `x.or(y)` is two cases, not one.**
  `one_of.as_ref().or(&any_of)` is selected identically by a document that writes
  only `anyOf`, and a selector naming `schema.oneOf` does not count that document,
  so both spellings are declared. Where a second `or` sits inside the first the
  cases are their product; where the callee narrows one spelling away —
  `discriminated_union` returns `None` for a `discriminator` beside an `any_of` —
  only the surviving spelling is declared.
- **A selector is never narrower than the case it names.** A case is named by the
  positive shape a document writes, and where the branch narrows that shape by
  something no kind can express — an arity, a value's form — the selector stays
  the shape and the case row says what it does not carry. A selector *narrower*
  than its case would leave documents that select the branch uncounted, which is
  the same defect as naming only the `oneOf` spelling of an `or`; it is why
  `resolve_schema_pointer` is recorded as holes rather than covered by one
  continuation of each of its arms.

The conjunctions are themselves a closed list of 34, declared in
`scripts/openapi-surface-census.py` beside the predicate table and restated here,
with a drift gate over the pair:

- `schema.anyOf>schema.$ref` — one per Schema Object one of whose `anyOf`
  members is a Reference Object.
- `schema.anyOf>schema.allOf` — one per Schema Object one of whose `anyOf`
  members declares `allOf`.
- `schema.anyOf>schema.example&schema.type=object` — one per Schema Object one
  of whose `anyOf` members declares both an `example` and `type: object`.
- `schema.anyOf>schema.examples&schema.type=object` — one per Schema Object one
  of whose `anyOf` members declares both `examples` and `type: object`.
- `schema.anyOf>schema.properties` — one per Schema Object one of whose `anyOf`
  members declares `properties`.
- `schema.anyOf>schema.type=array&schema.items>schema.allOf` — one per Schema
  Object one of whose `anyOf` members declares `type: array` with an `items`
  value declaring `allOf`.
- `schema.anyOf>schema.type=array&schema.items>schema.anyOf` — one per Schema
  Object one of whose `anyOf` members declares `type: array` with an `items`
  value declaring `anyOf`.
- `schema.anyOf>schema.type=array&schema.items>schema.discriminator&schema.oneOf`
  — one per Schema Object one of whose `anyOf` members declares `type: array`
  with an `items` value declaring both a `discriminator` and a `oneOf`.
- `schema.anyOf>schema.type=array&schema.items>schema.oneOf` — one per Schema
  Object one of whose `anyOf` members declares `type: array` with an `items`
  value declaring `oneOf`.
- `schema.anyOf>schema.type=array&schema.items>schema.properties` — one per
  Schema Object one of whose `anyOf` members declares `type: array` with an
  `items` value declaring `properties`.
- `schema.items>schema.$ref` — one per Schema Object whose `items` value is a
  Reference Object.
- `schema.items>schema.allOf` — one per Schema Object whose `items` value
  declares `allOf`.
- `schema.items>schema.anyOf` — one per Schema Object whose `items` value
  declares `anyOf`.
- `schema.items>schema.discriminator&schema.oneOf` — one per Schema Object
  whose `items` value declares both a `discriminator` and a `oneOf`.
- `schema.items>schema.oneOf` — one per Schema Object whose `items` value
  declares `oneOf`.
- `schema.items>schema.properties` — one per Schema Object whose `items` value
  declares `properties`.
- `schema.items>schema.type=array` — one per Schema Object whose `items` value
  declares `type: array`.
- `schema.oneOf>schema.$ref` — one per Schema Object one of whose `oneOf`
  members is a Reference Object.
- `schema.oneOf>schema.allOf` — one per Schema Object one of whose `oneOf`
  members declares `allOf`.
- `schema.oneOf>schema.example&schema.type=object` — one per Schema Object one
  of whose `oneOf` members declares both an `example` and `type: object`.
- `schema.oneOf>schema.examples&schema.type=object` — one per Schema Object one
  of whose `oneOf` members declares both `examples` and `type: object`.
- `schema.oneOf>schema.properties` — one per Schema Object one of whose `oneOf`
  members declares `properties`.
- `schema.oneOf>schema.type=array&schema.items>schema.allOf` — one per Schema
  Object one of whose `oneOf` members declares `type: array` with an `items`
  value declaring `allOf`.
- `schema.oneOf>schema.type=array&schema.items>schema.anyOf` — one per Schema
  Object one of whose `oneOf` members declares `type: array` with an `items`
  value declaring `anyOf`.
- `schema.oneOf>schema.type=array&schema.items>schema.discriminator&schema.oneOf`
  — one per Schema Object one of whose `oneOf` members declares `type: array`
  with an `items` value declaring both a `discriminator` and a `oneOf`.
- `schema.oneOf>schema.type=array&schema.items>schema.oneOf` — one per Schema
  Object one of whose `oneOf` members declares `type: array` with an `items`
  value declaring `oneOf`.
- `schema.oneOf>schema.type=array&schema.items>schema.properties` — one per
  Schema Object one of whose `oneOf` members declares `type: array` with an
  `items` value declaring `properties`.
- `schema.properties>schema.allOf` — one per Schema Object one of whose
  properties declares `allOf`.
- `schema.properties>schema.anyOf` — one per Schema Object one of whose
  properties declares `anyOf`.
- `schema.properties>schema.discriminator&schema.oneOf` — one per Schema Object
  one of whose properties declares both a `discriminator` and a `oneOf`.
- `schema.properties>schema.enum` — one per Schema Object one of whose
  properties declares `enum`.
- `schema.properties>schema.oneOf` — one per Schema Object one of whose
  properties declares `oneOf`.
- `schema.properties>schema.properties` — one per Schema Object one of whose
  properties declares `properties`.
- `schema.properties>schema.type=array` — one per Schema Object one of whose
  properties declares `type: array`.

A conjunction selector is a selector like any other everywhere else: `--selector`
accepts one, refuses a misspelling of one by name — and refuses a well-formed
combination nobody declared, because the list is closed by the code rather than
by the operators — and reports an undeclared one as absent.

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
  It reads **164** registered sources, of which
  **147** carry a committed golden. `document-paths`'s own evidence cells are
  transcribed from that walk; the other five region files' cells are still dated
  to the earlier walks each was taken on, and refreshing them is each file's own
  measurement against this same pin. No classification in this section depends on
  which walk a cell was taken from — a category moves only when a source is
  registered or a selector is added, and both are recorded in that section's own
  history.
- **`just fixtures-coverage`**, for criterion 2 alone. That recipe is outside
  `just check` — it needs network and runs the corpus instrumented — so its
  per-file counts are a dated snapshot (2026-08-25), stated once, in the join
  table under
  [The ranked list against `golden blind spots`](#the-ranked-list-against-golden-blind-spots).
  The gate cannot produce that measurement, but it does reconcile against it:
  see [Refreshing the coverage snapshot](#refreshing-the-coverage-snapshot).

What this section takes from the six region files, `RankedBacklogTests` in
`tests/surface_census_test.py` takes back from them — the per-region counts and
the totals narrated from them, both backlogs' membership and their stated sizes, each ranked row's
owning region, criterion 1 and the rubric order and median it produces. `just
check` runs it offline, so a region row added, reclassified or re-measured fails
the gate here rather than leaving this section quietly stale. Criteria 3 and 4
are the two the gate cannot take back, because the region files publish no number
for either; each bullet below says where its number comes from.

### What the walk enumerated

| region | features | `golden` | `limitations` | `gap` | `FIXTURE` | `PROBE` | `UNREACHABLE` |
|---|---:|---:|---:|---:|---:|---:|---:|
| [`parameters`](openapi-surface/parameters.md) | 70 | 49 | 14 | 7 | 7 | 0 | 0 |
| [`schemas`](openapi-surface/schemas.md) | 117 | 93 | 8 | 16 | 13 | 0 | 3 |
| [`bodies-media`](openapi-surface/bodies-media.md) | 47 | 36 | 11 | 0 | 0 | 0 | 0 |
| [`security`](openapi-surface/security.md) | 50 | 37 | 8 | 5 | 5 | 0 | 0 |
| [`document-paths`](openapi-surface/document-paths.md) | 67 | 62 | 5 | 0 | 0 | 0 | 0 |
| [`oas31-extensions`](openapi-surface/oas31-extensions.md) | 52 | 33 | 1 | 18 | 1 | 0 | 17 |
| **total** | **403** | **310** | **47** | **46** | **26** | **0** | **20** |

The walk enumerated **403** features and landed each in exactly one category:
**310** `golden`, **47** `limitations`, **46** `gap`. The `gap` column splits by
settlement class into **26** `FIXTURE`, **0** `PROBE` and **20** `UNREACHABLE`.

**What the `gap` count means.** 46 is the number of OpenAPI shapes for which
crozier's behaviour is vouched for by nothing but crozier: no committed golden's
source declares the shape, so no byte comparison against Fern touches it, and
[`fern-limitations.md`](fern-limitations.md) has never measured Fern on it, so
nothing contradicts whatever crozier does. `just check` is green over all 46
either way. It is not a defect count — 20 of them (`UNREACHABLE`) have no
position in a generated Python SDK at all, and saying so is their settlement.
The two backlogs below are the other 26.

### Reconciliation

**Each feature is classified exactly once.** The 403 rows carry 403 distinct
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

**Every ledger key is accounted for.** The canonical join reports 63 keys, of
which 59 are a region row's key verbatim. The other four:

| ledger key | how it is accounted for |
|---|---|
| `status_code` | **Not a feature key.** It is a row label inside the ledger's 407/421 probe table, which the join's `\| key \| N \|` shape matches by accident — the `bodies-media` region's method notes say the same. The join's real yield is 62. |
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

**No region's category is overturned.** This node re-derived the census join, the
ledger join and the site counts it ranks on, and found no row whose `category` or
`settlement` cell it would change.

### The ranked `FIXTURE` backlog

**Pinned from this backlog:** [`header-allow-empty-value`](openapi-surface/parameters.md)
is pinned by corpus row 94, `ndw-accessibility-map`; its two Header Objects declare
the field and its Fern 5.20.0 golden byte-matches with no exclusions.

The two highest-ranked entries stayed, and the issue #188 witness search
[the `parameters` region records](openapi-surface/parameters.md#witness-search-issue-188)
replaces the earlier GitHub-only look with a seven-source sweep and a measured
reason for each. `header-allow-reserved` reads `witness-blocked`: exactly two
declaring files exist anywhere the sweep reaches and both are synthetic, because
`allowReserved` is defined for query parameters and a Header Object carrying it
is a reader test. `header-deprecated` reads `fern-rejected`: a real API's own
description declares it — the openEHR EHR API — and Fern refuses that document,
as it refuses the only other real declarer. Neither is settled here; each row's
own region-file cell carries that evidence, and `probe-backlog` works from it.
`header-content` was the third and left this backlog on corpus row 121.

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
`parameter-style-simple-header-scalar` beside row 115. Two recorded alternates are
**not** registered and each is refused on its own record rather than for
redundancy: Setu is a generated composite the fixture ledger disqualifies, and
LORIS is `GPL-3.0`, outside the corpus's redistribution set.

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

[`parameter-style-pipedelimited-query-scalar`](openapi-surface/parameters.md) is
the one row of that batch that stayed. Its recorded witness — AlayaCare's Billable
Item Management API, CC0-1.0 at an immutable ref — was put to Fern for
registration and met the *exit-0-and-nothing-happened* refusal
[`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md) names: `fern check`
and the 5.20.0 generate both exit 0 over a document Fern never parsed, and the
tree it wrote is an empty SDK. The document is logged REJECTED there, the row
carries that evidence, and the only other declarer the search found is `GPL-3.0`.

[`dollar-comment`](openapi-surface/schemas.md) never reached this backlog: it was
a `PROBE` until the issue #188 search found it a publisher-owned, Apache-2.0
witness, and the change that settled it registered that witness as corpus row 109,
`volview-backend-contract`, whose two `$comment` declarations and byte-matching
Fern 5.20.0 golden make the row `golden` outright.
[`format-relative-json-pointer`](openapi-surface/schemas.md) arrives here from the
other direction: the same search found it a publisher-owned witness Fern accepts
whose licence is proprietary, and a witness blocked on redistribution puts the row
in this backlog rather than the probe one. Under
[the amended rule](#the-settlement-rule-as-amended) a blocked witness now also
licenses a probe that would settle the row as `limitations`; this row has not
taken that route.

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

All 26 `FIXTURE` gaps remaining across the six regions, in one total order, by [the ranking
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
  can only score above zero here from a source with no committed golden, which is
what makes it a gap — 25 of the 26 score zero, and the one that does not names
  its one source in that cell.

**The median blind-spot count of this list is 0** — 19 of the 26 entries name no
`src/` file at all, which is also why they win criterion 1 outright.

| # | key | region | 1. crozier sites | 2. blind spots | 3. artifacts | 4. witnesses |
|---|---|---|---|---|---|---|
| 1 | [`header-allow-reserved`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 2 | [`header-deprecated`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 3 | [`reference-summary`](openapi-surface/oas31-extensions.md) | `oas31-extensions` | **0** (none) | **0** (no `src/` file) | **3** (types/, client.py, reference.md) | **0** |
| 4 | [`securityscheme-ref`](openapi-surface/security.md) | `security` | **0** (none) | **0** (no `src/` file) | **2** (client.py, core/) | **0** |
| 5 | [`parameter-style-matrix-path-scalar`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **1** (raw_client.py) | **1** |
| 6 | [`contains`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 7 | [`dependent-schemas`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 8 | [`dollar-anchor`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 9 | [`format-idn-email`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 10 | [`format-idn-hostname`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 11 | [`format-ipv6`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 12 | [`format-iri`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 13 | [`format-iri-reference`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 14 | [`format-relative-json-pointer`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 15 | [`max-contains`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 16 | [`min-contains`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 17 | [`multiple-of`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 18 | [`parameter-style-simple-path-object`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **1** (raw_client.py) | **0** |
| 19 | [`unevaluated-items`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 20 | [`parameter-style-form-cookie-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 21 | [`parameter-style-pipedelimited-query-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 22 | [`parameter-style-spacedelimited-query-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 23 | [`http-hoba`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 24 | [`http-oauth`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 25 | [`http-scram-sha-1`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 26 | [`http-scram-sha-256`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |

### The ranked list against `golden blind spots`

[`tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md#where-the-goldens-are-blind--just-fixtures-coverage)
calls the `golden blind spots` block "the fixture backlog", and it is — the same
backlog as the table above, expressed per `src/` file instead of per feature. The
two are joined below, in the report's own columns: **printed** is the count
`just fixtures-coverage` prints for the file and the one criterion 2 ranks on,
and **by tier** is the breakdown it prints beside it. Printed sums the two
non-golden tiers, so a region both tiers reach counts twice — the report's own
`total 1510 region(s) across 12 file(s)` line is the de-duplicated union, and the
functions named in each verdict are counted from that union.

| `src/` file | printed | by tier | ranked gaps pointing at it | verdict |
|---|---:|---:|---|---|
| `src/settings.rs` | 864 | all-e2e 434, non-e2e 430 | none | **Neither.** `explain` 148, `resolve` 44, `merge` 37, `merge_generator` 28, `load` 21, `read_config` 20: the CLI > env > `crozier.yml` layering behind `crozier config`. No OpenAPI shape reaches it and no Fern golden can — Fern reads a different config format — so neither a corpus row nor a Fern probe is the instrument. The journeys are, and they already reach 434 of the 448. |
| `src/openapi.rs` | 511 | all-e2e 221, non-e2e 290 | 4 — #23 `http-hoba`, #24 `http-oauth`, #25 `http-scram-sha-1`, #26 `http-scram-sha-256` | **Agrees, and accounts for the rest.** #23–#26 — `http-hoba`, `http-oauth`, `http-scram-sha-1` and `http-scram-sha-256` — are one `#[serde(other)]` scheme fallback arm, four IANA scheme members that collapse through it. `normalize_parameters`, 3 regions, was a fifth until corpus row 122 settled `operation-overrides-path-item-parameter` `golden` and it left the ranked list, and the `operation_id` field declaration was a sixth until corpus row 128 settled `duplicate-operation-id` the same way. The largest block, `filter_ignored` 72, is the walk's `x-fern-or-crozier-ignore` — now `golden`, on corpus row 108's four `x-fern-ignore` operations, though golden-classified is not golden-*exhausted*: one witness reaches the Operation-Object arm and leaves the schema arm and the `x-crozier-*` precedence to unit tests. `filter_by_audience` 47 + `audiences` 8 belong to `audience-dual-header-policy`, classified `golden`: golden-classified is not golden-*exhausted*, since the two audience goldens declare 8 sites between them and leave the rest of the branch space to unit tests. `collect_schema_refs` 46 + `expand_schema_closure` 32 + `operation_schema_seed` 24 is `$ref`-closure pruning under `reference-ref` (`golden`); `load` 26 + `visit_seq` 7 + `de_composition` 5 are malformed-document deserialization paths the corpus excludes by taking only documents Fern generates. |
| `src/cli.rs` | 292 | all-e2e 133, non-e2e 159 | none | **Neither**, as `src/settings.rs`: `do_config` 60, `run` 43, `do_init` 26, `do_generate` 12 are the command surface, not document behaviour. |
| `src/emit.rs` | 261 | all-e2e 29, non-e2e 232 | none | **A shape the walk missed.** The one ranked gap that pointed here, `media-type-range`, named `append_request_call_args` — which is not among the blind regions at all — and corpus row 127 has since settled it `golden`. The blind regions are example rendering — `raw_type_str_ctx` 40, `example_matches_type` 24, `build_example_inner` 23, `named_value_inner` 13, `value_from_example` 12, `example_from_json` 6 — and streaming docstrings, `client_stream_docstring` 11 + `raw_stream_docstring` 10. Every `example`/`examples` field is classified `golden`, but the walk enumerates the *field*; those branches switch on the JSON value *kind* an example holds, and example values are not in the grammar's closed list of valued selectors, so no `gap` row could have named them. |
| `src/ir.rs` | 201 | all-e2e 9, non-e2e 192 | 7 — #20–#26 | **Agrees on the file, misses the shapes.** The blind regions are type-lowering conjunctions: `resolve_schema_pointer` 25, `nested_array_element` 25, `hoist_union_variant` 24, `ref_to_class` 22, `prop_type_ref` 20, `path_group` 15. Each driving field — `$ref`, `items`, `oneOf`, `properties` — is `golden` on its own; it is their *combinations* that no golden reaches, and the census emitted one selector per field and none per conjunction until the [conjunction selectors](#the-selector-grammar) were declared off these six functions' own branches ([case by case](#the-six-blind-regions-of-srcirrs-case-by-case)) — naming the shapes, which is what makes them classifiable, not what classifies them. Two regions built bespoke conjunction passes for exactly this reason (`parameters`' style × `in` × schema matrix, `schemas`' variant scan); nobody ran one over schema-composition combinations. |
| `src/refs.rs` | 74 | all-e2e 17, non-e2e 57 | none | **Only a probe can settle it.** `resolve_reference` 16, `document` 10, `pointer` 9, `error` 7, `curl_fetch` 7 are the cross-document `$ref` path. The corpus is single-document by construction ([`matching.md`](matching.md#cross-document-ref-resolution-issue-77)), and the ledger's `relative-file-ref` row is already `discards + pipeline` — its own note being that crozier's fixture pipeline cannot register the tree that would make the reference resolve. No corpus row is in reach. |
| `src/schema.rs` | 46 | all-e2e 23, non-e2e 23 | none | **Neither.** `build` 20 emits crozier's own config JSON Schema. |
| `src/lib.rs` | 33 | all-e2e 1, non-e2e 32 | none | **Neither.** `render_files` 29 is the filesystem write path. |
| `src/naming.rs` | 31 | all-e2e 8, non-e2e 23 | none | **A shape the walk missed, and the half of it that is now enumerated.** `digit_word` 10, `enum_words` 7, `numeric_enum_identifier` 2, `finalize_enum_ident` 2, `sanitize_identifier` 1 are driven by OpenAPI *names* — schema names, enum member spellings — which the grammar excludes as map keys that are names. The schema-name half is no longer unreachable: `components.schemas:normalized-collision` is a predicate selector over exactly those keys, and it is what made `normalization-collision` enumerable above. What still has no selector is the enum-member spellings, which is where four of these five regions sit — a predicate over `schema.enum` members would reach them, and none is declared. |
| `src/config.rs` | 31 | all-e2e 13, non-e2e 18 | none | **Neither.** `default_package_name` 10 and `new` 8 are generator-config defaults. |
| `src/pyfmt.rs` | 24 | all-e2e 0, non-e2e 24 | none | **Neither.** `format_source` 24 is the `ruff format` shell-out and its failure paths. |
| `src/main.rs` | 6 | all-e2e 6, non-e2e 0 | none | **Neither.** The binary entry point; `just test-fixtures-coverage` asserts it is reachable at all. |

**Where the two backlogs agree.** Both name `src/ir.rs` and `src/openapi.rs` —
every `src/` file any ranked gap points at is one the blind-spot block also
lists, and in the same order of size (`openapi.rs` 511 > `ir.rs` 201). `emit.rs`
was a third until corpus row 127 settled `media-type-range`. Ranking on criterion
2 therefore does not fight the repository's own measurement; it refines it,
because 19 of the 26 ranked entries reach no `src/` file at all and so are
invisible to a per-file view.

**Where they do not.** The two largest files no ranked gap points at,
`src/settings.rs` and `src/cli.rs`, together 1,156 of the block's 2,374 printed
regions — almost half of it — hold no OpenAPI-derived code, so the fixture
backlog can never shorten
them and a reader taking the block at face value as "the fixture backlog" will
mis-prioritise. Nine of the twelve files have no ranked gap pointing at them: one
(`src/refs.rs`) is a region only a probe can settle, one (`src/naming.rs`) is a
shape the walk missed, and the remaining seven are outside the walk's subject
entirely — they carry no OpenAPI-derived code, so neither a fixture nor a probe
is their instrument.

### The six blind regions of `src/ir.rs`, case by case

The join table's `src/ir.rs` verdict names six functions the goldens never reach
and says why the walk could not name them: *"it is their combinations that no
golden reaches, and the census emits one selector per field and none per
conjunction."* It now emits one per conjunction, and this is the derivation —
every branch of each of those six functions a source document can select, under
[the enumeration rule](#the-selector-grammar), quoting the function and the case
it distinguishes.

**Every case below is in exactly one of two states.** It carries exactly one
selector from the closed list of 34, or it is recorded as an enumeration hole
naming the property no selector kind can express and what closing it would take —
the way `normalization-collision` was recorded before `components.schemas:normalized-collision`
existed. No case is in neither, and none is in both.

| hole | what no selector kind can express | what closing it would take |
|---|---|---|
| **H-residual** | a function's residual arm is selected by the *absence* of every case above it | a negation operator over a group's members, deliberately absent: a complement is not a shape a document declares |
| **H-arity** | the *number* of members a composition field declares — `let [member] = schema.all_of…as_slice()`, `non_null.len() == 1` | a predicate over a composition field's length (`schema.allOf:sole-member`, `schema.oneOf:sole-non-null-member`), of the family `operation.tags:multiple` already is |
| **H-boolean-value** | which *boolean* a schema-or-boolean field was written with — `is_inline_struct`'s `AdditionalProperties::Bool(false)` arm | `schema.additionalProperties` added to the closed list of valued fields for its boolean spelling |
| **H-inferred-discriminant** | that a union's members each carry a property whose value is a one-member `enum`, which is the discriminant `inferred_union_discriminant_property` finds with no `discriminator` field written | a predicate comparing the members of one `oneOf` against each other, of the family `operation.operationId:duplicate` already is |
| **H-ref-target** | the shape of the schema a `$ref` *points at*: the walk counts a Reference Object and never descends | a resolving walk, which is a different instrument — the target's own declaration site is already counted where it is written |
| **H-pointer-form** | the segment structure of a `$ref` *value*, as in `#/components/schemas/A/allOf/0/properties/b` | a predicate family over `schema.$ref` (`:components-schemas-pointer`, `:nested-properties`, `:nested-items`, `:composition-index`, `:foreign-pointer`), of the family the three `openapi.paths:` predicates already are over a key's shape |
| **H-pointer-nesting** | that a `$ref` value's segment sequence addresses the nesting a schema declares: each arm's schema-side half is already named by a plain field selector (`schema.allOf`, `schema.properties`, `schema.items`), and what no kind can express is the *correspondence* between the two, which is a joint property of a value and the document it points into | the `schema.$ref` pointer-form predicate family H-pointer-form names, evaluated against the resolving walk H-ref-target names — both together, and neither is a conjunction over one node's declared fields |
| **H-pointer-target** | whether a `$ref` value names a key `components.schemas` declares | a predicate comparing one document's `$ref` values against its own component names, of the family `components.schemas:normalized-collision` already is |
| **H-key-segment-position** | *which* segment of a Paths Object key carries a template expression | a predicate `openapi.paths:leading-template-segment`, of the family the three `openapi.paths:` predicates already are |
| **H-key-all-templated** | that *every* segment of a Paths Object key is a template expression | a predicate `openapi.paths:all-segments-templated`, same family |

Declaring any of those predicates is a change to the *predicate* list, not to the
conjunction list this section derives; each hole says which one it would take, so
the next node reads the work off the row rather than rediscovering it.

#### `resolve_schema_pointer`

Every branch here is selected by the pointer *string* — `match part` reads a
segment of the `$ref` value, never a field of the document — and each arm then
resolves only where the schema at that position declares the field that segment
names, with that index or key. The schema-side half of every arm is therefore a
single field the grammar already names (`schema.allOf`, `schema.oneOf`,
`schema.anyOf`, `schema.properties`, `schema.items`); what is unnamed is the
correspondence between a `$ref` value's segments and the nesting they address,
which is a joint property of a value and the document it points into rather than
a combination of fields at one node. A conjunction such as
`schema.allOf>schema.properties` would name *one* continuation of the `"allOf"`
arm — the pointer that goes on to `properties` — and would leave
`allOf/{i}/items`, `allOf/{i}/oneOf/{j}`, a bare `allOf/{i}` and every deeper form
uncounted, so this region is recorded as holes rather than covered by a narrower
shape.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1 | `reference.strip_prefix("#/components/schemas/")?` — the reference is not a component-schema pointer | **H-pointer-form** |
| 2 | `schemas.get(parts.next()?)?` — the pointer's head names no declared component | **H-pointer-target** |
| 3 | `"allOf" => schema.all_of.as_ref()?.get(parts.next()?.parse::<usize>().ok()?)?` — schema-side half `schema.allOf`, entered for any continuation | **H-pointer-nesting** |
| 4 | `"oneOf" => schema.one_of.as_ref()?.get(…)?` — schema-side half `schema.oneOf` | **H-pointer-nesting** |
| 5 | `"anyOf" => schema.any_of.as_ref()?.get(…)?` — schema-side half `schema.anyOf` | **H-pointer-nesting** |
| 6 | `"properties" => schema.properties.get(parts.next()?)?` — schema-side half `schema.properties`, keyed by a property *name*, which the count rule excludes | **H-pointer-nesting** |
| 7 | `"items" => schema.items.as_deref()?` — schema-side half `schema.items` | **H-pointer-nesting** |
| 8 | `_ => return None` — a segment none of the five names | **H-pointer-form** |

#### `nested_array_element`

Its entry gate is `let items = array.items.as_deref()?`, carried as the leftmost
member `schema.items` of every case rather than listed as a case of its own.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1 | `items.reference.is_none() && items.ty…primary() == Some("array")` — the recursive nested-array descent | `schema.items>schema.type=array` |
| 2 | `self.discriminated_union(&name, &module, items, …)` returning `Some` on an `items` writing an explicit `discriminator`; the callee returns `None` for a `discriminator` beside an `any_of`, so only the `oneOf` spelling survives | `schema.items>schema.discriminator&schema.oneOf` |
| 3 | the same arm on an `items` writing no `discriminator`, either spelling, where the discriminant is inferred from the members | **H-inferred-discriminant** |
| 4 | `if items.reference.is_some() { return None; }` | `schema.items>schema.$ref` |
| 5 | `is_inline_struct(items)` → `add_object`, on an `items` declaring `properties` | `schema.items>schema.properties` |
| 6 | the same arm on an `items` declaring `allOf` | `schema.items>schema.allOf` |
| 7 | the same arm on an `items` declaring `additionalProperties: false` | **H-boolean-value** |
| 8 | `items.one_of.as_ref().or(items.any_of.as_ref())` → the hoisted union alias, `oneOf` spelling | `schema.items>schema.oneOf` |
| 9 | the same arm, `anyOf` spelling: an `items` declaring only `anyOf` reaches it identically | `schema.items>schema.anyOf` |
| 10 | the closing `None` | **H-residual** |

#### `hoist_union_variant`

Every caller reaches it through `one_of.as_ref().or(any_of.as_ref())` — the
named-schema, response and request-body hoisters, `prop_type_ref`, and its own
recursion — so a document declaring only `anyOf` selects every case below exactly
as one declaring `oneOf` does. Each case is therefore two, `schema.oneOf` and
`schema.anyOf` at the head, and where the arm reads a second `or` the cases are
the product of the two.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1 | `if let Some(reference) = &variant.reference` — the variant is a Reference Object, `oneOf` head | `schema.oneOf>schema.$ref` |
| 2 | the same arm, `anyOf` head | `schema.anyOf>schema.$ref` |
| 3 | `if let Some(member) = simple_nullable_member(item)` — one element member beside `type: null`, typed `List[Optional[…]]`; either head, and the callee reads its own `any_of.as_ref().or(one_of.as_ref())` | **H-arity** |
| 4 | an array variant whose item composes, `hoist_discriminated_union(&item_name, item, …)` returning `Some`; the callee needs the item's `one_of`, so the inner spelling is fixed — `oneOf` head | `schema.oneOf>schema.type=array&schema.items>schema.discriminator&schema.oneOf` |
| 5 | the same arm, `anyOf` head | `schema.anyOf>schema.type=array&schema.items>schema.discriminator&schema.oneOf` |
| 6 | the same item falling through to the `TypeDecl::Alias` union over `item.one_of.as_ref().or(item.any_of.as_ref())` — `oneOf` head, `oneOf` item | `schema.oneOf>schema.type=array&schema.items>schema.oneOf` |
| 7 | the same arm, `oneOf` head, `anyOf` item | `schema.oneOf>schema.type=array&schema.items>schema.anyOf` |
| 8 | the same arm, `anyOf` head, `oneOf` item | `schema.anyOf>schema.type=array&schema.items>schema.oneOf` |
| 9 | the same arm, `anyOf` head, `anyOf` item | `schema.anyOf>schema.type=array&schema.items>schema.anyOf` |
| 10 | `described_all_of_ref(item)` resolving → `hoist_named_copy` of the annotated `$ref`, `oneOf` head | `schema.oneOf>schema.type=array&schema.items>schema.allOf` |
| 11 | the same arm, `anyOf` head | `schema.anyOf>schema.type=array&schema.items>schema.allOf` |
| 12 | `item.reference.is_none() && is_inline_struct(item)` → `hoist_object`, `oneOf` head | `schema.oneOf>schema.type=array&schema.items>schema.properties` |
| 13 | the same arm, `anyOf` head | `schema.anyOf>schema.type=array&schema.items>schema.properties` |
| 14 | `is_inline_object(variant)` → `hoist_object`, on a variant declaring `properties`, `oneOf` head | `schema.oneOf>schema.properties` |
| 15 | the same arm, `anyOf` head | `schema.anyOf>schema.properties` |
| 16 | the same arm on a variant declaring `allOf`, `oneOf` head | `schema.oneOf>schema.allOf` |
| 17 | the same arm, `anyOf` head | `schema.anyOf>schema.allOf` |
| 18 | `is_bare_object(variant) && schema_example(variant).is_some_and(…)` where `schema_example` reads `schema.example`, `oneOf` head | `schema.oneOf>schema.example&schema.type=object` |
| 19 | the same arm, `anyOf` head | `schema.anyOf>schema.example&schema.type=object` |
| 20 | the same arm where `schema_example` falls to its `.or_else(… schema.examples.first())`, `oneOf` head | `schema.oneOf>schema.examples&schema.type=object` |
| 21 | the same arm, `anyOf` head | `schema.anyOf>schema.examples&schema.type=object` |
| 22 | the closing `base_type_ref(variant)` | **H-residual** |

#### `prop_type_ref`

It is called on each member of `properties`, so `schema.properties` is the
leftmost member of every case.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1 | the outer `if let (Some(schemas), Some((reference, description))) = (self.schemas, described_all_of_ref(prop_schema))` gate | `schema.properties>schema.allOf` |
| 2 | inside it, `if let Some(values) = string_enum_values(&target)` → a hoisted enum | **H-ref-target** |
| 3 | inside it, `if target.one_of.is_some() \|\| target.any_of.is_some()` → `hoist_named_copy` | **H-ref-target** |
| 4 | inside it, `!is_map(&target) && !is_bare_object(&target) && …` → `hoist_object_with_doc` | **H-ref-target** |
| 5 | inside it, the closing `full_type_ref_resolved(&target, schemas)` | **H-ref-target** |
| 6 | `if let Some(member) = sole_inline_all_of(prop_schema)` — one inline `allOf` member and nothing else declared | **H-arity** |
| 7 | `string_enum_values(prop_schema)` → a hoisted enum | `schema.properties>schema.enum` |
| 8 | `prop_schema.reference.is_none() && is_inline_struct(prop_schema)` → `hoist_object` | `schema.properties>schema.properties` |
| 9 | `if let Some(members) = prop_schema.one_of.as_ref().or(prop_schema.any_of.as_ref())` — the composition gate, `oneOf` spelling | `schema.properties>schema.oneOf` |
| 10 | the same gate, `anyOf` spelling: a property declaring only `anyOf` reaches every arm below it identically | `schema.properties>schema.anyOf` |
| 11 | inside it, `non_null.len() == 1 && non_null.len() != members.len()` — the nullable pair collapsing to its one member | **H-arity** |
| 12 | inside it, `members.len() == 1 && is_inline_struct(&members[0])` | **H-arity** |
| 13 | inside it, `if let Some(union) = self.hoist_discriminated_union(&name, prop_schema, …)`; the callee returns `None` for a `discriminator` beside an `any_of`, so only the `oneOf` spelling survives | `schema.properties>schema.discriminator&schema.oneOf` |
| 14 | inside it, the closing alias over the members left after `is_null_variant` filtering | **H-residual** |
| 15 | `prop_schema.ty…primary() == Some("array")` → `hoist_array_item_type` | `schema.properties>schema.type=array` |
| 16 | the closing `base_type_ref(prop_schema)` | **H-residual** |

#### `ref_to_class`

Wholly an enumeration hole, and routed there rather than left underived: the
function opens no schema — it reads the reference *string* and nothing else — so
no conjunction over declared fields changes its path, and every one of its cases
is decided by the pointer's segment structure, which is what a predicate selector
is for and which the grammar declares none over.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1 | `let Some(pointer) = reference.strip_prefix("#/components/schemas/") else { … }` — a foreign pointer, named off its last segment | **H-pointer-form** |
| 2 | `"properties" if index + 1 < parts.len() => name.push_str(&naming::class_name(parts[index + 1]))` | **H-pointer-form** |
| 3 | `"items" => name.push_str("Item")` | **H-pointer-form** |
| 4 | `"allOf" \| "oneOf" \| "anyOf" => index += 2` — a composition index contributes no name | **H-pointer-form** |
| 5 | `_ => index += 1` | **H-pointer-form** |

#### `path_group`

Wholly an enumeration hole for the same reason: it reads the request URL and
opens no schema. `openapi.paths:templated-key` says a key carries a template
expression and `openapi.paths:several-template-expressions` says it carries more
than one; neither says *which* segment carries it or whether all of them do,
which is the only thing this function reads.

| # | the branch it distinguishes | selector or hole |
|---|---|---|
| 1 | `.find(\|s\| !(s.starts_with('{') && s.ends_with('}')))` returning the key's first segment | **H-key-segment-position** |
| 2 | the same `find` returning a later segment, having skipped a templated one | **H-key-segment-position** |
| 3 | `.unwrap_or("service")` — every segment is templated, or the URL has none | **H-key-all-templated** |

**What this section does not do.** It declares selectors and adds no row to any
region file: every category, every settlement and every published total is what
it was. Naming a shape is what makes it classifiable, not what classifies it —
the census can now answer for these conjunctions, and what the answers mean for
the six region files is the next node's work.

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
and the two-largest-files figure below against the `printed` column it sums, so
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
so a corpus row settles either outright. Both are `FIXTURE` gaps above, ranked
#40 and #5.

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

**What a found witness settles.** The bar above is narrower than it first reads:
a witness the search *did* find does not leave a row here on witness-supply
grounds, however unusable that document turns out to be. What it leaves *as*
depends on why it is unusable, and a search returns one of five outcomes.

1. **`witness-found`** — a real-world document declares the shape, at an
   immutable ref, under a redistribution-compatible licence, and Fern accepts it.
   The row becomes `FIXTURE`, and retires outright to `golden` the moment that
   document is registered: `dollar-comment` did exactly that, as corpus row 109.
2. **`witness-blocked`** or **`fern-rejected`** — such a document exists and this
   corpus cannot use it: outside its redistribution set, reachable at no
   immutable ref, or refused by Fern. The row still becomes `FIXTURE`, because
   the search proved the shape has a real-world witness and what is short is that
   document rather than the world — which is what `dollar-anchor` records.
   **Amended:** such a row may *instead* be settled by a locally authored Fern
   probe recorded in [`fern-limitations.md`](fern-limitations.md), at which point
   its category here becomes `limitations` under
   [the classification precedence](#the-category-rules). The three properties
   that route carries are stated below.
3. **`none-found`** — no document reaching that bar was found anywhere the
   region's declared sources reach. The row stays here as a witness-supply probe.
   This is the case the rule already covered and the amendment does not touch it.
4. **`search-incomplete`** — **the outcome the amendment adds**, for a search a
   required source did not answer: the registry was unreachable, the query was
   refused, the index returned an error rather than a result. The row says so in
   that source's own segment of its `sources searched and the exact query used
   against each` cell, with the word `unanswered` beside what the source did
   instead of answering, so the record names what is outstanding. It says the
   world was not fully asked and therefore leaves the row's question **open**: it
   is the one outcome that settles nothing and licenses no route above. A record
   marking a required source `unanswered` reads `search-incomplete` rather than
   `none-found`, and the reconciliation refuses that pairing — which is what
   keeps an unread source from becoming evidence of absence. No row in the tree
   reads it today.

**This is an amendment, and this is what it replaced.** The rule used to close
with one sentence covering outcomes 1 and 2 together: a witness-supply probe
*"leaves this list the day any witness turns up, blocked or not, and it leaves as
a `FIXTURE` rather than as a measured probe."* Under it, a `FIXTURE` row whose
only real-world witness is outside the corpus's redistribution set, reachable at
no immutable ref, or refused by Fern could be settled by nothing at all: no
corpus row may pin it, because the document cannot be registered, and no probe
may measure it, because a witness was found. Nine rows of the ranked backlog
already stand in exactly that state, and every further search puts more there.
Route 2 above is the one way out of it, and it is the whole of the change.

**The recorded exhaustive search is the gate.** Route 2 is never a shortcut past
searching, and its gate is a property of this repository rather than of anything
outside it. A row is eligible only where **its own region file** records a search
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

**The row stays convertible, so it names its blocker.** A row settled this way
records that a real witness exists and names precisely what stops that witness
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

**How a row says it took this route.** Its `evidence` cell carries what every
`limitations` row carries — the [`fern-limitations.md`](fern-limitations.md) key
and its verdict — and beside it the words **`blocked-witness probe`**, the
outcome its own region file's search recorded, and the blocker after
**`blocker:`**.

**Nothing else moves.** `golden` still beats `limitations` still beats `gap`; the
corpus still takes real-world specifications only; a probe is still never
proposed as a corpus fixture; and a probe still produces no byte-comparison
evidence. A row settled by route 2 therefore carries a measured Fern verdict and
no crozier-versus-Fern parity evidence — that is the whole of what this route
buys and the whole of what it costs.

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
measurement that settles it.

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
