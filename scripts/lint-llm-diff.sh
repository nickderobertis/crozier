#!/usr/bin/env bash
# Run llmlint over only the lines this branch changed since it forked from main.
#
# Lints the diff at the branch's *fork point* (the merge-base with main), not a
# raw diff against current main's tip — so unrelated commits that landed on main
# after the branch started are never linted, and a stale branch still checks
# exactly what it introduced. This is the `origin/main...HEAD` three-dot set.
#
# `--diff --diff-base` scopes both the *files* (llmlint self-discovers the ones
# changed since the fork point, honoring llmlint.yml's `files.exclude`) and the
# *lines* (the judge reviews each file's fork-point diff, not the whole file) — so
# a PR is judged on exactly what it introduced.
#
# This is what the blocking `llmlint` CI check runs (diff-scoped, so a PR pays for
# its own changes, not a full-repo sweep). Run it locally before pushing.
#
# Usage:
#   scripts/lint-llm-diff.sh [BASE_REF] [-- <extra llmlint args>]
#   BASE_REF defaults to origin/main (falls back to main). In CI, fetch main
#   first so the ref resolves.
#
# Exit codes are llmlint's own (0 clean, 1 violations, 2 config/harness error);
# a diff with no lintable files is a clean 0.
# llmlint: ignore[robust_shell] `set -e` deliberately omitted — the script controls its own exit codes (2 on resolve errors, 0 on no-diff) and must not abort early
set -uo pipefail

base_ref="origin/main"
extra=()
while [ $# -gt 0 ]; do
  case "$1" in
    --) shift; extra=("$@"); break ;;
    *) base_ref="$1"; shift ;;
  esac
done

# Resolve a usable base: prefer the given ref, fall back to local `main`.
if ! git rev-parse --verify --quiet "$base_ref" >/dev/null; then
  if git rev-parse --verify --quiet main >/dev/null; then
    echo "lint-llm-diff: '$base_ref' not found; falling back to 'main'" >&2
    base_ref="main"
  else
    echo "lint-llm-diff: cannot resolve base ref '$base_ref' (and no 'main')" >&2
    exit 2
  fi
fi

merge_base="$(git merge-base "$base_ref" HEAD)" || {
  echo "lint-llm-diff: no merge-base between '$base_ref' and HEAD" >&2
  exit 2
}

echo "lint-llm-diff: linting the diff vs ${base_ref} @ ${merge_base:0:9}" >&2
# Let llmlint discover the changed files itself (`--diff git --diff-base`): it
# scopes to the fork-point diff and applies llmlint.yml's `files.exclude`, so the
# vendored Fern fixtures are dropped in one place (not duplicated here). It reviews
# only the changed *lines*, skips empty-diff/deleted files, and exits 0 when
# nothing is left to lint.
exec llmlint --diff git --diff-base "$merge_base" "${extra[@]}"
