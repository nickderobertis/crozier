

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewOptionsChartAnnotationsXAxisType(enum.StrEnum):
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
        if self is ViewOptionsChartAnnotationsXAxisType.NONE:
            return none()
        if self is ViewOptionsChartAnnotationsXAxisType.SCORE:
            return score()
        if self is ViewOptionsChartAnnotationsXAxisType.METRIC:
            return metric()
        if self is ViewOptionsChartAnnotationsXAxisType.METADATA:
            return metadata()
