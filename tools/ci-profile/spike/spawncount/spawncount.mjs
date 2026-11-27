// SPIKE ONLY (spike-windows-lane-breakdown): the Node half of sitecustomize.py, loaded
// through NODE_OPTIONS=--import. Each process appends one JSON line per child it starts to
// <SPIKE_SPAWN_LOG>/node-<pid>.jsonl, tagged with its Nx task and the script it runs (Node's
// test runner starts one process per test file).
import childProcess from "node:child_process";
import { appendFileSync } from "node:fs";
import { syncBuiltinESMExports } from "node:module";
import { basename, join } from "node:path";

const dir = process.env.SPIKE_SPAWN_LOG;
if (dir) {
  const write = (program, event = "spawn", seconds = undefined) => {
    try {
      appendFileSync(join(dir, `node-${process.pid}.jsonl`), `${JSON.stringify({ event, seconds, program: basename(String(program)).replace(/\.(exe|cmd)$/, ""), pid: process.pid, test: process.argv[1] ? basename(process.argv[1]) : null, nx: `${process.env.NX_TASK_TARGET_PROJECT}:${process.env.NX_TASK_TARGET_TARGET}` })}\n`);
    } catch {}
  };
  // exec calls module.exports.execFile, so a call made inside a wrapped one is the same child.
  let inside = 0;
  for (const name of ["spawn", "spawnSync", "execFile", "execFileSync", "exec", "execSync", "fork"]) {
    const original = childProcess[name];
    childProcess[name] = function (command, ...rest) {
      if (inside) return original.call(this, command, ...rest);
      // exec and execSync take a shell command line, whose first word is the program; the
      // others take the program itself, spaces in its path included.
      const program = name === "fork" ? "node" : name === "exec" || name === "execSync" ? String(command).trim().split(/\s+/)[0] : command;
      write(program);
      const start = performance.now();
      const done = () => write(program, "child", (performance.now() - start) / 1000);
      inside += 1;
      let child;
      try {
        child = original.call(this, command, ...rest);
      } finally {
        inside -= 1;
        if (name.endsWith("Sync")) done();
      }
      if (name.endsWith("Sync")) return child;
      child.once?.("close", done);
      return child;
    };
  }
  syncBuiltinESMExports();
}
