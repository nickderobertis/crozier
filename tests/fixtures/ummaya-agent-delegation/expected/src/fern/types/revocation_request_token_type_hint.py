

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RevocationRequestTokenTypeHint(enum.StrEnum):
    ACCESS_TOKEN = "access_token"

    def visit(self, access_token: typing.Callable[[], T_Result]) -> T_Result:
        if self is RevocationRequestTokenTypeHint.ACCESS_TOKEN:
            return access_token()
