

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BoxSize(enum.StrEnum):
    SMALL = "small"
    LARGE = "large"

    def visit(self, small: typing.Callable[[], T_Result], large: typing.Callable[[], T_Result]) -> T_Result:
        if self is BoxSize.SMALL:
            return small()
        if self is BoxSize.LARGE:
            return large()
