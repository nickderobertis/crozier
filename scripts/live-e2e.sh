#!/usr/bin/env bash
# Spec-driven live e2e: boot a Prism OpenAPI mock server from each fixture's spec
# and drive the *generated* SDK through every documented endpoint, asserting a
# value of the method's declared return type comes back over real HTTP. This is
# the runtime complement to the byte-diff e2e (proves the source) and the wire
# tests (prove request/response shaping vs Fern): it proves the compiled client
# round-trips against a spec-shaped server. See tests/live_e2e/AGENTS.md.
#
# Quiet on success. SEPARATE from `just check` so the core gate stays Node-free;
# CI runs it as its own required leg. Linux/macOS (Unix venv layout).
#
# Needs: cargo (build the binary under test), ruff (crozier's generation-time
# dependency — it shells out to `ruff format`), Node/npx (Prism, the mock server),
# and uv (the Python test venv). Each missing tool is an actionable error here; the
# pytest suite additionally skips-locally / fails-under-CI on the same tools so it
# can never silently no-op in the gate.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

need() { command -v "$1" >/dev/null 2>&1 || { echo "live-e2e: $1 not found — $2" >&2; exit 1; }; }
need cargo "install Rust via https://rustup.rs"
need uv    "install uv via https://docs.astral.sh/uv/ (the Python test venv uses it)"
need node  "install Node 18+ via https://nodejs.org (Prism, the mock server, runs on it)"
need ruff  "run 'just bootstrap' (crozier shells out to 'ruff format' when generating)"

# Build the binary the suite drives — release, the artifact users run.
cargo build --release --locked --bin crozier >&2

# Cached venv with the generated SDK's runtime deps (httpx, pydantic), the test
# runner (pytest), and a YAML parser for the request-relaxer (pyyaml). Rebuilt only
# when missing or incomplete; lives under the gitignored scratch dir.
venv="$root/.crozier-tmp/live-e2e-venv"
py="$venv/bin/python"
if [ ! -x "$py" ] || ! "$py" -c "import httpx, pydantic, pytest, yaml" 2>/dev/null; then
  uv venv "$venv" >&2
  uv pip install --python "$py" --quiet httpx pydantic pytest pyyaml >&2
fi

# CROZIER_BIN is the compiled binary the suite generates each SDK with.
CROZIER_BIN="$root/target/release/crozier" "$py" -m pytest tests/live_e2e -q -p no:cacheprovider "$@"
