# GitHub workflow tooling

`github-workflows` is tagged `measures:release-packaging`: its artifact-contract
journeys read the cheap builder and publication scripts as source inputs without
invoking native packaging. Keep native compilation/install behind
`release-packaging:test`; workflow edits must not trigger that expensive suite.

`.github/governance.json` is the final required-check declaration and is not applied here;
the graph tests reconcile it with `ci.yml`. A remote reusable workflow is refused by
`workflow-graph.mjs`, because its jobs are slots this graph could not count.
