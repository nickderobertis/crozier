

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
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.message import Message
from ..types.thread import Thread
from ..types.thread_checkpoint import ThreadCheckpoint
from ..types.thread_state import ThreadState
from ..types.thread_status import ThreadStatus
from .types.thread_create_if_exists import ThreadCreateIfExists
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
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadStatus] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Thread]]:
        """
        Search for threads.

        This endpoint also functions as the endpoint to list all threads.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadStatus]
            Thread status to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

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
                "metadata": metadata,
                "values": values,
                "status": status,
                "limit": limit,
                "offset": offset,
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
            if _response.status_code == 404:
                raise NotFoundError(
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

    def copy_thread(
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
            if _response.status_code == 404:
                raise NotFoundError(
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
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Thread]:
        """
        Get a thread by ID.

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
            f"threads/{encode_path_param(thread_id)}",
            method="GET",
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

    def delete_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def patch_thread(
        self,
        thread_id: str,
        *,
        checkpoint: typing.Optional[ThreadCheckpoint] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        messages: typing.Optional[typing.Sequence[Message]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Thread]:
        """
        Update a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint : typing.Optional[ThreadCheckpoint]
            The identifier of the checkpoint to branch from. Ignored for metadata-only patches. If not provided, defaults to the latest checkpoint.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing thread metadata.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            Values to merge with existing thread values.

        messages : typing.Optional[typing.Sequence[Message]]
            Messages to combine with current thread messages.

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
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=ThreadCheckpoint, direction="write"
                ),
                "metadata": metadata,
                "values": values,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[Message], direction="write"
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


class AsyncRawThreadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_thread(
        self,
        *,
        thread_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        if_exists: typing.Optional[ThreadCreateIfExists] = OMIT,
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
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadStatus] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Thread]]:
        """
        Search for threads.

        This endpoint also functions as the endpoint to list all threads.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadStatus]
            Thread status to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

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
                "metadata": metadata,
                "values": values,
                "status": status,
                "limit": limit,
                "offset": offset,
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
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def copy_thread(
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
            if _response.status_code == 404:
                raise NotFoundError(
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
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Thread]:
        """
        Get a thread by ID.

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
            f"threads/{encode_path_param(thread_id)}",
            method="GET",
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

    async def delete_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def patch_thread(
        self,
        thread_id: str,
        *,
        checkpoint: typing.Optional[ThreadCheckpoint] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        messages: typing.Optional[typing.Sequence[Message]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Thread]:
        """
        Update a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint : typing.Optional[ThreadCheckpoint]
            The identifier of the checkpoint to branch from. Ignored for metadata-only patches. If not provided, defaults to the latest checkpoint.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing thread metadata.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            Values to merge with existing thread values.

        messages : typing.Optional[typing.Sequence[Message]]
            Messages to combine with current thread messages.

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
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=ThreadCheckpoint, direction="write"
                ),
                "metadata": metadata,
                "values": values,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[Message], direction="write"
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
