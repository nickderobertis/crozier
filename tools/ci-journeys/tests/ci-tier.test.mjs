// CI's tier routing: the selection `just ci-lint` and `just ci-test` make, fed the GitHub
// events the workflows run on, over a scratch repository with an origin/main.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { existsSync, rmSync } from "node:fs";
import { basename, join } from "node:path";
import { test } from "node:test";
import { commitChange, git, project, ran, scratchWorkspace, write } from "./support.mjs";

function decide(root, env) {
  const clean = Object.fromEntries(Object.entries(process.env).filter(([key]) => !key.startsWith("GITHUB_")));
  const run = spawnSync(process.execPath, [join(root, "tools/ci/ci-tier.mjs"), "--print"], {
    cwd: root, env: { ...clean, ...env }, encoding: "utf8",
  });
  assert.equal(run.status, 0, run.stderr);
  return JSON.parse(run.stdout);
}

test("a release-plz pull request is scoped like any other: its lint lane holds its content", (t) => {
  const root = scratchWorkspace(t);
  const base = git(root, "rev-parse", "HEAD");
  const decision = decide(root, {
    GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "release-plz-2026-10-07T12-00-00Z", GITHUB_BASE_REF: "main",
  });
  assert.deepEqual(decision, { tier: "affected", base, reason: "pull request: merge base with origin/main" });
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

test("a push has no change to scope against: CI does not run on one, and if asked it sweeps", (t) => {
  const root = scratchWorkspace(t);
  const before = git(root, "rev-parse", "HEAD");
  commitChange(root, "a/src.txt", "merged\n");
  const decision = decide(root, { GITHUB_EVENT_NAME: "push" });
  assert.equal(decision.tier, "sweep");
  assert.match(decision.reason, /event 'push' has no change to scope against/);
  assert.notEqual(decision.base, before);
});

test("a pull request sharing no history with its base branch runs the broader tier", (t) => {
  const root = scratchWorkspace(t);
  git(root, "checkout", "--quiet", "--orphan", "unrelated");
  commitChange(root, "a/src.txt", "a history of its own\n");
  const decision = decide(root, { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "unrelated", GITHUB_BASE_REF: "main" });
  assert.equal(decision.tier, "sweep");
  assert.match(decision.reason, /no merge base between HEAD and origin\/main in this checkout/);
});

test("an event with no derivable base runs the broader tier rather than a scoped one", (t) => {
  const root = scratchWorkspace(t);
  for (const env of [
    { GITHUB_EVENT_NAME: "push" },
    { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "x", GITHUB_BASE_REF: "$(id)" },
    { GITHUB_EVENT_NAME: "workflow_dispatch" },
  ]) {
    assert.equal(decide(root, env).tier, "sweep", JSON.stringify(env));
  }
});

// The dispatch itself, through the recipe the workflows call: the tier it
// chose, the base it hands the gate as NX_BASE, the arguments it forwards, and
// the gate's status as its own.
function ciLane(root, recipe, args, env) {
  const clean = Object.fromEntries(Object.entries(process.env).filter(([key]) =>
    !key.startsWith("GITHUB_") && key !== "NX_BASE"));
  const run = spawnSync("just", [recipe, ...args], {
    cwd: root, env: { ...clean, NX_DAEMON: "false", NX_NO_CLOUD: "true", ...env }, encoding: "utf8",
    shell: process.platform === "win32",
  });
  return { status: run.status, stdout: run.stdout ?? "", output: `${run.stdout}${run.stderr}` };
}

test("each lane recipe runs its gate in the tier it chose, with its base and the arguments it was given", (t) => {
  const root = scratchWorkspace(t);
  const base = git(root, "rev-parse", "HEAD");
  commitChange(root, "a/src.txt", "feature\n");

  const pr = ciLane(root, "ci-test", [], { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main" });
  assert.equal(pr.status, 0, pr.output);
  assert.match(pr.stdout, /ci-tier: affected — pull request: merge base with origin\/main/);
  assert.match(pr.stdout, new RegExp(`gate: affected tier against ${base.slice(0, 12)} \\(NX_BASE=${base}\\)`));
  assert.ok(ran(root, "a") && !ran(root, "b"), pr.output);

  rmSync(join(root, "ran-a"));
  const narrowed = ciLane(root, "ci-test", ["--exclude=a"], { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main" });
  assert.equal(narrowed.status, 0, narrowed.output);
  assert.match(narrowed.stdout, /gate: projects: \(none\)/);
  assert.ok(!ran(root, "a"), narrowed.output);

  const dispatched = ciLane(root, "ci-test", ["--exclude=a"], { GITHUB_EVENT_NAME: "workflow_dispatch" });
  assert.equal(dispatched.status, 0, dispatched.output);
  assert.match(dispatched.stdout, /gate: broader tier \(--sweep\)/);
  assert.match(dispatched.stdout, /gate: projects: b\n/);
  assert.ok(ran(root, "b"), dispatched.output);
});

test("the lint lane reaches a promoted project's lint in the same step; the test lane leaves it to a named one", (t) => {
  const root = scratchWorkspace(t);
  write(root, { "a/project.json": project("a", { tags: ["type:tier", "tier:promoted"], targets: {
    test: { command: "node -e \"require('fs').writeFileSync('ran-a-test', '')\"" },
    lint: { command: "node -e \"require('fs').writeFileSync('ran-a-lint', '')\"" },
  } }) });
  commitChange(root, "a/src.txt", "feature\n");
  const env = { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main" };
  const linted = ciLane(root, "ci-lint", [], env);
  assert.equal(linted.status, 0, linted.output);
  assert.ok(ran(root, "a-lint") && !ran(root, "a-test"), linted.output);
  const offline = ciLane(root, "ci-test", ["--exclude=tag:tier:promoted"], env);
  assert.equal(offline.status, 0, offline.output);
  assert.ok(!ran(root, "a-test"), offline.output);
  const named = ciLane(root, "ci-test", ["--projects=tag:tier:promoted"], env);
  assert.equal(named.status, 0, named.output);
  assert.ok(ran(root, "a-test"), named.output);
});

test("a gate argument carrying shell syntax is refused before anything runs", (t) => {
  const root = scratchWorkspace(t);
  commitChange(root, "a/src.txt", "feature\n");
  const refused = ciLane(root, "ci-test", ["--projects=a;touch${IFS}pwned"], {
    GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main",
  });
  assert.equal(refused.status, 2, refused.output);
  // On Windows the argument reaches ci-tier through Git Bash's sh, which has
  // dropped the braces by then; it is refused all the same.
  assert.match(refused.output, /ci-tier: gate argument "--projects=a;touch\$\{?IFS\}?pwned" carries a character the gate never takes/);
  assert.ok(!existsSync(join(root, "pwned")) && !ran(root, "a"), refused.output);
});

test("a lane recipe exits with the gate's own failure", (t) => {
  const root = scratchWorkspace(t);
  write(root, { "a/project.json": JSON.stringify({ name: "a", tags: ["type:tooling"], targets: { test: { command: "exit 3" } } }) });
  commitChange(root, "a/src.txt", "breaks\n");
  const failed = ciLane(root, "ci-test", [], { GITHUB_EVENT_NAME: "pull_request", GITHUB_HEAD_REF: "feature/x", GITHUB_BASE_REF: "main" });
  assert.notEqual(failed.status, 0, failed.output);
  assert.match(failed.output, /gate: a target failed/);
});
