# GitHub workflow tooling

`github-workflows` is tagged `measures:release-packaging`: its artifact-contract
journeys read the cheap builder and publication scripts as source inputs without
invoking native packaging. Keep native compilation/install behind
`release-packaging:test`; workflow edits must not trigger that expensive suite.

## Draft lift and the Mac check

A `ready_for_review` run of `ci.yml` never requests a Mac runner. It waits for
the draft's run (concurrency does not cancel it), then reuses that run's Mac job
if it passed on exactly the same head; otherwise its `macos` job fails on Linux
with the reason, and so does `gate`. Recovery: re-run the draft run's Mac job,
then re-run all jobs of the lift run (the policy job must re-read the API), or
push a commit, which runs Mac on the new head.
