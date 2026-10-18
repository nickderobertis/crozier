

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OAuthTokenBodyGrantType(enum.StrEnum):
    AUTHORIZATION_CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER = "urn:ietf:params:oauth:grant-type:jwt-bearer"

    def visit(
        self,
        authorization_code: typing.Callable[[], T_Result],
        refresh_token: typing.Callable[[], T_Result],
        urn_ietf_params_oauth_grant_type_jwt_bearer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OAuthTokenBodyGrantType.AUTHORIZATION_CODE:
            return authorization_code()
        if self is OAuthTokenBodyGrantType.REFRESH_TOKEN:
            return refresh_token()
        if self is OAuthTokenBodyGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER:
            return urn_ietf_params_oauth_grant_type_jwt_bearer()
