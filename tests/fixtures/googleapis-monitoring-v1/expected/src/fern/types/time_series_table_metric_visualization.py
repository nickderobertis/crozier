

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TimeSeriesTableMetricVisualization(enum.StrEnum):
    """
    Optional. Store rendering strategy
    """

    METRIC_VISUALIZATION_UNSPECIFIED = "METRIC_VISUALIZATION_UNSPECIFIED"
    NUMBER = "NUMBER"
    BAR = "BAR"

    def visit(
        self,
        metric_visualization_unspecified: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        bar: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TimeSeriesTableMetricVisualization.METRIC_VISUALIZATION_UNSPECIFIED:
            return metric_visualization_unspecified()
        if self is TimeSeriesTableMetricVisualization.NUMBER:
            return number()
        if self is TimeSeriesTableMetricVisualization.BAR:
            return bar()
