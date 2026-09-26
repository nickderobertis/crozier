

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenTokenType(enum.StrEnum):
    BEARER = "bearer"

    def visit(self, bearer: typing.Callable[[], T_Result]) -> T_Result:
        if self is TokenTokenType.BEARER:
            return bearer()
