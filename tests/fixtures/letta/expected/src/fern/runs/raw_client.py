

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.letta_message_union import LettaMessageUnion
from ..types.run import Run
from ..types.run_metrics import RunMetrics
from ..types.step import Step
from ..types.stop_reason_type import StopReasonType
from ..types.usage_statistics import UsageStatistics
from .types.list_messages_for_run_request_order import ListMessagesForRunRequestOrder
from .types.list_messages_for_run_request_order_by import ListMessagesForRunRequestOrderBy
from .types.list_runs_request_order import ListRunsRequestOrder
from .types.list_runs_request_order_by import ListRunsRequestOrderBy
from .types.list_steps_for_run_request_order import ListStepsForRunRequestOrder
from .types.list_steps_for_run_request_order_by import ListStepsForRunRequestOrderBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_runs(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        agent_ids: typing.Optional[typing.Sequence[str]] = None,
        statuses: typing.Optional[typing.Sequence[str]] = None,
        background: typing.Optional[bool] = None,
        stop_reason: typing.Optional[StopReasonType] = None,
        conversation_id: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListRunsRequestOrder] = None,
        order_by: typing.Optional[ListRunsRequestOrderBy] = None,
        active: typing.Optional[bool] = None,
        ascending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Run]]:
        """
        List all runs.

        Parameters
        ----------
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

        conversation_id : typing.Optional[str]
            Filter runs by conversation ID.

        before : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come before this run ID in the specified sort order

        after : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come after this run ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of runs to return

        order : typing.Optional[ListRunsRequestOrder]
            Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListRunsRequestOrderBy]
            Field to sort by

        active : typing.Optional[bool]
            Filter for active runs.

        ascending : typing.Optional[bool]
            Whether to sort agents oldest to newest (True) or newest to oldest (False, default). Deprecated in favor of order field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Run]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/runs/",
            method="GET",
            params={
                "agent_id": agent_id,
                "agent_ids": agent_ids,
                "statuses": statuses,
                "background": background,
                "stop_reason": stop_reason,
                "conversation_id": conversation_id,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "active": active,
                "ascending": ascending,
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

    def list_active_runs(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        background: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Run]]:
        """
        List all active runs.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The unique identifier of the agent associated with the run.

        background : typing.Optional[bool]
            If True, filters for runs that were created in background mode.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Run]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/runs/active",
            method="GET",
            params={
                "agent_id": agent_id,
                "background": background,
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

    def retrieve_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Run]:
        """
        Get the status of a run.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Run]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Run,
                    parse_obj_as(
                        type_=Run,
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

    def delete_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a run by its run_id.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def list_messages_for_run(
        self,
        run_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForRunRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForRunRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[LettaMessageUnion]]:
        """
        Get response messages associated with a run.

        Parameters
        ----------
        run_id : str

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForRunRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForRunRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LettaMessageUnion]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/messages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LettaMessageUnion],
                    parse_obj_as(
                        type_=typing.List[LettaMessageUnion],
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

    def retrieve_usage_for_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UsageStatistics]:
        """
        Get usage statistics for a run.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsageStatistics]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/usage",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsageStatistics,
                    parse_obj_as(
                        type_=UsageStatistics,
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

    def retrieve_metrics_for_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RunMetrics]:
        """
        Get run metrics by run ID.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunMetrics]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/metrics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunMetrics,
                    parse_obj_as(
                        type_=RunMetrics,
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

    def list_steps_for_run(
        self,
        run_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListStepsForRunRequestOrder] = None,
        order_by: typing.Optional[ListStepsForRunRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Step]]:
        """
        Get steps associated with a run with filtering options.

        Parameters
        ----------
        run_id : str

        before : typing.Optional[str]
            Cursor for pagination

        after : typing.Optional[str]
            Cursor for pagination

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListStepsForRunRequestOrder]
            Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListStepsForRunRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Step]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/steps",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Step],
                    parse_obj_as(
                        type_=typing.List[Step],
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

    def retrieve_trace_for_run(
        self,
        run_id: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[typing.Dict[str, typing.Any]]]:
        """
        Retrieve OTEL trace spans for a run.

        Returns a filtered set of spans relevant for observability:
        - agent_step: Individual agent reasoning steps
        - tool executions: Tool call spans
        - Root span: The top-level request span
        - time_to_first_token: TTFT measurement span

        Requires ClickHouse to be configured for trace storage.

        Parameters
        ----------
        run_id : str

        limit : typing.Optional[int]
            Maximum number of spans to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Dict[str, typing.Any]]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/trace",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Dict[str, typing.Any]],
                    parse_obj_as(
                        type_=typing.List[typing.Dict[str, typing.Any]],
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

    def retrieve_stream_for_run(
        self,
        run_id: str,
        *,
        starting_after: typing.Optional[int] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        poll_interval: typing.Optional[float] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        run_id : str

        starting_after : typing.Optional[int]
            Sequence id to use as a cursor for pagination. Response will start streaming after this chunk sequence id

        include_pings : typing.Optional[bool]
            Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.

        poll_interval : typing.Optional[float]
            Seconds to wait between polls when no new data.

        batch_size : typing.Optional[int]
            Number of entries to read per batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/stream",
            method="POST",
            json={
                "starting_after": starting_after,
                "include_pings": include_pings,
                "poll_interval": poll_interval,
                "batch_size": batch_size,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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


class AsyncRawRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_runs(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        agent_ids: typing.Optional[typing.Sequence[str]] = None,
        statuses: typing.Optional[typing.Sequence[str]] = None,
        background: typing.Optional[bool] = None,
        stop_reason: typing.Optional[StopReasonType] = None,
        conversation_id: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListRunsRequestOrder] = None,
        order_by: typing.Optional[ListRunsRequestOrderBy] = None,
        active: typing.Optional[bool] = None,
        ascending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Run]]:
        """
        List all runs.

        Parameters
        ----------
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

        conversation_id : typing.Optional[str]
            Filter runs by conversation ID.

        before : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come before this run ID in the specified sort order

        after : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come after this run ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of runs to return

        order : typing.Optional[ListRunsRequestOrder]
            Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListRunsRequestOrderBy]
            Field to sort by

        active : typing.Optional[bool]
            Filter for active runs.

        ascending : typing.Optional[bool]
            Whether to sort agents oldest to newest (True) or newest to oldest (False, default). Deprecated in favor of order field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Run]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/runs/",
            method="GET",
            params={
                "agent_id": agent_id,
                "agent_ids": agent_ids,
                "statuses": statuses,
                "background": background,
                "stop_reason": stop_reason,
                "conversation_id": conversation_id,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "active": active,
                "ascending": ascending,
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

    async def list_active_runs(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        background: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Run]]:
        """
        List all active runs.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The unique identifier of the agent associated with the run.

        background : typing.Optional[bool]
            If True, filters for runs that were created in background mode.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Run]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/runs/active",
            method="GET",
            params={
                "agent_id": agent_id,
                "background": background,
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

    async def retrieve_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Run]:
        """
        Get the status of a run.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Run]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Run,
                    parse_obj_as(
                        type_=Run,
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

    async def delete_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a run by its run_id.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def list_messages_for_run(
        self,
        run_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForRunRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForRunRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[LettaMessageUnion]]:
        """
        Get response messages associated with a run.

        Parameters
        ----------
        run_id : str

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForRunRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForRunRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LettaMessageUnion]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/messages",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LettaMessageUnion],
                    parse_obj_as(
                        type_=typing.List[LettaMessageUnion],
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

    async def retrieve_usage_for_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UsageStatistics]:
        """
        Get usage statistics for a run.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsageStatistics]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/usage",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsageStatistics,
                    parse_obj_as(
                        type_=UsageStatistics,
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

    async def retrieve_metrics_for_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RunMetrics]:
        """
        Get run metrics by run ID.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunMetrics]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/metrics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunMetrics,
                    parse_obj_as(
                        type_=RunMetrics,
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

    async def list_steps_for_run(
        self,
        run_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListStepsForRunRequestOrder] = None,
        order_by: typing.Optional[ListStepsForRunRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Step]]:
        """
        Get steps associated with a run with filtering options.

        Parameters
        ----------
        run_id : str

        before : typing.Optional[str]
            Cursor for pagination

        after : typing.Optional[str]
            Cursor for pagination

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListStepsForRunRequestOrder]
            Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListStepsForRunRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Step]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/steps",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Step],
                    parse_obj_as(
                        type_=typing.List[Step],
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

    async def retrieve_trace_for_run(
        self,
        run_id: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[typing.Dict[str, typing.Any]]]:
        """
        Retrieve OTEL trace spans for a run.

        Returns a filtered set of spans relevant for observability:
        - agent_step: Individual agent reasoning steps
        - tool executions: Tool call spans
        - Root span: The top-level request span
        - time_to_first_token: TTFT measurement span

        Requires ClickHouse to be configured for trace storage.

        Parameters
        ----------
        run_id : str

        limit : typing.Optional[int]
            Maximum number of spans to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Dict[str, typing.Any]]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/trace",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Dict[str, typing.Any]],
                    parse_obj_as(
                        type_=typing.List[typing.Dict[str, typing.Any]],
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

    async def retrieve_stream_for_run(
        self,
        run_id: str,
        *,
        starting_after: typing.Optional[int] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        poll_interval: typing.Optional[float] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        run_id : str

        starting_after : typing.Optional[int]
            Sequence id to use as a cursor for pagination. Response will start streaming after this chunk sequence id

        include_pings : typing.Optional[bool]
            Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.

        poll_interval : typing.Optional[float]
            Seconds to wait between polls when no new data.

        batch_size : typing.Optional[int]
            Number of entries to read per batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/runs/{encode_path_param(run_id)}/stream",
            method="POST",
            json={
                "starting_after": starting_after,
                "include_pings": include_pings,
                "poll_interval": poll_interval,
                "batch_size": batch_size,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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
