# Reference
<details><summary><code>client.<a href="src/fern/client.py">record_reading</a>(...)</code></summary>
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

client.record_reading(
    depot=9223372036854776000,
    vehicle="vehicle",
    metres=9223372036854776000,
    trip_count=9007199254740992,
    checkpoints=[
        9223372036854776000
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

**depot:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**vehicle:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metres:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**trip_count:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**checkpoints:** `typing.List[int]` 
    
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

