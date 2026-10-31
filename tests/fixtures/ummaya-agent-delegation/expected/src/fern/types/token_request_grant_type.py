

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenRequestGrantType(enum.StrEnum):
    """
    Device grant (RFC 8628) or token exchange (RFC 8693).
    """

    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE = "urn:ietf:params:oauth:grant-type:device_code"
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE = "urn:ietf:params:oauth:grant-type:token-exchange"

    def visit(
        self,
        urn_ietf_params_oauth_grant_type_device_code: typing.Callable[[], T_Result],
        urn_ietf_params_oauth_grant_type_token_exchange: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TokenRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE:
            return urn_ietf_params_oauth_grant_type_device_code()
        if self is TokenRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE:
            return urn_ietf_params_oauth_grant_type_token_exchange()
