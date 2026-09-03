# tests/fixtures/AGENTS.md

Folder-scoped notes for the golden fixture corpus. Layout, provenance, and the
gap manifest lives in [`README.md`](README.md) and
[`../../docs/matching.md`](../../docs/matching.md); the maintenance lifecycle is
[`../../docs/fern-goldens.md`](../../docs/fern-goldens.md). This file is the
judgment a script can't encode. See the root [`AGENTS.md`](../../AGENTS.md) for
the rest.

## Adding a fixture

Add one numbered [`CORPUS.md`](CORPUS.md) row and source URL per feature branch,
then wire a `Corpus` with `unmatched: &[]` into `tests/e2e.rs`, plus its
`#[test]` and its `just test-corpus-match` line —
`every_registered_corpus_is_wired_into_the_gate` fails without both, because a
corpus nothing runs is not coverage. Generate the golden with **Route A**, the
local Docker loop (`just fern-goldens-generate --version "$pin" --fixture
<name>`, always with the exact pin the goldens' provenance records — never a
blank, which resolves the latest tag and starts a Fern upgrade), then measure,
repair Crozier, and repeat; red comparison is expected until Crozier is repaired.
A dispatched agent cannot use the hosted workflow, because a dispatch needs the
branch on the remote and publication is the lifecycle's job. A Monday 05:17 UTC
run from `main` leaves both inputs blank to check the latest Fern against every
managed golden. Do Fern upgrade work on an expected-red feature branch, retain
the workflow's best-effort successful commits and exact known-failure evidence,
then rerun with the resolved exact version until the final run is green with no
changes to generate or publish. The complete selection, provenance, partial-success,
publication, and rerun contract is in
[`../../docs/fern-goldens.md`](../../docs/fern-goldens.md).

**One non-default Fern setting is corpus-wide.** Every golden — managed or
hand-authored — is generated with `pydantic_config.enum_type: python_enums`,
which `scripts/generate-fern-fixture.sh` writes into `generators.yml`
unconditionally for *all* fixtures rather than per row. It is not a column of the
config table below and no fixture opts out; Fern records it in each golden's
`.fern/metadata.json` (`generatorConfig`), and because crozier renders that enum
shape unconditionally the e2e normalizes the block off both sides
(`tests/e2e.rs::normalize_metadata`). Regenerate through that script, never a
hand-rolled `fern generate`, or the golden silently comes back in Fern's
out-of-the-box open-`Literal`-union enum shape.

Per-fixture non-default settings live in **one shared table**,
[`fern-generator-config.txt`](fern-generator-config.txt) — a single file for the
whole corpus keyed by fixture name (`fixture|audiences|audience_strict|
client_class_name|extra_fields`), not a file per fixture directory. Both routes
otherwise use Fern's standard corpus generator configuration, and both load that
table by fixture name whether the spec is vendored or fetched, so a fixture
needing a non-default audience, client-class-name, or extra-fields setting adds
one row there and nothing else. A hand-authored fixture also gets the settings
recorded in its golden's provenance (`expected/.crozier-fern-golden.json`); a
`CORPUS.md` row's provenance is the manifest form (name, ref, URL, version), so
for a corpus row this table is the authority for what it was generated with.
Model and test a new setting there before regenerating; do not silently use
different defaults.

A generator setting no OpenAPI document can express is pinned by giving an
already-registered source a second row name with that declaration
(`eos.local-extra-fields-forbid` over `eos.local`), not by hunting a new spec.

## Choosing a real-world spec — Fern must accept it FIRST

A candidate is only viable if **Fern itself generates it cleanly** (`fern check`
passes); crozier byte-matching Fern's output is meaningless if Fern rejected the
spec. Fern's real gate is stricter than "valid OpenAPI", and most raw public specs
fail it, so **screen before you spend a Docker generate**. The two failure modes
that kill most specs:

- **Inline request-body name collisions.** Fern coins `<Operation>Request` for a
  request body defined inline (no `$ref`); two endpoints that coin the same name
  across sub-clients are a hard error (`X is already declared in Y.yml`). Specs
  whose request bodies are all `$ref`s to named `components.schemas` avoid this.
- **Example / declared-type mismatches.** A `format: date` field whose `example`
  is a full datetime (or an integer `enum` value with no `x-fern-enum` name) is a
  hard error. Screen `format: date` examples and numeric `enum`s.

A clean generate is still not enough on its own: check the shape you are buying
against [`../../docs/fern-limitations.md`](../../docs/fern-limitations.md), which
records what Fern 5.20.0 was measured to discard, ignore, refuse or match only by
coincidence — a golden cannot pin a shape Fern throws away — plus the two
exit-0-and-nothing-happened failure modes no exit code reveals: a check that
passes over an unparsed document, and a duplicate `operationId` that collapses
operations into one method.

An optional pre-screen can count, per operation, request bodies without a `$ref`
schema and `format: date` fields whose example contains a time. Zero of both is a
good signal, but a real Fern generate is the authoritative check: locally via
Route A, or via the dispatched workflow, which retains any successful sibling
results when another selection fails.

### Specs already tried and REJECTED (do not re-attempt without a fix upstream)

Fern rejected these raw specs — an agent burned a full generate on each, so they
are logged here to stop the next one repeating it. Fern's *own* published SDK for
these is built from a spec with Fern overrides applied, not the raw document.

| spec | source | why Fern rejects it |
|---|---|---|
| `deepgram` | `deepgram/deepgram-api-specs@main/openapi.yml` | 342 errors: duplicate inline `ListRequest` across sub-clients, and integer enums (`16000`, `48000`, …) with no `x-fern-enum` names |
| `asana` (api-guru `asana.com/1.0`) | already attempted by a prior agent too | 17 errors: inline request-body collisions (`AddFollowersRequest`, `RemoveFollowersRequest`, `ProjectSaveAsTemplateRequest`) and `date` fields with datetime examples |
| `xtrf.eu` (api-guru `xtrf.eu/2.0`) | `https://api.apis.guru/v2/specs/xtrf.eu/2.0/openapi.json` | Python 5.20.0 generator rejects seven response-example fields across `getJobFiles` and `getTaskFiles`, despite `fern check` passing |
| `github.com-ghes-3.8` (api-guru `github.com/ghes-3.8/1.1.4`) | `https://api.apis.guru/v2/specs/github.com/ghes-3.8/1.1.4/openapi.json` | Python 5.20.0 generator rejects 29 request collisions, examples, duplicate declarations, and enum names, despite `fern check` passing |
| `zerkerlabs-treeship` | `zerkerlabs/treeship@322a55f11e6799cf79b3dcf1bc1c874eb2630099/docs/content/docs/api/hub-openapi.yaml` | `fern check` exits 1 with ten `Endpoint requires auth, but no auth is defined` errors: its **only** security scheme is `type: http` with `scheme: DPoP`, which Fern's importer does not support, so every secured endpoint is left with no auth. Screened while settling `http-dpop`; the registered witness for that scheme is corpus row 96, which pairs `dpop` with `bearer` |
| `apache-iceberg-rest-catalog` | `apache/iceberg@ebebc345624a8f51c2e9caf4bb5624c79fb2656b/open-api/rest-catalog-open-api.yaml` | Python 5.20.0 generator rejects the `NotAcceptableError` example: required `message`, `type`, and `code` are missing and `error` is unexpected |

Accepted and matched corpus status lives in [`CORPUS.md`](CORPUS.md); do not
duplicate its batch ledger here.

## Shrinking `unmatched` — don't diff by hand

The corpus is at full byte parity: every `unmatched` list is empty, so a
non-empty one means work in flight, not an accepted state. `just fixtures-gaps`
generates every available corpus and reports the exact divergent files as
ready-to-paste `unmatched` arrays; land the generator fix and empty the list
again. Every expected file outside that list is gated, including files newly
emitted by Fern, and the comparison also walks Crozier's output back, so nothing
can be suppressed by omission. The reporter rejects stale entries that now match.
`fixtures-candidates` is retained as an alias.

A validated `known-fern-failure.json` is the only reason a registered corpus may
have no `expected/` tree; every other missing golden is a hard error. That
registration is bound to one exact generator version, corpus identity, exit code,
and diagnostic fingerprint, so it cannot be copied onto a corpus that merely
diverges — see `a_known_fern_failure_registration_cannot_excuse_anything_else`.
Such a corpus remains a spec-level robustness test until Fern
succeeds, at which point remove the failure registration and use the managed
workflow to publish a provenanced golden so it rejoins byte comparison.

## Where the goldens are BLIND — `just fixtures-coverage`

`unmatched` answers *"does crozier reproduce the goldens we have?"*. It cannot
answer *"what does no golden exercise at all?"* — and nothing else in the repo
distinguishes "a committed Fern golden proves this" from "a crozier test asserts
crozier agrees with its own expectation". `just fixtures-coverage` measures three
tiers against one instrumented build and prints them side by side, per `src/`
file, in counter regions and lines:

| tier | what a covered region there means |
|---|---|
| `golden-only` | Fern produced this output and crozier reproduces it byte for byte — **the only Fern-parity evidence that exists** |
| `all-e2e` | the goldens *plus* crozier's own journeys, which pin behavior against crozier's expectation, not Fern's |
| `non-e2e` | a unit/integration test asserts crozier agrees with itself |

Read it in this order when choosing the next fixture:

1. **The `golden blind spots` block at the bottom is the fixture backlog.** Every
   region it lists is generator behavior only crozier vouches for. The file with
   the biggest count is where a new corpus spec buys the most parity evidence;
   `just fixtures-diff` then tells you what that spec's shapes must contain.
2. **`all-e2e` minus `golden-only` is what the journeys add** — and it is not
   parity evidence, however large. First measured at v0.0.46: the goldens reach
   17,691 of 20,013 production regions (88.4%), all-e2e 18,815 (94.0%), non-e2e
   19,037 (95.1%), leaving 1,798 regions blind to every golden. The journeys
   supply about half of that (351 regions in `emit.rs`, 360 in `settings.rs`,
   220 in `openapi.rs`, 15 in `ir.rs`), but a journey pins crozier against
   crozier. Only a golden moves the `golden-only` column, so don't read a rising
   `all-e2e` figure as progress toward parity.
3. **Regions, not lines.** A `match` with forty unexercised arms reads as covered
   *lines* the moment the match head runs; each arm is its own counter region.
   The crate emits no branch records at all, so regions are the closest branch
   proxy available — treat the region column as the real number.
4. **Scope while iterating.** The unscoped run fetches the corpus and measures it
   all; `just fixtures-coverage 'test(/frankfurter/) or test(/wrap::/)'` reruns in
   seconds. Every tier must still select at least one test, or the recipe refuses.

Two things the figures are *not*: they are not a gate (nothing here fails a
build on a percentage), and they are not comparable to `just test`'s 95% line
floor — that one counts `#[cfg(test)]` code and every tier at once, which is
exactly the inflation this recipe removes. `just test-fixtures-coverage` (in
`check`) is what keeps the recipe honest: it drives the real script under a
scope, asserts the three tiers partition the suite exactly, and proves the
spawned binary's profile is captured by requiring non-zero coverage of
`src/main.rs`, which exists only inside that binary.

## Why a file *doesn't* match — `just fixtures-diff`

The inverse tool. `just fixtures-diff [<corpus> [<file-substring>]]` prints the
**normalized** unified diff of every fixture file crozier does *not* reproduce
(`-` = Fern golden, `+` = crozier). It diffs exactly the bytes the gate compares —
comments, SDK-identity headers, and `__init__.py` import order are already
normalized out — so a raw `diff tempdir fixture` won't mislead you with
differences the gate ignores. Narrow to one file with the substring arg while
iterating on the generator. The gate's own failure message prints the same diff
inline, so a regression outside `unmatched` is diagnosable straight from
`just test-e2e` without a second pass.

## Non-negotiable

- **`unmatched` holds only measured divergence, never an accepted one.** Never
  edit a committed fixture to match crozier — the fixture is Fern's golden
  output; fix the generator instead. `just fixtures-gaps` reports divergence and
  never rewrites fixtures.
- **Keep attribution.** The corpus is Fern's output (Apache-2.0); `../../NOTICE`
  and `../../licenses/fern-APACHE-2.0.txt` must survive any regeneration (the
  refresh scripts preserve them).
- **`.py` is comment-stripped, scaffolding is verbatim.** The comparison uses the
  same `crozier internal-strip` that produced the fixtures; that normalization is
  the *only* difference allowed between crozier's output and Fern's.
