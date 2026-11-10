

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LiveActivityOptionsPriorityZero(enum.StrEnum):
    HIGH = "high"
    NORMAL = "normal"
    FIVE = "5"
    TEN = "10"

    def visit(
        self,
        high: typing.Callable[[], T_Result],
        normal: typing.Callable[[], T_Result],
        five: typing.Callable[[], T_Result],
        ten: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LiveActivityOptionsPriorityZero.HIGH:
            return high()
        if self is LiveActivityOptionsPriorityZero.NORMAL:
            return normal()
        if self is LiveActivityOptionsPriorityZero.FIVE:
            return five()
        if self is LiveActivityOptionsPriorityZero.TEN:
            return ten()
