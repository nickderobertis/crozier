

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.get_agent_code_snippets_response import GetAgentCodeSnippetsResponse
from .raw_client import AsyncRawAgentsClient, RawAgentsClient


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

    def get_code_snippets(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentCodeSnippetsResponse:
        """
        TypeScript TrueForge SDK samples (stream and non-stream) for creating a session and turn against this agent.

        Parameters
        ----------
        agent_id : str
            Immutable agent identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentCodeSnippetsResponse
            TypeScript SDK samples and the origin to use as `baseUrl`.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.agents.get_code_snippets(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.get_code_snippets(agent_id, request_options=request_options)
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

    async def get_code_snippets(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentCodeSnippetsResponse:
        """
        TypeScript TrueForge SDK samples (stream and non-stream) for creating a session and turn against this agent.

        Parameters
        ----------
        agent_id : str
            Immutable agent identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentCodeSnippetsResponse
            TypeScript SDK samples and the origin to use as `baseUrl`.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.agents.get_code_snippets(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_code_snippets(agent_id, request_options=request_options)
        return _response.data
