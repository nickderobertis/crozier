# Reference
## EndpointsContainer
<details><summary><code>client.endpoints_container.<a href="src/fern/endpoints_container/client.py">endpoints_container_get_and_return_list_of_primitives</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_container.endpoints_container_get_and_return_list_of_primitives(
    request=["string"],
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

**request:** `typing.Sequence[str]` 
    
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

<details><summary><code>client.endpoints_container.<a href="src/fern/endpoints_container/client.py">endpoints_container_get_and_return_list_of_objects</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TypesObjectWithRequiredField

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_container.endpoints_container_get_and_return_list_of_objects(
    request=[
        TypesObjectWithRequiredField(
            string="string",
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

**request:** `typing.Sequence[TypesObjectWithRequiredField]` 
    
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

<details><summary><code>client.endpoints_container.<a href="src/fern/endpoints_container/client.py">endpoints_container_get_and_return_set_of_primitives</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_container.endpoints_container_get_and_return_set_of_primitives(
    request=["string"],
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

**request:** `typing.Sequence[str]` 
    
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

<details><summary><code>client.endpoints_container.<a href="src/fern/endpoints_container/client.py">endpoints_container_get_and_return_set_of_objects</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TypesObjectWithRequiredField

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_container.endpoints_container_get_and_return_set_of_objects(
    request=[
        TypesObjectWithRequiredField(
            string="string",
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

**request:** `typing.Sequence[TypesObjectWithRequiredField]` 
    
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

<details><summary><code>client.endpoints_container.<a href="src/fern/endpoints_container/client.py">endpoints_container_get_and_return_map_prim_to_prim</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_container.endpoints_container_get_and_return_map_prim_to_prim(
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

**request:** `typing.Dict[str, str]` 
    
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

<details><summary><code>client.endpoints_container.<a href="src/fern/endpoints_container/client.py">endpoints_container_get_and_return_map_of_prim_to_object</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TypesObjectWithRequiredField

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_container.endpoints_container_get_and_return_map_of_prim_to_object(
    request={
        "key": TypesObjectWithRequiredField(
            string="string",
        )
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

**request:** `typing.Dict[str, TypesObjectWithRequiredField]` 
    
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

<details><summary><code>client.endpoints_container.<a href="src/fern/endpoints_container/client.py">endpoints_container_get_and_return_map_of_prim_to_undiscriminated_union</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_container.endpoints_container_get_and_return_map_of_prim_to_undiscriminated_union(
    request={"key": 1.1},
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

**request:** `typing.Dict[str, TypesMixedType]` 
    
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

<details><summary><code>client.endpoints_container.<a href="src/fern/endpoints_container/client.py">endpoints_container_get_and_return_optional</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_container.endpoints_container_get_and_return_optional(
    string="string",
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

**string:** `str` 
    
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

## EndpointsContentType
<details><summary><code>client.endpoints_content_type.<a href="src/fern/endpoints_content_type/client.py">endpoints_content_type_post_json_patch_content_type</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_content_type.endpoints_content_type_post_json_patch_content_type()

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

**string:** `typing.Optional[str]` — This is a rather long descriptor of this single field in a more complex type. If you ask me I think this is a pretty good description for this field all things considered.
    
</dd>
</dl>

<dl>
<dd>

**integer:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**long_:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**double:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bool_:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**datetime:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[dt.date]` 
    
</dd>
</dl>

<dl>
<dd>

**uuid_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**base64:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**list_:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**set_:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**map_:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**bigint:** `typing.Optional[int]` 
    
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

<details><summary><code>client.endpoints_content_type.<a href="src/fern/endpoints_content_type/client.py">endpoints_content_type_post_json_patch_content_with_charset_type</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_content_type.endpoints_content_type_post_json_patch_content_with_charset_type()

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

**string:** `typing.Optional[str]` — This is a rather long descriptor of this single field in a more complex type. If you ask me I think this is a pretty good description for this field all things considered.
    
</dd>
</dl>

<dl>
<dd>

**integer:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**long_:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**double:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bool_:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**datetime:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[dt.date]` 
    
</dd>
</dl>

<dl>
<dd>

**uuid_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**base64:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**list_:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**set_:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**map_:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**bigint:** `typing.Optional[int]` 
    
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

## EndpointsEnum
<details><summary><code>client.endpoints_enum.<a href="src/fern/endpoints_enum/client.py">endpoints_enum_get_and_return_enum</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TypesWeatherReport

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_enum.endpoints_enum_get_and_return_enum(
    request=TypesWeatherReport.SUNNY,
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

**request:** `TypesWeatherReport` 
    
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

## EndpointsHttpMethods
<details><summary><code>client.endpoints_http_methods.<a href="src/fern/endpoints_http_methods/client.py">endpoints_http_methods_test_get</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_http_methods.endpoints_http_methods_test_get(
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

**id:** `str` 
    
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

<details><summary><code>client.endpoints_http_methods.<a href="src/fern/endpoints_http_methods/client.py">endpoints_http_methods_test_put</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_http_methods.endpoints_http_methods_test_put(
    id="id",
    string="string",
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**string:** `str` 
    
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

<details><summary><code>client.endpoints_http_methods.<a href="src/fern/endpoints_http_methods/client.py">endpoints_http_methods_test_delete</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_http_methods.endpoints_http_methods_test_delete(
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

**id:** `str` 
    
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

<details><summary><code>client.endpoints_http_methods.<a href="src/fern/endpoints_http_methods/client.py">endpoints_http_methods_test_patch</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_http_methods.endpoints_http_methods_test_patch(
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**string:** `typing.Optional[str]` — This is a rather long descriptor of this single field in a more complex type. If you ask me I think this is a pretty good description for this field all things considered.
    
</dd>
</dl>

<dl>
<dd>

**integer:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**long_:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**double:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bool_:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**datetime:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[dt.date]` 
    
</dd>
</dl>

<dl>
<dd>

**uuid_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**base64:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**list_:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**set_:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**map_:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**bigint:** `typing.Optional[int]` 
    
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

<details><summary><code>client.endpoints_http_methods.<a href="src/fern/endpoints_http_methods/client.py">endpoints_http_methods_test_post</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_http_methods.endpoints_http_methods_test_post(
    string="string",
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

**string:** `str` 
    
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

## EndpointsObject
<details><summary><code>client.endpoints_object.<a href="src/fern/endpoints_object/client.py">endpoints_object_get_and_return_with_optional_field</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_object.endpoints_object_get_and_return_with_optional_field()

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

**string:** `typing.Optional[str]` — This is a rather long descriptor of this single field in a more complex type. If you ask me I think this is a pretty good description for this field all things considered.
    
</dd>
</dl>

<dl>
<dd>

**integer:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**long_:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**double:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**bool_:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**datetime:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[dt.date]` 
    
</dd>
</dl>

<dl>
<dd>

**uuid_:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**base64:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**list_:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**set_:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**map_:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**bigint:** `typing.Optional[int]` 
    
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

<details><summary><code>client.endpoints_object.<a href="src/fern/endpoints_object/client.py">endpoints_object_get_and_return_with_required_field</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_object.endpoints_object_get_and_return_with_required_field(
    string="string",
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

**string:** `str` 
    
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

<details><summary><code>client.endpoints_object.<a href="src/fern/endpoints_object/client.py">endpoints_object_get_and_return_with_map_of_map</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_object.endpoints_object_get_and_return_with_map_of_map(
    map_={"key": {"key": "value"}},
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

**map_:** `typing.Dict[str, typing.Dict[str, str]]` 
    
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

<details><summary><code>client.endpoints_object.<a href="src/fern/endpoints_object/client.py">endpoints_object_get_and_return_nested_with_optional_field</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_object.endpoints_object_get_and_return_nested_with_optional_field()

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

**string:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**nested_object:** `typing.Optional[TypesObjectWithOptionalField]` 
    
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

<details><summary><code>client.endpoints_object.<a href="src/fern/endpoints_object/client.py">endpoints_object_get_and_return_nested_with_required_field</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TypesObjectWithOptionalField

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_object.endpoints_object_get_and_return_nested_with_required_field(
    string_="string",
    string="string",
    nested_object=TypesObjectWithOptionalField(),
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

**string_:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**string:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**nested_object:** `TypesObjectWithOptionalField` 
    
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

<details><summary><code>client.endpoints_object.<a href="src/fern/endpoints_object/client.py">endpoints_object_get_and_return_nested_with_required_field_as_list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import (
    FernApi,
    TypesNestedObjectWithRequiredField,
    TypesObjectWithOptionalField,
)

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_object.endpoints_object_get_and_return_nested_with_required_field_as_list(
    request=[
        TypesNestedObjectWithRequiredField(
            string="string",
            nested_object=TypesObjectWithOptionalField(),
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

**request:** `typing.Sequence[TypesNestedObjectWithRequiredField]` 
    
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

<details><summary><code>client.endpoints_object.<a href="src/fern/endpoints_object/client.py">endpoints_object_get_and_return_with_unknown_field</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_object.endpoints_object_get_and_return_with_unknown_field(
    unknown={"key": "value"},
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

**unknown:** `typing.Optional[typing.Any]` 
    
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

<details><summary><code>client.endpoints_object.<a href="src/fern/endpoints_object/client.py">endpoints_object_get_and_return_with_documented_unknown_type</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_object.endpoints_object_get_and_return_with_documented_unknown_type(
    documented_unknown_type={"key": "value"},
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

**documented_unknown_type:** `TypesDocumentedUnknownType` 
    
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

<details><summary><code>client.endpoints_object.<a href="src/fern/endpoints_object/client.py">endpoints_object_get_and_return_map_of_documented_unknown_type</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_object.endpoints_object_get_and_return_map_of_documented_unknown_type(
    request={},
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

**request:** `TypesMapOfDocumentedUnknownType` 
    
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

<details><summary><code>client.endpoints_object.<a href="src/fern/endpoints_object/client.py">endpoints_object_get_and_return_with_datetime_like_string</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tests that string fields containing datetime-like values are NOT reformatted.
The datetimeLikeString field should preserve its exact value "2023-08-31T14:15:22Z"
without being converted to "2023-08-31T14:15:22.000Z".
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

from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_object.endpoints_object_get_and_return_with_datetime_like_string(
    datetime_like_string="datetimeLikeString",
    actual_datetime=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**datetime_like_string:** `str` — A string field that happens to contain a datetime-like value
    
</dd>
</dl>

<dl>
<dd>

**actual_datetime:** `dt.datetime` — An actual datetime field for comparison
    
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

## EndpointsPagination
<details><summary><code>client.endpoints_pagination.<a href="src/fern/endpoints_pagination/client.py">endpoints_pagination_list_items</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List items with cursor pagination
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_pagination.endpoints_pagination_list_items()

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

**cursor:** `typing.Optional[str]` — The cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
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

## EndpointsParams
<details><summary><code>client.endpoints_params.<a href="src/fern/endpoints_params/client.py">endpoints_params_get_with_path</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GET with path param
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_params.endpoints_params_get_with_path(
    param="param",
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

**param:** `str` 
    
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

<details><summary><code>client.endpoints_params.<a href="src/fern/endpoints_params/client.py">endpoints_params_modify_with_path</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

PUT to update with path param
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_params.endpoints_params_modify_with_path(
    param="param",
    request="string",
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

**param:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
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

<details><summary><code>client.endpoints_params.<a href="src/fern/endpoints_params/client.py">endpoints_params_get_with_inline_path</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GET with path param
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_params.endpoints_params_get_with_inline_path(
    param="param",
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

**param:** `str` 
    
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

<details><summary><code>client.endpoints_params.<a href="src/fern/endpoints_params/client.py">endpoints_params_modify_with_inline_path</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

PUT to update with path param
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_params.endpoints_params_modify_with_inline_path(
    param="param",
    request="string",
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

**param:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
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

<details><summary><code>client.endpoints_params.<a href="src/fern/endpoints_params/client.py">endpoints_params_get_with_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GET with query param
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_params.endpoints_params_get_with_query(
    query="query",
    number=1,
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

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**number:** `int` 
    
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

<details><summary><code>client.endpoints_params.<a href="src/fern/endpoints_params/client.py">endpoints_params_get_with_allow_multiple_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GET with multiple of same query param
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_params.endpoints_params_get_with_allow_multiple_query(
    query=["query"],
    number=[1],
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

**query:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**number:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` 
    
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

<details><summary><code>client.endpoints_params.<a href="src/fern/endpoints_params/client.py">endpoints_params_get_with_path_and_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GET with path and query params
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_params.endpoints_params_get_with_path_and_query(
    param="param",
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

**param:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` 
    
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

<details><summary><code>client.endpoints_params.<a href="src/fern/endpoints_params/client.py">endpoints_params_get_with_inline_path_and_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

GET with path and query params
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_params.endpoints_params_get_with_inline_path_and_query(
    param="param",
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

**param:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` 
    
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

## EndpointsPrimitive
<details><summary><code>client.endpoints_primitive.<a href="src/fern/endpoints_primitive/client.py">endpoints_primitive_get_and_return_string</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_primitive.endpoints_primitive_get_and_return_string(
    request="string",
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

**request:** `str` 
    
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

<details><summary><code>client.endpoints_primitive.<a href="src/fern/endpoints_primitive/client.py">endpoints_primitive_get_and_return_int</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_primitive.endpoints_primitive_get_and_return_int(
    request=1,
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

**request:** `int` 
    
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

<details><summary><code>client.endpoints_primitive.<a href="src/fern/endpoints_primitive/client.py">endpoints_primitive_get_and_return_long</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_primitive.endpoints_primitive_get_and_return_long(
    request=1000000,
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

**request:** `int` 
    
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

<details><summary><code>client.endpoints_primitive.<a href="src/fern/endpoints_primitive/client.py">endpoints_primitive_get_and_return_double</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_primitive.endpoints_primitive_get_and_return_double(
    request=1.1,
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

**request:** `float` 
    
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

<details><summary><code>client.endpoints_primitive.<a href="src/fern/endpoints_primitive/client.py">endpoints_primitive_get_and_return_bool</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_primitive.endpoints_primitive_get_and_return_bool(
    request=True,
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

**request:** `bool` 
    
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

<details><summary><code>client.endpoints_primitive.<a href="src/fern/endpoints_primitive/client.py">endpoints_primitive_get_and_return_datetime</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_primitive.endpoints_primitive_get_and_return_datetime(
    request=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
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

**request:** `dt.datetime` 
    
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

<details><summary><code>client.endpoints_primitive.<a href="src/fern/endpoints_primitive/client.py">endpoints_primitive_get_and_return_date</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from fern import FernApi

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_primitive.endpoints_primitive_get_and_return_date(
    request=datetime.date.fromisoformat(
        "2023-01-15",
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

**request:** `dt.date` 
    
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

<details><summary><code>client.endpoints_primitive.<a href="src/fern/endpoints_primitive/client.py">endpoints_primitive_get_and_return_uuid</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_primitive.endpoints_primitive_get_and_return_uuid(
    request="string",
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

**request:** `str` 
    
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

<details><summary><code>client.endpoints_primitive.<a href="src/fern/endpoints_primitive/client.py">endpoints_primitive_get_and_return_base64</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_primitive.endpoints_primitive_get_and_return_base64(
    request="string",
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

**request:** `str` 
    
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

## EndpointsPut
<details><summary><code>client.endpoints_put.<a href="src/fern/endpoints_put/client.py">endpoints_put_add</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_put.endpoints_put_add(
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

**id:** `str` 
    
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

## EndpointsUnion
<details><summary><code>client.endpoints_union.<a href="src/fern/endpoints_union/client.py">endpoints_union_get_and_return_union</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TypesAnimalZero, TypesAnimalZeroAnimal

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_union.endpoints_union_get_and_return_union(
    request=TypesAnimalZero(
        name="name",
        likes_to_woof=True,
        animal=TypesAnimalZeroAnimal.DOG,
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

**request:** `TypesAnimal` 
    
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

## EndpointsUrls
<details><summary><code>client.endpoints_urls.<a href="src/fern/endpoints_urls/client.py">endpoints_urls_with_mixed_case</a>()</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_urls.endpoints_urls_with_mixed_case()

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

<details><summary><code>client.endpoints_urls.<a href="src/fern/endpoints_urls/client.py">endpoints_urls_no_ending_slash</a>()</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_urls.endpoints_urls_no_ending_slash()

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

<details><summary><code>client.endpoints_urls.<a href="src/fern/endpoints_urls/client.py">endpoints_urls_with_ending_slash</a>()</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_urls.endpoints_urls_with_ending_slash()

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

<details><summary><code>client.endpoints_urls.<a href="src/fern/endpoints_urls/client.py">endpoints_urls_with_underscores</a>()</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.endpoints_urls.endpoints_urls_with_underscores()

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

## Inlinedrequests
<details><summary><code>client.inlinedrequests.<a href="src/fern/inlinedrequests/client.py">postwithobjectbodyandresponse</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

POST with custom object in request body, response is an object
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
from fern import FernApi, TypesObjectWithOptionalField

client = FernApi(
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.inlinedrequests.postwithobjectbodyandresponse(
    string="string",
    integer=1,
    nested_object=TypesObjectWithOptionalField(),
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

**string:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**integer:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**nested_object:** `TypesObjectWithOptionalField` 
    
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

## Noauth
<details><summary><code>client.noauth.<a href="src/fern/noauth/client.py">postwithnoauth</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

POST request with no auth
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.noauth.postwithnoauth(
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

**request:** `typing.Optional[typing.Any]` 
    
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

## Noreqbody
<details><summary><code>client.noreqbody.<a href="src/fern/noreqbody/client.py">getwithnorequestbody</a>()</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.noreqbody.getwithnorequestbody()

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

<details><summary><code>client.noreqbody.<a href="src/fern/noreqbody/client.py">postwithnorequestbody</a>()</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.noreqbody.postwithnorequestbody()

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

## Reqwithheaders
<details><summary><code>client.reqwithheaders.<a href="src/fern/reqwithheaders/client.py">getwithcustomheader</a>(...)</code></summary>
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
    token="YOUR_TOKEN",
    base_url="https://yourhost.com/path/to/api",
)
client.reqwithheaders.getwithcustomheader(
    test_endpoint_header="X-TEST-ENDPOINT-HEADER",
    request="string",
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

**test_endpoint_header:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
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

