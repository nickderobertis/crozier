

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawCranesClient, RawCranesClient


class CranesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCranesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCranesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCranesClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Crane ids.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.yard.cranes.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncCranesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCranesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCranesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCranesClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Crane ids.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.yard.cranes.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
