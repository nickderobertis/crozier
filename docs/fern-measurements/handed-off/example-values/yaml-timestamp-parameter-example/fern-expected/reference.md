# Reference
## Tides
<details><summary><code>client.tides.<a href="src/fern/tides/client.py#L31-L87">list_tides</a>(...) -> typing.List[float]</code></summary>
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

<details><summary><code>client.tides.<a href="src/fern/tides/client.py#L89-L123">get_gauge</a>(...) -> GetGaugeResponse</code></summary>
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

<details><summary><code>client.tides.<a href="src/fern/tides/client.py#L125-L188">log_reading</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A body whose schema-level example gives date-time properties unquoted YAML timestamps, beside the sentinel instant the pair also drops.
</dd>
</dl>
</dd>
</dl>

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

client.tides.log_reading(
    gauge_id="gaugeId",
    level=3.4,
    high_water_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    low_water_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    calibrated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**request:** `TideReading` 
    
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

<details><summary><code>client.tides.<a href="src/fern/tides/client.py#L190-L241">log_readings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The same schema posted as an array body.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TideReading
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.tides.log_readings(
    gauge_id="gaugeId",
    request=[
        TideReading(
            level=3.4,
            high_water_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            low_water_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            calibrated_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
        )
    ],
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

**request:** `typing.List[TideReading]` 
    
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

