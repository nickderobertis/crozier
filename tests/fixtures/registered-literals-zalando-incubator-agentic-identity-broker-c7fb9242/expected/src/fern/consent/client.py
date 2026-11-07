

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_or_update_grant_response import CreateOrUpdateGrantResponse
from ..types.get_agent_delegations_response import GetAgentDelegationsResponse
from ..types.get_agent_detail_response import GetAgentDetailResponse
from ..types.get_agent_grants_response import GetAgentGrantsResponse
from .raw_client import AsyncRawConsentClient, RawConsentClient


OMIT = typing.cast(typing.Any, ...)


class ConsentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConsentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConsentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConsentClient
        """
        return self._raw_client

    def get_agent_delegations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentDelegationsResponse:
        """
        Returns a list of all agents to which the current user has granted access.

        Each agent delegation includes:

        - **Agent ID**: Unique identifier for the agent
        - **Display Name**: Human-readable agent name
        - **Logo URL**: Optional agent logo/icon
        - **Active Grant Count**: Number of third-party services delegated
        - **Last Modified**: When the delegation was last updated
        - **Expires At**: Optional expiration date (null = indefinite)

        **Response Characteristics**:

        - Returns empty array if user has no active delegations
        - Only includes agents with at least one active grant
        - Ordered by display name in ascending order. Agents with the same display name are ordered by agent ID in ascending order.

        **Use Cases**:

        - Dashboard showing all active agent delegations
        - Quick overview of user's consent status
        - Navigation to detailed agent management

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentDelegationsResponse
            Agent delegations retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.consent.get_agent_delegations()
        """
        _response = self._raw_client.get_agent_delegations(request_options=request_options)
        return _response.data

    def get_agent_detail(
        self,
        agent_id: str,
        *,
        session_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAgentDetailResponse:
        """
        Returns detailed information about a specific agent and all available third-party OAuth2 services that can be delegated to that agent.

        **Agent Detail Includes**:

        - Agent metadata (name, description, logo)
        - Governance documentation URL
        - User documentation URL
        - Agent interface URL

        **Service Information Includes**:

        - Service ID (UUID)
        - Service name (e.g., "Google Drive", "GitHub")
        - Service logo URL
        - The OAuth2 permissions the agent can receive for the service, with human-readable descriptions. For a `require_all_scopes` requirement, this is the sorted, deduplicated union from this agent's assigned Permission Sets that cover that service.

        **Use Cases**:

        - Display agent information before granting access
        - Show available services and permissions
        - Help users make informed consent decisions
        - Link to governance and documentation

        Parameters
        ----------
        agent_id : str
            Unique agent identifier (UUID format).
            The agent ID identifies a specific agent in the system.
            Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.

        session_token : typing.Optional[str]
            JWE authorization session token for all agent modes (local, proxy, CIMD). When present, the response includes authorization context extracted from the decrypted token (agent_id, principal, original_url). For CIMD agents, also includes CIMD metadata (client_id_url, redirect_uri, verified_domain, requested_scopes, logo_uri). Present whenever the user arrived via an OAuth2 authorization redirect.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentDetailResponse
            Agent detail retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.consent.get_agent_detail(
            agent_id="550e8400-e29b-41d4-a716-446655440000",
            session_token="eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0...",
        )
        """
        _response = self._raw_client.get_agent_detail(
            agent_id, session_token=session_token, request_options=request_options
        )
        return _response.data

    def get_agent_grants(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentGrantsResponse:
        """
        Returns all active grants the authenticated user has granted to the specified agent.

        **Grant Information Includes**:

        - Grant ID (UUID)
        - Principal (user identifier)
        - Agent ID
        - Valid until date (null = indefinite)
        - Delegated OAuth2 tokens (services and scopes)
        - Creation timestamp
        - Last update timestamp

        **Response Characteristics**:

        - Returns empty array if no grants exist
        - Only includes active (non-expired) grants
        - Typically one grant per user-agent pair (upsert semantics)

        **Use Cases**:

        - Check if user has existing grants before showing consent UI
        - Pre-populate consent form with current grants
        - Display current delegation status

        Parameters
        ----------
        agent_id : str
            Unique agent identifier (UUID format).
            The agent ID identifies a specific agent in the system.
            Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentGrantsResponse
            Grants retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.consent.get_agent_grants(
            agent_id="550e8400-e29b-41d4-a716-446655440000",
        )
        """
        _response = self._raw_client.get_agent_grants(agent_id, request_options=request_options)
        return _response.data

    def create_or_update_grant(
        self,
        agent_id: str,
        *,
        granted_permission_sets: typing.Dict[str, typing.Sequence[str]],
        session_token: typing.Optional[str] = None,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[CreateOrUpdateGrantResponse]:
        """
        Creates a new grant or updates an existing grant for the specified agent.

        **Upsert Semantics**:

        - One grant per user-agent pair
        - Subsequent POSTs update the existing grant

        - Previous granted permission sets are replaced (not merged)

        **Grant Expiration**:

        - `valid_until` is optional (omit for indefinite grant)
        - Must be a future date if specified
        - Expired grants are automatically filtered out

        **Revocation (Special Case)**:

        - Submit empty `granted_permission_sets` object to revoke

        - Returns `204 No Content` on successful revocation
        - Deletes the grant entirely

        **Session-Based Consent (FR-029)**:

        - Use `session_token` query parameter to resume an OAuth2 authorization flow after consent
        - Applies to all agent modes: local, proxy, and CIMD
        - Token is a self-contained JWE carrying all authorization session claims (agent_id, principal, original_url, TTL) — no server-side session lookup is performed
        - Returns HTTP 201 with `redirect_url` field containing the original authorization URL (with original `state`, `redirect_uri`, PKCE, and `client_id` parameters intact)
        - Frontend must navigate to `redirect_url` using `window.location.href` to resume the OAuth2 flow
        - Returns `400 Bad Request` with error code `session_expired` if the token is invalid or expired
        - Returns `400 Bad Request` if the session agent does not match the agent in the URL path
        - Returns `403 Forbidden` if the session principal does not match the authenticated user

        **Standalone Consent Management**:

        - Requests without `session_token` are treated as direct consent-management operations (not authorization resumption)
        - Returns HTTP 201 with grant data only (no `redirect_url` field)

        **Validation**:

        - All service IDs must exist and be available to the agent
        - All scopes must be valid for the specified services
        - At least one scope required per service
        - Returns `400 Bad Request` with details if validation fails

        **Use Cases**:

        - User grants initial access to an agent
        - User updates existing grant (adds/removes services or scopes)
        - User revokes all access to an agent
        - Redirect to authorization flow continuation URL after consent approval

        Parameters
        ----------
        agent_id : str
            Unique agent identifier (UUID format).
            The agent ID identifies a specific agent in the system.
            Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.

        granted_permission_sets : typing.Dict[str, typing.Sequence[str]]
            Map of permission sets to grant to the agent. Keys are permission set UUIDs, values are arrays of service UUIDs included in each permission set grant.

            **Special Case**: Empty object `{}` revokes the grant entirely
            and returns `204 No Content`.
            **Special Case**: Empty array `[]` revokes the grant entirely and returns `204 No Content`.
            **Validation**:
            - Each permission set ID must exist and be assigned to the agent
            - Each service ID must be valid for the specified permission set

        session_token : typing.Optional[str]
            JWE authorization session token (FR-029). When present, the grant endpoint decrypts the token to resolve the redirect target. Returns 400 if the token is invalid or expired; 400 if the session agent does not match the requested agent; 403 if the session principal does not match the authenticated caller.

        valid_until : typing.Optional[dt.datetime]
            Optional grant expiration (ISO 8601 format).

            **Validation**:

            - Must be a future date if specified
            - Omit for indefinite grant (no expiration)

            **Behavior**:

            - Expired grants are automatically filtered out in queries
            - Users can extend expiration by updating the grant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CreateOrUpdateGrantResponse]
            Grant created or updated. When session_token was provided, response includes redirect_url containing the original authorization URL for flow resumption.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.consent.create_or_update_grant(
            agent_id="550e8400-e29b-41d4-a716-446655440000",
            granted_permission_sets={
                "770e8400-e29b-41d4-a716-446655440001": [
                    "880e8400-e29b-41d4-a716-446655440010",
                    "880e8400-e29b-41d4-a716-446655440011",
                ],
                "770e8400-e29b-41d4-a716-446655440002": [
                    "880e8400-e29b-41d4-a716-446655440012"
                ],
            },
        )
        """
        _response = self._raw_client.create_or_update_grant(
            agent_id,
            granted_permission_sets=granted_permission_sets,
            session_token=session_token,
            valid_until=valid_until,
            request_options=request_options,
        )
        return _response.data

    def revoke_agent_grant(self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Permanently deletes the authenticated user's grant for the specified agent.
        After revocation, the agent can no longer perform token exchanges on behalf of
        the user.

        **Important**: This action only removes the delegation grant. Connected OAuth2
        sessions (e.g., GitHub, Google) remain active and are NOT terminated by this
        action. Users may manage OAuth2 sessions separately.

        **Idempotency**: Non-idempotent — returns 404 if no grant exists. To silently
        revoke if a grant exists, use `POST /api/consent/agents/{agent-id}/grants` with
        an empty `granted_permission_sets` object.

        **Security**: Only the grant owner may revoke. The principal is derived from the
        `X-Remote-User` authentication header. Cross-user revocation is not possible —
        grants are scoped to the authenticated principal.

        Parameters
        ----------
        agent_id : str
            Unique agent identifier (UUID format).
            The agent ID identifies a specific agent in the system.
            Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.

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
        client.consent.revoke_agent_grant(
            agent_id="550e8400-e29b-41d4-a716-446655440000",
        )
        """
        _response = self._raw_client.revoke_agent_grant(agent_id, request_options=request_options)
        return _response.data


class AsyncConsentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConsentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConsentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConsentClient
        """
        return self._raw_client

    async def get_agent_delegations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentDelegationsResponse:
        """
        Returns a list of all agents to which the current user has granted access.

        Each agent delegation includes:

        - **Agent ID**: Unique identifier for the agent
        - **Display Name**: Human-readable agent name
        - **Logo URL**: Optional agent logo/icon
        - **Active Grant Count**: Number of third-party services delegated
        - **Last Modified**: When the delegation was last updated
        - **Expires At**: Optional expiration date (null = indefinite)

        **Response Characteristics**:

        - Returns empty array if user has no active delegations
        - Only includes agents with at least one active grant
        - Ordered by display name in ascending order. Agents with the same display name are ordered by agent ID in ascending order.

        **Use Cases**:

        - Dashboard showing all active agent delegations
        - Quick overview of user's consent status
        - Navigation to detailed agent management

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentDelegationsResponse
            Agent delegations retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.consent.get_agent_delegations()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent_delegations(request_options=request_options)
        return _response.data

    async def get_agent_detail(
        self,
        agent_id: str,
        *,
        session_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAgentDetailResponse:
        """
        Returns detailed information about a specific agent and all available third-party OAuth2 services that can be delegated to that agent.

        **Agent Detail Includes**:

        - Agent metadata (name, description, logo)
        - Governance documentation URL
        - User documentation URL
        - Agent interface URL

        **Service Information Includes**:

        - Service ID (UUID)
        - Service name (e.g., "Google Drive", "GitHub")
        - Service logo URL
        - The OAuth2 permissions the agent can receive for the service, with human-readable descriptions. For a `require_all_scopes` requirement, this is the sorted, deduplicated union from this agent's assigned Permission Sets that cover that service.

        **Use Cases**:

        - Display agent information before granting access
        - Show available services and permissions
        - Help users make informed consent decisions
        - Link to governance and documentation

        Parameters
        ----------
        agent_id : str
            Unique agent identifier (UUID format).
            The agent ID identifies a specific agent in the system.
            Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.

        session_token : typing.Optional[str]
            JWE authorization session token for all agent modes (local, proxy, CIMD). When present, the response includes authorization context extracted from the decrypted token (agent_id, principal, original_url). For CIMD agents, also includes CIMD metadata (client_id_url, redirect_uri, verified_domain, requested_scopes, logo_uri). Present whenever the user arrived via an OAuth2 authorization redirect.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentDetailResponse
            Agent detail retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.consent.get_agent_detail(
                agent_id="550e8400-e29b-41d4-a716-446655440000",
                session_token="eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0...",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent_detail(
            agent_id, session_token=session_token, request_options=request_options
        )
        return _response.data

    async def get_agent_grants(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentGrantsResponse:
        """
        Returns all active grants the authenticated user has granted to the specified agent.

        **Grant Information Includes**:

        - Grant ID (UUID)
        - Principal (user identifier)
        - Agent ID
        - Valid until date (null = indefinite)
        - Delegated OAuth2 tokens (services and scopes)
        - Creation timestamp
        - Last update timestamp

        **Response Characteristics**:

        - Returns empty array if no grants exist
        - Only includes active (non-expired) grants
        - Typically one grant per user-agent pair (upsert semantics)

        **Use Cases**:

        - Check if user has existing grants before showing consent UI
        - Pre-populate consent form with current grants
        - Display current delegation status

        Parameters
        ----------
        agent_id : str
            Unique agent identifier (UUID format).
            The agent ID identifies a specific agent in the system.
            Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentGrantsResponse
            Grants retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.consent.get_agent_grants(
                agent_id="550e8400-e29b-41d4-a716-446655440000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent_grants(agent_id, request_options=request_options)
        return _response.data

    async def create_or_update_grant(
        self,
        agent_id: str,
        *,
        granted_permission_sets: typing.Dict[str, typing.Sequence[str]],
        session_token: typing.Optional[str] = None,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[CreateOrUpdateGrantResponse]:
        """
        Creates a new grant or updates an existing grant for the specified agent.

        **Upsert Semantics**:

        - One grant per user-agent pair
        - Subsequent POSTs update the existing grant

        - Previous granted permission sets are replaced (not merged)

        **Grant Expiration**:

        - `valid_until` is optional (omit for indefinite grant)
        - Must be a future date if specified
        - Expired grants are automatically filtered out

        **Revocation (Special Case)**:

        - Submit empty `granted_permission_sets` object to revoke

        - Returns `204 No Content` on successful revocation
        - Deletes the grant entirely

        **Session-Based Consent (FR-029)**:

        - Use `session_token` query parameter to resume an OAuth2 authorization flow after consent
        - Applies to all agent modes: local, proxy, and CIMD
        - Token is a self-contained JWE carrying all authorization session claims (agent_id, principal, original_url, TTL) — no server-side session lookup is performed
        - Returns HTTP 201 with `redirect_url` field containing the original authorization URL (with original `state`, `redirect_uri`, PKCE, and `client_id` parameters intact)
        - Frontend must navigate to `redirect_url` using `window.location.href` to resume the OAuth2 flow
        - Returns `400 Bad Request` with error code `session_expired` if the token is invalid or expired
        - Returns `400 Bad Request` if the session agent does not match the agent in the URL path
        - Returns `403 Forbidden` if the session principal does not match the authenticated user

        **Standalone Consent Management**:

        - Requests without `session_token` are treated as direct consent-management operations (not authorization resumption)
        - Returns HTTP 201 with grant data only (no `redirect_url` field)

        **Validation**:

        - All service IDs must exist and be available to the agent
        - All scopes must be valid for the specified services
        - At least one scope required per service
        - Returns `400 Bad Request` with details if validation fails

        **Use Cases**:

        - User grants initial access to an agent
        - User updates existing grant (adds/removes services or scopes)
        - User revokes all access to an agent
        - Redirect to authorization flow continuation URL after consent approval

        Parameters
        ----------
        agent_id : str
            Unique agent identifier (UUID format).
            The agent ID identifies a specific agent in the system.
            Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.

        granted_permission_sets : typing.Dict[str, typing.Sequence[str]]
            Map of permission sets to grant to the agent. Keys are permission set UUIDs, values are arrays of service UUIDs included in each permission set grant.

            **Special Case**: Empty object `{}` revokes the grant entirely
            and returns `204 No Content`.
            **Special Case**: Empty array `[]` revokes the grant entirely and returns `204 No Content`.
            **Validation**:
            - Each permission set ID must exist and be assigned to the agent
            - Each service ID must be valid for the specified permission set

        session_token : typing.Optional[str]
            JWE authorization session token (FR-029). When present, the grant endpoint decrypts the token to resolve the redirect target. Returns 400 if the token is invalid or expired; 400 if the session agent does not match the requested agent; 403 if the session principal does not match the authenticated caller.

        valid_until : typing.Optional[dt.datetime]
            Optional grant expiration (ISO 8601 format).

            **Validation**:

            - Must be a future date if specified
            - Omit for indefinite grant (no expiration)

            **Behavior**:

            - Expired grants are automatically filtered out in queries
            - Users can extend expiration by updating the grant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CreateOrUpdateGrantResponse]
            Grant created or updated. When session_token was provided, response includes redirect_url containing the original authorization URL for flow resumption.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.consent.create_or_update_grant(
                agent_id="550e8400-e29b-41d4-a716-446655440000",
                granted_permission_sets={
                    "770e8400-e29b-41d4-a716-446655440001": [
                        "880e8400-e29b-41d4-a716-446655440010",
                        "880e8400-e29b-41d4-a716-446655440011",
                    ],
                    "770e8400-e29b-41d4-a716-446655440002": [
                        "880e8400-e29b-41d4-a716-446655440012"
                    ],
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update_grant(
            agent_id,
            granted_permission_sets=granted_permission_sets,
            session_token=session_token,
            valid_until=valid_until,
            request_options=request_options,
        )
        return _response.data

    async def revoke_agent_grant(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Permanently deletes the authenticated user's grant for the specified agent.
        After revocation, the agent can no longer perform token exchanges on behalf of
        the user.

        **Important**: This action only removes the delegation grant. Connected OAuth2
        sessions (e.g., GitHub, Google) remain active and are NOT terminated by this
        action. Users may manage OAuth2 sessions separately.

        **Idempotency**: Non-idempotent — returns 404 if no grant exists. To silently
        revoke if a grant exists, use `POST /api/consent/agents/{agent-id}/grants` with
        an empty `granted_permission_sets` object.

        **Security**: Only the grant owner may revoke. The principal is derived from the
        `X-Remote-User` authentication header. Cross-user revocation is not possible —
        grants are scoped to the authenticated principal.

        Parameters
        ----------
        agent_id : str
            Unique agent identifier (UUID format).
            The agent ID identifies a specific agent in the system.
            Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.

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
            await client.consent.revoke_agent_grant(
                agent_id="550e8400-e29b-41d4-a716-446655440000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_agent_grant(agent_id, request_options=request_options)
        return _response.data
