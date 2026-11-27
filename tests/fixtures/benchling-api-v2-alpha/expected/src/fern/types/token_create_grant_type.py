

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenCreateGrantType(enum.StrEnum):
    CLIENT_CREDENTIALS = "client_credentials"
    AUTHORIZATION_CODE = "authorization_code"

    def visit(
        self, client_credentials: typing.Callable[[], T_Result], authorization_code: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TokenCreateGrantType.CLIENT_CREDENTIALS:
            return client_credentials()
        if self is TokenCreateGrantType.AUTHORIZATION_CODE:
            return authorization_code()
