# Reference
## Signs
<details><summary><code>client.signs.<a href="src/fern/signs/client.py#L30-L64">hang_signs</a>(...)</code></summary>
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

client.signs.hang_signs(
    wordings=[
        "say \"cheese\""
    ],
    motto="the \'early\' bird",
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

**wordings:** `typing.List[HangSignsRequestWordingsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**motto:** `HangSignsRequestMotto` 
    
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

