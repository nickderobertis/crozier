# Canonical command surface for crozier. Keep this list small and memorable.
# `just bootstrap` must work from a clean clone; `just check` is the full gate
# and must fail on any issue (no warnings-only mode).

# List available recipes.
default:
    @just --list

# Set up from a clean clone: toolchain (from rust-toolchain.toml), deps, dev tools.
bootstrap:
    @rustup show active-toolchain >/dev/null 2>&1 || rustup toolchain install
    @rustup component add rustfmt clippy llvm-tools-preview >/dev/null 2>&1 || true
    cargo fetch --locked
    @./scripts/install-dev-tools.sh
    @./scripts/install-ruff.sh
    @git config core.hooksPath .githooks && echo "enabled .githooks (visual-regression pre-push guard)"

# Full quality gate. Fails on any issue. e2e is part of the gate, not opt-in.
check: fmt-check lint test test-e2e test-fern-goldens supply-chain doc
    @echo "check: ok"

# Format check (does not modify files).
fmt-check:
    cargo fmt --all -- --check

# Lint; warnings are errors.
lint:
    cargo clippy --all-targets --all-features --locked -- -D warnings

# Fast tests (unit + integration, excluding the e2e binary target) with coverage
# enforced. 95% line coverage is the gate; lower it only with a reason in AGENTS.md.
test:
    cargo llvm-cov --locked --fail-under-lines 95 \
        --ignore-filename-regex 'main\.rs$' \
        nextest -E 'not binary(e2e)'

# End-to-end: drive the compiled binary the way a user runs it (assert_cmd),
# byte-comparing its stripped output to the committed Fern fixtures. Also run by
# `check`; this recipe runs the journeys in isolation.
test-e2e:
    cargo nextest run --locked -E 'binary(e2e)'

# Runtime ("wire") test only: record the compiled client's behavior via an
# injected httpx.MockTransport (the pytest suite in tests/runtime/) and assert it
# matches the real Fern fixture SDK's behavior, modulo the normalized SDK-identity
# headers. Part of `test-e2e`/`check`; this runs it in isolation. Needs Python +
# httpx/pydantic/pytest (uv or pip); see tests/runtime/AGENTS.md.
test-runtime:
    cargo nextest run --locked -E 'binary(e2e) and test(crozier_matches_fern_runtime_behavior)'

# Live e2e: boot a Prism OpenAPI mock server from each fixture's spec and drive the
# generated SDK through every documented endpoint, asserting a value of the method's
# declared return type comes back over real HTTP. Spec-driven (the endpoints and
# example args come from the SDK's generated reference.md), so it grows to more
# fixtures via conftest.FIXTURES. SEPARATE from `check` to keep the core gate
# Node-free; CI runs it as its own required leg. Needs Node/Prism + uv + ruff; see
# tests/live_e2e/AGENTS.md.
test-live-e2e *args:
    ./scripts/live-e2e.sh {{args}}

# Enforce the real-world corpus byte-match: fetch the `link-ok` corpus specs (not
# vendored; see tests/fixtures/CORPUS.md) and byte-compare crozier's output for the
# vendored Fern goldens (apideck-crm, appwrite, and bungie fully; bunq's matched
# subset).
# SEPARATE from `check` because it needs network to
# fetch the specs; CI runs it in the live-e2e leg. `CROZIER_REQUIRE_CORPUS` turns a
# missing spec from a skip into a hard failure so the leg can't no-op. One
# `cargo test` invocation per corpus keeps a fetch/spec problem attributable to
# its API rather than hidden in a shared filter.
test-corpus-match:
    ./scripts/fetch-corpus.sh
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_crm_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e bunq_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e bungie_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e appwrite_server_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e anchore_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apache_airflow_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apicurio_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e discourse_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e gambitcomm_mimic_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e dnd5eapi_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apache_qakka_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e authentiqio_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e etsi_mec010_2_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_webhook_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_vault_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e airbyte_config_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e bintable_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apis_guru_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e color_pizza_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e byautomata_io_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_proxy_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_connector_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_ecommerce_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_issue_tracking_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e appwrite_client_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_file_storage_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_hris_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_accounting_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e calorieninjas_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e eos_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_sms_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_ecosystem_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_customer_support_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apideck_lead_matches_fern_output
    CROZIER_REQUIRE_CORPUS=1 cargo test --locked --test e2e apache_org_airflow_matches_fern_output

# Format the codebase in place.
format:
    cargo fmt --all

# Supply-chain gate (Linux; run once, not across an OS matrix).
supply-chain:
    cargo deny --locked check
    cargo machete

# Docs must build cleanly (broken intra-doc links are errors).
doc:
    RUSTDOCFLAGS="-D warnings" cargo doc --no-deps --all-features --locked

# Upgrade dependencies, then re-run the full gate.
upgrade:
    cargo update
    @just check

# Re-vendor the Fern reference fixtures (comment-stripped) into tests/fixtures.
# The offline corpus needs no Docker; pass `exhaustive` to also run Fern's
# container generator for the exhaustive spec. See docs/matching.md.
fixtures-refresh *args:
    ./scripts/fixtures-refresh.sh {{args}}


# Fetch the link-only real-world corpus source repositories into .local/corpus
# (or a caller-provided destination). Golden generation remains explicit because
# licensing must be reviewed per spec before anything is committed.
fetch-corpus *args:
    ./scripts/fetch-corpus.sh {{args}}


# Fetch missing link-only source repos, discover/vendor their OpenAPI specs, and
# generate Fern golden `expected/` trees for the issue #77 corpus. Pass
# `--committed` to refresh only rows already vendored. Needs Docker + fern.
fixtures-generate-corpus *args:
    ./scripts/generate-corpus-fixtures.sh {{args}}

# Deterministic Fern golden refresh: resolve an exact generator tag, generate
# every selected corpus independently, then aggregate all Crozier byte diffs.
# `--fixture NAME` may be repeated; omitting it refreshes existing corpus goldens.
fern-goldens *args:
    ./scripts/fern-goldens run {{args}}

# Phase recipes used by the workflow so successful goldens can be published
# before generation/diff failures determine the final status.
fern-goldens-generate *args:
    ./scripts/fern-goldens generate {{args}}

fern-goldens-compare:
    ./scripts/fern-goldens compare

fern-goldens-publish branch:
    ./scripts/fern-goldens publish --branch "{{branch}}"

fern-goldens-result *args:
    ./scripts/fern-goldens result {{args}}

# Process/filesystem/workflow-boundary coverage for the automation itself.
test-fern-goldens:
    python3 tests/fern_goldens_test.py

# Coverage-growth aid: for each corpus, report which committed fixture files
# crozier ALREADY reproduces byte-for-byte but are missing from its `matched` list
# in tests/e2e.rs, printed as ready-to-paste array entries. Not part of `check`.
# Run after a generator change to grow the manifest. See tests/fixtures/AGENTS.md.
# The grep is a drift gate: `cargo test <name>` exits 0 even when the exact-name
# filter matches nothing, so if `report_matched_candidates` is renamed/removed in
# tests/e2e.rs this recipe would silently no-op — asserting the report's summary
# line turns that into a hard failure instead.
fixtures-candidates corpus="":
    #!/usr/bin/env bash
    set -uo pipefail
    out=$(CROZIER_CANDIDATES_CORPUS="{{corpus}}" \
      cargo test --locked --test e2e -- --ignored --nocapture report_matched_candidates 2>&1)
    if grep -q 'candidate file(s) across all corpora' <<<"$out"; then
      # Quiet on success: print only the report the user asked for, not cargo's
      # build/test scaffolding — from the first corpus header through the summary.
      awk '/^=== /{p=1} p; /candidate file\(s\) across all corpora/{p=0}' <<<"$out"
    else
      # Drift (test renamed → 0 tests run) or a failed self-check: surface it all.
      echo "$out" >&2
      echo "fixtures-candidates: no report from report_matched_candidates — renamed/removed in tests/e2e.rs, or its self-check failed" >&2
      exit 1
    fi

# Mismatch-investigation aid (inverse of `fixtures-candidates`): print the
# normalized unified diff of every committed fixture file crozier does NOT
# reproduce byte-for-byte — exactly the bytes the gate compares (`-` = Fern
# golden, `+` = crozier; comments, SDK headers, and __init__ import order already
# normalized out), so what you see is what to fix. Optional args narrow scope:
# `just fixtures-diff <corpus> <file-substring>`. Not part of `check`. Run it to
# see WHY a file doesn't match; see tests/fixtures/AGENTS.md. Same drift guard as
# `fixtures-candidates`: assert the report's summary line so a renamed
# `report_fixture_diffs` fails loudly instead of silently no-op'ing.
fixtures-diff corpus="" file="":
    #!/usr/bin/env bash
    set -uo pipefail
    out=$(CROZIER_DIFF_CORPUS="{{corpus}}" CROZIER_DIFF_FILE="{{file}}" \
      cargo test --locked --test e2e -- --ignored --nocapture report_fixture_diffs 2>&1)
    if grep -q 'differing file(s) across the reported corpora' <<<"$out"; then
      # Quiet on success: print only the report (corpus headers, diffs, summary),
      # not cargo's build/test scaffolding.
      awk '/^=== /{p=1} p; /differing file\(s\) across the reported corpora/{p=0}' <<<"$out"
    else
      # Drift (test renamed → 0 tests run) or a bad-corpus/broken-walk assertion.
      echo "$out" >&2
      echo "fixtures-diff: no report from report_fixture_diffs — renamed/removed in tests/e2e.rs, or the corpus filter matched nothing" >&2
      exit 1
    fi

# Install/refresh the llmlint toolchain (oneharness + llmlint). Idempotent.
setup-llmlint:
    ./scripts/setup-llmlint.sh

# Make the generated fixture path runnable end to end (fern CLI, docker daemon,
# release binary) — each only if not already present. Idempotent; also run by the
# SessionStart hook. The offline path needs none of it. See tests/fixtures/AGENTS.md.
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

# `--diff` self-discovers the changed files (a three-dot compare against the base
# that skips files main also touched) and honors llmlint.yml's excludes, so no
# wrapper script is needed — it lints only what this branch introduced.
# Blocking `llmlint` PR check; run before pushing. BASE defaults to origin/main.
lint-llm-diff base="origin/main" *args:
    llmlint --diff git --diff-base {{base}} {{args}}

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
    python3 scripts/demo-gif.py

# Refresh the committed baseline manifest from a fresh capture (after an intended
# output change). Commit shots/baseline/*.json + docs/screenshots/ alongside.
screenshots-bless: screenshots
    @command -v screencomp >/dev/null || { echo "screencomp not installed: https://github.com/nickderobertis/screencomp#install" >&2; exit 1; }
    screencomp manifest --input shots/current --output shots/baseline/$(uname -m | sed 's/amd64/x86_64/;s/aarch64/arm64/').json
    @echo "baseline refreshed; commit shots/baseline/ + docs/screenshots/"
