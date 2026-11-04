

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAgentToolsClient, RawAgentToolsClient
from .types.create_agent_tool_request_tool_type import CreateAgentToolRequestToolType
from .types.create_agent_tool_response import CreateAgentToolResponse
from .types.delete_agent_tool_response import DeleteAgentToolResponse
from .types.get_agent_tool_response import GetAgentToolResponse
from .types.list_agent_tools_response import ListAgentToolsResponse
from .types.update_agent_tool_response import UpdateAgentToolResponse


OMIT = typing.cast(typing.Any, ...)


class AgentToolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentToolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentToolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentToolsClient
        """
        return self._raw_client

    def list_agent_tools(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAgentToolsResponse:
        """
        List all tools for an agent

        Parameters
        ----------
        agent_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAgentToolsResponse
            List of tools

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_tools.list_agent_tools(
            agent_uuid="agent_uuid",
        )
        """
        _response = self._raw_client.list_agent_tools(agent_uuid, request_options=request_options)
        return _response.data

    def create_agent_tool(
        self,
        agent_uuid: str,
        *,
        name: str,
        description: str,
        tool_type: CreateAgentToolRequestToolType,
        tool_config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAgentToolResponse:
        """
        Create a new tool for an agent

        Parameters
        ----------
        agent_uuid : str

        name : str

        description : str

        tool_type : CreateAgentToolRequestToolType

        tool_config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentToolResponse
            Tool created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_tools.create_agent_tool(
            agent_uuid="agent_uuid",
            name="name",
            description="description",
            tool_type="webhook",
            tool_config={"key": "value"},
        )
        """
        _response = self._raw_client.create_agent_tool(
            agent_uuid,
            name=name,
            description=description,
            tool_type=tool_type,
            tool_config=tool_config,
            request_options=request_options,
        )
        return _response.data

    def get_agent_tool(
        self, agent_uuid: str, tool_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentToolResponse:
        """
        Get details of a specific tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentToolResponse
            Tool details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_tools.get_agent_tool(
            agent_uuid="agent_uuid",
            tool_uuid="tool_uuid",
        )
        """
        _response = self._raw_client.get_agent_tool(agent_uuid, tool_uuid, request_options=request_options)
        return _response.data

    def delete_agent_tool(
        self, agent_uuid: str, tool_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAgentToolResponse:
        """
        Delete a tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAgentToolResponse
            Tool deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_tools.delete_agent_tool(
            agent_uuid="agent_uuid",
            tool_uuid="tool_uuid",
        )
        """
        _response = self._raw_client.delete_agent_tool(agent_uuid, tool_uuid, request_options=request_options)
        return _response.data

    def update_agent_tool(
        self,
        agent_uuid: str,
        tool_uuid: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tool_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAgentToolResponse:
        """
        Update an existing tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        tool_config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAgentToolResponse
            Tool updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_tools.update_agent_tool(
            agent_uuid="agent_uuid",
            tool_uuid="tool_uuid",
        )
        """
        _response = self._raw_client.update_agent_tool(
            agent_uuid,
            tool_uuid,
            name=name,
            description=description,
            tool_config=tool_config,
            request_options=request_options,
        )
        return _response.data


class AsyncAgentToolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentToolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentToolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentToolsClient
        """
        return self._raw_client

    async def list_agent_tools(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAgentToolsResponse:
        """
        List all tools for an agent

        Parameters
        ----------
        agent_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAgentToolsResponse
            List of tools

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_tools.list_agent_tools(
                agent_uuid="agent_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_agent_tools(agent_uuid, request_options=request_options)
        return _response.data

    async def create_agent_tool(
        self,
        agent_uuid: str,
        *,
        name: str,
        description: str,
        tool_type: CreateAgentToolRequestToolType,
        tool_config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAgentToolResponse:
        """
        Create a new tool for an agent

        Parameters
        ----------
        agent_uuid : str

        name : str

        description : str

        tool_type : CreateAgentToolRequestToolType

        tool_config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentToolResponse
            Tool created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_tools.create_agent_tool(
                agent_uuid="agent_uuid",
                name="name",
                description="description",
                tool_type="webhook",
                tool_config={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_agent_tool(
            agent_uuid,
            name=name,
            description=description,
            tool_type=tool_type,
            tool_config=tool_config,
            request_options=request_options,
        )
        return _response.data

    async def get_agent_tool(
        self, agent_uuid: str, tool_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentToolResponse:
        """
        Get details of a specific tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentToolResponse
            Tool details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_tools.get_agent_tool(
                agent_uuid="agent_uuid",
                tool_uuid="tool_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent_tool(agent_uuid, tool_uuid, request_options=request_options)
        return _response.data

    async def delete_agent_tool(
        self, agent_uuid: str, tool_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAgentToolResponse:
        """
        Delete a tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAgentToolResponse
            Tool deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_tools.delete_agent_tool(
                agent_uuid="agent_uuid",
                tool_uuid="tool_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_agent_tool(agent_uuid, tool_uuid, request_options=request_options)
        return _response.data

    async def update_agent_tool(
        self,
        agent_uuid: str,
        tool_uuid: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tool_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAgentToolResponse:
        """
        Update an existing tool

        Parameters
        ----------
        agent_uuid : str

        tool_uuid : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        tool_config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAgentToolResponse
            Tool updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_tools.update_agent_tool(
                agent_uuid="agent_uuid",
                tool_uuid="tool_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_agent_tool(
            agent_uuid,
            tool_uuid,
            name=name,
            description=description,
            tool_config=tool_config,
            request_options=request_options,
        )
        return _response.data
