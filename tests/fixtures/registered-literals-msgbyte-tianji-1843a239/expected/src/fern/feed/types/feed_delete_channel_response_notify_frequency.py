

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedDeleteChannelResponseNotifyFrequency(enum.StrEnum):
    NONE = "none"
    EVENT = "event"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        event: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FeedDeleteChannelResponseNotifyFrequency.NONE:
            return none()
        if self is FeedDeleteChannelResponseNotifyFrequency.EVENT:
            return event()
        if self is FeedDeleteChannelResponseNotifyFrequency.DAY:
            return day()
        if self is FeedDeleteChannelResponseNotifyFrequency.WEEK:
            return week()
        if self is FeedDeleteChannelResponseNotifyFrequency.MONTH:
            return month()
