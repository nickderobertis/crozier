# GitHub workflow tooling

`github-workflows` is tagged `measures:release-packaging`: its artifact-contract
journeys read the cheap builder and publication scripts as source inputs without
invoking native packaging. Keep native compilation/install behind
`release-packaging:test`; workflow edits must not trigger that expensive suite.

## Draft lift

Marking a draft ready starts no `ci.yml` run; the draft's head-commit results
are the merge verdict. Do not re-add `ready_for_review` (why: beside
`pull_request.types` in `ci.yml`).
