

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBooksByReadListIdRequestReadStatusItem(enum.StrEnum):
    UNREAD = "UNREAD"
    READ = "READ"
    IN_PROGRESS = "IN_PROGRESS"

    def visit(
        self,
        unread: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBooksByReadListIdRequestReadStatusItem.UNREAD:
            return unread()
        if self is GetBooksByReadListIdRequestReadStatusItem.READ:
            return read()
        if self is GetBooksByReadListIdRequestReadStatusItem.IN_PROGRESS:
            return in_progress()
