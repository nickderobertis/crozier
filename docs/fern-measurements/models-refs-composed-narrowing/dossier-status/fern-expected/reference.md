# Reference
<details><summary><code>client.<a href="src/fern/client.py">file_dossier</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, DossierStanding

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.file_dossier(
    reference="reference",
    standing=DossierStanding.DRAFT,
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

**reference:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**standing:** `DossierStanding` — A filed dossier is never a draft.
    
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

