# Reference
## Beacons
<details><summary><code>client.beacons.<a href="src/fern/beacons/client.py#L28-L74">place_beacon</a>(...)</code></summary>
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

client.beacons.place_beacon(
    position={
        "lat": 41.5,
        "lon": -70.25
    },
    labels={
        "north": "tall",
        "south": "squat"
    },
    toggles={
        "lamp": True,
        "horn": False
    },
    offset={
        "dx": 3
    },
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

**position:** `typing.Dict[str, float]` — Two numeric pairs.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Dict[str, str]` — Two string pairs.
    
</dd>
</dl>

<dl>
<dd>

**toggles:** `typing.Dict[str, bool]` — Two boolean pairs.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Dict[str, int]` — One numeric pair (control).
    
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

