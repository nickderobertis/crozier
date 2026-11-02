# Reference
<details><summary><code>client.<a href="src/fern/client.py">send_alert</a>(...) -> QueuedAlert</code></summary>
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

client.send_alert(
    device_id="deviceId",
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

**device_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**deliver_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**headline:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**muted:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**chime:** `typing.Optional[AlertPayloadChime]` 
    
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

