

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SystemMetricsMetricsGetRequestFormat(enum.StrEnum):
    """
    Response format: prometheus (default) or json
    """

    PROMETHEUS = "prometheus"
    JSON = "json"

    def visit(self, prometheus: typing.Callable[[], T_Result], json: typing.Callable[[], T_Result]) -> T_Result:
        if self is SystemMetricsMetricsGetRequestFormat.PROMETHEUS:
            return prometheus()
        if self is SystemMetricsMetricsGetRequestFormat.JSON:
            return json()
