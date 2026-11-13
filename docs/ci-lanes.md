# CI lanes

`.github/workflows/ci.yml` runs one `lint` job and one test job per platform. None waits for
another. `tools/ci/lanes.json` is the executable inventory: every test, build, coverage and
budget entrypoint, with the platforms that owe it. `lane-inventory:lint` fails a change that
loses one, and `.github/governance.json` declares the contexts branch protection requires:
the four job ids, and nothing else a pull request push starts (`ci:test` expands every
workflow, reusable call and matrix leg against it).

| Lane | Limit | Runs |
| --- | --- | --- |
| `lint` | 30 min | Release guard, pull request title, suppressions comment, `just ci-lint` (format, lint, typecheck, supply chain, doc), judged lint over the diff, visual docs |
| `test-linux` | 240 min | Crate dry run, install and smoke, packaging, offline projects, SDK environments, host budget, live and corpus proof |
| `test-windows` | 150 min | Offline projects, SDK environments, install and smoke |
| `test-macos` | 150 min | Offline projects, SDK environments, install and smoke |

**The limits above 30 let a broad change finish; none is meant to cut off work that would pass.** Run
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
90, so a cold one needs about 110. On 2026-11-08 broad pull requests took about 95 minutes on
Linux, 77 to more than 90 on Windows and more than 120 on macOS; the old 90-minute Windows limit
cancelled #790 and #792, and the old 120-minute macOS limit cancelled #792, with nothing failed.
The old 150-minute Linux limit cancelled #793 the same day: its main
tier ran about 60 minutes and its final census-fallback, corpus-match and live-e2e step more
than 78 before the cut-off. Windows and macOS are now at 150 and Linux at 240. Mac's stands until that lane has a warm result
cache (main's cache writer serves lint, Linux and Windows only; whether Mac joins it is an open
decision) or the follow-up on the cold Mac leg is resolved.

**CI budgets.** The root `budgets.yaml` registers three `release-tail` budgets:
`crozier-ci-check-time` (the longest counted job, 1800 s), `crozier-ci-job-count` (jobs per
pull-request push, 4) and `crozier-pr-read-requests` (GitHub reads per pull request, 2). The
last step of release.yml's `major-tag` job measures them over the release's pull requests with
`scripts/actions-budget-figures.sh` (dero-skills' copy) from `onevcs host` answers. GitHub
Actions' run and job records for these lanes are what they read. Nothing reads that step's
result, so an over figure turns it red after everything has published. The 30-minute line is a
budget reading at each release, not a job timeout, while the lanes above need more. `just
budgets` excludes the `release-tail` and `onepipeline` labels, so the gate never reads GitHub.
`tools/ci-journeys/tests/release-tail.test.mjs` runs that step over recorded answers.

## Golden replays

The golden byte comparisons (`crozier-e2e:test`, the corpus recipes) and the suites that share
their build (`sdk-env`, `runtime`) run on the `e2e` cargo profile: crozier at opt-level 2 with
debug assertions and overflow checks on, so a replay panics wherever a dev build would. Most of
a large golden's time is crozier's own generation and comparison, which run about four times
faster there. Coverage and the instrumented measurements stay on `dev`. Each nextest run drives
a copy of the binary its first test pins, so a concurrent rebuild cannot reach it.

On Linux, `corpus-match:test-offline` runs the byte-match and its strict form through their
real recipes with sockets denied, so the live step runs each once (`carried` in
`tools/ci/lanes.json`). The offline proof's census, refusal-class and fallback recipes are
`corpus-offline-tools:test`, a project of its own: an installer, workflow, CI, judged-lint,
refusal or visual-docs edit selects no golden comparison, which
`tools/ci-journeys/tests/selection.test.mjs` checks over the real graph.

## Setup that can fail without a code change

- Each bootstrapping job runs `tools/ci/require-tools.mjs` after its install steps, so an
  installer that reported success without its executable is named before the gate starts.
- The judged lint retries a batch the judge left unanswered on the same tree. If it is still
  unanswered, the lane's last step cancels the run: the required `lint` context is then
  neither `success` nor `failure`. Re-run the workflow once the judge answers.
- The visual-docs capture fetches its pinned tools through `screenshots/fetch-tool.sh`, which
  retries a transient transfer failure.

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
