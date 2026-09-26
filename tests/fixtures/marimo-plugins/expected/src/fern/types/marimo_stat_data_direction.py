

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoStatDataDirection(enum.StrEnum):
    INCREASE = "increase"
    DECREASE = "decrease"

    def visit(self, increase: typing.Callable[[], T_Result], decrease: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoStatDataDirection.INCREASE:
            return increase()
        if self is MarimoStatDataDirection.DECREASE:
            return decrease()
