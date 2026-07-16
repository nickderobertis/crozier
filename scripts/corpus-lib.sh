#!/usr/bin/env bash
# Shared helpers for the issue #77 fixture corpus manifest.

corpus_rows() {
  local manifest="$1"
  awk -F '|' '
    # CORPUS.md contains status tables after the canonical numbered manifest.
    # Accept only numbered rows from that first table; otherwise prose/status
    # cells are misread as fixture names and URLs.
    $2 ~ /^[[:space:]]*[0-9]+[[:space:]]*$/ {
      name=$3; url=$5; ref=$6; decision=$8;
      gsub(/^[ `]+|[ `]+$/, "", name);
      gsub(/^[ ]+|[ ]+$/, "", url);
      gsub(/^[ `]+|[ `]+$/, "", ref);
      gsub(/^[ ]+|[ ]+$/, "", decision);
      if (name != "" && (decision == "link-ok" || decision == "committed"))
        print name "\t" url "\t" ref "\t" decision;
    }
  ' "$manifest"
}

corpus_aliases_file() {
  local corpus_lib_dir
  corpus_lib_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  printf '%s\n' "$corpus_lib_dir/../tests/fixtures/corpus-aliases.tsv"
}

corpus_fixture_for() {
  local aliases
  aliases="$(corpus_aliases_file)"
  [ -f "$aliases" ] || {
    echo "corpus: missing fixture alias file $aliases" >&2
    return 1
  }
  awk -F '\t' -v requested="$1" '
    function valid_fixture(value) {
      return value ~ /^[A-Za-z0-9][A-Za-z0-9._-]*$/ \
        && value !~ /^[.-]/ && index(value, "..") == 0;
    }
    function fail(reason) {
      printf "corpus: invalid fixture alias file %s line %d: %s\n", \
        FILENAME, NR, reason > "/dev/stderr";
      invalid=1;
      exit 2;
    }
    BEGIN { resolved=requested; }
    /^[[:space:]]*(#|$)/ { next; }
    {
      if (NF != 2 || !valid_fixture($1) || !valid_fixture($2))
        fail("expected two safe fixture names separated by one tab");
      if ($1 == $2)
        fail("alias source and fixture directory must differ");
      if ($1 in sources)
        fail("duplicate alias source " $1);
      if ($2 in fixtures)
        fail("duplicate fixture directory " $2);
      sources[$1]=1;
      fixtures[$2]=1;
      count++;
      if ($1 == requested)
        resolved=$2;
    }
    END {
      if (!invalid && count == 0) {
        printf "corpus: fixture alias file %s has no aliases\n", FILENAME > "/dev/stderr";
        exit 2;
      }
      if (!invalid)
        print resolved;
    }
  ' "$aliases"
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
  local fetch_root="$1" name="$2" url="$3" ref="$4" target
  target="$fetch_root/$name"
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

corpus_spec_cache_filename() {
  case "$1" in
    *.json) printf '%s\n' openapi.json ;;
    *.yaml) printf '%s\n' openapi.yaml ;;
    *.yml) printf '%s\n' openapi.yml ;;
    *)
      echo "corpus: direct spec URL has no supported OpenAPI suffix: $1" >&2
      return 1
      ;;
  esac
}

corpus_fetch_source() {
  local fetch_root="$1" name="$2" url="$3" ref="$4"
  if corpus_is_direct_spec_url "$url"; then
    local target_dir="$fetch_root/$name" target temporary stale
    mkdir -p "$target_dir"
    # Crozier deliberately dispatches JSON/YAML parsing by extension. Preserve the
    # raw source suffix while keeping one canonical basename for every consumer.
    target="$target_dir/$(corpus_spec_cache_filename "$url")"
    temporary="$(mktemp "$target_dir/.openapi.XXXXXX")"
    if ! curl -fsSL -A crozier-fixture-builder "$url" -o "$temporary"; then
      rm -f "$temporary"
      return 1
    fi
    if [ ! -s "$temporary" ]; then
      echo "corpus: fetched an empty spec for $name from $url" >&2
      rm -f "$temporary"
      return 1
    fi
    mv "$temporary" "$target"
    for stale in "$target_dir/openapi.json" "$target_dir/openapi.yaml" "$target_dir/openapi.yml"; do
      [ "$stale" = "$target" ] || rm -f "$stale"
    done
    printf '%s\n' "$target"
  else
    corpus_fetch_repo "$fetch_root" "$name" "$url" "$ref"
  fi
}
