

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PickTimeSeriesFilterRankingMethod(enum.StrEnum):
    """
    ranking_method is applied to each time series independently to produce the value which will be used to compare the time series to other time series.
    """

    METHOD_UNSPECIFIED = "METHOD_UNSPECIFIED"
    METHOD_MEAN = "METHOD_MEAN"
    METHOD_MAX = "METHOD_MAX"
    METHOD_MIN = "METHOD_MIN"
    METHOD_SUM = "METHOD_SUM"
    METHOD_LATEST = "METHOD_LATEST"

    def visit(
        self,
        method_unspecified: typing.Callable[[], T_Result],
        method_mean: typing.Callable[[], T_Result],
        method_max: typing.Callable[[], T_Result],
        method_min: typing.Callable[[], T_Result],
        method_sum: typing.Callable[[], T_Result],
        method_latest: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PickTimeSeriesFilterRankingMethod.METHOD_UNSPECIFIED:
            return method_unspecified()
        if self is PickTimeSeriesFilterRankingMethod.METHOD_MEAN:
            return method_mean()
        if self is PickTimeSeriesFilterRankingMethod.METHOD_MAX:
            return method_max()
        if self is PickTimeSeriesFilterRankingMethod.METHOD_MIN:
            return method_min()
        if self is PickTimeSeriesFilterRankingMethod.METHOD_SUM:
            return method_sum()
        if self is PickTimeSeriesFilterRankingMethod.METHOD_LATEST:
            return method_latest()
