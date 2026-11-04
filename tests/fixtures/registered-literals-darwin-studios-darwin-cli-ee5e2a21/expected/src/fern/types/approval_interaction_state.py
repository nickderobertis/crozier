

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApprovalInteractionState(enum.StrEnum):
    REQUIRED = "required"
    PENDING = "pending"
    COMPLETE = "complete"
    DECLINED = "declined"
    EXPIRED = "expired"
    FAILED = "failed"

    def visit(
        self,
        required: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApprovalInteractionState.REQUIRED:
            return required()
        if self is ApprovalInteractionState.PENDING:
            return pending()
        if self is ApprovalInteractionState.COMPLETE:
            return complete()
        if self is ApprovalInteractionState.DECLINED:
            return declined()
        if self is ApprovalInteractionState.EXPIRED:
            return expired()
        if self is ApprovalInteractionState.FAILED:
            return failed()
