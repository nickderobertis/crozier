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
one of four categories and each uncovered one carrying what it would take to
settle it.

**What this is not.** It is not a claim about what Fern does — that is
[`fern-limitations.md`](fern-limitations.md), measured against a real Fern run —
and it is not a claim that crozier is *wrong* anywhere. A `gap` row says the
question is unanswered by anything in this repository, not that the answer is bad.
It is also not a fixture backlog on its own: what a `gap` row becomes is decided
by its `settlement` cell, and the corpus registration rules in
[`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md) still govern.

**What it says today.** *Does crozier byte-match Fern on every OpenAPI feature
and scenario?* **No, not yet on all of them, and here is the exact remainder.**
The walk enumerates 628 features. By category, 494 are `golden`, 52
`limitations`, 60 `handwritten` and 22 `gap`. Taken back from the region files,
the ledger, [`MANIFEST.tsv`](openapi-surface/probe-expected/MANIFEST.tsv) and
the [hand-written fixtures](openapi-surface/handwritten/AGENTS.md), those 628
split four ways:

- **492 carry byte-match evidence against a registered real-world
  specification.** At least one golden-only witness that is not a hand-authored
  feature target declares the feature, and its committed Fern golden
  byte-matches where the feature's code lands.
- **66 carry a committed Fern measurement of non-generation that crozier is
  byte-compared against.** These are the 52 `limitations` rows and the 14
  `UNREACHABLE` `gap` rows. Each has a `MANIFEST.tsv` row whose artifact
  `witness_supply_probes_match_fern_measurements` in `crates/crozier-e2e/tests/e2e.rs` compares
  crozier against.
- **60 rest on a hand-written fixture, a weaker proof than a real
  specification.** These are the `handwritten` rows. No registered real
  specification declares the feature, its real-specification search failed, and
  crozier byte-matches the tree Fern generated from a document written for the
  purpose. Five have a search record that reads `exhausted`: every candidate is
  decided and none is registrable. Fifty-five read `search-incomplete`. Of those,
  six read `search-incomplete`
  only because GitHub refused 12 candidates at every route the first searches
  took. The
  [renewed search](openapi-surface/witness-search-renewed/README.md) found each
  of those six `none-registrable`, and seven of the 12 are still refused. The
  seventh, `component-same-primitive-union`, has not been searched at any
  declared source; its
  [renewed search](openapi-surface/witness-search-union-shapes/README.md) read
  693 documents a bounded code search returned and found it `none-registrable`.
  The next four — `unread-date-time-example`, `allof-parent-request-body`,
  `request-example-nested-null` and `request-example-deprecated-property` —
  have not been searched at any declared source either; their
  [renewed search](openapi-surface/witness-search-example-shapes/README.md)
  read 941 documents a bounded code search returned and found each
  `none-registrable`.
  Two more, `request-body-described-inline-scalar` and
  `response-status-space-suffixed`, have not been searched at any declared
  source either; their
  [renewed search](openapi-surface/witness-search-bodies-responses/README.md)
  read 1,469 documents a bounded code search returned, and none declares
  either.
  The parameter-lowering shapes `query-array-items-union`,
  `header-subset-string-default` and `base-path-extension` have not been
  searched at any declared source either: their
  [search](openapi-surface/witness-search-parameter-lowering/README.md) read the
  documents already acquired for the coverage searches, issued no live query,
  and found each `none-registrable`.
  The thirteen parameter extension and serialization shapes read
  `search-incomplete` on their
  [search](openapi-surface/witness-search-parameters-extension-evidence/README.md),
  which screened the candidate real specifications it names against Fern.
  Three more — `cycle-into-cycle`,
  `request-body-property-closed-empty-object` and `type-misspelled-scalar` —
  have not been searched at any declared source either; their
  [renewed search](openapi-surface/witness-search-type-and-cycle-shapes/README.md)
  read 703 documents and found each `none-registrable`, while registering the
  real witnesses of their three neighbours (corpus rows 313 to 315).
  `response-contentless-200-with-created` has the same bounded verdict: its
  [search](openapi-surface/witness-search-contentless-success/README.md) read
  238 registered sources and 40 additional pinned candidates, finding one
  converter example that fails publisher provenance.
  [Generated shapes with no registrable witness](#generated-shapes-with-no-registrable-witness)
  gives each one's evidence and what would unblock it. They are not among the
  492 and never count as a real-specification match.
- **10 remain unproven.** 8 are the `FIXTURE` `gap` rows. Each is a feature the
  naming and example predicates of #361 brought inside the census that no
  registered golden source declares, and none has had a witness search, so each
  reads `not searched` ([Unproven features, named](#unproven-features-named)):
  `operation-id-digit-leading-method`, `schema-example-fractional-on-integer`,
  `schema-example-array-null-element`, `schema-example-temporal-duplicate-element`,
  `schema-example-union-ref-sentinel`, `schema-example-on-ref-to-object`,
  `schema-example-on-ref-to-enum` and `schema-example-on-ref-to-union`. 2 are
  `golden` rows resting only on residual goldens whose code moves no
  byte-matched file: `schema-example-null` and `extension-server`
  ([the attribution](#golden-rows-resting-only-on-residual-goldens)). The
  other 0 are `golden` rows declared only by corpus rows that carry no golden;
  the census no longer reads such a row as a source
  ([the list](#golden-rows-with-no-golden-only-witness)).

492 + 66 + 60 + 10 = 628.

`golden` is still not `golden`-exhausted, so the handling sites are split the
same way. The 494 `golden` rows declare 945 handling sites in
[the site table](openapi-surface/golden-reach-sites.tsv), and
[`golden-reach.tsv`](openapi-surface/golden-reach.tsv), measured at commit
`ac0535b3a` over all 244 golden tests, with the records it links splits them
three ways:

- **854 are reached by a registered real specification.** A golden-only
  witness executes the arm and its golden byte-matches.
- **83 are reached only by a hand-written fixture.** An arm-level cover
  in [the hand-written fixtures](openapi-surface/handwritten/AGENTS.md) executes
  the arm, and crozier byte-matches the tree Fern generated from it. That is the
  same weaker proof as the `handwritten` rows, so each of the 83 is still
  one of the 91 [unreached arms](#every-unreached-arm-and-its-search-verdict).
  The cited records of 52 read `exhausted`, 30 read `search-incomplete`
  and 1 read `config-gated`. The bounded replacement searches preserve their
  limits. The config-gated `discriminator-mapping` arm runs only under an
  audience filter, which no search probe sets.
- **5 are reachable only by a document Fern refuses**, which leaves no Fern tree
  to byte-match. They are `enum-leading-zero-member`'s,
  `enum-leading-digit-identifier`'s and `enum-empty-identifier-member`'s
  enum-naming arms, refusal class `enum-name-unsuitable`, and `add_object`'s
  recursion guard, once each for `recursive-graph` and
  `mutually-recursive-graph`, refusal class `generator-lint-failure`. Each
  six-source search reads `exhausted`. Each record, a minimal refused document
  and a control Fern generates from, is in
  [Arms only a refused document reaches](fern-limitations.md#arms-only-a-refused-document-reaches).
- **3 are named gaps**, arms no proof crozier can show covers yet, each new with
  a row the example predicates of #361 made `golden`, and each `not searched`:
  `schema-example-empty-object`'s field-less model arm,
  `schema-example-object-on-map`'s `Dict` test and
  `schema-example-outside-enum`'s enum test
  ([Unproven arms, named](#unproven-arms-named)). `format-duration`'s `scalar_body` arm is reached on this measurement by corpus row 308,
  `yourbrand-ticketing`.

854 + 83 + 5 + 3 = 945. Fourteen sites left the table with the two functions
that served only the `Body_*` exemption and the HTTP Basic header drop,
`form_body_source_names` and `operation_uses_basic_auth`; the ledger re-joins its
committed measurement without them. No arm rests on a witness whose redistribution grant is
disputed. `ref-pointer-composition-index`'s `ref_to_class` composition-index
walk was reached only through corpus row 224 until that row was withdrawn for
its disputed grant. It now rests on the hand-written fixture
`composition-index-pointer` and is one of the 83. Corpus row 223
(`nexmo-conversation`) rested on the same aggregation-only grant and is
withdrawn too
([record](openapi-surface/withdrawn-witnesses/nexmo-conversation.md)).

**Earlier reconstruction from main's 826 of 886.** That historical
measurement was re-joined three ways over the 465 rows main's ledger held;
the 27 rows #361 adds bring 34 sites of their own, 31 reached and 3 the named
gaps above.

- **The corrected fixture-to-test mapping: 0 sites against main.** Main's ledger
  was measured at `c7fdee1b2`, whose mapper did not recognise
  `assert_committed_corpus_matches`; the census's `golden_registrations`, which
  `golden-reach.py` now reads, recognises every corpus assertion helper the
  tests use. Main's committed ledger already credits those witnesses: joined
  with the uncorrected mapper, that measurement reached 612 of main's 886
  sites, and joined with the corrected one 827, so the correction's 215 sites
  were in main's 826 already.
- **Withdrawing corpus row 223 (Nexmo): 0 sites lost.** Main's ledger was
  measured after the withdrawal, and no site main reached is unreached now. Its
  [record](openapi-surface/withdrawn-witnesses/nexmo-conversation.md) measured
  the loss when it was made: no site lost its last witness, two lost regions only
  it executed, and four behaviours lost their only golden (listed below).
- **Newly registered specifications: +1 site.** Of the specifications
  registered since `c7fdee1b2` (`yourbrand-ticketing`, `huatuo-node-tree`, the
  `apideck.com-ecosystem` re-registration under a client-class-name setting and
  the `crozier-property-name` target), `yourbrand-ticketing` reaches
  `format-duration`'s `scalar_body` arm; joined without them the measurement
  reaches 826.

**Every remaining unproven scenario, named.** Nothing below counts as a
real-specification match.

- **Features no proof covers (10):** the 8 `FIXTURE` gaps and the 2 residual-only
  `golden` rows above, each `not searched` or unattributable as stated there.
- **Output of a proven row that lands in an `unmatched` file (1):**
  `format-idn-hostname`'s `reference.md`. Its `client.py` and `raw_client.py`
  output is byte-matched on `short-io` and proven; the `reference.md` part is
  in `short-io`'s measured `unmatched` set, so no byte comparison covers it
  ([the attribution](#golden-rows-resting-only-on-residual-goldens)).
- **Arms no proof covers (3):** the 3 named gaps above, each `not searched`. No
  arm reads `search-incomplete`.
- **Features and arms resting on hand-written fixtures only (11 features, 54
  arms):** weaker proof, counted apart above; each fixture's cover cites the
  failed real-specification search that admitted it.
- **Behaviours the Nexmo withdrawal left on a hand-written fixture alone (4):** a
  `$ref` whose text names `properties` copied at the reference; such a union
  variant named after its reference with its `type` tag kept; a union of such
  copies tagged by its inferred `type`; and an unquoted YAML timestamp dropped as
  an optional non-temporal query-parameter example. Each rests on the
  hand-written `ref-pointer-walk` fixture, each real-specification search reads
  `search-incomplete` because none has been run, and the YAML-timestamp drop is
  an open gap: no real specification is known to witness it
  ([record](openapi-surface/withdrawn-witnesses/nexmo-conversation.md#the-reach-row-223-alone-carried)).
  No census selector names these four yet.
- **Authored-probe gaps (29):** every case committed under
  [`authored-probes/`](openapi-surface/authored-probes/README.md) is a document
  written to isolate one shape, with the tree pinned Fern generated from it, that
  crozier byte-matches. No real-specification search backs any of them, so each
  is an open gap of undecided evidence tier, neither a real-specification nor a
  hand-written match: [`353-method-optional-array`](openapi-surface/authored-probes/353-method-optional-array/), [`353-method-required-array`](openapi-surface/authored-probes/353-method-required-array/), [`353-promoted-required-array`](openapi-surface/authored-probes/353-promoted-required-array/), [`353-solo-required-array`](openapi-surface/authored-probes/353-solo-required-array/), [`353-string-default-control`](openapi-surface/authored-probes/353-string-default-control/), [`353-string-default-probe`](openapi-surface/authored-probes/353-string-default-probe/), [`353-string-default-scalar`](openapi-surface/authored-probes/353-string-default-scalar/), [`356-defs-pointer`](openapi-surface/authored-probes/356-defs-pointer/), [`356-defs-property`](openapi-surface/authored-probes/356-defs-property/), [`356-defs-required-property`](openapi-surface/authored-probes/356-defs-required-property/), [`358-absent-allof-member`](openapi-surface/authored-probes/358-absent-allof-member/), [`358-absent-array-item`](openapi-surface/authored-probes/358-absent-array-item/), [`358-absent-items-segment`](openapi-surface/authored-probes/358-absent-items-segment/), [`358-absent-map-value`](openapi-surface/authored-probes/358-absent-map-value/), [`358-absent-property`](openapi-surface/authored-probes/358-absent-property/), [`358-absent-request-body`](openapi-surface/authored-probes/358-absent-request-body/), [`358-absent-required-property`](openapi-surface/authored-probes/358-absent-required-property/), [`358-absent-response-body`](openapi-surface/authored-probes/358-absent-response-body/), [`358-undeclared-head-properties-required`](openapi-surface/authored-probes/358-undeclared-head-properties-required/), [`376-350-declared-type-name`](openapi-surface/authored-probes/376-350-declared-type-name/), [`376-350-declared-type-name-blank`](openapi-surface/authored-probes/376-350-declared-type-name-blank/), [`376-350-declared-type-name-shared`](openapi-surface/authored-probes/376-350-declared-type-name-shared/), [`376-350-declared-type-name-slash`](openapi-surface/authored-probes/376-350-declared-type-name-slash/), [`376-350-declared-type-name-tilde`](openapi-surface/authored-probes/376-350-declared-type-name-tilde/), [`376-354-model-property-construct`](openapi-surface/authored-probes/376-354-model-property-construct/), [`376-357-tag-only-operation-id`](openapi-surface/authored-probes/376-357-tag-only-operation-id/), [`parity-property-anyof-composed-members`](openapi-surface/authored-probes/parity-property-anyof-composed-members/), [`parity-required-query-array-examples`](openapi-surface/authored-probes/parity-required-query-array-examples/), [`parity-unrequired-tag-variant-classes`](openapi-surface/authored-probes/parity-unrequired-tag-variant-classes/). The `parity-property-` and `parity-unrequired-` cases vary the shapes registered corpus rows 311 and 312 witness once each: an inner `oneOf` and `anyOf` beside a sibling, each with and without a discriminator, and unrequired tags with no `default` under `oneOf` and `anyOf`. `parity-required-query-array-examples` varies the required query array that registered goldens declare on each side of the measured rule — corpus row 316 for a JSON response, `amazonaws.com-cloudformation` for `text/xml` and `query-parameters-openapi` for a required object parameter beside it — in three operations that differ in the decisive attribute alone.

Where crozier deliberately differs from Fern is decided per refusal class in
[`fern-refusals/`](fern-refusals/README.md). Each of its 39 classes is decided
`refuse`: crozier refuses those documents with or without `fern-strict`, so no
class is yet one where crozier generates and Fern does not. A `generate`
decision, which would write an SDK by default and refuse only under
`fern-strict`, is the registry's to make, with a wire test proving the SDK.

**What the census still cannot enumerate.** The 628 are what a selector over a
parsed document can count. What lies outside is a list, not a number, because
the census cannot measure the population beyond its own reach.

1. **Branches of generator functions no case analysis has read.** Only the six
   blind functions of `src/ir.rs` have
   [a case table](#the-six-blind-regions-of-srcirrs-case-by-case) that turns
   every branch into a selector. The 2026-09-28 golden-only coverage run still
   leaves 405 regions of `src/emit.rs`, 249 of `src/refs.rs` and 124 of
   `src/openapi.rs` blind ([the join](#the-ranked-list-against-golden-blind-spots)).
   Their branches are not features until a case table names them. Reading each
   function's branches into selectors, as was done for `src/ir.rs`, would bring
   them inside.
2. **Token-level and content-level value spaces outside the case table.** The
   enum-member connector joining, digit-adjacent underscores, Latin deburring
   and the arithmetic ranges of `numeric_enum_identifier`, and the example
   contents the case table names — empty arrays and objects, temporal strings,
   nested element kinds, required and undeclared fields — are counted now
   ([the case table](#enum-member-and-example-value-cases)): every branch it
   names has a predicate, and its hole column reads none. What stays outside is
   content a branch reads that no case table names, such as the unquoted YAML
   timestamp `src/emit.rs` drops as a query-parameter example, one of
   [the four behaviours the Nexmo withdrawal left on a hand-written fixture](openapi-surface/withdrawn-witnesses/nexmo-conversation.md#the-reach-row-223-alone-carried).
3. **Branches that switch on generated state rather than on the document.**
   `example_is_object` and `named_value_inner` match on the `TypeRef` or
   `TypeDecl` crozier builds. The four `on-ref-to` example readings
   resolve the `$ref` at an example site to the declaration those arms switch
   on, and `schema.properties:optional-example` names the `Optional` arm, so the
   arms the case table names are counted. A generated-state branch of a function
   no case table reads stays outside, which is entry 1.
4. **Names that are map keys, beyond the predicates declared for them.**
   Collisions and sanitization are counted for component-schema names, path
   templates and enum members, and an operation ID's leading-digit method name
   after `endpoint_method_name`'s transform is counted now. Property, parameter
   and header names are not. Name predicates over those maps, ported from
   `src/naming.rs` as the existing ones are, would bring them inside.
5. **Documents the census cannot read.** The census parses with a
   standard-library YAML subset. The witness searches recorded 4,380 candidate
   documents it refused for the thirteen keys searched as `FIXTURE` rows, and
   [`witness-search-recensus.py`](../tools/witness-search/witness-search-recensus.py) read
   every one of them again with the arm search's pinned `ruamel.yaml`: each is
   censused, or recorded `census-refused` with the parser's error
   ([the escalation](#generated-shapes-with-no-registrable-witness)). The
   census proper keeps its standard-library loader, which now also reads the
   three flow forms one of those documents, APWG's eCX description, writes,
   and explicit `? ` mapping keys, scalar and structured, as the pinned
   `ruamel.yaml` reads them: the pinned Stripe description, which needed the
   fallback for its three long component names, is
   [a committed sample](../tools/surface-census/tests/data/census-fallback-sample.tsv) the standard
   path reads to the full loader's counts (#363). What stays outside is the
   parse failures the searches recorded for keys already `golden`, and any
   document neither reading parses.
6. **Cross-document references beyond the pinned trees.** The census follows a
   relative `$ref` only inside a registered source's pinned tree, and an
   absolute-URL `$ref` only through
   [`corpus-remote-ref-pins.tsv`](../tests/fixtures/corpus-remote-ref-pins.tsv).
   Shapes a document reaches through any other reference are not counted.
   Pinning the referenced documents would bring them inside.
7. **The specification versions the walk was not read from.** The region files
   enumerate the OpenAPI 3.0.3 and 3.1.1 object tables. Fields a later minor
   version adds have no row until a region file walks that version's tables.
8. **Behaviour that is not document-derived.** CLI and configuration layering,
   the `ruff format` shell-out and the filesystem write path. Their code is
   `src/settings.rs`, `src/cli.rs`, `src/schema.rs`, `src/config.rs`,
   `src/pyfmt.rs`, `src/lib.rs` and `src/main.rs`. No OpenAPI shape selects it,
   so no census can count it. crozier's own journeys are its instrument, not
   a Fern golden.

**The denominator is the instrument's.** The grammar expansion grew it from
482 to 511. This pass adds 18 enum-member and example-kind features, bringing
it to 529, and the relative-file Path Item predicate adds the 530th. The PayPal
registration left its then-current denominator unchanged: it adds one source
and moves one existing feature from `gap` to `golden`. Re-deriving
`hoist_union_variant`'s case table when corpus row 193 gave it a nested-composition
arm adds four features, one per head and member spelling: two `golden` and two
`gap`. With the string-enum member arm's four, which the witness searches'
registrations added, and the four the closed and open empty-object disjunct of
`hoist_union_variant`'s closing object arm added (cases 10a to 10d, three
`golden` and one `gap`) when corpus rows 168 and 169 needed it, the walk counted
542, and `fergus` made one of the nested-composition arm's two `gap` rows,
`anyof-anyof-variant`, `golden`. The naming and example branches of #361 add
35 — 27 `golden` and 8 `gap` — bringing it to 577, and the component
composition of one primitive (`component-same-primitive-union`), a `handwritten`
row, to 578, the four worked-example shapes the example repairs measured
(`unread-date-time-example` and three `bodies-media` request-example shapes),
`handwritten` rows, to 582, the described inline scalar request body
(`request-body-described-inline-scalar`) and the status key spelled with a space
and a suffix (`response-status-space-suffixed`), two `handwritten` rows, to
584, the three `handwritten` rows the float, closed-object and reference-cycle
repairs added (`cycle-into-cycle`, `request-body-property-closed-empty-object`,
`type-misspelled-scalar`) to 587, and the three parameter-lowering shapes their
hand-written fixtures cover (`query-array-items-union`,
`header-subset-string-default` and `base-path-extension`), each a `handwritten`
row, to 590. The contentless 200 beside a 201 with content adds
`response-contentless-200-with-created`, one more `handwritten` row, to 593. The
parameter extension and serialization shapes add thirteen `handwritten` rows and
`single-operation-required-header`, a `golden` row, for **607**. Counting only the
registered rows whose Fern golden crozier byte-matches as golden sources (#352)
moved no row's category: every `golden` row's declarers include one.

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
just surface-census                                # every registered source (committed copies)
just surface-census --selector pathItem.trace      # one feature: who declares it, how often
just surface-census --fixture apideck.com-crm --json
```

Every registered source is committed: the 31 original
`tests/fixtures/<name>/openapi.*` documents and the remaining sources under
`tests/fixtures/corpus-sources/`, including every referenced file. Pinned URLs in
[`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md) are rebuild provenance;
`corpus-sources.tsv` records each file's digest. A missing source is a hard failure
rather than a silent zero. `just test-surface-census` drives the same script
without fetching; `just test-corpus-offline` also drives the complete census
recipe with sockets denied and no ignored cache.

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
`securityScheme.scheme`, `schema.additionalProperties`, `schema.example`.

The six example values are `schema.example=object`, `schema.example=array`,
`schema.example=string`, `schema.example=number`, `schema.example=boolean` and
`schema.example=null`. They are the JSON arms read by `example_matches_type` and
`example_from_json` of `src/emit.rs`; finer content tests remain enumeration holes.
Selection reads a non-null example field when written, otherwise the first
examples member, exactly as `schema_example` of `src/ir.rs` reads its
`Option<Value>` field. An empty examples array selects nothing, a null example
falls through to that array, and a non-null scalar takes precedence over it.
`de_schema_examples` also accepts a map of named Example Objects, selecting the
first entry's value, or a single scalar as a one-member list; the census makes
the same selection before assigning the kind.

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

For a registered source tree, the walk follows a relative `$ref` only when its
resolved file is one of that tree's pinned members. It reads the referenced
object at its writing position, once even when several documents point to it;
each `$ref` declaration still counts at its own site. The object keeps its
normal selector kind (for example, `schema.properties` in a sibling schema
file). A reference outside the registered tree contributes only its `$ref`
declaration, never fields from the unregistered target.

`pathItem.$ref:relative-file` counts the referencing Path Item when its `$ref`
names a relative file, whether or not that file is registered. The ordinary
`pathItem.$ref` selector still counts every reference spelling; this predicate
distinguishes the file path that `src/refs.rs` resolves from a local pointer or
absolute URL. The resolver also accepts absolute local filesystem paths; those
remain ordinary `pathItem.$ref` declarations because this predicate describes
relative files only.

A shape the two kinds above cannot express emits a **predicate selector**,
`<selector>:<predicate>` — the notation
[`security.md`](openapi-surface/security.md)'s method notes already use for a
shape the field selector cannot read (`securityScheme:$ref`). A field selector says a
field was written and a valued selector says which member of a closed set it was
written with; neither can say anything about a field's *array members*, about two
declarations' values *compared*, or about the map keys the count rule above
deliberately excludes as names. The predicates are themselves a closed list of
116, declared in `tools/surface-census/openapi-surface-census.py` and restated here, with a
drift gate over the pair:

- `pathItem.$ref:relative-file` — one per Path Item Object whose `$ref` names
  a relative file; its declaration counts even when the target is outside the
  registered tree.
- `info.title:non-ascii` — one per Info Object whose title contains a
  non-ASCII character; this distinguishes the title probe from its control.
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
- `components.schemas:nonidentifier-name` — one per component schema name whose
  Pascal casing contains a character `sanitize_identifier` replaces with `_`.
- `components.schemas:same-primitive-union` — one per component schema whose
  `oneOf` (else `anyOf`) holds two or more inline scalar alternatives that all
  convert to one primitive, with nothing declared beside them — the shape
  `same_primitive_union_last` of `src/ir.rs` reads and
  `normalize_same_primitive_unions` of `src/openapi.rs` renames after its last
  alternative's ordinal. Read at the Components Object, the one position where
  the name shows; `integer` and `format: int64` convert to different primitives,
  as Fern keeps them apart.
- `schema.example:unread-date-time` — one per `format: date-time` Schema Object
  whose selected example is a string Fern's reading rejects once it has appended
  `Z` to a value that neither ends in `Z` nor holds a `+`; `datetime_example` of
  `src/emit.rs` writes Fern's default for it.
- `mediaType.schema:allof-parent-body` — one per request body's selected JSON
  media type whose schema `$ref`s a component composed `allOf` of one inline
  object and one `$ref` base, which another component's `allOf` names in turn,
  and whose example names a required field of each side: the body whose
  Markdown examples list their own fields first.
- `mediaType.example:nested-null-member` — one per request body's selected JSON
  media type whose example (its `example`, else its first named one) gives
  `null` to a property a nested object's schema declares and does not require.
- `mediaType.example:deprecated-property` — one per request body's selected JSON
  media type whose example names, at any depth, a property whose own schema is
  marked `deprecated: true` — not one it reaches through a `$ref` or an `allOf`,
  as `own_deprecated` of `src/ir.rs` reads it.
- `components.schemas:fields-reach-cycles-unsorted` — one per component schema
  composing no `oneOf` or `anyOf` whose `properties`, read in order, name
  members of two or more reference cycles (strongly connected components of the
  `components.schemas` `$ref` graph), where each cycle's members sorted and the
  cycles taken in the order the properties first reach them are not in sorted
  order: the trailing deferred imports `object_deferred_order` of `src/emit.rs`
  writes in that order.
- `components.schemas:cycle-into-cycle` — one per component schema composing no
  `oneOf` or `anyOf` that names a member of a reference cycle with an edge into
  a different reference cycle the schema names no member of: the case
  `forward_repair_map` of `src/emit.rs` repairs with the first cycle only.
- `mediaType.schema:closed-empty-object-property` — one per inline schema
  `{type: object, additionalProperties: false}` declaring no `properties` that is
  a property of a request body's selected JSON media type's inline schema: the
  position `base_type_ref` of `src/ir.rs` types `Dict[str, Any]` where
  `is_inline_struct` once hoisted an empty model. The same object as an inline
  success response is corpus row 314's.
- `schema.type:misspelled-scalar` — one per Schema Object whose `type` names
  `double`, `int32`, `long`, `bool` or `decimal`, none an OpenAPI type: Fern
  reads each as unknown, and `base_type_ref` types it `Any` too. `float`, which
  `normalize_float_type` of `src/openapi.rs` reads as a number, and `int` are
  corpus row 313's, and kept apart.
- `securityScheme:$ref` — one per `components.securitySchemes` entry that is a
  Reference Object rather than a Security Scheme Object, the entry
  `normalize_security_scheme_refs` of `src/openapi.rs` resolves. The walk counts
  every Reference Object as `reference.$ref` wherever it stands, so this is read
  at the Components Object, from that one map's own values.
- `schema.enum:empty-member` — one per schema with an empty string enum member;
  `enum_words` names that member EMPTY.
- `schema.enum:empty-identifier-member` — one per schema with a non-empty
  string enum member whose normalized identifier is empty; `finalize_enum_ident`
  supplies `_`.
- `schema.enum:wildcard-member` — one per schema with a string enum member
  containing `*`, which `enum_words` spells ALL when it is the whole value and
  treats as a word boundary otherwise (Tally's `image/*` is `IMAGE`).
- `schema.enum:apostrophe-member` — one per schema with a string enum member
  containing an ASCII or curly apostrophe, which `enum_words` removes.
- `schema.enum:digit-word-member` — one per schema with a UUID-shaped string
  enum member beginning with exactly one digit before a letter; this is the
  `digit_word` branch of `uuid_enum_identifier`.
- `schema.enum:numeric-prefix-member` — one per schema with a string enum
  member beginning with a canonical integer from 10 to 9999; the numeric
  prefix is spelled in English by `numeric_enum_identifier`.
- `schema.enum:leading-zero-member` — one per schema with a string enum member
  containing a multi-digit leading-zero token, which the canonical numeric
  reader refuses.
- `schema.enum:leading-digit-identifier` — one per schema with a string enum
  member whose normalized identifier still begins with a digit, so
  `finalize_enum_ident` prefixes `_`.
- `schema.enum:uuid-member` — one per schema with a UUID-shaped string enum
  member, which takes `uuid_enum_identifier` rather than `enum_words`.
- `schema.enum:reserved-member` — one per schema with a string enum member
  whose normalized visit parameter is reserved, so `finalize_enum_ident`
  appends `_`.
- `schema.enum:normalized-collision` — one per schema with two string enum
  members yielding the same crozier member identifier after normalization.
- `schema.enum:numeric-member` — one per schema with a numeric enum member;
  `string_enum_values` does not yield a named member from it.
- `schema.enum:deburred-member` — one per schema with a string enum member
  holding a Latin-1 Supplement or Latin Extended-A letter, which
  `enum_identifier`'s `deburr` folds to ASCII before naming it (`SUBSTÂNCIA` is
  `SUBSTANCIA`).
- `schema.enum:letter-run-member` — one per schema with a string enum member
  whose split words hold consecutive single letters, which `enum_words` joins
  into one word (`u.s. virgin islands` is `US_VIRGIN_ISLANDS`).
- `schema.enum:alphanumeric-join-member` — one per schema with a string enum
  member where `enum_words` joins a word to the one before it: a letter run of
  at most two after a digits-then-letter word, or a letter-then-digits word
  after a single letter (`a b12` is `AB12`).
- `schema.enum:digit-boundary-member` — one per schema with a string enum
  member whose joined words carry an underscore beside a digit, which
  `enum_words` collapses (`DB-25` is `DB25`).
- `schema.enum:single-digit-prefix-member` — one per schema with a string enum
  member whose leading numeric run, as written, is one digit that `enum_words`
  spells through `numeric_enum_identifier` (`5G` is `FIVE_G`).
- `schema.enum:numeric-small-member`, `schema.enum:numeric-tens-member`,
  `schema.enum:numeric-hundreds-member` and
  `schema.enum:numeric-thousands-member` — one per schema with a string enum
  member whose number `enum_words` spells through `numeric_enum_identifier`
  falls in that function's below-20, 20-to-99, 100-to-999 or 1000-to-9999
  branch. Each reads the number the function is handed — a zero-led whole value
  read without its zeros, or a leading run — so `05` is small and `1200 bps`
  thousands.
- `operation.operationId:digit-leading-method` — one per Operation Object under
  the Paths Object whose `operationId`-derived method name starts with a digit,
  so `sanitize_identifier` prefixes it with `_`. The name is
  `endpoint_method_name`'s after its tag, group, FastAPI-suffix, duplicate-suffix
  and template transforms, which the census ports function by function; an
  operation naming its method by extension, or by no id, is not one.
- `schema.example:date-time-string` and `schema.example:date-string` — one per
  schema writing `format: date-time` (or `date`) whose selected example is a
  string, which `value_from_example` renders through
  `datetime.datetime.fromisoformat` (or `datetime.date.fromisoformat`).
- `schema.example:integral-on-number` — one per schema whose primary type is
  `number` and whose selected example is a JSON integer, which
  `value_from_example` writes with a `.0` for the float annotation.
- `schema.example:fractional-on-integer` — one per schema whose primary type is
  `integer` and whose selected example is a JSON fraction, which
  `example_matches_type`'s integer arm refuses.
- `schema.example:empty-array` and `schema.example:empty-object` — one per
  schema whose selected example is `[]` (or `{}`).
- `schema.example:array-null-element` — one per schema whose selected example
  is an array holding a `null`, which `value_from_example`'s list arm replaces
  with a synthesized element.
- `schema.example:array-object-element` — one per schema whose selected example
  is an array holding an object, a nested element the list arm renders through
  the item type.
- `schema.example:temporal-duplicate-element` — one per schema whose `items`
  write `format: date` or `date-time` and whose selected example repeats an
  element, which the list arm de-duplicates.
- `schema.example:union-ref-sentinel` — one per schema declaring `oneOf` or
  `anyOf` whose selected example is an object holding only `$ref`, which
  `value_from_example`'s union arm answers with its list member.
- `schema.example:missing-required-field` and `schema.example:undeclared-field`
  — one per schema with a non-empty `properties` map whose selected example is
  an object omitting a property `required` names (or holding a key the map does
  not declare); `example_matches_type`'s object arm refuses either.
- `schema.example:empty-object-member` and `schema.example:empty-array-member`
  — one per schema whose selected example is an object one of whose values is
  `{}` (no argument for an optional model field) or `[]` (no example value for
  the field).
- `schema.example:object-on-map` — one per schema writing
  `additionalProperties` as `true` or a schema, with no non-empty `properties`
  map, whose selected example is an object: the `Dict` an example renders as a
  dictionary.
- `schema.example:outside-enum` — one per schema with a string-valued `enum`
  whose selected example is a string none of its members is, which
  `example_matches_type`'s enum arm refuses.
- `schema.example:on-ref-to-object`, `schema.example:on-ref-to-enum`,
  `schema.example:on-ref-to-union` and `schema.example:on-ref-to-alias` — one
  per schema with a selected example whose `$ref` resolves, in the document's
  own `components.schemas`, to a schema declaring a non-empty `properties` map
  (object), a string-valued `enum` (enum), a `oneOf` or `anyOf` (union), or none
  of those nor an `allOf` (alias): the named declaration `named_value_inner` and
  `example_is_object` switch on, reached from the example site. A target
  declaring a union counts as one before anything else it declares, and an enum
  before an object.
- `schema.properties:optional-example` — one per schema one of whose
  properties its `required` list does not name selects an example: the
  `Optional` the example arms unwrap first.
- `parameter.example:non-scalar-query` — one per query Parameter Object
  declaring an example whose schema, after one local `$ref`, is neither a
  string, integer, number or boolean nor an array of one, so
  `build_example_inner` does not render the declared example.
- `parameter.schema:query-items-union` — one per query Parameter Object whose
  inline schema is an array whose inline `items` is a `oneOf` (else `anyOf`) of
  two or more non-null members: the union `hoist_param_enum` hoists as the
  parameter's `{Param}Item`.
- `parameter.schema:subset-header-string-default` — one per header Parameter
  Object declaring a non-empty string `default` whose name rides at least three
  quarters but not all of the document's operations and is neither a header the
  transport or an apiKey scheme owns nor `Authorization`: the header
  `global_headers` promotes as a one-value `Literal`.
- `parameter.in:absent` — one per inline Parameter Object with a name and an
  inline schema but no `in` field: the parameter `build_endpoint` skips.
- `parameter.schema:nullable-array-explode-false` — one per optional form-style
  query Parameter Object writing `explode: false` whose inline schema is a
  `nullable: true` array of strings: the list sent unjoined.
- `parameter.schema:nullable-array-items-oas-three-zero` — one per query Parameter Object
  of an OpenAPI 3.0 document whose inline array schema's inline `items` is a
  `nullable: true` scalar: the item nullability the query type drops.
- `parameter.schema:required-nullable-scalar-oas-three-zero` — one per required query
  Parameter Object of an OpenAPI 3.0 document whose inline scalar schema is
  `nullable: true`: the required parameter lowered as optional.
- `parameter.schema:date-union-query-oneof` — one per query Parameter Object
  whose inline `oneOf` has an integer member and a `format: date` string
  member: the union the query serializer converts.
- `parameter.schema:promoted-date-header` — one per `format: date` header
  Parameter Object whose name rides at least three quarters of the document's
  operations and is neither a header the transport or an apiKey scheme owns nor
  `Authorization`: the client field typed `dt.date`.
- `parameter.schema:single-required-header` — one per required header
  Parameter Object of a document with exactly one operation: the header
  `global_headers` promotes to a required constructor field.
- `operation.parameters:path-order-oas-three-one` — one per Operation Object of an
  OpenAPI 3.1 document declaring two or more untitled path parameters in an
  order other than its URL template's, with no path-level path parameter: the
  signature `build_endpoint` orders by template position.
- `mediaType.examples:named-beside-example` and `mediaType.examples:named-only`
  — one per request body's selected JSON media type writing a named example that
  resolves to a value, beside a non-null `example` (which `reference.md` then
  documents) or without one (the first named one is documented).
- `operation.responses:wildcard-binary` — one per Operation Object whose success
  response, chosen as `has_wildcard_binary_response` chooses it, serves `*/*`
  with an inline string schema of format `binary`: the endpoint mode
  `build_example_inner` reads before it renders any parameter example.
- `operation.requestBody:body-prefixed-single-use` — one per Operation Object
  other than a GET or HEAD whose request body's `application/json` schema is a
  `$ref` to a `components.schemas` entry named `Body_…` that no other `$ref` of
  the document names: FastAPI's embedded-body model, which
  `inline_body_source_names` of `src/ir.rs` drops like any single-use body.
- `operation.requestBody:titled-inline-container-oas-three-zero` — one per Operation
  Object of an OpenAPI 3.0 document, declaring no parameter itself or on its
  Path Item, whose request body's `application/json` schema is an inline array
  or map (`additionalProperties` true or a schema, no `properties`) declaring a
  `title`: the body `inline_container_carries_content_type` of `src/ir.rs` sends
  the JSON content-type header for.
- `operation.responses:contentless-two-hundred-with-created` — one per operation
  whose 200 response declares no content while its 201 declares content,
  resolving local Response Object references. `success_response_with_content`
  selects the latter body, preserving a 200 with content as the first choice.
- `operation.responses:empty-schema-success-oas-three-zero` — one per Operation Object of
  an OpenAPI 3.0 document whose success response, declared inline rather than by
  a Response `$ref`, holds an `application/json` media type whose `schema` is the
  empty schema `{}` and no other media type: the unknown body
  `response_may_be_empty` of `src/ir.rs` guards.
- `operation.responses:schemaless-text-success` — one per Operation Object whose
  success response holds a `text/*` media type other than `text/event-stream`
  declaring no `schema`, and no `application/json` beside it: the body
  `success_response` of `src/ir.rs` types `str`.
- `operation.responses:schemaless-download-success` — one per Operation Object
  whose success response holds an `audio/*`, `video/*` or `application/pdf`
  media type declaring no `schema`, and no `application/json` beside it: the
  download `is_download_media_type` of `src/ir.rs` streams.
- `operation.requestBody:blank-description-optional-object` — one per Operation
  Object declaring no parameter itself or on its Path Item whose request body's
  `description` is the empty string and whose `application/json` schema, inline
  or behind one local `$ref`, declares properties not all of which `required`
  lists: the body crozier once sent without the JSON content-type header.
- `operation.requestBody:described-inline-scalar` — one per Operation Object
  declaring no parameter itself or on its Path Item whose request body's
  `application/json` schema is an inline string, integer, number or boolean
  declaring no `enum` and a `description`: the body `resolve_request_body` of
  `src/ir.rs` sends with the JSON content-type header, where a `title` alone
  does not.
- `operation.requestBody:plain-string-map` — one per Operation Object whose
  JSON-like request content declares a top-level object without named
  properties, with an unformatted, non-enum, non-nullable string
  `additionalProperties` schema. Local component references are resolved with
  cycle protection, and multiple qualifying media types still count once.
- `operation.requestBody:schemaless-json` — one per Operation Object whose
  request body's content holds only JSON media types and none of them declares a
  `schema`: the body `request_body_ignored` of `src/ir.rs` sends nothing for.
- `operation.responses:schemaless-wav-success` — one per Operation Object whose
  success response holds an `audio/wav` media type declaring no `schema`, and no
  `application/json` beside it: the download `is_download_media_type` of
  `src/ir.rs` streams.
- `operation.responses:space-suffixed-status-key` — one per Responses Object key,
  of an operation the Paths Object holds, that is a three-digit status code, a
  space and further text (`429 (live)`): the spelling `response_key_status` of
  `src/ir.rs` reads by its leading integer.
- `operation.responses:suffixed-status-key` — one per Responses Object key, of
  an operation the Paths Object holds, that begins with a digit and is neither a
  three-digit status code nor an upper-case range (`4XX`): the spelling
  `response_key_status` of `src/ir.rs` reads by its leading integer.
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
- `schema.type:primary=object` — one per Schema Object whose `type` names
  `object` first among its non-`null` members, which is the first disjunct of
  `src/ir.rs`'s `is_object_type` and the reading every arm that asks whether a
  schema closes an object makes.
- `schema.type:primary-scalar` — one per Schema Object whose `type` names
  `string`, `number`, `integer` or `boolean` first among its non-`null` members,
  which is exactly what `src/ir.rs`'s `declares_scalar_type` reads. It is one
  predicate rather than four because the arms reading it read the disjunction and
  never one member of it, and it is not the four valued spellings `schema.type` =
  `string` and its neighbours emit: those count a 3.1 `type` of `[object,
  string]`, whose primary member is `object`, and this does not.
- `schema.properties:non-empty` — one per Schema Object whose `properties` map
  holds at least one entry, so a declared-but-empty `properties: {}` counts
  none.
- `schema.oneOf:sole-member` — one per Schema Object whose `oneOf` array holds
  exactly one member.
- `schema.anyOf:sole-member` — one per Schema Object whose `anyOf` array holds
  exactly one member.
- `schema.allOf:sole-member` — one per Schema Object whose `allOf` array holds
  exactly one member, the arity `src/ir.rs`'s `sole_inline_all_of` tests, on the
  same terms as the two above.
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
- `schema.example:schema-shaped` — one per Schema Object whose selected example
  is a non-empty object every value of which is an object declaring at least one
  of `type`, `$ref`, `properties`, `allOf`, `oneOf` or `anyOf`. Selection uses
  `example`, then the first `examples` member, and the content test is the one
  `src/ir.rs`'s since-removed `example_is_schema_definition` made.

**Seventy-four of the 116 are node-local**, which is what makes them one family:
each is decided from one object-model node's own declared fields and their
values, with no `$ref` resolution and no document-scope comparison. The six
`schema.$ref:` spellings that read a pointer's segment structure are node-local
in exactly that sense — a `$ref` *value* is one of the node's own declared
fields, and reading its segments is not resolving it, and so is
`schema.allOf:annotated-ref`, which reads one node's `allOf` members and no
further, and `schema.example:unread-date-time`, which reads one node's `format`
and selected example. The other
forty-two — `operation.operationId:duplicate`,
`openapi.paths:normalized-collision`, `components.schemas:normalized-collision`,
`schema.$ref:undeclared-component-head`,
`schema.$ref:resolves-to-component`, `schema.oneOf:discriminated-union`,
`schema.anyOf:discriminated-union`,
`schema.discriminator:inheritance-union`,
`parameter.schema:subset-header-string-default`,
`parameter.schema:promoted-date-header`,
`parameter.schema:single-required-header`,
`operation.operationId:digit-leading-method`,
`operation.responses:wildcard-binary`, `parameter.example:non-scalar-query`,
`mediaType.examples:named-beside-example`, `mediaType.examples:named-only`,
`schema.example:on-ref-to-object`, `schema.example:on-ref-to-enum`,
`schema.example:on-ref-to-union`, `schema.example:on-ref-to-alias`,
`operation.requestBody:body-prefixed-single-use`,
`operation.requestBody:titled-inline-container-oas-three-zero`,
`operation.responses:empty-schema-success-oas-three-zero`,
`operation.responses:schemaless-text-success`,
`operation.responses:schemaless-download-success`,
`operation.responses:suffixed-status-key`,
`operation.requestBody:schemaless-json`,
`operation.responses:schemaless-wav-success`,
`operation.responses:space-suffixed-status-key`,
`operation.requestBody:blank-description-optional-object` and
`operation.requestBody:described-inline-scalar`,
`operation.requestBody:plain-string-map`,
`operation.responses:contentless-two-hundred-with-created`,
`parameter.schema:nullable-array-items-oas-three-zero`,
`parameter.schema:required-nullable-scalar-oas-three-zero`,
`operation.parameters:path-order-oas-three-one`,
`mediaType.schema:allof-parent-body`, `mediaType.example:nested-null-member`,
`mediaType.example:deprecated-property`,
`components.schemas:fields-reach-cycles-unsorted`,
`components.schemas:cycle-into-cycle` and
`mediaType.schema:closed-empty-object-property` — read the document beyond the
node, and say so in their own sentence. The first eleven and the two cycle
readings compare one document's own values against each other; the next
twenty-five read where the node stands (an operation's route, a request body's
selected media type, the document's version) or resolve one local
`#/components/...` reference; the last four read a request body's selected
media type and resolve the `#/components/schemas/...` references reached by its
schema or examples. Those two
numbers partition the closed list, and a check reconciles the split with it. Every
document-reading predicate reads **the document context**: the census carries the
document's own `components` maps, its route and request-body positions, and the
set of its schema keys, reachable from every node it walks, and it is the
document being censused and nothing else — no fetch, no cross-document
resolution, no second document. A property that would need the *shape* of the
schema a `$ref` points at is a predicate in two cases only: the four
`on-ref-to` example readings and the last three request-example readings,
because the arms they are read off are `src/emit.rs`'s, which no `src/ir.rs`
case can carry a `~>` conjunction for.
Everywhere else it is declared nowhere: that is what the `~>` operator below
descends for.

A predicate selector is a selector like any other everywhere else: `--selector`
accepts one, refuses a misspelling of one by name, and reports an undeclared one
as absent.

##### The member-only readings

Five readings are a conjunction **member** and are not selectors. They are a
closed list of 5, declared as `MEMBER_ONLY_PREDICATES` in
`tools/surface-census/openapi-surface-census.py` and restated here, with a drift gate over the
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
  `hoist_union_variant` sent all three to `base_type_ref` while it still hoisted
  a bare object with a concrete example. One-hundred-and-six of the
  one-hundred-and-seven cases below survive this test; the other one names the
  extension that would close it.

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
The frozen closed-member witness searches retain their original selectors,
which count members with or without `properties`. Cases 12c and 12d use the
stricter selectors requiring that field; the historical search counts do not
measure those stricter cases.

The conjunctions are themselves a closed list of 96, declared in
`tools/surface-census/openapi-surface-census.py` beside the predicate table and restated here,
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
- `schema.oneOf>schema.enum:string-valued` — one per Schema Object one of
  whose `oneOf` members declares a string-valued `enum`.
- `schema.anyOf>schema.enum:string-valued` — one per Schema Object one of
  whose `anyOf` members declares a string-valued `enum`.
- `schema.oneOf>schema.const:string-valued` — one per Schema Object one of
  whose `oneOf` members declares a string-valued `const`.
- `schema.anyOf>schema.const:string-valued` — one per Schema Object one of
  whose `anyOf` members declares a string-valued `const`.
- `schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&!schema.example:schema-shaped&!schema.properties:non-empty&schema.example=object&schema.type:primary=object` — one per Schema Object one of whose `oneOf` members is a bare object carrying an object-valued example that is not itself a schema definition.
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
- `schema.oneOf>schema.oneOf` —
  one per Schema Object one of whose `oneOf` members itself declares `oneOf`.
- `schema.oneOf>schema.anyOf` —
  one per Schema Object one of whose `oneOf` members itself declares `anyOf`.
- `schema.anyOf>schema.oneOf` —
  one per Schema Object one of whose `anyOf` members itself declares `oneOf`.
- `schema.anyOf>schema.anyOf` —
  one per Schema Object one of whose `anyOf` members itself declares `anyOf`.
- `schema.properties>schema.enum:string-valued` — one per Schema Object one of
  whose properties declares a string-valued `enum`.
- `schema.properties>schema.const:string-valued` — one per Schema Object one
  of whose properties declares a string-valued `const`.
- `schema.properties>schema.properties:non-empty` — one per Schema Object one
  of whose properties declares a non-empty `properties` map.
- `schema.properties>schema.additionalProperties=false&schema.properties` — one per Schema
  Object one of whose properties writes both `additionalProperties: false` and `properties`, including an empty map.
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
- `schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.additionalProperties=false` — one per Schema Object one of whose properties
  declares a one-member `oneOf` whose member writes `additionalProperties: false`,
  whether or not it writes `properties`.

- `schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.additionalProperties=false&schema.properties` —
  one per Schema Object one of whose properties declares a one-member `oneOf`
  whose member writes both `additionalProperties: false` and `properties`, including an empty map.
- `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.additionalProperties=false` — one per Schema Object one of whose properties
  declares a one-member `anyOf` whose member writes `additionalProperties: false`,
  whether or not it writes `properties`.

- `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.additionalProperties=false&schema.properties` —
  one per Schema Object one of whose properties declares a one-member `anyOf`
  whose member writes both `additionalProperties: false` and `properties`, including an empty map.
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
- `schema.items>!schema.type:primary-scalar&schema.allOf` —
  one per Schema Object whose `items` value declares `allOf` and declares no
  scalar `type`, which is the composition disjunct of `is_inline_struct`.
- `schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` —
  one per Schema Object whose `items` value writes an explicitly empty
  `properties` map beside no `additionalProperties`, on an `object` primary
  type.
- `schema.oneOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` declaring `allOf` and no scalar `type`.
- `schema.anyOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` declaring `allOf` and no scalar `type`.
- `schema.oneOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` —
  one per Schema Object one of whose `oneOf` members declares `array` as its
  primary type over `items` writing an explicitly empty `properties` map
  beside no `additionalProperties`, on an `object` primary type.
- `schema.anyOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` —
  one per Schema Object one of whose `anyOf` members declares `array` as its
  primary type over `items` writing an explicitly empty `properties` map
  beside no `additionalProperties`, on an `object` primary type.
- `schema.properties>!schema.$ref&!schema.additionalProperties&!schema.anyOf&!schema.enum&!schema.items&!schema.oneOf&!schema.properties&!schema.type&schema.allOf:sole-member&schema.allOf>!schema.$ref` —
  one per Schema Object one of whose properties is a one-member `allOf` and
  nothing else — no `$ref` of its own and none on the member, no `type`, no
  `properties`, no `oneOf`, no `anyOf`, no `items`, no
  `additionalProperties` and no `enum` — which is the shape
  `sole_inline_all_of` of `src/ir.rs` reads.
- `schema.properties>!schema.type:primary-scalar&schema.allOf` —
  one per Schema Object one of whose properties declares `allOf` and
  declares no scalar `type`.
- `schema.properties>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` —
  one per Schema Object one of whose properties writes an explicitly empty
  `properties` map beside no `additionalProperties`, on an `object` primary
  type.
- `schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.type:primary-scalar&schema.allOf` —
  one per Schema Object one of whose properties declares a one-member
  `oneOf` whose member declares `allOf` and no scalar `type`.
- `schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf` —
  one per Schema Object one of whose properties declares a one-member
  `anyOf` whose member declares `allOf` and no scalar `type`.
- `schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` —
  one per Schema Object one of whose properties declares a one-member
  `oneOf` whose member writes an explicitly empty `properties` map beside no
  `additionalProperties`, on an `object` primary type.
- `schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` —
  one per Schema Object one of whose properties declares a one-member
  `anyOf` whose member writes an explicitly empty `properties` map beside no
  `additionalProperties`, on an `object` primary type.
- `schema.oneOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` —
  one per Schema Object one of whose `oneOf` members writes an explicitly
  empty `properties` map beside no `additionalProperties`, on an `object`
  primary type.
- `schema.anyOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` —
  one per Schema Object one of whose `anyOf` members writes an explicitly
  empty `properties` map beside no `additionalProperties`, on an `object`
  primary type.
- `schema.oneOf>!schema.properties:non-empty&schema.additionalProperties=false&schema.properties&schema.type:primary=object` —
  one per Schema Object one of whose `oneOf` members writes an explicitly
  empty `properties` map beside `additionalProperties: false`, on an
  `object` primary type.
- `schema.anyOf>!schema.properties:non-empty&schema.additionalProperties=false&schema.properties&schema.type:primary=object` —
  one per Schema Object one of whose `anyOf` members writes an explicitly
  empty `properties` map beside `additionalProperties: false`, on an
  `object` primary type.
- `schema.items>!schema.$ref&!schema.additionalProperties=false&!schema.anyOf&!schema.anyOf:discriminated-union&!schema.discriminator:inheritance-union&!schema.oneOf&!schema.oneOf:discriminated-union&!schema.properties:non-empty&!schema.type:primary=array` —
  one per Schema Object whose `items` value declares none of the members
  `nested_array_element`'s other cases carry, which is the residual arm its
  closing `None` is.
- `schema.oneOf>!schema.$ref&!schema.allOf&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty` —
  one per Schema Object one of whose `oneOf` members declares none of the
  members `hoist_union_variant`'s other cases carry at the variant, which is
  the residual arm its closing `base_type_ref` is.
- `schema.anyOf>!schema.$ref&!schema.allOf&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty` —
  one per Schema Object one of whose `anyOf` members declares none of them,
  the same residual arm reached through the other union head.
- `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>!schema.additionalProperties=false&!schema.allOf&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty` —
  one per Schema Object one of whose properties is an annotated `$ref` whose
  target declares none of the members the arms inside `prop_type_ref`'s
  resolution gate read, which is the residual arm its closing
  `full_type_ref_resolved` is.
- `schema.properties>!schema.oneOf:discriminated-union&!schema.oneOf:sole-non-null-member&schema.oneOf` —
  one per Schema Object one of whose properties declares a `oneOf` that is
  none of the shapes the arms inside `prop_type_ref`'s composition gate
  read, which is the residual arm its closing union alias is.
- `schema.properties>!schema.anyOf:discriminated-union&!schema.anyOf:sole-non-null-member&schema.anyOf` —
  one per Schema Object one of whose properties declares an `anyOf` that is
  none of them, the same residual arm reached through the other composition
  spelling.
- `schema.properties>!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty&!schema.type:primary=array` —
  one per Schema Object one of whose properties declares none of the members
  `prop_type_ref`'s own arms carry, which is the residual arm its closing
  `base_type_ref` is.

A conjunction selector is a selector like any other everywhere else: `--selector`
accepts one, refuses a misspelling of one by name — and refuses a well-formed
combination nobody declared, because the list is closed by the code rather than
by the operators — and reports an undeclared one as absent.

The five `schema.$ref:pointer-walk-reaches=` entries above are the five arms of
`resolve_schema_pointer`'s segment loop, each
behind that function's own **caller gate**: `field_type_ref` calls it on an
array-typed property's `items` reference and nowhere else, so the three members in
front of the [member-only reading](#the-member-only-readings) are what keep the
count off a pointer the generator never walks.
`openbanking-brasil-directory` writes such a pointer — its
`#/components/schemas/ClientCreationResponse/properties/client_id` sits on a path
parameter's schema — and no selector counts it, because that node selects no case
of the function's table. Declaring the reading on its own would have counted it,
which is why it is a member and not a selector.

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
| `category` | exactly one of `golden`, `limitations`, `handwritten`, `gap` |
| `evidence` | see the category rules below — each category fixes what belongs here |
| `crozier sites` | **required on a `gap` row**: the `src/` files that read this feature and how many distinct places in them do, or `none` when crozier reads it nowhere. A measurement, and what the ranking's first two criteria are computed from. **On a `golden` row it is the row's reach cell** — which declared handling sites its golden-only witnesses execute and which they do not — generated by `just golden-reach` and never edited by hand ([Golden reach, row by row](#golden-reach-row-by-row)). Empty on a `limitations` or `handwritten` row |
| `why bytes could move` | **required on a `gap` row, empty otherwise**: one sentence naming the generated artifact that would differ if crozier and Fern disagree about this feature |
| `settlement` | **required on a `gap` row, empty otherwise**: one of `FIXTURE`, `PROBE` or `UNREACHABLE`, followed by one sentence saying what settling it takes |

## Parity repair proof index

These 35 rows are the 27 generator categories, the base-path and string-map
example gaps, and the six additional scenarios the parameter fix closed.
Other scenarios remain in a separate follow-on plan and are not proof claims
here. Each path is committed output from Fern CLI **5.67.1** with
`fernapi/fern-python-sdk` **5.20.0**, compared by the named deterministic e2e
test. Hand-written and measurement documents certify their shapes without
counting as real-specification matches.

The defect ids are the `kind: fern-defect` entries of
[`assets/departures.yml`](../assets/departures.yml), each assigned to one row.
Their evidence notes and the line-pinned
[`departures ledger`](../tests/fixtures/departures-ledger.tsv) describe the
corrections the shared comparison engine applies. All other bytes must match.

| gap | shape | classification | closing node | committed proof | comparison test | defect ids |
|---|---|---|---|---|---|---|
| same-type-anyof-alias-name | Named component union of members with the same primitive type | Fern behaviour | `fix-unions` | docs/openapi-surface/handwritten/same-primitive-union-components/fern-expected | `handwritten_fixtures_match_fern_goldens` | — |
| nested-discriminated-union-in-anyof | Discriminated union nested inside an ordinary union | Fern behaviour | `fix-unions` | tests/fixtures/oal-example/expected | `oal_example_matches_fern_output` | — |
| discriminated-union-variant-classes | Tagged member wrappers and classes | Fern behaviour | `fix-unions` | tests/fixtures/qontract-api/expected | `qontract_api_matches_fern_output` | — |
| variant-required-fields-optional | Optional properties of tagged union variants | Fern behaviour | `fix-unions` | tests/fixtures/openfoodfacts-taxonomy-editor/expected | `openfoodfacts_taxonomy_editor_matches_fern_output` | — |
| empty-closed-object-schema | Closed objects with and without a written properties map; invalid free-form examples corrected | Fern behaviour + Fern defect | `fix-models` | docs/openapi-surface/handwritten/closed-empty-inline-objects/fern-expected | `handwritten_fixtures_match_fern_goldens` | `closed-empty-object-example` |
| nonstandard-type-float | Misspelled scalar type mapped to unknown | Fern behaviour | `fix-models` | tests/fixtures/protoform-conformance/expected | `protoform_conformance_matches_fern_output` | — |
| circular-import-order | Deferred imports through chained reference cycles | Fern behaviour | `fix-models` | docs/openapi-surface/handwritten/chained-reference-cycles/fern-expected | `handwritten_fixtures_match_fern_goldens` | — |
| forward-refs-set | Forward-reference sets for models connected by reference cycles | Fern behaviour | `fix-models` | docs/openapi-surface/handwritten/chained-reference-cycles/fern-expected | `handwritten_fixtures_match_fern_goldens` | — |
| inline-query-param-union-placement | Inline query unions placed by composition members and title | Fern behaviour | `fix-parameters` | docs/fern-measurements/parameter-lowering/query-union-placement/fern-expected | `parameter_lowering_measurements_match_fern` | — |
| query-param-enum-or-string-items | Inline query array items formed from enum and string members | Fern behaviour | `fix-parameters` | docs/openapi-surface/handwritten/query-array-items-union/fern-expected | `handwritten_fixtures_match_fern_goldens` | — |
| required-query-param-scalar-or-array-union | Required scalar-or-array query compositions lowered as one-or-many arguments | Fern behaviour | `fix-parameters` | docs/fern-measurements/parameter-lowering/query-scalar-or-array/fern-expected | `parameter_lowering_measurements_match_fern` | — |
| union-param-write-serialization | Scalar and union query value serialization | Fern behaviour | `fix-parameters` | tests/fixtures/ego-microservices/expected | `ego_microservices_matches_fern_output` | — |
| form-urlencoded-body | JSON Body_* request model retention by operation shape; body/query wire-key collision, multipart required-file examples and aliased-body reference arguments corrected | Fern behaviour + Fern defect | `fix-bodies-responses` | tests/fixtures/millenium-falcon-challenge/expected; tests/fixtures/waylay-queries/expected; docs/openapi-surface/handwritten/multipart-alias-object/fern-expected; docs/openapi-surface/handwritten/multipart-json-module/fern-expected; docs/openapi-surface/handwritten/request-alias/fern-expected | `millenium_falcon_challenge_matches_fern_output; waylay_queries_matches_fern_output; handwritten_fixtures_match_fern_goldens; multipart_object_encoding_matches_certified_output_in_both_enum_modes; alias_object_request_matches_certified_output_in_both_enum_modes` | `body-query-parameter-value, multipart-object-required-file-example, request-alias-reference-parameters` |
| content-type-header | JSON content-type selection by request shape and OpenAPI version; binary JSON body examples corrected | Fern behaviour + Fern defect | `fix-bodies-responses` | tests/fixtures/g4brym-download-manager/expected; docs/openapi-surface/handwritten/json-binary-path/fern-expected | `g4brym_download_manager_matches_fern_output; handwritten_fixtures_match_fern_goldens; json_request_shapes_match_certified_output_in_both_enum_modes` | `binary-json-body-example` |
| authorization-header-parameter | Declared authorization header exposed as an operation argument | Fern behaviour | `fix-parameters` | tests/fixtures/lootlog-battlelog/expected | `lootlog_battlelog_matches_fern_output` | — |
| header-string-default-literal | Defaulted string headers sent as constants; documentation arguments corrected | Fern behaviour + Fern defect | `fix-parameters` | docs/fern-measurements/parameter-lowering/header-default-constants/fern-expected | `parameter_lowering_measurements_match_fern` | `constant-header-docs-arguments` |
| status-code-key-with-suffix | Numeric response statuses with nonnumeric suffixes | Fern behaviour | `fix-bodies-responses` | tests/fixtures/chat-rest-api/expected | `chat_rest_api_matches_fern_output` | — |
| empty-body-guard | OpenAPI 3.0 empty success-body handling; contentless 200 beside typed 201 | Fern behaviour | `fix-bodies-responses` | tests/fixtures/maximo-wxo-integration/expected | `maximo_wxo_integration_matches_fern_output` | — |
| non-json-response-text | Text media returned as text; differing typed 404 bodies become Any | Fern behaviour | `fix-bodies-responses` | tests/fixtures/mi-music/expected | `mi_music_matches_fern_output` | — |
| non-json-response-binary | Binary media streamed as bytes | Fern behaviour | `fix-bodies-responses` | tests/fixtures/esp32-streamline-bridge/expected | `esp32_streamline_bridge_matches_fern_output` | — |
| readme-organization-casing | Mixed-case flat package README imports corrected to actual generated class names | Fern defect | `fix-examples-docs` | tests/fixtures/swagger-petstore-distribution/expected-flat | `compare::compare_reports_the_readme_casing_departure_on_the_mixed_case_organization_golden` | `readme-client-class-casing` |
| docstring-example-import-blank-line | Flat package root and tag imports grouped without a blank line | Fern behaviour | `fix-examples-docs` | tests/fixtures/swagger-petstore-distribution/expected-flat | `compare::compare_reports_the_readme_casing_departure_on_the_mixed_case_organization_golden` | — |
| example-enum-array-value | Required query array example inclusion depends on response/body shape | Fern behaviour | `fix-examples-docs` | tests/fixtures/typescript-service-template/expected | `typescript_service_template_matches_fern_output` | — |
| invalid-datetime-example | Invalid and negative-offset date-time example fallback | Fern behaviour | `fix-examples-docs` | docs/openapi-surface/handwritten/unread-date-time-examples/fern-expected | `handwritten_fixtures_match_fern_goldens` | — |
| allof-example-property-order | Own and inherited request-example property order | Fern behaviour | `fix-examples-docs` | docs/openapi-surface/handwritten/allof-parent-body-order/fern-expected | `handwritten_fixtures_match_fern_goldens` | — |
| example-null-values | Null request-example values interpreted by requiredness and output location | Fern behaviour | `fix-examples-docs` | docs/openapi-surface/handwritten/request-example-nulls/fern-expected | `handwritten_fixtures_match_fern_goldens` | — |
| example-datetime-values | Deprecated optional request-example properties omitted; required ones retained | Fern behaviour | `fix-examples-docs` | docs/openapi-surface/handwritten/request-example-deprecated/fern-expected | `handwritten_fixtures_match_fern_goldens` | — |
| x-fern-base-path | Document-level base-path arguments lifted to clients; broken constructor and method examples corrected | Fern behaviour + Fern defect | `fix-parameters` | docs/openapi-surface/handwritten/base-path-client-argument/fern-expected | `handwritten_fixtures_match_fern_goldens` | `lifted-base-path-docs-examples, lifted-base-path-positional-example` |
| plain-string-map-request-body-example | Plain string-map body examples use key/value placeholders | Fern behaviour | `fix-string-map-example` | tests/fixtures/confluent-kafka-connect/expected | `confluent_kafka_connect_matches_fern_output` | — |
| query-union-with-date-member-not-converted | Date/date-time members in query unions converted on the wire | Fern behaviour | `fix-parameters` | docs/fern-measurements/parameter-lowering/query-union-temporal-member/fern-expected | `parameter_lowering_measurements_match_fern` | — |
| required-and-nullable-query-param-made-optional | Required nullable query schema becomes an optional method argument | Fern behaviour | `fix-parameters` | docs/fern-measurements/parameter-lowering/query-nullable-31/fern-expected | `parameter_lowering_measurements_match_fern` | — |
| query-array-nullable-items-optional | Nullable query-array items stripped from signature; incompatible documentation type/example corrected | Fern behaviour + Fern defect | `fix-parameters` | docs/fern-measurements/parameter-lowering/query-nullable-31/fern-expected | `parameter_lowering_measurements_match_fern` | `nullable-items-docs` |
| single-operation-required-header-promoted | Required header on a sole operation promoted to the client | Fern behaviour | `fix-parameters` | docs/fern-measurements/parameter-lowering/single-operation-headers/fern-expected | `parameter_lowering_measurements_match_fern` | — |
| client-header-date-format-typed-str | Promoted date header typed `dt.date` on the client; invalid constructor example corrected | Fern behaviour + Fern defect | `fix-parameters` | docs/openapi-surface/handwritten/observatory-client-date/fern-expected | `handwritten_fixtures_match_fern_goldens` | `date-header-constructor-example` |
| sdk-variables-extension-ignored | SDK-variable path parameters lifted to the client; constructor and method documentation corrected | Fern behaviour + Fern defect | `fix-parameters` | docs/openapi-surface/handwritten/observatory-client-variable/fern-expected | `handwritten_fixtures_match_fern_goldens` | `sdk-variable-docs-examples` |

| allof-enum-ref-narrowed-by-scalar-member | Enum and scalar allOf alias rendering; pattern-invalid generated example corrected | Fern behaviour + Fern defect | `models-refs` | docs/openapi-surface/handwritten/measurement-phase/fern-expected; docs/fern-measurements/models-refs-literals/measurement-phase/fern-expected | `handwritten_fixtures_match_fern_goldens; remaining_model_shapes_match_the_certified_fern_trees` | `pattern-narrowed-enum-example` |

Additional boundaries of these rows are held by the same gate: the
`empty-body-guard` row also uses
`docs/openapi-surface/handwritten/contentless-created-success/fern-expected`;
the text-response row has the differing-404-schema case in
`tests/fixtures/dot-ai/expected`. The content-type row also compares
`opentosca-license-engine`, `redocly.com-museum`, `oip-web-api`,
`flask-example-heroku` and the hand-written `described-scalar-bodies`.

### Handed-off real witnesses

NetGSM is now registered as corpus row 332: its complete certified golden is
`tests/fixtures/netgsm-sms/expected`, compared by
`netgsm_sms_matches_fern_output`. Waylay is already registered as row 329
and compares with only the indexed body/query correction. The remaining eight
witnesses do not byte-match and are **not** real-specification proof. Their
pinned sources, exact remaining file differences and owning follow-on shapes
are recorded in
[the finished-tree measurement](fern-measurements/blocked-witnesses/README.md).
In particular, `vocode-core` remains unregistered: its comparison has 14
differing files, five Fern-only files and four crozier-only files. The follow-on
scenario plan owns its ignored server-name extension
(`server-name-extension-ignored`), omitted allOf-wrapped request-body operation
and inherited property type reuse; the latter two have no confirmed scenario
id. The linked measurement records every file difference.
They were handed off for `inline-query-param-union-placement`,
`required-query-param-scalar-or-array-union`, and
`nested-discriminated-union-in-anyof`; their separate blockers are named in
that measurement rather than hidden behind those closed categories.

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
   `fern-limitations.md` carries a row for it with a non-generation verdict:
   `discards`, `ignores`, `refuses`, `crashes` or `coincidence`. Under
   [the amended settlement rule](#what-a-probe-may-settle-as-amended-again) a
   probe settles only such a verdict. A ledger row reading `implements`, or
   carrying only a qualifier, leaves the feature at condition 3.
   **Evidence cell:** the `fern-limitations.md` key and its verdict, spelled the
   way that file's *How to read a verdict* section spells them (`implements`,
   `discards`, `ignores`, `refuses`, `crashes`, `coincidence`, `unmeasured`) —
   never a synonym.
3. **`handwritten`** — no registered golden source declares it, no
   non-generation verdict settles it, and at least one hand-written fixture's
   **feature-level** cover names it. A hand-written fixture is a **lower level
   of proof than a real specification**: a document written for the purpose,
   with the tree Fern generated from it, that crozier byte-matches. It is
   admitted as generation evidence only after the real-specification search for
   the shape failed — its cover cites that search's `exhausted` or
   `search-incomplete` record — and it never counts as a real-specification
   match, in any count this document or the census states. An **arm-level**
   cover proves one handling site of a `golden` row: the row stays `golden`, the
   arm stays counted as unreached by real specifications, and the fixture
   appears only in [the unreached-arm table](#every-unreached-arm-and-its-search-verdict)'s
   `hand-written fixture` column and in
   [`handwritten-reach.tsv`](openapi-surface/handwritten-reach.tsv). The
   fixture directory, `evidence.toml` and the gate are stated once, in
   [`openapi-surface/handwritten/AGENTS.md`](openapi-surface/handwritten/AGENTS.md).
   **Evidence cell:** `handwritten: <fixture>[, <fixture>…]; search: <verdict>
   ([record](<link>))`, spelled exactly so: the covering fixtures' names, sorted
   and comma-separated; the verdict their covers cite; and a link, relative to
   the region file, to the search record they cite. Its `crozier sites`, `why
   bytes could move` and `settlement` cells are empty.
4. **`gap`** — none of those holds. This is the answer the whole document
   exists to produce.
   **Evidence cell:** the census result showing zero declarations across every
   registered source, together with the statement that no `fern-limitations.md`
   row names it — or, for a row demoted from `limitations`, the ledger key, the
   verdict that demoted it after **`demoted to gap:`**, and what it now needs.

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
  current walk is the **2026-10-07** one, pinned by digest (`f16ddf39…`) in
  [`document-paths.md`'s snapshot reconciliation](openapi-surface/document-paths.md#snapshot-reconciliation),
  which `just check` now runs. Since issue #352 the census's population is the
  registered rows whose committed Fern golden crozier byte-matches: the tree
  acquires 260 sources (corpus rows through 332, after the withdrawals of rows
  224 and 223, with the `crozier-property-name` feature target), and the walk
  reads the **244** registered sources, of which
  **244** carry a committed golden; the 17 others carry none and are acquisition
  evidence only.
  `document-paths`'s evidence cells are all re-transcribed from that walk. In
  the other five region files, this walk re-derived every claim a category
  rests on. Every `golden` row's golden-only witnesses are recomputed from it by
  [`golden-reach.tsv`](openapi-surface/golden-reach.tsv), whose reach cells
  every `golden` row carries. Every `gap` selector still reads zero
  golden-bearing declarers. The twenty-two rows it found declared are promoted,
  with their cells re-transcribed from it. What stays dated there is the
  per-source count lists inside the other cells: each cell names the walk it
  was taken on (a 169-source walk, a 208-source walk, and so on). They are
  freeform prose, several hundred cells, and no category depends on them,
  because a walk over more sources can promote a row and never demote one. A
  count in such a cell is that walk's and says so. **Where a paragraph below
  says a walk read 164 sources, that is the walk it was taken on and not a
  second count of the corpus.**
- **`just fixtures-coverage`**, for criterion 2 alone. That recipe is outside
  `just check` — it needs network and runs the corpus instrumented — so its
  per-file counts are a dated snapshot (2026-09-28), stated once, in the join
  table under
  [The ranked list against `golden blind spots`](#the-ranked-list-against-golden-blind-spots).
  The gate cannot produce that measurement, but it does reconcile against it:
  see [Refreshing the coverage snapshot](#refreshing-the-coverage-snapshot).

What this section takes from the six region files, `RankedBacklogTests` in
`tools/surface-census/tests/surface_census_test.py` takes back from them — the per-region counts and
the totals narrated from them, both backlogs' membership and their stated sizes, each ranked row's
owning region, criterion 1, and — while the ranked list has rows — the rubric
order and the median it produces. `just
check` runs it offline, so a region row added, reclassified or re-measured fails
the gate here rather than leaving this section quietly stale. Criteria 3 and 4
are the two the gate cannot take back, because the region files publish no number
for either; each bullet below says where its number comes from.

### What the walk enumerated

| region | features | `golden` | `limitations` | `handwritten` | `gap` | `FIXTURE` | `PROBE` | `UNREACHABLE` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [`parameters`](openapi-surface/parameters.md) | 87 | 53 | 19 | 15 | 0 | 0 | 0 | 0 |
| [`schemas`](openapi-surface/schemas.md) | 309 | 248 | 14 | 38 | 9 | 7 | 0 | 2 |
| [`bodies-media`](openapi-surface/bodies-media.md) | 57 | 46 | 5 | 6 | 0 | 0 | 0 | 0 |
| [`security`](openapi-surface/security.md) | 50 | 41 | 9 | 0 | 0 | 0 | 0 | 0 |
| [`document-paths`](openapi-surface/document-paths.md) | 72 | 68 | 3 | 0 | 1 | 1 | 0 | 0 |
| [`oas31-extensions`](openapi-surface/oas31-extensions.md) | 53 | 38 | 2 | 1 | 12 | 0 | 0 | 12 |
| **total** | **628** | **494** | **52** | **60** | **22** | **8** | **0** | **14** |

The walk enumerated **628** features and landed each in exactly one category:
**494** `golden`, **52** `limitations`, **60** `handwritten`, **22** `gap`. The `gap` column splits by
settlement class into **8** `FIXTURE`, **0** `PROBE` and **14** `UNREACHABLE`.
The 35 rows the naming and example branches of #361 added are 30 `schemas`
rows, three `bodies-media`, one `parameters` and one `document-paths`; 27 are
`golden` and 8 `FIXTURE` gaps, each named `not searched`
([the case tables](#enum-member-and-example-value-cases)).

The denominator's previous increase came from the instrument's new selectors.
The subsequent PayPal registration adds one source (32 vendored plus 138
`link-ok`) and promotes `anyof-sole-member` to `golden`, leaving the 511-feature
denominator unchanged. Its four declarations retain concrete generated item
models. See [the registration measurement](openapi-surface/schemas.md#paypal-registration-measurement).

The subsequent [wide acquisition reconciliation](openapi-surface/witness-scrape-wide/README.md#finished-tree-reconciliation)
adds no registered source or golden and promotes no feature. Its one registration
slot exhausted an empty ranked queue; all 26 acquisition baseline keys remain
search-incomplete within the fixture backlog. The report separates finite
inventory closure from unanswered searches and excludes Postman from new work
and future obligations while preserving historical source evidence.

The witness searches' registrations add twenty-three sources — corpus rows 144
to 166, `paloalto-cspm-alerts`, `paloalto-cspm-reports`,
`paloalto-cspm-search-manager`, `thrivecart`, `truefoundry-trueforge-5adde28`,
`fergus`, `groupe-psa`, `timelyapp`, `nextgen`, `auto-agent-protocol`, `skool`,
`spendesk`, `billie`, `alma-france`, `outreach`, `tally`, `billie-entry`,
`skool-entry`, `timelyapp-entry`, `cradl`, `zulip`, `zulip-jentic` and
`zulip-jentic-entry` (32 vendored plus 163 `link-ok`) — and promote nine `schemas` features to `golden`:
`annotated-ref-target-composed`, `annotated-ref-target-oneof`,
`annotated-ref-target-closed-object`, `anyof-array-variant-struct-item`,
`anyof-array-variant-closed-object-item`, `oneof-array-variant-closed-object-item`,
`ref-pointer-undeclared-component-head`, `ref-pointer-unnamed-segment` and
`schema-name-nonidentifier-name`. Row 164's repairs add one generator arm, the
string-enum member of `hoist_union_variant` (cases 2a to 2d), and with it four
`schemas` features, `golden` at once, so the denominator moves from 530 to 534. Rows 165 and 166, jentic's
two serializations of another Zulip revision, promote nothing: every row they
declare is already `golden`. Only the `fergus`, `auto-agent-protocol` and three
Zulip goldens reach the `src/ir.rs` sites their rows name; each row's evidence cell says
which of crozier's handling sites its golden reaches and which it does not.

The continuation of that registration adds thirteen sources — corpus rows 167 to
179, `viskit-studio`, `milvus-restful-v2-3`, `milvus-restful-v2-4`, `ramu-shogi`,
`embedpdf-cloudpdf`, `langchain-agent-protocol`, `hse`, `milvus-vector-operations`,
`npq-registration`, `mistle-control-plane`, `osparc-payments`, `huatuo-node` and
`huatuo-server` (32 vendored plus 176 `link-ok`) — and promotes twelve features to
`golden`: ten `schemas` rows the witness searches named, and the two `security`
rows the amended rule had demoted, `oauth2-password` and `securityscheme-ref`.
Rows 168 and 169's repairs add one disjunct to `hoist_union_variant`'s closing
object arm, `is_declared_empty_object`, and with it cases 10a to 10d and four
`schemas` features: three `golden` at once, and `oneof-closed-empty-object-variant`,
the `oneOf` spelling of the closed empty member, a `FIXTURE` gap no registered
source declares. So the denominator moves from 534 to 538. Six of the twelve
promoted rows' goldens reach the site their row names — `hse`, the three Milvus
goldens, `mistle-control-plane`, `osparc-payments` and the two HuaTuo goldens —
and the other six `schemas` rows' witnesses lower through the component builder or,
for `array-item-pointer-walk-anyof`, through the loader's new pointer inlining, so
each evidence cell says which of crozier's handling sites its golden reaches,
measured on a coverage run over that golden alone, and which it does not.

The golden-reach witnesses, corpus rows 191 to 196 (`openlinksw-osdb`,
`ziptax-node`, `nexmo-messages`, `deepsearch-ds-v2`, `mindee-ocr` and
`opencodeui`), were registered beside those batches, so the walk reads 214 sources
(32 vendored plus 182 `link-ok`) and, with `hoist_union_variant`'s
nested-composition arm (cases 13a to 13d) beside the four cases rows 168 and 169
added, 542 features. They settle no `gap` row, but one tree
now holds every batch, and `fergus` declares `schema.anyOf>schema.anyOf` seven
times: `anyof-anyof-variant`, one of the two `gap` rows the nested-composition
re-derivation added, is `golden` here. Corpus rows 216 to 222, the seven
pending witnesses the golden-reach continuation registered (`sim-logs`,
`sim-tables`, `vellum-gateway`, `dot-ai`, `paloalto-code-technologies`,
`marimo-plugins` and `otoroshi`), bring the walk to 221 sources (32 vendored
plus 189 `link-ok`); they declare no `gap` selector and move no category. Corpus
rows 223 to 231, the witnesses the arm searches found (`nexmo-conversation`,
`codat-assess`, `googleapis-monitoring-v1`, `docu-goapiserver`, `onevoice`,
`xfsc-oidc-identity-resolver`, `adyen-acs-notification`, `peopledatalabs` and
`standrig`), bring it to 230 (32 vendored plus 198 `link-ok`); they declare no
`gap` selector and move no category either. Rows 223 and 224 have since been
withdrawn for want of a publisher grant, as the walk count below records. Corpus row 232, MockServer's own
description (`mockserver`), brings it to 231 (32 vendored plus 199 `link-ok`),
and declares no `gap` selector either.

The final reconciliation registers no source and adds no feature. It applies
[the classification precedence](#the-category-rules) to one current walk, the
2026-09-28 one pinned in
[`document-paths.md`](openapi-surface/document-paths.md#snapshot-reconciliation).
That walk promotes twenty-two rows to `golden`: sixteen that read
`limitations` and six `UNREACHABLE` `gap` rows. Every one of them is declared by
golden-bearing registered sources that earlier cells did not count. The census
selector reads twelve of them (`link-description`, `nonascii-info-title`,
`multiple-of`, `contains`, `format-idn-hostname`, `format-iri`, `xml-wrapped`,
and the Server, Components, Request Body, Media Type and Example extension
rows). The census's own object-model walk reads the other ten, at positions
no selector names: response-range keys (`range-3XX`, `range-4XX`, `range-5XX`),
`application/xml` content keys (`xml-request`, `xml-response`), multi-word
Server descriptions (`server-description-multiword`), `const` value kinds
(`const-boolean`, `const-integer`), a `true` schema under `properties`
(`boolean-schema-true`), and `in: query` on a real `apiKey` scheme
(`apiKey-query`). Each row's evidence cell names its declarers, and each keeps
the committed Fern measurement it was settled on as a cross-reference.
`xml-attribute` stayed `golden` on a `DROPPED` row until corpus row 302.

The remaining-gap searches register corpus rows 301 to 306
(`ideaconsult-enanomapper`, `openaire-graph`, `qredence-fleet-rlm`,
`fiware-context-generator`, `hasura-metadata` and `zoonk`), bringing the walk to
237 sources (32 vendored plus 205 `link-ok`); withdrawing row 224
(`codat-assess`) for its disputed grant leaves 236 (32 vendored plus 204
`link-ok`), withdrawing row 223 (`nexmo-conversation`) for want of a
publisher grant leaves 235 (32 vendored plus 203 `link-ok`), and row 307
(`apideck.com-ecosystem-client-class-name`, row 13's document under
`client_class_name: EcosystemClient`) makes 236 (32 vendored plus 204
`link-ok`); the `crozier-property-name` feature target makes 237 (33 vendored
plus 204 `link-ok`), row 308 (`yourbrand-ticketing`) makes 238 (33 vendored
plus 205 `link-ok`), and row 309 (`huatuo-node-tree`) makes 239 (33 vendored
plus 206 `link-ok`). Rows 301 and 302 are the first
golden-only witnesses of `operation-external-docs` and `xml-attribute`, which
[Golden rows with no golden-only witness](#golden-rows-with-no-golden-only-witness)
listed until then. Rows 303 to 305 declare `schema.oneOf>schema.anyOf` and move
`oneof-anyof-variant` from `gap` to `golden`, and row 306, Zoonk's own API,
declares the closed empty `oneOf` member and moves
`oneof-closed-empty-object-variant` too, so the category counts read 465
`golden` and 25 `gap` on the same 542 features.

**What the `golden` count means, and what it does not.** 465 of those 542
features carry byte-match evidence: a registered source declares the feature and
its committed Fern golden byte-matches, so crozier and Fern are compared over
real bytes there and `just check` fails if they diverge. The other 77 do not. 52
carry a committed Fern measurement of non-generation that crozier is byte-compared
against on a locally authored probe, 11 rest on a hand-written fixture, and 14
are `gap`. Neither
column is a defect count, and neither 465 nor 542 is a claim of exhaustion —
[the section below](#golden-classified-is-not-golden-exhausted) states where the
remaining distance lies, including the part of it this walk cannot enumerate.

**What the `gap` count means.** 22 is the number of OpenAPI shapes no committed
golden's source declares and no hand-written fixture covers, so no byte
comparison touches them. `just check` is green over all 22 either way, and it
is not a defect count. 14 of them (`UNREACHABLE`) have no position in a
generated Python SDK at all, each proved so by a committed differential pair
that crozier is byte-compared against, and saying so is their settlement. The
other 8 are the `FIXTURE` gaps the naming and example case tables brought
inside the census: no registered golden source declares any of them, no witness
search has been run for any of them, and each stands only as a row of
[Unproven features, named](#unproven-features-named), ranked in
[the ranked backlog](#the-ranked-fixture-backlog). The eleven branches of
`src/ir.rs` the earlier instrument passes named that no registered source
declares are `handwritten`, each byte-matched on a
[hand-written fixture](openapi-surface/handwritten/AGENTS.md) its failed search
admitted; the paragraphs of [the ranked backlog](#the-ranked-fixture-backlog)
tell how every earlier row left this count.

### Reconciliation

**Each feature is classified exactly once.** The 628 rows carry 628 distinct
keys, and no `spec location` string appears in two region files — the assertion
[`document-paths.md`](openapi-surface/document-paths.md#snapshot-reconciliation)
already runs over all six files, re-run here and passing. Eighteen spec
locations carry more than one row, every one of them inside a single region and
every one of them the grammar's field-versus-value split: `Schema Object.format`
heads 28 rows (the field, plus one per registered format value), `Media Type
Object content-map key` 11, `Schema Object.additionalProperties` 4. A field row
and a valued row are two features, not one feature counted twice — the census
emits `schema.format` and `schema.format=uuid` as two selectors.

**Nothing is left unclassified.** Every row's `category` cell holds one of
`golden`, `limitations`, `handwritten`, `gap`, and every `gap` row's `settlement` cell holds one
of `FIXTURE`, `PROBE`, `UNREACHABLE`.

**Every ledger key is accounted for.** The canonical join reports 104 keys, of
which 101 are a region row's key verbatim. The other three:

| ledger key | how it is accounted for |
|---|---|
| `status_code` | **Not a feature key.** It is a row label inside the ledger's 407/421 probe table, which the join's `\| key \| N \|` shape matches by accident — the `bodies-media` region's method notes say the same. The join's real yield is 103. |
| `encoding-explode-or-allowReserved` | One ledger row covering two fields; `bodies-media` splits it into `encoding-explode` and `encoding-allow-reserved`, both `limitations`, both citing that verdict. |
| `servers-multiple-path-or-operation` | One ledger row covering two levels; `document-paths` splits it into `pathitem-servers` and `operation-servers`, both `golden`. |

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
that document's own shapes produce are pinned, and nothing else is. [Golden
reach, row by row](#golden-reach-row-by-row) measures that for every `golden`
row, and the four rows this paragraph used to argue from in prose now read off
it: `x-fern-or-crozier-ignore`'s one witness reaches `filter_ignored`'s
Operation-Object arm and not its component-schema arm;
`schema.anyOf>schema.allOf`'s — `anyof-allof-variant`'s — one witness never
reaches the inline-object arm of `hoist_union_variant` at all, its four
declarations going through the component path instead;
`audience-dual-header-policy`'s witnesses reach every handling site, and until
corpus row 192 all of them were hand-authored feature targets; and
`media-type-range` reaches all three of its range-handling sites across five
witnesses, the request side and the range-beside-concrete-types side included,
so the *"two of seven reads"* this paragraph once quoted describes a corpus that
predates corpus rows 134 and 136. Every conjunction row says the same thing in its
own evidence cell, because a conjunction row is about a *branch*: a golden pinning
one pins the bytes for the shapes its document sends down the arm, not the arm's
behaviour.

**A `limitations` row has no registered corpus byte comparison.** 52 features
are there. Each has a committed Contract A proof that compares crozier's bytes
against Fern's on a locally authored probe, and none still reads `proof
outstanding`. Neither form compares against a registered real-world document.
The final reconciliation shows how provisional that is. Sixteen rows this
paragraph once counted are `golden` now, because the 2026-09-28 walk found
registered goldens declaring them. The cost is not rhetorical either, and
[the join below](#the-ranked-list-against-golden-blind-spots) shows it as a
number. Settling rows by probe put generator code into `src/` that no committed
golden reaches: the object-typed path parameter block in `src/emit.rs` (125
regions of its union on the 2026-09-28 run) is driven by a shape no registered
source declares. Each such row stays convertible, and the day a registrable
witness turns up the classification precedence promotes it to `golden`. That
is what makes the gap a *supply* problem rather than a closed question.

**The enumeration cannot see everything, and it says where it stops.** A feature
is enumerable only where a selector can name it, so
[the walk's 607](#what-the-walk-enumerated) is a
denominator bounded by the grammar rather than by the specification. The sharpest
statement of that bound is
[the case analysis](#the-six-blind-regions-of-srcirrs-case-by-case): of the 107
branches those six functions of `src/ir.rs` offer a document, all 107 carry an exact
selector and **none** is an enumeration hole. Case 11's bare-object example arm
is closed by its object-kind and schema-shaped conjunction, and the new
example-kind family extends that same reading. **That bound has moved seven
times, and moving it is what a reader should expect of it.** It read *"of the 53
branches, 9 carry an exact selector and 44 are enumeration holes"* until the
node-local predicate family was declared, *"of the 76 branches, 40 carry an
exact selector and 36 are enumeration holes"* until the annotated-`$ref` pass read
the four arms inside `prop_type_ref`'s resolution gate at the grain their
selectors need, *"of the 83 branches, 60 carry an exact selector and 23 are
enumeration holes"* until the discriminated-union pass closed
**H-discriminant-value**, and *"of the 89 branches, 74 carry an exact selector and
15 are enumeration holes"* until the negation operator closed **H-residual** and
**H-negated-value** together, and *"of the 95 branches, all 95 carry an exact
selector"* until `hoist_union_variant` gained its string-enum member arm, cases 2a
to 2d, its nested-composition arm, cases 13a to 13d, and its empty-object
disjunct, cases 10a to 10d. The branch count moves when a case is read at a finer
grain — a disjunction split disjunct by disjunct is more rows describing the same
code — and the hole count moves when the grammar grows. The enum-member
spellings in `src/naming.rs` and the selected JSON value kinds in `src/emit.rs`
are now in the denominator. Their remaining token, content and generated-type
holes are named in [their case table](#enum-member-and-example-value-cases).
The cross-document `$ref` path of `src/refs.rs` now has pinned FOLIO and
Raybot trees and the `pathItem.$ref:relative-file` selector; its prior pipeline
exclusion is closed. The new schema-name gap is in the ranked
backlog; the other newly named features were already declared by golden sources.

**And the thin end is one document wide.** A `golden` row rests on whichever
registered sources happen to declare the shape, and for many that is a single
one: `schema.anyOf>schema.allOf` is `golden` on `braintrust-dev`'s 4 declaration
sites and nothing else. Withdraw that corpus row and the feature is a `gap`
without a line of `src/` changing. That is a fact about this corpus at this
commit rather than a property of the feature, and it is the reason "the backlog
is empty" is a statement about today's registered sources and not a property the
generator has earned. [Rows resting on one document](#rows-resting-on-one-document)
is every such row, recomputed by the gate rather than remembered here.

### Golden reach, row by row

A `golden` row's evidence says which registered sources *declare* its feature.
Its `crozier sites` column says what their goldens *reach*: the **reach cell**,
generated by `just golden-reach` and held to the committed ledger
[`openapi-surface/golden-reach.tsv`](openapi-surface/golden-reach.tsv) by
`RankedBacklogTests`. Three inputs make it:

- the row's **witnesses** — the registered sources `just surface-census` reports
  declaring the row's selectors that carry a committed golden, so they are in the
  golden-only tier. A shape no selector expresses (a content-map or status-code
  *key*) names its witnesses from its own evidence cell instead, and the gate
  holds the two together;
- the row's **handling sites** — the crozier functions, or brace-delimited arms
  inside them, that run *because* a document declares the feature, declared per
  row in [`openapi-surface/golden-reach-sites.tsv`](openapi-surface/golden-reach-sites.tsv).
  A rejection or absence arm — the branch a document *without* the feature takes,
  or the error a malformed one raises — is not a handling site, since no document
  declaring the feature can take it;
- the **golden-only tier** of `just fixtures-coverage`, measured one golden test
  at a time. Counter hits add, so a row's scoped run — the tier restricted to its
  witnesses — is the union of those per-test runs; the decomposition was checked
  against `cargo llvm-cov report` over the same test and differs in no region.

A site is **reached** when that scoped run executed one of its counter regions.
Which sites a row has is a declaration read off `src/`; whether its witnesses
reach them is the measurement, and nothing in a cell asserts it. The cells in the
region files are the run named in the ledger's first line.

#### The reach ranking

Golden rows ranked by unreached handling sites, then unreached handling regions,
then key. **425** golden rows reach every handling site and tie below every row
listed here; each says so in its own cell. Unreached regions break ties and
create no obligation of their own.

**The boundary.** The first pass of this measurement owned the rows ranked above
`anyof-allof-variant` when it fixed the boundary, together with the four rows
the section above names — the table below, with the rank each held then. That
ranking is this same measurement over the corpus before corpus rows 191 and 192
were registered, with the site table already cleared of rejection, absence and
unreachable arms and of arms that belong to a `gap` row. One row joined the
owned set after the boundary was fixed: `anyof-oneof-variant` is one of the four
rows [the case analysis](#hoist_union_variant) gained when corpus row 193's
repair gave `hoist_union_variant` its nested-composition arm, and it ranks above
`anyof-allof-variant` on the current ledger, so the table gives its current rank
marked `(new)`. The rows the witness searches' registrations (corpus rows 144 to
166) made `golden`, and `anyof-anyof-variant`, which `fergus` made `golden` once
both batches stood in one tree, joined the ledger after the boundary was fixed,
and so did the fifteen rows the continuation's registrations (corpus rows 167 to
179) made `golden`, first measured once that continuation was merged with the
golden-reach witnesses. The same merge moved the `$ref`-pointer rows: the loader
now copies a pointer into a component schema where it is used, so no golden
reaches `resolve_schema_pointer`'s segment arms or `ref_to_class`'s pointer arms
any longer, and
`ref-pointer-composition-index`, `ref-pointer-nested-properties`,
`ref-pointer-nested-items` and the four `array-item-pointer-walk-*` rows carry
unreached sites they did not before.
The boundary stays where the ranking measured at `721c6090`, before that merge,
put it: the rows the merged ranking newly places above `anyof-allof-variant` are
open like every other row outside the owned set. Each
owned row is left either with a registered real-world witness reaching the arm no
earlier witness reached, or with a search record over the six declared sources
for one. Every other row listed here with an unreached site is **open**, and the
continuation node `thin-goldens-continue` recorded an arm search for each over the
six declared sources, linked from its disposition and from its reach cell. That
search registered corpus rows 223 to 231, which took `anyof-anyof-variant`,
`anyof-string-const-variant`, `mutualTLS` and `securityscheme-type-openidconnect`
off this list and bought `ref-pointer-composition-index` its pointer-walk site
(rows 223 and 224 were later withdrawn for want of a publisher grant, and that
site now rests on a hand-written fixture); the
repairs rows 225, 229 and 230 needed narrowed the `enum-leading-zero-member` and
`enum-leading-digit-identifier` fallbacks to names Fern refuses, so their sites stay
unreached by any Fern-accepted document.

| rank | key | region | unreached sites | unreached regions | golden-only witnesses | boundary |
|---|---|---|---|---|---|---|
| 1 | `request-body-content` | `bodies-media` | **7** | **59** | **207** | open — real-specification witness search remains open |
| 2 | `parameter-schema` | `parameters` | **4** | **84** | **199** | open — real-specification witness search remains open |
| 3 | `ref-pointer-composition-index` | `schemas` | **4** | **52** | **2** | owned — first-pass search record below |
| 4 | `parameter-in-header` | `parameters` | **3** | **19** | **63** | open — real-specification witness search remains open |
| 5 | `format-binary` | `schemas` | **3** | **5** | **40** | open — real-specification witness search remains open |
| 6 | `anyof-discriminated-union` | `schemas` | **2** | **45** | **14** | owned — first-pass search record below |
| 7 | `parameter-in-path` | `parameters` | **2** | **28** | **168** | open — real-specification witness search remains open |
| 8 | `ref-pointer-nested-properties` | `schemas` | **2** | **10** | **3** | open — real-specification witness search remains open |
| 9 | `media-type-multipart` | `bodies-media` | **2** | **6** | **28** | open — real-specification witness search remains open |
| 10 | `ref-pointer-nested-items` | `schemas` | **2** | **6** | **2** | open — real-specification witness search remains open |
| 11 | `format-byte` | `schemas` | **2** | **4** | **13** | open — real-specification witness search remains open |
| 12 | `oneof-anyof-variant` | `schemas` | **1** | **69** | **3** | open — real-specification witness search remains open |
| 13 | `anyof-oneof-variant` | `schemas` | **1** | **64** | **6** | owned — first-pass search record below |
| 14 | `oneof-array-variant-anyof-item` | `schemas` | **1** | **41** | **1** | open — real-specification witness search remains open |
| 15 | `oneof-discriminated-union` | `schemas` | **1** | **36** | **39** | owned — first-pass search record below |
| 16 | `oneof` | `schemas` | **1** | **32** | **81** | open — real-specification witness search remains open |
| 17 | `parameter-style-form-query-object` | `parameters` | **1** | **30** | **20** | open — real-specification witness search remains open |
| 18 | `array-item-oneof-discriminated-union` | `schemas` | **1** | **25** | **11** | open — real-specification witness search remains open |
| 19 | `items-oneof-element` | `schemas` | **1** | **23** | **23** | owned — first-pass search record below |
| 20 | `array-item-anyof-discriminated-union` | `schemas` | **1** | **22** | **9** | open — real-specification witness search remains open |
| 21 | `oneof-string-const-variant` | `schemas` | **1** | **20** | **4** | open — real-specification witness search remains open |
| 22 | `annotated-ref-shape` | `schemas` | **1** | **19** | **13** | owned — first-pass search record below |
| 23 | `discriminator-mapping` | `schemas` | **1** | **18** | **29** | open — real-specification witness search remains open |
| 24 | `anyof-array-variant-annotated-ref-item` | `schemas` | **1** | **17** | **1** | owned — first-pass search record below |
| 25 | `anyof-array-variant-composed-item` | `schemas` | **1** | **17** | **1** | owned — first-pass search record below |
| 26 | `oneof-array-variant-closed-object-item` | `schemas` | **1** | **17** | **4** | open — real-specification witness search remains open |
| 27 | `anyof-array-variant-closed-object-item` | `schemas` | **1** | **13** | **5** | open — real-specification witness search remains open |
| 28 | `anyof-allof-variant` | `schemas` | **1** | **12** | **2** | owned — first-pass search record below |
| 29 | `array-item-empty-object` | `schemas` | **1** | **12** | **4** | open — real-specification witness search remains open |
| 30 | `oneof-closed-empty-object-variant` | `schemas` | **1** | **12** | **1** | open — real-specification witness search remains open |
| 31 | `array-item-pointer-walk-allof` | `schemas` | **1** | **11** | **1** | open — real-specification witness search remains open |
| 32 | `array-item-pointer-walk-anyof` | `schemas` | **1** | **11** | **1** | open — real-specification witness search remains open |
| 33 | `parameter-in-query` | `parameters` | **1** | **9** | **163** | open — real-specification witness search remains open |
| 34 | `annotated-ref-target-anyof` | `schemas` | **1** | **8** | **1** | open — real-specification witness search remains open |
| 35 | `anyof-array-variant-anyof-nullable-item` | `schemas` | **1** | **8** | **2** | open — real-specification witness search remains open |
| 36 | `anyof-array-variant-oneof-nullable-item` | `schemas` | **1** | **8** | **1** | open — real-specification witness search remains open |
| 37 | `inheritance-discriminated-union` | `schemas` | **1** | **8** | **3** | open — real-specification witness search remains open |
| 38 | `property-sole-anyof-closed-object-member` | `schemas` | **1** | **8** | **1** | open — real-specification witness search remains open |
| 39 | `property-sole-anyof-struct-member` | `schemas` | **1** | **8** | **1** | open — real-specification witness search remains open |
| 40 | `array-item-pointer-walk-properties` | `schemas` | **1** | **6** | **2** | open — real-specification witness search remains open |
| 41 | `http-dpop` | `security` | **1** | **5** | **3** | open — real-specification witness search remains open |
| 42 | `http-mutual` | `security` | **1** | **5** | **1** | open — real-specification witness search remains open |
| 43 | `http-negotiate` | `security` | **1** | **5** | **2** | open — real-specification witness search remains open |
| 44 | `schema-example-empty-object` | `schemas` | **1** | **5** | **3** | open — real-specification witness search remains open |
| 45 | `media-type-malformed-key` | `bodies-media` | **1** | **4** | **5** | open — real-specification witness search remains open |
| 46 | `array-item-pointer-walk-items` | `schemas` | **1** | **3** | **2** | open — real-specification witness search remains open |
| 47 | `enum-leading-zero-member` | `schemas` | **1** | **3** | **5** | open — real-specification witness search remains open |
| 48 | `format-uuid` | `schemas` | **1** | **3** | **42** | open — real-specification witness search remains open |
| 49 | `format-date` | `schemas` | **1** | **2** | **35** | open — real-specification witness search remains open |
| 50 | `mutually-recursive-graph` | `schemas` | **1** | **2** | **217** | open — real-specification witness search remains open |
| 51 | `recursive-graph` | `schemas` | **1** | **2** | **217** | open — real-specification witness search remains open |
| 52 | `schema-example-object-on-map` | `schemas` | **1** | **2** | **11** | open — real-specification witness search remains open |
| 53 | `schema-example-outside-enum` | `schemas` | **1** | **2** | **3** | open — real-specification witness search remains open |
| 54 | `x-fern-or-crozier-ignore` | `oas31-extensions` | **1** | **2** | **2** | owned — first-pass search record below |
| 55 | `enum-empty-identifier-member` | `schemas` | **1** | **1** | **3** | open — real-specification witness search remains open |
| 56 | `enum-leading-digit-identifier` | `schemas` | **1** | **1** | **1** | open — real-specification witness search remains open |
| 57 | `format-email` | `schemas` | **1** | **1** | **37** | open — real-specification witness search remains open |
| 58 | `format-hostname` | `schemas` | **1** | **1** | **2** | open — real-specification witness search remains open |
| 59 | `format-idn-hostname` | `schemas` | **1** | **1** | **1** | open — real-specification witness search remains open |
| 60 | `format-ipv4` | `schemas` | **1** | **1** | **4** | open — real-specification witness search remains open |
| 61 | `format-iri` | `schemas` | **1** | **1** | **1** | open — real-specification witness search remains open |
| 62 | `format-json-pointer` | `schemas` | **1** | **1** | **1** | open — real-specification witness search remains open |
| 63 | `format-password` | `schemas` | **1** | **1** | **8** | open — real-specification witness search remains open |
| 64 | `format-regex` | `schemas` | **1** | **1** | **1** | open — real-specification witness search remains open |
| 65 | `format-time` | `schemas` | **1** | **1** | **1** | open — real-specification witness search remains open |
| 66 | `format-uri` | `schemas` | **1** | **1** | **58** | open — real-specification witness search remains open |
| 67 | `format-uri-reference` | `schemas` | **1** | **1** | **3** | open — real-specification witness search remains open |
| 68 | `format-uri-template` | `schemas` | **1** | **1** | **1** | owned — first-pass search record below |
| 69 | `ref-pointer-undeclared-component-head` | `schemas` | **1** | **1** | **13** | open — real-specification witness search remains open |


#### The rows this measurement's first pass owned

An owned row with a site still unreached carries an **arm search**: the six
declared sources searched for a real-world document that declares the row *and*
executes the site, recorded at `golden-reach-witnesses/searches/<key>.md` and
linked from the row's reach cell. `tools/surface-census/golden-reach-search.py` walks the four
enumerable sources' pinned documents and issues two phrasings to each text-query
source through the guarded acquirer; every declarer the census finds is then run
through the instrumented `crozier` the reach cells were measured with, and only
a declarer that executes an unreached site is a candidate owing the licence,
ref and Fern screens. A probe counts only when `src/` is the very commit that
build was measured at, since the site's span is read from the one and its
regions from the other: probes run while `src/` had moved on read another arm's
regions, registered `mindee-ocr` for an arm it does not reach and handed off a
document that reached none, and every probe row without a build stamp is
therefore counted nowhere. Its evidence sits under
`golden-reach-witnesses/<source>/` in Contract B's `records.tsv` form, and
`RankedBacklogTests` reconciles every linked record with it through Contract B's
own gate. A candidate passing every screen is registered, or — where it declares
a `gap` selector, or cannot yet be generated — handed off in
[`handoff.tsv`](openapi-surface/golden-reach-witnesses/handoff.tsv). A document
written to exercise a tool is declined as `not a real-world specification: a
test fixture written to exercise a tool`, naming its repository, its path at the
pinned commit and what makes it a fixture: it is hand-written, and only a real
specification is evidence that Fern generates from a shape (the manager's
ruling to `thin-goldens-continue-2`). Each record states its arm's verdict
itself: `exhausted` when nothing is outstanding, every declarer reaching the arm
on the counted build is screened, and none passing every screen is left
unregistered, otherwise `search-incomplete`. An arm only a generation setting
reaches reads `config-gated` instead, with no search
([configuration-gated arms](#every-unreached-arm-and-its-search-verdict)). A declarer screened while an
earlier build's probe reached the arm, and whose probe of the counted build no
longer does, is no candidate and holds nothing open.
No record owes anything now, and `outstanding.tsv` lists no item. The six
records whose arms a registered witness has since reached —
`property-anyof-discriminated-union`, `anyof-sole-member`, `anyof-anyof-variant`,
`anyof-string-const-variant`, `mutualTLS` and `securityscheme-type-openidconnect`
— read `witness-found`, and `thin-goldens-continue-2` probed every declarer they
had left unprobed on build `4828cc2b`, against the arm each searched for as it
resolves in today's `src/`; `mutualTLS`'s and `securityscheme-type-openidconnect`'s
arm was restructured out of `src/` by the openIdConnect repair, so theirs are
probed against the row's handling sites as the ledger names them. A document the census
could not read that a full standard parser refuses too — Python's `json` on
syntax, ruamel.yaml 0.19.1 (YAML 1.2) on syntax, or either reading it as no
OpenAPI or Swagger description — is `census-refused`, listed in its source's
`census-refused.tsv` with the parser's verdict and the document's digest, and is
not outstanding: 161 in `vendor-portals`, 46 in `github-publisher-trees`, 55 in
`github-code-search` and 20 in `sourcegraph`. The rest the full parser reads, and
`recensus` counts them through it, as the census's own object-model walk over
ruamel.yaml's reading, named in each source's `census-fallback.tsv`: 12 in
`vendor-portals`, 11 in `github-publisher-trees`, 72 in `github-code-search` and
45 in `sourcegraph` (`just test-census-fallback` holds that reading to the stdlib
loader's counts on every registered YAML source). `thin-goldens-continue` walked
the four walked sources again with the repaired loader and the current enum
naming, counted every query-source copy again, probed every declarer of the 51
rows with an unreached site on the instrumented build `4828cc2b` with `src/` at
that commit and an 1800 s limit — none timed out and none aborted, once the
crash repairs the first pass exposed had landed — and screened every declarer
that reached an arm: Fern 5.20.0 refuses every new one but the copies of
AssemblyAI's description, which pass it and fail the licence screen on the
publisher's revenue-ceiling terms. The earlier Fern screens quoted Fern's
diagnostic but not its exit status, so `thin-goldens-continue-2` took every
refusal of a reaching declarer again with `fern-rescreen` (Fern CLI 5.67.1
`fern check`, and python-sdk 5.20.0 `fern generate` where the check passed): 467
distinct documents, each result in its source's `fern-rescreen.jsonl`, and
every screen now quotes the exit status and the first diagnostic Fern printed.
None passes. The 51 retained records state each search's current verdict and
outstanding work; an arm without a real witness stays open. In six of them — `anyof-discriminated-union`,
`format-hostname`, `oneof-string-const-variant`, `ref-pointer-nested-items`,
`ref-pointer-nested-properties` and `x-fern-or-crozier-ignore` — the only
declarers reaching the arm that pass every screen are nine synthetic inputs, each
retained with its decline. Six walked
declarers share a path (`openapi.yaml` or `openapi.json`) with another publisher
tree's document; each copy is its own declarer, named `<walk>:<path>`.

| boundary rank | key | outcome |
|---:|---|---|
| 1 | `property-anyof-discriminated-union` | witness registered for both arms — corpus row 194 (`deepsearch-ds-v2`) executes `hoist_discriminated_union`, and corpus row 196 (`opencodeui`) reaches the `prop_type_ref` arm, so every handling site is reached; the arm search the reach cell links reads `witness-found`, every declarer probed on build `4828cc2b` for the arm it searched |
| 2 | `ref-pointer-composition-index` | searched on build `4828cc2b`, nothing outstanding — every declarer in the six sources probed and every one reaching an arm screened; the record reads `exhausted`; the one arm a witness once reached, `ref_to_class`'s pointer walk, lost that witness when corpus row 224 (`codat-assess`) was withdrawn for a disputed grant, and [a replacement search](openapi-surface/withdrawn-witnesses/codat-assess.md#replacement-search) reads `exhausted`, so the hand-written fixture `composition-index-pointer` covers it; the three `resolve_schema_pointer` composition arms stay unreached, since the loader copies every resolvable pointer where it is used, and the declarers the probes found reaching them — Cvent and Sellsy (handed off, then rejected: Fern's exit 0 was over an unparsed document) and Codat Commerce (the same) — are not Fern-accepted; corpus row 223 (`nexmo-conversation`) reached the pointer walk on the probe build and no longer did once its `properties` pointers were copied, and is since withdrawn for want of a publisher grant; [arm search](openapi-surface/golden-reach-witnesses/searches/ref-pointer-composition-index.md) |
| 3 | `media-type-key-parameters` | no arm to buy — its witness list named one fixture; the predicate finds `vtex-pricing` and `sftpgo` declaring the shape too, and their goldens reach both sites |
| 4 | `anyof-discriminated-union` | searched on build `4828cc2b`, nothing outstanding — every declarer in the six sources probed and every one reaching an arm screened; the record reads `exhausted`; no witness yet — every declarer reaching the arm is Fern-refused (Kibana, gcore, ogx) or a test fixture declined as no real-world specification (Monite's Spectral test input); [arm search](openapi-surface/golden-reach-witnesses/searches/anyof-discriminated-union.md) |
| 5 | `x-fern-or-crozier-ignore` | historical arm search on build `4828cc2b`; its [search record](openapi-surface/golden-reach-witnesses/searches/x-fern-or-crozier-ignore.md) states the current verdict and outstanding screens. No witness was admitted — Cloudflare's `api-schemas` reaches both schema arms but declares `gap` selectors and Fern refuses it; excluded synthetic inputs reach them and are declined as no real-world specification; copies of AssemblyAI's description (jentic's, and `atacan/AssemblyAI`'s) reach them and pass Fern, and fail the licence screen on AssemblyAI's own revenue-ceiling terms (CORPUS.md's REJECTED `assemblyai-autosdk`); [arm search](openapi-surface/golden-reach-witnesses/searches/x-fern-or-crozier-ignore.md) |
| 6 | `format-uri-template` | searched on build `4828cc2b`, nothing outstanding — every declarer in the six sources probed and every one reaching an arm screened; the record reads `exhausted`; witness registered for one arm — corpus row 191 (`openlinksw-osdb`) reaches `base_type_ref`'s string fallback; no probed declarer reaches the `scalar_body` fallback; [arm search](openapi-surface/golden-reach-witnesses/searches/format-uri-template.md) |
| 7 | `anyof-sole-member` | witness registered — corpus row 196 (`opencodeui`) reaches the arm, so every handling site is reached. It was handed off while it declared the then-`gap` row `anyof-anyof-variant`, and was registered once the merge of crozier main made that row `golden`. The arm search the reach cell links reads `witness-found`, every declarer probed on build `4828cc2b` for the arm it searched |
| 8 | `annotated-ref-shape` | searched on build `4828cc2b`, nothing outstanding — every declarer in the six sources probed and every one reaching an arm screened; the record reads `exhausted`; no witness yet — no probed declarer reaches the arm; [arm search](openapi-surface/golden-reach-witnesses/searches/annotated-ref-shape.md) |
| 9 | `items-oneof-element` | searched on build `4828cc2b`, nothing outstanding — every declarer in the six sources probed and every one reaching an arm screened; the record reads `exhausted`; no witness yet — none of the 1,051 declarers probed on the stamped build reaches the arm; `mindee-ocr` (row 195), registered for it on a misaligned probe, reaches no site of it; [arm search](openapi-surface/golden-reach-witnesses/searches/items-oneof-element.md) |
| 10 | `anyof-array-variant-annotated-ref-item` | searched on build `4828cc2b`, nothing outstanding — every declarer in the six sources probed and every one reaching an arm screened; the record reads `exhausted`; no witness yet — no probed declarer reaches the arm; [arm search](openapi-surface/golden-reach-witnesses/searches/anyof-array-variant-annotated-ref-item.md) |
| 11 | `anyof-array-variant-composed-item` | searched on build `4828cc2b`, nothing outstanding — every declarer in the six sources probed and every one reaching an arm screened; the record reads `exhausted`; no witness yet — no probed declarer reaches the arm; [arm search](openapi-surface/golden-reach-witnesses/searches/anyof-array-variant-composed-item.md) |
| 12 | `oneof-discriminated-union` | searched on build `4828cc2b`, nothing outstanding — every declarer in the six sources probed and every one reaching an arm screened; the record reads `exhausted`; no witness yet — none of the 1,216 declarers probed reaches the arm; [arm search](openapi-surface/golden-reach-witnesses/searches/oneof-discriminated-union.md) |
| 13 | `all-of-nested-composition` | witness registered — corpus row 193 (`nexmo-messages`), whose `sendMessage` body's single-`allOf` SMS channel reaches `hoist_union_variant`'s inline-object arm through the nested-composition arm's sole-member recursion |
| 14 | `anyof-allof-variant` | searched on build `4828cc2b`, nothing outstanding — every declarer in the six sources probed and every one reaching an arm screened; the record reads `exhausted`; no witness yet — DigitalOcean reaches the arm, and its hand-off was rejected: Fern's 35 files are its generation over an unparsed document; [arm search](openapi-surface/golden-reach-witnesses/searches/anyof-allof-variant.md) |
| 214 | `audience-dual-header-policy` | witness registered — corpus row 192 (`ziptax-node`), the row's first real-world witness, generated for audience `v60` so the filter removes 7 of 34 operations |
| 311 | `media-type-range` | no arm to buy — every range-handling site is reached by the five witnesses rows 124, 127, 130, 134 and 136 registered |
| 7 (new) | `anyof-oneof-variant` | searched on build `4828cc2b`, nothing outstanding — every declarer in the six sources probed and every one reaching an arm screened; the record reads `exhausted`; no witness yet — Mistral and Cloudflare reach the nested-composition arm and Fern refuses both; [arm search](openapi-surface/golden-reach-witnesses/searches/anyof-oneof-variant.md) |

#### Every unreached arm, and its search verdict

The golden rows split in two. **425** reach every handling site their
[site table](openapi-surface/golden-reach-sites.tsv) declares, and **69** carry at least one handling site no golden-only witness executes: 91 unreached arms in all. Every one is named below with the verdict its linked arm-search record
states under Contract B's six declared sources, or `not searched` where no arm
search has run. 57 read `exhausted`: each of those arms' six-source searches
owes nothing and found no registrable real-world document that executes it.
Ten read `search-incomplete`: the ignored-schema arm and the nine
parameter-lowering covers. Their
records keep the source-search obligations separate from certified generation. `discriminator-mapping`'s
`collect_schema_refs` arm reads `config-gated`. Twenty-three have no arm search:
three example arms remain named gaps (`schema-example-empty-object`,
`schema-example-object-on-map` and `schema-example-outside-enum`); four root-body
format or typed-query arms and `parameter-in-query`'s declared-default arm are
instead covered by independent fixtures whose bounded searches remain
`search-incomplete`; fifteen request-body, response-media
and multipart arms the body and response repair added are covered by its
hand-written fixtures, whose shape searches are their `witness-search-*` records. Their fixture names appear in the
hand-written column below. The remaining-gap searches ran four of
them. Two are the `scalar_body` fallback of `format-idn-hostname` and
`format-iri`, the rows that joined `golden` in the final reconciliation on
`short-io`, which does not reach that arm. The third is
`hoist_union_variant`'s nested-composition arm, `oneof-anyof-variant`'s inline
one. The row's three registered witnesses declare the shape in a component,
which `Builder::composed_variant` handles, and the one declarer whose
instrumented run reaches the inline arm, Vercel's description in `jentic`, is
refused by `fern check`. The fourth is case 10c of `hoist_union_variant`,
`oneof-closed-empty-object-variant`'s inline arm. Its witness, Zoonk, declares
the member in a component, which `Builder::variant_ref` handles. The declarers
whose instrumented runs reach the inline arm fail a screen: GitHub's 144
dereferenced descriptions `fern check` rejects, and the Hevy and Paddle
descriptions are third-party copies. Every arm
here stays an unreached arm of a `golden` row, not a settled one. The last
column names each [hand-written fixture](openapi-surface/handwritten/AGENTS.md)
whose arm-level cover executes the arm, or `—`. A hand-written fixture is weaker
proof than a real specification, so an arm it covers stays in this table and
in every count of unreached arms. `RankedBacklogTests` rebuilds this table from
[`golden-reach.tsv`](openapi-surface/golden-reach.tsv), the records and the
fixtures' covers, so a re-measured ledger, a re-rendered record or a cover that
moves an arm fails the gate until the table follows.

**What the hand-written fixtures for the non-schema arms moved.** Five
fixtures cover 17 arms: `format-scalar-bodies` the thirteen `format-*` rows'
`scalar_body` arm, `x-fern-ignore-schema` the ignore row's component-schema
arm, and one `http-*-unrequired` fixture for each of `auth_model`'s
`Auth::None` fallback rows. The changes below took one arm off the count, from
60 to 59 after the [`example` arm's removal](#the-example-arm-removed-as-a-proven-divergence)
took it from 61 to 60, and each is stated here rather than left to the ledger.
Withdrawing corpus row 224 then put `ref_to_class`'s composition-index walk back
on the count, for 60; *No arm rests on a disputed grant*, after the table, says
why. The changes that took the arm off:

- **Three divergences, repaired and proven on the corpus goldens.** Commit
  `35afbf97a` names the member of `01_00_AM` `ONE00AM` as Fern does, not
  `ONE_00_AM`. Commit `63c6be587` makes a scalar string body of any format other
  than date, date-time, uuid, byte and binary generate as `str`. crozier used to
  drop that endpoint, so the thirteen `format-*` rows' arm moved to the
  successor each record names in its **Successor arm** section. The same commit
  stops an ignored component schema from pruning the schemas only it
  referenced. That removed the ignore row's
  `filter_ignored[if ignored_schemas\.contains\(key\) \{]` arm, and its
  `for key in &ignored_schemas` arm now spans 2 regions, not 10. The prune's
  closure walk was also the only golden-only path into `collect_schema_refs`'s
  discriminator arm, so `discriminator-mapping` gains the unreached arm above.
- **One dead arm removed.** `endpoint_module`'s `if !id.is_empty()` block could
  not run. An operation with no tag returns at the empty-id check, at the
  no-dot check, or inside the dotted block. One with a tag returns inside the
  underscore block or the tag block. The block's removal changes no output, and
  `non-identifier-operation-id` now reaches every handling site.
- **Five arms only a refused document reaches.** The three enum-naming arms of
  `enum-leading-zero-member`, `enum-leading-digit-identifier` and
  `enum-empty-identifier-member`, and `add_object`'s recursion guard for
  `recursive-graph` and `mutually-recursive-graph`, carry no fixture. Each has
  a minimal document Fern refuses and a control it generates, recorded in
  [Arms only a refused document reaches](fern-limitations.md#arms-only-a-refused-document-reaches).
- **Nothing else in the ledger moved because of these changes.** The
  ledger was re-measured on this tree, and a control was measured on main's
  `77c5f1535` with the same recipe. The two differ only in the rows above,
  plus `format`, `type-single` and `operation-id`. Those three declare the
  `scalar_body` and `endpoint_module` sites this node changed, and each
  still reaches every site. Sixteen further rows, among them
  `anyof-discriminated-union`'s 29 unreached regions becoming 45, moved
  against the ledger main had committed. That ledger was measured at
  `e8e8dbfb8`, before #322's own changes to `src/ir.rs`. main re-measured
  on its own source gives the same numbers this tree does.

| rank | key | unreached site | regions | search verdict | hand-written cover |
|---|---|---|---|---|---|
| 1 | `request-body-content` | `src/ir.rs::resolve_request_body[if is_optional\(target\) \&\&]` | 1 | `not searched` — no arm search has run | `json-request-shapes` |
| 1 | `request-body-content` | `src/ir.rs::resolve_request_body[let own_count = fields\.len\(\)]` | 27 | `not searched` — no arm search has run | `json-request-shapes` |
| 1 | `request-body-content` | `src/ir.rs::request_media_variants[let mut view = op\.with_sdk_method_name]` | 4 | `not searched` — no arm search has run | `request-media-methods` |
| 1 | `request-body-content` | `src/openapi.rs::Operation::with_sdk_method_name` | 8 | `not searched` — no arm search has run | `request-media-methods` |
| 1 | `request-body-content` | `src/name_refusals.rs::validate_ir[=body\.content\.len\(\) == 1]` | 1 | `not searched` — no arm search has run | `multipart-request-name` |
| 1 | `request-body-content` | `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | 1 | `not searched` — no arm search has run | `request-alias` |
| 1 | `request-body-content` | `src/ir.rs::resolve_request_body[if let Some\(own\) = fields$]` | 5 | `not searched` — no arm search has run | `inline-body-readonly-own-overlap` |
| 2 | `parameter-schema` | `src/ir.rs::InlineHoister::hoist_param_composition[if let Some\(\(items, values\)\) = enum_item \{]` | 21 | `search-incomplete` | `query-union-array-enum-member` |
| 2 | `parameter-schema` | `src/ir.rs::InlineHoister::hoist_param_enum[if let Some\(\(item, members\)\) = schema]` | 19 | `search-incomplete` | `query-array-items-union` |
| 2 | `parameter-schema` | `src/ir.rs::InlineHoister::hoist_param_enum[=^\s*TypeRef::Optional\(element\) => \*element,]` | 2 | `search-incomplete` | `nullable-query-union-items` |
| 2 | `parameter-schema` | `src/ir.rs::InlineHoister::hoist_param_enum[=^\s*element => element,]` | 2 | `search-incomplete` | `query-array-items-union` |
| 3 | `ref-pointer-composition-index` | `src/ir.rs::ref_to_class[while index < parts.len\(\) \{]` | 19 | `exhausted` | `composition-index-pointer` |
| 3 | `ref-pointer-composition-index` | `src/ir.rs::resolve_schema_pointer[^\s*"allOf" => \{]` | 11 | `exhausted` | `ref-pointer-walk` |
| 3 | `ref-pointer-composition-index` | `src/ir.rs::resolve_schema_pointer[^\s*"oneOf" => \{]` | 11 | `exhausted` | `ref-pointer-walk` |
| 3 | `ref-pointer-composition-index` | `src/ir.rs::resolve_schema_pointer[^\s*"anyOf" => \{]` | 11 | `exhausted` | `ref-pointer-walk` |
| 4 | `parameter-in-header` | `src/ir.rs::global_headers[Some\(default\) if count < total && py_type == HeaderType::Str => \{]` | 1 | `search-incomplete` | `header-subset-string-default` |
| 4 | `parameter-in-header` | `src/ir.rs::header_py_type[=^\s*HeaderType::Date]` | 1 | `search-incomplete` | `observatory-client-date` |
| 4 | `parameter-in-header` | `src/ir.rs::global_headers[for header in doc\.global_header_extensions]` | 11 | `search-incomplete` | `observatory-client-headers` |
| 5 | `format-binary` | `src/ir.rs::scalar_body[=Some\("binary"\)]` | 2 | `not searched` — no arm search has run | `json-binary-path`, `json-request-shapes` |
| 5 | `format-binary` | `src/emit.rs::build_example_inner[if s\.type_ref == TypeRef::Primitive\(Prim::Bytes\)]` | 2 | `not searched` — no arm search has run | `json-binary-path`, `json-request-shapes` |
| 5 | `format-binary` | `src/ir.rs::hoist_form_object[if nullable_binary]` | 1 | `not searched` — no arm search has run | `multipart-nullable-array` |
| 6 | `anyof-discriminated-union` | `src/ir.rs::Builder::discriminated_union[if schema.discriminator.is_some\(\) && schema.one_of.is_none\(\) \{]` | 9 | `exhausted` | `nested-array-discriminated-unions` |
| 6 | `anyof-discriminated-union` | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | 5 | `exhausted` | `nested-array-discriminated-unions` |
| 7 | `parameter-in-path` | `src/ir.rs::lifted_client_path_parameters[\.map\(\x7cparameter\x7c ClientPathParameter \{]` | 4 | `search-incomplete` | `base-path-client-argument` |
| 7 | `parameter-in-path` | `src/ir.rs::lifted_client_path_parameters[if let Some\(variable\) = parameter\.sdk_variable]` | 7 | `search-incomplete` | `observatory-client-variable` |
| 8 | `ref-pointer-nested-properties` | `src/ir.rs::ref_to_class["properties" if index]` | 4 | `exhausted` | `ref-pointer-walk` |
| 8 | `ref-pointer-nested-properties` | `src/ir.rs::resolve_schema_pointer[^\s*"properties" => \{]` | 6 | `exhausted` | `ref-pointer-walk` |
| 9 | `media-type-multipart` | `src/ir.rs::resolve_form_object_alias[=^ {8}resolved$]` | 1 | `not searched` — no arm search has run | `multipart-alias-object` |
| 9 | `media-type-multipart` | `src/emit.rs::Imports::json_module[=^ {12}self\.json_module_alias = true;$]` | 1 | `not searched` — no arm search has run | `multipart-json-module` |
| 10 | `ref-pointer-nested-items` | `src/ir.rs::ref_to_class["items" => \{]` | 3 | `exhausted` | `ref-pointer-walk` |
| 10 | `ref-pointer-nested-items` | `src/ir.rs::resolve_schema_pointer[^\s*"items" => \{]` | 3 | `exhausted` | `ref-pointer-walk` |
| 11 | `format-byte` | `src/ir.rs::scalar_body[=Some\("uuid" \x7c "byte"\)]` | 3 | `not searched` — no arm search has run | `sonar-packet-envelope` |
| 11 | `format-byte` | `src/ir.rs::has_byte_text_response[=^ {16}return true;$]` | 1 | `not searched` — no arm search has run | `byte-text-response`, `byte-text-response-controls` |
| 12 | `oneof-anyof-variant` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = variant\.one_of\.as_ref\(\)\.or\(variant\.any_of\.as_ref\(\)\) \{]` | 64 | `exhausted` | `inline-oneof-variants` |
| 13 | `anyof-oneof-variant` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = variant\.one_of\.as_ref\(\)\.or\(variant\.any_of\.as_ref\(\)\) \{]` | 64 | `exhausted` | `inline-anyof-variants` |
| 14 | `oneof-array-variant-anyof-item` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(members\) = item.one_of]` | 41 | `exhausted` | `inline-oneof-variants` |
| 15 | `oneof-discriminated-union` | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | 5 | `exhausted` | `nested-array-discriminated-unions` |
| 16 | `oneof` | `src/ir.rs::hoist_error_body_types[if schema\.discriminator\.is_some\(\)]` | 10 | `not searched` — no arm search has run | `error-body-shapes` |
| 17 | `parameter-style-form-query-object` | `src/emit.rs::append_request_call_args[\} else if qp\.convert \{]` | 30 | `not searched` — no arm search has run | `ore-bin-screen` |
| 18 | `array-item-oneof-discriminated-union` | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | 5 | `exhausted` | `nested-array-discriminated-unions` |
| 19 | `items-oneof-element` | `src/ir.rs::Builder::nested_array_element[if let Some\(members\) = items.one_of]` | 21 | `exhausted` | `nested-array-elements` |
| 20 | `array-item-anyof-discriminated-union` | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | 5 | `exhausted` | `nested-array-discriminated-unions` |
| 21 | `oneof-string-const-variant` | `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(values\) = string_enum_values\(variant\) \{]` | 15 | `exhausted` | `inline-oneof-variants` |
| 22 | `annotated-ref-shape` | `src/ir.rs::InlineHoister::hoist_union_variant[^ {16}\{$]` | 15 | `exhausted` | `inline-oneof-variants` |
| 23 | `discriminator-mapping` | `src/openapi.rs::collect_schema_refs[if let Some\(disc\) = &schema\.discriminator \{]` | 9 | `config-gated` | `discriminator-mapping-audience` |
| 24 | `anyof-array-variant-annotated-ref-item` | `src/ir.rs::InlineHoister::hoist_union_variant[^ {16}\{$]` | 15 | `exhausted` | `inline-anyof-variants` |
| 25 | `anyof-array-variant-composed-item` | `src/ir.rs::InlineHoister::hoist_union_variant[if item.reference.is_none\(\) && is_inline_struct\(item\) \{]` | 13 | `exhausted` | `inline-anyof-variants` |
| 26 | `oneof-array-variant-closed-object-item` | `src/ir.rs::InlineHoister::hoist_union_variant[if item.reference.is_none\(\) && is_inline_struct\(item\) \{]` | 13 | `exhausted` | `inline-oneof-variants` |
| 27 | `anyof-array-variant-closed-object-item` | `src/ir.rs::InlineHoister::hoist_union_variant[if item.reference.is_none\(\) && is_inline_struct\(item\) \{]` | 13 | `exhausted` | `inline-anyof-variants` |
| 28 | `anyof-allof-variant` | `src/ir.rs::InlineHoister::hoist_union_variant[^ {8}\{$]` | 11 | `exhausted` | `inline-anyof-variants` |
| 29 | `array-item-empty-object` | `src/ir.rs::Builder::nested_array_element[if is_inline_struct\(items\) \{]` | 10 | `exhausted` | `nested-array-elements` |
| 30 | `oneof-closed-empty-object-variant` | `src/ir.rs::InlineHoister::hoist_union_variant[^ {8}\{$]` | 11 | `exhausted` | `inline-oneof-variants` |
| 31 | `array-item-pointer-walk-allof` | `src/ir.rs::resolve_schema_pointer[^\s*"allOf" => \{]` | 11 | `exhausted` | `ref-pointer-walk` |
| 32 | `array-item-pointer-walk-anyof` | `src/ir.rs::resolve_schema_pointer[^\s*"anyOf" => \{]` | 11 | `exhausted` | `ref-pointer-walk` |
| 33 | `parameter-in-query` | `src/emit.rs::method_params[if let Some\(default\) = &qp\.default]` | 2 | `not searched` — no arm search has run | `observatory-query-extensions` |
| 34 | `annotated-ref-target-anyof` | `src/ir.rs::InlineHoister::prop_type_ref[if target.one_of.is_some\(\)]` | 6 | `exhausted` | `inline-property-unions` |
| 35 | `anyof-array-variant-anyof-nullable-item` | `src/ir.rs::InlineHoister::hoist_union_variant[simple_nullable_member\(item\) \{]` | 8 | `exhausted` | `inline-anyof-variants` |
| 36 | `anyof-array-variant-oneof-nullable-item` | `src/ir.rs::InlineHoister::hoist_union_variant[simple_nullable_member\(item\) \{]` | 8 | `exhausted` | `inline-anyof-variants` |
| 37 | `inheritance-discriminated-union` | `src/ir.rs::Builder::nested_array_element[^\s*\) \{$]` | 5 | `exhausted` | `nested-array-discriminated-unions` |
| 38 | `property-sole-anyof-closed-object-member` | `src/ir.rs::InlineHoister::prop_type_ref[if members.len\(\) == 1 && is_inline_struct]` | 8 | `exhausted` | `inline-property-unions` |
| 39 | `property-sole-anyof-struct-member` | `src/ir.rs::InlineHoister::prop_type_ref[if members.len\(\) == 1 && is_inline_struct]` | 8 | `exhausted` | `inline-property-unions` |
| 40 | `array-item-pointer-walk-properties` | `src/ir.rs::resolve_schema_pointer[^\s*"properties" => \{]` | 6 | `exhausted` | `ref-pointer-walk` |
| 41 | `http-dpop` | `src/ir.rs::auth_model[=_ => Auth::None,]` | 1 | `exhausted` | `http-dpop-unrequired` |
| 42 | `http-mutual` | `src/ir.rs::auth_model[=_ => Auth::None,]` | 1 | `exhausted` | `http-mutual-unrequired` |
| 43 | `http-negotiate` | `src/ir.rs::auth_model[=_ => Auth::None,]` | 1 | `exhausted` | `http-negotiate-unrequired` |
| 44 | `schema-example-empty-object` | `src/emit.rs::ExampleCtx::value_from_example[if fields.is_empty\(\) \{]` | 5 | `not searched` — no arm search has run | — |
| 45 | `media-type-malformed-key` | `src/ir.rs::has_dispatchable_media[=^ {16}return true;$]` | 1 | `not searched` — no arm search has run | `slashless-json-response` |
| 46 | `array-item-pointer-walk-items` | `src/ir.rs::resolve_schema_pointer[^\s*"items" => \{]` | 3 | `exhausted` | `ref-pointer-walk` |
| 47 | `enum-leading-zero-member` | `src/naming.rs::enum_words[if leads_with_zero_led_digits \{]` | 1 | `exhausted` | — |
| 48 | `format-uuid` | `src/ir.rs::scalar_body[=Some\("uuid" \x7c "byte"\)]` | 3 | `not searched` — no arm search has run | `meadow-tag-code` |
| 49 | `format-date` | `src/ir.rs::scalar_body[=Some\("date"\) =>]` | 2 | `not searched` — no arm search has run | `skyglass-observation-date` |
| 50 | `mutually-recursive-graph` | `src/ir.rs::Builder::add_object[if !self\.building_types\.insert]` | 1 | `exhausted` | — |
| 51 | `recursive-graph` | `src/ir.rs::Builder::add_object[if !self\.building_types\.insert]` | 1 | `exhausted` | — |
| 52 | `schema-example-object-on-map` | `src/emit.rs::ExampleCtx::example_matches_type_through[=TypeRef::Dict\(_, _\) => value.is_object\(\),]` | 2 | `not searched` — no arm search has run | — |
| 53 | `schema-example-outside-enum` | `src/emit.rs::ExampleCtx::example_matches_type_through[=Some\(TypeDecl::Enum\(decl\)\) => value]` | 2 | `not searched` — no arm search has run | — |
| 54 | `x-fern-or-crozier-ignore` | `src/openapi.rs::filter_ignored[for key in &ignored_schemas \{]` | 2 | `search-incomplete` | `x-fern-ignore-schema` |
| 55 | `enum-empty-identifier-member` | `src/naming.rs::finalize_enum_ident[if name.is_empty\(\) \{]` | 1 | `exhausted` | — |
| 56 | `enum-leading-digit-identifier` | `src/naming.rs::finalize_enum_ident[if name.starts_with]` | 1 | `exhausted` | — |
| 57 | `format-email` | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` | 1 | `exhausted` | `format-scalar-bodies` |
| 58 | `format-hostname` | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` | 1 | `exhausted` | `format-scalar-bodies` |
| 59 | `format-idn-hostname` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | 1 | `exhausted` | `format-scalar-bodies` |
| 60 | `format-ipv4` | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` | 1 | `exhausted` | `format-scalar-bodies` |
| 61 | `format-iri` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | 1 | `exhausted` | `format-scalar-bodies` |
| 62 | `format-json-pointer` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | 1 | `exhausted` | `format-scalar-bodies` |
| 63 | `format-password` | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` | 1 | `exhausted` | `format-scalar-bodies` |
| 64 | `format-regex` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | 1 | `exhausted` | `format-scalar-bodies` |
| 65 | `format-time` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | 1 | `exhausted` | `format-scalar-bodies` |
| 66 | `format-uri` | `src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]` | 1 | `exhausted` | `format-scalar-bodies` |
| 67 | `format-uri-reference` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | 1 | `exhausted` | `format-scalar-bodies` |
| 68 | `format-uri-template` | `src/ir.rs::scalar_body[=^ {12}_ => TypeRef::Primitive\(Prim::Str\)]` | 1 | `exhausted` | `format-scalar-bodies` |
| 69 | `ref-pointer-undeclared-component-head` | `src/ir.rs::resolve_schema_pointer[=(?<=schemas\.get\(parts\.next\(\)\?\))\?;$]` | 1 | `exhausted` | `ref-pointer-ignored-head` |

**Configuration-gated arms.** An arm only a generation setting reaches is
not searched for. Contract B's probe runs each declarer through `crozier
generate` with no setting, so no document in any source could execute it, and
an `exhausted` reading would claim a search that never ran. Its record reads
`config-gated` instead, under a `### Configuration gate` heading, and
`RankedBacklogTests` holds it to three parts, each checked against the tree:

1. the configuration field that gates the arm, which the schema names, and the
   crozier function that shows the gate;
2. the gate measured: a hand-written fixture declaring the setting executes the
   arm when generated with it and none of the arm's regions without it. `just
   handwritten-reach` records both runs in
   [`handwritten-config-gates.tsv`](openapi-surface/handwritten-config-gates.tsv);
3. for each declared source, that its probe sets no such setting, and the
   committed files that show the key was never walked or queried there.

The search basis is the setting, then, not a census or an instrumented probe of
every declarer. A hand-written cover cites a `config-gated` record the way it
cites an `exhausted` one. `discriminator-mapping`'s
[record](openapi-surface/golden-reach-witnesses/searches/discriminator-mapping.md)
is the only one. Its arm runs only under an audience filter: since commit
`63c6be587`, `collect_schema_refs` is called only from `filter_by_audience`. The
fixture [`discriminator-mapping-audience`](openapi-surface/handwritten/discriminator-mapping-audience/)
declares `audiences = ["public"]` and executes 9 of the arm's 9 regions with it
and 0 without. Fern keeps the subtypes only the `mapping` names. The
real-specification route stays open: a corpus row registered with an audience
over a document that declares a `discriminator`.

**No arm rests on a disputed grant.** `ref-pointer-composition-index`'s
`ref_to_class` pointer-walk site was reached only through corpus row 224,
`codat-assess`: Codat's `assess/1.0` description at
`APIs-guru/openapi-directory` `f04b8d0b`, registered under the aggregator's
grant while
[`witness-search-blocked-artifacts.tsv`](openapi-surface/witness-search-blocked-artifacts.tsv)
lists the same bytes as grant-blocked for want of a publisher grant. Row 224 is
withdrawn: its golden, its test and its corpus-match line are gone, and
`tests/fixtures/CORPUS.md` records why. [The replacement
search](openapi-surface/withdrawn-witnesses/codat-assess.md#replacement-search)
read Codat's own publication (no licence), every real declarer of
`schema.$ref:composition-index` the committed arm searches name, and their six
sources, and reads `exhausted`: no document reaches the walk and passes all three
corpus screens. So the arm is unreached by any real specification
([the table above](#every-unreached-arm-and-its-search-verdict) counts it), and
the hand-written fixture `composition-index-pointer` covers it at arm level, its
Fern tree byte-matched. That fixture is how crozier learned that Fern types a
pointer ending on a composition member as unknown. Every other row and selector
`codat-assess` declared keeps a golden-bearing witness: the ledger now lists two for
`ref-pointer-composition-index`, three for `ref-pointer-nested-properties` and one,
`auto-agent-protocol`, for `ref-pointer-unnamed-segment`. The seven selectors no
other golden-bearing source declares — `schema.definitions`,
`schema.format=ISO4217` and five vendor extensions — back no feature: none is a
region row's key or a `witness-search-keys.tsv` selector, so none needs a witness
([the list](openapi-surface/withdrawn-witnesses/codat-assess.md#selectors-no-other-golden-bearing-source-declares)). The
2026-09-28 evidence cells that listed it no longer do.

Corpus row 223, `nexmo-conversation`, rested on the same evidence: the Vonage
(Nexmo) Conversation API 2.0.1 at `APIs-guru/openapi-directory` `f04b8d0b`,
under the aggregation's grant alone. [The publisher-grant
search](openapi-surface/withdrawn-witnesses/nexmo-conversation.md#the-publisher-grant-search)
found no Vonage or Nexmo repository publishing it under any licence, so it is
withdrawn the same way. Re-measured without it, every `golden-reach.tsv` site
it reached keeps a golden-only witness, and the three selectors it alone
declared back no feature. Four behaviours no remaining golden executes are
copying a `$ref` whose text names `properties`, naming a variant so copied
after its reference, the inferred `type` tag of a union of such copies, and
dropping an unquoted YAML timestamp example. They now rest on the hand-written
fixture `ref-pointer-walk`, regenerated with the pinned Fern and byte-matched.
That is hand-written evidence, counted as no real-specification match, and each
behaviour's real-specification search reads `search-incomplete`; the YAML
timestamp drop is an open gap
([the table](openapi-surface/withdrawn-witnesses/nexmo-conversation.md#the-reach-row-223-alone-carried)).


#### Unproven arms, named

An unreached arm with neither an arm-level hand-written cover nor a refused-document
record is unproven. It may stand only as a **named gap**: a row below saying why,
which `finished_state_failures` in `tools/surface-census/tests/surface_census_test.py` checks. Over an
arm search the reason is that search's `search-incomplete` verdict; where no arm
search has been run, the reason is `not searched`, its own reason, and never
`exhausted` or `search-incomplete`. A named gap is never counted as proven. It
leaves the list when the reach ledger shows the arm reached, or when a search
decides it. `format-duration`'s `scalar_body` arm, the one row this table carried
before, left it that way: the reach ledger re-measured over corpus row 308,
`yourbrand-ticketing`, reaches it.

| key | unreached arm | why it is unproven |
|---|---|---|
| `schema-example-empty-object` | `src/emit.rs::ExampleCtx::value_from_example[if fields.is_empty\(\) \{]` | `not searched` — the row is new with the example predicates of #361; its three golden witnesses declare an empty-object example but none renders it through a field-less model, and no arm search has been run |
| `schema-example-object-on-map` | `src/emit.rs::ExampleCtx::example_matches_type_through[=TypeRef::Dict\(_, _\) => value.is_object\(\),]` | `not searched` — the row is new with the example predicates of #361; its eleven golden witnesses declare an object example on an open map but none reaches the `Dict` test of a union member, and no arm search has been run |
| `schema-example-outside-enum` | `src/emit.rs::ExampleCtx::example_matches_type_through[=Some\(TypeDecl::Enum\(decl\)\) => value]` | `not searched` — the row is new with the example predicates of #361; its three golden witnesses declare a string outside the enum but none tests it against an enum union member, and no arm search has been run |

#### Unproven features, named

A `FIXTURE` gap row with neither a registered witness nor a hand-written cover is
unproven, and it may stand only as a row below, which the same gate checks. Every
row here is one of the features the naming and example predicates of #361
brought inside the census that no registered golden source declares. None has had
a witness search, so each reads `not searched`; a search's verdict replaces that
reason, and a registered witness removes the row.

| key | region | why it is unproven |
|---|---|---|
| `operation-id-digit-leading-method` | `document-paths` | `not searched` — no registered golden source writes an `operationId` whose derived method name leads with a digit, and no witness search has been run |
| `schema-example-fractional-on-integer` | `schemas` | `not searched` — no registered golden source writes a fractional example on an integer schema, and no witness search has been run |
| `schema-example-array-null-element` | `schemas` | `not searched` — no registered golden source writes an array example holding a `null`, and no witness search has been run |
| `schema-example-temporal-duplicate-element` | `schemas` | `not searched` — no registered golden source writes a date array example repeating an element, and no witness search has been run |
| `schema-example-union-ref-sentinel` | `schemas` | `not searched` — no registered golden source writes a `$ref`-only example on a union, and no witness search has been run |
| `schema-example-on-ref-to-object` | `schemas` | `not searched` — no registered golden source writes an example beside a `$ref` to an object schema, and no witness search has been run |
| `schema-example-on-ref-to-enum` | `schemas` | `not searched` — no registered golden source writes an example beside a `$ref` to an enum schema, and no witness search has been run |
| `schema-example-on-ref-to-union` | `schemas` | `not searched` — no registered golden source writes an example beside a `$ref` to a union schema, and no witness search has been run |

#### The `example` arm, removed as a proven divergence

The table had 61 arms across 55 rows until `example`'s one unreached site,
`src/ir.rs::example_is_schema_definition`, left it: 60 arms across 54 rows. That
helper's only caller was the `InlineHoister::hoist_union_variant` disjunct that
hoisted a bare `type: object` union member carrying a concrete object example
into a named model. Fern at CLI 5.67.1 and python-sdk 5.20.0 never does. It types
the member `typing.Dict[str, typing.Any]` in the hand-written
[`inline-oneof-variants`](openapi-surface/handwritten/inline-oneof-variants/)
fixture's inline response `oneOf`. Local runs at the same pin gave the same
result for an inline request-body `oneOf` (plain, with a `title`, with a
`description`, and with 3.1 `examples`) and for a `oneOf` under an inline
property. The committed probe
[`oneof-bare-object-example-variant`](openapi-surface/probe-expected/oneof-bare-object-example-variant/)
shows it for a component union. No golden reached the disjunct. The byte-match
repair therefore removed it and the helper, and the site left the `example`
row of the [site table](openapi-surface/golden-reach-sites.tsv). The row still
reaches its other five sites; the fixture's feature-level cover of
`oneof-bare-object-example-variant` keeps the shape gated.

#### Rows resting on one document

**57** golden rows rest on one document: a single golden-only witness declares
the feature, so withdrawing that one corpus row would leave the row without a
golden while no line of `src/` changed. The gate recomputes this list from the
ledger, so a registration that adds a second witness removes the row here.

| key | region | only golden-only witness |
|---|---|---|
| `oneof-array-variant-anyof-item` | `schemas` | `langchain-agent-protocol` |
| `anyof-array-variant-annotated-ref-item` | `schemas` | `braintrust-dev` |
| `anyof-array-variant-composed-item` | `schemas` | `braintrust-dev` |
| `oneof-closed-empty-object-variant` | `schemas` | `zoonk` |
| `array-item-pointer-walk-allof` | `schemas` | `dnd5eapi.co` |
| `array-item-pointer-walk-anyof` | `schemas` | `embedpdf-cloudpdf` |
| `annotated-ref-target-anyof` | `schemas` | `braintrust-dev` |
| `anyof-array-variant-oneof-nullable-item` | `schemas` | `ramu-shogi` |
| `property-sole-anyof-closed-object-member` | `schemas` | `npq-registration` |
| `property-sole-anyof-struct-member` | `schemas` | `npq-registration` |
| `http-mutual` | `security` | `cyberark-conjur-api` |
| `enum-leading-digit-identifier` | `schemas` | `bungie.net` |
| `format-idn-hostname` | `schemas` | `short-io` |
| `format-iri` | `schemas` | `short-io` |
| `format-json-pointer` | `schemas` | `k8s-container-service-provider` |
| `format-regex` | `schemas` | `eozilla` |
| `format-time` | `schemas` | `maif.local-otoroshi` |
| `format-uri-template` | `schemas` | `openlinksw-osdb` |
| `request-body-string-map` | `bodies-media` | `confluent-kafka-connect` |
| `parameter-style-pipedelimited-query-scalar` | `parameters` | `loris-dataquery` |
| `single-operation-required-header` | `parameters` | `aws-mobileanalytics` |
| `property-oneof-nullable-pair` | `schemas` | `discord-com` |
| `parameter-style-label-path-scalar` | `parameters` | `slurmdb-rest` |
| `oneof-array-variant-oneof-discriminated-union-item` | `schemas` | `letta` |
| `enum-digit-word-member` | `schemas` | `reverb.com` |
| `oneof-array-variant-composed-item` | `schemas` | `hse` |
| `schema-example-null` | `schemas` | `webflow-v2` |
| `media-type-octet-stream` | `bodies-media` | `apache.org-qakka` |
| `oneof-array-variant-empty-object-item` | `schemas` | `milvus-vector-operations` |
| `oneof-array-variant-oneof-nullable-item` | `schemas` | `discord-com` |
| `oneof-empty-object-variant` | `schemas` | `milvus-vector-operations` |
| `enum-uuid-member` | `schemas` | `reverb.com` |
| `extension-paths` | `oas31-extensions` | `apicurio.local-registry` |
| `boolean-schema-false` | `schemas` | `tamoss` |
| `boolean-schema-true` | `schemas` | `webflow-v2` |
| `contains` | `schemas` | `auto-agent-protocol` |
| `content-schema` | `schemas` | `osparc-simcore-webserver` |
| `dependent-required` | `schemas` | `helixdb-http-api` |
| `dollar-comment` | `schemas` | `volview-backend-contract` |
| `dollar-id` | `schemas` | `sigstore-rekor` |
| `enum-alphanumeric-join-member` | `schemas` | `netbox.dev` |
| `extension-components` | `oas31-extensions` | `hse` |
| `extension-server` | `oas31-extensions` | `webflow-v2` |
| `header-allow-empty-value` | `parameters` | `ndw-accessibility-map` |
| `header-content` | `parameters` | `vtex-pricing` |
| `header-examples` | `parameters` | `microcks.local` |
| `is-beta-extension` | `oas31-extensions` | `squareup.com` |
| `link-description` | `bodies-media` | `listennotes` |
| `link-operation-ref` | `bodies-media` | `gambitcomm.local-mimic` |
| `multiple-of` | `schemas` | `fergus` |
| `operation-external-docs` | `document-paths` | `ideaconsult-enanomapper` |
| `property-sole-oneof-closed-object-member` | `schemas` | `mistle-control-plane` |
| `range-3XX` | `bodies-media` | `osparc-simcore-webserver` |
| `ref-pointer-unnamed-segment` | `schemas` | `auto-agent-protocol` |
| `request-media-named-beside-example` | `bodies-media` | `mockserver` |
| `unevaluated-properties` | `schemas` | `tamoss` |
| `xml-wrapped` | `schemas` | `swagger-petstore` |

#### Golden rows with no golden-only witness

Rows the census classifies `golden` while every source declaring the feature is
a `CORPUS.md` row that carries no committed golden — a `DROPPED` or `REJECTED`
row. The census no longer reads such a row as a source (#352), so none can stand
again. Their cells say so; the
category itself is not this measurement's to move. None stands today: the last
two, `operation-external-docs` (declared by `calorieninjas.com` and `github.com`)
and `xml-attribute` (declared by `atlassian.com-jira`), gained golden-only
witnesses in corpus rows 301 (`ideaconsult-enanomapper`) and 302
(`openaire-graph`).

| key | region | declared only by |
|---|---|---|

#### Golden rows resting only on residual goldens

Three golden tests byte-compare their golden with a measured `unmatched`
residual: `komga` (corpus row 130, 16 files), `short-io` (row 131, 60 files) and
`webflow-v2` (row 132, 304 files). Each is a registered golden source, and every
file of its golden outside that list is byte-compared. A row whose only
golden-only witnesses are among the three is proven only where the code it emits
sits in a byte-matched file, so
[`residual-attribution.py`](../tools/surface-census/residual-attribution.py) (`just
residual-attribution`) answers that from crozier itself: it renders the witness
with the feature's declaring nodes perturbed, generates both documents, and
splits the files that move by whether the golden test compares them. Five rows
rest on those three alone. Three land in byte-matched files and stay proven,
and one of them, `format-idn-hostname`, also moves `reference.md`, which
`short-io` does not byte-match: that part is an open gap of its own, and the
row's disposition is `split` — proven where its code lands in byte-matched
files, unproven in the `unmatched` one named. Two move no generated file at all,
so no byte-matched file vouches for them; they are open gaps, counted among the
unproven, while the
[category rules](#the-category-rules) still classify them `golden` because a
registered golden source declares them.

| key | residual witness | files the feature moves | verdict |
|---|---|---|---|
| `format-idn-hostname` | `short-io` | `src/fern/domains/client.py`, `src/fern/domains/raw_client.py`; open gap: `reference.md`, which is `unmatched` | `split` |
| `format-iri` | `short-io` | `src/fern/domains/types/get_api_domains_response_item.py`, `src/fern/domains/types/get_domains_domain_id_response.py`, `src/fern/domains/types/post_domains_response.py`, `src/fern/domains/types/post_domains_settings_domain_id_request_webhook_url.py` | `byte-matched` |
| `boolean-schema-true` | `webflow-v2` | `src/fern/collections/fields/types/update_fields_response_validations_additional_properties_additional_properties.py`, `src/fern/collections/types/create_collections_response_fields_item_validations_additional_properties_additional_properties.py`, `src/fern/collections/types/get_collections_response_fields_item_validations_additional_properties_additional_properties.py`, `src/fern/collections/types/patch_collections_response_fields_item_validations_additional_properties_additional_properties.py` | `byte-matched` |
| `schema-example-null` | `webflow-v2` | none: replacing its three null examples with a string moves no generated file | `open gap` |
| `extension-server` | `webflow-v2` | none: removing its one Server Object extension moves no generated file | `open gap` |

### The ranked `FIXTURE` backlog

**Where this list stands, and the four ways a row left it.** It carries eight
rows, all new: the `FIXTURE` gaps the naming and example case tables of #361
named, which no registered golden source declares and no witness search has
reached ([tabled at the end of this section](#the-ranked-fixture-backlog), each
also [named `not searched`](#unproven-features-named)). Before them it carried
none. The last eleven left it as `handwritten`, each on a hand-written fixture.
Before them it carried thirteen: `oneof-anyof-variant` left it on corpus rows
303 to 305, and
`oneof-closed-empty-object-variant` on corpus row 306, the remaining-gap
searches' registrations. It carried twenty-four — the twenty-three left when corpus rows
144 to 164 registered witnesses for nine of the thirty-two it carried, and
`oneof-anyof-variant`, one of the two rows
[`hoist_union_variant`'s nested-composition arm](#hoist_union_variant) added, the
other, `anyof-anyof-variant`, being `golden` on `fergus` — before corpus rows 167
to 179 registered witnesses for twelve of them — ten `schemas` rows and both
`security` ones — and the repair two of those registrations needed added one,
`oneof-closed-empty-object-variant`, a new case of `hoist_union_variant` no
registered source declares. Thirty of those thirty-two never stood here
before: the list was exhausted, and seven instrument passes refilled it from the
one direction an exhausted backlog can be refilled from — the instrument, not the
corpus. Twenty-nine branches of `src/ir.rs`'s six blind functions were named that
way; twenty-one of them are still declared by no *golden-bearing* registered
source, which is what a `gap` is, and the other eight are `golden` now.
Two came back by a rule rather than by the instrument. This pass added the schema-name row.
`securityscheme-ref` left this list on route 2 and returned when
[the amended settlement rule](#what-a-probe-may-settle-as-amended-again) stopped a
probe settling a shape Fern generates from. `oauth2-password` joined it from
`limitations` as an `unmeasured` row.
They are
[tabled at the end of this section](#the-ranked-fixture-backlog) and narrated in
[the paragraph that added the first eleven](#the-eleven-rows-the-node-local-predicates-added),
[the one that added the next two](#the-two-rows-the-pointer-form-predicates-added),
[the one that added the next five](#the-five-rows-the-annotated-ref-pass-added),
[the one that added the next two](#the-two-rows-the-discriminated-union-pass-added),
[the one that added the next two](#the-two-rows-the-pointer-walk-pass-added)
and [the one that added the last seven](#the-seven-rows-the-negation-pass-added).
Everything below them is history: every row that ever stood here left by one of
four routes, and which route a row took is what decides the evidence the tree
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
  its search left unanswered. Twenty-three are still settled that way, and each
  now owes a committed proof of its non-generation verdict. The twenty-fourth,
  `securityscheme-ref`, is back in this list, because its verdict is
  `implements`. Every one of them stays convertible: a registrable
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
- **By a hand-written fixture.** The real-specification search failed: five
  searches read `exhausted`, and six read `search-incomplete` until the
  [renewed search](openapi-surface/witness-search-renewed/README.md) found them
  `none-registrable`. So a document written for the purpose was put to Fern at
  the corpus pin, and crozier is byte-compared against the tree Fern generated
  from it. The row is `handwritten`. That is crozier-versus-Fern evidence, but
  weaker than a real specification's, and it never counts as one. The last
  eleven rows left this way. Each stays a search target, and a registrable
  witness found later promotes it to `golden`.

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
The later FOLIO and Raybot tree registrations reach the resolver with committed
byte-matching goldens. The join table below is re-taken on a fresh `just fixtures-coverage` run, and
its `src/refs.rs` row states what they reach.

**What did not move.** These predicates read a `$ref` at the node that writes it,
which the census already visited, so no count rule changed, no existing row's
category, settlement or evidence-cell count moved, and no snapshot digest was
re-pinned.

**The `FIXTURE` backlog refilled from the instrument, not the corpus.**
All 8 `FIXTURE` gaps across the six regions are in the table below; with the
hand-written fixtures it had been exhausted, and the eight rows the #361 case
tables added are what an exhausted backlog refills from.
The eleven rows it held before are `handwritten`: five on the fixtures whose
searches read `exhausted`, and six on the fixtures the
[renewed search](openapi-surface/witness-search-renewed/README.md) admitted.
A hand-written fixture is weaker proof than a real specification, so each of
the eleven stays a search target, and a registered witness would make it
`golden`. The rubric and its four criteria stay stated because the next
`FIXTURE` gap the walk enumerates is ranked by them, and a row that returns is
ranked by [the ranking rubric](#the-ranking-rubric) — crozier sites ascending,
then blind-spot reach descending, then artifact breadth descending, then
witness supply descending, then key. Each row publishes the measured value of
all four, so the order can be checked rather than trusted.

- **Criterion 1**, `crozier sites`: the integer in the row's own `crozier sites`
  cell, re-measured against `src/`.
- **Criterion 2**, blind-spot reach: the `golden blind spots` count
  `just fixtures-coverage` reports for each `src/` file that cell names, summed
  when it names more than one. A `none` cell scores **0**, as the rubric says.
- **Criterion 3**, artifact breadth: a reading, made here and stated once. The
  region files name the artifacts at risk in prose and publish no count, so this
  column normalizes that prose over the rubric's six kinds — `types/`,
  `client.py`, `raw_client.py`, `errors/`, `reference.md`, `core/` — and lists
  the ones it counted beside the number. Re-read the row's `why bytes could move`
  cell after rewording it.
- **Criterion 4**, witness supply: registered sources the census reports
  declaring the shape, read off the row's own `evidence` cell. The census counts
  only registered golden sources now, so a `FIXTURE` gap scores zero here by
  construction — 8 of the 8 score zero. The last row to score above zero,
  `annotated-ref-target-composed` (`box.com` and `asana.com`, both documents
  Fern's own check refuses), left this list when corpus row 144 registered a
  witness Fern accepts.

**The median blind-spot count of this list is 835** — seven entries name
`src/emit.rs` and one `src/naming.rs`, and 0 of the 8 entries name no `src/`
file at all. 0 of the 8 ranked entries reach no blind region. Criteria 1 to 4
separate three groups: the six example arms naming one `src/emit.rs` place,
then `operation-id-digit-leading-method`, whose one place is in the less blind
`src/naming.rs`, then `schema-example-on-ref-to-object`, which names two places.
Criterion 5 orders the six.

| # | key | region | 1. crozier sites | 2. blind spots | 3. artifacts | 4. witnesses |
|---|---|---|---|---|---|---|
| 1 | [`schema-example-array-null-element`](openapi-surface/schemas.md) | `schemas` | **1** (`src/emit.rs` 1) | **835** (`src/emit.rs` 405) | **2** (client.py, reference.md) | **0** |
| 2 | [`schema-example-fractional-on-integer`](openapi-surface/schemas.md) | `schemas` | **1** (`src/emit.rs` 1) | **835** (`src/emit.rs` 405) | **2** (client.py, reference.md) | **0** |
| 3 | [`schema-example-on-ref-to-enum`](openapi-surface/schemas.md) | `schemas` | **1** (`src/emit.rs` 1) | **835** (`src/emit.rs` 405) | **2** (client.py, reference.md) | **0** |
| 4 | [`schema-example-on-ref-to-union`](openapi-surface/schemas.md) | `schemas` | **1** (`src/emit.rs` 1) | **835** (`src/emit.rs` 405) | **2** (client.py, reference.md) | **0** |
| 5 | [`schema-example-temporal-duplicate-element`](openapi-surface/schemas.md) | `schemas` | **1** (`src/emit.rs` 1) | **835** (`src/emit.rs` 405) | **2** (client.py, reference.md) | **0** |
| 6 | [`schema-example-union-ref-sentinel`](openapi-surface/schemas.md) | `schemas` | **1** (`src/emit.rs` 1) | **835** (`src/emit.rs` 405) | **2** (client.py, reference.md) | **0** |
| 7 | [`operation-id-digit-leading-method`](openapi-surface/document-paths.md) | `document-paths` | **1** (`src/naming.rs` 1) | **42** (`src/naming.rs` 38) | **3** (client.py, raw_client.py, reference.md) | **0** |
| 8 | [`schema-example-on-ref-to-object`](openapi-surface/schemas.md) | `schemas` | **2** (`src/emit.rs` 2) | **835** (`src/emit.rs` 405) | **2** (client.py, reference.md) | **0** |

### Generated shapes with no registrable witness

This section is the escalation the amended settlement rule requires. It lists
every shape Fern generates output from that still has no registrable real-world
witness, with its full search record. None is settled by a probe or as
`limitations`. The set is the eleven rows that were the `FIXTURE` rows of the
[ranked backlog](#the-ranked-fixture-backlog), all in
[`schemas.md`](openapi-surface/schemas.md). Each is now `handwritten`, on the
[hand-written fixture](openapi-surface/handwritten/AGENTS.md) its search
admitted, which is weaker proof than a real specification. Each stays a search
target until a registrable witness makes it `golden`. Each one names a branch of
`src/ir.rs` that emits a model, union or alias. For every one of them the branch
was measured by a committed probe that Fern generates from: each has a
`measured` `absent-tree` row in
[`MANIFEST.tsv`](openapi-surface/probe-expected/MANIFEST.tsv) that crozier is
byte-compared against. That comparison is not parity evidence, because the
corpus admits real specifications only.

A twelfth joined later, `handwritten` from the start and never a `FIXTURE` row:
`component-same-primitive-union`, a component composition whose alternatives
all convert to one primitive, which Fern names after its last alternative. No
`MANIFEST.tsv` probe measures it; its
[hand-written fixture](openapi-surface/handwritten/same-primitive-union-components/)
is the measurement. Its line reads `search-incomplete` because no declared
source has been walked or queried for it, and its
[renewed search](openapi-surface/witness-search-union-shapes/README.md) found
the 35 documents declaring it among 693 a bounded code search returned, every
one failing a screen.

Three more joined the same way, from the parameter-lowering repairs:
`query-array-items-union` and `header-subset-string-default` in
[`parameters.md`](openapi-surface/parameters.md),
and `base-path-extension` in
[`oas31-extensions.md`](openapi-surface/oas31-extensions.md). No registered
source declares any of them, and the census predicates each one's key tracks
were run over the documents already acquired for the coverage searches, with no
live query, so each reads `search-incomplete`;
[the record](openapi-surface/witness-search-parameter-lowering/README.md) names
every declarer that search found and why none is registrable.

Four more joined with the worked-example repairs, `handwritten` from the start
in the same way: `unread-date-time-example` here, and three `bodies-media` rows
(`allof-parent-request-body`, `request-example-nested-null`,
`request-example-deprecated-property`). Their
[hand-written fixtures](openapi-surface/handwritten/AGENTS.md) are the
measurement, each line reads `search-incomplete` because no declared source has
been walked or queried for it, and their
[renewed search](openapi-surface/witness-search-example-shapes/README.md) read
941 documents a bounded code search returned and found none registrable. The
table below names `unread-date-time-example`'s candidates; the three
`bodies-media` keys' lines, and the candidates each search found, are under
[`bodies-media.md`'s Witness search (exhaustive)](openapi-surface/bodies-media.md#witness-search-exhaustive)
and in that record.

**Five read `exhausted`, six read `search-incomplete` under the scope
exception.** Each key's reconciled record is its
line under
[`schemas.md`'s Witness search (exhaustive)](openapi-surface/schemas.md#witness-search-exhaustive).
It carries one segment per declared source, counted off that source's
`records.tsv`.

- **Every parse failure is decided.** The 4,380 candidates the census's
  standard-library YAML loader refused for the thirteen searched keys were read
  again by
  [`witness-search-recensus.py`](../tools/witness-search/witness-search-recensus.py)
  `full-yaml`, from the cached copy each ledger row pins, verified against its
  digest. It uses the arm search's pinned `ruamel.yaml` 0.19.1, relaxed on
  duplicate keys and unrecognised tags only where the strict reading refuses
  those. Each document is censused with the key's selector, and its
  `records.tsv` row names the loader. Where every reading refuses it, the row
  reads `census-refused` with each error and the document's sha256. Those are
  Helm and Go templates, JSONC configuration files, truncated JSON, and YAML
  that is not UTF-8 or not well indented. Three documents declare a key; the
  table names each and its measured reason.
- **Six refused candidates were read from the forks' parents.** 18 candidates'
  pinned blob had answered 404. `reacquire-head` requested each again, through
  the rate-limit guard's `core` bucket, at its repository's current revision,
  and at Sourcegraph's mirror of the pinned commit. `reacquire-namesake` then
  sought each in every repository GitHub's repository search names exactly as
  its own is named, which is where a deleted fork's parent is: that
  repository's history of the path, kept only at a commit whose file hashes to
  the blob GitHub's search named. `jdgiles26/inference_builder`'s three
  `builder/samples` documents are NVIDIA-AI-IOT's, and
  `ethandong16/lobehub`'s `packages/openapi/openapi.yml` is LobeHub's. All six
  candidates they account for read `census 0`, each row naming the repository
  that served it.
- **12 candidates stay open, because GitHub refused them.** 9
  are in seven repositories that `GET /repos/<owner>/<repo>` now answers 404 for.
  Three, in two repositories, are in ones whose head no longer holds the file,
  and whose history of the path lists no commit. Sourcegraph's mirror of the pinned
  commit answered 404 for all 12, and no namesake repository holds any of
  their blobs. Each refusal, with its status and time, is the `census` cell of
  the candidate's `records.tsv` row and the note of its key's line. Six keys
  carry at least one, so they read `search-incomplete` and are not closed.
  [The renewed search](openapi-surface/witness-search-renewed/README.md) took
  the routes those records do not show as tried. Five of the 12 were in the
  source's own acquisition cache under another key's row, each hashing to its
  blob, and each reads `census 0`. Every other new route refused the other
  seven: the repository by its numeric id, the blob and the commit by their
  hashes, the owner's code search, and Sourcegraph's default branch. Each key
  reads `none-registrable` there. The ledgers above are unchanged, so the six
  lines keep their verdict.
- **Five keys read `exhausted`.** `oneof-array-variant-annotated-ref-item` and
  `oneof-bare-object-example-variant` had no candidate refused.
  `annotated-ref-target-string-const`,
  `oneof-array-variant-anyof-discriminated-union-item` and
  `oneof-array-variant-anyof-nullable-item` had theirs read from the forks'
  parents. Every candidate of the five is decided.
- **The two keys the final reconciliation left unsearched have left this list.**
  `oneof-anyof-variant` and `oneof-closed-empty-object-variant` joined the
  census after the witness-search-redo contract froze. The remaining-gap
  searches ran each one's first search over all six sources, and each found the
  witnesses it is now `golden` on: corpus rows 303 to 305 for the first, and
  Zoonk's own API, row 306, for the second.

Each census-negative candidate is one `records.tsv` row whose `census 0`, or
whose not-OpenAPI exclusion or `census-refused` reason, is the measured reason
it is unusable. The tables below count those rows rather than restating them,
and name every candidate the census confirmed.

| key | selector | outstanding, per source | census-confirmed candidates, and the measured reason each is unusable | what would unblock it |
|---|---|---|---|---|
| `annotated-ref-target-string-const` | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.const:string-valued` | none | none | nothing a search can add: every candidate is decided |
| `array-item-inheritance-union` | `schema.items>schema.discriminator:inheritance-union` | github-code-search 1, each refused by GitHub at its current revision and by Sourcegraph's mirror, and held by no namesake repository | `AndreVelde/cars-trip` `openapi.yaml`: passes all three screens and is declined as a synthetic kata fixture, as the row's own evidence cell records. `atacan/MistralAPI` `openapi.yaml`: `fern check` exit 1, 12 errors. `opastorello/unifi-api-docs`, eight `network/v9.*/openapi.json` versions at two revisions each: no licence evidence (no `info.license`, no repository licence) and `fern check` exit 1. `airlift/airlift` `api/src/test/resources/openapi/complex-recursive.json`: passes all three screens and is declined as a unit-test resource | a publisher-owned declarer Fern accepts; GitHub or a mirror serving the refused blob again |
| `array-item-pointer-walk-oneof` | `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=oneOf` | github-code-search 2, each refused by GitHub at its current revision and by Sourcegraph's mirror, and held by no namesake repository | `Gi60s/kaos-api` `docs/openapi.json`: no licence evidence, and Fern did not parse it. `api-evangelist` copies of Beyond Identity (three files) and Cvent (two): no licence evidence and `fern check` exit 1. Jentic's Cvent `ea` and Sellsy `2.128.0` trees, ten files: eight fail the licence screen (the aggregator's CC0 grant is admitted, the publisher's grant is unproven), and Cvent's two `*-entry.json` pass it but Fern generates an empty SDK. `api-evangelist/beyond-identity` `openapi/beyond-identity-credential-binding-jobs-api-openapi.yml`, read by the full YAML parser: no licence evidence (no `info.license`, repository licence 404), and the repository describes itself as an independent third-party profile, not Beyond Identity's publication; `fern check` at CLI 5.67.1 exits 0 over its OpenAPI 3.2.0 | a Cvent or Sellsy redistribution grant; GitHub or a mirror serving the refused blob again |
| `component-same-primitive-union` | `components.schemas:same-primitive-union` | not asked: no declared source has been walked or queried for this key | none in a declared source. The [renewed search][union-shapes-search] found 35 among 693 documents: the 32 OpenAPI Generator petstore samples, `jstz-dev/jstz` `crates/jstz_node/openapi.json` and `quay/clair` `httptransport/api/v1/openapi.yaml` fail `fern check`, and `weather-gov/api` `assets/openapi.yaml` grants no licence | a walk or query of each declared source |
| `cycle-into-cycle` | `components.schemas:cycle-into-cycle` | not asked: no declared source has been walked or queried for this key | none in a declared source. The [renewed search][type-and-cycle-search] found 5 among 703 documents: `GetStream/protocol` `openapi/moderation-openapi.yaml` grants no licence (`NOASSERTION`), `Open-EO/openeo-api` `openapi.yaml` and both `apostrophecms` copies fail Fern, and `qoretechnologies/qore` `qlib/BitbucketDataProvider/bitbucket-openapi.json` passes all three screens but diverges apart from the shape (an `allOf` base class inside a cycle) | a walk or query of each declared source |
| `oneof-array-variant-annotated-ref-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component` | none | none | nothing a search can add: every candidate is decided |
| `oneof-array-variant-anyof-discriminated-union-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union` | none | `api-evangelist/unleash` `unleash-projects-api-openapi.yml`: no licence evidence and `fern check` exit 1. `api-evangelist/unleash` `openapi/unleash-unstable-api-openapi.yml`, read by the full YAML parser: no licence evidence and a self-described third-party profile, as the other Unleash copy; `fern check` at CLI 5.67.1 exits 0 over its OpenAPI 3.2.0 | Unleash's own publication of the document with a grant; nothing a search can add: every candidate is decided |
| `oneof-array-variant-anyof-nullable-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member` | none | `screened-nonpublic-input:v2:2a9e147687d94da191ed78449f6ed061:5` at three anonymous revisions: passes all three screens and is declined as an excluded synthetic input, which serves no API | nothing a search can add: every candidate is decided |
| `oneof-bare-object-example-variant` | `schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&!schema.example:schema-shaped&!schema.properties:non-empty&schema.example=object&schema.type:primary=object` | none | `konfig-dev/konfig` `sdks/db/intermediate-fixed-specs/ironclad/openapi.yaml`: passes all three screens and is declined as an SDK vendor's copy, not Ironclad's publication. `api-evangelist/ironclad` `ironclad-workflows-api-openapi.yml`: no licence evidence and `fern check` exit 1. `wiremock/wiremock` `wiremock-admin-api.json`: `fern check` exit 1. Jentic's Ironclad tree, five files: the publisher's grant is unproven | an Ironclad redistribution grant; nothing a search can add: every candidate is decided |
| `property-sole-anyof-composed-member` | `schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf` | github-code-search 2, each refused by GitHub at its current revision and by Sourcegraph's mirror, and held by no namesake repository | `OpenAPITools/openapi-generator` `src/test/resources/3_0/ocaml/enum-in-composed-schema.yaml`: passes all three screens and is declined as a generator's test fixture. `APWG/ecx2-openapi-doc` `ecx2-openapi.yaml` at `9218d45`, 6 sites, read by the full YAML parser: the Anti-Phishing Working Group's own description, GPL-3.0 by its repository `LICENSE` and `info.license`, and `fern check` exits 0, but the generator at `fernapi/fern-python-sdk:5.20.0` exits 1 with `Found 24 errors and 0 warnings`: `Objects can only extend other objects, and root.Brand is not an object`, one per scalar component its search filters list under `allOf` | a Fern that generates APWG's eCX document; GitHub or a mirror serving the refused blob again |
| `property-sole-anyof-empty-object-member` | `schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` | github-code-search 4, each refused by GitHub at its current revision and by Sourcegraph's mirror, and held by no namesake repository | none | GitHub or a mirror serving the refused blob again |
| `property-sole-oneof-composed-member` | `schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.type:primary-scalar&schema.allOf` | github-code-search 2, each refused by GitHub at its current revision and by Sourcegraph's mirror, and held by no namesake repository | `api-evangelist` copies of Cvent (two files) and Infoworks (four): no licence evidence and `fern check` exit 1. `OpenRailAssociation/osrd` `editoast/openapi.yaml`: `fern check` passes and the generator exits 1. `macro-inc/macro` `service-storage/openapi.json`: `fern check` exit 1, 2 errors. Jentic's Cvent `ea` tree, five files: three fail the licence screen, and the two `*-entry.json` pass it but Fern generates an empty SDK | a Cvent redistribution grant, or a Fern that generates OSRD; GitHub or a mirror serving the refused blob again |
| `property-sole-oneof-empty-object-member` | `schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` | github-code-search 1, each refused by GitHub at its current revision and by Sourcegraph's mirror, and held by no namesake repository | `Dynamsoft/Dynamic-Web-TWAIN` `dwt-openapi.yaml`: repository licence `NOASSERTION`, and `fern check` exit 1. `nhsengland/innovation-service-backend-api` `apps/innovations/.apim/swagger.yaml`: Fern accepts it, and its repository licence reads `NOASSERTION` | NHS England's licence evidenced for the file; GitHub or a mirror serving the refused blob again |
| `request-body-property-closed-empty-object` | `mediaType.schema:closed-empty-object-property` | not asked: no declared source has been walked or queried for this key | none in a declared source. The [renewed search][type-and-cycle-search] found 1 among 703 documents: `dcp-ai-protocol/dcp-ai` `api/openapi.yaml` passes all three screens but diverges apart from the shape (a worked example's union variant) | a walk or query of each declared source |
| `type-misspelled-scalar` | `schema.type:misspelled-scalar` | not asked: no declared source has been walked or queried for this key | none in a declared source. The [renewed search][type-and-cycle-search] found 4 among 703 documents: `5GZORRO/slice-manager`, `easysoft/zendata` and `oqlos/oqlos` fail `fern check`, and `jentic/jentic-public-apis`'s BulkSMS description declares the names only on query parameters, where crozier diverges | a walk or query of each declared source |
| `unread-date-time-example` | `schema.example:unread-date-time` | not asked: no declared source has been walked or queried for this key | none in a declared source. The [renewed search][example-shapes-search] found 51 among 941 documents: 24 grant no admissible licence and 12 fail `fern check`; of the 15 Fern generates from, `netgsm/netgsm-sms-js` `openapi.json` differs from crozier only by the content-type-header gap, five byte-match but declare the example only on response models no worked example reads, and nine differ in files apart from the shape | a walk or query of each declared source; the content-type-header repair, which would let `netgsm-sms-js` register |

[union-shapes-search]: openapi-surface/witness-search-union-shapes/README.md
[example-shapes-search]: openapi-surface/witness-search-example-shapes/README.md
[type-and-cycle-search]: openapi-surface/witness-search-type-and-cycle-shapes/README.md

**What would move the rest.** The seventh `search-incomplete` key,
`component-same-primitive-union`, is the other way about: every declared source
still owes it a walk or a query. Nothing a search can still do closes the six
`search-incomplete` keys: their only open items are the 12 blobs GitHub and
Sourcegraph's mirror both refuse. Each would be decided the moment either
served one again, and `tools/witness-search/witness-search-recensus.py reacquire-head --again`
and `reacquire-namesake --again` re-request them. The renewed search decided
five from the acquisition cache, and seven are still refused. A Fern that
generates APWG's eCX document at any of its census-confirmed revisions, or
OSRD's editoast document, would give a key a witness. So would a grant from a
publisher the table names.

**The three grant-blocked artifacts' keys are settled on replacement witnesses,
and none on a blocked artifact.** The eight artifacts
[`witness-search-blocked-artifacts.tsv`](openapi-surface/witness-search-blocked-artifacts.tsv)
lists name three keys. They are Codat's seven `APIs-guru` copies for
`ref-pointer-unnamed-segment` and PandaScore's for
`annotated-ref-target-closed-object` and `annotated-ref-target-oneof`. All
three keys are `golden` on registered documents that declare the same shape,
carry an evidenced licence and byte-match their Fern 5.20.0 goldens:

- `ref-pointer-unnamed-segment` is `golden` on `auto-agent-protocol`, corpus
  row 153 (Apache-2.0, the document's own `info.license`).
- `annotated-ref-target-closed-object` is `golden` on
  `truefoundry-trueforge-5adde28` (row 148, MIT) and on `zulip`,
  `zulip-jentic` and `zulip-jentic-entry` (rows 164 to 166, Apache-2.0 and the
  aggregator's CC0-1.0).
- `annotated-ref-target-oneof` is `golden` on the three Prisma Cloud
  `paloalto-cspm-*` rows (144 to 146, MIT) and on the same three Zulip rows.

None of the three is in this section, and none rests on a probe.

### The ranked list against `golden blind spots`

[`tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md#where-the-goldens-are-blind--just-fixtures-coverage)
calls the `golden blind spots` block "the fixture backlog", and it is — the same
backlog as the table above, expressed per `src/` file instead of per feature. The
two are joined below, in the report's own columns: **printed** is the count
`just fixtures-coverage` reports for the file and the one criterion 2 ranks on,
and **by tier** is the breakdown it reports beside it. Printed sums the two
non-golden tiers, so a region both tiers reach counts twice — the report's own
`total 6909 region(s) across 23 file(s)` line is the de-duplicated union, and the
functions named in each verdict are counted from that union.

| `src/` file | printed | by tier | ranked gaps pointing at it | verdict |
|---|---:|---:|---|---|
| `src/settings.rs` | 1312 | all-e2e 654, non-e2e 658 | none | **Neither.** Generator settings and source precedence are held by configuration journeys, outside the OpenAPI feature census. Measured union: 678 regions. Largest function contributions: `explain` 233, `merge` 46, `resolve` 44. |
| `src/document_refusals/examples.rs` | 1242 | all-e2e 619, non-e2e 623 | none | **Still blind, and why: refusal and malformed-document paths.** Successful goldens cannot reach all rejected shapes; certified refusal measurements and boundary tests hold those paths separately. Measured union: 623 regions. Largest function contributions: `validate` 97, `fern_examples` 85, `merged_member_enum` 57. |
| `src/document_refusals.rs` | 1238 | all-e2e 603, non-e2e 635 | none | **Still blind, and why: refusal and malformed-document paths.** Successful goldens cannot reach all rejected shapes; certified refusal measurements and boundary tests hold those paths separately. Measured union: 637 regions. Largest function contributions: `example_without_discriminant` 66, `check_sdk` 66, `imported_reference_scheme` 55. |
| `src/compare/mod.rs` | 1206 | all-e2e 568, non-e2e 638 | none | **Neither.** SDK comparison, catalog validation and mismatch diagnostics are held by migration journeys and departure tests; they are not an OpenAPI declaration shape. Measured union: 639 regions. Largest function contributions: `check_generator` 242, `run` 100, `check_config` 53. |
| `src/departures.rs` | 1011 | all-e2e 423, non-e2e 588 | none | **Neither.** SDK comparison, catalog validation and mismatch diagnostics are held by migration journeys and departure tests; they are not an OpenAPI declaration shape. Measured union: 593 regions. Largest function contributions: `nullable_items_docs` 96, `from_sources` 46, `crozier_docs_without_lifted` 43. |
| `src/emit.rs` | 835 | all-e2e 316, non-e2e 519 | 7 (the example `FIXTURE` gaps) | **Still blind, and why: example and serialization combinations.** Seven named example gaps point here; the arm inventory distinguishes their missing real-specification proof. Measured union: 535 regions. Largest function contributions: `build_example_inner` 52, `clean_flat_tree` 43, `path_object_value` 39. 7 of [the 91 unreached arms](#every-unreached-arm-and-its-search-verdict) are in this file. |
| `src/ir.rs` | 822 | all-e2e 365, non-e2e 457 | none | **Still blind, and why: schema lowering combinations and refusal paths.** Real-specification parity reaches the implemented cases; the unreached arms below retain their separate proof level. Measured union: 545 regions. Largest function contributions: `hoist_union_variant` 55, `resolve_schema_pointer` 49, `field_type_ref` 43. 77 of [the 91 unreached arms](#every-unreached-arm-and-its-search-verdict) are in this file. |
| `src/openapi.rs` | 736 | all-e2e 332, non-e2e 404 | none | **Still blind, and why: document validation, pruning and malformed input.** Successful corpus generation cannot exercise every rejection and configuration path. Measured union: 407 regions. Largest function contributions: `properties_reference_target` 69, `degrade_unresolved_pointers` 58, `parameters` 44. 3 of [the 91 unreached arms](#every-unreached-arm-and-its-search-verdict) are in this file. |
| `src/name_refusals.rs` | 674 | all-e2e 347, non-e2e 327 | none | **Still blind, and why: refusal and malformed-document paths.** Successful goldens cannot reach all rejected shapes; certified refusal measurements and boundary tests hold those paths separately. Measured union: 347 regions. Largest function contributions: `source_refusals` 121, `validate_ir` 46, `source_request_properties` 44. 1 of [the 91 unreached arms](#every-unreached-arm-and-its-search-verdict) is in this file. |
| `src/compare/report.rs` | 596 | all-e2e 260, non-e2e 336 | none | **Neither.** SDK comparison, catalog validation and mismatch diagnostics are held by migration journeys and departure tests; they are not an OpenAPI declaration shape. Measured union: 336 regions. Largest function contributions: `render_result` 95, `render` 77, `nullable` 44. |
| `src/document_refusals/type_not_defined.rs` | 579 | all-e2e 285, non-e2e 294 | none | **Still blind, and why: refusal and malformed-document paths.** Successful goldens cannot reach all rejected shapes; certified refusal measurements and boundary tests hold those paths separately. Measured union: 294 regions. Largest function contributions: `api_file_reference` 102, `declares_type` 53, `body_declares_type` 39. |
| `src/parity.rs` | 422 | all-e2e 199, non-e2e 223 | none | **Neither.** SDK comparison, catalog validation and mismatch diagnostics are held by migration journeys and departure tests; they are not an OpenAPI declaration shape. Measured union: 223 regions. Largest function contributions: `unified_diff` 83, `compare_trees` 79, `file_difference` 47. |
| `src/compare/discover.rs` | 408 | all-e2e 203, non-e2e 205 | none | **Neither.** SDK comparison, catalog validation and mismatch diagnostics are held by migration journeys and departure tests; they are not an OpenAPI declaration shape. Measured union: 206 regions. Largest function contributions: `discover` 68, `configs_in_tree` 51, `walk_without_git` 39. |
| `src/cli.rs` | 392 | all-e2e 178, non-e2e 214 | none | **Neither.** CLI dispatch and configuration presentation are held by subprocess journeys. Measured union: 217 regions. Largest function contributions: `do_config` 60, `run_other` 43, `do_compare` 30. |
| `src/refs.rs` | 341 | all-e2e 159, non-e2e 182 | none | **Still blind, and why: cross-document resolution failure and tree traversal paths.** Successful pinned documents do not exercise every missing-file or failed-fetch boundary. Measured union: 199 regions. Largest function contributions: `from_reference` 35, `document` 23, `resolve_path_item` 22. |
| `src/compare/reference.rs` | 265 | all-e2e 116, non-e2e 149 | none | **Neither.** SDK comparison, catalog validation and mismatch diagnostics are held by migration journeys and departure tests; they are not an OpenAPI declaration shape. Measured union: 149 regions. Largest function contributions: `locate` 52, `run` 36, `diagnostic` 17. |
| `src/lib.rs` | 138 | all-e2e 38, non-e2e 100 | none | **Neither.** Filesystem output and rendering failures are held by generator journeys. Measured union: 107 regions. Largest function contributions: `render_files` 64, `resolved_names` 30, `generate` 13. |
| `src/compare/color.rs` | 110 | all-e2e 55, non-e2e 55 | none | **Neither.** SDK comparison, catalog validation and mismatch diagnostics are held by migration journeys and departure tests; they are not an OpenAPI declaration shape. Measured union: 55 regions. Largest function contributions: `color_enabled` 18, `status` 11, `exit` 11. |
| `src/schema.rs` | 66 | all-e2e 23, non-e2e 43 | none | **Neither.** The configuration JSON Schema is held by its derivation and drift tests. Measured union: 43 regions. Largest function contributions: `compare_report` 20, `build` 20, `modeline` 3. |
| `src/naming.rs` | 42 | all-e2e 12, non-e2e 30 | 1 (`operation-id-digit-leading-method`) | **Still blind, and why: identifier token shapes.** The digit-leading operation gap points here, and some enum-name refusal arms cannot be reached by a successful golden. Measured union: 30 regions. Largest function contributions: `digit_word` 10, `enum_words` 9, `whole_value_enum_words` 7. 3 of [the 91 unreached arms](#every-unreached-arm-and-its-search-verdict) are in this file. |
| `src/pyfmt.rs` | 38 | all-e2e 14, non-e2e 24 | none | **Neither.** Formatter invocation and failures are held by subprocess journeys. Measured union: 24 regions. Largest function contributions: `format_source` 24. |
| `src/config.rs` | 27 | all-e2e 11, non-e2e 16 | none | **Neither.** Generator configuration defaults are held by configuration tests. Measured union: 16 regions. Largest function contributions: `default_package_name` 10, `new` 4, `new` 2. |
| `src/main.rs` | 6 | all-e2e 6, non-e2e 0 | none | **Neither.** The binary entry point is reached by subprocesses; the coverage gate holds this boundary. Measured union: 6 regions. Largest function contributions: `main` 6. |

**Where the two backlogs agree.** Seven `FIXTURE` gaps point at `src/emit.rs`
and the digit-leading method gap points at `src/naming.rs`. Their criterion-2
scores are this measurement's printed counts, 835 and 42. The other files
have no ranked `FIXTURE` gap pointing at them; their per-arm proof and refusal
measurements are independent of that backlog.

**Where they do not, and the reading that has to change with them.** A blind
region is work only crozier's own tests hold; it is not automatically an OpenAPI
feature awaiting a corpus witness. Configuration, comparison, rendering and
refusal boundaries occupy much of this block. The two largest unranked files,
`src/document_refusals/examples.rs`, `src/settings.rs`,
together 2,554 of the block's 12,506 printed regions, are
configuration and refusal code. Successful corpus goldens cannot prove every
failure path there. The table's verdicts distinguish those boundaries from
lowering and example combinations that a new real specification could reach.

### Enum member and example value cases

The enum predicates read each Schema Object's enum *values*, never its property
names. Their identifier comparison ports `enum_identifier` from `src/naming.rs`:
Latin deburring, UUID handling, word splitting, canonical numbers, connector
joining, digit-boundary collapse and final uppercasing. A collision counts one
schema, as a two-key collision in `components.schemas` counts its two keys. The
branch predicates the token-level arms needed read a trace the port keeps of the
branches each value takes, so a predicate is exact for the arm it names rather
than a second reading of the value beside the port.

| function and branch | exact selector now | enumeration hole left |
|---|---|---|
| `digit_word`: the one-digit numeric prefix of a UUID member | `schema.enum:digit-word-member` | none — the function's ten return words are outputs, not separate source shapes |
| `enum_words`: empty input, wildcard, apostrophe, UUID diversion and a value reducing to no words | `schema.enum:empty-member`, `schema.enum:wildcard-member`, `schema.enum:apostrophe-member`, `schema.enum:uuid-member`, `schema.enum:empty-identifier-member` | none |
| `enum_words`: connector joining — a single-letter run, and a short letter run or letter-then-digits word joined to the word before it | `schema.enum:letter-run-member`, `schema.enum:alphanumeric-join-member` | none |
| `enum_words`: digit-adjacent underscore collapse | `schema.enum:digit-boundary-member` | none |
| `enum_identifier`: Latin deburring | `schema.enum:deburred-member` | none |
| `enum_words` into `numeric_enum_identifier`: canonical leading number of at least two digits, rejected leading-zero token and number too large for a word | `schema.enum:numeric-prefix-member`, `schema.enum:leading-zero-member`, `schema.enum:leading-digit-identifier` | none |
| `enum_words` into `numeric_enum_identifier`: a single-digit leading number, and the small, tens, hundreds and thousands branches inside 0–9999 | `schema.enum:single-digit-prefix-member`, `schema.enum:numeric-small-member`, `schema.enum:numeric-tens-member`, `schema.enum:numeric-hundreds-member`, `schema.enum:numeric-thousands-member` | none |
| `finalize_enum_ident`: empty, still digit-leading, or reserved visit parameter | `schema.enum:empty-identifier-member`, `schema.enum:leading-digit-identifier`, `schema.enum:reserved-member` | none — a member with a second spelling of the same output is named separately by `schema.enum:normalized-collision` |
| `sanitize_identifier`: a class name retains a non-identifier character after Pascal casing | `components.schemas:nonidentifier-name` | none |
| `sanitize_identifier`: the leading-digit prefix on an operation ID after `endpoint_method_name`'s method-name transform | `operation.operationId:digit-leading-method` | none — the transform is ported function by function and pinned by digest, and the port reproduces `src/ir.rs`'s own `endpoint_method_name` expectations |

`src/emit.rs` receives examples from several OpenAPI positions, but the
schema-level selection used by `src/ir.rs` is the one the existing
`schema.example=object` selector had already pinned. The extension partitions
that selection into object, array, string, number, boolean and null. It treats
`example: null` as an absent `Option<Value>` and tries the first `examples`
member, flattening a named Example Object map as `de_schema_examples` does. The
predicates the second table adds read that same selection through the type the
node's own fields give it (resolved type), through its members (nested value),
through the declaration a `$ref` beside it names (resolved type, across one local
reference), or at the position it is written in (position).

| function and branch | exact selector now | enumeration hole left |
|---|---|---|
| `example_matches_type`: object, array, string, number, boolean and null tests | the six `schema.example=<kind>` selectors; required object fields `schema.example:missing-required-field` and `schema.example:undeclared-field`; integer versus other numbers `schema.example:fractional-on-integer`; the enum test `schema.example:outside-enum`; the `Dict` test `schema.example:object-on-map` | none |
| `example_is_object`: optional and named object or alias | `schema.properties:optional-example`, `schema.example:on-ref-to-object`, `schema.example:on-ref-to-alias` | none |
| `value_from_example`: array, object, scalar and null rendering | the six kind selectors; empty arrays and objects `schema.example:empty-array`, `schema.example:empty-object`; temporal strings `schema.example:date-time-string`, `schema.example:date-string`; the float literal `schema.example:integral-on-number`; union `$ref` sentinels `schema.example:union-ref-sentinel`; nested element kinds `schema.example:array-null-element`, `schema.example:array-object-element`, `schema.example:temporal-duplicate-element`; model members `schema.example:empty-object-member`, `schema.example:empty-array-member` | none |
| `named_value_inner`: object, alias, enum and union | `schema.example:on-ref-to-object`, `schema.example:on-ref-to-alias`, `schema.example:on-ref-to-enum`, `schema.example:on-ref-to-union` | none — each resolves the `$ref` written at the example site to the named declaration the arm switches on |
| `build_example_inner`: an object request-body example and its field values, parameter examples, and the endpoint mode | `schema.example=object`; the parameter position `parameter.example:non-scalar-query`; the media-type position `mediaType.examples:named-beside-example`, `mediaType.examples:named-only`; the endpoint mode `operation.responses:wildcard-binary` | none — the documentation, docstring and `reference.md` writers are three renderings of every endpoint rather than a document shape, so no selector distinguishes them |
| `flat`: atom, call, list and dictionary rendering | atom: `schema.example=string`, `=number`, `=boolean`; call: `schema.example:date-time-string`, `schema.example:date-string`, `schema.example:on-ref-to-object`; list: `schema.example=array`; dictionary: `schema.example:object-on-map` | none — its `Example` variants are built by the arms above, each of which a selector now names |

Eight of the 35 features these two tables added have no registered golden
declarer and are `gap` rows, each `FIXTURE`, ranked in
[the ranked `FIXTURE` backlog](#the-ranked-fixture-backlog):
`operation-id-digit-leading-method`, `schema-example-fractional-on-integer`,
`schema-example-array-null-element`, `schema-example-temporal-duplicate-element`,
`schema-example-union-ref-sentinel`, `schema-example-on-ref-to-object`,
`schema-example-on-ref-to-enum` and `schema-example-on-ref-to-union`. The other
27 are `golden`, each on registered sources whose committed Fern golden crozier
byte-matches, and each publishes the reach cell `just golden-reach` measures.

The `hoist_union_variant` bare-object arm this reading was written for, case 11,
is gone: Fern types a bare `type: object` union member as a map whatever example
it carries (the hand-written `inline-oneof-variants` fixture), so the arm and
`example_is_schema_definition` were removed. Its conjunction survives as the
`oneof-bare-object-example-variant` row's selector, and the six-kind extension
leaves no `src/ir.rs` enumeration hole.

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
is recorded as an enumeration hole of one remaining kind, naming the property no
selector kind can express and what closing it would take — the way
`normalization-collision` was recorded before
`components.schemas:normalized-collision` existed. No case is in neither, and none
is in both.

| hole | property the current grammar cannot express | extension that would close it |
|---|---|---|
| **H-ordered-members** | Exactly two ordered `allOf` members: first a reference resolving to a string enum, then a string scalar carrying a pattern and no enum, reference, properties or nested composition | Ordered member selection with target resolution and sibling conjunctions |

**This table is machine-readable, and this is the restatement of it.** The
derivation is declared once, as `CASES` in `tools/surface-census/openapi-surface-census.py` —
one entry per blind function, its cases in order, each case's selector or hole,
and the enclosing gate each case sits inside. `tools/surface-census/tests/surface_census_test.py`
reconciles the two in both directions, so a case in one and not the other fails
the gate, and so does a case whose verdict differs. The declaration lives there
rather than here because something has to be *composed* from it: a residual arm's
selector is the complement of the cases above it, and a complement written out as
prose is a hand-copy of the table that goes quietly wrong the day a branch is
added.

**And the table is tied to the code it reads.** It is a reading of six functions
of `src/ir.rs`, and nothing used to fail when one of those functions grew a
branch, lost one or had one edited — an enumeration whose honesty rests on nobody
having touched the code is exactly the failure this document exists to avoid. So
each function's body carries a digest in that same table, over the body with
blank lines and whole-line comments dropped and each remaining line's whitespace
collapsed, and the offline check recomputes it. **What it catches** is all three
changes: any of them moves the body. **What it does not catch** is *which* case
moved — the digest names the function and nothing finer — and it fires on a
change that moves no branch at all, a renamed local or a reordered `&&` included.
That is over-reporting rather than under-reporting, and re-deriving the function's
rows is what clears it.

A case number carrying a letter is one arm read at the grain the selectors need.
Two things put a letter on a row. A branch reached through `x.or(y)` is two cases
under [the enumeration rule](#the-selector-grammar), so the `oneOf` and `anyOf`
spellings of one arm are two rows; and where an arm's condition is a *disjunction*
— `is_inline_struct` is four conditions joined by `||`, and this table already
split it into separate cases where `nested_array_element` reads it — each disjunct
is its own row, because a conjunction selector cannot express a disjunction and a
selector naming one disjunct would be narrower than the whole arm.

**All three former hole kinds are gone.**
H-residual named every residual arm — the arm selected by the *absence* of every
case above it — and H-negated-value named every arm whose condition was that a
value was not written. Both wanted the same thing, a negation operator over a
group's members, and both are closed by it: the residuals are composed from the
case table and the negated conditions are spelled member by member.
H-example-value named the JSON kind and content of the selected example. It is
closed by `schema.example=object`, `schema.example:schema-shaped`, and their
composition in the former case 11, removed with the arm it read (see
[the removed arm](#the-example-arm-removed-as-a-proven-divergence)).

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
it is why that row ranked first. Corpus row 144 has since supplied that document,
and rows 144 to 146 the `annotated-ref-target-oneof` witness beside it: both rows
are `golden`, and each evidence cell records that the goldens reach the component
builder's `use_site_copy` rather than the `prop_type_ref` arm the row names.

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
distinctly on one shared property, and it *ignores* a `discriminator` written
beside an `anyOf` with no `oneOf`, reading the union as though none were written —
the one place in these six functions the two union heads are not
interchangeable, because Fern applies an explicit discriminator to `oneOf` alone.
This pass first read that as a refusal; the hand-written
`nested-array-discriminated-unions` fixture showed Fern discriminating such a
union over `type: string` tags, and Marimo's golden leaves it ordinary over
untyped `enum` tags, so an `anyOf` member's `enum` tag counts only when typed. A predicate reading only "a `discriminator` beside
a `oneOf`" would have been broader than all three arms and would have put parity
evidence under documents the generator demonstrably sends elsewhere. The reading
is a port of the function rather than a resemblance to it, and
`tools/surface-census/tests/surface_census_test.py` drives the real census over four documents alike in
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
and `tools/surface-census/tests/surface_census_test.py` now drives the real census over the fifteen
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
count changed, and no count rule did: the five conjunctions name positions the
walk did not name before, and `>`, `&`, `~>`, a field, a valued and a predicate
selector all keep the meaning they had. The five readings those conjunctions
carry are member-only and are not selectors, so they add nothing to what the
census counts on its own — a
[member-only reading](#the-member-only-readings) reaches a count only through the
gated conjunction that carries it.

#### The seven rows the negation pass added

**Twenty-three more branches named, sixteen of them already `golden`, and both
enumeration-hole kinds that turned on an absence closed.** This pass declared one
operator, three predicates and twenty conjunctions. The operator is `!` over a
member of a group — the complement of a selector read at one node — and it is
what H-residual and H-negated-value had both been waiting for: the first named
every arm selected by the *absence* of every case above it, and the second every
arm whose own condition was that a value was not written. Seven of the twenty
conjunctions are those residual arms, and their spelling is **composed by the
census from the case table** rather than written anywhere, so adding a case to a
block changes what that block's residual matches with no selector text edited.

**The case table is machine-readable now, and that is why the residuals could be
composed at all.** A residual written out as prose would be a hand-copy of the
table that goes quietly wrong the day a branch is added; declared as `CASES` in
`tools/surface-census/openapi-surface-census.py`, with the coverage document's case analysis
restating it and the gate reconciling the two in both directions, it is a single
source with two readers. The table also carries a digest of each of the six
functions' normalized bodies, so a branch added, removed or edited without the
table being re-derived fails the gate rather than going unnoticed.

**Sixteen came back `golden` and seven `gap`.** The census was run over all 169
registered sources and every one of the twenty-three selectors was put to it by
name. The `golden` sixteen include every residual arm, which is what a residual
should look like: `prop_type_ref`'s own residual is declared at 16,159 sites
across 162 sources, 146 of them carrying a committed golden, and
`nested_array_element`'s at 4,568 across 115. They also include three shapes the
corpus writes rarely and had never been asked about —
`schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object`
rests on `webflow-v2` alone (2 sites), and
`schema.anyOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf`
on `braintrust-dev` alone (1).

**The seven `gap` rows are all `FIXTURE`, and the probe backlog stays empty.**
Each is the `oneOf` twin of a shape the corpus writes under `anyOf`, the
one-member-composition form of a shape it writes at the property, or the
inside-a-union form of a shape it writes outside one — so a real, redistributable
document plausibly writes each, and Fern plausibly emits bytes from it, which is
what `FIXTURE` means. None of them is a measurement no single specification can
hold, and none is a shape for which no witness could be found at all, which are
the two things that would have made one a `PROBE`. **That contradicts the plan
this pass ran under**, which predicted both backlogs would refill; the fixture one
did, from twenty-two rows to twenty-nine, and the probe one is still empty, on the
measurement rather than on the prediction.

**One reading of `src/ir.rs` this pass had to settle against the code, and it is
the reason case 16 looks under-negated.** A residual negates only those cases in
its own block whose selector is the block's gate and one member — a case whose
condition reaches into a subtree states a property no member at this node can
complement — and it does **not** negate a gate that *falls through*.
`prop_type_ref`'s case 1 is exactly that: it holds over an annotated `$ref` that
resolves to nothing and then falls through to the arms below it, so negating it
would make the function's residual narrower than its own arm, which
[the exactness rule](#the-selector-grammar) disqualifies as firmly as a broader
one. The nodes the un-negated cases claim are counted by the residual, which is
the chain overlap that rule permits between two cases of one table — visible,
because every one of those cases is a row here.

**What did not move.** No existing row's category, settlement or evidence-cell
count changed, and no count rule did: `!` adds a way to say what a node does not
declare and leaves `&`, `>`, `~>` and every selector kind meaning what they
meant. The three predicates and twenty conjunctions name positions the walk did
not name before, which is why the feature denominator moves over an unchanged
corpus.

**The size of what this leaves, in numbers rather than in prose.** Twenty-three
rows landed, all of them [`schemas`](openapi-surface/schemas.md)'s: **16
`golden`** and **7 `gap`**, every one of the seven `FIXTURE` and none
`limitations`, because [`fern-limitations.md`](fern-limitations.md) names no row
for any of them. After the example-value selector landed, the case analysis derives
**95** branches, all of which carry an exact selector and **0** of which are
enumeration holes. The follow-on
work the tree inherits is therefore **seven screened corpus rows** — one witness
apiece for the seven `FIXTURE` gaps, each of which promotes its row to `golden`
under [the classification precedence](#the-category-rules) — and **zero probe
work**, because [the probe backlog](#the-probe-backlog) gains nothing here. The
former H-example-value hole is closed by the valued and predicate selectors
`hoist_union_variant`'s former case 11 asked for.

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
`schema.$ref:pointer-walk-reaches=`
[member-only readings](#the-member-only-readings) make that walk instead — the
prefixed pointer walk, not the last-segment lookup `~>` performs — and answer,
for one reference against one document, which segment spellings the loop read.
Each is carried by the conjunction that puts this function's caller gate in front
of it, and it is the conjunction that is the selector.
A **later** segment is read only where every earlier arm's body resolved, which
is why a predicate over the reference string alone would not do:
`A/items/allOf/0` selects case 3 where `A` writes `items` and selects only case 7
where it does not, and `tools/surface-census/tests/surface_census_test.py` drives the census over both
documents and over one addressing a position under two arms in sequence.

**Every one of the five carries this function's caller gate**, which is the other
half of what the rows below say. `resolve_schema_pointer` has exactly one
production call site — `field_type_ref`, on an array-typed property whose `items`
is a reference, behind a `starts_with("#/components/schemas/")` guard — so each
selector's three leftmost members are that gate and the
[member-only reading](#the-member-only-readings) of the arm is its last. Without
them a row would count a pointer the generator never walks, which
`openbanking-brasil-directory` writes: its
`#/components/schemas/ClientCreationResponse/properties/client_id` sits on a path
parameter's schema and selects no case of this table, so **nothing counts it** —
which is why the reading is declared as a member and never as a selector of its
own. The
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
| 2b | the same arm over an `items` whose head is `anyOf`, written where no `oneOf` is. Only the *inferred* spelling reaches it: `discriminated_union` ignores a written `discriminator` beside an `anyOf` with no `oneOf`, and an `anyOf` member's `enum` tag counts only when it declares `type: string`, which is the one place in these six functions the two heads are not interchangeable | `schema.items>schema.anyOf:discriminated-union` |
| 2c | the same call over an `items` declaring neither, which `discriminated_union` delegates to `inheritance_discriminated_union` — OpenAPI's other polymorphism spelling, a base object whose `discriminator.mapping` names the subtypes. **The selector reads one thing the code does not test:** the Rust lets a mapping entry naming the union's *own* coined class name through without resolving it, and that name is coined from the call site rather than declared by the document, so the predicate requires every entry to resolve instead. The two disagree only on a mapping naming a component this document does not declare whose class name is nonetheless the one the caller would coin, which is a document contradicting itself | `schema.items>schema.discriminator:inheritance-union` |
| 3 | `if items.reference.is_some() { return None; }` — the arm's own condition is that the field is written, and nothing more | `schema.items>schema.$ref` |
| 4 | `is_inline_struct(items)` → `add_object`, on an `items` whose `properties` are non-empty | `schema.items>schema.properties:non-empty` |
| 5 | the same arm on an `items` declaring `allOf`, which `is_inline_struct` takes only for a schema declaring no scalar `type`. The negated member is `declares_scalar_type` exactly — the *primary* member of a `type` array — and not the four valued spellings, which would leave a 3.1 `type: [object, string]` beside an `allOf` uncounted while the arm takes it | `schema.items>!schema.type:primary-scalar&schema.allOf` |
| 6 | the same arm on an `items` writing `additionalProperties: false`, which `is_object_type` reads as an object however — or whether — the `type` is written | `schema.items>schema.additionalProperties=false` |
| 6b | the same arm on an `items` writing an explicitly empty `properties: {}` beside no `additionalProperties` — `is_inline_struct`'s third disjunct, which the account this table replaces did not derive. With the map empty and no `additionalProperties`, `is_object_type` reduces to its first disjunct, which is what the last member spells | `schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| 7 | `items.one_of.as_ref().or(items.any_of.as_ref())` → the hoisted union alias, `oneOf` spelling; the gate is `Option::is_some`, so an empty `oneOf: []` reaches it. **What the account this row replaces got wrong is which arm an empty one then takes:** case 2 runs first and claims it, because `inferred_union_discriminant_property` finds `type` inferable vacuously over no members at all and `discriminated_union` returns `Some` with none — the generator coins a `Union({Ctx}ItemItem)` for `items: {oneOf: []}` and no alias, which `tests/resolving-arm-inputs.json`'s `du-nested-empty-oneof` drives and `src/ir.rs`'s own observation of the arm confirms. This row's selector still counts the node, which is the chain overlap [the exactness rule](#the-selector-grammar) permits between two listed cases | `schema.items>schema.oneOf` |
| 8 | the same arm, `anyOf` spelling: an `items` declaring only `anyOf` reaches it identically, and an empty `anyOf: []` is claimed by case 2b for the reason case 7 states | `schema.items>schema.anyOf` |
| 9 | the closing `None` — the residual arm, selected by the absence of every case above it. Its selector is **composed from the case table** and written nowhere: one negated member per case above whose own selector is this block's gate and one member. Cases 5 and 6b state a property of the `items` node that takes two members apiece and case 2's three readings are negated separately, so the composed spelling is the nine below | `schema.items>!schema.$ref&!schema.additionalProperties=false&!schema.anyOf&!schema.anyOf:discriminated-union&!schema.discriminator:inheritance-union&!schema.oneOf&!schema.oneOf:discriminated-union&!schema.properties:non-empty&!schema.type:primary=array` |

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
| 2a | `if let Some(values) = string_enum_values(variant)` — a member declaring a string enum, hoisted as an enum named for the variant; `oneOf` head | `schema.oneOf>schema.enum:string-valued` |
| 2b | the same arm, `anyOf` head | `schema.anyOf>schema.enum:string-valued` |
| 2c | the same arm reached by a string `const`, which `string_enum_values` reads as a one-value enum; `oneOf` head | `schema.oneOf>schema.const:string-valued` |
| 2d | 2c's member, `anyOf` head | `schema.anyOf>schema.const:string-valued` |
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
| 7e | the same arm on an item declaring `allOf`, which `is_inline_struct` takes only for an item declaring no scalar `type`; `oneOf` head | `schema.oneOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf` |
| 7f | the same, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf` |
| 7g | the same arm on an item writing an explicitly empty `properties: {}` beside no `additionalProperties`; `oneOf` head | `schema.oneOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| 7h | the same, `anyOf` head | `schema.anyOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| 13a | `variant.reference.is_none() && variant.all_of.is_none()` over `variant.one_of.as_ref().or(variant.any_of.as_ref())` — a variant that is itself an inline composition becomes a named union, as a component union's does in `Builder::variant_ref`: a sole member is that member, recursed with the parent's own name and index; one member beside `type: null` (`simple_nullable_member`) is that member recursed the same way and made optional — Primula Tracker's `anyOf: [anyOf: [$ref Report, null], array]`, corpus row 226, is `Union[Optional[Report], List[…]]` — and two or more are `hoist_discriminated_union` or else a `TypeDecl::Alias` union of recursed members. The variant's `oneOf` spelling, `oneOf` head. Numbered after the table was published and listed where the body reads it, so the numbers of cases 8 to 12 hold. A variant declaring `allOf` beside the composition is claimed by case 9 instead, which is the chain overlap [the exactness rule](#the-selector-grammar) permits between two listed cases | `schema.oneOf>schema.oneOf` |
| 13b | the variant's `anyOf` spelling, `oneOf` head; the `or` reads `oneOf` first, so a variant declaring both is counted by 13a and 13b alike and takes 13a | `schema.oneOf>schema.anyOf` |
| 13c | the variant's `oneOf` spelling, `anyOf` head | `schema.anyOf>schema.oneOf` |
| 13d | the variant's `anyOf` spelling, `anyOf` head | `schema.anyOf>schema.anyOf` |
| 8a | `is_inline_object(variant)` → `hoist_object` on a variant whose `properties` are non-empty; `oneOf` head. The helper carries no scalar-type guard, so the disjunct is the whole of its own condition | `schema.oneOf>schema.properties:non-empty` |
| 8b | the same, `anyOf` head | `schema.anyOf>schema.properties:non-empty` |
| 9 | the same arm on a variant declaring `allOf` — `is_inline_object` is a disjunction and carries no scalar-type guard, so `all_of.is_some()` is the whole of it; `oneOf` head | `schema.oneOf>schema.allOf` |
| 10 | the same arm, `anyOf` head | `schema.anyOf>schema.allOf` |
| 10a | `is_declared_empty_object(variant)` → `hoist_object` — an explicitly empty `properties: {}` on a `type: object` variant beside no `additionalProperties`; `oneOf` head | `schema.oneOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| 10b | the same, `anyOf` head | `schema.anyOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| 10c | the same arm on such a variant writing `additionalProperties: false`, which the helper admits as its other spelling; `oneOf` head | `schema.oneOf>!schema.properties:non-empty&schema.additionalProperties=false&schema.properties&schema.type:primary=object` |
| 10d | the same, `anyOf` head | `schema.anyOf>!schema.properties:non-empty&schema.additionalProperties=false&schema.properties&schema.type:primary=object` |
| 12a | the closing `base_type_ref(variant)` — the residual arm, its selector **composed from the case table**; `oneOf` head. Only cases 1, 2a, 2c, 8a, 9, 13a and 13b are negatable: every case inside the `type: array` guard states a property of the item rather than of the variant. The nodes those cases claim are counted here too, which is the chain overlap [the exactness rule](#the-selector-grammar) permits between two cases of one table | `schema.oneOf>!schema.$ref&!schema.allOf&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty` |
| 12b | the same, `anyOf` head | `schema.anyOf>!schema.$ref&!schema.allOf&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty` |

#### `prop_type_ref`

It is called on each member of `properties`, so `schema.properties` is the
leftmost member of every case. Cases 8a to 8d are `is_inline_struct` read one
disjunct at a time, as in `nested_array_element`; cases 12a to 12f are the same
helper read again, inside the one-member arity its own arm tests. Cases 11a and
11b are read at their gate: the arms inside it — the member's string enum, its
`$ref`, an unknown, a map, an inline struct, and an array whose inline element
hoists as case 15's does (corpus row 218's `directoryScopeOptions`) — are not
split into rows.

Case 17 precedes the annotated-reference gate. It hoists a string enum reference
narrowed by the second `allOf` member's pattern. Cases 11a and 11b retain the
nullable member's description for an enum, and use the enclosing description
before the member's description for an inline object; their selectors do not change.

**Cases 8d, 12c and 12d require a written `properties` field.** A closed
object without it takes the free-form path, returning `Dict[str, Any]` before
these hoisting cases. Their conjunctions now retain that distinction, including
an explicitly empty `properties: {}`. Case 8d is now a conjunction, so the
composed residual cannot negate it: the closed-empty shape overlaps case 8d
and case 16, while a closed object without `properties` reaches case 16 alone.

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
| 17 | `scalar_narrowed_enum_type` succeeds on exactly two ordered members: a reference resolving to a string enum and a string scalar declaring a pattern; returns the hoisted enum identity | **H-ordered-members** |
| 1 | the outer `if let (Some(schemas), Some((reference, description))) = (self.schemas, described_all_of_ref(prop_schema))` gate, which the arm-observation surface records on entry — before the resolution below. **The code tests one thing more than the four cases inside this gate state:** it also requires `resolve_ref_from_schemas(schemas, reference)` to return `Some`, and a property whose gate holds over a reference naming no component of this document takes none of cases 2 to 5 at all — it falls through to case 6 and beyond. The surface reports exactly that, case 1 without any of 2 to 5, which is how the disagreement was found, and it is why this row's selector carries no resolution while every row below it does. `self.schemas` is `Some` at every call site that reaches a property | `schema.properties>schema.allOf:annotated-ref` |
| 2a | inside it, `if let Some(values) = string_enum_values(&target)` → a hoisted enum, over a target writing an `enum`, which the helper refuses unless the values are strings | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.enum:string-valued` |
| 2b | the same over a target writing a `const`, the spelling the helper falls back to when no `enum` is written. A target writing both is read by its `enum` alone, exactly as case 7b's selector already reads one, so a target whose `enum` is not string-valued beside a string `const` is counted here and falls to cases 3 to 5 — every one of them a case of this table | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.const:string-valued` |
| 3a | inside it, `if target.one_of.is_some() \|\| target.any_of.is_some()` → `hoist_named_copy`; the `oneOf` disjunct. **The code has one continuation this row does not derive:** `hoist_named_copy` returning `None` — a target whose copy declares nothing — falls through to cases 4 and 5 rather than returning, so entering this arm is not the same as taking its product | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.oneOf` |
| 3b | the same arm's `anyOf` disjunct, which a target declaring only `anyOf` reaches identically | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.anyOf` |
| 4a | inside it, `!is_map(&target) && !is_bare_object(&target) && (…)` → `hoist_object_with_doc`; the `!target.properties.is_empty()` disjunct, which excludes both negated helpers on its own — each of them requires an empty `properties` map | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.properties:non-empty` |
| 4b | the same arm's `target.all_of.is_some()` disjunct. `is_bare_object` is excluded by the `allOf` itself; `is_map` is not, so a target declaring `allOf` beside `type: object` and a schema-valued or `true` `additionalProperties` with no properties is counted here and taken by case 5, which is a case of this table and carries its own row | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.allOf` |
| 4c | the same arm's `is_object_type(&target)` disjunct, on a target closing itself. That is the whole of what the disjunct adds over 4a and 4b: with no properties and no `allOf`, `!is_bare_object` needs an `additionalProperties` written and `!is_map` needs it to be `false`, and a scalar `type` beside it is the contradiction [the exactness rule](#the-selector-grammar) already excuses | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.additionalProperties=false` |
| 5 | inside it, the closing `full_type_ref_resolved(&target, schemas)`, selected by the *absence* of cases 2 to 4: `string_enum_values` yielding nothing, no `oneOf` or `anyOf`, and then `is_map` or `is_bare_object` or none of the three positive disjuncts above. No property is common to every target that reaches it — a `type: string`, a bare `{}`, an open map, a bare `type: object` and a `{format: date}` all do — and every way of reaching it is an emptiness test or a negation. It is the residual arm of the **resolution block alone**, so its selector is composed from that block's seven cases and from nothing above the gate: the `~>` in front of the negated members is what scopes it | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>!schema.additionalProperties=false&!schema.allOf&!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty` |
| 6 | `if let Some(member) = sole_inline_all_of(prop_schema)` — one inline `allOf` member and nothing else declared. The arity half is `schema.allOf:sole-member` and the nine sibling-absence tests are the nine negated members, eight at the property and one at the member the descent reaches. Without them the arity alone counts VolView's `TaskSpec.id`, a `type: string` beside a one-member `allOf`, which this function sends to its closing `base_type_ref` | `schema.properties>!schema.$ref&!schema.additionalProperties&!schema.anyOf&!schema.enum&!schema.items&!schema.oneOf&!schema.properties&!schema.type&schema.allOf:sole-member&schema.allOf>!schema.$ref` |
| 7a | `string_enum_values(prop_schema)` → a hoisted enum, over a written `enum`, which the helper refuses unless the values are strings | `schema.properties>schema.enum:string-valued` |
| 7b | the same over a `const`, the spelling the helper falls back to when no `enum` is written | `schema.properties>schema.const:string-valued` |
| 8a | `prop_schema.reference.is_none() && is_inline_struct(prop_schema)` → `hoist_object`, on a property whose `properties` are non-empty | `schema.properties>schema.properties:non-empty` |
| 8b | the same arm on a property declaring `allOf`, which `is_inline_struct` takes only for a property declaring no scalar `type` | `schema.properties>!schema.type:primary-scalar&schema.allOf` |
| 8c | the same arm on a property writing an explicitly empty `properties: {}` beside no `additionalProperties` | `schema.properties>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| 8d | the same arm on a property writing `additionalProperties: false` | `schema.properties>schema.additionalProperties=false&schema.properties` |
| 9 | `if let Some(members) = prop_schema.one_of.as_ref().or(prop_schema.any_of.as_ref())` — the composition gate, whose own condition is that the field is written; `oneOf` spelling | `schema.properties>schema.oneOf` |
| 10 | the same gate, `anyOf` spelling: a property declaring only `anyOf` reaches every arm below it identically | `schema.properties>schema.anyOf` |
| 11a | inside it, `non_null.len() == 1 && non_null.len() != members.len()` — the nullable pair collapsing to its one member; `oneOf` spelling | `schema.properties>schema.oneOf:sole-non-null-member` |
| 11b | the same, `anyOf` spelling | `schema.properties>schema.anyOf:sole-non-null-member` |
| 12a | inside it, `members.len() == 1 && is_inline_struct(&members[0])`, on a member whose `properties` are non-empty; `oneOf` spelling | `schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.properties:non-empty` |
| 12b | the same, `anyOf` spelling | `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.properties:non-empty` |
| 12c | the same on a member writing `additionalProperties: false`; `oneOf` spelling | `schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.additionalProperties=false&schema.properties` |
| 12d | the same, `anyOf` spelling | `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.additionalProperties=false&schema.properties` |
| 12e | the same on a member declaring `allOf` and no scalar `type`; `oneOf` spelling | `schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.type:primary-scalar&schema.allOf` |
| 12f | the same, `anyOf` spelling | `schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf` |
| 12g | the same on a member writing an explicitly empty `properties: {}` beside no `additionalProperties`; `oneOf` spelling | `schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| 12h | the same, `anyOf` spelling | `schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| 13a | inside it, `if let Some(union) = self.hoist_discriminated_union(&name, prop_schema, …)`; the property's `oneOf` spelling. The composition gate above it is what puts the arm inside, so this counts no node cases 9 and 10 do not | `schema.properties>schema.oneOf:discriminated-union` |
| 13b | the same arm, the property's `anyOf` spelling, which only the inferred reading reaches for the reason case 2b states | `schema.properties>schema.anyOf:discriminated-union` |
| 14a | inside it, the closing alias over the members left after `is_null_variant` filtering — unless every one of them is a `boolean` with no composition of its own, which is one `bool` (StandRig's motion `loop`, `anyOf` of `const: false` and `const: true`, corpus row 231) rather than an alias; the residual of the **composition block alone**, so the gate is its one positive member and the complement is of cases 11 and 13 within that gate rather than of everything above it; `oneOf` spelling. Case 12's four rows each state a property of the sole member and take two members apiece, so they are not negatable and the nodes they claim are counted here | `schema.properties>!schema.oneOf:discriminated-union&!schema.oneOf:sole-non-null-member&schema.oneOf` |
| 14b | the same, `anyOf` spelling | `schema.properties>!schema.anyOf:discriminated-union&!schema.anyOf:sole-non-null-member&schema.anyOf` |
| 15 | `prop_schema.ty…primary() == Some("array")` → `hoist_array_item_type` | `schema.properties>schema.type:primary=array` |
| 16 | the closing `base_type_ref(prop_schema)` — the function's own residual, composed from its own arms and not from the two blocks inside them: negating cases 9 and 10 already excludes every case of the composition block. **Case 1 is deliberately not negated**, and that is the one place this composition reads something a string comparison could not: its gate *falls through* when the annotated `$ref` resolves to nothing, so a property taking it can still reach this arm, and negating it would make the residual narrower than its own arm | `schema.properties>!schema.anyOf&!schema.const:string-valued&!schema.enum:string-valued&!schema.oneOf&!schema.properties:non-empty&!schema.type:primary=array` |

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

**The three arms this pass left as holes are now enumerated.** The later
negation pass spells `prop_type_ref`'s former sibling-absence conditions and the
residual composition arms member by member. The example-value pass likewise
named `hoist_union_variant`'s former case 11 with the concrete-object and
schema-shaped-example predicates, before that arm was removed. The case table above is the current source of
truth; these names describe the historical gaps that motivated those later
operators, not entries that remain open.

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
`docs/`, `tools/surface-census/openapi-surface-census.py` and `tools/surface-census/tests/surface_census_test.py`
and nothing else: no `src/` file, no `tests/fixtures/` golden, no `CORPUS.md`
row. A pass that registers no golden cannot move a golden blind spot, and this
pair of columns is what says so with a number instead of an argument. What did
move them is everything else that landed between the two runs — eleven changes
to `src/ir.rs`, 2,608 insertions against 318 deletions, and the corpus rows
other work registered, which is also why `ref_to_class` fell to 2 and why the
file's printed count stood at 235 while `src/openapi.rs`'s fell from 511 to 184
— and then rose to 218, on a probe rather than on a golden (423 and 110 on the
run the join table now comes from).
So the pair of columns answers *what did the conjunction pass buy in the
generator?* with **nothing**, and it is only by publishing both halves that the
much larger movement beside them is not mistaken for an answer to that
question. **The refresh after it reproduced the `after` column digit for digit**
— 43, 25, 23, 22, 15 and 2, the same 130 — so a column that moved elsewhere in
the join table then moved because the measurement did, not because the
attribution drifted. Later runs no longer reproduce it, on the `src/` changes
that landed between them rather than on any census pass: the tree that
registered corpus rows 191 to 196 read the six as 47, 35, 24, 29, 15 and 3, 153
between them, and the run the join table now comes from, over both batches,
reads 52, 49, 7, 9, 15 and 12, 144 between them — the counts the branch that
registered corpus rows 167 to 179 measured on its own tree.
[What those rows moved](#what-corpus-rows-167-to-179-moved) is published below.

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
`tools/surface-census/fixtures-coverage-report.py`, and it lands a blind region on the
innermost `fn` whose brace-matched span contains its first line.

    python3 blind-by-function.py src/ir.rs
"""
import importlib.util, re, sys
from pathlib import Path

REPO = Path.cwd()
spec = importlib.util.spec_from_file_location(
    "fixtures_coverage_report", REPO / "tools" / "surface-census" / "fixtures-coverage-report.py"
)
report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report)

recipe = (REPO / "tools" / "surface-census" / "fixtures-coverage.sh").read_text(encoding="utf-8")
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

**The seven files whose verdicts did not move are what says the attribution is
the join table's own.** Run over this tree, the script reproduces every function
count `src/settings.rs`, `src/cli.rs`, `src/schema.rs`, `src/lib.rs`,
`src/config.rs`, `src/pyfmt.rs` and `src/main.rs` publish, digit for digit and
with no cell edited — so where a count did move, it moved because the
measurement did. `src/refs.rs` and `src/naming.rs` were re-taken on the same run:
the first published no function counts before, and the second's moved on code
landed since, the same with or without corpus rows 167 to 179.

#### What corpus rows 167 to 179 moved

The thirteen goldens this continuation registered are the only change a golden
blind spot answers to, so they are measured the only way that isolates them:
the same tree, run twice. The tree is the branch's, before corpus rows 191 to 196
were merged into it, so the totals below are that tree's and not the join
table's. **With** is the unscoped `just fixtures-coverage` the
join table quotes; **without** is the same recipe scoped to leave out those
thirteen `*_matches_fern_output` tests (`just fixtures-coverage --no-fetch --out
DIR 'not (test(=viskit_studio_matches_fern_output) or …)'`, one `test(=…)` per
row), so a region they alone reach reads blind. The recipe prints `total 1875
region(s)` without them and `total 1764` with them; the three files that moved,
and every function in them whose count did, attributed by the script above
against each run's exports:

| file | function | without | with | |
|---|---|---:|---:|---:|
| `src/ir.rs` | `add_named` | 16 | 1 | −15 |
| `src/ir.rs` | `field_type_ref` | 79 | 66 | −13 |
| `src/ir.rs` | `variant_ref` | 75 | 64 | −11 |
| `src/ir.rs` | `build_enum` | 3 | 0 | −3 |
| `src/ir.rs` | `fastapi_endpoint_name` | 2 | 0 | −2 |
| `src/ir.rs` | `is_declared_empty_object`, `python`, top level | 10 | 5 | −5 |
| `src/ir.rs` | **union** | **472** | **423** | **−49** |
| `src/openapi.rs` | `inline_schema_pointers` | 27 | 1 | −26 |
| `src/openapi.rs` | `normalize_security_scheme_refs` | 18 | 2 | −16 |
| `src/openapi.rs` | `normalize_unlisted_required` | 11 | 0 | −11 |
| `src/openapi.rs` | `schema_pointer_target`, `visit_map`, `de_required` | 12 | 7 | −5 |
| `src/openapi.rs` | **union** | **201** | **143** | **−58** |
| `src/emit.rs` | `named_value_inner`, `client_wrapper_file` | 14 | 10 | −4 |
| `src/emit.rs` | **union** | **304** | **300** | **−4** |

**None of the six blind functions moved.** `hoist_union_variant` holds 52,
`resolve_schema_pointer` 49, `ref_to_class` 12, `prop_type_ref` 9,
`path_group` 15 and `nested_array_element` 7 with and without the thirteen,
though the rows those goldens promoted name arms of `hoist_union_variant` and
`prop_type_ref`: the arms they enter are ones another golden already reached or
no other tier reaches at all, so they pin those arms' bytes without shrinking a
count. What the thirteen did shorten is the code the byte-match repairs landed
beside them — the loader's pointer inlining and the `required` normalization
in `src/openapi.rs`, the component and variant naming in `src/ir.rs` — and
the `$ref` position `securityscheme-ref` names, which a probe had put there.
What stays blind of the code this branch added is five `src/ir.rs` regions and
ten `src/openapi.rs` ones, each a defensive arm only unit tests reach. In
`src/ir.rs`: three of the `HeaderType` float and boolean arms,
`is_binary_media_type`'s slashless fallback, and one short-circuit of
`is_declared_empty_object`. In `src/openapi.rs`: six in `schema_pointer_target`'s
`properties`, `additionalProperties` and composition segments, three in
`RequiredNames`' unlisted-to-listed promotion and its non-list fallback, and
`inline_schema_pointers`' cycle guard.

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

**The cells in the join table now come from one run**: `just fixtures-coverage`
on **2026-10-08**, with production `src/` unchanged from commit `509917e7b94f`.
It measures 243 golden-only tests and their union with 349 other e2e tests,
plus the non-e2e tier. The printed columns and function contributions above
are derived from those exports, with test code excluded. The per-row reach
cells remain a separate per-test measurement (`just golden-reach`), whose
ledger states its own measured commit.

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
`RankedBacklogTests` in `tools/surface-census/tests/surface_census_test.py`. Run it with
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
`tools/surface-census/tests/surface_census_test.py` reconciles the derivation both ways, so a reworded
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
against each. Any search that calls GitHub, Postman or Sourcegraph goes through
[`tools/witness-search/rate_limit_guard.py`](../tools/witness-search/rate_limit_guard.py), whose docstring is
the one statement of the per-bucket wait rule it enforces. What becomes of a row when that search *does* find a witness is
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

**The rule, in one statement.** A row's search returns one of five outcomes, or
the sixth, **`exhausted`**, that [the exhaustive-search contract](#what-makes-a-search-exhaustive)
adds; the outcome decides which of three routes settles the row, and routes 2
and 3 now settle only
[a non-generation verdict](#what-a-probe-may-settle-as-amended-again). **Route 1** settles it
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

**Why Postman is not a declared source.** Postman's public API network is
excluded from every witness search by the user's decision. Reading an OpenAPI
body there requires a Postman API key. This host has none, and the user will not
obtain one. Without a key the network yields only metadata. Its API resources
answer HTTP 401. A collection's unauthenticated JSON link returns a Postman
collection, which is not an OpenAPI description. So no key's record cites
Postman as searched or as outstanding.
[`witness-search-postman/`](openapi-surface/witness-search-postman/README.md)
is kept only as historical evidence of the requests that were issued, and no
gate counts it.

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
[`../tools/surface-census/tests/surface_census_test.py`](../tools/surface-census/tests/surface_census_test.py) accepts a
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

#### What a probe may settle, as amended again

**A locally authored probe settles a row only where its own Fern measurement
shows non-generation.** The rule above let a probe settle any row whose search
reached the right outcome, whatever Fern did with the shape, and that is how a
Fern verdict came to stand where parity evidence belongs: `securityscheme-ref`'s
probe measured Fern *emitting* the scheme a reference names, and the row sat in
`limitations` on it while the code that measurement drove into `src/openapi.rs`
was reached by no committed golden. So the rule is amended a second time.
Where Fern emits output derived from the shape — verdict `implements` — no probe
settles the row however its search ended. The row stays `gap`, carries its full
search record, and waits for a real specification. Routes 2 and 3 survive for
non-generation verdicts alone (`discards`, `ignores`, `refuses`, `crashes`,
`coincidence`), and every row either route settles now owes the committed proof
[below](#what-a-committed-proof-of-non-generation-is) as well as its prose
verdict. A row with no such proof yet records the proof as outstanding in its
own `evidence` cell ([the classification below](#the-limitations-rows-under-the-amended-rule)).

#### What a committed proof of non-generation is

This is Contract A. [`openapi-surface/probe-expected/MANIFEST.tsv`](openapi-surface/probe-expected/MANIFEST.tsv)
is the one declaration of every committed probe measurement the gate reads —
each non-generation proof, and each `measured` tree below: tab-separated,
a header line, one row per key sorted by key, and six columns:

```
key	form	verdict	artifact	control	digest
```

- `key` is the region-file row key the proof settles, spelled as that row spells
  it.
- `form` is `absent-tree`, `refusal` or `differential`.
- `verdict` admits exactly six values: `discards`, `ignores`, `refuses`,
  `crashes`, `coincidence` and `measured`. The first five are
  [`fern-limitations.md`](fern-limitations.md#how-to-read-a-verdict) verdicts,
  each naming the non-generation the proof establishes. `measured`, admitted on
  `absent-tree` rows only, marks a committed Fern tree that records Fern
  **generating** output from a hand-written probe. crozier is byte-gated against
  it, but it settles no row and no gate or report counts it as a non-generation
  proof. The 29 trees the `schemas` witness-supply probes committed are those
  rows, and their region rows stay `gap` until a real specification lands.
  `implements` is refused by construction: a shape Fern emits output derived
  from is not settleable by a probe at all.
- `artifact` is the path, from the repository root, where the proof is committed.
- `control` is the control probe's key for a `differential` row, and `—` for the
  other two forms.
- `digest` is the lower-case hex SHA-256 of the artifact. For a `refusal` it is
  taken over the record's bytes. For the two tree forms it is taken over the
  tree's canonical stream: every file sorted by relative path, each contributing
  its path, a NUL, its byte length, a NUL and its bytes. The digest is what makes
  a corrupted proof something the gate detects, rather than something somebody
  has to remember.

Each form commits one kind of artifact:

1. **`absent-tree`** — Fern accepted the probe, generated an SDK, and emitted
   nothing derived from the shape. The artifact is the complete comment-stripped
   Fern tree at `probe-expected/<key>/`, generated the way
   [`probes/AGENTS.md`](openapi-surface/probes/AGENTS.md) prescribes.
2. **`refusal`** — Fern refused the probe or crashed on it. The artifact is
   `probe-expected/<key>.fern-refusal.txt`, holding five fields in this order and
   spelling: `fern_cli_version`, `fern_python_sdk_version`, `generate_exit`,
   `diagnostic`, `output_tree`. `diagnostic` carries a phrase Fern itself
   printed, and no output tree may exist for the key.
3. **`differential`** — Fern generated output, and no byte of it derives from the
   feature under test. The artifacts are two probes that differ in that feature
   and in nothing else, `probes/<key>.yml` and `probes/<control>.yml`, and two
   committed trees, `probe-expected/<key>/` and `probe-expected/<control>/`,
   which are identical to each other under the gate's normalization. This is the
   form for `ignores` and `coincidence`, and for the `x-` extension positions.

**How the gate reads it.** `witness_supply_probes_match_fern_measurements` in
[`../crates/crozier-e2e/tests/e2e.rs`](../crates/crozier-e2e/tests/e2e.rs) derives its keys from the manifest and from
nothing else. For every row it checks that the artifact's computed digest equals
the declared one. For `absent-tree` and `differential` rows it generates the
named probe with crozier and byte-compares the output against the committed tree,
under the normalization a corpus golden gets. For a `differential` row it also
checks three more things. The two committed trees must be identical; if they are
not, the feature is generation, the row leaves the manifest, and it goes to the
real-specification route as a `gap`. The two documents must not be
byte-identical. And the pair must isolate its feature:
[`../tools/surface-census/probe-differential-isolation.py`](../tools/surface-census/probe-differential-isolation.py)
runs the shape's census selector over both parsed documents, requires the probe
to declare the shape and the control not to, and requires every difference
between them to lie inside that declaration. For a `refusal` row it checks the
five fields against the pin, a non-zero exit, a non-empty diagnostic and an
`output_tree` of `none`. It also checks that no tree sits beside the record, and
it runs crozier over the probe, which must refuse it and write nothing. Both
directions are enforced: a row whose artifact is missing fails, and so does an
artifact under `probe-expected/` that no row names. A divergence is repaired in
`src/`, never by editing a committed tree or record.

This branch also leaves one tier out: the one that requires every non-`golden`
region row to carry either a manifest row or a `gap` classification with an
exhaustive search record. Adding it before the proofs exist would fail the gate
over work that has not been done yet, so until the final reconciliation lands,
the manifest is a growing set and the gate checks only what it names.

#### What makes a search exhaustive

This is Contract B. **The declared sources are the rows of the capability
table below**, which the gate reconciles with the set it enforces. Postman is not
one, for
[the reason recorded beside SwaggerHub's](#the-settlement-rule-as-amended). A record naming any other source answers for no
declared source and leaves no obligation outstanding, and no key's outcome cites
it as searched or as still owed.

**What each source offers decides what it owes.** This table is authoritative.
`RankedBacklogTests` reads it to decide which obligations a key's segment owes
for each source, and nothing a search record says about a source overrides it.

| source | text query | enumerable | established by |
|---|---|---|---|
| apis.guru | no | yes | The catalogue's documented interface is enumeration: `https://api.apis.guru/v2/list.json` lists every API and version, and the service documents no search endpoint over document bodies. Recorded acquisition: `just apis-guru-gap-screen` read the whole catalogue ([`catalogue-portals.md`](openapi-surface/witness-search-redo/catalogue-portals.md)). |
| jentic | no | yes | `jentic/jentic-public-apis` is a git repository whose tree is its index, and it exposes no query interface of its own. Recorded acquisition: the local census over the whole tree at commit `eb9d12a2684b0fbcb5aecf51e8ae54dba0929743` ([`catalogue-portals.md`](openapi-surface/witness-search-redo/catalogue-portals.md)). |
| github-code-search | yes | no | GitHub's documented REST `GET /search/code` takes a text query and returns at most 1,000 results per query, so its index cannot be walked. Recorded acquisition: the `gh api -X GET search/code` sweep and its controls ([`code-platforms.md`](openapi-surface/witness-search-redo/code-platforms.md)). |
| github-publisher-trees | no | yes | A publisher's repository is read by its documented git trees interface at a pinned commit, and has no text query of its own; a query against GitHub is `github-code-search`. Recorded acquisition: the five pinned publisher trees the wide acquisition walked ([`witness-scrape-wide/README.md`](openapi-surface/witness-scrape-wide/README.md)). |
| sourcegraph | yes | no | Sourcegraph's documented stream search API (`/.api/search/stream`) takes a text query with a result cap and offers no listing of its index. Recorded acquisition: the stream queries and their controls ([`code-platforms.md`](openapi-surface/witness-search-redo/code-platforms.md)). |
| vendor-portals | no | yes | A vendor portal publishes its specifications as a set of files at pinned publisher commits, read by listing them, with no query interface over their bodies. Recorded acquisition: the local census over the pinned publisher files ([`catalogue-portals.md`](openapi-surface/witness-search-redo/catalogue-portals.md)). |

Later search nodes measure these same sources, and that measurement is how this
table gets compared against reality. A source that answers a query where the
table says it accepts none, or that turns out to be enumerable where the table
says it is not, is a discrepancy those nodes record against the table. The final
reconciliation then reconciles it.

**A search for a shape is exhaustive only when all five of these hold:**

1. **Every declared source was asked and answered.** A source that accepts a text
   query is answered when condition 2 holds for it. An enumerable source is
   answered when the record names the tree or index and the immutable ref or page
   range it was read at. It must also list every readable OpenAPI 3 document in
   it with the census-selector output over that document, or name the document
   with the measured reason it could not be read. A source that offers both is
   answered only when both hold, because a tree the queries did not walk is an
   unread tree whatever the queries returned.
2. **At least two query phrasings per shape, for each source that accepts a text
   query.** No two may be the same string, and each is recorded verbatim in a
   code span with the count it returned.
3. **A candidate is tested for the shape by the census, never by a keyword
   grep.** It is parsed and run through `tools/surface-census/openapi-surface-census.py`'s own
   selector engine. Keyword queries find candidates, and the census alone decides
   whether a candidate declares the shape.
4. **Every candidate the census confirms is screened on all three corpus
   screens:** licence ([`corpus-licensing.md`](corpus-licensing.md)), immutable
   ref, and Fern's acceptance of the raw document. The outcome is recorded per
   candidate.
5. **No line reads `unanswered` for a required source.**

**The outcome vocabulary gains a sixth word:** **`exhausted`** is `none-found`
over a search meeting all five conditions. It is the only outcome that licenses
the statement that a shape has no registrable real-world witness. A `none-found`
over a search that does not meet the five reads `search-incomplete`, exactly as
before.

**A rate-limit cap is never `unanswered`.** `unanswered` is reserved for a source
that refused, errored, or does not exist. A bucket reaching its cap is not a
source declining to answer: the search waits for the reset and continues. The
gate refuses, at any outcome, a record that reads a source `unanswered` for a
rate-limit cap.

**Where the record lives.** It lives in two places, and the gate reconciles them
in both directions.

- The row's own region file, in a `### Witness search (exhaustive)` table with
  one line per `(key, source)`:

  ```
  | key | source | outcome | queries | walk | candidates | screens |
  ```

  `source` is one declared source in a code span. `outcome` is the key's outcome
  in a code span, the same on every line of the key. `queries` gives each
  phrasing in a code span, followed by `→` and the count it returned, with
  phrasings separated by `;`. `walk` reads `` `<tree or index>` at `<ref or page
  range>` → <n> documents ``. `candidates` lists each candidate the queries or
  the walk surfaced, in code spans. `screens` gives, per census-confirmed
  candidate, `` `<candidate>` licence `<outcome>` ref `<outcome>` fern
  `<outcome>` ``, with candidates separated by `;` and each outcome reading
  `passed` or `failed: <reason>`. A cell with nothing to record reads `—`.
- The per-source evidence directory,
  `openapi-surface/witness-search-<source>/`, holds the raw acquisition
  manifests, the census output over every candidate and every walked document,
  the per-candidate screen records, and the quota-guard wait log. Its
  `records.tsv` indexes them, one row per fact, under the header
  `key	kind	subject	result	file`:
  - A `query` row has the phrasing as its `subject` and the count as its
    `result`.
  - A `walk` row has `<tree>@<ref>` as its `subject` and the document count as
    its `result`.
  - For an enumerable source, `enumeration.tsv` carries one row for every
    document in each named pinned walk, under
    `walk\tdocument\trevision\tsha256\tmatched_keys\tstatus`. `matched_keys`
    is the comma-separated set of gap keys whose selector matched, empty when
    none did; `status` is `readable` or `unreadable: <reason>`.
  - A `document` row in `records.tsv` exists only when that key matched, with `census <n>`
    for positive `n`. This compact form avoids repeating a zero for every
    `(key, document)` pair in a large tree. The independent pinned listing is
    `acquisition-manifest.tsv`, under
    `walk\tdocument\trevision\tsha256`; its path set and digests must equal
    `enumeration.tsv` exactly. A query source keeps its ordinary candidate
    census records in `records.tsv`.
  - A `candidate` row has the candidate as its `subject` and `census <n>` as its
    `result`.
  - A `screen` row has `<candidate> licence|ref|fern` as its `subject` and the
    screen outcome as its `result`.
  - A `wait` row indexes the quota-guard wait log.

  `file` names the evidence file under that directory that the row rests on.

Every query, count, walk, candidate and screen outcome in the table must be a
row of the evidence directory, and every row there must be accounted for in the
table. The gate checks that `enumeration.tsv` has exactly the named walk's
document count with no duplicate identity, that its paths and digests equal
the independent pinned acquisition manifest, and that every matched key has
exactly one positive `document` record
and no positive record exists without a census match. Every other evidence file
must be named by a record, and every named file must exist. So an unsupported
table cell, an absent document, and an unaccounted evidence file all fail.

**The gate reads all of it.** `RankedBacklogTests` refuses an `exhausted` record
that does any of the following:

- drops a declared source, or reads any declared source `unanswered`;
- records fewer than two distinct phrasings for a source the table above says
  accepts a text query;
- records no tree or index at an immutable ref or page range for a source the
  table says is enumerable, or leaves a walked document with neither a census
  output nor a recorded reason;
- lists a candidate with no census confirmation, screens a confirmed candidate
  on fewer than three screens, or keeps a confirmed candidate that passes all
  three, which is a witness rather than an absence;
- disagrees with its evidence directory in either direction;
- counts an undeclared source among the sources it answered for.

It reads each source's obligations from the table and never from the record, so
a record that claims a source offers less than the table declares is refused,
naming the source, rather than being believed.

#### The limitations rows under the amended rule

The 70 rows that read `limitations` before this amendment were each read against
their own [`fern-limitations.md`](fern-limitations.md) verdict. Each row's cell
was read for the feature *that row* is about. Where a compound cell rules on two
features, the row says so. Every row's own `evidence` cell now records which of
six classes it falls in: a non-generation row names its committed measurement
after **`Committed Fern measurement:`**, or the proof it still owes after
**`proof outstanding:`**. A demoted row names the verdict that demoted it after
**`demoted to gap:`**, and one a registered specification has since settled names
that verdict after **`settled after demotion:`** instead. A row the final reconciliation promoted
reads **`Promoted by the final reconciliation`** from `limitations`: the
2026-09-28 walk found golden-bearing registered sources declaring it, so the
[precedence](#the-category-rules) makes it `golden`. Its committed proof stays
in its cell as a cross-reference rather than its settlement. Sixteen rows moved
this way: 14 on an `absent-tree` or `refusal` artifact and 2 on a
`differential` pair (`nonascii-info-title` and `boolean-schema-true`). The six
`gap` rows promoted beside them were `UNREACHABLE` and never read `limitations`,
so they are outside this population. So are the other fourteen `UNREACHABLE`
rows, whose differentials are cited in the same spelling.

| class | rows | settlement instrument |
|---|---:|---|
| non-generation, using a Contract A artifact (`absent-tree` or `refusal`) | 47 | its tree or refusal record, declared in the manifest when committed |
| non-generation, using a `differential` pair | 5 | a probe and control isolating the feature, and their two identical trees when committed |
| demoted to `gap` for a generation verdict (`implements`) | 0 | a registered real-world specification |
| demoted to `gap` as `unmeasured` | 0 | a real specification, or first a measurement of what Fern does |
| demoted, since settled `golden` by a registered specification | 2 | its witness's committed golden |
| non-generation, promoted to `golden` by the final reconciliation, its proof kept | 16 | its witnesses' committed goldens; the Contract A proof stays as a cross-reference |
| **total** | **70** | |

Both demoted rows are settled. The generation row, `securityscheme-ref`, whose
probe measured Fern emitting the scheme the reference names, is `golden` on the
HuaTuo node and server descriptions, corpus rows 178 and 179, which reference a
scheme inside their own document. The `unmeasured` row, `oauth2-password`, whose
ledger cell carries only the `supply` qualifier, is `golden` on oSPARC's payments
service, corpus row 177, which declares a password flow. The three compound
cells rule this way:

- `encoding-explode`'s cell rules `refuses` on a multipart object's `explode` and
  `ignores` on a list's. Its list differential pair is committed. The object
  refusal has no distinct region key or Contract A artifact and remains open.
- `encoding-allow-reserved` reads only the `ignores` half; its pair is committed.
- `boolean-schema-true` reads `coincidence` at `items` and `discards` at a
  property. Its committed pair measures the first; the ledger records the
  candidate measurement for the second.

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
