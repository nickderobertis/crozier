# Canonical command surface for crozier. Keep this list small and memorable.
# `just bootstrap` must work from a clean clone; `just check` is the gate and
# must fail on any issue (no warnings-only mode). Every gate recipe delegates to
# the Nx project graph; the projects and their targets are the project.json files.

set positional-arguments := true

# List available recipes.
default:
    @just --list

# Set up from a clean clone: toolchain (from rust-toolchain.toml), deps, the pinned
# Nx (bun.lock), dev tools.
bootstrap:
    @rustup show active-toolchain >/dev/null 2>&1 || rustup toolchain install
    @rustup component add rustfmt clippy llvm-tools-preview >/dev/null 2>&1 || true
    cargo fetch --locked
    @just install-nx
    @./scripts/install-dev-tools.sh
    @./scripts/install-ruff.sh
    @git config core.hooksPath .githooks
    @echo "enabled .githooks (visual-regression pre-push guard)"

# Install the pinned Nx the gate runs through (bun.lock). Part of `bootstrap`;
# CI jobs that need Nx but not the rest of bootstrap call it alone.
install-nx:
    @command -v bun >/dev/null 2>&1 || { echo "install-nx: bun not found — install it (https://bun.sh), then rerun" >&2; exit 1; }
    bun install --frozen-lockfile

# The quality gate — one recipe, two tiers, the tier a flag on it. tools/ci/gate.mjs
# validates the base and selects the projects; the Nx command below runs over them:
#   just check            the affected tier: every gate target (format, lint, test,
#                         build, coverage, supply-chain, doc) of the projects a change
#                         since the base can reach. The base is NX_BASE (a ref name or
#                         commit SHA) or the merge base of HEAD with origin/main.
#   just check --sweep    the broader tier: the same targets over every project,
#                         promoted tiers included, uncached.
#   just check --plan     either tier's selection and Nx command, without running it.
# `--projects=` / `--exclude=` (names or tag:<tag>) scope either tier; CI uses them
# to run each promoted tier on the runner that holds its toolchain. Fails on any
# issue (no warnings-only mode); e2e is part of the gate, not opt-in.
check *args:
    @node tools/ci/gate.mjs "$@" -- nx run-many --targets=format,lint,test,build,coverage,supply-chain,doc

# What CI runs: the tier the GitHub event owes (tools/ci/ci-tier.mjs) — the
# broader tier on the release-plz release pull request, the affected tier against
# an explicitly derived base on every other pull request and on a push to main —
# then `check` with it. Arguments pass through to `check`.
ci-check *args:
    @node tools/ci/ci-tier.mjs -- "$@"

# Run Nx itself against this workspace (`just nx show projects`, `just nx graph`).
nx *args:
    @[ -e node_modules/.bin/nx ] || [ -e node_modules/.bin/nx.exe ] || [ -e node_modules/.bin/nx.cmd ] || { echo "nx: not installed — run 'just bootstrap'" >&2; exit 1; }
    @NX_DAEMON="${NX_DAEMON:-false}" NX_NO_CLOUD=true NX_TUI=false node_modules/.bin/nx "$@"

# Format check (does not modify files).
fmt-check:
    @just nx run-many --targets=format

# Every affected project's `lint` (clippy with warnings as errors, the module-
# boundary rule, the corpus/licence lints); `--sweep` for all of them.
lint *args:
    @node tools/ci/gate.mjs "$@" -- nx run-many --targets=lint

# Every affected project's `test`, then the 95% line-coverage floor over the crate
# (`workspace:coverage`, over the profiles `crozier:test` writes); `--sweep` for all.
# Lower the floor only with a reason in AGENTS.md.
test *args:
    @node tools/ci/gate.mjs "$@" -- nx run-many --targets=test,coverage

# End-to-end: drive the compiled binary the way a user runs it (assert_cmd),
# byte-comparing its stripped output to the committed Fern fixtures — the
# crozier-e2e project's `test`, which builds crozier first. `check` runs it
# whenever a change can reach it; this recipe runs the journeys in isolation.
test-e2e:
    @just nx run crozier-e2e:test

# SDK Python-environment tier: the e2e journeys (`sdk_env_*`, `#[ignore]`d so the
# offline crozier-e2e run never runs them) that build a virtualenv from PyPI for
# a generated SDK and run mypy or pytest in it — the runtime wire suite, the
# SDK's own-pin type-check, the shared env's concurrent first build, and the
# fern-refusals gate's `wire_test.py` condition: the `sdk-env` and `runtime`
# projects. Promoted out of the affected tier (it reaches PyPI); CI runs it in
# the `sdk-env` job, which `gate` requires. Needs Python (uv used when present).
test-sdk-env:
    @just nx run-many --targets=test --projects=sdk-env,runtime

# Runtime ("wire") test only — the `runtime` project: record the compiled
# client's behavior via an injected httpx.MockTransport (tests/runtime/) and
# assert it matches the real Fern fixture SDK's behavior, modulo the normalized
# SDK-identity headers. Part of `test-sdk-env`. Needs Python + httpx/pydantic/
# pytest (uv or pip); see tests/runtime/AGENTS.md.
test-runtime:
    @just nx run runtime:test

# Live e2e: boot a Prism OpenAPI mock server from each fixture's spec and drive the
# generated SDK through every documented endpoint, asserting a value of the method's
# declared return type comes back over real HTTP. Spec-driven (the endpoints and
# example args come from the SDK's generated reference.md), so it grows to more
# fixtures via conftest.FIXTURES. The `live-e2e` project: promoted out of the
# affected tier (Prism comes from npm, the venv from PyPI); `check --sweep` and
# CI's required live-e2e leg run it. Needs Node/Prism + uv + ruff; see
# tests/live_e2e/AGENTS.md.
test-live-e2e *args:
    @just nx run live-e2e:test "$@"

# Enforce the real-world corpus byte-match over the committed sources — the
# corpus-match project's `test-match` (tests/corpus_match/match.sh, which
# states the contract and holds the per-corpus list). CI runs it in the
# live-e2e leg.
test-corpus-match:
    @just nx run corpus-match:test-match

# The corpus byte-match with strict Fern compatibility on (docs/fern-refusals/):
# a refusal class that refuses a document Fern generates from fails it.
test-corpus-match-strict:
    @just nx run corpus-match:test-strict

# Format the codebase in place: every project's `format` target, writing.
format:
    @just nx run-many --targets=format --configuration=write

# Supply-chain gate (Linux; run once, not across an OS matrix): cargo deny + machete.
supply-chain:
    @just nx run workspace:supply-chain

# Docs must build cleanly (broken intra-doc links are errors).
doc:
    @just nx run workspace:doc

# Upgrade dependencies, then re-run the gate over everything the update reaches.
upgrade:
    cargo update
    @just check

# Legacy reproduction aid for the offline seed; pass `exhaustive` to reproduce
# that historical container-generated target too. Numbered corpus maintenance
# uses the Fern goldens workflow; see docs/fern-goldens.md.
fixtures-refresh *args:
    ./tools/fern-goldens/fixtures-refresh.sh {{args}}


# Rebuild-only: fetch pinned corpus sources into .local/corpus or a supplied
# destination. Routine checks use committed copies; this is Fern maintenance.
fetch-corpus *args:
    ./tools/corpus/fetch-corpus.sh {{args}}


# Legacy local reproduction for issue #77 goldens. Routine generation and safe
# publication belong to the Fern goldens workflow. Needs Docker + fern.
fixtures-generate-corpus *args:
    ./tools/fern-goldens/generate-corpus-fixtures.sh {{args}}

# Local diagnostic for the workflow lifecycle: resolve an exact generator tag,
# generate every selected corpus independently, then aggregate all Crozier byte
# diffs. `--fixture NAME` may be repeated; omitting it selects existing goldens.
fern-goldens *args:
    ./tools/fern-goldens/fern-goldens run "$@"

# Phase recipes used by the workflow so successful goldens can be published
# before generation/diff failures determine the final status.
fern-goldens-generate *args:
    ./tools/fern-goldens/fern-goldens generate "$@"

fern-goldens-compare:
    ./tools/fern-goldens/fern-goldens compare

fern-goldens-publish branch:
    ./tools/fern-goldens/fern-goldens publish --branch "$1"

fern-goldens-result *args:
    ./tools/fern-goldens/fern-goldens result "$@"

# Process/filesystem/workflow-boundary coverage for the automation itself.
test-fern-goldens:
    @just nx run-many --targets=test --projects=fern-goldens,fern-goldens-git

# Live Fern measurement for the witness-supply probe Fern refuses. Separate
# from `check`: Fern's pinned Python generator runs in Docker and needs network.
test-fern-probe-refusal:
    @just nx run crozier-e2e:fern-probe-refusal

# Process/filesystem/test-selection-boundary coverage for `fixtures-coverage`.
# Drives the real recipe under a SCOPE so it measures a handful of tests instead
# of the whole corpus; the unmeasured thing would otherwise be the measurement.
# Part of `check` (the recipe itself is not — it needs network and is slow).
# The hand-written reach recipe is driven the same way, over temporary fixtures;
# both build crozier instrumented, so they are the surface-reach project's. The
# golden-reach suite runs twice: the second time without `fcntl` and the other
# POSIX-only modules, as on Windows, on every host.
test-fixtures-coverage:
    @just nx run-many --targets=test-fixtures-coverage --projects=surface-census,surface-reach

# The arm search's YAML fallback against the census's stdlib loader: identical
# counts on every registered YAML source, and each refused form's committed sample
# (`tools/surface-census/tests/data/census-fallback-sample/`) read as what it declares. Fetches no
# specification; `test-corpus-offline` runs it with sockets denied.
test-census-fallback-samples:
    @just nx run census-fallback:test-samples

# The samples above, then the arm search and the witness-search re-census CLI
# over temporary ledgers, a loopback GitHub and Sourcegraph, and the same pinned
# parser. Promoted out of the affected tier — it installs the pinned ruamel.yaml
# (read from each script's own inline metadata) through uv; `check --sweep` and
# CI's live-e2e leg run it.
test-census-fallback:
    @just nx run census-fallback:test

# Census aid: report the exact expected files crozier still does not reproduce.
# The output is the ready-to-paste `unmatched` task list. Not part of `check`.
# The crozier-e2e project's `fixtures-gaps` (crates/crozier-e2e/fixtures-report.sh,
# whose summary-line drift gate turns a renamed reporter into a hard failure).
fixtures-gaps corpus="":
    @CROZIER_GAPS_CORPUS="{{corpus}}" just nx run crozier-e2e:fixtures-gaps

# Backward-compatible alias for the former reporter name.
fixtures-candidates corpus="":
    just fixtures-gaps "{{corpus}}"

# Mismatch-investigation aid: print the unified diff of every committed fixture
# file crozier does NOT reproduce byte-for-byte — exactly what the gate's
# comparison engine decides on (`-` = Fern golden, `+` = crozier; comments
# stripped and every catalog departure already applied), so what you see is what
# to fix. Optional args narrow scope: `just fixtures-diff <corpus> <file-substring>`.
# Not part of `check`; see tests/fixtures/AGENTS.md.
fixtures-diff corpus="" file="":
    @CROZIER_DIFF_CORPUS="{{corpus}}" CROZIER_DIFF_FILE="{{file}}" just nx run crozier-e2e:fixtures-diff

# Regenerate the per-golden departure ledger, tests/fixtures/departures-ledger.tsv
# (crates/crozier-e2e/departures-ledger.sh says how). Run it after a change that
# adds, moves or removes a departure, and review the diff before committing; see
# docs/departures/README.md.
departures-ledger:
    @just nx run crozier-e2e:departures-ledger

# Measure what the committed Fern GOLDENS reach in src/, apart from what
# crozier's own tests reach — the number that answers "which fixture next?".
# Outside `check`: needs network and runs the whole corpus instrumented. Takes an
# optional cargo-nextest filter expression to scope it. Reading the split:
# tests/fixtures/AGENTS.md.
fixtures-coverage *args:
    ./tools/surface-census/fixtures-coverage.sh "$@"

# Per `golden` census row: which of crozier's declared handling sites for it
# (docs/openapi-surface/golden-reach-sites.tsv) the row's own witnesses execute
# in the golden-only tier, one instrumented run per golden test. Writes the
# ranked ledger (docs/openapi-surface/golden-reach.tsv) and every golden row's
# reach cell. Outside `check`: runs the corpus instrumented.
golden-reach:
    python3 tools/corpus/corpus_sources.py check
    python3 tools/surface-census/golden-reach.py measure
    "$(./scripts/census-python.sh)" ./tools/surface-census/openapi-surface-census.py --json > .local/golden-reach/census.json
    python3 tools/surface-census/golden-reach.py report --write

# Re-join the last `just golden-reach` measurement after the site table changes.
golden-reach-report:
    python3 tools/surface-census/golden-reach.py report --write

# Which generated files each `golden` row resting only on a residual golden
# (komga, short-io, webflow-v2) lands in, split by whether that golden test
# byte-compares them: renders the witness with the feature perturbed and diffs
# crozier's two outputs. Restated in docs/openapi-surface-coverage.md. Outside
# `check`: it needs a built crozier and ruff.
residual-attribution:
    cargo build --locked -q
    python3 tools/surface-census/residual-attribution.py

# Per arm-level cover of a hand-written fixture (docs/openapi-surface/handwritten/AGENTS.md):
# how many regions of its arm an instrumented crozier run over that fixture's
# openapi.yml alone executes, one run per fixture as `golden-reach` scopes one
# golden test. Writes docs/openapi-surface/handwritten-reach.tsv, and for a
# fixture declaring a setting, its arms with and without it into
# handwritten-config-gates.tsv. Outside `check`, like `golden-reach`: it builds
# and runs crozier instrumented. `--handwritten-dir DIR --ledger PATH --gates
# PATH` measure another tree into other files.
handwritten-reach *args:
    python3 tools/surface-census/handwritten-fixtures.py measure "$@"

# Census which OpenAPI shapes the registered golden sources DECLARE — the input
# to docs/openapi-surface-coverage.md, and the only measurement of what the
# corpus has never seen. Walks each source document's object model (never its
# generated expected/ tree, never a text match) and prints one row per
# (selector, fixture, count). Reads the committed source copies. The script's own flags pass straight through, e.g.
# `just surface-census --selector pathItem.trace --json`.
surface-census *args:
    "$(./scripts/census-python.sh)" ./tools/surface-census/openapi-surface-census.py "$@"

# Boundary coverage for `surface-census`: drives the REAL script over the REAL
# vendored source documents, offline, so the gate keeps the instrument honest
# without the network the unscoped recipe needs. Part of `check` (the recipe
# above is not). Same split as test-fixtures-coverage vs fixtures-coverage.
test-surface-census:
    @just nx run surface-census:test-census

# Screen every APIs.guru catalogue version for the owned surface-gap selectors.
apis-guru-gap-screen *args:
    "$(./scripts/census-python.sh)" ./tools/surface-census/apis-guru-gap-screen.py {{args}}

# The corpus's admissible-licence rule is stated in ONE file,
# docs/corpus-licensing.md. This fails when any other tracked Markdown document
# enumerates the admissible licences again — the drift that left a dozen copies
# of the old set and no source. Prose that REFERS to the rule is fine; a second
# list of licence names is not. Part of `check`.
lint-corpus-licensing:
    @just nx run corpus-licensing:lint-licensing

# Boundary coverage for that gate: drives the REAL script over the REAL tree,
# and over the real tree with a second enumeration planted in it, so a check
# that had stopped discriminating fails here instead of passing silently.
# Part of `check`.
test-corpus-licensing:
    @just nx run corpus-licensing:test

# A corpus row whose document names another document by absolute URL is only
# reproducible if that URL is immutable. tests/fixtures/corpus-remote-ref-pins.tsv
# records the substitutions that make it so; this is the offline gate over the
# manifest itself — well-formed records, real corpus names, immutable pinned URLs,
# no duplicates, sorted. No network. Part of `check`.
lint-corpus-remote-ref-pins:
    @just nx run corpus:lint-remote-ref-pins

# Boundary coverage for the pin MECHANISM, which the manifest cannot prove: the
# corpus-fetch project drives the REAL tools/corpus/fetch-corpus.sh against a
# loopback HTTP server the suite starts itself, so real curl and the real
# filesystem publish a real document; the corpus project holds the offline
# lint's malformed-manifest cases. No test reaches GitHub, so `check` takes a
# loopback socket and no external host. Part of `check`.
test-corpus-remote-ref-pins:
    @just nx run-many --targets=test-remote-ref-pins --projects=corpus,corpus-fetch

# Every registered corpus row's source document is committed under
# tests/fixtures/corpus-sources/, recorded with the SHA-256 of the bytes fetched
# at its pinned revision in tests/fixtures/corpus-sources.tsv, so no gate fetches
# one. This is the offline gate over those copies: every row committed and
# recorded, every byte at its digest, every multi-document file present, no
# stray file. No network. Part of `check`.
lint-corpus-sources:
    @just nx run corpus:lint-sources

# Boundary coverage for that gate and for the rebuild tooling below: the real
# tree, a synthetic root broken one demand at a time, and `vendor`/`audit`
# through the real fetch against a loopback server (the corpus-fetch project's
# half, since it runs real curl). Part of `check`.
test-corpus-sources:
    @just nx run-many --targets=test-sources --projects=corpus,corpus-fetch

# Linux CI proof: run the real byte-match, census, refusal and census-fallback
# sample recipes with sockets denied and the ignored corpus caches absent. Does
# not fetch a specification (cargo fetches the locked crates and uv the pinned
# parser first).
test-corpus-offline:
    @just nx run corpus-match:test-offline

# Rebuild-only: `vendor --fixture NAME` fetches a row from its pinned URL and
# commits its source (run it when a row is added or its pin moves); `audit`
# re-fetches and compares without writing. Needs network; never part of a gate.
corpus-sources *args:
    python3 tools/corpus/corpus_sources.py "$@"

# The screening record for the widened admissible-licence rule,
# docs/licence-rescreening.md: one line per candidate the six region files
# record as blocked on a licence. This fails when a line omits its admission
# verdict, the reason behind it, the ref it was screened at, either half of the
# Fern screen, or names a coverage row no region file carries. Part of `check`.
lint-licence-rescreening:
    @just nx run corpus:lint-licence-rescreening

# Boundary coverage for that gate: drives the REAL script over the REAL record,
# then over a record breaking each demand in turn, so a gate that had stopped
# discriminating fails here instead of passing silently. Part of `check`.
test-licence-rescreening:
    @just nx run corpus:test-licence-rescreening

# The Fern refusal registry's population tables (docs/fern-refusals/) against
# the committed records they are built from: tools/fern-refusals/fern-refusals.py `check`
# over the real tree, `build` reproducing it, and drift cases that must fail, plus
# `measure` with the freshly built crozier (fern-refusals-strict).
test-fern-refusals:
    @just nx run-many --targets=test --projects=fern-refusals,fern-refusals-strict

# Measure the Fern refusal population (docs/fern-refusals/): fetch each document,
# run Fern and crozier over it. Rebuilds the release binary first, so crozier's
# counts come from the current tree. Network + Fern (`just setup-fern`).
fern-refusals-measure *args:
    cargo build --release --locked --bin crozier
    python3 tools/fern-refusals/fern-refusals.py measure {{args}}

# Install/refresh the llmlint toolchain (oneharness + llmlint). Idempotent.
setup-llmlint:
    ./scripts/setup-llmlint.sh

# Re-fetch every plugin `llmlint-plugins/lock.json` records, at its recorded
# `@pin`, and rewrite the vendored copies + the lock. This is the ONLY way an
# upstream rule change reaches the judged tier — it lands as a reviewable diff
# rather than on whatever the network answers mid-PR. Needs network + llmlint.
# See docs/llmlint-plugins.md.
# Refresh the vendored llmlint rule plugins and their lock.
llmlint-plugins-refresh:
    ./tools/llmlint/llmlint-plugins.py refresh

# Boundary coverage for that plugin set: drives the REAL llmlint over the REAL
# llmlint.yml with the plugin origin refused (a proxy at a closed port, a cold
# cache), so a job-time fetch reintroduced into the config fails here instead of
# failing a required PR check on a flaked connection. Part of `check`; skips
# where llmlint is absent unless CROZIER_REQUIRE_LLMLINT=1, which CI's llmlint
# job sets so the step cannot no-op.
# Prove the judged tier resolves its rules with the plugin origin unreachable.
test-llmlint-plugins:
    @just nx run llmlint-tooling:test-plugins

# Set up local Fern-golden reproduction (Fern CLI, Docker daemon, release binary).
# Idempotent; also run by the SessionStart hook. The hosted workflow is the normal
# maintenance path. See docs/fern-goldens.md.
setup-fern:
    ./scripts/setup-fern.sh

# LLM-judge lint (llmlint) — non-deterministic, harness-backed; kept OUT of
# `check`. Run on demand over the configured set (or pass paths). See llmlint.yml.
lint-llm *paths:
    @command -v llmlint >/dev/null 2>&1 || { echo "llmlint not installed — run 'just setup-llmlint'"; exit 1; }
    llmlint {{paths}}


# Deterministic llmlint config/ignore/version-bump validation.
lint-llm-validate *args:
    PATH="$HOME/.local/bin:$PATH" llmlint validate {{args}}

# `--diff` lints only what this branch introduced against the merge base, and
# honors llmlint.yml's excludes. llmlint hands one rule batch every changed file,
# so tools/llmlint/llmlint-diff.py splits a diff too large for the judge into file
# batches it can hold, and runs the one plain invocation otherwise.
# Blocking `llmlint` PR check; run before pushing. BASE defaults to origin/main.
lint-llm-diff base="origin/main" *args:
    python3 tools/llmlint/llmlint-diff.py {{base}} {{args}}

# Offline tests of the batching wrapper, against a stub llmlint.
test-llmlint-diff:
    @just nx run llmlint-tooling:test-diff

# --- Terminal screenshots (informational; never part of `check`) --------------
# Deterministic SVGs of the real CLI output, rendered by `freeze` from a vendored
# pinned font and gated/galleried/PR-commented by screencomp. Regenerating is out
# of the gate; CI's Visual-docs workflow owns the comparison, and the pre-push
# guard re-captures locally on drift. See screenshots/AGENTS.md.

# Install the screenshot renderer (`freeze`) on demand, pinned to `.freeze-version`
# (the single source of truth CI's Visual-docs capture reads too). Needs Go.
screenshots-tools:
    @command -v go >/dev/null || { echo "go not found: needed to install freeze; see https://go.dev/dl" >&2; exit 1; }
    go install github.com/charmbracelet/freeze@v"$(cat .freeze-version)"
    @echo "installed freeze to $(go env GOPATH)/bin (ensure it is on PATH)"

# Capture the screenshots: drive the real binary against screenshots/petstore.yml,
# render each scene to shots/current/<arch>/ + docs/screenshots/. Needs `freeze`
# and `ruff` on PATH (the latter is crozier's generation-time dependency).
screenshots:
    @bash scripts/screenshots.sh

# Regenerate the animated demo GIF (docs/screenshots/demo.gif — the README hero:
# a real `generate` run, then the generated enum streaming in). Drives the REAL
# release binary against the demo spec, then draws faithful frames with the
# vendored JetBrains Mono font (Pillow only — no ttyd/ffmpeg). Informational, NOT
# hash-gated (a GIF isn't byte-reproducible), so regenerate on demand and commit
# the result. Needs Python 3 + Pillow (`pip install Pillow`).
screenshots-gif:
    @command -v python3 >/dev/null || { echo "python3 not found: needed to render the demo GIF" >&2; exit 1; }
    @python3 -c "import PIL" 2>/dev/null || { echo "Pillow not installed: pip install Pillow" >&2; exit 1; }
    cargo build --release --locked --bin crozier
    python3 screenshots/demo-gif.py

# Refresh the committed baseline manifest from a fresh capture (after an intended
# output change). Commit shots/baseline/*.json + docs/screenshots/ alongside.
screenshots-bless: screenshots
    @command -v screencomp >/dev/null || { echo "screencomp not installed: https://github.com/nickderobertis/screencomp#install" >&2; exit 1; }
    screencomp manifest --input shots/current --output shots/baseline/$(uname -m | sed 's/amd64/x86_64/;s/aarch64/arm64/').json
    @echo "baseline refreshed; commit shots/baseline/ + docs/screenshots/"

# Validate the witness ledger and its CLI against real temporary documents.
test-witness-search-redo:
    @just nx run witness-search:test-redo

# Drive witness-search acquisition, census and ledger derivation through the real CLIs.
test-witness-search-acquisition:
    @just nx run witness-search:test-acquisition

# Offline HTTP journey for the GitHub/Sourcegraph witness acquisition path.
test-witness-search-github:
    @just nx run witness-search:test-github

# The measured screening stage both witness-search families file screens through:
# its CLI over a loopback raw-GitHub server and a stub `fern`, and the legacy
# index reading what it files.
test-witness-screen:
    @just nx run witness-search:test-screen

# Take one legacy witness-search candidate's licence, ref and Fern screens, measured.
# Network (the guarded raw route) and Fern (`just setup-fern`).
witness-screen *args:
    @"$(./scripts/census-python.sh)" ./tools/witness-search/witness_screen.py "$@"

# Canonical reproduction entry point; archived evidence retains original commands.
witness-search-local-census *args:
    @"$(./scripts/census-python.sh)" ./tools/witness-search/witness-search-local-census.py "$@"

# Drives the real module against a local HTTP server serving authored responses.
# Offline tier for the GitHub/Postman/Sourcegraph rate-limit guard.
test-rate-limit-guard:
    @just nx run witness-search:test-rate-limit-guard

# Needs network (and GITHUB_TOKEN for the token's own buckets); never waits, so
# it stays out of `check`. Rule and interface: tools/witness-search/rate_limit_guard.py.
# Live GitHub REST bucket figures from one free /rate_limit read, plus paced-host spacing.
quota-status:
    @"$(./scripts/census-python.sh)" tools/witness-search/rate_limit_guard.py status
