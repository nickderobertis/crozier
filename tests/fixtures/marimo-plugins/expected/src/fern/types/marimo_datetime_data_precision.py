

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoDatetimeDataPrecision(enum.StrEnum):
    HOUR = "hour"
    MINUTE = "minute"
    SECOND = "second"

    def visit(
        self,
        hour: typing.Callable[[], T_Result],
        minute: typing.Callable[[], T_Result],
        second: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarimoDatetimeDataPrecision.HOUR:
            return hour()
        if self is MarimoDatetimeDataPrecision.MINUTE:
            return minute()
        if self is MarimoDatetimeDataPrecision.SECOND:
            return second()
