

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AggregationCrossSeriesReducer(enum.StrEnum):
    """
    The reduction operation to be used to combine time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.Not all reducer operations can be applied to all time series. The valid choices depend on the metric_kind and the value_type of the original time series. Reduction can yield a time series with a different metric_kind or value_type than the input time series.Time series data must first be aligned (see per_series_aligner) in order to perform cross-time series reduction. If cross_series_reducer is specified, then per_series_aligner must be specified, and must not be ALIGN_NONE. An alignment_period must also be specified; otherwise, an error is returned.
    """

    REDUCE_NONE = "REDUCE_NONE"
    REDUCE_MEAN = "REDUCE_MEAN"
    REDUCE_MIN = "REDUCE_MIN"
    REDUCE_MAX = "REDUCE_MAX"
    REDUCE_SUM = "REDUCE_SUM"
    REDUCE_STDDEV = "REDUCE_STDDEV"
    REDUCE_COUNT = "REDUCE_COUNT"
    REDUCE_COUNT_TRUE = "REDUCE_COUNT_TRUE"
    REDUCE_COUNT_FALSE = "REDUCE_COUNT_FALSE"
    REDUCE_FRACTION_TRUE = "REDUCE_FRACTION_TRUE"
    REDUCE_PERCENTILE99 = "REDUCE_PERCENTILE_99"
    REDUCE_PERCENTILE95 = "REDUCE_PERCENTILE_95"
    REDUCE_PERCENTILE50 = "REDUCE_PERCENTILE_50"
    REDUCE_PERCENTILE05 = "REDUCE_PERCENTILE_05"

    def visit(
        self,
        reduce_none: typing.Callable[[], T_Result],
        reduce_mean: typing.Callable[[], T_Result],
        reduce_min: typing.Callable[[], T_Result],
        reduce_max: typing.Callable[[], T_Result],
        reduce_sum: typing.Callable[[], T_Result],
        reduce_stddev: typing.Callable[[], T_Result],
        reduce_count: typing.Callable[[], T_Result],
        reduce_count_true: typing.Callable[[], T_Result],
        reduce_count_false: typing.Callable[[], T_Result],
        reduce_fraction_true: typing.Callable[[], T_Result],
        reduce_percentile99: typing.Callable[[], T_Result],
        reduce_percentile95: typing.Callable[[], T_Result],
        reduce_percentile50: typing.Callable[[], T_Result],
        reduce_percentile05: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AggregationCrossSeriesReducer.REDUCE_NONE:
            return reduce_none()
        if self is AggregationCrossSeriesReducer.REDUCE_MEAN:
            return reduce_mean()
        if self is AggregationCrossSeriesReducer.REDUCE_MIN:
            return reduce_min()
        if self is AggregationCrossSeriesReducer.REDUCE_MAX:
            return reduce_max()
        if self is AggregationCrossSeriesReducer.REDUCE_SUM:
            return reduce_sum()
        if self is AggregationCrossSeriesReducer.REDUCE_STDDEV:
            return reduce_stddev()
        if self is AggregationCrossSeriesReducer.REDUCE_COUNT:
            return reduce_count()
        if self is AggregationCrossSeriesReducer.REDUCE_COUNT_TRUE:
            return reduce_count_true()
        if self is AggregationCrossSeriesReducer.REDUCE_COUNT_FALSE:
            return reduce_count_false()
        if self is AggregationCrossSeriesReducer.REDUCE_FRACTION_TRUE:
            return reduce_fraction_true()
        if self is AggregationCrossSeriesReducer.REDUCE_PERCENTILE99:
            return reduce_percentile99()
        if self is AggregationCrossSeriesReducer.REDUCE_PERCENTILE95:
            return reduce_percentile95()
        if self is AggregationCrossSeriesReducer.REDUCE_PERCENTILE50:
            return reduce_percentile50()
        if self is AggregationCrossSeriesReducer.REDUCE_PERCENTILE05:
            return reduce_percentile05()
