// A scratch repository the gate's own suites drive: a git repository holding
// the real justfile and the real gate drivers, a real Nx (linked from this
// checkout's install), and two tiny projects whose `test` target leaves a
// marker file when it runs, so a test can see exactly which targets ran.
import { execFileSync, spawnSync } from "node:child_process";
import { cpSync, existsSync, mkdirSync, mkdtempSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

export const REPO = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..", "..");

export function git(cwd, ...args) {
  return execFileSync("git", args, { cwd, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] }).trim();
}

/** Write `files` (path -> text) under `root`, creating directories. */
export function write(root, files) {
  for (const [path, text] of Object.entries(files)) {
    mkdirSync(dirname(join(root, path)), { recursive: true });
    writeFileSync(join(root, path), text);
  }
}

const marker = (name) =>
  `node -e "require('fs').writeFileSync('ran-${name}', '')"`;

/** A project whose `test` leaves `ran-<name>` at the workspace root. */
export function project(name, extra = {}) {
  return JSON.stringify({ name, tags: ["type:tooling"], targets: { test: { command: marker(name) } }, ...extra });
}

/**
 * A committed scratch workspace with projects `a` and `b`, `origin/main` at
 * the first commit; returns its root. `cleanup` removes it.
 */
export function scratchWorkspace(t) {
  const root = mkdtempSync(join(tmpdir(), "crozier-gate-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  for (const path of ["justfile", "tools/ci/gate.mjs", "tools/ci/ci-tier.mjs", "scripts/check-project-boundaries.mjs", "package.json"]) {
    mkdirSync(dirname(join(root, path)), { recursive: true });
    cpSync(join(REPO, path), join(root, path));
  }
  // A junction on Windows needs no privilege; elsewhere it is a symlink.
  symlinkSync(join(REPO, "node_modules"), join(root, "node_modules"), "junction");
  write(root, {
    ".gitignore": "/node_modules\n/.nx\nran-*\n",
    "nx.json": JSON.stringify({ defaultBase: "main", namedInputs: { default: ["{projectRoot}/**/*"] } }),
    "a/project.json": project("a"),
    "a/src.txt": "a\n",
    "b/project.json": project("b"),
    "b/src.txt": "b\n",
  });
  git(root, "init", "--quiet", "--initial-branch=main");
  git(root, "-c", "user.name=t", "-c", "user.email=t@example.com", "add", "-A");
  git(root, "-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "--quiet", "-m", "base");
  git(root, "update-ref", "refs/remotes/origin/main", "HEAD");
  return root;
}

/** Commit a change to `path` in `root`; returns the new commit's SHA. */
export function commitChange(root, path, text) {
  write(root, { [path]: text });
  git(root, "-c", "user.name=t", "-c", "user.email=t@example.com", "add", "-A");
  git(root, "-c", "user.name=t", "-c", "user.email=t@example.com", "commit", "--quiet", "-m", `change ${path}`);
  return git(root, "rev-parse", "HEAD");
}

/** Run `just <args>` in `root` with `env` over this environment. */
export function just(root, args, env = {}) {
  const merged = { ...process.env, NX_DAEMON: "false", NX_NO_CLOUD: "true", ...env };
  for (const [key, value] of Object.entries(env)) if (value === undefined) delete merged[key];
  const run = spawnSync("just", args, { cwd: root, env: merged, encoding: "utf8", shell: process.platform === "win32" });
  return { status: run.status, stdout: run.stdout ?? "", stderr: run.stderr ?? "", output: `${run.stdout}${run.stderr}` };
}

export const ran = (root, name) => existsSync(join(root, `ran-${name}`));
