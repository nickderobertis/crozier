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

# Full quality gate. Fails on any issue. e2e is part of the gate, not opt-in.
check: fmt-check lint test test-e2e supply-chain doc
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
# injected httpx.MockTransport (tests/runtime/wire_test.py) and assert it matches
# the real Fern fixture SDK's behavior, modulo the normalized SDK-identity
# headers. Part of `test-e2e`/`check`; this runs it in isolation. Needs Python +
# httpx/pydantic (uv or pip); see tests/runtime/AGENTS.md.
test-runtime:
    cargo nextest run --locked -E 'binary(e2e) and test(crozier_matches_fern_runtime_behavior)'

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

# Coverage-growth aid: for each corpus, report which committed fixture files
# crozier ALREADY reproduces byte-for-byte but are missing from its `matched` list
# in tests/e2e.rs, printed as ready-to-paste array entries. Not part of `check`.
# Run after a generator change to grow the manifest. See tests/fixtures/AGENTS.md.
# The grep is a drift gate: `cargo test <name>` exits 0 even when the exact-name
# filter matches nothing, so if `report_matched_candidates` is renamed/removed in
# tests/e2e.rs this recipe would silently no-op — asserting the report's summary
# line turns that into a hard failure instead.
fixtures-candidates:
    #!/usr/bin/env bash
    set -uo pipefail
    out=$(cargo test --locked --test e2e -- --ignored --nocapture report_matched_candidates 2>&1)
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
