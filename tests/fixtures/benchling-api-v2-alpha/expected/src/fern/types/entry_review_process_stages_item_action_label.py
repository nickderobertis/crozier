

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryReviewProcessStagesItemActionLabel(enum.StrEnum):
    """
    Action reviewer is doing during the review
    """

    APPROVE = "APPROVE"
    COMPLETE = "COMPLETE"
    ACCEPT = "ACCEPT"
    REVIEW = "REVIEW"
    WITNESS = "WITNESS"
    SELF_REVIEW = "SELF_REVIEW"

    def visit(
        self,
        approve: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        accept: typing.Callable[[], T_Result],
        review: typing.Callable[[], T_Result],
        witness: typing.Callable[[], T_Result],
        self_review: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntryReviewProcessStagesItemActionLabel.APPROVE:
            return approve()
        if self is EntryReviewProcessStagesItemActionLabel.COMPLETE:
            return complete()
        if self is EntryReviewProcessStagesItemActionLabel.ACCEPT:
            return accept()
        if self is EntryReviewProcessStagesItemActionLabel.REVIEW:
            return review()
        if self is EntryReviewProcessStagesItemActionLabel.WITNESS:
            return witness()
        if self is EntryReviewProcessStagesItemActionLabel.SELF_REVIEW:
            return self_review()
