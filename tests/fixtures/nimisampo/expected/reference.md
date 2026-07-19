# Reference
<details><summary><code>client.<a href="src/fern/client.py">return_faceted_search_results_with_pagination</a>(...) -> PostFacetedSearchResultClassPaginatedResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.return_faceted_search_results_with_pagination(
    result_class="perspective1",
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

**result_class:** `str` — The class of the results
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**pagesize:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">return_all_search_results_as_a_csv_file</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.return_all_search_results_as_a_csv_file(...)
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

**result_class:** `str` — The class of the results
    
</dd>
</dl>

<dl>
<dd>

**facet_class:** `str` — The class for facet configs
    
</dd>
</dl>

<dl>
<dd>

**result_format:** `str` — Result format, only support for CSV for now.
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[str]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">return_all_search_results</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.return_all_search_results(
    result_class="placesMsProduced",
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

**result_class:** `str` — The class of the results
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">return_the_total_count_of_the_faceted_search_results</a>(...) -> PostFacetedSearchResultClassCountResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.return_the_total_count_of_the_faceted_search_results(
    result_class="perspective1",
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

**result_class:** `str` — The class of the results
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">return_values_for_a_single_facet</a>(...) -> PostFacetedSearchFacetClassFacetIdResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.return_values_for_a_single_facet(
    facet_class="perspective1",
    id="language",
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

**facet_class:** `str` — The class of the facet
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The id of the facet
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**constrain_self:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">return_information_about_a_single_resource_optionally_applying_facet_filters</a>(...) -> PostResultClassPageUriResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.return_information_about_a_single_resource_optionally_applying_facet_filters(
    result_class="perspective1",
    uri="http://ldf.fi/mmm/manifestation_singleton/bibale_10003",
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

**result_class:** `str` — The class of the resource
    
</dd>
</dl>

<dl>
<dd>

**uri:** `str` — The URI of the resource
    
</dd>
</dl>

<dl>
<dd>

**facet_class:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[typing.List[typing.Dict[str, typing.Any]]]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">full_text_search</a>(...) -> GetFullTextSearchResponse</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.full_text_search(
    q="q",
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

**q:** `str` — The query string
    
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

<details><summary><code>client.<a href="src/fern/client.py">federated_search_can_be_used_for_retrieving_the_initial_result_set_from_multiple_sparql_endpoints_for_client_side_faceted_search</a>(...) -> typing.List[typing.Dict[str, typing.Any]]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.federated_search_can_be_used_for_retrieving_the_initial_result_set_from_multiple_sparql_endpoints_for_client_side_faceted_search(
    perspective_id="perspectiveID",
    dataset=[
        "dataset"
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

**perspective_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**dataset:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — The query string
    
</dd>
</dl>

<dl>
<dd>

**lat_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**long_min:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**lat_max:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**long_max:** `typing.Optional[float]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">make_preconfigured_web_feature_service_wfs_api_calls_via_the_backend</a>(...) -> typing.List[typing.Any]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.make_preconfigured_web_feature_service_wfs_api_calls_via_the_backend(
    layer_id=[
        "layerID"
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

**layer_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">route_for_password_protected_wms_layers</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.route_for_password_protected_wms_layers(...)
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

**service:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**layers:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**styles:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**transparent:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**width:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**height:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**crs:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**bbox:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">route_for_nls_wmts_api_only_for_contract_customers</a>(...) -> typing.List[typing.Any]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.route_for_nls_wmts_api_only_for_contract_customers(
    layer_id="layerID",
    x="x",
    y="y",
    z="z",
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

**layer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**x:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**y:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**z:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">route_for_nls_wmts_api_free_but_requires_an_api_key</a>(...) -> typing.List[typing.Any]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.route_for_nls_wmts_api_free_but_requires_an_api_key(
    layer_id="layerID",
    x="x",
    y="y",
    z="z",
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

**layer_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**x:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**y:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**z:** `str` 
    
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

<details><summary><code>client.<a href="src/fern/client.py">route_for_nls_vectortiles_api_free_but_requires_an_api_key</a>() -> typing.Dict[str, typing.Any]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.route_for_nls_vectortiles_api_free_but_requires_an_api_key()

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

<details><summary><code>client.<a href="src/fern/client.py">retrieve_a_vo_id_description</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
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
    environment=FernApiEnvironment.DEFAULT,
)

client.retrieve_a_vo_id_description(
    perspective_id="perspective1",
    result_class="perspective1KnowledgeGraphMetadata",
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

**perspective_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**result_class:** `str` 
    
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

