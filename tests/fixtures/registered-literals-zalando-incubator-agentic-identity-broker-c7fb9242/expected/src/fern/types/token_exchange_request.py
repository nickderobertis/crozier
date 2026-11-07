

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .token_exchange_request_actor_token_type import TokenExchangeRequestActorTokenType
from .token_exchange_request_client_assertion_type import TokenExchangeRequestClientAssertionType
from .token_exchange_request_grant_type import TokenExchangeRequestGrantType
from .token_exchange_request_requested_token_type import TokenExchangeRequestRequestedTokenType


class TokenExchangeRequest(UniversalBaseModel):
    """
    Unified token endpoint request schema supporting multiple OAuth2 grant types.
    Required fields vary by grant_type:

    **client_credentials**: requires client_id, client_secret. Optional: scope.
    **authorization_code** (local/hybrid): requires client_id, code, redirect_uri. client_secret required for confidential clients, optional for public clients. Optional: code_verifier.
    **authorization_code** (proxy): requires client_id, client_secret, code, redirect_uri.
    **token-exchange** (RFC 8693): requires subject_token, subject_token_type, resource, client_assertion_type, client_assertion.
    **token-exchange (user impersonation)** (RFC 8693, local mode only): activated only by one `audience` equal to `<audience_prefix>/<canonical lower-case AgentID UUID or canonical_id>`, which must resolve to a registered target. Both forms retain the target UUID as issued `agent_id`; that target supplies local-policy `agent.*`, and optional scope policy through `allowed_scopes`; an empty allow-list is unrestricted, while the reserved refresh-token scopes `offline` and `offline_access` are always permitted. Required credentials are client assertion, actor token, and subject token. `resource` MUST be absent; a target-disallowed non-reserved optional scope is `invalid_scope`.
    """

    grant_type: TokenExchangeRequestGrantType = pydantic.Field()
    """
    The OAuth2 grant type:
    - `urn:ietf:params:oauth:grant-type:token-exchange` for RFC 8693 token exchange
    - `authorization_code` for standard OAuth2 authorization code flow (proxied or local/hybrid)
    - `client_credentials` for broker-issued client credentials (local/hybrid mode)
    """

    client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    In proxy mode: the agent's internal UUID (`agent.id`). In local/hybrid mode
    with CIMD enabled: may also be an HTTPS URL identifying the agent's Client ID
    Metadata Document. The broker resolves the upstream OAuth2 client ID internally.
    """

    client_secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    Broker-issued client secret (for client_credentials in local/hybrid mode, and
    for confidential-client authorization_code exchanges) or upstream OAuth2 client
    secret (proxy mode). Optional for public authorization_code clients in local/hybrid mode.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Authorization code received from the /oauth2/authorize endpoint.
    Required for authorization_code grant type.
    """

    redirect_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    Redirect URI used in the original authorization request.
    Required for authorization_code grant type. Must match the URI
    used in the authorization request exactly.
    """

    code_verifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    PKCE code verifier (RFC 7636). Required if code_challenge was
    provided in the authorization request.
    """

    subject_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    For third-party token exchange, a JWT from which the broker extracts the user
    principal and agent identifier. For user impersonation, a signed subject JWT or,
    only when a matching rule declares `verification: none`, an unsigned `alg:none`
    subject JWT whose claims provide the impersonated principal. Required for
    token-exchange grant type.
    """

    subject_token_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the subject_token.
    - `urn:ietf:params:oauth:token-type:access_token`: third-party token exchange (default).
    - `urn:ietf:params:oauth:token-type:jwt`: user impersonation (local mode only). A
      signed subject is signature-verified; a rule declaring `verification: none` accepts
      an unsigned (`alg:none`) subject JWT and rejects signed JWSs on that path. An
      unsigned JWT is rejected by signed subject roles.
    Required for token-exchange grant type.
    """

    actor_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Signed JWT identifying the acting party for user impersonation. Required for the
    impersonation flow. Its validated issuer and extracted identity surface as
    `act.iss` and `act.sub` in the issued token.
    """

    actor_token_type: typing.Optional[TokenExchangeRequestActorTokenType] = pydantic.Field(default=None)
    """
    Type of the actor_token. MUST be the RFC 8693 JWT token type. Required for the
    impersonation flow.
    """

    requested_token_type: typing.Optional[TokenExchangeRequestRequestedTokenType] = pydantic.Field(default=None)
    """
    Optional for the impersonation flow. When present it MUST equal the access-token
    type; any other value is rejected with `invalid_request`. When absent the
    access-token type is assumed.
    """

    resource: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required for third-party token exchange. It must match a protected_resource on a
    ThirdpartyOAuth2Service and is normalized by removing trailing slashes before
    matching. It MUST be absent for audience-activated user impersonation.
    """

    client_assertion_type: typing.Optional[TokenExchangeRequestClientAssertionType] = pydantic.Field(default=None)
    """
    The client authentication method. Must be JWT bearer. Required for token-exchange grant type.
    """

    client_assertion: typing.Optional[str] = pydantic.Field(default=None)
    """
    Signed JWT authenticating the privileged client. Third-party token exchange
    validates it against the configured client-assertion issuer; user impersonation
    validates it against a trusted issuer in the matching impersonation rule. Required
    for token-exchange grant type.
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional literal-space-separated scope request. For user impersonation, every non-reserved value must be permitted by the resolved target agent's `allowed_scopes`; an empty allow-list is unrestricted. The reserved refresh-token scopes `offline` and `offline_access` are always permitted. A denied non-reserved value returns `invalid_scope`.
    """

    audience: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional token-exchange audience. For local impersonation it must be exactly one
    `<audience_prefix>/<canonical lower-case AgentID UUID or canonical_id>` URI. The suffix
    selects the registered target agent; the routing audience never sets issued-token `aud`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
