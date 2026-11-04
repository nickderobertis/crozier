

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.token_response import TokenResponse
from ..types.user_out import UserOut
from .raw_client import AsyncRawAuthClient, RawAuthClient


OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.auth.login(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.login(username=username, password=password, request_options=request_options)
        return _response.data

    def me(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserOut:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.auth.me()
        """
        _response = self._raw_client.me(request_options=request_options)
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TokenResponse:
        """
        Parameters
        ----------
        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.auth.login(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login(username=username, password=password, request_options=request_options)
        return _response.data

    async def me(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserOut:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.auth.me()


        asyncio.run(main())
        """
        _response = await self._raw_client.me(request_options=request_options)
        return _response.data
