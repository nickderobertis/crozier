

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReasoningItemParamType(enum.StrEnum):
    """
    The item type. Always `reasoning`.
    """

    REASONING = "reasoning"

    def visit(self, reasoning: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReasoningItemParamType.REASONING:
            return reasoning()
