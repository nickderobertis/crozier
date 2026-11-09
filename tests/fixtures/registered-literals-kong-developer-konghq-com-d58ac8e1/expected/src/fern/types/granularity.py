

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Granularity(enum.StrEnum):
    """
    Force time grouping into buckets of the specified duration.  Only has an effect if "time" is in the "dimensions" list.

    The granularity of the result may be coarser than requested.  The finest allowed granularity depends on the query's time range: data farther in the past may have coarser granularity.  The exact result granularity will be reported in the response `meta.granularity_ms` field.

    If granularity is not specified and "time" is in the dimensions list, a default will be chosen based on the time range requested.

    Different relative times support different granularities:
      - 15m => tenSecondly, thirtySecondly, minutely
      - 1h  => tenSecondly, thirtySecondly, minutely, fiveMinutely, tenMinutely
      - 6h  => thirtySecondly, minutely, fiveMinutely, tenMinutely, thirtyMinutely, hourly
      - 12h => minutely, fiveMinutely, tenMinutely, thirtyMinutely, hourly
      - 24h => fiveMinutely, tenMinutely, thirtyMinutely, hourly
      - 7d  => thirtyMinutely, hourly, twoHourly, twelveHourly, daily
      - 30d => hourly, twoHourly, twelveHourly, daily, weekly

    For special time ranges:
      - current_week, previous_week   => thirtyMinutely, hourly, twoHourly, twelveHourly, daily
      - current_month, previous_month => hourly, twoHourly, twelveHourly, daily, weekly

    For absolute time ranges, daily will be used.
    """

    TEN_SECONDLY = "tenSecondly"
    THIRTY_SECONDLY = "thirtySecondly"
    MINUTELY = "minutely"
    FIVE_MINUTELY = "fiveMinutely"
    TEN_MINUTELY = "tenMinutely"
    THIRTY_MINUTELY = "thirtyMinutely"
    HOURLY = "hourly"
    TWO_HOURLY = "twoHourly"
    TWELVE_HOURLY = "twelveHourly"
    DAILY = "daily"
    WEEKLY = "weekly"

    def visit(
        self,
        ten_secondly: typing.Callable[[], T_Result],
        thirty_secondly: typing.Callable[[], T_Result],
        minutely: typing.Callable[[], T_Result],
        five_minutely: typing.Callable[[], T_Result],
        ten_minutely: typing.Callable[[], T_Result],
        thirty_minutely: typing.Callable[[], T_Result],
        hourly: typing.Callable[[], T_Result],
        two_hourly: typing.Callable[[], T_Result],
        twelve_hourly: typing.Callable[[], T_Result],
        daily: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Granularity.TEN_SECONDLY:
            return ten_secondly()
        if self is Granularity.THIRTY_SECONDLY:
            return thirty_secondly()
        if self is Granularity.MINUTELY:
            return minutely()
        if self is Granularity.FIVE_MINUTELY:
            return five_minutely()
        if self is Granularity.TEN_MINUTELY:
            return ten_minutely()
        if self is Granularity.THIRTY_MINUTELY:
            return thirty_minutely()
        if self is Granularity.HOURLY:
            return hourly()
        if self is Granularity.TWO_HOURLY:
            return two_hourly()
        if self is Granularity.TWELVE_HOURLY:
            return twelve_hourly()
        if self is Granularity.DAILY:
            return daily()
        if self is Granularity.WEEKLY:
            return weekly()
