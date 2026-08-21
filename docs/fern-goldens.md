# Maintaining Fern goldens

The **Fern goldens** GitHub Actions workflow is the maintenance path for numbered
rows in [`tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md). It runs Fern in
the hosted environment, records reproducible provenance, compares Crozier, and
safely publishes every complete Fern result back to its branch. Adding or
repairing a single fixture does not need it: [Route A](#add-or-change-a-fixture)
below runs the same generation locally and publishes nothing.

It has two trigger contracts:

- Every Monday at 05:17 UTC, the schedule runs from `main`. Scheduled events
  have no dispatch inputs, so both values are explicitly treated as blank: the
  run resolves the latest stable Fern version and selects every corpus row with
  an existing managed golden. Current provenance takes the normal per-fixture
  skip path; when everything is current and matched, publication is a no-op and
  the aggregate comparison is green.
- An operator can use **Actions → Fern goldens → Run workflow**, select any
  branch, and optionally enter an exact `fern-version` and comma-separated
  `fixtures` subset. Tag dispatches are rejected. Use a feature branch for new
  fixtures and expected-red Fern upgrades so the repair cycle remains isolated.

Both events use the selected branch ref for checkout, concurrency, and normal
fast-forward publication. Runs for one branch queue instead of cancelling a
writer midway; different branches remain independent.

## Add or change a fixture

Before spending a generate on a shape, check
[`fern-limitations.md`](fern-limitations.md): it records, with the measured
evidence, which shapes Fern 5.20.0 discards, ignores or refuses — a golden cannot
pin a style Fern throws away — and which candidate pools are exhausted.

Work on one corpus row at a time. There are two routes to the same golden, and
who can run them differs:

- **[Route A — the local Docker loop](#route-a--the-local-docker-loop-any-agent).**
  Any agent or maintainer with Docker and the `fern` CLI can run it end to end on
  one machine, with no push and no remote state.
- **[Route B — the hosted workflow dispatch](#route-b--the-hosted-workflow-dispatch-operator-only).**
  The operator's route: it publishes the golden back to the branch and records
  run evidence, and it is what the Monday schedule and routine maintenance use.

**A dispatched agent cannot take Route B**, because a `workflow_dispatch` can
only select a ref that already exists on the remote and publication is the
lifecycle's job, not the agent's — so an agent that may not push can never
dispatch a run against its own work. Route A is therefore the procedure to follow
when adding or repairing a fixture from inside a working tree; Route B is how an
operator refreshes or republishes one afterwards.

### Both routes resolve the same generator image and configuration

Verify this before trusting a locally generated golden, by naming where each
route resolves each of the two. They agree because Route B *is* Route A with the
version supplied from a workflow input:

| | Route A (local) | Route B (hosted) |
|---|---|---|
| **generator image** | `just fern-goldens-generate --version X` → `scripts/fern-goldens` `generate()`, which validates `X` and passes it to the generator script | the `Generate every selected fixture independently` step of [`fern-goldens.yml`](../.github/workflows/fern-goldens.yml) turns `inputs.fern-version` into that same `just fern-goldens-generate --version X` |
| **generator config** | `scripts/generate-fern-fixture.sh`, which reads the fixture's row from [`fern-generator-config.txt`](../tests/fixtures/fern-generator-config.txt) and writes `generators.yml` | identical — the workflow has no generator-config input and no second config site |

Both therefore emit one `generators.yml` naming `fernapi/fern-python-sdk` at the
resolved version, and both apply the corpus-wide `pydantic_config.enum_type:
python_enums` that `generate-fern-fixture.sh` writes unconditionally for every
fixture (crozier renders string enums as real `enum.Enum` classes; see
[`matching.md`](matching.md)). A fixture's own non-default settings — audiences,
`client_class_name`, `extra_fields` — reach the same block from
`fern-generator-config.txt`, so a golden generated locally is the artifact the
hosted route would have published.

### Route A — the local Docker loop (any agent)

Needs Docker, the `fern` CLI, Rust, and Ruff; publishes nothing. `just setup-fern`
installs and starts what is missing (it also runs from the session-start hook, so
it is usually already done).

1. Create a feature branch. Add or update one numbered, eight-cell `CORPUS.md`
   row with its unique spec name, credential-free HTTPS source URL, and pinned
   source ref. A direct spec URL must end in `.json`, `.yaml`, or `.yml`. A
   generator setting no OpenAPI document can express needs no new spec: give the
   already-registered source a second row name and declare the setting for that
   name in `fern-generator-config.txt`.
2. Register the same name as a `Corpus` in `tests/e2e.rs` with `unmatched: &[]`,
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

### Route B — the hosted workflow dispatch (operator only)

Push the branch first; a dispatch can only select a ref the remote already has.
Then, from **Actions → Fern goldens → Run workflow**, or equivalently:

```sh
gh workflow run fern-goldens.yml --ref <branch> \
  -f fern-version="$pin" -f fixtures=<name>
```

`$pin` is the same provenance-derived version Route A step 3 reads; a dispatch
never guesses it.

Both inputs are optional, and **neither blank is a safe default**:

- `fern-version` — an exact `fernapi/fern-python-sdk` semantic version. Leaving
  it blank deliberately starts an upgrade to the latest stable image tag; it is
  not a request to preserve the current shared runtime/scaffolding pin, so a
  blank turns a fixture add into a Fern-upgrade repair cycle. Give the exact
  version the goldens record.
- `fixtures` — comma-separated `CORPUS.md` names. Select the new or changed
  fixture explicitly; leave this blank only when refreshing all corpus rows that
  already have committed goldens.

Then:

1. Expect the first run for a new fixture, a changed URL/ref, or a Fern upgrade
   branch to be red. Generation runs each selection independently. Every
   successful fixture is installed atomically. Before comparison starts, the
   publication job makes one best-effort commit of all successful fixture trees,
   pushes it with
   `expected/.crozier-fern-golden.json`, which records the exact generator
   version and the manifest name, ref, and URL, and uploads immutable generation
   evidence. A failed fixture preserves its prior complete golden and provenance;
   it does not discard successful sibling results.
2. Inspect the GitHub job summaries and the generation, publication, and
   comparison logs. The `fern-goldens-generation-<run-id>-<attempt>` artifact
   contains `generation-summary.txt`, `generation-failures.txt`, the exact known
   upstream failure list, per-fixture generation logs, and the patch/archive of
   successful output. The later
   `fern-goldens-comparison-<run-id>-<attempt>` artifact contains
   `comparison-summary.txt`, `comparison.log`, and separate known-upstream,
   spec-fetch, and comparison-process failure reports. Comparison covers every
   available managed corpus golden, not only the fixtures selected for
   generation. It runs one fixture per process with progress heartbeats and
   reports differing paths, Crozier generation failures, processing failures,
   and fetch failures without fail-fast. Run `just fixtures-diff <fixture>`
   locally when a full unified diff is needed.
3. Repair Crozier on the same feature branch. Use `just fixtures-gaps` to
   re-measure each `unmatched` list; never edit Fern's
   output to make Crozier pass. Commit and push the repair, then dispatch the
   workflow again with the same inputs. Repeat until every `unmatched` list is
   empty again, the aggregate comparison is
   green, and the final run reports no generated changes and no publication.

Once a fixture's exact generator version and manifest identity are current, a
rerun fetches the source but skips Fern generation. A fully repaired final rerun
then compares green with no generated changes, and publication is a no-op. When
`fern-version` was initially
blank, the expected repair includes updating Crozier's pinned Fern-derived
runtime/scaffolding metadata and `NOTICE` when the aggregate diff requires it.
Use the exact resolved version shown in the run evidence on later reruns so a
newly released Fern version cannot join the same repair cycle.

### Exact known upstream failures

`calorieninjas.com` is the single registered exception across the whole corpus at
`fernapi/fern-python-sdk:5.20.0`. Its source operation has no `operationId`, and
Fern emits unnamed methods (`def (` and `_raw_client.(`) before Ruff rejects the
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
remove the failure registration and let the managed workflow publish its
provenanced tree; CalorieNinjas then rejoins normal byte comparison.

Red is expected during an upgrade loop. Successful fixtures are committed on a
best-effort basis and remain usable even when another selection fails generation
or Crozier still differs. Publication, the generation summary, and generation
evidence complete before the isolated comparison job can start, so a terminated
comparison runner cannot lose successful Fern output. The final status job
accounts for generation, publication, both job summaries, comparison, and both
required evidence uploads; a missing/failed phase stays red. If the comparison
runner is terminated before its upload step, the comparison artifact may be
absent, but the earlier generation artifact and published fixture commit remain.

## Publication safety

Each fixture is generated into a same-filesystem staging directory and replaces
`expected/` only after the complete packaged SDK and provenance are ready. The
workflow stages only fixtures listed as successfully generated; it never commits
unrelated branch changes or a partial failed tree.

Before committing, publication fetches the selected remote branch and requires
its head to equal the workflow checkout. If the branch advanced while generation
was running, publication refuses to commit or push. Let the other branch update
finish and dispatch again. Successful publication uses an ordinary fast-forward
push—never force-push—and same-branch workflow runs are queued so two workflow
writers do not race.

## Local diagnostics

Route A above is the local generation procedure; the commands here are the wider
local surface around it. GitHub Actions still owns routine maintenance and is the
only thing that publishes: every local command requires the same Fern, Docker,
Rust, and Ruff prerequisites as the workflow and writes nothing to a branch.

Generate selected fixtures and then run the aggregate comparison:

```sh
just fern-goldens --version 5.20.0 --fixture anchore.io
```

Repeat `--fixture` for an exact multi-fixture selection. Omit `--version` to use
the latest stable Fern tag; omit all `--fixture` arguments to select existing
corpus goldens.

Keep generation and comparison separate when diagnosing a phase:

```sh
just fern-goldens-generate --version 5.20.0 --fixture anchore.io
just fern-goldens-compare
```

The second command deliberately compares every available managed golden. For a
narrower human-readable diff after that aggregate pass, use
`just fixtures-diff anchore.io`, or add a literal path substring such as
`just fixtures-diff anchore.io client.py`.

Any fixture can carry fixture-owned non-default settings as a row in the shared
table [`fern-generator-config.txt`](../tests/fixtures/fern-generator-config.txt):
the audience list, Crozier strict-audience identity, Fern `client_class_name`,
and Fern `pydantic_config.extra_fields`. `scripts/generate-fern-fixture.sh` loads
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
`scripts/generate-fern-fixture.sh` writes `pydantic_config.enum_type:
python_enums` into `generators.yml` for every fixture it generates — on both
routes, since both drive the same script. Fern records it in each golden's
`.fern/metadata.json` (`generatorConfig`) and the e2e normalizes that block off
both sides, so it never shows up as a per-fixture setting; regenerating a golden
any other way silently reverts its enums to Fern's default open-`Literal` union.
