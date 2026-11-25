# Reference
## Dispatches
<details><summary><code>client.dispatches.<a href="src/fern/dispatches/client.py#L29-L63">send_dispatch</a>(...) -> Receipt</code></summary>
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

client.dispatches.send_dispatch(
    channel="channel",
    notes=[
        {
            "key": "value"
        }
    ],
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

**channel:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.List[typing.Dict[str, typing.Any]]` — Free-form note objects; each item is a placeholder map.
    
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

