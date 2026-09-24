

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToNowTimeRangeConfigModelValue(enum.StrEnum):
    """
    Time range object
    """

    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"
    EPOCH = "EPOCH"
    LOGIN = "LOGIN"

    def visit(
        self,
        minute: typing.Callable[[], T_Result],
        hour: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
        epoch: typing.Callable[[], T_Result],
        login: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToNowTimeRangeConfigModelValue.MINUTE:
            return minute()
        if self is ToNowTimeRangeConfigModelValue.HOUR:
            return hour()
        if self is ToNowTimeRangeConfigModelValue.DAY:
            return day()
        if self is ToNowTimeRangeConfigModelValue.WEEK:
            return week()
        if self is ToNowTimeRangeConfigModelValue.MONTH:
            return month()
        if self is ToNowTimeRangeConfigModelValue.YEAR:
            return year()
        if self is ToNowTimeRangeConfigModelValue.EPOCH:
            return epoch()
        if self is ToNowTimeRangeConfigModelValue.LOGIN:
            return login()
