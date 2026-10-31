

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawHealthCheckClient, RawHealthCheckClient


class HealthCheckClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthCheckClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthCheckClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthCheckClient
        """
        return self._raw_client

    def health_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.health_check.health_check()
        """
        _response = self._raw_client.health_check(request_options=request_options)
        return _response.data


class AsyncHealthCheckClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthCheckClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthCheckClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthCheckClient
        """
        return self._raw_client

    async def health_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.health_check.health_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.health_check(request_options=request_options)
        return _response.data
