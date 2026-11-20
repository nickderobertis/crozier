

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CrossingSailedNoticePhase(enum.StrEnum):
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
        if self is CrossingSailedNoticePhase.SCHEDULED:
            return scheduled()
        if self is CrossingSailedNoticePhase.BOARDING:
            return boarding()
        if self is CrossingSailedNoticePhase.DELAYED:
            return delayed()
        if self is CrossingSailedNoticePhase.SAILED:
            return sailed()
        if self is CrossingSailedNoticePhase.CANCELLED:
            return cancelled()
