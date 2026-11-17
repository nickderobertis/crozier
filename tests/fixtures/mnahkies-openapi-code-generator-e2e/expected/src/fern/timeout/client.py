

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTimeoutClient, RawTimeoutClient
from .types.get_timeout_response import GetTimeoutResponse


class TimeoutClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTimeoutClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTimeoutClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTimeoutClient
        """
        return self._raw_client

    def get_timeout(self, *, ms: float, request_options: typing.Optional[RequestOptions] = None) -> GetTimeoutResponse:
        """
        Parameters
        ----------
        ms : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTimeoutResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.timeout.get_timeout(
            ms=1.1,
        )
        """
        _response = self._raw_client.get_timeout(ms=ms, request_options=request_options)
        return _response.data


class AsyncTimeoutClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTimeoutClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTimeoutClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTimeoutClient
        """
        return self._raw_client

    async def get_timeout(
        self, *, ms: float, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTimeoutResponse:
        """
        Parameters
        ----------
        ms : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTimeoutResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.timeout.get_timeout(
                ms=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_timeout(ms=ms, request_options=request_options)
        return _response.data
