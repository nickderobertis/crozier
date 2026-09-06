

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSeriesByCollectionIdRequestReadStatusItem(enum.StrEnum):
    UNREAD = "UNREAD"
    READ = "READ"
    IN_PROGRESS = "IN_PROGRESS"

    def visit(
        self,
        unread: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSeriesByCollectionIdRequestReadStatusItem.UNREAD:
            return unread()
        if self is GetSeriesByCollectionIdRequestReadStatusItem.READ:
            return read()
        if self is GetSeriesByCollectionIdRequestReadStatusItem.IN_PROGRESS:
            return in_progress()
