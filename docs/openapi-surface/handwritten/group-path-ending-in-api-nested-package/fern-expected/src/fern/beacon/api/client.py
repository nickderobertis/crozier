

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawApiClient, RawApiClient


class ApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApiClient
        """
        return self._raw_client

    def status(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The beacon's status line.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.beacon.api.status()
        """
        _response = self._raw_client.status(request_options=request_options)
        return _response.data


class AsyncApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApiClient
        """
        return self._raw_client

    async def status(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The beacon's status line.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.beacon.api.status()


        asyncio.run(main())
        """
        _response = await self._raw_client.status(request_options=request_options)
        return _response.data
