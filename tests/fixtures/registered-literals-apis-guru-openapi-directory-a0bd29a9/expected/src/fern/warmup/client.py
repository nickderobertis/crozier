

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWarmupClient, RawWarmupClient


class WarmupClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWarmupClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWarmupClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWarmupClient
        """
        return self._raw_client

    def get_warmup(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.warmup.get_warmup()
        """
        _response = self._raw_client.get_warmup(request_options=request_options)
        return _response.data


class AsyncWarmupClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWarmupClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWarmupClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWarmupClient
        """
        return self._raw_client

    async def get_warmup(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.warmup.get_warmup()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_warmup(request_options=request_options)
        return _response.data
