#!/usr/bin/env node
// What a cached reuse test runs under, beyond its files: Nx hashes this output as a
// runtime input, because it hashes neither the host nor the environment by itself,
// and a listed env input cannot name a family such as `CARGO_PROFILE_*` or see the
// user-level cargo config. It must never fail: a failing runtime input stops Nx
// hashing the whole run.
//
//   node tools/ci/suite-cases/cache-key.mjs          for `suite-cases:test`
//   node tools/ci/suite-cases/cache-key.mjs python   for a suite that only runs Python
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { existsSync, readFileSync } from "node:fs";
import { arch, homedir, platform } from "node:os";
import { dirname, join } from "node:path";

const COMPILER_ENV = /^(RUSTC|RUSTC_WRAPPER|RUSTC_WORKSPACE_WRAPPER|RUSTFLAGS|RUSTDOCFLAGS|CARGO_ENCODED_RUSTFLAGS|CARGO_ENCODED_RUSTDOCFLAGS|CARGO_BUILD_.+|CARGO_PROFILE_.+|CARGO_TARGET_.+_(RUSTFLAGS|LINKER|RUNNER))$/;
// `UV_PYTHON` and its family are absent on purpose: the interpreter they select is hashed by what it is.
const PYTHON_ENV = /^PYTHON[A-Z]+$/;
// By what the interpreter is, not where: a clone's `.venv` and its base report the same.
const PYTHON_IDENTITY = `import platform, sys
print(sys.implementation.name, sys.version.replace("\\n", " "), sys.implementation.cache_tag, getattr(sys, "abiflags", ""), sys.platform, platform.machine())
`;

// `uv run --locked --all-packages` reads every workspace member's manifest, and an
// edit to one can make it reject the lock. These six are type:tier, so nx.json's
// boundary rule forbids a type:tooling target from declaring them as inputs (the
// other members' manifests are declared in `project.json`). Hashing them here keeps
// a cached success from being replayed; it does not make these targets affected by
// such an edit, which the tier's own `uv run --locked` targets are.
const TIER_MANIFESTS = [
  "tests/census_fallback/pyproject.toml",
  "tests/corpus_match/pyproject.toml",
  "tests/corpus_match_selection/pyproject.toml",
  "tests/live_e2e/pyproject.toml",
  "tests/runtime/pyproject.toml",
  "tests/nested-discriminator/runtime/pyproject.toml",
];

const isWindows = process.platform === "win32";
const digest = (path) => createHash("sha256").update(readFileSync(path)).digest("hex");

/** What `program args` prints, or "absent" for a tool that is missing or refuses. */
function ask(program, args, options = {}) {
  // A shell on Windows, for `.cmd` tools, joins its arguments unquoted.
  const [file, words] = isWindows ? [`"${program}"`, args.map((word) => `"${word}"`)] : [program, args];
  const run = spawnSync(file, words, { encoding: "utf8", shell: isWindows, ...options });
  return run.status === 0 ? run.stdout.trim() : "absent";
}

/**
 * The interpreter `uv run` runs the suites under here. `uv python find` only reads,
 * unlike `uv run`, which would sync; it ignores `UV_PYTHON`, which `uv run` obeys, so
 * that request is passed on.
 */
function pythonIdentity() {
  const request = process.env.UV_PYTHON;
  const interpreter = ask("uv", ["python", "find", ...(request ? [request] : [])]);
  return interpreter === "absent" ? interpreter : ask(interpreter, ["-I", "-"], { input: PYTHON_IDENTITY });
}

/** Every config file cargo merges for a build here: this directory, its parents, then cargo's home. */
function cargoConfigs(start) {
  const directories = [];
  for (let directory = start; ; directory = dirname(directory)) {
    directories.push(join(directory, ".cargo"));
    if (directory === dirname(directory)) break;
  }
  directories.push(process.env.CARGO_HOME ?? join(homedir(), ".cargo"));
  return directories.flatMap((directory) => ["config", "config.toml"].map((name) => join(directory, name))).filter(existsSync);
}

const named = (family) => Object.keys(process.env).filter((name) => family.test(name)).sort().map((name) => `${name}=${process.env[name]}`);

const lines = [
  `os: ${platform()} ${arch()}`,
  `python: ${pythonIdentity()}`,
  `uv: ${ask("uv", ["--version"])}`,
  ...named(PYTHON_ENV),
  ...TIER_MANIFESTS.map((path) => `tier manifest ${path}: ${existsSync(path) ? digest(path) : "absent"}`),
];
if (process.argv[2] !== "python") {
  lines.push(
    `node: ${process.version}`,
    `rustc: ${ask("rustc", ["-vV"])}`,
    `cargo: ${ask("cargo", ["-V"])}`,
    `nextest: ${ask("cargo", ["nextest", "--version"])}`,
    `llvm-cov: ${ask("cargo", ["llvm-cov", "--version"])}`,
    ...named(COMPILER_ENV),
    // By content, so moving a clone does not change the key.
    ...cargoConfigs(process.cwd()).map((path) => `cargo config: ${digest(path)}`),
  );
}
console.log(lines.join("\n"));
