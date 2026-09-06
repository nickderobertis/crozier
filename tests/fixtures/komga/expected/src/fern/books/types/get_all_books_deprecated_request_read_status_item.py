

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAllBooksDeprecatedRequestReadStatusItem(enum.StrEnum):
    UNREAD = "UNREAD"
    READ = "READ"
    IN_PROGRESS = "IN_PROGRESS"

    def visit(
        self,
        unread: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAllBooksDeprecatedRequestReadStatusItem.UNREAD:
            return unread()
        if self is GetAllBooksDeprecatedRequestReadStatusItem.READ:
            return read()
        if self is GetAllBooksDeprecatedRequestReadStatusItem.IN_PROGRESS:
            return in_progress()
