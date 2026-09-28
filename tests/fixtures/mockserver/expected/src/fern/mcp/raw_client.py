

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMcpClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def not_supported(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Documented so the behaviour is not mistaken for SSE support: MockServer's MCP endpoint does not implement the server-initiated SSE stream, and a GET is always refused.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/mcp",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 405:
                raise MethodNotAllowedError(
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

    def mcp_model_context_protocol_json_rpc_endpoint(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        mcp_session_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Streamable-HTTP MCP endpoint, letting AI agents and LLM tooling drive MockServer as an MCP server. The body is a JSON-RPC 2.0 request object or a batch array. Call `initialize` first; the response carries a new session id in the `Mcp-Session-Id` response header, which subsequent calls must send back in the `Mcp-Session-Id` request header. Protocol versions 2025-06-18 (default), 2025-03-26 and 2024-11-05 are negotiated. Note that a missing or invalid session is reported as a JSON-RPC error inside a 200 response, not as a 4xx. Unlike its sibling endpoints this path has no bare `/mcp` alias, and sub-paths under `/mockserver/mcp/` also route here.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        mcp_session_id : typing.Optional[str]
            session id returned by a previous `initialize` call; omit on `initialize` itself

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON-RPC response. Also used for JSON-RPC-level errors such as an missing or invalid session. On `initialize` the response carries the new session id in the Mcp-Session-Id header.
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/mcp",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
                "Mcp-Session-Id": str(mcp_session_id) if mcp_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def end_an_mcp_session(
        self, *, mcp_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Removes the MCP session identified by the `Mcp-Session-Id` request header.

        Parameters
        ----------
        mcp_session_id : str
            the session to end

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/mcp",
            method="DELETE",
            headers={
                "Mcp-Session-Id": str(mcp_session_id) if mcp_session_id is not None else None,
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


class AsyncRawMcpClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def not_supported(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Documented so the behaviour is not mistaken for SSE support: MockServer's MCP endpoint does not implement the server-initiated SSE stream, and a GET is always refused.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/mcp",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 405:
                raise MethodNotAllowedError(
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

    async def mcp_model_context_protocol_json_rpc_endpoint(
        self,
        *,
        request: typing.Dict[str, typing.Any],
        mcp_session_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Streamable-HTTP MCP endpoint, letting AI agents and LLM tooling drive MockServer as an MCP server. The body is a JSON-RPC 2.0 request object or a batch array. Call `initialize` first; the response carries a new session id in the `Mcp-Session-Id` response header, which subsequent calls must send back in the `Mcp-Session-Id` request header. Protocol versions 2025-06-18 (default), 2025-03-26 and 2024-11-05 are negotiated. Note that a missing or invalid session is reported as a JSON-RPC error inside a 200 response, not as a 4xx. Unlike its sibling endpoints this path has no bare `/mcp` alias, and sub-paths under `/mockserver/mcp/` also route here.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        mcp_session_id : typing.Optional[str]
            session id returned by a previous `initialize` call; omit on `initialize` itself

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON-RPC response. Also used for JSON-RPC-level errors such as an missing or invalid session. On `initialize` the response carries the new session id in the Mcp-Session-Id header.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/mcp",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
                "Mcp-Session-Id": str(mcp_session_id) if mcp_session_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def end_an_mcp_session(
        self, *, mcp_session_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Removes the MCP session identified by the `Mcp-Session-Id` request header.

        Parameters
        ----------
        mcp_session_id : str
            the session to end

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/mcp",
            method="DELETE",
            headers={
                "Mcp-Session-Id": str(mcp_session_id) if mcp_session_id is not None else None,
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
