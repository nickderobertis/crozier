

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ShiftSortField(enum.StrEnum):
    """
    Enumerates the `Shift` fields to sort on.
    """

    START_AT = "START_AT"
    END_AT = "END_AT"
    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"

    def visit(
        self,
        start_at: typing.Callable[[], T_Result],
        end_at: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ShiftSortField.START_AT:
            return start_at()
        if self is ShiftSortField.END_AT:
            return end_at()
        if self is ShiftSortField.CREATED_AT:
            return created_at()
        if self is ShiftSortField.UPDATED_AT:
            return updated_at()
