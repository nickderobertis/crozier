

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTimeEntriesRequestSort(enum.StrEnum):
    DAY = "day"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListTimeEntriesRequestSort.DAY:
            return day()
        if self is ListTimeEntriesRequestSort.CREATED_AT:
            return created_at()
        if self is ListTimeEntriesRequestSort.UPDATED_AT:
            return updated_at()
