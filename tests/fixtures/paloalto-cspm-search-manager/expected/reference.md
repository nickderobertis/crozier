# Reference
## Search Manager
<details><summary><code>client.search_manager.<a href="src/fern/search_manager/client.py">search_history</a>(...) -> typing.List[SavedRecentSearch]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists saved or recent search queries based on your filter.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search_manager.search_history(
    filter="filter",
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

**filter:** `str` — Available values: recent, saved
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of searches to be returned. A single API call retrieves a maximum of 1000 searches, which is also the default. Setting the limit to -1 will also return the default.
    
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

<details><summary><code>client.search_manager.<a href="src/fern/search_manager/client.py">search_history_by_id</a>(...) -> SearchModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a search query. You can access only queries that are either saved or recent searches.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search_manager.search_history_by_id(
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

**id:** `str` — Search ID
    
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

<details><summary><code>client.search_manager.<a href="src/fern/search_manager/client.py">search_history_manage</a>(...) -> SearchResponseModelSearchModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allows you to manage a search query (save a search query to the **Saved Searches** list under the specified ID, convert a recent search to a saved search, update an existing search). For details on how to manage a saved search, see [Manage Saved Search](/prisma-cloud/docs/cspm/manage-saved-search)  

Required parameters include the search ID, the RQL query, the flag that 
marks this search as saved, and a unique name for the saved search. A best 
practice is to copy data from the results of a search history, update the 
data as necessary, and set the **saved** parameter to **true**.

This API requires Prisma Cloud system administrator role access if you don't own the search with the given search ID.
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
from fern import FernApi, SearchModelTimeRange_Absolute, AbsoluteTimeRangeConfigModelValue
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search_manager.search_history_manage(
    id_="id",
    query="query",
    time_range=SearchModelTimeRange_Absolute(
        value=AbsoluteTimeRangeConfigModelValue(),
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

**id:** `str` — Search ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchModel` 
    
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

<details><summary><code>client.search_manager.<a href="src/fern/search_manager/client.py">search_history_delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a saved search query.
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
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.search_manager.search_history_delete(
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

**id:** `str` — Search ID
    
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

