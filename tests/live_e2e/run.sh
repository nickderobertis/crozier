#!/usr/bin/env bash
# The live e2e runner: the generated SDK driven against a Prism mock of each
# fixture's spec. What the suite proves is tests/live_e2e/AGENTS.md's.
#
# Quiet on success. The `live-e2e` project's `test`: promoted out of the affected
# tier (`just check --sweep` runs it); CI runs it as its own required leg.
# Linux/macOS (Unix venv layout).
#
# Needs: cargo (build the binary under test), ruff (crozier's generation-time
# dependency — it shells out to `ruff format`), Node/npx (Prism, the mock server),
# and uv (the Python test venv). Each missing tool is an actionable error here; the
# pytest suite additionally skips-locally / fails-under-CI on the same tools so it
# can never silently no-op in the gate.
set -euo pipefail

root="$(cd "$(dirname "$0")/../.." && pwd)" && cd "$root" || {
  echo "live-e2e: cannot enter the checkout above $0 — run it by its path from a readable checkout, then re-run" >&2
  exit 1
}

need() { command -v "$1" >/dev/null 2>&1 || { echo "live-e2e: $1 not found — $2" >&2; exit 1; }; }
need cargo "install Rust via https://rustup.rs"
need uv    "install uv via https://docs.astral.sh/uv/ (the Python test venv uses it)"
need node  "install Node 18+ via https://nodejs.org (Prism, the mock server, runs on it)"
need ruff  "run 'just bootstrap' (crozier shells out to 'ruff format' when generating)"

# Build the binary the suite drives — release, the artifact users run.
cargo build --release --locked --bin crozier >&2 || {
  echo "live-e2e: building the release crozier failed (cargo's error is above) — fix it, or run" \
       "'cargo fetch --locked' with network if a crate could not be fetched, then re-run" >&2
  exit 1
}

# Cached venv with the generated SDK's runtime deps (httpx, pydantic), the test
# runner (pytest), and a YAML parser for the request-relaxer (pyyaml). Rebuilt only
# when missing or incomplete; lives under the gitignored scratch dir unless
# CROZIER_LIVE_E2E_VENV names another (test_runner.py's, so a forced failure
# never touches the venv this suite is running in).
venv="${CROZIER_LIVE_E2E_VENV:-$root/.crozier-tmp/live-e2e-venv}"
py="$venv/bin/python"
if [ ! -x "$py" ] || ! "$py" -c "import httpx, pydantic, pytest, yaml" 2>/dev/null; then
  uv venv "$venv" >&2 || {
    echo "live-e2e: could not create the test venv at $venv — check that directory's" \
         "permissions and free space, delete it (rm -rf '$venv'), then re-run" >&2
    exit 1
  }
  uv pip install --python "$py" --quiet httpx pydantic pytest pyyaml >&2 || {
    echo "live-e2e: could not install httpx, pydantic, pytest and pyyaml into $venv —" \
         "check that PyPI is reachable, then re-run (the incomplete venv is rebuilt)" >&2
    exit 1
  }
fi

# Pin the suite to the release binary just built, over any CROZIER_BIN the
# caller's environment carries.
CROZIER_BIN="$root/target/release/crozier" "$py" -m pytest tests/live_e2e -q -p no:cacheprovider "$@"
