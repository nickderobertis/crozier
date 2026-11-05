# Repin cost

Run from the repository root with the orchestrator checkout available through
`ONEPIPELINE_ORCHESTRATOR_ROOT` and journals through `ONEPIPELINE_RUNS_DIR`:

```sh
python3 tools/repin-cost/repin_cost.py --window runs:<run>[,<run>] --runs-root "$ONEPIPELINE_RUNS_DIR" --until <ISO-cutoff> --out <dir>
python3 tools/repin-cost/repin_cost.py --window base-carries:<sha>[,<sha>] --runs-root "$ONEPIPELINE_RUNS_DIR" --until <ISO-cutoff> --out <dir>
python3 tools/repin-cost/repin_cost.py compare tools/repin-cost/baseline tools/repin-cost/after
```

The base is the merge base with main of the last head pushed before the cutoff;
a branch introducing a required commit itself does not qualify. The five output
files preserve the spike's classification and interval rules. `compare` writes
`<after>/comparison.md`; append transcript-reviewed recipe-versus-hand counts
after running it. Re-running `compare` replaces that file.

`baseline/` preserves the spike's committed measurement. `selection-journeys/`
preserves its historical evidence; portable replacements run with
`just nx run repin-cost:test` against scratch journals, repositories and a guarded
loopback server. No live service or host runs directory is needed for tests.
`ONEPIPELINE_RESULTS_COMMAND` accepts a JSON argv prefix for a portable results
provider; the default is the orchestrator checkout's `node_modules/.bin/onepipeline`.

All REST reads use [the shared guard](../witness-search/rate_limit_guard.py) and
its response cache through `gh.py`. A non-200 response, including a missing job
log, stops the measurement. Cache evidence is ignored under `github-evidence/`.

Run measurements serially within one checkout: the inherited harness reserves
`refs/repin-cost/` and deletes those temporary refs when it finishes.
