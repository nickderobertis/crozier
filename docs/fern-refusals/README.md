# Fern refusal registry

The classes of input Fern (CLI 5.163.1, `fernapi/fern-python-sdk` 5.41.3, the
certified pair `assets/scaffolding/metadata.json` declares) refuses, crashes on,
or falsely reports success over, and what crozier does with each. The whole
population, every class's probe and committed shapes, and each class's
confirmations are measured at that pair.
crozier's default is to generate wherever its output is valid and useful;
`fern-strict` refuses as Fern does. This directory is the one statement of which inputs that covers. The gate
(`crates/crozier-e2e/tests/e2e.rs::fern_refusal_classes_hold`, in `just check`) reads it, and
nothing but the steps below writes it.

## The contract

**The setting.** `fern-strict` (default `false`) layers like `audience-strict`:
`--fern-strict` on `crozier generate`, `CROZIER_FERN_STRICT`, and `fern-strict`
at the config's top level or under `generators.<name>`. Strict mode only ever
decides whether an SDK is written, never a byte of one that is.

**A refusal**, in either mode, exits 1, writes nothing to the output directory,
and prints one stderr line naming the class id, the offending element (its
method and route, and the parameter, property, schema, enum value or scheme
name, or its JSON pointer) and, for a strict-mode refusal, that `fern-strict`
caused it.

**The files.**

- [`classes.tsv`](classes.tsv) — one row per class, sorted by `class`:
  `class` (kebab-case id), `family` (`names` for a diagnostic about a name Fern
  cannot form or that collides with another; `documents` for every other),
  `fern_stage` (`check` or `generate`), `fern_exit`, `diagnostic` (Fern's phrase
  verbatim, document-specific parts written `<…>`), `documents` (how many
  `documents.tsv` rows carry it), `status` (`unevaluated`, `generate` or
  `refuse`), `crozier_diagnostic` (the literal substring crozier's refusal line
  must contain; `—` while `unevaluated`), `population_strict`
  (`<refused>/<total>` over the retrievable documents carrying the class,
  each refused with the diagnostic of one of its classes; `—` while
  `unevaluated`). `build` writes `documents` and `population_strict`.
- [`documents.tsv`](documents.tsv) — one row per distinct refused document,
  sorted by `digest` (lower-hex SHA-256 of its exact bytes): `source`,
  `locator`, `revision` (immutable), `recorded_by` (the committed records naming
  the refusal, `;`-separated), `fern_stage`, `fern_exit`, `fern_log` (the
  committed log holding Fern's complete diagnostic list), `classes`
  (`,`-separated, never empty), `crozier_exit`, `crozier_files` (crozier's
  release build, default mode, as an earlier tree recorded it; `—` where none
  did), `crozier_strict_exit` (the release build under `--fern-strict`; `—`
  until one of the document's classes is evaluated). That run's stderr is
  committed under
  [`../openapi-surface/fern-refusals/crozier-logs/`](../openapi-surface/fern-refusals/crozier-logs/)
  and named by the document's `measurements.jsonl` record, and `build` fails
  unless its exit agrees with that log and its refusal line names one of the
  document's own classes: a refusal at the parser, or by a class Fern does not
  report, is no refusal by the class. All three come from
  `measurements.jsonl`, which `just fern-refusals-measure` fills, so `build`
  reproduces them. `measure` takes only the strict verdict: crozier refuses
  before it generates, so that run is quick, while a default-mode run writes
  the whole SDK (up to tens of thousands of files and many minutes on the
  largest documents), and no classification, table or gate reads its exit or
  file count — the gate reads `classes` and `crozier_strict_exit` alone.
- [`unretrievable.tsv`](unretrievable.tsv) — a selected document whose bytes
  could not be read again, or whose Fern run never finished inside `measure`'s
  bound (`unmeasured: …`), with its revision and the reason.
- [`generated.tsv`](generated.tsv) — a selected document whose `fern check`
  failed but whose `fern generate` at the pin still writes an SDK, with its log
  and the check-only phrases it printed. Fern produces output for these, so
  crozier is expected to byte-match them, not refuse them: this is a candidate
  list the witness-registration work may screen, and nothing here registers one.
- [`dispositions.tsv`](dispositions.tsv) — every refused document crozier's
  strict run refuses with a class its Fern log does not carry, and why that
  agrees with Fern, sorted by `crozier_class` then `document`:
  `generate-stage` (a class only `fern generate` reports, on a document Fern's
  check stopped before generating), or the Fern verdict on a `representative`
  reduced (`reduction`: `;`-separated JSON pointers deleted, `*-a,b` keeping
  only `a` and `b`, `—` none) until its own classes are gone: `masked` (Fern
  then names crozier's class), `reported-other` (another class, or a check-only
  finding), or `over-broad` (Fern's check accepts it; crozier's detector is
  narrowed to match, so the row is history and the document is refused by
  another class). `reduce` measures each reduction at the pin, one Fern run at
  a time, into
  [`../openapi-surface/fern-refusals/reductions/`](../openapi-surface/fern-refusals/reductions/)
  and the row's `reduced_digest`, `check_exit`, `generate_exit`, `classes` and
  `log`, which `check` holds to that log.
- [`findings.tsv`](findings.tsv) — shapes measured and found **not** to be
  refusals, each with its probe under
  [`../openapi-surface/fern-refusals/findings/`](../openapi-surface/fern-refusals/findings/):
  `check-only` phrases `fern check` refuses while `fern generate` writes an SDK
  past them, and `generates` shapes neither stage objects to. crozier departs
  from one on purpose: `parameter-normalization-collision`'s shape (parameters
  in two locations normalizing to one name) is refused in both modes as
  `request-property-camelcase-collision`, under the ruling that such a name
  collision is a Fern defect crozier does not copy, since Fern writes past it
  into Python its own message calls broken.
- `<class>/probe.yml` — a minimal hand-written document isolating the class.
- `<class>/*-probe.yml` and `<class>/*-control.yml` — the class's other
  measured shapes: a `-probe` is one Fern refuses, a `-control` a near miss it
  generates from. `shapes` measures each at the pin into
  `evaluation-logs/fern-<name>.log` and
  [`shapes.tsv`](../openapi-surface/fern-refusals/shapes.tsv), and `check`
  fails when a shape's verdict is not its role's or its log is another pair's.
- `<class>/fern-refusal.txt` — Fern's measured outcome on the probe in Contract
  A's five fields (`fern_cli_version`, `fern_python_sdk_version`,
  `generate_exit`, `diagnostic`, `output_tree`). A false success records
  `generate_exit: 0` with the stderr phrase. A shape Fern turns out to generate
  from is no refusal class and is not recorded here.
- `<class>/evaluation.md` — once evaluated: whether crozier's default output
  imports, its `mypy` error count under the generated `pyproject.toml`'s own
  configuration, and what it sends and parses at the offending element against
  what the document declares, each linked to a committed log.
- `<class>/wire_test.py` — exactly when `status` is `generate`: a pytest module
  run against crozier's default SDK for the probe. The gate generates that SDK
  with `--package-name fern`, installs what its `pyproject.toml` declares (the
  pinned `mypy` among it), and runs the module with `CROZIER_SDK_DIR` (the SDK
  root), `CROZIER_SDK_SRC` (its `src/`) and `CROZIER_PROBE` set. It asserts that
  the package imports, that `mypy .` in the SDK root reports zero errors, and,
  through an injected `httpx.MockTransport` as `tests/runtime/` does, that the
  request at the offending element carries exactly the wire names and values the
  probe declares and that a declared response parses into its declared model.

**The gate** fails when a row's `probe.yml` or `fern-refusal.txt` is missing,
the record's versions differ from the pin or its `diagnostic` is empty; when a
`refuse` class's probe is not refused (as above) with and without
`--fern-strict`, or its line lacks `crozier_diagnostic`; when a `generate`
class's probe does not generate by default, its `wire_test.py` fails, or it is
not refused under `--fern-strict` with such a line; and when a `documents.tsv`
class id or a directory here is no `classes.tsv` row. An `unevaluated` row is
checked for its files only. `fern_refusal_classes_hold` checks every condition
but the `wire_test.py` run in the offline `just check`; that one builds the
SDK's environment from PyPI, so `sdk_env_fern_refusal_wire_tests_hold` runs the
whole gate in `just test-sdk-env` (CI's `sdk-env` job, required by `gate`).

**No false refusals.** `just test-corpus-match-strict` runs the corpus
byte-match with `CROZIER_FERN_STRICT=true`, so a class that refuses a document
Fern generates from fails it.

## The population

Every document crozier's committed records name as refused, crashed on or
falsely reported successful by Fern: the `DROPPED` rows of
`tests/fixtures/CORPUS.md` whose reason names Fern (located by
[`dropped-sources.tsv`](../openapi-surface/fern-refusals/dropped-sources.tsv)),
and every `docs/openapi-surface/**/screens.jsonl` record whose `fern` verdict is
`failed:` or `refused:`. Deduplicated by digest. A served APIs.guru document no
immutable commit holds is pinned by its recorded digest (`revision` is
`sha256:<digest>`). `fern-docs-fai`'s row drops every revision of one document
by a rule rather than a list, so the population carries the revision
`dropped-sources.tsv` names for it. Fourteen `DROPPED` rows name a document
without ever recording the ref that was screened; they are in
`unretrievable.tsv` with what later searches did record, and the ref the
`letta` row names answers 404.

A document is **refused** when its `fern generate` exits non-zero, writes
nothing, or reports a refusal class over a document it did not parse (a false
success). Its classes are the ones its `fern check` names when the check names
any (`fern_stage` `check`), else the ones its generation names (`generate`).
A document's generate outcome is **derived from its classes**, not measured
document by document: each class's probe shows whether its phrase stops
`fern generate` (a phrase that does not is a `check-only` finding), so a
document whose check names a class is refused, and one whose check names only
check-only findings goes to `generated.tsv`. `fern generate` was run on a
document only where its check named no class (a check that passed, or one that
reported a document it could not parse); those per-document results are kept in
`measurements.jsonl`. The derivation is confirmed on the population: `confirm`
runs `fern generate` on up to three real documents per class — documents
carrying only that class first, from different publishers where they exist —
into
[`confirmations.tsv`](../openapi-surface/fern-refusals/confirmations.tsv), and
`check` fails if any of them generates where its class says Fern refuses.

`tools/fern-refusals/fern-refusals.py` builds the tables:

```sh
tools/fern-refusals/fern-refusals.py select            # the population, offline
just fern-refusals-measure                 # rebuild the release binary, then measure: fetch, run Fern and crozier (network, Docker)
tools/fern-refusals/fern-refusals.py build             # rewrite documents.tsv, generated.tsv, unretrievable.tsv, class counts
tools/fern-refusals/fern-refusals.py confirm           # sample each class's real documents through fern generate
tools/fern-refusals/fern-refusals.py shapes            # measure every class's probe and control shapes (Fern, one at a time)
tools/fern-refusals/fern-refusals.py reduce            # measure each dispositions.tsv reduction (Fern, one at a time)
tools/fern-refusals/fern-refusals.py check             # offline drift check; tools/fern-refusals/tests/fern_refusals_test.py runs it
```

`measure` fetches through `tools/witness-search/rate_limit_guard.py`'s paced raw lane
(answered from its shared GitHub response cache where the request was made
before), and takes every Fern verdict at the certified pair
`assets/scaffolding/metadata.json` declares. It reuses a committed screen's
`fern check` log only where the screen's record states the exit and names that
pair's CLI (and no other generator), and keeps a `measurements.jsonl` record
only where its `fern_cli` and `fern_python_sdk` are that pair; everything else
gets a fresh `fern check` — then `fern generate` unless the check named a class
— in a scratch workspace outside any checkout, writing each log to
[`../openapi-surface/fern-refusals/logs/`](../openapi-surface/fern-refusals/logs/)
(its first line naming the pair) and the result to `measurements.jsonl` beside
it. A fetch that failed under another pair is tried again. Fern runs `--jobs`
at a time and crozier `--crozier-jobs`, and a Fern run past `--timeout` is
ended with every process it started; its document gets no generation and is
listed in `unretrievable.tsv` as unmeasured, with the stage that ran past the
bound. Fern runs with a 16 GB Node
heap: at the default 4 GB the largest documents (the GitHub REST descriptions)
report the host's memory rather than Fern's diagnostics. The
`crozier_exit` and `crozier_files` on record were last taken by the release
build after `main`'s `layout` setting merged, each run bounded at
45 minutes and none reaching it: [`crozier-timings.tsv`](../openapi-surface/fern-refusals/crozier-timings.tsv)
keeps each document's size, outcome and wall-clock seconds from that run, taken
with up to eighteen measurement runs at once on a shared, loaded host; `measure`
no longer takes them. `measure --crozier-again` retakes every document's
strict verdict and its log after crozier changes, and a record without its log
is retaken by a plain `measure`. `build` classifies
every diagnostic in a document's logs against `classes.tsv`'s and
`findings.tsv`'s templates; one that matches no single template fails the
build, so a new phrase becomes a class or a finding on purpose.

`probe <class>…` measures Fern on a class's probe (`fern check`, then
`fern generate` whatever the check said) and writes its `fern-refusal.txt` and
the class's `fern_stage`/`fern_exit`, refusing to record a probe Fern generates
from; `finding <name>…` does the same for `findings.tsv`, refusing a probe Fern
refuses. Both keep Fern's logs under
[`../openapi-surface/fern-refusals/probe-logs/`](../openapi-surface/fern-refusals/probe-logs/).

## What the measurement settled

- **Every refused document is refused by a class detector.** All 737 refused
  documents are refused under `--fern-strict` with a class diagnostic (each
  one's `crozier-logs/` record): 721 with a class their Fern log carries, and
  16 with one [`dispositions.tsv`](dispositions.tsv) shows agrees with Fern
  (11 generate-stage, one masked, four where Fern names another class or a
  check-only finding at the same element). None stops at the parser any more.
  Twenty GitHub Enterprise Server descriptions passed the parser's default
  bounds, so crozier once stopped before any class ran: `068ff58b…` replays
  about 1.8 million YAML alias events, and nineteen share a schema by more
  than ten aliases per anchor. The replay bound is now one event per
  byte of the document (never below a million) and the alias/anchor ratio
  pre-scan is off, while an alias-expansion bomb is still refused
  (`src/yaml.rs`). A Mistral description Fern generates from writes
  `nullable: 1`, which crozier now reads by its truth (`src/openapi.rs`), so
  all 13 documents in `generated.tsv` generate in crozier's strict mode too;
  `build` holds both halves.
- **Reducing the representatives narrowed eight rules in five classes.** Where crozier
  refused a document with a class Fern did not report, a representative was
  reduced until Fern's own classes were gone. In 25 of those documents Fern's
  check then accepted it, and each detector now follows a committed shape
  measured at the pin: an extension's reference reached through an array
  (`extension-reference-cycle`), an `allOf` over any union or a
  one-member alias (`object-extends-non-object`), a cycle that grows by one
  reference a turn, which Fern refuses as `generated-file-name-too-long`
  rather than `heap-exhausted`, and a one-member `allOf` alias that grows
  nothing (`heap-exhausted`), a plain YAML timestamp and an error example
  whose status code has more than one body (`example-type-mismatch`), and an
  unresolved legacy `#/definitions/` reference (`type-name-not-letter-led`).
  A tag led by a digit names a sub-client that is no identifier and is now
  `generator-lint-failure`, as Fern's `ruff check` fails it. Each class's
  `evaluation.md` names its shapes. The expanding-union check also
  enumerated every path through the reference graph, which ran unbounded on
  Stripe's descriptions once the cycle check no longer refused them first; it
  is now decided once per document.

- **GitHub's duplicate request names no longer collide.** None of the 276
  GitHub REST descriptions in the population carries
  `request-property-name-collision` at the pin: Fern's importer renames a path
  parameter a body property shares to `{name}PathParam` (the finding
  `request-property-name-collision-generates`). It reserves only the body's own
  properties and its `allOf` parents' own, so a path `id` beside an inline body
  whose grandparent declares `id` keeps its name and is refused (the class's
  probe; Rebilly's KYC requests). A header collides with a query parameter of
  its name (`X-Namespace` with `namespace`) only where it rides too few
  operations for Fern to lift it to the client, as crozier's `global_headers`
  decides (`header-query-*` shapes).
- **A redeclared property is mostly generated.** An object or request body
  redeclaring a property of its one `allOf` parent, or two parents sharing one,
  generates (`object-property-name-collision-generates`; Mistral's
  conversations). `object-property-name-collision` remains for an `allOf` of
  two `$ref` parents that share a property one of them inherits (the class's
  probe; Cloudflare's error bodies), and `request-property-name-collision` for
  an inline body's own property beside a parent's.
- **`appng-rest-api`** does not fail after a passing check at the pin: its
  `fern check` exits 1 with `Service requires auth, but no auth is defined.`,
  because its only security scheme is an `apiKey` in a cookie, which Fern does
  not import (`service-auth-undefined`). `CORPUS.md`'s reason predates the pin.
- **Enum members led by a digit** (`1st` → `ONE_ST`) **or a zero-led digit run**
  (`007` → `SEVEN`) are generated by Fern, and crozier emits the same members:
  both are `generates` findings. What Fern refuses is a member it can name no
  way (`enum-value-unnameable`, e.g. `10080`) or names with a leading digit
  (`enum-name-unsuitable`, e.g. `#0094FF` → `0094Ff`).
- **A security scheme `$ref` into another document** is `unresolved-reference`,
  a false success: `fern generate` exits 0 over a document Fern never parsed,
  printing `Failed to resolve ./components.yaml#/components/securitySchemes/…`.
  Where the referenced document is present Fern keeps the referenced scheme's
  credential, and crozier resolves it the same way: corpus row 309
  (`huatuo-node-tree`) is a real tree whose `BearerAuth` names
  `../components.yaml`, and its golden byte-matches (issue #351).
- **The generator's own crashes** are classes too, measured in `fern generate`
  after a clean check: `generator-lint-failure` (the generated package fails
  `ruff check`, e.g. two union variants or a method and a sub-client given one
  Python name), `generator-missing-type` (a `KeyError` over a type Fern named
  but never emitted, e.g. an inline enum header), and
  `generated-file-name-too-long`. The `Failed to format …` lines printed before
  a lint failure only say which snippet did not parse; they were never seen
  without the failure they precede. `heap-exhausted` is Fern's check running
  out of a 16 GB heap on a document of 120 to 150 kilobytes (both of its
  documents); a union recursing through a component's `$defs` is followed as a
  schema of its own and generates (`defs-json-value` shape).
- **Shapes Fern stopped refusing.** A required property beside an `allOf`
  member referenced into a component's own `definitions` (NSwag's
  `KitchenSink`) is no `example-unexpected-property`; a boolean `enum` or
  `const` with a default is no `named-type-default`, where a string `const` is.
  Each is a control of its class, and crozier generates it.
- **Contract A's refusal rows** (`header-array`, `header-object`,
  `nonascii-operationId`, `ref-pointer-unnamed-segment` in
  [`../openapi-surface/probe-expected/MANIFEST.tsv`](../openapi-surface/probe-expected/MANIFEST.tsv))
  stay there. Where a phrase class would share one's shape, its probe isolates
  the phrase another way: `type-name-not-letter-led` names a schema `123456`
  rather than `$ref`ing an unnamed pointer segment, and `example-type-mismatch`
  is probed with a date rather than a header list. That class's detector also
  refuses `header-array`'s shape, an optional array header Fern promotes to a
  client field, with `header-array-*-probe.yml` documents of its own (issue
  #353).
