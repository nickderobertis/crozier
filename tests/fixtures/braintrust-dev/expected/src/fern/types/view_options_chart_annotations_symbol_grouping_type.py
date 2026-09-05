

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewOptionsChartAnnotationsSymbolGroupingType(enum.StrEnum):
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
        if self is ViewOptionsChartAnnotationsSymbolGroupingType.NONE:
            return none()
        if self is ViewOptionsChartAnnotationsSymbolGroupingType.SCORE:
            return score()
        if self is ViewOptionsChartAnnotationsSymbolGroupingType.METRIC:
            return metric()
        if self is ViewOptionsChartAnnotationsSymbolGroupingType.METADATA:
            return metadata()
