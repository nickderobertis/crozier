// CI's tier routing: the selection `just ci-check` makes, fed the GitHub
// events the workflows run on, over a scratch repository with an origin/main.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { existsSync } from "node:fs";
import { join } from "node:path";
import { test } from "node:test";
import { commitChange, git, ran, scratchWorkspace, write } from "./support.mjs";

function decide(root, env) {
  const clean = Object.fromEntries(Object.entries(process.env).filter(([key]) => !key.startsWith("GITHUB_") && key !== "CROZIER_PUSH_BEFORE"));
  const run = spawnSync(process.execPath, [join(root, "tools/ci/ci-tier.mjs"), "--print"], {
    cwd: root, env: { ...clean, ...env }, encoding: "utf8",
  });
  assert.equal(run.status, 0, run.stderr);
  return JSON.parse(run.stdout);
}

test("the release-plz release pull request runs the broader tier", (t) => {
  const root = scratchWorkspace(t);
  const decision = decide(root, {
    GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "release-plz-2026-10-07T12-00-00Z", GITHUB_BASE_REF: "main",
  });
  assert.equal(decision.tier, "sweep");
  assert.match(decision.reason, /release pull request/);
});

test("any other pull request runs the affected tier against the merge base with its base branch", (t) => {
  const root = scratchWorkspace(t);
  const base = git(root, "rev-parse", "HEAD");
  commitChange(root, "a/src.txt", "feature\n");
  const decision = decide(root, { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main" });
  assert.deepEqual(decision, { tier: "affected", base, reason: "pull request: merge base with origin/main" });
});

test("a pull request scopes against its base branch as origin holds it now, not a stale local copy", (t) => {
  const root = scratchWorkspace(t);
  const stale = git(root, "rev-parse", "HEAD");
  const merged = commitChange(root, "b/src.txt", "merged upstream\n");
  git(root, "push", "--quiet", "origin", "main");
  git(root, "update-ref", "refs/remotes/origin/main", stale);
  commitChange(root, "a/src.txt", "feature\n");
  const decision = decide(root, { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main" });
  assert.deepEqual(decision, { tier: "affected", base: merged, reason: "pull request: merge base with origin/main" });
  assert.equal(git(root, "rev-parse", "origin/main"), merged);
});

test("a pull request whose base branch cannot be refreshed runs the broader tier", (t) => {
  const root = scratchWorkspace(t);
  commitChange(root, "a/src.txt", "feature\n");
  git(root, "remote", "set-url", "origin", join(root, "no-such-remote"));
  const decision = decide(root, { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main" });
  assert.equal(decision.tier, "sweep");
  assert.match(decision.reason, /could not refresh origin\/main from origin/);
});

test("a push to main runs the affected tier against the commit the push replaced", (t) => {
  const root = scratchWorkspace(t);
  const before = git(root, "rev-parse", "HEAD");
  commitChange(root, "a/src.txt", "merged\n");
  const decision = decide(root, { GITHUB_EVENT_NAME: "push", CROZIER_PUSH_BEFORE: before });
  assert.deepEqual(decision, { tier: "affected", base: before, reason: "push: the commit the push replaced" });
});

test("an event with no derivable base runs the broader tier rather than a scoped one", (t) => {
  const root = scratchWorkspace(t);
  for (const env of [
    { GITHUB_EVENT_NAME: "push", CROZIER_PUSH_BEFORE: "0".repeat(40) },
    { GITHUB_EVENT_NAME: "push", CROZIER_PUSH_BEFORE: "not a sha" },
    { GITHUB_EVENT_NAME: "push", CROZIER_PUSH_BEFORE: "f".repeat(40) },
    { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "x", GITHUB_BASE_REF: "$(id)" },
    { GITHUB_EVENT_NAME: "workflow_dispatch" },
  ]) {
    assert.equal(decide(root, env).tier, "sweep", JSON.stringify(env));
  }
});

// The dispatch itself, through the recipe the workflows call: the tier it
// chose, the base it hands the gate as NX_BASE, the arguments it forwards, and
// the gate's status as its own.
function ciCheck(root, args, env) {
  const clean = Object.fromEntries(Object.entries(process.env).filter(([key]) =>
    !key.startsWith("GITHUB_") && key !== "CROZIER_PUSH_BEFORE" && key !== "NX_BASE"));
  const run = spawnSync("just", ["ci-check", ...args], {
    cwd: root, env: { ...clean, NX_DAEMON: "false", NX_NO_CLOUD: "true", ...env }, encoding: "utf8",
    shell: process.platform === "win32",
  });
  return { status: run.status, stdout: run.stdout ?? "", output: `${run.stdout}${run.stderr}` };
}

test("ci-check runs the gate in the tier it chose, with its base and the arguments it was given", (t) => {
  const root = scratchWorkspace(t);
  const base = git(root, "rev-parse", "HEAD");
  commitChange(root, "a/src.txt", "feature\n");

  const pr = ciCheck(root, [], { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main" });
  assert.equal(pr.status, 0, pr.output);
  assert.match(pr.stdout, /ci-tier: affected — pull request: merge base with origin\/main/);
  assert.match(pr.stdout, new RegExp(`gate: affected tier against ${base.slice(0, 12)} \\(NX_BASE=${base}\\)`));
  assert.ok(ran(root, "a") && !ran(root, "b"), pr.output);

  const release = ciCheck(root, ["--exclude=a"], {
    GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "release-plz-2026-10-07T12-00-00Z", GITHUB_BASE_REF: "main",
  });
  assert.equal(release.status, 0, release.output);
  assert.match(release.stdout, /gate: broader tier \(--sweep\)/);
  assert.match(release.stdout, /gate: projects: b\n/);
  assert.ok(ran(root, "b"), release.output);
});

test("a gate argument carrying shell syntax is refused before anything runs", (t) => {
  const root = scratchWorkspace(t);
  commitChange(root, "a/src.txt", "feature\n");
  const refused = ciCheck(root, ["--projects=a;touch pwned"], {
    GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main",
  });
  assert.equal(refused.status, 2, refused.output);
  assert.match(refused.output, /ci-tier: gate argument "--projects=a;touch pwned" carries a character the gate never takes/);
  assert.ok(!existsSync(join(root, "pwned")) && !ran(root, "a"), refused.output);
});

test("ci-check exits with the gate's own failure", (t) => {
  const root = scratchWorkspace(t);
  write(root, { "a/project.json": JSON.stringify({ name: "a", tags: ["type:tooling"], targets: { test: { command: "exit 3" } } }) });
  commitChange(root, "a/src.txt", "breaks\n");
  const failed = ciCheck(root, [], { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main" });
  assert.notEqual(failed.status, 0, failed.output);
  assert.match(failed.output, /gate: a target failed/);
});
