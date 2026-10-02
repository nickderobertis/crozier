

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawConfigClient, RawConfigClient


OMIT = typing.cast(typing.Any, ...)


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

    def update_config(
        self, *, config: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        config : typing.Dict[str, typing.Any]

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
        client.config.update_config(
            config={"key": "value"},
        )
        """
        _response = self._raw_client.update_config(config=config, request_options=request_options)
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

    async def update_config(
        self, *, config: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        config : typing.Dict[str, typing.Any]

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
            await client.config.update_config(
                config={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_config(config=config, request_options=request_options)
        return _response.data
