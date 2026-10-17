

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.http_sse._api import EventSource
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as, parse_sse_obj
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.checkpoint_config import CheckpointConfig
from ..types.error_response import ErrorResponse
from ..types.join_thread_stream_threads_thread_id_stream_get_request_stream_modes import (
    JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes,
)
from ..types.thread import Thread
from ..types.thread_prune_response import ThreadPruneResponse
from ..types.thread_state import ThreadState
from ..types.thread_state_update_response import ThreadStateUpdateResponse
from ..types.thread_storage import ThreadStorage
from .types.thread_count_request_status import ThreadCountRequestStatus
from .types.thread_create_if_exists import ThreadCreateIfExists
from .types.thread_create_supersteps_item import ThreadCreateSuperstepsItem
from .types.thread_create_ttl import ThreadCreateTtl
from .types.thread_patch_ttl import ThreadPatchTtl
from .types.thread_prune_request_strategy import ThreadPruneRequestStrategy
from .types.thread_search_request_select_item import ThreadSearchRequestSelectItem
from .types.thread_search_request_sort_by import ThreadSearchRequestSortBy
from .types.thread_search_request_sort_order import ThreadSearchRequestSortOrder
from .types.thread_search_request_status import ThreadSearchRequestStatus
from .types.thread_state_update_values import ThreadStateUpdateValues
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawThreadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_thread(
        self,
        *,
        thread_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        if_exists: typing.Optional[ThreadCreateIfExists] = OMIT,
        ttl: typing.Optional[ThreadCreateTtl] = OMIT,
        supersteps: typing.Optional[typing.Sequence[ThreadCreateSuperstepsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Thread]:
        """
        Create a thread.

        Parameters
        ----------
        thread_id : typing.Optional[str]
            The ID of the thread. If not provided, a random UUID will be generated.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to add to thread.

        if_exists : typing.Optional[ThreadCreateIfExists]
            How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing thread).

        ttl : typing.Optional[ThreadCreateTtl]
            The time-to-live for the thread.

        supersteps : typing.Optional[typing.Sequence[ThreadCreateSuperstepsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Thread]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "threads",
            method="POST",
            json={
                "thread_id": thread_id,
                "metadata": metadata,
                "if_exists": if_exists,
                "ttl": convert_and_respect_annotation_metadata(
                    object_=ttl, annotation=ThreadCreateTtl, direction="write"
                ),
                "supersteps": convert_and_respect_annotation_metadata(
                    object_=supersteps, annotation=typing.Sequence[ThreadCreateSuperstepsItem], direction="write"
                ),
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
                    Thread,
                    parse_obj_as(
                        type_=Thread,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def search_threads(
        self,
        *,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadSearchRequestStatus] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[ThreadSearchRequestSortBy] = OMIT,
        sort_order: typing.Optional[ThreadSearchRequestSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[ThreadSearchRequestSelectItem]] = OMIT,
        extract: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Thread]]:
        """
        Search for threads.

        This endpoint also functions as the endpoint to list all threads.

        Parameters
        ----------
        ids : typing.Optional[typing.Sequence[str]]
            List of thread IDs to include. Others are excluded.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadSearchRequestStatus]
            Thread status to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

        sort_by : typing.Optional[ThreadSearchRequestSortBy]
            Sort by field.

        sort_order : typing.Optional[ThreadSearchRequestSortOrder]
            Sort order.

        select : typing.Optional[typing.Sequence[ThreadSearchRequestSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        extract : typing.Optional[typing.Dict[str, str]]
            Map of alias to JSONB path for extracting specific values. Paths must start with values, metadata, config, or interrupts. Example: {"last_msg": "values.messages[-1]"}.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Thread]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "threads/search",
            method="POST",
            json={
                "ids": ids,
                "metadata": metadata,
                "values": values,
                "status": status,
                "limit": limit,
                "offset": offset,
                "sort_by": sort_by,
                "sort_order": sort_order,
                "select": select,
                "extract": extract,
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
                    typing.List[Thread],
                    parse_obj_as(
                        type_=typing.List[Thread],
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

    def count_threads(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadCountRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Get the count of threads matching the specified criteria.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadCountRequestStatus]
            Thread status to filter on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "threads/count",
            method="POST",
            json={
                "metadata": metadata,
                "values": values,
                "status": status,
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

    def prune_threads(
        self,
        *,
        thread_ids: typing.Sequence[str],
        strategy: typing.Optional[ThreadPruneRequestStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadPruneResponse]:
        """
        Prune threads by ID. The 'delete' strategy removes threads entirely. The 'keep_latest' strategy prunes old checkpoints but keeps threads and their latest state.

        Parameters
        ----------
        thread_ids : typing.Sequence[str]
            List of thread IDs to prune.

        strategy : typing.Optional[ThreadPruneRequestStrategy]
            The prune strategy. 'delete' removes threads entirely. 'keep_latest' prunes old checkpoints but keeps threads and their latest state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThreadPruneResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "threads/prune",
            method="POST",
            json={
                "thread_ids": thread_ids,
                "strategy": strategy,
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
                    ThreadPruneResponse,
                    parse_obj_as(
                        type_=ThreadPruneResponse,
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

    def get_thread_storage(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ThreadStorage]:
        """
        Bytes the thread's checkpoints occupy in the built-in checkpointer, as stored: checkpoints, channel values (per channel) and pending writes. Returns 501 when a custom checkpointer is configured.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThreadStorage]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/storage",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadStorage,
                    parse_obj_as(
                        type_=ThreadStorage,
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

    def get_latest_thread_state(
        self,
        thread_id: str,
        *,
        subgraphs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadState]:
        """
        Get state for a thread.

        The latest state of the thread (i.e. latest checkpoint) is returned.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        subgraphs : typing.Optional[bool]
            Whether to include subgraphs in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThreadState]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/state",
            method="GET",
            params={
                "subgraphs": subgraphs,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadState,
                    parse_obj_as(
                        type_=ThreadState,
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

    def update_thread_state(
        self,
        thread_id: str,
        *,
        values: typing.Optional[ThreadStateUpdateValues] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        as_node: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadStateUpdateResponse]:
        """
        Add state to a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        values : typing.Optional[ThreadStateUpdateValues]
            The values to update the state with.

        checkpoint : typing.Optional[CheckpointConfig]
            The checkpoint to update the state of.

        as_node : typing.Optional[str]
            Update the state as if this node had just executed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThreadStateUpdateResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/state",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values, annotation=typing.Optional[ThreadStateUpdateValues], direction="write"
                ),
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
                "as_node": as_node,
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
                    ThreadStateUpdateResponse,
                    parse_obj_as(
                        type_=ThreadStateUpdateResponse,
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

    def get_thread_state_at_checkpoint(
        self,
        thread_id: str,
        checkpoint_id: str,
        *,
        subgraphs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadState]:
        """
        Get state for a thread at a specific checkpoint.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint_id : str
            The ID of the checkpoint.

        subgraphs : typing.Optional[bool]
            Whether to include subgraphs in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThreadState]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/state/{encode_path_param(checkpoint_id)}",
            method="GET",
            params={
                "subgraphs": subgraphs,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadState,
                    parse_obj_as(
                        type_=ThreadState,
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

    def post_thread_state_at_checkpoint_threads_thread_id_state_checkpoint_id_get(
        self,
        thread_id: str,
        *,
        checkpoint: CheckpointConfig,
        subgraphs: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadState]:
        """
        Get state for a thread at a specific checkpoint.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint : CheckpointConfig
            The checkpoint to get the state for.

        subgraphs : typing.Optional[bool]
            Include subgraph states.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThreadState]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/state/checkpoint",
            method="POST",
            json={
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
                "subgraphs": subgraphs,
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
                    ThreadState,
                    parse_obj_as(
                        type_=ThreadState,
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

    def get_thread_history(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ThreadState]]:
        """
        Get all past states for a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        limit : typing.Optional[int]

        before : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ThreadState]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/history",
            method="GET",
            params={
                "limit": limit,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ThreadState],
                    parse_obj_as(
                        type_=typing.List[ThreadState],
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

    def get_thread_history_post(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = OMIT,
        before: typing.Optional[CheckpointConfig] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ThreadState]]:
        """
        Get all past states for a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        limit : typing.Optional[int]
            The maximum number of states to return.

        before : typing.Optional[CheckpointConfig]
            Return states before this checkpoint.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Filter states by metadata key-value pairs.

        checkpoint : typing.Optional[CheckpointConfig]
            Return states for this subgraph.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ThreadState]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/history",
            method="POST",
            json={
                "limit": limit,
                "before": convert_and_respect_annotation_metadata(
                    object_=before, annotation=CheckpointConfig, direction="write"
                ),
                "metadata": metadata,
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
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
                    typing.List[ThreadState],
                    parse_obj_as(
                        type_=typing.List[ThreadState],
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

    def copy_thread_post(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Thread]:
        """
        Create a new thread with a copy of the state and checkpoints from an existing thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Thread]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/copy",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Thread,
                    parse_obj_as(
                        type_=Thread,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_thread(
        self,
        thread_id: str,
        *,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Thread]:
        """
        Get a thread by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        include : typing.Optional[str]
            Comma-separated list of additional fields to include. Supported values: ttl

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Thread]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="GET",
            params={
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Thread,
                    parse_obj_as(
                        type_=Thread,
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

    def delete_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a thread by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
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

    def patch_thread(
        self,
        thread_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ttl: typing.Optional[ThreadPatchTtl] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Thread]:
        """
        Update a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing thread metadata.

        ttl : typing.Optional[ThreadPatchTtl]
            The time-to-live for the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Thread]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="PATCH",
            json={
                "metadata": metadata,
                "ttl": convert_and_respect_annotation_metadata(
                    object_=ttl, annotation=ThreadPatchTtl, direction="write"
                ),
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
                    Thread,
                    parse_obj_as(
                        type_=Thread,
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

    @contextlib.contextmanager
    def join_thread_stream(
        self,
        thread_id: str,
        *,
        stream_modes: typing.Optional[JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes] = None,
        last_event_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[str]]]:
        """
        This endpoint streams output in real-time from a thread. The stream will include the output of each run executed sequentially on the thread and will remain open indefinitely. It is the responsibility of the calling client to close the connection.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        stream_modes : typing.Optional[JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes]

        last_event_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[str]]]
            Success
        """
        with self._client_wrapper.httpx_client.stream(
            f"threads/{encode_path_param(thread_id)}/stream",
            method="GET",
            params={
                "stream_modes": convert_and_respect_annotation_metadata(
                    object_=stream_modes,
                    annotation=JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes,
                    direction="write",
                ),
            },
            headers={
                "Last-Event-ID": str(last_event_id) if last_event_id is not None else None,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[str]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        str,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=str,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawThreadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_thread(
        self,
        *,
        thread_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        if_exists: typing.Optional[ThreadCreateIfExists] = OMIT,
        ttl: typing.Optional[ThreadCreateTtl] = OMIT,
        supersteps: typing.Optional[typing.Sequence[ThreadCreateSuperstepsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Thread]:
        """
        Create a thread.

        Parameters
        ----------
        thread_id : typing.Optional[str]
            The ID of the thread. If not provided, a random UUID will be generated.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to add to thread.

        if_exists : typing.Optional[ThreadCreateIfExists]
            How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing thread).

        ttl : typing.Optional[ThreadCreateTtl]
            The time-to-live for the thread.

        supersteps : typing.Optional[typing.Sequence[ThreadCreateSuperstepsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Thread]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "threads",
            method="POST",
            json={
                "thread_id": thread_id,
                "metadata": metadata,
                "if_exists": if_exists,
                "ttl": convert_and_respect_annotation_metadata(
                    object_=ttl, annotation=ThreadCreateTtl, direction="write"
                ),
                "supersteps": convert_and_respect_annotation_metadata(
                    object_=supersteps, annotation=typing.Sequence[ThreadCreateSuperstepsItem], direction="write"
                ),
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
                    Thread,
                    parse_obj_as(
                        type_=Thread,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def search_threads(
        self,
        *,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadSearchRequestStatus] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[ThreadSearchRequestSortBy] = OMIT,
        sort_order: typing.Optional[ThreadSearchRequestSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[ThreadSearchRequestSelectItem]] = OMIT,
        extract: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Thread]]:
        """
        Search for threads.

        This endpoint also functions as the endpoint to list all threads.

        Parameters
        ----------
        ids : typing.Optional[typing.Sequence[str]]
            List of thread IDs to include. Others are excluded.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadSearchRequestStatus]
            Thread status to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

        sort_by : typing.Optional[ThreadSearchRequestSortBy]
            Sort by field.

        sort_order : typing.Optional[ThreadSearchRequestSortOrder]
            Sort order.

        select : typing.Optional[typing.Sequence[ThreadSearchRequestSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        extract : typing.Optional[typing.Dict[str, str]]
            Map of alias to JSONB path for extracting specific values. Paths must start with values, metadata, config, or interrupts. Example: {"last_msg": "values.messages[-1]"}.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Thread]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "threads/search",
            method="POST",
            json={
                "ids": ids,
                "metadata": metadata,
                "values": values,
                "status": status,
                "limit": limit,
                "offset": offset,
                "sort_by": sort_by,
                "sort_order": sort_order,
                "select": select,
                "extract": extract,
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
                    typing.List[Thread],
                    parse_obj_as(
                        type_=typing.List[Thread],
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

    async def count_threads(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadCountRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Get the count of threads matching the specified criteria.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadCountRequestStatus]
            Thread status to filter on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "threads/count",
            method="POST",
            json={
                "metadata": metadata,
                "values": values,
                "status": status,
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

    async def prune_threads(
        self,
        *,
        thread_ids: typing.Sequence[str],
        strategy: typing.Optional[ThreadPruneRequestStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadPruneResponse]:
        """
        Prune threads by ID. The 'delete' strategy removes threads entirely. The 'keep_latest' strategy prunes old checkpoints but keeps threads and their latest state.

        Parameters
        ----------
        thread_ids : typing.Sequence[str]
            List of thread IDs to prune.

        strategy : typing.Optional[ThreadPruneRequestStrategy]
            The prune strategy. 'delete' removes threads entirely. 'keep_latest' prunes old checkpoints but keeps threads and their latest state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThreadPruneResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "threads/prune",
            method="POST",
            json={
                "thread_ids": thread_ids,
                "strategy": strategy,
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
                    ThreadPruneResponse,
                    parse_obj_as(
                        type_=ThreadPruneResponse,
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

    async def get_thread_storage(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ThreadStorage]:
        """
        Bytes the thread's checkpoints occupy in the built-in checkpointer, as stored: checkpoints, channel values (per channel) and pending writes. Returns 501 when a custom checkpointer is configured.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThreadStorage]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/storage",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadStorage,
                    parse_obj_as(
                        type_=ThreadStorage,
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

    async def get_latest_thread_state(
        self,
        thread_id: str,
        *,
        subgraphs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadState]:
        """
        Get state for a thread.

        The latest state of the thread (i.e. latest checkpoint) is returned.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        subgraphs : typing.Optional[bool]
            Whether to include subgraphs in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThreadState]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/state",
            method="GET",
            params={
                "subgraphs": subgraphs,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadState,
                    parse_obj_as(
                        type_=ThreadState,
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

    async def update_thread_state(
        self,
        thread_id: str,
        *,
        values: typing.Optional[ThreadStateUpdateValues] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        as_node: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadStateUpdateResponse]:
        """
        Add state to a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        values : typing.Optional[ThreadStateUpdateValues]
            The values to update the state with.

        checkpoint : typing.Optional[CheckpointConfig]
            The checkpoint to update the state of.

        as_node : typing.Optional[str]
            Update the state as if this node had just executed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThreadStateUpdateResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/state",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values, annotation=typing.Optional[ThreadStateUpdateValues], direction="write"
                ),
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
                "as_node": as_node,
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
                    ThreadStateUpdateResponse,
                    parse_obj_as(
                        type_=ThreadStateUpdateResponse,
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

    async def get_thread_state_at_checkpoint(
        self,
        thread_id: str,
        checkpoint_id: str,
        *,
        subgraphs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadState]:
        """
        Get state for a thread at a specific checkpoint.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint_id : str
            The ID of the checkpoint.

        subgraphs : typing.Optional[bool]
            Whether to include subgraphs in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThreadState]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/state/{encode_path_param(checkpoint_id)}",
            method="GET",
            params={
                "subgraphs": subgraphs,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadState,
                    parse_obj_as(
                        type_=ThreadState,
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

    async def post_thread_state_at_checkpoint_threads_thread_id_state_checkpoint_id_get(
        self,
        thread_id: str,
        *,
        checkpoint: CheckpointConfig,
        subgraphs: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadState]:
        """
        Get state for a thread at a specific checkpoint.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint : CheckpointConfig
            The checkpoint to get the state for.

        subgraphs : typing.Optional[bool]
            Include subgraph states.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThreadState]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/state/checkpoint",
            method="POST",
            json={
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
                "subgraphs": subgraphs,
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
                    ThreadState,
                    parse_obj_as(
                        type_=ThreadState,
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

    async def get_thread_history(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ThreadState]]:
        """
        Get all past states for a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        limit : typing.Optional[int]

        before : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ThreadState]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/history",
            method="GET",
            params={
                "limit": limit,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ThreadState],
                    parse_obj_as(
                        type_=typing.List[ThreadState],
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

    async def get_thread_history_post(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = OMIT,
        before: typing.Optional[CheckpointConfig] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ThreadState]]:
        """
        Get all past states for a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        limit : typing.Optional[int]
            The maximum number of states to return.

        before : typing.Optional[CheckpointConfig]
            Return states before this checkpoint.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Filter states by metadata key-value pairs.

        checkpoint : typing.Optional[CheckpointConfig]
            Return states for this subgraph.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ThreadState]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/history",
            method="POST",
            json={
                "limit": limit,
                "before": convert_and_respect_annotation_metadata(
                    object_=before, annotation=CheckpointConfig, direction="write"
                ),
                "metadata": metadata,
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
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
                    typing.List[ThreadState],
                    parse_obj_as(
                        type_=typing.List[ThreadState],
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

    async def copy_thread_post(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Thread]:
        """
        Create a new thread with a copy of the state and checkpoints from an existing thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Thread]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/copy",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Thread,
                    parse_obj_as(
                        type_=Thread,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_thread(
        self,
        thread_id: str,
        *,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Thread]:
        """
        Get a thread by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        include : typing.Optional[str]
            Comma-separated list of additional fields to include. Supported values: ttl

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Thread]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="GET",
            params={
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Thread,
                    parse_obj_as(
                        type_=Thread,
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

    async def delete_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a thread by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
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

    async def patch_thread(
        self,
        thread_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ttl: typing.Optional[ThreadPatchTtl] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Thread]:
        """
        Update a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing thread metadata.

        ttl : typing.Optional[ThreadPatchTtl]
            The time-to-live for the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Thread]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="PATCH",
            json={
                "metadata": metadata,
                "ttl": convert_and_respect_annotation_metadata(
                    object_=ttl, annotation=ThreadPatchTtl, direction="write"
                ),
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
                    Thread,
                    parse_obj_as(
                        type_=Thread,
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

    @contextlib.asynccontextmanager
    async def join_thread_stream(
        self,
        thread_id: str,
        *,
        stream_modes: typing.Optional[JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes] = None,
        last_event_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]:
        """
        This endpoint streams output in real-time from a thread. The stream will include the output of each run executed sequentially on the thread and will remain open indefinitely. It is the responsibility of the calling client to close the connection.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        stream_modes : typing.Optional[JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes]

        last_event_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]
            Success
        """
        async with self._client_wrapper.httpx_client.stream(
            f"threads/{encode_path_param(thread_id)}/stream",
            method="GET",
            params={
                "stream_modes": convert_and_respect_annotation_metadata(
                    object_=stream_modes,
                    annotation=JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes,
                    direction="write",
                ),
            },
            headers={
                "Last-Event-ID": str(last_event_id) if last_event_id is not None else None,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[str]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        str,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=str,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
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
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
