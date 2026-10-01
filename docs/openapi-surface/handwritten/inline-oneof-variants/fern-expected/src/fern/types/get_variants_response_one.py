

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetVariantsResponseOne(enum.StrEnum):
    FIXED = "fixed"

    def visit(self, fixed: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetVariantsResponseOne.FIXED:
            return fixed()
