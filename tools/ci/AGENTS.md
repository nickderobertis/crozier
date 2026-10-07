# ci

- The workflows call recipes (`just ci-check`), never Nx directly; the tier an
  event owes is decided in `ci-tier.mjs` alone, so the workflow-contract tests and
  the node suites here are the whole proof of CI's routing.
- `gate.mjs` validates `NX_BASE` before Nx runs and strips it from Nx's
  environment: Nx reads that variable itself and hands it to a shell.
- The module-boundary rule is `scripts/check-project-boundaries.mjs`, a shared
  script, so every project's `lint` can run it without depending on this project.
