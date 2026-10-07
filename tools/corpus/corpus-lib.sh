#!/usr/bin/env bash
# Shared helpers for the issue #77 fixture corpus manifest. Sourced by scripts
# that already run strict; set here too so a new caller cannot source it lax.
set -euo pipefail

# corpus_rows MANIFEST — each fetchable row as `name<TAB>url<TAB>ref<TAB>decision`.
# A row whose name, source or ref is not one the fetch can use safely (a name
# becomes a path, the source a fetch, the ref a checkout) fails the whole read,
# naming the row, rather than reaching those commands.
corpus_rows() {
  local manifest="$1"
  awk -F '|' -v manifest="$manifest" '
    function refuse(problem) {
      printf "corpus-lib: %s row %s (%s): %s — fix the row in tests/fixtures/CORPUS.md, then re-run\n", manifest, number, name, problem > "/dev/stderr"
      failed = 1
      exit 1
    }
    # CORPUS.md contains status tables after the canonical numbered manifest.
    # Accept only numbered rows from that first table; otherwise prose/status
    # cells are misread as fixture names and URLs.
    $2 ~ /^[[:space:]]*[0-9]+[[:space:]]*$/ {
      number=$2; name=$3; url=$5; ref=$6; decision=$8;
      gsub(/[[:space:]]/, "", number);
      gsub(/^[ `]+|[ `]+$/, "", name);
      gsub(/^[ ]+|[ ]+$/, "", url);
      gsub(/^[ `]+|[ `]+$/, "", ref);
      gsub(/^[ ]+|[ ]+$/, "", decision);
      if (name == "" || (decision != "link-ok" && decision != "committed")) next;
      if (name !~ /^[A-Za-z0-9][A-Za-z0-9._-]*$/ || name ~ /\.\./)
        refuse("the name is not a fixture name (letters, digits, `.`, `_`, `-`; no `..`)");
      # https for a published source; loopback http and an absolute local path
      # are how the offline suites stand in for one.
      if (url !~ /^https:\/\/[^[:space:]`]+$/ && url !~ /^http:\/\/(127\.0\.0\.1|localhost)(:[0-9]+)?\/[^[:space:]`]*$/ && url !~ /^\/[^[:space:]`]+$/)
        refuse("the source is not an https URL");
      if (ref !~ /^[A-Za-z0-9._][A-Za-z0-9._\/-]*$/)
        refuse("the pinned ref is not a commit, tag or branch name");
      print name "\t" url "\t" ref "\t" decision;
    }
  ' "$manifest"
}

corpus_scripts_dir() {
  cd "$(dirname "${BASH_SOURCE[0]}")" && pwd
}

corpus_aliases_file() {
  printf '%s\n' "$(corpus_scripts_dir)/../../tests/fixtures/corpus-aliases.tsv"
}

# Substitute a row's recorded remote-`$ref` pins into a freshly fetched document,
# and refuse any document that would be published carrying a mutable absolute
# `$ref`. See tools/corpus/corpus_remote_ref_pins.py.
corpus_pin_apply() {
  local name="$1" file="$2" document_name="$3"
  python3 "$(corpus_scripts_dir)/corpus_remote_ref_pins.py" \
    apply "$name" "$file" --as "$document_name"
}

# Whether a cached document is already in the state `corpus_pin_apply` leaves it
# in. A mismatch is a routine cache miss rather than an error, so the caller
# refetches instead of reporting: anything genuinely wrong resurfaces loudly from
# `corpus_pin_apply` on that refetch.
corpus_pin_verify() {
  local name="$1" file="$2"
  python3 "$(corpus_scripts_dir)/corpus_remote_ref_pins.py" \
    verify "$name" "$file" >/dev/null 2>&1
}

corpus_tree_root() {
  python3 "$(corpus_scripts_dir)/corpus_remote_ref_pins.py" tree-root "$1"
}

corpus_tree_verify() {
  python3 "$(corpus_scripts_dir)/corpus_remote_ref_pins.py" \
    verify-tree "$1" "$2" >/dev/null 2>&1
}

corpus_fixture_for() {
  local aliases
  aliases="$(corpus_aliases_file)"
  [ -f "$aliases" ] || {
    echo "corpus: missing fixture alias file $aliases — it is committed; restore it with" \
         "git checkout -- tests/fixtures/corpus-aliases.tsv, then re-run" >&2
    return 1
  }
  awk -F '\t' -v requested="$1" '
    function valid_fixture(value) {
      return value ~ /^[A-Za-z0-9][A-Za-z0-9._-]*$/ \
        && value !~ /^[.-]/ && index(value, "..") == 0;
    }
    function fail(reason) {
      printf "corpus: invalid fixture alias file %s line %d: %s — fix that line, or restore" \
        " the file with git checkout -- tests/fixtures/corpus-aliases.tsv, then re-run\n", \
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
        printf "corpus: fixture alias file %s has no aliases — restore it with git checkout" \
          " -- tests/fixtures/corpus-aliases.tsv, then re-run\n", FILENAME > "/dev/stderr";
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

# Callers run these fetchers inside a command substitution, where errexit does
# not apply, so every step returns its failure explicitly: a path is printed
# only once the source behind it is really there.
corpus_fetch_repo() {
  local fetch_root="$1" name="$2" url="$3" ref="$4" target clone_url
  target="$fetch_root/$name"
  mkdir -p "$fetch_root" || {
    echo "corpus: cannot create the fetch root $fetch_root for $name — choose a writable" \
         "fetch root, then re-run" >&2
    return 1
  }
  if [ -d "$target/.git" ]; then
    git -C "$target" fetch --quiet --tags origin || {
      echo "corpus: could not update the cached clone of $name in $target — check network" \
           "access, or remove the clone (rm -rf $target) to re-clone it, then re-run" >&2
      return 1
    }
  else
    clone_url="$(corpus_github_clone_url "$url")"
    git clone --quiet --filter=blob:none "$clone_url" "$target" || {
      echo "corpus: could not clone $clone_url for $name — check network access and the" \
           "row's source URL in tests/fixtures/CORPUS.md, then re-run" >&2
      return 1
    }
  fi
  if [ "$ref" != HEAD ]; then
    git -C "$target" checkout --quiet "$ref" || {
      echo "corpus: could not check out $ref for $name in $target — check the row's pinned" \
           "ref in tests/fixtures/CORPUS.md, or remove the clone (rm -rf $target) to" \
           "re-clone it, then re-run" >&2
      return 1
    }
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
      echo "corpus: direct spec URL has no supported OpenAPI suffix: $1 — point the row's" \
           "source URL in tests/fixtures/CORPUS.md at a document ending in .json, .yaml or" \
           ".yml, then re-run" >&2
      return 1
      ;;
  esac
}

corpus_fetch_source() {
  local fetch_root="$1" name="$2" url="$3" ref="$4"
  local tree_root
  tree_root="$(corpus_tree_root "$name")" || return 1
  if [ -n "$tree_root" ]; then
    python3 "$(corpus_scripts_dir)/corpus_remote_ref_pins.py" \
      fetch-tree "$name" "$fetch_root/$name"
    return
  fi
  if corpus_is_direct_spec_url "$url"; then
    local target_dir="$fetch_root/$name" target filename temporary stale
    mkdir -p "$target_dir" || {
      echo "corpus: cannot create the cache directory $target_dir for $name — remove" \
           "whatever is in its way or choose a writable fetch root, then re-run" >&2
      return 1
    }
    # Crozier deliberately dispatches JSON/YAML parsing by extension. Preserve the
    # raw source suffix while keeping one canonical basename for every consumer.
    filename="$(corpus_spec_cache_filename "$url")" || return 1
    target="$target_dir/$filename"
    temporary="$(mktemp "$target_dir/.openapi.XXXXXX")" || {
      echo "corpus: cannot create a temporary file in $target_dir for $name — check that it" \
           "is writable and has free space, then re-run" >&2
      return 1
    }
    if ! curl -fsSL -A crozier-fixture-builder "$url" -o "$temporary"; then
      rm -f "$temporary"
      echo "corpus: could not download the spec for $name from $url — check network access" \
           "and the row's source URL in tests/fixtures/CORPUS.md, then re-run" >&2
      return 1
    fi
    if [ ! -s "$temporary" ]; then
      echo "corpus: fetched an empty spec for $name from $url — check that the row's source" \
           "URL in tests/fixtures/CORPUS.md serves the OpenAPI document itself, then re-run" >&2
      rm -f "$temporary"
      return 1
    fi
    # Pin before publishing, so a document carrying a mutable absolute `$ref`
    # never reaches a consumer: this is a gate, not a post-hoc repair.
    if ! corpus_pin_apply "$name" "$temporary" "${target##*/}"; then
      rm -f "$temporary"
      return 1
    fi
    # Stale siblings are removed only once the new document is published.
    if ! mv "$temporary" "$target"; then
      rm -f "$temporary"
      echo "corpus: could not publish the fetched spec for $name to $target — check that" \
           "$target_dir is writable and nothing there blocks the rename, then re-run" >&2
      return 1
    fi
    for stale in "$target_dir/openapi.json" "$target_dir/openapi.yaml" "$target_dir/openapi.yml"; do
      [ "$stale" = "$target" ] || rm -f "$stale" || {
        echo "corpus: could not remove the stale cached spec $stale for $name — delete it" \
             "(rm -rf $stale), then re-run" >&2
        return 1
      }
    done
    printf '%s\n' "$target"
  else
    corpus_fetch_repo "$fetch_root" "$name" "$url" "$ref"
  fi
}
