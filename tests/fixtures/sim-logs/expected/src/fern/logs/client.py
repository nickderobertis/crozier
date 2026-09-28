

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v2log_detail_response import V2LogDetailResponse
from ..types.v2log_list_response import V2LogListResponse
from ..types.v2log_stats_response import V2LogStatsResponse
from .raw_client import AsyncRawLogsClient, RawLogsClient
from .types.get_log_stats_request_level import GetLogStatsRequestLevel
from .types.list_logs_request_details import ListLogsRequestDetails
from .types.list_logs_request_level import ListLogsRequestLevel
from .types.list_logs_request_sort_by import ListLogsRequestSortBy
from .types.list_logs_request_sort_order import ListLogsRequestSortOrder


class LogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLogsClient
        """
        return self._raw_client

    def list_logs(
        self,
        *,
        workspace_id: str,
        workflow_ids: typing.Optional[str] = None,
        triggers: typing.Optional[str] = None,
        level: typing.Optional[ListLogsRequestLevel] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        min_duration_ms: typing.Optional[int] = None,
        max_duration_ms: typing.Optional[int] = None,
        min_cost: typing.Optional[float] = None,
        max_cost: typing.Optional[float] = None,
        model: typing.Optional[str] = None,
        details: typing.Optional[ListLogsRequestDetails] = None,
        include_trace_spans: typing.Optional[bool] = None,
        include_final_output: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        workflow_name: typing.Optional[str] = None,
        include_job_runs: typing.Optional[bool] = None,
        run_id: typing.Optional[str] = None,
        sort_by: typing.Optional[ListLogsRequestSortBy] = None,
        sort_order: typing.Optional[ListLogsRequestSortOrder] = None,
        folder_paths: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2LogListResponse:
        """
        List logs with filters, selectable detail, sorting, and cursor pagination. `includeJobRuns=true` includes chat and Sim-agent jobs only with `sortBy=startedAt`, because other orderings are unsupported. `files` contains only run-produced files; use the files API for input attachments. Expired runs are permanently deleted. Retention is 30 days from run start on Free, unlimited on Pro and Team, and configured per organization on Enterprise with workspace overrides. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        workspace_id : str
            Workspace whose execution logs should be returned.

        workflow_ids : typing.Optional[str]
            Comma-separated workflow identifiers to include. An empty entry is rejected. At most 200 entries.

        triggers : typing.Optional[str]
            Comma-separated, lowercase trigger types or webhook provider IDs. Matching is exact and case-sensitive; unknown values select no runs. An empty entry is rejected. The sentinel `all` disables this filter, even when listed with other values. At most 100 entries.

        level : typing.Optional[ListLogsRequestLevel]
            Severity level to include.

        start_date : typing.Optional[dt.datetime]
            Only include runs started at or after this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.

        end_date : typing.Optional[dt.datetime]
            Only include runs started at or before this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.

        min_duration_ms : typing.Optional[int]
            Minimum total execution duration in milliseconds. Whole milliseconds from 0 to 2147483647; the stored duration is a 32-bit integer, so a fractional or out-of-range bound is rejected.

        max_duration_ms : typing.Optional[int]
            Maximum total execution duration in milliseconds. Whole milliseconds from 0 to 2147483647; the stored duration is a 32-bit integer, so a fractional or out-of-range bound is rejected.

        min_cost : typing.Optional[float]
            Minimum execution cost in USD, from 0 to 1000000. A run is never charged a negative amount, so a negative bound is rejected rather than treated as a filter that matches every run.

        max_cost : typing.Optional[float]
            Maximum execution cost in USD, from 0 to 1000000. A run is never charged a negative amount, so a negative bound is rejected rather than treated as a filter that matches every run.

        model : typing.Optional[str]
            AI model used during execution.

        details : typing.Optional[ListLogsRequestDetails]
            Response detail level. `full` adds the `workflow` summary to every workflow run; a job run never carries one, whatever this is set to. `includeTraceSpans=true` and `includeFinalOutput=true` each imply `full`, so either one adds `workflow` even when `details=basic` is sent explicitly.

        include_trace_spans : typing.Optional[bool]
            Whether to include block-level trace spans. Implies `details=full`. Spans are pruned on their own retention schedule, so a run whose spans have aged out returns `traceSpans: []` rather than an error.

        include_final_output : typing.Optional[bool]
            Whether to include the final workflow output. Implies `details=full`, so the `workflow` summary is present regardless of what `details` is set to.

        limit : typing.Optional[int]
            Maximum log entries per page. Values outside 1–1000 are truncated and clamped into that range rather than rejected. Defaults to 100.

        cursor : typing.Optional[str]
            Opaque cursor from the previous page. Send it back with the same sort and filters; only `limit` may change. Change anything else and pagination must restart without a cursor.

        status : typing.Optional[str]
            Comma-separated execution statuses to include, from `pending` | `running` | `paused` | `redacting` | `completed` | `failed` | `cancelled`. An empty entry is rejected. ANDed with `level`, which reports severity rather than lifecycle.

        workflow_name : typing.Optional[str]
            Case-insensitive substring match against the run's workflow name. Runs whose workflow has been deleted match nothing, because the name is no longer joinable.

        include_job_runs : typing.Optional[bool]
            Include Chat and Sim-agent jobs alongside workflow runs. Jobs use `kind: "job"` and have no workflow or cost ledger. Workflow, folder, model, or status filters exclude jobs. This option is valid only when sorting by `startedAt`.

        run_id : typing.Optional[str]
            Exact run identifier to match.

        sort_by : typing.Optional[ListLogsRequestSortBy]
            Field used to sort the result. `durationMs` and `cost` are null until a run settles; those runs sort before recorded values in ascending order and after them in descending order. Only `startedAt` can order Chat and Sim-agent job runs, so any other value is rejected when job runs are included.

        sort_order : typing.Optional[ListLogsRequestSortOrder]
            Sort direction.

        folder_paths : typing.Optional[str]
            Comma-separated workflow folder paths, including descendants. Up to 100 paths. Unknown folder paths contribute no matches.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2LogListResponse
            A page of execution logs matching the filters.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.logs.list_logs(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_logs(
            workspace_id=workspace_id,
            workflow_ids=workflow_ids,
            triggers=triggers,
            level=level,
            start_date=start_date,
            end_date=end_date,
            min_duration_ms=min_duration_ms,
            max_duration_ms=max_duration_ms,
            min_cost=min_cost,
            max_cost=max_cost,
            model=model,
            details=details,
            include_trace_spans=include_trace_spans,
            include_final_output=include_final_output,
            limit=limit,
            cursor=cursor,
            status=status,
            workflow_name=workflow_name,
            include_job_runs=include_job_runs,
            run_id=run_id,
            sort_by=sort_by,
            sort_order=sort_order,
            folder_paths=folder_paths,
            request_options=request_options,
        )
        return _response.data

    def get_log(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> V2LogDetailResponse:
        """
        Get a run's workflow graph, trace spans, final output, and cost. Trace spans expire separately, so an empty `traceSpans` array does not prove none were recorded. Expired runs are permanently deleted. Retention is 30 days from run start on Free, unlimited on Pro and Team, and configured per organization on Enterprise with workspace overrides. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        run_id : str
            Unique workflow run identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2LogDetailResponse
            The requested diagnostic log representation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.logs.get_log(
            run_id="runId",
        )
        """
        _response = self._raw_client.get_log(run_id, request_options=request_options)
        return _response.data

    def get_log_stats(
        self,
        *,
        workspace_id: str,
        workflow_ids: typing.Optional[str] = None,
        folder_paths: typing.Optional[str] = None,
        triggers: typing.Optional[str] = None,
        level: typing.Optional[GetLogStatsRequestLevel] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        segment_count: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2LogStatsResponse:
        """
        Get run counts, success and error counts, and latency by workspace or workflow. Default bounds span recorded runs, or the last 24 hours when empty. Buckets may extend past the end. Folder filters include descendants; `workflowsTruncated` affects series, not totals. Expired runs are permanently deleted. Retention is 30 days from run start on Free, unlimited on Pro and Team, and configured per organization on Enterprise with workspace overrides. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        workspace_id : str
            Workspace whose execution statistics to summarize.

        workflow_ids : typing.Optional[str]
            Comma-separated workflow identifiers to include. At most 200 entries. An empty entry is rejected.

        folder_paths : typing.Optional[str]
            Comma-separated workflow folder paths, including descendants. Up to 100 paths. Unknown folder paths contribute no matches.

        triggers : typing.Optional[str]
            Comma-separated trigger types to include. An empty entry is rejected. The vocabulary is open, so an unrecognized member selects no runs; the literal `all` disables this filter.

        level : typing.Optional[GetLogStatsRequestLevel]
            Severity level to include.

        start_date : typing.Optional[dt.datetime]
            Only include runs started at or after this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.

        end_date : typing.Optional[dt.datetime]
            Only include runs started at or before this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.

        segment_count : typing.Optional[int]
            Number of time buckets, up to 500. Exactly this many are returned, each at least one minute wide. Short windows extend past the requested end and include empty trailing buckets.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2LogStatsResponse
            Bucketed execution statistics for the workspace.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.logs.get_log_stats(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_log_stats(
            workspace_id=workspace_id,
            workflow_ids=workflow_ids,
            folder_paths=folder_paths,
            triggers=triggers,
            level=level,
            start_date=start_date,
            end_date=end_date,
            segment_count=segment_count,
            request_options=request_options,
        )
        return _response.data


class AsyncLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLogsClient
        """
        return self._raw_client

    async def list_logs(
        self,
        *,
        workspace_id: str,
        workflow_ids: typing.Optional[str] = None,
        triggers: typing.Optional[str] = None,
        level: typing.Optional[ListLogsRequestLevel] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        min_duration_ms: typing.Optional[int] = None,
        max_duration_ms: typing.Optional[int] = None,
        min_cost: typing.Optional[float] = None,
        max_cost: typing.Optional[float] = None,
        model: typing.Optional[str] = None,
        details: typing.Optional[ListLogsRequestDetails] = None,
        include_trace_spans: typing.Optional[bool] = None,
        include_final_output: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        workflow_name: typing.Optional[str] = None,
        include_job_runs: typing.Optional[bool] = None,
        run_id: typing.Optional[str] = None,
        sort_by: typing.Optional[ListLogsRequestSortBy] = None,
        sort_order: typing.Optional[ListLogsRequestSortOrder] = None,
        folder_paths: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2LogListResponse:
        """
        List logs with filters, selectable detail, sorting, and cursor pagination. `includeJobRuns=true` includes chat and Sim-agent jobs only with `sortBy=startedAt`, because other orderings are unsupported. `files` contains only run-produced files; use the files API for input attachments. Expired runs are permanently deleted. Retention is 30 days from run start on Free, unlimited on Pro and Team, and configured per organization on Enterprise with workspace overrides. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        workspace_id : str
            Workspace whose execution logs should be returned.

        workflow_ids : typing.Optional[str]
            Comma-separated workflow identifiers to include. An empty entry is rejected. At most 200 entries.

        triggers : typing.Optional[str]
            Comma-separated, lowercase trigger types or webhook provider IDs. Matching is exact and case-sensitive; unknown values select no runs. An empty entry is rejected. The sentinel `all` disables this filter, even when listed with other values. At most 100 entries.

        level : typing.Optional[ListLogsRequestLevel]
            Severity level to include.

        start_date : typing.Optional[dt.datetime]
            Only include runs started at or after this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.

        end_date : typing.Optional[dt.datetime]
            Only include runs started at or before this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.

        min_duration_ms : typing.Optional[int]
            Minimum total execution duration in milliseconds. Whole milliseconds from 0 to 2147483647; the stored duration is a 32-bit integer, so a fractional or out-of-range bound is rejected.

        max_duration_ms : typing.Optional[int]
            Maximum total execution duration in milliseconds. Whole milliseconds from 0 to 2147483647; the stored duration is a 32-bit integer, so a fractional or out-of-range bound is rejected.

        min_cost : typing.Optional[float]
            Minimum execution cost in USD, from 0 to 1000000. A run is never charged a negative amount, so a negative bound is rejected rather than treated as a filter that matches every run.

        max_cost : typing.Optional[float]
            Maximum execution cost in USD, from 0 to 1000000. A run is never charged a negative amount, so a negative bound is rejected rather than treated as a filter that matches every run.

        model : typing.Optional[str]
            AI model used during execution.

        details : typing.Optional[ListLogsRequestDetails]
            Response detail level. `full` adds the `workflow` summary to every workflow run; a job run never carries one, whatever this is set to. `includeTraceSpans=true` and `includeFinalOutput=true` each imply `full`, so either one adds `workflow` even when `details=basic` is sent explicitly.

        include_trace_spans : typing.Optional[bool]
            Whether to include block-level trace spans. Implies `details=full`. Spans are pruned on their own retention schedule, so a run whose spans have aged out returns `traceSpans: []` rather than an error.

        include_final_output : typing.Optional[bool]
            Whether to include the final workflow output. Implies `details=full`, so the `workflow` summary is present regardless of what `details` is set to.

        limit : typing.Optional[int]
            Maximum log entries per page. Values outside 1–1000 are truncated and clamped into that range rather than rejected. Defaults to 100.

        cursor : typing.Optional[str]
            Opaque cursor from the previous page. Send it back with the same sort and filters; only `limit` may change. Change anything else and pagination must restart without a cursor.

        status : typing.Optional[str]
            Comma-separated execution statuses to include, from `pending` | `running` | `paused` | `redacting` | `completed` | `failed` | `cancelled`. An empty entry is rejected. ANDed with `level`, which reports severity rather than lifecycle.

        workflow_name : typing.Optional[str]
            Case-insensitive substring match against the run's workflow name. Runs whose workflow has been deleted match nothing, because the name is no longer joinable.

        include_job_runs : typing.Optional[bool]
            Include Chat and Sim-agent jobs alongside workflow runs. Jobs use `kind: "job"` and have no workflow or cost ledger. Workflow, folder, model, or status filters exclude jobs. This option is valid only when sorting by `startedAt`.

        run_id : typing.Optional[str]
            Exact run identifier to match.

        sort_by : typing.Optional[ListLogsRequestSortBy]
            Field used to sort the result. `durationMs` and `cost` are null until a run settles; those runs sort before recorded values in ascending order and after them in descending order. Only `startedAt` can order Chat and Sim-agent job runs, so any other value is rejected when job runs are included.

        sort_order : typing.Optional[ListLogsRequestSortOrder]
            Sort direction.

        folder_paths : typing.Optional[str]
            Comma-separated workflow folder paths, including descendants. Up to 100 paths. Unknown folder paths contribute no matches.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2LogListResponse
            A page of execution logs matching the filters.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.logs.list_logs(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_logs(
            workspace_id=workspace_id,
            workflow_ids=workflow_ids,
            triggers=triggers,
            level=level,
            start_date=start_date,
            end_date=end_date,
            min_duration_ms=min_duration_ms,
            max_duration_ms=max_duration_ms,
            min_cost=min_cost,
            max_cost=max_cost,
            model=model,
            details=details,
            include_trace_spans=include_trace_spans,
            include_final_output=include_final_output,
            limit=limit,
            cursor=cursor,
            status=status,
            workflow_name=workflow_name,
            include_job_runs=include_job_runs,
            run_id=run_id,
            sort_by=sort_by,
            sort_order=sort_order,
            folder_paths=folder_paths,
            request_options=request_options,
        )
        return _response.data

    async def get_log(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V2LogDetailResponse:
        """
        Get a run's workflow graph, trace spans, final output, and cost. Trace spans expire separately, so an empty `traceSpans` array does not prove none were recorded. Expired runs are permanently deleted. Retention is 30 days from run start on Free, unlimited on Pro and Team, and configured per organization on Enterprise with workspace overrides. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        run_id : str
            Unique workflow run identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2LogDetailResponse
            The requested diagnostic log representation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.logs.get_log(
                run_id="runId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log(run_id, request_options=request_options)
        return _response.data

    async def get_log_stats(
        self,
        *,
        workspace_id: str,
        workflow_ids: typing.Optional[str] = None,
        folder_paths: typing.Optional[str] = None,
        triggers: typing.Optional[str] = None,
        level: typing.Optional[GetLogStatsRequestLevel] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        segment_count: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2LogStatsResponse:
        """
        Get run counts, success and error counts, and latency by workspace or workflow. Default bounds span recorded runs, or the last 24 hours when empty. Buckets may extend past the end. Folder filters include descendants; `workflowsTruncated` affects series, not totals. Expired runs are permanently deleted. Retention is 30 days from run start on Free, unlimited on Pro and Team, and configured per organization on Enterprise with workspace overrides. Workspace folder trees exceeding 10,000 folders return `413`.

        OAuth scope: `api:read`.

        Parameters
        ----------
        workspace_id : str
            Workspace whose execution statistics to summarize.

        workflow_ids : typing.Optional[str]
            Comma-separated workflow identifiers to include. At most 200 entries. An empty entry is rejected.

        folder_paths : typing.Optional[str]
            Comma-separated workflow folder paths, including descendants. Up to 100 paths. Unknown folder paths contribute no matches.

        triggers : typing.Optional[str]
            Comma-separated trigger types to include. An empty entry is rejected. The vocabulary is open, so an unrecognized member selects no runs; the literal `all` disables this filter.

        level : typing.Optional[GetLogStatsRequestLevel]
            Severity level to include.

        start_date : typing.Optional[dt.datetime]
            Only include runs started at or after this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.

        end_date : typing.Optional[dt.datetime]
            Only include runs started at or before this UTC ISO 8601 timestamp, e.g. `2026-08-06T00:00:00Z`. A date without a time, or a timestamp carrying a UTC offset instead of `Z`, is rejected, as is year `0000`, which names no storable instant.

        segment_count : typing.Optional[int]
            Number of time buckets, up to 500. Exactly this many are returned, each at least one minute wide. Short windows extend past the requested end and include empty trailing buckets.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2LogStatsResponse
            Bucketed execution statistics for the workspace.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.logs.get_log_stats(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log_stats(
            workspace_id=workspace_id,
            workflow_ids=workflow_ids,
            folder_paths=folder_paths,
            triggers=triggers,
            level=level,
            start_date=start_date,
            end_date=end_date,
            segment_count=segment_count,
            request_options=request_options,
        )
        return _response.data
