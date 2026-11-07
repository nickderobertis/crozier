

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenExchangeRequestActorTokenType(enum.StrEnum):
    """
    Type of the actor_token. MUST be the RFC 8693 JWT token type. Required for the
    impersonation flow.
    """

    URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_JWT = "urn:ietf:params:oauth:token-type:jwt"

    def visit(self, urn_ietf_params_oauth_token_type_jwt: typing.Callable[[], T_Result]) -> T_Result:
        if self is TokenExchangeRequestActorTokenType.URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_JWT:
            return urn_ietf_params_oauth_token_type_jwt()
