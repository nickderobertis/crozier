

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.obtain_token_response import ObtainTokenResponse
from ..types.renew_token_response import RenewTokenResponse
from ..types.revoke_token_response import RevokeTokenResponse
from .raw_client import AsyncRawOAuthClient, RawOAuthClient


OMIT = typing.cast(typing.Any, ...)


class OAuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOAuthClient
        """
        return self._raw_client

    def renew_token(
        self,
        client_id: str,
        *,
        access_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RenewTokenResponse:
        """
        `RenewToken` is deprecated. For information about refreshing OAuth access tokens, see
        [Migrate from Renew to Refresh OAuth Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).


        Renews an OAuth access token before it expires.

        OAuth access tokens besides your application's personal access token expire after __30 days__.
        You can also renew expired tokens within __15 days__ of their expiration.
        You cannot renew an access token that has been expired for more than 15 days.
        Instead, the associated user must re-complete the OAuth flow from the beginning.

        __Important:__ The `Authorization` header for this endpoint must have the
        following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace `APPLICATION_SECRET` with the application secret on the Credentials
        page in the [developer dashboard](https://developer.squareup.com/apps).

        Parameters
        ----------
        client_id : str
            Your application ID, available from the [developer dashboard](https://developer.squareup.com/apps).

        access_token : typing.Optional[str]
            The token you want to renew.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RenewTokenResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.o_auth.renew_token(
            client_id="client_id",
        )
        """
        _response = self._raw_client.renew_token(client_id, access_token=access_token, request_options=request_options)
        return _response.data

    def revoke_token(
        self,
        *,
        access_token: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        merchant_id: typing.Optional[str] = OMIT,
        revoke_only_access_token: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RevokeTokenResponse:
        """
        Revokes an access token generated with the OAuth flow.

        If an account has more than one OAuth access token for your application, this
        endpoint revokes all of them, regardless of which token you specify. When an
        OAuth access token is revoked, all of the active subscriptions associated
        with that OAuth token are canceled immediately.

        __Important:__ The `Authorization` header for this endpoint must have the
        following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace `APPLICATION_SECRET` with the application secret on the OAuth
        page in the [developer dashboard](https://developer.squareup.com/apps).

        Parameters
        ----------
        access_token : typing.Optional[str]
            The access token of the merchant whose token you want to revoke.
            Do not provide a value for merchant_id if you provide this parameter.

        client_id : typing.Optional[str]
            The Square issued ID for your application, available from the
            [developer dashboard](https://developer.squareup.com/apps).

        merchant_id : typing.Optional[str]
            The ID of the merchant whose token you want to revoke.
            Do not provide a value for access_token if you provide this parameter.

        revoke_only_access_token : typing.Optional[bool]
            If `true`, terminate the given single access token, but do not
            terminate the entire authorization.
            Default: `false`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RevokeTokenResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.o_auth.revoke_token()
        """
        _response = self._raw_client.revoke_token(
            access_token=access_token,
            client_id=client_id,
            merchant_id=merchant_id,
            revoke_only_access_token=revoke_only_access_token,
            request_options=request_options,
        )
        return _response.data

    def obtain_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: str,
        code: typing.Optional[str] = OMIT,
        migration_token: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        short_lived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObtainTokenResponse:
        """
        Returns an OAuth access token.

        The endpoint supports distinct methods of obtaining OAuth access tokens.
        Applications specify a method by adding the `grant_type` parameter
        in the request and also provide relevant information.

        __Note:__ Regardless of the method application specified,
        the endpoint always returns two items; an OAuth access token and
        a refresh token in the response.

        __OAuth tokens should only live on secure servers. Application clients
        should never interact directly with OAuth tokens__.

        Parameters
        ----------
        client_id : str
            The Square-issued ID of your application, available from the
            [developer dashboard](https://developer.squareup.com/apps).

        client_secret : str
            The Square-issued application secret for your application, available
            from the [developer dashboard](https://developer.squareup.com/apps).

        grant_type : str
            Specifies the method to request an OAuth access token.
            Valid values are: `authorization_code`, `refresh_token`, and `migration_token`

        code : typing.Optional[str]
            The authorization code to exchange.
            This is required if `grant_type` is set to `authorization_code`, to indicate that
            the application wants to exchange an authorization code for an OAuth access token.

        migration_token : typing.Optional[str]
            Legacy OAuth access token obtained using a Connect API version prior
            to 2019-03-13. This parameter is required if `grant_type` is set to
            `migration_token` to indicate that the application wants to get a replacement
            OAuth access token. The response also returns a refresh token.
            For more information, see [Migrate to Using Refresh Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).

        redirect_uri : typing.Optional[str]
            The redirect URL assigned in the [developer dashboard](https://developer.squareup.com/apps).

        refresh_token : typing.Optional[str]
            A valid refresh token for generating a new OAuth access token.
            A valid refresh token is required if `grant_type` is set to `refresh_token` , to indicate the application wants a replacement for an expired OAuth access token.

        scopes : typing.Optional[typing.Sequence[str]]
            A JSON list of strings representing the permissions the application is requesting.
            For example: "`["MERCHANT_PROFILE_READ","PAYMENTS_READ","BANK_ACCOUNTS_READ"]`"
            The access token returned in the response is granted the permissions
            that comprise the intersection between the requested list of permissions, and those
            that belong to the provided refresh token.

        short_lived : typing.Optional[bool]
            A boolean indicating a request for a short-lived access token.
            The short-lived access token returned in the response will expire in 24 hours.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObtainTokenResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.o_auth.obtain_token(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="grant_type",
        )
        """
        _response = self._raw_client.obtain_token(
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            code=code,
            migration_token=migration_token,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
            scopes=scopes,
            short_lived=short_lived,
            request_options=request_options,
        )
        return _response.data


class AsyncOAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOAuthClient
        """
        return self._raw_client

    async def renew_token(
        self,
        client_id: str,
        *,
        access_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RenewTokenResponse:
        """
        `RenewToken` is deprecated. For information about refreshing OAuth access tokens, see
        [Migrate from Renew to Refresh OAuth Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).


        Renews an OAuth access token before it expires.

        OAuth access tokens besides your application's personal access token expire after __30 days__.
        You can also renew expired tokens within __15 days__ of their expiration.
        You cannot renew an access token that has been expired for more than 15 days.
        Instead, the associated user must re-complete the OAuth flow from the beginning.

        __Important:__ The `Authorization` header for this endpoint must have the
        following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace `APPLICATION_SECRET` with the application secret on the Credentials
        page in the [developer dashboard](https://developer.squareup.com/apps).

        Parameters
        ----------
        client_id : str
            Your application ID, available from the [developer dashboard](https://developer.squareup.com/apps).

        access_token : typing.Optional[str]
            The token you want to renew.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RenewTokenResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth.renew_token(
                client_id="client_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.renew_token(
            client_id, access_token=access_token, request_options=request_options
        )
        return _response.data

    async def revoke_token(
        self,
        *,
        access_token: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        merchant_id: typing.Optional[str] = OMIT,
        revoke_only_access_token: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RevokeTokenResponse:
        """
        Revokes an access token generated with the OAuth flow.

        If an account has more than one OAuth access token for your application, this
        endpoint revokes all of them, regardless of which token you specify. When an
        OAuth access token is revoked, all of the active subscriptions associated
        with that OAuth token are canceled immediately.

        __Important:__ The `Authorization` header for this endpoint must have the
        following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace `APPLICATION_SECRET` with the application secret on the OAuth
        page in the [developer dashboard](https://developer.squareup.com/apps).

        Parameters
        ----------
        access_token : typing.Optional[str]
            The access token of the merchant whose token you want to revoke.
            Do not provide a value for merchant_id if you provide this parameter.

        client_id : typing.Optional[str]
            The Square issued ID for your application, available from the
            [developer dashboard](https://developer.squareup.com/apps).

        merchant_id : typing.Optional[str]
            The ID of the merchant whose token you want to revoke.
            Do not provide a value for access_token if you provide this parameter.

        revoke_only_access_token : typing.Optional[bool]
            If `true`, terminate the given single access token, but do not
            terminate the entire authorization.
            Default: `false`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RevokeTokenResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth.revoke_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_token(
            access_token=access_token,
            client_id=client_id,
            merchant_id=merchant_id,
            revoke_only_access_token=revoke_only_access_token,
            request_options=request_options,
        )
        return _response.data

    async def obtain_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: str,
        code: typing.Optional[str] = OMIT,
        migration_token: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        short_lived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObtainTokenResponse:
        """
        Returns an OAuth access token.

        The endpoint supports distinct methods of obtaining OAuth access tokens.
        Applications specify a method by adding the `grant_type` parameter
        in the request and also provide relevant information.

        __Note:__ Regardless of the method application specified,
        the endpoint always returns two items; an OAuth access token and
        a refresh token in the response.

        __OAuth tokens should only live on secure servers. Application clients
        should never interact directly with OAuth tokens__.

        Parameters
        ----------
        client_id : str
            The Square-issued ID of your application, available from the
            [developer dashboard](https://developer.squareup.com/apps).

        client_secret : str
            The Square-issued application secret for your application, available
            from the [developer dashboard](https://developer.squareup.com/apps).

        grant_type : str
            Specifies the method to request an OAuth access token.
            Valid values are: `authorization_code`, `refresh_token`, and `migration_token`

        code : typing.Optional[str]
            The authorization code to exchange.
            This is required if `grant_type` is set to `authorization_code`, to indicate that
            the application wants to exchange an authorization code for an OAuth access token.

        migration_token : typing.Optional[str]
            Legacy OAuth access token obtained using a Connect API version prior
            to 2019-03-13. This parameter is required if `grant_type` is set to
            `migration_token` to indicate that the application wants to get a replacement
            OAuth access token. The response also returns a refresh token.
            For more information, see [Migrate to Using Refresh Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).

        redirect_uri : typing.Optional[str]
            The redirect URL assigned in the [developer dashboard](https://developer.squareup.com/apps).

        refresh_token : typing.Optional[str]
            A valid refresh token for generating a new OAuth access token.
            A valid refresh token is required if `grant_type` is set to `refresh_token` , to indicate the application wants a replacement for an expired OAuth access token.

        scopes : typing.Optional[typing.Sequence[str]]
            A JSON list of strings representing the permissions the application is requesting.
            For example: "`["MERCHANT_PROFILE_READ","PAYMENTS_READ","BANK_ACCOUNTS_READ"]`"
            The access token returned in the response is granted the permissions
            that comprise the intersection between the requested list of permissions, and those
            that belong to the provided refresh token.

        short_lived : typing.Optional[bool]
            A boolean indicating a request for a short-lived access token.
            The short-lived access token returned in the response will expire in 24 hours.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObtainTokenResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth.obtain_token(
                client_id="client_id",
                client_secret="client_secret",
                grant_type="grant_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.obtain_token(
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            code=code,
            migration_token=migration_token,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
            scopes=scopes,
            short_lived=short_lived,
            request_options=request_options,
        )
        return _response.data
