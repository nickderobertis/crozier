# tools/ci-profile

A measurement harness: it profiles CI runs, and nothing in the product depends on it.

- Parse what the runners print on CI, not on a terminal: Nx opens each task as a
  `::group::` with its status icon, and Node's test runner prints TAP.
- `parallelism: false` is modelled as Nx runs it, alone: Nx drains every running task
  first, so a replay that only serialises those tasks among themselves is a bound.
- `shutil.copytree` recurses through its own public name, so the spawn hook times only
  the outermost call.
- Runner processors vary between runs, so compare figures from one run, or from
  repeated runs, not one run against another.
