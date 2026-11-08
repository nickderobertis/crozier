# CI lanes

`.github/workflows/ci.yml` runs one `lint` job and one test job per platform. None waits for
another. `tools/ci/lanes.json` is the executable inventory: every test, build, coverage and
budget entrypoint, with the platforms that owe it. `lane-inventory:lint` fails a change that
loses one, and `.github/governance.json` declares the contexts branch protection requires
once the transition below ends.

| Lane | Limit | Runs |
| --- | --- | --- |
| `lint` | 30 min | Release guard, suppressions comment, `just ci-lint` (format, lint, typecheck, supply chain, doc), visual docs |
| `test-linux` | 150 min | Crate dry run, install and smoke, packaging, offline projects, SDK environments, host budget, live and corpus proof |
| `test-windows` | 90 min | Offline projects, SDK environments, install and smoke |
| `test-macos` | 120 min | Offline projects, SDK environments, install and smoke |

**The limits above 30 are transitional and measured.** Run
[42345332459](https://github.com/nickderobertis/crozier/actions/runs/42345332459), a broad pull
request, spent this work across its old jobs: Linux 7371 s (Check 3053, SDK 160,
live/corpus/fallback 3814, packaging 168, install 176), Windows 4307 s (Check 3557, SDK 363,
install 387), macOS 3767 s (Check 2451, SDK 1153, install 163). That split includes lint work
that has since moved. The re-measure tightens these toward the 30-minute line. Linux has since
run in this shape: run [42433200026](https://github.com/nickderobertis/crozier/actions/runs/42433200026)'s
`test-linux` took 136 minutes (it failed one corpus-match test, since fixed). The Mac lane
has too: a whole-graph change's `ci-test` step alone took 84 minutes in run
[42402692714](https://github.com/nickderobertis/crozier/actions/runs/42402692714), and run
[42422342228](https://github.com/nickderobertis/crozier/actions/runs/42422342228) was cancelled at
90, so a cold one needs about 110. Its limit is 120 until the Mac lane has a warm result cache
(main's cache writer serves lint, Linux and Windows only; whether Mac joins it is an open
decision) or the follow-up on the cold Mac leg is resolved.

**Transition.** `gate`, `commitlint` and `llmlint` report the contexts main requires today, so
seven jobs run per pull request. Only `gate` has a `needs` edge, and it accepts a skipped test
lane only when lint's release guard step really passed. Once protection moves to the four
lanes, cleanup folds the title and judged checks into `lint`, removes the three jobs and
registers the CI budgets (`scripts/actions-budget-figures.sh` is ready for them).

## What selects a suite

A target's `inputs` are its cache key and its affected trigger. Three limits on that are easy
to miss:

- **Nx ignores a negated input when it decides what is affected.** `!{workspaceRoot}/x` only
  shapes the cache key, so a read set that must exclude something enumerates what it includes.
  That is why `censusScripts` in `nx.json` lists scripts.
- **The Python floor runs every member's suite.** `python-workspace:coverage` needs all their
  data, so on Linux and macOS a change to any member runs them all. Windows holds no floor.
  `corpus-licensing` is a task dependency rather than a project edge, because its suite reads
  all Markdown and an edge would send every documentation edit through the floor.
- **A generator, template, lock or toolchain edit is cold by design.** It reaches every journey.
  Selection and caching shrink other changes and repeat pushes, not this one.

`tools/ci-journeys/tests/selection.test.mjs` runs each of these through the real gate and Nx
over the real graph, observing what executes.

## What carries between runs

- **Results.** `tools/ci/result-cache.mjs` serves `.ci-results` to Nx over its self-hosted cache
  protocol on loopback. Restoring `.nx/cache` does not work: Nx finds entries through a database
  named after the machine id, so another runner sees none. The Actions key holds what Nx does
  not hash: the host and tool versions, locks, toolchain, generator pin and `ci.yml`.
- **Builds and packages.** `target`, the cargo registry and uv's wheel cache, keyed on their
  locks. Cargo still fingerprints every artifact and every environment is really built.
- **Never.** Targets whose external state is the proof (`cache: false`): SDK environments, live
  Prism, the offline corpus proof, the host budget.

**Main seeds them.** GitHub lets a pull request read caches from its own ref and its base
branch, so `ci-caches.yml` runs on each push to main and saves under the keys the lanes restore:
its job ids are the lanes', because the keys carry `github.job`, and `ci_workflow.rs` holds the
keys equal. Each job runs every offline project through the result cache, so a push pays for what
it changed. A red target there fails nothing: the step continues so the job's cache saves still
run, and only passing results are stored. It has no Mac job, because
`crozier-macos-runs-per-change` holds a change to two Mac-spending runs and a pull request and a
release build use both. So `test-macos` starts cold on a pull request's first push (up to the
measured 3767 s) and reuses results on its later ones.

## Platform-specific lint

Lint runs once on Linux. `tools/ci/lanes.json` (`platformLint`) names the only checks repeated
elsewhere, because they read different code there: clippy over crates with `cfg(unix)` or
`cfg(windows)` gates and `ty` over `sys.platform` branches on Windows, and clippy over the e2e
suite's `cfg(target_os = "linux")` case on macOS.

## Not on pull request pushes

`tools/ci/lanes.json` (`nonCheckWorkflows`) lists each workflow a push to main starts, and
`lane-inventory:lint` fails one that is unlisted or that a pull request also starts. None gates
anything: `ci-caches.yml` writes the caches above, `visual-docs-gallery.yml` publishes the gh-pages
root gallery, `golden-reach-base.yml` publishes the measurement `just census-repin` steps from, and
`release-plz.yml` is CD. `release.yml` is CD too. `visual-docs.yml` deletes a closed pull request's
preview and prunes gh-pages monthly. The broader tier
(`--sweep`) runs by hand and on a manual `ci` dispatch.
