

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadScenarioReportThresholdResultsItemMetric(enum.StrEnum):
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
        if self is LoadScenarioReportThresholdResultsItemMetric.LATENCY_P50:
            return latency_p50()
        if self is LoadScenarioReportThresholdResultsItemMetric.LATENCY_P95:
            return latency_p95()
        if self is LoadScenarioReportThresholdResultsItemMetric.LATENCY_P99:
            return latency_p99()
        if self is LoadScenarioReportThresholdResultsItemMetric.LATENCY_P999:
            return latency_p999()
        if self is LoadScenarioReportThresholdResultsItemMetric.ERROR_RATE:
            return error_rate()
        if self is LoadScenarioReportThresholdResultsItemMetric.THROUGHPUT_RPS:
            return throughput_rps()
        if self is LoadScenarioReportThresholdResultsItemMetric.CHECK_FAILURE_RATE:
            return check_failure_rate()
