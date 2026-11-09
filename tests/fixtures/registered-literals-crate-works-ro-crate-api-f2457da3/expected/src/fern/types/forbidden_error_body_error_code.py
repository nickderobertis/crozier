

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ForbiddenErrorBodyErrorCode(enum.StrEnum):
    FORBIDDEN = "FORBIDDEN"

    def visit(self, forbidden: typing.Callable[[], T_Result]) -> T_Result:
        if self is ForbiddenErrorBodyErrorCode.FORBIDDEN:
            return forbidden()
