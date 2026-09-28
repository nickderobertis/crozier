

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.tools_get_response import ToolsGetResponse
from ..types.tools_tool_name_post_request import ToolsToolNamePostRequest
from ..types.tools_tool_name_post_response import ToolsToolNamePostResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawToolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def discover_available_tools_with_optional_filtering_by_category_tag_or_search_term(
        self,
        *,
        category: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolsGetResponse]:
        """
        Discover available tools with optional filtering by category, tag, or search term

        Parameters
        ----------
        category : typing.Optional[str]
            Filter tools by category

        tag : typing.Optional[str]
            Filter tools by tag

        search : typing.Optional[str]
            Search tools by name or description

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ToolsGetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/tools",
            method="GET",
            params={
                "category": category,
                "tag": tag,
                "search": search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolsGetResponse,
                    parse_obj_as(
                        type_=ToolsGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def execute_a_tool_with_the_provided_parameters(
        self,
        tool_name: str,
        *,
        request: ToolsToolNamePostRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolsToolNamePostResponse]:
        """
        Execute a tool with the provided parameters

        Parameters
        ----------
        tool_name : str
            Name of the tool to execute

        request : ToolsToolNamePostRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ToolsToolNamePostResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/tools/{encode_path_param(tool_name)}",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolsToolNamePostResponse,
                    parse_obj_as(
                        type_=ToolsToolNamePostResponse,
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


class AsyncRawToolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def discover_available_tools_with_optional_filtering_by_category_tag_or_search_term(
        self,
        *,
        category: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ToolsGetResponse]:
        """
        Discover available tools with optional filtering by category, tag, or search term

        Parameters
        ----------
        category : typing.Optional[str]
            Filter tools by category

        tag : typing.Optional[str]
            Filter tools by tag

        search : typing.Optional[str]
            Search tools by name or description

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ToolsGetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/tools",
            method="GET",
            params={
                "category": category,
                "tag": tag,
                "search": search,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolsGetResponse,
                    parse_obj_as(
                        type_=ToolsGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def execute_a_tool_with_the_provided_parameters(
        self,
        tool_name: str,
        *,
        request: ToolsToolNamePostRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ToolsToolNamePostResponse]:
        """
        Execute a tool with the provided parameters

        Parameters
        ----------
        tool_name : str
            Name of the tool to execute

        request : ToolsToolNamePostRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ToolsToolNamePostResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/tools/{encode_path_param(tool_name)}",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolsToolNamePostResponse,
                    parse_obj_as(
                        type_=ToolsToolNamePostResponse,
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
