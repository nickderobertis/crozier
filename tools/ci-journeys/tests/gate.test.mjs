// The gate recipes' base selection and tiers, driven through the real recipes
// over a scratch repository: which base the affected tier keys off, that a
// hostile or unresolvable NX_BASE runs nothing, and that `--sweep` runs all.
// The scratch projects define only `test`, whose marker file shows exactly
// which projects the tier selected and ran.
import assert from "node:assert/strict";
import { test } from "node:test";
import { existsSync, mkdirSync, readFileSync, rmSync, unlinkSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { spawnSync } from "node:child_process";
import { commitChange, git, just, project, ran, scratchWorkspace, write } from "./support.mjs";

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

test("NX_BASE set to a branch name is the affected base", (t) => {
  const root = scratchWorkspace(t);
  const afterA = commitChange(root, "a/src.txt", "a changed\n");
  git(root, "branch", "release/base", afterA);
  commitChange(root, "b/src.txt", "b changed\n");

  const run = just(root, ["check"], { NX_BASE: "release/base" });

  assert.equal(run.status, 0, run.output);
  assert.match(run.stdout, new RegExp(`affected tier against ${afterA.slice(0, 12)} \\(NX_BASE=release/base\\)`));
  assert.match(run.stdout, /gate: projects: b\n/);
  assert.ok(ran(root, "b") && !ran(root, "a"), run.output);
});

test("a change not yet committed, staged or not, or a new file, is affected too", (t) => {
  const root = scratchWorkspace(t);
  write(root, { "a/src.txt": "a edited, unstaged\n" });
  const unstaged = just(root, ["check"], { NX_BASE: undefined });
  assert.equal(unstaged.status, 0, unstaged.output);
  assert.match(unstaged.stdout, /gate: projects: a\n/);
  assert.ok(ran(root, "a") && !ran(root, "b"), unstaged.output);

  git(root, "checkout", "--", "a/src.txt");
  rmSync(join(root, "ran-a"), { force: true });
  write(root, { "b/new.txt": "untracked\n" });
  const untracked = just(root, ["check"], { NX_BASE: undefined });
  assert.equal(untracked.status, 0, untracked.output);
  assert.match(untracked.stdout, /gate: projects: b\n/);
  assert.ok(ran(root, "b") && !ran(root, "a"), untracked.output);

  rmSync(join(root, "b", "new.txt"));
  rmSync(join(root, "ran-b"), { force: true });
  write(root, { "a/src.txt": "a edited, staged\n" });
  git(root, "add", "a/src.txt");
  const staged = just(root, ["check"], { NX_BASE: undefined });
  assert.equal(staged.status, 0, staged.output);
  assert.match(staged.stdout, /gate: projects: a\n/);
  assert.ok(ran(root, "a") && !ran(root, "b"), staged.output);
});

test("an inherited NX_HEAD never moves the affected tier's head off the checkout", (t) => {
  const root = scratchWorkspace(t);
  const afterA = commitChange(root, "a/src.txt", "a changed\n");
  commitChange(root, "b/src.txt", "b changed\n");

  // Read as Nx reads it, NX_HEAD=afterA against NX_BASE=afterA would leave
  // nothing affected, and b's change would never be tested.
  const run = just(root, ["check"], { NX_BASE: afterA, NX_HEAD: afterA });

  assert.equal(run.status, 0, run.output);
  assert.match(run.stdout, /gate: projects: b\n/);
  assert.ok(ran(root, "b") && !ran(root, "a"), run.output);
});

test("NX_BASE that is neither a ref name nor a SHA fails closed and runs no target", (t) => {
  const root = scratchWorkspace(t);
  commitChange(root, "a/src.txt", "a changed\n");

  for (const hostile of ["main;touch pwned", "$(touch pwned)", "HEAD~1", "a b"]) {
    const run = just(root, ["check"], { NX_BASE: hostile });
    assert.equal(run.status, 2, `${hostile}: ${run.output}`);
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
    assert.equal(run.status, 1, run.output);
    assert.match(run.stderr, new RegExp(`NX_BASE '${missing}' does not name a commit in this checkout; no target ran`));
  }
  assert.ok(!ran(root, "a") && !ran(root, "b"));
});

test("with no origin/main and no NX_BASE the affected tier refuses rather than guessing", (t) => {
  const root = scratchWorkspace(t);
  git(root, "update-ref", "-d", "refs/remotes/origin/main");

  const run = just(root, ["check"], { NX_BASE: undefined });

  assert.equal(run.status, 1, run.output);
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

test("--sweep runs a promoted project without --projects naming it", (t) => {
  const root = scratchWorkspace(t);
  commitChange(root, "b/project.json", JSON.stringify({
    name: "b", tags: ["type:tooling", "tier:promoted"],
    targets: { test: { command: "node -e \"require('fs').writeFileSync('ran-b', '')\"" } },
  }));

  const run = just(root, ["check", "--sweep"]);

  assert.equal(run.status, 0, run.output);
  assert.match(run.stdout, /gate: projects: a, b\n/);
  assert.doesNotMatch(run.stdout, /promoted, run by their own CI legs/);
  assert.ok(ran(root, "a") && ran(root, "b"), run.output);
});

test("an unknown argument or project is refused before anything runs", (t) => {
  const root = scratchWorkspace(t);
  for (const args of [["check", "--sweap"], ["check", "--projects=nope"], ["check", "--targets=te;st"]]) {
    const run = just(root, args);
    assert.equal(run.status, 2, `${args}: ${run.output}`);
  }
  assert.ok(!ran(root, "a") && !ran(root, "b"));
  // A switch given a value is refused, not read as set: `--plan=false` would
  // otherwise run nothing, and `--sweep=false` would sweep.
  for (const flag of ["--plan", "--sweep"]) {
    const run = just(root, ["check", `${flag}=false`]);
    assert.equal(run.status, 2, run.output);
    assert.match(run.output, new RegExp(`${flag} takes no value, not 'false'`));
  }
  assert.ok(!ran(root, "a") && !ran(root, "b"));
});

test("--plan prints the selection and the command, and runs nothing", (t) => {
  const root = scratchWorkspace(t);
  commitChange(root, "a/src.txt", "a changed\n");

  const run = just(root, ["check", "--plan"], { NX_BASE: undefined });

  assert.equal(run.status, 0, run.output);
  assert.match(run.stdout, /gate: projects: a\n/);
  assert.match(run.stdout, /gate: would run: nx run-many --targets=format,lint,typecheck,test,build,coverage,supply-chain,doc --projects=a /);
  assert.ok(!ran(root, "a") && !ran(root, "b"));
});

// A stand-in `nx` in place of the scratch workspace's linked install: `graph
// --file=` writes `graph`, and `show projects --affected` prints `affected`.
function standInNx(root, graph, affected) {
  // Unlink, never recurse: the link leads to this checkout's own install.
  unlinkSync(join(root, "node_modules"));
  mkdirSync(join(root, "node_modules", ".bin"), { recursive: true });
  const script = join(root, "node_modules", ".bin", "nx");
  writeFileSync(script, `#!/usr/bin/env node
const fs = require("fs");
const file = process.argv.find((arg) => arg.startsWith("--file="));
if (file) fs.writeFileSync(file.slice("--file=".length), ${JSON.stringify(JSON.stringify({ graph }))});
else process.stdout.write(${JSON.stringify(JSON.stringify(affected))});
`, { mode: 0o755 });
}

test("an Nx answer of the wrong shape stops the gate before any target runs", { skip: process.platform === "win32" }, (t) => {
  const good = { nodes: { a: { data: { root: "a", tags: ["type:tooling"] } } }, dependencies: {} };
  for (const [graph, affected, message] of [
    [{ nodes: { a: { data: { tags: [1] } } } }, ["a"], /nodes are not projects with string tags/],
    [{ nodes: "a" }, ["a"], /nodes are not projects with string tags/],
    [{ nodes: { a: { data: { root: "a" } } } }, ["a"], /nodes are not projects with string tags/],
    [{ nodes: { a: null } }, ["a"], /nodes are not projects with string tags/],
    [good, { a: true }, /answered \{"a":true\}, not a list of this graph's projects/],
    [good, ["a", "ghost"], /answered \["ghost"\], not a list of this graph's projects/],
    // A name that is not a string is refused, not coerced to the project it spells.
    [good, [["a"]], /answered \[\["a"\]\], not a list of this graph's projects/],
  ]) {
    const root = scratchWorkspace(t);
    commitChange(root, "a/src.txt", "a changed\n");
    standInNx(root, graph, affected);
    const run = just(root, ["check"], { NX_BASE: undefined });
    assert.equal(run.status, 1, run.output);
    assert.match(run.stderr, message);
    assert.match(run.stderr, /just bootstrap/);
    assert.doesNotMatch(run.stderr, /TypeError/);
    assert.ok(!ran(root, "a") && !ran(root, "b"));
  }
});

test("a project name that is no name --projects takes stops the gate before any target runs", { skip: process.platform === "win32" }, (t) => {
  // It would reach Nx's command line, which Windows runs through a shell.
  // A tag selector is list syntax, never a project's name.
  for (const name of ["a&calc", "tag:x", "a,b"]) {
    const root = scratchWorkspace(t);
    commitChange(root, "a/src.txt", "a changed\n");
    standInNx(root, { nodes: { [name]: { data: { root: "a", tags: [] } } }, dependencies: {} }, ["a"]);
    const run = just(root, ["check"], { NX_BASE: undefined });
    assert.equal(run.status, 1, run.output);
    assert.match(run.stderr, new RegExp(`names project\\(s\\) \\[${JSON.stringify(name)}\\], which are not project names`));
    assert.match(run.stderr, /rename the project in its project.json/);
    assert.ok(!ran(root, "a") && !ran(root, "b"));
  }
});

test("a missing Nx or a failing target exits 1, apart from an invocation error's 2", (t) => {
  const root = scratchWorkspace(t);
  commitChange(root, "a/project.json", project("a", { targets: { test: { command: "node -e \"process.exit(3)\"" } } }));
  const failed = just(root, ["check", "--projects=a"]);
  assert.equal(failed.status, 1, failed.output);
  assert.match(failed.stderr, /a target failed/);

  // Unlink, never recurse: the link leads to this checkout's own install.
  unlinkSync(join(root, "node_modules"));
  const missing = just(root, ["check", "--sweep"]);
  assert.equal(missing.status, 1, missing.output);
  assert.match(missing.stderr, /Nx is not installed/);
  assert.match(missing.stderr, /just bootstrap/);
  assert.ok(!ran(root, "a") && !ran(root, "b"));
});

test("a failing target's whole output reaches a slow reader before the gate exits", { skip: process.platform === "win32" }, (t) => {
  // CI reads the gate through a pipe that holds one buffer (64 KiB on Linux).
  // A reader slower than the gate must still get the whole replay of the run's
  // log, not the first buffer of it. The target exits only once its own output
  // has drained, so the log is past one buffer whatever the load — and only
  // just past it on macOS, where Nx kept 65,904 bytes of this run's log.
  const root = scratchWorkspace(t);
  const noisy = "node -e \"for (let i = 0; i < 4000; i++) console.log('line ' + i + ' ' + '.'.repeat(60)); setTimeout(() => process.exit(3), 500)\"";
  commitChange(root, "a/project.json", project("a", { targets: { test: { command: noisy } } }));
  const env = { ...process.env, NX_DAEMON: "false", NX_NO_CLOUD: "true" };
  delete env.NX_SKIP_NX_CACHE;
  const slow = spawnSync("sh", ["-c", "just check --projects=a 2>&1 >/dev/null | { sleep 2; cat; }"], { cwd: root, env, encoding: "utf8" });
  const log = /gate: a target failed \(full output above and in (\S+)\)/.exec(slow.stdout);
  assert.ok(log, slow.stdout.slice(-2000));
  const replay = readFileSync(log[1], "utf8");
  assert.ok(replay.length > 64 * 1024, `the run's log holds ${replay.length} bytes`);
  assert.ok(slow.stdout.startsWith(replay), `${slow.stdout.length} of the log's ${replay.length} bytes reached the reader`);
});

test("--projects=tag:<tag> selects that tag's carriers and --exclude drops one, in either tier", (t) => {
  const root = scratchWorkspace(t);
  write(root, {
    "a/project.json": project("a", { tags: ["type:tooling", "lang:rust"] }),
    "b/project.json": project("b", { tags: ["type:tooling", "lang:python"] }),
  });
  git(root, "-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "--quiet", "-am", "tag a and b");

  // Both projects changed since origin/main, so the affected tier reaches both
  // and the selection alone decides what runs, as it does under --sweep.
  for (const tier of [[], ["--sweep"]]) {
    for (const name of ["a", "b"]) rmSync(join(root, `ran-${name}`), { force: true });
    const tagged = just(root, ["check", ...tier, "--projects=tag:lang:python"], { NX_BASE: undefined });
    assert.equal(tagged.status, 0, tagged.output);
    assert.match(tagged.stdout, tier.length ? /gate: broader tier/ : /gate: affected tier against/);
    assert.match(tagged.stdout, /gate: projects: b\n/);
    assert.ok(ran(root, "b") && !ran(root, "a"), tagged.output);

    rmSync(join(root, "ran-b"), { force: true });
    const excluded = just(root, ["check", ...tier, "--exclude=b"], { NX_BASE: undefined });
    assert.equal(excluded.status, 0, excluded.output);
    assert.match(excluded.stdout, /gate: projects: a\n/);
    assert.ok(ran(root, "a") && !ran(root, "b"), excluded.output);

    const none = just(root, ["check", ...tier, "--projects=tag:lang:go"], { NX_BASE: undefined });
    assert.equal(none.status, 2, none.output);
    assert.match(none.stderr, /no project carries the tag 'lang:go'/);
  }
});

test("--sweep reruns a target the affected tier replays from cache, nested Nx included", (t) => {
  const root = scratchWorkspace(t);
  const marker = (name) => `node -e "require('fs').writeFileSync('ran-${name}', '')"`;
  write(root, {
    // `a`'s test is cached; `n`'s runs `a`'s through a nested Nx, as a target can.
    "a/project.json": JSON.stringify({ name: "a", tags: ["type:tooling"],
      targets: { test: { command: marker("a"), cache: true, inputs: ["default"] } } }),
    "n/project.json": JSON.stringify({ name: "n", tags: ["type:tooling"],
      targets: { test: { command: "node node_modules/nx/dist/bin/nx.js run a:test --outputStyle=static", cache: false } } }),
  });
  git(root, "-c", "user.name=t", "-c", "user.email=t@example.com", "add", "-A");
  git(root, "-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "--quiet", "-m", "cache a");

  const warm = just(root, ["check", "--projects=a"], { NX_BASE: undefined });
  assert.equal(warm.status, 0, warm.output);
  assert.ok(ran(root, "a"), warm.output);
  rmSync(join(root, "ran-a"));
  const replayed = just(root, ["check", "--projects=a"], { NX_BASE: undefined });
  assert.equal(replayed.status, 0, replayed.output);
  assert.ok(!ran(root, "a"), "the affected tier was meant to replay a from cache, not rerun it");

  const swept = just(root, ["check", "--sweep", "--projects=a"]);
  assert.equal(swept.status, 0, swept.output);
  assert.ok(ran(root, "a"), `the sweep replayed a from cache: ${swept.output}`);
  rmSync(join(root, "ran-a"));
  // Outside the sweep the nested Nx replays a from cache, so the rerun below
  // is the sweep's doing.
  const nestedReplay = just(root, ["check", "--projects=n"], { NX_BASE: undefined });
  assert.equal(nestedReplay.status, 0, nestedReplay.output);
  assert.ok(!ran(root, "a"), `the nested Nx was meant to replay a from cache: ${nestedReplay.output}`);
  const nested = just(root, ["check", "--sweep", "--projects=n"]);
  assert.equal(nested.status, 0, nested.output);
  assert.ok(ran(root, "a"), `the nested Nx under --sweep replayed a from cache: ${nested.output}`);
});

test("the gate loads Nx's plugins in its own process, not in workers that a busy runner can starve", (t) => {
  const root = scratchWorkspace(t);
  write(root, {
    "a/record.cjs": "require('fs').writeFileSync('isolate-plugins', String(process.env.NX_ISOLATE_PLUGINS))\n",
    "a/project.json": JSON.stringify({ name: "a", tags: ["type:tooling"], targets: { test: { command: "node a/record.cjs" } } }),
  });
  commitChange(root, "a/src.txt", "a changed\n");

  const run = just(root, ["check"], { NX_BASE: undefined, NX_ISOLATE_PLUGINS: undefined });

  assert.equal(run.status, 0, run.output);
  assert.equal(readFileSync(join(root, "isolate-plugins"), "utf8"), "false", run.output);
});

// A rustup that records each call, and whether a target had already run by then.
function standInRustup(root, { fail = false } = {}) {
  const bin = join(root, "stand-in-bin");
  mkdirSync(bin);
  writeFileSync(join(bin, "rustup"), `#!/bin/sh
ls ran-* >/dev/null 2>&1 && after=after-a-target || after=before-any-target
echo "rustup $* ($after)" >> rustup-calls
${fail ? "echo 'error: could not download file from static.rust-lang.org' >&2; exit 1" : "echo 'info: the active toolchain is installed' >&2"}
`, { mode: 0o755 });
  return { PATH: `${bin}:${process.env.PATH}`, NX_BASE: undefined };
}

const rustupCalls = (root) => (existsSync(join(root, "rustup-calls")) ? readFileSync(join(root, "rustup-calls"), "utf8") : "");

test("the gate installs the pinned Rust toolchain once, before any target can race to", { skip: process.platform === "win32" }, (t) => {
  const root = scratchWorkspace(t);
  write(root, { ".gitignore": "/node_modules\n/.nx\nran-*\nrustup-calls\nstand-in-bin\n" });
  commitChange(root, "rust-toolchain.toml", "[toolchain]\nchannel = \"1.96.0\"\n");
  const env = standInRustup(root);

  const run = just(root, ["check", "--sweep"], env);

  assert.equal(run.status, 0, run.output);
  assert.ok(ran(root, "a") && ran(root, "b"), run.output);
  assert.equal(rustupCalls(root), "rustup toolchain install --no-self-update (before-any-target)\n");
  const log = readFileSync(/output in (\S+)\)/.exec(run.stdout)[1], "utf8");
  assert.match(log, /^\$ rustup toolchain install --no-self-update\ninfo: the active toolchain is installed\n\$ nx run-many/);

  // --plan runs nothing, and a checkout pinning no toolchain needs none.
  rmSync(join(root, "rustup-calls"));
  assert.equal(just(root, ["check", "--sweep", "--plan"], env).status, 0);
  git(root, "rm", "--quiet", "rust-toolchain.toml");
  assert.equal(just(root, ["check", "--sweep"], env).status, 0);
  assert.equal(rustupCalls(root), "");
});

test("a toolchain that will not install stops the gate before any target runs", { skip: process.platform === "win32" }, (t) => {
  const root = scratchWorkspace(t);
  write(root, { ".gitignore": "/node_modules\n/.nx\nran-*\nrustup-calls\nstand-in-bin\n" });
  commitChange(root, "rust-toolchain.toml", "[toolchain]\nchannel = \"1.96.0\"\n");

  const run = just(root, ["check", "--sweep"], standInRustup(root, { fail: true }));

  assert.equal(run.status, 1, run.output);
  assert.match(run.stderr, /error: could not download file from static\.rust-lang\.org/);
  assert.match(run.stderr, /could not install the Rust toolchain rust-toolchain\.toml pins .*; no target ran/);
  assert.match(run.stderr, /rustup self update/);
  assert.ok(!ran(root, "a") && !ran(root, "b"), run.output);
});
