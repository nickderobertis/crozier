

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListFormRecordsRequestSort(enum.StrEnum):
    NEWEST = "newest"
    OLDEST = "oldest"
    PRIORITY = "priority"
    UPDATED = "updated"

    def visit(
        self,
        newest: typing.Callable[[], T_Result],
        oldest: typing.Callable[[], T_Result],
        priority: typing.Callable[[], T_Result],
        updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListFormRecordsRequestSort.NEWEST:
            return newest()
        if self is ListFormRecordsRequestSort.OLDEST:
            return oldest()
        if self is ListFormRecordsRequestSort.PRIORITY:
            return priority()
        if self is ListFormRecordsRequestSort.UPDATED:
            return updated()
