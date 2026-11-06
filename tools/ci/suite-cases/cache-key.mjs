#!/usr/bin/env node
// What `suite-cases:test` compiles and collects under, beyond its files: Nx hashes
// this output as a runtime input, because it hashes neither the operating system
// nor the environment by itself, and a listed env input cannot name a family such
// as `CARGO_PROFILE_*` or see the user-level cargo config. It must never fail: a
// failing runtime input stops Nx hashing the whole run.
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { existsSync, readFileSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join } from "node:path";

const COMPILER_ENV = /^(RUSTC|RUSTC_WRAPPER|RUSTC_WORKSPACE_WRAPPER|RUSTFLAGS|RUSTDOCFLAGS|CARGO_ENCODED_RUSTFLAGS|CARGO_ENCODED_RUSTDOCFLAGS|CARGO_BUILD_.+|CARGO_PROFILE_.+|CARGO_TARGET_.+_(RUSTFLAGS|LINKER|RUNNER))$/;

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

const rustc = spawnSync("rustc", ["-vV"], { encoding: "utf8", shell: process.platform === "win32" });
const lines = [
  `os: ${process.platform} ${process.arch}`,
  `rustc: ${rustc.status === 0 ? rustc.stdout.trim() : "absent"}`,
  ...Object.keys(process.env).filter((name) => COMPILER_ENV.test(name)).sort().map((name) => `${name}=${process.env[name]}`),
  // By content, so moving a clone does not change the key.
  ...cargoConfigs(process.cwd()).map((path) => `cargo config: ${createHash("sha256").update(readFileSync(path)).digest("hex")}`),
];
console.log(lines.join("\n"));
