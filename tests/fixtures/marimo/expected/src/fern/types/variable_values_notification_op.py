

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VariableValuesNotificationOp(enum.StrEnum):
    VARIABLE_VALUES = "variable-values"

    def visit(self, variable_values: typing.Callable[[], T_Result]) -> T_Result:
        if self is VariableValuesNotificationOp.VARIABLE_VALUES:
            return variable_values()
