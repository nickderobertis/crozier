

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Trend(str, enum.Enum):
    """
    Evolution trend qualifier
    """

    DOWN = "DOWN"
    LOW_DOWN = "LOW_DOWN"
    STABLE = "STABLE"
    LOW_UP = "LOW_UP"
    UP = "UP"

    def visit(
        self,
        down: typing.Callable[[], T_Result],
        low_down: typing.Callable[[], T_Result],
        stable: typing.Callable[[], T_Result],
        low_up: typing.Callable[[], T_Result],
        up: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Trend.DOWN:
            return down()
        if self is Trend.LOW_DOWN:
            return low_down()
        if self is Trend.STABLE:
            return stable()
        if self is Trend.LOW_UP:
            return low_up()
        if self is Trend.UP:
            return up()
