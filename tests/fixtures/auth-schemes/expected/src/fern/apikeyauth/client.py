

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawApikeyauthClient, RawApikeyauthClient


class ApikeyauthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApikeyauthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApikeyauthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApikeyauthClient
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
        client.apikeyauth.whoami()
        """
        _response = self._raw_client.whoami(request_options=request_options)
        return _response.data


class AsyncApikeyauthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApikeyauthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApikeyauthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApikeyauthClient
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
            await client.apikeyauth.whoami()


        asyncio.run(main())
        """
        _response = await self._raw_client.whoami(request_options=request_options)
        return _response.data
