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
`tests/fixtures/<name>/openapi.*` documents, and the 108 `link-ok` documents
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
three, declared in `scripts/openapi-surface-census.py` and restated here, with a
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

A predicate selector is a selector like any other everywhere else: `--selector`
accepts one, refuses a misspelling of one by name, and reports an undeclared one
as absent.

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
  things put a row in this class — a measurement no single specification can
  hold, and a shape for which no witness has been found at all — and only the
  first is
  permanent; [The probe backlog](#the-probe-backlog) draws that line, and each
  row's own `settlement` cell says which side it is on.
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
  snapshot is the one every region file's evidence was taken from, pinned by
  digest in
  [`document-paths.md`'s snapshot reconciliation](openapi-surface/document-paths.md#snapshot-reconciliation)
  rather than restated here. It reads **140** registered sources, of which
  **123** carry a committed golden.
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
| [`parameters`](openapi-surface/parameters.md) | 70 | 42 | 14 | 14 | 13 | 1 | 0 |
| [`schemas`](openapi-surface/schemas.md) | 116 | 84 | 5 | 27 | 19 | 5 | 3 |
| [`bodies-media`](openapi-surface/bodies-media.md) | 47 | 35 | 11 | 1 | 1 | 0 | 0 |
| [`security`](openapi-surface/security.md) | 50 | 35 | 4 | 11 | 7 | 4 | 0 |
| [`document-paths`](openapi-surface/document-paths.md) | 67 | 58 | 5 | 4 | 2 | 2 | 0 |
| [`oas31-extensions`](openapi-surface/oas31-extensions.md) | 52 | 33 | 1 | 18 | 1 | 0 | 17 |
| **total** | **402** | **287** | **40** | **75** | **43** | **12** | **20** |

The walk enumerated **402** features and landed each in exactly one category:
**287** `golden`, **40** `limitations`, **75** `gap`. The `gap` column splits by
settlement class into **43** `FIXTURE`, **12** `PROBE` and **20** `UNREACHABLE`.

**What the `gap` count means.** 75 is the number of OpenAPI shapes for which
crozier's behaviour is vouched for by nothing but crozier: no committed golden's
source declares the shape, so no byte comparison against Fern touches it, and
[`fern-limitations.md`](fern-limitations.md) has never measured Fern on it, so
nothing contradicts whatever crozier does. `just check` is green over all 75
either way. It is not a defect count — 20 of them (`UNREACHABLE`) have no
position in a generated Python SDK at all, and saying so is their settlement.
The two backlogs below are the other 55.

### Reconciliation

**Each feature is classified exactly once.** The 402 rows carry 402 distinct
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

**Every ledger key is accounted for.** The canonical join reports 56 keys, of
which 51 are a region row's key verbatim. The other five:

| ledger key | how it is accounted for |
|---|---|
| `status_code` | **Not a feature key.** It is a row label inside the ledger's 407/421 probe table, which the join's `\| key \| N \|` shape matches by accident — the `bodies-media` region's method notes say the same. The join's real yield is 55. |
| `encoding-explode-or-allowReserved` | One ledger row covering two fields; `bodies-media` splits it into `encoding-explode` and `encoding-allow-reserved`, both `limitations`, both citing that verdict. |
| `servers-multiple-path-or-operation` | One ledger row covering two levels; `document-paths` splits it into `pathitem-servers` and `operation-servers`, both `golden`. |
| `relative-file-ref` | A *target form* of `Path Item Object.$ref`, which `document-paths` classifies once as `pathitem-ref` (`golden` since corpus row 99 declares 36 of them, citing verdict `discards`). The walk enumerates the field; the ledger additionally rules on one form of what it points at. |
| `normalization-collision` | **The walk's one enumeration hole** — see below. |

**The one correction this node records.** `normalization-collision` is the shape
of two `components.schemas` names that collide after identifier normalization
(`OBRate1_0` beside `OB_Rate1_0`). No region row carries it, because the selector
grammar excludes map keys that are *names* by design, so no selector can reach
it. The path-side counterpart, `document-paths`'s `duplicate-normalized-paths`,
is both enumerated **and** measured — by the `openapi.paths:normalized-collision`
predicate selector, which normalizes each path key's template expressions and
reports zero across all 140 registered sources. So the inconsistency between the
two regions is now only that the schema-name side has no counterpart predicate:
what the `schemas` region needs is a selector over `components.schemas` keys under
`naming::class_name`, not a hand measurement. Were the row written it would be
`limitations`, citing
ledger `normalization-collision`, verdict `discards`, with two byte-matching
golden witnesses (`openbanking.org.uk-account-info-openapi`,
`amazonaws.com-cloudformation`), so it moves no count in either backlog below.
Writing it belongs to a change that owns [`schemas.md`](openapi-surface/schemas.md);
recording it is this node's part, and no region file is edited here.

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

The three highest-ranked entries were passed over after a GitHub
code search of real OpenAPI 3 documents: `header-allow-reserved` has only
conformance-fixture Header Object witnesses because `allowReserved` is defined
for query parameters; `header-content` and `header-deprecated` likewise yielded
only meta-schema or conformance examples, not a redistributable real-world API.

[`content-encoding`](openapi-surface/schemas.md) is pinned by corpus row 95,
`marimo`; its `Base64String` component declares `contentEncoding: base64` and
its Fern 5.20.0 golden byte-matches with no exclusions.

[`format-duration`](openapi-surface/schemas.md) is pinned by corpus row 97,
`mosip-esignet`, registered as one of the three `http-dpop` witnesses; two of its
schemas declare `format: duration` and its Fern 5.20.0 golden byte-matches with
no exclusions.

All 43 `FIXTURE` gaps remaining across the six regions, in one total order, by [the ranking
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
what makes it a gap — 41 of the 43 score zero, and the two that do not name
  their one source in that cell.

**The median blind-spot count of this list is 0** — 27 of the 43 entries name no
`src/` file at all, which is also why they win criterion 1 outright.

| # | key | region | 1. crozier sites | 2. blind spots | 3. artifacts | 4. witnesses |
|---|---|---|---|---|---|---|
| 1 | [`header-allow-reserved`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 2 | [`header-content`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 3 | [`header-deprecated`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 4 | [`reference-summary`](openapi-surface/oas31-extensions.md) | `oas31-extensions` | **0** (none) | **0** (no `src/` file) | **3** (types/, client.py, reference.md) | **0** |
| 5 | [`parameter-style-simple-header-scalar`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **2** (client.py, raw_client.py) | **0** |
| 6 | [`securityscheme-ref`](openapi-surface/security.md) | `security` | **0** (none) | **0** (no `src/` file) | **2** (client.py, core/) | **0** |
| 7 | [`contains`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 8 | [`content-media-type`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 9 | [`content-schema`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 10 | [`dependent-required`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 11 | [`dependent-schemas`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 12 | [`dollar-anchor`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 13 | [`dollar-defs`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 14 | [`exclusive-maximum-numeric`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 15 | [`format-idn-email`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 16 | [`format-idn-hostname`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 17 | [`format-ipv6`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 18 | [`format-iri`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 19 | [`format-iri-reference`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 20 | [`format-json-pointer`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 21 | [`max-contains`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 22 | [`min-contains`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 23 | [`multiple-of`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 24 | [`parameter-style-simple-path-array`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **1** (raw_client.py) | **0** |
| 25 | [`parameter-style-simple-path-object`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **1** (raw_client.py) | **0** |
| 26 | [`property-names`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 27 | [`unevaluated-items`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 28 | [`operation-overrides-path-item-parameter`](openapi-surface/parameters.md) | `parameters` | **1** (`src/openapi.rs` 1) | **511** (`src/openapi.rs` 511) | **3** (client.py, raw_client.py, reference.md) | **1** |
| 29 | [`oauth2-multiple-flows`](openapi-surface/security.md) | `security` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (types/, reference.md) | **0** |
| 30 | [`parameter-style-deepobject-query-array`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 31 | [`parameter-style-deepobject-query-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 32 | [`parameter-style-form-cookie-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 33 | [`parameter-style-form-query-object`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 34 | [`parameter-style-pipedelimited-query-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 35 | [`parameter-style-spacedelimited-query-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 36 | [`http-hoba`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 37 | [`http-oauth`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 38 | [`http-scram-sha-1`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 39 | [`http-scram-sha-256`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 40 | [`security-optional-requirement-operation`](openapi-surface/security.md) | `security` | **3** (`src/ir.rs` 3) | **201** (`src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **1** |
| 41 | [`templated-path-segment`](openapi-surface/document-paths.md) | `document-paths` | **3** (`src/ir.rs` 3) | **201** (`src/ir.rs` 201) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 42 | [`several-path-template-variables`](openapi-surface/document-paths.md) | `document-paths` | **3** (`src/ir.rs` 3) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 43 | [`media-type-range`](openapi-surface/bodies-media.md) | `bodies-media` | **7** (`src/emit.rs` 1, `src/ir.rs` 6) | **462** (`src/emit.rs` 261 + `src/ir.rs` 201) | **4** (types/, client.py, raw_client.py, reference.md) | **0** |

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
| `src/openapi.rs` | 511 | all-e2e 221, non-e2e 290 | 5 — #27 `operation-overrides-path-item-parameter`, #35 `http-hoba`, #36 `http-oauth`, #37 `http-scram-sha-1`, #38 `http-scram-sha-256` | **Agrees, and the walk found the rest as probes.** #27 is `normalize_parameters`, 3 regions, and #35–#38 — `http-hoba`, `http-oauth`, `http-scram-sha-1` and `http-scram-sha-256` — are the one `#[serde(other)]` scheme fallback beside it, four IANA scheme members that collapse through the same arm. The largest block, `filter_ignored` 72, is the walk's `x-fern-or-crozier-ignore` — now `golden`, on corpus row 108's four `x-fern-ignore` operations, though golden-classified is not golden-*exhausted*: one witness reaches the Operation-Object arm and leaves the schema arm and the `x-crozier-*` precedence to unit tests. `filter_by_audience` 47 + `audiences` 8 belong to `audience-dual-header-policy`, classified `golden`: golden-classified is not golden-*exhausted*, since the two audience goldens declare 8 sites between them and leave the rest of the branch space to unit tests. `collect_schema_refs` 46 + `expand_schema_closure` 32 + `operation_schema_seed` 24 is `$ref`-closure pruning under `reference-ref` (`golden`); `load` 26 + `visit_seq` 7 + `de_composition` 5 are malformed-document deserialization paths the corpus excludes by taking only documents Fern generates. |
| `src/cli.rs` | 292 | all-e2e 133, non-e2e 159 | none | **Neither**, as `src/settings.rs`: `do_config` 60, `run` 43, `do_init` 26, `do_generate` 12 are the command surface, not document behaviour. |
| `src/emit.rs` | 261 | all-e2e 29, non-e2e 232 | 1 — #42 `media-type-range` | **A shape the walk missed.** #42 names `append_request_call_args`, which is not among the blind regions at all. Those are example rendering — `raw_type_str_ctx` 40, `example_matches_type` 24, `build_example_inner` 23, `named_value_inner` 13, `value_from_example` 12, `example_from_json` 6 — and streaming docstrings, `client_stream_docstring` 11 + `raw_stream_docstring` 10. Every `example`/`examples` field is classified `golden`, but the walk enumerates the *field*; those branches switch on the JSON value *kind* an example holds, and example values are not in the grammar's closed list of valued selectors, so no `gap` row could have named them. |
| `src/ir.rs` | 201 | all-e2e 9, non-e2e 192 | 15 — #28–#42 | **Agrees on the file, misses the shapes.** The blind regions are type-lowering conjunctions: `resolve_schema_pointer` 25, `nested_array_element` 25, `hoist_union_variant` 24, `ref_to_class` 22, `prop_type_ref` 20, `path_group` 15. Each driving field — `$ref`, `items`, `oneOf`, `properties` — is `golden` on its own; it is their *combinations* that no golden reaches, and the census emits one selector per field and none per conjunction. Two regions built bespoke conjunction passes for exactly this reason (`parameters`' style × `in` × schema matrix, `schemas`' variant scan); nobody ran one over schema-composition combinations. |
| `src/refs.rs` | 74 | all-e2e 17, non-e2e 57 | none | **Only a probe can settle it.** `resolve_reference` 16, `document` 10, `pointer` 9, `error` 7, `curl_fetch` 7 are the cross-document `$ref` path. The corpus is single-document by construction ([`matching.md`](matching.md#cross-document-ref-resolution-issue-77)), and the ledger's `relative-file-ref` row is already `discards + pipeline` — its own note being that crozier's fixture pipeline cannot register the tree that would make the reference resolve. No corpus row is in reach. |
| `src/schema.rs` | 46 | all-e2e 23, non-e2e 23 | none | **Neither.** `build` 20 emits crozier's own config JSON Schema. |
| `src/lib.rs` | 33 | all-e2e 1, non-e2e 32 | none | **Neither.** `render_files` 29 is the filesystem write path. |
| `src/naming.rs` | 31 | all-e2e 8, non-e2e 23 | none | **A shape the walk missed — and the same hole as `normalization-collision` above.** `digit_word` 10, `enum_words` 7, `numeric_enum_identifier` 2, `finalize_enum_ident` 2, `sanitize_identifier` 1 are driven by OpenAPI *names* — schema names, enum member spellings — which the grammar excludes as map keys that are names, so no selector reaches them. |
| `src/config.rs` | 31 | all-e2e 13, non-e2e 18 | none | **Neither.** `default_package_name` 10 and `new` 8 are generator-config defaults. |
| `src/pyfmt.rs` | 24 | all-e2e 0, non-e2e 24 | none | **Neither.** `format_source` 24 is the `ruff format` shell-out and its failure paths. |
| `src/main.rs` | 6 | all-e2e 6, non-e2e 0 | none | **Neither.** The binary entry point; `just test-fixtures-coverage` asserts it is reachable at all. |

**Where the two backlogs agree.** Both name `src/ir.rs`, `src/openapi.rs` and
`src/emit.rs` — every `src/` file any ranked gap points at is one the blind-spot
block also lists, and in the same order of size (`openapi.rs` 511 > `emit.rs` 261
> `ir.rs` 201). Ranking on criterion 2 therefore does not fight the repository's
own measurement; it refines it, because 27 of the 43 ranked entries reach no
`src/` file at all and so are invisible to a per-file view.

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

The other 12 `gap` rows whose settlement is not a fixture. **These are probe
work, not fixture work** — the corpus takes real-world specifications only, and a
probe is never proposed as a fixture
([`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md)). When one is
measured, the result belongs in [`fern-limitations.md`](fern-limitations.md) as a
row with a verdict, at which point the feature's category here becomes
`limitations` and it leaves this list. Nothing below is ranked: a probe costs one
Fern run, so the order to do them in is whichever the next Fern session has
loaded.

**Two different reasons put a row here, and they are not equally durable.** This
section used to state one — that each row asks what Fern does with a shape *no
real-world document can isolate* — and that is now false of part of the list, so
the distinction is drawn here rather than left to be inferred:

- A **structural** probe is one the rewritten claim still fits. The measurement
  is a differential or a collision that no single specification can hold: the
  same schema with and without a keyword, or two declarations a real document
  would not carry at once. No corpus row could ever pin it, so the row is here
  permanently — a probe is genuinely its only instrument.
- A **witness-supply** probe is one where the shape is perfectly isolable in a
  single document and the authoritative issue #188 search found **no witness at
  all**. Nothing about the shape prevents a corpus row; the supply of documents
  does. That bar is the whole of it, and it is narrower than it first reads:
  a witness the search *did* find does not leave a row here, however unusable
  that document turns out to be. One blocked on redistribution, reachable at no
  immutable ref, or refused by `fern check` is a screening failure of that
  candidate rather than evidence the feature has no witness, so it moves the row
  to `FIXTURE` at once — which is what `dollar-anchor` records. A witness-supply
  probe therefore leaves this list the day any witness turns up, blocked or not,
  and it leaves as a `FIXTURE` rather than as a measured probe.

**Which kind a row is, is its own region row's business, not this section's.**
Each `settlement` cell in the six region files states the reason its own row
rests on, in the terms the row's evidence supports, and that cell is the
authority; this index does not re-adjudicate the twelve, and it transcribes no
per-row verdict here that would go stale when one of those cells is reworded.
The rows saying *witness supply* in those words come out as a list with

```
grep -h 'witness.supply' docs/openapi-surface/*.md | grep -oP '^\| `?\K[a-z0-9-]+'
```

the same way the ledger keys do above. Each row that command returns names every
source searched and the exact query put to it. How many there are is deliberately
not written down here: this section states the rule and the derivation, and a
count beside a command that prints it is the transcription the paragraph above
promises not to make.

Read the rest the same way: a settlement cell that names a differential
measurement is structural, and one that reports a search finding no witness at
all is supply. A cell naming a candidate the search
*did* find is neither — under the rule above that row belongs in the fixture
backlog, so a cell like that is a row still to be moved rather than a third kind
of probe.

**Two rows in the table below do not yet satisfy the rule above, and that is
recorded rather than quietly fixed.** `format-relative-json-pointer` is
`witness-blocked` on a publisher-owned document Fern accepts, blocked only by a
proprietary licence — `dollar-anchor`'s exact case, which the rule moves to
`FIXTURE` — and `dollar-comment` is `witness-found` on a redistributable document
Fern accepts, which the rule makes registrable. Both are
[`schemas.md`](openapi-surface/schemas.md) rows belonging to the change that
settles that file's `$comment`, `$vocabulary` and `format` witnesses; moving them
here would move counts that change has to move too. Until it lands, the twelve
below are the probe backlog as measured, and two of them are known to be leaving
it. Nothing in the gate catches this: `RankedBacklogTests` reconciles membership
and counts against the region files' `settlement` cells, so a cell that has not
caught up with the rule reconciles perfectly. Making that a red — a check that
fails when a `witness-blocked` or `witness-found` row settles `PROBE` — needs the
two rows moved first, and belongs to the change that moves them.

**So this backlog's membership is provisional in a way the fixture backlog's is
not.** A row can leave it without any Fern run at all — `dollar-anchor` did,
moving to `FIXTURE` on a publisher-owned witness Fern accepts that the corpus may
not redistribute — so a reader taking the twelve as a fixed body of Fern
measurements will over-count the probe work by however many of them are waiting
on a document rather than on a probe.

| key | region | spec location | the Fern measurement that settles it |
|---|---|---|---|
| [`duplicate-normalized-paths`](openapi-surface/document-paths.md) | `document-paths` | `Paths Object paths equal after template-name normalization` | Generate two path templates that normalize to one name and record which endpoints Fern emits. |
| [`duplicate-operation-id`](openapi-surface/document-paths.md) | `document-paths` | `Operation Object.operationId duplicated` | Generate two operations sharing one `operationId` and record which method survives. |
| [`parameter-style-matrix-path-scalar`](openapi-surface/parameters.md) | `parameters` | Parameter Object.style (`matrix`, `in: path`, scalar schema) | Generate a `matrix` path parameter with a scalar schema, beside the ledger's `matrix-array`/`matrix-object` rows. |
| [`dollar-comment`](openapi-surface/schemas.md) | `schemas` | `Schema Object.$comment` | Generate a schema carrying `$comment` and diff against the same schema without it. |
| [`dollar-dynamic-anchor`](openapi-surface/schemas.md) | `schemas` | `Schema Object.$dynamicAnchor` | Generate a `$dynamicAnchor`/`$dynamicRef` recursion and record what Fern emits. |
| [`dollar-dynamic-ref`](openapi-surface/schemas.md) | `schemas` | `Schema Object.$dynamicRef` | As `dollar-dynamic-anchor`: the pair is only exercisable together. |
| [`dollar-vocabulary`](openapi-surface/schemas.md) | `schemas` | `Schema Object.$vocabulary` | Generate a schema under a custom dialect declaring `$vocabulary`. |
| [`format-relative-json-pointer`](openapi-surface/schemas.md) | `schemas` | `Schema Object.format` | Generate `format: relative-json-pointer` and record the Python type Fern annotates. |
| [`http-concealed`](openapi-surface/security.md) | `security` | `Security Scheme Object.scheme` = `concealed` (RFC 9729) | Run `fern check` and `fern generate` on a document declaring `scheme: concealed` alone, and again beside a supported scheme, and record both outcomes. |
| [`http-gnap`](openapi-surface/security.md) | `security` | `Security Scheme Object.scheme` = `gnap` (RFC 9635) | Run `fern check` and `fern generate` on a document declaring `scheme: gnap` alone, and again beside a supported scheme, and record both outcomes. |
| [`http-privatetoken`](openapi-surface/security.md) | `security` | `Security Scheme Object.scheme` = `privatetoken` (RFC 9577) | Run `fern check` and `fern generate` on a document declaring `scheme: privatetoken` alone, and again beside a supported scheme, and record both outcomes. |
| [`http-vapid`](openapi-surface/security.md) | `security` | `Security Scheme Object.scheme` = `vapid` (RFC 8292) | Run `fern check` and `fern generate` on a document declaring `scheme: vapid` alone, and again beside a supported scheme, and record both outcomes. |
