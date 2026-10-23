

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetContactAttributeKeysRequestSortBy(enum.StrEnum):
    """
    Sort by field
    """

    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"

    def visit(self, created_at: typing.Callable[[], T_Result], updated_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetContactAttributeKeysRequestSortBy.CREATED_AT:
            return created_at()
        if self is GetContactAttributeKeysRequestSortBy.UPDATED_AT:
            return updated_at()
