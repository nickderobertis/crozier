

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryReviewProcessStagesItemReviewersItemStatus(enum.StrEnum):
    """
    Status of the Reviewer
    """

    BLOCKED = "BLOCKED"
    PENDING = "PENDING"
    FINISHED = "FINISHED"
    REJECTED = "REJECTED"

    def visit(
        self,
        blocked: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        finished: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntryReviewProcessStagesItemReviewersItemStatus.BLOCKED:
            return blocked()
        if self is EntryReviewProcessStagesItemReviewersItemStatus.PENDING:
            return pending()
        if self is EntryReviewProcessStagesItemReviewersItemStatus.FINISHED:
            return finished()
        if self is EntryReviewProcessStagesItemReviewersItemStatus.REJECTED:
            return rejected()
