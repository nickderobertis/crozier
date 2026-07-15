

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BillsSortBy(str, enum.Enum):
    """
    The field on which to sort the Bills
    """

    UPDATED_AT = "updated_at"

    def visit(self, updated_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is BillsSortBy.UPDATED_AT:
            return updated_at()
