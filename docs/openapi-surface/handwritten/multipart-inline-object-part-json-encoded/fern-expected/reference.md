# Reference
## Specimens
<details><summary><code>client.specimens.<a href="src/fern/specimens/client.py">upload_specimen</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.specimens import UploadSpecimenRequestLabel

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.specimens.upload_specimen(
    image="example_image",
    label=UploadSpecimenRequestLabel(),
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

**image:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `UploadSpecimenRequestLabel` 
    
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

