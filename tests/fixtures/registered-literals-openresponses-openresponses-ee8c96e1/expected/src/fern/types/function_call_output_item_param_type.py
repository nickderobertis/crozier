

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionCallOutputItemParamType(enum.StrEnum):
    """
    The type of the function tool call output. Always `function_call_output`.
    """

    FUNCTION_CALL_OUTPUT = "function_call_output"

    def visit(self, function_call_output: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionCallOutputItemParamType.FUNCTION_CALL_OUTPUT:
            return function_call_output()
