

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBearerauthClient, RawBearerauthClient


class BearerauthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBearerauthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBearerauthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBearerauthClient
        """
        return self._raw_client

    def whoami(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.bearerauth.whoami()
        """
        _response = self._raw_client.whoami(request_options=request_options)
        return _response.data


class AsyncBearerauthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBearerauthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBearerauthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBearerauthClient
        """
        return self._raw_client

    async def whoami(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.bearerauth.whoami()


        asyncio.run(main())
        """
        _response = await self._raw_client.whoami(request_options=request_options)
        return _response.data
