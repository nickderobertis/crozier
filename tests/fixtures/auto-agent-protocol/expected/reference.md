# Reference
<details><summary><code>client.<a href="src/fern/client.py">send_message</a>(...) -> A2AMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

POST an A2A Message whose DataPart carries the AAP request payload. Dispatch is by `type` inside the DataPart.
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
from fern import FernApi, A2AMessage, A2AMessageRole, A2ADataPart, A2AMessageRequestConfiguration
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.send_message(
    message=A2AMessage(
        message_id="01HZ9G5N8D1Y4M6SP9C4XKVW3Q",
        role=A2AMessageRole.ROLE_USER,
        parts=[
            A2ADataPart(
                data={
                    "type": "dealer.information.request"
                },
                media_type="application/vnd.autoagent.dealer-information-request+json",
            )
        ],
    ),
    configuration=A2AMessageRequestConfiguration(
        accepted_output_modes=[
            "application/vnd.autoagent.dealer-information-response+json"
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

**message:** `A2AMessage` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[A2AMessageRequestConfiguration]` 
    
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

