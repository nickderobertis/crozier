

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTechnicalUserTokenRequestSubjectTokenType(enum.StrEnum):
    """
    The type of the subject token
    """

    URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_JWT = "urn:ietf:params:oauth:token-type:jwt"
    URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ACCESS_TOKEN = "urn:ietf:params:oauth:token-type:access_token"

    def visit(
        self,
        urn_ietf_params_oauth_token_type_jwt: typing.Callable[[], T_Result],
        urn_ietf_params_oauth_token_type_access_token: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTechnicalUserTokenRequestSubjectTokenType.URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_JWT:
            return urn_ietf_params_oauth_token_type_jwt()
        if self is GetTechnicalUserTokenRequestSubjectTokenType.URN_IETF_PARAMS_OAUTH_TOKEN_TYPE_ACCESS_TOKEN:
            return urn_ietf_params_oauth_token_type_access_token()
