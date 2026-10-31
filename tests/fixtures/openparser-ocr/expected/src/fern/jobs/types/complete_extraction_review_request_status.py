

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CompleteExtractionReviewRequestStatus(enum.StrEnum):
    APPROVED = "approved"
    REJECTED = "rejected"

    def visit(self, approved: typing.Callable[[], T_Result], rejected: typing.Callable[[], T_Result]) -> T_Result:
        if self is CompleteExtractionReviewRequestStatus.APPROVED:
            return approved()
        if self is CompleteExtractionReviewRequestStatus.REJECTED:
            return rejected()
