# tools/ci-profile

A measurement harness: it profiles CI runs and nothing in the product depends on it.

- `node tools/ci-profile/ci-profile.mjs run <run-id>` reads one run of `ci.yml` into
  JSON (per lane: steps, targets with slots, test cases, crozier phases, spawn costs);
  `local <artifact-dir>` reads artifacts already downloaded. Fetches are cached and
  refused under 40% of the GitHub core rate limit.
- The reader parses what each runner prints on CI, not on a terminal: Nx opens each
  task as a `::group::` with its status icon, and Node's test runner prints TAP.
- `spike/schedule.mjs` replays measured durations through Nx's task graph. It models
  `parallelism: false` as Nx runs it: alone, with every other task drained first.
- `spike/spawncount/` counts children with a `sitecustomize` audit hook and a Node
  `--import` preload. `shutil.copytree` recurses through its own public name, so only
  the outermost call is timed.
