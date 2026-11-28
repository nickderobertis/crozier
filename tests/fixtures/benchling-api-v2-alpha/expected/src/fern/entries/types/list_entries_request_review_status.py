

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListEntriesRequestReviewStatus(enum.StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    NEEDS_REVIEW = "NEEDS_REVIEW"
    RETRACTED = "RETRACTED"

    def visit(
        self,
        in_progress: typing.Callable[[], T_Result],
        accepted: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        needs_review: typing.Callable[[], T_Result],
        retracted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListEntriesRequestReviewStatus.IN_PROGRESS:
            return in_progress()
        if self is ListEntriesRequestReviewStatus.ACCEPTED:
            return accepted()
        if self is ListEntriesRequestReviewStatus.REJECTED:
            return rejected()
        if self is ListEntriesRequestReviewStatus.NEEDS_REVIEW:
            return needs_review()
        if self is ListEntriesRequestReviewStatus.RETRACTED:
            return retracted()
