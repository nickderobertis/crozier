

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferDiligenceStatus(enum.StrEnum):
    """
    Originator’s diligence status.
    """

    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    DENIED = "denied"

    def visit(
        self,
        under_review: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        denied: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferDiligenceStatus.UNDER_REVIEW:
            return under_review()
        if self is TransferDiligenceStatus.APPROVED:
            return approved()
        if self is TransferDiligenceStatus.DENIED:
            return denied()
