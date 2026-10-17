# Reference
## Radio
<details><summary><code>client.radio.<a href="src/fern/radio/client.py">broadcast</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.radio import BroadcastRequestMessage, BroadcastRequestMessagePartsItem_Voice, BroadcastRequestMessagePartsItem_Position

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.radio.broadcast(
    message=BroadcastRequestMessage(
        channel="16",
        parts=[
            BroadcastRequestMessagePartsItem_Voice(
                transcript="Requesting a berth for the night",
            ),
            BroadcastRequestMessagePartsItem_Position(
                fix={
                    "grid": "SU4205"
                },
            )
        ],
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

**message:** `BroadcastRequestMessage` 
    
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

