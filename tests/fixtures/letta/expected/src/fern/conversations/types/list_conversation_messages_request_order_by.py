

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListConversationMessagesRequestOrderBy(enum.StrEnum):
    """
    Field to sort by
    """

    CREATED_AT = "created_at"

    def visit(self, created_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListConversationMessagesRequestOrderBy.CREATED_AT:
            return created_at()
