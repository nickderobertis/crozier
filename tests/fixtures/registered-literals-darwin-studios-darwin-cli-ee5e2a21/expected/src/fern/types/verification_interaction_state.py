

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VerificationInteractionState(enum.StrEnum):
    REQUIRED = "required"
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    INCONCLUSIVE = "inconclusive"
    EXPIRED = "expired"

    def visit(
        self,
        required: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        inconclusive: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VerificationInteractionState.REQUIRED:
            return required()
        if self is VerificationInteractionState.PENDING:
            return pending()
        if self is VerificationInteractionState.SUCCEEDED:
            return succeeded()
        if self is VerificationInteractionState.FAILED:
            return failed()
        if self is VerificationInteractionState.INCONCLUSIVE:
            return inconclusive()
        if self is VerificationInteractionState.EXPIRED:
            return expired()
