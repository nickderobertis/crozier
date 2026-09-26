

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
from ..types.run import Run
from ..types.run_create_config import RunCreateConfig
from ..types.run_create_if_not_exists import RunCreateIfNotExists
from ..types.run_create_input import RunCreateInput
from ..types.run_create_on_completion import RunCreateOnCompletion
from ..types.run_create_on_disconnect import RunCreateOnDisconnect
from ..types.run_status import RunStatus
from ..types.run_stream_stream_mode import RunStreamStreamMode
from ..types.run_wait_response import RunWaitResponse
from .types.cancel_run_request_action import CancelRunRequestAction
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBackgroundRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_runs(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[RunStatus] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Run]]:
        """
        List runs for a thread, agent or status

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Run metadata to filter on.

        status : typing.Optional[RunStatus]
            Run status to filter on.

        thread_id : typing.Optional[str]
            The ID of the thread to filter on.

        agent_id : typing.Optional[str]
            The ID of the agent to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Run]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs/search",
            method="POST",
            json={
                "metadata": metadata,
                "status": status,
                "thread_id": thread_id,
                "agent_id": agent_id,
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
                    typing.List[Run],
                    parse_obj_as(
                        type_=typing.List[Run],
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

    def get_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Run]:
        """
        Get a run by ID.

        Parameters
        ----------
        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Run]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}",
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

    def delete_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Delete a run by ID.

        Parameters
        ----------
        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}",
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

    def wait_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RunWaitResponse]:
        """
        Wait for a run to finish, return the final output. If the run already finished, returns its final output immediately.

        Parameters
        ----------
        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunWaitResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}/wait",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunWaitResponse,
                    parse_obj_as(
                        type_=RunWaitResponse,
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

    def stream_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Join the output stream of an existing run. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. Only output produced after this endpoint is called will be streamed.

        Parameters
        ----------
        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}/stream",
            method="GET",
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

    def cancel_run(
        self,
        run_id: str,
        *,
        wait: typing.Optional[bool] = None,
        action: typing.Optional[CancelRunRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        run_id : str
            The ID of the run.

        wait : typing.Optional[bool]

        action : typing.Optional[CancelRunRequestAction]
            Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}/cancel",
            method="POST",
            params={
                "wait": wait,
                "action": action,
            },
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

    def create_run(
        self,
        *,
        stream_mode: typing.Optional[RunStreamStreamMode] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        input: typing.Optional[RunCreateInput] = OMIT,
        messages: typing.Optional[typing.Sequence[Message]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateConfig] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        on_completion: typing.Optional[RunCreateOnCompletion] = OMIT,
        on_disconnect: typing.Optional[RunCreateOnDisconnect] = OMIT,
        if_not_exists: typing.Optional[RunCreateIfNotExists] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Run]:
        """
        Create a run in a new thread, return the run ID immediately. Don't wait for the final run output.

        Parameters
        ----------
        stream_mode : typing.Optional[RunStreamStreamMode]
            The stream mode(s) to use.

        thread_id : typing.Optional[str]
            The ID of the thread to run. If not provided, creates a stateless run. 'thread_id' is ignored unless Threads stage is implemented.

        agent_id : typing.Optional[str]
            The agent ID to run. If not provided will use the default agent for this service. 'agent_id' is ignored unless Agents stage is implemented.

        input : typing.Optional[RunCreateInput]
            The input to the agent.

        messages : typing.Optional[typing.Sequence[Message]]
            The messages to pass an input to the agent.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateConfig]
            The configuration for the agent.

        webhook : typing.Optional[str]
            Webhook to call after run finishes.

        on_completion : typing.Optional[RunCreateOnCompletion]
            Whether to delete or keep the thread when run completes. Must be one of 'delete' or 'keep'. Defaults to 'delete' when thread_id not provided, otherwise 'keep'.

        on_disconnect : typing.Optional[RunCreateOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        if_not_exists : typing.Optional[RunCreateIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Run]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs",
            method="POST",
            json={
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunStreamStreamMode, direction="write"
                ),
                "thread_id": thread_id,
                "agent_id": agent_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateInput], direction="write"
                ),
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[Message], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateConfig, direction="write"
                ),
                "webhook": webhook,
                "on_completion": on_completion,
                "on_disconnect": on_disconnect,
                "if_not_exists": if_not_exists,
            },
            request_options=request_options,
            omit=OMIT,
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


class AsyncRawBackgroundRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_runs(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[RunStatus] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Run]]:
        """
        List runs for a thread, agent or status

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Run metadata to filter on.

        status : typing.Optional[RunStatus]
            Run status to filter on.

        thread_id : typing.Optional[str]
            The ID of the thread to filter on.

        agent_id : typing.Optional[str]
            The ID of the agent to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Run]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs/search",
            method="POST",
            json={
                "metadata": metadata,
                "status": status,
                "thread_id": thread_id,
                "agent_id": agent_id,
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
                    typing.List[Run],
                    parse_obj_as(
                        type_=typing.List[Run],
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

    async def get_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Run]:
        """
        Get a run by ID.

        Parameters
        ----------
        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Run]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}",
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

    async def delete_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a run by ID.

        Parameters
        ----------
        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}",
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

    async def wait_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RunWaitResponse]:
        """
        Wait for a run to finish, return the final output. If the run already finished, returns its final output immediately.

        Parameters
        ----------
        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunWaitResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}/wait",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunWaitResponse,
                    parse_obj_as(
                        type_=RunWaitResponse,
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

    async def stream_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Join the output stream of an existing run. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. Only output produced after this endpoint is called will be streamed.

        Parameters
        ----------
        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}/stream",
            method="GET",
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

    async def cancel_run(
        self,
        run_id: str,
        *,
        wait: typing.Optional[bool] = None,
        action: typing.Optional[CancelRunRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        run_id : str
            The ID of the run.

        wait : typing.Optional[bool]

        action : typing.Optional[CancelRunRequestAction]
            Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"runs/{encode_path_param(run_id)}/cancel",
            method="POST",
            params={
                "wait": wait,
                "action": action,
            },
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

    async def create_run(
        self,
        *,
        stream_mode: typing.Optional[RunStreamStreamMode] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        input: typing.Optional[RunCreateInput] = OMIT,
        messages: typing.Optional[typing.Sequence[Message]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateConfig] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        on_completion: typing.Optional[RunCreateOnCompletion] = OMIT,
        on_disconnect: typing.Optional[RunCreateOnDisconnect] = OMIT,
        if_not_exists: typing.Optional[RunCreateIfNotExists] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Run]:
        """
        Create a run in a new thread, return the run ID immediately. Don't wait for the final run output.

        Parameters
        ----------
        stream_mode : typing.Optional[RunStreamStreamMode]
            The stream mode(s) to use.

        thread_id : typing.Optional[str]
            The ID of the thread to run. If not provided, creates a stateless run. 'thread_id' is ignored unless Threads stage is implemented.

        agent_id : typing.Optional[str]
            The agent ID to run. If not provided will use the default agent for this service. 'agent_id' is ignored unless Agents stage is implemented.

        input : typing.Optional[RunCreateInput]
            The input to the agent.

        messages : typing.Optional[typing.Sequence[Message]]
            The messages to pass an input to the agent.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateConfig]
            The configuration for the agent.

        webhook : typing.Optional[str]
            Webhook to call after run finishes.

        on_completion : typing.Optional[RunCreateOnCompletion]
            Whether to delete or keep the thread when run completes. Must be one of 'delete' or 'keep'. Defaults to 'delete' when thread_id not provided, otherwise 'keep'.

        on_disconnect : typing.Optional[RunCreateOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        if_not_exists : typing.Optional[RunCreateIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Run]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs",
            method="POST",
            json={
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunStreamStreamMode, direction="write"
                ),
                "thread_id": thread_id,
                "agent_id": agent_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateInput], direction="write"
                ),
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[Message], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateConfig, direction="write"
                ),
                "webhook": webhook,
                "on_completion": on_completion,
                "on_disconnect": on_disconnect,
                "if_not_exists": if_not_exists,
            },
            request_options=request_options,
            omit=OMIT,
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
