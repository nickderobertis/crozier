# Reference
<details><summary><code>client.<a href="src/fern/client.py">log_inspection</a>(...)</code></summary>
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
import datetime

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.log_inspection(
    opened_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    closed_at=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    sealed_at=datetime.datetime.fromisoformat("2022-08-11T21:45:00+00:00"),
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

**opened_at:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**closed_at:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**sealed_at:** `datetime.datetime` 
    
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

