#!/usr/bin/env node
// Prove each tool a lane's install steps put on PATH is there and runs, before the gate
// starts, so an installer that reported success without installing names its tool here
// instead of failing the first recipe that needs it.
//
//   node tools/ci/require-tools.mjs NAME[@VERSION]...
//
// NAME is the executable a later step runs: found on PATH (with PATHEXT on Windows), then
// asked its version — `cargo SUB --version` for a `cargo-SUB` plugin, `NAME --version`
// otherwise. `@VERSION` also holds that output to the pinned version.
//
// Exit status: 0 when every tool answered (one line naming them and their versions); 1
// naming each tool that is missing, does not run or answers another version, with what
// to do; 2 for an invocation it does not take.
import { spawnSync } from "node:child_process";
import { existsSync, statSync } from "node:fs";
import { delimiter, join } from "node:path";

const TOOL = "require-tools";
const NAME = /^[A-Za-z0-9][A-Za-z0-9._-]*$/;

function usage(message) {
  console.error(`${TOOL}: ${message}`);
  console.error(`${TOOL}: usage: node tools/ci/require-tools.mjs NAME[@VERSION]...`);
  process.exit(2);
}

/** The executable `name` resolves to on PATH, or null. */
function onPath(name) {
  const extensions = process.platform === "win32" ? ["", ...(process.env.PATHEXT ?? ".EXE;.CMD").split(";")] : [""];
  for (const directory of (process.env.PATH ?? "").split(delimiter)) {
    if (!directory) continue;
    for (const extension of extensions) {
      const candidate = join(directory, name + extension);
      if (existsSync(candidate) && statSync(candidate).isFile()) return candidate;
    }
  }
  return null;
}

const wanted = process.argv.slice(2).map((argument) => {
  const [name, version, ...rest] = argument.split("@");
  if (rest.length || !NAME.test(name) || version === "") usage(`'${argument}' is not NAME or NAME@VERSION`);
  return { name, version };
});
if (!wanted.length) usage("name at least one tool");

const found = [];
const problems = [];
for (const { name, version } of wanted) {
  const path = onPath(name);
  if (!path) {
    problems.push(`\`${name}\` is not on PATH`);
    continue;
  }
  const plugin = name.startsWith("cargo-") ? name.slice("cargo-".length) : null;
  const [command, args] = plugin ? ["cargo", [plugin, "--version"]] : [name, ["--version"]];
  // A Windows `.cmd` shim (an npm-installed CLI) runs only through the shell.
  const shell = !plugin && /\.(cmd|bat)$/i.test(path);
  const run = spawnSync(command, args, { encoding: "utf8", shell });
  const answer = `${run.stdout ?? ""}${run.stderr ?? ""}`.trim().split(/\r?\n/)[0] ?? "";
  if (run.error || run.status !== 0) {
    problems.push(`\`${[command, ...args].join(" ")}\` did not run (${run.error?.message ?? `exit ${run.status}`}): ${answer}`);
  } else if (version && !answer.split(/\s+/).some((word) => word.replace(/^v/, "") === version)) {
    problems.push(`\`${name}\` is not the pinned ${version}: it answered '${answer}'`);
  } else {
    found.push(answer.startsWith(name) ? answer : `${name} ${answer}`.trim());
  }
}

if (problems.length) {
  for (const problem of problems) console.error(`${TOOL}: ${problem}`);
  console.error(
    `${TOOL}: an install step reported success without leaving this on PATH; re-run the job, and if it recurs, fix that install step in the workflow`,
  );
  process.exit(1);
}
console.log(`${TOOL}: ${found.join(", ")}`);
