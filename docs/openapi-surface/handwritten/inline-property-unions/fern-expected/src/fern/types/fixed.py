

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Fixed(enum.StrEnum):
    FIXED = "fixed"

    def visit(self, fixed: typing.Callable[[], T_Result]) -> T_Result:
        if self is Fixed.FIXED:
            return fixed()
