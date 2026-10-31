# Reference
<details><summary><code>client.<a href="src/fern/client.py">exchange_token</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TokenBodyGrantType

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.exchange_token(
    grant_type=TokenBodyGrantType.AUTHORIZATION_CODE,
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

**request:** `TokenBody` 
    
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

