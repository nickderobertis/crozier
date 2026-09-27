

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AggregationPerSeriesAligner(enum.StrEnum):
    """
    An Aligner describes how to bring the data points in a single time series into temporal alignment. Except for ALIGN_NONE, all alignments cause all the data points in an alignment_period to be mathematically grouped together, resulting in a single data point for each alignment_period with end timestamp at the end of the period.Not all alignment operations may be applied to all time series. The valid choices depend on the metric_kind and value_type of the original time series. Alignment can change the metric_kind or the value_type of the time series.Time series data must be aligned in order to perform cross-time series reduction. If cross_series_reducer is specified, then per_series_aligner must be specified and not equal to ALIGN_NONE and alignment_period must be specified; otherwise, an error is returned.
    """

    ALIGN_NONE = "ALIGN_NONE"
    ALIGN_DELTA = "ALIGN_DELTA"
    ALIGN_RATE = "ALIGN_RATE"
    ALIGN_INTERPOLATE = "ALIGN_INTERPOLATE"
    ALIGN_NEXT_OLDER = "ALIGN_NEXT_OLDER"
    ALIGN_MIN = "ALIGN_MIN"
    ALIGN_MAX = "ALIGN_MAX"
    ALIGN_MEAN = "ALIGN_MEAN"
    ALIGN_COUNT = "ALIGN_COUNT"
    ALIGN_SUM = "ALIGN_SUM"
    ALIGN_STDDEV = "ALIGN_STDDEV"
    ALIGN_COUNT_TRUE = "ALIGN_COUNT_TRUE"
    ALIGN_COUNT_FALSE = "ALIGN_COUNT_FALSE"
    ALIGN_FRACTION_TRUE = "ALIGN_FRACTION_TRUE"
    ALIGN_PERCENTILE99 = "ALIGN_PERCENTILE_99"
    ALIGN_PERCENTILE95 = "ALIGN_PERCENTILE_95"
    ALIGN_PERCENTILE50 = "ALIGN_PERCENTILE_50"
    ALIGN_PERCENTILE05 = "ALIGN_PERCENTILE_05"
    ALIGN_PERCENT_CHANGE = "ALIGN_PERCENT_CHANGE"

    def visit(
        self,
        align_none: typing.Callable[[], T_Result],
        align_delta: typing.Callable[[], T_Result],
        align_rate: typing.Callable[[], T_Result],
        align_interpolate: typing.Callable[[], T_Result],
        align_next_older: typing.Callable[[], T_Result],
        align_min: typing.Callable[[], T_Result],
        align_max: typing.Callable[[], T_Result],
        align_mean: typing.Callable[[], T_Result],
        align_count: typing.Callable[[], T_Result],
        align_sum: typing.Callable[[], T_Result],
        align_stddev: typing.Callable[[], T_Result],
        align_count_true: typing.Callable[[], T_Result],
        align_count_false: typing.Callable[[], T_Result],
        align_fraction_true: typing.Callable[[], T_Result],
        align_percentile99: typing.Callable[[], T_Result],
        align_percentile95: typing.Callable[[], T_Result],
        align_percentile50: typing.Callable[[], T_Result],
        align_percentile05: typing.Callable[[], T_Result],
        align_percent_change: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AggregationPerSeriesAligner.ALIGN_NONE:
            return align_none()
        if self is AggregationPerSeriesAligner.ALIGN_DELTA:
            return align_delta()
        if self is AggregationPerSeriesAligner.ALIGN_RATE:
            return align_rate()
        if self is AggregationPerSeriesAligner.ALIGN_INTERPOLATE:
            return align_interpolate()
        if self is AggregationPerSeriesAligner.ALIGN_NEXT_OLDER:
            return align_next_older()
        if self is AggregationPerSeriesAligner.ALIGN_MIN:
            return align_min()
        if self is AggregationPerSeriesAligner.ALIGN_MAX:
            return align_max()
        if self is AggregationPerSeriesAligner.ALIGN_MEAN:
            return align_mean()
        if self is AggregationPerSeriesAligner.ALIGN_COUNT:
            return align_count()
        if self is AggregationPerSeriesAligner.ALIGN_SUM:
            return align_sum()
        if self is AggregationPerSeriesAligner.ALIGN_STDDEV:
            return align_stddev()
        if self is AggregationPerSeriesAligner.ALIGN_COUNT_TRUE:
            return align_count_true()
        if self is AggregationPerSeriesAligner.ALIGN_COUNT_FALSE:
            return align_count_false()
        if self is AggregationPerSeriesAligner.ALIGN_FRACTION_TRUE:
            return align_fraction_true()
        if self is AggregationPerSeriesAligner.ALIGN_PERCENTILE99:
            return align_percentile99()
        if self is AggregationPerSeriesAligner.ALIGN_PERCENTILE95:
            return align_percentile95()
        if self is AggregationPerSeriesAligner.ALIGN_PERCENTILE50:
            return align_percentile50()
        if self is AggregationPerSeriesAligner.ALIGN_PERCENTILE05:
            return align_percentile05()
        if self is AggregationPerSeriesAligner.ALIGN_PERCENT_CHANGE:
            return align_percent_change()
