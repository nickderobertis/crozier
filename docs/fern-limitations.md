# Fern 5.20.0 — measured limitations

What `fernapi/fern-python-sdk:5.20.0` **does not do** with an OpenAPI document, as
measured, not as read off a specification. crozier's contract is byte-match with
Fern ([`matching.md`](matching.md)), so a shape Fern discards is a shape no golden
can pin: this file is the record of which shapes those are, so the next person
choosing a fixture does not spend a screen re-deriving it.

The measurements come from four **screens** run on one host on 2026-08-20 — one
each for *serialization*, *auth-and-responses*, *structure-and-media* and
*naming-and-types* — plus the **Round 3** pass that decided what to register from
them. Each screen carried documents from a pinned URL through `fern check` and
then a real local `fern generate`, and cross-checked real documents against
minimal locally authored probes. The screen reports themselves lived in host
scratch outside every repository and are gone; the evidence below is quoted from
them rather than linked, so this file is readable with nothing but this checkout.

**Versions in force for every measurement below:** Fern CLI `5.67.1`
(`fern.config.json`) and generator `fernapi/fern-python-sdk:5.20.0`
(`generators.yml`) — the same pin the corpus goldens record. Runs set
`CI=true`/`GITHUB_ACTIONS=true` to match `scripts/generate-fern-fixture.sh`, which
is why quoted logs carry doubled `::warning::` annotation lines.

## How to read a verdict

Findings are not all the same kind of fact, and the difference decides whether a
future probe is worth running:

| verdict | meaning |
|---|---|
| **discards** | Fern accepts the shape, emits nothing derived from it, and reports nothing |
| **ignores** | Fern emits the node but the modifier under test (a `style`, an `explode`) changes no byte |
| **refuses** | `fern check` exits non-zero on the shape |
| **crashes** | `fern check` passes and `fern generate` fails |
| **coincidence** | Fern's output happens to equal the standard's wire form, produced by an unconditional default rather than by handling the shape |
| **unmeasured** | **an open question**, not a proven absence: no screen probed what Fern emits here, and a probe could still answer it |

A **probe** is a minimal, locally authored OpenAPI document isolating one shape.
Probes are evidence about Fern; none is a corpus fixture and none is proposed as
one — the corpus takes real-world specifications only
([`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md)).

## What these measurements do *not* establish

The screens measured **Fern**. None of them built or ran crozier, and none
compared a byte of crozier's output against Fern's. Where this file says what
crozier does beside Fern, it is reading crozier's source and says so — the thing
that settles it is the ordinary end-to-end byte comparison the corpus already
does, not this document.

Two pieces of evidence could not be recovered from the screens and are recorded
as absent rather than reconstructed:

- The serialization screen's probe runner created its Fern workspace with
  `mktemp -d /tmp/fernscreen.XXXXXX` and removed it on exit. For probes whose
  `fern check` failed, the generate stage — the only stage that prints the
  workspace path — never ran, so **the literal inner command path for the
  `header-array` probe is unrecoverable**. Its exit code and full diagnostics were
  captured to files and are quoted below; the path is not invented.
- Every generated SDK tree was deleted at the end of its own run. What survives of
  Fern's output is the extracts quoted here.

## Parameter serialization

The largest finding of the round, and the one that changes what a serialization
fixture is worth.

### Fern branches on the declared `style` in exactly one place

An **array** query parameter declared `style: form` with `explode: false` is
comma-joined. Nothing else in the emitted Python reads `style` at all. Measured on
single-parameter control probes, and reproduced by one operation carrying six
query parameters differing only in style:

| probe | declared | Fern emits |
|---|---|---|
| `form-array-explode-false-CONTROL` | `form`, `explode: false`, array | `"probeParam": ",".join(map(str, probe_param))` |
| `form-array-explode-true-CONTROL` | `form`, `explode: true`, array | `"probeParam": probe_param` (httpx repeated key) |
| `pipeDelimited-array-explode-false` | `pipeDelimited`, `explode: false` | `"probeParam": probe_param` — **not** pipe-joined |
| `pipeDelimited-array-explode-absent` | `pipeDelimited`, explode absent | `"probeParam": probe_param` — **not** pipe-joined |
| `spaceDelimited-array` | `spaceDelimited`, `explode: false` | `"probeParam": probe_param` — **not** space-joined |
| `deepObject-real-object` | `deepObject`, object | `convert_and_respect_annotation_metadata(...)` |
| `pipeDelimited-object` / `spaceDelimited-object` | object-valued | `convert_and_respect_annotation_metadata(...)` — the same call, byte-identical |
| `matrix-array` / `label-array` (path) | `matrix` / `label` | `f"probe/{encode_path_param(probe_param)}"` — no `;` or `.` prefix |
| `matrix-object` / `label-object` (path) | object-valued | `encode_path_param(convert_and_respect_annotation_metadata(...))` |
| `cookie-primitive` / `cookie-array` / `cookie-object` | `in: cookie` | **parameter absent from the generated client** |

Every row above ran `fern check` 0 and `fern generate` 0 unless stated otherwise.

- **`pipeDelimited` and `spaceDelimited` arrays are not joined** — verdict
  *discards*. The declared style leaves no trace in the output.
- **Object-valued query parameters are not style-conditioned at all** — verdict
  *coincidence*. `deepObject`, `form` with `explode` true and false,
  `pipeDelimited` and `spaceDelimited` objects all emit byte-identical code, and
  the runtime `query_encoder.py`'s `traverse_query_dict` then flattens *every*
  dict-valued query parameter to `key[subkey]=value` unconditionally. That wire
  form is what `deepObject` prescribes, so **Fern's `deepObject` output coincides
  with the standard rather than Fern implementing `deepObject` as a style**: it
  produces the same encoding for objects that declare `form`.
- **Path parameters ignore `style` entirely.** `matrix` and `label` emit a plain
  `f"probe/{encode_path_param(probe_param)}"`, `fern check` 0, `fern generate` 0.
  Worse than style-blind: `encode_path_param` is `str(jsonable_encoder(obj))`, so a
  `Sequence[str]` path parameter renders Python's `str(['a','b'])` — a literally
  malformed path segment.

*Beside crozier's source:* crozier's whole style-and-explode rule is one
expression in `src/ir.rs` (`let comma_separated = p.explode == Some(false) &&
p.style.as_deref().is_none_or(|style| style == "form") && …schema is an array…`),
which selects the same parameters Fern comma-joins and falls through where Fern
falls through. That reading is inference from source; only a golden proves it.

### Cookie parameters are dropped from the generated client entirely

Fern emits `Skipping cookie parameter, <name>, in <METHOD> <path>` as a
**warning** — `fern check` still prints `All checks passed` and exits 0 — and the
parameter is then absent from the client. Probe `cookie-primitive`, one operation
with one parameter:

```
$ fern check      → exit 0
[api]: Skipping cookie parameter, probeParam, in GET /probe
All checks passed
$ fern generate --group python-sdk --local --preview --output <tmp> --force   → exit 0
```

Emitted call site: **parameter absent from the generated client.**

Measured **188 times across 32 of the 94 documents** the serialization screen
carried. On `MateEke/picture-frame` the check exits 0 with two such warnings and
the emitted SDK contains zero occurrences of the string `cookie`. A cookie fixture
would pin *"both crozier and Fern emit nothing"*, which is why Round 3 registers
none. crozier drops cookie parameters too (`src/ir.rs`, the
`has_unsupported_params` comment), so the two already agree by construction.

### A `content:`-typed parameter collapses to a bare `str`

Probe `param-content-path` emits `def op(self, probe_param: str, ...)`, losing the
declared JSON object. Verdict *discards*.

### Header parameters: array refuses, object crashes

An **array-typed header parameter fails `fern check`**. Fern synthesizes an
endpoint example for the header using the parameter *name* as a string, then
rejects its own synthesized example against the array schema. Probe `header-array`,
inner `fern check` exit **1** (the wrapper process exits 0 regardless, so the inner
code was captured to a file):

```
[sdk] 1 error
    [error]
        path: probe.yml -> service -> endpoints -> op -> examples[0] -> headers
        issue: Expected example to be a list. Example is: "probeParam"

Found 1 error and 0 warnings in 0.000 seconds.
```

`fern generate` never ran — the runner guards it behind a zero check exit. This is
the same failure [`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md)
records for `jaewook-epcis`, reproduced from first principles on a three-line
specification.

An **object-typed header parameter crashes the generator**. Probe `header-object`:
`fern check` exit **0** (`All checks passed`), `fern generate` exit **1**, tail of
the container traceback:

```
File "/src/fern_python/generators/sdk/declaration_referencers/type_declaration_referencer.py", line 25, in get_filepath
  declaration_fern_filepath = self._types[name.type_id].name.fern_filepath
KeyError: 'type_:ProbeOpRequestProbeParam'
```

### Where the supply ran out, and where it was only test stubs

Six serialization gaps ended **empty**, and the supply is exhausted rather than
unsearched. `matrix-object`, `param-content-path` and `param-content-cookie` each
had one or two candidates carry end to end — short of a primary plus two backups;
`explode-true-simple-header`, `header-array` and `header-object` had none at all.
The screen went past the census's ranked top eight and screened **every remaining
eligible permissively licensed document in the whole 7,137-document census** — six
more, all of which failed `fern check`: `erraggy/oastools` on
`Unsupported OpenAPI version: 3.3.0`, and four `OpenUdon/oas` copies plus
`pb33f/libopenapi` on multipart `is exploded and must be a list` errors.

Four further gaps closed **only on tooling test fixtures** and are therefore not
registrable: `matrix-array`, `label-array-or-object`, `spaceDelimited-object` and
`pipeDelimited-object` each verified, but every candidate is a parser or
code-generator test stub rather than a specification anyone runs an API from — the
"document nobody writes" the real-world constraint exists to exclude — and Fern
discards `matrix` and `label` anyway. The stubs, named so the supply reads as
searched rather than missed:

- `thephpleague/openapi-psr7-validator:tests/stubs/pathParams.yaml`
- `eve0415/oasts:fixtures/{msw-empty-path-3.1,strict-flags-3.1,msw-showcase-3.1}/openapi.yaml`
- `Cornutum/tcases:.../openapi/{styles,normalize-form}.json`
- `micronaut-projects/micronaut-openapi:.../3_0/params-with-style.yml`
- `hey-api/hey-api:specs/3.1.x/rpc-query-styles.yaml`
- `stoicflame/enunciate-openapi:.../arguments/openapi.yml`
- `enorganic/oapi:tests/input-data/parameter-styles.json`

The one non-stub among them,
`on-org/nuxt-openapi-docs-module:playground/docs/openapi/dynamic-query-params.yaml`,
is a real document whose every backup is a stub, so `pipeDelimited-object` cannot
reach a primary plus two backups without them.

## Auth and responses

### The importer drops four security schemes outright

`apiKey` in **query**, `apiKey` in **cookie**, **`mutualTLS`** and HTTP
**`digest`** never reach the generated client. Measured on isolated probes:

| declared security | `fern check` | what Fern generates |
|---|:--:|---|
| `apiKey` in header (control) | 0 | required `api_key: str` → `headers["X-API-Key"]` |
| `apiKey` in **query**, sole scheme, ops secured | **1** | — `Service requires auth, but no auth is defined.` |
| `apiKey` in **cookie**, sole scheme, ops secured | **1** | same refusal |
| `mutualTLS`, sole scheme, ops secured | **1** | same refusal |
| http `digest`, sole scheme, ops secured | **1** | same refusal |
| any of those four declared but **no** operation requires auth | 0 | a **credential-free** client — no `token`, no `api_key`, no `Authorization` |
| unsupported scheme **then** a supported one | 0 | the supported one only; the unsupported scheme leaves no trace |
| `openIdConnect`, sole scheme, all ops secured | 0 | **required** `token: Union[str, Callable[[], str]]` → `Authorization: Bearer` |
| `openIdConnect` with one public operation | 0 | **optional** `token: Optional[...] = None` |
| `oauth2` implicit / password | 0 | `token` → `Authorization: Bearer` (required when every op is secured) |
| operation-level security **alternatives** | 0 | collapses to one credential — the first supported scheme |
| ranged `1XX`/`3XX`/`4XX`/`5XX` response | 0 | **no `errors/` package entry at all**; the operation falls through to `ApiError` |

So for those four schemes **there is no such thing as a specification that
isolates the feature**: declare one alone and Fern refuses the document; declare
one unenforced and Fern emits a credential-free client; pair one with a supported
scheme and Fern generates from the supported one. Every proposed primary in the
screen therefore pairs the unsupported scheme with a supported one.

**`openIdConnect` is the exception in that list** — Fern imports it as a bearer
`token`, required when every operation is secured and optional when one operation
is public. Two independent documents show it:
`gh:questsin/UBC-Rogers-CAMARA-Hackathon:API/sim-swap.yaml` (sole scheme, all ops
secured) and `gh:tractionguest/guest-api:openapi.yml` (MIT, 43 ops, all secured),
both exit 0 at both stages and both emit a **required** token.

*Beside crozier's source:* `auth_model` in `src/ir.rs` selects the first header
`apiKey`, http `bearer`/`basic`, or `oauth2` scheme and falls through to
`_ => Auth::Bearer { required: false }`; it returns `Auth::None` only when the
scheme map is *empty*. Read against the two rows above, an openIdConnect-only fully
secured document and an unenforced-unsupported-scheme document both look like
divergences. Inference from source — no screen ran crozier.

### Ranged responses yield no error class

A `1XX`/`3XX`/`4XX`/`5XX` response key produces **no `errors/` package entry** and
no `raise` branch; the operation falls through to `ApiError`. `fern check` 0,
`fern generate` 0. Verdict *discards*.

### All 21 unpinned status exception names are correct — and 428 is `PreconditionError`

**Read this twice before "fixing" anything.** Issue #148 reasoned from RFC 6585
(which calls 428 *"Precondition Required"*) that crozier's `PreconditionError`
was likely wrong. It is not. Fern 5.20.0 names the 428 exception
**`PreconditionError`**, and names 412 `PreconditionFailedError`, so the two are
distinct classes and nothing collides. Measured three ways: an isolated 428 probe,
a 21-status probe, and two real documents.

Verbatim from the 21-status probe's `raw_client.py`:

```python
            if _response.status_code == 428:
                raise PreconditionError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
```

and from `errors/precondition_error.py`:

```python
class PreconditionError(ApiError):
    def __init__(self, body: Problem, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=428, headers=headers, body=body)
```

A probe declaring all 21 statuses on 21 operations passed `fern check` (exit 0)
and generated (exit 0), emitting exactly 21 error classes. Every class was read
three ways — the `class X(ApiError)` line, the `errors/<module>.py` filename, and
the `super().__init__(status_code=…)` argument — and cross-checked against the
branch the generated `raw_client.py` raises. **Every one of the 21 hand-written
names in crozier's `error_class_name` (`src/ir.rs`) matches, class name,
module filename and status code alike: 0 mismatches out of 21.**

| status | Fern class | `errors/` module | verified real specs emitting it |
|---:|---|---|---:|
| 407 | `ProxyAuthenticationRequiredError` | `proxy_authentication_required_error.py` | 0 (probe only) |
| 408 | `RequestTimeoutError` | `request_timeout_error.py` | 6 |
| 412 | `PreconditionFailedError` | `precondition_failed_error.py` | 5 |
| 414 | `UriTooLongError` | `uri_too_long_error.py` | 1 |
| 417 | `ExpectationFailedError` | `expectation_failed_error.py` | 2 |
| 418 | `ImATeapotError` | `im_a_teapot_error.py` | 4 |
| 421 | `MisdirectedRequestError` | `misdirected_request_error.py` | 0 (probe only) |
| 423 | `LockedError` | `locked_error.py` | 7 |
| 424 | `FailedDependencyError` | `failed_dependency_error.py` | 6 |
| 425 | `TooEarlyError` | `too_early_error.py` | 1 |
| 426 | `UpgradeRequiredError` | `upgrade_required_error.py` | 6 |
| 428 | `PreconditionError` | `precondition_error.py` | 2 |
| 431 | `RequestHeaderFieldsTooLargeError` | `request_header_fields_too_large_error.py` | 1 |
| 451 | `UnavailableForLegalReasonsError` | `unavailable_for_legal_reasons_error.py` | 5 |
| 502 | `BadGatewayError` | `bad_gateway_error.py` | 16 |
| 505 | `HttpVersionNotSupportedError` | `http_version_not_supported_error.py` | 5 |
| 506 | `VariantAlsoNegotiatesError` | `variant_also_negotiates_error.py` | 5 |
| 507 | `InsufficientStorageError` | `insufficient_storage_error.py` | 7 |
| 508 | `LoopDetectedError` | `loop_detected_error.py` | 5 |
| 510 | `NotExtendedError` | `not_extended_error.py` | 6 |
| 511 | `NetworkAuthenticationRequiredError` | `network_authentication_required_error.py` | 5 |

The names being right is not the same as their being *pinned*: eight of the 21
have no registrable witness set, listed under
[What Round 3 did not register](#what-round-3-did-not-register-and-why).

### 407 and 421 — a corpus limit, not a Fern one

**Zero** documents in the eligible pool of 4,864 declare either status anywhere, so
no real specification can pin them. Probed directly, Fern handles both:

| | 407 | 421 |
|---|---|---|
| `fern check` | exit **0**, `All checks passed` | exit **0**, `All checks passed` |
| `fern generate` | exit **0**, packaged SDK | exit **0**, packaged SDK |
| class emitted | `ProxyAuthenticationRequiredError` | `MisdirectedRequestError` |
| module | `errors/proxy_authentication_required_error.py` | `errors/misdirected_request_error.py` |
| `status_code` | 407 | 421 |

The only ways to pin these two are a probe-style specification (which the corpus
rules exclude) or a wider pool.

## Fern exiting zero while doing nothing

Exit codes are the weakest evidence in this whole file. Every failure mode in this
section ends with two zeros.

### `fern check` can exit 0 while the document did not parse

The log carries `Failed to parse openapi document <title>` and a
`CliError: Failed to resolve …`, and then still prints `All checks passed` and
exits 0 — after which Fern generates an empty SDK. Ten of 105 check-passes in the
structure-and-media screen and eight documents in the auth-and-responses screen
are exactly this shape.
[`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md) already records it for
`conjur.local` and `digitalocean.com` (*"Fern falsely returned success"*).

The instructive case is `gh:speakeasy-sdks/moov-go`: 73 operations, 235 KB, both
stages exit 0, and the result is a **26-file skeleton with no client, no types and
no errors**, because `"429": {"$ref": "#/components/schemas/RateLimited"}` points
a response at a *schema* and Fern cannot resolve it.

> **The practical rule for any future fixture work:** exit codes are not enough.
> Grep the check log for `Failed to resolve` and `Failed to parse`, and assert the
> generated tree contains `raw_client.py`.

### Duplicate `operationId` silently collapses operations into one method

`networknt/light-rest-4j`'s `openapi-meta/src/test/resources/config/openapi.yaml`
reuses `operationId: showPetById` across **18 operations** and Fern emits one. On
the sibling `openapi-validator/.../config/openapi.yaml`: **22 operations in, 5
client methods out**. Both exit 0 at both stages, so only reading the output finds
it. Across those three documents only 1 of the 15 operations carrying the shapes
they were ranked for reaches the generated client — and that document was the
census's **#1-ranked candidate** for `matrix-array`, `matrix-object`,
`label-array-or-object` and `cookie-array`. A byte-match fixture on it would have
proved almost nothing about the shapes it was selected for.

### 28 candidates generated a complete, valid, *empty* SDK

Exit 0, packaged, zero endpoints. Seven had no `paths` at all and could never have
been fixtures. The other **21 declared operations that never arrived**, almost all
behind a Path Item `$ref` (`AppcentMobile/medusa` declares 158,
`trajectoryjp/cudi-oss` 98, `1024XEngineer/XE3-ESL` 85, `stellar/stellar-docs`
46) — and **11 of those printed no failure marker at all**. An empty SDK witnesses
no feature, so a screen reading exit codes alone would have proposed several of
them as primaries.

### `fern check` passing does not mean the generator will

Nine of 115 in the auth-and-responses screen, from two distinct causes:

- **AWS-shaped specifications** die with
  `KeyError: 'type_:<Operation>RequestXAmzTarget'` inside the generator —
  `amazonaws.com:cloudtrail@2013-11-01`, `codedeploy@2014-10-06`,
  `codecommit@2015-04-13`, and non-AWS `gh:kciceblue/sshserver` with
  `KeyError: 'type_:GetHealthRequestJatProtocolVersion'`. Not all AWS
  specifications: `cloudfront@2016-11-25` and `redshift@2012-12-01` generate
  cleanly. The cause was not diagnosed; only that it reproduces.
- **Emitted Python that does not parse.** Five documents fail the generator's own
  `ruff check --fix --no-cache --ignore E741 /fern/output` step. The clearest is
  `gh:koxudaxi/fastapi-code-generator:tests/data/openapi/coverage/python_literal_escaping.yaml`,
  a code-injection test fixture whose path template makes Fern emit
  `"items/'+(__import__("os").system("path") or "")+'/detail"` into
  `raw_client.py` — a `SyntaxError`. It was the census's top 418 candidate.

### A Fern overrides fragment is not a specification

`aabiro/xcelsior:fern/openapi-overrides.yml` was counted by the census at 290
operations and 211 `x-fern-ignore` occurrences. It passes both stages and emits 26
`.py` files with **zero** `types/` modules — the runtime scaffold and nothing else;
a one-operation probe emits 30. An `openapi-overrides.yml` fragment cannot serve as
a fixture.

## Structure and media

### Fern silently discards every Path Item `$ref` that is not a remote URL

A two-path probe with one inline operation and one
`$ref: "#/components/pathItems/ViaRef"`, everything resolvable inside the single
file: `fern check` exit 0 `All checks passed`, `fern generate` exit 0, and the
emitted client has `def get_inline` and **no** `def get_via_ref`. Nothing is
reported. This is worse than the "unresolved reference" failure it looks like: it
also happens when the reference is internal and perfectly resolvable.

Reproduced on every real candidate carrying the shape:

| document | declared | emitted |
|---|---|---|
| `SecondBox` | 48 inline + 5 by internal ref | 48 |
| `0rkx/codex-openai-bridge` | 5 + 10 | 5 |
| `apache/apisix` | 6 + 1 | 6 |
| `Sakayori-Iroha-168/Software_Teamwork` | 2 + 22 | 2 |
| `ga4gh/tool-registry-service-schemas` | 10 + 1 **remote-URL** ref | **11** |

A **remote-URL** Path Item `$ref` is the one form that survives.

### Fern emits no client method for `options` or `trace`

An eight-method probe — one path, all eight OpenAPI methods, each with its own
`operationId` — generates a six-endpoint SDK: `get`, `post`, `put`, `patch`,
`delete`, `head`. `options_thing` and `trace_thing` are absent, `fern check` exits
0 with `All checks passed`, and nothing is reported. A fixture named for either
method would pin *Fern emitting nothing* — still a real regression guard, but the
fixture note would have to say so. No row this round registers carries either
method. crozier's `PathItem` (`src/openapi.rs`) deserializes exactly the six
methods Fern emits, so the two already agree by construction.

### A multi-document specification cannot be registered today

The blocker is the **Fern workspace**, not the fetcher. Three facts about this
repository, unchanged by the screen:

1. `scripts/fern-goldens` validates each `CORPUS.md` URL and refuses a path that
   does not end in `.json`/`.yaml`/`.yml`; its `fetch_spec` then requires exactly
   one spec path pointing at an existing non-empty file.
2. `scripts/corpus-lib.sh` does have a repository-clone shape
   (`corpus_fetch_repo`, a `git clone --filter=blob:none` at the pinned ref), but
   the suffix check in (1) makes it unreachable from the golden path — and all 81
   numbered `CORPUS.md` rows are direct spec URLs anyway.
3. `scripts/generate-fern-fixture.sh` copies the one spec file into the workspace,
   leaving its siblings behind.

Given the tree, **Fern resolves relative-file `$ref`s perfectly well**: the
`Foxcapades/softask-api-doc` entry document emits **0** endpoints when fetched
alone, and **31**, across six sub-clients, with its `v1/` tree present in the
workspace.

Three registration shapes would answer this. Each is a decision for the
maintainer, not a lookup:

- **(a) Register a pre-bundled single document.** Some repositories commit one
  (`trajectoryjp/cudi-oss` has `docs/openapi/cudi/gen/bundled.yaml` beside its
  split source). Needs no crozier change and fits the existing `github-raw` method
  exactly — the bundled document gave byte-for-byte the same `fern check` verdict
  as the tree probe (exit 1, the same single `CreateSaleScoped`/`sales_channel_id`
  error, the same 8 warnings). What it does **not** do is exercise multi-document
  resolution: crozier would be handed a flat document, exactly as Fern is.
- **(b) Register the entry document and accept the loss.** This is what happens
  today if such a URL is registered: Fern generates cleanly and the golden omits
  every operation behind a reference. Legitimate only if the row records that the
  golden pins Fern's silent drop.
- **(c) Teach the workspace about a tree** — a manifest cell naming the spec
  directory plus its entry document, `validate_url` accepting it, and
  `generate-fern-fixture.sh` copying the tree. A small, real crozier change; the
  `softask` probe above establishes it would work.

### A `$ref` key is not always a reference

Three of the census's ranked candidates did not carry the shape they were ranked
for, because the census's feature keys are textual matches on a `$ref` key:

- `factset/enterprise-sdk` — 3 counted relative-file and 9 remote-URL refs are
  SCIM data fields literally named `$ref` **inside request-body examples**;
- `Relequestual/openapi-diff-testing` and `fern-api/swift-sdk-comparison` — the
  single counted relative-file ref is Redoc's
  `x-topics[0].content.$ref -> ./docs/getting-started.md`, a pointer to markdown;
- `gematik/api-erp` — all 17 counted remote-URL refs sit inside a media-type
  `example`.

Screen gap membership from the parsed document, not from a census key.

## Naming and types

### Non-ASCII identifiers split three ways, and the middle case is the dangerous one

Each probe is a minimal OpenAPI 3.0.0 document differing from the others in one
identifier, run `fern check` → `fern generate` → `python3 -m py_compile` over every
emitted module:

| probe | identifier under test | `fern check` | `fern generate` | verdict |
|---|---|:--:|:--:|---|
| `schema-name` | schema `気温` | **1** | 1 | **refuses** — `issue: Type name must begin with a letter` |
| `schema-name-mixed` | schema `気温Data` | **1** | 1 | **refuses** |
| `enum-value` | enum members `暑い`, `寒い` | **1** | 1 | **refuses** |
| `property-name` | property `気温` | 0 | **1** | **emits invalid Python** |
| `property-name-cyrillic` | property `температура` | 0 | **1** | **emits invalid Python** |
| `property-name-greek` | property `θερμοκρασία` | 0 | **1** | **emits invalid Python** |
| `param-name` | query parameter `気温` | 0 | **1** | **emits invalid Python** |
| `operationid` | operationId `天気取得` | 0 | **1** | **emits invalid Python** |
| `schema-name-ascii-lead` | schema `Data気温` | 0 | 0 | normalizes → `class Data` |
| `schema-name-latin1` | schema `Medicação` | 0 | 0 | normalizes → `class Medicacao` |
| `property-name-mixed` | properties `a気温b`, `温度C` | 0 | 0 | normalizes → `a_b`, `c` |
| `property-name-latin1` | property `preço` | 0 | 0 | normalizes → `pre_o` |
| `info-title` | `info.title: 推奨データセット` | 0 | 0 | accepted; never reaches an identifier |
| `path-segment` | path `/天気/current` | 0 | 0 | accepted; emitted verbatim as a URL string |

The middle block is the dangerous one: `fern check` passes and the **generator
fails on its own output**. Every probe that generated also passed
`python3 -m py_compile` on every emitted module (exit 0), so "emits invalid Python"
is Fern failing on what it wrote, not an artefact of how it was checked.

### Float, list and object enum members are accepted and the enum is discarded

| probe | enum declared | `fern check` | `fern generate` | emitted |
|---|---|:--:|:--:|---|
| `enum-member-float` | `[1.5, 2.25]` | 0 | 0 | `Kind = float` — no members |
| `enum-member-list` | `[[a,b],[c,d]]` | 0 | 0 | `Kind = typing.List[str]` |
| `enum-member-object` | `[{a:1},{b:2}]` | 0 | 0 | `Kind = typing.Dict[str, typing.Any]` |

No `Literal`, no members, nothing reported. A golden here pins the *absence* of the
enum.

### Seven naming and type gaps have no complete proposable set, for four reasons

| gap | reason |
|---|---|
| `nonascii-schema-name` | **Fern refuses the shape** — all nine licence-defensible candidates fail `fern check` |
| `nonascii-param-name` | **Fern emits invalid Python** — all three candidates fail |
| `nonascii-path-segment` | **zero documents in the pool carry it**, and Fern handles it anyway: a path segment is emitted verbatim as a URL string |
| `nonascii-operationId` | pool exhausted at 1 eligible (`naming.nonascii.operationId`: 10 documents, A=1 B=4, 5 untiered) |
| `enum-member-float` | pool exhausted at 2 eligible (`types.enum.member.float`: 353 documents, B=2, 351 untiered) |
| `enum-member-object` | pool exhausted at 1 eligible (`types.enum.member.object`: 6 documents, A=1 B=1, 4 untiered) |
| `enum-member-list` | both clean generates are licence **tier Q**, quarantined — a do-not-propose rule, not a gap in verification |

Every tier A/B document in the three exhausted pools was examined. Widening any of
them means extending the census's licence tiering to documents it never tiered,
which is census work rather than screening work — for `types.enum.member.float`
alone that is 351 documents.

## Measurement caveats that outlive this round

### Witness count and witness *independence* are different measures

The screens reported how many documents witnessed a shape; they did not report how
many **independent** documents did, and the two come apart. Round 3 hit it twice:

- Statuses 505, 506, 508 and 511 each have five eligible, licence-clean,
  screen-verified witnesses emitting the same exception class — and those five are
  revisions of just two APIs, `amazonaws.com:cloudfront` (four revisions) and
  `amazonaws.com:redshift`.
- `Ekveer-Sahoo/kepel-xenia` and `jaccen/AIRoute` are forks of one document —
  188,400 against 188,477 bytes — and would otherwise have served as two
  independent backups for status 426.

A count of three witnesses is not a claim that three independent things agree.
Whether that matters depends on **what the fixture pins**. For an exception class
*name*, measured identical across every witness, a fork-family witness pins it just
as correctly as an unrelated one — so the count is the right measure and all four
statuses above were registered. For a fixture pinning a *shape*, it would not be.
Round 3 therefore applied independence one level down: to choosing among equally
eligible backups, where preferring two different documents over two forks costs
nothing — and not to deciding whether a gap is closable at all.

### The four screens applied different licence bars

The most reusable finding of the round, and no screen could see it from inside
itself. Joining the census's own licence pass (`licence-evidence.jsonl`, 1,066
records, 243 of them tier Q) to what each screen proposed shows the four disagreed
about what "verified" meant:

| screen | joined the licence pass? | candidates clean |
|---|---|---|
| naming-and-types | yes, and said so | 46 of 48 |
| serialization | yes — quarantined 11 of its 70 ranked candidates | 51 of 96 |
| structure-and-media | only partly | 31 of 54 |
| auth-and-responses | no | 18 of 39 |

Two exclusion reasons behind those numbers are **not** the same thing, and a reader
comparing screens will otherwise conflate them:

- **Licence tier Q** — the census *verified* that the document describes a
  third-party API whose licence is not the host repository's. This is the same
  distinction [`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md) already
  draws in rejecting `assemblyai-autosdk`.
- **Licence untiered** — the census never measured a licence for the document at
  all. Not a failed check but an absent one; Round 3 treats an unmeasured licence
  as ineligible rather than settling it mid-dispatch.

What the join cost, concretely: an MIT tutorial repository holding AbstractAPI's
specification; a CC0 catalogue holding HERE's under a "HERE Documentation
License"; three `mongodb/openapi` documents whose specification declares **CC
BY-NC-SA 3.0 US**; a permissive repository holding Google's under CC BY 3.0.

Two consequences worth recording so the supply is not re-searched:

- **`http-digest` has no redistribution-compatible witness at all** — a distinct
  empty reason from any the screens recorded, since all four of its verified
  witnesses fail the licence bar rather than failing Fern (three declare CC
  BY-NC-SA 3.0 US; one is tier Q).
- **`oauth2-implicit` is the near miss beside it**: its one licence-clean
  candidate, `xataio/xata`, declares zero operations, and an empty SDK is not a
  witness.

### Two exclusions a name-based filter does not catch

Both were missed by exclusion-by-repository-name and caught only by reading each
candidate's own `info.title` against the recorded do-not-retry names. The next
screen will need the same second pass.

- `atacan/AssemblyAI` (both `openapi.yaml` and `original_openapi.yaml`) and the
  `gr2m/ai-provider-monitor` cache copy are the **AssemblyAI** specification
  re-hosted in third-party repositories.
  [`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md) records
  `assemblyai-autosdk` as REJECTED because its *source* licence is
  revenue-limited, and a host repository's MIT or ISC licence does not change the
  licence of the specification it re-hosts.
- `open-feature/protocol:service/event-streams.yaml` is the same ref recorded
  DROPPED as `openfeature-protocol`, independently reproduced at `fern check`
  exit 1.

## What Round 3 did not register, and why

The round's main result. Round 3 registers a fixture only where **both** bars are
met:

1. **Semantic** — a screen must have measured Fern *implementing* the shape and
   emitting something that reflects it, and all three candidates must witness that
   same behaviour. A successful, non-empty generation is not that: it says the
   document generates, not that the feature reaches the output.
2. **Eligibility** — a verified primary and at least two verified backups, each
   with a pinned credential-free URL and a licence tier the census measured.

Four gaps clear both bars. **Fifty-five do not.** That ratio is the finding, and it
is the opposite of what issue #148 assumed: for most of this surface Fern either
discards the shape, ignores it, refuses it, or produces output that matches only by
coincidence with an unconditional default — and where it does none of those, no
screen measured what it emits.

`eligible` and `verified` below are the screens' own counts: how many candidates
the screen carried end to end (`verified`), and how many of those also clear the
census licence bar (`eligible`). A row whose verdict is **unmeasured** is an **open
question a future probe could answer**, not a proven absence.

| gap | eligible | verified | verdict | why no fixture was proposed |
|---|---:|---:|---|---|
| `apiKey-cookie` | 4 | 6 | discards | the importer drops the scheme outright; the client is generated from whatever other scheme the document declares |
| `apiKey-query` | 2 | 6 | discards + supply | as `apiKey-cookie`; and only 2 eligible of 6 verified — 4× licence tier Q — short of a primary plus two backups |
| `boolean-schema-true` | 4 | 4 | **unmeasured** | no screen measured what Fern emits for a boolean schema `true`; the verdict recorded is a non-empty generation |
| `components-links` | 2 | 4 | **unmeasured** | no screen measured Fern emitting anything derived from a `components.links` block |
| `components-pathItems` | 6 | 7 | discards | `components.pathItems` reaches the SDK only through a Path Item `$ref`, which Fern discards; the one candidate that loses nothing witnesses the *declaration* alone |
| `const-boolean` | 13 | 13 | **unmeasured** | no screen measured what Fern emits for a boolean `const`; the verdict recorded is a non-empty generation |
| `const-integer` | 7 | 8 | **unmeasured** | no screen measured what Fern emits for an integer `const`; the verdict recorded is a non-empty generation |
| `cookie-array` | 0 | 3 | discards + supply | cookie parameters are dropped from the client entirely; and 0 eligible of 3 verified — 3× licence untiered |
| `cookie-object` | 1 | 6 | discards + supply | as `cookie-array`; 1 eligible of 6 verified — 5× licence untiered |
| `cookie-parameter` | 7 | 7 | discards | cookie parameters are dropped from the client entirely; the warning does not fail `fern check` |
| `cycle-via-additionalProperties` | 3 | 3 | **unmeasured** | no screen measured what Fern emits for a map-of-self cycle; the verdict recorded is a non-empty generation |
| `deepObject-real-object` | 5 | 5 | **coincidence** | `query_encoder.py` flattens *every* dict-valued query parameter to `key[subkey]=value` unconditionally, and `form`, `pipeDelimited` and `deepObject` objects emit byte-identical code. A golden would pin the default, not style handling |
| `encoding-explode-or-allowReserved` | 3 | 3 | **unmeasured** | no screen measured Fern honouring `encoding.explode` or `encoding.allowReserved`; both fields measured at zero across the audited corpus and neither was probed |
| `encoding-object` | 4 | 6 | **unmeasured** | no screen measured Fern emitting anything derived from an `Encoding` object; the gap was closed on documents generating a non-empty SDK |
| `enum-member-float` | 2 | 2 | discards + supply | Fern accepts the schema and silently strips the enum, emitting `Kind = float` with no members; and only 2 eligible, pool exhausted |
| `enum-member-object` | 1 | 1 | discards + supply | as above, emitting `Kind = typing.Dict[str, typing.Any]`; only 1 eligible, pool exhausted |
| `explode-true-simple-header` | 0 | 0 | refuses | `fern check` refuses the header parameter that carries it, exit 1; no candidate carried end to end at all |
| `explode-true-simple-path` | 4 | 4 | ignores | the parameter is emitted but `explode` is ignored entirely on a simple-style path parameter |
| `header-array` | 0 | 0 | refuses | `fern check` refuses an array-typed header parameter, exit 1; no candidate carried end to end at all |
| `header-object` | 0 | 0 | crashes | `fern generate` crashes on an object-typed header parameter with an internal `KeyError`; no candidate carried end to end at all |
| `http-digest` | 0 | 4 | discards + licence | the importer drops the scheme outright; and 0 eligible of 4 verified — 3× the specification declares CC BY-NC-SA 3.0 US, 1× licence tier Q |
| `label-array-or-object` | 0 | 3 | discards + licence | Fern discards the `label` style and renders `str(list)` into the path segment; 0 eligible of 3 verified — 3× licence untiered |
| `link-description` | 5 | 9 | **unmeasured** | no screen measured Fern emitting anything derived from a Link object; the verdict recorded is a non-empty SDK, not that the Link reaches the output |
| `link-requestBody` | 2 | 3 | **unmeasured** | as `link-description`; the structure screen's own text records Link objects as absent from every audited document |
| `link-server` | 1 | 3 | **unmeasured** | no screen measured Fern emitting anything derived from a Link object |
| `matrix-array` | 0 | 4 | discards + licence | Fern discards the `matrix` style and renders `str(list)` into the path segment; 0 eligible of 4 verified — 4× licence untiered |
| `matrix-object` | 0 | 0 | discards | Fern discards the `matrix` style; no candidate carried end to end at all |
| `mutualTLS` | 2 | 6 | discards + supply | the importer drops the scheme outright; 2 eligible of 6 verified — 2× tier Q, 2× untiered |
| `nesting-depth-ge-15` | 6 | 6 | **unmeasured** | no screen measured what Fern emits at depth; the verdict recorded is a non-empty generation |
| `nonascii-info-title` | 5 | 5 | ignores | probed directly: `info.title: 推奨データセット` is accepted and never reaches an identifier, so nothing emitted derives from it |
| `nonascii-operationId` | 1 | 1 | crashes + supply | the generator emits invalid Python for a genuinely non-ASCII operationId; the one surviving candidate carries a Latin-1 accented one that folds, so it does not carry the shape |
| `normalization-collision` | 4 | 5 | **unmeasured** | no screen measured how Fern resolves a post-normalization collision; the verdict recorded is a non-empty generation |
| `oauth2-implicit` | 0 | 7 | supply | no eligible candidate carries the screen's verdict that Fern selected the flow; 0 eligible of 7 verified — 4× untiered, 3× tier Q |
| `oauth2-password` | 5 | 6 | supply | only two eligible candidates carry the screen's verdict that Fern *selected* the password flow; the others show Fern selecting a different scheme from the same document |
| `operation-security-alternatives` | 2 | 5 | ignores + supply | Fern collapses declared alternatives to a single credential — the first supported scheme — so the alternatives are not represented; 2 eligible of 5 verified — 2× tier Q, 1× OGC license |
| `options-operation` | 3 | 6 | discards | Fern emits no client method for `options` |
| `param-content-cookie` | 0 | 0 | discards | cookie parameters are dropped from the client entirely; no candidate carried end to end at all |
| `param-content-path` | 0 | 0 | discards | Fern collapses a `content:`-typed parameter to a bare `str`, losing the declared object; no candidate carried end to end at all |
| `pathitem-ref` | 7 | 7 | discards | only the **remote-URL** form resolves; every other form is silently discarded. Exactly one eligible candidate witnesses the resolving behaviour, and the available backups witness the opposite one |
| `pipeDelimited-array` | 7 | 7 | discards | Fern discards the declared style: the array emits as an httpx repeated key, `"probeParam": probe_param`, not pipe-joined |
| `pipeDelimited-object` | 1 | 7 | discards + supply | Fern discards the declared style; object query parameters are flattened regardless of it; 1 eligible of 7 verified — 6× licence untiered |
| `range-1XX` | 1 | 6 | discards + supply | a ranged response yields no error class at all; the operation falls through to `ApiError`; 1 eligible of 6 verified — 5× licence untiered |
| `range-3XX` | 3 | 5 | discards | a ranged response yields no error class at all |
| `range-4XX` | 5 | 6 | discards | a ranged response yields no error class at all |
| `range-5XX` | 4 | 4 | discards | a ranged response yields no error class at all |
| `relative-file-ref` | 2 | 2 | discards + pipeline | Fern discards a relative-file Path Item `$ref` when the document is fetched alone, and crozier's fixture pipeline cannot register the tree that would make it resolve; only 2 eligible |
| `server-description-multiword` | 15 | 16 | **unmeasured** | no screen measured the environment member names Fern derives from a server description |
| `servers-multiple-path-or-operation` | 2 | 5 | **unmeasured** | no screen measured what Fern derives from several servers below the root |
| `servers-three-levels` | 1 | 5 | **unmeasured** | no screen measured what Fern derives from a server override at each level |
| `spaceDelimited-object` | 0 | 6 | discards + licence | Fern discards the declared style; object query parameters are flattened regardless of it; 0 eligible of 6 verified — 6× licence untiered |
| `trace-operation` | 2 | 5 | discards + supply | Fern emits no client method for `trace`; 2 eligible of 5 verified — 3× licence tier Q |
| `type-array-multi-nonnull` | 8 | 8 | **unmeasured** | no screen measured what Fern emits for a 3.1 multi-type array; the verdict recorded is a non-empty generation |
| `x-fern-or-crozier-ignore` | 2 | 4 | supply | two of its four verified candidates are the AssemblyAI specification `CORPUS.md` records REJECTED, leaving two eligible |
| `xml-request` | 18 | 20 | **unmeasured** | no screen measured any XML-specific emission; the gap was closed on documents generating a non-empty SDK |
| `xml-response` | 20 | 24 | **unmeasured** | no screen measured any XML-specific emission; the gap was closed on documents generating a non-empty SDK |

### The eight HTTP statuses left unpinned

The rule is applied **per status rather than per document**: a status is pinned
only when three eligible witnesses each emit that same exception name for it, so a
row claiming several statuses has to be backed for every one of them separately.
Two rows this round registers name their backups per status, because no single
document witnesses both statuses they claim.

**428 is the one to read twice.** Issue #148 reasoned from RFC 6585 that
`PreconditionError` was likely wrong; the screens measured that it is exactly what
Fern emits; and it still cannot be pinned, because only two eligible witnesses
exist in the whole pool. Both halves are true — the name is correct, and no fixture
holds it.

| status | eligible | verified | class Fern emits | why no fixture was proposed |
|---|---:|---:|---|---|
| 407 | 0 | 0 | `ProxyAuthenticationRequiredError` (probe) | **zero pool documents declare it anywhere** in the eligible pool of 4,864. Probed directly, Fern generates it correctly — a corpus supply limit, not a Fern one |
| 414 | 0 | 1 | `UriTooLongError` | 0 eligible witnesses of 1 verified — short of a primary plus two backups |
| 417 | 2 | 2 | `ExpectationFailedError` | 2 eligible witnesses of 2 verified — short of a primary plus two backups |
| 418 | 1 | 4 | `ImATeapotError` | 1 eligible witness of 4 verified — short of a primary plus two backups |
| 421 | 0 | 0 | `MisdirectedRequestError` (probe) | **zero pool documents declare it anywhere** in the eligible pool of 4,864. Probed directly, Fern generates it correctly — a corpus supply limit, not a Fern one |
| 425 | 1 | 1 | `TooEarlyError` | 1 eligible witness of 1 verified — short of a primary plus two backups |
| 428 | 2 | 2 | `PreconditionError` | 2 eligible witnesses of 2 verified — short of a primary plus two backups |
| 431 | 1 | 1 | `RequestHeaderFieldsTooLargeError` | 1 eligible witness of 1 verified — short of a primary plus two backups |

In every row above the class name itself is **not** in doubt — it was measured
against Fern's output and matches crozier's table. What is missing is a
redistributable witness set to pin it.

## See also

- [`matching.md`](matching.md) — the byte-match contract these limitations bound,
  and why each shape crozier *does* generate generates the way it does.
- [`fern-goldens.md`](fern-goldens.md) — how a golden is produced and published.
- [`../tests/fixtures/AGENTS.md`](../tests/fixtures/AGENTS.md) — choosing a
  real-world specification, and the specs already tried and rejected.
- [`../tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md) — the corpus ledger,
  including every `DROPPED` / `REJECTED` ref this file refers to.
