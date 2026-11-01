# Reference
## Scans
<details><summary><code>client.scans.<a href="src/fern/scans/client.py">file_scan</a>(...)</code></summary>
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

client.scans.file_scan(
    scan="example_scan",
    drawer="drawer",
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

**scan:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**drawer:** `FileScanRequestDrawer` 
    
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

