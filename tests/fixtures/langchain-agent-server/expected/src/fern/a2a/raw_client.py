

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
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from .types.post_a2a_request_jsonrpc import PostA2ARequestJsonrpc
from .types.post_a2a_request_method import PostA2ARequestMethod
from .types.post_a2a_request_params import PostA2ARequestParams
from .types.post_a2a_response import PostA2AResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawA2AClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_a2a(
        self,
        assistant_id: str,
        *,
        accept: str,
        jsonrpc: PostA2ARequestJsonrpc,
        id: str,
        method: PostA2ARequestMethod,
        params: typing.Optional[PostA2ARequestParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostA2AResponse]:
        """
        Communicate with an assistant using the Agent-to-Agent (A2A) Protocol over JSON-RPC 2.0.
        This endpoint accepts a JSON-RPC envelope and dispatches based on `method`.

        **Supported Methods:**
        - `message/send`: Send a message and wait for the final Task result.
        - `message/stream`: Send a message and receive Server-Sent Events (SSE) JSON-RPC responses.
        - `tasks/get`: Fetch the current state of a Task by ID.
        - `tasks/cancel`: Request cancellation (currently not supported; returns an error).

        **LangGraph Mapping:**
        - `message.contextId` maps to LangGraph `thread_id`.

        **Notes:**
        - Only `text` and `data` parts are supported; `file` parts are not.
        - If `message.contextId` is omitted, a new context is created.
        - Text parts require the assistant input schema to include a `messages` field.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to communicate with

        accept : str
            For `message/stream`, must include `text/event-stream`. For all other methods, use `application/json`.

        jsonrpc : PostA2ARequestJsonrpc
            JSON-RPC version

        id : str
            Request identifier

        method : PostA2ARequestMethod
            The method to invoke

        params : typing.Optional[PostA2ARequestParams]
            Method parameters; shape depends on the method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostA2AResponse]
            JSON-RPC response for non-streaming methods. For `message/stream`, the response is an SSE stream of JSON-RPC envelopes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"a2a/{encode_path_param(assistant_id)}",
            method="POST",
            json={
                "jsonrpc": jsonrpc,
                "id": id,
                "method": method,
                "params": convert_and_respect_annotation_metadata(
                    object_=params, annotation=PostA2ARequestParams, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Accept": str(accept) if accept is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostA2AResponse,
                    parse_obj_as(
                        type_=PostA2AResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawA2AClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_a2a(
        self,
        assistant_id: str,
        *,
        accept: str,
        jsonrpc: PostA2ARequestJsonrpc,
        id: str,
        method: PostA2ARequestMethod,
        params: typing.Optional[PostA2ARequestParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostA2AResponse]:
        """
        Communicate with an assistant using the Agent-to-Agent (A2A) Protocol over JSON-RPC 2.0.
        This endpoint accepts a JSON-RPC envelope and dispatches based on `method`.

        **Supported Methods:**
        - `message/send`: Send a message and wait for the final Task result.
        - `message/stream`: Send a message and receive Server-Sent Events (SSE) JSON-RPC responses.
        - `tasks/get`: Fetch the current state of a Task by ID.
        - `tasks/cancel`: Request cancellation (currently not supported; returns an error).

        **LangGraph Mapping:**
        - `message.contextId` maps to LangGraph `thread_id`.

        **Notes:**
        - Only `text` and `data` parts are supported; `file` parts are not.
        - If `message.contextId` is omitted, a new context is created.
        - Text parts require the assistant input schema to include a `messages` field.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to communicate with

        accept : str
            For `message/stream`, must include `text/event-stream`. For all other methods, use `application/json`.

        jsonrpc : PostA2ARequestJsonrpc
            JSON-RPC version

        id : str
            Request identifier

        method : PostA2ARequestMethod
            The method to invoke

        params : typing.Optional[PostA2ARequestParams]
            Method parameters; shape depends on the method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostA2AResponse]
            JSON-RPC response for non-streaming methods. For `message/stream`, the response is an SSE stream of JSON-RPC envelopes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"a2a/{encode_path_param(assistant_id)}",
            method="POST",
            json={
                "jsonrpc": jsonrpc,
                "id": id,
                "method": method,
                "params": convert_and_respect_annotation_metadata(
                    object_=params, annotation=PostA2ARequestParams, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Accept": str(accept) if accept is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostA2AResponse,
                    parse_obj_as(
                        type_=PostA2AResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
