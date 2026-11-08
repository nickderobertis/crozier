#!/usr/bin/env node
// Which tier of the gate a CI run owes, derived from the GitHub event.
//
//   node tools/ci/ci-tier.mjs [--print] [--recipe=NAME] [-- GATE-ARGS...]
//
// CI runs on pull requests, each from an explicitly derived base:
//   * every pull request runs the affected tier against the merge base of its
//     head with its base branch. A release pull request is no exception: its lint
//     lane holds it to version and changelog edits (scripts/release-branch-guard.mjs)
//     and its test lanes skip it;
//   * anything else (a manual diagnostic run), a base branch it cannot refresh from
//     origin, or a base this checkout cannot resolve, runs the broader tier and says
//     why: a scoped run must never pass as a full one.
//
// `--print` prints the decision as JSON and runs nothing (the workflow-contract
// test drives it that way); otherwise it runs the named recipe (`check` by default)
// with the decision: `lane-lint`, `lane-test` and `lane-budgets-host` are what the
// lint and test lanes call through `just ci-lint`, `just ci-test` and
// `just ci-budgets-host`.
import { spawnSync } from "node:child_process";
import { existsSync, realpathSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");
const NAME = "ci-tier";
const RECIPES = new Set(["check", "lane-lint", "lane-test", "lane-budgets-host"]);
const SHA40 = /^[0-9a-f]{40}$/;
const BRANCH = /^[A-Za-z0-9][A-Za-z0-9._/-]*$/;

function git(args) {
  const result = spawnSync("git", args, { cwd: ROOT, encoding: "utf8" });
  return { ok: result.status === 0, out: (result.stdout ?? "").trim() };
}

/** The tier, its base (affected tier only), and the reason, for one event. */
export function decide(env = process.env) {
  const event = env.GITHUB_EVENT_NAME ?? "";
  const sweep = (reason) => ({ tier: "sweep", reason });
  if (event === "pull_request") {
    const baseRef = env.GITHUB_BASE_REF ?? "";
    if (!BRANCH.test(baseRef) || baseRef.includes("..")) {
      return sweep(`pull request with no usable base branch ('${baseRef}')`);
    }
    const refreshed = git(["fetch", "--no-tags", "--quiet", "origin", `+refs/heads/${baseRef}:refs/remotes/origin/${baseRef}`]);
    if (!refreshed.ok) {
      return sweep(`could not refresh origin/${baseRef} from origin, so its merge base could be stale`);
    }
    const base = git(["merge-base", `origin/${baseRef}`, "HEAD"]);
    if (!base.ok || !SHA40.test(base.out)) {
      return sweep(`no merge base between HEAD and origin/${baseRef} in this checkout`);
    }
    return { tier: "affected", base: base.out, reason: `pull request: merge base with origin/${baseRef}` };
  }
  return sweep(`event '${event || "(none)"}' has no change to scope against`);
}

function main() {
  const argv = process.argv.slice(2);
  const split = argv.indexOf("--");
  const own = split < 0 ? argv : argv.slice(0, split);
  const gateArgs = split < 0 ? [] : argv.slice(split + 1);
  const recipeArg = own.find((arg) => arg.startsWith("--recipe="));
  const recipe = recipeArg ? recipeArg.slice("--recipe=".length) : "check";
  const unknown = own.filter((arg) => arg !== "--print" && arg !== recipeArg);
  if (unknown.length > 0 || !RECIPES.has(recipe)) {
    console.error(`${NAME}: unknown argument '${unknown[0] ?? recipeArg}'`);
    console.error(`${NAME}: usage: node tools/ci/ci-tier.mjs [--print] [--recipe=${[...RECIPES].join("|")}] [-- GATE-ARGS...]`);
    process.exit(2);
  }
  // On Windows `just` is started through a shell, which would read these before
  // the gate could refuse them; the gate's own arguments never need its syntax.
  const unsafe = gateArgs.find((arg) => !/^[A-Za-z0-9_.,:=@\/+-]+$/.test(arg));
  if (unsafe !== undefined) {
    console.error(`${NAME}: gate argument ${JSON.stringify(unsafe)} carries a character the gate never takes`);
    console.error(`${NAME}: pass the gate's flags and project names as they are (letters, digits and _.,:=@/+-)`);
    process.exit(2);
  }
  const decision = decide();
  if (own.includes("--print")) {
    console.log(JSON.stringify(decision));
    return;
  }
  console.log(`${NAME}: ${decision.tier} — ${decision.reason}`);
  const env = { ...process.env };
  const args = [recipe, ...(decision.tier === "sweep" ? ["--sweep"] : []), ...gateArgs];
  if (decision.tier === "affected") env.NX_BASE = decision.base;
  else delete env.NX_BASE;
  const run = spawnSync("just", args, { cwd: ROOT, env, stdio: "inherit", shell: process.platform === "win32" });
  process.exit(run.status ?? 1);
}

// Node names its main module by its real path, so the path it was started by is
// resolved the same way: through macOS's /var -> /private/var, say.
if (process.argv[1] && existsSync(process.argv[1]) && realpathSync(process.argv[1]) === fileURLToPath(import.meta.url)) main();
