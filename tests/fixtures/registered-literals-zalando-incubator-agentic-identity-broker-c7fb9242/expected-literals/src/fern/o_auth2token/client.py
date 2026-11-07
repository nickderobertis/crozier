

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.token_exchange_request_actor_token_type import TokenExchangeRequestActorTokenType
from ..types.token_exchange_request_client_assertion_type import TokenExchangeRequestClientAssertionType
from ..types.token_exchange_request_grant_type import TokenExchangeRequestGrantType
from ..types.token_exchange_request_requested_token_type import TokenExchangeRequestRequestedTokenType
from ..types.token_exchange_response import TokenExchangeResponse
from .raw_client import AsyncRawOAuth2TokenClient, RawOAuth2TokenClient
from .types.oauth2authorize_request_code_challenge_method import Oauth2AuthorizeRequestCodeChallengeMethod
from .types.oauth2authorize_request_response_type import Oauth2AuthorizeRequestResponseType


OMIT = typing.cast(typing.Any, ...)


class OAuth2TokenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOAuth2TokenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOAuth2TokenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOAuth2TokenClient
        """
        return self._raw_client

    def oauth2authorize(
        self,
        *,
        client_id: str,
        response_type: Oauth2AuthorizeRequestResponseType,
        redirect_uri: str,
        state: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[Oauth2AuthorizeRequestCodeChallengeMethod] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
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

        Parameters
        ----------
        client_id : str
            The internal agent identifier (UUID) registered with the identity broker. This MUST be the agent's `id` field, NOT the upstream OAuth2 `client_id`. Example: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"

        response_type : Oauth2AuthorizeRequestResponseType
            OAuth2 response type. Must be "code" for authorization code flow.

        redirect_uri : str
            Callback URI to redirect to after authorization. Must be pre-registered.

        state : typing.Optional[str]
            Opaque value used to maintain state between request and callback (CSRF protection).

        scope : typing.Optional[str]
            Space-delimited list of requested OAuth2 scopes.

        code_challenge : typing.Optional[str]
            PKCE code challenge (RFC 7636). SHA256 hash of code_verifier, base64url-encoded.

        code_challenge_method : typing.Optional[Oauth2AuthorizeRequestCodeChallengeMethod]
            PKCE code challenge method. Must be "S256".

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
        client.o_auth2token.oauth2authorize(
            client_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            response_type="code",
            redirect_uri="redirect_uri",
        )
        """
        _response = self._raw_client.oauth2authorize(
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            state=state,
            scope=scope,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            request_options=request_options,
        )
        return _response.data

    def token_exchange(
        self,
        *,
        grant_type: TokenExchangeRequestGrantType,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[str] = OMIT,
        actor_token: typing.Optional[str] = OMIT,
        actor_token_type: typing.Optional[TokenExchangeRequestActorTokenType] = OMIT,
        requested_token_type: typing.Optional[TokenExchangeRequestRequestedTokenType] = OMIT,
        resource: typing.Optional[str] = OMIT,
        client_assertion_type: typing.Optional[TokenExchangeRequestClientAssertionType] = OMIT,
        client_assertion: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        audience: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenExchangeResponse:
        """
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

        Parameters
        ----------
        grant_type : TokenExchangeRequestGrantType
            The OAuth2 grant type:
            - `urn:ietf:params:oauth:grant-type:token-exchange` for RFC 8693 token exchange
            - `authorization_code` for standard OAuth2 authorization code flow (proxied or local/hybrid)
            - `client_credentials` for broker-issued client credentials (local/hybrid mode)

        client_id : typing.Optional[str]
            In proxy mode: the agent's internal UUID (`agent.id`). In local/hybrid mode
            with CIMD enabled: may also be an HTTPS URL identifying the agent's Client ID
            Metadata Document. The broker resolves the upstream OAuth2 client ID internally.

        client_secret : typing.Optional[str]
            Broker-issued client secret (for client_credentials in local/hybrid mode, and
            for confidential-client authorization_code exchanges) or upstream OAuth2 client
            secret (proxy mode). Optional for public authorization_code clients in local/hybrid mode.

        code : typing.Optional[str]
            Authorization code received from the /oauth2/authorize endpoint.
            Required for authorization_code grant type.

        redirect_uri : typing.Optional[str]
            Redirect URI used in the original authorization request.
            Required for authorization_code grant type. Must match the URI
            used in the authorization request exactly.

        code_verifier : typing.Optional[str]
            PKCE code verifier (RFC 7636). Required if code_challenge was
            provided in the authorization request.

        subject_token : typing.Optional[str]
            For third-party token exchange, a JWT from which the broker extracts the user
            principal and agent identifier. For user impersonation, a signed subject JWT or,
            only when a matching rule declares `verification: none`, an unsigned `alg:none`
            subject JWT whose claims provide the impersonated principal. Required for
            token-exchange grant type.

        subject_token_type : typing.Optional[str]
            Type of the subject_token.
            - `urn:ietf:params:oauth:token-type:access_token`: third-party token exchange (default).
            - `urn:ietf:params:oauth:token-type:jwt`: user impersonation (local mode only). A
              signed subject is signature-verified; a rule declaring `verification: none` accepts
              an unsigned (`alg:none`) subject JWT and rejects signed JWSs on that path. An
              unsigned JWT is rejected by signed subject roles.
            Required for token-exchange grant type.

        actor_token : typing.Optional[str]
            Signed JWT identifying the acting party for user impersonation. Required for the
            impersonation flow. Its validated issuer and extracted identity surface as
            `act.iss` and `act.sub` in the issued token.

        actor_token_type : typing.Optional[TokenExchangeRequestActorTokenType]
            Type of the actor_token. MUST be the RFC 8693 JWT token type. Required for the
            impersonation flow.

        requested_token_type : typing.Optional[TokenExchangeRequestRequestedTokenType]
            Optional for the impersonation flow. When present it MUST equal the access-token
            type; any other value is rejected with `invalid_request`. When absent the
            access-token type is assumed.

        resource : typing.Optional[str]
            Required for third-party token exchange. It must match a protected_resource on a
            ThirdpartyOAuth2Service and is normalized by removing trailing slashes before
            matching. It MUST be absent for audience-activated user impersonation.

        client_assertion_type : typing.Optional[TokenExchangeRequestClientAssertionType]
            The client authentication method. Must be JWT bearer. Required for token-exchange grant type.

        client_assertion : typing.Optional[str]
            Signed JWT authenticating the privileged client. Third-party token exchange
            validates it against the configured client-assertion issuer; user impersonation
            validates it against a trusted issuer in the matching impersonation rule. Required
            for token-exchange grant type.

        scope : typing.Optional[str]
            Optional literal-space-separated scope request. For user impersonation, every non-reserved value must be permitted by the resolved target agent's `allowed_scopes`; an empty allow-list is unrestricted. The reserved refresh-token scopes `offline` and `offline_access` are always permitted. A denied non-reserved value returns `invalid_scope`.

        audience : typing.Optional[str]
            Optional token-exchange audience. For local impersonation it must be exactly one
            `<audience_prefix>/<canonical lower-case AgentID UUID or canonical_id>` URI. The suffix
            selects the registered target agent; the routing audience never sets issued-token `aud`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenExchangeResponse
            Successful token exchange or authorization code exchange

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )
        client.o_auth2token.token_exchange(
            grant_type="client_credentials",
            client_id="550e8400-e29b-41d4-a716-446655440000",
            client_secret="brk_sec_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
            scope="openid profile",
        )
        """
        _response = self._raw_client.token_exchange(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri,
            code_verifier=code_verifier,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            actor_token=actor_token,
            actor_token_type=actor_token_type,
            requested_token_type=requested_token_type,
            resource=resource,
            client_assertion_type=client_assertion_type,
            client_assertion=client_assertion,
            scope=scope,
            audience=audience,
            request_options=request_options,
        )
        return _response.data


class AsyncOAuth2TokenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOAuth2TokenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOAuth2TokenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOAuth2TokenClient
        """
        return self._raw_client

    async def oauth2authorize(
        self,
        *,
        client_id: str,
        response_type: Oauth2AuthorizeRequestResponseType,
        redirect_uri: str,
        state: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        code_challenge: typing.Optional[str] = None,
        code_challenge_method: typing.Optional[Oauth2AuthorizeRequestCodeChallengeMethod] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
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

        Parameters
        ----------
        client_id : str
            The internal agent identifier (UUID) registered with the identity broker. This MUST be the agent's `id` field, NOT the upstream OAuth2 `client_id`. Example: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"

        response_type : Oauth2AuthorizeRequestResponseType
            OAuth2 response type. Must be "code" for authorization code flow.

        redirect_uri : str
            Callback URI to redirect to after authorization. Must be pre-registered.

        state : typing.Optional[str]
            Opaque value used to maintain state between request and callback (CSRF protection).

        scope : typing.Optional[str]
            Space-delimited list of requested OAuth2 scopes.

        code_challenge : typing.Optional[str]
            PKCE code challenge (RFC 7636). SHA256 hash of code_verifier, base64url-encoded.

        code_challenge_method : typing.Optional[Oauth2AuthorizeRequestCodeChallengeMethod]
            PKCE code challenge method. Must be "S256".

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
            await client.o_auth2token.oauth2authorize(
                client_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                response_type="code",
                redirect_uri="redirect_uri",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.oauth2authorize(
            client_id=client_id,
            response_type=response_type,
            redirect_uri=redirect_uri,
            state=state,
            scope=scope,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
            request_options=request_options,
        )
        return _response.data

    async def token_exchange(
        self,
        *,
        grant_type: TokenExchangeRequestGrantType,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        code_verifier: typing.Optional[str] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[str] = OMIT,
        actor_token: typing.Optional[str] = OMIT,
        actor_token_type: typing.Optional[TokenExchangeRequestActorTokenType] = OMIT,
        requested_token_type: typing.Optional[TokenExchangeRequestRequestedTokenType] = OMIT,
        resource: typing.Optional[str] = OMIT,
        client_assertion_type: typing.Optional[TokenExchangeRequestClientAssertionType] = OMIT,
        client_assertion: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        audience: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenExchangeResponse:
        """
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

        Parameters
        ----------
        grant_type : TokenExchangeRequestGrantType
            The OAuth2 grant type:
            - `urn:ietf:params:oauth:grant-type:token-exchange` for RFC 8693 token exchange
            - `authorization_code` for standard OAuth2 authorization code flow (proxied or local/hybrid)
            - `client_credentials` for broker-issued client credentials (local/hybrid mode)

        client_id : typing.Optional[str]
            In proxy mode: the agent's internal UUID (`agent.id`). In local/hybrid mode
            with CIMD enabled: may also be an HTTPS URL identifying the agent's Client ID
            Metadata Document. The broker resolves the upstream OAuth2 client ID internally.

        client_secret : typing.Optional[str]
            Broker-issued client secret (for client_credentials in local/hybrid mode, and
            for confidential-client authorization_code exchanges) or upstream OAuth2 client
            secret (proxy mode). Optional for public authorization_code clients in local/hybrid mode.

        code : typing.Optional[str]
            Authorization code received from the /oauth2/authorize endpoint.
            Required for authorization_code grant type.

        redirect_uri : typing.Optional[str]
            Redirect URI used in the original authorization request.
            Required for authorization_code grant type. Must match the URI
            used in the authorization request exactly.

        code_verifier : typing.Optional[str]
            PKCE code verifier (RFC 7636). Required if code_challenge was
            provided in the authorization request.

        subject_token : typing.Optional[str]
            For third-party token exchange, a JWT from which the broker extracts the user
            principal and agent identifier. For user impersonation, a signed subject JWT or,
            only when a matching rule declares `verification: none`, an unsigned `alg:none`
            subject JWT whose claims provide the impersonated principal. Required for
            token-exchange grant type.

        subject_token_type : typing.Optional[str]
            Type of the subject_token.
            - `urn:ietf:params:oauth:token-type:access_token`: third-party token exchange (default).
            - `urn:ietf:params:oauth:token-type:jwt`: user impersonation (local mode only). A
              signed subject is signature-verified; a rule declaring `verification: none` accepts
              an unsigned (`alg:none`) subject JWT and rejects signed JWSs on that path. An
              unsigned JWT is rejected by signed subject roles.
            Required for token-exchange grant type.

        actor_token : typing.Optional[str]
            Signed JWT identifying the acting party for user impersonation. Required for the
            impersonation flow. Its validated issuer and extracted identity surface as
            `act.iss` and `act.sub` in the issued token.

        actor_token_type : typing.Optional[TokenExchangeRequestActorTokenType]
            Type of the actor_token. MUST be the RFC 8693 JWT token type. Required for the
            impersonation flow.

        requested_token_type : typing.Optional[TokenExchangeRequestRequestedTokenType]
            Optional for the impersonation flow. When present it MUST equal the access-token
            type; any other value is rejected with `invalid_request`. When absent the
            access-token type is assumed.

        resource : typing.Optional[str]
            Required for third-party token exchange. It must match a protected_resource on a
            ThirdpartyOAuth2Service and is normalized by removing trailing slashes before
            matching. It MUST be absent for audience-activated user impersonation.

        client_assertion_type : typing.Optional[TokenExchangeRequestClientAssertionType]
            The client authentication method. Must be JWT bearer. Required for token-exchange grant type.

        client_assertion : typing.Optional[str]
            Signed JWT authenticating the privileged client. Third-party token exchange
            validates it against the configured client-assertion issuer; user impersonation
            validates it against a trusted issuer in the matching impersonation rule. Required
            for token-exchange grant type.

        scope : typing.Optional[str]
            Optional literal-space-separated scope request. For user impersonation, every non-reserved value must be permitted by the resolved target agent's `allowed_scopes`; an empty allow-list is unrestricted. The reserved refresh-token scopes `offline` and `offline_access` are always permitted. A denied non-reserved value returns `invalid_scope`.

        audience : typing.Optional[str]
            Optional token-exchange audience. For local impersonation it must be exactly one
            `<audience_prefix>/<canonical lower-case AgentID UUID or canonical_id>` URI. The suffix
            selects the registered target agent; the routing audience never sets issued-token `aud`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenExchangeResponse
            Successful token exchange or authorization code exchange

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            remote_user="YOUR_REMOTE_USER",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.o_auth2token.token_exchange(
                grant_type="client_credentials",
                client_id="550e8400-e29b-41d4-a716-446655440000",
                client_secret="brk_sec_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
                scope="openid profile",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_exchange(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri,
            code_verifier=code_verifier,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            actor_token=actor_token,
            actor_token_type=actor_token_type,
            requested_token_type=requested_token_type,
            resource=resource,
            client_assertion_type=client_assertion_type,
            client_assertion=client_assertion,
            scope=scope,
            audience=audience,
            request_options=request_options,
        )
        return _response.data
