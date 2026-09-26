

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.v2error import V2Error
from ..types.v2log_detail_response import V2LogDetailResponse
from ..types.v2log_list_response import V2LogListResponse
from ..types.v2log_stats_response import V2LogStatsResponse
from .types.get_log_stats_request_level import GetLogStatsRequestLevel
from .types.list_logs_request_details import ListLogsRequestDetails
from .types.list_logs_request_level import ListLogsRequestLevel
from .types.list_logs_request_sort_by import ListLogsRequestSortBy
from .types.list_logs_request_sort_order import ListLogsRequestSortOrder
from pydantic import ValidationError


class RawLogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[V2LogListResponse]:
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
        HttpResponse[V2LogListResponse]
            A page of execution logs matching the filters.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/logs",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "workflowIds": workflow_ids,
                "triggers": triggers,
                "level": level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "minDurationMs": min_duration_ms,
                "maxDurationMs": max_duration_ms,
                "minCost": min_cost,
                "maxCost": max_cost,
                "model": model,
                "details": details,
                "includeTraceSpans": include_trace_spans,
                "includeFinalOutput": include_final_output,
                "limit": limit,
                "cursor": cursor,
                "status": status,
                "workflowName": workflow_name,
                "includeJobRuns": include_job_runs,
                "runId": run_id,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "folderPaths": folder_paths,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2LogListResponse,
                    parse_obj_as(
                        type_=V2LogListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_log(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V2LogDetailResponse]:
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
        HttpResponse[V2LogDetailResponse]
            The requested diagnostic log representation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/logs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2LogDetailResponse,
                    parse_obj_as(
                        type_=V2LogDetailResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[V2LogStatsResponse]:
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
        HttpResponse[V2LogStatsResponse]
            Bucketed execution statistics for the workspace.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/logs/stats",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "workflowIds": workflow_ids,
                "folderPaths": folder_paths,
                "triggers": triggers,
                "level": level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "segmentCount": segment_count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2LogStatsResponse,
                    parse_obj_as(
                        type_=V2LogStatsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[V2LogListResponse]:
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
        AsyncHttpResponse[V2LogListResponse]
            A page of execution logs matching the filters.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/logs",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "workflowIds": workflow_ids,
                "triggers": triggers,
                "level": level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "minDurationMs": min_duration_ms,
                "maxDurationMs": max_duration_ms,
                "minCost": min_cost,
                "maxCost": max_cost,
                "model": model,
                "details": details,
                "includeTraceSpans": include_trace_spans,
                "includeFinalOutput": include_final_output,
                "limit": limit,
                "cursor": cursor,
                "status": status,
                "workflowName": workflow_name,
                "includeJobRuns": include_job_runs,
                "runId": run_id,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "folderPaths": folder_paths,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2LogListResponse,
                    parse_obj_as(
                        type_=V2LogListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_log(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V2LogDetailResponse]:
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
        AsyncHttpResponse[V2LogDetailResponse]
            The requested diagnostic log representation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/logs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2LogDetailResponse,
                    parse_obj_as(
                        type_=V2LogDetailResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[V2LogStatsResponse]:
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
        AsyncHttpResponse[V2LogStatsResponse]
            Bucketed execution statistics for the workspace.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/logs/stats",
            method="GET",
            params={
                "workspaceId": workspace_id,
                "workflowIds": workflow_ids,
                "folderPaths": folder_paths,
                "triggers": triggers,
                "level": level,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "segmentCount": segment_count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V2LogStatsResponse,
                    parse_obj_as(
                        type_=V2LogStatsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        V2Error,
                        parse_obj_as(
                            type_=V2Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
