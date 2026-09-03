

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.introspection_response import IntrospectionResponse
from ..types.token_response import TokenResponse
from ..types.user_info import UserInfo
from .raw_client import AsyncRawOAuth21OidcClient, RawOAuth21OidcClient
from .types.authorize_request_code_challenge_method import AuthorizeRequestCodeChallengeMethod
from .types.authorize_request_response_type import AuthorizeRequestResponseType
from .types.introspect_request_token_type_hint import IntrospectRequestTokenTypeHint
from .types.pushed_authorization_request_request_code_challenge_method import (
    PushedAuthorizationRequestRequestCodeChallengeMethod,
)
from .types.pushed_authorization_request_request_purpose import PushedAuthorizationRequestRequestPurpose
from .types.pushed_authorization_request_request_response_type import PushedAuthorizationRequestRequestResponseType
from .types.pushed_authorization_request_response import PushedAuthorizationRequestResponse
from .types.token_request_client_assertion_type import TokenRequestClientAssertionType
from .types.token_request_grant_type import TokenRequestGrantType


OMIT = typing.cast(typing.Any, ...)


class OAuth21OidcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOAuth21OidcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOAuth21OidcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOAuth21OidcClient
        """
        return self._raw_client

    def authorize(
        self,
        *,
        response_type: AuthorizeRequestResponseType,
        client_id: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: AuthorizeRequestCodeChallengeMethod,
        nonce: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        FAPI 2.0 compliant OAuth 2.1 authorization endpoint. Supports PAR (Pushed Authorization Requests)
        and requires PKCE for all authorization flows.

        Parameters
        ----------
        response_type : AuthorizeRequestResponseType
            Must be 'code' for authorization code flow

        client_id : str
            OAuth client identifier

        redirect_uri : str
            Client redirect URI

        scope : str
            Requested OAuth scopes

        state : str
            Client state parameter for CSRF protection

        code_challenge : str
            PKCE code challenge (S256)

        code_challenge_method : AuthorizeRequestCodeChallengeMethod
            PKCE code challenge method

        nonce : typing.Optional[str]
            OpenID Connect nonce

        request_uri : typing.Optional[str]
            PAR request URI (urn:ietf:params:oauth:request_uri:*)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.o_auth21oidc import (
            AuthorizeRequestCodeChallengeMethod,
            AuthorizeRequestResponseType,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth21oidc.authorize(
            response_type=AuthorizeRequestResponseType.CODE,
            client_id="client_id",
            redirect_uri="redirect_uri",
            scope="scope",
            state="state",
            code_challenge="code_challenge",
            code_challenge_method=AuthorizeRequestCodeChallengeMethod.S256,
        )
        """
        _response = self._raw_client.authorize(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            nonce=nonce,
            request_uri=request_uri,
            request_options=request_options,
        )
        return _response.data

    def token(
        self,
        *,
        grant_type: TokenRequestGrantType,
        client_id: str,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        client_assertion_type: typing.Optional[TokenRequestClientAssertionType] = OMIT,
        client_assertion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        FAPI 2.0 compliant token endpoint supporting authorization_code and refresh_token grants.
        Requires mTLS or private_key_jwt client authentication.

        Parameters
        ----------
        grant_type : TokenRequestGrantType

        client_id : str

        code : typing.Optional[str]
            Required for authorization_code grant

        redirect_uri : typing.Optional[str]
            Required for authorization_code grant

        code_verifier : typing.Optional[str]
            PKCE code verifier

        refresh_token : typing.Optional[str]
            Required for refresh_token grant

        client_assertion_type : typing.Optional[TokenRequestClientAssertionType]
            For private_key_jwt authentication

        client_assertion : typing.Optional[str]
            JWT assertion for private_key_jwt authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Access token response

        Examples
        --------
        from fern.o_auth21oidc import TokenRequestGrantType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth21oidc.token(
            grant_type=TokenRequestGrantType.AUTHORIZATION_CODE,
            client_id="bank-client-001",
            code="auth_code_123",
            redirect_uri="https://client.examples.com/callback",
            code_verifier="pkce_verifier_123",
        )
        """
        _response = self._raw_client.token(
            grant_type=grant_type,
            client_id=client_id,
            code=code,
            redirect_uri=redirect_uri,
            code_verifier=code_verifier,
            refresh_token=refresh_token,
            client_assertion_type=client_assertion_type,
            client_assertion=client_assertion,
            request_options=request_options,
        )
        return _response.data

    def userinfo(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserInfo:
        """
        Returns user information for the authenticated user. Supports DPoP token binding.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInfo
            User information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth21oidc.userinfo()
        """
        _response = self._raw_client.userinfo(request_options=request_options)
        return _response.data

    def introspect(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[IntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IntrospectionResponse:
        """
        RFC 7662 compliant token introspection endpoint for resource servers.

        Parameters
        ----------
        token : str
            Token to introspect

        token_type_hint : typing.Optional[IntrospectRequestTokenTypeHint]
            Hint about token type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IntrospectionResponse
            Token introspection response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth21oidc.introspect(
            token="token",
        )
        """
        _response = self._raw_client.introspect(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data

    def pushed_authorization_request(
        self,
        *,
        client_id: str,
        response_type: PushedAuthorizationRequestRequestResponseType,
        scope: str,
        redirect_uri: str,
        code_challenge: str,
        code_challenge_method: PushedAuthorizationRequestRequestCodeChallengeMethod,
        state: typing.Optional[str] = OMIT,
        nonce: typing.Optional[str] = OMIT,
        purpose: typing.Optional[PushedAuthorizationRequestRequestPurpose] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PushedAuthorizationRequestResponse:
        """
        FAPI 2.0 compliant PAR endpoint for securely submitting authorization request parameters.

        Parameters
        ----------
        client_id : str

        response_type : PushedAuthorizationRequestRequestResponseType

        scope : str

        redirect_uri : str

        code_challenge : str

        code_challenge_method : PushedAuthorizationRequestRequestCodeChallengeMethod

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        purpose : typing.Optional[PushedAuthorizationRequestRequestPurpose]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PushedAuthorizationRequestResponse
            PAR response with request_uri

        Examples
        --------
        from fern.o_auth21oidc import (
            PushedAuthorizationRequestRequestCodeChallengeMethod,
            PushedAuthorizationRequestRequestResponseType,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth21oidc.pushed_authorization_request(
            client_id="client_id",
            response_type=PushedAuthorizationRequestRequestResponseType.CODE,
            scope="scope",
            redirect_uri="redirect_uri",
            code_challenge="code_challenge",
            code_challenge_method=PushedAuthorizationRequestRequestCodeChallengeMethod.S256,
        )
        """
        _response = self._raw_client.pushed_authorization_request(
            client_id=client_id,
            response_type=response_type,
            scope=scope,
            redirect_uri=redirect_uri,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            state=state,
            nonce=nonce,
            purpose=purpose,
            request_options=request_options,
        )
        return _response.data


class AsyncOAuth21OidcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOAuth21OidcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOAuth21OidcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOAuth21OidcClient
        """
        return self._raw_client

    async def authorize(
        self,
        *,
        response_type: AuthorizeRequestResponseType,
        client_id: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: AuthorizeRequestCodeChallengeMethod,
        nonce: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        FAPI 2.0 compliant OAuth 2.1 authorization endpoint. Supports PAR (Pushed Authorization Requests)
        and requires PKCE for all authorization flows.

        Parameters
        ----------
        response_type : AuthorizeRequestResponseType
            Must be 'code' for authorization code flow

        client_id : str
            OAuth client identifier

        redirect_uri : str
            Client redirect URI

        scope : str
            Requested OAuth scopes

        state : str
            Client state parameter for CSRF protection

        code_challenge : str
            PKCE code challenge (S256)

        code_challenge_method : AuthorizeRequestCodeChallengeMethod
            PKCE code challenge method

        nonce : typing.Optional[str]
            OpenID Connect nonce

        request_uri : typing.Optional[str]
            PAR request URI (urn:ietf:params:oauth:request_uri:*)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.o_auth21oidc import (
            AuthorizeRequestCodeChallengeMethod,
            AuthorizeRequestResponseType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth21oidc.authorize(
                response_type=AuthorizeRequestResponseType.CODE,
                client_id="client_id",
                redirect_uri="redirect_uri",
                scope="scope",
                state="state",
                code_challenge="code_challenge",
                code_challenge_method=AuthorizeRequestCodeChallengeMethod.S256,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authorize(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            nonce=nonce,
            request_uri=request_uri,
            request_options=request_options,
        )
        return _response.data

    async def token(
        self,
        *,
        grant_type: TokenRequestGrantType,
        client_id: str,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        client_assertion_type: typing.Optional[TokenRequestClientAssertionType] = OMIT,
        client_assertion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        FAPI 2.0 compliant token endpoint supporting authorization_code and refresh_token grants.
        Requires mTLS or private_key_jwt client authentication.

        Parameters
        ----------
        grant_type : TokenRequestGrantType

        client_id : str

        code : typing.Optional[str]
            Required for authorization_code grant

        redirect_uri : typing.Optional[str]
            Required for authorization_code grant

        code_verifier : typing.Optional[str]
            PKCE code verifier

        refresh_token : typing.Optional[str]
            Required for refresh_token grant

        client_assertion_type : typing.Optional[TokenRequestClientAssertionType]
            For private_key_jwt authentication

        client_assertion : typing.Optional[str]
            JWT assertion for private_key_jwt authentication

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Access token response

        Examples
        --------
        import asyncio

        from fern.o_auth21oidc import TokenRequestGrantType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth21oidc.token(
                grant_type=TokenRequestGrantType.AUTHORIZATION_CODE,
                client_id="bank-client-001",
                code="auth_code_123",
                redirect_uri="https://client.examples.com/callback",
                code_verifier="pkce_verifier_123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token(
            grant_type=grant_type,
            client_id=client_id,
            code=code,
            redirect_uri=redirect_uri,
            code_verifier=code_verifier,
            refresh_token=refresh_token,
            client_assertion_type=client_assertion_type,
            client_assertion=client_assertion,
            request_options=request_options,
        )
        return _response.data

    async def userinfo(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserInfo:
        """
        Returns user information for the authenticated user. Supports DPoP token binding.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserInfo
            User information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth21oidc.userinfo()


        asyncio.run(main())
        """
        _response = await self._raw_client.userinfo(request_options=request_options)
        return _response.data

    async def introspect(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[IntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IntrospectionResponse:
        """
        RFC 7662 compliant token introspection endpoint for resource servers.

        Parameters
        ----------
        token : str
            Token to introspect

        token_type_hint : typing.Optional[IntrospectRequestTokenTypeHint]
            Hint about token type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IntrospectionResponse
            Token introspection response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth21oidc.introspect(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.introspect(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data

    async def pushed_authorization_request(
        self,
        *,
        client_id: str,
        response_type: PushedAuthorizationRequestRequestResponseType,
        scope: str,
        redirect_uri: str,
        code_challenge: str,
        code_challenge_method: PushedAuthorizationRequestRequestCodeChallengeMethod,
        state: typing.Optional[str] = OMIT,
        nonce: typing.Optional[str] = OMIT,
        purpose: typing.Optional[PushedAuthorizationRequestRequestPurpose] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PushedAuthorizationRequestResponse:
        """
        FAPI 2.0 compliant PAR endpoint for securely submitting authorization request parameters.

        Parameters
        ----------
        client_id : str

        response_type : PushedAuthorizationRequestRequestResponseType

        scope : str

        redirect_uri : str

        code_challenge : str

        code_challenge_method : PushedAuthorizationRequestRequestCodeChallengeMethod

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        purpose : typing.Optional[PushedAuthorizationRequestRequestPurpose]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PushedAuthorizationRequestResponse
            PAR response with request_uri

        Examples
        --------
        import asyncio

        from fern.o_auth21oidc import (
            PushedAuthorizationRequestRequestCodeChallengeMethod,
            PushedAuthorizationRequestRequestResponseType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth21oidc.pushed_authorization_request(
                client_id="client_id",
                response_type=PushedAuthorizationRequestRequestResponseType.CODE,
                scope="scope",
                redirect_uri="redirect_uri",
                code_challenge="code_challenge",
                code_challenge_method=PushedAuthorizationRequestRequestCodeChallengeMethod.S256,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pushed_authorization_request(
            client_id=client_id,
            response_type=response_type,
            scope=scope,
            redirect_uri=redirect_uri,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            state=state,
            nonce=nonce,
            purpose=purpose,
            request_options=request_options,
        )
        return _response.data
