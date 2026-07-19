

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.mcp_tool import McpTool
from ..types.npm_requirement import NpmRequirement
from ..types.pip_requirement import PipRequirement
from ..types.tool import Tool
from ..types.tool_return_message import ToolReturnMessage
from ..types.tool_search_result import ToolSearchResult
from .types.add_mcp_server_request import AddMcpServerRequest
from .types.add_mcp_server_response_item import AddMcpServerResponseItem
from .types.connect_mcp_server_request import ConnectMcpServerRequest
from .types.delete_mcp_server_response_item import DeleteMcpServerResponseItem
from .types.list_mcp_servers_response_value import ListMcpServersResponseValue
from .types.list_tools_request_order import ListToolsRequestOrder
from .types.list_tools_request_order_by import ListToolsRequestOrderBy
from .types.test_mcp_server_request import TestMcpServerRequest
from .types.tool_search_request_search_mode import ToolSearchRequestSearchMode
from .types.update_mcp_server_request_body import UpdateMcpServerRequestBody
from .types.update_mcp_server_response import UpdateMcpServerResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawToolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_tool(
        self, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Tool]:
        """
        Get a tool by ID

        Parameters
        ----------
        tool_id : str
            The ID of the tool in the format 'tool-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tool]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tools/{encode_path_param(tool_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tool,
                    parse_obj_as(
                        type_=Tool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def delete_tool(
        self, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a tool by name

        Parameters
        ----------
        tool_id : str
            The ID of the tool in the format 'tool-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tools/{encode_path_param(tool_id)}",
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def modify_tool(
        self,
        tool_id: str,
        *,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        source_code: typing.Optional[str] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        args_json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        return_char_limit: typing.Optional[int] = OMIT,
        pip_requirements: typing.Optional[typing.Sequence[PipRequirement]] = OMIT,
        npm_requirements: typing.Optional[typing.Sequence[NpmRequirement]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        default_requires_approval: typing.Optional[bool] = OMIT,
        enable_parallel_execution: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Tool]:
        """
        Update an existing tool

        Parameters
        ----------
        tool_id : str
            The ID of the tool in the format 'tool-<uuid4>'

        description : typing.Optional[str]
            The description of the tool.

        tags : typing.Optional[typing.Sequence[str]]
            Metadata tags.

        source_code : typing.Optional[str]
            The source code of the function.

        source_type : typing.Optional[str]
            The type of the source code.

        json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The JSON schema of the function (auto-generated from source_code if not provided)

        args_json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The args JSON schema of the function.

        return_char_limit : typing.Optional[int]
            The maximum number of characters in the response.

        pip_requirements : typing.Optional[typing.Sequence[PipRequirement]]
            Optional list of pip packages required by this tool.

        npm_requirements : typing.Optional[typing.Sequence[NpmRequirement]]
            Optional list of npm packages required by this tool.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            A dictionary of additional metadata for the tool.

        default_requires_approval : typing.Optional[bool]
            Whether or not to require approval before executing this tool.

        enable_parallel_execution : typing.Optional[bool]
            If set to True, then this tool will potentially be executed concurrently with other tools. Default False.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tool]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tools/{encode_path_param(tool_id)}",
            method="PATCH",
            json={
                "description": description,
                "tags": tags,
                "source_code": source_code,
                "source_type": source_type,
                "json_schema": json_schema,
                "args_json_schema": args_json_schema,
                "return_char_limit": return_char_limit,
                "pip_requirements": convert_and_respect_annotation_metadata(
                    object_=pip_requirements,
                    annotation=typing.Optional[typing.Sequence[PipRequirement]],
                    direction="write",
                ),
                "npm_requirements": convert_and_respect_annotation_metadata(
                    object_=npm_requirements,
                    annotation=typing.Optional[typing.Sequence[NpmRequirement]],
                    direction="write",
                ),
                "metadata_": metadata,
                "default_requires_approval": default_requires_approval,
                "enable_parallel_execution": enable_parallel_execution,
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
                    Tool,
                    parse_obj_as(
                        type_=Tool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def count_tools(
        self,
        *,
        name: typing.Optional[str] = None,
        names: typing.Optional[typing.Sequence[str]] = None,
        tool_ids: typing.Optional[typing.Sequence[str]] = None,
        search: typing.Optional[str] = None,
        tool_types: typing.Optional[typing.Sequence[str]] = None,
        exclude_tool_types: typing.Optional[typing.Sequence[str]] = None,
        return_only_letta_tools: typing.Optional[bool] = None,
        exclude_letta_tools: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Get a count of all tools available to agents belonging to the org of the user.

        Parameters
        ----------
        name : typing.Optional[str]

        names : typing.Optional[typing.Sequence[str]]
            Filter by specific tool names

        tool_ids : typing.Optional[typing.Sequence[str]]
            Filter by specific tool IDs - accepts repeated params or comma-separated values

        search : typing.Optional[str]
            Search tool names (case-insensitive partial match)

        tool_types : typing.Optional[typing.Sequence[str]]
            Filter by tool type(s) - accepts repeated params or comma-separated values

        exclude_tool_types : typing.Optional[typing.Sequence[str]]
            Tool type(s) to exclude - accepts repeated params or comma-separated values

        return_only_letta_tools : typing.Optional[bool]
            Count only tools with tool_type starting with 'letta_'

        exclude_letta_tools : typing.Optional[bool]
            Exclude built-in Letta tools from the count

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/count",
            method="GET",
            params={
                "name": name,
                "names": names,
                "tool_ids": tool_ids,
                "search": search,
                "tool_types": tool_types,
                "exclude_tool_types": exclude_tool_types,
                "return_only_letta_tools": return_only_letta_tools,
                "exclude_letta_tools": exclude_letta_tools,
            },
            request_options=request_options,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListToolsRequestOrder] = None,
        order_by: typing.Optional[ListToolsRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        names: typing.Optional[typing.Sequence[str]] = None,
        tool_ids: typing.Optional[typing.Sequence[str]] = None,
        search: typing.Optional[str] = None,
        tool_types: typing.Optional[typing.Sequence[str]] = None,
        exclude_tool_types: typing.Optional[typing.Sequence[str]] = None,
        return_only_letta_tools: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Tool]]:
        """
        Get a list of all tools available to agents.

        Parameters
        ----------
        before : typing.Optional[str]
            Tool ID cursor for pagination. Returns tools that come before this tool ID in the specified sort order

        after : typing.Optional[str]
            Tool ID cursor for pagination. Returns tools that come after this tool ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of tools to return

        order : typing.Optional[ListToolsRequestOrder]
            Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListToolsRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Filter by single tool name

        names : typing.Optional[typing.Sequence[str]]
            Filter by specific tool names

        tool_ids : typing.Optional[typing.Sequence[str]]
            Filter by specific tool IDs - accepts repeated params or comma-separated values

        search : typing.Optional[str]
            Search tool names (case-insensitive partial match)

        tool_types : typing.Optional[typing.Sequence[str]]
            Filter by tool type(s) - accepts repeated params or comma-separated values

        exclude_tool_types : typing.Optional[typing.Sequence[str]]
            Tool type(s) to exclude - accepts repeated params or comma-separated values

        return_only_letta_tools : typing.Optional[bool]
            Return only tools with tool_type starting with 'letta_'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Tool]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "name": name,
                "names": names,
                "tool_ids": tool_ids,
                "search": search,
                "tool_types": tool_types,
                "exclude_tool_types": exclude_tool_types,
                "return_only_letta_tools": return_only_letta_tools,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Tool],
                    parse_obj_as(
                        type_=typing.List[Tool],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def create_tool(
        self,
        *,
        source_code: str,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        args_json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        return_char_limit: typing.Optional[int] = OMIT,
        pip_requirements: typing.Optional[typing.Sequence[PipRequirement]] = OMIT,
        npm_requirements: typing.Optional[typing.Sequence[NpmRequirement]] = OMIT,
        default_requires_approval: typing.Optional[bool] = OMIT,
        enable_parallel_execution: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Tool]:
        """
        Create a new tool

        Parameters
        ----------
        source_code : str
            The source code of the function.

        description : typing.Optional[str]
            The description of the tool.

        tags : typing.Optional[typing.Sequence[str]]
            Metadata tags.

        source_type : typing.Optional[str]
            The source type of the function.

        json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The JSON schema of the function (auto-generated from source_code if not provided)

        args_json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The args JSON schema of the function.

        return_char_limit : typing.Optional[int]
            The maximum number of characters in the response.

        pip_requirements : typing.Optional[typing.Sequence[PipRequirement]]
            Optional list of pip packages required by this tool.

        npm_requirements : typing.Optional[typing.Sequence[NpmRequirement]]
            Optional list of npm packages required by this tool.

        default_requires_approval : typing.Optional[bool]
            Whether or not to require approval before executing this tool.

        enable_parallel_execution : typing.Optional[bool]
            If set to True, then this tool will potentially be executed concurrently with other tools. Default False.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tool]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/",
            method="POST",
            json={
                "description": description,
                "tags": tags,
                "source_code": source_code,
                "source_type": source_type,
                "json_schema": json_schema,
                "args_json_schema": args_json_schema,
                "return_char_limit": return_char_limit,
                "pip_requirements": convert_and_respect_annotation_metadata(
                    object_=pip_requirements,
                    annotation=typing.Optional[typing.Sequence[PipRequirement]],
                    direction="write",
                ),
                "npm_requirements": convert_and_respect_annotation_metadata(
                    object_=npm_requirements,
                    annotation=typing.Optional[typing.Sequence[NpmRequirement]],
                    direction="write",
                ),
                "default_requires_approval": default_requires_approval,
                "enable_parallel_execution": enable_parallel_execution,
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
                    Tool,
                    parse_obj_as(
                        type_=Tool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def upsert_tool(
        self,
        *,
        source_code: str,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        args_json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        return_char_limit: typing.Optional[int] = OMIT,
        pip_requirements: typing.Optional[typing.Sequence[PipRequirement]] = OMIT,
        npm_requirements: typing.Optional[typing.Sequence[NpmRequirement]] = OMIT,
        default_requires_approval: typing.Optional[bool] = OMIT,
        enable_parallel_execution: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Tool]:
        """
        Create or update a tool

        Parameters
        ----------
        source_code : str
            The source code of the function.

        description : typing.Optional[str]
            The description of the tool.

        tags : typing.Optional[typing.Sequence[str]]
            Metadata tags.

        source_type : typing.Optional[str]
            The source type of the function.

        json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The JSON schema of the function (auto-generated from source_code if not provided)

        args_json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The args JSON schema of the function.

        return_char_limit : typing.Optional[int]
            The maximum number of characters in the response.

        pip_requirements : typing.Optional[typing.Sequence[PipRequirement]]
            Optional list of pip packages required by this tool.

        npm_requirements : typing.Optional[typing.Sequence[NpmRequirement]]
            Optional list of npm packages required by this tool.

        default_requires_approval : typing.Optional[bool]
            Whether or not to require approval before executing this tool.

        enable_parallel_execution : typing.Optional[bool]
            If set to True, then this tool will potentially be executed concurrently with other tools. Default False.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tool]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/",
            method="PUT",
            json={
                "description": description,
                "tags": tags,
                "source_code": source_code,
                "source_type": source_type,
                "json_schema": json_schema,
                "args_json_schema": args_json_schema,
                "return_char_limit": return_char_limit,
                "pip_requirements": convert_and_respect_annotation_metadata(
                    object_=pip_requirements,
                    annotation=typing.Optional[typing.Sequence[PipRequirement]],
                    direction="write",
                ),
                "npm_requirements": convert_and_respect_annotation_metadata(
                    object_=npm_requirements,
                    annotation=typing.Optional[typing.Sequence[NpmRequirement]],
                    direction="write",
                ),
                "default_requires_approval": default_requires_approval,
                "enable_parallel_execution": enable_parallel_execution,
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
                    Tool,
                    parse_obj_as(
                        type_=Tool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def search_tools(
        self,
        *,
        query: typing.Optional[str] = OMIT,
        search_mode: typing.Optional[ToolSearchRequestSearchMode] = OMIT,
        tool_types: typing.Optional[typing.Sequence[str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ToolSearchResult]]:
        """
        Search tools using semantic search.

        Requires tool embedding to be enabled (embed_tools=True). Uses vector search,
        full-text search, or hybrid mode to find tools matching the query.

        Returns tools ranked by relevance with their search scores.

        Parameters
        ----------
        query : typing.Optional[str]
            Text query for semantic search.

        search_mode : typing.Optional[ToolSearchRequestSearchMode]
            Search mode: vector, fts, or hybrid.

        tool_types : typing.Optional[typing.Sequence[str]]
            Filter by tool types (e.g., 'custom', 'letta_core').

        tags : typing.Optional[typing.Sequence[str]]
            Filter by tags (match any).

        limit : typing.Optional[int]
            Maximum number of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ToolSearchResult]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/search",
            method="POST",
            json={
                "query": query,
                "search_mode": search_mode,
                "tool_types": tool_types,
                "tags": tags,
                "limit": limit,
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
                    typing.List[ToolSearchResult],
                    parse_obj_as(
                        type_=typing.List[ToolSearchResult],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def add_base_tools(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Tool]]:
        """
        Upsert base tools

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Tool]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/add-base-tools",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Tool],
                    parse_obj_as(
                        type_=typing.List[Tool],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def run_tool_from_source(
        self,
        *,
        source_code: str,
        args: typing.Dict[str, typing.Any],
        env_vars: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        args_json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        pip_requirements: typing.Optional[typing.Sequence[PipRequirement]] = OMIT,
        npm_requirements: typing.Optional[typing.Sequence[NpmRequirement]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolReturnMessage]:
        """
        Attempt to build a tool from source, then run it on the provided arguments

        Parameters
        ----------
        source_code : str
            The source code of the function.

        args : typing.Dict[str, typing.Any]
            The arguments to pass to the tool.

        env_vars : typing.Optional[typing.Dict[str, str]]
            The environment variables to pass to the tool.

        name : typing.Optional[str]
            The name of the tool to run.

        source_type : typing.Optional[str]
            The type of the source code.

        args_json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The args JSON schema of the function.

        json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The JSON schema of the function (auto-generated from source_code if not provided)

        pip_requirements : typing.Optional[typing.Sequence[PipRequirement]]
            Optional list of pip packages required by this tool.

        npm_requirements : typing.Optional[typing.Sequence[NpmRequirement]]
            Optional list of npm packages required by this tool.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ToolReturnMessage]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/run",
            method="POST",
            json={
                "source_code": source_code,
                "args": args,
                "env_vars": env_vars,
                "name": name,
                "source_type": source_type,
                "args_json_schema": args_json_schema,
                "json_schema": json_schema,
                "pip_requirements": convert_and_respect_annotation_metadata(
                    object_=pip_requirements,
                    annotation=typing.Optional[typing.Sequence[PipRequirement]],
                    direction="write",
                ),
                "npm_requirements": convert_and_respect_annotation_metadata(
                    object_=npm_requirements,
                    annotation=typing.Optional[typing.Sequence[NpmRequirement]],
                    direction="write",
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
                    ToolReturnMessage,
                    parse_obj_as(
                        type_=ToolReturnMessage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def list_mcp_servers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, ListMcpServersResponseValue]]:
        """
        Get a list of all configured MCP servers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, ListMcpServersResponseValue]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/mcp/servers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, ListMcpServersResponseValue],
                    parse_obj_as(
                        type_=typing.Dict[str, ListMcpServersResponseValue],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def add_mcp_server(
        self, *, request: AddMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[AddMcpServerResponseItem]]:
        """
        Add a new MCP server to the Letta MCP server config

        Parameters
        ----------
        request : AddMcpServerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AddMcpServerResponseItem]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/mcp/servers",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=AddMcpServerRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AddMcpServerResponseItem],
                    parse_obj_as(
                        type_=typing.List[AddMcpServerResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def list_mcp_tools_by_server(
        self, mcp_server_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[McpTool]]:
        """
        Get a list of all tools for a specific MCP server

        Parameters
        ----------
        mcp_server_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[McpTool]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}/tools",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[McpTool],
                    parse_obj_as(
                        type_=typing.List[McpTool],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def resync_mcp_server_tools(
        self,
        mcp_server_name: str,
        *,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Resync tools for an MCP server by:
        1. Fetching current tools from the MCP server
        2. Deleting tools that no longer exist on the server
        3. Updating schemas for existing tools
        4. Adding new tools from the server

        Returns a summary of changes made.

        Parameters
        ----------
        mcp_server_name : str

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}/resync",
            method="POST",
            params={
                "agent_id": agent_id,
            },
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def add_mcp_tool(
        self, mcp_server_name: str, mcp_tool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Tool]:
        """
        Register a new MCP tool as a Letta server by MCP server + tool name

        Parameters
        ----------
        mcp_server_name : str

        mcp_tool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tool]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}/{encode_path_param(mcp_tool_name)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tool,
                    parse_obj_as(
                        type_=Tool,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def delete_mcp_server(
        self, mcp_server_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[DeleteMcpServerResponseItem]]:
        """
        Delete a MCP server configuration

        Parameters
        ----------
        mcp_server_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[DeleteMcpServerResponseItem]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DeleteMcpServerResponseItem],
                    parse_obj_as(
                        type_=typing.List[DeleteMcpServerResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_mcp_server(
        self,
        mcp_server_name: str,
        *,
        request: UpdateMcpServerRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateMcpServerResponse]:
        """
        Update an existing MCP server configuration

        Parameters
        ----------
        mcp_server_name : str

        request : UpdateMcpServerRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateMcpServerResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateMcpServerRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateMcpServerResponse,
                    parse_obj_as(
                        type_=UpdateMcpServerResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def test_mcp_server(
        self, *, request: TestMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Test connection to an MCP server without adding it.
        Returns the list of available tools if successful.

        Parameters
        ----------
        request : TestMcpServerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/mcp/servers/test",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=TestMcpServerRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def connect_mcp_server(
        self, *, request: ConnectMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Connect to an MCP server with support for OAuth via SSE.
        Returns a stream of events handling authorization state and exchange if OAuth is required.

        Parameters
        ----------
        request : ConnectMcpServerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/mcp/servers/connect",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ConnectMcpServerRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def execute_mcp_tool(
        self,
        mcp_server_name: str,
        tool_name: str,
        *,
        args: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Execute a specific MCP tool from a configured server.
        Returns the tool execution result.

        Parameters
        ----------
        mcp_server_name : str

        tool_name : str

        args : typing.Optional[typing.Dict[str, typing.Any]]
            Arguments to pass to the tool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}/tools/{encode_path_param(tool_name)}/execute",
            method="POST",
            json={
                "args": args,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def mcp_oauth_callback(
        self,
        *,
        code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Handle OAuth callback for MCP server authentication.
        Session is identified via the state parameter instead of URL path.

        Parameters
        ----------
        code : typing.Optional[str]
            OAuth authorization code

        state : typing.Optional[str]
            OAuth state parameter

        error : typing.Optional[str]
            OAuth error

        error_description : typing.Optional[str]
            OAuth error description

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tools/mcp/oauth/callback",
            method="GET",
            params={
                "code": code,
                "state": state,
                "error": error,
                "error_description": error_description,
            },
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def retrieve_tool(
        self, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Tool]:
        """
        Get a tool by ID

        Parameters
        ----------
        tool_id : str
            The ID of the tool in the format 'tool-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tool]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tools/{encode_path_param(tool_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tool,
                    parse_obj_as(
                        type_=Tool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def delete_tool(
        self, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a tool by name

        Parameters
        ----------
        tool_id : str
            The ID of the tool in the format 'tool-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tools/{encode_path_param(tool_id)}",
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def modify_tool(
        self,
        tool_id: str,
        *,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        source_code: typing.Optional[str] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        args_json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        return_char_limit: typing.Optional[int] = OMIT,
        pip_requirements: typing.Optional[typing.Sequence[PipRequirement]] = OMIT,
        npm_requirements: typing.Optional[typing.Sequence[NpmRequirement]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        default_requires_approval: typing.Optional[bool] = OMIT,
        enable_parallel_execution: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Tool]:
        """
        Update an existing tool

        Parameters
        ----------
        tool_id : str
            The ID of the tool in the format 'tool-<uuid4>'

        description : typing.Optional[str]
            The description of the tool.

        tags : typing.Optional[typing.Sequence[str]]
            Metadata tags.

        source_code : typing.Optional[str]
            The source code of the function.

        source_type : typing.Optional[str]
            The type of the source code.

        json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The JSON schema of the function (auto-generated from source_code if not provided)

        args_json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The args JSON schema of the function.

        return_char_limit : typing.Optional[int]
            The maximum number of characters in the response.

        pip_requirements : typing.Optional[typing.Sequence[PipRequirement]]
            Optional list of pip packages required by this tool.

        npm_requirements : typing.Optional[typing.Sequence[NpmRequirement]]
            Optional list of npm packages required by this tool.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            A dictionary of additional metadata for the tool.

        default_requires_approval : typing.Optional[bool]
            Whether or not to require approval before executing this tool.

        enable_parallel_execution : typing.Optional[bool]
            If set to True, then this tool will potentially be executed concurrently with other tools. Default False.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tool]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tools/{encode_path_param(tool_id)}",
            method="PATCH",
            json={
                "description": description,
                "tags": tags,
                "source_code": source_code,
                "source_type": source_type,
                "json_schema": json_schema,
                "args_json_schema": args_json_schema,
                "return_char_limit": return_char_limit,
                "pip_requirements": convert_and_respect_annotation_metadata(
                    object_=pip_requirements,
                    annotation=typing.Optional[typing.Sequence[PipRequirement]],
                    direction="write",
                ),
                "npm_requirements": convert_and_respect_annotation_metadata(
                    object_=npm_requirements,
                    annotation=typing.Optional[typing.Sequence[NpmRequirement]],
                    direction="write",
                ),
                "metadata_": metadata,
                "default_requires_approval": default_requires_approval,
                "enable_parallel_execution": enable_parallel_execution,
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
                    Tool,
                    parse_obj_as(
                        type_=Tool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def count_tools(
        self,
        *,
        name: typing.Optional[str] = None,
        names: typing.Optional[typing.Sequence[str]] = None,
        tool_ids: typing.Optional[typing.Sequence[str]] = None,
        search: typing.Optional[str] = None,
        tool_types: typing.Optional[typing.Sequence[str]] = None,
        exclude_tool_types: typing.Optional[typing.Sequence[str]] = None,
        return_only_letta_tools: typing.Optional[bool] = None,
        exclude_letta_tools: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Get a count of all tools available to agents belonging to the org of the user.

        Parameters
        ----------
        name : typing.Optional[str]

        names : typing.Optional[typing.Sequence[str]]
            Filter by specific tool names

        tool_ids : typing.Optional[typing.Sequence[str]]
            Filter by specific tool IDs - accepts repeated params or comma-separated values

        search : typing.Optional[str]
            Search tool names (case-insensitive partial match)

        tool_types : typing.Optional[typing.Sequence[str]]
            Filter by tool type(s) - accepts repeated params or comma-separated values

        exclude_tool_types : typing.Optional[typing.Sequence[str]]
            Tool type(s) to exclude - accepts repeated params or comma-separated values

        return_only_letta_tools : typing.Optional[bool]
            Count only tools with tool_type starting with 'letta_'

        exclude_letta_tools : typing.Optional[bool]
            Exclude built-in Letta tools from the count

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/count",
            method="GET",
            params={
                "name": name,
                "names": names,
                "tool_ids": tool_ids,
                "search": search,
                "tool_types": tool_types,
                "exclude_tool_types": exclude_tool_types,
                "return_only_letta_tools": return_only_letta_tools,
                "exclude_letta_tools": exclude_letta_tools,
            },
            request_options=request_options,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListToolsRequestOrder] = None,
        order_by: typing.Optional[ListToolsRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        names: typing.Optional[typing.Sequence[str]] = None,
        tool_ids: typing.Optional[typing.Sequence[str]] = None,
        search: typing.Optional[str] = None,
        tool_types: typing.Optional[typing.Sequence[str]] = None,
        exclude_tool_types: typing.Optional[typing.Sequence[str]] = None,
        return_only_letta_tools: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Tool]]:
        """
        Get a list of all tools available to agents.

        Parameters
        ----------
        before : typing.Optional[str]
            Tool ID cursor for pagination. Returns tools that come before this tool ID in the specified sort order

        after : typing.Optional[str]
            Tool ID cursor for pagination. Returns tools that come after this tool ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of tools to return

        order : typing.Optional[ListToolsRequestOrder]
            Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListToolsRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Filter by single tool name

        names : typing.Optional[typing.Sequence[str]]
            Filter by specific tool names

        tool_ids : typing.Optional[typing.Sequence[str]]
            Filter by specific tool IDs - accepts repeated params or comma-separated values

        search : typing.Optional[str]
            Search tool names (case-insensitive partial match)

        tool_types : typing.Optional[typing.Sequence[str]]
            Filter by tool type(s) - accepts repeated params or comma-separated values

        exclude_tool_types : typing.Optional[typing.Sequence[str]]
            Tool type(s) to exclude - accepts repeated params or comma-separated values

        return_only_letta_tools : typing.Optional[bool]
            Return only tools with tool_type starting with 'letta_'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Tool]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "name": name,
                "names": names,
                "tool_ids": tool_ids,
                "search": search,
                "tool_types": tool_types,
                "exclude_tool_types": exclude_tool_types,
                "return_only_letta_tools": return_only_letta_tools,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Tool],
                    parse_obj_as(
                        type_=typing.List[Tool],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def create_tool(
        self,
        *,
        source_code: str,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        args_json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        return_char_limit: typing.Optional[int] = OMIT,
        pip_requirements: typing.Optional[typing.Sequence[PipRequirement]] = OMIT,
        npm_requirements: typing.Optional[typing.Sequence[NpmRequirement]] = OMIT,
        default_requires_approval: typing.Optional[bool] = OMIT,
        enable_parallel_execution: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Tool]:
        """
        Create a new tool

        Parameters
        ----------
        source_code : str
            The source code of the function.

        description : typing.Optional[str]
            The description of the tool.

        tags : typing.Optional[typing.Sequence[str]]
            Metadata tags.

        source_type : typing.Optional[str]
            The source type of the function.

        json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The JSON schema of the function (auto-generated from source_code if not provided)

        args_json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The args JSON schema of the function.

        return_char_limit : typing.Optional[int]
            The maximum number of characters in the response.

        pip_requirements : typing.Optional[typing.Sequence[PipRequirement]]
            Optional list of pip packages required by this tool.

        npm_requirements : typing.Optional[typing.Sequence[NpmRequirement]]
            Optional list of npm packages required by this tool.

        default_requires_approval : typing.Optional[bool]
            Whether or not to require approval before executing this tool.

        enable_parallel_execution : typing.Optional[bool]
            If set to True, then this tool will potentially be executed concurrently with other tools. Default False.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tool]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/",
            method="POST",
            json={
                "description": description,
                "tags": tags,
                "source_code": source_code,
                "source_type": source_type,
                "json_schema": json_schema,
                "args_json_schema": args_json_schema,
                "return_char_limit": return_char_limit,
                "pip_requirements": convert_and_respect_annotation_metadata(
                    object_=pip_requirements,
                    annotation=typing.Optional[typing.Sequence[PipRequirement]],
                    direction="write",
                ),
                "npm_requirements": convert_and_respect_annotation_metadata(
                    object_=npm_requirements,
                    annotation=typing.Optional[typing.Sequence[NpmRequirement]],
                    direction="write",
                ),
                "default_requires_approval": default_requires_approval,
                "enable_parallel_execution": enable_parallel_execution,
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
                    Tool,
                    parse_obj_as(
                        type_=Tool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def upsert_tool(
        self,
        *,
        source_code: str,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        args_json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        return_char_limit: typing.Optional[int] = OMIT,
        pip_requirements: typing.Optional[typing.Sequence[PipRequirement]] = OMIT,
        npm_requirements: typing.Optional[typing.Sequence[NpmRequirement]] = OMIT,
        default_requires_approval: typing.Optional[bool] = OMIT,
        enable_parallel_execution: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Tool]:
        """
        Create or update a tool

        Parameters
        ----------
        source_code : str
            The source code of the function.

        description : typing.Optional[str]
            The description of the tool.

        tags : typing.Optional[typing.Sequence[str]]
            Metadata tags.

        source_type : typing.Optional[str]
            The source type of the function.

        json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The JSON schema of the function (auto-generated from source_code if not provided)

        args_json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The args JSON schema of the function.

        return_char_limit : typing.Optional[int]
            The maximum number of characters in the response.

        pip_requirements : typing.Optional[typing.Sequence[PipRequirement]]
            Optional list of pip packages required by this tool.

        npm_requirements : typing.Optional[typing.Sequence[NpmRequirement]]
            Optional list of npm packages required by this tool.

        default_requires_approval : typing.Optional[bool]
            Whether or not to require approval before executing this tool.

        enable_parallel_execution : typing.Optional[bool]
            If set to True, then this tool will potentially be executed concurrently with other tools. Default False.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tool]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/",
            method="PUT",
            json={
                "description": description,
                "tags": tags,
                "source_code": source_code,
                "source_type": source_type,
                "json_schema": json_schema,
                "args_json_schema": args_json_schema,
                "return_char_limit": return_char_limit,
                "pip_requirements": convert_and_respect_annotation_metadata(
                    object_=pip_requirements,
                    annotation=typing.Optional[typing.Sequence[PipRequirement]],
                    direction="write",
                ),
                "npm_requirements": convert_and_respect_annotation_metadata(
                    object_=npm_requirements,
                    annotation=typing.Optional[typing.Sequence[NpmRequirement]],
                    direction="write",
                ),
                "default_requires_approval": default_requires_approval,
                "enable_parallel_execution": enable_parallel_execution,
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
                    Tool,
                    parse_obj_as(
                        type_=Tool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def search_tools(
        self,
        *,
        query: typing.Optional[str] = OMIT,
        search_mode: typing.Optional[ToolSearchRequestSearchMode] = OMIT,
        tool_types: typing.Optional[typing.Sequence[str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ToolSearchResult]]:
        """
        Search tools using semantic search.

        Requires tool embedding to be enabled (embed_tools=True). Uses vector search,
        full-text search, or hybrid mode to find tools matching the query.

        Returns tools ranked by relevance with their search scores.

        Parameters
        ----------
        query : typing.Optional[str]
            Text query for semantic search.

        search_mode : typing.Optional[ToolSearchRequestSearchMode]
            Search mode: vector, fts, or hybrid.

        tool_types : typing.Optional[typing.Sequence[str]]
            Filter by tool types (e.g., 'custom', 'letta_core').

        tags : typing.Optional[typing.Sequence[str]]
            Filter by tags (match any).

        limit : typing.Optional[int]
            Maximum number of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ToolSearchResult]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/search",
            method="POST",
            json={
                "query": query,
                "search_mode": search_mode,
                "tool_types": tool_types,
                "tags": tags,
                "limit": limit,
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
                    typing.List[ToolSearchResult],
                    parse_obj_as(
                        type_=typing.List[ToolSearchResult],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def add_base_tools(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Tool]]:
        """
        Upsert base tools

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Tool]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/add-base-tools",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Tool],
                    parse_obj_as(
                        type_=typing.List[Tool],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def run_tool_from_source(
        self,
        *,
        source_code: str,
        args: typing.Dict[str, typing.Any],
        env_vars: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        args_json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        json_schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        pip_requirements: typing.Optional[typing.Sequence[PipRequirement]] = OMIT,
        npm_requirements: typing.Optional[typing.Sequence[NpmRequirement]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ToolReturnMessage]:
        """
        Attempt to build a tool from source, then run it on the provided arguments

        Parameters
        ----------
        source_code : str
            The source code of the function.

        args : typing.Dict[str, typing.Any]
            The arguments to pass to the tool.

        env_vars : typing.Optional[typing.Dict[str, str]]
            The environment variables to pass to the tool.

        name : typing.Optional[str]
            The name of the tool to run.

        source_type : typing.Optional[str]
            The type of the source code.

        args_json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The args JSON schema of the function.

        json_schema : typing.Optional[typing.Dict[str, typing.Any]]
            The JSON schema of the function (auto-generated from source_code if not provided)

        pip_requirements : typing.Optional[typing.Sequence[PipRequirement]]
            Optional list of pip packages required by this tool.

        npm_requirements : typing.Optional[typing.Sequence[NpmRequirement]]
            Optional list of npm packages required by this tool.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ToolReturnMessage]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/run",
            method="POST",
            json={
                "source_code": source_code,
                "args": args,
                "env_vars": env_vars,
                "name": name,
                "source_type": source_type,
                "args_json_schema": args_json_schema,
                "json_schema": json_schema,
                "pip_requirements": convert_and_respect_annotation_metadata(
                    object_=pip_requirements,
                    annotation=typing.Optional[typing.Sequence[PipRequirement]],
                    direction="write",
                ),
                "npm_requirements": convert_and_respect_annotation_metadata(
                    object_=npm_requirements,
                    annotation=typing.Optional[typing.Sequence[NpmRequirement]],
                    direction="write",
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
                    ToolReturnMessage,
                    parse_obj_as(
                        type_=ToolReturnMessage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def list_mcp_servers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, ListMcpServersResponseValue]]:
        """
        Get a list of all configured MCP servers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, ListMcpServersResponseValue]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/mcp/servers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, ListMcpServersResponseValue],
                    parse_obj_as(
                        type_=typing.Dict[str, ListMcpServersResponseValue],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def add_mcp_server(
        self, *, request: AddMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[AddMcpServerResponseItem]]:
        """
        Add a new MCP server to the Letta MCP server config

        Parameters
        ----------
        request : AddMcpServerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AddMcpServerResponseItem]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/mcp/servers",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=AddMcpServerRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AddMcpServerResponseItem],
                    parse_obj_as(
                        type_=typing.List[AddMcpServerResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def list_mcp_tools_by_server(
        self, mcp_server_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[McpTool]]:
        """
        Get a list of all tools for a specific MCP server

        Parameters
        ----------
        mcp_server_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[McpTool]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}/tools",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[McpTool],
                    parse_obj_as(
                        type_=typing.List[McpTool],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def resync_mcp_server_tools(
        self,
        mcp_server_name: str,
        *,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Resync tools for an MCP server by:
        1. Fetching current tools from the MCP server
        2. Deleting tools that no longer exist on the server
        3. Updating schemas for existing tools
        4. Adding new tools from the server

        Returns a summary of changes made.

        Parameters
        ----------
        mcp_server_name : str

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}/resync",
            method="POST",
            params={
                "agent_id": agent_id,
            },
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def add_mcp_tool(
        self, mcp_server_name: str, mcp_tool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Tool]:
        """
        Register a new MCP tool as a Letta server by MCP server + tool name

        Parameters
        ----------
        mcp_server_name : str

        mcp_tool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tool]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}/{encode_path_param(mcp_tool_name)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tool,
                    parse_obj_as(
                        type_=Tool,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def delete_mcp_server(
        self, mcp_server_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[DeleteMcpServerResponseItem]]:
        """
        Delete a MCP server configuration

        Parameters
        ----------
        mcp_server_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[DeleteMcpServerResponseItem]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DeleteMcpServerResponseItem],
                    parse_obj_as(
                        type_=typing.List[DeleteMcpServerResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_mcp_server(
        self,
        mcp_server_name: str,
        *,
        request: UpdateMcpServerRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateMcpServerResponse]:
        """
        Update an existing MCP server configuration

        Parameters
        ----------
        mcp_server_name : str

        request : UpdateMcpServerRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateMcpServerResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateMcpServerRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateMcpServerResponse,
                    parse_obj_as(
                        type_=UpdateMcpServerResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def test_mcp_server(
        self, *, request: TestMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Test connection to an MCP server without adding it.
        Returns the list of available tools if successful.

        Parameters
        ----------
        request : TestMcpServerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/mcp/servers/test",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=TestMcpServerRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def connect_mcp_server(
        self, *, request: ConnectMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Connect to an MCP server with support for OAuth via SSE.
        Returns a stream of events handling authorization state and exchange if OAuth is required.

        Parameters
        ----------
        request : ConnectMcpServerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/mcp/servers/connect",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ConnectMcpServerRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def execute_mcp_tool(
        self,
        mcp_server_name: str,
        tool_name: str,
        *,
        args: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Execute a specific MCP tool from a configured server.
        Returns the tool execution result.

        Parameters
        ----------
        mcp_server_name : str

        tool_name : str

        args : typing.Optional[typing.Dict[str, typing.Any]]
            Arguments to pass to the tool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tools/mcp/servers/{encode_path_param(mcp_server_name)}/tools/{encode_path_param(tool_name)}/execute",
            method="POST",
            json={
                "args": args,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def mcp_oauth_callback(
        self,
        *,
        code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Handle OAuth callback for MCP server authentication.
        Session is identified via the state parameter instead of URL path.

        Parameters
        ----------
        code : typing.Optional[str]
            OAuth authorization code

        state : typing.Optional[str]
            OAuth state parameter

        error : typing.Optional[str]
            OAuth error

        error_description : typing.Optional[str]
            OAuth error description

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tools/mcp/oauth/callback",
            method="GET",
            params={
                "code": code,
                "state": state,
                "error": error,
                "error_description": error_description,
            },
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
