# Reference
## Server
<details><summary><code>client.server.<a href="src/fern/server/client.py">get_version</a>() -> GetVersionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current version of the API.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.server.get_version()

```
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

<details><summary><code>client.server.<a href="src/fern/server/client.py">post_disconnect</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnects the application from the Fergus API and revokes all tokens.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.server.post_disconnect(
    refresh_token="refreshToken",
    client_id="clientId",
    client_secret="clientSecret",
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

**refresh_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
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

## Favourites
<details><summary><code>client.favourites.<a href="src/fern/favourites/client.py">get_favourites</a>(...) -> FavouritesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all favourite sections, in flat or tree view
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.favourites.get_favourites()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetFavouritesRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_section_name:** `typing.Optional[str]` 

Searchable fields:
- representation: tree
  - `section.name`
- representation: flat
  - `section.name`
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetFavouritesRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**representation:** `typing.Optional[GetFavouritesRequestRepresentation]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search_text:** `typing.Optional[str]` 

Searchable fields:
- representation: tree
  - `section.name`
  - `lineItem.itemName`,
- representation: flat
  - `section.name`
  - `section.description`,
  - `lineItem.itemName`
    
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

<details><summary><code>client.favourites.<a href="src/fern/favourites/client.py">get_favourites_section_id</a>(...) -> FavouritesSection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific favourite section
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.favourites.get_favourites_section_id(
    section_id="sectionId",
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

**section_id:** `str` 
    
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

## Jobs
<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_jobs</a>(...) -> JobsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of jobs. The list can be filtered by job type.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetJobsRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_job_no:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_job_status:** `typing.Optional[GetJobsRequestFilterJobStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_job_type:** `typing.Optional[GetJobsRequestFilterJobType]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_customer_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_site_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetJobsRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_show_on_hold:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_show_archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search_text:** `typing.Optional[str]` 

Searchable fields:
- `description`
- `longDescription`
- `jobNo`
- `customer.customerFullName`
- `siteAddress.name`
- `siteAddress.firstName`
- `siteAddress.lastName`
- `mainContact.firstName`
- `mainContact.lastName`
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">post_jobs</a>(...) -> JobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new job
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
from fern.jobs import PostJobsRequestJobType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.post_jobs(
    job_type=PostJobsRequestJobType.QUOTE,
    title="title",
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

**job_type:** `PostJobsRequestJobType` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**is_draft:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_reference:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**site_id:** `typing.Optional[float]` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_jobs_job_id</a>(...) -> JobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a job by id
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_jobs_job_id(
    job_id=1.1,
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

**job_id:** `float` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">put_jobs_job_id</a>(...) -> JobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a draft job
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
from fern.jobs import PutJobsJobIdRequestBodyTitle

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.put_jobs_job_id(
    job_id=1.1,
    request=PutJobsJobIdRequestBodyTitle(
        title="title",
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

**job_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PutJobsJobIdRequestBody` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">put_jobs_job_id_finalise</a>(...) -> JobResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finalise a draft job.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.put_jobs_job_id_finalise(
    job_id=1.1,
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

**job_id:** `float` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_jobs_job_id_phases</a>(...) -> JobPhasesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of job phases
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_jobs_job_id_phases(
    job_id="jobId",
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

**job_id:** `str` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">post_jobs_job_id_phases</a>(...) -> JobPhaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a job phase
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.post_jobs_job_id_phases(
    job_id="jobId",
    title="title",
    description="description",
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

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_jobs_job_id_phases_job_phase_id</a>(...) -> JobPhaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a job phase
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_jobs_job_id_phases_job_phase_id(
    job_id="jobId",
    job_phase_id="jobPhaseId",
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

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_phase_id:** `str` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">put_jobs_job_id_phases_job_phase_id</a>(...) -> JobPhaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a job phase
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.put_jobs_job_id_phases_job_phase_id(
    job_id="jobId",
    job_phase_id="jobPhaseId",
    title="title",
    description="description",
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

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**job_phase_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">post_jobs_job_id_phases_job_phase_id_void</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Void a job phase by JobId and Job PhaseId
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.post_jobs_job_id_phases_job_phase_id_void(
    job_id=1.1,
    job_phase_id=1.1,
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

**job_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**job_phase_id:** `float` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_jobs_job_id_financial_summary</a>(...) -> JobFinancialSummaryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a job financial summary
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_jobs_job_id_financial_summary(
    job_id=1.1,
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

**job_id:** `float` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_jobs_job_id_phases_job_phase_id_financial_summary</a>(...) -> JobFinancialSummaryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a job phase financial summary
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_jobs_job_id_phases_job_phase_id_financial_summary(
    job_id=1.1,
    job_phase_id=1.1,
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

**job_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**job_phase_id:** `float` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_jobs_job_id_quotes</a>(...) -> GetQuotesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all quotes for a job
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_jobs_job_id_quotes(
    job_id="jobId",
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

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetJobsJobIdQuotesRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include_combined_item_parents:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_status:** `typing.Optional[GetJobsJobIdQuotesRequestFilterStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetJobsJobIdQuotesRequestSortField]` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">post_jobs_job_id_quotes</a>(...) -> AddQuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new quote
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
from fern.jobs import PostJobsJobIdQuotesRequestSectionsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.post_jobs_job_id_quotes(
    job_id="jobId",
    title="title",
    due_days=1.1,
    sections=[
        PostJobsJobIdQuotesRequestSectionsItem(
            name="name",
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

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**due_days:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**sections:** `typing.List[PostJobsJobIdQuotesRequestSectionsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**version_number:** `typing.Optional[float]` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">get_jobs_job_id_quotes_quote_id</a>(...) -> GetQuoteByIdQuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a quote
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.get_jobs_job_id_quotes_quote_id(
    job_id=1.1,
    quote_id=1.1,
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

**job_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**quote_id:** `float` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">put_jobs_job_id_quotes_quote_id</a>(...) -> UpdateQuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a quote by ID
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
from fern.jobs import PutJobsJobIdQuotesQuoteIdRequestSectionsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.put_jobs_job_id_quotes_quote_id(
    job_id=1.1,
    quote_id=1.1,
    sections=[
        PutJobsJobIdQuotesQuoteIdRequestSectionsItem(
            name="name",
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

**job_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**quote_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**sections:** `typing.List[PutJobsJobIdQuotesQuoteIdRequestSectionsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

<details><summary><code>client.jobs.<a href="src/fern/jobs/client.py">put_jobs_job_id_quotes_version_version_number</a>(...) -> UpdateQuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a quote by version number
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
from fern.jobs import PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs.put_jobs_job_id_quotes_version_version_number(
    job_id=1.1,
    version_number=1.1,
    sections=[
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem(
            name="name",
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

**job_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**version_number:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**sections:** `typing.List[PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

## JobsQuotes
<details><summary><code>client.jobs_quotes.<a href="src/fern/jobs_quotes/client.py">get_jobs_quotes</a>(...) -> GetStandaloneQuotesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all quotes from across all jobs, sorted by created date and last modified date.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_quotes.get_jobs_quotes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetJobsQuotesRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_status:** `typing.Optional[GetJobsQuotesRequestFilterStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetJobsQuotesRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Get quote created after certain time. Overrides sortField and sortOrder
    
</dd>
</dl>

<dl>
<dd>

**modified_after:** `typing.Optional[datetime.datetime]` — Get quote modified after certain time. Overrides sortField and sortOrder
    
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

<details><summary><code>client.jobs_quotes.<a href="src/fern/jobs_quotes/client.py">get_jobs_quotes_quote_id</a>(...) -> GetQuoteByIdQuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific quote by ID from across all jobs.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_quotes.get_jobs_quotes_quote_id(
    quote_id=1.1,
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

**quote_id:** `float` 
    
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

<details><summary><code>client.jobs_quotes.<a href="src/fern/jobs_quotes/client.py">get_jobs_quotes_guid_guid</a>(...) -> GetQuoteByIdQuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific quote by GUID with full details.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_quotes.get_jobs_quotes_guid_guid(
    guid="guid",
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

**guid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**include_combined_item_parents:** `typing.Optional[bool]` — Include the parents of combined line item in the `lineItems` list (default: false)
    
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

<details><summary><code>client.jobs_quotes.<a href="src/fern/jobs_quotes/client.py">post_jobs_quotes_quote_id_publish</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publishes a quote.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_quotes.post_jobs_quotes_quote_id_publish(
    quote_id="quoteId",
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

**quote_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**published_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**published_by:** `typing.Optional[str]` 
    
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

<details><summary><code>client.jobs_quotes.<a href="src/fern/jobs_quotes/client.py">post_jobs_quotes_quote_id_mark_as_sent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks a quote as sent.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_quotes.post_jobs_quotes_quote_id_mark_as_sent(
    quote_id="quoteId",
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

**quote_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**is_sent:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.jobs_quotes.<a href="src/fern/jobs_quotes/client.py">post_jobs_quotes_quote_id_accept</a>(...) -> typing.Optional[AcceptQuoteResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accepts a quote.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_quotes.post_jobs_quotes_quote_id_accept(
    quote_id="quoteId",
    accepted_by="acceptedBy",
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

**quote_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accepted_by:** `str` — The name or employee GUID of the person accepting the quote
    
</dd>
</dl>

<dl>
<dd>

**accepted_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**selected_section_ids:** `typing.Optional[typing.List[int]]` — The IDs of the sections that the customer has accepted. Required if the quote has optional or multi-select sections.
    
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

<details><summary><code>client.jobs_quotes.<a href="src/fern/jobs_quotes/client.py">post_jobs_quotes_quote_id_decline</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Declines a quote.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_quotes.post_jobs_quotes_quote_id_decline(
    quote_id="quoteId",
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

**quote_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**declined_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**reason_notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rejected_by:** `typing.Optional[str]` 
    
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

<details><summary><code>client.jobs_quotes.<a href="src/fern/jobs_quotes/client.py">post_jobs_quotes_quote_id_void</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Voids a quote.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_quotes.post_jobs_quotes_quote_id_void(
    quote_id="quoteId",
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

**quote_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**voided_at:** `typing.Optional[datetime.datetime]` 
    
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

<details><summary><code>client.jobs_quotes.<a href="src/fern/jobs_quotes/client.py">post_jobs_quotes_quote_id_totals</a>(...) -> QuoteTotalsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get totals for a quote. Fixed sections are always included. Optionally provide optional/multiselect section IDs to include in the totals.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_quotes.post_jobs_quotes_quote_id_totals(
    quote_id=1.1,
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

**quote_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**selected_section_ids:** `typing.Optional[typing.List[int]]` — [] — returns totals for fixed sections only. [1, 2, 3] — returns totals for fixed sections + the provided optional/multiselect section IDs.
    
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

## CustomerInvoices
<details><summary><code>client.customer_invoices.<a href="src/fern/customer_invoices/client.py">get_customer_invoices</a>(...) -> ListCustomerInvoicesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of invoices. The list can be filtered by customer, job, invoice number, and due dates.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.customer_invoices.get_customer_invoices()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetCustomerInvoicesRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetCustomerInvoicesRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[float]` — Filter by customer ID
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `typing.Optional[float]` — Filter by job ID
    
</dd>
</dl>

<dl>
<dd>

**invoice_number:** `typing.Optional[str]` — Search by invoiceNumber
    
</dd>
</dl>

<dl>
<dd>

**due_before:** `typing.Optional[datetime.datetime]` — Filter invoices due before this datetime
    
</dd>
</dl>

<dl>
<dd>

**due_after:** `typing.Optional[datetime.datetime]` — Filter invoices due after this datetime
    
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

<details><summary><code>client.customer_invoices.<a href="src/fern/customer_invoices/client.py">get_customer_invoices_invoice_id</a>(...) -> GetCustomerInvoiceByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single invoice by ID with customer details and sections
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.customer_invoices.get_customer_invoices_invoice_id(
    invoice_id=1.1,
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

**invoice_id:** `float` 
    
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

## Customers
<details><summary><code>client.customers.<a href="src/fern/customers/client.py">get_customers</a>(...) -> GetCustomersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of customers. The list can be filtered by customer name.<br/><br/>
    A note about contact items on each person:<br>
    <ul>
      <li>The contact items are an array of objects. Each object has a `contactType` and a `contactValue`.
      <li>The `contactType` can be one of the following: email, phone, mobile, or fax.
      <li>The `contactValue` can be an email address or phone number.
    </ul>
    
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.customers.get_customers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetCustomersRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetCustomersRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search_text:** `typing.Optional[str]` 

Searchable fields:
- `customerFullName`
- `mainContact.firstName`
- `mainContact.lastName`
- `mainContact.contactItems[].contactValue`
- `billingContact.firstName`
- `billingContact.lastName`,
- `billingContact.contactItems[].contactValue`
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">post_customers</a>(...) -> GetCustomerByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new customer.
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
from fern import FernApi, PersonPayload
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.customers.post_customers(
    customer_full_name="customerFullName",
    main_contact=PersonPayload(
        first_name="firstName",
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

**customer_full_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**main_contact:** `PersonPayload` 
    
</dd>
</dl>

<dl>
<dd>

**physical_address:** `typing.Optional[AddressPayload]` 
    
</dd>
</dl>

<dl>
<dd>

**postal_address:** `typing.Optional[AddressPayload]` 
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">get_customers_customer_id</a>(...) -> GetCustomerByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a customer by ID.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.customers.get_customers_customer_id(
    customer_id=1.1,
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

**customer_id:** `float` 
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">put_customers_customer_id</a>(...) -> GetCustomerByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a customer.
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
from fern import FernApi, PersonPayload
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.customers.put_customers_customer_id(
    customer_id=1.1,
    customer_full_name="customerFullName",
    main_contact=PersonPayload(
        first_name="firstName",
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

**customer_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**customer_full_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**main_contact:** `PersonPayload` 
    
</dd>
</dl>

<dl>
<dd>

**physical_address:** `typing.Optional[AddressPayload]` 
    
</dd>
</dl>

<dl>
<dd>

**postal_address:** `typing.Optional[AddressPayload]` 
    
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

<details><summary><code>client.customers.<a href="src/fern/customers/client.py">delete_customers_customer_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a customer by ID.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.customers.delete_customers_customer_id(
    customer_id=1.1,
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

**customer_id:** `float` 
    
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

## Sites
<details><summary><code>client.sites.<a href="src/fern/sites/client.py">get_sites</a>(...) -> SitesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of sites. The list can be filtered by site name, address city, and address postal code.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sites.get_sites()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetSitesRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_site_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_address_city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_address_postal_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetSitesRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search_text:** `typing.Optional[str]` 

Searchable fields:
- `name`
- `defaultContact.firstName`
- `defaultContact.lastName`
- `customer.customerFullName`
- `billingContact.firstName`
- `billingContact.lastName`
- `physicalAddress.address1`
- `physicalAddress.address2`
    
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

<details><summary><code>client.sites.<a href="src/fern/sites/client.py">post_sites</a>(...) -> SiteByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new site
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
from fern import FernApi, PersonPayload, AddressPayload
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sites.post_sites(
    default_contact=PersonPayload(
        first_name="firstName",
    ),
    site_address=AddressPayload(
        address1="address1",
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

**default_contact:** `PersonPayload` 
    
</dd>
</dl>

<dl>
<dd>

**site_address:** `AddressPayload` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**billing_contact:** `typing.Optional[PersonPayload]` 
    
</dd>
</dl>

<dl>
<dd>

**postal_address:** `typing.Optional[AddressPayload]` 
    
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

<details><summary><code>client.sites.<a href="src/fern/sites/client.py">get_sites_site_id</a>(...) -> SiteByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a site by ID.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sites.get_sites_site_id(
    site_id=1.1,
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

**site_id:** `float` 
    
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

<details><summary><code>client.sites.<a href="src/fern/sites/client.py">patch_sites_site_id</a>(...) -> SiteByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update site
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
from fern import FernApi, AddressPayload
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sites.patch_sites_site_id(
    site_id="siteId",
    site_address=AddressPayload(
        address1="address1",
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

**site_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**site_address:** `AddressPayload` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**postal_address:** `typing.Optional[AddressPayload]` 
    
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

<details><summary><code>client.sites.<a href="src/fern/sites/client.py">post_sites_site_id_archive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive Site.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sites.post_sites_site_id_archive(
    site_id=1.1,
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

**site_id:** `float` 
    
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

<details><summary><code>client.sites.<a href="src/fern/sites/client.py">post_sites_site_id_restore</a>(...) -> SiteByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore Site.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.sites.post_sites_site_id_restore(
    site_id=1.1,
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

**site_id:** `float` 
    
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

## Contacts
<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">get_contacts</a>(...) -> ContactsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of contacts. The list can be filtered by contact type.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.get_contacts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetContactsRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetContactsRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_contact_type:** `typing.Optional[GetContactsRequestFilterContactType]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_customer_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_site_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search_text:** `typing.Optional[str]` 

Searchable fields:
- `firstName`
- `lastName`
- `email`
- `phoneNumber`
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">post_contacts</a>(...) -> ContactByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new contact for a customer or site.

  - **firstName** is required
  - **email** is required and must be a valid email address. This will be added as a contact item.
  - **contactType** is required and must be one of the following: `CUSTOMER`, `SITE`.
    - When **contactType** is `CUSTOMER`:
      - **customerId** is required
      - **isMain** cannot be set to true and is optional. To update the main contact, use the '/customers' endpoint.
      - **isBilling** is optional and defaults to false.
    - When **contactType** is `SITE`:
      - **siteId** is required
      - **isMain** is optional and defaults to false.
      - **isBilling** is optional and defaults to false.
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
from fern.contacts import CreateContactPayloadContactType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.post_contacts(
    first_name="firstName",
    email="email",
    contact_type=CreateContactPayloadContactType.CUSTOMER,
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

**first_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**contact_type:** `CreateContactPayloadContactType` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**position:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_items:** `typing.Optional[typing.List[ContactItemPayload]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_main:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_billing:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**site_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[float]` 
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">get_contacts_contact_id</a>(...) -> ContactByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a contact by ID.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.get_contacts_contact_id(
    contact_id=1.1,
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

**contact_id:** `float` 
    
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

<details><summary><code>client.contacts.<a href="src/fern/contacts/client.py">put_contacts_contact_id</a>(...) -> ContactByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a customer contact or site contact.

  - **firstName** is required
  - NOTE: To update the main contact of a `CUSTOMER`, please use the /customers endpoint.
    - When the contact to update is of type `CUSTOMER`:
      - **isMain** cannot be set to true and is optional. To update the main contact, use the '/customers' endpoint.
      - **isBilling** is optional and defaults to false.
  - NOTE: To unset the main contact of a `SITE` as non-main is not allowed, either use the create endpoint or update another contact of this site and set it as the main contact.
    - When the contact to update is of type `SITE`:
      - **isMain** is optional and defaults to false.
      - **isBilling** is optional and defaults to false.
      - If the contact to update is the main and billing contact of the `SITE`, the **isBilling** flag will have no impact and the contact details will be updated. If you want to change the contact that is assigned as the billing contact, please use the create method or update another contact of this site and set it as a billing contact.
  - **contactItems** at least one contact item of type email is required. 
    - It will replace the existing contact items.
    - To update a specific contact item, you have to provide the id of the contact item to update. Otherwise, new contact items will be added.
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
from fern import FernApi, ContactItemPayload, ContactItemPayloadContactType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.contacts.put_contacts_contact_id(
    contact_id=1.1,
    first_name="firstName",
    contact_items=[
        ContactItemPayload(
            contact_type=ContactItemPayloadContactType.EMAIL,
            contact_value="contactValue",
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

**contact_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**contact_items:** `typing.List[ContactItemPayload]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**position:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_main:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_billing:** `typing.Optional[bool]` 
    
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

## Enquiries
<details><summary><code>client.enquiries.<a href="src/fern/enquiries/client.py">get_enquiries</a>(...) -> EnquiriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all enquiries
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.enquiries.get_enquiries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetEnquiriesRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetEnquiriesRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_status:** `typing.Optional[GetEnquiriesRequestFilterStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search_text:** `typing.Optional[str]` 

Searchable fields:
- `name`
- `description`
- `phone`
- `email`
    
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

<details><summary><code>client.enquiries.<a href="src/fern/enquiries/client.py">post_enquiries</a>(...) -> EnquiryCreatedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Enquiry
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.enquiries.post_enquiries(
    name="name",
    email="email",
    phone_number="phoneNumber",
    description="description",
    source="source",
    address1="address1",
    post_enquiries_request_address_city="addressCity",
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**address1:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**post_enquiries_request_address_city:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**address2:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address_suburb:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address_region:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address_postcode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address_country:** `typing.Optional[str]` 
    
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

<details><summary><code>client.enquiries.<a href="src/fern/enquiries/client.py">get_enquiries_enquiry_id</a>(...) -> EnquiryByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns enquiry by ID.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.enquiries.get_enquiries_enquiry_id(
    enquiry_id=1.1,
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

**enquiry_id:** `float` 
    
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

## JobsPhases
<details><summary><code>client.jobs_phases.<a href="src/fern/jobs_phases/client.py">get_phases_job_phase_id_stock_on_hand</a>(...) -> StockOnHandListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Job Phase stock on hand
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_phases.get_phases_job_phase_id_stock_on_hand(
    job_phase_id=1.1,
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

**job_phase_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetPhasesJobPhaseIdStockOnHandRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetPhasesJobPhaseIdStockOnHandRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search_text:** `typing.Optional[str]` 

Searchable fields:
- `itemDescription`
    
</dd>
</dl>

<dl>
<dd>

**last_modified:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**date_entered:** `typing.Optional[datetime.datetime]` 
    
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

<details><summary><code>client.jobs_phases.<a href="src/fern/jobs_phases/client.py">post_phases_job_phase_id_stock_on_hand</a>(...) -> StockOnHandResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add stock on hand to job phase. Two scenarios are supported:

**With `priceBookLineItemId`:** Only `itemQuantity` is required. `itemDescription`, `itemPrice`, and `itemCost` will be populated from the price book item. No other fields may be passed.

**Without `priceBookLineItemId`:** `itemDescription`, `itemPrice`, `itemCost`, and `itemQuantity` are all required.
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
from fern.jobs_phases import PostPhasesJobPhaseIdStockOnHandRequestBodyPriceBookLineItemId

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_phases.post_phases_job_phase_id_stock_on_hand(
    job_phase_id=1.1,
    request=PostPhasesJobPhaseIdStockOnHandRequestBodyPriceBookLineItemId(
        item_quantity=1.1,
        price_book_line_item_id=1.1,
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

**job_phase_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PostPhasesJobPhaseIdStockOnHandRequestBody` 
    
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

<details><summary><code>client.jobs_phases.<a href="src/fern/jobs_phases/client.py">get_phases_stock_on_hand</a>(...) -> StockOnHandListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stock on hand across all Job Phases
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_phases.get_phases_stock_on_hand()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetPhasesStockOnHandRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetPhasesStockOnHandRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search_text:** `typing.Optional[str]` 

Searchable fields:
- `itemDescription`
    
</dd>
</dl>

<dl>
<dd>

**last_modified:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**date_entered:** `typing.Optional[datetime.datetime]` 
    
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

<details><summary><code>client.jobs_phases.<a href="src/fern/jobs_phases/client.py">delete_phases_job_phase_id_stock_on_hand_stock_on_hand_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete stock on hand on job phase
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_phases.delete_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
    job_phase_id=1.1,
    stock_on_hand_id=1.1,
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

**job_phase_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**stock_on_hand_id:** `float` 
    
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

<details><summary><code>client.jobs_phases.<a href="src/fern/jobs_phases/client.py">patch_phases_job_phase_id_stock_on_hand_stock_on_hand_id</a>(...) -> StockOnHandResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update stock on hand on job phase
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.jobs_phases.patch_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
    job_phase_id=1.1,
    stock_on_hand_id=1.1,
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

**job_phase_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**stock_on_hand_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**item_description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**item_price:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**item_cost:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**item_quantity:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sales_account_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**is_labour:** `typing.Optional[bool]` 
    
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

## StockUsed
<details><summary><code>client.stock_used.<a href="src/fern/stock_used/client.py">get_stock_used</a>(...) -> StockUsedListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>


  Returns historical stock used across all jobs, optionally filtered by filterDateFrom.
  
  Stock used is defined as material line items that:
  - Have been invoiced to the customer (sent or paid).
  - And are assigned as materials sales account.
  - And are not from purchase orders.
  - And are not invoiced from suppliers.
  
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.stock_used.get_stock_used()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter_date_from:** `typing.Optional[datetime.date]` — Filter stock used on or after this date (yyyy-mm-dd) default is 90 days ago and max up to 180 days ago
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
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

## Users
<details><summary><code>client.users.<a href="src/fern/users/client.py">get_users</a>(...) -> UsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of users. The list can be filtered by first name, last name or email.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.get_users()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetUsersRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetUsersRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_user_type:** `typing.Optional[GetUsersRequestFilterUserType]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_status:** `typing.Optional[GetUsersRequestFilterStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search_text:** `typing.Optional[str]` 

Searchable fields:
- `firstName`
- `lastName`
- `employee's username`
- `email`
- `address.address1`
- `address.address2`
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_users_user_id</a>(...) -> UserByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a user by ID.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.get_users_user_id(
    user_id=1.1,
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

**user_id:** `float` 
    
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

<details><summary><code>client.users.<a href="src/fern/users/client.py">patch_users_user_id</a>(...) -> UserByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update user
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.patch_users_user_id(
    user_id=1.1,
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

**user_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[AddressPayload]` 
    
</dd>
</dl>

<dl>
<dd>

**pay_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**charge_out_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**contact_items:** `typing.Optional[typing.List[PatchUsersUserIdRequestContactItemsItem]]` 
    
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

## TimeEntries
<details><summary><code>client.time_entries.<a href="src/fern/time_entries/client.py">get_time_entries</a>(...) -> TimeEntriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all time entries
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.time_entries.get_time_entries(
    filter_search_text="John",
    filter_date_from=datetime.date.fromisoformat("2023-01-21"),
    filter_date_to=datetime.date.fromisoformat("2023-01-21"),
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

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetTimeEntriesRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetTimeEntriesRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_search_text:** `typing.Optional[str]` 

Searchable fields:
- `user`
- `employee's username`
- `jobPhaseTitle`,
- `jobPhaseDetails`
    
</dd>
</dl>

<dl>
<dd>

**filter_locked_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_user_id:** `typing.Optional[float]` — The user id to filter time entries by
    
</dd>
</dl>

<dl>
<dd>

**filter_job_no:** `typing.Optional[float]` — The job no to filter time entries by
    
</dd>
</dl>

<dl>
<dd>

**filter_job_phase_id:** `typing.Optional[float]` — The job phase id to filter time entries by
    
</dd>
</dl>

<dl>
<dd>

**filter_date_from:** `typing.Optional[datetime.date]` — The start date in yyyy-mm-dd format
    
</dd>
</dl>

<dl>
<dd>

**filter_date_to:** `typing.Optional[datetime.date]` — The end date in yyyy-mm-dd format
    
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

## CalendarEvents
<details><summary><code>client.calendar_events.<a href="src/fern/calendar_events/client.py">get_calendar_events</a>(...) -> CalendarEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of CalendarEvents. The list can be filtered by user name, event type or active events only.
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.calendar_events.get_calendar_events(
    filter_date_from=datetime.datetime.fromisoformat("2025-12-01T11:00:00+00:00"),
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

**filter_calendar_event_type:** `typing.Optional[GetCalendarEventsRequestFilterCalendarEventType]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_user_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_job_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_job_phase_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_job_events_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_non_job_events_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_unassigned_events_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_active_only:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_date_from:** `typing.Optional[datetime.datetime]` 

The start date for filtering calendar events, in ISO 8601 format. 

- The time portion is discarded only the date is used. 

- A timezone offset (+/-HH:MM or +/-HHMM) is expected to ensure accurate timezone interpretation. 

- If none is provided, the value will be treated as UTC.
    
</dd>
</dl>

<dl>
<dd>

**filter_calendar_range:** `typing.Optional[GetCalendarEventsRequestFilterCalendarRange]` 

The filterDateFrom (or currentDate if not provided) sets the start of the period.

- For DAY and THREE_DAY options, it's that exact date.

- For WEEK and MONTH options, it's the week or month that includes that date (weeks run Monday to Sunday).

- For FORTNIGHT option, it starts at the Monday of the week that contains that date. 

This defaults to WEEK if not provided.
    
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

<details><summary><code>client.calendar_events.<a href="src/fern/calendar_events/client.py">post_calendar_events</a>(...) -> CalendarEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new calendar event.
  - **eventType** must be one of : `JOB_PHASE`, `QUOTE`, `ESTIMATE`, `OTHER`.
    - **JOB_PHASE**: Event type for a job phase. `jobPhaseId` must be provided.
    - **QUOTE**: Event type for a quote. `jobId` must be provided.
    - **ESTIMATE**: Event type for an estimate. `jobId` must be provided.
    - **OTHER**: General event type. Default value.
  - **frequency** must be one of : `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `NEVER`.
    - **DAILY**: Repeats every day.
    - **WEEKLY**: Repeats every week.
    - **MONTHLY**: Repeats every month.
    - **YEARLY**: Repeats every year.
    - **NEVER**: Does not repeat. Default value.
  - If the event is recurring, **frequency** is ***not*** `NEVER`.
    - **interval** controls how often the event repeats, 
      - Example:  `WEEKLY` with an `interval = 2`, the event repeats every 2 weeks.
      - Default is `1`.
    - **repeatEndType** must be one of:
      - `NEVER`: Repeats indefinitely. Default value.
      - `ON_DATE`: Repeats until the specified **repeatEndDate**.
      - `AFTER`: Repeats for the specified **repeatCount** number of occurrences.
    - If `repeatEndType = ON_DATE`, the **repeatEndDate** must be provided.
    - If `repeatEndType = AFTER`, the **repeatCount** must be provided.
  - If **userId** or **linkedUserIds** is provided, the event is assigned to those user(s). Otherwise, the event is unassigned. 
  
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
import datetime
from fern.calendar_events import PostCalendarEventsRequestEventType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.calendar_events.post_calendar_events(
    start_time=datetime.datetime.fromisoformat("2021-01-01T07:00:00+00:00"),
    end_time=datetime.datetime.fromisoformat("2021-01-01T17:00:00+00:00"),
    event_title="eventTitle",
    event_type=PostCalendarEventsRequestEventType.JOB_PHASE,
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

**start_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**event_title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `PostCalendarEventsRequestEventType` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**linked_user_ids:** `typing.Optional[typing.List[float]]` 
    
</dd>
</dl>

<dl>
<dd>

**job_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**job_phase_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**frequency:** `typing.Optional[PostCalendarEventsRequestFrequency]` 
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**repeat_end_type:** `typing.Optional[PostCalendarEventsRequestRepeatEndType]` 
    
</dd>
</dl>

<dl>
<dd>

**repeat_end_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**repeat_count:** `typing.Optional[float]` 
    
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

<details><summary><code>client.calendar_events.<a href="src/fern/calendar_events/client.py">get_calendar_events_calendar_event_id</a>(...) -> CalendarEventByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a CalendarEvent by ID.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.calendar_events.get_calendar_events_calendar_event_id(
    calendar_event_id=1.1,
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

**calendar_event_id:** `float` 
    
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

<details><summary><code>client.calendar_events.<a href="src/fern/calendar_events/client.py">post_calendar_events_calendar_event_id</a>(...) -> CalendarEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a calendar event.
  - To set the event to update to recurring, **frequency** must be set to a value other than `NEVER`.
    - **interval** controls how often the event repeats, 
      - Example:  `WEEKLY` with an `interval = 2`, the event repeats every 2 weeks.
      - Default is `1`.
    - **repeatEndType** must be one of:
      - `NEVER`: Repeats indefinitely. Default value.
      - `ON_DATE`: Repeats until the specified **repeatEndDate**.
      - `AFTER`: Repeats for the specified **repeatCount** number of occurrences.
    - If `repeatEndType = ON_DATE`, the **repeatEndDate** must be provided.
    - If `repeatEndType = AFTER`, the **repeatCount** must be provided.
  - If the event to update is recurring, **updateAllRecurring** must be specified:
    - If **updateAllRecurring** is true, all future occurrences of the current event are updated.
    - If **updateAllRecurring** is false, only the current event is updated and future occurrences are not updated. 
      - An optional **repeatSplitOnDate** can be provided and the event is only updated on the specified date and future occurrences are not updated.
      - if the **repeatSplitOnDate** is not provided, this is set to the event's **startTime** value.
  - If the event to update is assigned to a group, **updateAllGrouped** must be specified:
    - If **updateAllGrouped** is true, all events in the group are updated otherwise only the current event is updated.
  - To assign the event to update, **userId** or **linkedUserIds** can be provided, and the event is assigned to those user(s). Otherwise, the event is unassigned.
    - When assigning to a group, i.e. the **linkedUserIds** is provided, the **updateAllGrouped** property must be set to true.
  
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
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.calendar_events.post_calendar_events_calendar_event_id(
    calendar_event_id=1.1,
    start_time=datetime.datetime.fromisoformat("2021-01-01T07:00:00+00:00"),
    end_time=datetime.datetime.fromisoformat("2021-01-01T17:00:00+00:00"),
    event_title="eventTitle",
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

**calendar_event_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `datetime.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**event_title:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**linked_user_ids:** `typing.Optional[typing.List[float]]` 
    
</dd>
</dl>

<dl>
<dd>

**frequency:** `typing.Optional[PostCalendarEventsCalendarEventIdRequestFrequency]` 
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**repeat_end_type:** `typing.Optional[PostCalendarEventsCalendarEventIdRequestRepeatEndType]` 
    
</dd>
</dl>

<dl>
<dd>

**repeat_end_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**repeat_count:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**repeat_split_on_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**update_all_recurring:** `typing.Optional[PostCalendarEventsCalendarEventIdRequestUpdateAllRecurring]` 
    
</dd>
</dl>

<dl>
<dd>

**update_all_grouped:** `typing.Optional[PostCalendarEventsCalendarEventIdRequestUpdateAllGrouped]` 
    
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

<details><summary><code>client.calendar_events.<a href="src/fern/calendar_events/client.py">delete_calendar_events_calendar_event_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a calendar event.
  - If the event to delete is recurring, **deleteAllRecurring** must be specified:
    - If **deleteAllRecurring** is true, all future occurrences of the event are deleted
    - If **deleteAllRecurring** is false, an optional **deleteOnDate** can be provided.
      - if **deleteOnDate** is provided, the event is split and the event is only deleted on the specified date and previous or future events are not deleted.
      - if the **deleteOnDate** is not provided, this is set to the event's **startTime** value.
  - If the event to delete is assigned to a group, **deleteAllGrouped** must be specified:
    - If **deleteAllGrouped** is true, all events in the group are deleted otherwise only the current event is deleted.
  
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.calendar_events.delete_calendar_events_calendar_event_id(
    calendar_event_id=1.1,
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

**calendar_event_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**delete_on_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**delete_all_recurring:** `typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring]` 
    
</dd>
</dl>

<dl>
<dd>

**delete_all_grouped:** `typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped]` 
    
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

## PricingTiers
<details><summary><code>client.pricing_tiers.<a href="src/fern/pricing_tiers/client.py">get_pricing_tiers</a>(...) -> GetPricingTiersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schema for a Pricing Tier
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pricing_tiers.get_pricing_tiers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetPricingTiersRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetPricingTiersRequestSortField]` 
    
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

<details><summary><code>client.pricing_tiers.<a href="src/fern/pricing_tiers/client.py">get_pricing_tiers_id</a>(...) -> GetPricingTierByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schema for a Pricing Tier by ID
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pricing_tiers.get_pricing_tiers_id(
    id=1.1,
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

**id:** `float` 
    
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

## Pricebooks
<details><summary><code>client.pricebooks.<a href="src/fern/pricebooks/client.py">post_pricebooks_search</a>(...) -> SearchPricebooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for pricebook items across multiple pricebooks

This endpoint allows you to search for products/items across one or more supplier pricebooks using a text-based search query. The search is performed across item names, product codes, and search values.

**Search Behavior:**
- Searches match when the search term appears anywhere within searchable fields (substring matching)
- Results are ranked by relevance (exact matches and word-start matches ranked higher)
- Pagination uses cursor-based navigation with encoded ranking information

**allSuppliers**

When `allSuppliers` is provided and set to `true`, it will override the list of `supplierIds` array.

For example the below payload will search across all suppliers for the term "hammer" and apply the pricing tier with id 123:

```
{
  "search": "hammer",
  "pricingTierId": 123,
  "allSuppliers": true,
  "supplierIds": [
    101,
    102,
    103
  ]
}
```

To narrow search by specific suppliers, set `allSuppliers` to `false` and provide a list of supplier IDs:

```
{
  "search": "hammer",
  "pricingTierId": 123,
  "allSuppliers": false,
  "supplierIds": [
    101,
    102,
    103
  ]
}
```

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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pricebooks.post_pricebooks_search(
    search="hammer",
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

**search:** `str` 

Search term for pricebook items (minimum 3 characters). Searches across:
- `name` - Product or item name
- `productCode` - Product identification code
- `supplierSku` - Supplier SKU/part number
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[PostPricebooksSearchRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**pricing_tier_id:** `typing.Optional[float]` — Filter results to show prices for a specific pricing tier ID. If not provided, the default pricing tier will be used
    
</dd>
</dl>

<dl>
<dd>

**all_suppliers:** `typing.Optional[bool]` — When true (default), searches across all supplier pricebooks. When false, only searches pricebooks specified in supplierIds
    
</dd>
</dl>

<dl>
<dd>

**supplier_ids:** `typing.Optional[typing.List[float]]` — Array of supplier/pricebook IDs to limit the search scope. Only used when allSuppliers is false
    
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

<details><summary><code>client.pricebooks.<a href="src/fern/pricebooks/client.py">get_pricebooks</a>(...) -> GetPricebooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schema for Pricebooks
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pricebooks.get_pricebooks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetPricebooksRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetPricebooksRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_supplier_name:** `typing.Optional[str]` — Filter pricebooks by supplier name containing this string
    
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

<details><summary><code>client.pricebooks.<a href="src/fern/pricebooks/client.py">get_pricebooks_id</a>(...) -> GetPriceBookByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schema for a Pricebook by ID
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pricebooks.get_pricebooks_id(
    id=1.1,
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

**id:** `float` 
    
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

<details><summary><code>client.pricebooks.<a href="src/fern/pricebooks/client.py">get_pricebooks_id_pricebook_items</a>(...) -> GetPricebookItemsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schema for Pricebook Items
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pricebooks.get_pricebooks_id_pricebook_items(
    id=1.1,
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

**id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetPricebooksIdPricebookItemsRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
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

<details><summary><code>client.pricebooks.<a href="src/fern/pricebooks/client.py">get_pricebooks_id_pricebook_items_pricebook_item_id</a>(...) -> GetPricebookItemByIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schema for a Pricebook Item by ID
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.pricebooks.get_pricebooks_id_pricebook_items_pricebook_item_id(
    id=1.1,
    pricebook_item_id=1.1,
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

**id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**pricebook_item_id:** `float` 
    
</dd>
</dl>

<dl>
<dd>

**filter_pricing_tier_id:** `typing.Optional[float]` 
    
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

## Notes
<details><summary><code>client.notes.<a href="src/fern/notes/client.py">get_notes</a>(...) -> GetNotesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schema for Notes
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.notes.get_notes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[GetNotesRequestSortOrder]` 
    
</dd>
</dl>

<dl>
<dd>

**page_cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetNotesRequestSortField]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_entity_id:** `typing.Optional[float]` — The entity id to filter notes by
    
</dd>
</dl>

<dl>
<dd>

**filter_entity_name:** `typing.Optional[GetNotesRequestFilterEntityName]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_created_by_id:** `typing.Optional[float]` — The user id who created the notes to filter by
    
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

## Company
<details><summary><code>client.company.<a href="src/fern/company/client.py">get_company</a>() -> GetCompanyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns company information for the authenticated company.
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
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.company.get_company()

```
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

