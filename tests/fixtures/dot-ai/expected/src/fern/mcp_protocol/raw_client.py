

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.http_sse._api import EventSource
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as, parse_sse_obj
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..types.error_response import ErrorResponse
from ..types.mcp_json_rpc_response import McpJsonRpcResponse
from .types.mcp_json_rpc_request_id import McpJsonRpcRequestId
from .types.mcp_json_rpc_request_jsonrpc import McpJsonRpcRequestJsonrpc
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMcpProtocolClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def open_mcp_sse_stream(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[str]]]:
        """
        Opens a Server-Sent Events (SSE) stream for Model Context Protocol communication. This endpoint allows the server to push messages to the client without the client first sending data.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[str]]]
            SSE stream opened successfully
        """
        with self._client_wrapper.httpx_client.stream(
            method="GET",
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
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
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

    def send_mcp_json_rpc_message(
        self,
        *,
        jsonrpc: McpJsonRpcRequestJsonrpc,
        method: str,
        id: typing.Optional[McpJsonRpcRequestId] = OMIT,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[McpJsonRpcResponse]:
        """
        Send a JSON-RPC message using Model Context Protocol. Used for tool calls, initialization, and other MCP operations. The server may respond with either a JSON object or open an SSE stream.

        Parameters
        ----------
        jsonrpc : McpJsonRpcRequestJsonrpc
            JSON-RPC version

        method : str
            Method name (e.g., initialize, tools/call, tools/list)

        id : typing.Optional[McpJsonRpcRequestId]
            Request identifier

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Method parameters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[McpJsonRpcResponse]
            JSON-RPC response or SSE stream
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            json={
                "jsonrpc": jsonrpc,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=typing.Optional[McpJsonRpcRequestId], direction="write"
                ),
                "method": method,
                "params": params,
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
                    McpJsonRpcResponse,
                    parse_obj_as(
                        type_=McpJsonRpcResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawMcpProtocolClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def open_mcp_sse_stream(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]:
        """
        Opens a Server-Sent Events (SSE) stream for Model Context Protocol communication. This endpoint allows the server to push messages to the client without the client first sending data.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]
            SSE stream opened successfully
        """
        async with self._client_wrapper.httpx_client.stream(
            method="GET",
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
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
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

    async def send_mcp_json_rpc_message(
        self,
        *,
        jsonrpc: McpJsonRpcRequestJsonrpc,
        method: str,
        id: typing.Optional[McpJsonRpcRequestId] = OMIT,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[McpJsonRpcResponse]:
        """
        Send a JSON-RPC message using Model Context Protocol. Used for tool calls, initialization, and other MCP operations. The server may respond with either a JSON object or open an SSE stream.

        Parameters
        ----------
        jsonrpc : McpJsonRpcRequestJsonrpc
            JSON-RPC version

        method : str
            Method name (e.g., initialize, tools/call, tools/list)

        id : typing.Optional[McpJsonRpcRequestId]
            Request identifier

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Method parameters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[McpJsonRpcResponse]
            JSON-RPC response or SSE stream
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            json={
                "jsonrpc": jsonrpc,
                "id": convert_and_respect_annotation_metadata(
                    object_=id, annotation=typing.Optional[McpJsonRpcRequestId], direction="write"
                ),
                "method": method,
                "params": params,
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
                    McpJsonRpcResponse,
                    parse_obj_as(
                        type_=McpJsonRpcResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
