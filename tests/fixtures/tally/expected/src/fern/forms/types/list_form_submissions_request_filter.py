

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListFormSubmissionsRequestFilter(enum.StrEnum):
    ALL = "all"
    COMPLETED = "completed"
    PARTIAL = "partial"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListFormSubmissionsRequestFilter.ALL:
            return all_()
        if self is ListFormSubmissionsRequestFilter.COMPLETED:
            return completed()
        if self is ListFormSubmissionsRequestFilter.PARTIAL:
            return partial()
