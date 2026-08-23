# OpenAPI surface coverage

Which OpenAPI features the registered golden corpus has **never seen** and
[`fern-limitations.md`](fern-limitations.md) has **never ruled on**. Each one is
generator behaviour only crozier vouches for: no golden pins it, no measurement of
Fern contradicts it, and `just check` stays green whatever crozier does with it.
This file is the index; the classified entries live in the six region files below.

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

Every region file carries the same four sections, in this order: `# ...` title and
a one-line statement of what the region owns, `## Scope` (the boundary row above,
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

The registered sources are both halves of the corpus: the 31 vendored
`tests/fixtures/<name>/openapi.*` documents, and the 93 `link-ok` documents
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
   way that file's *How to read a verdict* section spells it (`implements`,
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
- **`PROBE`** — what Fern does with the feature is unknown and no corpus row could
  settle it, so the settlement is a locally authored probe recorded in
  [`fern-limitations.md`](fern-limitations.md). The corpus takes real-world
  specifications only; a probe is never proposed as a fixture.
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

<!-- Filled by the synthesis pass from the six region files: the FIXTURE-class
     gap rows of every region, ranked by the rubric above. -->
