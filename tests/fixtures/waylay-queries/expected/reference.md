# Reference
## Status
<details><summary><code>client.status.<a href="src/fern/status/client.py">get_version_and_health</a>() -> typing.Dict[str, str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the version and health status for waylay-query.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.status.get_version_and_health()

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

## Execute
<details><summary><code>client.execute.<a href="src/fern/execute/client.py">execute_query</a>(...) -> QueryResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a timeseries query.

Executes the timeseries query specified in the request body,
after applying any overrides from the url parameters.

Note that string values in the query body can contain `{var_name}` placeholders.
These will get replaced with by `var_name` bindings
in the query body for that variable.

```json
{
    "station_id": "29758",
    "resource": "weather_station_{station_id}",
    ...
}
```
results in using a `weather_station_29758` resource.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.execute.execute_query(
    resource="13efb488-75ac-4dac-828a-d49c5c2ebbfc",
    metric="temperature",
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

**request:** `QueryInput` 
    
</dd>
</dl>

<dl>
<dd>

**resource:** `typing.Optional[str]` — Default Resource Override.
    
</dd>
</dl>

<dl>
<dd>

**metric:** `typing.Optional[str]` — Default Metric Override.
    
</dd>
</dl>

<dl>
<dd>

**aggregation:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**interpolation:** `typing.Optional[InterpolationMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**freq:** `typing.Optional[str]` — Override for the `freq` query attribute.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**window:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**periods:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**render:** `typing.Optional[RenderMode]` 
    
</dd>
</dl>

<dl>
<dd>

**accept:** `typing.Optional[str]` — Use a 'text/csv' accept header to get CSV formatted results.
    
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

<details><summary><code>client.execute.<a href="src/fern/execute/client.py">by_name</a>(...) -> QueryResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a named timeseries query.

Retrieves a stored query definition by name,
applies overrides from the url parameters, and executes it.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.execute.by_name(
    query_name="query_name",
    resource="13efb488-75ac-4dac-828a-d49c5c2ebbfc",
    metric="temperature",
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

**query_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**resource:** `typing.Optional[str]` — Default Resource Override.
    
</dd>
</dl>

<dl>
<dd>

**metric:** `typing.Optional[str]` — Default Metric Override.
    
</dd>
</dl>

<dl>
<dd>

**aggregation:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**interpolation:** `typing.Optional[InterpolationMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**freq:** `typing.Optional[str]` — Override for the `freq` query attribute.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**window:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**periods:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**render:** `typing.Optional[RenderMode]` 
    
</dd>
</dl>

<dl>
<dd>

**accept:** `typing.Optional[str]` — Use a 'text/csv' accept header to get CSV formatted results.
    
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

## Manage
<details><summary><code>client.manage.<a href="src/fern/manage/client.py">list_queries</a>(...) -> QueriesListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List named queries.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.manage.list_queries(
    q="resource:APL4995",
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

**q:** `typing.Optional[str]` — The QDSL filter condition for the stored queries. Note that this value needs to be escaped when passed as an url paramater.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximal number of items return in one response.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Numbers of items to skip before listing results in the response page.
    
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

<details><summary><code>client.manage.<a href="src/fern/manage/client.py">post_query</a>(...) -> QueryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new named query.
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
from fern import FernApi, QueryInput
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.manage.post_query(
    name="name",
    query=QueryInput(),
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

**name:** `str` — Name of the stored query definition.
    
</dd>
</dl>

<dl>
<dd>

**query:** `QueryInput` 
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[typing.Dict[str, typing.Any]]` — User metadata for the query definition.
    
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

<details><summary><code>client.manage.<a href="src/fern/manage/client.py">get_query</a>(...) -> QueryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the definition of a named query.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.manage.get_query(
    query_name="query_name",
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

**query_name:** `str` — Name of the stored query.
    
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

<details><summary><code>client.manage.<a href="src/fern/manage/client.py">update_query</a>(...) -> QueryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update a named query definition.
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
from fern import FernApi, QueryUpdateInput
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.manage.update_query(
    query_name="query_name",
    request=QueryUpdateInput(),
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

**query_name:** `str` — Name of the stored query.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateQueryQueriesV1QueryQueryNamePutRequestBody` 
    
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

<details><summary><code>client.manage.<a href="src/fern/manage/client.py">remove_query</a>(...) -> DeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove definition of a named query.
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
from fern.environment import FernApiEnvironment

client = FernApi(
    username="<username>",
    password="<password>",
    environment=FernApiEnvironment.DEFAULT,
)

client.manage.remove_query(
    query_name="query_name",
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

**query_name:** `str` — Name of the stored query.
    
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

