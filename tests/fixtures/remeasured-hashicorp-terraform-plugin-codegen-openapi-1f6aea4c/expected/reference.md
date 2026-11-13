# Reference
<details><summary><code>client.<a href="src/fern/client.py#L107-L131">test_for_objects_that_have_no_types</a>() -> GetObjNoTypeResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.test_for_objects_that_have_no_types()

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

<details><summary><code>client.<a href="src/fern/client.py#L133-L159">test_for_nested_collections_list_within_a_list_set_within_a_list_map_within_a_list</a>() -> GetNestedCollectionsResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.test_for_nested_collections_list_within_a_list_set_within_a_list_map_within_a_list()

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

<details><summary><code>client.<a href="src/fern/client.py#L161-L187">test_for_map_nested_attributes_and_map_attributes_in_a_data_source</a>() -> GetMapTestResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.test_for_map_nested_attributes_and_map_attributes_in_a_data_source()

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

<details><summary><code>client.<a href="src/fern/client.py#L189-L235">test_for_map_nested_attributes_and_map_attributes_in_a_resource</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MapnestedSchemaValue

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.test_for_map_nested_attributes_and_map_attributes_in_a_resource(
    mapnested_prop={
        "key": MapnestedSchemaValue()
    },
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

**mapnested_prop:** `MapnestedSchema` 
    
</dd>
</dl>

<dl>
<dd>

**mapnested_nullable:** `typing.Optional[MapnestedAllofOneofNullable]` 
    
</dd>
</dl>

<dl>
<dd>

**map_prop:** `typing.Optional[typing.Dict[str, str]]` — This is a map of strings
    
</dd>
</dl>

<dl>
<dd>

**map_stringified:** `typing.Optional[MapAllofOneofStringified]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py#L237-L263">test_for_set_nested_attributes_and_set_attributes_in_a_data_source</a>() -> GetSetTestResponse</code></summary>
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
    base_url="https://yourhost.com/path/to/api",
)

client.test_for_set_nested_attributes_and_set_attributes_in_a_data_source()

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

<details><summary><code>client.<a href="src/fern/client.py#L265-L301">test_for_set_nested_attributes_and_set_attributes_in_a_resource</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SetnestedSchemaItem

client = FernApi(
    base_url="https://yourhost.com/path/to/api",
)

client.test_for_set_nested_attributes_and_set_attributes_in_a_resource(
    setnested_prop=[
        SetnestedSchemaItem()
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

**setnested_prop:** `SetnestedSchema` 
    
</dd>
</dl>

<dl>
<dd>

**set_prop:** `typing.Optional[typing.List[str]]` — This is a set of strings
    
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

