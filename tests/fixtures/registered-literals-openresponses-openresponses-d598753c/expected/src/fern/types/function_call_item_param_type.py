

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionCallItemParamType(enum.StrEnum):
    """
    The item type. Always `function_call`.
    """

    FUNCTION_CALL = "function_call"

    def visit(self, function_call: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionCallItemParamType.FUNCTION_CALL:
            return function_call()
