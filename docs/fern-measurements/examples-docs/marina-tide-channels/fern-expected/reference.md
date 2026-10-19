# Reference
## Tides
<details><summary><code>client.tides.<a href="src/fern/tides/client.py">get_tides</a>(...) -> GetTidesResponse</code></summary>
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

client.tides.get_tides(
    station_id="station_id",
    since={"key": "value"},
    step=1.1,
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

**station_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `GetTidesRequestSince` 
    
</dd>
</dl>

<dl>
<dd>

**step:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**gauges:** `typing.Optional[typing.Union[float, typing.Sequence[float]]]` — Gauge numbers to read
    
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

<details><summary><code>client.tides.<a href="src/fern/tides/client.py">get_surge</a>(...) -> GetSurgeResponse</code></summary>
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

client.tides.get_surge(
    station_id="station_id",
    since={"key": "value"},
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

**station_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `GetSurgeRequestSince` 
    
</dd>
</dl>

<dl>
<dd>

**gauges:** `typing.Optional[typing.Union[float, typing.Sequence[float]]]` 
    
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

