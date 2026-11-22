# Abbreviated README calls of a method requiring an argument

**Kind:** `fern-defect`. Measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25.

Fern's README abbreviates the demonstrated call in its exception-handling,
raw-response, retry and timeout snippets: `client.probe(...)` when the
operation takes a path, query or body argument, `client.probe()` otherwise. A
required header is not counted. The authored probe
`docs/openapi-surface/authored-probes/353-method-required-array` declares one
operation whose only parameter is a required array header; its golden's
`README.md` writes `client.probe()` (line 96) and
`client.probe(request_options={` (lines 144 and 159), while its client declares
`def probe(self, *, probe_param: typing.Sequence[str], ...)`. On the golden's
own SDK:

```text
$ python -B -c "
import sys; sys.path.insert(0, 'docs/openapi-surface/authored-probes/353-method-required-array/fern-expected/src')
from fern import FernApi
FernApi().probe()"
TypeError: FernApi.probe() missing 1 required keyword-only argument: 'probe_param'
```

crozier counts a required header as an argument and writes Fern's own elision,
`client.probe(...)` and `client.probe(..., request_options={`. The rule admits
only a `README.md` line equal to Fern's but for that elision, where crozier's
called client defines the method with a parameter that has no default; its unit
test rejects another argument list, another method, a trailing change and a
method whose parameter is optional. The departures ledger pins every
occurrence.

**Historical.** This record was measured at Fern CLI 5.200.0 /
`fernapi/fern-python-sdk` 5.41.25, the pair certified when it was taken; where it
says "the certified pair" it means that pair. It has not been re-measured at
the current certified pair, Fern CLI 5.216.0 / fern-python-sdk 5.42.0. There
the goldens it cites were regenerated and differ from 5.41.25's only in each
README's Retries section and `.fern/metadata.json`, and the departure's rows in
`tests/fixtures/departures-ledger.tsv` recur on the same lines of Fern's output
(a README row after the Retries section ten lines earlier), so the defective
lines the record shows failing are Fern's at that pair too.
