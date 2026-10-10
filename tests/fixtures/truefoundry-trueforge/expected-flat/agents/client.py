

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent_spec import AgentSpec
from ..types.delete_agent_response import DeleteAgentResponse
from ..types.get_agent_response import GetAgentResponse
from ..types.list_agents_response import ListAgentsResponse
from ..types.resource_name import ResourceName
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

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListAgentsResponse:
        """
        All configured agents for the tenant.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAgentsResponse
            All configured agents.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.agents.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def create(
        self, *, manifest: AgentSpec, name: ResourceName, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentResponse:
        """
        Creates an agent and allocates an immutable id. Fails if `name` is already taken. Name cannot be changed later.

        Parameters
        ----------
        manifest : AgentSpec

        name : ResourceName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponse
            The created agent.

        Examples
        --------
        from fern import AgentSpec, FernApi, Model

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.agents.create(
            manifest=AgentSpec(
                model=Model(
                    name="name",
                ),
            ),
            name="name",
        )
        """
        _response = self._raw_client.create(manifest=manifest, name=name, request_options=request_options)
        return _response.data

    def get(self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetAgentResponse:
        """
        Fetch a configured agent by immutable id.

        Parameters
        ----------
        agent_id : str
            Immutable agent identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponse
            The agent.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.agents.get(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.get(agent_id, request_options=request_options)
        return _response.data

    def update(
        self, agent_id: str, *, manifest: AgentSpec, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentResponse:
        """
        Replaces the manifest for an existing agent keyed by immutable `agent_id`.

        Parameters
        ----------
        agent_id : str
            Immutable agent identifier.

        manifest : AgentSpec

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponse
            The saved agent.

        Examples
        --------
        from fern import AgentSpec, FernApi, Model

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.agents.update(
            agent_id="agent_id",
            manifest=AgentSpec(
                model=Model(
                    name="name",
                ),
            ),
        )
        """
        _response = self._raw_client.update(agent_id, manifest=manifest, request_options=request_options)
        return _response.data

    def delete(self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteAgentResponse:
        """
        Delete a configured agent by immutable id. Idempotent if already gone.

        Parameters
        ----------
        agent_id : str
            Immutable agent identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAgentResponse
            Agent deleted.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.agents.delete(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.delete(agent_id, request_options=request_options)
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

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListAgentsResponse:
        """
        All configured agents for the tenant.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAgentsResponse
            All configured agents.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.agents.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def create(
        self, *, manifest: AgentSpec, name: ResourceName, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentResponse:
        """
        Creates an agent and allocates an immutable id. Fails if `name` is already taken. Name cannot be changed later.

        Parameters
        ----------
        manifest : AgentSpec

        name : ResourceName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponse
            The created agent.

        Examples
        --------
        import asyncio

        from fern import AgentSpec, AsyncFernApi, Model

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.agents.create(
                manifest=AgentSpec(
                    model=Model(
                        name="name",
                    ),
                ),
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(manifest=manifest, name=name, request_options=request_options)
        return _response.data

    async def get(self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetAgentResponse:
        """
        Fetch a configured agent by immutable id.

        Parameters
        ----------
        agent_id : str
            Immutable agent identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponse
            The agent.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.agents.get(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(agent_id, request_options=request_options)
        return _response.data

    async def update(
        self, agent_id: str, *, manifest: AgentSpec, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentResponse:
        """
        Replaces the manifest for an existing agent keyed by immutable `agent_id`.

        Parameters
        ----------
        agent_id : str
            Immutable agent identifier.

        manifest : AgentSpec

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponse
            The saved agent.

        Examples
        --------
        import asyncio

        from fern import AgentSpec, AsyncFernApi, Model

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.agents.update(
                agent_id="agent_id",
                manifest=AgentSpec(
                    model=Model(
                        name="name",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(agent_id, manifest=manifest, request_options=request_options)
        return _response.data

    async def delete(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAgentResponse:
        """
        Delete a configured agent by immutable id. Idempotent if already gone.

        Parameters
        ----------
        agent_id : str
            Immutable agent identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAgentResponse
            Agent deleted.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.agents.delete(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(agent_id, request_options=request_options)
        return _response.data
