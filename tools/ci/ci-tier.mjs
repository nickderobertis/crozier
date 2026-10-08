#!/usr/bin/env node
// Which tier of the gate a CI run owes, derived from the GitHub event.
//
//   node tools/ci/ci-tier.mjs [--print] [-- GATE-ARGS...]
//
// crozier batches releases: release-plz's release pull request accumulates the
// merges since the last tag, and a person merges it. So (references/ci.md,
// "Where the broader tier runs"):
//   * the release pull request (head branch `release-plz-*`) runs the broader
//     tier — the one sweep each release gets before it ships;
//   * every other pull request runs the affected tier against the merge base
//     of its head with its base branch;
//   * a push to main runs the affected tier against the commit the push
//     replaced (`github.event.before`, passed as CROZIER_PUSH_BEFORE);
//   * anything else, a base branch it cannot refresh from origin, or a base this
//     checkout cannot resolve, runs the broader tier and says why — a scoped run
//     must never pass as a full one.
//
// `--print` prints the decision as JSON and runs nothing (the workflow-contract
// test drives it that way); otherwise it runs `just check` with the decision.
import { spawnSync } from "node:child_process";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");
const NAME = "ci-tier";
const RELEASE_BRANCH_PREFIX = "release-plz-";
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
    const head = env.GITHUB_HEAD_REF ?? "";
    if (head.startsWith(RELEASE_BRANCH_PREFIX)) {
      return sweep(`release pull request (${head}): the broader tier runs at release-prep`);
    }
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
  if (event === "push") {
    const before = env.CROZIER_PUSH_BEFORE ?? "";
    if (!SHA40.test(before) || /^0+$/.test(before)) {
      return sweep(`push with no previous commit to compare against ('${before}')`);
    }
    if (!git(["cat-file", "-e", `${before}^{commit}`]).ok) {
      git(["fetch", "--no-tags", "--quiet", "origin", before]);
      if (!git(["cat-file", "-e", `${before}^{commit}`]).ok) {
        return sweep(`push: the replaced commit ${before} is not in this checkout`);
      }
    }
    return { tier: "affected", base: before, reason: "push: the commit the push replaced" };
  }
  return sweep(`event '${event || "(none)"}' has no change to scope against`);
}

function main() {
  const argv = process.argv.slice(2);
  const split = argv.indexOf("--");
  const own = split < 0 ? argv : argv.slice(0, split);
  const gateArgs = split < 0 ? [] : argv.slice(split + 1);
  const unknown = own.filter((arg) => arg !== "--print");
  if (unknown.length > 0) {
    console.error(`${NAME}: unknown argument '${unknown[0]}'`);
    console.error(`${NAME}: usage: node tools/ci/ci-tier.mjs [--print] [-- GATE-ARGS...]`);
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
  const args = ["check", ...(decision.tier === "sweep" ? ["--sweep"] : []), ...gateArgs];
  if (decision.tier === "affected") env.NX_BASE = decision.base;
  else delete env.NX_BASE;
  const run = spawnSync("just", args, { cwd: ROOT, env, stdio: "inherit", shell: process.platform === "win32" });
  process.exit(run.status ?? 1);
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) main();
