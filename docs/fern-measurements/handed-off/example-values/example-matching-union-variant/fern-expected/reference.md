# Reference
## Seals
<details><summary><code>client.seals.<a href="src/fern/seals/client.py">verify_seal</a>(...) -> VerifySealResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.seals import VerifySealRequestSeal_Stamp

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.seals.verify_seal(
    seal=VerifySealRequestSeal_Stamp(
        stamp_id="stamp_id",
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

**seal:** `VerifySealRequestSeal` 
    
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

