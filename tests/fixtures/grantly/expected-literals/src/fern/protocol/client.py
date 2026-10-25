

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.registered_client import RegisteredClient
from .raw_client import AsyncRawProtocolClient, RawProtocolClient
from .types.get_auth_request_code_challenge_method import GetAuthRequestCodeChallengeMethod
from .types.get_auth_request_prompt import GetAuthRequestPrompt
from .types.get_jwks_response import GetJwksResponse
from .types.get_me_response import GetMeResponse
from .types.post_introspect_request_token_type_hint import PostIntrospectRequestTokenTypeHint
from .types.post_introspect_response import PostIntrospectResponse
from .types.post_revoke_request_token_type_hint import PostRevokeRequestTokenTypeHint
from .types.post_token_request import PostTokenRequest
from .types.post_token_response import PostTokenResponse


OMIT = typing.cast(typing.Any, ...)


class ProtocolClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProtocolClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProtocolClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProtocolClient
        """
        return self._raw_client

    def discovery_document(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns issuer metadata - endpoint URLs, supported scopes, grant types, signing algorithms.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Discovery document

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.discovery_document()
        """
        _response = self._raw_client.discovery_document(request_options=request_options)
        return _response.data

    def public_signing_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetJwksResponse:
        """
        JSON Web Key Set used to verify id_tokens issued by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetJwksResponse
            JWKS document

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.public_signing_keys()
        """
        _response = self._raw_client.public_signing_keys(request_options=request_options)
        return _response.data

    def authorization_endpoint(
        self,
        *,
        client_id: str,
        response_type: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: GetAuthRequestCodeChallengeMethod,
        prompt: typing.Optional[GetAuthRequestPrompt] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Starts an OAuth/OIDC authorization flow. Must be opened as a real browser navigation, not called via fetch/XHR - it involves interactive login and redirects.

        Parameters
        ----------
        client_id : str

        response_type : str

        redirect_uri : str

        scope : str

        state : str

        code_challenge : str
            PKCE code challenge (S256), required for all clients

        code_challenge_method : GetAuthRequestCodeChallengeMethod

        prompt : typing.Optional[GetAuthRequestPrompt]
            Set to "consent" to request a refresh token alongside offline_access scope

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.authorization_endpoint(
            client_id="client_id",
            response_type="code",
            redirect_uri="redirect_uri",
            scope="openid profile email",
            state="state",
            code_challenge="code_challenge",
            code_challenge_method="S256",
        )
        """
        _response = self._raw_client.authorization_endpoint(
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            prompt=prompt,
            request_options=request_options,
        )
        return _response.data

    def token_exchange(
        self, *, request: PostTokenRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostTokenResponse:
        """
        Exchanges an authorization code or refresh token for tokens. Rate-limited to 20 requests/60s per IP. CORS-scoped to FRONTEND_URL.

        Parameters
        ----------
        request : PostTokenRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostTokenResponse
            Token response

        Examples
        --------
        from fern.protocol import PostTokenRequest_AuthorizationCode

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.token_exchange(
            request=PostTokenRequest_AuthorizationCode(
                code="code",
                redirect_uri="redirect_uri",
                code_verifier="code_verifier",
            ),
        )
        """
        _response = self._raw_client.token_exchange(request=request, request_options=request_options)
        return _response.data

    def userinfo(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetMeResponse:
        """
        Returns claims for the access token's subject, scoped by the token's granted scopes. CORS-scoped to FRONTEND_URL.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMeResponse
            Claims

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.userinfo()
        """
        _response = self._raw_client.userinfo(request_options=request_options)
        return _response.data

    def dynamic_client_registration_rfc7591(
        self,
        *,
        redirect_uris: typing.Sequence[str],
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegisteredClient:
        """
        Anonymous client registration, gated by an Initial Access Token (minted via `npm run mint-token`).

        Parameters
        ----------
        redirect_uris : typing.Sequence[str]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisteredClient
            Client registered

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.dynamic_client_registration_rfc7591(
            redirect_uris=["redirect_uris"],
        )
        """
        _response = self._raw_client.dynamic_client_registration_rfc7591(
            redirect_uris=redirect_uris,
            grant_types=grant_types,
            response_types=response_types,
            request_options=request_options,
        )
        return _response.data

    def read_own_registration(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisteredClient:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisteredClient
            Current client configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.read_own_registration(
            client_id="clientId",
        )
        """
        _response = self._raw_client.read_own_registration(client_id, request_options=request_options)
        return _response.data

    def update_own_registration(
        self,
        client_id_: str,
        *,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        registration_access_token: typing.Optional[str] = OMIT,
        registration_client_uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Replaces the full client metadata - not a partial patch.

        Parameters
        ----------
        client_id_ : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        redirect_uris : typing.Optional[typing.Sequence[str]]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        registration_access_token : typing.Optional[str]

        registration_client_uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.update_own_registration(
            client_id_="clientId",
        )
        """
        _response = self._raw_client.update_own_registration(
            client_id_,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uris=redirect_uris,
            grant_types=grant_types,
            response_types=response_types,
            registration_access_token=registration_access_token,
            registration_client_uri=registration_client_uri,
            request_options=request_options,
        )
        return _response.data

    def deregister(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.deregister(
            client_id="clientId",
        )
        """
        _response = self._raw_client.deregister(client_id, request_options=request_options)
        return _response.data

    def token_revocation(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostRevokeRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostRevokeRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.token_revocation(
            token="token",
        )
        """
        _response = self._raw_client.token_revocation(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data

    def token_introspection(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostIntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostIntrospectResponse:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostIntrospectRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostIntrospectResponse
            Token metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.token_introspection(
            token="token",
        )
        """
        _response = self._raw_client.token_introspection(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data

    def rp_initiated_logout(
        self,
        *,
        id_token_hint: typing.Optional[str] = None,
        post_logout_redirect_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Must be opened as a browser navigation.

        Parameters
        ----------
        id_token_hint : typing.Optional[str]

        post_logout_redirect_uri : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.protocol.rp_initiated_logout()
        """
        _response = self._raw_client.rp_initiated_logout(
            id_token_hint=id_token_hint,
            post_logout_redirect_uri=post_logout_redirect_uri,
            request_options=request_options,
        )
        return _response.data


class AsyncProtocolClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProtocolClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProtocolClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProtocolClient
        """
        return self._raw_client

    async def discovery_document(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns issuer metadata - endpoint URLs, supported scopes, grant types, signing algorithms.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Discovery document

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.discovery_document()


        asyncio.run(main())
        """
        _response = await self._raw_client.discovery_document(request_options=request_options)
        return _response.data

    async def public_signing_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetJwksResponse:
        """
        JSON Web Key Set used to verify id_tokens issued by this server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetJwksResponse
            JWKS document

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.public_signing_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.public_signing_keys(request_options=request_options)
        return _response.data

    async def authorization_endpoint(
        self,
        *,
        client_id: str,
        response_type: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: GetAuthRequestCodeChallengeMethod,
        prompt: typing.Optional[GetAuthRequestPrompt] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Starts an OAuth/OIDC authorization flow. Must be opened as a real browser navigation, not called via fetch/XHR - it involves interactive login and redirects.

        Parameters
        ----------
        client_id : str

        response_type : str

        redirect_uri : str

        scope : str

        state : str

        code_challenge : str
            PKCE code challenge (S256), required for all clients

        code_challenge_method : GetAuthRequestCodeChallengeMethod

        prompt : typing.Optional[GetAuthRequestPrompt]
            Set to "consent" to request a refresh token alongside offline_access scope

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.authorization_endpoint(
                client_id="client_id",
                response_type="code",
                redirect_uri="redirect_uri",
                scope="openid profile email",
                state="state",
                code_challenge="code_challenge",
                code_challenge_method="S256",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authorization_endpoint(
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            prompt=prompt,
            request_options=request_options,
        )
        return _response.data

    async def token_exchange(
        self, *, request: PostTokenRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostTokenResponse:
        """
        Exchanges an authorization code or refresh token for tokens. Rate-limited to 20 requests/60s per IP. CORS-scoped to FRONTEND_URL.

        Parameters
        ----------
        request : PostTokenRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostTokenResponse
            Token response

        Examples
        --------
        import asyncio

        from fern.protocol import PostTokenRequest_AuthorizationCode

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.token_exchange(
                request=PostTokenRequest_AuthorizationCode(
                    code="code",
                    redirect_uri="redirect_uri",
                    code_verifier="code_verifier",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_exchange(request=request, request_options=request_options)
        return _response.data

    async def userinfo(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetMeResponse:
        """
        Returns claims for the access token's subject, scoped by the token's granted scopes. CORS-scoped to FRONTEND_URL.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMeResponse
            Claims

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.userinfo()


        asyncio.run(main())
        """
        _response = await self._raw_client.userinfo(request_options=request_options)
        return _response.data

    async def dynamic_client_registration_rfc7591(
        self,
        *,
        redirect_uris: typing.Sequence[str],
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegisteredClient:
        """
        Anonymous client registration, gated by an Initial Access Token (minted via `npm run mint-token`).

        Parameters
        ----------
        redirect_uris : typing.Sequence[str]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisteredClient
            Client registered

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.dynamic_client_registration_rfc7591(
                redirect_uris=["redirect_uris"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.dynamic_client_registration_rfc7591(
            redirect_uris=redirect_uris,
            grant_types=grant_types,
            response_types=response_types,
            request_options=request_options,
        )
        return _response.data

    async def read_own_registration(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisteredClient:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisteredClient
            Current client configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.read_own_registration(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_own_registration(client_id, request_options=request_options)
        return _response.data

    async def update_own_registration(
        self,
        client_id_: str,
        *,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        grant_types: typing.Optional[typing.Sequence[str]] = OMIT,
        response_types: typing.Optional[typing.Sequence[str]] = OMIT,
        registration_access_token: typing.Optional[str] = OMIT,
        registration_client_uri: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Replaces the full client metadata - not a partial patch.

        Parameters
        ----------
        client_id_ : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        redirect_uris : typing.Optional[typing.Sequence[str]]

        grant_types : typing.Optional[typing.Sequence[str]]

        response_types : typing.Optional[typing.Sequence[str]]

        registration_access_token : typing.Optional[str]

        registration_client_uri : typing.Optional[str]

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.update_own_registration(
                client_id_="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_own_registration(
            client_id_,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uris=redirect_uris,
            grant_types=grant_types,
            response_types=response_types,
            registration_access_token=registration_access_token,
            registration_client_uri=registration_client_uri,
            request_options=request_options,
        )
        return _response.data

    async def deregister(self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        client_id : str

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.deregister(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deregister(client_id, request_options=request_options)
        return _response.data

    async def token_revocation(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostRevokeRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostRevokeRequestTokenTypeHint]

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.token_revocation(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_revocation(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data

    async def token_introspection(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[PostIntrospectRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostIntrospectResponse:
        """
        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[PostIntrospectRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostIntrospectResponse
            Token metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.token_introspection(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_introspection(
            token=token, token_type_hint=token_type_hint, request_options=request_options
        )
        return _response.data

    async def rp_initiated_logout(
        self,
        *,
        id_token_hint: typing.Optional[str] = None,
        post_logout_redirect_uri: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Must be opened as a browser navigation.

        Parameters
        ----------
        id_token_hint : typing.Optional[str]

        post_logout_redirect_uri : typing.Optional[str]

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.protocol.rp_initiated_logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.rp_initiated_logout(
            id_token_hint=id_token_hint,
            post_logout_redirect_uri=post_logout_redirect_uri,
            request_options=request_options,
        )
        return _response.data
