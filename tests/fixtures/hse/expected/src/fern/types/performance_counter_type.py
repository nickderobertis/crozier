

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PerformanceCounterType(enum.StrEnum):
    INVALID = "invalid"
    BASIC = "basic"
    RATE = "rate"
    LATENCY = "latency"
    DISTRIBUTION = "distribution"
    SIMPLE_LATENCY = "simple_latency"

    def visit(
        self,
        invalid: typing.Callable[[], T_Result],
        basic: typing.Callable[[], T_Result],
        rate: typing.Callable[[], T_Result],
        latency: typing.Callable[[], T_Result],
        distribution: typing.Callable[[], T_Result],
        simple_latency: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PerformanceCounterType.INVALID:
            return invalid()
        if self is PerformanceCounterType.BASIC:
            return basic()
        if self is PerformanceCounterType.RATE:
            return rate()
        if self is PerformanceCounterType.LATENCY:
            return latency()
        if self is PerformanceCounterType.DISTRIBUTION:
            return distribution()
        if self is PerformanceCounterType.SIMPLE_LATENCY:
            return simple_latency()
