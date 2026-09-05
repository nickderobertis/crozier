

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListUsersAccountsRequestReviewStatus(enum.StrEnum):
    PENDING = "PENDING"
    REVIEWED = "REVIEWED"

    def visit(self, pending: typing.Callable[[], T_Result], reviewed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListUsersAccountsRequestReviewStatus.PENDING:
            return pending()
        if self is ListUsersAccountsRequestReviewStatus.REVIEWED:
            return reviewed()
