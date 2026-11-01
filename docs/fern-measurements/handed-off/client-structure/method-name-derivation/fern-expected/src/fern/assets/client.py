

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsClient, RawAssetsClient


class AssetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsClient
        """
        return self._raw_client

    def serve_robots_txt(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The robots file.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.assets.serve_robots_txt()
        """
        _response = self._raw_client.serve_robots_txt(request_options=request_options)
        return _response.data

    def list_badges_ega_page_of_them(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            A page of badges.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.assets.list_badges_ega_page_of_them()
        """
        _response = self._raw_client.list_badges_ega_page_of_them(request_options=request_options)
        return _response.data


class AsyncAssetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsClient
        """
        return self._raw_client

    async def serve_robots_txt(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The robots file.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.assets.serve_robots_txt()


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_robots_txt(request_options=request_options)
        return _response.data

    async def list_badges_ega_page_of_them(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            A page of badges.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.assets.list_badges_ega_page_of_them()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_badges_ega_page_of_them(request_options=request_options)
        return _response.data
