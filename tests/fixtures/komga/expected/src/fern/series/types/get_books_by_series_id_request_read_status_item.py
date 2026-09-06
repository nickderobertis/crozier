

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBooksBySeriesIdRequestReadStatusItem(enum.StrEnum):
    UNREAD = "UNREAD"
    READ = "READ"
    IN_PROGRESS = "IN_PROGRESS"

    def visit(
        self,
        unread: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBooksBySeriesIdRequestReadStatusItem.UNREAD:
            return unread()
        if self is GetBooksBySeriesIdRequestReadStatusItem.READ:
            return read()
        if self is GetBooksBySeriesIdRequestReadStatusItem.IN_PROGRESS:
            return in_progress()
