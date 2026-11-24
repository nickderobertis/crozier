# Reference
## AgentRuntime
<details><summary><code>client.agent_runtime.<a href="src/fern/agent_runtime/client.py#L30-L58">create_runtime_profile</a>(...) -> Profile</code></summary>
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
from fern.agent_runtime import CreateRuntimeProfileRequestMode

client = FernApi(
    environment=FernApiEnvironment.PRODUCTION,
)

client.agent_runtime.create_runtime_profile(
    mode=CreateRuntimeProfileRequestMode.WARM,
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

**mode:** `CreateRuntimeProfileRequestMode` 
    
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

## Versions
<details><summary><code>client.versions.<a href="src/fern/versions/client.py#L26-L53">list_versions</a>(...) -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.versions.list_versions()

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

**channel:** `typing.Optional[ListVersionsRequestChannel]` 
    
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

## Zones
<details><summary><code>client.zones.<a href="src/fern/zones/client.py#L26-L53">list_zones</a>(...) -> typing.List[str]</code></summary>
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.zones.list_zones()

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

**kind:** `typing.Optional[ListZonesRequestKind]` 
    
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

