

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedCreateChannelRequestNotifyFrequency(enum.StrEnum):
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
        if self is FeedCreateChannelRequestNotifyFrequency.NONE:
            return none()
        if self is FeedCreateChannelRequestNotifyFrequency.EVENT:
            return event()
        if self is FeedCreateChannelRequestNotifyFrequency.DAY:
            return day()
        if self is FeedCreateChannelRequestNotifyFrequency.WEEK:
            return week()
        if self is FeedCreateChannelRequestNotifyFrequency.MONTH:
            return month()
