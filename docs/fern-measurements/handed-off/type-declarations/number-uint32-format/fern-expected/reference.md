# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_lamp</a>(...) -> Lamp</code></summary>
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

client.get_lamp(
    lamp_id="lampId",
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

**lamp_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**min_lumens:** `typing.Optional[int]` — Brightness floor, a whole number declared as a number.
    
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

