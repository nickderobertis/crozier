# github-action

The composite GitHub Action's scripts (`install.sh`, `compare.sh`, `finish.sh`,
`summary.sh`, `lib.sh`), which `action.yml` (at the root, where consumers'
`uses: nickderobertis/crozier@v0` finds it) runs from `$GITHUB_ACTION_PATH`, and
the `crozier-github-action` test crate holding `action.yml` to its docs page and
example workflow.

- The Action's behaviour over a real binary is driven by crozier-e2e's
  `action.rs`; these scripts are inputs of `crozier-e2e:test`.
- `install.sh` installs the release through `scripts/install.sh`, the end-user
  installer, which stays at that path: the README tells users to fetch it there.
