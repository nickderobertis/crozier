

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAuthClient, RawAuthClient
from .types.get_auth_token_response import GetAuthTokenResponse


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

    def submit_login_form(
        self, *, password: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        password : typing.Optional[str]
            Access token or password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Login page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.auth.submit_login_form()
        """
        _response = self._raw_client.submit_login_form(password=password, request_options=request_options)
        return _response.data

    def get_the_auth_token_for_the_current_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAuthTokenResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAuthTokenResponse
            The auth token (null if auth is disabled)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.auth.get_the_auth_token_for_the_current_session()
        """
        _response = self._raw_client.get_the_auth_token_for_the_current_session(request_options=request_options)
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

    async def submit_login_form(
        self, *, password: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        password : typing.Optional[str]
            Access token or password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Login page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.auth.submit_login_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_login_form(password=password, request_options=request_options)
        return _response.data

    async def get_the_auth_token_for_the_current_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAuthTokenResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAuthTokenResponse
            The auth token (null if auth is disabled)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.auth.get_the_auth_token_for_the_current_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_auth_token_for_the_current_session(request_options=request_options)
        return _response.data
