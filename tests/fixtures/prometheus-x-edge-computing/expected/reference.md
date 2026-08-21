# Reference
## customerAPI
<details><summary><code>client.customer_api.<a href="src/fern/customer_api/client.py">request_edge_proc</a>(...) -> ExecutionResult</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.customer_api.request_edge_proc()

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

**function:** `typing.Optional[FunctionId]` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[DataId]` 
    
</dd>
</dl>

<dl>
<dd>

**data_contract:** `typing.Optional[ContractId]` 
    
</dd>
</dl>

<dl>
<dd>

**func_contract:** `typing.Optional[ContractId]` 
    
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

<details><summary><code>client.customer_api.<a href="src/fern/customer_api/client.py">request_privacy_edge_proc</a>(...) -> PrivateExecutionResult</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.customer_api.request_privacy_edge_proc()

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

**function:** `typing.Optional[FunctionId]` 
    
</dd>
</dl>

<dl>
<dd>

**private_data:** `typing.Optional[DataId]` 
    
</dd>
</dl>

<dl>
<dd>

**data_contract:** `typing.Optional[ContractId]` 
    
</dd>
</dl>

<dl>
<dd>

**func_contract:** `typing.Optional[ContractId]` 
    
</dd>
</dl>

<dl>
<dd>

**consent:** `typing.Optional[ConsentId]` 
    
</dd>
</dl>

<dl>
<dd>

**token:** `typing.Optional[AccessToken]` 
    
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

## connectorAPI
<details><summary><code>client.connector_api.<a href="src/fern/connector_api/client.py">get_pz_data</a>(...) -> PrivacyZoneData</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.connector_api.get_pz_data()

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

**data_provider:** `typing.Optional[DataProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**private_data:** `typing.Optional[DataId]` 
    
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

<details><summary><code>client.connector_api.<a href="src/fern/connector_api/client.py">request_function</a>(...) -> Function</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.connector_api.request_function()

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

**function:** `typing.Optional[FunctionId]` 
    
</dd>
</dl>

<dl>
<dd>

**func_contract:** `typing.Optional[ContractId]` 
    
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

<details><summary><code>client.connector_api.<a href="src/fern/connector_api/client.py">request_privacy_preserving_data</a>(...) -> PrivateData</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.connector_api.request_privacy_preserving_data()

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

**private_data:** `typing.Optional[DataId]` 
    
</dd>
</dl>

<dl>
<dd>

**data_contract:** `typing.Optional[ContractId]` 
    
</dd>
</dl>

<dl>
<dd>

**consent:** `typing.Optional[ConsentId]` 
    
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

