# GitHub workflow tooling

`github-workflows` is tagged `measures:release-packaging`: its artifact-contract
journeys read the cheap builder and publication scripts as source inputs without
invoking native packaging. Keep native compilation/install behind
`release-packaging:test`; workflow edits must not trigger that expensive suite.

## Draft lift and the Mac check

`ci.yml` does not run when a draft is marked ready for review: its
`pull_request` types are `opened`, `synchronize` and `reopened`. The draft's run
already reported `gate` (Mac lane included), `commitlint` and `llmlint` on the
head commit, and the lift changes no commit, so those results satisfy branch
protection. A failed draft run is recovered by re-running it or pushing a commit.
