# `crozier compare`

`crozier compare` checks, for every generator a repository's crozier configs
declare, that crozier's output matches a **reference SDK** produced by a command
you control, and times both sides. It is the same byte-match crozier's own
golden suite applies, run against your configurations in your repository or CI.

For each generator it:

1. runs your reference command, which writes the reference SDK into a temporary
   directory;
2. generates crozier's SDK into another temporary directory;
3. compares the two whole trees with crozier's one comparison engine
   ([`src/parity.rs`](../src/parity.rs)), the same one crozier's own golden
   suite runs: Python comments are not compared, and every **intended
   departure** in crozier's [departure catalog](departures/README.md) — the
   `X-Crozier-*` identity headers, a corrected Fern defect, and the rest — is
   recognised line by line and reported (see
   [Intended departures](#intended-departures)). Any other difference fails;
4. records the wall time of each side.

```sh
crozier compare                       # search the whole repository you are in
crozier compare services/billing      # search one tree
crozier compare ci/crozier.yml        # check one config file
crozier compare --json report.json --diff-dir diffs
```

One way to produce a reference is the copy-paste
[Fern reference recipe](fern-reference.md). To run the check in GitHub Actions,
use the [crozier GitHub Action](github-action.md), which wraps this command; its
page includes the workflow a repository migrating from Fern adds.

## Finding configs

- **No path**: the whole repository the working directory is in is searched —
  its git top-level, or the working directory itself outside a git repository —
  so a run from `repo/sub/` still finds `repo/other/crozier.yml`. The report's
  `searched_paths` names that root.
- **A directory**: its tree is searched. `.git` and anything git ignores
  (`.gitignore`, `.git/info/exclude`, the global excludes file) are skipped when
  the directory is inside a git work tree. Hidden config names such as
  `.crozier.yml` are still found.
- **A file**: checked directly as a crozier config, whatever its name.
- **A path that does not exist**: exit 1, naming it.

In each directory the config is the first of `crozier.yml`, `crozier.yaml`,
`.crozier.yml`, `.crozier.yaml` present, the rule `crozier generate` applies.
Each config's relative paths resolve against the config file's own directory,
which is what running `crozier generate` in that directory does. `--config` and
`--no-config` do not apply: combining either with `compare` is a usage error
(exit 2); pass a config file as a path instead.

Every generator a config declares is checked (the built-in `python` when it
declares none). Its generation settings (`spec`, `package-name`, `layout`, …)
come from the config file alone: `compare` applies no `CROZIER_*` generation
environment variable and takes no per-generation flag, since one value would
silently retarget every generator it finds. crozier generates its side into a
temporary directory, never into the configured `output`.

## The `reference` setting

```yaml
reference:
  command: ./scripts/reference-sdk.sh   # shared by every generator in the file

generators:
  python:
    spec: ./openapi.yml
    output: ./sdk/python
  admin:
    spec: ./admin.yml
    output: ./sdk/admin
    reference:
      command: ./scripts/reference-sdk.sh --admin   # this generator's own
```

`reference` holds one key, `command`, at the top level (shared) and per
generator. It resolves as:

```text
--reference-command  >  generators.<name>.reference.command  >  top-level reference.command
```

There is **no default command** and no environment variable sets it. A generator
with no command resolved is `could_not_check`, with the reason "no reference
command configured: set `reference.command` in crozier.yml or pass
`--reference-command`". `crozier generate` ignores the block, and `crozier
config` shows the resolved `reference.command` with its source.

## The reference-command contract

- The command is a string run by `sh -c` on Linux and macOS, with the config
  file's directory as its working directory. On Windows every generator is
  `could_not_check`.
- It inherits crozier's environment, plus these variables and nothing else:

  | Variable | Value |
  | --- | --- |
  | `CROZIER_REFERENCE_OUTPUT` | An empty temporary directory to write the reference SDK into. |
  | `CROZIER_REFERENCE_GENERATOR` | The generator's name. |
  | `CROZIER_REFERENCE_CONFIG_FILE` | The config file's absolute path. |
  | `CROZIER_REFERENCE_SPEC` | The OpenAPI document's absolute path. |
  | `CROZIER_REFERENCE_PACKAGE_NAME` | The resolved package name. |
  | `CROZIER_REFERENCE_PROJECT_NAME` | The resolved project (distribution) name. |
  | `CROZIER_REFERENCE_CLIENT_CLASS_NAME` | The resolved root client class name. |
  | `CROZIER_REFERENCE_AUDIENCES` | The audiences, comma-separated (empty for none). |
  | `CROZIER_REFERENCE_AUDIENCE_STRICT` | `true` or `false`. |
  | `CROZIER_REFERENCE_EXTRA_FIELDS` | `allow`, `ignore` or `forbid`. |
  | `CROZIER_REFERENCE_ENUM_TYPE` | `python-enums` or `literals`. |
  | `CROZIER_REFERENCE_DEFAULT_MAX_RETRIES` | A non-negative integer (`2` unless set). |
  | `CROZIER_REFERENCE_LAYOUT` | `packaged` or `flat`. |

  Every value is the resolved one, crozier's defaults included (for example
  the package name derived from the API title), so a command never re-derives
  them.
- After the command exits 0, the reference SDK is `$CROZIER_REFERENCE_OUTPUT`
  itself, or its single subdirectory when it holds exactly one entry and that
  entry is a directory.
  <!-- llmlint: ignore[no_redundant_instruction_pointers] The task requires this page to link configuration.md for the layout setting rather than restate it; human readers reach compare.md from the README, not through AGENTS.md. -->
- The generator's [`layout` setting](configuration.md#output-layout) names
  the layout the reference is expected to have (`packaged` or `flat`). crozier
  generates its side with that layout and compares the whole reference tree
  with its whole output tree. It does not detect the reference's layout, so a reference in the
  other layout is reported as `mismatched`. The report names the layout compared.
- A non-zero exit, or a reference that is empty or ambiguous (several
  directories and no file), is `could_not_check`, carrying the command's exit
  status and the tail of its stderr (of its stdout when stderr is empty). A
  reference tool that refuses a document lands here.
- The command's stdin is empty and its output is captured, never echoed, so
  `--json -` keeps stdout to the report.

crozier's own writes change nothing in the searched repository except the
`--json` and `--diff-dir` paths you name. **The reference command is yours and is
not isolated**: it runs from the config file's directory, and anything it writes
outside `$CROZIER_REFERENCE_OUTPUT` stays written.

## Statuses

| Status | Meaning |
| --- | --- |
| `matched` | crozier's whole output tree equals the whole reference tree once the catalog's intended departures are applied. |
| `mismatched` | At least one file differs, or is only in the reference, or only in crozier's output; or the reference produced output and crozier's own generation failed, when `reason` carries crozier's error and `comparison` is null. |
| `could_not_check` | The reference could not produce output to compare: the config could not be read or resolved (a spec crozier cannot read included, found before the command runs), no reference command is configured, the command failed or left no usable reference, or a tree holds a symbolic link. The `reason` says which. |

Every generator is checked before the command exits; one failure never skips the
rest.

## Intended departures

crozier writes some lines differently from Fern on purpose: it names itself in
the identity headers, corrects Fern defects such as a README importing a class
the package does not define, and so on. Each is an entry of the
[departure catalog](departures/README.md), compiled into crozier, whose rule
recognises exactly Fern's construct and crozier's replacement. The comparison
applies every rule and lists each departure it applied by catalog id, file and
crozier's 1-based line, or line 0 for a departure accounting for a whole file
only one side has — in the human report (`intended departures applied`) and in
the JSON report's `comparison.departures`. A generator whose only
differences are departures is `matched`, exit 0.

A rule never excuses a file: a difference no rule explains still makes the
generator `mismatched`, naming the file, even on the same line as a departure or
in the same file. The `--diff-dir` diff shows only what still differs, with the
departures already applied.

## Output

Progress goes to stderr as it happens: each config found, and each generator's
reference command and crozier run starting and finishing. Then one collated
report lists every generator's status and reference command, the differing,
reference-only and crozier-only paths of each mismatch, the intended departures
applied, each `could_not_check` reason, and the timings. When no config is found it says so.

| Flag | Effect |
| --- | --- |
| `--reference-command <CMD>` | Use `<CMD>` for every generator, over any `reference.command`. |
| `--json <PATH>` | Write the JSON report to `<PATH>`; `-` writes it to stdout (the human report stays on stderr). The file is created before any reference command runs, so a target that cannot be written is refused then, with exit 1. |
| `--diff-dir <DIR>` | Write one normalized unified diff per mismatched generator into `<DIR>` (created if missing); the report and `comparison.diff_file` name each file. A file that cannot be written does not stop the run: the report states it, `diff_file` stays null, and the command exits 1. |

### Colour

The human output shows `matched` in green, `mismatched` in red and
`could_not_check` in yellow, in the progress lines and the report, and the
overall result line in its exit status's colour (0 green, 3 red, 4 yellow).
Colour is decided once per run:

1. `NO_COLOR` set to a non-empty value turns colour off, whatever else is set;
2. otherwise `CLICOLOR_FORCE` set to a non-empty value other than `0` turns it
   on (how CI logs, which are not terminals, get colour);
3. otherwise colour is on only when stderr is a terminal.

There is no `--color` flag. The JSON report (including `--json -`) and the
`--diff-dir` files never carry colour codes.

### The JSON report

The report's schema is derived from crozier's own types and committed as
[`assets/compare-report.schema.json`](../assets/compare-report.schema.json); a
test fails when the two part. Every field is always present, `null` when it has
no value:

```text
schema_version: 2
crozier_version: string
searched_paths: [string]
exit_code: 0 | 3 | 4
counts: {matched, mismatched, could_not_check: integer}
timing_totals: {generators_timed: integer, reference_seconds: number, crozier_seconds: number, speedup: number|null, saved_seconds: number}
results: [{
  status: "matched" | "mismatched" | "could_not_check",
  config_file: string, generator: string|null, spec: string|null,
  reference: {command: string, exit_code: integer|null, diagnostic: string|null}|null,
  comparison: {layout: "packaged" | "flat", files_compared: integer, differing: [string], only_in_reference: [string], only_in_crozier: [string], departures: [{id: string, file: string, line: integer}], diff_file: string|null}|null,
  timing: {reference_seconds: number|null, crozier_seconds: number|null, speedup: number|null, saved_seconds: number|null}|null,
  reason: string|null
}]
```

A config that cannot be read is one result with `generator: null`.
`files_compared` counts the distinct paths the two trees hold between them.
`departures` lists every intended departure applied, each by catalog `id`,
`file` and crozier's 1-based `line`, in a matched tree or a mismatched one.
Version 2 of the report added it; nothing else changed from version 1.

### Exit statuses

| Exit | Meaning |
| --- | --- |
| `0` | Every checked generator matched, or nothing was checked. |
| `1` | The command itself failed. Before any reference runs — a path argument that does not exist, a `--json` target that cannot be written, a `--diff-dir` that cannot be created — no report is written. A `--diff-dir` file that cannot be written fails only at the end: every generator is still checked, both reports are written (the JSON's `exit_code` is the `0`, `3` or `4` its results give), and the human report states the failure. |
| `2` | Usage error: bad flags, or `compare` combined with the global `--config` or `--no-config`. |
| `3` | At least one generator mismatched. A mismatch dominates. |
| `4` | No mismatch, but at least one generator could not be checked. |

## Timings

Each generator gets exactly two measurements:

- **reference**: the wall time of that generator's one invocation of the
  reference command, everything the command does included;
- **crozier**: the wall time of crozier's generation for the same generator,
  the comparison excluded.

From those two numbers alone the report gives, per generator, both times, the
**speed-up** (reference ÷ crozier) and the **time saved** (reference − crozier).
The run totals sum the times over the generators where both sides ran, and give
the overall speed-up from the sums and the summed saving. A generator whose
reference failed has no speed-up.

The reference figure is the whole command. A first invocation can include costs
your command pays once, such as downloading a tool or pulling a container image;
run the command once beforehand (or pre-pull what it needs) to keep them out of
the first generator's figure.
