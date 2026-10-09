# Reference
<details><summary><code>client.<a href="src/fern/client.py">put_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The PutEvents operation records one or more events. You can have up to 1,500 unique custom events per app, any combination of up to 40 attributes and metrics per custom event, and any number of attribute or metric values.
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
from fern import FernApi, Event
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    amz_client_context="<x-amz-Client-Context>",
    environment=FernApiEnvironment.DEFAULT,
)

client.put_events(
    events=[
        Event(
            event_type="eventType",
            timestamp="timestamp",
        )
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

**events:** `typing.List[Event]` — An array of Event JSON objects
    
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

