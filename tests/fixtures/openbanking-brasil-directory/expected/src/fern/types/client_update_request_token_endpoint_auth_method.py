

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ClientUpdateRequestTokenEndpointAuthMethod(enum.StrEnum):
    """
    Token endpoint authentication method
    """

    PRIVATE_KEY_JWT = "private_key_jwt"
    TLS_CLIENT_AUTH = "tls_client_auth"
    CLIENT_SECRET_BASIC = "client_secret_basic"

    def visit(
        self,
        private_key_jwt: typing.Callable[[], T_Result],
        tls_client_auth: typing.Callable[[], T_Result],
        client_secret_basic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClientUpdateRequestTokenEndpointAuthMethod.PRIVATE_KEY_JWT:
            return private_key_jwt()
        if self is ClientUpdateRequestTokenEndpointAuthMethod.TLS_CLIENT_AUTH:
            return tls_client_auth()
        if self is ClientUpdateRequestTokenEndpointAuthMethod.CLIENT_SECRET_BASIC:
            return client_secret_basic()
