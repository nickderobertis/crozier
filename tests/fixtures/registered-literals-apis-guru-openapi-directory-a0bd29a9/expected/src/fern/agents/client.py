

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent_response import AgentResponse
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

    def get_api_v1agents_family(
        self, family: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentResponse:
        """
        Parameters
        ----------
        family : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agents.get_api_v1agents_family(
            family="family",
        )
        """
        _response = self._raw_client.get_api_v1agents_family(family, request_options=request_options)
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

    async def get_api_v1agents_family(
        self, family: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentResponse:
        """
        Parameters
        ----------
        family : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agents.get_api_v1agents_family(
                family="family",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1agents_family(family, request_options=request_options)
        return _response.data
