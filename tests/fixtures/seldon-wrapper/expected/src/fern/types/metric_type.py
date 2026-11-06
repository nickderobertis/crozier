

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricType(enum.StrEnum):
    COUNTER = "COUNTER"
    GAUGE = "GAUGE"
    TIMER = "TIMER"

    def visit(
        self,
        counter: typing.Callable[[], T_Result],
        gauge: typing.Callable[[], T_Result],
        timer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricType.COUNTER:
            return counter()
        if self is MetricType.GAUGE:
            return gauge()
        if self is MetricType.TIMER:
            return timer()
