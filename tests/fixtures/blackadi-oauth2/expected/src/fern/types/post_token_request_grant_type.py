

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostTokenRequestGrantType(enum.StrEnum):
    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_CREDENTIALS = "client_credentials"
    PASSWORD = "password"
    REFRESH_TOKEN = "refresh_token"
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE = "urn:ietf:params:oauth:grant-type:token-exchange"
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER = "urn:ietf:params:oauth:grant-type:jwt-bearer"
    URN_OPENID_PARAMS_GRANT_TYPE_CIBA = "urn:openid:params:grant-type:ciba"
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE = "urn:ietf:params:oauth:grant-type:device_code"

    def visit(
        self,
        authorization_code: typing.Callable[[], T_Result],
        client_credentials: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
        refresh_token: typing.Callable[[], T_Result],
        urn_ietf_params_oauth_grant_type_token_exchange: typing.Callable[[], T_Result],
        urn_ietf_params_oauth_grant_type_jwt_bearer: typing.Callable[[], T_Result],
        urn_openid_params_grant_type_ciba: typing.Callable[[], T_Result],
        urn_ietf_params_oauth_grant_type_device_code: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostTokenRequestGrantType.AUTHORIZATION_CODE:
            return authorization_code()
        if self is PostTokenRequestGrantType.CLIENT_CREDENTIALS:
            return client_credentials()
        if self is PostTokenRequestGrantType.PASSWORD:
            return password()
        if self is PostTokenRequestGrantType.REFRESH_TOKEN:
            return refresh_token()
        if self is PostTokenRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE:
            return urn_ietf_params_oauth_grant_type_token_exchange()
        if self is PostTokenRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER:
            return urn_ietf_params_oauth_grant_type_jwt_bearer()
        if self is PostTokenRequestGrantType.URN_OPENID_PARAMS_GRANT_TYPE_CIBA:
            return urn_openid_params_grant_type_ciba()
        if self is PostTokenRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE:
            return urn_ietf_params_oauth_grant_type_device_code()
