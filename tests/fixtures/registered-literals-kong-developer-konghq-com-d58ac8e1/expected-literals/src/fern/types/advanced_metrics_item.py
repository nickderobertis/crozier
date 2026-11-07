

import typing

AdvancedMetricsItem = typing.Union[
    typing.Literal[
        "kong_latency_average",
        "kong_latency_p50",
        "kong_latency_p95",
        "kong_latency_p99",
        "request_count",
        "request_per_minute",
        "request_size_average",
        "request_size_p50",
        "request_size_p95",
        "request_size_p99",
        "request_size_sum",
        "response_latency_average",
        "response_latency_p50",
        "response_latency_p95",
        "response_latency_p99",
        "response_size_average",
        "response_size_p50",
        "response_size_p95",
        "response_size_p99",
        "response_size_sum",
        "upstream_latency_average",
        "upstream_latency_p50",
        "upstream_latency_p95",
        "upstream_latency_p99",
    ],
    typing.Any,
]
