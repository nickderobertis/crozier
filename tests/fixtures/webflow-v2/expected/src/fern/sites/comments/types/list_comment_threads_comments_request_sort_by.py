

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListCommentThreadsCommentsRequestSortBy(enum.StrEnum):
    CREATED_ON = "createdOn"
    LAST_UPDATED = "lastUpdated"

    def visit(self, created_on: typing.Callable[[], T_Result], last_updated: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListCommentThreadsCommentsRequestSortBy.CREATED_ON:
            return created_on()
        if self is ListCommentThreadsCommentsRequestSortBy.LAST_UPDATED:
            return last_updated()
