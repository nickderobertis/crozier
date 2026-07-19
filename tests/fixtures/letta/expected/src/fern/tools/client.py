

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.mcp_tool import McpTool
from ..types.npm_requirement import NpmRequirement
from ..types.pip_requirement import PipRequirement
from ..types.tool import Tool
from ..types.tool_return_message import ToolReturnMessage
from ..types.tool_search_result import ToolSearchResult
from .raw_client import AsyncRawToolsClient, RawToolsClient
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


OMIT = typing.cast(typing.Any, ...)


class ToolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawToolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawToolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawToolsClient
        """
        return self._raw_client

    def retrieve_tool(self, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Tool:
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
        Tool
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.retrieve_tool(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_tool(tool_id, request_options=request_options)
        return _response.data

    def delete_tool(self, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.delete_tool(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_tool(tool_id, request_options=request_options)
        return _response.data

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
    ) -> Tool:
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
        Tool
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.modify_tool(
            tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.modify_tool(
            tool_id,
            description=description,
            tags=tags,
            source_code=source_code,
            source_type=source_type,
            json_schema=json_schema,
            args_json_schema=args_json_schema,
            return_char_limit=return_char_limit,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            metadata=metadata,
            default_requires_approval=default_requires_approval,
            enable_parallel_execution=enable_parallel_execution,
            request_options=request_options,
        )
        return _response.data

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
    ) -> int:
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
        int
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.count_tools()
        """
        _response = self._raw_client.count_tools(
            name=name,
            names=names,
            tool_ids=tool_ids,
            search=search,
            tool_types=tool_types,
            exclude_tool_types=exclude_tool_types,
            return_only_letta_tools=return_only_letta_tools,
            exclude_letta_tools=exclude_letta_tools,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[Tool]:
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
        typing.List[Tool]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.list_tools()
        """
        _response = self._raw_client.list_tools(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            name=name,
            names=names,
            tool_ids=tool_ids,
            search=search,
            tool_types=tool_types,
            exclude_tool_types=exclude_tool_types,
            return_only_letta_tools=return_only_letta_tools,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Tool:
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
        Tool
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.create_tool(
            source_code="source_code",
        )
        """
        _response = self._raw_client.create_tool(
            source_code=source_code,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            args_json_schema=args_json_schema,
            return_char_limit=return_char_limit,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            default_requires_approval=default_requires_approval,
            enable_parallel_execution=enable_parallel_execution,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Tool:
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
        Tool
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.upsert_tool(
            source_code="source_code",
        )
        """
        _response = self._raw_client.upsert_tool(
            source_code=source_code,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            args_json_schema=args_json_schema,
            return_char_limit=return_char_limit,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            default_requires_approval=default_requires_approval,
            enable_parallel_execution=enable_parallel_execution,
            request_options=request_options,
        )
        return _response.data

    def search_tools(
        self,
        *,
        query: typing.Optional[str] = OMIT,
        search_mode: typing.Optional[ToolSearchRequestSearchMode] = OMIT,
        tool_types: typing.Optional[typing.Sequence[str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ToolSearchResult]:
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
        typing.List[ToolSearchResult]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.search_tools()
        """
        _response = self._raw_client.search_tools(
            query=query,
            search_mode=search_mode,
            tool_types=tool_types,
            tags=tags,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def add_base_tools(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Tool]:
        """
        Upsert base tools

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tool]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.add_base_tools()
        """
        _response = self._raw_client.add_base_tools(request_options=request_options)
        return _response.data

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
    ) -> ToolReturnMessage:
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
        ToolReturnMessage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.run_tool_from_source(
            source_code="source_code",
            args={"key": "value"},
        )
        """
        _response = self._raw_client.run_tool_from_source(
            source_code=source_code,
            args=args,
            env_vars=env_vars,
            name=name,
            source_type=source_type,
            args_json_schema=args_json_schema,
            json_schema=json_schema,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            request_options=request_options,
        )
        return _response.data

    def list_mcp_servers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, ListMcpServersResponseValue]:
        """
        Get a list of all configured MCP servers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ListMcpServersResponseValue]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.list_mcp_servers()
        """
        _response = self._raw_client.list_mcp_servers(request_options=request_options)
        return _response.data

    def add_mcp_server(
        self, *, request: AddMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AddMcpServerResponseItem]:
        """
        Add a new MCP server to the Letta MCP server config

        Parameters
        ----------
        request : AddMcpServerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AddMcpServerResponseItem]
            Successful Response

        Examples
        --------
        from fern import FernApi, StdioServerConfig

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.add_mcp_server(
            request=StdioServerConfig(
                server_name="server_name",
                command="command",
                args=["args"],
            ),
        )
        """
        _response = self._raw_client.add_mcp_server(request=request, request_options=request_options)
        return _response.data

    def list_mcp_tools_by_server(
        self, mcp_server_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[McpTool]:
        """
        Get a list of all tools for a specific MCP server

        Parameters
        ----------
        mcp_server_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[McpTool]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.list_mcp_tools_by_server(
            mcp_server_name="mcp_server_name",
        )
        """
        _response = self._raw_client.list_mcp_tools_by_server(mcp_server_name, request_options=request_options)
        return _response.data

    def resync_mcp_server_tools(
        self,
        mcp_server_name: str,
        *,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.resync_mcp_server_tools(
            mcp_server_name="mcp_server_name",
        )
        """
        _response = self._raw_client.resync_mcp_server_tools(
            mcp_server_name, agent_id=agent_id, request_options=request_options
        )
        return _response.data

    def add_mcp_tool(
        self, mcp_server_name: str, mcp_tool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tool:
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
        Tool
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.add_mcp_tool(
            mcp_server_name="mcp_server_name",
            mcp_tool_name="mcp_tool_name",
        )
        """
        _response = self._raw_client.add_mcp_tool(mcp_server_name, mcp_tool_name, request_options=request_options)
        return _response.data

    def delete_mcp_server(
        self, mcp_server_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeleteMcpServerResponseItem]:
        """
        Delete a MCP server configuration

        Parameters
        ----------
        mcp_server_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeleteMcpServerResponseItem]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.delete_mcp_server(
            mcp_server_name="mcp_server_name",
        )
        """
        _response = self._raw_client.delete_mcp_server(mcp_server_name, request_options=request_options)
        return _response.data

    def update_mcp_server(
        self,
        mcp_server_name: str,
        *,
        request: UpdateMcpServerRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateMcpServerResponse:
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
        UpdateMcpServerResponse
            Successful Response

        Examples
        --------
        from fern import FernApi, LettaSchemasMcpUpdateStdioMcpServer

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.update_mcp_server(
            mcp_server_name="mcp_server_name",
            request=LettaSchemasMcpUpdateStdioMcpServer(),
        )
        """
        _response = self._raw_client.update_mcp_server(
            mcp_server_name, request=request, request_options=request_options
        )
        return _response.data

    def test_mcp_server(
        self, *, request: TestMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, StdioServerConfig

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.test_mcp_server(
            request=StdioServerConfig(
                server_name="server_name",
                command="command",
                args=["args"],
            ),
        )
        """
        _response = self._raw_client.test_mcp_server(request=request, request_options=request_options)
        return _response.data

    def connect_mcp_server(
        self, *, request: ConnectMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi, StdioServerConfig

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.connect_mcp_server(
            request=StdioServerConfig(
                server_name="server_name",
                command="command",
                args=["args"],
            ),
        )
        """
        _response = self._raw_client.connect_mcp_server(request=request, request_options=request_options)
        return _response.data

    def execute_mcp_tool(
        self,
        mcp_server_name: str,
        tool_name: str,
        *,
        args: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.execute_mcp_tool(
            mcp_server_name="mcp_server_name",
            tool_name="tool_name",
        )
        """
        _response = self._raw_client.execute_mcp_tool(
            mcp_server_name, tool_name, args=args, request_options=request_options
        )
        return _response.data

    def mcp_oauth_callback(
        self,
        *,
        code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tools.mcp_oauth_callback()
        """
        _response = self._raw_client.mcp_oauth_callback(
            code=code, state=state, error=error, error_description=error_description, request_options=request_options
        )
        return _response.data


class AsyncToolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawToolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawToolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawToolsClient
        """
        return self._raw_client

    async def retrieve_tool(self, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Tool:
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
        Tool
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.retrieve_tool(
                tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_tool(tool_id, request_options=request_options)
        return _response.data

    async def delete_tool(self, tool_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.delete_tool(
                tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_tool(tool_id, request_options=request_options)
        return _response.data

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
    ) -> Tool:
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
        Tool
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.modify_tool(
                tool_id="tool-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_tool(
            tool_id,
            description=description,
            tags=tags,
            source_code=source_code,
            source_type=source_type,
            json_schema=json_schema,
            args_json_schema=args_json_schema,
            return_char_limit=return_char_limit,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            metadata=metadata,
            default_requires_approval=default_requires_approval,
            enable_parallel_execution=enable_parallel_execution,
            request_options=request_options,
        )
        return _response.data

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
    ) -> int:
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
        int
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.count_tools()


        asyncio.run(main())
        """
        _response = await self._raw_client.count_tools(
            name=name,
            names=names,
            tool_ids=tool_ids,
            search=search,
            tool_types=tool_types,
            exclude_tool_types=exclude_tool_types,
            return_only_letta_tools=return_only_letta_tools,
            exclude_letta_tools=exclude_letta_tools,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.List[Tool]:
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
        typing.List[Tool]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.list_tools()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tools(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            name=name,
            names=names,
            tool_ids=tool_ids,
            search=search,
            tool_types=tool_types,
            exclude_tool_types=exclude_tool_types,
            return_only_letta_tools=return_only_letta_tools,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Tool:
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
        Tool
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.create_tool(
                source_code="source_code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_tool(
            source_code=source_code,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            args_json_schema=args_json_schema,
            return_char_limit=return_char_limit,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            default_requires_approval=default_requires_approval,
            enable_parallel_execution=enable_parallel_execution,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Tool:
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
        Tool
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.upsert_tool(
                source_code="source_code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_tool(
            source_code=source_code,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            args_json_schema=args_json_schema,
            return_char_limit=return_char_limit,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            default_requires_approval=default_requires_approval,
            enable_parallel_execution=enable_parallel_execution,
            request_options=request_options,
        )
        return _response.data

    async def search_tools(
        self,
        *,
        query: typing.Optional[str] = OMIT,
        search_mode: typing.Optional[ToolSearchRequestSearchMode] = OMIT,
        tool_types: typing.Optional[typing.Sequence[str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ToolSearchResult]:
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
        typing.List[ToolSearchResult]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.search_tools()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_tools(
            query=query,
            search_mode=search_mode,
            tool_types=tool_types,
            tags=tags,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def add_base_tools(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Tool]:
        """
        Upsert base tools

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tool]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.add_base_tools()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_base_tools(request_options=request_options)
        return _response.data

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
    ) -> ToolReturnMessage:
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
        ToolReturnMessage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.run_tool_from_source(
                source_code="source_code",
                args={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_tool_from_source(
            source_code=source_code,
            args=args,
            env_vars=env_vars,
            name=name,
            source_type=source_type,
            args_json_schema=args_json_schema,
            json_schema=json_schema,
            pip_requirements=pip_requirements,
            npm_requirements=npm_requirements,
            request_options=request_options,
        )
        return _response.data

    async def list_mcp_servers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, ListMcpServersResponseValue]:
        """
        Get a list of all configured MCP servers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ListMcpServersResponseValue]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.list_mcp_servers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_mcp_servers(request_options=request_options)
        return _response.data

    async def add_mcp_server(
        self, *, request: AddMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AddMcpServerResponseItem]:
        """
        Add a new MCP server to the Letta MCP server config

        Parameters
        ----------
        request : AddMcpServerRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AddMcpServerResponseItem]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, StdioServerConfig

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.add_mcp_server(
                request=StdioServerConfig(
                    server_name="server_name",
                    command="command",
                    args=["args"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_mcp_server(request=request, request_options=request_options)
        return _response.data

    async def list_mcp_tools_by_server(
        self, mcp_server_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[McpTool]:
        """
        Get a list of all tools for a specific MCP server

        Parameters
        ----------
        mcp_server_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[McpTool]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.list_mcp_tools_by_server(
                mcp_server_name="mcp_server_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_mcp_tools_by_server(mcp_server_name, request_options=request_options)
        return _response.data

    async def resync_mcp_server_tools(
        self,
        mcp_server_name: str,
        *,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.resync_mcp_server_tools(
                mcp_server_name="mcp_server_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resync_mcp_server_tools(
            mcp_server_name, agent_id=agent_id, request_options=request_options
        )
        return _response.data

    async def add_mcp_tool(
        self, mcp_server_name: str, mcp_tool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Tool:
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
        Tool
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.add_mcp_tool(
                mcp_server_name="mcp_server_name",
                mcp_tool_name="mcp_tool_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_mcp_tool(mcp_server_name, mcp_tool_name, request_options=request_options)
        return _response.data

    async def delete_mcp_server(
        self, mcp_server_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeleteMcpServerResponseItem]:
        """
        Delete a MCP server configuration

        Parameters
        ----------
        mcp_server_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeleteMcpServerResponseItem]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.delete_mcp_server(
                mcp_server_name="mcp_server_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_mcp_server(mcp_server_name, request_options=request_options)
        return _response.data

    async def update_mcp_server(
        self,
        mcp_server_name: str,
        *,
        request: UpdateMcpServerRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateMcpServerResponse:
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
        UpdateMcpServerResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LettaSchemasMcpUpdateStdioMcpServer

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.update_mcp_server(
                mcp_server_name="mcp_server_name",
                request=LettaSchemasMcpUpdateStdioMcpServer(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_mcp_server(
            mcp_server_name, request=request, request_options=request_options
        )
        return _response.data

    async def test_mcp_server(
        self, *, request: TestMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, StdioServerConfig

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.test_mcp_server(
                request=StdioServerConfig(
                    server_name="server_name",
                    command="command",
                    args=["args"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.test_mcp_server(request=request, request_options=request_options)
        return _response.data

    async def connect_mcp_server(
        self, *, request: ConnectMcpServerRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, StdioServerConfig

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.connect_mcp_server(
                request=StdioServerConfig(
                    server_name="server_name",
                    command="command",
                    args=["args"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connect_mcp_server(request=request, request_options=request_options)
        return _response.data

    async def execute_mcp_tool(
        self,
        mcp_server_name: str,
        tool_name: str,
        *,
        args: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.execute_mcp_tool(
                mcp_server_name="mcp_server_name",
                tool_name="tool_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_mcp_tool(
            mcp_server_name, tool_name, args=args, request_options=request_options
        )
        return _response.data

    async def mcp_oauth_callback(
        self,
        *,
        code: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tools.mcp_oauth_callback()


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp_oauth_callback(
            code=code, state=state, error=error, error_description=error_description, request_options=request_options
        )
        return _response.data
