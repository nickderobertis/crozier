

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config import Config
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

    def get_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> Config:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.config.get_config()
        """
        _response = self._raw_client.get_config(request_options=request_options)
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

    async def get_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> Config:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Config
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.config.get_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_config(request_options=request_options)
        return _response.data
