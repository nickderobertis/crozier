# Reference
<details><summary><code>client.<a href="src/fern/client.py">post_graph_ql</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs a GraphQL Query
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
client.post_graph_ql(
    query="query",
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

**query:** `str` — The GraphQL query
    
</dd>
</dl>

<dl>
<dd>

**operation_name:** `typing.Optional[str]` — If the Query contains several named operations, the operationName controls which one should be executed
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional Query variables
    
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

<details><summary><code>client.<a href="src/fern/client.py">get_documentation</a>()</code></summary>
<dl>
<dd>

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
client.get_documentation()

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

## ServiceCredentialType
<details><summary><code>client.service_credential_type.<a href="src/fern/service_credential_type/client.py">list_service_credential_types</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceCredentialType objects
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
client.service_credential_type.list_service_credential_types()

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

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.service_credential_type.<a href="src/fern/service_credential_type/client.py">show_service_credential_type</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a ServiceCredentialType object
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
client.service_credential_type.show_service_credential_type(
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

**id:** `str` — ID of the resource
    
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

## ServiceCredential
<details><summary><code>client.service_credential.<a href="src/fern/service_credential/client.py">list_service_credentials</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceCredential objects
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
client.service_credential.list_service_credentials()

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

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.service_credential.<a href="src/fern/service_credential/client.py">show_service_credential</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a ServiceCredential object
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
client.service_credential.show_service_credential(
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

**id:** `str` — ID of the resource
    
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

## ServiceInstance
<details><summary><code>client.service_instance.<a href="src/fern/service_instance/client.py">list_service_instances</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceInstance objects
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
client.service_instance.list_service_instances()

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

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.service_instance.<a href="src/fern/service_instance/client.py">show_service_instance</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a ServiceInstance object
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
client.service_instance.show_service_instance(
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

**id:** `str` — ID of the resource
    
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

## ServiceInventory
<details><summary><code>client.service_inventory.<a href="src/fern/service_inventory/client.py">list_service_inventories</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceInventory objects
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
client.service_inventory.list_service_inventories()

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

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.service_inventory.<a href="src/fern/service_inventory/client.py">show_service_inventory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a ServiceInventory object
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
client.service_inventory.show_service_inventory(
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

**id:** `str` — ID of the resource
    
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

<details><summary><code>client.service_inventory.<a href="src/fern/service_inventory/client.py">tag_service_inventory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tags a ServiceInventory object
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
from fern import FernApi, Tag

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.service_inventory.tag_service_inventory(
    id="id",
    request=[Tag()],
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[Tag]` 
    
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

<details><summary><code>client.service_inventory.<a href="src/fern/service_inventory/client.py">list_service_inventory_tags</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of Tag objects
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
client.service_inventory.list_service_inventory_tags(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.service_inventory.<a href="src/fern/service_inventory/client.py">untag_service_inventory</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Untags a ServiceInventory object
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
from fern import FernApi, Tag

client = FernApi(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
)
client.service_inventory.untag_service_inventory(
    id="id",
    request=[Tag()],
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[Tag]` 
    
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

## ServiceOfferingNode
<details><summary><code>client.service_offering_node.<a href="src/fern/service_offering_node/client.py">list_service_offering_nodes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceOfferingNode objects
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
client.service_offering_node.list_service_offering_nodes()

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

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.service_offering_node.<a href="src/fern/service_offering_node/client.py">show_service_offering_node</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a ServiceOfferingNode object
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
client.service_offering_node.show_service_offering_node(
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

**id:** `str` — ID of the resource
    
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

## ServiceOffering
<details><summary><code>client.service_offering.<a href="src/fern/service_offering/client.py">list_service_offerings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceOffering objects
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
client.service_offering.list_service_offerings()

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

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.service_offering.<a href="src/fern/service_offering/client.py">show_service_offering</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a ServiceOffering object
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
client.service_offering.show_service_offering(
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

**id:** `str` — ID of the resource
    
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

<details><summary><code>client.service_offering.<a href="src/fern/service_offering/client.py">applied_inventories_tags_for_service_offering</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of inventories tags
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
client.service_offering.applied_inventories_tags_for_service_offering(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**service_parameters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The provider specific parameters needed to compute list of used service inventories
    
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

<details><summary><code>client.service_offering.<a href="src/fern/service_offering/client.py">order_service_offering</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a Task id
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
client.service_offering.order_service_offering(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**provider_control_parameters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The provider specific parameters needed to provision this service. This might include namespaces, special keys
    
</dd>
</dl>

<dl>
<dd>

**service_parameters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — JSON object with provisioning parameters
    
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

<details><summary><code>client.service_offering.<a href="src/fern/service_offering/client.py">list_service_offering_service_instances</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceInstance objects
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
client.service_offering.list_service_offering_service_instances(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.service_offering.<a href="src/fern/service_offering/client.py">list_service_offering_service_offering_nodes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceOfferingNode objects
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
client.service_offering.list_service_offering_service_offering_nodes(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.service_offering.<a href="src/fern/service_offering/client.py">list_service_offering_service_plans</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServicePlan objects
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
client.service_offering.list_service_offering_service_plans(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

## ServicePlan
<details><summary><code>client.service_plan.<a href="src/fern/service_plan/client.py">list_service_plans</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServicePlan objects
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
client.service_plan.list_service_plans()

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

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.service_plan.<a href="src/fern/service_plan/client.py">show_service_plan</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a ServicePlan object
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
client.service_plan.show_service_plan(
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

**id:** `str` — ID of the resource
    
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

## Source
<details><summary><code>client.source.<a href="src/fern/source/client.py">list_sources</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of Source objects
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
client.source.list_sources()

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

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.source.<a href="src/fern/source/client.py">show_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a Source object
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
client.source.show_source(
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

**id:** `str` — ID of the resource
    
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

<details><summary><code>client.source.<a href="src/fern/source/client.py">incremental_refresh_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Incremental Refresh a source object
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
client.source.incremental_refresh_source(
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

**id:** `str` — ID of the resource
    
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

<details><summary><code>client.source.<a href="src/fern/source/client.py">refresh_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refresh a source object
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
client.source.refresh_source(
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

**id:** `str` — ID of the resource
    
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

<details><summary><code>client.source.<a href="src/fern/source/client.py">list_source_service_instances</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceInstance objects
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
client.source.list_source_service_instances(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.source.<a href="src/fern/source/client.py">list_source_service_inventories</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceInventory objects
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
client.source.list_source_service_inventories(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.source.<a href="src/fern/source/client.py">list_source_service_offering_nodes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceOfferingNode objects
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
client.source.list_source_service_offering_nodes(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.source.<a href="src/fern/source/client.py">list_source_service_offerings</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServiceOffering objects
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
client.source.list_source_service_offerings(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.source.<a href="src/fern/source/client.py">list_source_service_plans</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of ServicePlan objects
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
client.source.list_source_service_plans(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.source.<a href="src/fern/source/client.py">list_source_tasks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of Task objects
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
client.source.list_source_tasks(
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

**id:** `str` — ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

## Tags
<details><summary><code>client.tags.<a href="src/fern/tags/client.py">list_tags</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of Tag objects
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
client.tags.list_tags()

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

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

## Task
<details><summary><code>client.task.<a href="src/fern/task/client.py">list_tasks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an array of Task objects
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
client.task.list_tasks()

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

**limit:** `typing.Optional[int]` — The numbers of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The number of items to skip before starting to collect the result set.
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Filter for querying collections.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The list of attribute and order to sort the result set by.
    
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

<details><summary><code>client.task.<a href="src/fern/task/client.py">show_task</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a Task object
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
client.task.show_task(
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

**id:** `str` — UUID of task
    
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

<details><summary><code>client.task.<a href="src/fern/task/client.py">update_task</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a Task object
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
client.task.update_task(
    id_="id",
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

**id_:** `str` — UUID of task
    
</dd>
</dl>

<dl>
<dd>

**archived_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**child_task_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**completed_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**controller_message_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[Uuid]` 
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[Id]` 
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[TaskState]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TaskStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**target_source_ref:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**target_type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` 
    
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

