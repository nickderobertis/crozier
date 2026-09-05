

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewOptionsChartAnnotationsYMetricType(enum.StrEnum):
    NONE = "none"
    SCORE = "score"
    METRIC = "metric"
    METADATA = "metadata"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        score: typing.Callable[[], T_Result],
        metric: typing.Callable[[], T_Result],
        metadata: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ViewOptionsChartAnnotationsYMetricType.NONE:
            return none()
        if self is ViewOptionsChartAnnotationsYMetricType.SCORE:
            return score()
        if self is ViewOptionsChartAnnotationsYMetricType.METRIC:
            return metric()
        if self is ViewOptionsChartAnnotationsYMetricType.METADATA:
            return metadata()
