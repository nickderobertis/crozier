

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewReplyStatus(enum.StrEnum):
    PENDING = "pending"
    REPLIED = "replied"
    ERROR = "error"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        replied: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewReplyStatus.PENDING:
            return pending()
        if self is ReviewReplyStatus.REPLIED:
            return replied()
        if self is ReviewReplyStatus.ERROR:
            return error()
