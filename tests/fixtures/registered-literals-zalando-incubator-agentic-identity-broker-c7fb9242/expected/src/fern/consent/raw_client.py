

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.create_or_update_grant_response import CreateOrUpdateGrantResponse
from ..types.get_agent_delegations_response import GetAgentDelegationsResponse
from ..types.get_agent_detail_response import GetAgentDetailResponse
from ..types.get_agent_grants_response import GetAgentGrantsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConsentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_agent_delegations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAgentDelegationsResponse]:
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
        HttpResponse[GetAgentDelegationsResponse]
            Agent delegations retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/consent/agents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentDelegationsResponse,
                    parse_obj_as(
                        type_=GetAgentDelegationsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_agent_detail(
        self,
        agent_id: str,
        *,
        session_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentDetailResponse]:
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
        HttpResponse[GetAgentDetailResponse]
            Agent detail retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/consent/agents/{encode_path_param(agent_id)}",
            method="GET",
            params={
                "session_token": session_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentDetailResponse,
                    parse_obj_as(
                        type_=GetAgentDetailResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_agent_grants(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAgentGrantsResponse]:
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
        HttpResponse[GetAgentGrantsResponse]
            Grants retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/consent/agents/{encode_path_param(agent_id)}/grants",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentGrantsResponse,
                    parse_obj_as(
                        type_=GetAgentGrantsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_or_update_grant(
        self,
        agent_id: str,
        *,
        granted_permission_sets: typing.Dict[str, typing.Sequence[str]],
        session_token: typing.Optional[str] = None,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[CreateOrUpdateGrantResponse]]:
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
        HttpResponse[typing.Optional[CreateOrUpdateGrantResponse]]
            Grant created or updated. When session_token was provided, response includes redirect_url containing the original authorization URL for flow resumption.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/consent/agents/{encode_path_param(agent_id)}/grants",
            method="POST",
            params={
                "session_token": session_token,
            },
            json={
                "granted_permission_sets": granted_permission_sets,
                "valid_until": valid_until,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CreateOrUpdateGrantResponse],
                    parse_obj_as(
                        type_=typing.Optional[CreateOrUpdateGrantResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def revoke_agent_grant(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/consent/agents/{encode_path_param(agent_id)}/grants",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawConsentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_agent_delegations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAgentDelegationsResponse]:
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
        AsyncHttpResponse[GetAgentDelegationsResponse]
            Agent delegations retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/consent/agents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentDelegationsResponse,
                    parse_obj_as(
                        type_=GetAgentDelegationsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_agent_detail(
        self,
        agent_id: str,
        *,
        session_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAgentDetailResponse]:
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
        AsyncHttpResponse[GetAgentDetailResponse]
            Agent detail retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/consent/agents/{encode_path_param(agent_id)}",
            method="GET",
            params={
                "session_token": session_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentDetailResponse,
                    parse_obj_as(
                        type_=GetAgentDetailResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_agent_grants(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAgentGrantsResponse]:
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
        AsyncHttpResponse[GetAgentGrantsResponse]
            Grants retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/consent/agents/{encode_path_param(agent_id)}/grants",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentGrantsResponse,
                    parse_obj_as(
                        type_=GetAgentGrantsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_or_update_grant(
        self,
        agent_id: str,
        *,
        granted_permission_sets: typing.Dict[str, typing.Sequence[str]],
        session_token: typing.Optional[str] = None,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[CreateOrUpdateGrantResponse]]:
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
        AsyncHttpResponse[typing.Optional[CreateOrUpdateGrantResponse]]
            Grant created or updated. When session_token was provided, response includes redirect_url containing the original authorization URL for flow resumption.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/consent/agents/{encode_path_param(agent_id)}/grants",
            method="POST",
            params={
                "session_token": session_token,
            },
            json={
                "granted_permission_sets": granted_permission_sets,
                "valid_until": valid_until,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CreateOrUpdateGrantResponse],
                    parse_obj_as(
                        type_=typing.Optional[CreateOrUpdateGrantResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def revoke_agent_grant(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/consent/agents/{encode_path_param(agent_id)}/grants",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
