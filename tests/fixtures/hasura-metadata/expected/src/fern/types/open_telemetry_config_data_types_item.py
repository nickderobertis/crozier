

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenTelemetryConfigDataTypesItem(enum.StrEnum):
    TRACES = "traces"
    METRICS = "metrics"
    LOGS = "logs"

    def visit(
        self,
        traces: typing.Callable[[], T_Result],
        metrics: typing.Callable[[], T_Result],
        logs: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OpenTelemetryConfigDataTypesItem.TRACES:
            return traces()
        if self is OpenTelemetryConfigDataTypesItem.METRICS:
            return metrics()
        if self is OpenTelemetryConfigDataTypesItem.LOGS:
            return logs()
