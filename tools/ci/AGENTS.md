# ci

- The workflows call recipes (`just ci-lint`, `just ci-test`), never Nx directly; the tier an
  event owes is decided in `ci-tier.mjs` alone, so the workflow-contract tests
  here and the node journeys in `tools/ci-journeys/` are the whole proof of CI's
  routing.
- Tests here read the workflows and run their steps with stand-in tools; a
  suite that drives the real git, just, Nx or cargo belongs to `ci-journeys`.
- `gate.mjs` validates `NX_BASE` before Nx runs and strips it from Nx's
  environment: Nx reads that variable itself and hands it to a shell.
- The module-boundary rule is `scripts/check-project-boundaries.mjs`, a shared
  script, so every project's `lint` can run it without depending on this project.
- `ci-caches.yml`'s job ids are the lanes' on purpose, for the `github.job` in the cache keys;
  its display names differ so it reports no required context.
- `lanes.json` is the frozen pre-refactor inventory plus what was added since; a row may
  move (`now`), never vanish silently. `lane-inventory.mjs` reconciles it, as
  `lane-inventory:lint`, which a tier manifest edit selects.
