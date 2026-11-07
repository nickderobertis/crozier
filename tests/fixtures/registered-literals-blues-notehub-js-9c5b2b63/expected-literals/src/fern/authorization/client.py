

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.o_auth2token_response import OAuth2TokenResponse
from .raw_client import AsyncRawAuthorizationClient, RawAuthorizationClient
from .types.login_response import LoginResponse
from .types.o_auth2client_credentials_request_grant_type import OAuth2ClientCredentialsRequestGrantType


OMIT = typing.cast(typing.Any, ...)


class AuthorizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthorizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthorizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthorizationClient
        """
        return self._raw_client

    def login(
        self,
        *,
        password: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginResponse:
        """
        Gets an API key from username and password

        Parameters
        ----------
        password : typing.Optional[str]

        username : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authorization.login(
            password="test-password",
            username="name@example.com",
        )
        """
        _response = self._raw_client.login(password=password, username=username, request_options=request_options)
        return _response.data

    def o_auth2client_credentials(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: OAuth2ClientCredentialsRequestGrantType,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OAuth2TokenResponse:
        """
        Exchanges client credentials for an access token. Parameters must be sent as application/x-www-form-urlencoded.

        Parameters
        ----------
        client_id : str

        client_secret : str

        grant_type : OAuth2ClientCredentialsRequestGrantType

        scope : typing.Optional[str]
            Space-delimited scopes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuth2TokenResponse
            Successful token response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authorization.o_auth2client_credentials(
            client_id="d37ae69a-c739-44e9-9722-81a4cb7aeb67",
            client_secret="2a40832d028a3e24a717f023fdcaa8ab452dd12223d472aff38223ffdfeee4bf",
            grant_type="client_credentials",
        )
        """
        _response = self._raw_client.o_auth2client_credentials(
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            scope=scope,
            request_options=request_options,
        )
        return _response.data


class AsyncAuthorizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthorizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthorizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthorizationClient
        """
        return self._raw_client

    async def login(
        self,
        *,
        password: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoginResponse:
        """
        Gets an API key from username and password

        Parameters
        ----------
        password : typing.Optional[str]

        username : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoginResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authorization.login(
                password="test-password",
                username="name@example.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.login(password=password, username=username, request_options=request_options)
        return _response.data

    async def o_auth2client_credentials(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: OAuth2ClientCredentialsRequestGrantType,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OAuth2TokenResponse:
        """
        Exchanges client credentials for an access token. Parameters must be sent as application/x-www-form-urlencoded.

        Parameters
        ----------
        client_id : str

        client_secret : str

        grant_type : OAuth2ClientCredentialsRequestGrantType

        scope : typing.Optional[str]
            Space-delimited scopes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuth2TokenResponse
            Successful token response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authorization.o_auth2client_credentials(
                client_id="d37ae69a-c739-44e9-9722-81a4cb7aeb67",
                client_secret="2a40832d028a3e24a717f023fdcaa8ab452dd12223d472aff38223ffdfeee4bf",
                grant_type="client_credentials",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.o_auth2client_credentials(
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            scope=scope,
            request_options=request_options,
        )
        return _response.data
