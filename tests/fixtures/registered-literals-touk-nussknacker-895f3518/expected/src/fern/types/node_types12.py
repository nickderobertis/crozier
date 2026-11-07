

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes12(enum.StrEnum):
    SWITCH = "Switch"

    def visit(self, switch: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes12.SWITCH:
            return switch()
