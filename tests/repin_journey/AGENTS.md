# repin-journey

- A promoted tier: `just census-repin` over a scratch clone of a pinned crozier
  commit, built and run instrumented step by step (hours at `--jobs 1`). Its edges
  name only the tooling it drives, never `crozier`, so a `src/` change never
  selects it; `ci.yml`'s `repin-journey` job runs it when that tooling changes.
- Re-pin `PINNED` (and the edits it anchors) only when the pinned tree no longer
  builds with the toolchain file.
