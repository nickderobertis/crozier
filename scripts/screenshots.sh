#!/usr/bin/env bash
# Capture the terminal screenshots that screencomp gates, galleries, and posts to
# PRs (see screencomp.toml + .github/workflows/visual-docs.yml).
#
# It drives the REAL release `crozier` binary against the committed demo spec
# (screenshots/petstore.yml) — exactly as a user runs it — so every capture is
# genuine CLI output: the two `--help` screens, a real `generate` run with its
# summary line and the tree it wrote, a real generated pydantic model, and the
# real actionable error crozier prints for a malformed document. Only the shell
# prompt lines (`$ …`) are synthetic framing; everything below each one is the
# binary's own output, captured live.
#
# Each scene is rendered to a deterministic SVG by `freeze` using the VENDORED,
# pinned font (screenshots/fonts/JetBrainsMono-Regular.ttf), so the bytes — and
# therefore the screencomp digests — are identical on every machine and CI runner
# without a pinned container. That byte-determinism is the whole contract: change
# a command's output (or its formatting) and that scene's SVG (and hash) changes;
# otherwise it does not. The few values that vary per machine (the temp output
# path) are kept out of the frame by running from a scratch dir and using
# relative paths, so nothing needs normalizing.
#
# Scenes — one card per facet of the CLI, so the gallery documents the whole
# surface (crozier's one real command, `generate`, seen from every angle):
#   help      the CLI surface, with a `command` toggle the gallery flips between
#             the top-level `crozier --help` (`main`) and `crozier generate
#             --help` (`generate`).
#   generate  a real run: the invocation, crozier's one-line summary, and the
#             tree of files it wrote — the whole SDK, from one OpenAPI document.
#   model     one of the generated files (types/pet.py): the pydantic model
#             crozier emits, byte-for-byte Fern's — the product, on screen.
#   error     a malformed document rejected at the boundary with an actionable
#             message and a non-zero exit — the validation invariant, shown.
#
# Output (screencomp's capture contract):
#   $SHOTS_OUT/captures.json   index: {schema, shots:[{name,toggles,hash,image}]}
#   $SHOTS_OUT/<scene>.svg     one SVG per scene (help has one per `command` toggle)
# $SHOTS_OUT defaults to shots/current/<arch> (the reusable workflow exports it
# per lane). The SVGs are also copied to docs/screenshots/ (committed) for the
# README + gallery.
#
# Requires `freeze` on PATH (install the pinned version with `just screenshots-tools`)
# and `ruff` on PATH (crozier defers Python wrapping to it; `just bootstrap` or
# scripts/install-ruff.sh installs the pinned one).
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

arch="$(uname -m)"
case "$arch" in
  x86_64 | amd64) arch="x86_64" ;;
  arm64 | aarch64) arch="arm64" ;;
esac
SHOTS_OUT="${SHOTS_OUT:-shots/current/$arch}"
font="$repo_root/screenshots/fonts/JetBrainsMono-Regular.ttf"
spec="$repo_root/screenshots/petstore.yml"
broken="$repo_root/screenshots/broken.yml"
docs_dir="$repo_root/docs/screenshots"

if ! command -v freeze >/dev/null 2>&1; then
  echo "screenshots: 'freeze' not on PATH. Install the pinned version with:" >&2
  echo "             just screenshots-tools" >&2
  exit 1
fi
if ! command -v ruff >/dev/null 2>&1; then
  echo "screenshots: 'ruff' not on PATH. crozier defers Python wrapping to it." >&2
  echo "             Install the pinned one with: ./scripts/install-ruff.sh" >&2
  exit 1
fi

# Build the binary the capture drives — release, like a user would run. Skip the
# rebuild when SCREENSHOTS_NO_BUILD is set and the binary already exists.
crozier_bin="$repo_root/target/release/crozier"
if [ -z "${SCREENSHOTS_NO_BUILD:-}" ] || [ ! -x "$crozier_bin" ]; then
  cargo build --release --locked --bin crozier >&2
fi

# Portable SHA-256 (Linux coreutils vs macOS/BSD).
sha256() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | cut -d' ' -f1
  else
    shasum -a 256 "$1" | cut -d' ' -f1
  fi
}

# Deterministic freeze flags. The vendored font (embedded into the SVG as base64)
# is what makes the output reproducible across machines; everything else is fixed
# window styling. A constant width + wrap keeps the rendered text size uniform
# across every card in the gallery (an auto-width scales each card's text
# differently); 835px = 30+30 padding + 92*~8.42px/char at this font. See llmlint,
# the same recipe.
freeze_flags=(
  --language ansi
  --font.file "$font"
  --font.family "JetBrains Mono"
  --font.size 14
  --window
  --background "#0d1117"
  --padding "20,30"
  --margin 0
  --border.radius 8
  --width 835
  --wrap 92
)

rm -rf "$SHOTS_OUT"
mkdir -p "$SHOTS_OUT" "$docs_dir"
tmp_state="$(mktemp -d)"
trap 'rm -rf "$tmp_state"' EXIT

# captures.json identity is `name + JSON.stringify(toggles)`; entries collect one
# "name|toggles|hash|image" record per rendered scene, sorted at the end.
entries=()

# Render one captured text file to a scene SVG, hash it, and record it. A scene
# must be non-empty (an empty capture means the binary failed to produce output,
# which `--language ansi` would otherwise render as a blank window).
render_scene() {
  local name="$1" toggles="$2" image="$3" src="$4"
  if [ ! -s "$src" ]; then
    echo "screenshots: scene '$name' produced no output — cannot render." >&2
    exit 1
  fi
  # `< /dev/null`: freeze reads stdin whenever it is not a character device (its
  # IsPipe check), so under CI's piped stdin it would ignore the file argument and
  # render empty input ("No input"). Pointing stdin at /dev/null (a char device)
  # forces it down the read-the-file path on every runner.
  freeze "$src" "${freeze_flags[@]}" -o "$SHOTS_OUT/$image" </dev/null >&2
  local hash
  hash="$(sha256 "$SHOTS_OUT/$image")"
  entries+=("$name|$toggles|$hash|$image")
  # The committed copies: same bytes, just outside the gitignored shots/ tree.
  cp "$SHOTS_OUT/$image" "$docs_dir/$image"
}

# A green `$` prompt followed by the command, styled to read as a real terminal
# session. These prompt lines are the only synthetic text in any scene; the ANSI
# is fixed, so it does not affect determinism.
prompt() {
  printf '\033[32m$\033[0m \033[1m%s\033[0m\n' "$1"
}

# --- help: the two --help screens, a `command` toggle flips between them -------
out="$tmp_state/help-main.ansi"
{ prompt "crozier --help"; echo; "$crozier_bin" --help; } >"$out" 2>&1 || true
render_scene "help" '{"command":"main"}' "help-main.svg" "$out"

out="$tmp_state/help-generate.ansi"
{ prompt "crozier generate --help"; echo; "$crozier_bin" generate --help; } >"$out" 2>&1 || true
render_scene "help" '{"command":"generate"}' "help-generate.svg" "$out"

# --- generate: a real run + the tree it wrote ---------------------------------
# Run from a scratch dir with a RELATIVE --output, so crozier's summary prints
# the bare `sdk` (its `output.display()` echoes the arg verbatim) — no per-machine
# temp path leaks into the frame. The tree is `find` sorted with LC_ALL=C so the
# ordering is identical on every filesystem, then indented into a plain tree.
work="$tmp_state/work"
mkdir -p "$work"
out="$tmp_state/generate.ansi"
{
  prompt "crozier generate --spec petstore.yml --output sdk --package-name petstore"
  ( cd "$work" && "$crozier_bin" generate --spec "$spec" --output sdk \
      --package-name petstore --project-name petstore ) 2>&1
  echo
  prompt "find sdk -print | sort"
  ( cd "$work" && find sdk | LC_ALL=C sort | sed -e 's|[^/]*/|  |g' )
} >"$out" || true
render_scene "generate" "{}" "generate.svg" "$out"

# --- model: one of the generated files (the product, on screen) ---------------
# crozier's job is byte-for-byte Fern-matching Python; show a generated model so
# the gallery documents WHAT it emits, not just that it ran.
out="$tmp_state/model.ansi"
{
  prompt "cat sdk/src/petstore/types/pet.py"
  echo
  cat "$work/sdk/src/petstore/types/pet.py"
} >"$out" || true
render_scene "model" "{}" "model.svg" "$out"

# --- error: a malformed document rejected at the boundary ---------------------
# crozier validates the OpenAPI document at the boundary: a malformed spec fails
# with a non-zero exit and an actionable message, never a panic. Run with a
# relative spec path so the message reads `broken.yml`, stable on every machine.
out="$tmp_state/error.ansi"
{
  prompt "crozier generate --spec broken.yml --output sdk"
  ( cd "$repo_root/screenshots" && "$crozier_bin" generate --spec broken.yml --output "$tmp_state/never" ) 2>&1 || true
} >"$out" || true
render_scene "error" "{}" "error.svg" "$out"

# Write captures.json, shots sorted by identity, schema 1, trailing newline — the
# exact shape screencomp's classify/manifest/gallery read. All fields are safe
# ASCII (names, toggle values, hex digests, file names), so plain printf is sound.
{
  printf '{\n  "schema": 1,\n  "shots": [\n'
  IFS=$'\n' sorted=($(printf '%s\n' "${entries[@]}" | sort)); unset IFS
  last=$((${#sorted[@]} - 1))
  for i in "${!sorted[@]}"; do
    IFS='|' read -r name toggles hash image <<<"${sorted[$i]}"
    comma=","
    [ "$i" -eq "$last" ] && comma=""
    printf '    {\n      "name": "%s",\n      "toggles": %s,\n      "hash": "%s",\n      "image": "%s"\n    }%s\n' \
      "$name" "$toggles" "$hash" "$image" "$comma"
  done
  printf '  ]\n}\n'
} >"$SHOTS_OUT/captures.json"

echo "screenshots: wrote ${#entries[@]} shots to $SHOTS_OUT and docs/screenshots/" >&2
