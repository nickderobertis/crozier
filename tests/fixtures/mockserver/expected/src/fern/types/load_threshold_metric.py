

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadThresholdMetric(enum.StrEnum):
    """
    the per-run metric to evaluate: latency percentiles in milliseconds, ERROR_RATE as a 0.0-1.0 fraction, THROUGHPUT_RPS as requests/second over the run's elapsed time, CHECK_FAILURE_RATE as failed per-step checks as a 0.0-1.0 fraction of all evaluated checks (0 when no checks ran)
    """

    LATENCY_P50 = "LATENCY_P50"
    LATENCY_P95 = "LATENCY_P95"
    LATENCY_P99 = "LATENCY_P99"
    LATENCY_P999 = "LATENCY_P999"
    ERROR_RATE = "ERROR_RATE"
    THROUGHPUT_RPS = "THROUGHPUT_RPS"
    CHECK_FAILURE_RATE = "CHECK_FAILURE_RATE"

    def visit(
        self,
        latency_p50: typing.Callable[[], T_Result],
        latency_p95: typing.Callable[[], T_Result],
        latency_p99: typing.Callable[[], T_Result],
        latency_p999: typing.Callable[[], T_Result],
        error_rate: typing.Callable[[], T_Result],
        throughput_rps: typing.Callable[[], T_Result],
        check_failure_rate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadThresholdMetric.LATENCY_P50:
            return latency_p50()
        if self is LoadThresholdMetric.LATENCY_P95:
            return latency_p95()
        if self is LoadThresholdMetric.LATENCY_P99:
            return latency_p99()
        if self is LoadThresholdMetric.LATENCY_P999:
            return latency_p999()
        if self is LoadThresholdMetric.ERROR_RATE:
            return error_rate()
        if self is LoadThresholdMetric.THROUGHPUT_RPS:
            return throughput_rps()
        if self is LoadThresholdMetric.CHECK_FAILURE_RATE:
            return check_failure_rate()
