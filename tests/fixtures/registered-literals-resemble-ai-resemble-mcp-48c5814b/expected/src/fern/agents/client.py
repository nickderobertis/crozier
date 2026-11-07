

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAgentsClient, RawAgentsClient
from .types.create_agent_request_asr import CreateAgentRequestAsr
from .types.create_agent_request_dynamic_variables_value import CreateAgentRequestDynamicVariablesValue
from .types.create_agent_request_llm import CreateAgentRequestLlm
from .types.create_agent_request_search_mode import CreateAgentRequestSearchMode
from .types.create_agent_request_turn import CreateAgentRequestTurn
from .types.create_agent_response import CreateAgentResponse
from .types.delete_agent_response import DeleteAgentResponse
from .types.dispatch_agent_response import DispatchAgentResponse
from .types.get_agent_capabilities_response import GetAgentCapabilitiesResponse
from .types.get_agent_response import GetAgentResponse
from .types.get_system_tools_response import GetSystemToolsResponse
from .types.list_agents_response import ListAgentsResponse
from .types.update_agent_request_search_mode import UpdateAgentRequestSearchMode
from .types.update_agent_response import UpdateAgentResponse


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

    def list_agents(
        self,
        *,
        phone_number: typing.Optional[str] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAgentsResponse:
        """
        Retrieve all agents for the authenticated team

        Parameters
        ----------
        phone_number : typing.Optional[str]
            Filter by associated phone number

        advanced : typing.Optional[bool]
            Include detailed configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAgentsResponse
            List of agents

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agents.list_agents()
        """
        _response = self._raw_client.list_agents(
            phone_number=phone_number, advanced=advanced, request_options=request_options
        )
        return _response.data

    def create_agent(
        self,
        *,
        name: str,
        voice_uuid: str,
        phone_number_id: typing.Optional[int] = OMIT,
        languages: typing.Optional[typing.Sequence[str]] = OMIT,
        dynamic_variables: typing.Optional[typing.Dict[str, CreateAgentRequestDynamicVariablesValue]] = OMIT,
        asr: typing.Optional[CreateAgentRequestAsr] = OMIT,
        turn: typing.Optional[CreateAgentRequestTurn] = OMIT,
        llm: typing.Optional[CreateAgentRequestLlm] = OMIT,
        search_mode: typing.Optional[CreateAgentRequestSearchMode] = OMIT,
        max_chunks_per_query: typing.Optional[int] = OMIT,
        webhooks: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        system_tools: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAgentResponse:
        """
        Create a new voice agent

        Parameters
        ----------
        name : str

        voice_uuid : str

        phone_number_id : typing.Optional[int]

        languages : typing.Optional[typing.Sequence[str]]

        dynamic_variables : typing.Optional[typing.Dict[str, CreateAgentRequestDynamicVariablesValue]]

        asr : typing.Optional[CreateAgentRequestAsr]

        turn : typing.Optional[CreateAgentRequestTurn]

        llm : typing.Optional[CreateAgentRequestLlm]

        search_mode : typing.Optional[CreateAgentRequestSearchMode]
            RAG search strategy - speed (faster) or accuracy (more thorough)

        max_chunks_per_query : typing.Optional[int]
            Number of relevant chunks to retrieve per query for RAG

        webhooks : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        system_tools : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentResponse
            Agent created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agents.create_agent(
            name="name",
            voice_uuid="voice_uuid",
        )
        """
        _response = self._raw_client.create_agent(
            name=name,
            voice_uuid=voice_uuid,
            phone_number_id=phone_number_id,
            languages=languages,
            dynamic_variables=dynamic_variables,
            asr=asr,
            turn=turn,
            llm=llm,
            search_mode=search_mode,
            max_chunks_per_query=max_chunks_per_query,
            webhooks=webhooks,
            system_tools=system_tools,
            request_options=request_options,
        )
        return _response.data

    def get_agent(
        self,
        uuid_: str,
        *,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAgentResponse:
        """
        Retrieve a specific agent's details

        Parameters
        ----------
        uuid_ : str

        advanced : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponse
            Agent details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agents.get_agent(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_agent(uuid_, advanced=advanced, request_options=request_options)
        return _response.data

    def delete_agent(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAgentResponse:
        """
        Delete an agent and all its configurations

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAgentResponse
            Agent deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agents.delete_agent(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.delete_agent(uuid_, request_options=request_options)
        return _response.data

    def update_agent(
        self,
        uuid_: str,
        *,
        name: typing.Optional[str] = OMIT,
        voice_uuid: typing.Optional[str] = OMIT,
        phone_number_id: typing.Optional[int] = OMIT,
        languages: typing.Optional[typing.Sequence[str]] = OMIT,
        dynamic_variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        asr: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        turn: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        search_mode: typing.Optional[UpdateAgentRequestSearchMode] = OMIT,
        max_chunks_per_query: typing.Optional[int] = OMIT,
        webhooks: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        system_tools: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAgentResponse:
        """
        Update an existing agent's configuration

        Parameters
        ----------
        uuid_ : str

        name : typing.Optional[str]

        voice_uuid : typing.Optional[str]

        phone_number_id : typing.Optional[int]

        languages : typing.Optional[typing.Sequence[str]]

        dynamic_variables : typing.Optional[typing.Dict[str, typing.Any]]

        asr : typing.Optional[typing.Dict[str, typing.Any]]

        turn : typing.Optional[typing.Dict[str, typing.Any]]

        llm : typing.Optional[typing.Dict[str, typing.Any]]

        search_mode : typing.Optional[UpdateAgentRequestSearchMode]
            RAG search strategy

        max_chunks_per_query : typing.Optional[int]
            Number of chunks to retrieve per query for RAG

        webhooks : typing.Optional[typing.Sequence[typing.Any]]

        system_tools : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAgentResponse
            Agent updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agents.update_agent(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.update_agent(
            uuid_,
            name=name,
            voice_uuid=voice_uuid,
            phone_number_id=phone_number_id,
            languages=languages,
            dynamic_variables=dynamic_variables,
            asr=asr,
            turn=turn,
            llm=llm,
            search_mode=search_mode,
            max_chunks_per_query=max_chunks_per_query,
            webhooks=webhooks,
            system_tools=system_tools,
            request_options=request_options,
        )
        return _response.data

    def dispatch_agent(
        self,
        uuid_: str,
        *,
        phone_number: str,
        dynamic_variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DispatchAgentResponse:
        """
        Make an outbound call with an agent

        Parameters
        ----------
        uuid_ : str

        phone_number : str
            Destination phone number

        dynamic_variables : typing.Optional[typing.Dict[str, typing.Any]]
            Runtime variable overrides

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DispatchAgentResponse
            Call dispatched

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agents.dispatch_agent(
            uuid_="uuid",
            phone_number="phone_number",
        )
        """
        _response = self._raw_client.dispatch_agent(
            uuid_, phone_number=phone_number, dynamic_variables=dynamic_variables, request_options=request_options
        )
        return _response.data

    def get_agent_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentCapabilitiesResponse:
        """
        List supported ASR and LLM providers and models

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentCapabilitiesResponse
            Agent capabilities

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agents.get_agent_capabilities()
        """
        _response = self._raw_client.get_agent_capabilities(request_options=request_options)
        return _response.data

    def get_system_tools(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetSystemToolsResponse:
        """
        List available system tools

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSystemToolsResponse
            System tools

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agents.get_system_tools()
        """
        _response = self._raw_client.get_system_tools(request_options=request_options)
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

    async def list_agents(
        self,
        *,
        phone_number: typing.Optional[str] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAgentsResponse:
        """
        Retrieve all agents for the authenticated team

        Parameters
        ----------
        phone_number : typing.Optional[str]
            Filter by associated phone number

        advanced : typing.Optional[bool]
            Include detailed configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAgentsResponse
            List of agents

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.list_agents()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_agents(
            phone_number=phone_number, advanced=advanced, request_options=request_options
        )
        return _response.data

    async def create_agent(
        self,
        *,
        name: str,
        voice_uuid: str,
        phone_number_id: typing.Optional[int] = OMIT,
        languages: typing.Optional[typing.Sequence[str]] = OMIT,
        dynamic_variables: typing.Optional[typing.Dict[str, CreateAgentRequestDynamicVariablesValue]] = OMIT,
        asr: typing.Optional[CreateAgentRequestAsr] = OMIT,
        turn: typing.Optional[CreateAgentRequestTurn] = OMIT,
        llm: typing.Optional[CreateAgentRequestLlm] = OMIT,
        search_mode: typing.Optional[CreateAgentRequestSearchMode] = OMIT,
        max_chunks_per_query: typing.Optional[int] = OMIT,
        webhooks: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        system_tools: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAgentResponse:
        """
        Create a new voice agent

        Parameters
        ----------
        name : str

        voice_uuid : str

        phone_number_id : typing.Optional[int]

        languages : typing.Optional[typing.Sequence[str]]

        dynamic_variables : typing.Optional[typing.Dict[str, CreateAgentRequestDynamicVariablesValue]]

        asr : typing.Optional[CreateAgentRequestAsr]

        turn : typing.Optional[CreateAgentRequestTurn]

        llm : typing.Optional[CreateAgentRequestLlm]

        search_mode : typing.Optional[CreateAgentRequestSearchMode]
            RAG search strategy - speed (faster) or accuracy (more thorough)

        max_chunks_per_query : typing.Optional[int]
            Number of relevant chunks to retrieve per query for RAG

        webhooks : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        system_tools : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentResponse
            Agent created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.create_agent(
                name="name",
                voice_uuid="voice_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_agent(
            name=name,
            voice_uuid=voice_uuid,
            phone_number_id=phone_number_id,
            languages=languages,
            dynamic_variables=dynamic_variables,
            asr=asr,
            turn=turn,
            llm=llm,
            search_mode=search_mode,
            max_chunks_per_query=max_chunks_per_query,
            webhooks=webhooks,
            system_tools=system_tools,
            request_options=request_options,
        )
        return _response.data

    async def get_agent(
        self,
        uuid_: str,
        *,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAgentResponse:
        """
        Retrieve a specific agent's details

        Parameters
        ----------
        uuid_ : str

        advanced : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponse
            Agent details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.get_agent(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent(uuid_, advanced=advanced, request_options=request_options)
        return _response.data

    async def delete_agent(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAgentResponse:
        """
        Delete an agent and all its configurations

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAgentResponse
            Agent deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.delete_agent(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_agent(uuid_, request_options=request_options)
        return _response.data

    async def update_agent(
        self,
        uuid_: str,
        *,
        name: typing.Optional[str] = OMIT,
        voice_uuid: typing.Optional[str] = OMIT,
        phone_number_id: typing.Optional[int] = OMIT,
        languages: typing.Optional[typing.Sequence[str]] = OMIT,
        dynamic_variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        asr: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        turn: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        search_mode: typing.Optional[UpdateAgentRequestSearchMode] = OMIT,
        max_chunks_per_query: typing.Optional[int] = OMIT,
        webhooks: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        system_tools: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAgentResponse:
        """
        Update an existing agent's configuration

        Parameters
        ----------
        uuid_ : str

        name : typing.Optional[str]

        voice_uuid : typing.Optional[str]

        phone_number_id : typing.Optional[int]

        languages : typing.Optional[typing.Sequence[str]]

        dynamic_variables : typing.Optional[typing.Dict[str, typing.Any]]

        asr : typing.Optional[typing.Dict[str, typing.Any]]

        turn : typing.Optional[typing.Dict[str, typing.Any]]

        llm : typing.Optional[typing.Dict[str, typing.Any]]

        search_mode : typing.Optional[UpdateAgentRequestSearchMode]
            RAG search strategy

        max_chunks_per_query : typing.Optional[int]
            Number of chunks to retrieve per query for RAG

        webhooks : typing.Optional[typing.Sequence[typing.Any]]

        system_tools : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAgentResponse
            Agent updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.update_agent(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_agent(
            uuid_,
            name=name,
            voice_uuid=voice_uuid,
            phone_number_id=phone_number_id,
            languages=languages,
            dynamic_variables=dynamic_variables,
            asr=asr,
            turn=turn,
            llm=llm,
            search_mode=search_mode,
            max_chunks_per_query=max_chunks_per_query,
            webhooks=webhooks,
            system_tools=system_tools,
            request_options=request_options,
        )
        return _response.data

    async def dispatch_agent(
        self,
        uuid_: str,
        *,
        phone_number: str,
        dynamic_variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DispatchAgentResponse:
        """
        Make an outbound call with an agent

        Parameters
        ----------
        uuid_ : str

        phone_number : str
            Destination phone number

        dynamic_variables : typing.Optional[typing.Dict[str, typing.Any]]
            Runtime variable overrides

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DispatchAgentResponse
            Call dispatched

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.dispatch_agent(
                uuid_="uuid",
                phone_number="phone_number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.dispatch_agent(
            uuid_, phone_number=phone_number, dynamic_variables=dynamic_variables, request_options=request_options
        )
        return _response.data

    async def get_agent_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentCapabilitiesResponse:
        """
        List supported ASR and LLM providers and models

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentCapabilitiesResponse
            Agent capabilities

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.get_agent_capabilities()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent_capabilities(request_options=request_options)
        return _response.data

    async def get_system_tools(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSystemToolsResponse:
        """
        List available system tools

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSystemToolsResponse
            System tools

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.get_system_tools()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_tools(request_options=request_options)
        return _response.data
