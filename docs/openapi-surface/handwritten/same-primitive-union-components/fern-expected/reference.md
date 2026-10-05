# Reference
## Readings
<details><summary><code>client.readings.<a href="src/fern/readings/client.py">submit_reading</a>(...) -> Reading</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.readings.submit_reading(
    station_code="station_code",
    level_cm=1.1,
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

**station_code:** `StationCodeOne` 
    
</dd>
</dl>

<dl>
<dd>

**level_cm:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[GaugeChannelTwo]` 
    
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

