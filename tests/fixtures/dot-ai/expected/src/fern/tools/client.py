

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tools_get_response import ToolsGetResponse
from ..types.tools_tool_name_post_request import ToolsToolNamePostRequest
from ..types.tools_tool_name_post_response import ToolsToolNamePostResponse
from .raw_client import AsyncRawToolsClient, RawToolsClient


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

    def discover_available_tools_with_optional_filtering_by_category_tag_or_search_term(
        self,
        *,
        category: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolsGetResponse:
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
        ToolsGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tools.discover_available_tools_with_optional_filtering_by_category_tag_or_search_term()
        """
        _response = self._raw_client.discover_available_tools_with_optional_filtering_by_category_tag_or_search_term(
            category=category, tag=tag, search=search, request_options=request_options
        )
        return _response.data

    def execute_a_tool_with_the_provided_parameters(
        self,
        tool_name: str,
        *,
        request: ToolsToolNamePostRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolsToolNamePostResponse:
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
        ToolsToolNamePostResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tools.execute_a_tool_with_the_provided_parameters(
            tool_name="toolName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.execute_a_tool_with_the_provided_parameters(
            tool_name, request=request, request_options=request_options
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

    async def discover_available_tools_with_optional_filtering_by_category_tag_or_search_term(
        self,
        *,
        category: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolsGetResponse:
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
        ToolsGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tools.discover_available_tools_with_optional_filtering_by_category_tag_or_search_term()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.discover_available_tools_with_optional_filtering_by_category_tag_or_search_term(
                category=category, tag=tag, search=search, request_options=request_options
            )
        )
        return _response.data

    async def execute_a_tool_with_the_provided_parameters(
        self,
        tool_name: str,
        *,
        request: ToolsToolNamePostRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolsToolNamePostResponse:
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
        ToolsToolNamePostResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tools.execute_a_tool_with_the_provided_parameters(
                tool_name="toolName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_a_tool_with_the_provided_parameters(
            tool_name, request=request, request_options=request_options
        )
        return _response.data
