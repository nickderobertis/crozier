# Reference
<details><summary><code>client.<a href="src/fern/client.py">list_tides</a>(...) -> typing.List[TideTable]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the tide tables the harbour publishes.

Archived tables are filed under C:\
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
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.list_tides()

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

**port:** `typing.Optional[str]` — The port whose tables to list.
    
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

<details><summary><code>client.<a href="src/fern/client.py">forecast_surge_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forecasts a storm surge for one port.

Raw readings are filed under D:\
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
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.forecast_surge_stream(
    port="port",
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

**stream:** `typing.Literal` — Whether to stream the forecast as it is computed.
    
</dd>
</dl>

<dl>
<dd>

**port:** `str` — The port to forecast for.
    
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

<details><summary><code>client.<a href="src/fern/client.py">forecast_surge</a>(...) -> Surge</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forecasts a storm surge for one port.

Raw readings are filed under D:\
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
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.forecast_surge_stream(
    port="port",
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

**stream:** `typing.Literal` — Whether to stream the forecast as it is computed.
    
</dd>
</dl>

<dl>
<dd>

**port:** `str` — The port to forecast for.
    
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

## Forecasts
<details><summary><code>client.forecasts.<a href="src/fern/forecasts/client.py">forecast_the_next_tide</a>(...) -> Forecast</code></summary>
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.forecasts.forecast_the_next_tide(
    port="port",
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

**stream:** `typing.Literal` — Whether to stream the forecast as it is computed.
    
</dd>
</dl>

<dl>
<dd>

**port:** `str` — The port to forecast for.
    
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

## Gauges
<details><summary><code>client.gauges.<a href="src/fern/gauges/client.py">list_gauges</a>() -> typing.List[Gauge]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the harbour's tide gauges.

Calibration files sit under E:\
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
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.gauges.list_gauges()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

