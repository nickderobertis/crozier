

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawConfigClient, RawConfigClient


class ConfigClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConfigClient
        """
        return self._raw_client

    def get_backends_order_value(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The order.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.config.get_backends_order_value()
        """
        _response = self._raw_client.get_backends_order_value(request_options=request_options)
        return _response.data

    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = FernApi()
        client.config.ping()
        """
        _response = self._raw_client.ping(request_options=request_options)
        return _response.data


class AsyncConfigClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConfigClient
        """
        return self._raw_client

    async def get_backends_order_value(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The order.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.get_backends_order_value()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_backends_order_value(request_options=request_options)
        return _response.data

    async def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.ping()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping(request_options=request_options)
        return _response.data
