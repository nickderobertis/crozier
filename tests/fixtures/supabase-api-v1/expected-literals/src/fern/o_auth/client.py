

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.o_auth_token_body_grant_type import OAuthTokenBodyGrantType
from ..types.o_auth_token_response_output import OAuthTokenResponseOutput
from .raw_client import AsyncRawOAuthClient, RawOAuthClient
from .types.v1authorize_user_request_code_challenge_method import V1AuthorizeUserRequestCodeChallengeMethod
from .types.v1authorize_user_request_response_type import V1AuthorizeUserRequestResponseType
from .types.v1oauth_authorize_project_claim_request_code_challenge_method import (
    V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod,
)
from .types.v1oauth_authorize_project_claim_request_response_type import V1OauthAuthorizeProjectClaimRequestResponseType


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

    def v1authorize_user(
        self,
        *,
        client_id: str,
        response_type: V1AuthorizeUserRequestResponseType,
        redirect_uri: str,
        scope: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        response_mode: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[V1AuthorizeUserRequestCodeChallengeMethod] = None,
        organization_slug: typing.Optional[str] = None,
        target_flow: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        client_id : str

        response_type : V1AuthorizeUserRequestResponseType

        redirect_uri : str

        scope : typing.Optional[str]

        state : typing.Optional[str]

        response_mode : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[V1AuthorizeUserRequestCodeChallengeMethod]

        organization_slug : typing.Optional[str]
            Organization slug

        target_flow : typing.Optional[str]

        resource : typing.Optional[str]
            Resource indicator for MCP (Model Context Protocol) clients

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
        client.o_auth.v1authorize_user(
            client_id="66666666-6666-4666-8666-666666666666",
            response_type="code",
            redirect_uri="https://app.acme.com/auth/callback",
            scope="projects:read projects:write",
            state="st_9f4d3a206b2e4a7e8c91",
            response_mode="query",
            code_challenge="Z_P4EKbGwIkA01e3Y5fp4tMCvn_Ae5nUw7qY7XwkTrQ",
            organization_slug="tsrqponmlkjihgfedcba",
            resource="https://mcp.supabase.com/projects",
        )
        """
        _response = self._raw_client.v1authorize_user(
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            response_mode=response_mode,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            organization_slug=organization_slug,
            target_flow=target_flow,
            resource=resource,
            request_options=request_options,
        )
        return _response.data

    def v1exchange_oauth_token(
        self,
        *,
        grant_type: typing.Optional[OAuthTokenBodyGrantType] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        assertion: typing.Optional[str] = OMIT,
        resource: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OAuthTokenResponseOutput:
        """
        Supports `authorization_code`, `refresh_token`, and `urn:ietf:params:oauth:grant-type:jwt-bearer` grant types. The `jwt-bearer` grant type (IDJAG — identity-directed JWT assertion) is in beta and available on Team and Enterprise plans only.

        Parameters
        ----------
        grant_type : typing.Optional[OAuthTokenBodyGrantType]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        code : typing.Optional[str]

        code_verifier : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        refresh_token : typing.Optional[str]

        assertion : typing.Optional[str]
            IDJAG assertion JWT for grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer. Beta - available on Team and Enterprise plans only.

        resource : typing.Optional[str]
            Resource indicator for MCP (Model Context Protocol) clients

        scope : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuthTokenResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.o_auth.v1exchange_oauth_token(
            grant_type="authorization_code",
            client_id="66666666-6666-4666-8666-666666666666",
            client_secret="sb_secret_live_example_9f4d3a206b2e4a7e8c91",
            code="oauth_code_9f4d3a206b2e4a7e8c91",
            code_verifier="qW0Z6d9pQnW0mL1dK1q9wFq6Yz2nV5rA8jT3mP7sH4c",
            redirect_uri="https://app.acme.com/auth/callback",
            scope="projects:read projects:write",
        )
        """
        _response = self._raw_client.v1exchange_oauth_token(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            code_verifier=code_verifier,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
            assertion=assertion,
            resource=resource,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    def v1revoke_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        client_id : str

        client_secret : str

        refresh_token : str

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
        client.o_auth.v1revoke_token(
            client_id="66666666-6666-4666-8666-666666666666",
            client_secret="sb_secret_live_example_9f4d3a206b2e4a7e8c91",
            refresh_token="oauth_refresh_9f4d3a206b2e4a7e8c91",
        )
        """
        _response = self._raw_client.v1revoke_token(
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
            request_options=request_options,
        )
        return _response.data

    def v1oauth_authorize_project_claim(
        self,
        *,
        project_ref: str,
        client_id: str,
        response_type: V1OauthAuthorizeProjectClaimRequestResponseType,
        redirect_uri: str,
        state: typing.Optional[str] = None,
        response_mode: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Initiates the OAuth authorization flow for the specified provider. After successful authentication, the user can claim ownership of the specified project.

        Parameters
        ----------
        project_ref : str
            Project ref

        client_id : str

        response_type : V1OauthAuthorizeProjectClaimRequestResponseType

        redirect_uri : str

        state : typing.Optional[str]

        response_mode : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod]

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
        client.o_auth.v1oauth_authorize_project_claim(
            project_ref="abcdefghijklmnopqrst",
            client_id="66666666-6666-4666-8666-666666666666",
            response_type="code",
            redirect_uri="https://app.acme.com/auth/callback",
            state="st_9f4d3a206b2e4a7e8c91",
            response_mode="query",
            code_challenge="Z_P4EKbGwIkA01e3Y5fp4tMCvn_Ae5nUw7qY7XwkTrQ",
        )
        """
        _response = self._raw_client.v1oauth_authorize_project_claim(
            project_ref=project_ref,
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            state=state,
            response_mode=response_mode,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
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

    async def v1authorize_user(
        self,
        *,
        client_id: str,
        response_type: V1AuthorizeUserRequestResponseType,
        redirect_uri: str,
        scope: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        response_mode: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[V1AuthorizeUserRequestCodeChallengeMethod] = None,
        organization_slug: typing.Optional[str] = None,
        target_flow: typing.Optional[str] = None,
        resource: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        client_id : str

        response_type : V1AuthorizeUserRequestResponseType

        redirect_uri : str

        scope : typing.Optional[str]

        state : typing.Optional[str]

        response_mode : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[V1AuthorizeUserRequestCodeChallengeMethod]

        organization_slug : typing.Optional[str]
            Organization slug

        target_flow : typing.Optional[str]

        resource : typing.Optional[str]
            Resource indicator for MCP (Model Context Protocol) clients

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
            await client.o_auth.v1authorize_user(
                client_id="66666666-6666-4666-8666-666666666666",
                response_type="code",
                redirect_uri="https://app.acme.com/auth/callback",
                scope="projects:read projects:write",
                state="st_9f4d3a206b2e4a7e8c91",
                response_mode="query",
                code_challenge="Z_P4EKbGwIkA01e3Y5fp4tMCvn_Ae5nUw7qY7XwkTrQ",
                organization_slug="tsrqponmlkjihgfedcba",
                resource="https://mcp.supabase.com/projects",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1authorize_user(
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
            response_mode=response_mode,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            organization_slug=organization_slug,
            target_flow=target_flow,
            resource=resource,
            request_options=request_options,
        )
        return _response.data

    async def v1exchange_oauth_token(
        self,
        *,
        grant_type: typing.Optional[OAuthTokenBodyGrantType] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        refresh_token: typing.Optional[str] = OMIT,
        assertion: typing.Optional[str] = OMIT,
        resource: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OAuthTokenResponseOutput:
        """
        Supports `authorization_code`, `refresh_token`, and `urn:ietf:params:oauth:grant-type:jwt-bearer` grant types. The `jwt-bearer` grant type (IDJAG — identity-directed JWT assertion) is in beta and available on Team and Enterprise plans only.

        Parameters
        ----------
        grant_type : typing.Optional[OAuthTokenBodyGrantType]

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        code : typing.Optional[str]

        code_verifier : typing.Optional[str]

        redirect_uri : typing.Optional[str]

        refresh_token : typing.Optional[str]

        assertion : typing.Optional[str]
            IDJAG assertion JWT for grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer. Beta - available on Team and Enterprise plans only.

        resource : typing.Optional[str]
            Resource indicator for MCP (Model Context Protocol) clients

        scope : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuthTokenResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth.v1exchange_oauth_token(
                grant_type="authorization_code",
                client_id="66666666-6666-4666-8666-666666666666",
                client_secret="sb_secret_live_example_9f4d3a206b2e4a7e8c91",
                code="oauth_code_9f4d3a206b2e4a7e8c91",
                code_verifier="qW0Z6d9pQnW0mL1dK1q9wFq6Yz2nV5rA8jT3mP7sH4c",
                redirect_uri="https://app.acme.com/auth/callback",
                scope="projects:read projects:write",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1exchange_oauth_token(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            code_verifier=code_verifier,
            redirect_uri=redirect_uri,
            refresh_token=refresh_token,
            assertion=assertion,
            resource=resource,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    async def v1revoke_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        client_id : str

        client_secret : str

        refresh_token : str

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
            await client.o_auth.v1revoke_token(
                client_id="66666666-6666-4666-8666-666666666666",
                client_secret="sb_secret_live_example_9f4d3a206b2e4a7e8c91",
                refresh_token="oauth_refresh_9f4d3a206b2e4a7e8c91",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1revoke_token(
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
            request_options=request_options,
        )
        return _response.data

    async def v1oauth_authorize_project_claim(
        self,
        *,
        project_ref: str,
        client_id: str,
        response_type: V1OauthAuthorizeProjectClaimRequestResponseType,
        redirect_uri: str,
        state: typing.Optional[str] = None,
        response_mode: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Initiates the OAuth authorization flow for the specified provider. After successful authentication, the user can claim ownership of the specified project.

        Parameters
        ----------
        project_ref : str
            Project ref

        client_id : str

        response_type : V1OauthAuthorizeProjectClaimRequestResponseType

        redirect_uri : str

        state : typing.Optional[str]

        response_mode : typing.Optional[str]

        code_challenge : typing.Optional[str]

        code_challenge_method : typing.Optional[V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod]

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
            await client.o_auth.v1oauth_authorize_project_claim(
                project_ref="abcdefghijklmnopqrst",
                client_id="66666666-6666-4666-8666-666666666666",
                response_type="code",
                redirect_uri="https://app.acme.com/auth/callback",
                state="st_9f4d3a206b2e4a7e8c91",
                response_mode="query",
                code_challenge="Z_P4EKbGwIkA01e3Y5fp4tMCvn_Ae5nUw7qY7XwkTrQ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1oauth_authorize_project_claim(
            project_ref=project_ref,
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            state=state,
            response_mode=response_mode,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            request_options=request_options,
        )
        return _response.data
