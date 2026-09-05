

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccessTokenRequestGrantType(enum.StrEnum):
    """
    The Grant Type
    """

    CLIENT_CREDENTIALS = "client_credentials"
    PRIVATE_KEY_JWT = "private_key_jwt"
    TLS_CLIENT_AUTH = "tls_client_auth"
    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE = "urn:ietf:params:oauth:grant-type:device_code"

    def visit(
        self,
        client_credentials: typing.Callable[[], T_Result],
        private_key_jwt: typing.Callable[[], T_Result],
        tls_client_auth: typing.Callable[[], T_Result],
        urn_ietf_params_oauth_grant_type_device_code: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccessTokenRequestGrantType.CLIENT_CREDENTIALS:
            return client_credentials()
        if self is AccessTokenRequestGrantType.PRIVATE_KEY_JWT:
            return private_key_jwt()
        if self is AccessTokenRequestGrantType.TLS_CLIENT_AUTH:
            return tls_client_auth()
        if self is AccessTokenRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE:
            return urn_ietf_params_oauth_grant_type_device_code()
