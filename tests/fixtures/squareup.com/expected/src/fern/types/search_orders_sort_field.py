

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchOrdersSortField(enum.StrEnum):
    """
    Specifies which timestamp to use to sort `SearchOrder` results.
    """

    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"
    CLOSED_AT = "CLOSED_AT"

    def visit(
        self,
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        closed_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchOrdersSortField.CREATED_AT:
            return created_at()
        if self is SearchOrdersSortField.UPDATED_AT:
            return updated_at()
        if self is SearchOrdersSortField.CLOSED_AT:
            return closed_at()
