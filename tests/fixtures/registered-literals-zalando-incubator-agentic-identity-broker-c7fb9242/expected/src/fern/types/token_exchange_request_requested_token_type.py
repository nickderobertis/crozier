

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenExchangeRequestRequestedTokenType(enum.StrEnum):
    """
    Optional for the impersonation flow. When present it MUST equal the access-token
    type; any other value is rejected with `invalid_request`. When absent the
    access-token type is assumed.
    """

    URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ACCESS_TOKEN = "urn:ietf:params:oauth:token-type:access_token"

    def visit(self, urn_ietf_params_oauth_token_type_access_token: typing.Callable[[], T_Result]) -> T_Result:
        if self is TokenExchangeRequestRequestedTokenType.URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ACCESS_TOKEN:
            return urn_ietf_params_oauth_token_type_access_token()
