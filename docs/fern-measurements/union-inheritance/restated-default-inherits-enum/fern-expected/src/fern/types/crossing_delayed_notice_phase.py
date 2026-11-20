

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CrossingDelayedNoticePhase(enum.StrEnum):
    """
    Where the crossing stands.
    """

    SCHEDULED = "scheduled"
    BOARDING = "boarding"
    DELAYED = "delayed"
    SAILED = "sailed"
    CANCELLED = "cancelled"

    def visit(
        self,
        scheduled: typing.Callable[[], T_Result],
        boarding: typing.Callable[[], T_Result],
        delayed: typing.Callable[[], T_Result],
        sailed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CrossingDelayedNoticePhase.SCHEDULED:
            return scheduled()
        if self is CrossingDelayedNoticePhase.BOARDING:
            return boarding()
        if self is CrossingDelayedNoticePhase.DELAYED:
            return delayed()
        if self is CrossingDelayedNoticePhase.SAILED:
            return sailed()
        if self is CrossingDelayedNoticePhase.CANCELLED:
            return cancelled()
