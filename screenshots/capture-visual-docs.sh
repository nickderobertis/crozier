#!/usr/bin/env bash
# The visual-docs capture CI's lint lane runs, in the container that pins its renderer
# inputs to crozier's toolchain, twice: the second capture is screencomp's
# reproducibility gate. Writes shots/current/x86_64 and shots/verify/x86_64, owned by
# the caller. The build stays in a volume of its own, off the host's target/: root-owned
# and built against another registry path, it would dirty every later cargo run.
#
# llmlint: ignore[changed_behavior_has_e2e] The whole capture needs Docker and two release downloads, so its tests stop at the container's boundary; the lint lane really runs it on every pull request and screencomp holds its bytes to the baseline there.
set -euo pipefail

toolchain="$(sed -n 's/^channel = "\(.*\)"$/\1/p' rust-toolchain.toml 2>/dev/null)" || toolchain=""
if [ -z "$toolchain" ]; then
  echo "capture-visual-docs: no channel in rust-toolchain.toml; run this from the repository root" >&2
  exit 2
fi
# A linked worktree's .git file names a directory outside it, which the capture's git reads.
git_common="$(git rev-parse --path-format=absolute --git-common-dir)" || {
  echo "capture-visual-docs: not a git checkout; run this from the repository root" >&2
  exit 2
}

docker run --rm -v "$PWD":/work -v "$git_common":"$git_common":ro -v crozier-visual-docs-target:/work/target -w /work \
  -e RUSTUP_TOOLCHAIN="$toolchain" \
  -e HOST_OWNER="$(id -u):$(id -g)" \
  -e GIT_COMMON="$git_common" \
  "rust:$toolchain-bookworm" bash -euo pipefail -c '
    # Whatever the capture leaves is the caller'\''s, including after a failed capture.
    trap '\''chown -R "$HOST_OWNER" shots docs/screenshots'\'' EXIT
    git config --global --add safe.directory /work
    git config --global --add safe.directory "$GIT_COMMON"
    # freeze renders the deterministic SVGs; ruff is what crozier defers Python
    # wrapping to. Both prebuilt, pinned to the files the local recipes read, so the
    # local and CI renderers cannot silently diverge.
    freeze_ver="$(cat .freeze-version)"
    curl -fsSL -o /tmp/freeze.tgz "https://github.com/charmbracelet/freeze/releases/download/v${freeze_ver}/freeze_${freeze_ver}_Linux_x86_64.tar.gz"
    tar -xzf /tmp/freeze.tgz -C /tmp
    install /tmp/freeze*/freeze /usr/local/bin/freeze
    ruff_ver="$(cat .ruff-version)"
    curl -fsSL -o /tmp/ruff.tgz "https://github.com/astral-sh/ruff/releases/download/${ruff_ver}/ruff-x86_64-unknown-linux-gnu.tar.gz"
    tar -xzf /tmp/ruff.tgz -C /tmp
    install /tmp/ruff-x86_64-unknown-linux-gnu/ruff /usr/local/bin/ruff
    # llmlint: ignore[work_goes_through_command_surface] The rust image carries no `just`, and each capture needs its own SHOTS_OUT; `just screenshots` is this same one-line script.
    capture() {
      SHOTS_OUT="$1" bash scripts/screenshots.sh > /tmp/capture.log 2>&1 || { cat /tmp/capture.log >&2; return 1; }
    }
    capture shots/current/x86_64
    capture shots/verify/x86_64
    echo "capture-visual-docs: shots/current and shots/verify written"
  ' || {
  status=$?
  echo "capture-visual-docs: the capture failed (status $status, above); run ./screenshots/capture-visual-docs.sh locally, or fix the download or scripts/screenshots.sh error it names" >&2
  exit "$status"
}
