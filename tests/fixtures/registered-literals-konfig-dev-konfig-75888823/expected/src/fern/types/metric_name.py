

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricName(enum.StrEnum):
    """
    Available metrics to query over time.
    """

    CPU = "cpu"
    MEMORY = "memory"
    RATE_EGRESS = "rate_egress"
    TOTAL_EGRESS = "total_egress"
    ACTIVE_CONNECTIONS = "active_connections"

    def visit(
        self,
        cpu: typing.Callable[[], T_Result],
        memory: typing.Callable[[], T_Result],
        rate_egress: typing.Callable[[], T_Result],
        total_egress: typing.Callable[[], T_Result],
        active_connections: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricName.CPU:
            return cpu()
        if self is MetricName.MEMORY:
            return memory()
        if self is MetricName.RATE_EGRESS:
            return rate_egress()
        if self is MetricName.TOTAL_EGRESS:
            return total_egress()
        if self is MetricName.ACTIVE_CONNECTIONS:
            return active_connections()
