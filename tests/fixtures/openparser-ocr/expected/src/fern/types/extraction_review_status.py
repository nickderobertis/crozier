

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionReviewStatus(enum.StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExtractionReviewStatus.PENDING:
            return pending()
        if self is ExtractionReviewStatus.APPROVED:
            return approved()
        if self is ExtractionReviewStatus.REJECTED:
            return rejected()
