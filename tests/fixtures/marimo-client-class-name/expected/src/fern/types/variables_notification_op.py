

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VariablesNotificationOp(enum.StrEnum):
    VARIABLES = "variables"

    def visit(self, variables: typing.Callable[[], T_Result]) -> T_Result:
        if self is VariablesNotificationOp.VARIABLES:
            return variables()
