# A null example on an optional body property

`openapi.yml` was authored from scratch: `submit_signal`'s body has an optional
`memo` whose only example is `null`. `fern-expected/` is the complete
comment-stripped output of Fern CLI 5.163.1 and Python SDK 5.41.3, with native
tree digest
`24b849f045c8b6a298154244b62b19ef9a1870b74f9d4d1dc330daec0a7fbe9e`.

`residual_null_example_is_absent_from_matching_request_snippets`, in
`crates/crozier-e2e/tests/e2e.rs`, byte-compares crozier's tree with it. It
then checks that the null argument is absent from both request snippets, and
that a required, non-null control reaches the worked call.

This tree used to be the hand-written supplemental proof of
`schema-example-null`, whose only golden witness, `webflow-v2`, was residual.
RS-Server, corpus row 3477, now byte-matches as a golden witness of that row.
The proof was retired from `docs/openapi-surface/residual-handwritten.toml`,
and the tree moved here, so it is no longer counted as coverage evidence. It
remains a regression test.
