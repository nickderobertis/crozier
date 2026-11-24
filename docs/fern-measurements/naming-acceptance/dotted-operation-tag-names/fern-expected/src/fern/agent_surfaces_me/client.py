

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAgentSurfacesMeClient, RawAgentSurfacesMeClient


class AgentSurfacesMeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentSurfacesMeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentSurfacesMeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentSurfacesMeClient
        """
        return self._raw_client

    def agent_surface_list_mine(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            My surfaces.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.agent_surfaces_me.agent_surface_list_mine()
        """
        _response = self._raw_client.agent_surface_list_mine(request_options=request_options)
        return _response.data

    def agent_surface_set_my_default(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.agent_surfaces_me.agent_surface_set_my_default()
        """
        _response = self._raw_client.agent_surface_set_my_default(request_options=request_options)
        return _response.data


class AsyncAgentSurfacesMeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentSurfacesMeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentSurfacesMeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentSurfacesMeClient
        """
        return self._raw_client

    async def agent_surface_list_mine(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            My surfaces.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.agent_surfaces_me.agent_surface_list_mine()


        asyncio.run(main())
        """
        _response = await self._raw_client.agent_surface_list_mine(request_options=request_options)
        return _response.data

    async def agent_surface_set_my_default(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.agent_surfaces_me.agent_surface_set_my_default()


        asyncio.run(main())
        """
        _response = await self._raw_client.agent_surface_set_my_default(request_options=request_options)
        return _response.data
