# Reference
## Signals
<details><summary><code>client.signals.<a href="src/fern/signals/client.py">list_signals</a>(...) -> typing.List[str]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.signals.list_signals(
    quoted_from=datetime.datetime.fromisoformat("2032-06-02T04:30:00+00:00"),
    lamp="lamp-east",
    observed_to=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**observed_to:** `Moment` 
    
</dd>
</dl>

<dl>
<dd>

**observed_from:** `typing.Optional[Moment]` 
    
</dd>
</dl>

<dl>
<dd>

**quoted_from:** `typing.Optional[QuotedMoment]` 
    
</dd>
</dl>

<dl>
<dd>

**lamp:** `typing.Optional[LampCode]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

