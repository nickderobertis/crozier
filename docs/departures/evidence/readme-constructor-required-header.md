# Required typed headers in README and reference constructions

**Kind:** `fern-defect`. Measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25.

A header declared on every operation is promoted to a client constructor
parameter. Fern's `README.md` and `reference.md` constructions pass a required
string header (`tenant="<X-Tenant>"`) but leave a required boolean, numeric or
array one out (the measurement in
`docs/fern-measurements/handed-off/snippet-rendering/snippet-rendering/`
recorded the omission). The authored probe
`docs/openapi-surface/authored-probes/353-promoted-required-array` declares a
required array header on its operations; its golden's `README.md` constructs
`client = FernApi()` (lines 40 and 53, `AsyncFernApi()` at 67, and
`reference.md` lines 18 and 66), while its client declares
`probe_param: typing.List[str]` with no default (`src/fern/client.py`
line 70). On the golden's own SDK:

```text
$ python -B -c "
import sys; sys.path.insert(0, 'docs/openapi-surface/authored-probes/353-promoted-required-array/fern-expected/src')
from fern import FernApi
FernApi()"
TypeError: FernApi.__init__() missing 1 required keyword-only argument: 'probe_param'
```

crozier passes the header with the typed example its client docstrings give it:
two copies of the item's placeholder for an array (`probe_param=["probeParam",
"probeParam"]`, the form Fern writes for a method's array header), `True`, `1`
or `1.1` otherwise (`non-string-client-header-example`, which also replaces the
docstrings' `probe_param="YOUR_PROBE_PARAM"`). The region rule admits a
`README.md` or `reference.md` construction only where crozier's, without the
arguments for required boolean, numeric or list-typed parameters its own client
constructor declares (and closed on its opening line when nothing else is
left), is Fern's at the nearest place. Its unit test rejects a string or
optional parameter, any other change, a method call and a code file; the
departures ledger pins every occurrence.

**Historical.** This record was measured at Fern CLI 5.200.0 /
`fernapi/fern-python-sdk` 5.41.25, the pair certified when it was taken; where it
says "the certified pair" it means that pair. It has not been re-measured at
the current certified pair, Fern CLI 5.216.0 / fern-python-sdk 5.42.0. There
the goldens it cites were regenerated and differ from 5.41.25's only in each
README's Retries section and `.fern/metadata.json`, and the departure's rows in
`tests/fixtures/departures-ledger.tsv` recur on the same lines of Fern's output
(a README row after the Retries section ten lines earlier), so the defective
lines the record shows failing are Fern's at that pair too.
