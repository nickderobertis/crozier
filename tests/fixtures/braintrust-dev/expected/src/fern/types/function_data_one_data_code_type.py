

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataOneDataCodeType(enum.StrEnum):
    INLINE = "inline"

    def visit(self, inline: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataOneDataCodeType.INLINE:
            return inline()
