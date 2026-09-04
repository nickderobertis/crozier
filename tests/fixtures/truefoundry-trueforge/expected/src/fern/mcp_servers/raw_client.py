

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.pagination import AsyncPager, SyncPager
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.failed_dependency_error import FailedDependencyError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.available_mcp_server import AvailableMcpServer
from ..types.get_mcp_server_response import GetMcpServerResponse
from ..types.list_available_mcp_servers_response import ListAvailableMcpServersResponse
from ..types.list_mcp_server_tools_response import ListMcpServerToolsResponse
from ..types.mcp_auth_status import McpAuthStatus
from ..types.request_error_response import RequestErrorResponse
from pydantic import ValidationError


class RawMcpServersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[AvailableMcpServer, ListAvailableMcpServersResponse]:
        """
        Paginated MCP servers as a slim name/url list for the composer.

        Parameters
        ----------
        limit : typing.Optional[int]
            Page size. Defaults to 100, max 200.

        page_token : typing.Optional[str]
            Opaque token from a previous response `next_page_token`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[AvailableMcpServer, ListAvailableMcpServersResponse]
            Paginated MCP servers (chat projection).
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/mcp-servers",
            method="GET",
            params={
                "limit": limit,
                "page_token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListAvailableMcpServersResponse,
                    parse_obj_as(
                        type_=ListAvailableMcpServersResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = False
                _get_next = None
                if _parsed_response.pagination is not None:
                    _parsed_next = _parsed_response.pagination.next_page_token
                    _has_next = _parsed_next is not None and _parsed_next != ""
                    _get_next = lambda: self.list(
                        limit=limit,
                        page_token=_parsed_next,
                        request_options=request_options,
                    )
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
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

    def authorize(
        self,
        name: str,
        *,
        return_to: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[McpAuthStatus]:
        """
        Returns current auth status. When OAuth is required, includes an authorization URL. Optional return_to is the post-consent landing path.

        Parameters
        ----------
        name : str
            MCP server name.

        return_to : typing.Optional[str]
            Same-origin path to land in the browser after consent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[McpAuthStatus]
            Either already authenticated, or an authorization URL to redirect to.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/mcp-servers/{encode_path_param(name)}/authorize",
            method="GET",
            params={
                "return_to": return_to,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpAuthStatus,
                    parse_obj_as(
                        type_=McpAuthStatus,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 424:
                raise FailedDependencyError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
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

    def delete_authorization(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMcpServerResponse]:
        """
        Disconnects OAuth for the MCP server when applicable and returns the updated server with auth_status. No-op when the server does not use stored OAuth tokens.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMcpServerResponse]
            The MCP server after disconnect.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/mcp-servers/{encode_path_param(name)}/authorize",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMcpServerResponse,
                    parse_obj_as(
                        type_=GetMcpServerResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
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

    def list_tools(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListMcpServerToolsResponse]:
        """
        All tools exposed by the given MCP server (non-paginated), as returned by the MCP `tools/list` call.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMcpServerToolsResponse]
            All tools of the MCP server.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/mcp-servers/{encode_path_param(name)}/tools",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMcpServerToolsResponse,
                    parse_obj_as(
                        type_=ListMcpServerToolsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
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


class AsyncRawMcpServersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[AvailableMcpServer, ListAvailableMcpServersResponse]:
        """
        Paginated MCP servers as a slim name/url list for the composer.

        Parameters
        ----------
        limit : typing.Optional[int]
            Page size. Defaults to 100, max 200.

        page_token : typing.Optional[str]
            Opaque token from a previous response `next_page_token`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[AvailableMcpServer, ListAvailableMcpServersResponse]
            Paginated MCP servers (chat projection).
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/mcp-servers",
            method="GET",
            params={
                "limit": limit,
                "page_token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListAvailableMcpServersResponse,
                    parse_obj_as(
                        type_=ListAvailableMcpServersResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = False
                _get_next = None
                if _parsed_response.pagination is not None:
                    _parsed_next = _parsed_response.pagination.next_page_token
                    _has_next = _parsed_next is not None and _parsed_next != ""

                    async def _get_next():
                        return await self.list(
                            limit=limit,
                            page_token=_parsed_next,
                            request_options=request_options,
                        )

                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
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

    async def authorize(
        self,
        name: str,
        *,
        return_to: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[McpAuthStatus]:
        """
        Returns current auth status. When OAuth is required, includes an authorization URL. Optional return_to is the post-consent landing path.

        Parameters
        ----------
        name : str
            MCP server name.

        return_to : typing.Optional[str]
            Same-origin path to land in the browser after consent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[McpAuthStatus]
            Either already authenticated, or an authorization URL to redirect to.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/mcp-servers/{encode_path_param(name)}/authorize",
            method="GET",
            params={
                "return_to": return_to,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    McpAuthStatus,
                    parse_obj_as(
                        type_=McpAuthStatus,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 424:
                raise FailedDependencyError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
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

    async def delete_authorization(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMcpServerResponse]:
        """
        Disconnects OAuth for the MCP server when applicable and returns the updated server with auth_status. No-op when the server does not use stored OAuth tokens.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMcpServerResponse]
            The MCP server after disconnect.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/mcp-servers/{encode_path_param(name)}/authorize",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMcpServerResponse,
                    parse_obj_as(
                        type_=GetMcpServerResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
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

    async def list_tools(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListMcpServerToolsResponse]:
        """
        All tools exposed by the given MCP server (non-paginated), as returned by the MCP `tools/list` call.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMcpServerToolsResponse]
            All tools of the MCP server.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/mcp-servers/{encode_path_param(name)}/tools",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMcpServerToolsResponse,
                    parse_obj_as(
                        type_=ListMcpServerToolsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
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
