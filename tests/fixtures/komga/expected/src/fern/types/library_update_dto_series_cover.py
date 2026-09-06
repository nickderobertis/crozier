

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LibraryUpdateDtoSeriesCover(enum.StrEnum):
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
        if self is LibraryUpdateDtoSeriesCover.FIRST:
            return first()
        if self is LibraryUpdateDtoSeriesCover.FIRST_UNREAD_OR_FIRST:
            return first_unread_or_first()
        if self is LibraryUpdateDtoSeriesCover.FIRST_UNREAD_OR_LAST:
            return first_unread_or_last()
        if self is LibraryUpdateDtoSeriesCover.LAST:
            return last()
