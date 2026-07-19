

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.comparison_operator import ComparisonOperator
from ..types.http_validation_error import HttpValidationError
from ..types.run import Run
from ..types.stop_reason_type import StopReasonType
from .types.list_internal_runs_request_duration_operator import ListInternalRunsRequestDurationOperator
from .types.list_internal_runs_request_order import ListInternalRunsRequestOrder
from .types.list_internal_runs_request_order_by import ListInternalRunsRequestOrderBy
from pydantic import ValidationError


class RawInternalRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_internal_runs(
        self,
        *,
        run_id: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        agent_ids: typing.Optional[typing.Sequence[str]] = None,
        statuses: typing.Optional[typing.Sequence[str]] = None,
        background: typing.Optional[bool] = None,
        stop_reason: typing.Optional[StopReasonType] = None,
        template_family: typing.Optional[str] = None,
        step_count: typing.Optional[int] = None,
        step_count_operator: typing.Optional[ComparisonOperator] = None,
        tools_used: typing.Optional[typing.Sequence[str]] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListInternalRunsRequestOrder] = None,
        order_by: typing.Optional[ListInternalRunsRequestOrderBy] = None,
        active: typing.Optional[bool] = None,
        ascending: typing.Optional[bool] = None,
        project_id: typing.Optional[str] = None,
        conversation_id: typing.Optional[str] = None,
        duration_percentile: typing.Optional[int] = None,
        duration_value: typing.Optional[int] = None,
        duration_operator: typing.Optional[ListInternalRunsRequestDurationOperator] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Run]]:
        """
        List all runs.

        Parameters
        ----------
        run_id : typing.Optional[str]
            Filter by a specific run ID.

        agent_id : typing.Optional[str]
            The unique identifier of the agent associated with the run.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The unique identifiers of the agents associated with the run. Deprecated in favor of agent_id field.

        statuses : typing.Optional[typing.Sequence[str]]
            Filter runs by status. Can specify multiple statuses.

        background : typing.Optional[bool]
            If True, filters for runs that were created in background mode.

        stop_reason : typing.Optional[StopReasonType]
            Filter runs by stop reason.

        template_family : typing.Optional[str]
            Filter runs by template family (base_template_id).

        step_count : typing.Optional[int]
            Filter runs by step count. Must be provided with step_count_operator.

        step_count_operator : typing.Optional[ComparisonOperator]
            Operator for step_count filter: 'eq' for equals, 'gte' for greater than or equal, 'lte' for less than or equal.

        tools_used : typing.Optional[typing.Sequence[str]]
            Filter runs that used any of the specified tools.

        before : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come before this run ID in the specified sort order

        after : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come after this run ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of runs to return

        order : typing.Optional[ListInternalRunsRequestOrder]
            Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListInternalRunsRequestOrderBy]
            Field to sort by

        active : typing.Optional[bool]
            Filter for active runs.

        ascending : typing.Optional[bool]
            Whether to sort agents oldest to newest (True) or newest to oldest (False, default). Deprecated in favor of order field.

        project_id : typing.Optional[str]
            Filter runs by project ID.

        conversation_id : typing.Optional[str]
            Filter runs by conversation ID.

        duration_percentile : typing.Optional[int]
            Filter runs by duration percentile (1-100). Returns runs slower than this percentile.

        duration_value : typing.Optional[int]
            Duration value in nanoseconds for filtering. Must be used with duration_operator.

        duration_operator : typing.Optional[ListInternalRunsRequestDurationOperator]
            Comparison operator for duration filter: 'gt' (greater than), 'lt' (less than), 'eq' (equals).

        start_date : typing.Optional[dt.datetime]
            Filter runs created on or after this date (ISO 8601 format).

        end_date : typing.Optional[dt.datetime]
            Filter runs created on or before this date (ISO 8601 format).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Run]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/_internal_runs/",
            method="GET",
            params={
                "run_id": run_id,
                "agent_id": agent_id,
                "agent_ids": agent_ids,
                "statuses": statuses,
                "background": background,
                "stop_reason": stop_reason,
                "template_family": template_family,
                "step_count": step_count,
                "step_count_operator": step_count_operator,
                "tools_used": tools_used,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "active": active,
                "ascending": ascending,
                "project_id": project_id,
                "conversation_id": conversation_id,
                "duration_percentile": duration_percentile,
                "duration_value": duration_value,
                "duration_operator": duration_operator,
                "start_date": serialize_datetime(start_date) if start_date is not None else None,
                "end_date": serialize_datetime(end_date) if end_date is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Run],
                    parse_obj_as(
                        type_=typing.List[Run],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawInternalRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_internal_runs(
        self,
        *,
        run_id: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        agent_ids: typing.Optional[typing.Sequence[str]] = None,
        statuses: typing.Optional[typing.Sequence[str]] = None,
        background: typing.Optional[bool] = None,
        stop_reason: typing.Optional[StopReasonType] = None,
        template_family: typing.Optional[str] = None,
        step_count: typing.Optional[int] = None,
        step_count_operator: typing.Optional[ComparisonOperator] = None,
        tools_used: typing.Optional[typing.Sequence[str]] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListInternalRunsRequestOrder] = None,
        order_by: typing.Optional[ListInternalRunsRequestOrderBy] = None,
        active: typing.Optional[bool] = None,
        ascending: typing.Optional[bool] = None,
        project_id: typing.Optional[str] = None,
        conversation_id: typing.Optional[str] = None,
        duration_percentile: typing.Optional[int] = None,
        duration_value: typing.Optional[int] = None,
        duration_operator: typing.Optional[ListInternalRunsRequestDurationOperator] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Run]]:
        """
        List all runs.

        Parameters
        ----------
        run_id : typing.Optional[str]
            Filter by a specific run ID.

        agent_id : typing.Optional[str]
            The unique identifier of the agent associated with the run.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The unique identifiers of the agents associated with the run. Deprecated in favor of agent_id field.

        statuses : typing.Optional[typing.Sequence[str]]
            Filter runs by status. Can specify multiple statuses.

        background : typing.Optional[bool]
            If True, filters for runs that were created in background mode.

        stop_reason : typing.Optional[StopReasonType]
            Filter runs by stop reason.

        template_family : typing.Optional[str]
            Filter runs by template family (base_template_id).

        step_count : typing.Optional[int]
            Filter runs by step count. Must be provided with step_count_operator.

        step_count_operator : typing.Optional[ComparisonOperator]
            Operator for step_count filter: 'eq' for equals, 'gte' for greater than or equal, 'lte' for less than or equal.

        tools_used : typing.Optional[typing.Sequence[str]]
            Filter runs that used any of the specified tools.

        before : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come before this run ID in the specified sort order

        after : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come after this run ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of runs to return

        order : typing.Optional[ListInternalRunsRequestOrder]
            Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListInternalRunsRequestOrderBy]
            Field to sort by

        active : typing.Optional[bool]
            Filter for active runs.

        ascending : typing.Optional[bool]
            Whether to sort agents oldest to newest (True) or newest to oldest (False, default). Deprecated in favor of order field.

        project_id : typing.Optional[str]
            Filter runs by project ID.

        conversation_id : typing.Optional[str]
            Filter runs by conversation ID.

        duration_percentile : typing.Optional[int]
            Filter runs by duration percentile (1-100). Returns runs slower than this percentile.

        duration_value : typing.Optional[int]
            Duration value in nanoseconds for filtering. Must be used with duration_operator.

        duration_operator : typing.Optional[ListInternalRunsRequestDurationOperator]
            Comparison operator for duration filter: 'gt' (greater than), 'lt' (less than), 'eq' (equals).

        start_date : typing.Optional[dt.datetime]
            Filter runs created on or after this date (ISO 8601 format).

        end_date : typing.Optional[dt.datetime]
            Filter runs created on or before this date (ISO 8601 format).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Run]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/_internal_runs/",
            method="GET",
            params={
                "run_id": run_id,
                "agent_id": agent_id,
                "agent_ids": agent_ids,
                "statuses": statuses,
                "background": background,
                "stop_reason": stop_reason,
                "template_family": template_family,
                "step_count": step_count,
                "step_count_operator": step_count_operator,
                "tools_used": tools_used,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "active": active,
                "ascending": ascending,
                "project_id": project_id,
                "conversation_id": conversation_id,
                "duration_percentile": duration_percentile,
                "duration_value": duration_value,
                "duration_operator": duration_operator,
                "start_date": serialize_datetime(start_date) if start_date is not None else None,
                "end_date": serialize_datetime(end_date) if end_date is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Run],
                    parse_obj_as(
                        type_=typing.List[Run],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
