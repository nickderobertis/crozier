# Reference
## Captions Media
<details><summary><code>client.captions.media.<a href="src/fern/captions/media/client.py">caption_url</a>(...) -> CaptionMediaResponse</code></summary>
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

client.captions.media.caption_url(
    url="url",
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

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dialect:** `typing.Optional[CaptionMediaRequestDialect]` 
    
</dd>
</dl>

<dl>
<dd>

**speed:** `typing.Optional[CaptionMediaRequestSpeed]` 
    
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

<details><summary><code>client.captions.media.<a href="src/fern/captions/media/client.py">caption_file</a>(...) -> CaptionMediaResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.captions.media.caption_file(...)
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

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` 
    
</dd>
</dl>

<dl>
<dd>

**dialect:** `typing.Optional[CaptionMediaRequestDialect]` 
    
</dd>
</dl>

<dl>
<dd>

**speed:** `typing.Optional[CaptionMediaRequestSpeed]` 
    
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

