

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IntrospectionRequestTokenTypeHint(enum.StrEnum):
    ACCESS_TOKEN = "access_token"

    def visit(self, access_token: typing.Callable[[], T_Result]) -> T_Result:
        if self is IntrospectionRequestTokenTypeHint.ACCESS_TOKEN:
            return access_token()
