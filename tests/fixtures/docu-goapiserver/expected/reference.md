# Reference
## sessions
<details><summary><code>client.sessions.<a href="src/fern/sessions/client.py">post_sessions_v3</a>(...) -> Session</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Authenticate with username and password. A single JSON object is required and unknown properties are rejected. Returns access_token and refresh_token with HTTP 201; V3 has no refresh or logout operation.
</dd>
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

client.sessions.post_sessions_v3(
    username="example.user",
    password="<your-password>",
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

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## schools
<details><summary><code>client.schools.<a href="src/fern/schools/client.py">get_schools_v3</a>(...) -> typing.List[School]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns an unpaginated array; school_ids and only_active are optional filters.
</dd>
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

client.schools.get_schools_v3(
    company_id="11111111-1111-4111-8111-111111111111",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Restrict to these school UUIDs. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**only_active:** `typing.Optional[bool]` — Return active schools only. Only true/1 enables the filter; other values disable it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schools.<a href="src/fern/schools/client.py">get_schools_id_v3</a>(...) -> School</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns 404 when the school does not exist for the requested company.
</dd>
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

client.schools.get_schools_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schools.<a href="src/fern/schools/client.py">patch_schools_id_v3</a>(...) -> School</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires company_id, an authenticated session with schools assigned, and the target school in those assignments. Updates capacity, then reads the school in the requested company. A failed subsequent read can return 404 or 500 after the write has executed.
</dd>
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

client.schools.patch_schools_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    capacity=120,
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**capacity:** `int` — New school capacity; must be greater than zero.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## companies
<details><summary><code>client.companies.<a href="src/fern/companies/client.py">get_companies_id_settings_v3</a>(...) -> CompanySettings</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The path ID is the EMS company UUID. It must match the session company when the session has one. Returns 404 when the company or its settings are absent.
</dd>
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

client.companies.get_companies_id_settings_v3(
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/fern/companies/client.py">get_companies_id_v3</a>(...) -> Company</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The path ID is the EMS company UUID. It must match the session company when the session has one. Returns 404 when the company or its settings are absent.
</dd>
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

client.companies.get_companies_id_v3(
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## rooms
<details><summary><code>client.rooms.<a href="src/fern/rooms/client.py">get_rooms_v3</a>(...) -> typing.List[typing.Optional[Room]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. school_id is required. Returns an unpaginated list.
</dd>
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

client.rooms.get_rooms_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.rooms.<a href="src/fern/rooms/client.py">get_rooms_id_v3</a>(...) -> Room</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. The room ID identifies the room; school_id is not required.
</dd>
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

client.rooms.get_rooms_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## users
<details><summary><code>client.users.<a href="src/fern/users/client.py">get_users_v3</a>(...) -> typing.List[User]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Without email, returns users sorted by updated_at and optionally filters to updated_at strictly after updated_after. When email is supplied, returns zero or one matching user in an array; updated_after is ignored and not validated in that branch.
</dd>
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

client.users.get_users_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    email="user@example.com",
    updated_after=datetime.datetime.fromisoformat("2026-01-01T00:00:00+00:00"),
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Exact email lookup; takes precedence over updated_after.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[datetime.datetime]` — Only users whose non-null updated_at is strictly later than this RFC3339 timestamp; applies only without email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_users_id_v3</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns 404 when the user does not exist for the company.
</dd>
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

client.users.get_users_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## leads
<details><summary><code>client.leads.<a href="src/fern/leads/client.py">get_leads_v3</a>(...) -> GetLeadsV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns paginated lead rows, or paginated LeadStages objects when view=stages.

Normal lookup precedence is ids, then query, then the filtered school collection. ids is limited to 200 UUIDs and missing IDs are omitted. query performs a name search with optional max_results. status, date_from/date_to and age_min/age_max are validated before these branches but only filter the normal school collection; ids and query bypass those filters. Negative ages are accepted for expected children. The age interval defaults to -12 through 180 months. date_to cannot precede date_from, and age_max cannot be smaller than age_min.

view=stages requires the school in the session assignments and accepts only company_id, school_id, view, page and per_page. Any other parameter in this view returns 400.
</dd>
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

client.leads.get_leads_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    date_from=datetime.date.fromisoformat("2026-01-01"),
    date_to=datetime.date.fromisoformat("2026-01-31"),
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID.
    
</dd>
</dl>

<dl>
<dd>

**view:** `typing.Optional[GetLeadsV3RequestView]` — Omit for lead rows; stages includes per-stage timestamps.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[GetLeadsV3RequestFieldsItem, typing.Sequence[GetLeadsV3RequestFieldsItem]]]` — Select response properties. Unknown names return 400. Normal lead representation only; names are case-sensitive. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Read at most 200 lead UUIDs; takes precedence over query. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Name search; used only when ids is omitted.
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]` — Maximum name-search results; 0 keeps the backend default.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetLeadsV3RequestStatus]` — Procare lead status; exact case required. Applies only to normal school collection.
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[datetime.date]` — Inclusive start date in YYYY-MM-DD. Optional created-date window for the normal school collection.
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[datetime.date]` — Inclusive end date in YYYY-MM-DD. Optional created-date window for the normal school collection.
    
</dd>
</dl>

<dl>
<dd>

**age_min:** `typing.Optional[float]` — Minimum child age in months; normal school collection only.
    
</dd>
</dl>

<dl>
<dd>

**age_max:** `typing.Optional[float]` — Maximum child age in months; normal school collection only.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.leads.<a href="src/fern/leads/client.py">patch_leads_v3</a>(...) -> typing.List[LeadStages]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires school_id assigned to the session. The body is an array of 1 to 200 items, each with lead_id and at least one non-null stage. All items are validated before writes. Missing leads are omitted from the response. Repeated lead IDs are allowed; each appears once in the response in first-occurrence order with its final stages. The batch is not atomic: a database failure returns 500 and stops processing after any earlier writes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, BulkLeadStagesItem, UpdateLeadStagesRequestStageTourCompleted
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.leads.patch_leads_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    request=[
        BulkLeadStagesItem(
            lead_id="44444444-4444-4444-8444-444444444444",
            stages=UpdateLeadStagesRequestStageTourCompleted(
                stage_tour_completed=True,
            ),
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[BulkLeadStagesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.leads.<a href="src/fern/leads/client.py">get_leads_id_v3</a>(...) -> GetLeadsIdV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. fields selects properties from the lead projection; unknown fields return 400. Returns 404 when the scoped lead does not exist.
</dd>
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

client.leads.get_leads_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[GetLeadsIdV3RequestFieldsItem, typing.Sequence[GetLeadsIdV3RequestFieldsItem]]]` — Select response properties. Unknown names return 400.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.leads.<a href="src/fern/leads/client.py">get_leads_id_stages_v3</a>(...) -> typing.List[LeadStage]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires school_id assigned to the session. Each stage includes its own state and timestamp. The company lead-stages setting selects the underlying stage source for both reading and writing; it is not a read-only permission.
</dd>
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

client.leads.get_leads_id_stages_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.leads.<a href="src/fern/leads/client.py">patch_leads_id_stages_v3</a>(...) -> typing.List[LeadStage]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires school_id assigned to the session and at least one non-null boolean stage. Unknown properties return 400. Stages are written in the documented schema order. Each stage is a separate write: a later failure returns 404/500 and earlier stages may remain applied; an error response does not include a partial stage list. On success the current stages are read back.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, UpdateLeadStagesRequestStageTourCompleted
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.leads.patch_leads_id_stages_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    request=UpdateLeadStagesRequestStageTourCompleted(
        stage_tour_completed=True,
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateLeadStagesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.leads.<a href="src/fern/leads/client.py">patch_leads_intended_start_date_v3</a>(...) -> UpdateIntendedStartDatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires school_id assigned to the session. At most 200 lead IDs are accepted across all update groups, and duplicates anywhere in the request return 400. Dates must be future YYYY-MM-DD values or TBD. Leads with a CRM/Procare expected start date are not overwritten and are reported in lead_ids_not_updated. Missing lead IDs and leads without raw records are omitted. Per-lead write failures are reported with HTTP 200 in lead_ids_not_updated; a group lookup failure returns 500 after any earlier groups may have been applied.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, IntendedStartDateUpdate
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.leads.patch_leads_intended_start_date_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    updates=[
        IntendedStartDateUpdate(
            lead_ids=[
                "44444444-4444-4444-8444-444444444444"
            ],
            intended_start_date=datetime.date.fromisoformat("2030-09-01"),
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**updates:** `typing.List[IntendedStartDateUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## students
<details><summary><code>client.students.<a href="src/fern/students/client.py">get_students_v3</a>(...) -> GetStudentsV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Returns paginated students. The normal collection includes only Procare Desktop enrollment statuses configured as visible for the school. status defaults to active plus hold; all includes active, hold, inactive and graduate. Unknown status values also fall back to active plus hold.

ids switches to a batch lookup of at most 200 UUIDs and requires school_id; this branch bypasses the normal status selection. Missing IDs are omitted. fields selects JSON properties, case-insensitively, and duplicate field names are removed.
</dd>
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

client.students.get_students_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional batch of at most 200 student UUIDs; requires school_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Normal collection: active, hold, inactive, graduate or all. Omitted/unrecognized values select active plus hold.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[GetStudentsV3RequestFieldsItem, typing.Sequence[GetStudentsV3RequestFieldsItem]]]` — Select response properties. Unknown names return 400. Names are normalized to lowercase. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.students.<a href="src/fern/students/client.py">get_students_id_v3</a>(...) -> GetStudentsIdV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. Returns the full student or the requested field projection. This item read does not apply the collection's session-school assignment check.
</dd>
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

client.students.get_students_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[GetStudentsIdV3RequestFieldsItem, typing.Sequence[GetStudentsIdV3RequestFieldsItem]]]` — Select response properties. Unknown names return 400.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.students.<a href="src/fern/students/client.py">patch_students_id_v3</a>(...) -> UpdateStudentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires school_id assigned to the session and an authenticated user belonging to company_id. Attribution comes from that user; updated_by_email is accepted but ignored. At least one update property is required. Unknown properties return 400. Dates and room UUIDs may be cleared with null or an empty string; omission leaves them unchanged.

Validation uses the resulting student state, including existing values:
- transition_date_2 requires transition_date.
- transition_room_override_id requires transition_date.
- transition_room_2_id requires transition_date_2.
- Effective start date must precede transition_date; transition_date must precede transition_date_2 when present; both transitions must precede the effective withdrawal date.
- Specified room IDs must be active rooms in the student's school.

Returns an update summary containing student_data, not the full GET representation. Unlike the shared write decoder, this handler does not enforce Content-Type. A post-update retrieval failure can return 404 or 500 after the write has executed.
</dd>
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

client.students.patch_students_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    request={"transition_date": "2030-09-01"},
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateStudentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## payments
<details><summary><code>client.payments.<a href="src/fern/payments/client.py">get_payments_v3</a>(...) -> GetPaymentsV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Without group_by, returns sparse payment rows. With group_by and metrics, returns nested PaymentAggregate rows. school_id and school_ids are both applied when provided (their intersection); omitted school filters read the company scope. Row queries support family_id/family_ids; these IDs do not filter the aggregate representation. fields and pagination apply only to rows. Aggregate responses use limit, X-Total-Count and X-Truncated, without Link.

An explicit date range requires both bounds and date_to >= date_from. These date checks occur in the data layer; failures currently produce HTTP 500 rather than 400. last_n_days and explicit bounds can both restrict the result. Item and collection school filters are independent of the session school assignments.
</dd>
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

client.payments.get_payments_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    date_from=datetime.date.fromisoformat("2026-01-01"),
    date_to=datetime.date.fromisoformat("2026-01-31"),
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**school_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**family_id:** `typing.Optional[str]` — Row view only: optional family UUID. When family_ids is also supplied, the reader first restricts to this family; family_ids cannot widen that scope.
    
</dd>
</dl>

<dl>
<dd>

**family_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional family UUIDs; row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[str]` — Case-insensitive family-name substring filter.
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[datetime.date]` — Inclusive start date in YYYY-MM-DD. Optional; both date bounds must be supplied together and date_to must not precede date_from.
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[datetime.date]` — Inclusive end date in YYYY-MM-DD. Optional; both date bounds must be supplied together and date_to must not precede date_from.
    
</dd>
</dl>

<dl>
<dd>

**last_n_days:** `typing.Optional[int]` — Rolling lookback on payment created_at (not transaction_date). Positive values add this filter; zero/negative values do not. May be combined with a transaction-date range.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — Case-insensitive payment state filter.
    
</dd>
</dl>

<dl>
<dd>

**is_posted:** `typing.Optional[bool]` — Filter by posted state; omit for both states. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**successful_only:** `typing.Optional[bool]` — Include payments that are posted or whose normalized state is success, succeeded, completed, paid, posted, processed, settled or state_success. Only true/1 enables the filter; other values disable it.
    
</dd>
</dl>

<dl>
<dd>

**payment_mode:** `typing.Optional[str]` — Case-insensitive payment mode filter.
    
</dd>
</dl>

<dl>
<dd>

**payment_method_sub_kind:** `typing.Optional[str]` — Case-insensitive payment method subtype filter.
    
</dd>
</dl>

<dl>
<dd>

**min_amount:** `typing.Optional[float]` — Inclusive minimum payment amount.
    
</dd>
</dl>

<dl>
<dd>

**max_amount:** `typing.Optional[float]` — Inclusive maximum payment amount.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[GetPaymentsV3RequestFieldsItem, typing.Sequence[GetPaymentsV3RequestFieldsItem]]]` — Select response properties. Unknown names return 400. Default: payment_id, family_id, family_name, transaction_date, amount, total_amount, state. Row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Rows: transaction_date, amount, total_amount, created_at or family_name with _asc/_desc (default transaction_date_desc). Aggregates: group or any supported metric with _asc/_desc. Unrecognized sort keys fall back to the backend default. Aggregate default: count_desc.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[GetPaymentsV3RequestGroupBy]` — Select an aggregate representation; metrics must also be supplied.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[GetPaymentsV3RequestMetricsItem, typing.Sequence[GetPaymentsV3RequestMetricsItem]]]` — Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. Row view only.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 200 are clamped to 200. Row view only.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/fern/payments/client.py">get_payments_id_v3</a>(...) -> Payment</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Only school_id/school_ids and fields affect the item lookup. The shared filter parser still validates supplied family IDs, last_n_days, is_posted and amount bounds, but collection filters do not narrow the item. Returns 404 when no payment matches its ID and school scope.
</dd>
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

client.payments.get_payments_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**school_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[GetPaymentsIdV3RequestFieldsItem, typing.Sequence[GetPaymentsIdV3RequestFieldsItem]]]` — Select response properties. Unknown names return 400. Default: payment_id, family_id, family_name, transaction_date, amount, total_amount, state.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## enrollments
<details><summary><code>client.enrollments.<a href="src/fern/enrollments/client.py">get_enrollments_v3</a>(...) -> GetEnrollmentsV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. The response representation is selected in this order:

| Selection | Response | Date selectors |
| --- | --- | --- |
| view=trend | EnrollmentTrend array | Optional period_from/period_to |
| group_by=period (unless trend) | EnrollmentPeriodAnalytics array | year_from/year_to |
| view=analytics, group_by=month | EnrollmentAnalytics array | period_from/period_to |
| Default: view=basic, group_by=month | EnrollmentMonthly array | period_from/period_to |

Monthly basic/analytics default to 2023-01 through the current month. Period analytics defaults to 2023 through the current year. Trend uses the available calculated periods when bounds are omitted. No pagination is implemented. Each representation returns its row count in X-Total-Count. For view=trend, omit both range bounds or provide both; endpoints must lie within the available horizon. Incomplete, invalid, inverted or out-of-horizon trend ranges fail in the data layer and currently return HTTP 500.
</dd>
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

client.enrollments.get_enrollments_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID.
    
</dd>
</dl>

<dl>
<dd>

**view:** `typing.Optional[GetEnrollmentsV3RequestView]` — Select the representation.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[GetEnrollmentsV3RequestGroupBy]` — period implies period analytics unless view=trend.
    
</dd>
</dl>

<dl>
<dd>

**period_from:** `typing.Optional[str]` — First monthly period for monthly or trend views.
    
</dd>
</dl>

<dl>
<dd>

**period_to:** `typing.Optional[str]` — Last monthly period for monthly or trend views.
    
</dd>
</dl>

<dl>
<dd>

**year_from:** `typing.Optional[str]` — First year for group_by=period; defaults to 2023.
    
</dd>
</dl>

<dl>
<dd>

**year_to:** `typing.Optional[str]` — Last year for group_by=period; defaults to the current year.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## family_balances
<details><summary><code>client.family_balances.<a href="src/fern/family_balances/client.py">get_family_balances_v3</a>(...) -> GetFamilyBalancesV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Default: sparse balance rows, one per family, with optional fields. group_by plus metrics selects nested FamilyBalanceAggregate rows; family_ids does not filter aggregates. school_id and school_ids are both applied when provided (their intersection).

view=transactions takes precedence and returns FamilyLedger objects (family_id, student_ids, transactions). This view requires school_id assigned to the session. It ignores balance filters, fields, school_ids and grouping after the shared filter parser validates supplied filter values. last_n_days defaults to 30 and is clamped to 0..365. Pagination applies to families, not to transactions inside each family.

Balance rows use per_page capped at 200; transaction-family pages use 500. Aggregates use limit and X-Truncated without Link.
</dd>
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

client.family_balances.get_family_balances_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**school_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**family_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional family UUIDs; balance row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**family_name:** `typing.Optional[str]` — Case-insensitive family-name substring filter; balance rows and aggregates.
    
</dd>
</dl>

<dl>
<dd>

**balance_min:** `typing.Optional[float]` — Inclusive minimum balance; balance rows and aggregates.
    
</dd>
</dl>

<dl>
<dd>

**balance_max:** `typing.Optional[float]` — Inclusive maximum balance; balance rows and aggregates.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[GetFamilyBalancesV3RequestFieldsItem, typing.Sequence[GetFamilyBalancesV3RequestFieldsItem]]]` — Select response properties. Unknown names return 400. Default: family_id, family_name, balance, transaction_date. Balance row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Rows: balance, family_name or transaction_date with _asc/_desc. Aggregates: group or a supported metric with _asc/_desc. Unsupported keys use the backend default. Defaults: balance_desc for rows, count_desc for aggregates.
    
</dd>
</dl>

<dl>
<dd>

**view:** `typing.Optional[GetFamilyBalancesV3RequestView]` — Read per-family transaction ledgers; takes precedence over grouping.
    
</dd>
</dl>

<dl>
<dd>

**last_n_days:** `typing.Optional[int]` — Transactions only: defaults to 30 and clamps to 0 through 365.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[GetFamilyBalancesV3RequestGroupBy]` — Select an aggregate representation; metrics must also be supplied.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[GetFamilyBalancesV3RequestMetricsItem, typing.Sequence[GetFamilyBalancesV3RequestMetricsItem]]]` — Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. Balance rows clamp at 200; view=transactions instead clamps at 500.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 200 are clamped to 200. Balance rows clamp at 200; view=transactions instead clamps at 500.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.family_balances.<a href="src/fern/family_balances/client.py">get_family_balances_id_transactions_v3</a>(...) -> typing.List[FamilyLedger]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires school_id assigned to the session. Returns an unpaginated array of per-family ledger objects, each containing student_ids and transactions; it is not a flat transaction array. The path ID is the family UUID. No matches produce an empty array rather than 404. last_n_days defaults to 30 and is clamped to 0..365.
</dd>
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

client.family_balances.get_family_balances_id_transactions_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**last_n_days:** `typing.Optional[int]` — Lookback in days; default 30, clamped to 0..365.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.family_balances.<a href="src/fern/family_balances/client.py">get_family_balances_id_v3</a>(...) -> FamilyBalance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. The path ID is the family UUID. school_id/school_ids narrow the lookup and fields selects the response properties. Other collection filters do not apply, although the shared parser still validates supplied family_ids and balance bounds. No matching family balance returns 404.
</dd>
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

client.family_balances.get_family_balances_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**school_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional school UUID filter. When school_id is also supplied, both filters apply. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[GetFamilyBalancesIdV3RequestFieldsItem, typing.Sequence[GetFamilyBalancesIdV3RequestFieldsItem]]]` — Select response properties. Unknown names return 400. Default: family_id, family_name, balance, transaction_date.  Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## pre_registration_fallout
<details><summary><code>client.pre_registration_fallout.<a href="src/fern/pre_registration_fallout/client.py">get_pre_registration_fallout_v3</a>(...) -> GetPreRegistrationFalloutV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Omitting view returns a PreRegistrationFalloutReport object containing years, school_summaries and total_summary. view=students returns a paginated array of PreRegistrationFalloutStudent.

The report accepts only company_id, school_id and view. The students view additionally accepts year, query, withdrew_only, sort_by, page and per_page. Any other parameter, including a students-only parameter on the report view, returns 400. year defaults to the current year; all includes every supported year. Supported years run from 2024 to the current year. Pagination headers are emitted only for view=students.
</dd>
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

client.pre_registration_fallout.get_pre_registration_fallout_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**view:** `typing.Optional[GetPreRegistrationFalloutV3RequestView]` — Omit for the full report; students selects paginated detail.
    
</dd>
</dl>

<dl>
<dd>

**year:** `typing.Optional[str]` — Students view only: a year from 2024 through the current year, or all (case-insensitive). Defaults to the current year.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Students view only: student search text.
    
</dd>
</dl>

<dl>
<dd>

**withdrew_only:** `typing.Optional[bool]` — Students view only: restrict to withdrawals in the same year. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetPreRegistrationFalloutV3RequestSortBy]` — Students view only: sort column with _asc/_desc.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. Applies only to view=students.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. Applies only to view=students.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## absences
<details><summary><code>client.absences.<a href="src/fern/absences/client.py">get_absences_v3</a>(...) -> typing.List[Absence]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Provide school_id or student_id; student_id takes precedence when both are supplied (both IDs are still validated). Provide date_from, optionally date_to (defaults to today), OR a positive last_n_days. last_n_days cannot be combined with either date bound. Default order is date descending.
</dd>
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

client.absences.get_absences_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    date_from=datetime.date.fromisoformat("2026-01-01"),
    date_to=datetime.date.fromisoformat("2026-01-31"),
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**student_id:** `typing.Optional[str]` — Required when school_id is omitted; takes precedence over school_id.
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[datetime.date]` — Inclusive start date in YYYY-MM-DD. Required date_from unless last_n_days is supplied; date_to defaults to today.
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[datetime.date]` — Inclusive end date in YYYY-MM-DD. Required date_from unless last_n_days is supplied; date_to defaults to today.
    
</dd>
</dl>

<dl>
<dd>

**last_n_days:** `typing.Optional[int]` — Rolling date window; mutually exclusive with explicit dates.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetAbsencesV3RequestSortBy]` — Sort by a supported column with an _asc or _desc suffix.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## waitlist
<details><summary><code>client.waitlist.<a href="src/fern/waitlist/client.py">get_waitlist_v3</a>(...) -> typing.List[Waitlist]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Waitlist entries with room eligibility derived from the preferred start date.
</dd>
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

client.waitlist.get_waitlist_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Search text passed to the waitlist student lookup.
    
</dd>
</dl>

<dl>
<dd>

**has_alerts:** `typing.Optional[bool]` — Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetWaitlistV3RequestSortBy]` — Sort by a supported column with an _asc or _desc suffix.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.waitlist.<a href="src/fern/waitlist/client.py">get_waitlist_student_id_v3</a>(...) -> Waitlist</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.
</dd>
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

client.waitlist.get_waitlist_student_id_v3(
    student_id="student_id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**student_id:** `str` — UUID identifying this student.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.waitlist.<a href="src/fern/waitlist/client.py">patch_waitlist_student_id_v3</a>(...) -> Waitlist</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The student must exist in Waitlist onboarding status and belong to a school assigned to the session. preferred_start_date must be later than today. Recomputes and returns the waitlist entry and room eligibility. Clearing this date is not supported. The update may have executed if the subsequent read returns 500.
</dd>
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

client.waitlist.patch_waitlist_student_id_v3(
    student_id="student_id",
    company_id="11111111-1111-4111-8111-111111111111",
    preferred_start_date=datetime.date.fromisoformat("2030-09-01"),
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

**student_id:** `str` — UUID identifying this student.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**preferred_start_date:** `datetime.date` — Required future date. Today, past dates, empty strings and null are rejected.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## billing_plans
<details><summary><code>client.billing_plans.<a href="src/fern/billing_plans/client.py">get_billing_plans_v3</a>(...) -> GetBillingPlansV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns consolidated billing-plan rows, or nested BillingPlanAggregate rows when group_by and metrics are supplied. school_id is always required. A consolidated row keeps the ID of the first plan in its group.

Rows support plan_status, room filters, query, has_alerts, active_rooms_only and pagination; sorting rows returns 400. Aggregates use school, room filters, plan_status (default active), group_by, metrics, sort_by and limit. query, has_alerts and active_rooms_only do not affect aggregate results, although boolean values are parsed and validated. X-Has-Alerts applies only to row responses; X-Room-Filter-Count and X-Truncated apply only to aggregates.
</dd>
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

client.billing_plans.get_billing_plans_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID.
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Alias combined with room_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**room_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional room UUID filters, combined with room_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**plan_status:** `typing.Optional[str]` — Free-text plan status. Aggregate view defaults to active when omitted.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — Row view only: search text.
    
</dd>
</dl>

<dl>
<dd>

**has_alerts:** `typing.Optional[bool]` — Row view only: return only plans with alerts when true. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**active_rooms_only:** `typing.Optional[bool]` — Row view only: restrict to active rooms. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetBillingPlansV3RequestSortBy]` — Aggregate view only. Sending sort_by without group_by returns 400.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[GetBillingPlansV3RequestGroupBy]` — Select an aggregate representation; metrics must also be supplied.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[GetBillingPlansV3RequestMetricsItem, typing.Sequence[GetBillingPlansV3RequestMetricsItem]]]` — Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. Row view only.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. Row view only.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing_plans.<a href="src/fern/billing_plans/client.py">get_billing_plans_id_v3</a>(...) -> BillingPlan</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Requires school_id. The ID is the consolidated row ID returned by the collection (the first plan ID in a group). Collection filters do not affect the lookup, though the shared parser still validates any supplied room IDs and boolean filters. Returns 404 when the school has no matching consolidated plan.
</dd>
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

client.billing_plans.get_billing_plans_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## spaces
<details><summary><code>client.spaces.<a href="src/fern/spaces/client.py">get_spaces_v3</a>(...) -> SpacesSnapshot</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires schools assigned to the session. Only company_id and optional school_id are accepted; all other parameters return 400. With school_id, the school must be assigned to the session and its name selects the snapshot entry. Without school_id, the current implementation matches session school entries directly against the snapshot keys, which are school names; UUID-based assignments can therefore yield an empty map. Returns a nested map without pagination or collection headers.
</dd>
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

client.spaces.get_spaces_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/fern/spaces/client.py">get_spaces_detailed_list_v3</a>(...) -> GetSpacesDetailedListV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. The selected representation determines accepted parameters; every unsupported parameter returns 400.

| Representation | Selection | Required scope and dates | Additional parameters |
| --- | --- | --- | --- |
| Rows | Omit view/group_by/metrics | school_id, period | room_id, room_ids, fields, sort_by, page, per_page |
| Aggregate | Omit view; set group_by and metrics | school_id, period | room_ids, sort_by, limit |
| Trend | view=trend | school_id, room_id | period_from, period_to, fields |
| Projection | view=projection | school_id | room_id, room_ids, period_from, period_to, fields |
| Periods | view=periods | Session schools | school_ids, only_active |

All modes accept company_id and view. Periods rejects school_id; use school_ids instead. Rows are paginated. Aggregate returns flat properties for the grouping key and metrics, with default limit 50 and cap 200. Trend, projection and periods are unpaginated. Omitting both range bounds uses the available calculated horizon. If filtering, both bounds must be present and within that horizon. An inverted range returns 400; a single bound or an out-of-horizon range fails in the data layer and currently returns 500. Projection always returns one row per room and period. Without a room filter it includes all rooms. The default projection fields omit room_id and room_name, so request those fields to distinguish rooms. fields differs between SpacesRow (rows/trend) and SpacesProjection. occupancy_rate is a ratio (0.8 means 80%).
</dd>
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

client.spaces.get_spaces_detailed_list_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**view:** `typing.Optional[GetSpacesDetailedListV3RequestView]` — Omit for paginated rows or aggregation selected with group_by.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Required for rows and aggregates; not accepted in the other views.
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[str]` — Optional for rows/projection; required for trend; rejected for aggregates and periods.
    
</dd>
</dl>

<dl>
<dd>

**room_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional for rows, aggregates and projection. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**school_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Periods view only; each ID must be assigned to the session. Defaults to all assigned schools. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**only_active:** `typing.Optional[bool]` — Periods view only: include only active schools. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**period_from:** `typing.Optional[str]` — Trend/projection only: optional first monthly period. Omit both bounds or provide both within the available horizon.
    
</dd>
</dl>

<dl>
<dd>

**period_to:** `typing.Optional[str]` — Trend/projection only: optional last monthly period; must not precede period_from. Omit both bounds or provide both within the available horizon.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[GetSpacesDetailedListV3RequestFieldsItem, typing.Sequence[GetSpacesDetailedListV3RequestFieldsItem]]]` — Select response properties. Unknown names return 400. Rows and trend use SpacesRow fields; projection uses SpacesProjection fields. Invalid fields for the selected view return 400. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Rows: room_name, available_spaces, open_spaces, occupied_spaces or occupancy_rate with _asc/_desc. Aggregates: sum_available_spaces, sum_open_spaces, sum_occupied_spaces, sum_closed_spaces, sum_unavailable_spaces, capacity or occupancy_rate with _asc/_desc. Other views reject sort_by. Defaults: room_name_asc for rows; sum_open_spaces_desc for aggregates.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[GetSpacesDetailedListV3RequestGroupBy]` — Select an aggregate representation; metrics must also be supplied.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[GetSpacesDetailedListV3RequestMetricsItem, typing.Sequence[GetSpacesDetailedListV3RequestMetricsItem]]]` — Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. If provided, must be positive.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. Rows only; other representations reject pagination parameters.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 200 are clamped to 200. Rows only; other representations reject pagination parameters.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.spaces.<a href="src/fern/spaces/client.py">patch_spaces_closed_spaces_v3</a>(...) -> UpdateClosedSpacesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires an authenticated user in the Operations or Admin group, school_id assigned to the session, and room IDs belonging to that school. Each room_id/period pair must be unique in the body. closed_spaces must be nonnegative and no greater than room capacity. Positive values create/update overrides; zero removes an existing override. All cells are validated before writes. Upserts and deletes execute separately; a later failure may leave earlier changes applied. modified counts upserts plus existing rows deleted (a zero for a missing override does not increase it).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ClosedSpaceCell
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.spaces.patch_spaces_closed_spaces_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    closed_spaces=[
        ClosedSpaceCell(
            room_id="55555555-5555-4555-8555-555555555555",
            period="2030-09",
            closed_spaces=2,
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**closed_spaces:** `typing.List[ClosedSpaceCell]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## enrollment_tracker
<details><summary><code>client.enrollment_tracker.<a href="src/fern/enrollment_tracker/client.py">get_enrollment_tracker_v3</a>(...) -> EnrollmentTracker</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires school_id assigned to the session. Returns the school tracker grid and computed enrollment information, optionally narrowed by room_id and monthly period. Returns 404 if the tracker is absent.
</dd>
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

client.enrollment_tracker.get_enrollment_tracker_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[str]` — Optional room UUID.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[str]` — Optional monthly period in YYYY-MM.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## efficiency_ratios
<details><summary><code>client.efficiency_ratios.<a href="src/fern/efficiency_ratios/client.py">get_efficiency_ratios_v3</a>(...) -> typing.List[EfficiencyRatio]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Returns ratios sorted by school_name ascending. No school_id filter or pagination is implemented.
</dd>
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

client.efficiency_ratios.get_efficiency_ratios_v3(
    company_id="11111111-1111-4111-8111-111111111111",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## procare_messages
<details><summary><code>client.procare_messages.<a href="src/fern/procare_messages/client.py">get_procare_messages_v3</a>(...) -> typing.List[ProcareMessageTask]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists incomplete tasks in the global message queue. Tasks are not scoped to a company or school. status=incomplete is required; completed-task history is not available from this operation. last_n_hours defaults to 6 and accepts positive fractional hours. Returns an unpaginated array.
</dd>
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
from fern.procare_messages import GetProcareMessagesV3RequestStatus

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.procare_messages.get_procare_messages_v3(
    status=GetProcareMessagesV3RequestStatus.INCOMPLETE,
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

**status:** `GetProcareMessagesV3RequestStatus` — Required queue selection; case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**last_n_hours:** `typing.Optional[float]` — Look back this many hours; must be greater than zero.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.procare_messages.<a href="src/fern/procare_messages/client.py">post_procare_messages_v3</a>(...) -> ProcareMessageCreated</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queues office_chat or classroom_chat delivery through the configured message service. Requires authentication but does not take company_id or enforce a company/school scope here. HTTP 202 means the task was accepted, not that delivery has finished. Poll the relative URL in Location for status. Non-2xx upstream responses other than 404 become 502.
</dd>
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
from fern.procare_messages import CreateProcareMessageRequestType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.procare_messages.post_procare_messages_v3(
    type=CreateProcareMessageRequestType.OFFICE_CHAT,
    username="example.user",
    password="<procare-password>",
    students_ids=[
        "33333333-3333-4333-8333-333333333333"
    ],
    message="Example reminder.",
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

**type:** `CreateProcareMessageRequestType` — Case-insensitive; surrounding whitespace is ignored.
    
</dd>
</dl>

<dl>
<dd>

**students_ids:** `typing.List[str]` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Procare username forwarded to the message service; not required by the V3 handler.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Procare password forwarded to the message service; not required by the V3 handler.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.procare_messages.<a href="src/fern/procare_messages/client.py">get_procare_messages_task_id_v3</a>(...) -> typing.Optional[ProcareMessageStatus]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reads a task in the global queue. No company/school filter is applied. A service-side 404 becomes a JSON 404; other unsuccessful or malformed upstream responses become 502. The bundled service returns HTTP 200 with JSON null for an unknown task; V3 preserves that result.
</dd>
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

client.procare_messages.get_procare_messages_task_id_v3(
    task_id="task_id",
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

**task_id:** `str` — Task identifier returned by POST /procare_messages; not required to be a UUID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## attendances
<details><summary><code>client.attendances.<a href="src/fern/attendances/client.py">get_attendances_v3</a>(...) -> GetAttendancesV3Response</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Provide date_from AND date_to, or a positive last_n_days; mixing them returns 400. Defaults min_hours to 2; records below that threshold are excluded. room_id/room_ids and student_id/student_ids are merged. Row responses are sparse Attendance objects and support fields and pagination; sort_by on rows returns 400. group_by plus metrics selects nested AttendanceAggregate rows with a limit instead of pagination. Room/student filter counts, when positive, are returned in headers.
</dd>
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

client.attendances.get_attendances_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    date_from=datetime.date.fromisoformat("2026-01-01"),
    date_to=datetime.date.fromisoformat("2026-01-31"),
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID.
    
</dd>
</dl>

<dl>
<dd>

**room_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Alias combined with room_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**room_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional room UUIDs; combined with room_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**student_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Alias combined with student_ids. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**student_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional student UUIDs; combined with student_id. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[datetime.date]` — Inclusive start date in YYYY-MM-DD. Both dates required unless last_n_days is supplied.
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[datetime.date]` — Inclusive end date in YYYY-MM-DD. Both dates required unless last_n_days is supplied.
    
</dd>
</dl>

<dl>
<dd>

**last_n_days:** `typing.Optional[int]` — Positive rolling-window length; cannot be combined with either explicit date bound.
    
</dd>
</dl>

<dl>
<dd>

**min_hours:** `typing.Optional[float]` — Minimum hours attended per record. Use zero to include records below the historical two-hour threshold.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[GetAttendancesV3RequestFieldsItem, typing.Sequence[GetAttendancesV3RequestFieldsItem]]]` — Select response properties. Unknown names return 400. Default: student_id, date, room_id, room_name, hours_attended. Row view only. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetAttendancesV3RequestSortBy]` — Aggregate view only; sending sort_by without group_by returns 400. Default group_asc.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[GetAttendancesV3RequestGroupBy]` — Select an aggregate representation; metrics must also be supplied.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Union[GetAttendancesV3RequestMetricsItem, typing.Sequence[GetAttendancesV3RequestMetricsItem]]]` — Metrics to calculate; required with group_by and invalid without it. Accepts repeated query parameters or comma-separated values; empty entries are dropped and surrounding whitespace is trimmed.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Aggregate result limit. Defaults to 50 and clamps values above 200 to 200. Zero and negative values use the default.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. Row view only.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 200 are clamped to 200. Row view only.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## billing_attendance_audits
<details><summary><code>client.billing_attendance_audits.<a href="src/fern/billing_attendance_audits/client.py">get_billing_attendance_audits_v3</a>(...) -> typing.List[BillingAttendanceAudit]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns attendance checked against billing, including unpaid_day. The backend supports a rolling window only: last_n_days is required. Each result is an attendance row flattened from its student record.
</dd>
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

client.billing_attendance_audits.get_billing_attendance_audits_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    last_n_days=1,
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID.
    
</dd>
</dl>

<dl>
<dd>

**last_n_days:** `int` — Required positive rolling-window length in days.
    
</dd>
</dl>

<dl>
<dd>

**unpaid_only:** `typing.Optional[bool]` — Restrict to unpaid attendance. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## classroom_attendance
<details><summary><code>client.classroom_attendance.<a href="src/fern/classroom_attendance/client.py">get_classroom_attendance_v3</a>(...) -> ClassroomAttendance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Daily classroom counters and student states, with their synchronization timestamp. date defaults to the current server date. Returns 404 if no snapshot exists.
</dd>
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

client.classroom_attendance.get_classroom_attendance_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
    date=datetime.date.fromisoformat("2026-01-15"),
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID.
    
</dd>
</dl>

<dl>
<dd>

**date:** `typing.Optional[datetime.date]` — Snapshot calendar date; defaults to today.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## activities_summary
<details><summary><code>client.activities_summary.<a href="src/fern/activities_summary/client.py">get_activities_summary_v3</a>(...) -> typing.List[ActivitySummaryKid]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Authenticated proxy to the activity service. company_id and school_id are required nonempty strings. This handler does not validate them as UUIDs or apply session company/school equality checks. It forwards the upstream status, Content-Type and body. Local validation and gateway errors are plain text; no pagination or count headers are added. Returns a flat kid-summary array sorted by kid key.
</dd>
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

client.activities_summary.get_activities_summary_v3(
    company_id="company_id",
    school_id="school_id",
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

**company_id:** `str` — Required company identifier forwarded to the source.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — Required school identifier forwarded to the source.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## activity_details
<details><summary><code>client.activity_details.<a href="src/fern/activity_details/client.py">get_activity_details_v3</a>(...) -> typing.List[typing.Optional[typing.List[DailyActivity]]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Authenticated proxy to the activity service. company_id and school_id are required nonempty strings. This handler does not validate them as UUIDs or apply session company/school equality checks. It forwards the upstream status, Content-Type and body. Local validation and gateway errors are plain text; no pagination or count headers are added. Returns an array of per-kid activity arrays, not a flat activity array. Kids are sorted by key when kid_id is omitted. A missing kid may produce a null inner array; filtering with since can produce an empty array.
</dd>
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

client.activity_details.get_activity_details_v3(
    company_id="company_id",
    school_id="school_id",
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

**company_id:** `str` — Required company identifier forwarded to the source.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — Required school identifier forwarded to the source.
    
</dd>
</dl>

<dl>
<dd>

**kid_id:** `typing.Optional[str]` — Optional kid UUID. If absent, returns activity lists for all kids in the school.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` — Optional RFC3339 timestamp to filter activities.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## data_refresh
<details><summary><code>client.data_refresh.<a href="src/fern/data_refresh/client.py">get_data_refresh_v3</a>(...) -> DataRefresh</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest recorded company process. Returns 404 when no process is available. last_data_refresh_at is a display timestamp rather than an RFC3339 value.
</dd>
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

client.data_refresh.get_data_refresh_v3(
    company_id="11111111-1111-4111-8111-111111111111",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_refresh.<a href="src/fern/data_refresh/client.py">get_data_refresh_details_v3</a>(...) -> typing.List[SchoolRefresh]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest school process statuses grouped by school. An explicit school_id must be assigned to the session. Without school_id, the current process lookup requests company-wide statuses. The school-name lookup uses the session school assignments. Returns an array without pagination headers.
</dd>
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

client.data_refresh.get_data_refresh_details_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## sibling_discounts
<details><summary><code>client.sibling_discounts.<a href="src/fern/sibling_discounts/client.py">get_sibling_discounts_v3</a>(...) -> typing.List[SiblingDiscount]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Students from families with siblings and resolved billing-plan discounts.
</dd>
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

client.sibling_discounts.get_sibling_discounts_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetSiblingDiscountsV3RequestStatus]` — Optional status filter, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**sibling_filter:** `typing.Optional[GetSiblingDiscountsV3RequestSiblingFilter]` — Optional sibling-family filter, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**active_sibling_filter:** `typing.Optional[GetSiblingDiscountsV3RequestActiveSiblingFilter]` — Require all siblings to be active, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**has_alerts:** `typing.Optional[bool]` — Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetSiblingDiscountsV3RequestSortBy]` — Sort by a supported column with an _asc or _desc suffix.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sibling_discounts.<a href="src/fern/sibling_discounts/client.py">get_sibling_discounts_student_id_v3</a>(...) -> SiblingDiscount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.
</dd>
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

client.sibling_discounts.get_sibling_discounts_student_id_v3(
    student_id="student_id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**student_id:** `str` — UUID identifying this student.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## new_start_tracker
<details><summary><code>client.new_start_tracker.<a href="src/fern/new_start_tracker/client.py">get_new_start_tracker_v3</a>(...) -> typing.List[NewStartStudent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Start-date invoicing, service windows, and pro-rate information per student.
</dd>
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

client.new_start_tracker.get_new_start_tracker_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**ems_student_status:** `typing.Optional[GetNewStartTrackerV3RequestEmsStudentStatus]` — Optional onboarding status, matched case-insensitively.
    
</dd>
</dl>

<dl>
<dd>

**has_alerts:** `typing.Optional[bool]` — Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetNewStartTrackerV3RequestSortBy]` — Sort by a supported column with an _asc or _desc suffix.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.new_start_tracker.<a href="src/fern/new_start_tracker/client.py">get_new_start_tracker_student_id_v3</a>(...) -> NewStartStudent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.
</dd>
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

client.new_start_tracker.get_new_start_tracker_student_id_v3(
    student_id="student_id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**student_id:** `str` — UUID identifying this student.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## withdrawal_tracker
<details><summary><code>client.withdrawal_tracker.<a href="src/fern/withdrawal_tracker/client.py">get_withdrawal_tracker_v3</a>(...) -> typing.List[WithdrawalStudent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Withdrawal invoicing, deposit and service-window information per student.
</dd>
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

client.withdrawal_tracker.get_withdrawal_tracker_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**ems_student_status:** `typing.Optional[GetWithdrawalTrackerV3RequestEmsStudentStatus]` — Optional onboarding status, matched case-insensitively.
    
</dd>
</dl>

<dl>
<dd>

**withdrawal_date_filter:** `typing.Optional[GetWithdrawalTrackerV3RequestWithdrawalDateFilter]` — Choose which withdrawal date supplies the tracker.
    
</dd>
</dl>

<dl>
<dd>

**has_alerts:** `typing.Optional[bool]` — Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetWithdrawalTrackerV3RequestSortBy]` — Sort by a supported column with an _asc or _desc suffix.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.withdrawal_tracker.<a href="src/fern/withdrawal_tracker/client.py">get_withdrawal_tracker_student_id_v3</a>(...) -> WithdrawalStudent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.
</dd>
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

client.withdrawal_tracker.get_withdrawal_tracker_student_id_v3(
    student_id="student_id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**student_id:** `str` — UUID identifying this student.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## transition_tracker
<details><summary><code>client.transition_tracker.<a href="src/fern/transition_tracker/client.py">get_transition_tracker_v3</a>(...) -> typing.List[TransitionStudent]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The session must have schools assigned. Results are restricted to those schools; an optional school_id narrows this scope and must be assigned to the session. Student transition date, destination room, days until transition, and alert information.
</dd>
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

client.transition_tracker.get_transition_tracker_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `typing.Optional[str]` — School UUID. Must be assigned to the authenticated session. Omit to use the operation's documented company/session scope.
    
</dd>
</dl>

<dl>
<dd>

**ems_student_status:** `typing.Optional[GetTransitionTrackerV3RequestEmsStudentStatus]` — Optional onboarding status, matched case-insensitively.
    
</dd>
</dl>

<dl>
<dd>

**has_alerts:** `typing.Optional[bool]` — Return only entries with alerts when true; false leaves all entries eligible. Accepts true/1 and false/0, case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[GetTransitionTrackerV3RequestSortBy]` — Sort by a supported column with an _asc or _desc suffix.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transition_tracker.<a href="src/fern/transition_tracker/client.py">get_transition_tracker_student_id_v3</a>(...) -> TransitionStudent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The student UUID identifies the entry. Requires schools assigned to the session. Collection filters do not apply. A student outside the session schools returns 403; no applicable entry returns 404.
</dd>
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

client.transition_tracker.get_transition_tracker_student_id_v3(
    student_id="student_id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**student_id:** `str` — UUID identifying this student.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## gusto_companies
<details><summary><code>client.gusto_companies.<a href="src/fern/gusto_companies/client.py">get_gusto_companies_v3</a>(...) -> typing.List[GustoCompany]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns the company catalog as an unpaginated array.
</dd>
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

client.gusto_companies.get_gusto_companies_v3(
    company_id="11111111-1111-4111-8111-111111111111",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gusto_companies.<a href="src/fern/gusto_companies/client.py">get_gusto_companies_id_time_off_v3</a>(...) -> typing.List[EmployeeTimeOff]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. First verifies that the Gusto company belongs to company_id, returning 404 if absent. Defaults date_to to today and date_from to three calendar months before date_to. date_to cannot precede date_from. Sorts by effective_time ascending, breaking ties by employee_id.
</dd>
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

client.gusto_companies.get_gusto_companies_id_time_off_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
    date_from=datetime.date.fromisoformat("2026-01-01"),
    date_to=datetime.date.fromisoformat("2026-01-31"),
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**employee_id:** `typing.Optional[str]` — Restrict to one employee UUID.
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[datetime.date]` — Inclusive start date in YYYY-MM-DD. Both bounds are optional; see operation defaults.
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[datetime.date]` — Inclusive end date in YYYY-MM-DD. Both bounds are optional; see operation defaults.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — One-based page number. 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Items per page; values greater than 500 are clamped to 500. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gusto_companies.<a href="src/fern/gusto_companies/client.py">get_gusto_companies_id_v3</a>(...) -> GustoCompany</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. The ID is the internal record UUID. Records outside the requested company return 404.
</dd>
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

client.gusto_companies.get_gusto_companies_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## gusto_employees
<details><summary><code>client.gusto_employees.<a href="src/fern/gusto_employees/client.py">get_gusto_employees_v3</a>(...) -> typing.List[GustoEmployee]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns the company catalog as an unpaginated array.
</dd>
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

client.gusto_employees.get_gusto_employees_v3(
    company_id="11111111-1111-4111-8111-111111111111",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gusto_employees.<a href="src/fern/gusto_employees/client.py">get_gusto_employees_id_v3</a>(...) -> GustoEmployee</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. The ID is the internal record UUID. Records outside the requested company return 404.
</dd>
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

client.gusto_employees.get_gusto_employees_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## gusto_contractors
<details><summary><code>client.gusto_contractors.<a href="src/fern/gusto_contractors/client.py">get_gusto_contractors_v3</a>(...) -> typing.List[GustoContractor]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns the company catalog as an unpaginated array.
</dd>
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

client.gusto_contractors.get_gusto_contractors_v3(
    company_id="11111111-1111-4111-8111-111111111111",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gusto_contractors.<a href="src/fern/gusto_contractors/client.py">get_gusto_contractors_id_v3</a>(...) -> GustoContractor</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. The ID is the internal record UUID. Records outside the requested company return 404.
</dd>
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

client.gusto_contractors.get_gusto_contractors_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## gusto_payrolls
<details><summary><code>client.gusto_payrolls.<a href="src/fern/gusto_payrolls/client.py">get_gusto_payrolls_v3</a>(...) -> typing.Optional[typing.List[Payroll]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a school assigned to the session. period selects one pay-period end date; period_from and period_to select a range. period cannot be combined with either range bound, and period_to cannot precede period_from. Returns an unpaginated array without collection metadata headers. Omitting selectors reads the available payroll records for the school.
</dd>
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

client.gusto_payrolls.get_gusto_payrolls_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[datetime.date]` — Exact pay-period end date; mutually exclusive with range bounds.
    
</dd>
</dl>

<dl>
<dd>

**period_from:** `typing.Optional[datetime.date]` — Earliest pay-period end date, inclusive.
    
</dd>
</dl>

<dl>
<dd>

**period_to:** `typing.Optional[datetime.date]` — Latest pay-period end date, inclusive.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gusto_payrolls.<a href="src/fern/gusto_payrolls/client.py">get_gusto_payrolls_totals_v3</a>(...) -> typing.Optional[typing.List[PayrollTotal]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a school assigned to the session. period selects one pay-period end date; period_from and period_to select a range. period cannot be combined with either range bound, and period_to cannot precede period_from. Returns an unpaginated array without collection metadata headers. When selectors are omitted the totals return the most recent nine periods. Any period selector removes that cap.
</dd>
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

client.gusto_payrolls.get_gusto_payrolls_totals_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[datetime.date]` — Exact pay-period end date; mutually exclusive with range bounds.
    
</dd>
</dl>

<dl>
<dd>

**period_from:** `typing.Optional[datetime.date]` — Earliest pay-period end date, inclusive.
    
</dd>
</dl>

<dl>
<dd>

**period_to:** `typing.Optional[datetime.date]` — Latest pay-period end date, inclusive.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## procare_staff
<details><summary><code>client.procare_staff.<a href="src/fern/procare_staff/client.py">get_procare_staff_v3</a>(...) -> typing.Optional[typing.List[ProcareStaff]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires school_id assigned to the session. Returns the school staff array directly, without pagination or X-Total-Count.
</dd>
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

client.procare_staff.get_procare_staff_v3(
    company_id="11111111-1111-4111-8111-111111111111",
    school_id="22222222-2222-4222-8222-222222222222",
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

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**school_id:** `str` — School UUID. Must be assigned to the authenticated session.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.procare_staff.<a href="src/fern/procare_staff/client.py">get_procare_staff_id_v3</a>(...) -> ProcareStaff</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scoped to company_id; the handler does not restrict this read to the session school assignments. Returns the staff record directly. A missing record raises a data-layer error which this handler currently reports as HTTP 500.
</dd>
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

client.procare_staff.get_procare_staff_id_v3(
    id="id",
    company_id="11111111-1111-4111-8111-111111111111",
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

**id:** `str` — UUID identifying this resource.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `str` — Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

