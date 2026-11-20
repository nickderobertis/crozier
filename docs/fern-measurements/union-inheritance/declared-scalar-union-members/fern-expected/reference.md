# Reference
<details><summary><code>client.<a href="src/fern/client.py#L101-L139">record_reading</a>(...)</code></summary>
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
    sensor="sensor",
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

**sensor:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[ReadingValue]` 
    
</dd>
</dl>

<dl>
<dd>

**threshold:** `typing.Optional[ReadingThreshold]` 
    
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

