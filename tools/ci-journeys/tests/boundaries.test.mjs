// The module-boundary rule over a scratch graph: an edge onto an expensive
// suite from an unrelated project fails the project that draws it, in each form
// an edge can take, and the same graph without the edge passes.
import assert from "node:assert/strict";
import { execFileSync, spawnSync } from "node:child_process";
import { copyFileSync, mkdirSync, mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { test } from "node:test";
import { REPO, scratchWorkspace, write } from "./support.mjs";

const BOUNDARIES = {
  allow: { "type:tooling": ["type:tooling", "type:e2e"], "type:e2e": ["type:tooling"] },
  unreachable: {
    "cost:expensive": {
      rule: "expensive-suites-stay-unreachable",
      from: ["cost:expensive"],
      why: "an expensive suite may be depended on only by another",
    },
  },
};

function check(root, name, env = {}) {
  return spawnSync(process.execPath, [join(root, "scripts/check-project-boundaries.mjs"), name], {
    cwd: root, encoding: "utf8", env: { ...process.env, NX_DAEMON: "false", ...env },
  });
}

function graph(t, a) {
  const root = scratchWorkspace(t);
  write(root, {
    "nx.json": JSON.stringify({ namedInputs: { default: ["{projectRoot}/**/*"] }, boundaries: BOUNDARIES }),
    "a/project.json": JSON.stringify({ name: "a", tags: ["type:tooling"], targets: { test: { command: "true" } }, ...a }),
    "b/project.json": JSON.stringify({ name: "b", tags: ["type:e2e", "cost:expensive"], targets: { test: { command: "true" } } }),
  });
  return root;
}

test("without the edge both projects pass", (t) => {
  const root = graph(t, {});
  for (const name of ["a", "b"]) {
    const run = check(root, name);
    assert.equal(run.status, 0, run.stderr);
    assert.match(run.stdout, new RegExp(`${name} ok`));
  }
});

for (const [form, a] of [
  ["an implicit dependency", { implicitDependencies: ["b"] }],
  ["a cross-project dependsOn", { targets: { test: { command: "true", dependsOn: [{ projects: ["b"], target: "test" }] } } }],
  ["an input under the suite's root", { targets: { test: { command: "true", inputs: ["{workspaceRoot}/b/src.txt"] } } }],
]) {
  test(`an edge onto an expensive suite through ${form} fails, naming the rule`, (t) => {
    const root = graph(t, a);
    const run = check(root, "a");
    assert.equal(run.status, 1, run.stdout);
    assert.match(run.stderr, /expensive-suites-stay-unreachable: a may not depend on b \(tagged cost:expensive\)/);
    // The suite's own lint sees the edge drawn into it as well.
    assert.equal(check(root, "b").status, 1);
  });
}

test("Markdown is prose: reading every AGENTS.md draws no edge", (t) => {
  const root = graph(t, { targets: { test: { command: "true", inputs: ["{workspaceRoot}/**/*.md"] } } });
  assert.equal(check(root, "a").status, 0);
});

test("a project carrying no type tag is refused", (t) => {
  const root = graph(t, { tags: [] });
  const run = check(root, "a");
  assert.equal(run.status, 1);
  assert.match(run.stderr, /a carries 0 type: tags/);
});

test("an edge through a named input or a glob that descends into the suite fails", (t) => {
  for (const inputs of [["sharedReads"], ["{workspaceRoot}/b/**/*"]]) {
    const root = graph(t, { targets: { test: { command: "true", inputs } } });
    write(root, {
      "nx.json": JSON.stringify({
        namedInputs: { default: ["{projectRoot}/**/*"], sharedReads: ["{workspaceRoot}/b/src.txt"] },
        boundaries: BOUNDARIES,
      }),
    });
    const run = check(root, "a");
    assert.equal(run.status, 1, `${inputs}: ${run.stdout}`);
    assert.match(run.stderr, /expensive-suites-stay-unreachable: a may not depend on b/);
  }
});

test("a glob that stays in one directory reads no project below it", (t) => {
  const root = graph(t, { targets: { test: { command: "true", inputs: ["{workspaceRoot}/*.md", "{workspaceRoot}/*.txt"] } } });
  assert.equal(check(root, "a").status, 0);
});

test("a dependency the type table does not allow fails, naming type-allow", (t) => {
  const root = graph(t, {});
  write(root, { "c/project.json": JSON.stringify({ name: "c", tags: ["type:e2e"], implicitDependencies: ["a"], targets: {} }) });
  const allowed = check(root, "c");
  assert.equal(allowed.status, 0, allowed.stderr);
  write(root, { "a/project.json": JSON.stringify({ name: "a", tags: ["type:tooling"], implicitDependencies: ["c"], targets: {} }) });
  write(root, { "nx.json": JSON.stringify({ namedInputs: {}, boundaries: { ...BOUNDARIES, allow: { "type:tooling": ["type:tooling"], "type:e2e": ["type:tooling"] } } }) });
  const run = check(root, "a");
  assert.equal(run.status, 1);
  assert.match(run.stderr, /type-allow: a \(type:tooling\) may not depend on c \(type:e2e\)/);
});

test("the recorded exceptions admit an edge onto an expensive suite", (t) => {
  // Another expensive suite, by its `from` tag.
  let root = graph(t, { tags: ["type:tooling", "cost:expensive"], implicitDependencies: ["b"] });
  assert.equal(check(root, "a").status, 0, check(root, "a").stderr);
  // A project that measures the suite, by its `measures:` tag.
  root = graph(t, { tags: ["type:tooling", "measures:b"], implicitDependencies: ["b"] });
  assert.equal(check(root, "a").status, 0, check(root, "a").stderr);
  // ...but measuring one suite admits no other.
  root = graph(t, { tags: ["type:tooling", "measures:other"], implicitDependencies: ["b"] });
  assert.equal(check(root, "a").status, 1);
});

test("a cycle in the implicit graph fails both projects on it; an acyclic chain passes", (t) => {
  const root = graph(t, { implicitDependencies: ["c"] });
  write(root, { "c/project.json": JSON.stringify({ name: "c", tags: ["type:tooling"], targets: {} }) });
  assert.equal(check(root, "a").status, 0, check(root, "a").stderr);
  write(root, { "c/project.json": JSON.stringify({ name: "c", tags: ["type:tooling"], implicitDependencies: ["a"], targets: {} }) });
  for (const name of ["a", "c"]) {
    const run = check(root, name);
    assert.equal(run.status, 1, name);
    assert.match(run.stderr, /acyclic-graph: .* is a cycle/);
  }
});

test("a Cargo path dependency onto the suite's crate is an edge too", (t) => {
  const root = graph(t, {});
  write(root, {
    "Cargo.toml": '[workspace]\nmembers = ["a", "b"]\nresolver = "2"\n',
    "a/Cargo.toml": '[package]\nname = "a"\nversion = "0.0.0"\nedition = "2021"\npublish = false\n\n[dependencies]\nb = { path = "../b" }\n',
    "a/src/lib.rs": "",
    "b/Cargo.toml": '[package]\nname = "b"\nversion = "0.0.0"\nedition = "2021"\npublish = false\n',
    "b/src/lib.rs": "",
  });
  execFileSync("cargo", ["generate-lockfile", "--offline"], { cwd: root, stdio: "pipe" });
  const run = check(root, "a");
  assert.equal(run.status, 1, run.stdout);
  assert.match(run.stderr, /expensive-suites-stay-unreachable: a may not depend on b .*Cargo path dependency a -> b/);
});

test("a project with two type tags, or an undeclared one, is refused", (t) => {
  for (const tags of [["type:tooling", "type:e2e"], ["type:unknown"]]) {
    const root = graph(t, { tags });
    const run = check(root, "a");
    assert.equal(run.status, 1, JSON.stringify(tags));
    assert.match(run.stderr, /a carries 2 type: tags|a is tagged type:unknown, which nx.json "boundaries.allow" does not declare/);
  }
});

test("a malformed boundaries table is refused rather than enforcing less", (t) => {
  for (const unreachable of [[], { "cost:expensive": { rule: "r", why: "w", from: [1] } }, { "cost:expensive": { from: [], why: "w" } }]) {
    const root = graph(t, {});
    write(root, { "nx.json": JSON.stringify({ namedInputs: {}, boundaries: { ...BOUNDARIES, unreachable } }) });
    const run = check(root, "a");
    assert.equal(run.status, 1, JSON.stringify(unreachable));
    assert.match(run.stderr, /no well-formed "boundaries" table/);
  }
});

/** A root whose `nx graph` is a stand-in writing `graph`, holding the real check. */
function standInGraph(t, graph, nxJson = { boundaries: BOUNDARIES }) {
  const root = mkdtempSync(join(tmpdir(), "crozier-graph-shape-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  mkdirSync(join(root, "scripts"));
  mkdirSync(join(root, "node_modules", "nx"), { recursive: true });
  writeFileSync(join(root, "package.json"), "{}");
  writeFileSync(join(root, "nx.json"), JSON.stringify(nxJson));
  writeFileSync(join(root, "node_modules", "nx", "package.json"), JSON.stringify({ name: "nx", bin: { nx: "./nx.js" } }));
  writeFileSync(join(root, "node_modules", "nx", "nx.js"),
    `const fs = require("fs");
     const file = process.argv.find((arg) => arg.startsWith("--file=")).slice("--file=".length);
     fs.writeFileSync(file, ${JSON.stringify(JSON.stringify({ graph }))});`);
  copyFileSync(join(REPO, "scripts", "check-project-boundaries.mjs"), join(root, "scripts", "check-project-boundaries.mjs"));
  return root;
}

test("a project graph of the wrong shape is refused with the fix, not a TypeError", (t) => {
  const node = (data) => ({ nodes: { a: { data: { root: "a", tags: ["type:tooling"], ...data } } }, dependencies: {} });
  for (const graph of [
    { nodes: { a: { data: { root: "a", tags: [1] } } }, dependencies: {} },
    { nodes: { a: { data: { root: "a", tags: ["type:tooling"] } } }, dependencies: { a: "b" } },
    { nodes: { a: { data: { root: "a", tags: ["type:tooling"] } } }, dependencies: { a: [{ source: "a" }] } },
    node({ targets: { test: "true" } }),
    node({ targets: { test: { dependsOn: "^build" } } }),
    node({ targets: { test: { dependsOn: [{ projects: ["b"] }] } } }),
    node({ targets: { test: { dependsOn: [{ target: "build", projects: [7] }] } } }),
    node({ targets: { test: { inputs: "default" } } }),
    node({ targets: { test: { inputs: [null] } } }),
    node({ namedInputs: { default: "{projectRoot}/**/*" } }),
  ]) {
    const run = check(standInGraph(t, graph), "a");
    assert.equal(run.status, 1, JSON.stringify(graph));
    assert.match(run.stderr, /not the shape this check reads/);
    assert.doesNotMatch(run.stderr, /TypeError/);
  }
  const named = check(standInGraph(t, node({}), { namedInputs: { default: "x" }, boundaries: BOUNDARIES }), "a");
  assert.equal(named.status, 1, named.stderr);
  assert.match(named.stderr, /"namedInputs" is not a map of input names to lists/);
});

test("Cargo metadata of the wrong shape is refused with the fix, not a TypeError", { skip: process.platform === "win32" }, (t) => {
  const root = standInGraph(t, { nodes: { a: { data: { root: "a", tags: ["type:tooling"] } } }, dependencies: {} });
  writeFileSync(join(root, "Cargo.toml"), "[workspace]\n");
  const bin = join(root, "bin");
  mkdirSync(bin);
  for (const metadata of [
    { packages: [{ name: "a" }] },
    { packages: [{ name: "a", manifest_path: "/r/a/Cargo.toml", dependencies: "b" }] },
    { packages: [{ name: "a", manifest_path: "/r/a/Cargo.toml", dependencies: [{ name: "b", path: 7 }] }] },
  ]) {
    writeFileSync(join(bin, "cargo"), `#!/bin/sh\nprintf '%s' '${JSON.stringify(metadata)}'\n`, { mode: 0o755 });
    const run = check(root, "a", { PATH: `${bin}:${process.env.PATH}` });
    assert.equal(run.status, 1, JSON.stringify(metadata));
    assert.match(run.stderr, /reading the Cargo workspace failed: its `packages` are not a list/);
    assert.match(run.stderr, /ACTION: check `cargo metadata/);
    assert.doesNotMatch(run.stderr, /TypeError/);
  }
});

test("a temporary directory the check cannot write to names itself and the fix", (t) => {
  const root = standInGraph(t, { nodes: { a: { data: { root: "a", tags: ["type:tooling"] } } }, dependencies: {} });
  const missing = join(root, "no-such-tmp");
  const run = check(root, "a", { TMPDIR: missing, TMP: missing, TEMP: missing });
  assert.equal(run.status, 1, run.stderr);
  assert.match(run.stderr, /creating a scratch directory for the project graph failed/);
  assert.match(run.stderr, /check that the temporary directory \(.*no-such-tmp\) is writable and has free space/);
  assert.doesNotMatch(run.stderr, /at mkdtempSync/);
});
