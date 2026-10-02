

import typing

LoadScenarioReportThresholdResultsItemMetric = typing.Union[
    typing.Literal[
        "LATENCY_P50",
        "LATENCY_P95",
        "LATENCY_P99",
        "LATENCY_P999",
        "ERROR_RATE",
        "THROUGHPUT_RPS",
        "CHECK_FAILURE_RATE",
    ],
    typing.Any,
]
