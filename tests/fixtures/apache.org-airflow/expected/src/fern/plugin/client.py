

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.plugin_collection import PluginCollection
from .raw_client import AsyncRawPluginClient, RawPluginClient


class PluginClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPluginClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPluginClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPluginClient
        """
        return self._raw_client

    def get_plugins(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PluginCollection:
        """
        Get a list of loaded plugins.

        *New in version 2.1.0*

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PluginCollection
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.plugin.get_plugins()
        """
        _response = self._raw_client.get_plugins(limit=limit, offset=offset, request_options=request_options)
        return _response.data


class AsyncPluginClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPluginClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPluginClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPluginClient
        """
        return self._raw_client

    async def get_plugins(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PluginCollection:
        """
        Get a list of loaded plugins.

        *New in version 2.1.0*

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PluginCollection
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.plugin.get_plugins()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_plugins(limit=limit, offset=offset, request_options=request_options)
        return _response.data
