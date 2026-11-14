# Escaped method names in README calls

**Kind:** `fern-defect`. Measured at Fern CLI 5.200.0 / fern-python-sdk 5.41.25.

The same escape as `reference-heading-escaped-method-name`, in `README.md`'s
exception-handling, raw-response, retry and timeout snippets. The Apideck
Connector golden (`tests/fixtures/apideck.com-connector/expected/README.md`)
writes `client.apis.all(...)` at lines 92, 140 and 155 and
`client.apis.with_raw_response.all(...)` at line 109, while its
`src/fern/apis/client.py` and `raw_client.py` define `all_`, and the usage
snippet of the same README calls `client.apis.all_(`. On the golden's own SDK:

```text
$ python -B -c "
import sys; sys.path.insert(0, 'tests/fixtures/apideck.com-connector/expected/src')
from fern import FernApi
client = FernApi(api_key='k', apideck_app_id='a')
client.apis.all"
AttributeError: 'ApisClient' object has no attribute 'all'. Did you mean: 'all_'?
```

crozier writes the method the client defines. The rule admits only a
`README.md` line whose call names a method ending in `_` that crozier's called
group's client or raw client defines, with Fern's line identical but for that
name less its escape. Its unit test rejects another argument list, another
name, another group and a context without the method; the departures ledger
pins every occurrence.
