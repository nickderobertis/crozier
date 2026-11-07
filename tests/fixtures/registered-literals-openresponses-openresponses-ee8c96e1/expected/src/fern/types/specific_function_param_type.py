

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpecificFunctionParamType(enum.StrEnum):
    """
    The tool to call. Always `function`.
    """

    FUNCTION = "function"

    def visit(self, function: typing.Callable[[], T_Result]) -> T_Result:
        if self is SpecificFunctionParamType.FUNCTION:
            return function()
