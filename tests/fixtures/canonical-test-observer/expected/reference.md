# Reference
<details><summary><code>client.<a href="src/fern/client.py#L140-L164">get_version_v1version_get</a>() -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.get_version_v1version_get()

```
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

<details><summary><code>client.<a href="src/fern/client.py#L166-L199">live_health_live_get</a>() -> typing.Dict[str, str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Liveness probe.

Returns 200 OK if the application process is running and responding to requests.
Does not check external dependencies like the database.

Use this probe with container orchestration to determine if the process should be restarted.
Note that this should only be accessible internally (e.g. from the host container)
and not accessible over the public API.
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.live_health_live_get()

```
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

<details><summary><code>client.<a href="src/fern/client.py#L201-L237">ready_health_ready_get</a>() -> typing.Dict[str, str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Readiness probe.

Returns 200 OK if the application is ready to serve traffic, including database connectivity.
Performs a simple database query to verify the connection is valid.

Use this probe with container orchestration to determine if traffic should be routed to this pod.
Note that this should only be accessible internally (e.g. from the host container)
and not accessible over the public API.
Returns 503 if the database is unavailable.
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.ready_health_ready_get()

```
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

<details><summary><code>client.<a href="src/fern/client.py#L239-L263">root_get</a>() -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.root_get()

```
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

<details><summary><code>client.<a href="src/fern/client.py#L265-L289">trigger_error_sentry_debug_get</a>() -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.trigger_error_sentry_debug_get()

```
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

## TestExecutions
<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L59-L116">end_test_execution</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, C3TestResult, C3TestResultStatus

client = FernApi(
    token="<token>",
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.end_test_execution(
    ci_link="ci_link",
    test_results=[
        C3TestResult(
            name="name",
            status=C3TestResultStatus.PASS,
            category="category",
            comment="comment",
            io_log="io_log",
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

**ci_link:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**test_results:** `typing.List[C3TestResult]` 
    
</dd>
</dl>

<dl>
<dd>

**c3link:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**checkbox_version:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L118-L148">get_test_results</a>(...) -> typing.List[TestResultResponse]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.get_test_results(
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L150-L192">post_results</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TestResultRequest, TestResultStatus

client = FernApi(
    token="<token>",
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.post_results(
    id=1,
    request=[
        TestResultRequest(
            name="name",
            status=TestResultStatus.PASSED,
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[TestResultRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L194-L230">post_link</a>(...) -> TestExecutionRelevantLinkResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.post_link(
    id=1,
    label="label",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TestExecutionRelevantLinkCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L232-L262">delete_link</a>(...)</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.delete_link(
    id=1,
    link_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L264-L315">get_rerun_requests</a>(...) -> typing.List[PendingRerun]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.get_rerun_requests()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**family:** `typing.Optional[FamilyName]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of rerun requests to return
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_architecture:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**build_architecture:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L317-L368">create_rerun_requests</a>(...) -> typing.Optional[typing.List[PendingRerun]]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.create_rerun_requests()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**silent:** `typing.Optional[bool]` — If true, omit returning created reruns in the response body. Speeds up bulk operations, as the rerun schema contains a lot of information and returning many reruns can be slow. Required when creating reruns with test_results_filters or test_executions_filters.
    
</dd>
</dl>

<dl>
<dd>

**test_execution_ids:** `typing.Optional[typing.List[int]]` 
    
</dd>
</dl>

<dl>
<dd>

**test_results_filters:** `typing.Optional[TestResultSearchFilters]` 
    
</dd>
</dl>

<dl>
<dd>

**test_executions_filters:** `typing.Optional[TestExecutionRerunFilters]` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L370-L412">delete_rerun_requests</a>(...) -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.delete_rerun_requests()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_execution_ids:** `typing.Optional[typing.List[int]]` 
    
</dd>
</dl>

<dl>
<dd>

**test_results_filters:** `typing.Optional[TestResultSearchFilters]` 
    
</dd>
</dl>

<dl>
<dd>

**test_executions_filters:** `typing.Optional[TestExecutionRerunFilters]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L414-L458">get_rerun_details</a>(...) -> RerunDetailsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FamilyName

client = FernApi(
    token="<token>",
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.get_rerun_details(
    family=FamilyName.SNAP,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**family:** `FamilyName` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L460-L490">get_test_execution</a>(...) -> TestExecutionResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.get_test_execution(
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L492-L544">patch_test_execution</a>(...) -> TestExecutionResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.patch_test_execution(
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**c3link:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ci_link:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TestExecutionsPatchRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**execution_metadata:** `typing.Optional[ExecutionMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L546-L687">search_test_executions</a>(...) -> TestExecutionSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search test executions with optional test result context.

Returns one item per matching test execution with paginated results.
The test_results field contains all filtered test results for that execution.

Use test_result=none to find executions without results,
test_result=any to find executions with results,
or test_result={id} to filter by specific test result IDs.
If test_result is omitted, executions are not filtered by result
presence at all.
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.search_test_executions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**families:** `typing.Optional[typing.List[FamilyName]]` — Filter by artefact families (e.g., charm,snap)
    
</dd>
</dl>

<dl>
<dd>

**artefacts:** `typing.Optional[typing.List[str]]` — Filter by artefact names
    
</dd>
</dl>

<dl>
<dd>

**artefact_versions:** `typing.Optional[typing.List[str]]` — Filter by artefact versions
    
</dd>
</dl>

<dl>
<dd>

**artefact_stages:** `typing.Optional[typing.List[str]]` — Filter by artefact stages
    
</dd>
</dl>

<dl>
<dd>

**artefact_tracks:** `typing.Optional[typing.List[str]]` — Filter by artefact tracks
    
</dd>
</dl>

<dl>
<dd>

**artefact_is_archived:** `typing.Optional[bool]` — Filter by whether the artefact is archived
    
</dd>
</dl>

<dl>
<dd>

**environments:** `typing.Optional[typing.List[str]]` — Filter by environment names
    
</dd>
</dl>

<dl>
<dd>

**test_plans:** `typing.Optional[typing.List[str]]` — Filter by test plan names
    
</dd>
</dl>

<dl>
<dd>

**test_execution_statuses:** `typing.Optional[typing.List[TestExecutionStatus]]` — Filter by test execution statuses
    
</dd>
</dl>

<dl>
<dd>

**reviewer_ids:** `typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds]` — Filter by reviewer user ids
    
</dd>
</dl>

<dl>
<dd>

**assignee_ids:** `typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds]` — DEPRECATED: Use reviewer_ids instead
    
</dd>
</dl>

<dl>
<dd>

**rerun_is_requested:** `typing.Optional[bool]` — Filter by whether a rerun has been requested for the test execution
    
</dd>
</dl>

<dl>
<dd>

**execution_is_latest:** `typing.Optional[bool]` — Filter by whether the test execution is the latest in its environment/artefact/test plan combination
    
</dd>
</dl>

<dl>
<dd>

**test_result:** `typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestTestResult]` — Filter by test result presence: 'any' (executions with results), 'none' (executions without results), or specific test result ID(s). If omitted, executions are not filtered by result presence, so executions with zero results (e.g. NOT_STARTED, ENDED_PREMATURELY) are included.
    
</dd>
</dl>

<dl>
<dd>

**event_names:** `typing.Optional[SearchTestExecutionsV1TestExecutionsGetRequestEventNames]` — Filter by event log: 'any' (executions with any events), 'none' (executions without events), or specific event name(s)
    
</dd>
</dl>

<dl>
<dd>

**from_date:** `typing.Optional[datetime.datetime]` — Filter executions updated on or after this datetime
    
</dd>
</dl>

<dl>
<dd>

**until_date:** `typing.Optional[datetime.datetime]` — Filter executions updated on or before this datetime
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**execution_metadata:** `typing.Optional[typing.List[str]]` — Filter by execution metadata (base64 encoded category:value pairs).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L689-L736">start_test_execution</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, SnapStage
from fern.test_executions import StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap

client = FernApi(
    token="<token>",
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.start_test_execution(
    request=StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap(
        name="name",
        version="version",
        arch="arch",
        environment="environment",
        test_plan="test_plan",
        revision=1,
        track="track",
        store="store",
        execution_stage=SnapStage.EDGE,
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

**request:** `StartTestExecutionV1TestExecutionsStartTestPutRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L738-L768">get_status_update</a>(...) -> typing.List[TestEventResponse]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.get_status_update(
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L770-L817">post_status_update</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TestEventResponse
import datetime

client = FernApi(
    token="<token>",
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.post_status_update(
    id=1,
    events=[
        TestEventResponse(
            event_name="event_name",
            timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            detail="detail",
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `StatusUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_executions.<a href="src/fern/test_executions/client.py#L819-L866">put_status_update</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TestEventResponse
import datetime

client = FernApi(
    token="<token>",
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_executions.put_status_update(
    id=1,
    events=[
        TestEventResponse(
            event_name="event_name",
            timestamp=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
            detail="detail",
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

**id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `StatusUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Artefacts
<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L40-L70">get_artefacts</a>(...) -> typing.List[ArtefactResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get latest artefacts optionally by family
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.get_artefacts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**family:** `typing.Optional[FamilyName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L72-L122">search_artefacts</a>(...) -> ArtefactSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for artefacts by name with pagination support.

Returns a list of distinct artefact names that match the search query.
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.search_artefacts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search term for artefact names
    
</dd>
</dl>

<dl>
<dd>

**families:** `typing.Optional[typing.List[FamilyName]]` — Filter by artefact families
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results (defaults to 50 if not specified)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L124-L192">get_artefact_history</a>(...) -> ArtefactHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the versioning history of an artefact for a given name, family, and track,
optionally filtered by stage, with pagination support.

Returns a list of artefact versions along with their creation date.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FamilyName

client = FernApi(
    token="<token>",
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.get_artefact_history(
    name="name",
    family=FamilyName.SNAP,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Artefact name
    
</dd>
</dl>

<dl>
<dd>

**family:** `FamilyName` — Artefact family
    
</dd>
</dl>

<dl>
<dd>

**track:** `typing.Optional[str]` — Artefact track
    
</dd>
</dl>

<dl>
<dd>

**stage:** `typing.Optional[StageName]` — Filter by stage
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results (defaults to 10 if not specified)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L194-L224">get_artefact</a>(...) -> ArtefactResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.get_artefact(
    artefact_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artefact_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L226-L253">delete_artefact</a>(...)</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.delete_artefact(
    artefact_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artefact_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L255-L340">patch_artefact</a>(...) -> ArtefactResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.patch_artefact(
    artefact_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artefact_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ArtefactStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**stage:** `typing.Optional[StageName]` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**jira_issue:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**expected_environments:** `typing.Optional[typing.List[ExpectedEnvironmentInput]]` — Expected environments, replacing the current set. Each environment is identified by name and architecture.
    
</dd>
</dl>

<dl>
<dd>

**assignee_id:** `typing.Optional[int]` — Legacy field. Mapped to reviewer_ids as a single-element list when reviewer_ids/reviewer_emails are not provided.
    
</dd>
</dl>

<dl>
<dd>

**assignee_email:** `typing.Optional[str]` — Legacy field. Mapped to reviewer_emails as a single-element list when reviewer_ids/reviewer_emails are not provided.
    
</dd>
</dl>

<dl>
<dd>

**reviewer_ids:** `typing.Optional[typing.List[int]]` — Reviewer user IDs. Preferred over legacy assignee_id/assignee_email for setting assignees.
    
</dd>
</dl>

<dl>
<dd>

**reviewer_emails:** `typing.Optional[typing.List[str]]` — Reviewer emails. Preferred over legacy assignee_id/assignee_email for setting assignees.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L342-L372">get_artefact_versions</a>(...) -> typing.List[ArtefactVersionResponse]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.get_artefact_versions(
    artefact_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artefact_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L374-L404">get_environment_reviews</a>(...) -> typing.List[ArtefactBuildEnvironmentReviewResponse]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.get_environment_reviews(
    artefact_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artefact_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L406-L445">bulk_update_environment_reviews</a>(...) -> typing.List[ArtefactBuildEnvironmentReviewResponse]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, EnvironmentReviewPatch

client = FernApi(
    token="<token>",
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.bulk_update_environment_reviews(
    artefact_id=1,
    request=[
        EnvironmentReviewPatch()
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

**artefact_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[EnvironmentReviewPatch]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L447-L500">update_environment_review</a>(...) -> ArtefactBuildEnvironmentReviewResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.update_environment_review(
    artefact_id=1,
    review_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artefact_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**review_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EnvironmentReviewPatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefacts.<a href="src/fern/artefacts/client.py#L502-L534">get_artefact_builds</a>(...) -> typing.List[ArtefactBuildResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get latest artefact builds of an artefact together with their test executions
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefacts.get_artefact_builds(
    artefact_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artefact_id:** `int` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.reports.<a href="src/fern/reports/client.py#L26-L64">get_testresults_report</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a csv report detailing all artefacts within a given date range. Together
with their test executions and test results in csv format.
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.reports.get_testresults_report()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/fern/reports/client.py#L66-L104">get_test_execution_reports</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a csv report detailing all test executions within a given date range.
Together with their artefact and environment details in csv format.
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.reports.get_test_execution_reports()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TestCases
<details><summary><code>client.test_cases.<a href="src/fern/test_cases/client.py#L31-L67">get_reported_issues</a>(...) -> typing.List[TestReportedIssueResponse]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_cases.get_reported_issues()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**case_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_cases.<a href="src/fern/test_cases/client.py#L69-L118">create_reported_issue</a>(...) -> TestReportedIssueResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_cases.create_reported_issue(
    description="description",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `TestReportedIssueRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_cases.<a href="src/fern/test_cases/client.py#L120-L174">update_reported_issue</a>(...) -> TestReportedIssueResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_cases.update_reported_issue(
    issue_id=1,
    description="description",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TestReportedIssueRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_cases.<a href="src/fern/test_cases/client.py#L176-L206">delete_reported_issue</a>(...) -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_cases.delete_reported_issue(
    issue_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_cases.<a href="src/fern/test_cases/client.py#L208-L260">get_test_cases</a>(...) -> TestCasesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns test cases as a flat list with their template IDs.

Template ID represents the generic test (e.g., "disk/stats_name")
Test case name is the specific instance (e.g., "disk/stats_nvme0n1")
Multiple test cases can share the same template ID but have different names.
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_cases.get_test_cases()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search term for test case names
    
</dd>
</dl>

<dl>
<dd>

**families:** `typing.Optional[typing.List[FamilyName]]` — Filter by artefact families
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results (defaults to 50 if not specified)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Environments
<details><summary><code>client.environments.<a href="src/fern/environments/client.py#L31-L59">get_reported_issues</a>(...) -> typing.List[EnvironmentReportedIssueResponse]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.environments.get_reported_issues()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**is_confirmed:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py#L61-L111">create_reported_issue</a>(...) -> EnvironmentReportedIssueResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.environments.create_reported_issue(
    environment_name="environment_name",
    description="description",
    is_confirmed=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EnvironmentReportedIssueRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py#L113-L168">update_reported_issue</a>(...) -> EnvironmentReportedIssueResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.environments.update_reported_issue(
    issue_id=1,
    environment_name="environment_name",
    description="description",
    is_confirmed=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `EnvironmentReportedIssueRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py#L170-L200">delete_reported_issue</a>(...) -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.environments.delete_reported_issue(
    issue_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/fern/environments/client.py#L202-L252">get_environments</a>(...) -> EnvironmentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns list of distinct environments that have been used in test executions.

Supports pagination and search filtering.
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.environments.get_environments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search term for environment names
    
</dd>
</dl>

<dl>
<dd>

**families:** `typing.Optional[typing.List[FamilyName]]` — Filter by artefact families
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results (defaults to 50 if not specified)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TestPlans
<details><summary><code>client.test_plans.<a href="src/fern/test_plans/client.py#L27-L77">get_test_plans</a>(...) -> TestPlansResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns list of distinct test plan names.

Supports pagination and search filtering.
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_plans.get_test_plans()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search term for test plan names
    
</dd>
</dl>

<dl>
<dd>

**families:** `typing.Optional[typing.List[FamilyName]]` — Filter by artefact families
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results (defaults to 50 if not specified)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Issues
<details><summary><code>client.issues.<a href="src/fern/issues/client.py#L37-L85">add_issue_attachments</a>(...) -> IssueResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.issues.add_issue_attachments(
    issue_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `IssueAttachmentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/fern/issues/client.py#L87-L135">remove_issue_attachments</a>(...) -> IssueResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.issues.remove_issue_attachments(
    issue_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `IssueAttachmentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/fern/issues/client.py#L137-L221">post_attachment_rule</a>(...) -> MinimalIssueTestResultAttachmentRuleResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.issues.post_attachment_rule(
    issue_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**families:** `typing.Optional[typing.List[FamilyName]]` 
    
</dd>
</dl>

<dl>
<dd>

**artefacts:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**artefact_versions:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**artefact_stages:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**artefact_tracks:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_names:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**test_plans:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**test_case_names:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**template_ids:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**test_result_statuses:** `typing.Optional[typing.List[TestResultStatus]]` 
    
</dd>
</dl>

<dl>
<dd>

**execution_metadata:** `typing.Optional[ExecutionMetadata]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/fern/issues/client.py#L223-L257">delete_attachment_rule</a>(...)</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.issues.delete_attachment_rule(
    issue_id=1,
    attachment_rule_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**attachment_rule_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/fern/issues/client.py#L259-L301">patch_attachment_rule</a>(...) -> MinimalIssueTestResultAttachmentRuleResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.issues.patch_attachment_rule(
    issue_id=1,
    attachment_rule_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**attachment_rule_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/fern/issues/client.py#L303-L368">get_issues</a>(...) -> IssuesGetResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.issues.get_issues()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source:** `typing.Optional[IssueSource]` — Filter by issue source (e.g., github, jira, launchpad)
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[str]` — Filter by project name
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[IssueStatus]]` — Filter by issue status. Accepts multiple values
    
</dd>
</dl>

<dl>
<dd>

**families:** `typing.Optional[typing.List[FamilyName]]` — Filter by artefact family (e.g., snap, deb, charm, image)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return (default: 50)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination (default: 0)
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search term for issue source, project, keys, title, and status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/fern/issues/client.py#L370-L414">create_or_update_issue</a>(...) -> IssueResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.issues.create_or_update_issue(
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[IssueStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_rerun_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/fern/issues/client.py#L416-L444">get_issue</a>(...) -> IssueResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.issues.get_issue(
    issue_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.issues.<a href="src/fern/issues/client.py#L446-L506">patch_issue</a>(...) -> IssueResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.issues.patch_issue(
    issue_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**issue_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[IssueStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_rerun_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**issue_patch_request_title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issue_patch_request_status:** `typing.Optional[IssueStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**issue_patch_request_auto_rerun_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TestResults
<details><summary><code>client.test_results.<a href="src/fern/test_results/client.py#L37-L181">search_test_results</a>(...) -> TestResultSearchResponseWithContext</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search test results across artefacts using flexible filters.

Returns one item per matching test result with execution, artefact, and build context.
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.test_results.search_test_results()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**families:** `typing.Optional[typing.List[FamilyName]]` — Filter by artefact families (e.g., charm,snap)
    
</dd>
</dl>

<dl>
<dd>

**artefacts:** `typing.Optional[typing.List[str]]` — Filter by artefact names
    
</dd>
</dl>

<dl>
<dd>

**artefact_versions:** `typing.Optional[typing.List[str]]` — Filter by artefact versions
    
</dd>
</dl>

<dl>
<dd>

**artefact_stages:** `typing.Optional[typing.List[str]]` — Filter by artefact stages
    
</dd>
</dl>

<dl>
<dd>

**artefact_tracks:** `typing.Optional[typing.List[str]]` — Filter by artefact tracks
    
</dd>
</dl>

<dl>
<dd>

**artefact_is_archived:** `typing.Optional[bool]` — Filter by whether the artefact is archived
    
</dd>
</dl>

<dl>
<dd>

**environments:** `typing.Optional[typing.List[str]]` — Filter by environment names
    
</dd>
</dl>

<dl>
<dd>

**test_plans:** `typing.Optional[typing.List[str]]` — Filter by test plan names
    
</dd>
</dl>

<dl>
<dd>

**test_cases:** `typing.Optional[typing.List[str]]` — Filter by test case names
    
</dd>
</dl>

<dl>
<dd>

**template_ids:** `typing.Optional[typing.List[str]]` — Filter by template IDs
    
</dd>
</dl>

<dl>
<dd>

**issues:** `typing.Optional[SearchTestResultsV1TestResultsGetRequestIssues]` — Filter by issue IDs
    
</dd>
</dl>

<dl>
<dd>

**test_result_statuses:** `typing.Optional[typing.List[TestResultStatus]]` — Filter by test result statuses
    
</dd>
</dl>

<dl>
<dd>

**test_execution_statuses:** `typing.Optional[typing.List[TestExecutionStatus]]` — Filter by test execution statuses
    
</dd>
</dl>

<dl>
<dd>

**reviewer_ids:** `typing.Optional[SearchTestResultsV1TestResultsGetRequestReviewerIds]` — Filter by reviewer user ids
    
</dd>
</dl>

<dl>
<dd>

**assignee_ids:** `typing.Optional[SearchTestResultsV1TestResultsGetRequestAssigneeIds]` — DEPRECATED: Use reviewer_ids instead
    
</dd>
</dl>

<dl>
<dd>

**rerun_is_requested:** `typing.Optional[bool]` — Filter by whether a rerun has been requested for the test execution
    
</dd>
</dl>

<dl>
<dd>

**execution_is_latest:** `typing.Optional[bool]` — Filter by whether the test execution is the latest in its environment/artifact/test plan combination
    
</dd>
</dl>

<dl>
<dd>

**from_date:** `typing.Optional[datetime.datetime]` — Filter results from this timestamp
    
</dd>
</dl>

<dl>
<dd>

**until_date:** `typing.Optional[datetime.datetime]` — Filter results until this timestamp
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**execution_metadata:** `typing.Optional[typing.List[str]]` — Filter by execution metadata (base64 encoded category:value pairs).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ExecutionMetadata
<details><summary><code>client.execution_metadata.<a href="src/fern/execution_metadata/client.py#L26-L52">get_execution_metadata</a>() -> ExecutionMetadataGetResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.execution_metadata.get_execution_metadata()

```
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

## Authentication
<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py#L25-L53">saml_login</a>(...) -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.authentication.saml_login()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**return_to:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py#L55-L83">saml_logout</a>(...) -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.authentication.saml_logout()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**return_to:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py#L85-L109">saml_login_callback</a>() -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.authentication.saml_login_callback()

```
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

<details><summary><code>client.authentication.<a href="src/fern/authentication/client.py#L111-L135">saml_logout_callback</a>() -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.authentication.saml_logout_callback()

```
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

## Users
<details><summary><code>client.users.<a href="src/fern/users/client.py#L30-L56">get_authenticated_user</a>() -> typing.Optional[UserResponse]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.get_authenticated_user()

```
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

<details><summary><code>client.users.<a href="src/fern/users/client.py#L58-L98">get_users</a>(...) -> UsersResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
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

**limit:** `typing.Optional[int]` — Maximum number of results to return (default: 50)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination (default: 0)
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search term for user email, name, launchpad handle, or id
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L100-L128">get_user</a>(...) -> UserResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.get_user(
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

**user_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L130-L157">delete_user</a>(...)</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.delete_user(
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

**user_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/fern/users/client.py#L159-L195">update_user</a>(...) -> UserResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.users.update_user(
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

**user_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**is_admin:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.teams.<a href="src/fern/teams/client.py#L31-L55">get_teams</a>() -> typing.List[TeamResponse]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.get_teams()

```
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

<details><summary><code>client.teams.<a href="src/fern/teams/client.py#L57-L103">create_team</a>(...) -> TeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new team
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.create_team(
    name="name",
)

```
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

**permissions:** `typing.Optional[typing.List[Permission]]` 
    
</dd>
</dl>

<dl>
<dd>

**artefact_matching_rules:** `typing.Optional[typing.List[ArtefactMatchingRuleBase]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py#L105-L133">get_team</a>(...) -> TeamResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.get_team(
    team_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py#L135-L179">update_team</a>(...) -> TeamResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.update_team(
    team_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**team_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[typing.List[Permission]]` 
    
</dd>
</dl>

<dl>
<dd>

**artefact_matching_rules:** `typing.Optional[typing.List[ArtefactMatchingRuleBase]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py#L181-L216">add_team_member</a>(...) -> TeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a user to a team
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.add_team_member(
    team_id=1,
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

**team_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.teams.<a href="src/fern/teams/client.py#L218-L253">remove_team_member</a>(...) -> TeamResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a user from a team
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.teams.remove_team_member(
    team_id=1,
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

**team_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `int` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.permissions.<a href="src/fern/permissions/client.py#L25-L49">get_permissions</a>() -> typing.Any</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.permissions.get_permissions()

```
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

## Applications
<details><summary><code>client.applications.<a href="src/fern/applications/client.py#L30-L56">get_applications</a>() -> typing.List[ApplicationResponse]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.get_applications()

```
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

<details><summary><code>client.applications.<a href="src/fern/applications/client.py#L58-L97">create_application</a>(...) -> ApplicationResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, Permission

client = FernApi(
    token="<token>",
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.create_application(
    name="name",
    permissions=[
        Permission.VIEW_USER
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.List[Permission]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/fern/applications/client.py#L99-L123">rotate_own_api_key</a>() -> ApplicationResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.rotate_own_api_key()

```
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

<details><summary><code>client.applications.<a href="src/fern/applications/client.py#L125-L155">rotate_api_key</a>(...) -> ApplicationResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.rotate_api_key(
    application_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**application_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/fern/applications/client.py#L157-L183">get_authenticated_application</a>() -> typing.Optional[ApplicationResponse]</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.get_authenticated_application()

```
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

<details><summary><code>client.applications.<a href="src/fern/applications/client.py#L185-L215">get_application</a>(...) -> ApplicationResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.get_application(
    application_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**application_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/fern/applications/client.py#L217-L246">delete_application</a>(...)</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.delete_application(
    application_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**application_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/fern/applications/client.py#L248-L286">update_application</a>(...) -> ApplicationResponse</code></summary>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.applications.update_application(
    application_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**application_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[typing.List[Permission]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notifications
<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py#L27-L71">get_own_notifications</a>(...) -> NotificationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all notifications for the authenticated user
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.notifications.get_own_notifications()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return (default: 50)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination (default: 0)
    
</dd>
</dl>

<dl>
<dd>

**unread_only:** `typing.Optional[bool]` — Whether to return only unread notifications (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py#L73-L106">get_own_notification_count</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the count of notifications for the authenticated user
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.notifications.get_own_notification_count()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unread_only:** `typing.Optional[bool]` — Whether to return only unread notifications (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py#L108-L140">mark_own_notification_as_read</a>(...) -> NotificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark the authenticated user's own notification as read
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.notifications.mark_own_notification_as_read(
    notification_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**notification_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py#L142-L192">get_notifications</a>(...) -> NotificationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all notifications for the specified user
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.notifications.get_notifications(
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

**user_id:** `int` — ID of the user whose notifications will be fetched
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return (default: 50)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination (default: 0)
    
</dd>
</dl>

<dl>
<dd>

**unread_only:** `typing.Optional[bool]` — Whether to return only unread notifications (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py#L194-L236">get_notification_count</a>(...) -> int</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the count of notifications for the specified user
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.notifications.get_notification_count(
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

**user_id:** `int` — ID of the user whose notification count will be fetched
    
</dd>
</dl>

<dl>
<dd>

**unread_only:** `typing.Optional[bool]` — Whether to return only unread notifications (default: false)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/fern/notifications/client.py#L238-L276">mark_notification_as_read</a>(...) -> NotificationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark a notification as read
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.notifications.mark_notification_as_read(
    user_id=1,
    notification_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `int` — ID of the user whose notification will be dismissed
    
</dd>
</dl>

<dl>
<dd>

**notification_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ArtefactMatchingRules
<details><summary><code>client.artefact_matching_rules.<a href="src/fern/artefact_matching_rules/client.py#L31-L61">get_artefact_matching_rules</a>(...) -> typing.List[ArtefactMatchingRuleResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all artefact matching rules, optionally filtered by family
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefact_matching_rules.get_artefact_matching_rules()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**family:** `typing.Optional[FamilyName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefact_matching_rules.<a href="src/fern/artefact_matching_rules/client.py#L63-L146">create_artefact_matching_rule</a>(...) -> ArtefactMatchingRuleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new artefact matching rule with at least one team
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, FamilyName

client = FernApi(
    token="<token>",
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefact_matching_rules.create_artefact_matching_rule(
    family=FamilyName.SNAP,
    team_ids=[
        1
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

**family:** `FamilyName` 
    
</dd>
</dl>

<dl>
<dd>

**team_ids:** `typing.List[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**stage:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**track:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**store:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**series:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**os:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**release:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**grant_permissions:** `typing.Optional[typing.List[Permission]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefact_matching_rules.<a href="src/fern/artefact_matching_rules/client.py#L148-L180">get_artefact_matching_rule</a>(...) -> ArtefactMatchingRuleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific artefact matching rule by ID
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefact_matching_rules.get_artefact_matching_rule(
    rule_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefact_matching_rules.<a href="src/fern/artefact_matching_rules/client.py#L182-L213">delete_artefact_matching_rule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an artefact matching rule
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefact_matching_rules.delete_artefact_matching_rule(
    rule_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.artefact_matching_rules.<a href="src/fern/artefact_matching_rules/client.py#L215-L301">update_artefact_matching_rule</a>(...) -> ArtefactMatchingRuleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an artefact matching rule
</dd>
</dl>
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
    csrf_token="<X-CSRF-Token>",
    base_url="https://yourhost.com/path/to/api",
)

client.artefact_matching_rules.update_artefact_matching_rule(
    rule_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**family:** `typing.Optional[FamilyName]` 
    
</dd>
</dl>

<dl>
<dd>

**stage:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**track:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**branch:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**store:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**series:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**os:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**release:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**team_ids:** `typing.Optional[typing.List[int]]` 
    
</dd>
</dl>

<dl>
<dd>

**grant_permissions:** `typing.Optional[typing.List[Permission]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

