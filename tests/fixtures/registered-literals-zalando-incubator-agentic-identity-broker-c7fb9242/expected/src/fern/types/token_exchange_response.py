

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TokenExchangeResponse(UniversalBaseModel):
    access_token: str = pydantic.Field()
    """
    The issued access token. For third-party exchange this is the token vault token. For
    user impersonation it is a locally signed broker JWT with `sub`, target-derived
    `agent_id` and local-policy `agent.*`, `act` = `{ "iss": <actor-token issuer>,
    "sub": <actor> }`, optional email, normal local base claims, and a `scope` claim
    equal to the granted requested scope. `aud`, if present, is emitted by the existing
    local token-claims policy.
    """

    token_type: str = pydantic.Field()
    """
    For third-party token exchange, the type passed through from the stored provider
    token. For user impersonation, always `Bearer` for the locally issued broker JWT.
    """

    issued_token_type: str = pydantic.Field()
    """
    URI indicating the type of issued token.
    """

    expires_in: typing.Optional[int] = pydantic.Field(default=None)
    """
    Remaining lifetime in seconds. For third-party token exchange it reflects the
    stored token; for user impersonation it reflects the configured local token TTL.
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    For user impersonation, the non-empty granted scope, including target-allowed values and any requested reserved refresh-token scopes (`offline`, `offline_access`); omitted when no scope was requested.
    """

    refresh_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Refresh token (typically not returned in token exchange as
    tokens are managed by the broker).
    """

    granted_permission_sets: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic.Field(default=None)
    """
    Map of granted permission sets associated with the token exchange.
    Keys are permission set UUIDs, values are arrays of service UUIDs.
    Only present when the token exchange is scoped to specific permission sets.
    """

    principal: typing.Optional[str] = pydantic.Field(default=None)
    """
    Verified subject-token principal; omitted when unresolved.
    """

    agent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resolved canonical agent ID from the verified subject token; omitted when unresolved.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
