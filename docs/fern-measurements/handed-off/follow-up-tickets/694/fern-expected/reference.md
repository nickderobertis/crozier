# Reference
## Fleets
<details><summary><code>client.fleets.<a href="src/fern/fleets/client.py#L35-L63">create</a>(...)</code></summary>
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

client.fleets.create()

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

**sensors:** `typing.Optional[typing.List[CreateFleetsRequestSensorsItem]]` 
    
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

## Fleets Sensors
<details><summary><code>client.fleets.sensors.<a href="src/fern/fleets/sensors/client.py#L29-L56">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.fleets.sensors import FixedSensor

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.fleets.sensors.create(
    request=FixedSensor(),
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

**request:** `CreateSensorsRequest` 
    
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

