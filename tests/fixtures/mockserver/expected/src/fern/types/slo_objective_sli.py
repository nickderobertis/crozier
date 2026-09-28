

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SloObjectiveSli(enum.StrEnum):
    """
    the service-level indicator to evaluate
    """

    LATENCY_P50 = "LATENCY_P50"
    LATENCY_P95 = "LATENCY_P95"
    LATENCY_P99 = "LATENCY_P99"
    ERROR_RATE = "ERROR_RATE"

    def visit(
        self,
        latency_p50: typing.Callable[[], T_Result],
        latency_p95: typing.Callable[[], T_Result],
        latency_p99: typing.Callable[[], T_Result],
        error_rate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SloObjectiveSli.LATENCY_P50:
            return latency_p50()
        if self is SloObjectiveSli.LATENCY_P95:
            return latency_p95()
        if self is SloObjectiveSli.LATENCY_P99:
            return latency_p99()
        if self is SloObjectiveSli.ERROR_RATE:
            return error_rate()
