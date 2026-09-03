

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TokenRequestClientAssertionType(enum.StrEnum):
    """
    For private_key_jwt authentication
    """

    URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"

    def visit(self, urn_ietf_params_oauth_client_assertion_type_jwt_bearer: typing.Callable[[], T_Result]) -> T_Result:
        if self is TokenRequestClientAssertionType.URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER:
            return urn_ietf_params_oauth_client_assertion_type_jwt_bearer()
