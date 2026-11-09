

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WatchlistScreeningHitStatus(enum.StrEnum):
    """
    The current state of review. All watchlist screening hits begin in a `pending_review` state but can be changed by creating a review. When a hit is in the `pending_review` state, it will always show the latest version of the watchlist data Plaid has available and be compared against the latest customer information saved in the watchlist screening. Once a hit has been marked as `confirmed` or `dismissed` it will no longer be updated so that the state is as it was when the review was first conducted.
    """

    CONFIRMED = "confirmed"
    PENDING_REVIEW = "pending_review"
    DISMISSED = "dismissed"

    def visit(
        self,
        confirmed: typing.Callable[[], T_Result],
        pending_review: typing.Callable[[], T_Result],
        dismissed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WatchlistScreeningHitStatus.CONFIRMED:
            return confirmed()
        if self is WatchlistScreeningHitStatus.PENDING_REVIEW:
            return pending_review()
        if self is WatchlistScreeningHitStatus.DISMISSED:
            return dismissed()
