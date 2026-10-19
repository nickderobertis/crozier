# fern-goldens-git

- The Fern goldens tooling's suites that drive the real `git` — the lifecycle's
  publication to a bare local remote, `generate-corpus-fixtures.sh` over a
  local upstream — and the one that drives
  the real `just`. They are a project of their own so an edit to an offline
  fern-goldens test never pays for them; a change to a script they exercise
  reaches them through their `{workspaceRoot}` inputs.
- The helpers both suites use (`mirror`, `load_goldens_tool`, the fixture
  constants) stay in `tools/fern-goldens/tests/fern_goldens_test.py` and are
  imported, so the two halves build the same synthetic root.
- No case reaches the network or runs Docker or the Fern CLI.
- `test-certified-pair` runs `tools/fern-goldens/certified_pair.py` over the
  tracked tree (it lists files with `git ls-files`, hence this project). It is
  its own target so the many paths it reads never rerun the lifecycle suite,
  and it reads `crates/crozier-e2e/` without running it — hence the
  `measures:crozier-e2e` tag.
