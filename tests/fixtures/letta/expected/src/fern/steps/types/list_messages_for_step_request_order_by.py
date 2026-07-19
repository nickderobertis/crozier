

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListMessagesForStepRequestOrderBy(enum.StrEnum):
    """
    Sort by field
    """

    CREATED_AT = "created_at"

    def visit(self, created_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListMessagesForStepRequestOrderBy.CREATED_AT:
            return created_at()
