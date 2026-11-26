# Reference
## Bulletins
<details><summary><code>client.bulletins.<a href="src/fern/bulletins/client.py#L29-L81">notify_bulletin</a>(...) -> Bulletin</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.bulletins.notify_bulletin(
    bulletin_id="bulletin_id",
    cc_addresses=[
        "alpha-one@example.com",
        "second-beta-twoooo@example.com"
    ],
    bcc_addresses=[
        "alpha-on@example.com",
        "second-beta-twooo@example.com"
    ],
    routing={
        "priority": "high",
        "channel": "postal-mail-express-one-twooo"
    },
    handling={
        "priority": "high",
        "channel": "postal-mail-express-one-tww"
    },
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

**bulletin_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cc_addresses:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**bcc_addresses:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**routing:** `typing.Dict[str, str]` 
    
</dd>
</dl>

<dl>
<dd>

**handling:** `typing.Dict[str, str]` 
    
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

