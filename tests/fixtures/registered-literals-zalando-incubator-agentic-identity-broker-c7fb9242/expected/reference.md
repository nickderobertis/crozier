# Reference
## Health
<details><summary><code>client.health.<a href="src/fern/health/client.py">get_health</a>() -> HealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current health status of the end-user HTTP server.

This endpoint does not require authentication and is intended for:

- Load balancer health checks
- Kubernetes liveness/readiness probes
- Monitoring systems
- Service discovery health validation

**Status Codes**:

- `200 OK`: Server is healthy and accepting requests
- `503 Service Unavailable`: Server is starting, shutting down, or unhealthy

**Health States**:

- `healthy`: Server is operational and processing requests normally
- `starting`: Server is initializing (binding to port, setting up routes)
- `shutting_down`: Graceful shutdown in progress, completing in-flight requests
- `unhealthy`: Server encountered an error and requires restart

In proxy and hybrid OAuth2 modes, the response may also include component-level health in `components`. The `upstream_jwks` component reports `healthy` or `degraded` without changing the top-level server lifecycle status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.health.get_health()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## User
<details><summary><code>client.user.<a href="src/fern/user/client.py">get_current_user</a>() -> GetUserInfoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about the currently authenticated user.

The user information includes:

- **Principal**: Unique identifier (email, UUID, etc.) from authentication system
- **Display Name**: Human-readable name for display in UI
- **Picture URL**: Optional avatar/profile picture URL

The principal is extracted from the `X-Remote-User` header set by the upstream authentication proxy (oauth2-proxy, nginx, etc.).

**Use Cases**:

- Display user info in application header
- Show "logged in as" indicators
- Personalize UI with user's name/avatar
- Verify authentication status
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.user.get_current_user()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Consent
<details><summary><code>client.consent.<a href="src/fern/consent/client.py">get_agent_delegations</a>() -> GetAgentDelegationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consent.get_agent_delegations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.consent.<a href="src/fern/consent/client.py">get_agent_detail</a>(...) -> GetAgentDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consent.get_agent_detail(
    agent_id="550e8400-e29b-41d4-a716-446655440000",
    session_token="eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0...",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 

Unique agent identifier (UUID format).
The agent ID identifies a specific agent in the system. 
Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.
    
</dd>
</dl>

<dl>
<dd>

**session_token:** `typing.Optional[str]` — JWE authorization session token for all agent modes (local, proxy, CIMD). When present, the response includes authorization context extracted from the decrypted token (agent_id, principal, original_url). For CIMD agents, also includes CIMD metadata (client_id_url, redirect_uri, verified_domain, requested_scopes, logo_uri). Present whenever the user arrived via an OAuth2 authorization redirect.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.consent.<a href="src/fern/consent/client.py">get_agent_grants</a>(...) -> GetAgentGrantsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consent.get_agent_grants(
    agent_id="550e8400-e29b-41d4-a716-446655440000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 

Unique agent identifier (UUID format).
The agent ID identifies a specific agent in the system. 
Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.consent.<a href="src/fern/consent/client.py">create_or_update_grant</a>(...) -> typing.Optional[CreateOrUpdateGrantResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consent.create_or_update_grant(
    agent_id="550e8400-e29b-41d4-a716-446655440000",
    granted_permission_sets={
        "770e8400-e29b-41d4-a716-446655440001": [
            "880e8400-e29b-41d4-a716-446655440010",
            "880e8400-e29b-41d4-a716-446655440011"
        ],
        "770e8400-e29b-41d4-a716-446655440002": [
            "880e8400-e29b-41d4-a716-446655440012"
        ]
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 

Unique agent identifier (UUID format).
The agent ID identifies a specific agent in the system. 
Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.
    
</dd>
</dl>

<dl>
<dd>

**granted_permission_sets:** `typing.Dict[str, typing.List[str]]` 

Map of permission sets to grant to the agent. Keys are permission set UUIDs, values are arrays of service UUIDs included in each permission set grant.

**Special Case**: Empty object `{}` revokes the grant entirely
and returns `204 No Content`.
**Special Case**: Empty array `[]` revokes the grant entirely and returns `204 No Content`.
**Validation**:
- Each permission set ID must exist and be assigned to the agent
- Each service ID must be valid for the specified permission set
    
</dd>
</dl>

<dl>
<dd>

**session_token:** `typing.Optional[str]` — JWE authorization session token (FR-029). When present, the grant endpoint decrypts the token to resolve the redirect target. Returns 400 if the token is invalid or expired; 400 if the session agent does not match the requested agent; 403 if the session principal does not match the authenticated caller.
    
</dd>
</dl>

<dl>
<dd>

**valid_until:** `typing.Optional[datetime.datetime]` 

Optional grant expiration (ISO 8601 format).

**Validation**:

- Must be a future date if specified
- Omit for indefinite grant (no expiration)

**Behavior**:

- Expired grants are automatically filtered out in queries
- Users can extend expiration by updating the grant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.consent.<a href="src/fern/consent/client.py">revoke_agent_grant</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.consent.revoke_agent_grant(
    agent_id="550e8400-e29b-41d4-a716-446655440000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 

Unique agent identifier (UUID format).
The agent ID identifies a specific agent in the system. 
Agents are registered in the identity broker and represent AI assistants or automated systems that require delegated access to user resources.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Third-Party Sessions
<details><summary><code>client.third_party_sessions.<a href="src/fern/third_party_sessions/client.py">list_third_party_sessions</a>() -> ListThirdPartySessionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all configured third-party OAuth2 services along with the current user's session status for each service.

For services where the user has an active session, includes:

- Session initiation timestamp
- Token expiration status
- Number of agents depending on this session, derived only from grants owned by the authenticated session principal
- Encryption status indicator
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.third_party_sessions.list_third_party_sessions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.third_party_sessions.<a href="src/fern/third_party_sessions/client.py">initiate_o_auth2flow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates an OAuth2 authorization code flow with PKCE for the specified third-party service. Redirects the user to the third-party's authorization endpoint.

PKCE applies to every service; the authorization-code exchange presents a client credential only for confidential services.

The flow:

1. Generates PKCE code verifier and challenge
2. Creates JWE state token containing principal, PKCE verifier, service ID, redirect_uri
3. Redirects user to third-party authorization endpoint

The redirect_uri parameter must match the host of the incoming request (same-origin validation).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.third_party_sessions.initiate_o_auth2flow(
    service_id="550e8400-e29b-41d4-a716-446655440000",
    redirect_uri="https://broker.example.com/sessions",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_id:** `str` — UUID of the third-party OAuth2 service
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` 

URI to redirect user after OAuth2 flow completes.
Must match the host of the incoming request (same-origin validation).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.third_party_sessions.<a href="src/fern/third_party_sessions/client.py">handle_o_auth2callback</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.third_party_sessions.handle_o_auth2callback(
    service_id="serviceId",
    code="code",
    state="state",
    error="access_denied",
    error_description="The user denied the request",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_id:** `str` — UUID of the third-party OAuth2 service
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — OAuth2 authorization code from third-party
    
</dd>
</dl>

<dl>
<dd>

**state:** `str` — JWE state token (must match token from authorize request)
    
</dd>
</dl>

<dl>
<dd>

**error:** `typing.Optional[str]` — OAuth2 error code from third-party (if authorization failed)
    
</dd>
</dl>

<dl>
<dd>

**error_description:** `typing.Optional[str]` — OAuth2 error description from third-party
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.third_party_sessions.<a href="src/fern/third_party_sessions/client.py">get_session_details</a>(...) -> GetSessionDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns detailed information about the user's session with a third-party service, including only agents with grants owned by the authenticated session principal that depend on this session.
Used to populate the session card and termination warning dialog.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.third_party_sessions.get_session_details(
    service_id="serviceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_id:** `str` — UUID of the third-party OAuth2 service
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.third_party_sessions.<a href="src/fern/third_party_sessions/client.py">terminate_session</a>(...) -> TerminateSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Terminates the user's session with a third-party service by deleting stored tokens. 
Returns information about affected agents for the confirmation dialog shown before this request.

Note: This does not revoke tokens at the third-party service.

Agents that were using this session will detect the missing session and request re-authentication.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.third_party_sessions.terminate_session(
    service_id="serviceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_id:** `str` — UUID of the third-party OAuth2 service
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.third_party_sessions.<a href="src/fern/third_party_sessions/client.py">refresh_third_party_session</a>(...) -> RefreshThirdPartySessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forces an immediate OAuth2 access-token refresh for the user's session with a
third-party service, using the stored refresh token via the RFC 6749 refresh_token
grant. Unlike the transparent refresh performed during token exchange, this refreshes
even when the current access token has not yet expired. Requires a stored, non-expired
refresh token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.third_party_sessions.refresh_third_party_session(
    service_id="serviceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_id:** `str` — UUID of the third-party OAuth2 service
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.third_party_sessions.<a href="src/fern/third_party_sessions/client.py">get_affected_agents</a>(...) -> GetAffectedAgentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of agents that would lose access if the user terminates their session with this third-party service. 
Used to populate the termination warning dialog.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.third_party_sessions.get_affected_agents(
    service_id="serviceId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_id:** `str` — UUID of the third-party OAuth2 service
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OAuth2 Token
<details><summary><code>client.o_auth2token.<a href="src/fern/o_auth2token/client.py">oauth2authorize</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates an OAuth2 authorization code flow. The broker validates the agent,
checks consent, and either redirects to the upstream OAuth2 authorization server
or issues an authorization code directly (local/hybrid mode).

**client_id semantics**:
In proxy mode the `client_id` MUST be the agent's internal UUID (`agent.id`).
In local/hybrid mode the `client_id` may also be an HTTPS URL identifying a
Client ID Metadata Document (CIMD) when CIMD is enabled.

**Local/Hybrid Mode**:
When the broker acts as its own OAuth2 authorization server:
- Validates the agent's registered `redirect_uris`
- If user has an active grant, redirects to `redirect_uri` with `code` and `state`
- If no active grant exists, redirects to the consent UI for user approval
- Supports PKCE (RFC 7636) with `code_challenge` and `code_challenge_method`

**Proxy Mode**:
When proxying to an upstream OAuth2 server:
- Redirects to the upstream authorization endpoint with PKCE parameters
- Agent ID is embedded in the state token for callback correlation

**Error Handling** (RFC 6749 §4.1.2.1):

Direct JSON responses (no redirect — RFC 6749 §4.1.2.1):
- `invalid_client` (400): `client_id` is not a valid UUID OR no agent with that UUID exists
- `invalid_redirect_uri` (400): `redirect_uri` not registered on the agent
- `invalid_request` (400): Missing PKCE parameters
- `unsupported_response_type` (400): `response_type` is not `code`
- `server_error` (500): Internal infrastructure failure

Redirect responses (error appended to `redirect_uri` as query params; redirect_uri has been validated):
- `invalid_scope`: Requested scope exceeds the agent's `allowed_scopes`
- `access_denied`: User explicitly denied consent
- `server_error`: Proxy mode — agent has no upstream `client_id` configured
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.o_auth2token import Oauth2AuthorizeRequestResponseType

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth2token.oauth2authorize(
    client_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    response_type=Oauth2AuthorizeRequestResponseType.CODE,
    redirect_uri="redirect_uri",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — The internal agent identifier (UUID) registered with the identity broker. This MUST be the agent's `id` field, NOT the upstream OAuth2 `client_id`. Example: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    
</dd>
</dl>

<dl>
<dd>

**response_type:** `Oauth2AuthorizeRequestResponseType` — OAuth2 response type. Must be "code" for authorization code flow.
    
</dd>
</dl>

<dl>
<dd>

**redirect_uri:** `str` — Callback URI to redirect to after authorization. Must be pre-registered.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — Opaque value used to maintain state between request and callback (CSRF protection).
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[str]` — Space-delimited list of requested OAuth2 scopes.
    
</dd>
</dl>

<dl>
<dd>

**code_challenge:** `typing.Optional[str]` — PKCE code challenge (RFC 7636). SHA256 hash of code_verifier, base64url-encoded.
    
</dd>
</dl>

<dl>
<dd>

**code_challenge_method:** `typing.Optional[Oauth2AuthorizeRequestCodeChallengeMethod]` — PKCE code challenge method. Must be "S256".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.o_auth2token.<a href="src/fern/o_auth2token/client.py">token_exchange</a>(...) -> TokenExchangeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange a token for another token, or obtain a token directly. This endpoint
supports three grant types:

### Client Credentials Grant (RFC 6749 §4.4 - Issue Token Mode)
Authenticate the agent directly using broker-issued client credentials and obtain
an access token. Used when the broker acts as an OAuth2 authorization server.
- `grant_type`: `client_credentials`
- `client_id`: Agent UUID (`agent.id`)
- `client_secret`: Broker-issued client secret
- `scope`: (optional) Space-delimited requested scopes

### Authorization Code Grant (RFC 6749 - Issue Token Mode)
Exchange an authorization code for an access token. Supports PKCE for public clients.
- `grant_type`: `authorization_code`
- `client_id`: Agent UUID (`agent.id`)
- `client_secret`: Broker-issued client secret
- `code`: Authorization code from /oauth2/authorize
- `redirect_uri`: Must match the URI used in the authorization request
- `code_verifier`: (optional) PKCE code verifier (RFC 7636)

### Authorization Code Grant (RFC 6749 - Proxy Mode)
Exchange an authorization code for an access token via the upstream OAuth2 server.
This is the standard OAuth2 authorization code flow used for initial user consent. The
broker forwards form fields, including `client_secret` when supplied, in the request body
and forwards only the validated form `Content-Type` request header. It does not forward
credential headers such as `Authorization`, cookies, or proxy identity headers. The broker
returns only `Content-Type`, `Cache-Control`, `Pragma`, and `WWW-Authenticate` from upstream
responses. It never returns upstream cookies or arbitrary response headers.
### Token Exchange Grant (RFC 8693)
Exchange a token issued by the Upstream OAuth2 Server for a third-party OAuth2 token
stored in the token vault.

The token exchange flow:
1. Gateway authenticates using client_assertion JWT (gateway identity)
2. System validates subject_token JWT (contains principal + agent identifier)
3. System evaluates CEL authorization policy
4. System looks up service by resource URI in protected_resources
5. System verifies user grant exists for agent+service
6. System retrieves (and optionally refreshes) stored third-party tokens
7. System returns RFC 8693 compliant response

**Authentication for Token Exchange:**
- client_assertion: Gateway JWT authenticated against upstream OAuth2 JWKS
- subject_token: User JWT containing principal and agent identifier
- Both validated to have correct issuer, audience, and expiration

**Resource Discovery:**
- resource parameter must match a protected_resource on ThirdpartyOAuth2Service
- URIs are normalized (trailing slashes removed) before matching
- Missing match returns 400 invalid_target error

**User Grant Verification:**
- User must have active (non-revoked, non-expired) grant to agent+service
- Missing grant returns 403 access_denied error

### Token Exchange Grant (RFC 8693) — User Impersonation (local mode only)
Mints a locally issued access token representing a subject user and attributing the acting
party with the standard `act` claim. Available only in `local` mode; `proxy` and `hybrid`
reject it.

The routing-only `oauth2_authorization_server.impersonation.audience_prefix` activates
impersonation only when exactly one request `audience` is
`<audience_prefix>/<canonical lower-case AgentID UUID or canonical_id>`. Both forms resolve
the same registered target agent, which supplies minted UUID `agent_id` and local-token CEL
`agent.*`. A signed client assertion is the privileged-client identity for authorization and
audit only. The routing audience is never copied into issued `aud`; the existing local
`token_claims_expression` emits `aud` or leaves it absent exactly as normal local issuance
does. Activation precedes the third-party mandatory-`resource` check.

- `grant_type`: `urn:ietf:params:oauth:grant-type:token-exchange`
- `audience`: one `<audience_prefix>/<canonical lower-case AgentID UUID or canonical_id>` URI
- `client_assertion_type`: `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`
- `client_assertion`: signed JWT authenticating the privileged client
- `actor_token_type`: `urn:ietf:params:oauth:token-type:jwt`
- `actor_token`: signed JWT identifying the actor
- `subject_token_type`: `urn:ietf:params:oauth:token-type:jwt`; a matching rule's
  `verification: none` selects the unsigned-subject profile
- `subject_token`: signed subject JWT, or, for a matching `verification: none` rule, an
  unsigned `alg:none` JWT
- `requested_token_type`: optional; when present MUST equal the access-token type

`resource` is rejected with `invalid_request`. An optional `scope` requests values from the
resolved target agent's `allowed_scopes`; an empty target allow-list is unrestricted, and
`offline` and `offline_access` are always permitted refresh-token scopes. An out-of-list
non-reserved value returns `invalid_scope`. The normal local JWT and response carry non-empty granted scope.
Signed credentials are validated for signature, issuer, audience, expiry, and not-before
before a CEL authorization predicate decides the request. Bare suffixes and suffixes matching
neither identifier form return `invalid_request`; a well-formed UUID or canonical-ID suffix
whose target is unknown returns `invalid_target`.
No-match precedence is `access_denied` > `invalid_request` > `invalid_client`.

After a rule authorizes the request, the broker requires an active user delegation for the
extracted subject and target agent. A missing or expired delegation returns `403 access_denied`
with the existing RFC 6749 `error_uri` response member set to the authenticated user's
target-agent consent page. The response intentionally does not distinguish a missing delegation
from an expired one. An unverified subject has no exemption; a delegation lookup failure returns
`500 server_error` without `error_uri`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, TokenExchangeRequestGrantType
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth2token.token_exchange(
    grant_type=TokenExchangeRequestGrantType.CLIENT_CREDENTIALS,
    client_id="550e8400-e29b-41d4-a716-446655440000",
    client_secret="brk_sec_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
    scope="openid profile",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `TokenExchangeRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Approvals
<details><summary><code>client.approvals.<a href="src/fern/approvals/client.py">sync_approvals</a>(...) -> ApprovalSyncResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all active approvals grouped by (principal, agent) pair.
Supports long-poll via If-None-Match + X-Long-Poll-Timeout headers.
Auth: client assertion only (CEL-validated). No subject token is required because this is a gateway control-plane sync channel rather than a user-facing operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approvals.sync_approvals()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**principal:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**agent_session_id:** `typing.Optional[str]` — Repeat for each active agent session. Session-scoped approvals are returned only for matching IDs.
    
</dd>
</dl>

<dl>
<dd>

**if_none_match:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**long_poll_timeout:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approvals.<a href="src/fern/approvals/client.py">create_approval</a>(...) -> CreateApprovalResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a pending approval record for a tool invocation that requires human-in-the-loop authorization.
Called by ExtProc when a tool call is intercepted that requires approval.
Dual-auth required: subject token + client assertion. The subject token binds the request to user/agent context, while the client assertion proves the trusted gateway caller that is allowed to mint approval prompts.
Idempotent: returns existing record for duplicate pending requests.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.approvals import CreateApprovalRequestMetadata

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approvals.create_approval(
    metadata=CreateApprovalRequestMetadata(
        description="description",
    ),
    tool_name="tool_name",
    arguments={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**metadata:** `CreateApprovalRequestMetadata` 
    
</dd>
</dl>

<dl>
<dd>

**tool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**arguments:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**traceparent:** `typing.Optional[str]` — W3C Trace Context propagation header.
    
</dd>
</dl>

<dl>
<dd>

**risk_level:** `typing.Optional[CreateApprovalRequestRiskLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approvals.<a href="src/fern/approvals/client.py">list_pending_approvals</a>() -> ListPendingApprovalsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all pending approvals for the authenticated user.
Used by the approval and tool authorization UIs.
Auth: acting user principal from the browser auth layer (for example `X-Remote-User` in pre-auth deployments).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approvals.list_pending_approvals()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approvals.<a href="src/fern/approvals/client.py">list_permanent_approvals</a>() -> ListPermanentApprovalsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all permanent approvals and denials for the authenticated user.
Used by the consent management UI.
Auth: acting user principal from the browser auth layer (for example `X-Remote-User` in pre-auth deployments).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approvals.list_permanent_approvals()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approvals.<a href="src/fern/approvals/client.py">get_approval</a>(...) -> ApprovalDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a tool approval record by ID for the Approval UI.
Auth: acting user principal from the browser auth layer; principal must match.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approvals.get_approval(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approvals.<a href="src/fern/approvals/client.py">approve_approval</a>(...) -> ApproveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transitions a pending approval to approved state with selected persistence scope.
Auth: acting user principal from the browser auth layer; principal must match.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.approvals import ApproveRequestPersistence

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approvals.approve_approval(
    id="id",
    persistence=ApproveRequestPersistence.ONCE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**persistence:** `ApproveRequestPersistence` 
    
</dd>
</dl>

<dl>
<dd>

**params_pattern:** `typing.Optional[typing.Dict[str, str]]` — Constrained argument names mapped to globs. Omit the field to cover only the reviewed argument values. This field is permitted only for session or permanent persistence. With once persistence, every supplied value, including an empty object, returns 422 invalid_pattern. The resulting pattern must cover the reviewed arguments.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approvals.<a href="src/fern/approvals/client.py">preview_approval_scope</a>(...) -> ScopePreviewResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approvals.preview_approval_scope(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**params_pattern:** `typing.Optional[typing.Dict[str, str]]` — Constrained argument names mapped to globs. Omit the field entirely to cover only the reviewed argument values; send an empty object to leave every argument unconstrained.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approvals.<a href="src/fern/approvals/client.py">deny_approval</a>(...) -> DenyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transitions a pending approval to denied state.
Auth: acting user principal from the browser auth layer; principal must match.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approvals.deny_approval(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**persistence:** `typing.Optional[DenyRequestPersistence]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approvals.<a href="src/fern/approvals/client.py">consume_approval</a>(...) -> ConsumeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks an approved once-persistence approval as consumed.
Auth: subject token only (Bearer); principal must match.
Idempotent: consuming already-consumed returns 200.
No client assertion is required because this is a per-approval, principal-scoped machine mutation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approvals.consume_approval(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approvals.<a href="src/fern/approvals/client.py">revoke_permanent_approval</a>(...) -> DenyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revokes a permanent approval or denial.
Auth: acting user principal from the browser auth layer; principal must match.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.approvals.revoke_permanent_approval(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OAuth2 Discovery
<details><summary><code>client.o_auth2discovery.<a href="src/fern/o_auth2discovery/client.py">get_jwks</a>() -> JwkSetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the broker's aggregated public signing keys in JWK Set format (RFC 7517).

Clients use this single endpoint to verify any token the broker asks them to trust,
regardless of operating mode. Only public key material is included — private keys
are never exposed.

**Mode-dependent content**:
- `local` mode: returns only the broker's locally-generated signing keys.
- `proxy` mode: republishes the upstream authorization server's public keys verbatim.
- `hybrid` mode: returns the union of local signing keys and upstream keys in a
  single JWKS document. If any `kid` appears in both sets, the endpoint returns 500.

**Availability**: Served in all three modes (`local`, `proxy`, `hybrid`). Returns
503 if the upstream JWKS is unavailable (proxy/hybrid modes). Returns 500 if a
duplicate `kid` is detected across local and upstream key sets (hybrid mode).

**Caching**: Responses include `Cache-Control: public, max-age=300` to allow
clients to cache the key set for 5 minutes. Clients should respect this header
and implement key rotation by periodically refreshing the JWKS.

**Key Rotation**: When signing keys are rotated, the new key appears in the
JWKS immediately. Previous keys remain in the set until removed by an admin.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth2discovery.get_jwks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.o_auth2discovery.<a href="src/fern/o_auth2discovery/client.py">get_o_auth2server_metadata</a>() -> OAuth2MetadataResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the broker's OAuth2 authorization server metadata as defined
in RFC 8414. This enables dynamic client discovery of the broker's
OAuth2 capabilities and endpoints.

**Mode-specific behavior**:
- `proxy` mode: `issuer` is the broker's own public URL. `jwks_uri` points to the
  broker's `/oauth2/jwks.json` endpoint, which republishes upstream keys.
- `local` mode: `issuer` is the broker's own public URL. `jwks_uri` points to the
  broker's `/oauth2/jwks.json` endpoint, which serves locally-generated signing keys.
- `hybrid` mode: `issuer` is the broker's public URL. `jwks_uri` points to the
  broker's `/oauth2/jwks.json` endpoint (union of local and upstream keys). The
  metadata reflects the union of capabilities for both proxy and local grant types.

**Caching**: Responses include `Cache-Control: public, max-age=3600` to allow
clients to cache metadata for 1 hour.

**No Authentication**: This endpoint is publicly accessible as required by RFC 8414.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    remote_user="<X-Remote-User>",
    environment=FernApiEnvironment.DEFAULT,
)

client.o_auth2discovery.get_o_auth2server_metadata()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

