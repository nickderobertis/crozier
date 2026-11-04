

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes14(enum.StrEnum):
    VARIABLE_BUILDER = "VariableBuilder"

    def visit(self, variable_builder: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes14.VARIABLE_BUILDER:
            return variable_builder()
