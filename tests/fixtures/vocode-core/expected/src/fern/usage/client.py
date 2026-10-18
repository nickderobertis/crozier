

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.usage import Usage
from .raw_client import AsyncRawUsageClient, RawUsageClient


class UsageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsageClient
        """
        return self._raw_client

    def get_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> Usage:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Usage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usage.get_usage()
        """
        _response = self._raw_client.get_usage(request_options=request_options)
        return _response.data


class AsyncUsageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsageClient
        """
        return self._raw_client

    async def get_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> Usage:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Usage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usage.get_usage()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_usage(request_options=request_options)
        return _response.data
