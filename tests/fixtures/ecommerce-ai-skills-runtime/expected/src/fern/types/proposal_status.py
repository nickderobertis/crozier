

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProposalStatus(enum.StrEnum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    APPROVED = "approved"
    REJECTED = "rejected"
    REVISION_REQUIRED = "revision_required"
    EXECUTING = "executing"
    EXECUTED = "executed"
    FAILED = "failed"
    EXPIRED = "expired"
    BLOCKED = "blocked"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        submitted: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        revision_required: typing.Callable[[], T_Result],
        executing: typing.Callable[[], T_Result],
        executed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProposalStatus.DRAFT:
            return draft()
        if self is ProposalStatus.SUBMITTED:
            return submitted()
        if self is ProposalStatus.APPROVED:
            return approved()
        if self is ProposalStatus.REJECTED:
            return rejected()
        if self is ProposalStatus.REVISION_REQUIRED:
            return revision_required()
        if self is ProposalStatus.EXECUTING:
            return executing()
        if self is ProposalStatus.EXECUTED:
            return executed()
        if self is ProposalStatus.FAILED:
            return failed()
        if self is ProposalStatus.EXPIRED:
            return expired()
        if self is ProposalStatus.BLOCKED:
            return blocked()
