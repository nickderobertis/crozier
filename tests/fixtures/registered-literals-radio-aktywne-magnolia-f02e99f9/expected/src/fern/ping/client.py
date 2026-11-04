

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPingClient, RawPingClient


class PingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPingClient
        """
        return self._raw_client

    def ping_ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Ping.

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.ping.ping_ping()
        """
        _response = self._raw_client.ping_ping(request_options=request_options)
        return _response.data

    def ping_headping(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Ping headers.

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.ping.ping_headping()
        """
        _response = self._raw_client.ping_headping(request_options=request_options)
        return _response.headers


class AsyncPingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPingClient
        """
        return self._raw_client

    async def ping_ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Ping.

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ping.ping_ping()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping_ping(request_options=request_options)
        return _response.data

    async def ping_headping(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Ping headers.

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ping.ping_headping()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping_headping(request_options=request_options)
        return _response.headers
