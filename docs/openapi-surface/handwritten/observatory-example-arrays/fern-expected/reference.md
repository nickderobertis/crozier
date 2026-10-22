# Reference
<details><summary><code>client.<a href="src/fern/client.py">record_reading</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
import datetime

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.record_reading(
    observed_days=[
        datetime.date.fromisoformat("2025-04-08"),
        datetime.date.fromisoformat("2025-04-08"),
        datetime.date.fromisoformat("2025-04-09")
    ],
    annotation=[
        "annotation"
    ],
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

**observed_days:** `typing.List[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**annotation:** `RecordReadingRequestAnnotation` 
    
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

