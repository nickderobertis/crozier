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
`tests/fixtures/<name>/openapi.*` documents, and the 109 `link-ok` documents
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
  snapshot is the one every region file's evidence was taken from, pinned by
  digest in
  [`document-paths.md`'s snapshot reconciliation](openapi-surface/document-paths.md#snapshot-reconciliation)
  rather than restated here. It reads **141** registered sources, of which
  **124** carry a committed golden.
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
| [`parameters`](openapi-surface/parameters.md) | 70 | 42 | 14 | 14 | 14 | 0 | 0 |
| [`schemas`](openapi-surface/schemas.md) | 116 | 85 | 5 | 26 | 20 | 3 | 3 |
| [`bodies-media`](openapi-surface/bodies-media.md) | 47 | 35 | 11 | 1 | 1 | 0 | 0 |
| [`security`](openapi-surface/security.md) | 50 | 35 | 4 | 11 | 7 | 4 | 0 |
| [`document-paths`](openapi-surface/document-paths.md) | 67 | 58 | 5 | 4 | 4 | 0 | 0 |
| [`oas31-extensions`](openapi-surface/oas31-extensions.md) | 52 | 33 | 1 | 18 | 1 | 0 | 17 |
| **total** | **402** | **288** | **40** | **74** | **47** | **7** | **20** |

The walk enumerated **402** features and landed each in exactly one category:
**288** `golden`, **40** `limitations`, **74** `gap`. The `gap` column splits by
settlement class into **47** `FIXTURE`, **7** `PROBE` and **20** `UNREACHABLE`.

**What the `gap` count means.** 74 is the number of OpenAPI shapes for which
crozier's behaviour is vouched for by nothing but crozier: no committed golden's
source declares the shape, so no byte comparison against Fern touches it, and
[`fern-limitations.md`](fern-limitations.md) has never measured Fern on it, so
nothing contradicts whatever crozier does. `just check` is green over all 74
either way. It is not a defect count — 20 of them (`UNREACHABLE`) have no
position in a generated Python SDK at all, and saying so is their settlement.
The two backlogs below are the other 54.

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

[`duplicate-normalized-paths`](openapi-surface/document-paths.md) (#5) and
[`duplicate-operation-id`](openapi-surface/document-paths.md) (#46) arrive from
the probe backlog with no witness found either way. Both were `PROBE` while the
census could not compare two values at all, and stayed there afterwards on a
measured zero over the registered sources. Neither is a
[structural probe](#structural-probes): the settling comparison is not between
two documents, because one document declaring the collision generates a golden
whose raw-client methods say what Fern did with it. No world-wide witness search
has been run for either, so what each needs is that search and then a corpus row.

All 47 `FIXTURE` gaps remaining across the six regions, in one total order, by [the ranking
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
what makes it a gap — 44 of the 47 score zero, and the three that do not name
  their one source in that cell.

**The median blind-spot count of this list is 0** — 30 of the 47 entries name no
`src/` file at all, which is also why they win criterion 1 outright.

| # | key | region | 1. crozier sites | 2. blind spots | 3. artifacts | 4. witnesses |
|---|---|---|---|---|---|---|
| 1 | [`header-allow-reserved`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 2 | [`header-content`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 3 | [`header-deprecated`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 4 | [`reference-summary`](openapi-surface/oas31-extensions.md) | `oas31-extensions` | **0** (none) | **0** (no `src/` file) | **3** (types/, client.py, reference.md) | **0** |
| 5 | [`duplicate-normalized-paths`](openapi-surface/document-paths.md) | `document-paths` | **0** (none) | **0** (no `src/` file) | **2** (raw_client.py, reference.md) | **0** |
| 6 | [`parameter-style-simple-header-scalar`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **2** (client.py, raw_client.py) | **0** |
| 7 | [`securityscheme-ref`](openapi-surface/security.md) | `security` | **0** (none) | **0** (no `src/` file) | **2** (client.py, core/) | **0** |
| 8 | [`parameter-style-matrix-path-scalar`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **1** (raw_client.py) | **1** |
| 9 | [`contains`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 10 | [`content-media-type`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 11 | [`content-schema`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 12 | [`dependent-required`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 13 | [`dependent-schemas`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 14 | [`dollar-anchor`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 15 | [`dollar-defs`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 16 | [`exclusive-maximum-numeric`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 17 | [`format-idn-email`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 18 | [`format-idn-hostname`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 19 | [`format-ipv6`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 20 | [`format-iri`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 21 | [`format-iri-reference`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 22 | [`format-json-pointer`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 23 | [`format-relative-json-pointer`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 24 | [`max-contains`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 25 | [`min-contains`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 26 | [`multiple-of`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 27 | [`parameter-style-simple-path-array`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **1** (raw_client.py) | **0** |
| 28 | [`parameter-style-simple-path-object`](openapi-surface/parameters.md) | `parameters` | **0** (none) | **0** (no `src/` file) | **1** (raw_client.py) | **0** |
| 29 | [`property-names`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 30 | [`unevaluated-items`](openapi-surface/schemas.md) | `schemas` | **0** (none) | **0** (no `src/` file) | **1** (types/) | **0** |
| 31 | [`operation-overrides-path-item-parameter`](openapi-surface/parameters.md) | `parameters` | **1** (`src/openapi.rs` 1) | **511** (`src/openapi.rs` 511) | **3** (client.py, raw_client.py, reference.md) | **1** |
| 32 | [`oauth2-multiple-flows`](openapi-surface/security.md) | `security` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (types/, reference.md) | **0** |
| 33 | [`parameter-style-deepobject-query-array`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 34 | [`parameter-style-deepobject-query-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 35 | [`parameter-style-form-cookie-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 36 | [`parameter-style-form-query-object`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 37 | [`parameter-style-pipedelimited-query-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 38 | [`parameter-style-spacedelimited-query-scalar`](openapi-surface/parameters.md) | `parameters` | **1** (`src/ir.rs` 1) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 39 | [`http-hoba`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 40 | [`http-oauth`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 41 | [`http-scram-sha-1`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 42 | [`http-scram-sha-256`](openapi-surface/security.md) | `security` | **2** (`src/openapi.rs` 1, `src/ir.rs` 1) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **0** |
| 43 | [`security-optional-requirement-operation`](openapi-surface/security.md) | `security` | **3** (`src/ir.rs` 3) | **201** (`src/ir.rs` 201) | **3** (client.py, core/, reference.md) | **1** |
| 44 | [`templated-path-segment`](openapi-surface/document-paths.md) | `document-paths` | **3** (`src/ir.rs` 3) | **201** (`src/ir.rs` 201) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 45 | [`several-path-template-variables`](openapi-surface/document-paths.md) | `document-paths` | **3** (`src/ir.rs` 3) | **201** (`src/ir.rs` 201) | **2** (client.py, raw_client.py) | **0** |
| 46 | [`duplicate-operation-id`](openapi-surface/document-paths.md) | `document-paths` | **7** (`src/openapi.rs` 1, `src/ir.rs` 6) | **712** (`src/openapi.rs` 511 + `src/ir.rs` 201) | **2** (client.py, reference.md) | **0** |
| 47 | [`media-type-range`](openapi-surface/bodies-media.md) | `bodies-media` | **7** (`src/emit.rs` 1, `src/ir.rs` 6) | **462** (`src/emit.rs` 261 + `src/ir.rs` 201) | **4** (types/, client.py, raw_client.py, reference.md) | **0** |

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
| `src/openapi.rs` | 511 | all-e2e 221, non-e2e 290 | 6 — #31 `operation-overrides-path-item-parameter`, #39 `http-hoba`, #40 `http-oauth`, #41 `http-scram-sha-1`, #42 `http-scram-sha-256`, #46 `duplicate-operation-id` | **Agrees, and accounts for the rest.** #31 is `normalize_parameters`, 3 regions; #39–#42 — `http-hoba`, `http-oauth`, `http-scram-sha-1` and `http-scram-sha-256` — are the one `#[serde(other)]` scheme fallback beside it, four IANA scheme members that collapse through the same arm; and #46 is the `operation_id` field declaration this file's one production read of the value is. The largest block, `filter_ignored` 72, is the walk's `x-fern-or-crozier-ignore` — now `golden`, on corpus row 108's four `x-fern-ignore` operations, though golden-classified is not golden-*exhausted*: one witness reaches the Operation-Object arm and leaves the schema arm and the `x-crozier-*` precedence to unit tests. `filter_by_audience` 47 + `audiences` 8 belong to `audience-dual-header-policy`, classified `golden`: golden-classified is not golden-*exhausted*, since the two audience goldens declare 8 sites between them and leave the rest of the branch space to unit tests. `collect_schema_refs` 46 + `expand_schema_closure` 32 + `operation_schema_seed` 24 is `$ref`-closure pruning under `reference-ref` (`golden`); `load` 26 + `visit_seq` 7 + `de_composition` 5 are malformed-document deserialization paths the corpus excludes by taking only documents Fern generates. |
| `src/cli.rs` | 292 | all-e2e 133, non-e2e 159 | none | **Neither**, as `src/settings.rs`: `do_config` 60, `run` 43, `do_init` 26, `do_generate` 12 are the command surface, not document behaviour. |
| `src/emit.rs` | 261 | all-e2e 29, non-e2e 232 | 1 — #47 `media-type-range` | **A shape the walk missed.** #47 names `append_request_call_args`, which is not among the blind regions at all. Those are example rendering — `raw_type_str_ctx` 40, `example_matches_type` 24, `build_example_inner` 23, `named_value_inner` 13, `value_from_example` 12, `example_from_json` 6 — and streaming docstrings, `client_stream_docstring` 11 + `raw_stream_docstring` 10. Every `example`/`examples` field is classified `golden`, but the walk enumerates the *field*; those branches switch on the JSON value *kind* an example holds, and example values are not in the grammar's closed list of valued selectors, so no `gap` row could have named them. |
| `src/ir.rs` | 201 | all-e2e 9, non-e2e 192 | 16 — #32–#47 | **Agrees on the file, misses the shapes.** The blind regions are type-lowering conjunctions: `resolve_schema_pointer` 25, `nested_array_element` 25, `hoist_union_variant` 24, `ref_to_class` 22, `prop_type_ref` 20, `path_group` 15. Each driving field — `$ref`, `items`, `oneOf`, `properties` — is `golden` on its own; it is their *combinations* that no golden reaches, and the census emits one selector per field and none per conjunction. Two regions built bespoke conjunction passes for exactly this reason (`parameters`' style × `in` × schema matrix, `schemas`' variant scan); nobody ran one over schema-composition combinations. |
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
own measurement; it refines it, because 30 of the 47 ranked entries reach no
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

The other 7 `gap` rows whose settlement is not a fixture. **These are probe
work, not fixture work** — the corpus takes real-world specifications only, and a
probe is never proposed as a fixture
([`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md)). When one is
measured, the result belongs in [`fern-limitations.md`](fern-limitations.md) as a
row with a verdict, at which point the feature's category here becomes
`limitations` and it leaves this list. Nothing below is ranked: a probe costs one
Fern run, so the order to do them in is whichever the next Fern session has
loaded.

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
#46 and #5.

### Witness-supply probes

**7 rows.** A witness-supply probe's shape is perfectly isolable in a single
document. Nothing about the shape prevents a corpus row; the supply of documents
does — the authoritative issue #188 search found **no witness at all**, and the
row's own region file records that search as a line of its `### Witness search
(issue #188)` table naming every source put to it and the exact query used
against each. What becomes of a row when that search *does* find a witness is
[the settlement rule](#the-settlement-rule-as-amended) below, which every region
file follows rather than restating.

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
  under that same address. The URL alone is not a blocker, because a URL is not
  by itself mutable.
- **`fern refusal`** — both halves of Fern's own refusal: the **exit status** it
  returned, and the diagnostic it printed, quoted in a code span of its own. The
  invocation is not the diagnostic — a refusal whose only code span is `fern
  check` has recorded that Fern ran, not what it said.

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
is built from.

**So this backlog's membership is provisional in a way the fixture backlog's is
not.** A row can leave it without any Fern run at all — `dollar-anchor` did,
moving to `FIXTURE` on a publisher-owned witness Fern accepts that the corpus may
not redistribute, and `format-relative-json-pointer` has since left the same way —
so a reader taking these rows as a fixed body of Fern measurements will
over-count the probe work by however many are waiting on a document rather than
on a probe. A row can also leave it *straight to `golden`*, which `dollar-comment`
did: its witness was redistributable, Fern accepted it, and registering it as
corpus row 109 settled the shape with a byte-matching golden rather than with a
probe.

| key | region | spec location | the Fern measurement that settles it |
|---|---|---|---|
| [`dollar-dynamic-anchor`](openapi-surface/schemas.md) | `schemas` | `Schema Object.$dynamicAnchor` | Generate a `$dynamicAnchor`/`$dynamicRef` recursion and record what Fern emits. |
| [`dollar-dynamic-ref`](openapi-surface/schemas.md) | `schemas` | `Schema Object.$dynamicRef` | As `dollar-dynamic-anchor`: the pair is only exercisable together. |
| [`dollar-vocabulary`](openapi-surface/schemas.md) | `schemas` | `Schema Object.$vocabulary` | Generate a schema under a custom dialect declaring `$vocabulary`. |
| [`http-concealed`](openapi-surface/security.md) | `security` | `Security Scheme Object.scheme` = `concealed` (RFC 9729) | Run `fern check` and `fern generate` on a document declaring `scheme: concealed` alone, and again beside a supported scheme, and record both outcomes. |
| [`http-gnap`](openapi-surface/security.md) | `security` | `Security Scheme Object.scheme` = `gnap` (RFC 9635) | Run `fern check` and `fern generate` on a document declaring `scheme: gnap` alone, and again beside a supported scheme, and record both outcomes. |
| [`http-privatetoken`](openapi-surface/security.md) | `security` | `Security Scheme Object.scheme` = `privatetoken` (RFC 9577) | Run `fern check` and `fern generate` on a document declaring `scheme: privatetoken` alone, and again beside a supported scheme, and record both outcomes. |
| [`http-vapid`](openapi-surface/security.md) | `security` | `Security Scheme Object.scheme` = `vapid` (RFC 8292) | Run `fern check` and `fern generate` on a document declaring `scheme: vapid` alone, and again beside a supported scheme, and record both outcomes. |
