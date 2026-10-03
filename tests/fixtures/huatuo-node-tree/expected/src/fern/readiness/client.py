

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawReadinessClient, RawReadinessClient


class ReadinessClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReadinessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReadinessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReadinessClient
        """
        return self._raw_client

    def get_readiness(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            base_url="https://yourhost.com/path/to/api",
        )
        client.readiness.get_readiness()
        """
        _response = self._raw_client.get_readiness(request_options=request_options)
        return _response.data


class AsyncReadinessClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReadinessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReadinessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReadinessClient
        """
        return self._raw_client

    async def get_readiness(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.readiness.get_readiness()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_readiness(request_options=request_options)
        return _response.data
