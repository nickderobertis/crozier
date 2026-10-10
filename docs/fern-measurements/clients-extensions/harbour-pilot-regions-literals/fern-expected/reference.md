# Reference
<details><summary><code>client.<a href="src/fern/client.py">book_pilot</a>(...) -> str</code></summary>
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

client.book_pilot(
    vessel="vessel",
    eta=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
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

**vessel:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**eta:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**tug:** `typing.Optional[BookPilotRequestTug]` 
    
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

