# Reference
## Entries
<details><summary><code>client.entries.<a href="src/fern/entries/client.py">list_entries</a>(...) -> typing.List[str]</code></summary>
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

client.entries.list_entries(
    tide=1,
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

**tide:** `ListEntriesRequestTide` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[ListEntriesRequestSince]` 
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[ListEntriesRequestUntil]` 
    
</dd>
</dl>

<dl>
<dd>

**season:** `typing.Optional[ListEntriesRequestSeason]` 
    
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

