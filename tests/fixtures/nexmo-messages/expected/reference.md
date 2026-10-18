# Reference
<details><summary><code>client.<a href="src/fern/client.py">send_message</a>(...) -> SendMessageResponseMessageUuid</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a Message
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SendMessageRequestZero, ChannelOptionsSmsChannel, TextMessageType
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.send_message(
    request=SendMessageRequestZero(
        to="apricot",
        from_="from",
        channel=ChannelOptionsSmsChannel.SMS,
        text={"key": "value"},
        message_type=TextMessageType.TEXT,
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

**request:** `SendMessageRequest` 
    
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

