

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SortingOptions(enum.StrEnum):
    """
    Sort records being returned.
    """

    CREATED_AT = "created_at"
    CREATED_AT = "-created_at"
    UPDATED_AT = "updated_at"
    UPDATED_AT = "-updated_at"

    def visit(self, created_at: typing.Callable[[], T_Result], updated_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is SortingOptions.CREATED_AT:
            return created_at()
        if self is SortingOptions.CREATED_AT:
            return created_at()
        if self is SortingOptions.UPDATED_AT:
            return updated_at()
        if self is SortingOptions.UPDATED_AT:
            return updated_at()
