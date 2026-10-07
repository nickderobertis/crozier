// The module-boundary rule over a scratch graph: an edge onto an expensive
// suite from an unrelated project fails the project that draws it, in each form
// an edge can take, and the same graph without the edge passes.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { join } from "node:path";
import { test } from "node:test";
import { scratchWorkspace, write } from "./support.mjs";

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

function check(root, name) {
  return spawnSync(process.execPath, [join(root, "scripts/check-project-boundaries.mjs"), name], {
    cwd: root, encoding: "utf8", env: { ...process.env, NX_DAEMON: "false" },
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
