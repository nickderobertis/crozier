

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerSortField(enum.StrEnum):
    """
    Specifies customer attributes as the sort key to customer profiles returned from a search.
    """

    DEFAULT = "DEFAULT"
    CREATED_AT = "CREATED_AT"

    def visit(self, default: typing.Callable[[], T_Result], created_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is CustomerSortField.DEFAULT:
            return default()
        if self is CustomerSortField.CREATED_AT:
            return created_at()
