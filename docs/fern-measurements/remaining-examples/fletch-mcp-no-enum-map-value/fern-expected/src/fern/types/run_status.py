

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunStatus(enum.StrEnum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"
    RETRACTED = "retracted"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        sent: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        retracted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunStatus.PENDING:
            return pending()
        if self is RunStatus.SENT:
            return sent()
        if self is RunStatus.FAILED:
            return failed()
        if self is RunStatus.RETRACTED:
            return retracted()
