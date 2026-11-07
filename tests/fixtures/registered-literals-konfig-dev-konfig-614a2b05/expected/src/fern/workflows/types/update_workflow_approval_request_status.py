

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateWorkflowApprovalRequestStatus(enum.StrEnum):
    """
    The new approval status.
    """

    APPROVED = "approved"
    PENDING = "pending"

    def visit(self, approved: typing.Callable[[], T_Result], pending: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateWorkflowApprovalRequestStatus.APPROVED:
            return approved()
        if self is UpdateWorkflowApprovalRequestStatus.PENDING:
            return pending()
