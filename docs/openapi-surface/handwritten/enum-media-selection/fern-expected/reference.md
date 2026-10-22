# Reference
<details><summary><code>client.<a href="src/fern/client.py">probe</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Choice

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.probe(
    valid=Choice.BETA,
    invalid="outside",
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

**valid:** `ProbeRequestValid` 
    
</dd>
</dl>

<dl>
<dd>

**invalid:** `ProbeRequestInvalid` 
    
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

