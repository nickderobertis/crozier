

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentRunReviewStatus(enum.StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REVISION_REQUIRED = "revision_required"
    REJECTED = "rejected"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        revision_required: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentRunReviewStatus.PENDING:
            return pending()
        if self is AgentRunReviewStatus.APPROVED:
            return approved()
        if self is AgentRunReviewStatus.REVISION_REQUIRED:
            return revision_required()
        if self is AgentRunReviewStatus.REJECTED:
            return rejected()
