#!/usr/bin/env bash
# Shared helpers for the issue #77 fixture corpus manifest.

corpus_rows() {
  local manifest="$1"
  awk -F '|' '
    NR > 6 {
      name=$3; url=$5; ref=$6; decision=$8;
      gsub(/^[ `]+|[ `]+$/, "", name);
      gsub(/^[ ]+|[ ]+$/, "", url);
      gsub(/^[ `]+|[ `]+$/, "", ref);
      gsub(/^[ ]+|[ ]+$/, "", decision);
      if (name != "") print name "\t" url "\t" ref "\t" decision;
    }
  ' "$manifest"
}

corpus_fixture_for() {
  case "$1" in
    fern-seed-query-parameters) printf '%s\n' query-parameters-openapi ;;
    fern-exhaustive) printf '%s\n' exhaustive ;;
    *) printf '%s\n' "$1" ;;
  esac
}

corpus_github_clone_url() {
  case "$1" in
    https://github.com/*/tree/*)
      local trimmed path owner repo
      trimmed="${1#https://github.com/}"
      owner="${trimmed%%/*}"
      path="${trimmed#*/}"
      repo="${path%%/*}"
      printf 'https://github.com/%s/%s\n' "$owner" "$repo"
      ;;
    *) printf '%s\n' "$1" ;;
  esac
}

corpus_fetch_repo() {
  local fetch_root="$1" name="$2" url="$3" ref="$4" target="$fetch_root/$name"
  mkdir -p "$fetch_root"
  if [ -d "$target/.git" ]; then
    git -C "$target" fetch --quiet --tags origin
  else
    git clone --quiet --filter=blob:none "$(corpus_github_clone_url "$url")" "$target"
  fi
  if [ "$ref" != HEAD ]; then
    git -C "$target" checkout --quiet "$ref"
  fi
  printf '%s\n' "$target"
}

corpus_is_direct_spec_url() {
  case "$1" in
    http://*.json|https://*.json|http://*.yaml|https://*.yaml|http://*.yml|https://*.yml) return 0 ;;
    *) return 1 ;;
  esac
}

corpus_fetch_source() {
  local fetch_root="$1" name="$2" url="$3" ref="$4"
  if corpus_is_direct_spec_url "$url"; then
    local ext="${url##*.}" target_dir="$fetch_root/$name" target
    mkdir -p "$target_dir"
    target="$target_dir/openapi.$ext"
    curl -fsSL -A crozier-fixture-builder "$url" -o "$target"
    printf '%s\n' "$target"
  else
    corpus_fetch_repo "$fetch_root" "$name" "$url" "$ref"
  fi
}
