

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1o_auth_authorized_application import V1OAuthAuthorizedApplication
from ..types.v1o_auth_introspect_response import V1OAuthIntrospectResponse
from ..types.v1o_auth_token_response import V1OAuthTokenResponse
from .raw_client import AsyncRawOAuthClient, RawOAuthClient
from .types.get_current_token_info_response import GetCurrentTokenInfoResponse
from .types.v1o_auth_introspect_request_token_type_hint import V1OAuthIntrospectRequestTokenTypeHint
from .types.v1o_auth_revoke_request_token_type_hint import V1OAuthRevokeRequestTokenTypeHint
from .types.v1o_auth_token_request_grant_type import V1OAuthTokenRequestGrantType


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

    def create_access_token(
        self,
        *,
        grant_type: V1OAuthTokenRequestGrantType,
        client_id: str,
        client_secret: str,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1OAuthTokenResponse:
        """
        Exchange an authorization code for an access token using OAuth 2.0 authorization code flow.

        Parameters
        ----------
        grant_type : V1OAuthTokenRequestGrantType
            OAuth 2.0 grant type

        client_id : str
            OAuth 2.0 client identifier

        client_secret : str
            OAuth 2.0 client secret

        code : typing.Optional[str]
            Authorization code (required for authorization_code grant)

        redirect_uri : typing.Optional[str]
            Redirect URI (required for authorization_code grant)

        refresh_token : typing.Optional[str]
            Refresh token (required for refresh_token grant)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1OAuthTokenResponse
            access token created

        Examples
        --------
        from fern.o_auth import V1OAuthTokenRequestGrantType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth.create_access_token(
            grant_type=V1OAuthTokenRequestGrantType.AUTHORIZATION_CODE,
            client_id="client_id",
            client_secret="client_secret",
        )
        """
        _response = self._raw_client.create_access_token(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
            request_options=request_options,
        )
        return _response.data

    def revoke_access_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[V1OAuthRevokeRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Revoke an access token or refresh token.

        Parameters
        ----------
        token : str
            OAuth 2.0 access or refresh token to revoke

        token_type_hint : typing.Optional[V1OAuthRevokeRequestTokenTypeHint]
            Hint about the type of token being revoked

        client_id : typing.Optional[str]
            OAuth 2.0 client identifier

        client_secret : typing.Optional[str]
            OAuth 2.0 client secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            token revoked

        Examples
        --------
        from fern.o_auth import V1OAuthRevokeRequestTokenTypeHint

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth.revoke_access_token(
            token="access_token_to_revoke",
            token_type_hint=V1OAuthRevokeRequestTokenTypeHint.ACCESS_TOKEN,
            client_id="EZPB04UG2RcRFOBd99k06MhN1WEl4opRHCun-8X1U9M",
            client_secret="8b93a66396d8dd37a32ae4ff85d99c192bf08b0270e73710cb7f3f29fc4530f1",
        )
        """
        _response = self._raw_client.revoke_access_token(
            token=token,
            token_type_hint=token_type_hint,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data

    def introspect_access_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[V1OAuthIntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1OAuthIntrospectResponse:
        """
        Check if an access token is active and get its metadata.

        Parameters
        ----------
        token : str
            OAuth 2.0 access token to introspect

        token_type_hint : typing.Optional[V1OAuthIntrospectRequestTokenTypeHint]
            Hint about the type of token being introspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1OAuthIntrospectResponse
            token introspection result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth.introspect_access_token(
            token="token",
        )
        """
        _response = self._raw_client.introspect_access_token(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data

    def get_current_token_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCurrentTokenInfoResponse:
        """
        Get information about the current access token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCurrentTokenInfoResponse
            token info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth.get_current_token_info()
        """
        _response = self._raw_client.get_current_token_info(request_options=request_options)
        return _response.data

    def list_authorized_applications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1OAuthAuthorizedApplication]:
        """
        List applications that the current user has authorized.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1OAuthAuthorizedApplication]
            authorized applications

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth.list_authorized_applications()
        """
        _response = self._raw_client.list_authorized_applications(request_options=request_options)
        return _response.data

    def revoke_application_authorization(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Revoke authorization for a specific application.

        Parameters
        ----------
        id : int
            Application ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth.revoke_application_authorization(
            id=1,
        )
        """
        _response = self._raw_client.revoke_application_authorization(id, request_options=request_options)
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

    async def create_access_token(
        self,
        *,
        grant_type: V1OAuthTokenRequestGrantType,
        client_id: str,
        client_secret: str,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1OAuthTokenResponse:
        """
        Exchange an authorization code for an access token using OAuth 2.0 authorization code flow.

        Parameters
        ----------
        grant_type : V1OAuthTokenRequestGrantType
            OAuth 2.0 grant type

        client_id : str
            OAuth 2.0 client identifier

        client_secret : str
            OAuth 2.0 client secret

        code : typing.Optional[str]
            Authorization code (required for authorization_code grant)

        redirect_uri : typing.Optional[str]
            Redirect URI (required for authorization_code grant)

        refresh_token : typing.Optional[str]
            Refresh token (required for refresh_token grant)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1OAuthTokenResponse
            access token created

        Examples
        --------
        import asyncio

        from fern.o_auth import V1OAuthTokenRequestGrantType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth.create_access_token(
                grant_type=V1OAuthTokenRequestGrantType.AUTHORIZATION_CODE,
                client_id="client_id",
                client_secret="client_secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_access_token(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
            request_options=request_options,
        )
        return _response.data

    async def revoke_access_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[V1OAuthRevokeRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Revoke an access token or refresh token.

        Parameters
        ----------
        token : str
            OAuth 2.0 access or refresh token to revoke

        token_type_hint : typing.Optional[V1OAuthRevokeRequestTokenTypeHint]
            Hint about the type of token being revoked

        client_id : typing.Optional[str]
            OAuth 2.0 client identifier

        client_secret : typing.Optional[str]
            OAuth 2.0 client secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            token revoked

        Examples
        --------
        import asyncio

        from fern.o_auth import V1OAuthRevokeRequestTokenTypeHint

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth.revoke_access_token(
                token="access_token_to_revoke",
                token_type_hint=V1OAuthRevokeRequestTokenTypeHint.ACCESS_TOKEN,
                client_id="EZPB04UG2RcRFOBd99k06MhN1WEl4opRHCun-8X1U9M",
                client_secret="8b93a66396d8dd37a32ae4ff85d99c192bf08b0270e73710cb7f3f29fc4530f1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_access_token(
            token=token,
            token_type_hint=token_type_hint,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data

    async def introspect_access_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[V1OAuthIntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1OAuthIntrospectResponse:
        """
        Check if an access token is active and get its metadata.

        Parameters
        ----------
        token : str
            OAuth 2.0 access token to introspect

        token_type_hint : typing.Optional[V1OAuthIntrospectRequestTokenTypeHint]
            Hint about the type of token being introspected

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1OAuthIntrospectResponse
            token introspection result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth.introspect_access_token(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.introspect_access_token(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data

    async def get_current_token_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCurrentTokenInfoResponse:
        """
        Get information about the current access token.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCurrentTokenInfoResponse
            token info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth.get_current_token_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_token_info(request_options=request_options)
        return _response.data

    async def list_authorized_applications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1OAuthAuthorizedApplication]:
        """
        List applications that the current user has authorized.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1OAuthAuthorizedApplication]
            authorized applications

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth.list_authorized_applications()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_authorized_applications(request_options=request_options)
        return _response.data

    async def revoke_application_authorization(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Revoke authorization for a specific application.

        Parameters
        ----------
        id : int
            Application ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth.revoke_application_authorization(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_application_authorization(id, request_options=request_options)
        return _response.data
