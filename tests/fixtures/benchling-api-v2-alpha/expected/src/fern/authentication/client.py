

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.token_create_grant_type import TokenCreateGrantType
from ..types.token_response import TokenResponse
from .raw_client import AsyncRawAuthenticationClient, RawAuthenticationClient


OMIT = typing.cast(typing.Any, ...)


class AuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthenticationClient
        """
        return self._raw_client

    def generate_token(
        self,
        *,
        grant_type: TokenCreateGrantType,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        Generate a token

        Parameters
        ----------
        grant_type : TokenCreateGrantType

        client_id : typing.Optional[str]
            ID of client to request token for. Leave off if client ID and secret are being supplied through Authorization header.

        client_secret : typing.Optional[str]
            Leave off if client ID and secret are being supplied through Authorization header.

        code : typing.Optional[str]
            Authorization code to request token for. Required if grant_type is authorization_code.

        code_verifier : typing.Optional[str]
            Code verifier to request token for. Only required if code_verifier is provided in the authorization code request.

        redirect_uri : typing.Optional[str]
            Redirect URI to request token for. Required if grant_type is authorization_code.

        state : typing.Optional[str]
            State to request token for. Only required if state is provided in the authorization code request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Generated token

        Examples
        --------
        from fern import FernApi, TokenCreateGrantType

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.authentication.generate_token(
            grant_type=TokenCreateGrantType.CLIENT_CREDENTIALS,
        )
        """
        _response = self._raw_client.generate_token(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            code_verifier=code_verifier,
            redirect_uri=redirect_uri,
            state=state,
            request_options=request_options,
        )
        return _response.data


class AsyncAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthenticationClient
        """
        return self._raw_client

    async def generate_token(
        self,
        *,
        grant_type: TokenCreateGrantType,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        Generate a token

        Parameters
        ----------
        grant_type : TokenCreateGrantType

        client_id : typing.Optional[str]
            ID of client to request token for. Leave off if client ID and secret are being supplied through Authorization header.

        client_secret : typing.Optional[str]
            Leave off if client ID and secret are being supplied through Authorization header.

        code : typing.Optional[str]
            Authorization code to request token for. Required if grant_type is authorization_code.

        code_verifier : typing.Optional[str]
            Code verifier to request token for. Only required if code_verifier is provided in the authorization code request.

        redirect_uri : typing.Optional[str]
            Redirect URI to request token for. Required if grant_type is authorization_code.

        state : typing.Optional[str]
            State to request token for. Only required if state is provided in the authorization code request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Generated token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TokenCreateGrantType

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.authentication.generate_token(
                grant_type=TokenCreateGrantType.CLIENT_CREDENTIALS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_token(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            code_verifier=code_verifier,
            redirect_uri=redirect_uri,
            state=state,
            request_options=request_options,
        )
        return _response.data
