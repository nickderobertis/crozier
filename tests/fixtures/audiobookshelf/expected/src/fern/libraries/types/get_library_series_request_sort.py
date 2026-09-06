

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetLibrarySeriesRequestSort(enum.StrEnum):
    NAME = "name"
    NUM_BOOKS = "numBooks"
    TOTAL_DURATION = "totalDuration"
    ADDED_AT = "addedAt"
    LAST_BOOK_ADDED = "lastBookAdded"
    LAST_BOOK_UPDATED = "lastBookUpdated"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        num_books: typing.Callable[[], T_Result],
        total_duration: typing.Callable[[], T_Result],
        added_at: typing.Callable[[], T_Result],
        last_book_added: typing.Callable[[], T_Result],
        last_book_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetLibrarySeriesRequestSort.NAME:
            return name()
        if self is GetLibrarySeriesRequestSort.NUM_BOOKS:
            return num_books()
        if self is GetLibrarySeriesRequestSort.TOTAL_DURATION:
            return total_duration()
        if self is GetLibrarySeriesRequestSort.ADDED_AT:
            return added_at()
        if self is GetLibrarySeriesRequestSort.LAST_BOOK_ADDED:
            return last_book_added()
        if self is GetLibrarySeriesRequestSort.LAST_BOOK_UPDATED:
            return last_book_updated()
