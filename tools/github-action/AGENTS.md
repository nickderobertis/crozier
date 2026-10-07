# github-action

- `action.yml` stays at the repository root, where `uses:
  nickderobertis/crozier@v0` finds it, and runs these scripts from
  `$GITHUB_ACTION_PATH/tools/github-action/`.
- The Action's behaviour over a real binary is driven by crozier-e2e's
  `action.rs`, so these scripts are inputs of `crozier-e2e:test`.
- `install.sh` installs the release through `scripts/install.sh`, the end-user
  installer, which stays at that path: the README tells users to fetch it there.
