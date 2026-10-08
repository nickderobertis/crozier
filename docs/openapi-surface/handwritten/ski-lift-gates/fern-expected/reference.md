# Reference
<details><summary><code>client.<a href="src/fern/client.py">scan_pass</a>(...) -> Turnstile</code></summary>
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
    lift_pass="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.scan_pass(
    gate_id="gateId",
    skier="skier",
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

**gate_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skier:** `str` 
    
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

