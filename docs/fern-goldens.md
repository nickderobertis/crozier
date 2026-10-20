# Maintaining Fern goldens

Every committed Fern reference crozier byte-matches against is Fern's output at
the certified pair `assets/scaffolding/metadata.json` declares. Two things keep
them current:

- **[Route A](#add-or-change-a-fixture)**, local: adding or repairing one
  fixture runs Fern on your machine and publishes nothing.
- **[The weekly run](#the-weekly-run)**, hosted: every Monday the **Fern
  goldens** workflow checks the newest Fern against every reference, and
  proposes the result as one pull request. It never pushes to `main`.
  [Route B](#route-b--a-dispatch-of-the-workflow-operator-only) is an
  operator's dispatch of it, at pinned versions or over a diagnostic subset.

Publishing a golden redistributes generated output derived from somebody else's
API document, so the source's licence has to permit it. Which licences do —
and which do not, and why each half was decided that way — is stated once, in
[`corpus-licensing.md`](corpus-licensing.md). Screen a candidate against it
before Route A or Route B spends a generate.

## Add or change a fixture

Before spending a generate on a shape, check
[`fern-limitations.md`](fern-limitations.md): it records, with the measured
evidence and the pair each measurement ran at, which shapes Fern discards,
ignores or refuses — a golden cannot pin a style Fern throws away — and which
candidate pools are exhausted.

Work on one corpus row at a time, through
[Route A](#route-a--the-local-docker-loop-any-agent): any agent or maintainer
with Docker and the `fern` CLI runs it end to end on one machine, with no push
and no remote state. The hosted workflow is no route for adding a fixture: it
publishes only a run over the whole inventory at a new Fern, and a
[Route B dispatch](#route-b--a-dispatch-of-the-workflow-operator-only) with `items` over one fixture shows what Fern
writes for it without changing anything.

### Route A and the weekly run resolve the same generator image and configuration

Verify this before trusting a locally generated golden, by naming where each
resolves each of the two. They agree because the weekly run regenerates every
item through the recipe Route A runs, with only the pair moved:

| | Route A (local) | the weekly run (hosted) |
|---|---|---|
| **generator image** | `just fern-goldens-generate --version X` → `tools/fern-goldens/fern-goldens` `generate()`, which validates `X` and passes it to the generator script | each shard moves `metadata.json` to the candidate pair and runs `fern-references.py generate <family> <item>`, which runs that same `fern-goldens generate --version X` for a `CORPUS.md` row |
| **generator config** | `tools/fern-goldens/generate-fern-fixture.sh`, which reads the fixture's row from [`fern-generator-config.txt`](../tests/fixtures/fern-generator-config.txt) and writes `generators.yml` | identical — the workflow has no generator-config input and no second config site |

Both therefore emit one `generators.yml` naming `fernapi/fern-python-sdk` at the
resolved version, and both apply the corpus-wide `pydantic_config.enum_type:
python_enums` that `generate-fern-fixture.sh` writes for every `expected/` golden
(crozier's default renders string enums as real `enum.Enum` classes). Only its `--enum-type literals` mode, which
produces the [literal-enum goldens](#literal-enum-goldens), leaves it unset. A fixture's own non-default settings — audiences,
`client_class_name`, `extra_fields` — reach the same block from
`fern-generator-config.txt`, so a golden generated locally is the artifact the
hosted run would have regenerated. A `CORPUS.md` row's provenance records that
row's settings (`fern_generator_config`), and a golden is current only for the
Fern CLI its own `.fern/metadata.json` records, so a changed setting or a new CLI
at the same generator version regenerates it rather than skipping it.

### Route A — the local Docker loop (any agent)

Needs Docker, the `fern` CLI, Rust, and Ruff; publishes nothing. `just setup-fern`
installs and starts what is missing (it also runs from the session-start hook, so
it is usually already done).

1. Create a feature branch. Add or update one numbered, eight-cell `CORPUS.md`
   row with its unique spec name, credential-free HTTPS source URL, and pinned
   source ref. A direct spec URL must end in `.json`, `.yaml`, or `.yml`. A
   multi-file source adds one `tree` record per document to
   [`corpus-remote-ref-pins.tsv`](../tests/fixtures/corpus-remote-ref-pins.tsv):
   repository-relative path, immutable URL at that row's commit, and SHA-256.
   Include the root document. The pin guard verifies the exact fetched file
   set, every digest, and that relative references stay within it. Fern receives
   those files under `openapi/` at their pinned relative paths; crozier receives
   the root at the same location in its cached tree. A generator setting no
   OpenAPI document can express needs no new spec: give the
   already-registered source a second row name and declare the setting for that
   name in `fern-generator-config.txt`.
2. Register the same name as a `Corpus` in `crates/crozier-e2e/tests/e2e.rs` with `unmatched: &[]`,
   add the `#[test]` that drives it, and — for a fetched `link-ok` spec — add its
   `just test-corpus-match` line;
   `every_registered_corpus_is_wired_into_the_gate` fails without both. Commit
   this registration on its own: it is a complete, reviewable change, and the
   golden it names does not exist yet.
3. Read the pin the corpus is on — every golden records the generator it was
   produced by, so take the version from provenance rather than from prose:

   ```sh
   pin=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["fern_python_sdk_version"])' \
     tests/fixtures/eos.local/expected/.crozier-fern-golden.json)
   ```

   Any managed golden's `expected/.crozier-fern-golden.json` answers the same;
   they agree, because a corpus-wide upgrade moves all of them together.
4. Generate the one fixture at that pin:

   ```sh
   just setup-fern                       # no-op when the prerequisites are there
   just fern-goldens-generate --version "$pin" --fixture <name>
   ```

   Always pass `--version`. Omitting it resolves the latest stable tag from
   Docker Hub, which turns a fixture add into a Fern upgrade. Success prints
   `generated <name> at fernapi/fern-python-sdk:<pin>` and installs
   `tests/fixtures/<name>/expected/` atomically, provenance included; failure
   leaves any prior golden untouched and writes a per-fixture log under
   `.local/fern-goldens/generation-logs/`.
5. Measure the first comparison with `just fixtures-gaps <name>`. It reports the
   exact divergent files as a ready-to-paste `unmatched` array.
6. Repair **Crozier** until that list is empty — never the golden. `just
   fixtures-diff <name> [<file-substring>]` prints the normalized diff of exactly
   the bytes the gate compares (`-` = Fern, `+` = Crozier). Re-run
   `just fixtures-gaps <name>` after each generator fix. Regenerating is only
   needed if the spec, the version, or the fixture's generator config changed;
   a Crozier fix does not invalidate the golden.
7. Prove it with the real gate rather than by eye: `just test-corpus-match`,
   which fetches every `link-ok` spec and runs every row's byte-match line,
   including the one step 2 added. Steps 5 and 6 are the fast inner loop — they
   perform the same comparison over one fixture — but this recipe is the tier CI
   runs, so it is what "byte-matched" means. Then commit the golden and the
   generator fix.

### Flat goldens

A fixture can also carry Fern's **flat** output as `expected-flat/`, beside its
packaged `expected/`. That is the tree `fern generate --local` writes to a
`local-file-system` output path without `--preview`, which crozier reproduces
with `--layout flat` (see [`matching.md`](matching.md#the-flat-layout)).
[`flat-goldens.txt`](../tests/fixtures/flat-goldens.txt) declares every flat
golden, and `crates/crozier-e2e/tests/e2e.rs::FLAT_GOLDENS` must list exactly its rows.

- **The script's layout option.** `tools/fern-goldens/generate-fern-fixture.sh --layout
  flat <fixture> <pin>` runs that local-file-system generation, strips comments,
  and installs the result atomically as `tests/fixtures/<fixture>/expected-flat/`.
  It refuses a fixture `flat-goldens.txt` does not declare. It runs Fern with no
  `FERN_TOKEN`, as the measurement did. The fixture's row in
  `fern-generator-config.txt` supplies its settings, as for the packaged form.
  `--layout packaged`, the default, is the unchanged `--preview` run into
  `expected/`.
- **Provenance** is the packaged form's with `"layout": "flat"` added: the
  vendored-spec record the script writes, or the manifest record `fern-goldens`
  writes for a `CORPUS.md` row. Packaged records carry no `layout` key, so no
  packaged golden goes stale over it.
- **Route A** for a hand-authored fixture: declare it in `flat-goldens.txt`, add
  its `FLAT_GOLDENS` entry and `flat_goldens!` test in `crates/crozier-e2e/tests/e2e.rs`, run the
  script's flat mode at the pin, then measure with `just fixtures-gaps
  <fixture>`. A flat golden whose directory has no spec names the fixture whose
  source it uses in its row's second column
  (`swagger-petstore-organization|swagger-petstore`).
- **`fern-goldens generate` and the weekly run** refresh the flat golden of
  every declared `CORPUS.md` row in the same generation as its packaged one,
  from the same fetched spec. The flat golden has its own currency check. A row
  whose packaged golden is current but whose flat one is stale regenerates only
  the flat one. A failed flat refresh keeps the prior `expected-flat/` and fails
  the item. Comparison needs no extra input: `just fixtures-diff <fixture>`
  reports the fixture's flat golden after its packaged one.
- **A fetched-spec flat test needs its `just test-corpus-match` line**, like its
  packaged sibling. `every_registered_corpus_is_wired_into_the_gate` fails without
  it.

### Literal-enum goldens

A targeted set of registered fixtures (`KINDS` in
`crates/crozier-e2e/tests/e2e/overlay_goldens.rs`, chosen so that together they reach every enum shape
crozier generates: named, inline-property, parameter, sanitized-name, optional
and nullable enums) also carries `expected-literals/`: Fern's output for the
same spec, pins and settings with
`pydantic_config.enum_type` left unset (fern-python-sdk's `literals` default),
which crozier reproduces with `--enum-type literals`.

- **It is an overlay of `expected/`.** Fern's literals output differs from the
  python-enums tree only where an enum appears, so the directory holds just the
  files whose bytes differ, plus `.crozier-overlay.json`: the Fern
  versions, and the `expected/` files Fern does not emit in that mode
  (`core/enum.py`). The gate in `crates/crozier-e2e/tests/e2e/overlay_goldens.rs` rebuilds the full tree
  as `expected/` minus those files plus the overlay, and compares it with the
  corpus's own residuals. The gate also fails when a listed fixture lacks the
  overlay, when an overlay sits outside the list, and when the overlay's Fern
  version differs from `expected/`'s provenance. Add a fixture to the set only
  for an enum shape the set does not yet reach.
- **Generate it locally**, after `expected/` is current:
  `tools/fern-goldens/fern-overlay-goldens.sh [--jobs N] --enum-type literals <fixture>...` runs
  `tools/fern-goldens/generate-fern-fixture.sh --enum-type literals` per fixture with the
  spec `expected/` was generated from (the vendored `openapi.yml`, the committed
  corpus source, or `just fetch-corpus` for a row with pinned remote refs), the
  version its provenance records, and its `fern-generator-config.txt` row. It
  needs what Route A needs and logs to `.local/fern-overlay/`.
- **The weekly run refreshes it** (the `overlays` family), in the same shard as
  the `expected/` it is reduced against and after it. After a local regeneration
  of `expected/`, rerun the script for the affected fixtures; the version check
  above names each stale one.
- **Other settings use the same mechanism.** `expected-default-max-retries/` is
  Fern with `default_max_retries: 0` for crozier's `default-max-retries: 0`, on
  `enum-query-param` and `openfigi.com`
  (`tools/fern-goldens/fern-overlay-goldens.sh --default-max-retries 0 <fixture>...`). It
  reaches only the root `client.py` and `core/client_wrapper.py`. A new setting
  gets a `KINDS` entry and the fewest fixtures that reach what it changes, never
  a copy of the corpus.

### Moving a remote-`$ref` pin forward

A corpus row whose document names another document by absolute URL is only
reproducible if that URL is immutable, so
[`../tests/fixtures/corpus-remote-ref-pins.tsv`](../tests/fixtures/corpus-remote-ref-pins.tsv)
records the substitution — `corpus_name`, the `mutable_url` upstream writes, the
`pinned_url` replacing it, and the SHA-256 of the bytes that URL serves.
`tools/corpus/fetch-corpus.sh` applies a row's records to the fetched document before
publishing it, so Fern generates from, and crozier byte-matches against, the same
pinned inputs. The manifest also records complete multi-file trees as `tree`
rows; those use one row revision and one digest per member.

The provenance rides along: `expected_state` writes those records into
`expected/.crozier-fern-golden.json` for a row that has them, and omits the key
entirely for a row that does not — which is what keeps every other golden
current, since `is_current()` byte-compares that file.

So the procedure is the ordinary one, and the manifest is its only input:

1. Edit the row's record — the new `pinned_url`, and the `sha256` of the bytes it
   serves (`curl -fsSL <pinned_url> | sha256sum`).
2. Run `just lint-corpus-remote-ref-pins`. That row's state file no longer matches
   `expected_state`, so the row is stale.
3. Regenerate the row at the certified pair with `just fern-references corpus
   <name>` ([Route A](#route-a--the-local-docker-loop-any-agent)). It refetches
   (applying the new pin, verifying the new digest) and regenerates the tree and
   its provenance; commit both.

No other row is touched. A record whose
`mutable_url` the fetched document does not reference fails the fetch rather than
applying nothing, so a manifest left behind by a root-`$ref` bump surfaces at
step 3 rather than silently pinning nothing.

### Exact known upstream failures

`calorieninjas.com` is the single registered exception across the whole corpus,
recorded at the certified `fernapi/fern-python-sdk` version. Its source
operation has no `operationId`, and Fern emits unnamed methods (`def (` and `_raw_client.(`) before Ruff rejects the
SDK. [`known-fern-failure.json`](../tests/fixtures/calorieninjas.com/known-fern-failure.json)
binds the exception to the exact generator version, corpus name/ref/URL, exit
code, six ordered syntax diagnostics and source lines, Ruff summary, and failed
command.

Generation always retries that fixture, even after an exact reproduction. Only
the normalized fingerprint is warning-only; a changed exit, diagnostic, source
line, command, corpus identity, malformed registration, or unexpected Fern
success is fatal. The registration is therefore not a suppression an operator can
reach for: it is bound to this one spec's measured failure, so it cannot be
copied onto a corpus whose golden merely started diverging, and a fixture
carrying both a registration and an `expected/` tree is an error. There is
deliberately no `expected/` tree: the former
unprovenanced snapshot came from an unidentified older Fern and could not support
a byte-parity claim. Comparison validates the registration and drives Crozier
over the real cached spec as a subprocess, including the assertion that Crozier
names the operation where Fern emits `def (`. A missing golden is otherwise a
hard harness error. When a future Fern version generates a complete valid SDK,
remove the failure registration and generate its provenanced tree (Route A);
CalorieNinjas then rejoins normal byte comparison.

Everything above holds at the registration's own version. At any other — the
candidate pair a weekly run or a `--version` regeneration checks — Fern's outcome
decides the registration like any other reference, and none of the three ends
the run:

- the same exit and fingerprint carry it: the registration is restated at the
  candidate version, and the weekly run counts it as no difference;
- a different exit or fingerprint rewrites it at the candidate with the failure
  Fern now gives, and Fern generating the fixture replaces it with the new
  `expected/` tree. `fern-goldens` lists both in
  `.local/fern-goldens/known-upstream-failure-changes.txt`, and the weekly run
  decides each a diff its pull request carries under **Known upstream Fern
  failures that changed**.

A failure with no Fern Ruff fingerprint (Docker, the network) rewrites nothing:
it is an ordinary generation failure and the registration stands.

## Regenerating every reference family

A move of the certified pair — `cliVersion` and `generatorVersion` in
[`../assets/scaffolding/metadata.json`](../assets/scaffolding/metadata.json),
the one place the pair is declared — regenerates every committed Fern
reference, family by family. Each family is one command, which runs Fern one
generation at a time in a scratch workspace outside the checkout and writes each
item where its gate reads it:

```sh
just fern-references-list <family>              # the family's item names, one per line
just fern-references <family>                   # every item, at the certified pair
just fern-references <family> <item>...         # exactly the named items
just fern-references <family> --version V --cli-version C [<item>...]   # another pair
```

| family | what it writes | through |
|---|---|---|
| `corpus` | `tests/fixtures/<fixture>/expected/` and `expected-flat/` | `fern-goldens generate` for a `CORPUS.md` row, `generate-fern-fixture.sh` for a vendored fixture |
| `overlays` | `tests/fixtures/<fixture>/expected-literals/` and `expected-default-max-retries/` | `fern-overlay-goldens.sh --jobs 1` |
| `handwritten` | `docs/openapi-surface/handwritten/<fixture>/fern-expected/`, with `evidence.toml`'s versions and `digest` | the probe workspace below |
| `measurements` | `docs/fern-measurements/<group>/<case>/fern-expected/`, or the case's Contract A `fern-refusal.txt` where its committed reference is Fern's refusal (a case Fern now generates from gets its tree and is reported), each `<stem>.fern.log` beside its `<stem>.openapi.*` refused document, and a case's pinned run its `measurement.json` records (its log and Fern's raw `raw_client.py`), as [`cases.tsv`](fern-measurements/cases.tsv) declares each case's document, enum mode, layout and overlay base, restating each case's `evidence.toml`/`evidence.md`; and `parameter-literals/<fixture>`, which re-measures that a hand-written fixture's literals tree is its python-enums tree less `core/enum.py` and records the metadata and digest | the probe workspace below |
| `probes` | `docs/openapi-surface/probe-expected/<name>/`, or its Contract A refusal record, with `MANIFEST.tsv`'s digest | the probe workspace below |
| `authored-probes` | `docs/openapi-surface/authored-probes/<case>/fern.log` and `fern-expected/` | the probe workspace below |
| `departure-evidence` | `docs/departures/evidence/<id>/fern-reference/`, a departure note's own Fern tree, under the settings its `fern-reference.json` records | the probe workspace below |
| `refusals` | `docs/fern-refusals/<class>/fern-refusal.txt`, `findings.tsv`, and each `<class>/evidence/<stem>.pinned-fern.log` whose probe document sits beside it | `fern-refusals.py probe` / `finding` with `--jobs 1` |

The probe workspace is the one `generate-fern-fixture.sh` scaffolds, built by
`tools/fern-goldens/fern-references.py` itself so it can write outside
`tests/fixtures/`. Run `corpus` before `overlays`, and `handwritten` before
`measurements`: an overlay is reduced against the tree it overlays. A probe
whose outcome changes form (a tree Fern now refuses, or a refusal it now
generates from) is written and reported, because its `MANIFEST.tsv` row's form
and verdict are a Contract A decision; an authored probe Fern now refuses moves
to the refusal registry. Two families refuse an override their delegate cannot
honour: `overlays` takes no `--version` (each overlay is generated at the version
its golden's provenance records, so run `corpus` first), and `refusals` takes
neither flag (`fern-refusals.py` measures at the pair `metadata.json` declares).
Omitting `--version` here keeps the certified pair;
`just fern-goldens-generate` without `--version` still resolves the newest
stable Fern tag.

Witness screens are records of a search, not references, so a move does not
regenerate them. Once the goldens carry the new pair, `python3
tools/witness-search/witness_screen.py historical` labels every committed
screen measured at an earlier pair as that pair's history, which no live
decision reads as a measurement; a candidate is re-measured at the new pair by
screening it again (`golden-reach-search.py screen`, or `witness_screen.py
screen`).

## The weekly run

[`fern-goldens.yml`](../.github/workflows/fern-goldens.yml) runs every Monday at
05:17 UTC from `main`, and on **Actions → Fern goldens → Run workflow**. Each of
its jobs is one phase of [`tools/fern-goldens/weekly.py`](../tools/fern-goldens/weekly.py),
which holds every decision, so the YAML stays thin and the tests drive the real
phases.

1. **Resolve** (`plan` job). The pair to check is the newest stable Fern CLI
   (the npm `fern-api` package) and the newest stable `fernapi/fern-python-sdk`
   Docker Hub tag. A dispatch's `fern-cli-version` and `fern-version` pin
   either exactly. A run over the whole inventory whose pair is the certified
   one, or is already a row of
   [`fern-pair-checks.tsv`](../tests/fixtures/fern-pair-checks.tsv), ends green
   here with a summary line saying so, and changes nothing.
2. **Plan** (`plan` job). Every family `fern-references.py list` names — corpus
   goldens and their flat golden, the literal and default-max-retries
   overlays, hand-written `fern-expected/` trees, measurement cases, probes,
   authored probes, departure evidence and the refusal registry's class,
   finding and evidence records — grouped into units that must generate in one
   shard: an overlay after the golden it is reduced against, a measurement after
   the hand-written tree it overlays, and every item of a family that rewrites
   one shared table (`probes`' `MANIFEST.tsv`, `refusals`' `classes.tsv` and
   `findings.tsv`). The units are packed into the **fewest shards** whose
   predicted generation fits the
   [`crozier-fern-goldens-weekly-minutes`](../.github/budgets.yaml) budget with a
   25% margin, each predicted from
   [`generation-seconds.tsv`](../tools/fern-goldens/generation-seconds.tsv) (an
   item no run has timed yet is planned at the mean corpus rate). The shard
   count therefore grows with the inventory, never from a hand-edited constant.
3. **Shard** (one `shard` job per planned shard, at most 20 at once, each with a
   `timeout-minutes` inside GitHub's six-hour limit). The shard moves
   `metadata.json` to the candidate pair and regenerates each item through
   `fern-references.py generate <family> <item>`, timing it. Its artifact,
   `fern-goldens-shard-<n>`, carries every file each item wrote, each item's log
   and the shard's `result.json` (per item: its seconds, outcome and files).
4. **Assemble** (`assemble` job). One job combines every shard into one tree,
   the `fern-goldens-bundle` artifact, with the measured seconds written back
   into `generation-seconds.tsv` and the candidate pair into `metadata.json`.
5. **Decide** (`decide` job). The bundle is laid over a checkout and every
   statement of the pair restated (`certified_pair.py restate`), so the tree is
   the one the pull request would carry; crozier is built from it, so its own
   version stamps are the candidate pair's. Every item is then decided by
   crozier's own comparison and nothing else, through the gates
   [`decision-gates.tsv`](../tools/fern-goldens/decision-gates.tsv) names:
   - **per item**: each corpus golden and its flat golden, through `just
     fixtures-diff <fixture>` (`report_fixture_diffs`: the parity engine, the
     departure catalog and the golden's ledger rows). A difference outside the
     corpus's `unmatched` list, or a crozier generation failure, is a diff; a
     comparison the reporter could not process is one that could not run;
   - **per family**: every other family, through the crozier-e2e suite
     (the tests `just test-e2e` runs, printing only what fails, which hold the overlay, hand-written,
     measurement, probe, authored-probe, departure-evidence and refusal-class
     gates, and every corpus golden's own test), and for the refusal registry
     also `tests/refusal_registry.rs` and `fern-refusals.py check`. A failing
     gate is a diff, and the pull request lists under that family every item
     whose name or regenerated files its report names, with the report's lines
     for it (or the report's tail, when it names none).

   A comparison that cannot run is a failure, never a pass. The
   `fern-goldens-decision` artifact holds the decision and every gate's report.
6. **Publish** (`publish` job, a run over the whole inventory only), under
   `RELEASE_PLZ_TOKEN` — the PAT `release-plz.yml` uses, since a pull request
   the default `GITHUB_TOKEN` opens triggers none of crozier's required checks.

### The pull request it opens

There is one, on the branch **`fern-goldens/update`**, labelled
**`fern-goldens`** (created when missing), titled `test(fern-goldens):
regenerate at Fern CLI <cli> / fern-python-sdk <generator>` — a Conventional
Commit, as the required `commitlint` check asks. A later run updates it rather
than opening another, and pushes the branch only with a lease on what it read.

- **Diff** — crozier's comparison fails for at least one item, or a reference
  could not be regenerated. The pull request carries every regenerated
  reference, the new pair in `metadata.json` and the measured seconds; its body
  lists the failing items per family, each with the comparison's own report. It
  is not auto-merged: crozier's checks on it show what crozier must change, and
  the retarget is a person's.
- **No diff** — every comparison passes. The pull request adopts the pair:
  `metadata.json` at the new pair, every regenerated reference, crozier's
  matching version stamps wherever the tree states the pair (so the pair drift
  check stays green), the measured seconds and one `fern-pair-checks.tsv` row
  (`fern_cli_version`, `fern_python_sdk_version`, `checked_on`, `outcome`). It
  is auto-merged once crozier's required checks pass.

A reference whose pinned upstream specification can no longer be fetched (a
404, as subsloth's source now returns) is never skipped silently and never stops
the rest: it keeps its committed tree, and is named in the run's summary and in
the pull request's **Not regenerated** section, which makes the run a diff.

### How a failure shows

Any failure before publication ends the run red with its step summary naming
each failure, and touches no branch, pull request or record: a shard that fails
or uploads nothing, an item whose generation fails (other than a registered known
upstream failure, above), an assembly that cannot account for every planned item
or finds two shards writing one file, a comparison that cannot run, or a
missing `RELEASE_PLZ_TOKEN` (which the `plan` job checks before any Fern runs).

A failure during publication — pushing the branch, labelling, opening or
updating the pull request, or enabling auto-merge — also ends the run red; its
summary lists the steps that completed. Every write reads the remote first, so
the next run reuses the branch and pull request, skips what is done, and
finishes the rest.

### Route B — a dispatch of the workflow (operator only)

From **Actions → Fern goldens → Run workflow**, or equivalently:

```sh
gh workflow run fern-goldens.yml --ref main \
  -f fern-cli-version=<cli> -f fern-version=<generator> [-f items=<subset>]
```

Every input is optional; a blank version resolves the newest stable one, as the
schedule does.

- **Without `items`** the dispatch is a weekly run at the pair it names: it runs
  from `main`, checks every reference and publishes as above.
- **With `items`** — comma-separated `family` or `family:item`, such as
  `handwritten,corpus:anchore.io` — it is a diagnostic: it plans, generates and
  decides exactly that subset and reports the result in its summary and
  artifacts, from any branch. It never opens a pull request, adopts a pair or
  records one as checked, so the next run over the whole inventory still
  regenerates and decides everything for that pair.

**A dispatched agent cannot take Route B**: a dispatch selects a ref already on
the remote, and publication is the lifecycle's job, not the agent's. Route A is
the procedure from inside a working tree.

## Publication safety

Each item is generated into a same-filesystem staging directory and replaces its
committed reference only after the complete tree and its provenance are ready;
a failed item keeps the prior one. The weekly run publishes only what one
assembly accounted for, item by item, and only from a decision crozier's
comparison made over that exact tree. It pushes nothing but
`fern-goldens/update`, with `--force-with-lease` on the commit it read there,
so a change made to the branch since is never overwritten, and runs of the
workflow queue rather than race (`concurrency`, never cancelled).

## Local diagnostics

Route A above is the local generation procedure; the commands here are the wider
local surface around it. The weekly run is the only thing that opens a pull
request: every local command requires the same Fern, Docker, Rust, and Ruff
prerequisites as the workflow and writes nothing to a branch.

Generate selected fixtures and then run the aggregate comparison:

```sh
just fern-goldens --version 5.41.3 --fixture anchore.io
```

Repeat `--fixture` for an exact multi-fixture selection. Omit `--version` to use
the latest stable Fern tag; omit all `--fixture` arguments to select existing
corpus goldens.

Keep generation and comparison separate when diagnosing a phase:

```sh
just fern-goldens-generate --version 5.41.3 --fixture anchore.io
just fern-goldens-compare
```

The second command deliberately compares every available managed golden. For a
narrower human-readable diff after that aggregate pass, use
`just fixtures-diff anchore.io`, or add a literal path substring such as
`just fixtures-diff anchore.io client.py`.

Any fixture can carry fixture-owned non-default settings as a row in the shared
table [`fern-generator-config.txt`](../tests/fixtures/fern-generator-config.txt):
the audience list, Crozier strict-audience identity, Fern `client_class_name`,
Fern `pydantic_config.extra_fields`, and the Fern workspace `organization` (the
input that names the module, client and README the way crozier's
`--package-name` does). `tools/fern-goldens/generate-fern-fixture.sh` loads
them by fixture name on both routes, so a `CORPUS.md` row is generated with them
too — that is what lets a generator setting no OpenAPI document can express
(`eos.local-extra-fields-forbid`, row 82) be pinned by a second row over an
already-registered source. Explicit environment values remain a diagnostic
override. Provenance differs by path: the hand-authored path records the
settings alongside the versions in `.crozier-fern-golden.json`, while a corpus
row's state file is the manifest form (`fern-goldens`' own name/ref/URL record),
so `fern-generator-config.txt` is the authority for what a corpus row was
generated with.

One non-default setting is **not** in that table and applies corpus-wide:
`tools/fern-goldens/generate-fern-fixture.sh` writes `pydantic_config.enum_type:
python_enums` into `generators.yml` for every fixture it generates — on both
routes, since both drive the same script. Fern records it in each golden's
`.fern/metadata.json` (`generatorConfig`) and the e2e normalizes that block off
both sides, so it never shows up as a per-fixture setting; regenerating a golden
any other way silently reverts its enums to Fern's default open-`Literal` union.
