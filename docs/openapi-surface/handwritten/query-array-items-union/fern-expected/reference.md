# Reference
## Readings
<details><summary><code>client.readings.<a href="src/fern/readings/client.py">list_readings</a>(...) -> typing.List[float]</code></summary>
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

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.readings.list_readings()

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

**gauges:** `typing.Optional[typing.Union[ListReadingsRequestGaugesItem, typing.Sequence[ListReadingsRequestGaugesItem]]]` 
    
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

