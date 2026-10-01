# extension-reference-cycle: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair.
Measurements use CPython 3.12.3, mypy 1.13.0 and the generated
`pyproject.toml` configuration with its declared dependencies.

The [probe package and client import](evaluation-logs/probe.log), and mypy
reports zero errors. `Node.x-link.target` refers back to `Node`; this is
extension metadata, while the declared wire object has only `id`. The
[public model journey](evaluation-logs/probe.wire.log) serializes `{id: A}`
and parses its unchanged `id`. The document declares no HTTP endpoint, so
this model boundary is the available sending/parsing interface.

One representative, [Stripe's SDK description,
`92363b86025d012852f648554372bf5fa6146af1472fb63f3c29d7c5fe6bd19a`](evaluation-logs/population.log),
cannot import its root client: a generated `application_fee_fee_source` module
is missing. Mypy reports **60 errors in 11 files**. The offending
`POST /v2/core/account_links` request's `account` string carries
`x-stripeProperty.referenced_resource`, referring to `v2.core.account` and
participating in a metadata-reference cycle. The [public client boundary](evaluation-logs/population.wire.log)
fails on import, so no client can send or parse that account field; no request
is sent and no response returned. This class is `refuse` because the population
package fails, although the small probe's crozier output works. Both population
documents come from this same Stripe publisher.

Fern's [probe record](fern-refusal.txt) is a false success: check and generation
exit 0 despite `Maximum call stack size exceeded`, and its 35-file output comes
from a document it never parsed. Pinned runs reproduce this for
[another extension key](evaluation-logs/fern-other-extension.log) and
[a two-schema metadata cycle](evaluation-logs/fern-two-schema-cycle.log).
They accept [ordinary schema recursion](evaluation-logs/fern-ordinary-recursion.log),
[an acyclic extension reference](evaluation-logs/fern-acyclic-extension.log),
and [a metadata edge with an ordinary property return edge](evaluation-logs/fern-ordinary-return-edge.log).
The detector follows extension references between their targets, leaving
ordinary Schema Object references to the normal loader. The CLI recovery
journey preserves the accepted cases, compares output bytes in both modes,
and covers an ignored source schema.

The [population refusal log](evaluation-logs/population-refusals.jsonl)
covers both retrievable documents in both modes: exit 1, no files, one line
identifying the class and `x-stripeProperty`, with `fern-strict` as the
strict-mode cause. A preserved detector build makes the measurement independent
of assertion-witness rebuilds.

The [CLI assertion fails with only the cycle check disabled](evaluation-logs/refusal-e2e-induced-red.log),
writing 37 files for the probe instead of refusing. This deliberately records
an induced earlier state; the finished source restores the check.
