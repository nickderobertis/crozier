# Tilecast replay evidence

The source is `gbyo/tilecast:docs/openapi.yaml` at immutable revision
`9b731f41de1c1387ebd7a7f74c3c783510aa67a0`, SHA-256
`832b9080645151da0612125abdb82afeb90c6dd0b33da87dcdcd5edc1d3178ce`.
`fern-expected/` and `expected-literals/` retain the certified pair’s golden and
literals overlay formerly registered as corpus row 5534. These are measurement
artifacts, with their original generation provenance, not corpus registrations.

Both normalized modes byte-matched. Earlier corpus runs passed in 1400.57
seconds (normal) and 974.31 seconds (instrumented). On merged tree `08b9ee650`,
`cargo test -p crozier-e2e --test e2e registered_literals_` passed the other 71
replays, but Tilecast remained active at 1805.75 seconds from thread creation.
The worker stopped that test process under the manager’s 30-minute ruling.
The root cause is `corpus test does not complete within 30 minutes`; registration
can resume after performance repair. The log does not isolate the dominant
phase. The base golden has 233 files including provenance, 2,363,405 bytes.

The [comparison record](../../comparisons/832b9080645151da0612125abdb82afeb90c6dd0b33da87dcdcd5edc1d3178ce.txt)
retains the successful normalized comparison. The source’s grant remains in
NOTICE.
