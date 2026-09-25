

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPricebooksRequestSortField(enum.StrEnum):
    CREATED_AT = "createdAt"

    def visit(self, created_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetPricebooksRequestSortField.CREATED_AT:
            return created_at()
