

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WatchlistScreeningStatus(enum.StrEnum):
    """
    A status enum indicating whether a screening is still pending review, has been rejected, or has been cleared.
    """

    REJECTED = "rejected"
    PENDING_REVIEW = "pending_review"
    CLEARED = "cleared"

    def visit(
        self,
        rejected: typing.Callable[[], T_Result],
        pending_review: typing.Callable[[], T_Result],
        cleared: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WatchlistScreeningStatus.REJECTED:
            return rejected()
        if self is WatchlistScreeningStatus.PENDING_REVIEW:
            return pending_review()
        if self is WatchlistScreeningStatus.CLEARED:
            return cleared()
