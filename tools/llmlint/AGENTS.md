# llmlint-tooling

- `test-plugins` skips where llmlint is absent unless
  `CROZIER_REQUIRE_LLMLINT=1` (CI's `llmlint` job sets it). Both the variable and
  `llmlint --version` are inputs, so a cached skip never replays where the binary
  or the requirement is present.
- `llmlint-plugins/` stays at the root: `llmlint.yml` and the lock name its files
  by that path. It is an input here, not part of this project.
