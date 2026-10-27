# Reference
<details><summary><code>client.<a href="src/fern/client.py">log_entry</a>(...) -> SurveyEntry</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SurveyEntry_Level
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.log_entry(
    pool_id="poolId",
    request=SurveyEntry_Level(
        level=,
    ),
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

**pool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `SurveyEntry` 
    
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

