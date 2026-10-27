# Reference
## Beacons
<details><summary><code>client.beacons.<a href="src/fern/beacons/client.py">get_beacon</a>(...) -> Beacon</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the beacon's lamp and its schedule. The lamp is lit at dusk.
A beacon that was retired answers 404.
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

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.beacons.get_beacon(
    beacon_id="beaconId",
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

**beacon_id:** `str` — The beacon's identifier, as #registered
    
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

