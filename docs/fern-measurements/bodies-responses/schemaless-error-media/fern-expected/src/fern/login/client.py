

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLoginClient, RawLoginClient


class LoginClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLoginClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLoginClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLoginClient
        """
        return self._raw_client

    def show_login(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The login page.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.login.show_login()
        """
        _response = self._raw_client.show_login(request_options=request_options)
        return _response.data

    def show_consent(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The consent page.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.login.show_consent()
        """
        _response = self._raw_client.show_consent(request_options=request_options)
        return _response.data


class AsyncLoginClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLoginClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLoginClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLoginClient
        """
        return self._raw_client

    async def show_login(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The login page.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.login.show_login()


        asyncio.run(main())
        """
        _response = await self._raw_client.show_login(request_options=request_options)
        return _response.data

    async def show_consent(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The consent page.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.login.show_consent()


        asyncio.run(main())
        """
        _response = await self._raw_client.show_consent(request_options=request_options)
        return _response.data
