

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedChannelInfoResponseNotifyFrequency(enum.StrEnum):
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
        if self is FeedChannelInfoResponseNotifyFrequency.NONE:
            return none()
        if self is FeedChannelInfoResponseNotifyFrequency.EVENT:
            return event()
        if self is FeedChannelInfoResponseNotifyFrequency.DAY:
            return day()
        if self is FeedChannelInfoResponseNotifyFrequency.WEEK:
            return week()
        if self is FeedChannelInfoResponseNotifyFrequency.MONTH:
            return month()
