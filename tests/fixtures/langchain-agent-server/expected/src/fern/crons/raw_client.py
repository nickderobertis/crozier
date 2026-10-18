

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.cron import Cron
from ..types.error_response import ErrorResponse
from .types.cron_create_config import CronCreateConfig
from .types.cron_create_durability import CronCreateDurability
from .types.cron_create_input import CronCreateInput
from .types.cron_create_interrupt_after import CronCreateInterruptAfter
from .types.cron_create_interrupt_before import CronCreateInterruptBefore
from .types.cron_create_on_run_completed import CronCreateOnRunCompleted
from .types.cron_create_stream_mode import CronCreateStreamMode
from .types.cron_patch_config import CronPatchConfig
from .types.cron_patch_durability import CronPatchDurability
from .types.cron_patch_input import CronPatchInput
from .types.cron_patch_interrupt_after import CronPatchInterruptAfter
from .types.cron_patch_interrupt_before import CronPatchInterruptBefore
from .types.cron_patch_on_run_completed import CronPatchOnRunCompleted
from .types.cron_patch_stream_mode import CronPatchStreamMode
from .types.cron_search_select_item import CronSearchSelectItem
from .types.cron_search_sort_by import CronSearchSortBy
from .types.cron_search_sort_order import CronSearchSortOrder
from .types.thread_cron_create_config import ThreadCronCreateConfig
from .types.thread_cron_create_durability import ThreadCronCreateDurability
from .types.thread_cron_create_input import ThreadCronCreateInput
from .types.thread_cron_create_interrupt_after import ThreadCronCreateInterruptAfter
from .types.thread_cron_create_interrupt_before import ThreadCronCreateInterruptBefore
from .types.thread_cron_create_multitask_strategy import ThreadCronCreateMultitaskStrategy
from .types.thread_cron_create_stream_mode import ThreadCronCreateStreamMode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCronsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_thread_cron(
        self,
        thread_id: str,
        *,
        schedule: str,
        assistant_id: str,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[ThreadCronCreateInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[ThreadCronCreateConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[ThreadCronCreateInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[ThreadCronCreateInterruptAfter] = OMIT,
        multitask_strategy: typing.Optional[ThreadCronCreateMultitaskStrategy] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[ThreadCronCreateStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[ThreadCronCreateDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Cron]:
        """
        Create a cron to schedule runs on a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        schedule : str
            The cron schedule to execute this job on.

        assistant_id : str

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron.

        input : typing.Optional[ThreadCronCreateInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the cron job runs.

        config : typing.Optional[ThreadCronCreateConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[ThreadCronCreateInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[ThreadCronCreateInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        multitask_strategy : typing.Optional[ThreadCronCreateMultitaskStrategy]
            Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

        enabled : typing.Optional[bool]
            Whether the cron job should be enabled. Disabled crons are not executed.

        stream_mode : typing.Optional[ThreadCronCreateStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[ThreadCronCreateDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Cron]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/crons",
            method="POST",
            json={
                "schedule": schedule,
                "timezone": timezone,
                "end_time": end_time,
                "assistant_id": assistant_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=ThreadCronCreateInput, direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=ThreadCronCreateConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=ThreadCronCreateInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=ThreadCronCreateInterruptAfter, direction="write"
                ),
                "multitask_strategy": multitask_strategy,
                "enabled": enabled,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=ThreadCronCreateStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "durability": durability,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cron,
                    parse_obj_as(
                        type_=Cron,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def create_cron(
        self,
        *,
        schedule: str,
        assistant_id: str,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[CronCreateInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[CronCreateConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[CronCreateInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[CronCreateInterruptAfter] = OMIT,
        on_run_completed: typing.Optional[CronCreateOnRunCompleted] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[CronCreateStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[CronCreateDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Cron]:
        """
        Create a cron to schedule runs on new threads.

        Parameters
        ----------
        schedule : str
            The cron schedule to execute this job on.

        assistant_id : str

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron.

        input : typing.Optional[CronCreateInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the cron job runs.

        config : typing.Optional[CronCreateConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[CronCreateInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[CronCreateInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        on_run_completed : typing.Optional[CronCreateOnRunCompleted]
            What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.

        enabled : typing.Optional[bool]
            Whether the cron job should be enabled. Disabled crons are not executed.

        stream_mode : typing.Optional[CronCreateStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[CronCreateDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Cron]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs/crons",
            method="POST",
            json={
                "schedule": schedule,
                "timezone": timezone,
                "end_time": end_time,
                "assistant_id": assistant_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=CronCreateInput, direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=CronCreateConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=CronCreateInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=CronCreateInterruptAfter, direction="write"
                ),
                "on_run_completed": on_run_completed,
                "enabled": enabled,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=CronCreateStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "durability": durability,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cron,
                    parse_obj_as(
                        type_=Cron,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def search_crons_runs_crons_post(
        self,
        *,
        assistant_id: typing.Optional[str] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[CronSearchSortBy] = OMIT,
        sort_order: typing.Optional[CronSearchSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[CronSearchSelectItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Cron]]:
        """
        Search all active crons

        Parameters
        ----------
        assistant_id : typing.Optional[str]
            The assistant ID or graph name to filter by using exact match.

        thread_id : typing.Optional[str]
            The thread ID to search for.

        enabled : typing.Optional[bool]
            Filter by enabled status. If not provided, returns both enabled and disabled crons.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        limit : typing.Optional[int]
            The maximum number of results to return.

        offset : typing.Optional[int]
            The number of results to skip.

        sort_by : typing.Optional[CronSearchSortBy]
            The field to sort by.

        sort_order : typing.Optional[CronSearchSortOrder]
            The order to sort by.

        select : typing.Optional[typing.Sequence[CronSearchSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Cron]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs/crons/search",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "thread_id": thread_id,
                "enabled": enabled,
                "metadata": metadata,
                "limit": limit,
                "offset": offset,
                "sort_by": sort_by,
                "sort_order": sort_order,
                "select": select,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Cron],
                    parse_obj_as(
                        type_=typing.List[Cron],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def count_crons(
        self,
        *,
        assistant_id: typing.Optional[str] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Get the count of crons matching the specified criteria.

        Parameters
        ----------
        assistant_id : typing.Optional[str]
            The assistant ID or graph name to search for.

        thread_id : typing.Optional[str]
            The thread ID to search for.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs/crons/count",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "thread_id": thread_id,
                "metadata": metadata,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_cron(self, cron_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Cron]:
        """
        Get a cron by ID.

        Parameters
        ----------
        cron_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Cron]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"runs/crons/{encode_path_param(cron_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cron,
                    parse_obj_as(
                        type_=Cron,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def delete_cron(
        self, cron_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a cron by ID.

        Parameters
        ----------
        cron_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"runs/crons/{encode_path_param(cron_id)}",
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def patch_cron(
        self,
        cron_id: str,
        *,
        schedule: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[CronPatchInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[CronPatchConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[CronPatchInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[CronPatchInterruptAfter] = OMIT,
        on_run_completed: typing.Optional[CronPatchOnRunCompleted] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[CronPatchStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[CronPatchDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Cron]:
        """
        Update a cron job by ID.

        Parameters
        ----------
        cron_id : str

        schedule : typing.Optional[str]
            The cron schedule to execute this job on.

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron. Send null to clear a previously set end time; omit this field to leave the existing value unchanged.

        input : typing.Optional[CronPatchInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing cron job metadata.

        config : typing.Optional[CronPatchConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[CronPatchInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[CronPatchInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        on_run_completed : typing.Optional[CronPatchOnRunCompleted]
            What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.

        enabled : typing.Optional[bool]
            Enable or disable the cron job.

        stream_mode : typing.Optional[CronPatchStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[CronPatchDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Cron]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"runs/crons/{encode_path_param(cron_id)}",
            method="PATCH",
            json={
                "schedule": schedule,
                "timezone": timezone,
                "end_time": end_time,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=CronPatchInput, direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=CronPatchConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=CronPatchInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=CronPatchInterruptAfter, direction="write"
                ),
                "on_run_completed": on_run_completed,
                "enabled": enabled,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=CronPatchStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "durability": durability,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cron,
                    parse_obj_as(
                        type_=Cron,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawCronsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_thread_cron(
        self,
        thread_id: str,
        *,
        schedule: str,
        assistant_id: str,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[ThreadCronCreateInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[ThreadCronCreateConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[ThreadCronCreateInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[ThreadCronCreateInterruptAfter] = OMIT,
        multitask_strategy: typing.Optional[ThreadCronCreateMultitaskStrategy] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[ThreadCronCreateStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[ThreadCronCreateDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Cron]:
        """
        Create a cron to schedule runs on a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        schedule : str
            The cron schedule to execute this job on.

        assistant_id : str

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron.

        input : typing.Optional[ThreadCronCreateInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the cron job runs.

        config : typing.Optional[ThreadCronCreateConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[ThreadCronCreateInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[ThreadCronCreateInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        multitask_strategy : typing.Optional[ThreadCronCreateMultitaskStrategy]
            Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

        enabled : typing.Optional[bool]
            Whether the cron job should be enabled. Disabled crons are not executed.

        stream_mode : typing.Optional[ThreadCronCreateStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[ThreadCronCreateDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Cron]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/crons",
            method="POST",
            json={
                "schedule": schedule,
                "timezone": timezone,
                "end_time": end_time,
                "assistant_id": assistant_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=ThreadCronCreateInput, direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=ThreadCronCreateConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=ThreadCronCreateInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=ThreadCronCreateInterruptAfter, direction="write"
                ),
                "multitask_strategy": multitask_strategy,
                "enabled": enabled,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=ThreadCronCreateStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "durability": durability,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cron,
                    parse_obj_as(
                        type_=Cron,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def create_cron(
        self,
        *,
        schedule: str,
        assistant_id: str,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[CronCreateInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[CronCreateConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[CronCreateInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[CronCreateInterruptAfter] = OMIT,
        on_run_completed: typing.Optional[CronCreateOnRunCompleted] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[CronCreateStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[CronCreateDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Cron]:
        """
        Create a cron to schedule runs on new threads.

        Parameters
        ----------
        schedule : str
            The cron schedule to execute this job on.

        assistant_id : str

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron.

        input : typing.Optional[CronCreateInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the cron job runs.

        config : typing.Optional[CronCreateConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[CronCreateInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[CronCreateInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        on_run_completed : typing.Optional[CronCreateOnRunCompleted]
            What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.

        enabled : typing.Optional[bool]
            Whether the cron job should be enabled. Disabled crons are not executed.

        stream_mode : typing.Optional[CronCreateStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[CronCreateDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Cron]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs/crons",
            method="POST",
            json={
                "schedule": schedule,
                "timezone": timezone,
                "end_time": end_time,
                "assistant_id": assistant_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=CronCreateInput, direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=CronCreateConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=CronCreateInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=CronCreateInterruptAfter, direction="write"
                ),
                "on_run_completed": on_run_completed,
                "enabled": enabled,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=CronCreateStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "durability": durability,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cron,
                    parse_obj_as(
                        type_=Cron,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def search_crons_runs_crons_post(
        self,
        *,
        assistant_id: typing.Optional[str] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[CronSearchSortBy] = OMIT,
        sort_order: typing.Optional[CronSearchSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[CronSearchSelectItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Cron]]:
        """
        Search all active crons

        Parameters
        ----------
        assistant_id : typing.Optional[str]
            The assistant ID or graph name to filter by using exact match.

        thread_id : typing.Optional[str]
            The thread ID to search for.

        enabled : typing.Optional[bool]
            Filter by enabled status. If not provided, returns both enabled and disabled crons.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        limit : typing.Optional[int]
            The maximum number of results to return.

        offset : typing.Optional[int]
            The number of results to skip.

        sort_by : typing.Optional[CronSearchSortBy]
            The field to sort by.

        sort_order : typing.Optional[CronSearchSortOrder]
            The order to sort by.

        select : typing.Optional[typing.Sequence[CronSearchSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Cron]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs/crons/search",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "thread_id": thread_id,
                "enabled": enabled,
                "metadata": metadata,
                "limit": limit,
                "offset": offset,
                "sort_by": sort_by,
                "sort_order": sort_order,
                "select": select,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Cron],
                    parse_obj_as(
                        type_=typing.List[Cron],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def count_crons(
        self,
        *,
        assistant_id: typing.Optional[str] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Get the count of crons matching the specified criteria.

        Parameters
        ----------
        assistant_id : typing.Optional[str]
            The assistant ID or graph name to search for.

        thread_id : typing.Optional[str]
            The thread ID to search for.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs/crons/count",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "thread_id": thread_id,
                "metadata": metadata,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_cron(
        self, cron_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Cron]:
        """
        Get a cron by ID.

        Parameters
        ----------
        cron_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Cron]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"runs/crons/{encode_path_param(cron_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cron,
                    parse_obj_as(
                        type_=Cron,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def delete_cron(
        self, cron_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a cron by ID.

        Parameters
        ----------
        cron_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"runs/crons/{encode_path_param(cron_id)}",
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def patch_cron(
        self,
        cron_id: str,
        *,
        schedule: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[CronPatchInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[CronPatchConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[CronPatchInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[CronPatchInterruptAfter] = OMIT,
        on_run_completed: typing.Optional[CronPatchOnRunCompleted] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[CronPatchStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[CronPatchDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Cron]:
        """
        Update a cron job by ID.

        Parameters
        ----------
        cron_id : str

        schedule : typing.Optional[str]
            The cron schedule to execute this job on.

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron. Send null to clear a previously set end time; omit this field to leave the existing value unchanged.

        input : typing.Optional[CronPatchInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing cron job metadata.

        config : typing.Optional[CronPatchConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[CronPatchInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[CronPatchInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        on_run_completed : typing.Optional[CronPatchOnRunCompleted]
            What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.

        enabled : typing.Optional[bool]
            Enable or disable the cron job.

        stream_mode : typing.Optional[CronPatchStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[CronPatchDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Cron]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"runs/crons/{encode_path_param(cron_id)}",
            method="PATCH",
            json={
                "schedule": schedule,
                "timezone": timezone,
                "end_time": end_time,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=CronPatchInput, direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=CronPatchConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=CronPatchInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=CronPatchInterruptAfter, direction="write"
                ),
                "on_run_completed": on_run_completed,
                "enabled": enabled,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=CronPatchStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "durability": durability,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cron,
                    parse_obj_as(
                        type_=Cron,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
