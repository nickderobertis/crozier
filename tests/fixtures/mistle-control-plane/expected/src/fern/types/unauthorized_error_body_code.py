

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UnauthorizedErrorBodyCode(enum.StrEnum):
    UNAUTHORIZED = "UNAUTHORIZED"

    def visit(self, unauthorized: typing.Callable[[], T_Result]) -> T_Result:
        if self is UnauthorizedErrorBodyCode.UNAUTHORIZED:
            return unauthorized()
