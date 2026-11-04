# Reference
## dataquery
<details><summary><code>client.dataquery.<a href="src/fern/dataquery/client.py">get_data_query_list</a>(...) -> typing.List[DataQueryListEntry]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This returns a list with basic information about the queries. Id, label (if present) and creation date. Basically for all parameters I'm not sure if we need them (at least right away)
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

client.dataquery.get_data_query_list()

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

**include_temporary:** `typing.Optional[bool]` — if set to true, queries spawned from other users are contained
    
</dd>
</dl>

<dl>
<dd>

**skip_validation:** `typing.Optional[bool]` — If true, do not validate the query and do not include a list of invalid terms.
    
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

<details><summary><code>client.dataquery.<a href="src/fern/dataquery/client.py">store_data_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The query will only be stored, nothing will be dispatched. Does not have to pass any validation and may be incomplete. May or may not contain result.
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
from fern import FernApi, Crtdl

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.dataquery.store_data_query(
    content=Crtdl(),
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

**request:** `Dataquery` 
    
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

<details><summary><code>client.dataquery.<a href="src/fern/dataquery/client.py">find_data_queries_by_user</a>(...) -> typing.List[DataQueryListEntry]</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.dataquery.find_data_queries_by_user(
    user_id="userId",
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

**user_id:** `str` — User to filter by (keycloak id)
    
</dd>
</dl>

<dl>
<dd>

**include_temporary:** `typing.Optional[bool]` — if set to true, queries spawned from other users are contained
    
</dd>
</dl>

<dl>
<dd>

**skip_validation:** `typing.Optional[bool]` — If true, do not validate the query and do not include a list of invalid terms.
    
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

<details><summary><code>client.dataquery.<a href="src/fern/dataquery/client.py">create_dataquery_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Crtdl

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.dataquery.create_dataquery_for_user(
    user_id="userId",
    ttl="ttl",
    content=Crtdl(),
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

**user_id:** `str` — ID of the user for whom to spawn the query
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `str` — How long until the query gets deleted (ISO 8601 Duration)
    
</dd>
</dl>

<dl>
<dd>

**request:** `Dataquery` 
    
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

<details><summary><code>client.dataquery.<a href="src/fern/dataquery/client.py">get_data_query_by_id</a>(...) -> Dataquery</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single dataquery.
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

client.dataquery.get_data_query_by_id(
    query_id=1000000,
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

**query_id:** `int` — ID of query to return
    
</dd>
</dl>

<dl>
<dd>

**skip_validation:** `typing.Optional[bool]` — If true, do not validate the query and do not include a list of invalid terms
    
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

<details><summary><code>client.dataquery.<a href="src/fern/dataquery/client.py">update_data_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The query will be updated. It must be provided completely, there are no partial updates.
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
from fern import FernApi, Crtdl

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.dataquery.update_data_query(
    query_id=1000000,
    content=Crtdl(),
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

**query_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `Dataquery` 
    
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

<details><summary><code>client.dataquery.<a href="src/fern/dataquery/client.py">delete_data_query</a>(...)</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.dataquery.delete_data_query(
    query_id=1000000,
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

**query_id:** `int` 
    
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

<details><summary><code>client.dataquery.<a href="src/fern/dataquery/client.py">get_data_query_crtdl_by_id</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns only the CRTDL part of a dataquery or alternatively a zip file containing the crtdl json and csv files
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

client.dataquery.get_data_query_crtdl_by_id(
    query_id=1000000,
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

**query_id:** `int` — ID of query to return
    
</dd>
</dl>

<dl>
<dd>

**skip_validation:** `typing.Optional[bool]` — If true, do not validate the query and do not include a list of invalid terms
    
</dd>
</dl>

<dl>
<dd>

**accept:** `typing.Optional[GetDataQueryCrtdlByIdRequestAccept]` — Specify the desired format
    
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

<details><summary><code>client.dataquery.<a href="src/fern/dataquery/client.py">convert_crtdl_to_csv</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Nothing will be stored, only a zip file will be generated
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

client.dataquery.convert_crtdl_to_csv()

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

**request:** `Crtdl` 
    
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

<details><summary><code>client.dataquery.<a href="src/fern/dataquery/client.py">get_data_query_slots</a>() -> DataQuerySlots</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.dataquery.get_data_query_slots()

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

## feasibility
<details><summary><code>client.feasibility.<a href="src/fern/feasibility/client.py">run_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The query will be spawned in the broker and directly be dispatched.
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
from fern import FernApi, Criterion, TermCode

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.feasibility.run_query(
    version="http://to_be_decided.com/draft-1/schema#",
    inclusion_criteria=[
        [
            Criterion(
                term_codes=[
                    TermCode(
                        code="code",
                        system="http://snomed.info/sct",
                        display="Amniotic fluid specimen (specimen)",
                    )
                ],
            )
        ]
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

**request:** `Ccdl` 
    
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

<details><summary><code>client.feasibility.<a href="src/fern/feasibility/client.py">get_query_result_summary</a>(...) -> QueryResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the aggregated results to a query. There is no breakdown by site. So, the resultLines parameter of the response is de facto an array of QueryResultLines, but it will always be empty in this case.
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

client.feasibility.get_query_result_summary(
    query_id=1000000,
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

**query_id:** `int` — ID of query for which the results are requested
    
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

<details><summary><code>client.feasibility.<a href="src/fern/feasibility/client.py">get_query_result_detailed</a>(...) -> QueryResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns results to query with the real site names - admin rights required
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

client.feasibility.get_query_result_detailed(
    query_id=1000000,
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

**query_id:** `int` — ID of query for which the results are requested
    
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

<details><summary><code>client.feasibility.<a href="src/fern/feasibility/client.py">get_query_result_detailed_obfuscated</a>(...) -> QueryResultObfuscated</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all results to query with the site names obfuscated.
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

client.feasibility.get_query_result_detailed_obfuscated(
    query_id=1000000,
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

**query_id:** `int` — ID of query for which the results are requested
    
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

<details><summary><code>client.feasibility.<a href="src/fern/feasibility/client.py">get_detailed_obfuscated_result_rate_limit</a>() -> QueryResultRateLimit</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.feasibility.get_detailed_obfuscated_result_rate_limit()

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

<details><summary><code>client.feasibility.<a href="src/fern/feasibility/client.py">get_quota</a>() -> QueryQuota</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.feasibility.get_quota()

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

<details><summary><code>client.feasibility.<a href="src/fern/feasibility/client.py">sq2cql</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Nothing will be persisted in the backend. It simply returns the cql.
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
from fern import FernApi, Criterion, TermCode

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.feasibility.sq2cql(
    version="http://to_be_decided.com/draft-1/schema#",
    inclusion_criteria=[
        [
            Criterion(
                term_codes=[
                    TermCode(
                        code="code",
                        system="http://snomed.info/sct",
                        display="Amniotic fluid specimen (specimen)",
                    )
                ],
            )
        ]
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

**request:** `Ccdl` 
    
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

## terminology
<details><summary><code>client.terminology.<a href="src/fern/terminology/client.py">get_filters</a>(...) -> typing.List[Filter]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can optionally be filtered to only get the filters of one category, depending on the selections of other categories
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

client.terminology.get_filters(
    target_filter="terminology",
    searchterm="terminology",
    contexts=[
        "Diagnosis"
    ],
    terminologies=[
        "ICD10"
    ],
    kds_modules=[
        "Condition"
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

**target_filter:** `typing.Optional[str]` — The requested filter category. Only if this is set, the further filters for contexts, kds-modules and terminologies are considered. If it is empty or null, ALL entries are returned.
    
</dd>
</dl>

<dl>
<dd>

**searchterm:** `typing.Optional[str]` — Allow to take the searchterm into consideration to narrow down the results further.
    
</dd>
</dl>

<dl>
<dd>

**contexts:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to any of the given contexts
    
</dd>
</dl>

<dl>
<dd>

**terminologies:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to a any of the given terminologies
    
</dd>
</dl>

<dl>
<dd>

**kds_modules:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to any of the given KDS modules
    
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

<details><summary><code>client.terminology.<a href="src/fern/terminology/client.py">get_terminology_systems</a>() -> TerminologySystems</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.terminology.get_terminology_systems()

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

<details><summary><code>client.terminology.<a href="src/fern/terminology/client.py">search_entry</a>(...) -> ElasticSearchResult</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.terminology.search_entry(
    searchterm="Diabetes Mellitus",
    contexts=[
        "Diagnosis"
    ],
    terminologies=[
        "ICD10"
    ],
    kds_modules=[
        "Condition"
    ],
    criteria_sets=[
        "http://fhir.de/CodeSystem/bfarm/icd-10-gm"
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

**searchterm:** `typing.Optional[str]` — The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically
    
</dd>
</dl>

<dl>
<dd>

**contexts:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to any of the given contexts
    
</dd>
</dl>

<dl>
<dd>

**terminologies:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to a any of the given terminologies
    
</dd>
</dl>

<dl>
<dd>

**kds_modules:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to any of the given KDS modules
    
</dd>
</dl>

<dl>
<dd>

**criteria_sets:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to certain criteria sets (specified via url)
    
</dd>
</dl>

<dl>
<dd>

**availability:** `typing.Optional[bool]` — Limit the search to available items? (Maybe better invert this one to make this the default?)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many results shall be returned per page
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Which page shall be returned
    
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

<details><summary><code>client.terminology.<a href="src/fern/terminology/client.py">bulk_search_entry</a>(...) -> ElasticSearchBulkResult</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.terminology.bulk_search_entry(
    terminology="http://fhir.de/CodeSystem/bfarm/icd-10-gm",
    context="Diagnose",
    searchterms=[
        "Z01.81"
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

**terminology:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**searchterms:** `typing.List[str]` 
    
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

<details><summary><code>client.terminology.<a href="src/fern/terminology/client.py">get_entry_by_id</a>(...) -> RelationsEntry</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.terminology.get_entry_by_id(
    id="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8",
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

**id:** `str` — The id (contextualized termcode hash) of the entry that shall be retrieved
    
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

<details><summary><code>client.terminology.<a href="src/fern/terminology/client.py">get_entries_by_id</a>(...) -> ElasticSearchResultEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This should be in the getEntryById call, but for better distinction between the return values it is listed separately here
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

client.terminology.get_entries_by_id(
    id="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8",
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

**id:** `str` — The ids (contextualized termcode hash) of the entries that shall be retrieved
    
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

<details><summary><code>client.terminology.<a href="src/fern/terminology/client.py">get_entries_by_ids_with_detail</a>(...) -> typing.List[CriteriaProfileData]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This should return all the information needed to build criteria in the frontend.
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

client.terminology.get_entries_by_ids_with_detail(
    ids="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8,203e04cd-4f0a-321b-b1ad-9ec6d211e0a9",
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

**ids:** `str` — A comma-separated list of IDs (contextualized termcode hashes) of the entries that shall be retrieved.
    
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

<details><summary><code>client.terminology.<a href="src/fern/terminology/client.py">get_ui_profiles</a>() -> UiProfileList</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.terminology.get_ui_profiles()

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

## codeable concepts
<details><summary><code>client.codeable_concepts.<a href="src/fern/codeable_concepts/client.py">search_codeable_concepts</a>(...) -> CodeableConceptSearchResult</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.codeable_concepts.search_codeable_concepts(
    searchterm="Diabetes Mellitus",
    value_sets=[
        "http://fhir.de/CodeSystem/bfarm/icd-10-gm"
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

**searchterm:** `typing.Optional[str]` — The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically
    
</dd>
</dl>

<dl>
<dd>

**value_sets:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to certain value sets (specified via url)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many results shall be returned per page
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Which page shall be returned
    
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

<details><summary><code>client.codeable_concepts.<a href="src/fern/codeable_concepts/client.py">bulk_search_codeable_concepts</a>(...) -> CodeableConceptBulkSearchResult</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.codeable_concepts.bulk_search_codeable_concepts(
    value_set="https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/ValueSet/sct-body-structures",
    searchterms=[
        "something invalid"
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

**value_set:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**searchterms:** `typing.List[str]` 
    
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

<details><summary><code>client.codeable_concepts.<a href="src/fern/codeable_concepts/client.py">get_codeable_concepts_by_code</a>(...) -> CodeableConceptEntry</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.codeable_concepts.get_codeable_concepts_by_code(
    ids="203e04cd-4f0a-321b-b1ad-9ec6d211e0a8,203e04cd-4f0a-321b-b1ad-9ec6d211e0a9",
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

**ids:** `str` — The ids (contextualized termcode hash) of the entry that shall be retrieved
    
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

## profile
<details><summary><code>client.profile.<a href="src/fern/profile/client.py">search_profiles</a>(...) -> ProfileSearchResult</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.profile.search_profiles(
    searchterm="Diagnose",
    modules=[
        "Diagnose"
    ],
    categories=[
        "element"
    ],
    resource_types=[
        "Condition"
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

**searchterm:** `typing.Optional[str]` — The term to search for. In case of an empty searchterm, return the first page of the whole index, sorted alphabetically
    
</dd>
</dl>

<dl>
<dd>

**modules:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to any of the given modules
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to any of the given categories
    
</dd>
</dl>

<dl>
<dd>

**resource_types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to any of the given FHIR resource types
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — How many results shall be returned per page
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Which page shall be returned
    
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

<details><summary><code>client.profile.<a href="src/fern/profile/client.py">get_profile_list_details_by_id</a>(...) -> ProfileEntry</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.profile.get_profile_list_details_by_id(
    id="diagnose-condition-id",
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

**id:** `str` — The id of the profile entry that shall be retrieved
    
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

<details><summary><code>client.profile.<a href="src/fern/profile/client.py">get_filter</a>(...) -> typing.List[ProfileFilter]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can optionally be filtered to only get the filter of one target category, depending on the selections of the other categories and/or a searchterm
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

client.profile.get_filter(
    searchterm="Diagnose",
    modules=[
        "Diagnose"
    ],
    categories=[
        "element"
    ],
    resource_types=[
        "Condition"
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

**target_filter:** `typing.Optional[GetFilterRequestTargetFilter]` — The requested filter category. Only if this is set, the further filters for searchterm, modules, categories and resource-types are considered. If it is empty or null, ALL filters are returned unfiltered.
    
</dd>
</dl>

<dl>
<dd>

**searchterm:** `typing.Optional[str]` — Allow to take the searchterm into consideration to narrow down the results further.
    
</dd>
</dl>

<dl>
<dd>

**modules:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to any of the given modules
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to any of the given categories
    
</dd>
</dl>

<dl>
<dd>

**resource_types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Limit the search to any of the given FHIR resource types
    
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

## dse
<details><summary><code>client.dse.<a href="src/fern/dse/client.py">get_profile_data</a>(...) -> ProfileDataList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get profile data for all submitted ids. If a profile is not found, an error message will be supplied.
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

client.dse.get_profile_data(
    ids="https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/ObservationLab,https://www.medizininformatik-initiative.de/fhir/core/modul-prozedur/StructureDefinition/Procedure",
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

**ids:** `str` — A comma-separated list of IDs (here - mostly URLs) of the entries that shall be retrieved.
    
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

## validation
<details><summary><code>client.validation.<a href="src/fern/validation/client.py">validate_crtdl</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if the json matches the schema and if the content does not contain invalid entries
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

client.validation.validate_crtdl()

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

**request:** `Crtdl` 
    
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

<details><summary><code>client.validation.<a href="src/fern/validation/client.py">validate_ccdl</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if the json matches the schema and if the content does not contain invalid entries
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
from fern import FernApi, Criterion, TermCode

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.validation.validate_ccdl(
    version="http://to_be_decided.com/draft-1/schema#",
    inclusion_criteria=[
        [
            Criterion(
                term_codes=[
                    TermCode(
                        code="code",
                        system="http://snomed.info/sct",
                        display="Amniotic fluid specimen (specimen)",
                    )
                ],
            )
        ]
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

**request:** `Ccdl` 
    
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

<details><summary><code>client.validation.<a href="src/fern/validation/client.py">validate_dataquery</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if the json matches the schema and if the content does not contain invalid entries
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
from fern import FernApi, Crtdl

client = FernApi(
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.validation.validate_dataquery(
    content=Crtdl(),
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

**request:** `Dataquery` 
    
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

## upgrade
<details><summary><code>client.upgrade.<a href="src/fern/upgrade/client.py">crtdl</a>(...) -> UpgradeWrapper</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Some common problems can be automatically fixed by either removing parts of the CRTDL or renaming things. Try to fix as many as possible
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

client.upgrade.crtdl()

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

**request:** `Crtdl` 
    
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

## intrinsics
<details><summary><code>client.intrinsics.<a href="src/fern/intrinsics/client.py">get_health</a>() -> typing.Any</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.intrinsics.get_health()

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

<details><summary><code>client.intrinsics.<a href="src/fern/intrinsics/client.py">get_info</a>() -> SystemInfo</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.intrinsics.get_info()

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

<details><summary><code>client.intrinsics.<a href="src/fern/intrinsics/client.py">get_settings</a>() -> SettingsInfo</code></summary>
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
    token="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.intrinsics.get_settings()

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

