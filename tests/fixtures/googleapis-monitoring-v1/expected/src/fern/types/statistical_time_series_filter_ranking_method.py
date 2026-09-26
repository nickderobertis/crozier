

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatisticalTimeSeriesFilterRankingMethod(enum.StrEnum):
    """
    rankingMethod is applied to a set of time series, and then the produced value for each individual time series is used to compare a given time series to others. These are methods that cannot be applied stream-by-stream, but rather require the full context of a request to evaluate time series.
    """

    METHOD_UNSPECIFIED = "METHOD_UNSPECIFIED"
    METHOD_CLUSTER_OUTLIER = "METHOD_CLUSTER_OUTLIER"

    def visit(
        self, method_unspecified: typing.Callable[[], T_Result], method_cluster_outlier: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is StatisticalTimeSeriesFilterRankingMethod.METHOD_UNSPECIFIED:
            return method_unspecified()
        if self is StatisticalTimeSeriesFilterRankingMethod.METHOD_CLUSTER_OUTLIER:
            return method_cluster_outlier()
