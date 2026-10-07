// CI's tier routing: the selection `just ci-check` makes, fed the GitHub
// events the workflows run on, over a scratch repository with an origin/main.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { join } from "node:path";
import { test } from "node:test";
import { commitChange, git, scratchWorkspace } from "./support.mjs";

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
