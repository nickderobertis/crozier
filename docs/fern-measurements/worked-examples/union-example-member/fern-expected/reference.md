# Reference
## Watches
<details><summary><code>client.watches.<a href="src/fern/watches/client.py#L31-L71">create_watch</a>(...) -> Receipt</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TideTrigger, SurgeAlarm
from fern.environment import FernApiEnvironment

client = FernApi(
    environment=FernApiEnvironment.DEFAULT,
)

client.watches.create_watch(
    name="name",
    trigger=TideTrigger(
        station="harbour-mouth",
        height_m=2.5,
    ),
    alarm=SurgeAlarm(
        id="alarm-7",
        surge_m=1.2,
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**trigger:** `Trigger` 
    
</dd>
</dl>

<dl>
<dd>

**alarm:** `Alarm` 
    
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

