

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenResponseDtoIssuedTokenType(enum.StrEnum):
    """
    The type of the issued token (present only for token-exchange responses, per RFC 8693)
    """

    URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ACCESS_TOKEN = "urn:ietf:params:oauth:token-type:access_token"

    def visit(self, urn_ietf_params_oauth_token_type_access_token: typing.Callable[[], T_Result]) -> T_Result:
        if self is TokenResponseDtoIssuedTokenType.URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ACCESS_TOKEN:
            return urn_ietf_params_oauth_token_type_access_token()
