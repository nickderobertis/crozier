

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.success_response import SuccessResponse
from .raw_client import AsyncRawUtilityClient, RawUtilityClient


class UtilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUtilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUtilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUtilityClient
        """
        return self._raw_client

    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> SuccessResponse:
        """
        Health check endpoint that returns a simple pong response

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Pong response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.utility.ping()
        """
        _response = self._raw_client.ping(request_options=request_options)
        return _response.data


class AsyncUtilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUtilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUtilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUtilityClient
        """
        return self._raw_client

    async def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> SuccessResponse:
        """
        Health check endpoint that returns a simple pong response

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Pong response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.utility.ping()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping(request_options=request_options)
        return _response.data
