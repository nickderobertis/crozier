# The judged tier's rule plugins

The `llmlint` PR check judges this repo against a rule set assembled from shared
plugins. This document records where that set comes from, why it comes from
there rather than over the network, and what it costs.

## The failure this repairs

`llmlint.yml` used to name five plugins by `raw.githubusercontent.com` URL. The
`llmlint` job's first llmlint step (`just lint-llm-validate`) resolves the
plugin set, and a GitHub runner starts with an **empty** plugin cache — so every
run fetched all five before judging anything. A connection reset there exits 2
before a single rule is evaluated, and because `llmlint` is a required check, the
branch cannot merge. Reproduced here with the origin refused and a cold cache:

```console
$ LLMLINT_CACHE_DIR=$(mktemp -d) https_proxy=http://127.0.0.1:9 llmlint config
llmlint: error: plugin https://raw.githubusercontent.com/…/base.llmlint.yml: io: Connection refused
$ echo $?
2
```

## What llmlint already tolerates, and what it doesn't

llmlint's own cache degrades gracefully: "A revalidation that *can't* be made —
offline, a transport failure, a refused request — reuses the cached copy and the
run keeps working: the cache is a speed-up, never a network dependency." Measured
against llmlint 0.4.1 over this repo's plugin set:

| plugin cache | origin | result |
| --- | --- | --- |
| cold (empty dir) | refused | **exit 2**, hard error — the CI failure |
| warm | refused | exit 0, resolves from the cache |
| warm, `confirmed_at` backdated to 2001, `LLMLINT_PLUGIN_TTL=0` | refused | exit 0, reuses the stale copy |
| warm, entry backdated | reachable | revalidates and adopts the newest version satisfying the pin |

So the only fatal case is the cold one — and a CI runner is cold on every job.
The repair is therefore about what the *tree* can answer with, not about making
the fetch more reliable.

## The mechanism: the plugins are vendored, and a lock records them

`llmlint.yml` resolves each shared plugin from a committed copy under
`llmlint-plugins/`. `llmlint-plugins/lock.json` is the record of that set: per
plugin, the `url` and `@pin` it was fetched from, the `file` it lives in, the
`version` that document declares, its `sha256`, and the `rules` it contributes.
There is no job-time plugin fetch left to flake.

The bundled `config_lint.yml` plugin stays a URL on purpose: it ships *inside*
the llmlint binary and resolves offline, so it is not a network dependency. The
lock records it as `"bundled": true` with the llmlint version its rules were
captured under, because its identity is the binary's, not the network's.

### Why not the alternatives

- **A bounded retry.** It narrows the window without closing it: an outage
  longer than the budget still fails the required check, and the check's runtime
  starts depending on how long the outage lasts. It also leaves the rule set a
  function of what the origin answered that day.
- **`actions/cache` across runs.** It only helps once a cache is warm, and the
  cold cases are exactly the ones that fail — a first run on a new PR branch (a
  branch reads its base's cache, not another PR's), a changed key, or the 7-day
  idle eviction. It would also make a required check's correctness depend on
  GitHub's cache service being up.
- **Exact `@version` pins (`@1.12.0`).** Measured to be *worse than the status
  quo*: the plugin URLs address `main`, a moving ref, so the first upstream bump
  makes the fetched document's declared version violate the pin, and a pin is an
  assertion — `llmlint: error: … requested version 1.0 but the config declares
  version 1.1`, exit 2, on an unrelated PR.
- **Seeding llmlint's on-disk cache from a committed copy, keeping `@1`.** The
  closest runner-up: a reachable origin would still revalidate and adopt a newer
  `1.x`, so freshness would stay automatic. Rejected on two counts — the rule set
  would still be whatever the network answered on the day (the record could only
  ever describe the offline fallback, not what actually judged the PR), and the
  seed would have to be written in the cache's private on-disk layout, which is
  llmlint's to change.

## What this freezes, and how the rules are refreshed

**Upstream rule changes no longer reach the judged tier on their own.** That is
the deliberate cost of this mechanism, not a side effect: the `@1` pins used to
mean the plugin authors' non-breaking bumps arrived automatically, and now they
arrive when someone runs

```console
$ just llmlint-plugins-refresh
```

which re-fetches every URL the lock records **at its recorded pin**, rewrites the
vendored copies and the lock, and prints the rules that moved. Commit
`llmlint-plugins/` and the lock together; the diff is the review. Run it when a
rule an `llmlint: ignore` directive names appears not to exist, when upstream
announces new rules, or on whatever cadence the repo wants its judge refreshed —
and note that a refresh can change the judged verdict on unrelated code, which is
why it lands as its own reviewable change rather than mid-PR.

Adding a plugin: add an entry with `name`, `url`, `pin`, and `file` to the lock,
add the `file` path to `llmlint.yml`, then refresh. Those four fields are the
hand-edited inputs; everything else in the lock is generated.

## What the repair changed about the rule set: nothing

The vendored set is exactly what the URLs resolved to at capture time — same
rules, same names, same source per rule, none dropped and none added. Before and
after both resolve **38 rules**:

| plugin | version | rules |
| --- | --- | --- |
| `base` | 1.12.0 | 17 |
| `ci` | 1.4 | 5 |
| `languages/bash` | 1.3.0 | 3 |
| `languages/rust` | 1.1 | 3 |
| `shapes/cli` | 1.1.1 | 2 |
| `config-lint` (bundled in the binary) | — | 8 |

A future refresh that moves a rule shows up as a change to `lock.json` — a
version bump, a different `sha256`, a name added or removed — so a genuine
upstream rule change reads as one, and a substitution under an unchanged name
cannot pass as the same rule. `just lint-llm-validate` now counts the vendored
copies among the versioned configs it checks, so a refresh that changed a
plugin's rules without upstream bumping its `version:` fails there too.

## Proving it: `just test-llmlint-plugins`

`tests/llmlint_plugins_test.py` drives the **real** llmlint binary over this
repo's **real** `llmlint.yml` with the plugin origin made unreachable from the
test process:

- every proxy variable points at a **closed local port** (bind to port 0, read
  the port, close the socket), so a fetch is refused rather than merely slow;
- `LLMLINT_CACHE_DIR` is a fresh empty directory, and `LLMLINT_PLUGIN_TTL=0`, so
  no cached copy exists and none would be trusted without revalidating —
  anything that resolves came out of the tree.

Under that induced failure it asserts the repaired config reaches a verdict
(`llmlint validate` exits 0), that the judged command's own path gets as far as
batching every recorded rule (`llmlint --plan-only`, which resolves plugins,
selects files, and plans batches without spending a judge call), and that the
resolved rules are exactly the ones the lock records; it
separately re-spells the same config with each plugin restored to its recorded
URL — the pre-repair configuration — and asserts *that* still fails, which is
what keeps the other assertions from being ones that could never fail.

Observed, in that order: with `llmlint.yml` restored to the pre-repair spelling,
all four llmlint-driving tests fail — the end-to-end one with the CI error
verbatim (`io: Connection refused`) — and reverting the workflow step as well
takes the whole suite to 11 failures across its 8 tests; over the repaired tree
all 8 pass, with the pre-repair control still failing offline. The suite is part
of `just check` and runs as its own step in the `llmlint` job with
`CROZIER_REQUIRE_LLMLINT=1`, which turns "llmlint is not installed" from a skip
into a failure so the required check cannot no-op.

## Provenance

The vendored documents are rule configs from
[`dero-skills`](https://github.com/nickderobertis/dero-skills) (same maintainer as
this repo), copied verbatim; `lock.json` records the exact URL, pin, and version
each came from. They are excluded from the judged file set in `llmlint.yml` —
they are someone else's authored config, judged in their own repository.
