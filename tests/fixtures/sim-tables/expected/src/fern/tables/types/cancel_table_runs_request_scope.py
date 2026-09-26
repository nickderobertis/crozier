

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CancelTableRunsRequestScope(enum.StrEnum):
    """
    Whether to cancel across the table or one row.
    """

    ALL = "all"
    ROW = "row"

    def visit(self, all_: typing.Callable[[], T_Result], row: typing.Callable[[], T_Result]) -> T_Result:
        if self is CancelTableRunsRequestScope.ALL:
            return all_()
        if self is CancelTableRunsRequestScope.ROW:
            return row()
