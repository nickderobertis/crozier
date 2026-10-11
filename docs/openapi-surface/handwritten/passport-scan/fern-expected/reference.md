# Reference
<details><summary><code>client.<a href="src/fern/client.py">submit_application</a>(...)</code></summary>
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

client.submit_application(
    photo="example_photo",
    signature="example_signature",
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

**photo:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `typing.Optional[core.File]` 
    
</dd>
</dl>

<dl>
<dd>

**remarks:** `typing.Optional[str]` 
    
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

