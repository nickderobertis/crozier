

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTasksRequestSort(enum.StrEnum):
    UPDATED_AT = "updated_at"
    CREATED_AT = "created_at"
    FROM = "from"
    TO = "to"

    def visit(
        self,
        updated_at: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        from_: typing.Callable[[], T_Result],
        to: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListTasksRequestSort.UPDATED_AT:
            return updated_at()
        if self is ListTasksRequestSort.CREATED_AT:
            return created_at()
        if self is ListTasksRequestSort.FROM:
            return from_()
        if self is ListTasksRequestSort.TO:
            return to()
