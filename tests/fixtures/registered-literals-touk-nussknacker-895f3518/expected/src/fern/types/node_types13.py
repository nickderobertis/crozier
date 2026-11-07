

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes13(enum.StrEnum):
    VARIABLE = "Variable"

    def visit(self, variable: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes13.VARIABLE:
            return variable()
