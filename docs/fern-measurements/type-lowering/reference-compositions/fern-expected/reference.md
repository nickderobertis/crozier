# Reference
## Scans
<details><summary><code>client.scans.<a href="src/fern/scans/client.py#L30-L56">start_scan</a>(...) -> ScanResponse</code></summary>
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

client.scans.start_scan(
    text="text",
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

**text:** `str` 
    
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

<details><summary><code>client.scans.<a href="src/fern/scans/client.py#L58-L84">get_portal</a>(...) -> Portal</code></summary>
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

client.scans.get_portal(
    portal_id="portalId",
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

**portal_id:** `str` 
    
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

