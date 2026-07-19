

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedsListSubscriptionHistoryResponseRunsItemStatus(enum.StrEnum):
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"
    TIMED_OUT = "timed_out"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        timed_out: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FeedsListSubscriptionHistoryResponseRunsItemStatus.RUNNING:
            return running()
        if self is FeedsListSubscriptionHistoryResponseRunsItemStatus.COMPLETED:
            return completed()
        if self is FeedsListSubscriptionHistoryResponseRunsItemStatus.FAILED:
            return failed()
        if self is FeedsListSubscriptionHistoryResponseRunsItemStatus.CANCELED:
            return canceled()
        if self is FeedsListSubscriptionHistoryResponseRunsItemStatus.TIMED_OUT:
            return timed_out()
