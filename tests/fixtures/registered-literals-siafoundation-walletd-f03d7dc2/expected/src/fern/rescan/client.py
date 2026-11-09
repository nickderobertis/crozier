

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.rescan_response import RescanResponse
from .raw_client import AsyncRawRescanClient, RawRescanClient


OMIT = typing.cast(typing.Any, ...)


class RescanClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRescanClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRescanClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRescanClient
        """
        return self._raw_client

    def get_rescan(self, *, request_options: typing.Optional[RequestOptions] = None) -> RescanResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RescanResponse
            Current rescan progress.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.rescan.get_rescan()
        """
        _response = self._raw_client.get_rescan(request_options=request_options)
        return _response.data

    def post_rescan(self, *, request: int, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Initiates a background rescan from the supplied height. Omitting the height or providing zero triggers a full rescan from genesis.

        Parameters
        ----------
        request : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.rescan.post_rescan(
            request=1000000,
        )
        """
        _response = self._raw_client.post_rescan(request=request, request_options=request_options)
        return _response.data


class AsyncRescanClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRescanClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRescanClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRescanClient
        """
        return self._raw_client

    async def get_rescan(self, *, request_options: typing.Optional[RequestOptions] = None) -> RescanResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RescanResponse
            Current rescan progress.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.rescan.get_rescan()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_rescan(request_options=request_options)
        return _response.data

    async def post_rescan(self, *, request: int, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Initiates a background rescan from the supplied height. Omitting the height or providing zero triggers a full rescan from genesis.

        Parameters
        ----------
        request : int

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
            await client.rescan.post_rescan(
                request=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_rescan(request=request, request_options=request_options)
        return _response.data
