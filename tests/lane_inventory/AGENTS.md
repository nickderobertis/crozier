# lane-inventory

- The check that no test entrypoint or platform leaves the pull request flow
  (`tools/ci/lanes.json` against every `project.json` and `ci.yml`). A project of its own
  because a tier's manifest edit must select it: only a `type:tier`, `cost:expensive` project
  may name tier manifests as inputs, and a deleted tier has no lint of its own left to fail.
- A new directory of tiers outside `tests/` needs its manifest added to this project's inputs.
