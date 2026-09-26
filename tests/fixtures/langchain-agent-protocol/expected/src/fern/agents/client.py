

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent import Agent
from ..types.agent_schema import AgentSchema
from .raw_client import AsyncRawAgentsClient, RawAgentsClient


OMIT = typing.cast(typing.Any, ...)


class AgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentsClient
        """
        return self._raw_client

    def search_agents(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Agent]:
        """
        List Agents available in this service.

        Parameters
        ----------
        name : typing.Optional[str]
            Name of the agent to search.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata of the agent to search.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Agent]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.agents.search_agents()
        """
        _response = self._raw_client.search_agents(
            name=name, metadata=metadata, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def get_agent(self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Agent:
        """
        Get an agent by ID.

        Parameters
        ----------
        agent_id : str
            The ID of the agent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.agents.get_agent(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.get_agent(agent_id, request_options=request_options)
        return _response.data

    def get_agent_schemas(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentSchema:
        """
        Get an agent's schemas by ID.

        Parameters
        ----------
        agent_id : str
            The ID of the agent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentSchema
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.agents.get_agent_schemas(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.get_agent_schemas(agent_id, request_options=request_options)
        return _response.data


class AsyncAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentsClient
        """
        return self._raw_client

    async def search_agents(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Agent]:
        """
        List Agents available in this service.

        Parameters
        ----------
        name : typing.Optional[str]
            Name of the agent to search.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata of the agent to search.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Agent]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.agents.search_agents()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_agents(
            name=name, metadata=metadata, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_agent(self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Agent:
        """
        Get an agent by ID.

        Parameters
        ----------
        agent_id : str
            The ID of the agent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Agent
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.agents.get_agent(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent(agent_id, request_options=request_options)
        return _response.data

    async def get_agent_schemas(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentSchema:
        """
        Get an agent's schemas by ID.

        Parameters
        ----------
        agent_id : str
            The ID of the agent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentSchema
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.agents.get_agent_schemas(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent_schemas(agent_id, request_options=request_options)
        return _response.data
