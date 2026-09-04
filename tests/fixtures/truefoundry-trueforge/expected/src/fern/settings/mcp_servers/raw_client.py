

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import encode_path_param
from ...core.pagination import AsyncPager, SyncPager
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...core.serialization import convert_and_respect_annotation_metadata
from ...errors.bad_request_error import BadRequestError
from ...errors.conflict_error import ConflictError
from ...errors.failed_dependency_error import FailedDependencyError
from ...errors.forbidden_error import ForbiddenError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.configured_mcp_server import ConfiguredMcpServer
from ...types.get_mcp_server_response import GetMcpServerResponse
from ...types.list_mcp_servers_response import ListMcpServersResponse
from ...types.mcp_server_manifest import McpServerManifest
from ...types.request_error_response import RequestErrorResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMcpServersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ConfiguredMcpServer, ListMcpServersResponse]:
        """
        Paginated MCP servers with auth_status. Header secrets are redacted.

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
        SyncPager[ConfiguredMcpServer, ListMcpServersResponse]
            Paginated MCP servers
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/settings/mcp-servers",
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
                    ListMcpServersResponse,
                    parse_obj_as(
                        type_=ListMcpServersResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def create(
        self, *, manifest: McpServerManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMcpServerResponse]:
        """
        Creates an MCP server by `name`. Fails if `name` is already taken. Runs DCR registration when `auth.type` is `dcr`. Header secrets: real value required; redacted with no stored value returns 400.

        Parameters
        ----------
        manifest : McpServerManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMcpServerResponse]
            The created MCP server with auth_status
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/settings/mcp-servers",
            method="POST",
            json={
                "manifest": convert_and_respect_annotation_metadata(
                    object_=manifest, annotation=McpServerManifest, direction="write"
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
                    GetMcpServerResponse,
                    parse_obj_as(
                        type_=GetMcpServerResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_or_update(
        self, *, manifest: McpServerManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMcpServerResponse]:
        """
        Create or replace by `name`. Header secrets: real value sets/rotates; redacted keeps existing (400 if none).

        Parameters
        ----------
        manifest : McpServerManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMcpServerResponse]
            The saved MCP server with auth_status
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/settings/mcp-servers",
            method="PUT",
            json={
                "manifest": convert_and_respect_annotation_metadata(
                    object_=manifest, annotation=McpServerManifest, direction="write"
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
                    GetMcpServerResponse,
                    parse_obj_as(
                        type_=GetMcpServerResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMcpServerResponse]:
        """
        A single MCP server by name, with nested live auth_status (settings / admin projection). Header auth values are redacted.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMcpServerResponse]
            The MCP server
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/settings/mcp-servers/{encode_path_param(name)}",
            method="GET",
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


class AsyncRawMcpServersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ConfiguredMcpServer, ListMcpServersResponse]:
        """
        Paginated MCP servers with auth_status. Header secrets are redacted.

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
        AsyncPager[ConfiguredMcpServer, ListMcpServersResponse]
            Paginated MCP servers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/settings/mcp-servers",
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
                    ListMcpServersResponse,
                    parse_obj_as(
                        type_=ListMcpServersResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def create(
        self, *, manifest: McpServerManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMcpServerResponse]:
        """
        Creates an MCP server by `name`. Fails if `name` is already taken. Runs DCR registration when `auth.type` is `dcr`. Header secrets: real value required; redacted with no stored value returns 400.

        Parameters
        ----------
        manifest : McpServerManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMcpServerResponse]
            The created MCP server with auth_status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/settings/mcp-servers",
            method="POST",
            json={
                "manifest": convert_and_respect_annotation_metadata(
                    object_=manifest, annotation=McpServerManifest, direction="write"
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
                    GetMcpServerResponse,
                    parse_obj_as(
                        type_=GetMcpServerResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_or_update(
        self, *, manifest: McpServerManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMcpServerResponse]:
        """
        Create or replace by `name`. Header secrets: real value sets/rotates; redacted keeps existing (400 if none).

        Parameters
        ----------
        manifest : McpServerManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMcpServerResponse]
            The saved MCP server with auth_status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/settings/mcp-servers",
            method="PUT",
            json={
                "manifest": convert_and_respect_annotation_metadata(
                    object_=manifest, annotation=McpServerManifest, direction="write"
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
                    GetMcpServerResponse,
                    parse_obj_as(
                        type_=GetMcpServerResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMcpServerResponse]:
        """
        A single MCP server by name, with nested live auth_status (settings / admin projection). Header auth values are redacted.

        Parameters
        ----------
        name : str
            MCP server name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMcpServerResponse]
            The MCP server
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/settings/mcp-servers/{encode_path_param(name)}",
            method="GET",
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
