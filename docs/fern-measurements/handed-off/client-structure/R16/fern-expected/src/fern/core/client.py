

import typing

from ..types.server_status import ServerStatus
from .client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawCoreClient, RawCoreClient
from .request_options import RequestOptions


class CoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreClient
        """
        return self._raw_client

    def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServerStatus:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServerStatus
            Server status.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.core.get_status()
        """
        _response = self._raw_client.get_status(request_options=request_options)
        return _response.data


class AsyncCoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreClient
        """
        return self._raw_client

    async def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServerStatus:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServerStatus
            Server status.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.core.get_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status(request_options=request_options)
        return _response.data
