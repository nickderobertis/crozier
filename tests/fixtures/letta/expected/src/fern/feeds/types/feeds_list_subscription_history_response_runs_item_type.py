

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedsListSubscriptionHistoryResponseRunsItemType(enum.StrEnum):
    SCHEDULED = "scheduled"
    MANUAL = "manual"
    BACKFILL = "backfill"

    def visit(
        self,
        scheduled: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
        backfill: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FeedsListSubscriptionHistoryResponseRunsItemType.SCHEDULED:
            return scheduled()
        if self is FeedsListSubscriptionHistoryResponseRunsItemType.MANUAL:
            return manual()
        if self is FeedsListSubscriptionHistoryResponseRunsItemType.BACKFILL:
            return backfill()
