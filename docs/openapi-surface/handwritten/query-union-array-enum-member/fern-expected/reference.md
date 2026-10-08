# Reference
## Signals
<details><summary><code>client.signals.<a href="src/fern/signals/client.py">inspect_signals</a>(...) -> str</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.signals import InspectSignalsRequestKindZero

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.signals.inspect_signals(
    kind=InspectSignalsRequestKindZero.OPTICAL,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kind:** `InspectSignalsRequestKind` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

