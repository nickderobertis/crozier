

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InvokeFunctionCommandType(enum.StrEnum):
    INVOKE_FUNCTION = "invoke-function"

    def visit(self, invoke_function: typing.Callable[[], T_Result]) -> T_Result:
        if self is InvokeFunctionCommandType.INVOKE_FUNCTION:
            return invoke_function()
