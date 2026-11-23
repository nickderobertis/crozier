# Reference
## Beacons
<details><summary><code>client.beacons.<a href="src/fern/beacons/client.py#L27-L61">list_beacons</a>(...) -> typing.List[str]</code></summary>
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

client.beacons.list_beacons()

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

**range:** `typing.Optional[ListBeaconsRequestRange]` — A range label, or a range in metres.
    
</dd>
</dl>

<dl>
<dd>

**weight:** `typing.Optional[ListBeaconsRequestWeight]` — A weight label, or a weight in grams.
    
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

