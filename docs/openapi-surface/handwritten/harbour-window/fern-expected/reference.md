# Reference
<details><summary><code>client.<a href="src/fern/client.py">book_crossing</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, CrossingWindow

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.book_crossing(
    route="route",
    window=CrossingWindow.SLACK,
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

**route:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**window:** `CrossingWindow` — Scheduled crossings never leave at slack water.
    
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

<details><summary><code>client.<a href="src/fern/client.py">book_charter</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, CharterWindow

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.book_charter(
    skipper="skipper",
    window=CharterWindow.SLACK,
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

**skipper:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**window:** `CharterWindow` — Charters never leave at slack water.
    
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

