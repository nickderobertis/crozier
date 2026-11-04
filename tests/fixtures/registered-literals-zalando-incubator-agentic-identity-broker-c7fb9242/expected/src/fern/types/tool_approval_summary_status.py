

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolApprovalSummaryStatus(enum.StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    DENIED = "denied"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        denied: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolApprovalSummaryStatus.PENDING:
            return pending()
        if self is ToolApprovalSummaryStatus.APPROVED:
            return approved()
        if self is ToolApprovalSummaryStatus.DENIED:
            return denied()
