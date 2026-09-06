

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListCommentRepliesCommentsRequestSortOrder(enum.StrEnum):
    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListCommentRepliesCommentsRequestSortOrder.ASC:
            return asc()
        if self is ListCommentRepliesCommentsRequestSortOrder.DESC:
            return desc()
