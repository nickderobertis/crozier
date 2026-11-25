# Reference
## Prints
<details><summary><code>client.prints.<a href="src/fern/prints/client.py#L29-L79">submit_print</a>(...) -> Print</code></summary>
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

client.prints.submit_print(
    instructions="instructions",
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

**instructions:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**negative:** `typing.Optional[bytes]` 
    
</dd>
</dl>

<dl>
<dd>

**contacts:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**layers:** `typing.Optional[typing.Dict[str, str]]` 
    
</dd>
</dl>

<dl>
<dd>

**mask:** `typing.Optional[bytes]` 
    
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

