

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoStatDataTargetDirection(enum.StrEnum):
    INCREASE = "increase"
    DECREASE = "decrease"

    def visit(self, increase: typing.Callable[[], T_Result], decrease: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoStatDataTargetDirection.INCREASE:
            return increase()
        if self is MarimoStatDataTargetDirection.DECREASE:
            return decrease()
