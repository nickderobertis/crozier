# Reference
<details><summary><code>client.<a href="src/fern/client.py">health</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import the full state of Otoroshi as a file
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.health()

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

## apikeys
<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">all_api_keys</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all api keys
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.all_api_keys()

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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">api_keys_from_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all api keys for the group of a service
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.api_keys_from_group(
    group_id="groupId",
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

**group_id:** `str` — The api key group id
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">create_api_key_from_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new api key for a group
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.create_api_key_from_group(
    group_id="groupId",
    authorized_entities=["a string value"],
    client_id="a string value",
    client_name="a string value",
    client_secret="a string value",
    enabled=True,
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

**group_id:** `str` — The api key group id
    
</dd>
</dl>

<dl>
<dd>

**authorized_entities:** `typing.Sequence[str]` — The group/service ids (prefixed by group_ or service_ on which the key is authorized
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**client_name:** `str` — The name of the api key, for humans ;-)
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` — Whether or not the key is enabled. If disabled, resources won't be available to calls using this key
    
</dd>
</dl>

<dl>
<dd>

**daily_quota:** `typing.Optional[int]` — Authorized number of calls per day
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Bunch of metadata for the key
    
</dd>
</dl>

<dl>
<dd>

**monthly_quota:** `typing.Optional[int]` — Authorized number of calls per month
    
</dd>
</dl>

<dl>
<dd>

**throttling_quota:** `typing.Optional[int]` — Authorized number of calls per second, measured on 10 seconds
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">api_key_from_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an api key for a specified service group
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.api_key_from_group(
    group_id="groupId",
    client_id="clientId",
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

**group_id:** `str` — The api key group id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">update_api_key_from_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an api key for a specified service group
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.update_api_key_from_group(
    group_id="groupId",
    client_id_="clientId",
    authorized_entities=["a string value"],
    client_id="a string value",
    client_name="a string value",
    client_secret="a string value",
    enabled=True,
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

**group_id:** `str` — The api key group id
    
</dd>
</dl>

<dl>
<dd>

**client_id_:** `str` — the api key id
    
</dd>
</dl>

<dl>
<dd>

**authorized_entities:** `typing.Sequence[str]` — The group/service ids (prefixed by group_ or service_ on which the key is authorized
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**client_name:** `str` — The name of the api key, for humans ;-)
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` — Whether or not the key is enabled. If disabled, resources won't be available to calls using this key
    
</dd>
</dl>

<dl>
<dd>

**daily_quota:** `typing.Optional[int]` — Authorized number of calls per day
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Bunch of metadata for the key
    
</dd>
</dl>

<dl>
<dd>

**monthly_quota:** `typing.Optional[int]` — Authorized number of calls per month
    
</dd>
</dl>

<dl>
<dd>

**throttling_quota:** `typing.Optional[int]` — Authorized number of calls per second, measured on 10 seconds
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">delete_api_key_from_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an api key for a specified service group
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.delete_api_key_from_group(
    group_id="groupId",
    client_id="clientId",
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

**group_id:** `str` — The api key group id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">patch_api_key_from_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an api key for a specified service descriptor with a diff
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.patch_api_key_from_group(
    group_id="groupId",
    client_id="clientId",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**group_id:** `str` — The api key group id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">api_key_from_group_quotas</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the quota state of an api key
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.api_key_from_group_quotas(
    group_id="groupId",
    client_id="clientId",
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

**group_id:** `str` — The api key group id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">reset_api_key_from_group_quotas</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reset the quota state of an api key
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.reset_api_key_from_group_quotas(
    group_id="groupId",
    client_id="clientId",
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

**group_id:** `str` — The api key group id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">api_keys</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all api keys for the group of a service
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.api_keys(
    service_id="serviceId",
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

**service_id:** `str` — The api key service id
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">create_api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.create_api_key(
    service_id="serviceId",
    authorized_entities=["a string value"],
    client_id="a string value",
    client_name="a string value",
    client_secret="a string value",
    enabled=True,
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

**service_id:** `str` — The api key service id
    
</dd>
</dl>

<dl>
<dd>

**authorized_entities:** `typing.Sequence[str]` — The group/service ids (prefixed by group_ or service_ on which the key is authorized
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**client_name:** `str` — The name of the api key, for humans ;-)
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` — Whether or not the key is enabled. If disabled, resources won't be available to calls using this key
    
</dd>
</dl>

<dl>
<dd>

**daily_quota:** `typing.Optional[int]` — Authorized number of calls per day
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Bunch of metadata for the key
    
</dd>
</dl>

<dl>
<dd>

**monthly_quota:** `typing.Optional[int]` — Authorized number of calls per month
    
</dd>
</dl>

<dl>
<dd>

**throttling_quota:** `typing.Optional[int]` — Authorized number of calls per second, measured on 10 seconds
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an api key for a specified service descriptor
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.api_key(
    service_id="serviceId",
    client_id="clientId",
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

**service_id:** `str` — The api key service id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">update_api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an api key for a specified service descriptor
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.update_api_key(
    service_id="serviceId",
    client_id_="clientId",
    authorized_entities=["a string value"],
    client_id="a string value",
    client_name="a string value",
    client_secret="a string value",
    enabled=True,
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

**service_id:** `str` — The api key service id
    
</dd>
</dl>

<dl>
<dd>

**client_id_:** `str` — the api key id
    
</dd>
</dl>

<dl>
<dd>

**authorized_entities:** `typing.Sequence[str]` — The group/service ids (prefixed by group_ or service_ on which the key is authorized
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**client_name:** `str` — The name of the api key, for humans ;-)
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` — Whether or not the key is enabled. If disabled, resources won't be available to calls using this key
    
</dd>
</dl>

<dl>
<dd>

**daily_quota:** `typing.Optional[int]` — Authorized number of calls per day
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Bunch of metadata for the key
    
</dd>
</dl>

<dl>
<dd>

**monthly_quota:** `typing.Optional[int]` — Authorized number of calls per month
    
</dd>
</dl>

<dl>
<dd>

**throttling_quota:** `typing.Optional[int]` — Authorized number of calls per second, measured on 10 seconds
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">delete_api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an api key for a specified service descriptor
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.delete_api_key(
    service_id="serviceId",
    client_id="clientId",
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

**service_id:** `str` — The api key service id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">patch_api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an api key for a specified service descriptor with a diff
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.patch_api_key(
    service_id="serviceId",
    client_id="clientId",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**service_id:** `str` — The api key service id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">api_key_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the group of an api key
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.api_key_group(
    service_id="serviceId",
    client_id="clientId",
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

**service_id:** `str` — The api key service id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">api_key_quotas</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the quota state of an api key
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.api_key_quotas(
    service_id="serviceId",
    client_id="clientId",
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

**service_id:** `str` — The api key service id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
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

<details><summary><code>client.apikeys.<a href="src/fern/apikeys/client.py">reset_api_key_quotas</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reset the quota state of an api key
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.apikeys.reset_api_key_quotas(
    service_id="serviceId",
    client_id="clientId",
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

**service_id:** `str` — The api key service id
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — the api key id
    
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

## auth-config
<details><summary><code>client.auth_config.<a href="src/fern/auth_config/client.py">find_all_global_auth_modules</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all global auth. module configs
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.auth_config.find_all_global_auth_modules()

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

<details><summary><code>client.auth_config.<a href="src/fern/auth_config/client.py">create_global_auth_module</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one global auth. module config
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
from fern import FernApi, LdapAuthModuleConfig

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.auth_config.create_global_auth_module(
    request=LdapAuthModuleConfig(
        admin_password="a string value",
        admin_username="a string value",
        desc="a string value",
        email_field="a string value",
        group_filter="a string value",
        id="a string value",
        name="a string value",
        name_field="a string value",
        search_base="a string value",
        search_filter="a string value",
        server_url="a string value",
        session_max_age=123123,
        type="a string value",
        user_base="a string value",
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

**request:** `CreateGlobalAuthModuleRequest` 
    
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

<details><summary><code>client.auth_config.<a href="src/fern/auth_config/client.py">find_global_auth_module_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one global auth. module configs
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.auth_config.find_global_auth_module_by_id(
    id="id",
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

**id:** `str` — The auth. config id
    
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

<details><summary><code>client.auth_config.<a href="src/fern/auth_config/client.py">update_global_auth_module</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one global auth. module config
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
from fern import FernApi, LdapAuthModuleConfig

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.auth_config.update_global_auth_module(
    id="id",
    request=LdapAuthModuleConfig(
        admin_password="a string value",
        admin_username="a string value",
        desc="a string value",
        email_field="a string value",
        group_filter="a string value",
        id="a string value",
        name="a string value",
        name_field="a string value",
        search_base="a string value",
        search_filter="a string value",
        server_url="a string value",
        session_max_age=123123,
        type="a string value",
        user_base="a string value",
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

**id:** `str` — The auth. config id
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateGlobalAuthModuleRequestBody` 
    
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

<details><summary><code>client.auth_config.<a href="src/fern/auth_config/client.py">delete_global_auth_module</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one global auth. module config
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.auth_config.delete_global_auth_module(
    id="id",
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

**id:** `str` — The auth. config id id
    
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

<details><summary><code>client.auth_config.<a href="src/fern/auth_config/client.py">patch_global_auth_module</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one global auth. module config
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.auth_config.patch_global_auth_module(
    id="id",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**id:** `str` — The auth. config id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

## certificates
<details><summary><code>client.certificates.<a href="src/fern/certificates/client.py">all_certs</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all certificates
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.certificates.all_certs()

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

<details><summary><code>client.certificates.<a href="src/fern/certificates/client.py">create_cert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one certificate
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.certificates.create_cert(
    auto_renew="a string value",
    ca="a string value",
    ca_ref="a string value",
    chain="a string value",
    domain="a string value",
    from_="a string value",
    id="a string value",
    private_key="a string value",
    self_signed="a string value",
    subject="a string value",
    to="a string value",
    valid="a string value",
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

**auto_renew:** `str` — Allow Otoroshi to renew the certificate (if self signed)
    
</dd>
</dl>

<dl>
<dd>

**ca:** `str` — Certificate is a CA (read only)
    
</dd>
</dl>

<dl>
<dd>

**ca_ref:** `str` — Reference for a CA certificate in otoroshi
    
</dd>
</dl>

<dl>
<dd>

**chain:** `str` — Certificate chain of trust in PEM format
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Domain of the certificate (read only)
    
</dd>
</dl>

<dl>
<dd>

**from_:** `str` — Start date of validity
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Id of the certificate
    
</dd>
</dl>

<dl>
<dd>

**private_key:** `str` — PKCS8 private key in PEM format
    
</dd>
</dl>

<dl>
<dd>

**self_signed:** `str` — Certificate is self signed  read only)
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject of the certificate (read only)
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — End date of validity
    
</dd>
</dl>

<dl>
<dd>

**valid:** `str` — Certificate is valid (read only)
    
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

<details><summary><code>client.certificates.<a href="src/fern/certificates/client.py">one_cert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one certificate by id
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.certificates.one_cert(
    id="id",
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

**id:** `str` — The auth. config id
    
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

<details><summary><code>client.certificates.<a href="src/fern/certificates/client.py">put_cert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one certificate by id
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.certificates.put_cert(
    id_="id",
    auto_renew="a string value",
    ca="a string value",
    ca_ref="a string value",
    chain="a string value",
    domain="a string value",
    from_="a string value",
    id="a string value",
    private_key="a string value",
    self_signed="a string value",
    subject="a string value",
    to="a string value",
    valid="a string value",
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

**id_:** `str` — The certificate id
    
</dd>
</dl>

<dl>
<dd>

**auto_renew:** `str` — Allow Otoroshi to renew the certificate (if self signed)
    
</dd>
</dl>

<dl>
<dd>

**ca:** `str` — Certificate is a CA (read only)
    
</dd>
</dl>

<dl>
<dd>

**ca_ref:** `str` — Reference for a CA certificate in otoroshi
    
</dd>
</dl>

<dl>
<dd>

**chain:** `str` — Certificate chain of trust in PEM format
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — Domain of the certificate (read only)
    
</dd>
</dl>

<dl>
<dd>

**from_:** `str` — Start date of validity
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Id of the certificate
    
</dd>
</dl>

<dl>
<dd>

**private_key:** `str` — PKCS8 private key in PEM format
    
</dd>
</dl>

<dl>
<dd>

**self_signed:** `str` — Certificate is self signed  read only)
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject of the certificate (read only)
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — End date of validity
    
</dd>
</dl>

<dl>
<dd>

**valid:** `str` — Certificate is valid (read only)
    
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

<details><summary><code>client.certificates.<a href="src/fern/certificates/client.py">delete_cert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one certificate by id
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.certificates.delete_cert(
    id="id",
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

**id:** `str` — The certificate id
    
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

<details><summary><code>client.certificates.<a href="src/fern/certificates/client.py">patch_cert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one certificate by id
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.certificates.patch_cert(
    id="id",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**id:** `str` — The certificate id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

## validation-authorities
<details><summary><code>client.validation_authorities.<a href="src/fern/validation_authorities/client.py">find_all_client_validators</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all validation authoritiess
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.validation_authorities.find_all_client_validators()

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

<details><summary><code>client.validation_authorities.<a href="src/fern/validation_authorities/client.py">create_client_validator</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one validation authorities
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.validation_authorities.create_client_validator(
    always_valid=True,
    bad_ttl=123,
    description="a string value",
    good_ttl=123,
    headers={"key": "value"},
    host="a string value",
    id="a string value",
    method="a string value",
    name="a string value",
    no_cache=True,
    path="a string value",
    timeout=123,
    url="a string value",
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

**always_valid:** `bool` — Bypass http calls, every certificates are valids
    
</dd>
</dl>

<dl>
<dd>

**bad_ttl:** `int` — The TTL for invalid access response caching
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The description of the settings
    
</dd>
</dl>

<dl>
<dd>

**good_ttl:** `int` — The TTL for valid access response caching
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Dict[str, str]` — HTTP call headers
    
</dd>
</dl>

<dl>
<dd>

**host:** `str` — The host of the server
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The id of the settings
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` — The HTTP method
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the settings
    
</dd>
</dl>

<dl>
<dd>

**no_cache:** `bool` — Avoid caching responses
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — The URL path
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `int` — The call timeout
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL of the server
    
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

<details><summary><code>client.validation_authorities.<a href="src/fern/validation_authorities/client.py">find_client_validator_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one validation authorities by id
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.validation_authorities.find_client_validator_by_id(
    id="id",
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

**id:** `str` — The auth. config id
    
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

<details><summary><code>client.validation_authorities.<a href="src/fern/validation_authorities/client.py">update_client_validator</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one validation authorities by id
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.validation_authorities.update_client_validator(
    id_="id",
    always_valid=True,
    bad_ttl=123,
    description="a string value",
    good_ttl=123,
    headers={"key": "value"},
    host="a string value",
    id="a string value",
    method="a string value",
    name="a string value",
    no_cache=True,
    path="a string value",
    timeout=123,
    url="a string value",
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

**id_:** `str` — The validation authorities id
    
</dd>
</dl>

<dl>
<dd>

**always_valid:** `bool` — Bypass http calls, every certificates are valids
    
</dd>
</dl>

<dl>
<dd>

**bad_ttl:** `int` — The TTL for invalid access response caching
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The description of the settings
    
</dd>
</dl>

<dl>
<dd>

**good_ttl:** `int` — The TTL for valid access response caching
    
</dd>
</dl>

<dl>
<dd>

**headers:** `typing.Dict[str, str]` — HTTP call headers
    
</dd>
</dl>

<dl>
<dd>

**host:** `str` — The host of the server
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The id of the settings
    
</dd>
</dl>

<dl>
<dd>

**method:** `str` — The HTTP method
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the settings
    
</dd>
</dl>

<dl>
<dd>

**no_cache:** `bool` — Avoid caching responses
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — The URL path
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `int` — The call timeout
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL of the server
    
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

<details><summary><code>client.validation_authorities.<a href="src/fern/validation_authorities/client.py">delete_client_validator</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one validation authorities by id
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.validation_authorities.delete_client_validator(
    id="id",
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

**id:** `str` — The validation authorities id
    
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

<details><summary><code>client.validation_authorities.<a href="src/fern/validation_authorities/client.py">patch_client_validator</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one validation authorities by id
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.validation_authorities.patch_client_validator(
    id="id",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**id:** `str` — The validation authorities id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

## data-exporter-configs
<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">find_all_data_exporters</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all data exporter configs
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.find_all_data_exporters()

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

<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">create_data_exporter_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new data exporter config
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.create_data_exporter_config()

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

**buffer_size:** `typing.Optional[int]` — buffer size
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[DataExporterConfigConfig]` — Data Exporter config
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[str]` — Description
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[str]` — Boolean
    
</dd>
</dl>

<dl>
<dd>

**filtering:** `typing.Optional[Filtering]` — filtering
    
</dd>
</dl>

<dl>
<dd>

**group_duration:** `typing.Optional[int]` — duration
    
</dd>
</dl>

<dl>
<dd>

**group_size:** `typing.Optional[int]` — Group size
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Id
    
</dd>
</dl>

<dl>
<dd>

**json_workers:** `typing.Optional[int]` — nb workers
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[Location]` — location
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Metadata
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name
    
</dd>
</dl>

<dl>
<dd>

**projection:** `typing.Optional[typing.Dict[str, str]]` — projection
    
</dd>
</dl>

<dl>
<dd>

**send_workers:** `typing.Optional[int]` — send workers
    
</dd>
</dl>

<dl>
<dd>

**typ:** `typing.Optional[DataExporterConfigTyp]` — Type of data exporter
    
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

<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">create_bulk_data_exporter_configs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new data exporter configs
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.create_bulk_data_exporter_configs()

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

**buffer_size:** `typing.Optional[int]` — buffer size
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[DataExporterConfigConfig]` — Data Exporter config
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[str]` — Description
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[str]` — Boolean
    
</dd>
</dl>

<dl>
<dd>

**filtering:** `typing.Optional[Filtering]` — filtering
    
</dd>
</dl>

<dl>
<dd>

**group_duration:** `typing.Optional[int]` — duration
    
</dd>
</dl>

<dl>
<dd>

**group_size:** `typing.Optional[int]` — Group size
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Id
    
</dd>
</dl>

<dl>
<dd>

**json_workers:** `typing.Optional[int]` — nb workers
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[Location]` — location
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Metadata
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name
    
</dd>
</dl>

<dl>
<dd>

**projection:** `typing.Optional[typing.Dict[str, str]]` — projection
    
</dd>
</dl>

<dl>
<dd>

**send_workers:** `typing.Optional[int]` — send workers
    
</dd>
</dl>

<dl>
<dd>

**typ:** `typing.Optional[DataExporterConfigTyp]` — Type of data exporter
    
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

<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">update_bulk_data_exporter_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a data exporter configs
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.update_bulk_data_exporter_config()

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

**buffer_size:** `typing.Optional[int]` — buffer size
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[DataExporterConfigConfig]` — Data Exporter config
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[str]` — Description
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[str]` — Boolean
    
</dd>
</dl>

<dl>
<dd>

**filtering:** `typing.Optional[Filtering]` — filtering
    
</dd>
</dl>

<dl>
<dd>

**group_duration:** `typing.Optional[int]` — duration
    
</dd>
</dl>

<dl>
<dd>

**group_size:** `typing.Optional[int]` — Group size
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Id
    
</dd>
</dl>

<dl>
<dd>

**json_workers:** `typing.Optional[int]` — nb workers
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[Location]` — location
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Metadata
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name
    
</dd>
</dl>

<dl>
<dd>

**projection:** `typing.Optional[typing.Dict[str, str]]` — projection
    
</dd>
</dl>

<dl>
<dd>

**send_workers:** `typing.Optional[int]` — send workers
    
</dd>
</dl>

<dl>
<dd>

**typ:** `typing.Optional[DataExporterConfigTyp]` — Type of data exporter
    
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

<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">deletebulk_data_exporter_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a data exporter config
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.deletebulk_data_exporter_config(
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**request:** `Patch` 
    
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

<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">patch_bulk_data_exporter_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a data exporter configs with a diff
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.patch_bulk_data_exporter_config(
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**request:** `Patch` 
    
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

<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">data_exporter_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all data exporter configs
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.data_exporter_template()

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

**type:** `typing.Optional[str]` — The data exporter config type
    
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

<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">find_data_exporter_config_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a data exporter config
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.find_data_exporter_config_by_id(
    data_exporter_config_id="dataExporterConfigId",
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

**data_exporter_config_id:** `str` — The data exporter config id
    
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

<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">update_data_exporter_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a data exporter config
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.update_data_exporter_config(
    data_exporter_config_id="dataExporterConfigId",
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

**data_exporter_config_id:** `str` — The data exporter config id
    
</dd>
</dl>

<dl>
<dd>

**buffer_size:** `typing.Optional[int]` — buffer size
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[DataExporterConfigConfig]` — Data Exporter config
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Optional[str]` — Description
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[str]` — Boolean
    
</dd>
</dl>

<dl>
<dd>

**filtering:** `typing.Optional[Filtering]` — filtering
    
</dd>
</dl>

<dl>
<dd>

**group_duration:** `typing.Optional[int]` — duration
    
</dd>
</dl>

<dl>
<dd>

**group_size:** `typing.Optional[int]` — Group size
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Id
    
</dd>
</dl>

<dl>
<dd>

**json_workers:** `typing.Optional[int]` — nb workers
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[Location]` — location
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Metadata
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name
    
</dd>
</dl>

<dl>
<dd>

**projection:** `typing.Optional[typing.Dict[str, str]]` — projection
    
</dd>
</dl>

<dl>
<dd>

**send_workers:** `typing.Optional[int]` — send workers
    
</dd>
</dl>

<dl>
<dd>

**typ:** `typing.Optional[DataExporterConfigTyp]` — Type of data exporter
    
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

<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">delete_data_exporter_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a data exporter config
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.delete_data_exporter_config(
    data_exporter_config_id="dataExporterConfigId",
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

**data_exporter_config_id:** `str` — The data exporter config id
    
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

<details><summary><code>client.data_exporter_configs.<a href="src/fern/data_exporter_configs/client.py">patch_data_exporter_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a data exporter config with a diff
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.data_exporter_configs.patch_data_exporter_config(
    data_exporter_config_id="dataExporterConfigId",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**data_exporter_config_id:** `str` — The data exporter config id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

## configuration
<details><summary><code>client.configuration.<a href="src/fern/configuration/client.py">global_config</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the full configuration of Otoroshi
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.configuration.global_config()

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

<details><summary><code>client.configuration.<a href="src/fern/configuration/client.py">put_global_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the global configuration
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
from fern import FernApi, IpFiltering, Webhook

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.configuration.put_global_config(
    alerts_emails=["admin@otoroshi.io"],
    alerts_webhooks=[
        Webhook(
            headers={"key": "value"},
            url="http://www.google.com",
        )
    ],
    analytics_webhooks=[
        Webhook(
            headers={"key": "value"},
            url="http://www.google.com",
        )
    ],
    api_read_only=True,
    auto_link_to_default_group=True,
    endless_ip_addresses=["192.192.192.192"],
    ip_filtering=IpFiltering(
        blacklist=["192.192.192.192"],
        whitelist=["192.192.192.192"],
    ),
    limit_concurrent_requests=True,
    max_concurrent_requests=123,
    per_ip_throttling_quota=123,
    stream_entity_only=True,
    throttling_quota=123,
    u2f_login_only=True,
    use_circuit_breakers=True,
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

**alerts_emails:** `typing.Sequence[str]` — Email addresses that will receive all Otoroshi alert events
    
</dd>
</dl>

<dl>
<dd>

**alerts_webhooks:** `typing.Sequence[Webhook]` — Webhook that will receive all Otoroshi alert events
    
</dd>
</dl>

<dl>
<dd>

**analytics_webhooks:** `typing.Sequence[Webhook]` — Webhook that will receive all internal Otoroshi events
    
</dd>
</dl>

<dl>
<dd>

**api_read_only:** `bool` — If enabled, Admin API won't be able to write/update/delete entities
    
</dd>
</dl>

<dl>
<dd>

**auto_link_to_default_group:** `bool` — If not defined, every new service descriptor will be added to the default group
    
</dd>
</dl>

<dl>
<dd>

**endless_ip_addresses:** `typing.Sequence[str]` — IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros
    
</dd>
</dl>

<dl>
<dd>

**ip_filtering:** `IpFiltering` 
    
</dd>
</dl>

<dl>
<dd>

**limit_concurrent_requests:** `bool` — If enabled, Otoroshi will reject new request if too much at the same time
    
</dd>
</dl>

<dl>
<dd>

**max_concurrent_requests:** `int` — The number of authorized request processed at the same time
    
</dd>
</dl>

<dl>
<dd>

**per_ip_throttling_quota:** `int` — Authorized number of calls per second globally per IP address, measured on 10 seconds
    
</dd>
</dl>

<dl>
<dd>

**stream_entity_only:** `bool` — HTTP will be streamed only. Doesn't work with old browsers
    
</dd>
</dl>

<dl>
<dd>

**throttling_quota:** `int` — Authorized number of calls per second globally, measured on 10 seconds
    
</dd>
</dl>

<dl>
<dd>

**u2f_login_only:** `bool` — If enabled, login to backoffice through Auth0 will be disabled
    
</dd>
</dl>

<dl>
<dd>

**use_circuit_breakers:** `bool` — If enabled, services will be authorized to use circuit breakers
    
</dd>
</dl>

<dl>
<dd>

**backoffice_auth0config:** `typing.Optional[Auth0Config]` — Optional configuration for the backoffice Auth0 domain
    
</dd>
</dl>

<dl>
<dd>

**clever_settings:** `typing.Optional[CleverSettings]` — Optional CleverCloud configuration
    
</dd>
</dl>

<dl>
<dd>

**elastic_reads_config:** `typing.Optional[ElasticConfig]` — Config. for elastic reads
    
</dd>
</dl>

<dl>
<dd>

**elastic_writes_configs:** `typing.Optional[typing.Sequence[ElasticConfig]]` — Configs. for Elastic writes
    
</dd>
</dl>

<dl>
<dd>

**lines:** `typing.Optional[typing.Sequence[str]]` — Possibles lines for Otoroshi
    
</dd>
</dl>

<dl>
<dd>

**mailer_settings:** `typing.Optional[MailerSettings]` — Optional mailer configuration
    
</dd>
</dl>

<dl>
<dd>

**max_http10response_size:** `typing.Optional[int]` — The max size in bytes of an HTTP 1.0 response
    
</dd>
</dl>

<dl>
<dd>

**max_logs_size:** `typing.Optional[int]` — Number of events kept locally
    
</dd>
</dl>

<dl>
<dd>

**middle_fingers:** `typing.Optional[bool]` — Use middle finger emoji as a response character for endless HTTP responses
    
</dd>
</dl>

<dl>
<dd>

**private_apps_auth0config:** `typing.Optional[Auth0Config]` — Optional configuration for the private apps Auth0 domain
    
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

<details><summary><code>client.configuration.<a href="src/fern/configuration/client.py">patch_global_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the global configuration with a diff
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.configuration.patch_global_config(
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**request:** `Patch` 
    
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

## groups
<details><summary><code>client.groups.<a href="src/fern/groups/client.py">all_service_groups</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all service groups
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.groups.all_service_groups()

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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">create_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new service group
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.groups.create_group(
    id="a string value",
    name="a string value",
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

**id:** `str` — The unique id of the group. Usually 64 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the group
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The descriptoin of the group
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">service_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a service group
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.groups.service_group(
    service_group_id="serviceGroupId",
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

**service_group_id:** `str` — The service group id
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">update_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a service group
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.groups.update_group(
    service_group_id="serviceGroupId",
    id="a string value",
    name="a string value",
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

**service_group_id:** `str` — The service group id
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique id of the group. Usually 64 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the group
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The descriptoin of the group
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">delete_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a service group
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.groups.delete_group(
    service_group_id="serviceGroupId",
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

**service_group_id:** `str` — The service group id
    
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

<details><summary><code>client.groups.<a href="src/fern/groups/client.py">patch_group</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a service group with a diff
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.groups.patch_group(
    service_group_id="serviceGroupId",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**service_group_id:** `str` — The service group id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

## services
<details><summary><code>client.services.<a href="src/fern/services/client.py">service_group_services</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all services descriptor for a group
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.service_group_services(
    service_group_id="serviceGroupId",
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

**service_group_id:** `str` — The service group id
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">all_services</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all services
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.all_services()

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

<details><summary><code>client.services.<a href="src/fern/services/client.py">create_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new service descriptor
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
from fern import FernApi, Target

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.create_service(
    build_mode=True,
    domain="a string value",
    enabled=True,
    enforce_secure_communication=True,
    env="a string value",
    force_https=True,
    groups=["a string value"],
    id="110e8400-e29b-11d4-a716-446655440000",
    maintenance_mode=True,
    name="a string value",
    private_app=True,
    root="a string value",
    subdomain="a string value",
    targets=[
        Target(
            host="www.google.com",
            scheme="a string value",
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

**build_mode:** `bool` — Display a construction page when a user try to use the service
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — The domain on which the service is available.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` — Activate or deactivate your service. Once disabled, users will get an error page saying the service does not exist
    
</dd>
</dl>

<dl>
<dd>

**enforce_secure_communication:** `bool` — When enabled, Otoroshi will try to exchange headers with downstream service to ensure no one else can use the service from outside
    
</dd>
</dl>

<dl>
<dd>

**env:** `str` — The line on which the service is available. Based on that value, the name of the line will be appended to the subdomain. For line prod, nothing will be appended. For example, if the subdomain is 'foo' and line is 'preprod', then the exposed service will be available at 'foo.preprod.mydomain'
    
</dd>
</dl>

<dl>
<dd>

**force_https:** `bool` — Will force redirection to https:// if not present
    
</dd>
</dl>

<dl>
<dd>

**groups:** `typing.Sequence[str]` — Each service descriptor is attached to groups. A group can have one or more services. Each API key is linked to a group and allow access to every service in the group
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — A unique random string to identify your service
    
</dd>
</dl>

<dl>
<dd>

**maintenance_mode:** `bool` — Display a maintainance page when a user try to use the service
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of your service. Only for debug and human readability purposes
    
</dd>
</dl>

<dl>
<dd>

**private_app:** `bool` — When enabled, user will be allowed to use the service (UI) only if they are registered users of the private apps domain
    
</dd>
</dl>

<dl>
<dd>

**root:** `str` — Otoroshi will append this root to any target choosen. If the specified root is '/api/foo', then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar
    
</dd>
</dl>

<dl>
<dd>

**subdomain:** `str` — The subdomain on which the service is available
    
</dd>
</dl>

<dl>
<dd>

**targets:** `typing.Sequence[Target]` — The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures
    
</dd>
</dl>

<dl>
<dd>

**canary:** `typing.Optional[Canary]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_headers:** `typing.Optional[typing.Dict[str, str]]` — Specify headers that will be added to each client request. Useful to add authentication
    
</dd>
</dl>

<dl>
<dd>

**api:** `typing.Optional[ExposedApi]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_config_ref:** `typing.Optional[str]` — A reference to a global auth module config
    
</dd>
</dl>

<dl>
<dd>

**chaos_config:** `typing.Optional[ChaosConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**client_config:** `typing.Optional[ClientConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**client_validator_ref:** `typing.Optional[str]` — A reference to validation authority
    
</dd>
</dl>

<dl>
<dd>

**cors:** `typing.Optional[CorsSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**gzip:** `typing.Optional[Gzip]` 
    
</dd>
</dl>

<dl>
<dd>

**headers_verification:** `typing.Optional[typing.Dict[str, str]]` — Specify headers that will be verified after routing.
    
</dd>
</dl>

<dl>
<dd>

**health_check:** `typing.Optional[HealthCheck]` 
    
</dd>
</dl>

<dl>
<dd>

**ip_filtering:** `typing.Optional[IpFiltering]` 
    
</dd>
</dl>

<dl>
<dd>

**jwt_verifier:** `typing.Optional[ServiceJwtVerifier]` 
    
</dd>
</dl>

<dl>
<dd>

**local_host:** `typing.Optional[str]` — The host used localy, mainly localhost:xxxx
    
</dd>
</dl>

<dl>
<dd>

**local_scheme:** `typing.Optional[str]` — The scheme used localy, mainly http
    
</dd>
</dl>

<dl>
<dd>

**matching_headers:** `typing.Optional[typing.Dict[str, str]]` — Specify headers that MUST be present on client request to route it. Useful to implement versioning
    
</dd>
</dl>

<dl>
<dd>

**matching_root:** `typing.Optional[str]` — The root path on which the service is available
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Just a bunch of random properties
    
</dd>
</dl>

<dl>
<dd>

**override_host:** `typing.Optional[bool]` — Host header will be overriden with Host of the target
    
</dd>
</dl>

<dl>
<dd>

**private_patterns:** `typing.Optional[typing.Sequence[str]]` — If you define a public pattern that is a little bit too much, you can make some of public URL private again
    
</dd>
</dl>

<dl>
<dd>

**public_patterns:** `typing.Optional[typing.Sequence[str]]` — By default, every services are private only and you'll need an API key to access it. However, if you want to expose a public UI, you can define one or more public patterns (regex) to allow access to anybody. For example if you want to allow anybody on any URL, just use '/.*'
    
</dd>
</dl>

<dl>
<dd>

**redirect_to_local:** `typing.Optional[bool]` — If you work locally with Otoroshi, you may want to use that feature to redirect one particuliar service to a local host. For example, you can relocate https://foo.preprod.bar.com to http://localhost:8080 to make some tests
    
</dd>
</dl>

<dl>
<dd>

**redirection:** `typing.Optional[RedirectionSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**sec_com_excluded_patterns:** `typing.Optional[typing.Sequence[str]]` — URI patterns excluded from secured communications
    
</dd>
</dl>

<dl>
<dd>

**sec_com_settings:** `typing.Optional[ServiceSecComSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**send_otoroshi_headers_back:** `typing.Optional[bool]` — When enabled, Otoroshi will send headers to consumer like request id, client latency, overhead, etc ...
    
</dd>
</dl>

<dl>
<dd>

**statsd_config:** `typing.Optional[StatsdConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**transformer_ref:** `typing.Optional[str]` — A reference to a request transformer
    
</dd>
</dl>

<dl>
<dd>

**user_facing:** `typing.Optional[bool]` — The fact that this service will be seen by users and cannot be impacted by the Snow Monkey
    
</dd>
</dl>

<dl>
<dd>

**x_forwarded_headers:** `typing.Optional[bool]` — Send X-Forwarded-* headers
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a service descriptor
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.service(
    service_id="serviceId",
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

**service_id:** `str` — The service id
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">update_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a service descriptor
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
from fern import FernApi, Target

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.update_service(
    service_id="serviceId",
    build_mode=True,
    domain="a string value",
    enabled=True,
    enforce_secure_communication=True,
    env="a string value",
    force_https=True,
    groups=["a string value"],
    id="110e8400-e29b-11d4-a716-446655440000",
    maintenance_mode=True,
    name="a string value",
    private_app=True,
    root="a string value",
    subdomain="a string value",
    targets=[
        Target(
            host="www.google.com",
            scheme="a string value",
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

**service_id:** `str` — The service id
    
</dd>
</dl>

<dl>
<dd>

**build_mode:** `bool` — Display a construction page when a user try to use the service
    
</dd>
</dl>

<dl>
<dd>

**domain:** `str` — The domain on which the service is available.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` — Activate or deactivate your service. Once disabled, users will get an error page saying the service does not exist
    
</dd>
</dl>

<dl>
<dd>

**enforce_secure_communication:** `bool` — When enabled, Otoroshi will try to exchange headers with downstream service to ensure no one else can use the service from outside
    
</dd>
</dl>

<dl>
<dd>

**env:** `str` — The line on which the service is available. Based on that value, the name of the line will be appended to the subdomain. For line prod, nothing will be appended. For example, if the subdomain is 'foo' and line is 'preprod', then the exposed service will be available at 'foo.preprod.mydomain'
    
</dd>
</dl>

<dl>
<dd>

**force_https:** `bool` — Will force redirection to https:// if not present
    
</dd>
</dl>

<dl>
<dd>

**groups:** `typing.Sequence[str]` — Each service descriptor is attached to groups. A group can have one or more services. Each API key is linked to a group and allow access to every service in the group
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — A unique random string to identify your service
    
</dd>
</dl>

<dl>
<dd>

**maintenance_mode:** `bool` — Display a maintainance page when a user try to use the service
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of your service. Only for debug and human readability purposes
    
</dd>
</dl>

<dl>
<dd>

**private_app:** `bool` — When enabled, user will be allowed to use the service (UI) only if they are registered users of the private apps domain
    
</dd>
</dl>

<dl>
<dd>

**root:** `str` — Otoroshi will append this root to any target choosen. If the specified root is '/api/foo', then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar
    
</dd>
</dl>

<dl>
<dd>

**subdomain:** `str` — The subdomain on which the service is available
    
</dd>
</dl>

<dl>
<dd>

**targets:** `typing.Sequence[Target]` — The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures
    
</dd>
</dl>

<dl>
<dd>

**canary:** `typing.Optional[Canary]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_headers:** `typing.Optional[typing.Dict[str, str]]` — Specify headers that will be added to each client request. Useful to add authentication
    
</dd>
</dl>

<dl>
<dd>

**api:** `typing.Optional[ExposedApi]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_config_ref:** `typing.Optional[str]` — A reference to a global auth module config
    
</dd>
</dl>

<dl>
<dd>

**chaos_config:** `typing.Optional[ChaosConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**client_config:** `typing.Optional[ClientConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**client_validator_ref:** `typing.Optional[str]` — A reference to validation authority
    
</dd>
</dl>

<dl>
<dd>

**cors:** `typing.Optional[CorsSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**gzip:** `typing.Optional[Gzip]` 
    
</dd>
</dl>

<dl>
<dd>

**headers_verification:** `typing.Optional[typing.Dict[str, str]]` — Specify headers that will be verified after routing.
    
</dd>
</dl>

<dl>
<dd>

**health_check:** `typing.Optional[HealthCheck]` 
    
</dd>
</dl>

<dl>
<dd>

**ip_filtering:** `typing.Optional[IpFiltering]` 
    
</dd>
</dl>

<dl>
<dd>

**jwt_verifier:** `typing.Optional[ServiceJwtVerifier]` 
    
</dd>
</dl>

<dl>
<dd>

**local_host:** `typing.Optional[str]` — The host used localy, mainly localhost:xxxx
    
</dd>
</dl>

<dl>
<dd>

**local_scheme:** `typing.Optional[str]` — The scheme used localy, mainly http
    
</dd>
</dl>

<dl>
<dd>

**matching_headers:** `typing.Optional[typing.Dict[str, str]]` — Specify headers that MUST be present on client request to route it. Useful to implement versioning
    
</dd>
</dl>

<dl>
<dd>

**matching_root:** `typing.Optional[str]` — The root path on which the service is available
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, str]]` — Just a bunch of random properties
    
</dd>
</dl>

<dl>
<dd>

**override_host:** `typing.Optional[bool]` — Host header will be overriden with Host of the target
    
</dd>
</dl>

<dl>
<dd>

**private_patterns:** `typing.Optional[typing.Sequence[str]]` — If you define a public pattern that is a little bit too much, you can make some of public URL private again
    
</dd>
</dl>

<dl>
<dd>

**public_patterns:** `typing.Optional[typing.Sequence[str]]` — By default, every services are private only and you'll need an API key to access it. However, if you want to expose a public UI, you can define one or more public patterns (regex) to allow access to anybody. For example if you want to allow anybody on any URL, just use '/.*'
    
</dd>
</dl>

<dl>
<dd>

**redirect_to_local:** `typing.Optional[bool]` — If you work locally with Otoroshi, you may want to use that feature to redirect one particuliar service to a local host. For example, you can relocate https://foo.preprod.bar.com to http://localhost:8080 to make some tests
    
</dd>
</dl>

<dl>
<dd>

**redirection:** `typing.Optional[RedirectionSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**sec_com_excluded_patterns:** `typing.Optional[typing.Sequence[str]]` — URI patterns excluded from secured communications
    
</dd>
</dl>

<dl>
<dd>

**sec_com_settings:** `typing.Optional[ServiceSecComSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**send_otoroshi_headers_back:** `typing.Optional[bool]` — When enabled, Otoroshi will send headers to consumer like request id, client latency, overhead, etc ...
    
</dd>
</dl>

<dl>
<dd>

**statsd_config:** `typing.Optional[StatsdConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**transformer_ref:** `typing.Optional[str]` — A reference to a request transformer
    
</dd>
</dl>

<dl>
<dd>

**user_facing:** `typing.Optional[bool]` — The fact that this service will be seen by users and cannot be impacted by the Snow Monkey
    
</dd>
</dl>

<dl>
<dd>

**x_forwarded_headers:** `typing.Optional[bool]` — Send X-Forwarded-* headers
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">delete_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a service descriptor
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.delete_service(
    service_id="serviceId",
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

**service_id:** `str` — The service id
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">patch_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a service descriptor with a diff
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.patch_service(
    service_id="serviceId",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**service_id:** `str` — The service id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">service_targets</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a service descriptor targets
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.service_targets(
    service_id="serviceId",
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

**service_id:** `str` — The service id
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">service_add_target</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a target to a service descriptor
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.service_add_target(
    service_id="serviceId",
    host="www.google.com",
    scheme="a string value",
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

**service_id:** `str` — The service id
    
</dd>
</dl>

<dl>
<dd>

**host:** `str` — The host on which the HTTP call will be forwarded. Can be a domain name, or an IP address. Can also have a port
    
</dd>
</dl>

<dl>
<dd>

**scheme:** `str` — The protocol used for communication. Can be http or https
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">service_delete_target</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a service descriptor target
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.service_delete_target(
    service_id="serviceId",
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

**service_id:** `str` — The service id
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">update_service_targets</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a service descriptor targets
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.update_service_targets(
    service_id="serviceId",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**service_id:** `str` — The service id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">service_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a service descriptor error template
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.service_template(
    service_id="serviceId",
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

**service_id:** `str` — The service id
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">create_service_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a service descriptor targets
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.create_service_template(
    service_id_="serviceId",
    messages={"key": "value"},
    service_id="a string value",
    template40x="a string value",
    template50x="a string value",
    template_build="a string value",
    template_maintenance="a string value",
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

**service_id_:** `str` — The service id
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Dict[str, str]` — Map for custom messages
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — The Id of the service for which the error template is enabled
    
</dd>
</dl>

<dl>
<dd>

**template40x:** `str` — The html template for 40x errors
    
</dd>
</dl>

<dl>
<dd>

**template50x:** `str` — The html template for 50x errors
    
</dd>
</dl>

<dl>
<dd>

**template_build:** `str` — The html template for build page
    
</dd>
</dl>

<dl>
<dd>

**template_maintenance:** `str` — The html template for maintenance page
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">update_service_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an error template to a service descriptor
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.update_service_template(
    service_id_="serviceId",
    messages={"key": "value"},
    service_id="a string value",
    template40x="a string value",
    template50x="a string value",
    template_build="a string value",
    template_maintenance="a string value",
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

**service_id_:** `str` — The service id
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Dict[str, str]` — Map for custom messages
    
</dd>
</dl>

<dl>
<dd>

**service_id:** `str` — The Id of the service for which the error template is enabled
    
</dd>
</dl>

<dl>
<dd>

**template40x:** `str` — The html template for 40x errors
    
</dd>
</dl>

<dl>
<dd>

**template50x:** `str` — The html template for 50x errors
    
</dd>
</dl>

<dl>
<dd>

**template_build:** `str` — The html template for build page
    
</dd>
</dl>

<dl>
<dd>

**template_maintenance:** `str` — The html template for maintenance page
    
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

<details><summary><code>client.services.<a href="src/fern/services/client.py">delete_service_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a service descriptor error template
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.services.delete_service_template(
    service_id="serviceId",
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

**service_id:** `str` — The service id
    
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

## import
<details><summary><code>client.import_.<a href="src/fern/import_/client.py">full_import_from_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import the full state of Otoroshi as a file
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
import datetime

from fern import (
    FernApi,
    GlobalConfig,
    ImportExportAdminsItem,
    ImportExportApiKeysItem,
    ImportExportErrorTemplatesItem,
    ImportExportServiceDescriptorsItem,
    ImportExportServiceGroupsItem,
    ImportExportSimpleAdminsItem,
    ImportExportStats,
    IpFiltering,
    Target,
    Webhook,
)

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.import_.full_import_from_file(
    admins=[
        ImportExportAdminsItem(
            created_at=123,
            label="a string value",
            password="a string value",
            registration={"key": "value"},
            username="a string value",
        )
    ],
    api_keys=[
        ImportExportApiKeysItem(
            authorized_entities=["a string value"],
            client_id="a string value",
            client_name="a string value",
            client_secret="a string value",
            enabled=True,
        )
    ],
    config=GlobalConfig(
        alerts_emails=["admin@otoroshi.io"],
        alerts_webhooks=[
            Webhook(
                headers={"key": "value"},
                url="http://www.google.com",
            )
        ],
        analytics_webhooks=[
            Webhook(
                headers={"key": "value"},
                url="http://www.google.com",
            )
        ],
        api_read_only=True,
        auto_link_to_default_group=True,
        endless_ip_addresses=["192.192.192.192"],
        ip_filtering=IpFiltering(
            blacklist=["192.192.192.192"],
            whitelist=["192.192.192.192"],
        ),
        limit_concurrent_requests=True,
        max_concurrent_requests=123,
        per_ip_throttling_quota=123,
        stream_entity_only=True,
        throttling_quota=123,
        u2f_login_only=True,
        use_circuit_breakers=True,
    ),
    date=datetime.datetime.fromisoformat(
        "2017-07-21 17:32:28+00:00",
    ),
    date_raw=123,
    error_templates=[
        ImportExportErrorTemplatesItem(
            messages={"key": "value"},
            service_id="a string value",
            template40x="a string value",
            template50x="a string value",
            template_build="a string value",
            template_maintenance="a string value",
        )
    ],
    label="a string value",
    service_descriptors=[
        ImportExportServiceDescriptorsItem(
            build_mode=True,
            domain="a string value",
            enabled=True,
            enforce_secure_communication=True,
            env="a string value",
            force_https=True,
            groups=["a string value"],
            id="110e8400-e29b-11d4-a716-446655440000",
            maintenance_mode=True,
            name="a string value",
            private_app=True,
            root="a string value",
            subdomain="a string value",
            targets=[
                Target(
                    host="www.google.com",
                    scheme="a string value",
                )
            ],
        )
    ],
    service_groups=[
        ImportExportServiceGroupsItem(
            id="a string value",
            name="a string value",
        )
    ],
    simple_admins=[
        ImportExportSimpleAdminsItem(
            created_at=123,
            label="a string value",
            password="a string value",
            username="a string value",
        )
    ],
    stats=ImportExportStats(
        calls=123,
        data_in=123,
        data_out=123,
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

**admins:** `typing.Sequence[ImportExportAdminsItem]` — Current U2F admin at the time of export
    
</dd>
</dl>

<dl>
<dd>

**api_keys:** `typing.Sequence[ImportExportApiKeysItem]` — Current apik keys at the time of export
    
</dd>
</dl>

<dl>
<dd>

**config:** `GlobalConfig` — Current global config at the time of export
    
</dd>
</dl>

<dl>
<dd>

**date:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**date_raw:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**error_templates:** `typing.Sequence[ImportExportErrorTemplatesItem]` — Current error templates at the time of export
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**service_descriptors:** `typing.Sequence[ImportExportServiceDescriptorsItem]` — Current service descriptors at the time of export
    
</dd>
</dl>

<dl>
<dd>

**service_groups:** `typing.Sequence[ImportExportServiceGroupsItem]` — Current service groups at the time of export
    
</dd>
</dl>

<dl>
<dd>

**simple_admins:** `typing.Sequence[ImportExportSimpleAdminsItem]` — Current simple admins at the time of export
    
</dd>
</dl>

<dl>
<dd>

**stats:** `ImportExportStats` — Current global stats at the time of export
    
</dd>
</dl>

<dl>
<dd>

**app_config:** `typing.Optional[typing.Dict[str, str]]` — Current env variables at the time of export
    
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

<details><summary><code>client.import_.<a href="src/fern/import_/client.py">full_export</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export the full state of Otoroshi
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.import_.full_export()

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

<details><summary><code>client.import_.<a href="src/fern/import_/client.py">full_import</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import the full state of Otoroshi
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
import datetime

from fern import (
    FernApi,
    GlobalConfig,
    ImportExportAdminsItem,
    ImportExportApiKeysItem,
    ImportExportErrorTemplatesItem,
    ImportExportServiceDescriptorsItem,
    ImportExportServiceGroupsItem,
    ImportExportSimpleAdminsItem,
    ImportExportStats,
    IpFiltering,
    Target,
    Webhook,
)

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.import_.full_import(
    admins=[
        ImportExportAdminsItem(
            created_at=123,
            label="a string value",
            password="a string value",
            registration={"key": "value"},
            username="a string value",
        )
    ],
    api_keys=[
        ImportExportApiKeysItem(
            authorized_entities=["a string value"],
            client_id="a string value",
            client_name="a string value",
            client_secret="a string value",
            enabled=True,
        )
    ],
    config=GlobalConfig(
        alerts_emails=["admin@otoroshi.io"],
        alerts_webhooks=[
            Webhook(
                headers={"key": "value"},
                url="http://www.google.com",
            )
        ],
        analytics_webhooks=[
            Webhook(
                headers={"key": "value"},
                url="http://www.google.com",
            )
        ],
        api_read_only=True,
        auto_link_to_default_group=True,
        endless_ip_addresses=["192.192.192.192"],
        ip_filtering=IpFiltering(
            blacklist=["192.192.192.192"],
            whitelist=["192.192.192.192"],
        ),
        limit_concurrent_requests=True,
        max_concurrent_requests=123,
        per_ip_throttling_quota=123,
        stream_entity_only=True,
        throttling_quota=123,
        u2f_login_only=True,
        use_circuit_breakers=True,
    ),
    date=datetime.datetime.fromisoformat(
        "2017-07-21 17:32:28+00:00",
    ),
    date_raw=123,
    error_templates=[
        ImportExportErrorTemplatesItem(
            messages={"key": "value"},
            service_id="a string value",
            template40x="a string value",
            template50x="a string value",
            template_build="a string value",
            template_maintenance="a string value",
        )
    ],
    label="a string value",
    service_descriptors=[
        ImportExportServiceDescriptorsItem(
            build_mode=True,
            domain="a string value",
            enabled=True,
            enforce_secure_communication=True,
            env="a string value",
            force_https=True,
            groups=["a string value"],
            id="110e8400-e29b-11d4-a716-446655440000",
            maintenance_mode=True,
            name="a string value",
            private_app=True,
            root="a string value",
            subdomain="a string value",
            targets=[
                Target(
                    host="www.google.com",
                    scheme="a string value",
                )
            ],
        )
    ],
    service_groups=[
        ImportExportServiceGroupsItem(
            id="a string value",
            name="a string value",
        )
    ],
    simple_admins=[
        ImportExportSimpleAdminsItem(
            created_at=123,
            label="a string value",
            password="a string value",
            username="a string value",
        )
    ],
    stats=ImportExportStats(
        calls=123,
        data_in=123,
        data_out=123,
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

**admins:** `typing.Sequence[ImportExportAdminsItem]` — Current U2F admin at the time of export
    
</dd>
</dl>

<dl>
<dd>

**api_keys:** `typing.Sequence[ImportExportApiKeysItem]` — Current apik keys at the time of export
    
</dd>
</dl>

<dl>
<dd>

**config:** `GlobalConfig` — Current global config at the time of export
    
</dd>
</dl>

<dl>
<dd>

**date:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**date_raw:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**error_templates:** `typing.Sequence[ImportExportErrorTemplatesItem]` — Current error templates at the time of export
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**service_descriptors:** `typing.Sequence[ImportExportServiceDescriptorsItem]` — Current service descriptors at the time of export
    
</dd>
</dl>

<dl>
<dd>

**service_groups:** `typing.Sequence[ImportExportServiceGroupsItem]` — Current service groups at the time of export
    
</dd>
</dl>

<dl>
<dd>

**simple_admins:** `typing.Sequence[ImportExportSimpleAdminsItem]` — Current simple admins at the time of export
    
</dd>
</dl>

<dl>
<dd>

**stats:** `ImportExportStats` — Current global stats at the time of export
    
</dd>
</dl>

<dl>
<dd>

**app_config:** `typing.Optional[typing.Dict[str, str]]` — Current env variables at the time of export
    
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

## stats
<details><summary><code>client.stats.<a href="src/fern/stats/client.py">global_live_stats</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get global otoroshi stats
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.stats.global_live_stats()

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

<details><summary><code>client.stats.<a href="src/fern/stats/client.py">service_live_stats</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get live feed of global otoroshi stats (global) or for a service {id}
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.stats.service_live_stats(
    id="id",
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

**id:** `str` — The service id or global for otoroshi stats
    
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

## scripts
<details><summary><code>client.scripts.<a href="src/fern/scripts/client.py">find_all_scripts</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all scripts
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.scripts.find_all_scripts()

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

<details><summary><code>client.scripts.<a href="src/fern/scripts/client.py">create_script</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new script
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.scripts.create_script(
    code={"key": "value"},
    desc={"key": "value"},
    id="a string value",
    name="a string value",
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

**code:** `typing.Dict[str, str]` — The code of the script
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Dict[str, str]` — The description of the script
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The id of the script
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the script
    
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

<details><summary><code>client.scripts.<a href="src/fern/scripts/client.py">compile_script</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compile a script
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.scripts.compile_script(
    code={"key": "value"},
    desc={"key": "value"},
    id="a string value",
    name="a string value",
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

**code:** `typing.Dict[str, str]` — The code of the script
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Dict[str, str]` — The description of the script
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The id of the script
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the script
    
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

<details><summary><code>client.scripts.<a href="src/fern/scripts/client.py">find_script_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a script
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.scripts.find_script_by_id(
    script_id="scriptId",
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

**script_id:** `str` — The script id
    
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

<details><summary><code>client.scripts.<a href="src/fern/scripts/client.py">update_script</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a script
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.scripts.update_script(
    script_id="scriptId",
    code={"key": "value"},
    desc={"key": "value"},
    id="a string value",
    name="a string value",
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

**script_id:** `str` — The script id
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Dict[str, str]` — The code of the script
    
</dd>
</dl>

<dl>
<dd>

**desc:** `typing.Dict[str, str]` — The description of the script
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The id of the script
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the script
    
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

<details><summary><code>client.scripts.<a href="src/fern/scripts/client.py">delete_script</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a script
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.scripts.delete_script(
    script_id="scriptId",
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

**script_id:** `str` — The script id
    
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

<details><summary><code>client.scripts.<a href="src/fern/scripts/client.py">patch_script</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a script with a diff
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.scripts.patch_script(
    script_id="scriptId",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**script_id:** `str` — The script id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

## snowmonkey
<details><summary><code>client.snowmonkey.<a href="src/fern/snowmonkey/client.py">start_snow_monkey</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start the Snow Monkey
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.snowmonkey.start_snow_monkey()

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

<details><summary><code>client.snowmonkey.<a href="src/fern/snowmonkey/client.py">stop_snow_monkey</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop the Snow Monkey
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.snowmonkey.stop_snow_monkey()

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

<details><summary><code>client.snowmonkey.<a href="src/fern/snowmonkey/client.py">get_snow_monkey_config</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current Snow Monkey config
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.snowmonkey.get_snow_monkey_config()

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

<details><summary><code>client.snowmonkey.<a href="src/fern/snowmonkey/client.py">update_snow_monkey</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update current Snow Monkey config
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.snowmonkey.update_snow_monkey(
    id="a string value",
    name="a string value",
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

**id:** `str` — The unique id of the group. Usually 64 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the group
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The descriptoin of the group
    
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

<details><summary><code>client.snowmonkey.<a href="src/fern/snowmonkey/client.py">patch_snow_monkey</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update current Snow Monkey config
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.snowmonkey.patch_snow_monkey(
    id="a string value",
    name="a string value",
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

**id:** `str` — The unique id of the group. Usually 64 random alpha numerical characters, but can be anything
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the group
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The descriptoin of the group
    
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

<details><summary><code>client.snowmonkey.<a href="src/fern/snowmonkey/client.py">get_snow_monkey_outages</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all current Snow Monkey ourages
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.snowmonkey.get_snow_monkey_outages()

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

<details><summary><code>client.snowmonkey.<a href="src/fern/snowmonkey/client.py">reset_snow_monkey</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reset Snow Monkey Outages for the day
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.snowmonkey.reset_snow_monkey()

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

## jwt-verifiers
<details><summary><code>client.jwt_verifiers.<a href="src/fern/jwt_verifiers/client.py">find_all_global_jwt_verifiers</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all global JWT verifiers
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.jwt_verifiers.find_all_global_jwt_verifiers()

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

<details><summary><code>client.jwt_verifiers.<a href="src/fern/jwt_verifiers/client.py">create_global_jwt_verifier</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create one global JWT verifiers
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
from fern import (
    FernApi,
    HsAlgoSettings,
    InQueryParam,
    PassThrough,
    VerificationSettings,
)

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.jwt_verifiers.create_global_jwt_verifier(
    algo_settings=HsAlgoSettings(
        secret="a string value",
        size=123123,
        type="a string value",
    ),
    desc="a string value",
    enabled=True,
    id="a string value",
    name="a string value",
    source=InQueryParam(
        name="a string value",
        type="a string value",
    ),
    strategy=PassThrough(
        type="a string value",
        verification_settings=VerificationSettings(
            fields={"key": "value"},
        ),
    ),
    strict=True,
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

**algo_settings:** `GlobalJwtVerifierAlgoSettings` 
    
</dd>
</dl>

<dl>
<dd>

**desc:** `str` — Verifier description
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` — Is it enabled
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Verifier id
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Verifier name
    
</dd>
</dl>

<dl>
<dd>

**source:** `GlobalJwtVerifierSource` 
    
</dd>
</dl>

<dl>
<dd>

**strategy:** `GlobalJwtVerifierStrategy` 
    
</dd>
</dl>

<dl>
<dd>

**strict:** `bool` — Does it fail if JWT not found
    
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

<details><summary><code>client.jwt_verifiers.<a href="src/fern/jwt_verifiers/client.py">find_global_jwt_verifiers_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one global JWT verifiers
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.jwt_verifiers.find_global_jwt_verifiers_by_id(
    verifier_id="verifierId",
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

**verifier_id:** `str` — The jwt verifier id
    
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

<details><summary><code>client.jwt_verifiers.<a href="src/fern/jwt_verifiers/client.py">update_global_jwt_verifier</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one global JWT verifiers
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
from fern import (
    FernApi,
    HsAlgoSettings,
    InQueryParam,
    PassThrough,
    VerificationSettings,
)

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.jwt_verifiers.update_global_jwt_verifier(
    verifier_id="verifierId",
    algo_settings=HsAlgoSettings(
        secret="a string value",
        size=123123,
        type="a string value",
    ),
    desc="a string value",
    enabled=True,
    id="a string value",
    name="a string value",
    source=InQueryParam(
        name="a string value",
        type="a string value",
    ),
    strategy=PassThrough(
        type="a string value",
        verification_settings=VerificationSettings(
            fields={"key": "value"},
        ),
    ),
    strict=True,
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

**verifier_id:** `str` — The jwt verifier id
    
</dd>
</dl>

<dl>
<dd>

**algo_settings:** `GlobalJwtVerifierAlgoSettings` 
    
</dd>
</dl>

<dl>
<dd>

**desc:** `str` — Verifier description
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `bool` — Is it enabled
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Verifier id
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Verifier name
    
</dd>
</dl>

<dl>
<dd>

**source:** `GlobalJwtVerifierSource` 
    
</dd>
</dl>

<dl>
<dd>

**strategy:** `GlobalJwtVerifierStrategy` 
    
</dd>
</dl>

<dl>
<dd>

**strict:** `bool` — Does it fail if JWT not found
    
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

<details><summary><code>client.jwt_verifiers.<a href="src/fern/jwt_verifiers/client.py">delete_global_jwt_verifier</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete one global JWT verifiers
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.jwt_verifiers.delete_global_jwt_verifier(
    verifier_id="verifierId",
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

**verifier_id:** `str` — The jwt verifier id
    
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

<details><summary><code>client.jwt_verifiers.<a href="src/fern/jwt_verifiers/client.py">patch_global_jwt_verifier</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update one global JWT verifiers
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
from fern import FernApi, PatchItem, PatchItemOp

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.jwt_verifiers.patch_global_jwt_verifier(
    verifier_id="verifierId",
    request=[
        PatchItem(
            op=PatchItemOp.ADD,
            path="a string value",
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

**verifier_id:** `str` — The jwt verifier id
    
</dd>
</dl>

<dl>
<dd>

**request:** `Patch` 
    
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

## environments
<details><summary><code>client.environments.<a href="src/fern/environments/client.py">all_lines</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all environments provided by the current Otoroshi instance
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.environments.all_lines()

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

<details><summary><code>client.environments.<a href="src/fern/environments/client.py">services_for_a_line</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all services for an environment provided by the current Otoroshi instance
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.environments.services_for_a_line(
    line="line",
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

**line:** `str` — The environment where to find services
    
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

## templates
<details><summary><code>client.templates.<a href="src/fern/templates/client.py">initiate_api_key</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a template of an Otoroshi Api Key. The generated entity is not persisted
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.templates.initiate_api_key()

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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">initiate_service_group</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a template of an Otoroshi service group. The generated entity is not persisted
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.templates.initiate_service_group()

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

<details><summary><code>client.templates.<a href="src/fern/templates/client.py">initiate_service</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a template of an Otoroshi service descriptor. The generated entity is not persisted
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
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.templates.initiate_service()

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

