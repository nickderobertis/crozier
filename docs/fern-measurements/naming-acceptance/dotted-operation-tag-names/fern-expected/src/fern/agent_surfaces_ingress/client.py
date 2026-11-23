

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAgentSurfacesIngressClient, RawAgentSurfacesIngressClient


class AgentSurfacesIngressClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentSurfacesIngressClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentSurfacesIngressClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentSurfacesIngressClient
        """
        return self._raw_client

    def surface_webhook_verify(self, platform: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        platform : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.agent_surfaces_ingress.surface_webhook_verify(
            platform="platform",
        )
        """
        _response = self._raw_client.surface_webhook_verify(platform, request_options=request_options)
        return _response.data


class AsyncAgentSurfacesIngressClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentSurfacesIngressClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentSurfacesIngressClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentSurfacesIngressClient
        """
        return self._raw_client

    async def surface_webhook_verify(
        self, platform: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        platform : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.agent_surfaces_ingress.surface_webhook_verify(
                platform="platform",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.surface_webhook_verify(platform, request_options=request_options)
        return _response.data
