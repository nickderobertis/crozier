

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawThirdPartySessionsClient, RawThirdPartySessionsClient
from .types.get_affected_agents_response import GetAffectedAgentsResponse
from .types.get_session_details_response import GetSessionDetailsResponse
from .types.list_third_party_sessions_response import ListThirdPartySessionsResponse
from .types.refresh_third_party_session_response import RefreshThirdPartySessionResponse
from .types.terminate_session_response import TerminateSessionResponse


class ThirdPartySessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawThirdPartySessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawThirdPartySessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawThirdPartySessionsClient
        """
        return self._raw_client

    def list_third_party_sessions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListThirdPartySessionsResponse:
        """
        Returns a list of all configured third-party OAuth2 services along with the current user's session status for each service.

        For services where the user has an active session, includes:

        - Session initiation timestamp
        - Token expiration status
        - Number of agents depending on this session, derived only from grants owned by the authenticated session principal
        - Encryption status indicator

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListThirdPartySessionsResponse
            List of services with session status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.third_party_sessions.list_third_party_sessions()
        """
        _response = self._raw_client.list_third_party_sessions(request_options=request_options)
        return _response.data

    def initiate_o_auth2flow(
        self, service_id: str, *, redirect_uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Initiates an OAuth2 authorization code flow with PKCE for the specified third-party service. Redirects the user to the third-party's authorization endpoint.

        PKCE applies to every service; the authorization-code exchange presents a client credential only for confidential services.

        The flow:

        1. Generates PKCE code verifier and challenge
        2. Creates JWE state token containing principal, PKCE verifier, service ID, redirect_uri
        3. Redirects user to third-party authorization endpoint

        The redirect_uri parameter must match the host of the incoming request (same-origin validation).

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        redirect_uri : str
            URI to redirect user after OAuth2 flow completes.
            Must match the host of the incoming request (same-origin validation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.third_party_sessions.initiate_o_auth2flow(
            service_id="550e8400-e29b-41d4-a716-446655440000",
            redirect_uri="https://broker.example.com/sessions",
        )
        """
        _response = self._raw_client.initiate_o_auth2flow(
            service_id, redirect_uri=redirect_uri, request_options=request_options
        )
        return _response.data

    def handle_o_auth2callback(
        self,
        service_id: str,
        *,
        code: str,
        state: str,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Processes the OAuth2 callback after user authorization at the third-party.

        PKCE applies to every service; the authorization-code exchange presents a client credential only for confidential services.

        Validates:

        - State token decrypts successfully (JWE)
        - State token is not expired
        - Principal in token matches current authenticated principal (CSRF protection)
        - Service ID in token matches path parameter

        On success:

        - Exchanges authorization code for access/refresh tokens (with PKCE)
        - Encrypts tokens using EncryptionPort
        - Stores session in database
        - Redirects user to original redirect_uri with success status

        On error:

        - Redirects user to sessions page with error message

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        code : str
            OAuth2 authorization code from third-party

        state : str
            JWE state token (must match token from authorize request)

        error : typing.Optional[str]
            OAuth2 error code from third-party (if authorization failed)

        error_description : typing.Optional[str]
            OAuth2 error description from third-party

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.third_party_sessions.handle_o_auth2callback(
            service_id="serviceId",
            code="code",
            state="state",
            error="access_denied",
            error_description="The user denied the request",
        )
        """
        _response = self._raw_client.handle_o_auth2callback(
            service_id,
            code=code,
            state=state,
            error=error,
            error_description=error_description,
            request_options=request_options,
        )
        return _response.data

    def get_session_details(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSessionDetailsResponse:
        """
        Returns detailed information about the user's session with a third-party service, including only agents with grants owned by the authenticated session principal that depend on this session.
        Used to populate the session card and termination warning dialog.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSessionDetailsResponse
            Session details retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.third_party_sessions.get_session_details(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.get_session_details(service_id, request_options=request_options)
        return _response.data

    def terminate_session(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TerminateSessionResponse:
        """
        Terminates the user's session with a third-party service by deleting stored tokens.
        Returns information about affected agents for the confirmation dialog shown before this request.

        Note: This does not revoke tokens at the third-party service.

        Agents that were using this session will detect the missing session and request re-authentication.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TerminateSessionResponse
            Session terminated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.third_party_sessions.terminate_session(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.terminate_session(service_id, request_options=request_options)
        return _response.data

    def refresh_third_party_session(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RefreshThirdPartySessionResponse:
        """
        Forces an immediate OAuth2 access-token refresh for the user's session with a
        third-party service, using the stored refresh token via the RFC 6749 refresh_token
        grant. Unlike the transparent refresh performed during token exchange, this refreshes
        even when the current access token has not yet expired. Requires a stored, non-expired
        refresh token.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefreshThirdPartySessionResponse
            Access token refreshed successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.third_party_sessions.refresh_third_party_session(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.refresh_third_party_session(service_id, request_options=request_options)
        return _response.data

    def get_affected_agents(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAffectedAgentsResponse:
        """
        Returns a list of agents that would lose access if the user terminates their session with this third-party service.
        Used to populate the termination warning dialog.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAffectedAgentsResponse
            List of affected agents

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.third_party_sessions.get_affected_agents(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.get_affected_agents(service_id, request_options=request_options)
        return _response.data


class AsyncThirdPartySessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawThirdPartySessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawThirdPartySessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawThirdPartySessionsClient
        """
        return self._raw_client

    async def list_third_party_sessions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListThirdPartySessionsResponse:
        """
        Returns a list of all configured third-party OAuth2 services along with the current user's session status for each service.

        For services where the user has an active session, includes:

        - Session initiation timestamp
        - Token expiration status
        - Number of agents depending on this session, derived only from grants owned by the authenticated session principal
        - Encryption status indicator

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListThirdPartySessionsResponse
            List of services with session status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.third_party_sessions.list_third_party_sessions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_third_party_sessions(request_options=request_options)
        return _response.data

    async def initiate_o_auth2flow(
        self, service_id: str, *, redirect_uri: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Initiates an OAuth2 authorization code flow with PKCE for the specified third-party service. Redirects the user to the third-party's authorization endpoint.

        PKCE applies to every service; the authorization-code exchange presents a client credential only for confidential services.

        The flow:

        1. Generates PKCE code verifier and challenge
        2. Creates JWE state token containing principal, PKCE verifier, service ID, redirect_uri
        3. Redirects user to third-party authorization endpoint

        The redirect_uri parameter must match the host of the incoming request (same-origin validation).

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        redirect_uri : str
            URI to redirect user after OAuth2 flow completes.
            Must match the host of the incoming request (same-origin validation).

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
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.third_party_sessions.initiate_o_auth2flow(
                service_id="550e8400-e29b-41d4-a716-446655440000",
                redirect_uri="https://broker.example.com/sessions",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.initiate_o_auth2flow(
            service_id, redirect_uri=redirect_uri, request_options=request_options
        )
        return _response.data

    async def handle_o_auth2callback(
        self,
        service_id: str,
        *,
        code: str,
        state: str,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Processes the OAuth2 callback after user authorization at the third-party.

        PKCE applies to every service; the authorization-code exchange presents a client credential only for confidential services.

        Validates:

        - State token decrypts successfully (JWE)
        - State token is not expired
        - Principal in token matches current authenticated principal (CSRF protection)
        - Service ID in token matches path parameter

        On success:

        - Exchanges authorization code for access/refresh tokens (with PKCE)
        - Encrypts tokens using EncryptionPort
        - Stores session in database
        - Redirects user to original redirect_uri with success status

        On error:

        - Redirects user to sessions page with error message

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        code : str
            OAuth2 authorization code from third-party

        state : str
            JWE state token (must match token from authorize request)

        error : typing.Optional[str]
            OAuth2 error code from third-party (if authorization failed)

        error_description : typing.Optional[str]
            OAuth2 error description from third-party

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
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.third_party_sessions.handle_o_auth2callback(
                service_id="serviceId",
                code="code",
                state="state",
                error="access_denied",
                error_description="The user denied the request",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.handle_o_auth2callback(
            service_id,
            code=code,
            state=state,
            error=error,
            error_description=error_description,
            request_options=request_options,
        )
        return _response.data

    async def get_session_details(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSessionDetailsResponse:
        """
        Returns detailed information about the user's session with a third-party service, including only agents with grants owned by the authenticated session principal that depend on this session.
        Used to populate the session card and termination warning dialog.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSessionDetailsResponse
            Session details retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.third_party_sessions.get_session_details(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_session_details(service_id, request_options=request_options)
        return _response.data

    async def terminate_session(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TerminateSessionResponse:
        """
        Terminates the user's session with a third-party service by deleting stored tokens.
        Returns information about affected agents for the confirmation dialog shown before this request.

        Note: This does not revoke tokens at the third-party service.

        Agents that were using this session will detect the missing session and request re-authentication.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TerminateSessionResponse
            Session terminated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.third_party_sessions.terminate_session(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.terminate_session(service_id, request_options=request_options)
        return _response.data

    async def refresh_third_party_session(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RefreshThirdPartySessionResponse:
        """
        Forces an immediate OAuth2 access-token refresh for the user's session with a
        third-party service, using the stored refresh token via the RFC 6749 refresh_token
        grant. Unlike the transparent refresh performed during token exchange, this refreshes
        even when the current access token has not yet expired. Requires a stored, non-expired
        refresh token.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefreshThirdPartySessionResponse
            Access token refreshed successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.third_party_sessions.refresh_third_party_session(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_third_party_session(service_id, request_options=request_options)
        return _response.data

    async def get_affected_agents(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAffectedAgentsResponse:
        """
        Returns a list of agents that would lose access if the user terminates their session with this third-party service.
        Used to populate the termination warning dialog.

        Parameters
        ----------
        service_id : str
            UUID of the third-party OAuth2 service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAffectedAgentsResponse
            List of affected agents

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.third_party_sessions.get_affected_agents(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_affected_agents(service_id, request_options=request_options)
        return _response.data
