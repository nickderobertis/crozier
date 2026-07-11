

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.session import Session
from .raw_client import AsyncRawCookiesClient, RawCookiesClient


class CookiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCookiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCookiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCookiesClient
        """
        return self._raw_client

    def getsession(self, *, request_options: typing.Optional[RequestOptions] = None) -> Session:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            tenant="YOUR_TENANT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cookies.getsession()
        """
        _response = self._raw_client.getsession(request_options=request_options)
        return _response.data


class AsyncCookiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCookiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCookiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCookiesClient
        """
        return self._raw_client

    async def getsession(self, *, request_options: typing.Optional[RequestOptions] = None) -> Session:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            tenant="YOUR_TENANT",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cookies.getsession()


        asyncio.run(main())
        """
        _response = await self._raw_client.getsession(request_options=request_options)
        return _response.data
