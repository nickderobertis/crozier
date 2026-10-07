// The gate recipes' base selection and tiers, driven through the real recipes
// over a scratch repository: which base the affected tier keys off, that a
// hostile or unresolvable NX_BASE runs nothing, and that `--sweep` runs all.
// The scratch projects define only `test`, whose marker file shows exactly
// which projects the tier selected and ran.
import assert from "node:assert/strict";
import { test } from "node:test";
import { commitChange, git, just, ran, scratchWorkspace } from "./support.mjs";

test("with NX_BASE unset the affected tier keys off the merge base with origin/main", (t) => {
  const root = scratchWorkspace(t);
  const base = git(root, "rev-parse", "HEAD");
  commitChange(root, "a/src.txt", "a changed\n");

  const run = just(root, ["check"], { NX_BASE: undefined });

  assert.equal(run.status, 0, run.output);
  assert.match(run.stdout, new RegExp(`affected tier against ${base.slice(0, 12)} \\(merge base with origin/main\\)`));
  assert.match(run.stdout, /gate: projects: a\n/);
  assert.ok(ran(root, "a"), run.output);
  assert.ok(!ran(root, "b"), "b was not changed, so its test must not run");
});

test("NX_BASE set to a commit SHA is the affected base", (t) => {
  const root = scratchWorkspace(t);
  const afterA = commitChange(root, "a/src.txt", "a changed\n");
  commitChange(root, "b/src.txt", "b changed\n");

  const run = just(root, ["check"], { NX_BASE: afterA });

  assert.equal(run.status, 0, run.output);
  assert.match(run.stdout, new RegExp(`affected tier against ${afterA.slice(0, 12)} \\(NX_BASE=${afterA}\\)`));
  assert.match(run.stdout, /gate: projects: b\n/);
  assert.ok(ran(root, "b") && !ran(root, "a"), run.output);
});

test("NX_BASE that is neither a ref name nor a SHA fails closed and runs no target", (t) => {
  const root = scratchWorkspace(t);
  commitChange(root, "a/src.txt", "a changed\n");

  for (const hostile of ["main;touch pwned", "$(touch pwned)", "HEAD~1", "a b"]) {
    const run = just(root, ["check"], { NX_BASE: hostile });
    assert.notEqual(run.status, 0, `${hostile}: ${run.output}`);
    assert.match(run.stderr, /NX_BASE '.*' is neither a plain ref name nor a commit SHA; no target ran/);
  }
  assert.ok(!ran(root, "a") && !ran(root, "b"));
  assert.ok(!git(root, "status", "--porcelain", "--ignored").includes("pwned"));
});

test("NX_BASE naming no commit in the checkout fails closed and runs no target", (t) => {
  const root = scratchWorkspace(t);
  commitChange(root, "a/src.txt", "a changed\n");

  for (const missing of ["no-such-branch", "0123456789abcdef0123456789abcdef01234567"]) {
    const run = just(root, ["check"], { NX_BASE: missing });
    assert.notEqual(run.status, 0, run.output);
    assert.match(run.stderr, new RegExp(`NX_BASE '${missing}' does not name a commit in this checkout; no target ran`));
  }
  assert.ok(!ran(root, "a") && !ran(root, "b"));
});

test("with no origin/main and no NX_BASE the affected tier refuses rather than guessing", (t) => {
  const root = scratchWorkspace(t);
  git(root, "update-ref", "-d", "refs/remotes/origin/main");

  const run = just(root, ["check"], { NX_BASE: undefined });

  assert.notEqual(run.status, 0, run.output);
  assert.match(run.stderr, /no merge base between HEAD and origin\/main/);
  assert.ok(!ran(root, "a") && !ran(root, "b"));
});

test("--sweep runs every project's targets whatever changed", (t) => {
  const root = scratchWorkspace(t);

  const run = just(root, ["check", "--sweep"]);

  assert.equal(run.status, 0, run.output);
  assert.match(run.stdout, /broader tier \(--sweep\)/);
  assert.ok(ran(root, "a") && ran(root, "b"), run.output);
});

test("a promoted project leaves the affected tier unless --projects names it", (t) => {
  const root = scratchWorkspace(t);
  commitChange(root, "b/project.json", JSON.stringify({
    name: "b", tags: ["type:tooling", "tier:promoted"],
    targets: { test: { command: "node -e \"require('fs').writeFileSync('ran-b', '')\"" } },
  }));

  const skipped = just(root, ["check"]);
  assert.equal(skipped.status, 0, skipped.output);
  assert.match(skipped.stdout, /promoted, run by their own CI legs: b/);
  assert.ok(!ran(root, "b"));

  const named = just(root, ["check", "--projects=b"]);
  assert.equal(named.status, 0, named.output);
  assert.ok(ran(root, "b"), named.output);
});

test("an unknown argument or project is refused before anything runs", (t) => {
  const root = scratchWorkspace(t);
  for (const args of [["check", "--sweap"], ["check", "--projects=nope"], ["check", "--targets=te;st"]]) {
    const run = just(root, args);
    assert.notEqual(run.status, 0, `${args}: ${run.output}`);
  }
  assert.ok(!ran(root, "a") && !ran(root, "b"));
});
