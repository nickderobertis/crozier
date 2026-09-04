

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ClientRegistrationRequestTokenEndpointAuthMethod(enum.StrEnum):
    PRIVATE_KEY_JWT = "private_key_jwt"
    TLS_CLIENT_AUTH = "tls_client_auth"

    def visit(
        self, private_key_jwt: typing.Callable[[], T_Result], tls_client_auth: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ClientRegistrationRequestTokenEndpointAuthMethod.PRIVATE_KEY_JWT:
            return private_key_jwt()
        if self is ClientRegistrationRequestTokenEndpointAuthMethod.TLS_CLIENT_AUTH:
            return tls_client_auth()
