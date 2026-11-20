# Reference
## retrieval_interface
<details><summary><code>client.retrieval_interface.<a href="src/fern/retrieval_interface/client.py#L28-L59">retrieve_uas_zones</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Note that some UAS Zones returned may lie entirely outside the requested ranges. Note that some data providers may choose not to permit unauthorized access to this endpoint, despite its definition in this specification for data providers that do choose to permit unauthorized access.
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
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.retrieval_interface.retrieve_uas_zones(
    request={"key": "value"},
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

**request:** `typing.Any` 
    
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

<details><summary><code>client.retrieval_interface.<a href="src/fern/retrieval_interface/client.py#L61-L92">retrieve_uas_zones_updates</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Note that some UAS Zones returned may lie entirely outside the requested ranges. Note that some data providers may choose not to permit unauthorized access to this endpoint, despite its definition in this specification for data providers that do choose to permit unauthorized access.
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
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.retrieval_interface.retrieve_uas_zones_updates(
    request={"key": "value"},
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

**request:** `typing.Any` 
    
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

## subscription_interface
<details><summary><code>client.subscription_interface.<a href="src/fern/subscription_interface/client.py#L28-L55">get_uas_zones_updates_subscription</a>() -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only subscriptions belonging to the caller are returned. This endpoint would be used if a data consumer lost track of subscriptions they had created and/or wanted to resolve an error indicating that they had too many existing subscriptions in an area.
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
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.subscription_interface.get_uas_zones_updates_subscription()

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

<details><summary><code>client.subscription_interface.<a href="src/fern/subscription_interface/client.py#L57-L88">subscribe_to_uas_zones_updates</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation creates a subscription for the user, with "PAUSED" state. The operation creates also a publication resource (i.e. queue) at the provider infrastructure, where all information updates related to the subscription will be delivered.
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
from fern import FernApi

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.subscription_interface.subscribe_to_uas_zones_updates(
    request={"key": "value"},
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

**request:** `typing.Any` 
    
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

