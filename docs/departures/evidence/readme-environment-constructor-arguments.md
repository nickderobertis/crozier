# Environments snippet constructor arguments

**Kind:** `fern-defect`. Measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25.

Fern's README writes an Environments snippet that constructs the client with
the environment alone. The Adyen Capital golden
(`tests/fixtures/adyen-capital/expected/README.md`, line 61) writes

```python
client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)
```

while its client requires a credential (`src/fern/client.py`:
`api_key: str` is keyword-only with no default), and the README's own usage
snippet passes `api_key="<value>"`. Running the documented construction against
the golden's own SDK fails:

```text
$ python -B -c "
import sys; sys.path.insert(0, 'tests/fixtures/adyen-capital/expected/src')
from fern import FernApi
from fern.environment import FernApiEnvironment
FernApi(environment=FernApiEnvironment.DEFAULT)"
TypeError: FernApi.__init__() missing 1 required keyword-only argument: 'api_key'
```

crozier passes the usage snippet's constructor arguments before the
environment. The rule admits only `README.md`'s Environments constructor, only
argument lines crozier writes that Fern's snippet lacks, and only lines
identical to one the README's usage constructor holds; a lifted base-path
argument is `lifted-base-path-docs-examples`' line. Its unit test rejects a
different value, an extra argument, a README without the usage constructor and
any other file. The departures ledger pins every occurrence.

**Historical.** This record was measured at Fern CLI 5.200.0 /
`fernapi/fern-python-sdk` 5.41.25, the pair certified when it was taken; where it
says "the certified pair" it means that pair. It has not been re-measured at
the current certified pair, Fern CLI 5.216.0 / fern-python-sdk 5.42.0. There
the goldens it cites were regenerated and differ from 5.41.25's only in each
README's Retries section and `.fern/metadata.json`, and the departure's rows in
`tests/fixtures/departures-ledger.tsv` recur on the same lines of Fern's output
(a README row after the Retries section ten lines earlier), so the defective
lines the record shows failing are Fern's at that pair too.
