# Digit-leading body properties in worked calls

**Kind:** `fern-defect`. Measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25.

A request-body property whose name starts with a digit, `5gMmCauseValue` in the
free5GC PDU-session document, is the method parameter `_5g_mm_cause_value`.
Where the property declares an example, Fern's worked calls pass it by another
name: `f_5g_mm_cause_value=0` in the client docstrings
(`tests/fixtures/free5gc-pdu-session/expected/src/fern/individual_sm_context/client.py`
lines 476 and 599, and the PDU-session client's) and `f_value=0` in
`reference.md` (lines 402, 489, 1216 and 1330). Across the 1308 trees the
golden comparisons read, these 10 lines in this one golden are every
occurrence. On the golden's own SDK:

```text
$ python -B -c "
import sys; sys.path.insert(0, 'tests/fixtures/free5gc-pdu-session/expected/src')
from fern import FernApi
client = FernApi(token='t', base_url='https://x.invalid')
client.individual_sm_context.update_sm_context(sm_context_ref='r', f_5g_mm_cause_value=0)"
TypeError: IndividualSmContextClient.update_sm_context() got an unexpected keyword argument 'f_5g_mm_cause_value'. Did you mean '_5g_mm_cause_value'?
```

crozier passes the parameter the method declares, with the same value. The
rule admits a docstring, `README.md` or `reference.md` argument line whose
keyword is `_<digit…>`, a parameter crozier's client declares, where Fern's line
is the same with `f_<digit…>` or `f_<last word>` for the keyword; its unit test
rejects another value, another keyword, another indent, a context without the
parameter and a model file.

**Historical.** This record was measured at Fern CLI 5.200.0 /
`fernapi/fern-python-sdk` 5.41.25, the pair certified when it was taken; where it
says "the certified pair" it means that pair. It has not been re-measured at
the current certified pair, Fern CLI 5.216.0 / fern-python-sdk 5.42.0. There
the goldens it cites were regenerated and differ from 5.41.25's only in each
README's Retries section and `.fern/metadata.json`, and the departure's rows in
`tests/fixtures/departures-ledger.tsv` recur on the same lines of Fern's output
(a README row after the Retries section ten lines earlier), so the defective
lines the record shows failing are Fern's at that pair too.
