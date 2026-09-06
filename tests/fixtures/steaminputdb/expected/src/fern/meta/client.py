

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ping import Ping
from .raw_client import AsyncRawMetaClient, RawMetaClient


class MetaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetaClient
        """
        return self._raw_client

    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> Ping:
        """
        Health check and basic information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ping
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.meta.ping()
        """
        _response = self._raw_client.ping(request_options=request_options)
        return _response.data


class AsyncMetaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetaClient
        """
        return self._raw_client

    async def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> Ping:
        """
        Health check and basic information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ping
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.meta.ping()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping(request_options=request_options)
        return _response.data
