# Reference
## Alerts
<details><summary><code>client.alerts.<a href="src/fern/alerts/client.py">subscribe_alerts</a>(...) -> SubscribeAlertsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, AlertKind

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.alerts.subscribe_alerts(
    kinds=[
        AlertKind.ALL
    ],
    callback="callback",
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

**kinds:** `typing.List[AlertKind]` 
    
</dd>
</dl>

<dl>
<dd>

**callback:** `str` 
    
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

