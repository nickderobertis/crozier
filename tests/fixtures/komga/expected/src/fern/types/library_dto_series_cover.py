

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LibraryDtoSeriesCover(enum.StrEnum):
    FIRST = "FIRST"
    FIRST_UNREAD_OR_FIRST = "FIRST_UNREAD_OR_FIRST"
    FIRST_UNREAD_OR_LAST = "FIRST_UNREAD_OR_LAST"
    LAST = "LAST"

    def visit(
        self,
        first: typing.Callable[[], T_Result],
        first_unread_or_first: typing.Callable[[], T_Result],
        first_unread_or_last: typing.Callable[[], T_Result],
        last: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LibraryDtoSeriesCover.FIRST:
            return first()
        if self is LibraryDtoSeriesCover.FIRST_UNREAD_OR_FIRST:
            return first_unread_or_first()
        if self is LibraryDtoSeriesCover.FIRST_UNREAD_OR_LAST:
            return first_unread_or_last()
        if self is LibraryDtoSeriesCover.LAST:
            return last()
