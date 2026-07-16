

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CustomerSortField(str, enum.Enum):
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
