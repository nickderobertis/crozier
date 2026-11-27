

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryReviewRecordStatus(enum.StrEnum):
    """
    Review Status of the entry
    """

    ACCEPTED = "ACCEPTED"
    NEEDS_REVIEW = "NEEDS_REVIEW"
    REJECTED = "REJECTED"
    RETRACTED = "RETRACTED"
    ACCEPTANCE_SNAPSHOT_IN_PROGRESS = "ACCEPTANCE_SNAPSHOT_IN_PROGRESS"
    REVIEW_SNAPSHOT_IN_PROGRESS = "REVIEW_SNAPSHOT_IN_PROGRESS"
    IN_PROGRESS = "IN_PROGRESS"
    ACTION_REQUIRED = "ACTION_REQUIRED"

    def visit(
        self,
        accepted: typing.Callable[[], T_Result],
        needs_review: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        retracted: typing.Callable[[], T_Result],
        acceptance_snapshot_in_progress: typing.Callable[[], T_Result],
        review_snapshot_in_progress: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        action_required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntryReviewRecordStatus.ACCEPTED:
            return accepted()
        if self is EntryReviewRecordStatus.NEEDS_REVIEW:
            return needs_review()
        if self is EntryReviewRecordStatus.REJECTED:
            return rejected()
        if self is EntryReviewRecordStatus.RETRACTED:
            return retracted()
        if self is EntryReviewRecordStatus.ACCEPTANCE_SNAPSHOT_IN_PROGRESS:
            return acceptance_snapshot_in_progress()
        if self is EntryReviewRecordStatus.REVIEW_SNAPSHOT_IN_PROGRESS:
            return review_snapshot_in_progress()
        if self is EntryReviewRecordStatus.IN_PROGRESS:
            return in_progress()
        if self is EntryReviewRecordStatus.ACTION_REQUIRED:
            return action_required()
