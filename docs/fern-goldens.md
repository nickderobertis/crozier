# Maintaining Fern goldens

The normal maintenance path for numbered rows in
[`tests/fixtures/CORPUS.md`](../tests/fixtures/CORPUS.md) is the manually
dispatched **Fern goldens** GitHub Actions workflow. It runs Fern in the hosted
environment, records reproducible provenance, compares Crozier, and safely
publishes every complete Fern result back to the selected feature branch.

## Add or change a fixture

Work on one corpus row at a time:

1. Create a feature branch. Add or update one numbered, eight-cell `CORPUS.md`
   row with its unique spec name, credential-free HTTPS source URL, and pinned
   source ref. A direct spec URL must end in `.json`, `.yaml`, or `.yml`.
2. For a new fixture, register the same name as a `Corpus` in `tests/e2e.rs` with
   `matched: &[]`. Keep `matched` empty until Crozier reproduces files exactly.
3. Commit and push the branch, then open **Actions → Fern goldens → Run
   workflow** and select that branch. The workflow inputs are:

   - `fern-version` — an exact `fernapi/fern-python-sdk` semantic version. Leaving
     it blank deliberately starts an upgrade to the latest stable image tag; it
     is not a request to preserve the current shared runtime/scaffolding pin.
   - `fixtures` — comma-separated `CORPUS.md` names. Select the new or changed
     fixture explicitly; leave this blank only when refreshing all corpus rows
     that already have committed goldens.

4. Expect the first run for a new fixture, a changed URL/ref, or a Fern upgrade
   to be red. Generation runs each selection independently. Every successful
   fixture is installed atomically, then the publication phase commits all
   successful fixture trees together and pushes them with
   `expected/.crozier-fern-golden.json`, which records the exact generator
   version and the manifest name, ref, and URL. A failed fixture preserves its
   prior complete golden and provenance; it does not discard successful sibling
   results.
5. Inspect the run summary and the generation, comparison, and publication step
   logs. Download the `fern-goldens-<run-id>-<attempt>` artifact for the aggregate
   `generation-summary.txt`, `generation-failures.txt`, per-fixture generation
   logs, `comparison-summary.txt`, `comparison.log`, spec-fetch failures, and the
   patch/archive of successful output. Comparison covers every available managed
   corpus golden, not only the fixtures selected for generation, and reports all
   missing, unexpected, changed, generation-failed, and processing-failed cases
   without fail-fast.
6. Repair Crozier on the same feature branch. Use `just fixtures-candidates` to
   add only newly byte-matched paths to each `matched` list; never edit Fern's
   output to make Crozier pass. Commit and push the repair, then dispatch the
   workflow again with the same inputs. Repeat until the aggregate comparison is
   green.

Once a fixture's exact generator version and manifest identity are current, a
rerun fetches the source but skips Fern generation. A fully repaired rerun then
compares green and publication is a no-op. When `fern-version` was initially
blank, the expected repair includes updating Crozier's pinned Fern-derived
runtime/scaffolding metadata and `NOTICE` when the aggregate diff requires it.
Use the exact resolved version shown in the run evidence on later reruns so a
newly released Fern version cannot join the same repair cycle.

Red is expected during this loop. Successful fixtures are committed and remain
usable even when another selection fails generation or Crozier still differs.
The final job status is deferred until evidence upload and publication have both
been attempted.

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

GitHub Actions owns routine golden maintenance and publication. The repository's
local commands are reproduction aids; they require the same Fern, Docker, Rust,
and Ruff prerequisites as the workflow and do not publish a branch.

Generate selected fixtures and then run the aggregate comparison:

```sh
just fern-goldens --version 4.35.0 --fixture anchore.io
```

Repeat `--fixture` for an exact multi-fixture selection. Omit `--version` to use
the latest stable Fern tag; omit all `--fixture` arguments to select existing
corpus goldens.

Keep generation and comparison separate when diagnosing a phase:

```sh
just fern-goldens-generate --version 4.35.0 --fixture anchore.io
just fern-goldens-compare
```

The second command deliberately compares every available managed golden. For a
narrower human-readable diff after that aggregate pass, use
`just fixtures-diff anchore.io`, or add a literal path substring such as
`just fixtures-diff anchore.io client.py`.
