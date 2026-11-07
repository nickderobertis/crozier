

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.introspection_response import IntrospectionResponse
from ..types.pushed_authorization_response import PushedAuthorizationResponse
from ..types.token_request_grant_type import TokenRequestGrantType
from ..types.token_response import TokenResponse
from .raw_client import AsyncRawOAuth20Client, RawOAuth20Client
from .types.get_oauth_authorize_request_code_challenge_method import GetOauthAuthorizeRequestCodeChallengeMethod
from .types.post_oauth_introspect_request_token_type_hint import PostOauthIntrospectRequestTokenTypeHint
from .types.post_oauth_pushed_authorization_request_request_code_challenge_method import (
    PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod,
)
from .types.post_oauth_revoke_request_token_type_hint import PostOauthRevokeRequestTokenTypeHint


OMIT = typing.cast(typing.Any, ...)


class OAuth20Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOAuth20Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOAuth20Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOAuth20Client
        """
        return self._raw_client

    def start_an_authorization_request(
        self,
        *,
        client_id: str,
        response_type: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        nonce: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[GetOauthAuthorizeRequestCodeChallengeMethod] = None,
        prompt: typing.Optional[str] = None,
        max_age: typing.Optional[int] = None,
        request: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        client_id : str

        response_type : str

        redirect_uri : typing.Optional[str]

        scope : typing.Optional[str]

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[GetOauthAuthorizeRequestCodeChallengeMethod]

        prompt : typing.Optional[str]

        max_age : typing.Optional[int]

        request : typing.Optional[str]
            JWT-secured authorization request

        request_uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth20.start_an_authorization_request(
            client_id="client_id",
            response_type="response_type",
        )
        """
        _response = self._raw_client.start_an_authorization_request(
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            nonce=nonce,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            prompt=prompt,
            max_age=max_age,
            request=request,
            request_uri=request_uri,
            request_options=request_options,
        )
        return _response.data

    def issue_or_refresh_tokens(
        self,
        *,
        grant_type: TokenRequestGrantType,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        client_assertion_type: typing.Optional[str] = OMIT,
        client_assertion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        Parameters
        ----------
        grant_type : TokenRequestGrantType

        code : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        code_verifier : typing.Optional[str]

        refresh_token : typing.Optional[str]

        username : typing.Optional[str]

        password : typing.Optional[str]

        scope : typing.Optional[str]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        client_assertion_type : typing.Optional[str]

        client_assertion : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Token response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth20.issue_or_refresh_tokens(
            grant_type="authorization_code",
        )
        """
        _response = self._raw_client.issue_or_refresh_tokens(
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            code_verifier=code_verifier,
            refresh_token=refresh_token,
            username=username,
            password=password,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
            client_assertion_type=client_assertion_type,
            client_assertion=client_assertion,
            request_options=request_options,
        )
        return _response.data

    def introspect_a_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostOauthIntrospectRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IntrospectionResponse:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostOauthIntrospectRequestTokenTypeHint]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IntrospectionResponse
            Token introspection result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth20.introspect_a_token(
            token="token",
        )
        """
        _response = self._raw_client.introspect_a_token(
            token=token,
            token_type_hint=token_type_hint,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data

    def create_a_pushed_authorization_request(
        self,
        *,
        client_id: str,
        response_type: str,
        client_secret: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        nonce: typing.Optional[str] = OMIT,
        code_challenge: typing.Optional[str] = OMIT,
        code_challenge_method: typing.Optional[PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod] = OMIT,
        request: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PushedAuthorizationResponse:
        """
        Parameters
        ----------
        client_id : str

        response_type : str

        client_secret : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        scope : typing.Optional[str]

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod]

        request : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PushedAuthorizationResponse
            Pushed authorization request created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth20.create_a_pushed_authorization_request(
            client_id="client_id",
            response_type="response_type",
        )
        """
        _response = self._raw_client.create_a_pushed_authorization_request(
            client_id=client_id,
            response_type=response_type,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            nonce=nonce,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def revoke_a_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostOauthRevokeRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostOauthRevokeRequestTokenTypeHint]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

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
        client.o_auth20.revoke_a_token(
            token="token",
        )
        """
        _response = self._raw_client.revoke_a_token(
            token=token,
            token_type_hint=token_type_hint,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data


class AsyncOAuth20Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOAuth20Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOAuth20Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOAuth20Client
        """
        return self._raw_client

    async def start_an_authorization_request(
        self,
        *,
        client_id: str,
        response_type: str,
        redirect_uri: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        nonce: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[GetOauthAuthorizeRequestCodeChallengeMethod] = None,
        prompt: typing.Optional[str] = None,
        max_age: typing.Optional[int] = None,
        request: typing.Optional[str] = None,
        request_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        client_id : str

        response_type : str

        redirect_uri : typing.Optional[str]

        scope : typing.Optional[str]

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[GetOauthAuthorizeRequestCodeChallengeMethod]

        prompt : typing.Optional[str]

        max_age : typing.Optional[int]

        request : typing.Optional[str]
            JWT-secured authorization request

        request_uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth20.start_an_authorization_request(
                client_id="client_id",
                response_type="response_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_an_authorization_request(
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            nonce=nonce,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            prompt=prompt,
            max_age=max_age,
            request=request,
            request_uri=request_uri,
            request_options=request_options,
        )
        return _response.data

    async def issue_or_refresh_tokens(
        self,
        *,
        grant_type: TokenRequestGrantType,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        client_assertion_type: typing.Optional[str] = OMIT,
        client_assertion: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        Parameters
        ----------
        grant_type : TokenRequestGrantType

        code : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        code_verifier : typing.Optional[str]

        refresh_token : typing.Optional[str]

        username : typing.Optional[str]

        password : typing.Optional[str]

        scope : typing.Optional[str]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        client_assertion_type : typing.Optional[str]

        client_assertion : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Token response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth20.issue_or_refresh_tokens(
                grant_type="authorization_code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_or_refresh_tokens(
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            code_verifier=code_verifier,
            refresh_token=refresh_token,
            username=username,
            password=password,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
            client_assertion_type=client_assertion_type,
            client_assertion=client_assertion,
            request_options=request_options,
        )
        return _response.data

    async def introspect_a_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostOauthIntrospectRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IntrospectionResponse:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostOauthIntrospectRequestTokenTypeHint]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IntrospectionResponse
            Token introspection result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth20.introspect_a_token(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.introspect_a_token(
            token=token,
            token_type_hint=token_type_hint,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data

    async def create_a_pushed_authorization_request(
        self,
        *,
        client_id: str,
        response_type: str,
        client_secret: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        state: typing.Optional[str] = OMIT,
        nonce: typing.Optional[str] = OMIT,
        code_challenge: typing.Optional[str] = OMIT,
        code_challenge_method: typing.Optional[PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod] = OMIT,
        request: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PushedAuthorizationResponse:
        """
        Parameters
        ----------
        client_id : str

        response_type : str

        client_secret : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        scope : typing.Optional[str]

        state : typing.Optional[str]

        nonce : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod]

        request : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PushedAuthorizationResponse
            Pushed authorization request created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth20.create_a_pushed_authorization_request(
                client_id="client_id",
                response_type="response_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_pushed_authorization_request(
            client_id=client_id,
            response_type=response_type,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            nonce=nonce,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def revoke_a_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostOauthRevokeRequestTokenTypeHint] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostOauthRevokeRequestTokenTypeHint]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

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
            await client.o_auth20.revoke_a_token(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_a_token(
            token=token,
            token_type_hint=token_type_hint,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data
