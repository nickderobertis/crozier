

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryReviewProcessCompletionStatus(enum.StrEnum):
    """
    State of the Entry at the end of the Review Process
    """

    APPROVED = "APPROVED"
    COMPLETED = "COMPLETED"
    ACCEPTED = "ACCEPTED"
    REVIEWED = "REVIEWED"
    WITNESSED = "WITNESSED"
    SELF_REVIEWED = "SELF_REVIEWED"

    def visit(
        self,
        approved: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        accepted: typing.Callable[[], T_Result],
        reviewed: typing.Callable[[], T_Result],
        witnessed: typing.Callable[[], T_Result],
        self_reviewed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntryReviewProcessCompletionStatus.APPROVED:
            return approved()
        if self is EntryReviewProcessCompletionStatus.COMPLETED:
            return completed()
        if self is EntryReviewProcessCompletionStatus.ACCEPTED:
            return accepted()
        if self is EntryReviewProcessCompletionStatus.REVIEWED:
            return reviewed()
        if self is EntryReviewProcessCompletionStatus.WITNESSED:
            return witnessed()
        if self is EntryReviewProcessCompletionStatus.SELF_REVIEWED:
            return self_reviewed()
