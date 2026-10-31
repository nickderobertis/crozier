

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenBodyGrantType(enum.StrEnum):
    AUTHORIZATION_CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"

    def visit(
        self, authorization_code: typing.Callable[[], T_Result], refresh_token: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TokenBodyGrantType.AUTHORIZATION_CODE:
            return authorization_code()
        if self is TokenBodyGrantType.REFRESH_TOKEN:
            return refresh_token()
