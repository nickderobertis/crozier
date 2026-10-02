# The crozier GitHub Action

<!-- llmlint: ignore[no_redundant_instruction_pointers] This page is what a GitHub Marketplace or README reader lands on, before any AGENTS.md: it must name the command the Action wraps, and compare.md is that command's one reference. -->
`nickderobertis/crozier` is a GitHub Action that runs
[`crozier compare`](compare.md) in a workflow and reports what it found in the
job's step summary, its outputs and its exit status. It wraps the CLI and adds
no comparison logic of its own: what is compared, the statuses, the timings and
the exit status are all the CLI's, read from its JSON report.

```yaml
      - uses: nickderobertis/crozier@v0
        with:
          reference-command: ./scripts/reference-sdk.sh   # optional
```

The Action finds every crozier config in the repository, runs each generator's
reference command and crozier, and byte-compares the two SDKs. The reference
command is yours: the Action never installs, configures or pins the tool that
produces the reference. For a team moving from Fern, the
[consumer workflow below](#migrating-from-fern) sets Fern up and runs the
[Fern reference recipe](fern-reference.md).

## Inputs

| Input | Default | Meaning |
| --- | --- | --- |
| `paths` | empty: the whole repository | crozier config files, or directories to search for them, as `crozier compare [PATHS...]` takes: separated by spaces, or one per line in a `paths: \|` block. |
| `reference-command` | empty: each config's `reference.command` | The command that writes each generator's reference SDK, used for every generator found (`--reference-command`). It runs under `sh -c` from each config file's directory, with the `CROZIER_REFERENCE_*` environment `crozier compare` gives every reference command. |
| `diff-artifact-name` | `crozier-compare-diffs` | Name of the artifact the per-generator diffs are uploaded as when anything mismatched. |
| `version` | empty: the release the action's own ref names | Empty installs `v<version>` for the `[package] version` in the action's own `Cargo.toml` — at `@vX.Y.Z` that is `vX.Y.Z`, at `@v0` the release `v0` points at — and fails, naming this input, when that file cannot be read; it never falls back to the latest release. Otherwise a release tag such as `v0.1.0`, `latest` for the newest release, or `local` to build the action's own source with `cargo`. |

## Outputs

| Output | Meaning |
| --- | --- |
| `matched` | How many generators matched their reference. |
| `mismatched` | How many generators mismatched their reference. |
| `could-not-check` | How many generators could not be checked. |
| `exit-code` | The exit status of `crozier compare`: `0`, `1`, `3` or `4` (see [Exit status](#exit-status)). |
| `report-path` | Path to the JSON report ([`assets/compare-report.schema.json`](../assets/compare-report.schema.json)); empty when the command failed before writing one. |
| `total-reference-seconds` | The reference commands' wall time, in seconds, summed over the generators where both sides ran. |
| `total-crozier-seconds` | crozier's generation time, in seconds, summed over the same generators. |
| `total-speedup` | `total-reference-seconds` ÷ `total-crozier-seconds`; empty when no generator ran on both sides. |
| `total-saved-seconds` | `total-reference-seconds` − `total-crozier-seconds`. |

The counts and totals are empty when `crozier compare` failed before writing
its report (`exit-code` `1`).

## Versioning

`@v0` is a **floating major tag**: it follows every stable `0.x` release, and
it will keep meaning `0.x` after a `v1` exists. The release workflow moves it as
its last job, and only when:

- the release's archives uploaded to its GitHub Release, and no publish or
  verify job failed. The crates.io and PyPI jobs are skipped while their
  publishing tokens are unset, and a skipped job does not hold `v0` back; when
  they run, a failure does;
- the GitHub Release is not flagged as a pre-release, and its tag is a plain
  `vX.Y.Z` with no pre-release (`-rc.1`) or build-metadata (`+build.3`) suffix;
- no newer `0.x` release already exists, so re-cutting an older one never moves
  `v0` backwards.

An exact tag — `nickderobertis/crozier@v0.0.88` — pins the Action **and** its
binary together: leave `version` unset and the Action installs the release its
own ref names, so there is no second version to keep in step.

## Requirements

- A **Linux or macOS runner** with `bash` and `jq` (GitHub's hosted runners have
  both). Windows runners are refused: `crozier compare` runs reference commands
  under `sh`.
- **The reference tool**, set up by your workflow before this step. The Action
  runs your command and nothing else.
- **`ruff`**, which crozier itself needs to format the Python it generates. The
  Action installs the version crozier pins when `ruff` is absent from `PATH`.
- `cargo`, only for `version: local`.

## What it reports

**Step summary.** The overall result — ✅ every checked generator matched (or
nothing was found to check), ❌ at least one mismatched, ⚠️ nothing mismatched
but something could not be checked — then the counts, and one row per
generator: its status beside the same mark, its config and generator, the
reference command, the differing files of a mismatch or the reason it could not
be checked, and its four timing figures. A last row gives the run totals of the
same figures. Markdown cannot colour text, so the marks are the summary's
signal; in the step log the CLI and the Action print `matched` in green,
`mismatched` in red and `could_not_check` in yellow.

**Colour.** The Action sets `CLICOLOR_FORCE=1`, so the log is coloured even
though it is not a terminal. Set `NO_COLOR` (to any non-empty value) in your
workflow's `env` to turn colour off; it wins, by the CLI's own colour rule.

**Artifact.** When anything mismatched, the per-generator unified diffs
(`crozier compare --diff-dir`) are uploaded as one artifact named by
`diff-artifact-name`. Nothing is uploaded otherwise.

**Timings.** Every figure is the CLI's own:

- **reference time** — the wall time of that generator's one reference-command
  invocation, everything the command does included. A first invocation may
  include one-time costs such as an image pull; pre-pull what your command needs
  to keep them out of it, as the example below does.
- **crozier time** — crozier's generation for the same generator, the
  comparison excluded.
- **speed-up** — reference time ÷ crozier time.
- **time saved** — reference time − crozier time.

`total-reference-seconds` and `total-crozier-seconds` sum those times over the
generators where both sides ran; `total-speedup` and `total-saved-seconds` are
computed from the two sums.

### Exit status

The Action's last step exits with `crozier compare`'s own status, so the job
passes on `0` (everything checked matched, or nothing was found) and fails on
`1` (the command itself failed), `3` (a mismatch) and `4` (nothing mismatched,
but something could not be checked). The diff artifact is uploaded before it
fails.

## Migrating from Fern

This is the one workflow a repository adds while it moves from Fern to crozier.
It runs on every pull request and every push to `main` that changes an OpenAPI
document or a crozier config — not on a schedule — sets Fern up, writes the
[Fern reference recipe](fern-reference.md) (an unchanged copy) to a file, and
runs the Action with that file as the reference command. It uses the Fern
versions crozier certifies: **Fern CLI 5.67.1** with **`fernapi/fern-python-sdk`
5.20.0**.

It is committed in crozier's repository as
[`docs/examples/migrate-from-fern.yml`](examples/migrate-from-fern.yml); copy it
to `.github/workflows/` in yours.

```yaml
# Check, on every change to your OpenAPI documents or crozier configs, that
# crozier generates byte-for-byte what Fern generates for them.
# Copy this file to .github/workflows/ and adjust the `paths:` globs below.
# See https://github.com/nickderobertis/crozier/blob/main/docs/github-action.md
#
# Fern versions crozier certifies: Fern CLI 5.67.1 with
# fernapi/fern-python-sdk 5.20.0. The recipe below defaults to them.
name: crozier compare

on:
  pull_request:
    paths:
      # Your OpenAPI documents: adjust these globs to where yours live.
      - "openapi/**"
      - "**/openapi.yml"
      - "**/openapi.yaml"
      - "**/openapi.json"
      # crozier's config files, at any depth.
      - "**/crozier.yml"
      - "**/crozier.yaml"
      - "**/.crozier.yml"
      - "**/.crozier.yaml"
  push:
    branches: [main]
    paths:
      # Your OpenAPI documents: adjust these globs to where yours live.
      - "openapi/**"
      - "**/openapi.yml"
      - "**/openapi.yaml"
      - "**/openapi.json"
      # crozier's config files, at any depth.
      - "**/crozier.yml"
      - "**/crozier.yaml"
      - "**/.crozier.yml"
      - "**/.crozier.yaml"

permissions:
  contents: read

jobs:
  compare:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # The reference tool is yours to set up: Fern needs Node, its CLI
      # launcher, and a container runtime for its Python generator.
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - name: Install the Fern CLI
        run: npm install -g fern-api@5.67.1
      - name: Confirm the container runtime
        run: docker version
      # Pulled before the comparison, so the download is not counted in the
      # first generator's reference time.
      - name: Pull the Fern Python generator image
        run: docker pull fernapi/fern-python-sdk:5.20.0

      # The Fern reference recipe, copied unchanged from
      # https://github.com/nickderobertis/crozier/blob/main/docs/fern-reference.md
      - name: Write the Fern reference recipe
        run: |
          cat > "$RUNNER_TEMP/fern-reference.sh" <<'RECIPE'
          #!/usr/bin/env bash
          # Write a Fern reference SDK for `crozier compare` into $CROZIER_REFERENCE_OUTPUT,
          # from the generator settings crozier passes as CROZIER_REFERENCE_*.
          # See https://github.com/nickderobertis/crozier/blob/main/docs/fern-reference.md
          set -euo pipefail

          # The Fern CLI and generator versions crozier certifies; override either here.
          FERN_CLI_VERSION="${FERN_REFERENCE_CLI_VERSION:-5.67.1}"
          FERN_PYTHON_SDK_VERSION="${FERN_REFERENCE_PYTHON_SDK_VERSION:-5.20.0}"

          fail() {
            echo "fern-reference: $*" >&2
            exit 1
          }

          # A value as a double-quoted YAML (and JSON) string, so characters YAML gives a
          # meaning to (`:`, `#`, `{`, quotes) reach Fern as written. A control character
          # cannot be carried that way, so it is refused.
          quote() {
            if [[ "$1" =~ [[:cntrl:]] ]]; then
              fail "value '$1' holds a control character, which the Fern workspace cannot carry"
            fi
            printf '"%s"' "$(printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g')"
          }

          for name in OUTPUT SPEC PACKAGE_NAME PROJECT_NAME CLIENT_CLASS_NAME \
            AUDIENCE_STRICT EXTRA_FIELDS ENUM_TYPE DEFAULT_MAX_RETRIES LAYOUT; do
            var="CROZIER_REFERENCE_$name"
            [ -n "${!var:-}" ] || fail "$var is not set; run this as a crozier compare reference command"
          done
          out="$CROZIER_REFERENCE_OUTPUT"
          package="$CROZIER_REFERENCE_PACKAGE_NAME"
          project="$CROZIER_REFERENCE_PROJECT_NAME"
          layout="$CROZIER_REFERENCE_LAYOUT"

          # Fern names the module, the `{Organization}Api` client class and the README
          # heading after the workspace organization, so the package name becomes it.
          case "$layout" in
            packaged)
              # Fern emits the packaged tree only for the `fern` organization, whose
              # distribution is always `default_package_name`.
              [ "$package" = fern ] || fail "package name '$package' cannot be reproduced under the packaged layout: Fern emits its packaged form only for the organization 'fern'; set package-name: fern, or compare under layout: flat"
              [ "$project" = default_package_name ] || fail "project name '$project' cannot be reproduced under the packaged layout: Fern's packaged distribution is always 'default_package_name'"
              ;;
            flat)
              # Measured: `acme`, `acme2` and `my_api` name Fern's module as given;
              # `my-api` does not (Fern renames it `my_api`), so only this shape is passed.
              [[ "$package" =~ ^[a-z][a-z0-9_]*$ ]] || fail "package name '$package' cannot be reproduced: Fern names the module after the organization, which reproduces only lowercase letters, digits and underscores, starting with a letter"
              # A flat tree has no distribution, so the project name reaches none of its files.
              ;;
            *)
              fail "unknown layout '$layout': expected packaged or flat"
              ;;
          esac

          # crozier's `python-enums` is Fern's `enum_type: python_enums`; its `literals` is
          # Fern with `enum_type` unset, which is fern-python-sdk's `literals` default.
          case "$CROZIER_REFERENCE_ENUM_TYPE" in
            python-enums) enum_type="            enum_type: python_enums"$'\n' ;;
            literals) enum_type="" ;;
            *)
              fail "unknown enum type '$CROZIER_REFERENCE_ENUM_TYPE': expected python-enums or literals"
              ;;
          esac

          # Fern's `default_max_retries` defaults to 2, as crozier's does; only another
          # value is written.
          retries="$CROZIER_REFERENCE_DEFAULT_MAX_RETRIES"
          [[ "$retries" =~ ^(0|[1-9][0-9]*)$ ]] || fail "default max retries '$retries' is not a non-negative integer"
          default_max_retries=""
          [ "$retries" = 2 ] || default_max_retries="          default_max_retries: $retries"$'\n'

          work="$(mktemp -d)"
          trap 'rm -rf "$work"' EXIT
          mkdir -p "$work/fern/openapi"
          spec_name="$(basename "$CROZIER_REFERENCE_SPEC")"
          cp "$CROZIER_REFERENCE_SPEC" "$work/fern/openapi/$spec_name"

          # Every value written into the workspace, quoted first: a refusal inside a
          # here-document would not stop the script.
          q_package="$(quote "$package")"
          q_cli_version="$(quote "$FERN_CLI_VERSION")"
          q_spec_path="$(quote "openapi/$spec_name")"
          q_sdk_version="$(quote "$FERN_PYTHON_SDK_VERSION")"
          q_client="$(quote "$CROZIER_REFERENCE_CLIENT_CLASS_NAME")"
          q_extra_fields="$(quote "$CROZIER_REFERENCE_EXTRA_FIELDS")"

          cat > "$work/fern/fern.config.json" <<JSON
          { "organization": $q_package, "version": $q_cli_version }
          JSON

          audiences=""
          if [ -n "${CROZIER_REFERENCE_AUDIENCES:-}" ]; then
            audiences="    audiences:"$'\n'
            IFS=',' read -ra names <<<"$CROZIER_REFERENCE_AUDIENCES"
            for audience in "${names[@]}"; do
              audiences+="      - $(quote "$audience")"$'\n'
            done
          fi

          # A local-file-system output: the flat tree is written to its path. Under
          # `--preview --output` the packaged tree goes to the --output directory instead,
          # and Fern still needs this output to emit the plain package (without one it
          # emits a publishable repository: CI workflow, poetry.lock, version 0.0.1).
          output_path="$work/unused"
          [ "$layout" = packaged ] || output_path="$out"
          q_output_path="$(quote "$output_path")"

          cat > "$work/fern/generators.yml" <<YAML
          api:
            path: $q_spec_path
          groups:
            crozier-reference:
          ${audiences}    generators:
                - name: fernapi/fern-python-sdk
                  version: $q_sdk_version
                  config:
                    client_class_name: $q_client
          ${default_max_retries}          pydantic_config:
          ${enum_type}            extra_fields: $q_extra_fields
                  output:
                    location: local-file-system
                    path: $q_output_path
          YAML

          # Fern stamps how it was invoked into .fern/metadata.json; crozier emits the
          # form a CI run records.
          export CI="${CI-true}"
          export GITHUB_ACTIONS="${GITHUB_ACTIONS-true}"

          cd "$work/fern"
          if [ "$layout" = packaged ]; then
            # `--preview` emits the packaged tree only with a non-empty token; nothing is
            # published, so a placeholder serves.
            export FERN_TOKEN="${FERN_TOKEN-preview-only-no-publish}"
            fern generate --group crozier-reference --local --preview --output "$out" --force >&2
          else
            # The flat tree is what a token-less local run writes, as measured.
            unset FERN_TOKEN
            fern generate --group crozier-reference --local --force >&2
          fi
          RECIPE
          chmod +x "$RUNNER_TEMP/fern-reference.sh"

      - uses: nickderobertis/crozier@v0
        with:
          reference-command: ${{ runner.temp }}/fern-reference.sh
```

**What to adjust.** The `paths:` filters under both triggers: replace the
OpenAPI globs with the paths of your own documents, and keep the four crozier
config names. Each generator's `layout` and names must be ones the recipe can
reproduce; it exits non-zero naming any it cannot, which the Action reports as
could not check.

**Non-blocking.** As written, the workflow reports without blocking: the
failed `compare` check and its step summary are there to read, and nothing
requires them. To keep even the check green while it reports, add
`continue-on-error: true` to the `nickderobertis/crozier@v0` step: a mismatch
then marks that step failed and still passes the job.

**Blocking.** Do not mark the example's `compare` job as a required status
check as it stands. Its `paths:` filters skip the whole workflow on a pull
request that changes no OpenAPI document or crozier config, and a required
check whose workflow never ran never reports: it stays "Expected — Waiting for
status to be reported" and the pull request cannot merge. For required use, run
the workflow on every pull request — no `paths:` filters — and let a first job
decide whether anything relevant changed. GitHub reports a job skipped by its
`if:` as a success, so the required `compare` check passes on a pull request
that touches none of those files and runs the comparison on one that does:

```yaml
on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  changes:
    runs-on: ubuntu-latest
    outputs:
      relevant: ${{ steps.changed.outputs.relevant }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Check for changed OpenAPI documents or crozier configs
        id: changed
        env:
          BASE: ${{ github.event.pull_request.base.sha || github.event.before }}
        run: |
          relevant=true
          # A base this checkout cannot name (a branch's first push) checks everything.
          if git cat-file -e "$BASE^{commit}" 2>/dev/null &&
            git diff --quiet "$BASE" HEAD -- \
              ':(glob)openapi/**' ':(glob)**/openapi.yml' ':(glob)**/openapi.yaml' \
              ':(glob)**/openapi.json' ':(glob)**/crozier.yml' ':(glob)**/crozier.yaml' \
              ':(glob)**/.crozier.yml' ':(glob)**/.crozier.yaml'; then
            relevant=false
          fi
          echo "relevant=$relevant" >> "$GITHUB_OUTPUT"

  compare:
    needs: changes
    if: ${{ needs.changes.outputs.relevant == 'true' }}
    runs-on: ubuntu-latest
    steps:
      # The example's steps, unchanged.
```

Keep the pathspecs in step with your OpenAPI documents, as you would the
`paths:` globs, then mark `compare` as a required status check in the branch's
protection rules or rulesets.
