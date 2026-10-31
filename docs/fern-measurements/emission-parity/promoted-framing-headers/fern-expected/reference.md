# Reference
<details><summary><code>client.<a href="src/fern/client.py">list_signals</a>() -> typing.List[Signal]</code></summary>
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
    forwarded_proto="<X-Forwarded-Proto>",
    tower="<X-Tower>",
    base_url="https://yourhost.com/path/to/api",
)

client.list_signals()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">raise_signal</a>(...) -> Signal</code></summary>
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
    forwarded_proto="<X-Forwarded-Proto>",
    tower="<X-Tower>",
    base_url="https://yourhost.com/path/to/api",
)

client.raise_signal(
    flag="amber",
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

**request:** `Signal` 
    
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

