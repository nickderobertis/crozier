

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleCooling(enum.StrEnum):
    SLOW = "slow"
    FAST = "fast"

    def visit(self, slow: typing.Callable[[], T_Result], fast: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScheduleCooling.SLOW:
            return slow()
        if self is ScheduleCooling.FAST:
            return fast()
