

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTeamsRequestSortBy(enum.StrEnum):
    """
    Sort by field
    """

    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"

    def visit(self, created_at: typing.Callable[[], T_Result], updated_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTeamsRequestSortBy.CREATED_AT:
            return created_at()
        if self is GetTeamsRequestSortBy.UPDATED_AT:
            return updated_at()
