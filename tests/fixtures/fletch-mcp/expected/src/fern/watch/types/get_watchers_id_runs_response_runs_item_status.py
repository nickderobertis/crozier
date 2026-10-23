

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWatchersIdRunsResponseRunsItemStatus(enum.StrEnum):
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
        if self is GetWatchersIdRunsResponseRunsItemStatus.PENDING:
            return pending()
        if self is GetWatchersIdRunsResponseRunsItemStatus.SENT:
            return sent()
        if self is GetWatchersIdRunsResponseRunsItemStatus.FAILED:
            return failed()
        if self is GetWatchersIdRunsResponseRunsItemStatus.RETRACTED:
            return retracted()
