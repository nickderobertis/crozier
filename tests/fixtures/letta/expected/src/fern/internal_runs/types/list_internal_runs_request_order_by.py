

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListInternalRunsRequestOrderBy(enum.StrEnum):
    """
    Field to sort by
    """

    CREATED_AT = "created_at"
    DURATION = "duration"

    def visit(self, created_at: typing.Callable[[], T_Result], duration: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListInternalRunsRequestOrderBy.CREATED_AT:
            return created_at()
        if self is ListInternalRunsRequestOrderBy.DURATION:
            return duration()
