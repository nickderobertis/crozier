# Reference
## Entries
<details><summary><code>client.entries.<a href="src/fern/entries/client.py#L29-L56">add_entry</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, StudioNote

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.entries.add_entry(
    request=StudioNote(
        text="text",
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

**request:** `AddEntryRequest` 
    
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

