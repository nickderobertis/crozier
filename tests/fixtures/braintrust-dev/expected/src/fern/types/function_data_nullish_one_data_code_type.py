

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataNullishOneDataCodeType(enum.StrEnum):
    INLINE = "inline"

    def visit(self, inline: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataNullishOneDataCodeType.INLINE:
            return inline()
