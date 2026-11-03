

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertOperator(enum.StrEnum):
    BELOW = "below"
    ABOVE = "above"

    def visit(self, below: typing.Callable[[], T_Result], above: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertOperator.BELOW:
            return below()
        if self is AlertOperator.ABOVE:
            return above()
