# Reference
## Transcripts
<details><summary><code>client.transcripts.<a href="src/fern/transcripts/client.py">create_transcript</a>(...)</code></summary>
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

client.transcripts.create_transcript(
    audio="example_audio",
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

**audio:** `typing.Optional[core.File]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[CaptionFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**margins:** `typing.Optional[Margins]` 
    
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

