

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.token_request_token_scope import TokenRequestTokenScope
from .raw_client import AsyncRawAuthClient, RawAuthClient
from .types.create_token_response import CreateTokenResponse


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

    def create_token(
        self,
        *,
        username: str,
        password: str,
        token_name: str,
        token_scope: TokenRequestTokenScope,
        token_expire: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTokenResponse:
        """
        Generate a new token to access REST API

        Parameters
        ----------
        username : str
            Username of the login user.

        password : str
            Password of the user trying to login.

        token_name : str
            Friendly name of the token

        token_scope : TokenRequestTokenScope
            The scope of the token.

        token_expire : dt.date
            Date when the token must expire (default max 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTokenResponse
            Token generated

        Examples
        --------
        import datetime

        from fern import FernApi, TokenRequestTokenScope

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.create_token(
            token_name="token_name",
            token_scope=TokenRequestTokenScope.READ,
            token_expire=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.create_token(
            username=username,
            password=password,
            token_name=token_name,
            token_scope=token_scope,
            token_expire=token_expire,
            request_options=request_options,
        )
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

    async def create_token(
        self,
        *,
        username: str,
        password: str,
        token_name: str,
        token_scope: TokenRequestTokenScope,
        token_expire: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTokenResponse:
        """
        Generate a new token to access REST API

        Parameters
        ----------
        username : str
            Username of the login user.

        password : str
            Password of the user trying to login.

        token_name : str
            Friendly name of the token

        token_scope : TokenRequestTokenScope
            The scope of the token.

        token_expire : dt.date
            Date when the token must expire (default max 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTokenResponse
            Token generated

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, TokenRequestTokenScope

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.create_token(
                token_name="token_name",
                token_scope=TokenRequestTokenScope.READ,
                token_expire=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_token(
            username=username,
            password=password,
            token_name=token_name,
            token_scope=token_scope,
            token_expire=token_expire,
            request_options=request_options,
        )
        return _response.data
