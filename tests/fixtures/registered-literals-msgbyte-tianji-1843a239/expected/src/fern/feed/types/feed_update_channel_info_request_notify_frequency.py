

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedUpdateChannelInfoRequestNotifyFrequency(enum.StrEnum):
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
        if self is FeedUpdateChannelInfoRequestNotifyFrequency.NONE:
            return none()
        if self is FeedUpdateChannelInfoRequestNotifyFrequency.EVENT:
            return event()
        if self is FeedUpdateChannelInfoRequestNotifyFrequency.DAY:
            return day()
        if self is FeedUpdateChannelInfoRequestNotifyFrequency.WEEK:
            return week()
        if self is FeedUpdateChannelInfoRequestNotifyFrequency.MONTH:
            return month()
