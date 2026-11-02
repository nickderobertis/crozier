# Reference
## Tides
<details><summary><code>client.tides.<a href="src/fern/tides/client.py">list_tides</a>(...) -> typing.List[float]</code></summary>
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

client.tides.list_tides(
    since=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    recorded_on="recordedOn",
    station="pier-7",
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

**since:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**recorded_on:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**logged_after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**station:** `typing.Optional[str]` 
    
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

<details><summary><code>client.tides.<a href="src/fern/tides/client.py">get_gauge</a>(...) -> GetGaugeResponse</code></summary>
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

client.tides.get_gauge(
    gauge_id="gauge-12",
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

**gauge_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**as_of:** `typing.Optional[datetime.datetime]` 
    
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

