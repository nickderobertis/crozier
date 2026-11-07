

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class OAuth2ClientCredentialsRequestGrantType(enum.StrEnum):
    CLIENT_CREDENTIALS = "client_credentials"

    def visit(self, client_credentials: typing.Callable[[], T_Result]) -> T_Result:
        if self is OAuth2ClientCredentialsRequestGrantType.CLIENT_CREDENTIALS:
            return client_credentials()
