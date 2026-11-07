

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdvancedMetricsItem(enum.StrEnum):
    KONG_LATENCY_AVERAGE = "kong_latency_average"
    KONG_LATENCY_P50 = "kong_latency_p50"
    KONG_LATENCY_P95 = "kong_latency_p95"
    KONG_LATENCY_P99 = "kong_latency_p99"
    REQUEST_COUNT = "request_count"
    REQUEST_PER_MINUTE = "request_per_minute"
    REQUEST_SIZE_AVERAGE = "request_size_average"
    REQUEST_SIZE_P50 = "request_size_p50"
    REQUEST_SIZE_P95 = "request_size_p95"
    REQUEST_SIZE_P99 = "request_size_p99"
    REQUEST_SIZE_SUM = "request_size_sum"
    RESPONSE_LATENCY_AVERAGE = "response_latency_average"
    RESPONSE_LATENCY_P50 = "response_latency_p50"
    RESPONSE_LATENCY_P95 = "response_latency_p95"
    RESPONSE_LATENCY_P99 = "response_latency_p99"
    RESPONSE_SIZE_AVERAGE = "response_size_average"
    RESPONSE_SIZE_P50 = "response_size_p50"
    RESPONSE_SIZE_P95 = "response_size_p95"
    RESPONSE_SIZE_P99 = "response_size_p99"
    RESPONSE_SIZE_SUM = "response_size_sum"
    UPSTREAM_LATENCY_AVERAGE = "upstream_latency_average"
    UPSTREAM_LATENCY_P50 = "upstream_latency_p50"
    UPSTREAM_LATENCY_P95 = "upstream_latency_p95"
    UPSTREAM_LATENCY_P99 = "upstream_latency_p99"

    def visit(
        self,
        kong_latency_average: typing.Callable[[], T_Result],
        kong_latency_p50: typing.Callable[[], T_Result],
        kong_latency_p95: typing.Callable[[], T_Result],
        kong_latency_p99: typing.Callable[[], T_Result],
        request_count: typing.Callable[[], T_Result],
        request_per_minute: typing.Callable[[], T_Result],
        request_size_average: typing.Callable[[], T_Result],
        request_size_p50: typing.Callable[[], T_Result],
        request_size_p95: typing.Callable[[], T_Result],
        request_size_p99: typing.Callable[[], T_Result],
        request_size_sum: typing.Callable[[], T_Result],
        response_latency_average: typing.Callable[[], T_Result],
        response_latency_p50: typing.Callable[[], T_Result],
        response_latency_p95: typing.Callable[[], T_Result],
        response_latency_p99: typing.Callable[[], T_Result],
        response_size_average: typing.Callable[[], T_Result],
        response_size_p50: typing.Callable[[], T_Result],
        response_size_p95: typing.Callable[[], T_Result],
        response_size_p99: typing.Callable[[], T_Result],
        response_size_sum: typing.Callable[[], T_Result],
        upstream_latency_average: typing.Callable[[], T_Result],
        upstream_latency_p50: typing.Callable[[], T_Result],
        upstream_latency_p95: typing.Callable[[], T_Result],
        upstream_latency_p99: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdvancedMetricsItem.KONG_LATENCY_AVERAGE:
            return kong_latency_average()
        if self is AdvancedMetricsItem.KONG_LATENCY_P50:
            return kong_latency_p50()
        if self is AdvancedMetricsItem.KONG_LATENCY_P95:
            return kong_latency_p95()
        if self is AdvancedMetricsItem.KONG_LATENCY_P99:
            return kong_latency_p99()
        if self is AdvancedMetricsItem.REQUEST_COUNT:
            return request_count()
        if self is AdvancedMetricsItem.REQUEST_PER_MINUTE:
            return request_per_minute()
        if self is AdvancedMetricsItem.REQUEST_SIZE_AVERAGE:
            return request_size_average()
        if self is AdvancedMetricsItem.REQUEST_SIZE_P50:
            return request_size_p50()
        if self is AdvancedMetricsItem.REQUEST_SIZE_P95:
            return request_size_p95()
        if self is AdvancedMetricsItem.REQUEST_SIZE_P99:
            return request_size_p99()
        if self is AdvancedMetricsItem.REQUEST_SIZE_SUM:
            return request_size_sum()
        if self is AdvancedMetricsItem.RESPONSE_LATENCY_AVERAGE:
            return response_latency_average()
        if self is AdvancedMetricsItem.RESPONSE_LATENCY_P50:
            return response_latency_p50()
        if self is AdvancedMetricsItem.RESPONSE_LATENCY_P95:
            return response_latency_p95()
        if self is AdvancedMetricsItem.RESPONSE_LATENCY_P99:
            return response_latency_p99()
        if self is AdvancedMetricsItem.RESPONSE_SIZE_AVERAGE:
            return response_size_average()
        if self is AdvancedMetricsItem.RESPONSE_SIZE_P50:
            return response_size_p50()
        if self is AdvancedMetricsItem.RESPONSE_SIZE_P95:
            return response_size_p95()
        if self is AdvancedMetricsItem.RESPONSE_SIZE_P99:
            return response_size_p99()
        if self is AdvancedMetricsItem.RESPONSE_SIZE_SUM:
            return response_size_sum()
        if self is AdvancedMetricsItem.UPSTREAM_LATENCY_AVERAGE:
            return upstream_latency_average()
        if self is AdvancedMetricsItem.UPSTREAM_LATENCY_P50:
            return upstream_latency_p50()
        if self is AdvancedMetricsItem.UPSTREAM_LATENCY_P95:
            return upstream_latency_p95()
        if self is AdvancedMetricsItem.UPSTREAM_LATENCY_P99:
            return upstream_latency_p99()
