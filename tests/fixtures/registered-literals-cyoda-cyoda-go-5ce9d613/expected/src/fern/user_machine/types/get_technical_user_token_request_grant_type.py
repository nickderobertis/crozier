

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTechnicalUserTokenRequestGrantType(enum.StrEnum):
    """
    The OAuth 2.0 grant type
    """

    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE = "urn:ietf:params:oauth:grant-type:token-exchange"

    def visit(self, urn_ietf_params_oauth_grant_type_token_exchange: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTechnicalUserTokenRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE:
            return urn_ietf_params_oauth_grant_type_token_exchange()
