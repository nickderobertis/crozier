

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PrivateChannelLocationKind(enum.StrEnum):
    PC = "pc"

    def visit(self, pc: typing.Callable[[], T_Result]) -> T_Result:
        if self is PrivateChannelLocationKind.PC:
            return pc()
