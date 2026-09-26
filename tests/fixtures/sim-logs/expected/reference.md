# Reference
## Logs
<details><summary><code>client.logs.<a href="src/fern/logs/client.py">list_logs</a>(...) -> V2LogListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List logs with filters, selectable detail, sorting, and cursor pagination. `includeJobRuns=true` includes chat and Sim-agent jobs only with `sortBy=startedAt`, because other orderings are unsupported. `files` contains only run-produced files; use the files API for input attachments. Expired runs are permanently deleted. Retention is 30 days from run start on Free, unlimited on Pro and Team, and configured per organization on Enterprise with workspace overrides. Workspace folder trees exceeding 10,000 folders return `413`.

OAuth scope: `api:read`.
</dd>
</dl>
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.logs.list_logs(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `str` — Workspace whose execution logs should be returned.
    
</dd>
</dl>

<dl>
<dd>

**workflow_ids:** `typing.Optional[str]` — Comma-separated workflow identifiers to include. An empty entry is rejected. At most 200 entries.
    
</dd>
</dl>

<dl>
<dd>

**triggers:** `typing.Optional[str]` — Comma-separated, lowercase trigger types or webhook provider IDs. Matching is exact and case-sensitive; unknown values select no runs. An empty entry is rejected. The sentinel `all` disables this filter, even when listed with other values. At most 100 entries.
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[ListLogsRequestLevel]` — Severity level to include.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Only include runs started at or after this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — Only include runs started at or before this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.
    
</dd>
</dl>

<dl>
<dd>

**min_duration_ms:** `typing.Optional[int]` — Minimum total execution duration in milliseconds. Whole milliseconds from 0 to 2147483647; the stored duration is a 32-bit integer, so a fractional or out-of-range bound is rejected.
    
</dd>
</dl>

<dl>
<dd>

**max_duration_ms:** `typing.Optional[int]` — Maximum total execution duration in milliseconds. Whole milliseconds from 0 to 2147483647; the stored duration is a 32-bit integer, so a fractional or out-of-range bound is rejected.
    
</dd>
</dl>

<dl>
<dd>

**min_cost:** `typing.Optional[float]` — Minimum execution cost in USD, from 0 to 1000000. A run is never charged a negative amount, so a negative bound is rejected rather than treated as a filter that matches every run.
    
</dd>
</dl>

<dl>
<dd>

**max_cost:** `typing.Optional[float]` — Maximum execution cost in USD, from 0 to 1000000. A run is never charged a negative amount, so a negative bound is rejected rather than treated as a filter that matches every run.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — AI model used during execution.
    
</dd>
</dl>

<dl>
<dd>

**details:** `typing.Optional[ListLogsRequestDetails]` — Response detail level. `full` adds the `workflow` summary to every workflow run; a job run never carries one, whatever this is set to. `includeTraceSpans=true` and `includeFinalOutput=true` each imply `full`, so either one adds `workflow` even when `details=basic` is sent explicitly.
    
</dd>
</dl>

<dl>
<dd>

**include_trace_spans:** `typing.Optional[bool]` — Whether to include block-level trace spans. Implies `details=full`. Spans are pruned on their own retention schedule, so a run whose spans have aged out returns `traceSpans: []` rather than an error.
    
</dd>
</dl>

<dl>
<dd>

**include_final_output:** `typing.Optional[bool]` — Whether to include the final workflow output. Implies `details=full`, so the `workflow` summary is present regardless of what `details` is set to.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum log entries per page. Values outside 1–1000 are truncated and clamped into that range rather than rejected. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from the previous page. Send it back with the same sort and filters; only `limit` may change. Change anything else and pagination must restart without a cursor.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Comma-separated execution statuses to include, from `pending` | `running` | `paused` | `redacting` | `completed` | `failed` | `cancelled`. An empty entry is rejected. ANDed with `level`, which reports severity rather than lifecycle.
    
</dd>
</dl>

<dl>
<dd>

**workflow_name:** `typing.Optional[str]` — Case-insensitive substring match against the run's workflow name. Runs whose workflow has been deleted match nothing, because the name is no longer joinable.
    
</dd>
</dl>

<dl>
<dd>

**include_job_runs:** `typing.Optional[bool]` — Include Chat and Sim-agent jobs alongside workflow runs. Jobs use `kind: "job"` and have no workflow or cost ledger. Workflow, folder, model, or status filters exclude jobs. This option is valid only when sorting by `startedAt`.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` — Exact run identifier to match.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListLogsRequestSortBy]` — Field used to sort the result. `durationMs` and `cost` are null until a run settles; those runs sort before recorded values in ascending order and after them in descending order. Only `startedAt` can order Chat and Sim-agent job runs, so any other value is rejected when job runs are included.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListLogsRequestSortOrder]` — Sort direction.
    
</dd>
</dl>

<dl>
<dd>

**folder_paths:** `typing.Optional[str]` — Comma-separated workflow folder paths, including descendants. Up to 100 paths. Unknown folder paths contribute no matches.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.logs.<a href="src/fern/logs/client.py">get_log</a>(...) -> V2LogDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a run's workflow graph, trace spans, final output, and cost. Trace spans expire separately, so an empty `traceSpans` array does not prove none were recorded. Expired runs are permanently deleted. Retention is 30 days from run start on Free, unlimited on Pro and Team, and configured per organization on Enterprise with workspace overrides. Workspace folder trees exceeding 10,000 folders return `413`.

OAuth scope: `api:read`.
</dd>
</dl>
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.logs.get_log(
    run_id="runId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` — Unique workflow run identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.logs.<a href="src/fern/logs/client.py">get_log_stats</a>(...) -> V2LogStatsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get run counts, success and error counts, and latency by workspace or workflow. Default bounds span recorded runs, or the last 24 hours when empty. Buckets may extend past the end. Folder filters include descendants; `workflowsTruncated` affects series, not totals. Expired runs are permanently deleted. Retention is 30 days from run start on Free, unlimited on Pro and Team, and configured per organization on Enterprise with workspace overrides. Workspace folder trees exceeding 10,000 folders return `413`.

OAuth scope: `api:read`.
</dd>
</dl>
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
    environment=FernApiEnvironment.PRODUCTION,
)

client.logs.get_log_stats(
    workspace_id="workspaceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workspace_id:** `str` — Workspace whose execution statistics to summarize.
    
</dd>
</dl>

<dl>
<dd>

**workflow_ids:** `typing.Optional[str]` — Comma-separated workflow identifiers to include. At most 200 entries. An empty entry is rejected.
    
</dd>
</dl>

<dl>
<dd>

**folder_paths:** `typing.Optional[str]` — Comma-separated workflow folder paths, including descendants. Up to 100 paths. Unknown folder paths contribute no matches.
    
</dd>
</dl>

<dl>
<dd>

**triggers:** `typing.Optional[str]` — Comma-separated trigger types to include. An empty entry is rejected. The vocabulary is open, so an unrecognized member selects no runs; the literal `all` disables this filter.
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[GetLogStatsRequestLevel]` — Severity level to include.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Only include runs started at or after this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — Only include runs started at or before this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.
    
</dd>
</dl>

<dl>
<dd>

**segment_count:** `typing.Optional[int]` — Number of time buckets, up to 500. Exactly this many are returned, each at least one minute wide. Short windows extend past the requested end and include empty trailing buckets.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

