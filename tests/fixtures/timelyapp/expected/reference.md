# Reference
## WebhookEvents
<details><summary><code>client.webhook_events.<a href="src/fern/webhook_events/client.py">webhook_event_types</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This is a documentation-only endpoint describing the webhook event payloads.

When you subscribe to webhook events, Timely will send HTTP POST requests to your configured URL with the following payloads:

| Event | Payload Schema |
|-------|----------------|
| `hours:created` | Hour |
| `hours:updated` | Hour |
| `hours:deleted` | Hour |
| `projects:created` | Project |
| `projects:updated` | Project |
| `projects:deleted` | Project |
| `labels:created` | Label |
| `labels:updated` | Label |
| `labels:deleted` | Label |
| `forecasts:created` | Forecast |
| `forecasts:updated` | Forecast |
| `forecasts:deleted` | Forecast |

See the webhook events below for the exact payload schemas.
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

client.webhook_events.webhook_event_types()

```
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

## Bulk Operations
<details><summary><code>client.bulk_operations.<a href="src/fern/bulk_operations/client.py">bulk_import_hours</a>(...) -> V1BulkImportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create, update, or delete multiple time entries in a single request. For large operations (100+ records), the operation runs asynchronously and returns a job ID.
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
from fern import FernApi, V1BulkHoursImportCreateItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bulk_operations.bulk_import_hours(
    account_id=1,
    create=[
        V1BulkHoursImportCreateItem(
            user_id=1,
            project_id=1,
            hours=3,
            minutes=30,
            seconds=0,
            day="2024-01-15",
            note="Test entry",
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

**account_id:** `int` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**request:** `V1BulkHoursImport` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_operations.<a href="src/fern/bulk_operations/client.py">bulk_import_events</a>(...) -> V1BulkImportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create, update, or delete multiple events in a single request. Events are the same as time entries - this is an alias endpoint. For large operations (100+ records), the operation runs asynchronously and returns a job ID.
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
from fern import FernApi, V1BulkHoursImportCreateItem
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.bulk_operations.bulk_import_events(
    account_id=1,
    create=[
        V1BulkHoursImportCreateItem(
            user_id=1,
            project_id=1,
            hours=2,
            minutes=0,
            seconds=0,
            day="2024-01-15",
            note="Test event",
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

**account_id:** `int` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**request:** `V1BulkHoursImport` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Clients
<details><summary><code>client.clients.<a href="src/fern/clients/client.py">list_all_clients_of_an_account</a>(...) -> typing.List[V1Company]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

NOTE: By default, client list will return first 10000 clients in alphabetical order. You can also use optional parameters like “limit”, “offset”, “show” and “order” to change the results.
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

client.clients.list_all_clients_of_an_account(
    account_id=1,
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

**account_id:** `int` — Account ID for the clients you want to retrieve
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Retrieve number of clients
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — "asc (default)" and "desc"
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Retrieve clients from offset
    
</dd>
</dl>

<dl>
<dd>

**show:** `typing.Optional[Get11AccountIdClientsRequestShow]` — Specifies which records to retrieve. Example: "show=all" or "show=active" or "show=archived"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/fern/clients/client.py">create_client</a>(...) -> V1Company</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API lets you create a client for an account.
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
from fern.clients import V1CompaniesCreateClient

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.clients.create_client(
    account_id=1,
    client=V1CompaniesCreateClient(
        name="New Client",
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

**account_id:** `int` — Account ID for the client you want to create
    
</dd>
</dl>

<dl>
<dd>

**client:** `V1CompaniesCreateClient` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/fern/clients/client.py">client_details</a>(...) -> V1Company</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Client details and project counts
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

client.clients.client_details(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID for the client you want to retrieve
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Client ID to retrieve
    
</dd>
</dl>

<dl>
<dd>

**project_counts:** `typing.Optional[str]` — Specify to retrieve project counts. Example values: "true" or "false"
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clients.<a href="src/fern/clients/client.py">client_update</a>(...) -> V1Company</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update client details just by using a client ID.
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
from fern.clients import V1CompaniesUpdateClient

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.clients.client_update(
    account_id=1,
    id=1,
    client=V1CompaniesUpdateClient(
        active=True,
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

**account_id:** `int` — Account ID for the client you want to update
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Client ID to update
    
</dd>
</dl>

<dl>
<dd>

**client:** `V1CompaniesUpdateClient` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Day Properties
<details><summary><code>client.day_properties.<a href="src/fern/day_properties/client.py">list_day_properties</a>(...) -> typing.List[V1DayProperty]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve day properties (locked days) for users in the account. Day properties control whether time entries can be modified for specific dates.

You can filter by date range using `since` and `until` parameters, or by specific dates using the `dates` parameter.
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

client.day_properties.list_day_properties(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.date]` — Start date for filtering (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[datetime.date]` — End date for filtering (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**dates:** `typing.Optional[str]` — Comma-separated list of specific dates (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.day_properties.<a href="src/fern/day_properties/client.py">create_day_properties</a>(...) -> typing.List[V1DayProperty]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update day properties to lock or unlock days for time entry modifications. This endpoint allows bulk operations across multiple users and dates.

When a day is locked, users cannot create, update, or delete time entries for that date. Only users with appropriate permissions (admins or managers) can lock/unlock days.
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
from fern.day_properties import V1DayPropertiesCreateDayProperty

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.day_properties.create_day_properties(
    account_id=1,
    day_property=V1DayPropertiesCreateDayProperty(
        dates=[
            "2024-01-01",
            "2024-01-02"
        ],
        user_ids=[
            1
        ],
        locked=True,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**day_property:** `V1DayPropertiesCreateDayProperty` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.day_properties.<a href="src/fern/day_properties/client.py">update_day_properties</a>(...) -> typing.List[V1DayProperty]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update day properties to lock or unlock days for time entry modifications. This endpoint allows bulk operations across multiple users and dates.

Use `locked: false` to unlock previously locked days, allowing users to modify time entries for those dates again.
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
from fern.day_properties import V1DayPropertiesUpdateDayProperty

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.day_properties.update_day_properties(
    account_id=1,
    day_property=V1DayPropertiesUpdateDayProperty(
        dates=[
            "2024-01-01"
        ],
        user_ids=[
            1
        ],
        locked=False,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**day_property:** `V1DayPropertiesUpdateDayProperty` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Forecasts (Tasks)
<details><summary><code>client.forecasts_tasks.<a href="src/fern/forecasts_tasks/client.py">list_tasks</a>(...) -> typing.List[V1Forecast]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all tasks in the account. Tasks are returned in a paginated format with optional filtering by date range, user, project, and completion status.
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

client.forecasts_tasks.list_tasks(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.date]` — Filter tasks from this date (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**upto:** `typing.Optional[datetime.date]` — Filter tasks up to this date (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**completed:** `typing.Optional[ListTasksRequestCompleted]` — Filter by completion status
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[str]` — Comma-separated list of user IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**project_ids:** `typing.Optional[str]` — Comma-separated list of project IDs, or "active"/"archived" to filter by project status
    
</dd>
</dl>

<dl>
<dd>

**forecast_ids:** `typing.Optional[str]` — Comma-separated list of task IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListTasksRequestSort]` — Field to sort by (default: updated_at)
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListTasksRequestOrder]` — Sort order (default: desc)
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page (max 5000)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forecasts_tasks.<a href="src/fern/forecasts_tasks/client.py">create_task</a>(...) -> V1Forecast</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new task. Requires the Planning feature to be enabled.
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
from fern.forecasts_tasks import V1ForecastsCreateForecast

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.forecasts_tasks.create_task(
    account_id=1,
    forecast=V1ForecastsCreateForecast(
        title="Implement API documentation",
        from_="2024-01-01",
        to="2024-01-08",
        project_id=1,
        estimated_minutes=480,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**forecast:** `V1ForecastsCreateForecast` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forecasts_tasks.<a href="src/fern/forecasts_tasks/client.py">show_task</a>(...) -> V1Forecast</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details for a specific task.
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

client.forecasts_tasks.show_task(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Task ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forecasts_tasks.<a href="src/fern/forecasts_tasks/client.py">delete_task</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a task.
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

client.forecasts_tasks.delete_task(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Task ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forecasts_tasks.<a href="src/fern/forecasts_tasks/client.py">update_task</a>(...) -> V1Forecast</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing task. Only the provided fields will be updated.
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
from fern.forecasts_tasks import V1ForecastsUpdateForecast

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.forecasts_tasks.update_task(
    account_id=1,
    id=1,
    forecast=V1ForecastsUpdateForecast(
        title="Updated task title",
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Task ID
    
</dd>
</dl>

<dl>
<dd>

**forecast:** `V1ForecastsUpdateForecast` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.forecasts_tasks.<a href="src/fern/forecasts_tasks/client.py">list_task_summaries</a>(...) -> typing.List[V1ForecastSummary]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get task summaries grouped by resource type (users or projects). Returns aggregate counts and duration totals.
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
from fern.forecasts_tasks import ListTaskSummariesRequestResource

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.forecasts_tasks.list_task_summaries(
    account_id=1,
    resource=ListTaskSummariesRequestResource.USERS,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**resource:** `ListTaskSummariesRequestResource` — Resource type to group summaries by
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.date]` — Filter tasks from this date
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[datetime.date]` — Filter tasks up to this date
    
</dd>
</dl>

<dl>
<dd>

**completed:** `typing.Optional[ListTaskSummariesRequestCompleted]` — Filter by completion status
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[str]` — Comma-separated user IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**project_ids:** `typing.Optional[str]` — Comma-separated project IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**forecast_ids:** `typing.Optional[str]` — Comma-separated task IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Events
<details><summary><code>client.events.<a href="src/fern/events/client.py">list_time_entries</a>(...) -> typing.List[V1Hour]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all time entries in the Timely account. Time entries will be returned in a paginated format with optional filtering.
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

client.events.list_time_entries(
    account_id=1,
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

**account_id:** `int` — Account ID for the time entries you want to retrieve
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.date]` — Filter time entries from this date (inclusive). Both since and upto needs to be present
    
</dd>
</dl>

<dl>
<dd>

**upto:** `typing.Optional[datetime.date]` — Filter time entries up to this date (inclusive). Both since and upto needs to be present
    
</dd>
</dl>

<dl>
<dd>

**day:** `typing.Optional[datetime.date]` — Filter time entries for a specific date. Defaults to current date if omitted. Disregarded if since and upto is present
    
</dd>
</dl>

<dl>
<dd>

**hour_ids:** `typing.Optional[str]` — Comma-separated list of time entry IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListTimeEntriesRequestSort]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListTimeEntriesRequestOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page (max 5000)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[int]` — Filter by project ID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[int]` — Filter by user ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/fern/events/client.py">create_hour</a>(...) -> V1Hour</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new time entry in the Timely account. The time entry will be created with the provided details.
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
from fern.events import V1HoursCreateEvent

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.create_hour(
    account_id=1,
    event=V1HoursCreateEvent(
        project_id=1,
        hours=2,
        minutes=30,
        day="2024-01-01",
        note="Working on API documentation",
        billable=True,
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

**account_id:** `int` — Account ID where the time entry will be created
    
</dd>
</dl>

<dl>
<dd>

**event:** `V1HoursCreateEvent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/fern/events/client.py">show_hour</a>(...) -> V1Hour</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details for a specific time entry.
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

client.events.show_hour(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Time entry ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/fern/events/client.py">update_hour</a>(...) -> V1Hour</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing time entry. Only the provided fields will be updated.
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
from fern.events import V1HoursUpdateEvent

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.events.update_hour(
    account_id=1,
    id=1,
    event=V1HoursUpdateEvent(
        hours=3,
        note="Updated note",
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Time entry ID
    
</dd>
</dl>

<dl>
<dd>

**event:** `V1HoursUpdateEvent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/fern/events/client.py">delete_hour</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a time entry. Locked or invoiced time entries cannot be deleted.
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

client.events.delete_hour(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Time entry ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Event Timers
<details><summary><code>client.event_timers.<a href="src/fern/event_timers/client.py">start_timer</a>(...) -> V1Hour</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start the timer for a specific time entry.
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

client.event_timers.start_timer(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Time entry ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_timers.<a href="src/fern/event_timers/client.py">stop_timer</a>(...) -> V1Hour</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop the timer for a specific time entry.
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

client.event_timers.stop_timer(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Time entry ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Event States
<details><summary><code>client.event_states.<a href="src/fern/event_states/client.py">list_hour_states</a>(...) -> typing.List[V1State]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all available time entry states for the account.
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

client.event_states.list_hour_states(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_states.<a href="src/fern/event_states/client.py">create_hour_state</a>(...) -> V1State</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new time entry state. Only admin users can create states.
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
from fern import FernApi, V1StatesCreateState
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_states.create_hour_state(
    account_id=1,
    state=V1StatesCreateState(
        name="Review Required",
        color="ff5722",
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `V1StatesCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_states.<a href="src/fern/event_states/client.py">update_hour_state</a>(...) -> V1State</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing time entry state. Only admin users can update states.
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
from fern import FernApi, V1StatesUpdateState
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_states.update_hour_state(
    account_id=1,
    id=1,
    state=V1StatesUpdateState(
        name="Updated State Name",
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — State ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `V1StatesUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_states.<a href="src/fern/event_states/client.py">delete_hour_state</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a time entry state. Only admin users can delete states and system-managed states cannot be deleted.
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

client.event_states.delete_hour_state(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — State ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_states.<a href="src/fern/event_states/client.py">create_state_permissions</a>(...) -> typing.List[V1StatePermission]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update permissions for a state. Admin access required. System-managed states cannot be modified.
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
from fern.event_states import V1StatePermissionsCreateStatePermission

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_states.create_state_permissions(
    account_id=1,
    state_id=1,
    state_permission=V1StatePermissionsCreateStatePermission(
        role_ids=[
            1
        ],
        team_lead=False,
        project_lead=False,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**state_id:** `int` — State ID
    
</dd>
</dl>

<dl>
<dd>

**state_permission:** `V1StatePermissionsCreateStatePermission` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_states.<a href="src/fern/event_states/client.py">delete_state_permissions</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all permissions for a state. Admin access required. System-managed states cannot be modified.
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

client.event_states.delete_state_permissions(
    account_id=1,
    state_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**state_id:** `int` — State ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — State permission ID (all permissions for the state are deleted regardless of ID)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_states.<a href="src/fern/event_states/client.py">list_states</a>(...) -> typing.List[V1State]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all states for the specified account, including their permissions.
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

client.event_states.list_states(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_states.<a href="src/fern/event_states/client.py">create_state</a>(...) -> V1State</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new state for the specified account. Only admin users can create states.
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
from fern import FernApi, V1StatesCreateState
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_states.create_state(
    account_id=1,
    state=V1StatesCreateState(
        name="New State",
        icon="star",
        color="ff0000",
        billed=True,
        locked=False,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `V1StatesCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_states.<a href="src/fern/event_states/client.py">update_state</a>(...) -> V1State</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing state. Only admin users can update states.
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
from fern import FernApi, V1StatesUpdateState
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.event_states.update_state(
    account_id=1,
    id=1,
    state=V1StatesUpdateState(
        name="Updated State",
        icon="circle",
        color="00ff00",
        billed=False,
        locked=True,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — State ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `V1StatesUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.event_states.<a href="src/fern/event_states/client.py">delete_state</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a state. Only admin users can delete states and system-managed states cannot be deleted.
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

client.event_states.delete_state(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — State ID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.tags.<a href="src/fern/tags/client.py">list_tags</a>(...) -> V1Label</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all labels (tags) for the specified account. Labels help classify work, group related tasks, and require certain information for events. Supports filtering by status and pagination.
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

client.tags.list_tags(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of labels to return (default: 10000)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of labels to skip (default: 0)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[ListTagsRequestFilter]` — Filter labels by status: all (default), active, or archived
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[int]` — Filter by parent label ID to get child labels only
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/fern/tags/client.py">create_tag</a>(...) -> V1Label</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new label (tag) for the account. Labels can be hierarchical by specifying a parent_id.
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
from fern.tags import V1LabelsCreateLabel

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tags.create_tag(
    account_id=1,
    label=V1LabelsCreateLabel(
        name="Project Management",
        emoji="https://emoji.memorycdn.com/tw64/1f4cb.png",
        active=True,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**label:** `V1LabelsCreateLabel` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/fern/tags/client.py">get_tag</a>(...) -> V1Label</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific label by ID. The response includes child labels if any exist.
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

client.tags.get_tag(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Label ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/fern/tags/client.py">update_tag</a>(...) -> V1Label</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing label. All fields are optional for partial updates. Set active to false to archive a label.
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
from fern.tags import V1LabelsUpdateLabel

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.tags.update_tag(
    account_id=1,
    id=1,
    label=V1LabelsUpdateLabel(
        name="Updated Name",
        emoji="https://emoji.memorycdn.com/tw64/1f504.png",
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Label ID
    
</dd>
</dl>

<dl>
<dd>

**label:** `V1LabelsUpdateLabel` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/fern/tags/client.py">delete_tag</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a label from the account. This will permanently remove the label.
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

client.tags.delete_tag(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Label ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OAuth
<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">create_access_token</a>(...) -> V1OAuthTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange an authorization code for an access token using OAuth 2.0 authorization code flow.
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
from fern.o_auth import V1OAuthTokenRequestGrantType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth.create_access_token(
    grant_type=V1OAuthTokenRequestGrantType.AUTHORIZATION_CODE,
    client_id="client_id",
    client_secret="client_secret",
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

**grant_type:** `V1OAuthTokenRequestGrantType` — OAuth 2.0 grant type
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `str` — OAuth 2.0 client identifier
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — OAuth 2.0 client secret
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — Authorization code (required for authorization_code grant)
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `typing.Optional[str]` — Redirect URI (required for authorization_code grant)
    
</dd>
</dl>

<dl>
<dd>

**refresh_token:** `typing.Optional[str]` — Refresh token (required for refresh_token grant)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">revoke_access_token</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke an access token or refresh token.
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
from fern.o_auth import V1OAuthRevokeRequestTokenTypeHint

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth.revoke_access_token(
    token="access_token_to_revoke",
    token_type_hint=V1OAuthRevokeRequestTokenTypeHint.ACCESS_TOKEN,
    client_id="EZPB04UG2RcRFOBd99k06MhN1WEl4opRHCun-8X1U9M",
    client_secret="8b93a66396d8dd37a32ae4ff85d99c192bf08b0270e73710cb7f3f29fc4530f1",
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

**token:** `str` — OAuth 2.0 access or refresh token to revoke
    
</dd>
</dl>

<dl>
<dd>

**token_type_hint:** `typing.Optional[V1OAuthRevokeRequestTokenTypeHint]` — Hint about the type of token being revoked
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — OAuth 2.0 client identifier
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` — OAuth 2.0 client secret
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">introspect_access_token</a>(...) -> V1OAuthIntrospectResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check if an access token is active and get its metadata.
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

client.o_auth.introspect_access_token(
    token="token",
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

**token:** `str` — OAuth 2.0 access token to introspect
    
</dd>
</dl>

<dl>
<dd>

**token_type_hint:** `typing.Optional[V1OAuthIntrospectRequestTokenTypeHint]` — Hint about the type of token being introspected
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">get_current_token_info</a>() -> GetCurrentTokenInfoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about the current access token.
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

client.o_auth.get_current_token_info()

```
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

<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">list_authorized_applications</a>() -> typing.List[V1OAuthAuthorizedApplication]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List applications that the current user has authorized.
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

client.o_auth.list_authorized_applications()

```
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

<details><summary><code>client.o_auth.<a href="src/fern/o_auth/client.py">revoke_application_authorization</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke authorization for a specific application.
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

client.o_auth.revoke_application_authorization(
    id=1,
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

**id:** `int` — Application ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Permissions
<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">list_current_user_permissions</a>(...) -> typing.List[V1Permission]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all resource permissions for the currently authenticated user.
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

client.permissions.list_current_user_permissions(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py">list_user_permissions</a>(...) -> typing.List[V1Permission]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all resource permissions for a specific user. Requires read access to users.
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

client.permissions.list_user_permissions(
    account_id=1,
    user_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — User ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Projects
<details><summary><code>client.projects.<a href="src/fern/projects/client.py">list_projects</a>(...) -> typing.List[V1Project]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all projects in the Timely account. The projects will be returned in a paginated format.
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

client.projects.list_projects(
    account_id=1,
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

**account_id:** `int` — Account ID for the clients you want to retrieve
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Retrieve projects from offset
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Retrieve number of projects
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Sorting order - desc, asc (Default desc)
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[ListProjectsRequestFilter]` — Deprecated: Filter projects - mine, active, archived, all (Default mine, ignored if state or relation parameter present)
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[ListProjectsRequestState]` — Filter projects - active, archived, all
    
</dd>
</dl>

<dl>
<dd>

**relation:** `typing.Optional[ListProjectsRequestRelation]` — Filter projects - assigned, created, all
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[str]` — Retrieve records updated after a certain timestamp
    
</dd>
</dl>

<dl>
<dd>

**project_ids:** `typing.Optional[typing.Union[float, typing.Sequence[float]]]` — Retrieve specific projects
    
</dd>
</dl>

<dl>
<dd>

**external_ids:** `typing.Optional[typing.Union[float, typing.Sequence[float]]]` — Retrieve specific projects by external ID reference
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">create_project</a>(...) -> V1Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project in the Timely account. The project will be created with the provided details.
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
from fern.projects import V1ProjectsCreateProject, V1ProjectsCreateProjectRateType

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.projects.create_project(
    account_id=1,
    project=V1ProjectsCreateProject(
        name="New Sideproject 2",
        color="d0915a",
        new_company="Timely Solo",
        hour_rate=20,
        rate_type=V1ProjectsCreateProjectRateType.PROJECT,
        label_ids=[
            1,
            2
        ],
        required_label_ids=[
            1
        ],
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

**account_id:** `int` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**project:** `V1ProjectsCreateProject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">show_project</a>(...) -> V1Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details for a specific project.
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

client.projects.show_project(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Project ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">update_project</a>(...) -> V1Project</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing project. Only the provided fields will be updated.
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
from fern.projects import V1ProjectsUpdateProject

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.projects.update_project(
    account_id=1,
    id=1,
    project=V1ProjectsUpdateProject(
        name="Updated Project Name",
        color="ff5733",
        description="Updated description",
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Project ID
    
</dd>
</dl>

<dl>
<dd>

**project:** `V1ProjectsUpdateProject` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/fern/projects/client.py">delete_project</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project. This will permanently remove the project from the account.
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

client.projects.delete_project(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Project ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Reports
<details><summary><code>client.reports.<a href="src/fern/reports/client.py">get_reports</a>(...) -> typing.List[V1ReportTotals]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve report totals grouped by clients and projects. This endpoint provides aggregated time tracking data including durations, costs, and billing information. The response includes clients with their associated projects and calculated metrics.
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

client.reports.get_reports(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.date]` — Start date for the report period (ISO 8601 format: YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[datetime.date]` — End date for the report period (ISO 8601 format: YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[str]` — Comma-separated list of user IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**project_ids:** `typing.Optional[str]` — Comma-separated list of project IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**client_ids:** `typing.Optional[str]` — Comma-separated list of client IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py">filter_reports</a>(...) -> typing.List[typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filter and retrieve report data with flexible grouping options. Returns aggregated totals grouped by clients, projects, users, labels, days, or teams. Use scope=events to retrieve individual time entries instead of aggregated totals.
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

client.reports.filter_reports(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.date]` — Start date for the report period (ISO 8601 format: YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[datetime.date]` — End date for the report period (ISO 8601 format: YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[str]` — Comma-separated list of user IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**project_ids:** `typing.Optional[str]` — Comma-separated list of project IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**client_ids:** `typing.Optional[str]` — Comma-separated list of client IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**label_ids:** `typing.Optional[str]` — Comma-separated list of label IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**team_ids:** `typing.Optional[str]` — Comma-separated list of team IDs to filter by (requires teams feature)
    
</dd>
</dl>

<dl>
<dd>

**state_ids:** `typing.Optional[str]` — Comma-separated list of state IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[str]` — Comma-separated list of grouping keys: clients, users, labels, days, teams. Default: all groups
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[FilterReportsRequestScope]` — Result scope: totals (aggregated data) or events (individual entries). Default: totals
    
</dd>
</dl>

<dl>
<dd>

**billed:** `typing.Optional[FilterReportsRequestBilled]` — Filter by billed status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Roles
<details><summary><code>client.roles.<a href="src/fern/roles/client.py">list_roles</a>(...) -> typing.List[V1Role]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all roles available in the account. Roles define permissions and access levels for users, including admin, manager, employee, and team lead roles.
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

client.roles.list_roles(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Teams
<details><summary><code>client.teams.<a href="src/fern/teams/client.py">search_teams</a>(...) -> typing.List[V1Team]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for teams by name
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

client.teams.search_teams(
    account_id=1,
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

**account_id:** `int` — Account ID for the teams you want to search
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search query
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of results per page
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">list_all_teams_of_an_account</a>(...) -> typing.List[V1Team]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

NOTE: By default, team list will return first 100 teams in alphabetical order. You can also use optional parameters like "limit", "offset", and "order" to change the results.
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

client.teams.list_all_teams_of_an_account(
    account_id=1,
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

**account_id:** `int` — Account ID for the teams you want to retrieve
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Retrieve number of teams
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — "asc (default)" and "desc"
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Retrieve teams from offset
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[str]` — Filter teams by "mine" or show all
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">create_team</a>(...) -> V1Team</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API lets you create a team for an account.
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
from fern.teams import V1TeamsCreateTeam

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.teams.create_team(
    account_id=1,
    team=V1TeamsCreateTeam(
        name="New Team",
        color="FF5733",
        emoji="🚀",
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

**account_id:** `int` — Account ID for the team you want to create
    
</dd>
</dl>

<dl>
<dd>

**team:** `V1TeamsCreateTeam` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">team_details</a>(...) -> V1Team</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Team details including users and project IDs
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

client.teams.team_details(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID for the team you want to retrieve
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Team ID to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">team_update</a>(...) -> V1Team</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update team details just by using a team ID.
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
from fern.teams import V1TeamsUpdateTeam

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.teams.team_update(
    account_id=1,
    id=1,
    team=V1TeamsUpdateTeam(
        name="Updated Team Name",
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

**account_id:** `int` — Account ID for the team you want to update
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Team ID to update
    
</dd>
</dl>

<dl>
<dd>

**team:** `V1TeamsUpdateTeam` 
    
</dd>
</dl>

<dl>
<dd>

**add_users_to_team_projects:** `typing.Optional[bool]` — Whether to add users to team projects
    
</dd>
</dl>

<dl>
<dd>

**delete_users_from_team_projects:** `typing.Optional[bool]` — Whether to delete users from team projects
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">team_delete</a>(...) -> Delete11AccountIdTeamsIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a team by ID.
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

client.teams.team_delete(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID for the team you want to delete
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Team ID to delete
    
</dd>
</dl>

<dl>
<dd>

**delete_project_users:** `typing.Optional[bool]` — Whether to delete users from team projects
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py">team_patch</a>(...) -> V1Team</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patch team details just by using a team ID.
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
from fern.teams import V1TeamsPatchTeam

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.teams.team_patch(
    account_id=1,
    id=1,
    team=V1TeamsPatchTeam(
        name="Patched Team Name",
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

**account_id:** `int` — Account ID for the team you want to patch
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Team ID to patch
    
</dd>
</dl>

<dl>
<dd>

**team:** `V1TeamsPatchTeam` 
    
</dd>
</dl>

<dl>
<dd>

**add_users_to_team_projects:** `typing.Optional[bool]` — Whether to add users to team projects
    
</dd>
</dl>

<dl>
<dd>

**delete_users_from_team_projects:** `typing.Optional[bool]` — Whether to delete users from team projects
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## User Capacities
<details><summary><code>client.user_capacities.<a href="src/fern/user_capacities/client.py">list_user_capacities</a>(...) -> typing.List[V1UserCapacity]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve capacity configurations for a specific user. Capacities define a user's working hours, working days, and daily/weekly hour limits.
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

client.user_capacities.list_user_capacities(
    account_id=1,
    user_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` — User ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_capacities.<a href="src/fern/user_capacities/client.py">list_users_capacities</a>(...) -> typing.List[ListUsersCapacitiesResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve capacity configurations for multiple users in the account. Supports filtering by user IDs and date range.
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

client.user_capacities.list_users_capacities(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[str]` — Comma-separated list of user IDs to filter by
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.date]` — Fetch capacities after this date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**until:** `typing.Optional[datetime.date]` — Fetch capacities before this date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.users.<a href="src/fern/users/client.py">get_current_user</a>(...) -> V1User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current user information for the authenticated user.
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

client.users.get_current_user(
    account_id=1,
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

**account_id:** `int` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">list_users</a>(...) -> typing.List[V1User]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists users in the account. Requires global user read permission or project update permission.
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

client.users.list_users(
    account_id=1,
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

**account_id:** `int` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[ListUsersRequestFilter]` — Filter for deleted users
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">invite_user</a>(...) -> V1User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invites user to the account. Requires trial/active subscription as also available seats in the workspace to accommodate additional users.
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
from fern import FernApi, V1UsersCreateUser, V1UsersCreateUserProjectsOneItem, V1UsersCreateUserUserLevel
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.invite_user(
    account_id=1,
    user=V1UsersCreateUser(
        admin=False,
        projects=[
            V1UsersCreateUserProjectsOneItem(
                project_id=1,
                hour_rate=10,
            )
        ],
        user_level=V1UsersCreateUserUserLevel.NORMAL,
        name="Marija Petrovic",
        email="marija@timely.com",
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

**account_id:** `int` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**request:** `V1UsersCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">get_user</a>(...) -> V1User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get specific user details. Requires read permission for the user.
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

client.users.get_user(
    account_id=1,
    id=1,
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

**account_id:** `int` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — User id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">update_user</a>(...) -> V1User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update user details. Requires update permission for the user.
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
from fern import FernApi, V1UsersCreateUser
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.users.update_user(
    account_id=1,
    id=1,
    user=V1UsersCreateUser(
        role_id=1,
        name="Updated Name",
        email="updated@timely.com",
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

**account_id:** `int` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — User id
    
</dd>
</dl>

<dl>
<dd>

**request:** `V1UsersCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">delete_user</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete/remove user from account. Requires delete permission for the user.
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

client.users.delete_user(
    account_id=1,
    id=1,
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

**account_id:** `int` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — User id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py">search_users</a>(...) -> typing.List[V1User]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search users. Requires create or update project permission.
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

client.users.search_users(
    account_id=1,
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

**account_id:** `int` — Workspace id
    
</dd>
</dl>

<dl>
<dd>

**q:** `str` — Search query
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Results per page
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">list_webhooks</a>(...) -> typing.List[V1Webhook]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all webhooks configured for the account. Webhooks allow you to receive HTTP POST notifications when events occur.
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

client.webhooks.list_webhooks(
    account_id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of webhooks to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of webhooks to skip
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">create_webhook</a>(...) -> V1Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new webhook subscription. Webhooks allow you to receive HTTP POST notifications when events occur in your account.

**Supported Events:**
- `hours:created` - When a new time entry is created
- `hours:updated` - When a time entry is updated
- `hours:deleted` - When a time entry is deleted
- `projects:created` - When a new project is created
- `projects:updated` - When a project is updated
- `projects:deleted` - When a project is deleted
- `labels:created` - When a new label is created
- `labels:updated` - When a label is updated
- `labels:deleted` - When a label is deleted
- `forecasts:created` - When a new forecast is created
- `forecasts:updated` - When a forecast is updated
- `forecasts:deleted` - When a forecast is deleted

**Security:**
When a `secret_token` is provided, each webhook request will include an `X-Signature` header containing an HMAC-SHA256 signature of the request body. You can use this to verify the authenticity of incoming webhook requests.
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
from fern.webhooks import V1WebhooksCreateWebhook, V1WebhooksCreateWebhookSubscriptionsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.create_webhook(
    account_id=1,
    webhook=V1WebhooksCreateWebhook(
        url="https://example.com/my-webhook",
        subscriptions=[
            V1WebhooksCreateWebhookSubscriptionsItem.HOURS_CREATED,
            V1WebhooksCreateWebhookSubscriptionsItem.HOURS_UPDATED
        ],
        secret_token="my-secret-token",
        active=True,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `V1WebhooksCreateWebhook` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">show_webhook</a>(...) -> V1Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details for a specific webhook.
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

client.webhooks.show_webhook(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Webhook ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">update_webhook</a>(...) -> V1Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing webhook. Only the provided fields will be updated.
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
from fern.webhooks import V1WebhooksUpdateWebhook, V1WebhooksUpdateWebhookSubscriptionsItem

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.webhooks.update_webhook(
    account_id=1,
    id=1,
    webhook=V1WebhooksUpdateWebhook(
        url="https://example.com/new-webhook",
        subscriptions=[
            V1WebhooksUpdateWebhookSubscriptionsItem.HOURS_CREATED,
            V1WebhooksUpdateWebhookSubscriptionsItem.PROJECTS_CREATED
        ],
        active=False,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Webhook ID
    
</dd>
</dl>

<dl>
<dd>

**webhook:** `V1WebhooksUpdateWebhook` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/fern/webhooks/client.py">delete_webhook</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a webhook. This will permanently remove the webhook and stop all future notifications.
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

client.webhooks.delete_webhook(
    account_id=1,
    id=1,
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

**account_id:** `int` — Account ID
    
</dd>
</dl>

<dl>
<dd>

**id:** `int` — Webhook ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

