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
import { commitChange, git, just, project, ran, REPO, scratchWorkspace, write } from "./support.mjs";

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
  const noisy = "node -e \"process.stdout.write(Array.from({ length: 4000 }, (_, i) => 'line ' + i + ' ' + '.'.repeat(60) + '\\\\n').join(''), () => process.exit(3))\"";
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

for (const exit of [0, 1]) {
  test(`task timings survive exit ${exit} without repeating the task`, (t) => {
    const root = scratchWorkspace(t);
    write(root, {
      "a/project.json": project("a", { targets: { test: { command: `node once.cjs ${exit}` } } }),
      "once.cjs": "const fs = require('fs'); fs.appendFileSync('ran-a', 'once\\n'); process.exit(Number(process.argv[2]));",
    });
    const run = just(root, ["test", "--sweep", "--projects=a"]);
    assert.equal(run.status, exit, run.output);
    assert.equal(readFileSync(join(root, "ran-a"), "utf8"), "once\n");
    assert.match(run.output, /gate: task a:test: [0-9.]+s \((success|failure)\)/);
    const log = run.output.match(/(?:output in |and in )([^\s)]+\.log)/)?.[1];
    assert.ok(log, run.output);
    assert.match(readFileSync(log, "utf8"), /gate: task a:test:/);
  });
}

// The real timing CLI with only its external read processes doubled. Seeds are
// recorded GitHub responses; variants induce cancellation, missing contexts and
// later attempts without changing any calculation in the implementation.
import { calculateHead, CLI_OPTIONS, SCHEMA_VERSION, summarize, taskTimings, validateReport } from '../../ci/gate-timing.mjs';
import { chmodSync, mkdtempSync, symlinkSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { fileURLToPath } from 'node:url';
const timingCLI = fileURLToPath(new URL('../../ci/gate-timing.mjs', import.meta.url));
const timingRecords = JSON.parse(readFileSync(new URL('./fixtures/gate-timing.json', import.meta.url), 'utf8'));

function timingReplay(t) {
  const root = mkdtempSync(join(tmpdir(), 'crozier-timing-replay-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const records = structuredClone(timingRecords);
  const answerFile = join(root, 'answers.json');
  const calls = join(root, 'calls.jsonl');
  writeFileSync(answerFile, JSON.stringify({ records }));
  const stub = `#!/usr/bin/env node
const fs = require('fs');
const a = JSON.parse(fs.readFileSync(process.env.ANSWERS, 'utf8'));
const args = process.argv.slice(2);
fs.appendFileSync(process.env.CALLS, JSON.stringify(args) + '\\n');
fs.appendFileSync(process.env.CALLS+'.timeline', JSON.stringify({args,at:Date.now()}) + '\\n');
let answer;
if(args[0] === 'auth' && args[1] === 'token') { process.stdout.write('replay-token'); process.exit(0); }
if(a.auth && args[0] === 'host' && process.env.GH_TOKEN !== 'replay-token') { console.error('missing bootstrapped token'); process.exit(1); }
if(a.noOnevcs && args[0] === 'host') { console.error('unrecognized subcommand run-jobs'); process.exit(2); }
const path = args.at(-1);
if(args.includes('rate_limit')) {
 const waited = fs.existsSync(process.env.CALLS+'.waited');
 if((a.quota || a.quotaFuture) && !waited) { fs.writeFileSync(process.env.CALLS+'.waited',''); answer={resources:{core:{limit:100,remaining:39,reset:a.quotaFuture ? Math.floor(Date.now()/1000)+1 : 0}}}; }
 else answer={resources:{core:{limit:100,remaining:100,reset:0}}};
} else if(path.endsWith('/protection')) answer=a.protection || {required_status_checks:{contexts:a.contexts || ['gate','llmlint']}};
else if(path.endsWith('/rules/branches/main')) answer=a.rules || [];
else if(path.includes('/actions/runs?')) { const page=Number(new URL('https://api.invalid/'+path).searchParams.get('page')); answer={workflow_runs:a.records.map(r=>r.run).slice(a.paginate ? (page-1)*100 : 0, a.paginate ? page*100 : undefined)}; }
else if(args.includes('run-jobs')) answer={jobs:a.records.find(r=>r.run.id===Number(args[args.indexOf('--run')+1])).jobs};
else if(/\\/attempts\\//.test(path)) { const jobs=a.previous || a.records.find(r=>r.run.id===Number(path.split('/')[5])).jobs; const page=Number(new URL('https://api.invalid/'+path).searchParams.get('page')); answer={jobs:a.paginateJobs ? jobs.slice((page-1)*100,page*100) : jobs}; }
else if(/\\/actions\\/runs\\/\\d+$/.test(path)) answer=a.records.find(r=>r.run.id===Number(path.split('/').at(-1)))?.run;
if(a.missing && path.includes('/actions/runs?')) answer={};
if(a.badQuota && args.includes('rate_limit')) answer={resources:{core:{limit:'100',remaining:39,reset:null}}};
if(a.badProtection && path.endsWith('/protection')) answer={required_status_checks:{contexts:[null]}};
if(a.badRules && path.endsWith('/rules/branches/main')) answer=[{type:'required_status_checks',parameters:{required_status_checks:'bad'}}];
if(a.badRun && path.includes('/actions/runs?')) answer={workflow_runs:[{...a.records[0].run,id:'bad'}]};
if(a.badFresh && /\\/actions\\/runs\\/\\d+$/.test(path)) answer={...answer,head_sha:'0'.repeat(40)};
if(a.fail) { console.error('read refused'); process.exit(1); }
if(!answer) { console.error('unexpected external request: '+args.join(' ')); process.exit(1); }
process.stdout.write(JSON.stringify(answer));
`;
  for (const name of ['gh', 'onevcs']) { writeFileSync(join(root, name), stub); chmodSync(join(root, name), 0o755); }
  const run = (extra = [], overrides = {}) => spawnSync(process.execPath, [timingCLI, 'runs', '--since', '2026-10-31T00:00:00Z', '--until', '2026-11-04T00:00:00Z', '--cache-dir', join(root, 'cache'), ...extra], { encoding: 'utf8', env: { ...process.env, GH_TOKEN: 'replay', PATH: `${root}:${process.env.PATH}`, ANSWERS: answerFile, CALLS: calls, ...overrides } });
  return { root, records, answerFile, calls, run };
}

test('timing CLI reconciles recorded heads, all jobs, real queue, filters and help', { skip: process.platform === 'win32' }, (t) => {
  const replay = timingReplay(t);
  const run = replay.run();
  assert.equal(run.status, 0, run.stderr);
  const report = validateReport(JSON.parse(run.stdout));
  assert.equal(report.runs.length, replay.records.length);
  assert.equal(report.observation.jobs, replay.records.reduce((n, r) => n + r.jobs.length, 0));
  for (const record of replay.records) {
    const actual = report.runs.find((r) => r.run_id === record.run.id);
    assert.deepEqual(actual, calculateHead([record], ['gate', 'llmlint']));
  }
  // Recorded release PR: last required gate completed 20:00:13, creation
  // 17:53:39. Job queue uses its own creation, not workflow creation.
  assert.equal(report.runs[0].gate_seconds, 7594);
  const seed = replay.records[0];
  const job = seed.jobs.find((j) => j.name === 'llmlint');
  const measured = report.runs[0].jobs.find((j) => j.name === 'llmlint');
  assert.equal(measured.queue_seconds, 2);
  assert.equal(measured.start_offset_seconds, 136);
  assert.equal(measured.run_seconds, 526);
  assert.notEqual(job.created_at, seed.run.created_at);
  assert.deepEqual(report.summary, summarize(report.runs));
  const filtered = replay.run(['--head-contains', replay.records.at(-1).run.head_sha.slice(0, 7)]);
  assert.equal(filtered.status, 0, filtered.stderr);
  assert.equal(JSON.parse(filtered.stdout).runs.length, 1);
  const help = spawnSync(process.execPath, [timingCLI, '--help'], { encoding: 'utf8' });
  assert.equal(help.status, 0);
  for (const token of [...Object.keys(CLI_OPTIONS).map((key) => '--'+key), `schema_version: ${SCHEMA_VERSION}`]) assert.ok(help.stdout.includes(token));
  const md = replay.run(['--format', 'markdown']);
  assert.equal(md.status, 0, md.stderr);
  assert.match(md.stdout, /release-pr/);
});

test('timing CLI refreshes later attempts while reusing completed responses', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  assert.equal(r.run().status, 0);
  const before = readFileSync(r.calls, 'utf8').trim().split('\n');
  const seed = r.records[0];
  const previous = structuredClone(seed.jobs);
  seed.run.run_attempt = 2;
  seed.jobs = seed.jobs.map((j) => ({ ...j, run_attempt: 2, completed_at: '2026-11-03T23:00:00Z' }));
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, previous }));
  const second = r.run();
  assert.equal(second.status, 0, second.stderr);
  const after = readFileSync(r.calls, 'utf8').trim().split('\n').slice(before.length).map(JSON.parse);
  assert.equal(after.filter((a) => a.includes('run-jobs')).length, 1);
  assert.ok(after.some((a) => a.at(-1) === `repos/nickderobertis/crozier/actions/runs/${seed.run.id}`));
  const measured = JSON.parse(second.stdout).runs.find((x) => x.run_id === seed.run.id);
  assert.equal(measured.attempt, 2);
  assert.equal(measured.jobs.length, previous.length * 2);
  assert.equal(measured.gate_seconds, 18381);
});

test('timing CLI excludes cancelled and missing contexts from passing summary and waits for quota', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  r.records[0].jobs.find((j) => j.name === 'gate').conclusion = 'cancelled';
  r.records[1].jobs = r.records[1].jobs.filter((j) => j.name !== 'gate');
  // Main measures every job's completion independently of PR contexts.
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, quota: true }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const report = JSON.parse(run.stdout);
  assert.equal(report.runs[0].gate_seconds, null);
  assert.match(report.runs[0].reason, /cancelled/);
  assert.equal(report.summary.kinds['release-pr'].unsuccessful, 1);
  assert.deepEqual(report.observation.events.map((e) => e.event), ['quota_wait', 'quota_resume']);
  // Induce a missing PR context independently of the main seed.
  r.records.at(-1).jobs = r.records.at(-1).jobs.filter((j) => j.name !== 'gate');
  rmSync(join(r.root, 'cache'), { recursive: true });
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  const missing = JSON.parse(r.run().stdout).runs.at(-1);
  assert.equal(missing.gate_seconds, null);
  assert.match(missing.reason, /missing/);
});

test('timing CLI rejects invalid invocation and failed or missing reads', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  assert.equal(r.run(['--limit', '0']).status, 2);
  assert.equal(r.run(['--until', 'yesterday']).status, 2);
  for (const variant of ['fail', 'missing']) {
    writeFileSync(r.answerFile, JSON.stringify({ records: r.records, [variant]: true }));
    const run = r.run();
    assert.equal(run.status, 1, run.stderr);
    assert.equal(run.stdout, '');
  }
});


test('timing CLI counts sibling workflows and excludes failed gates', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const pr = r.records.at(-1);
  pr.jobs.find((j) => j.name === 'llmlint').conclusion = 'failure';
  r.records.push({ run: { ...pr.run, id: 999 }, jobs: [{ ...pr.jobs[0], name: 'visual sibling', run_id: 999 }] });
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const report = JSON.parse(run.stdout);
  const measured = report.runs.find((head) => head.head_sha === pr.run.head_sha);
  assert.equal(measured.jobs.length, pr.jobs.length + 1);
  assert.equal(measured.conclusion, 'failure');
  assert.equal(typeof measured.gate_seconds, 'number');
  assert.equal(report.summary.kinds.pr.n, 0);
  assert.equal(report.summary.kinds.pr.unsuccessful, 1);
});


test('timing CLI refreshes jobs while an attempt is unfinished', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const seed = r.records[0];
  seed.run.status = 'in_progress';
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  assert.equal(r.run().status, 0);
  const count = readFileSync(r.calls, 'utf8').trim().split('\n').length;
  seed.run.status = 'completed';
  seed.jobs.push({ ...seed.jobs[0], name: 'late matrix job' });
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  assert.ok(JSON.parse(run.stdout).runs[0].jobs.some((j) => j.name === 'late matrix job'));
  const calls = readFileSync(r.calls, 'utf8').trim().split('\n').slice(count).map(JSON.parse);
  assert.equal(calls.filter((a) => a.includes('run-jobs')).length, 1);
});


test('timing CLI retains workflows cancelled before any job was created', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  r.records.push({ run: { ...r.records.at(-1).run, id: 41395650386, head_sha: 'b'.repeat(40), conclusion: 'cancelled' }, jobs: [] });
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const head = JSON.parse(run.stdout).runs.at(-1);
  assert.equal(head.gate_seconds, null);
  assert.equal(head.conclusion, 'cancelled');
  assert.match(head.reason, /cancelled workflow/);
  assert.deepEqual(head.jobs, []);
});


test('timing CLI reports main CI completion separately from other workflows', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const main = r.records.find((record) => record.run.event === 'push');
  const expected = calculateHead([main], ['gate', 'llmlint']).gate_seconds;
  r.records.push({ run: { ...main.run, id: 998, name: 'Visual docs', path: '.github/workflows/visual-docs.yml' }, jobs: [{ ...main.jobs[0], name: 'gallery', completed_at: '2026-11-04T00:00:00Z' }] });
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const measured = JSON.parse(run.stdout).runs.find((head) => head.head_sha === main.run.head_sha);
  assert.equal(measured.gate_seconds, expected);
  assert.equal(measured.jobs.length, main.jobs.length + 1);
});


for (const damage of ['missing', 'malformed', 'invalid']) for (const exit of [0, 1]) {
  test(`gate retains exit ${exit} and diagnoses ${damage} telemetry`, { skip: process.platform === 'win32' }, (t) => {
    const root = scratchWorkspace(t);
    // Forward every call to the installed Nx, then damage only its telemetry.
    // Both the gate and target still execute their real subprocess boundaries.
    unlinkSync(join(root, 'node_modules'));
    mkdirSync(join(root, 'node_modules', '.bin'), { recursive: true });
    symlinkSync(join(REPO, 'node_modules', 'nx'), join(root, 'node_modules', 'nx'), 'junction');
    const wrapper = `#!/usr/bin/env node
const { spawnSync } = require('node:child_process');
const fs = require('node:fs');
const run = spawnSync(process.execPath, [${JSON.stringify(join(REPO, 'node_modules', 'nx', 'dist', 'bin', 'nx.js'))}, ...process.argv.slice(2)], { stdio: 'inherit', env: process.env });
if (process.argv[2] === 'run-many') {
  const profile = process.env.NX_PROFILE;
  ${damage === 'missing' ? "fs.unlinkSync(profile);" : `fs.writeFileSync(profile, ${JSON.stringify(damage === 'malformed' ? '{' : '{}')});`}
}
process.exit(run.status ?? 1);
`;
    writeFileSync(join(root, 'node_modules', '.bin', 'nx'), wrapper);
    chmodSync(join(root, 'node_modules', '.bin', 'nx'), 0o755);
    write(root, {
      'a/project.json': project('a', { targets: { test: { command: `node once.cjs ${exit}` } } }),
      'once.cjs': "require('fs').appendFileSync('ran-a', 'once'); process.exit(Number(process.argv[2]));",
    });
    const run = just(root, ['test', '--sweep', '--projects=a']);
    assert.equal(run.status, exit, run.output);
    assert.equal(readFileSync(join(root, 'ran-a'), 'utf8'), 'once');
    assert.match(run.stderr, /gate: task timings unavailable:/);
    assert.doesNotMatch(run.stdout, /task timings unavailable/);
    const log = run.output.match(/(?:output in |and in )([^\s)]+\.log)/)?.[1];
    assert.ok(log, run.output);
    assert.match(readFileSync(log, 'utf8'), /task timings unavailable:/);
  });
}


test('timing CLI uses gh when the onevcs host verb is unavailable', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, noOnevcs: true }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  assert.equal(JSON.parse(run.stdout).runs.length, r.records.length);
  const calls = readFileSync(r.calls, 'utf8').trim().split('\n').map(JSON.parse);
  assert.ok(calls.some((args) => args.at(-1).includes('/attempts/1/jobs')));
});


test('timing CLI replays recorded crozier attempts even when timestamp order differs', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const records = JSON.parse(readFileSync(new URL('./fixtures/gate-timing-rerun.json', import.meta.url), 'utf8'));
  const context = 'visual-docs / report (x86_64)';
  r.records.push(records[0]);
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, contexts: [context] }));
  const first = r.run();
  assert.equal(first.status, 0, first.stderr);
  assert.equal(JSON.parse(first.stdout).runs.find((h) => h.run_id === 41288057298).gate_seconds, 2669);
  r.records[r.records.length-1] = records[1];
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, previous: records[0].jobs, contexts: [context] }));
  const second = r.run();
  assert.equal(second.status, 0, second.stderr);
  const head = JSON.parse(second.stdout).runs.find((h) => h.run_id === 41288057298);
  assert.equal(head.attempt, 2);
  assert.equal(head.conclusion, 'success');
  // 09:04:05 earliest observed creation to 09:59:36 last context completion,
  // including the failed attempt, even though attempt 2 completed earlier.
  assert.equal(head.gate_seconds, 3331);
  assert.equal(head.jobs.length, 10);
});


test('timing CLI independently verifies statistics and empty populations', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const seed = r.records.at(-1);
  const spans = [10, 20, 30, 40];
  r.records = spans.map((span, i) => ({ run: { ...seed.run, id: 800+i, head_sha: (i+1).toString(16).repeat(40), created_at: '2026-11-01T00:00:00Z' }, jobs: [{ ...seed.jobs[0], name: 'gate', created_at: '2026-11-01T00:00:00Z', started_at: '2026-11-01T00:00:02Z', completed_at: `2026-11-01T00:00:${span}Z` }] }));
  writeFileSync(r.answerFile, JSON.stringify({ records: r.records, contexts: ['gate'] }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const report = JSON.parse(run.stdout);
  assert.deepEqual(report.summary.kinds.pr, { n:4, median:25, p95:40, max:40, observed:4, unsuccessful:0 });
  assert.deepEqual(report.summary.kinds.main, { n:0, median:null, p95:null, max:null, observed:0, unsuccessful:0 });
  assert.deepEqual(report.summary.jobs.gate.run, { n:4, median:23, p95:38, max:38 });
  assert.deepEqual(report.summary.jobs.gate.queue, { n:4, median:2, p95:2, max:2 });
});

test('timing CLI retains unfinished and never-started required jobs', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const gate = r.records.at(-1).jobs.find((j) => j.name === 'gate');
  Object.assign(gate, { status:'queued', conclusion:null, started_at:null, completed_at:null });
  writeFileSync(r.answerFile, JSON.stringify({ records:r.records }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const head = JSON.parse(run.stdout).runs.at(-1);
  assert.equal(head.gate_seconds, null);
  assert.match(head.reason, /incomplete/);
  const job = head.jobs.find((j) => j.name === 'gate');
  assert.equal(job.queue_seconds, null);
  assert.equal(job.run_seconds, null);
  assert.equal(job.start_offset_seconds, 0);
  assert.match(job.start_offset_reason, /never started/);
});

test('timing CLI discovers credentials and unions protection with rulesets', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  writeFileSync(r.answerFile, JSON.stringify({ records:r.records, auth:true, protection:{ required_status_checks:{ checks:[{context:'gate'}], contexts:['llmlint'] } }, rules:[{type:'required_status_checks',parameters:{required_status_checks:[{context:'gate'},{context:'llmlint'}]}}] }));
  const run = r.run([], { GH_TOKEN:undefined, GITHUB_TOKEN:undefined });
  assert.equal(run.status, 0, run.stderr);
  assert.deepEqual(JSON.parse(run.stdout).required_contexts, ['gate','llmlint']);
  const calls = readFileSync(r.calls, 'utf8').trim().split('\n').map(JSON.parse);
  assert.ok(calls.some((args) => args[0] === 'auth' && args[1] === 'token'));
});

test('timing CLI pauses external reads until the observed quota reset', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  writeFileSync(r.answerFile, JSON.stringify({ records:r.records, quotaFuture:true }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const report = JSON.parse(run.stdout);
  const until = Date.parse(report.observation.events[0].until);
  const timeline = readFileSync(r.calls+'.timeline', 'utf8').trim().split('\n').map(JSON.parse);
  const firstRead = timeline.find((event) => !event.args.includes('rate_limit'));
  assert.ok(firstRead.at >= until, 'no protected read precedes the reset supplied by the quota response');
  assert.deepEqual(report.observation.events.map((e) => e.event), ['quota_wait','quota_resume']);
});

test('timing CLI paginates workflow history, excludes events, and reports capped sampling', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const excluded = Array.from({length:98}, (_,i) => ({ run:{...r.records[0].run,id:99000+i,event:'workflow_dispatch'},jobs:r.records[0].jobs }));
  writeFileSync(r.answerFile, JSON.stringify({ records:[...excluded,...r.records], paginate:true }));
  const run = r.run(['--limit','200']);
  assert.equal(run.status, 0, run.stderr);
  const report = JSON.parse(run.stdout);
  assert.equal(report.runs.length, r.records.length);
  assert.equal(report.observation.workflow_runs, r.records.length);
  assert.equal(report.observation.complete, true);
  assert.ok(readFileSync(r.calls,'utf8').includes('page=2'));
  const capped = r.run(['--limit','2']);
  assert.equal(capped.status, 0, capped.stderr);
  assert.equal(JSON.parse(capped.stdout).observation.complete, false);
  assert.equal(JSON.parse(capped.stdout).observation.workflow_runs, 2);
});

test('timing CLI fetches uncached historical attempts and every job page', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const seed = r.records[0];
  const previous = structuredClone(seed.jobs);
  while (previous.length < 101) previous.push({...previous[0],name:'historical-'+previous.length});
  seed.run.run_attempt = 2;
  seed.jobs = seed.jobs.map((j) => ({...j,run_attempt:2}));
  writeFileSync(r.answerFile, JSON.stringify({ records:r.records, previous, paginateJobs:true }));
  const run = r.run();
  assert.equal(run.status, 0, run.stderr);
  const head = JSON.parse(run.stdout).runs.find((h) => h.run_id === seed.run.id);
  assert.equal(head.jobs.length, 101 + seed.jobs.length);
  const calls = readFileSync(r.calls,'utf8').trim().split('\n').map(JSON.parse);
  assert.equal(calls.filter((a) => a.at(-1).includes('/attempts/1/jobs')).length, 2);
  assert.ok(calls.some((a) => a.at(-1).includes('/attempts/1/jobs?per_page=100&page=2')));
});

test('timing CLI rejects malformed boundary data and mismatched cached identities', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  assert.equal(r.run(['--until','2026-02-30T00:00:00Z']).status, 2);
  for (const field of ['badQuota','badProtection','badRules','badRun','badFresh']) {
    writeFileSync(r.answerFile, JSON.stringify({records:r.records,[field]:true}));
    const run = r.run();
    assert.equal(run.status, 1, field+': '+run.stderr);
    assert.equal(run.stdout, '');
  }
  writeFileSync(r.answerFile, JSON.stringify({records:r.records}));
  assert.equal(r.run().status, 0);
  const file = join(r.root,'cache',`run-${r.records[0].run.id}-attempt-1.json`);
  const cached = JSON.parse(readFileSync(file,'utf8'));
  cached.run.id += 1;
  writeFileSync(file,JSON.stringify(cached));
  const run = r.run();
  assert.equal(run.status,1);
  assert.match(run.stderr,/cached attempt identity mismatch/);
});

test('gate emits exact profile conversion and cache-replay status without executing again', (t) => {
  const root = scratchWorkspace(t);
  write(root, { 'a/project.json': project('a', { targets: { test: { cache:true, command:"node -e \"require('fs').appendFileSync('ran-a','once')\"" } } }) });
  commitChange(root,'a/src.txt','changed');
  const first = just(root,['test','--projects=a'],{NX_BASE:undefined});
  assert.equal(first.status,0,first.output);
  const firstLog = first.output.match(/output in ([^\s)]+\.log)/)[1];
  const profile = JSON.parse(readFileSync(firstLog.replace(/\.log$/,'.profile.json'),'utf8'));
  const event = profile.find((e) => e.ph === 'X' && e.name === 'a:test');
  assert.ok(first.stdout.includes(`gate: task a:test: ${(event.dur/1000000).toFixed(3)}s (${event.args.status})`));
  assert.deepEqual(taskTimings([{ph:'X',name:'a:test',dur:1500000,args:{status:'success'}}]),[{name:'a:test',seconds:1.5,status:'success'}]);
  // Select a on both calls while leaving its target inputs unchanged.
  const second = just(root,['test','--projects=a'],{NX_BASE:undefined});
  assert.equal(second.status,0,second.output);
  assert.match(second.stdout,/gate: task a:test: [0-9.]+s \((local-cache|local-cache-kept-existing|remote-cache)\)/);
  assert.equal(readFileSync(join(root,'ran-a'),'utf8'),'once');
});


test('timing CLI reports inconsistent job timestamps as unknown', { skip: process.platform === 'win32' }, (t) => {
  const r = timingReplay(t);
  const job = r.records[0].jobs[0];
  job.created_at = '2026-11-03T18:01:00Z';
  job.started_at = '2026-11-03T18:00:00Z';
  job.completed_at = '2026-11-03T17:59:00Z';
  writeFileSync(r.answerFile,JSON.stringify({records:r.records}));
  const run = r.run();
  assert.equal(run.status,0,run.stderr);
  const measured = JSON.parse(run.stdout).runs[0].jobs[0];
  assert.equal(measured.queue_seconds,null);
  assert.equal(measured.run_seconds,null);
});
