# Matching Fern's output

crozier's contract: **its generated Python, with comments stripped, is
byte-for-byte identical to Fern's**, for the same OpenAPI input and the same
naming. This doc explains how that is verified, why each shape generates the way
it does, and the one accepted upstream exception.

## Why the fixtures are what they are

crozier consumes an **OpenAPI document** — nothing else. Fern can be driven from
either its own definition files or an OpenAPI document, and the two produce
*structurally different* SDKs (the definition carries a package/namespace layout
that a plain OpenAPI document does not). So the golden fixtures must be Fern's
output **generated from OpenAPI**, or the target would be unreachable by design.

Two fixture sources, both Fern's real output (Apache-2.0, see `NOTICE`):

- **Offline corpus** — Fern commits Python SDK snapshots for its OpenAPI-sourced
  test APIs (the `*-openapi` seeds). These need no Docker, are reproducible, and
  gate on every run. `query-parameters-openapi` is the one vendored seed.
- **Exhaustive target** — the broad `exhaustive` spec. Fern's
  committed `exhaustive` Python output is *definition*-derived, so it is **not** a
  valid OpenAPI target. The OpenAPI-derived golden comes from running
  Fern's containerized generator over the vendored
  `tests/fixtures/exhaustive/openapi.yml`.

What a golden *can* pin is bounded by what Fern implements, and that boundary is
measured rather than guessed: [`fern-limitations.md`](fern-limitations.md) records
every limitation Fern 5.20.0 was measured to have — the shapes it discards,
ignores, refuses or matches only by coincidence — with the probe, the emitted
output and the exit code behind each. Read it before choosing what a new fixture
should contain.

Numbered real-world corpus goldens are maintained through the manually
dispatched **Fern goldens** workflow, not by running the generator scripts by
hand. The fixture/upgrade loop, exact provenance, partial-success behavior, and
local diagnostic recipes are documented in
[`fern-goldens.md`](fern-goldens.md).

## How the comparison works

The e2e (`tests/e2e.rs`) runs the compiled binary over a fixture's `openapi.yml`,
strips comments from crozier's output with the **same** stripper that produced
the committed fixtures (`crozier::strip_python_comments`, exposed as
`crozier internal-strip`), and asserts equality against
`tests/fixtures/<api>/expected/**`. Comment stripping is the *only* normalization
— everything else must match exactly.

## Parity status and the residual manifest

**Every registered corpus reproduces its whole committed Fern golden
byte-for-byte at `fernapi/fern-python-sdk:5.20.0`.** Every `Corpus` in
`tests/e2e.rs` carries an empty `unmatched` list; that file is the measured
truth, and this document holds the judgment about *why* each shape generates the
way it does. Per-corpus file counts deliberately live only next to the data they
describe, so prose here cannot drift away from them.

Parity is the harness's default rather than an opt-in claim. The gate walks the
full Fern `expected/` tree and requires every file to match, walks crozier's
output back so a newly emitted file cannot fall outside the compared set, and
requires each `unmatched` entry to *stay* divergent so a closed gap cannot linger
as a suppression. Nothing in the mechanism can hide a file that starts diverging:
adding a path to `unmatched` is a visible source change, and the reporter rejects
an entry that already matches. Registration alone would not be enough — a corpus
no test drives, or a fetched-spec corpus missing from `just test-corpus-match`,
would skip silently everywhere — so
`every_registered_corpus_is_wired_into_the_gate` derives both wirings from
`tests/e2e.rs` and the `justfile` and fails when either is absent.
`just fixtures-gaps` re-measures every corpus and
prints the census; `fixtures-candidates` remains an alias. `just fixtures-diff`
prints normalized diffs for investigation. See
[`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md).

### The one accepted exception

Every registered comparison corpus must have an `expected/` tree. The sole
exception is a corpus with a validated exact `known-fern-failure.json`: Fern
itself cannot produce an SDK, so there is no golden to compare, and the corpus
stays covered at the spec/process boundary instead. The harness fails on any
other missing golden, so removing a tree cannot silently reduce byte-comparison
coverage.

`calorieninjas.com` is the only such corpus. Its source operation declares no
`operationId`; Fern 5.20.0 emits unnamed methods (`def (`, `_raw_client.(`) and
its own Ruff pass then rejects the SDK, so the failure is upstream of crozier —
crozier generates that same spec successfully and *names* the operation. The
registration is bound to the exact generator version, corpus name/ref/URL, exit
code, ordered syntax diagnostics with their source lines, Ruff summary, and
failed command, and generation retries the fixture on every run: an unexpected
Fern *success* is fatal, so the exception cannot outlive the limitation. It is a
distinct harness state from an open gap — a corpus that carries both a
`known-fern-failure.json` and an `expected/` tree is an error, not a suppression.
See [`fern-goldens.md`](fern-goldens.md#exact-known-upstream-failures).

`query-parameters-openapi` is the one corpus whose golden is not the installed
result of `fern generate --preview`. It is Fern's committed
`seed/python-sdk/query-parameters-openapi/no-custom-config` repository tree at
commit `4d07e6aeeed1d88917ce59dfc9b4cf9e6008e553` (the commit releasing
`fernapi/fern-python-sdk:5.20.0`). That distinction is explicit in the harness:

- The generated-SDK comparison covers every file Crozier emits. The two real
  defects exposed by this seed are closed: a schema-less query parameter is a
  string, and a package-root raw client derives its class from the configured
  root client name. The packaged `_default_clients.py` helper matches too.
- Seventeen repository-only files are classified separately:
  `.github/workflows/ci.yml`, `.gitignore`, `poetry.lock`, `snippet.json`, and
  the thirteen files under `tests/custom/` and `tests/utils/`. Inspection across
  the packaged `--preview` corpora confirms that they do not occur there;
  `_default_clients.py`, by contrast, occurs broadly and remains compared.
- Six generated files have exact raw-byte expectations for Crozier's packaged
  form: `README.md`, `reference.md`, `pyproject.toml`, `.fern/metadata.json`,
  `src/seed/client.py`, and `src/seed/core/client_wrapper.py`. The seed embeds a
  local repository publication (`generatorVersion: local`, requested SDK
  version `0.0.1`, GitHub repository metadata, and the local generator's
  all-optional snippet policy). Those inputs are not present in the OpenAPI
  document or Crozier's naming settings. Length-plus-FNV fingerprints pin every
  byte of the packaged 5.20 output, while a separate assertion preserves the
  evidence that it differs from the local seed form.
- Conversely, `src/seed/core/enum.py` is present throughout the packaged 5.20
  corpora but absent from this local seed. It is an explicit packaged-only file,
  reverse-checked on both sides.

Both classifications are reverse-checked. A repository-only path becoming
Crozier output fails and must re-enter comparison; a packaged expectation
changing by any byte, disappearing, or unexpectedly matching the local seed
fails until its evidence is deliberately updated. The gate also walks Crozier's
output back against the golden, so a newly emitted file can never silently fall
outside the compared set.

**`exhaustive` matches its whole tree** — the widest single parity proof in
the corpus, and the only fixture that exercises the whole generator end to end.
This
covers `version.py`, `py.typed`, the **entire type
layer** (every `types/*.py` module including the hoisted `typesAnimal` variants),
the **entire `core/` runtime**, the
**`errors/` package** (a generated exception class per declared error plus its
lazy-loading `__init__.py`), each endpoint client's package marker
(`<tag>/__init__.py`), and the per-tag `raw_client.py` for **every endpoint
tag**. That spans the no-request-body tags (`endpoints_put`,
`endpoints_urls`, `noreqbody`), query parameters (`endpoints_pagination`,
incl. array/allow-multiple params in `endpoints_params`), scalar/enum/union `$ref`
bodies via the `convert_and_respect_annotation_metadata` wrapper where needed
(`endpoints_primitive`, `endpoints_enum`, `endpoints_union`), header params
(`reqwithheaders`), inlined object bodies — both `$ref` and inline — hoisted
field-by-field (`endpoints_object`, `endpoints_http_methods`,
`endpoints_content_type`, `inlinedrequests`), container bodies
(`endpoints_container`), unknown (`{}`) and `application/octet-stream` bytes bodies
plus mixed path/query/body operations (`endpoints_params`, `noauth`), and declared
4xx error responses that raise generated exceptions (`noauth`, `inlinedrequests`).
The **high-level per-tag `client.py`** and the **root
`client.py`**
(`FernApi`/`AsyncFernApi`, bearer auth) match too — each wrapper method returns
`_response.data` and carries a worked `Examples` docstring produced by a byte-exact
example-value generator (objects built from their required fields incl. inherited
ones, unions/enums, containers, maps, datetimes, the `long` placeholder; ruff
snippet formatting at line length 88). The two package `__init__.py` aggregators
(`types/__init__.py`, package-root `__init__.py`), the generated `README.md`, and
the project-root
**scaffolding** (`pyproject.toml`, `requirements.txt`, `.fern/metadata.json`) all
match.

Non-Python matched files (the scaffolding) are Fern's verbatim output and compared
without comment stripping; `.py` files are still comment-stripped before the
comparison.

## Verifying the tool as a user runs it

Byte-matching proves *equality to Fern* on the specs Fern has generated. The e2e
also covers the journeys a user actually takes, independent of the golden
fixtures:

- **The generated SDK is valid Python.** `assert_valid_python` compiles the whole
  emitted tree with `python -m compileall` — for the `exhaustive` fixture and for
  an **arbitrary spec outside the corpus**. Byte-matching Fern cannot catch a
  generation bug on a spec Fern never saw; compiling can (it first caught an empty
  `from .errors import` emitted when a spec declares no errors). The check skips
  with a message when no Python interpreter is on `PATH` (same posture as the
  coverage tier); GitHub's ubuntu/macos/windows runners all ship one, so the gate
  always runs it.
- **The generated SDK behaves right at runtime — verified differentially against
  Fern.** Compiling proves the source is legal Python; it does not prove the
  *client* issues the right HTTP request or parses the response. Rather than
  hand-author the expected behavior, `crozier_matches_fern_runtime_behavior`
  *derives* it from Fern: the committed **pytest** suite
  [`tests/runtime/test_wire.py`](../tests/runtime/test_wire.py) records the
  client's behavior (via a shared recorder, `_recorder.py`) for **both** the
  committed Fern fixture SDK (`exhaustive/expected/src` — real, runnable Fern
  output) and the crozier-generated SDK, and a parametrized test asserts — per
  journey — that the recordings are **identical**. (Both SDKs are named `fern`, so
  each recording runs in its own subprocess.) The generated client accepts an
  `httpx_client`, so the recorder injects one whose `httpx.MockTransport` captures
  the outgoing request and returns a scripted response, recording per journey the
  request (method, URL, headers, serialized body) and the outcome (the response
  model dumped to a dict, or the typed error's class/status/body). Between them the
  journeys cover URL/method
  construction, bearer auth and SDK-identity header injection, request-body
  serialization (wire aliasing and `OMIT` filtering), query encoding, typed
  pydantic deserialization, and typed error raising, for the sync **and** async
  clients. The **only** allowed difference is the deliberate SDK-identity branding
  (`X-Crozier-*` vs `X-Fern-*`), which the recorder folds to a common prefix on
  both sides — the runtime analog of the byte-diff's `normalize_sdk_headers` — so
  any other divergence fails the test. This is the in-process analog of Fern's own
  wire tests (Fern runs a
  WireMock server in Docker and verifies the request via its admin API), but that
  `tests/wire/` tree is generated output gated behind an Enterprise
  `enable_wire_tests` flag none of the corpora set, so crozier does not emit it and
  reproduces the behavior without Docker. It runs in a cached venv holding the
  SDK's runtime deps (`httpx` + `pydantic`) plus `pytest`; like the validity check
  it skips when Python/venv/deps are unavailable, but is a **hard failure under
  `CI`** so the gate stays honest.
- **Default naming.** The common bare invocation (no `--package-name` /
  `--project-name`) is exercised: the package directory is `snake_case(title)` and
  `version.py` records the same name.
- **Idempotent regeneration.** Generating twice into the same `--output` prunes a
  module whose schema was dropped from the spec (crozier clears its own
  `src/<package>` tree first) and the result still compiles — no orphaned modules.
- **`--version`.** Asserted against the crate version, the same string the release
  smoke test checks against the published binary.

Each corpus commits Fern's *whole* `expected/` tree, not the subset crozier
happens to reproduce, so the comparison is over the complete output and a
regression has nowhere to hide.

## What generates today

Named `components.schemas` → the Python type layer:

- **Objects** — pydantic models with Fern's field conventions: required vs
  optional (`nullable` or absent from `required`), `= None` /
  `pydantic.Field(default=None)` / `pydantic.Field()` defaults driven by
  optionality and whether the field is documented, reserved-name aliasing via
  `typing_extensions.Annotated[T, FieldMetadata(alias="wire")]`, and class/field
  docstrings (backslash-escaped, indented).
- **String enums** — an OpenAPI string `enum` becomes a real enum class
  (`class Name(enum.StrEnum)`, over the SDK's own `core/enum.py`: stdlib
  `enum.StrEnum` on Python ≥ 3.11, a `(str, enum.Enum)` mixin below it): a
  `SCREAMING_SNAKE = "value"` member per value and a generated `visit(...)`
  dispatch method. This is Fern's opt-in `enum_type:
  python_enums` shape, which crozier targets and the whole golden corpus is generated
  against (issue #41 gap 2b) — *not* Fern's out-of-the-box open `Literal` union.
  Integer enums stay `Name = int` (`python_enums` does not affect them).
- **Aliases** — unions (`oneOf`/`anyOf`), maps (`type: object` +
  `additionalProperties`, no properties → `Dict[..]`), nullable scalars
  (`Optional[..]`), and unknown/untyped schemas (`Optional[Any]`).
- **Hoisted inline schemas** — a `oneOf` object variant becomes a named model
  `{Name}{Ordinal}` (`TypesAnimalZero`), an `allOf`'s `$ref` members become its
  base classes, and an inline enum property becomes a named `{Owner}{Prop}` type.

Type mapping follows Fern's OpenAPI importer: `format: uuid`/`byte` → `str`,
`date-time` → `dt.datetime`, `date` → `dt.date`, integer formats → `int`, etc.
Imports are emitted in Fern's exact two-group order (stdlib `import`s/`from`s,
then everything else). `version.py` and `py.typed` are complete.

**Core runtime.** The `core/` SDK runtime (HTTP client, pydantic utilities,
serialization, SSE) is generator boilerplate, not derived from the spec — Fern
ships the same `core/` files into every SDK. crozier vendors them under
`assets/core/` (Apache-2.0; see `NOTICE`) and emits them verbatim. The one
exception is `client_wrapper.py`, which Fern shapes from the auth model: crozier
generates it ([`emit::client_wrapper_file`](../src/emit.rs)) from the SDK
name/version, the auth scheme, and any promoted global headers, so it is not one
of the vendored assets.

**Line wrapping.** Fern runs `ruff format` (line length 120) over its output, so
crozier delegates the wrapping to the same tool. The emitters build each
statement on one line (a small [`Doc`](../src/wrap.rs) expression rendered flat),
and a post-pass ([`pyfmt`](../src/pyfmt.rs)) runs `ruff format` over the generated
`.py` files. `ruff` is therefore a **generation-time dependency**, invoked over
the CLI (not the unstable `ruff_python_formatter` library crates) and pinned in CI
to match Fern's fixtures (the version lives in `.ruff-version`, installed by
`scripts/install-ruff.sh`); its formatter output is byte-identical, on the shapes
crozier emits, across `0.11`–`0.15` (verified by running the e2e under both). The vendored `core/` runtime is left unformatted — it is already
Fern's own `ruff`-formatted source, and reformatting it does not commute with the
comment-strip comparison.

**Aggregator imports.** The lazy-loader `__init__.py` files (`types/`, `errors/`,
the package root) are formatted like any other file, but two artifacts are
normalized on both sides of the e2e comparison (see `try_normalize_init` in
`tests/e2e.rs`) rather than reproduced: their leading blank lines (a comment-strip
artifact of Fern's multi-line header that a one-line header plus `ruff`, which
caps module-top blanks at two, cannot reproduce), and the order of the
`if typing.TYPE_CHECKING:` import block. That block is never executed, so its
order is meaningless — Fern emits it in traversal order; crozier sorts it
straightforwardly and the e2e canonicalizes both sides with `ruff` isort. The
`_dynamic_imports` map and `__all__` (which *are* executed) stay alphabetical.

**Which parameter examples reach a worked call.** Fern keeps a *parameter-level*
`example`/`examples` only on a `type: string` parameter, and does so identically
for query, header and path parameters. Probed directly against Fern 5.20.0: an
integer or boolean example declared on the parameter never reaches the call, nor
does a string-*valued* example on an `integer` schema — the gate is the declared
type, not the example's JSON kind — and a required argument whose example was
discarded falls back to Fern's synthesized placeholder (`1`, `1.1`). A
*schema-level* example has no such restriction and is used whatever its type is,
so `page: {type: integer, example: 0}` renders `page=0` beside a string example
in the same call. One shape overrides all of it: an **optional** enum-typed query
parameter is never exampled, however its enum (inline or `$ref`) and its example
are declared, while a required one is rendered from the enum's first member.
`med-anvisa-price` and `sac-backend` pin the combination.

**Example snippets.** The worked examples in docstrings/`README`/`reference.md`
are laid out by hand (`Example::render`), *not* through `ruff format`, because
Fern's committed examples are not a `ruff` fixed point: `ruff` reformats a long
`await <call>(...)` by parenthesizing the awaited expression, while Fern leaves
the long `await …(` line and only explodes the call arguments. Reproducing Fern
here means matching Fern, not `ruff`.

## The 5.20.0 refresh and the rules it established

`exhaustive` and the other hand-authored feature-coverage goldens were
regenerated with `fernapi/fern-python-sdk:5.20.0` — the version the real-world
corpus already pins — and each records that exact generator in its
`expected/.crozier-fern-golden.json` provenance. Their trees had been pre-5.20
Fern output, so the great majority of the residual measured before that refresh
was **version skew**: one shared scaffold block (`src/*/core/*`, `client.py`, the
`__init__.py` aggregators, `pyproject.toml`, `README.md`, `reference.md`,
`requirements.txt`, `.fern/metadata.json`) repeated once per corpus, not a crozier
defect. Measuring against a mixed-version corpus is why the count looked large; a
provenanced golden per corpus is why it cannot happen again.

What remained after the refresh was genuine divergence, and it closed through
four rules:

1. **Abbreviated calls in `README.md`** use `(...)` whenever the demonstrated
   method takes any argument; argument-free methods use `()`.
2. **Malformed-node optionality** is idempotent: an already-optional unknown
   property is not wrapped in a second `typing.Optional`.
3. **SSE** uses Fern 5.20's `typing.Any` stream element and `parse_sse_obj`
   deserializer. Method docstrings retain their iteration examples, while
   README/reference usage uses a plain call; the README also carries Fern's
   dedicated `## Streaming` section.
4. **Root-level method examples** derive environment presence from the actual
   document, so a root client without environments includes Fern's required
   `base_url=` constructor argument.

The independent real-world divergence in **`letta`'s `reference.md`** had two
causes. Crozier documented a `$ref` request body that Fern ignores on a `GET`
operation, even though both generated clients already omitted it; reference
generation now consults the normalized request body before using its source-only
type. Crozier also omitted an optional header whose default Fern promoted to a
constant transport header; Fern still documents that input as
`storage_unit: typing.Literal` and counts it when choosing `(...)` for the
abbreviated signature. Both reference-only rules now match the 5.20 golden.

The refresh also **closed** two divergences it had first exposed, both in
`exhaustive`:

- **Unknown (`{}`) request-body requiredness.** Fern splits on the schema's
  `nullable`, not the document version: a bare `{}` body is a *required*
  `typing.Any`, and `{nullable: true}` is `typing.Optional[typing.Any] = None`.
  crozier had gated the required form to OpenAPI 3.1 documents — a rule fitted to
  the stale pre-5.20 `exhaustive` golden — which mistyped that 3.0.1 spec's
  `noAuth_postWithNoAuth`. `letta` declares both shapes and pins the rule.
- **Doc type spelling.** A `reference.md` entry's ` -> <type>` summary spells the
  datetime types in full (`datetime.datetime`), never the `dt.` alias the
  generated Python imports them under — the same prose spelling the parameter
  rows already used.

The per-corpus measurement lives in the `CORPORA`/`FEATURE_TARGETS` data in
`tests/e2e.rs`, the single source of truth; `just fixtures-gaps` re-measures it.
The configured `audience-filter`, `audience-filter-strict`, `client-class-name`,
`pydantic-extra-fields`, and `eos.local-extra-fields-forbid` fixtures are on
5.20.0 like the rest.
`query-parameters-openapi` is re-vendored from Fern's 5.20.0 release commit; its
seed-repository boundary and exact packaged-output expectations are documented
above. `calorieninjas.com` is the accepted exception described earlier: it has no
golden because 5.20.0 cannot emit valid Python for it, and its former tree had no
managed provenance, so retaining it would have made byte parity depend on
unidentified older Fern output. The items below record how each shape generates;
paths the corpus does not yet exercise are called out inline.

The first **real-world** corpus, `apideck.com-crm` (issue #77), matches
byte-for-byte too. As a `link-ok` entry its OpenAPI spec is
fetched, not vendored, so its `apideck_crm_matches_fern_output` test resolves the
spec from `.local/corpus` (`corpus_spec`), skips when it is absent (the offline
`check` gate), and enforces the match under `CROZIER_REQUIRE_CORPUS` in the CI
live-e2e leg (`just test-corpus-match`). Reaching it exercised, on a messy
real-world document, the `$ref` parameter/response resolution, Fern-matching method
naming, ubiquitous-header promotion, inline-schema hoisting, and worked-example
value synthesis (spec `example`s, shown only for a plain-scalar required-and-not-
nullable field, with an enum rendered as its member).

### The `bunq.com` real-world corpus (issue #77): the at-scale target, fully matched

The second real-world `link-ok` corpus, `bunq.com`, is deliberately an order of
magnitude larger than apideck — **421 endpoints, 617 component schemas, 110 tags**.
Fern generates it cleanly (`fern check`
passes) and crozier's SDK round-trips live against it (`bunq.com` in
`conftest.FIXTURES`; see the mock-side-skip note below). It is **fully
byte-matched**: `bunq_matches_fern_output` walks and locks in the whole golden.
Its guard
mirrors apideck's — skip when the fetched spec is absent, enforce under
`CROZIER_REQUIRE_CORPUS` in `just test-corpus-match`.

**Fixed while landing bunq** (each guarded so the apideck/exhaustive/feature corpora
stay byte-identical — none of them exercised these paths):

- **Tag-based sub-client grouping.** bunq tags every operation, but its operationIds
  are `SCREAMING_Mixed` strings that *contain underscores* (`CREATE_AttachmentPublic`,
  `List_all_Content_for_AttachmentPublic`). Fern groups by the **`tags`** array;
  crozier's old heuristic treated any `_` as a `group_method` prefix and grouped by
  the operationId, producing ~2.5× too many sub-clients. `endpoint_module`/
  `endpoint_method_name` (`src/ir.rs`) now group by the tag unless the operationId
  prefix *is* the tag (`inlinedRequests_post…` under `InlinedRequests` — the case the
  synthetic seeds hit, where both rules agree). This was the bulk of the gap.
- **Latin accents fold in an enum member and vanish from a property.** Fern's two
  naming paths disagree with each other over the same word, and
  `med-anvisa-price` pins both halves from one document: the enum path folds a
  Latin accent to its base ASCII letter (`SUBSTÂNCIA` → the member `SUBSTANCIA`,
  `LABORATÓRIO` → `LABORATORIO`), while the property path treats it as a word
  separator (`laborat_rio`, aliased back to `LABORATÓRIO`); `sac-backend`
  witnesses the property half again in another language (`tamaño` → `tama_o`).
  [`naming::deburr`] therefore runs on the enum path only, over Latin-1
  Supplement and Latin Extended-A. Latin-1 is the *only* non-ASCII case worth
  encoding: Fern refuses a non-ASCII schema name or enum value outright and emits
  invalid Python for a non-ASCII property or parameter name — see
  [`fern-limitations.md`](fern-limitations.md).
- **Whitespace is a hard boundary for the property digit collapse.** The collapse
  that joins `day_0_end_time` → `day0end_time` and `user_fields[1]` →
  `user_fields1` never reaches across a space, so `EAN 1` stays `ean_1` and
  `PF 17,5% ALC` becomes `pf_175_alc` — the comma-separated digits still collapse
  *inside* one whitespace-delimited chunk. [`naming::field_name`] chunks on
  whitespace before collapsing; a name without whitespace is one chunk and folds
  exactly as it always did.
- **Global-header order + `User-Agent`.** Fern lists promoted headers optional-first
  (optionals in spec order, requireds by field name) and never promotes the
  transport-managed `User-Agent`; crozier sorted alphabetically and promoted it.
- **Property-less object → `Dict` alias.** A bare `type: object` with no properties is
  aliased to `typing.Dict[str, typing.Optional[typing.Any]]` (`is_bare_object`), not an
  empty model class.
- **Path-param empty-description docstrings.** A path param whose spec declares an
  *empty* `description` (bunq's `itemId: {description: ""}`) renders a blank docstring
  slot; one that omits `description` entirely (the seeds) renders none — the two now
  differ ([`ir::declared_doc`]/[`emit::push_path_param`]). The `reference.md` param
  table mirrors this: a declared (even empty) description gets the ` — ` separator,
  an omitted one the bare space.
- **Untyped error-body type + hoisted `{Error}Body` model.** A `$ref`-to-
  `components.responses` error whose body is an inline object (bunq's `GenericError`)
  types the *exception* body `typing.Optional[typing.Any]`, matching Fern; separately
  Fern hoists that inline body into a package-root `{ErrorClassName}Body` model
  (`BadRequestErrorBody`), emitted and re-exported through the `types/` aggregators
  though the exception never references it (`hoist_error_body_types`).
- **`content-type` header rule.** Fern emits
  `headers={"content-type": "application/json"}` iff the operation has a path/header
  param, an *undocumented* body, or a body whose fields are *all required*. bunq's
  `CREATE_Avatar` and `CREATE_SessionServer` share one header-parameter list, every
  entry of which promotes to the client wrapper, so the body decides: `Avatar`'s four
  properties declare no `required` and it gets no header, while `SessionServer`'s one
  `secret` property is `required` and it does.
- **Inline-schema hoisting + snake-case digits.** A top-level array of inline objects
  hoists its element to `{Name}Item`; a snake-cased word ending in a digit merges with
  the following segment (`Cvc2Create` → `cvc2create`, not `cvc2_create`) while a
  digit-led boundary (`2Factor` → `2_factor`) is preserved.
- **Forward references, verbatim descriptions, templated servers.** Cyclic types emit
  `update_forward_refs`; a request field's description is preserved byte-for-byte
  (no trim); a `servers` entry with URL variables resolves the variable defaults
  into the base URL (its environment member is named by the description rule
  below, which the URL shape does not enter into).
- **`reference.md` section titles + doc-snippet wrapping.** A section's `## ` title is
  the tag verbatim when the operationId carries an underscore separator (bunq's
  `attachment-public`), else the PascalCase tag (`Widgets`, `Companies`) or, untagged,
  the PascalCase operationId group (`EndpointsContainer`) — `module_title`. The root
  `client.py` wraps a lazy sub-client import into ruff's parenthesized, trailing-comma
  form past 107 columns (ruff won't split a single-name import itself); the `README.md`
  worked-example calls and their tag imports are laid out at Fern's 80-column example
  width ([`emit::Example::render_at`]), not the project `line-length` of 120 — the
  abbreviated error-handling snippets use ruff's 88 instead.

**Mock-side live-e2e skips.** Driving 421 endpoints through Prism surfaced 28
endpoints the *mock* — not the SDK — cannot honor: 20 crash Prism's json-schema-faker
response generator (a 5xx), and 8 return a body that omits a field its own response
schema marks `required`. Both are provable mock failures independent of the client
(Fern's own SDK would hit them identically), so `_driver._mock_side_reason`
classifies them as **skips**, not gate failures — every other failure still gates.
The byte-diff gate independently proves the affected models' required/optional shape,
so a skip can never mask a crozier defect. See `tests/live_e2e/AGENTS.md`.

### The `bungie.net` real-world corpus (issue #77): schema-heavy target, fully matched

The third real-world `link-ok` corpus, `bungie.net`, is the schema-layer-heavy
counterpart to endpoint-heavy bunq: **869 component schemas across only 13 tags**.
Fern generates it cleanly (`fern check`
passes) and crozier consumes it without error, so it is a valid byte-match target.
It is **fully byte-matched**: `bungie_matches_fern_output` locks in the entire
golden by walking it.
Its guard mirrors apideck's and bunq's — skip when the fetched spec is absent, enforce
under `CROZIER_REQUIRE_CORPUS` in `just test-corpus-match`.

**Fixed while landing bungie** (each guarded so the apideck/bunq/exhaustive/feature
corpora stay byte-identical — none of them exercised these paths):

1. **Operation grouping for dotted corpus APIs** (`src/ir.rs`) — operations Fern
   groups under its empty `_` namespace (an operationId such as `.GetAvailableLocales`)
   are now emitted, flattened onto the package root as `src/fern/raw_client.py` plus
   the root `client.py` methods ([`emit`]'s `empty_endpoint_namespace`), and wired into
   the `__init__` exports; crozier previously omitted that group entirely.
2. **Named per-operation response types** (`src/ir.rs`, `src/emit.rs`,
   `src/openapi.rs`) — Fern synthesizes a `<OperationId>Response` type from each
   operation's inline response body (Bungie's standard
   `{ Response, ErrorCode, ThrottleSeconds, Message, … }` envelope, which is the
   bulk of its `*_response.py` modules). crozier now hoists and names them
   identically, with their `types/__init__.py` lazy-import entries and the client
   return-type wiring that references them.
3. **README examples for no-body operations** (`src/emit.rs`) — matched Fern's
   rendering of the example calls.

Future Bungie source changes or Fern upgrades follow the standard
[`Fern golden lifecycle`](fern-goldens.md).

### Five more real-world corpora (issue #77): the harder batch

Beyond the three corpora above, five more `link-ok` corpora were added
together as a batch of deliberately harder, feature-diverse targets. All five pass
`fern check` (the prerequisite — Fern must accept the raw spec, and the largest raw
public specs do not: `github.com`, `box.com`, and `atlassian.com-jira` each fail its
gate, and `conjur.local` hits a ref-resolution error, so all four are out). Each
`Corpus` is registered in `tests/e2e.rs` with the usual `link-ok` guard, so the
offline `check` gate skips unfetched specs while
`just test-corpus-match` enforces them. All five now match byte-for-byte.

| corpus | shape it stresses |
|---|---|
| `anchore.io` | largest clean schema surface (149 schemas), heavy `allOf` + enums |
| `apache.org` (Airflow) | heaviest composition (`allOf`×22) + the only discriminated union; 18 tags |
| `discourse.local` | all-inline (0 named schemas → ~113 coined types) |
| `appwrite.io-server` | widest operation surface (95 ops); `url` format |
| `apicurio.local-registry` | the batch's only `int64`-format corpus; `allOf` |

Two rules closed the batch. Header `apiKey` security schemes past the first become
SDK-wide constructor fields, and an api-key header that *also* rides operations as
an explicit parameter is promoted once, not twice — crozier drops it from the
ordinary header set and appends the scheme-derived field, preserving Fern's
grouping of ordinary headers before security headers ([`ir::global_headers`]).
`appwrite.io-server` is the batch corpus that pins it: its four header `apiKey`
schemes (`X-Appwrite-JWT`, `-Key`, `-Locale`, `-Project`) yield the constructor's
`api_key` plus `appwrite_key`/`appwrite_locale`/`appwrite_project`. And an `x-*`
key under `paths` is a vendor extension, not a path item:
the `paths` deserializer skips it rather than trying to parse
`apicurio.local-registry`'s `x-codegen-contextRoot` as a route. Future fixture
refreshes use the standard [`Fern golden lifecycle`](fern-goldens.md).

### Issue #43: error responses, discriminated-union aliases, and SSE streaming

Three gaps found while checking whether crozier could stand in for a fern-python
SDK. All three are closed byte-for-byte against Fern goldens.

1. **Operations that declared any non-2xx response were silently dropped**
   (`error-responses`, gap #1 — the serious one). crozier emitted the response
   *type* but no client method and wired nothing into the root client, reporting a
   successful generation of an SDK with no way to call the API — every FastAPI-style
   spec (a `422` on every operation) lost every endpoint. The cause was
   [`ir::resolve_errors`] returning "unemittable" whenever an error status was
   unmapped or its body was not an `application/json` `$ref`. Now an error response
   **never** gates method generation: [`ir::error_class_name`] maps every standard
   4xx/5xx status to Fern's typed exception (`404` → `NotFoundError`, `500` →
   `InternalServerError`, …), an unmapped status (a non-standard `460`) is skipped so
   the operation falls through to the generic `ApiError` (exactly as Fern does), and
   the body parses per declared shape — a `$ref` (`Error`), a container
   (`typing.List[str]`), or `typing.Optional[typing.Any]` for a content-less error.
   Inline object error bodies are hoisted separately to package-root
   `types/{ClassName}Body` models and re-exported through the type aggregators.
   The exception keeps the body spelling Fern selects: a direct inline response
   uses the named model, while a `$ref` to `components.responses` whose body is
   inline remains `typing.Optional[typing.Any]` even though the separate body
   model is emitted. Bodies shared by a status are merged before hoisting so the
   root model is deterministic. The real-world `buildrelay` corpus pins the direct
   inline case at Fern 5.20.0. Its first measured run diverged in
   `README.md`, `reference.md`, the root client and environment modules, and—most
   importantly—the `InternalServerError` and jobs raw-client modules where crozier
   used `typing.Any`. Direct inline responses now type both sites as
   `InternalServerErrorBody`; the neighbouring `$ref`-to-`components.responses`
   behavior remains unchanged.
2. **Discriminated-union alias annotation** (gap #2) is **now closed** (issue #50
   part 2). Fern wraps the alias in
   `typing_extensions.Annotated[Union[...], pydantic.Field(discriminator="…")]` so
   pydantic can dispatch on the tag; a plain `Shape = typing.Union[...]` cannot.
   This landed in `fern-python-sdk` 4.35.0, so the corpus was bumped 4.34.0 → 4.35.0
   to pin it — a deliberately **minimal** bump: 4.35.0's only output change over
   4.34.0 is this annotation (the `exhaustive` tree of the day differed by only
   the `.fern/metadata.json` version string), so no other generator work was needed.
   [`emit::render_discriminated_union`] now emits the annotated alias.
3. **SSE streaming operations were reduced to a `-> None` method** that discarded
   the stream (`sse-streaming`, gap #3). A `text/event-stream` 2xx response now
   ([`ir::is_streaming`]) generates Fern's context-managed streaming shape: the raw
   client is a `@contextlib.(async)contextmanager` over `httpx_client.stream(...)`
   that decodes events through the vendored `core/http_sse` runtime
   (`EventSource.iter_sse`/`aiter_sse`) into
   `typing.(Async)Iterator[typing.Any]` chunks, and the high-level
   client yields each chunk with a worked streaming `Examples` block. The chunk stays
   untyped: Fern's OpenAPI importer does not resolve the `x-fern-streaming`
   `chunk-schema-ref` (the same limitation as the OAuth extension), so crozier keys
   off the content type alone. Fern 5.20 deserializes the untyped chunk through
   `parse_sse_obj`; its README/reference snippets show a plain call, while generated
   method docstrings retain the worked iteration loop and the README retains a
   separate `## Streaming` section.

The generated **README/reference** pick the first endpoint with a request body
for the worked example and abbreviate the error-handling/advanced snippets,
ruff-wrapped at the 88-col snippet width. At 5.20 the abbreviation is purely
arity-driven — `(...)` whenever the demonstrated method takes any argument, `()`
only for an argument-free method — which is refresh rule 1 above; the earlier
body-shape-driven rule was fitted to pre-5.20 goldens. Each shape has a
hand-authored **feature-coverage
target** under `tests/fixtures/` (a `FEATURE_TARGETS` corpus in `tests/e2e.rs`),
with the full Fern `expected/` tree committed and compared in its entirety; the
smoke test additionally asserts crozier consumes every spec without panicking. To
reproduce the
current output for a target (Fern generated these with the scaffold defaults):

```
cargo build --release
target/release/crozier generate \
  --spec tests/fixtures/<fixture>/openapi.yml \
  --output /tmp/<fixture> --package-name fern --project-name default_package_name
```

### Issues #84–#86: recursive schemas and malformed nodes

Three shapes that made crozier emit broken code — or crash — where Fern tolerates
the document. Each has a hand-authored feature-coverage target with the full Fern
`expected/` tree committed.

1. **Recursive schemas** (`recursive-types`, issue #84). A self-referential model
   (`TreeNode` containing a list of itself) emitted `from .tree_node import
   TreeNode` — a module importing the name it defines (a circular import at load) —
   and a recursive discriminated union overflowed the generator's stack. Both are
   fixed the way Fern does it: a type that closes a reference cycle back to itself
   renders the cyclic field as a **string forward reference** under `from __future__
   import annotations`, and the model is repaired at load time with
   `update_forward_refs`. A same-file cycle (a self-reference, or a variant
   referencing its own union alias) needs no import; a cross-module cycle (the
   `$ref`-variant schema `AndNode.children: List["Node"]`) **defers** its import to
   after the class body so it does not fire mid-load. The cycle set is computed by
   [`emit::forward_ref_map`] over the type-reference graph (a discriminated union
   contributes an edge to each of its mapped variant schemas, so a variant that
   recurses through the union is seen). Example synthesis, which walks the same
   graph for the README/reference, terminates a recursive list at `[]` rather than
   recursing forever ([`emit`]'s example cycle guard). Discriminated-union wrappers
   are now named after the discriminant **value** (`Node_And`), matching Fern —
   previously the referenced schema name (`Node_AndNode`) when the two differed.
   The hand-authored corpus **matches in full** at 5.20, but its variants are
   referenced and explicitly mapped, so the golden refresh did not cover the
   documented inline-variant residual. The real-world `tlon-notes` corpus now
   closes that coverage gap: `ImportNode` is a recursive `oneOf` whose two
   variants are inline, untitled, and unmapped. Fern names those variants from
   the last distinguishing property (`ImportNodeChildren` and `ImportNodeBody`);
   crozier applies that inference only when an inline union closes a reference
   cycle, preserving the established first-distinguishing-property rule for
   acyclic unions. Its recursive alias, deferred imports, and transitive
   `update_forward_refs` calls now match Fern 5.20 byte-for-byte. The same corpus
   also proves singleton-value inference for four inline discriminated unions.
2. **Nested-type `core` import depth** (`nested-core-imports`, issue #85). A
   per-operation hoisted type at `{pkg}/{tag}/types/…` reached `core.serialization`
   with a hardcoded `..core` — correct only at the root nesting level, a
   `ModuleNotFoundError` one level deeper. Every `core.*` import now routes through
   [`emit::Imports::add_core`], which picks the dot count from the file's actual
   package depth (`...core` for a tag's `types/`), matching the depth already used
   for `core.pydantic_utilities`.
3. **JSON-array property node** (`malformed-property-schema`, issue #86). A
   `required: [..]` list misplaced *inside* `properties` reads as a property whose
   value is a JSON array; serde's derived struct deserialization filled `Schema`
   fields positionally from that array, turning the first element into a bogus
   `$ref` and emitting a dangling type import. The `properties` deserializer now
   degrades any non-object value to a `malformed` unknown node
   ([`openapi`]'s `de_properties`), matching Fern's tolerance of the same document.
   Optionality on that node is idempotent (refresh rule 2): the degraded property
   renders as a plain `typing.Optional[typing.Any]` field rather than wrapping an
   already-optional unknown a second time
   (`typing.Optional[typing.Optional[typing.Any]]`). The request-body counterpart
   is the unknown-body requiredness rule above.

### Adding a new target's golden tree

Add the target as one numbered `CORPUS.md` row and a `Corpus` with
`unmatched: &[]`, wire its `#[test]` and its `just test-corpus-match` line, then
dispatch **Fern goldens** for its source URL. The first red comparison is the
generator work to land next; `just fixtures-gaps` measures exactly which files
diverge. The corpus joins at full parity or not at all — `unmatched` is a
staging area for work in flight, never a place to park a known divergence.
See the complete [`Fern golden lifecycle`](fern-goldens.md). This is
the maintained successor to the manual Docker process used for earlier targets
such as `basic-auth`, `oauth-client-credentials`, `inline-array-request`, and
`writeonly-fields`.

1. **Auth models beyond bearer** (`auth-schemes`, partially implemented).
   `components.securitySchemes` plus each operation's `security` now feed an
   [`ir::Auth`] model: the first declared scheme selects the credential, and it is
   *required* when every operation is authenticated (else optional, e.g. exhaustive's
   `noauth`). `client_wrapper.py` is generated from it — api-key (`api_key: str` +
   the scheme's header) and bearer (`token`, required/optional) both match across the
   fixtures, and the bearer-optional form stays byte-identical to Fern's default. The
   auth model is also threaded through the root `client.py` (constructor param, the
   docstring `Parameters` line, and the `Examples` instantiation) and every worked
   `Examples` snippet (per-tag `client.py`, README, reference), so `auth-schemes`
   matches in full under api-key. **HTTP `basic`**
   is now a first-class primary ([`ir::Auth::Basic`]): a required `username`/
   `password` pair (each `str` or callable), the `httpx.BasicAuth(...)._auth_header`
   header wiring, and both credentials threaded through the wrapper, root/per-tag
   clients, and worked examples — `basic-auth` matches in full. **OAuth2** as a
   plain-OpenAPI primary (no `x-fern-*` extensions) produces output identical to the
   optional-bearer fallback, which `oauth-client-credentials` pins in full; a
   token-provider wrapper would need Fern's OAuth extensions, which the OpenAPI
   document does not carry. Basic **is** split on `required` by the corpus: five
   goldens emit the optional primary — `apache.org`, `apache.org-airflow`,
   `http-toolkit`, `maif.local-otoroshi`, and `worldcoin-signup-sequencer`, each
   with `username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] =
   None` in `expected/src/fern/core/client_wrapper.py` — against ten that emit
   the required pair, so both branches are pinned. Two of those ten declare no
   operation Fern can see, and they are what pins the fallback
   [`ir::all_operations_authenticated`] takes when there is none: with no
   operation left to call the API unauthenticated, the credential stays required
   unless the document's own `security` says otherwise. `cyberark-conjur-api`
   reaches it with a root `security` naming its schemes; `adyen-report-notification`
   reaches it with no `security` at all — a webhook-only 3.1 document that omits
   `paths` entirely — and Fern requires the pair for both. A `webhooks` Path Item
   is deliberately *not* an operation for that question: `tamoss` declares
   `security: [{}]` on all eight of its webhooks beside authenticated `paths`, and
   its golden still emits the required pair, so a webhook's own security never
   reaches Fern's auth model. Still unexercised: an
   *optional* **api-key** primary. Every api-key golden declares it required
   (`api_key: str`), so the optional branch in [`emit::auth_wrapper_parts`]
   (`api_key: typing.Optional[str] = None` plus the `if self.api_key is not None:`
   header guard) is reached by no golden. Getting there needs a document that
   declares a root `security` with only empty requirements *and* leaves an
   operation unauthenticated — a header api-key with no root `security` at all
   stays required ([`ir::auth_model`], unit-tested by
   `header_api_key_without_root_security_is_still_required`) — so confirm the
   branch when such a fixture lands.
2. **Broader example coverage.** The example-value generator is proven against the
   corpus (objects, unions, enums, containers, maps, datetimes, a required `date`
   via `writeonly-fields`, `long`) and constructs hoisted tag-scoped element types
   (importing them `from <pkg>.<tag>`, e.g. `inline-array-request`'s
   `ItemsCreateBatchRequestItem`). Shapes the corpus still lacks — e.g. a
   nameless-slot enum — carry plausible-but-unverified placeholders; confirm them as
   new fixtures land.
   *Integer enums* now generate: a `type: integer` enum becomes a plain `Name = int`
   alias (Fern does not build a `Literal` union for them), and a `$ref` integer-enum
   request body is emittable (`json=request` + content-type header, like a string
   enum) — so `integer-enums` matches its whole tree, including the `enums`
   module, root client, README, and reference.
3. **Fern's `TYPE_CHECKING` order** in `types/__init__.py` is *not* reproduced,
   and no golden pins it. crozier sorts the block alphabetically
   ([`emit::types_init_file`]) while Fern emits it in endpoint-traversal order;
   the e2e canonicalizes every `__init__.py` on **both** sides with `ruff` isort
   before comparing (`tests/e2e.rs::try_normalize_init`), as [How the comparison
   works](#how-the-comparison-works) describes. The block is never executed, so
   its order is unobservable and no traversal derivation is owed — a spec with a
   different type-namespace layout cannot regress here.
4. **Request/response inline-schema hoisting (implemented).** A component schema
   used *only* as an inlined (plain-object `$ref`) request body is not emitted as a
   standalone type — Fern inlines its fields onto the request method and drops the
   type (`auth-schemes`' `TokenRequest`, `schema-constraints`' `CreateAccountRequest`,
   `servers-webhooks`' `CreateSubscriptionRequest`). An *inline* (non-`$ref`)
   request/response object body is hoisted into a named model in the **tag's own
   `types/` package** (Fern's `inlined/types/`): a response becomes
   `{Ctx}Response`, a request's nested inline objects `{Ctx}Request{Prop}`, and
   nested inline objects recurse as `{Parent}{Prop}` — structural names derived from
   the operation and property path, ignoring any `title`. `{Ctx}` is the PascalCase
   operationId alone ([`ir::endpoint_pascal_context`]), never the tag, so
   `inlined_search` yields `InlinedSearchResponse` and `InlinedSearchRequestFilter`.
   An [`ir::InlineHoister`] builds these tag-scoped types; a
   location-aware import resolver (`RefLoc`) picks the right relative path from any
   file, and the tag package/`types` package/root `__init__` re-export them.
   `inline-request-response` matches in full. An **inline array body** hoists its
   *element* the same way, as `{Ctx}RequestItem`
   (`inline-array-request`'s `ItemsCreateBatchRequestItem`), so the argument is
   `Sequence[{Ctx}Item]` through the convert wrapper and the worked example
   constructs it, importing it `from <pkg>.<tag>`; the hoisted-type method segment
   preserves the operationId's camelCase ([`ir::endpoint_pascal_context`]:
   `items_createBatch` → `ItemsCreateBatch`, distinct from the lowercased Python
   method).
5. **Cookie parameters + global-header promotion (implemented).** A `cookie` param
   (`ParameterLocation::Cookie`) is dropped from the method signature entirely, and
   an **optional** operation header is promoted to a client-wrapper-level "global"
   field (Fern lifts `X-Tenant` → a `tenant` field set once at construction, wired
   through `client_wrapper.py`, the root client, and the worked examples). The
   promotion heuristic is evidence-based: across the corpus the only two operation
   headers split exactly on `required` — `cookie-parameters`' optional `X-Tenant`
   promotes, `exhaustive`'s required `X-TEST-ENDPOINT-HEADER` stays per-method — so
   crozier promotes a header that is optional in every operation it appears in
   ([`ir::global_headers`]). `cookie-parameters` matches in full.
6. **Form request bodies (implemented).** `multipart/form-data` splits its fields
   into `data={...}` (non-file) and `files={...}` (`format: binary` → `core.File`)
   with `force_multipart=True`; `application/x-www-form-urlencoded` sends all fields
   via `data={...}` with the form content-type header. `form-bodies` matches in full
   (the reference table reproduces Fern's `core.File` `from __future__` artifact).
7. **Discriminated unions (implemented).** A `oneOf`/`anyOf` with a `discriminator`
   (`propertyName` + `mapping`) becomes Fern's `{Union}_{Variant}` wrapper models —
   each carrying the discriminant as a `typing.Literal[..]` field plus the referenced
   model's other fields — over a `{Union} = typing_extensions.Annotated[typing.Union[..],
   pydantic.Field(discriminator="…")]` alias (issue #50 part 2), and the
   discriminant property is stripped from each member's own model.
   `discriminated-unions` matches in full.
   A discriminator without an explicit `mapping` is inferred when every variant
   exposes a common singleton string value; otherwise it falls back to a plain
   union.
8. **Schema annotations and constraints** (`schema-constraints`).
   Fern ignores the validation keywords (`minLength`/`pattern`/`minimum`/`maxItems`/
   …), `default`, and `deprecated` in its generated models, so crozier does too;
   a `readOnly` property is now rendered optional even when `required` (it is
   server-populated), and `additionalProperties: true` maps to
   `Dict[str, Optional[Any]]`. `schema-constraints` matches in full. When one schema is used as
   *both* request body and response, Fern orders the inlined request signature and
   docstring **required-first** (optional `= OMIT` args last, a stable partition that
   preserves schema order within each group) while the `json={...}` dict keeps pure
   schema order — so a required `readOnly`/`writeOnly` field lands after the plain
   required ones. `writeonly-fields` pins this and matches in full. Not yet
   exercised: dropping a
   `writeOnly`-only field from the *response* representation (Fern keeps it here).
9. **Document-level `servers` and `webhooks` (implemented); `callbacks`
   (ignored).**
   When the document declares `servers`, crozier emits `environment.py` (an
   `enum.Enum` of environments) and threads an `environment` / optional-`base_url`
   through the root client, resolving the base URL via a generated `_get_base_url`
   and dropping the hardcoded `base_url` from the worked examples. Fern's OpenAPI
   importer emits a **single** environment member — the first server only (the
   "2 servers → only `PRODUCTION`" oddity) — and names it `DEFAULT` unless that
   server's description is, whole and case-insensitively, one of the two
   environment names Fern recognizes: `production` or `sandbox`. Probed directly
   against Fern 5.20.0 over one-server documents: `Prod`, `Staging`, `Live`,
   `Test`, `Development`, `Production API`, `Production server` and
   `Servidor de desarrollo local` are all `DEFAULT`, while `Production` stays
   `PRODUCTION` even on a templated or root-relative URL. [`ir::Environment`]
   reproduces that. OpenAPI 3.1 **`webhooks`** are modeled
   ([`openapi::OpenApi::webhooks`], an ordered map of `PathItem`) and consumed
   twice: [`ir::build`] hoists a named payload type from every webhook
   operation's *inline* `application/json` request body (`{METHOD}_{event}_payload`
   through [`naming::class_name`], `/` in the event name becoming `_`), and
   [`ir::document_discriminant_strips`] walks `paths` and `webhooks` alike. A
   `$ref` body is skipped — the referenced component is already a named type — so
   `servers-webhooks`, whose one webhook body `$ref`s `Event`, takes that
   early-continue path and pins nothing here. The real-world `tamoss` corpus is
   what pins it: its eight inline webhook bodies (`flows/created`,
   `flows/updated`, `flows/deleted`, `flows/segments_added`,
   `flows/segments_deleted`, `sources/created`, `sources/updated`,
   `sources/deleted`) produce `PostFlowsCreatedPayload`,
   `PostSourcesCreatedPayload`, `PostFlowsSegmentsAddedPayloadEvent` and their
   siblings under `tests/fixtures/tamoss/expected/src/fern/types/`. **`callbacks`**
   remain genuinely absent from the serde model and are ignored. `servers-webhooks`
   matches in full regardless.
   The three documents 3.1's minimum-content rule allows but 3.0 does not are each
   pinned by a corpus row, and all three generate an **endpoint-free** SDK: a
   client with no methods over whatever component types the document names.
   `adyen-report-notification` (row 100) omits `paths` outright and declares one
   webhook; `adyen-managed-risk-notification` (row 101) omits it and declares
   eight, the webhook-only shape standing alone; `go-kratos-casbin-admin`
   (row 102) declares `paths: {}` beside `components.schemas: {}` and an empty
   `info.title`, which Fern packages as `default_package_name` with no types at
   all. A webhook's *component* schemas still become types — Fern imports the
   `$ref`ed models even though no method sends them — which is why the two Adyen
   goldens carry a populated `types/` module and the go-kratos one carries none.
5. **The endpoint layer (implemented — kept as a reference of the covered
   shapes).** `paths` are read into an operation IR
   ([`ir::Endpoint`]): module, method name, HTTP method, URL, path params, and
   the success response type. crozier emits each client's package marker
   (`<tag>/__init__.py`) and the per-tag `raw_client.py` for the subset it fully
   supports today — operations with only path and query parameters, a single JSON
   2xx response (a named model or a scalar), and either no request body or a
   supported one: a `$ref` to a named string enum (`json=request` plus the
   `content-type` header) or a bare scalar (`json=request`, no header; the
   `uuid`/`byte` formats are excluded pending Fern's content-type nuance). Query
   parameters render as keyword-only optional arguments and a `params={...}` entry
   (`endpoints_pagination`); enum bodies as a `request` argument (`endpoints_enum`);
   union bodies through the `convert_and_respect_annotation_metadata` wrapper
   (`endpoints_union`); header params as keyword-only arguments and a `headers={...}`
   entry (`str(x) if x is not None else None`, the `X-` prefix dropped from the
   Python name), which also force the `content-type` header on when they accompany
   a body (`reqwithheaders`). A 2xx response with no content returns `None`. A whole
   module is emitted only when every one of its operations is in that subset
   (`Endpoint::emittable`), so output stays honest as coverage widens. Scalar
   bodies cover every JSON primitive, with `uuid`/`byte` rendered as `str` but
   carrying the content-type header (`endpoints_primitive`). A plain-object `$ref`
   body is *inlined* field-by-field (`endpoints_object`, `endpoints_http_methods`,
   `endpoints_content_type`): every field becomes a keyword-only `= OMIT` argument,
   the call sends `json={...}` mapping wire names to args, request-context
   collections render as `typing.Sequence` (vs `typing.List` in responses),
   reserved names are munged (`long_`, `bool_`, `set_`), object/union-valued fields
   serialize through `convert_and_respect_annotation_metadata`, and a path param
   colliding with a body field is suffixed with `_`. A `$ref` map body passes
   straight through (`json=request`); an inline array of objects goes through the
   convert wrapper with no content-type header. Container bodies (lists/sets/maps
   of primitives or objects) and inline/`$ref`/unknown/`octet-stream` bodies are
   covered, as are declared 4xx responses (each raising a generated `errors/`
   exception) and mixed path/query/body operations. **Every raw client, every
   high-level per-tag `client.py`, and the root `client.py` now match** — the
   per-tag wrappers return `_response.data` and carry a worked `Examples` docstring
   from a byte-exact example-value generator, and the root `FernApi`/`AsyncFernApi`
   aggregates the tag clients under bearer auth. The package `__init__.py`
   aggregators and the generated docs (`README.md`, `reference.md`) all match too,
   so the endpoint layer — and the whole `exhaustive` corpus — is complete. Item 4
   above (inline request/response hoisting) generalized it beyond these shapes.

## Real-world-spec robustness (issue #40)

The other corpora are hand-authored to have clean, Fern-style `group_method`
operationIds and property names. Real vendor specs are messier, and four shapes
that used to make crozier emit invalid Python or hard-error now generate legal —
and byte-matched — output. Each has its own feature-coverage
corpus (`digit-leading-property`, `operation-id-non-identifier`,
`bracketed-property-names`, `missing-operation-id`), registered in `tests/e2e.rs`.

- **Digit-leading property name** (`2fa_enabled`). [`naming::field_name`] prefixes
  `f_` when the snake-cased name would start with a digit, and the wire name is
  preserved as a `FieldMetadata` alias — byte-for-byte Fern's `f_2fa_enabled`
  (`digit-leading-property/expected/.../types/thing.py`).

- **Non-identifier `operationId`** (`get-all-widgets`, `verify code`).
  [`naming::sanitize_identifier`] coerces any non-`[A-Za-z0-9_]` character in a
  name derived from an operationId to `_`; legal names (every other fixture) pass
  through untouched. The method names snake-case to `get_all_widgets`/`verify_code`
  and the inline response hoists to `VerifyCodeResponse`, matching Fern.

- **Non-identifier property name** (`filter[name]`, `page[size]`). The bracketed
  JSON:API / Rails / Stripe convention for nested form and query params isn't a
  valid Python identifier; crozier once emitted it verbatim as a function
  parameter, producing source `ruff format` refuses to parse (issue #74).
  [`naming::field_name`] now folds every non-alphanumeric run to a word boundary
  before snake-casing (`filter[name]` → `filter_name`, `page[size]` →
  `page_size`), while the raw bracketed name rides along as the wire
  serialization key (`needs_alias` fires) — byte-for-byte Fern's parameters and
  `data`/`params` dict keys. `bracketed-property-names` matches in full, including
  its raw and high-level `widgets` clients.

- **Missing `operationId`** (optional in OpenAPI). Instead of hard-erroring,
  [`ir::endpoint_method_name`] falls back to the operation's `summary`, run
  through [`naming::prose_identifier`] (`List widgets` → `list_widgets`) — which
  is what the corpus pins, byte-for-byte against Fern. With no summary either,
  [`ir::synthesized_method_name`] joins the HTTP method and the full route,
  brace-stripped (`GET /widgets` → `get_widgets`, `GET /widgets/{id}` →
  `get_widgets_id`).

### Tag-based client grouping

Closing the last two required grouping operations by **tag**, as Fern does. Fern's
rule — reproduced in [`ir::endpoint_module`] — is: a `group_method` operationId
names its own client from the prefix (`endpoints_container`, `inlinedrequests`) and
the `tags` are ignored; a groupless operationId (or one with none) is grouped by
its first tag instead (`get-all-widgets`/`verify code`/`GET /widgets` under tag
`widgets` → the `widgets` client). The hoisted-type context comes from the
operationId alone ([`ir::endpoint_pascal_context`]), never the tag, so a tag-grouped
inline response stays `VerifyCodeResponse`, not `WidgetsVerifyCodeResponse`.

### No-auth parity

These specs declare **no security scheme**, so they exercise crozier's
unauthenticated client. [`ir::auth_model`] now returns [`ir::Auth::None`] for such a
document (rather than defaulting to an optional bearer token), and the client
wrapper, root client, and per-tag clients drop every credential parameter and the
`Authorization` header — byte-matching Fern's credential-free clients. The whole
SDK-code layer of all four corpora matches: the types, the tag-grouped raw and
high-level clients, the root client, and the aggregators.

### crozier vs Fern SDK-identity headers

crozier does not impersonate Fern in the generated SDK: it emits `X-Crozier-Language`
/ `X-Crozier-SDK-Name` / `X-Crozier-SDK-Version` where Fern emits `X-Fern-*`. It also
reproduces Fern's *packaged* client wrapper, so it always emits the
`SDK-Name`/`SDK-Version` headers that Fern's publishing metadata supplies — which the
credential-free local golden trees (below) omit. Both are deliberate,
non-behavioral differences in tool branding/packaging, so
`tests/e2e.rs::normalize_sdk_headers` drops the `SDK-Name`/`SDK-Version` lines and
canonicalizes the remaining `X-Crozier-` prefix (the `Language` header) to `X-Fern-`
on both sides before comparison. Every other line of `client_wrapper.py` matches
exactly, so the wrapper is gated (never on an `unmatched` list) in every corpus.

### Real-world corpora that pin these rules

All four corpora are now regenerated as Fern's *packaged* SDK (`fern generate
--preview`), so the packaging scaffolding — `pyproject.toml`, `README.md`,
`reference.md`, `requirements.txt` — is present and compared rather than absent.
`operation-id-non-identifier`, `missing-operation-id`, and the `f_2fa_enabled`
model plus the root-level `get_thing` method behind `digit-leading-property` match
in full.

The root-client rule is also durable against the real-world
`livepeer-ai-runner` corpus at Fern 5.20.0. Its three untagged, groupless
operations (`health`, `hardware_info`, and `hardware_stats`) are methods on the
root sync and async clients alongside the tagged `generate` sub-client, and are
wired through the package exports and their own `reference.md` sections exactly
as Fern emits them. The first measured run diverged only outside root-method
placement — the shared README/reference/root-client environment
default plus `environment.py` — and matching those established two adjacent Fern
rules: a server description Fern does not recognize as an environment name uses
the `DEFAULT` environment member, and multipart reference examples list required
file inputs before other required fields. Its whole golden matches, while
the synthetic `digit-leading-property` fixture stays matched alongside it.

The component-array-item rule is pinned by the real-world
`apideck.com-ats` corpus at Fern 5.20.0: its
`Applicant.properties.social_links.items` object becomes the package-root
`ApplicantSocialLinksItem` model, the `Applicant` field references it rather than
`typing.Any`, and the aggregators re-export it. The first measured corpus run
matched immediately because the general component hoister already covered the
shape; registering the corpus turned that previously unmeasured rule into a
byte-exact regression target.

The underscore-before-digit rename is now pinned by the real-world
`twilio.com-twilio_messaging_v1` corpus at Fern 5.20.0:
`MessagingV1BrandRegistrations.russell_3000` becomes the Python field
`russell3000` with `russell_3000` retained as its wire alias. The first measured
corpus run found that type file already byte-matched through the shared numeric
field-boundary rule; what diverged were `src/fern/client.py` and
`src/fern/raw_client.py`, where URL-encoded array inputs used `List` plus JSON
encoding instead of Fern's `Sequence` passed directly as form data. URL-encoded
form arrays now follow Fern without changing multipart JSON encoding. The naming
test keeps both adjacent rules explicit: a word ending in a digit still absorbs
the following segment (`Cvc2Create` → `cvc2create`), while a digit-led boundary
is preserved (`2Factor` → `f_2_factor` for a property).

The HTTP-status exception names are pinned by the five corpora of
[`CORPUS.md`](../tests/fixtures/CORPUS.md)'s batch 10. `error_class_name` maps a
status to the class Fern raises, and 21 of its entries were reached by no
golden; `kytos-sdntrace-cp`, `withsecure-gdpr-subject-rights`,
`prometheus-x-edge-computing`, `exa-gate` and `amazonaws.com-cloudfront` between
them pin 13, including the whole `5xx` tail above `503`. Getting one wrong is
never one line — it renames the `errors/` module file, its lazy-import and
`__all__` entries, its `reference.md` row, and every `raise` site that declares
the status — so these rows exist to make a future edit fail loudly. Fern's map
is also not the IANA registry: it names Esri's `498`, nginx's `499` and Apache's
`509`, which CloudFront declares alongside the standard ones.

CloudFront additionally moved two rules the corpus had only approximated:

- **An annotated `$ref` is a use-site copy, at every depth.** Swagger-generated
  AWS documents write `allOf: [$ref, { description }]` on nearly every node.
  Fern copies the target under the using node's name rather than subclassing it,
  and the copy cascades: an array alias copies its element with one `Item` per
  nesting level, and a copied element's own annotated properties copy in turn
  (`ActiveTrustedSigners.Items` over a list of `Signer` →
  `List[ActiveTrustedSignersItemsItem]`, whose `KeyPairIds` becomes
  `ActiveTrustedSignersItemsItemKeyPairIds`). A copy documents itself with the
  annotation that named it, falling back to the target's own description when
  the annotation carried none. A scalar or collection alias resolves straight to
  its underlying type, so `allOf: [$ref string, { xml }]` is `str`, not the
  `String` alias.
- **`text/csv` reads back as a `str` body**, exactly as `text/plain`,
  `text/markdown` and `text/xml` do.

## Fern-python parity shapes (issue #41)

Issue #41's shapes are all closed against real Fern golden trees, so each is a
byte-match target like the rest of the corpus.

- **Tag-based client grouping** (`tag-based-grouping`). Plain (no `group_method`)
  operationIds `listWidgets`/`createWidget` tagged `widgets` and
  `listGadgets`/`createGadget` tagged `gadgets`. Fern groups by first tag into one
  sub-client per tag (`client.widgets.list_widgets()`), snake-cases the method from
  the operationId, and hoists each inline response to `{Method}Response` in that
  tag's own `types/`. crozier already produced this structure (the #40 grouping
  work); the fixture additionally pinned **sub-client ordering** — Fern lists
  sub-clients in path-**declaration** order (`widgets` before `gadgets`) in the root
  client and `reference.md`, not alphabetically, while the root client's
  `TYPE_CHECKING` imports stay **alphabetical**. crozier now emits both (the earlier
  blanket alphabetical sort was the divergence).
- **Hoisted parameter enums** (`enum-query-param`, issue #41 gap 2a). An inline
  `type: string` enum on a query parameter is hoisted to a named type
  `{Method}Request{Prop}` (`ListWidgetsRequestLevel`) in the tag's `types/` package,
  referenced by name in the client/raw client, rather than inlined at every use site
  ([`ir::InlineHoister::hoist_param_enum`]).
- **Real `enum.Enum` classes (issue #41 gap 2b), the default.** Every string enum —
  a named `components.schemas` enum, a hoisted inline-property enum (`{Owner}{Prop}`),
  or a hoisted parameter enum — renders as `class Name(enum.StrEnum)` over the
  generated `core/enum.py` shim (the stdlib `enum.StrEnum` on Python >= 3.11, the
  `(str, Enum)` mixin below it) with `SCREAMING_SNAKE` members and a `visit(...)`
  dispatch method
  ([`ir::EnumType`]/[`emit::render_enum`]). This is Fern's `enum_type: python_enums`
  mode; the golden corpus was generated with
  `pydantic_config.enum_type: python_enums`, so exhaustive and every enum-bearing
  target byte-match the class
  form, and worked examples use member access (`TypesWeatherReport.SUNNY`). The one
  Fern-only artifact this introduces — the `generatorConfig` block Fern writes into
  `.fern/metadata.json` — is normalized out of the comparison
  (`tests/e2e.rs::normalize_metadata`), the same posture as the SDK-identity headers,
  since crozier renders `python_enums` unconditionally and carries no such config.
  (Note this deliberately diverges from Fern's *out-of-the-box* default, which is the
  open `Union[Literal[..], Any]`; per issue #41 real enums are the more useful shape
  and the config unlocks byte-parity with them.)

- **Audience-scoped multi-SDK filtering** (`audience-filter`, issue #41 gap 3).
  `crozier generate --audience <name>` (repeatable) prunes to the operations
  crozier's own `x-crozier-audiences` extension marks for that audience — plus
  operations with *no* audience label, which survive any filter — and emits only the
  **transitive `$ref` closure** of the surviving operations'
  parameter/request/response schemas ([`openapi::filter_by_audience`]). Every other
  `components.schemas` entry, even an unlabelled one no surviving operation reaches,
  is dropped, so each audience SDK is self-contained. Per the [dual-header
  extension policy](#fern-compatible-extension-policy) crozier reads **both**
  `x-crozier-audiences` (canonical) and `x-fern-audiences`, canonicalizing on its
  own spelling the same way it emits `X-Crozier-*` SDK headers where Fern emits
  `X-Fern-*`; the fixture spec carries both (identical values) so Fern reads
  `x-fern-audiences` to produce the golden while crozier reads either.
  `listWidgets`→`public` and
  `getStats`→`internal`; `--audience public` byte-matches Fern's filtered SDK — the
  `admin` client and the internal-only `Stats` type are gone, `Widget`→`WidgetDetail`
  are kept. Fern's golden uses a group-level `audiences: [public]` filter that acts
  on the spec's `x-fern-audiences`. Property-/schema-level audiences are not yet
  honoured (a follow-up); only operation-level filtering is applied.

- **Strict audience subsetting** (`audience-filter-strict`, issue #62). The
  permissive default above keeps un-annotated operations under any `--audience`
  filter, so it cannot carve a *strict* subset from a mostly-un-annotated API.
  `--audience-strict` excludes un-annotated operations too, so only operations
  carrying a matching audience survive — Fern's exclusive behaviour. The fixture
  spec is `audience-filter` plus an *un-annotated* `/health` operation; Fern's
  `audiences: [public]` filter drops both the internal `getStats` op and the
  un-annotated `healthCheck` op, so the golden is exactly the `public` subset
  (`listWidgets` + `Widget`→`WidgetDetail`). `crozier generate --audience public
  --audience-strict` byte-matches it, while the permissive default would keep
  `healthCheck`. Fern's golden uses the same `audiences: [public]` configuration.

- **Ignore extension** (issue #78). `x-crozier-ignore: true` (canonical) or
  `x-fern-ignore: true` on an operation excludes it from generation, and on a
  component schema keeps that schema from being emitted
  ([`openapi::filter_ignored`]). Dropping an operation also prunes any schema that
  falls out of the surviving operations' transitive `$ref` closure *as a result* —
  a type only the ignored op referenced — while standalone schemas that no
  operation referenced to begin with are left untouched (so the ignore is inert on
  a spec that carries no markers, and never perturbs a full generation). An explicit
  `x-crozier-ignore: false` wins over a sibling `x-fern-ignore: true`, which is what
  makes Fern's Overlay-driven "ignore a broad set, then un-ignore a few" pattern
  work (Overlay 1.0 has `remove` but no un-remove, so a reversible flag is the only
  way to express "drop all GETs except this one"). No Fern golden fixture: Fern's
  `x-fern-ignore` output is just the un-ignored subset, which the audience-filter
  goldens already prove crozier reproduces byte-for-byte; the ignore itself is
  covered by the pipeline tests (`tests/generation.rs`) and a real-binary journey
  (`tests/e2e.rs::ignore_extension_prunes_marked_ops_through_the_binary_and_stays_valid`),
  which assert the marked ops and their exclusive types are gone and the pruned SDK
  still compiles.

These fixtures are the *packaged* SDK form (like exhaustive), reproduced with
`fern generate --preview` (see the regeneration note below).

### Fern-compatible extension policy

crozier honours a small set of `x-*` vendor extensions that steer generation
(audience labels and per-node ignore today). Every one follows a single
**dual-header policy** ([`openapi`] module docs), so a project migrating off Fern
can point crozier at its existing, Fern-annotated specs with zero edits, confirm
the SDKs match, then migrate the annotations to `x-crozier-*` as unhurried cleanup:

- **Input is permissive** — both the `x-crozier-*` and the Fern `x-fern-*` spelling
  are read for every supported extension.
- **`x-crozier-*` is canonical** — it is the form crozier documents and the form
  that *wins* when both spellings appear on one node; the `x-fern-*` value applies
  only as a fallback.
- **crozier only ever emits the crozier variant** — it never writes `x-fern-*`,
  mirroring the `X-Crozier-*` vs `X-Fern-*` SDK-identity headers.

The precedence lives in the field accessors (`Operation::audiences`,
`Operation::ignored`, `Schema::ignored`); any future extension inherits the policy
by default.

## Enum name sanitization (issue #50)

The real-`enum.Enum` generator derived each member name and `visit()` parameter
straight from the wire *value*, so any value that was not already a bare Python
identifier emitted source that failed the final `ruff format` and discarded the
whole SDK. `enum-name-sanitization` pins Fern's sanitized output for the shapes
that occur in real specs:

- **Python keyword value** (`global`) — the member is the safe upper-cased form
  (`GLOBAL`) and the `visit()` parameter is keyword-escaped (`global_`), via
  [`naming::enum_visit_param`]/[`enum_member_name`] (Fern's `snake_case.safe_name`
  / `screaming_snake_case.safe_name`).
- **Punctuation + leading single digit** (`0: Active`) — the `:`/space become word
  boundaries and a bare single-digit word is spelled out
  (`ZERO_ACTIVE`/`zero_active`; `1: InActive` → `ONE_IN_ACTIVE`/`one_in_active`),
  matching Fern's enum-name generator, which carries a number-to-words map.
- **Type-mismatched enum** — a `type: string` enum whose values are all integers
  (`size: {enum: [100, 125, 175, 250]}`) has nothing to enumerate;
  [`ir::string_enum_values`] returns `None` so the schema falls back to the base
  `str` (`typing.Optional[str]`) rather than emitting an empty enum class with a
  body-less `visit()`. A *partial* mismatch still drops only the bad members.

Two enum members that sanitize to the same identifier are disambiguated with a
`_{n}` suffix ([`ir::dedupe`]) so the emitted Python stays valid.

**A multi-digit leading token Fern cannot name** (`_01_00_AM` → Fern's `0100Am`,
which it *rejects* with "not suitable for code generation") has no byte-match
target, so it is covered by the compile-only
`enum_sanitization_generates_valid_python` e2e instead: crozier prefixes `_` to
keep the identifier legal (`_01_00_AM`) and the whole tree compiles. This is the
same posture as the arbitrary-spec validity check — where Fern errors, the bar is
"valid Python," not byte-parity.

### Enum `visit()` receiver collision (issue #57)

One value in the same `visit()`-parameter path stayed broken after #50: an enum
value that sanitizes to the method receiver name **`self`** (e.g. an ownership
enum `["self", "spouse", "child"]`). The member upper-cases to `SELF` (fine), but
the `visit()` parameter is the lower-cased `self`, which duplicates the method's
own `self` receiver — a `SyntaxError: duplicate argument 'self'` at import, though
it is grammatically valid enough to pass the final `ruff format` and ship a
non-importable module. [`naming::enum_visit_param`] now escapes a value that
sanitizes to `self` with the same trailing `_` it applies to keywords (`self` →
`self_`), and the `return self_()` body call follows since both derive from the
same param. **`cls` is deliberately left unescaped:** `visit` is an ordinary
instance method, so a `cls` parameter is legal and shadows nothing — Fern escapes
`self` but not `cls`, and matching Fern is the contract. `enum-receiver-collision`
pins both: `WidgetOwner` (the `self` → `self_` escape) and `WidgetBinding` (the
`cls` non-escape) byte-match Fern's whole tree.

Issue #50 **part 2** (the **discriminated-union alias annotation**) is closed by the
same PR family: the corpus was bumped 4.34.0 → 4.35.0 and
[`emit::render_discriminated_union`] now emits
`typing_extensions.Annotated[Union[…], pydantic.Field(discriminator=…)]`. See the
issue-#43 gap #2 note above for why the bump is minimal (4.35.0's only output change
over 4.34.0 is this annotation).

> **How these golden trees are produced.** The workflow resolves and passes an
> exact Python generator version, records it in each fixture's provenance, pins
> the Fern CLI via `fern.config.json`, and installs the *packaged*
> SDK (a pip package: `src/<pkg>/…` + `pyproject.toml` + `README.md`/`reference.md` +
> `.fern/`). It gets the packaged form from `fern generate --preview --output`, which
> — unlike a plain `--local` `local-file-system` run, that emits only the flat module
> tree — writes the full package **and** needs no publishing credentials (a `pypi`/
> `github` output location tries to push and crashes locally). Environment notes:
> (1) `--preview` only emits the package when Fern considers itself authenticated, so
> the script sets a dummy `FERN_TOKEN` (no credential — a non-empty value suffices);
> (2) Fern's generator runs `npm install @fern-api/generator-cli` inside its
> container, which hangs forever under a TLS-intercepting sandbox — the container
> reaches neither the host proxy (it listens on `127.0.0.1`) nor the proxy CA. The
> script handles this automatically: when a proxy is configured (`HTTPS_PROXY`) it
> routes Fern's `docker run`/`create` through a generated shim injecting
> `--network host`, the proxy env, and `-v <ca>:/ca.crt -e
> NODE_EXTRA_CA_CERTS=/ca.crt` (CA from `$NODE_EXTRA_CA_CERTS`, override with
> `CROZIER_FERN_DOCKER_CA`; disable the shim with `CROZIER_FERN_NO_DOCKER_SHIM=1`);
> (3) on a sandbox whose Docker daemon can't see the host `mktemp` dir, point
> `TMPDIR` at a Docker-visible path.
>
> Resolving latest stable is an explicit upgrade: comparison remains red until
> Crozier's Fern-derived runtime/scaffolding metadata and `NOTICE` are moved to
> that same exact version. It is never treated as a no-diff refresh of the old
> pin.

## Configurable client class name (issue #61)

crozier derived the generated **root client class** name solely from the package
name, as `{PascalCase(package_name)}Api` (`FernApi`/`AsyncFernApi`). Fern exposes a
`client_class_name` generator config to override it, and crozier now mirrors it with
`--client-class-name`: when given, that string replaces the base name everywhere it
flows — the root `client.py` sync/async classes, the package `__init__.py`
re-exports, the per-tag client's worked `Examples`, the README/reference snippets,
and (with document `servers`) the `{ClientName}Environment` enum. Unset, the
package-derived default is unchanged, so every other corpus is unaffected.

`client-class-name` pins this against real Fern output: a two-endpoint `widgets`
API generated with `client_class_name: AcmeClient` byte-matches Fern's whole
tree (`AcmeClient`/`AsyncAcmeClient`). Its Fern generator config carries
`client_class_name: AcmeClient`; the value is recorded
in `.fern/metadata.json`'s `generatorConfig`, which the e2e already normalizes out
(`normalize_metadata`), so the provenance difference does not gate.

## Pydantic extra-fields behavior (issue #63)

Generated pydantic models always set `extra="allow"` — an unknown field on a
response is kept on the model. `--extra-fields <allow|ignore|forbid>` (Fern's
`pydantic_config.extra_fields`) now drives that, threaded from the CLI/env/config
layer through [`config::GenerateConfig`] and [`ir::Ir`] into every model body
([`emit::extra_config`]). It is a **Python-generator-specific** setting: it lives
only under a generator (or the `--extra-fields` flag / `CROZIER_EXTRA_FIELDS` env),
never among the shared top-level config defaults.

The one subtlety — and the reason a real Fern fixture pins it — is an asymmetry
between the two pydantic-version config blocks Fern emits. Under **pydantic v2**,
`ignore` drops the `extra=` kwarg entirely (`pydantic.ConfigDict(frozen=True)`,
since v2's own default is `ignore`), while `allow`/`forbid` spell it out
(`extra="allow"`/`extra="forbid"`). The **v1** `Config` always writes the explicit
member (`extra = pydantic.Extra.<name>`). `pydantic-extra-fields` — the two-endpoint
`widgets` API generated with `extra_fields: ignore` — byte-matches Fern's whole
tree, so `Widget`'s model reproduces that asymmetry exactly. Its Fern
generator config carries `extra_fields: ignore`; like the enum/client-class-name
config, Fern records it in `.fern/metadata.json`'s
`generatorConfig`, which the e2e normalizes out (`normalize_metadata`).

`forbid` is pinned the same way, by `eos.local-extra-fields-forbid` — CORPUS.md
row 82, which is row 43's real-world `eos.local` spec generated a second time
with `extra_fields: forbid`. A generator setting is not expressible in an
OpenAPI document, so pinning one needs no new spec, only a second corpus name
over a registered source with its own `fern-generator-config.txt` entry. Its
four models carry `extra="forbid"` in the v2 `model_config` and
`pydantic.Extra.forbid` in the v1 `Config`, and all 42 files byte-match.

## Cross-document `$ref` resolution (issue #77)

Every corpus spec but one is a single self-contained document: every `$ref` is a
local JSON pointer into the same file. `helios-verifiable-api` is not — many of
its component schemas are `$ref`s naming an `ethereum/execution-apis` document
by absolute URL, and Fern's importer **fetches** each one and resolves it
transitively. Its CORPUS.md row is keyed by that fixture name, and its shapes
cell carries the counts; they are not restated here. That is the only
reference form Fern was measured to follow rather than discard ([`fern-limitations.md`](fern-limitations.md)
records the ones it drops), so it is the only golden that can pin whether crozier
opens a second document at all.

[`src/refs.rs`](../src/refs.rs) runs that resolution as a load-time pass, before
every other normalization, so the rest of the pipeline still sees one document.
Fetching is a **conditional generation-time capability**: a document with no
remote `$ref` never opens a socket. It shells out to `curl`, the same shape
[`pyfmt`](../src/pyfmt.rs) uses for `ruff` — crozier ships one static binary, and
an in-process TLS stack would be a large supply-chain addition (a new license tier
in `deny.toml`, a C toolchain on every release target) for a path almost no spec
takes. A missing or failing `curl` is an actionable `Error::RemoteRef`, never a
silently dropped schema: dropping one would emit a plausible SDK with the wrong
types in it. Only `http`/`https` references reach the fetcher, and the URL is
passed after `--` so it can never be read as an option.

The golden pins four rules that follow from resolving at all:

- **A fetched schema takes its pointer's name, and the local key aliases it.**
  `TransactionReceipt: {$ref: …/receipt.yaml#/ReceiptInfo}` declares the model as
  `ReceiptInfo`, leaves `TransactionReceipt = ReceiptInfo` beside it, and types
  every other reference — `BlockReceiptsResponse`, `TransactionReceiptResponse` —
  against `ReceiptInfo`. Where the two names coincide (`address: {$ref:
  …#/address}`, which is most of them) the schema simply resolves in place.
- **A local pointer inside a fetched document resolves against the *root*.** The
  referenced files are schema fragments an assembling document is expected to
  supply, so their `#/components/schemas/…` pointers are left untouched. helios
  declares the ones it needs; the two it does not (`TransactionSigned`,
  `BlockNumberOrTagForRange`) are unresolvable, and Fern degrades them to the
  unknown type — `Optional[Any]` on a property, nothing at all as an `allOf`
  member. crozier had been inventing a class for such a reference, emitting an
  import of a module it never wrote.
- **An endpoint response follows a bare alias.** `BlockResponse: {$ref:
  …/Block}` still declares `BlockResponse = Block`, but `get_block_information`
  returns `Block`. A reference from *inside* another schema keeps the alias name
  — Airbyte's `DestinationAuthSpecification` stays itself on the property that
  carries it — so the rewrite is confined to response media schemas.
- **Nullability lives at the use site.** An explicit `type: null` alternative is
  not a union member: it leaves the composition and makes what remains nullable.
  One survivor becomes that type made optional (`FilterTopics =
  Optional[List[Optional[FilterTopic]]]`); two or more stay an undiscriminated
  union whose alias carries no `Optional` (`FilterTopic = Union[Bytes32,
  List[Bytes32]]`) and whose every *reference* is `Optional[FilterTopic]`.

Two unrelated rules the same golden forced out, neither of which needs a remote
reference to reach:

- **A query value that reaches nothing but scalars is serialized directly.**
  helios sends `block` (a `Union[Uint, BlockTag, Hash32]` of two string aliases
  and an enum) raw as a query parameter and through
  `convert_and_respect_annotation_metadata` as a request-body field. Only the
  query position takes the shortcut, because only there does the value go onto the
  URL as text.
- **A union example comes from the alternative that names values.** A free-form
  scalar alternative can only supply a placeholder from the argument name, so Fern
  reaches past `Uint` to `BlockTag` and uses `"earliest"` — as the plain string the
  union's own annotation accepts, not the `BlockTag.EARLIEST` member a
  single-enum argument would take.

The row's one standing liability is recorded in its `CORPUS.md` shapes cell: its
golden depends on a **third-party fetch at generation time**, and the referenced
URLs address `refs/heads/main` rather than an immutable ref, so an upstream edit
to any of the referenced files breaks this row's reproduction for a reason
unrelated to crozier.

## Map-of-self and multi-type arrays (issue #77)

`docs/fern-limitations.md`'s round 4 measured eighteen open questions and found
two shapes Fern reads and emits output *derived from*, with no golden pinning
either. `eozilla` (CORPUS.md row 92) and `openepcis-dpp-ready` (row 93) are those
two, and the rules below are what reproducing them cost. Three were probed
directly against `fernapi/fern-python-sdk:5.20.0` because no committed golden
could answer them; the rest were read off the two goldens.

**A `type` list with more than one non-`null` member is an `anyOf`.** A single
non-`null` member is nullability and nothing else, which is why
`TypeField::primary` answers every other caller. Two or more are a union of those
types, and Fern hoists a named alias for it exactly as it would for an inline
`anyOf` — `SingleValuedDataElementValue = typing.Union[str, float, bool]` in its
own module. [`openapi.rs`](../src/openapi.rs)'s `normalize_multi_type_schemas`
rewrites the node at load time so the union hoisting, naming, and
forward-reference passes need no second spelling of the shape; a `null` member
leaves the union and sets `nullable`. The origin survives the rewrite
(`Schema::multi_type_union`), because a *member* of another union that came from a
`type` list is named rather than inlined
(`MultiValuedDataElementValueItemZero`) where a hand-written `anyOf` in the same
position is inlined.

**Union members fold together where the last equal one stood.** Probed:
`oneOf: [string, integer, string/uri]` generates `typing.Union[int, str]` — the
surviving `str` sits at the `uri` member's index, not the bare `string`'s. Two
more probes settle what the members themselves render as: `format: binary` in a
union is the `string` it is declared as (`typing.Union[str, int]`, not `bytes`),
and a member declaring nothing but `nullable: true` is
`typing.Optional[typing.Any]`. Eozilla's twelve-member `InlineValue` is all three
rules at once: its `binary`, `uri` and bare `string` alternatives all render `str`,
and the ten-member union Fern emits carries one of them, after `dt.datetime`.

**A discriminated union's tag is an ordinary field bar its default.** A wire name
that does not survive Python naming carries the same alias metadata every other
field would, so EN 18222's `objectType` renders `object_type:
typing_extensions.Annotated[typing.Literal["…"], FieldMetadata(alias="objectType"),
pydantic.Field(alias="objectType")]`, and `pydantic.Field(discriminator=…)` names
the Python field. The wrapper is flat, and Fern writes the variant's *own*
properties before the ones its `allOf` base contributes —
`DataElement_RelatedResource` opens with `resource_title` and closes with the
base's `element_id`/`dictionary_reference` pair. The strip follows the `$ref` that put the tag there, but only when
the base's declaration says nothing the tag does not: `DataElementBase.objectType`
is an optional bare `type: string` and vanishes, while Microcks'
`AbstractExchange.type` is required with an `enum` of the discriminant values and
Fern keeps it, hoisting `AbstractExchangeType` for it.

**`update_forward_refs` arguments are per wrapper.** Each takes the module's
cyclic names *minus the model that wrapper flattened* — a wrapper cannot be asked
to resolve its own source — which is why `Node_And` takes `Node=Node` and not
`AndNode=AndNode`, and why EN 18222's two recursive wrappers each name the other's
source. The deferred imports below the alias follow the order the calls first
mention them, not a sort of the whole set. An alias that merely *wraps* a
discriminated union (`ProfitAndLossRecords = Optional[List[ProfitAndLossRecordsItem]]`)
imports it eagerly with no forward-reference machinery at all; an alias whose
target is itself a `Union[..]` defers into the cycle like any other member. And a
model that only *inherits* its way into a cycle — `QualifiedValue(Format)`, where
`Format.schema` closes Eozilla's map-of-self — takes `from __future__ import
annotations` and no repair call, because the base's own module already repaired it.

**One simple name imported from two modules is aliased in both.** Eozilla declares
a component schema called `ApiError`, which collides with crozier's core one in
every raw client that raises from it. Python cannot hold both, and Fern does not
pick a winner: it writes `from ..core.api_error import ApiError as
core_api_error_ApiError` beside `from ..types.api_error import ApiError as
types_api_error_ApiError` and uses the module-qualified alias at every occurrence,
including the `raise` sites and the `errors/` class's base. [`emit.rs`](../src/emit.rs)
renders each affected file twice for this: the collision is only knowable once
every reference has been walked, and the *body* has to carry the alias too.

**Response selection skips what it cannot dispatch on.** Eozilla puts
`executeProcess`'s `200` under the media type `/*`, which names no type and no
subtype. Fern skips that response entirely and types the operation from the next
`2xx` — the `201` carrying `JobInfo`, description and all — rather than reading it
as a bodyless success. Separately, a bodyless `201` **or `202`** beside a success
body is not an empty-body case: `updateDPPById` returns
`HttpResponse[DigitalProductPassport]` with a bodyless `202` in the document.

**Two smaller rules the goldens forced.** Promoted global headers that normalize
to one Python name emit one constructor parameter while keeping both assignments
and both header writes — EN 18222 declares `X-API-KEY` and `API-KEY`, and crozier
emitted `api_key` twice, which Ruff rejects as a syntax error rather than a
redundancy. And a query value serializes by the format the document declares even
when the emitted annotation is an alias name: `date: Timestamp` still goes onto the
URL through `serialize_datetime`.

Examples reach through a reference the same way. A property written as a
one-member `allOf` around a `$ref` (the 3.0 idiom for annotating a reference) is
exampled from the referenced schema, an array of such references is exampled as a
one-element list of it, and a date/date-time field's declared example is used
rather than the synthesized placeholder.

## Coverage note

The gate measures coverage with `cargo llvm-cov --fail-under-lines 95`, which
runs on every CI platform. It cannot run in every sandbox (some restrict the
linker features the LLVM profile runtime needs, and ptrace-based tools need
privileges those sandboxes withhold); when developing in such an environment, run
the rest of the gate and rely on CI for the coverage number.
